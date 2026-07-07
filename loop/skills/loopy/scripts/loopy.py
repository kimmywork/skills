#!/usr/bin/env python3
"""
loopy.py — Workflow scheduling and dispatch script.

Part of the Loop Creation Kit (@loop/ plugin).

Determines which workflows are due (by schedule or trigger),
detects concurrent runs via state file status, and outputs
a structured JSON dispatch list for the agent to execute.

Dependencies: PyYAML (stdlib), croniter (pip)
"""

import argparse
import datetime
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

import croniter
import yaml


# --- Constants ---

WORKFLOWS_DIR = "workflows"
STATE_DIR = os.path.join(WORKFLOWS_DIR, ".state")
DISPATCH_DIR = os.path.join(STATE_DIR, "dispatch")
TRIGGER_TIMEOUT_DEFAULT = 30  # seconds
TRIGGER_SHELL = "/bin/sh"
TRIGGER_TIMEOUT_ENV_VAR = "LOOPY_TRIGGER_TIMEOUT"


# --- Helpers ---

def project_root():
    """Return the intended project root. Script runs from project root."""
    return os.getcwd()


def parse_frontmatter(filepath):
    """Parse YAML front-matter and body from a markdown file.

    Returns (frontmatter_dict, body_text) or raises on error.
    """
    with open(filepath, "r") as f:
        content = f.read()

    # Match content between first two `---` markers
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)
    if not m:
        raise ValueError(f"Missing or malformed front-matter: {filepath}")

    fm = yaml.safe_load(m.group(1))
    if not isinstance(fm, dict):
        raise ValueError(f"Front-matter is not a dict: {filepath}")

    body = m.group(2).strip()
    return fm, body


def slugify(name):
    """Convert a workflow name to a filesystem-safe slug."""
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9-]", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    return slug[:64]


def today_prefix():
    return datetime.date.today().isoformat()  # YYYY-MM-DD


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def read_all_workflows():
    """Return list of (filepath, fm, body) for all valid workflow files."""
    pattern = os.path.join(WORKFLOWS_DIR, "*.md")
    files = sorted(glob.glob(pattern))
    results = []
    for fp in files:
        try:
            fm, body = parse_frontmatter(fp)
            results.append((fp, fm, body))
        except (ValueError, yaml.YAMLError, OSError) as e:
            results.append((fp, {"_error": str(e)}, ""))
    return results


def get_state_dir(name):
    return os.path.join(STATE_DIR, name)


def get_latest_state_file(name):
    """Return (filepath, data) for the most recent state file, or (None, None)."""
    sdir = get_state_dir(name)
    if not os.path.isdir(sdir):
        return None, None

    # List files matching YYYY-MM-DD-NNN.json, take latest by name
    files = [f for f in os.listdir(sdir) if re.match(r"\d{4}-\d{2}-\d{2}-\d{3}\.json$", f)]
    if not files:
        return None, None

    latest = sorted(files)[-1]
    path = os.path.join(sdir, latest)
    try:
        with open(path) as f:
            data = json.load(f)
        return path, data
    except (json.JSONDecodeError, IOError):
        return path, None


def next_nnn(name):
    """Compute next NNN sequence number for today."""
    sdir = get_state_dir(name)
    prefix = today_prefix() + "-"
    if not os.path.isdir(sdir):
        return 1

    max_n = 0
    for f in os.listdir(sdir):
        if f.startswith(prefix) and f.endswith(".json"):
            parts = f[len(prefix):-5]  # strip prefix and .json
            if parts.isdigit():
                max_n = max(max_n, int(parts))
    return max_n + 1


def create_state_file(name, trigger_output_file=None):
    """Create a state file with status 'scheduled' for a due workflow.

    Returns path to the created state file.
    """
    sdir = get_state_dir(name)
    os.makedirs(sdir, exist_ok=True)

    nnn = next_nnn(name)
    run_id = f"{today_prefix()}-{nnn:03d}"
    filename = f"{run_id}.json"
    path = os.path.join(sdir, filename)

    state = {
        "workflow": name,
        "run_id": run_id,
        "started_at": now_iso(),
        "completed_at": None,
        "status": "scheduled",
        "items_processed": None,
        "trigger_output_file": trigger_output_file,
    }

    # Atomic write: temp file then rename
    fd, tmp = tempfile.mkstemp(dir=sdir, prefix=".tmp_")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(state, f, indent=2)
        os.rename(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    return path


def create_skipped_state_file(name, reason):
    """Create a state file with status 'skipped'."""
    sdir = get_state_dir(name)
    os.makedirs(sdir, exist_ok=True)

    nnn = next_nnn(name)
    run_id = f"{today_prefix()}-{nnn:03d}"
    filename = f"{run_id}.json"
    path = os.path.join(sdir, filename)

    state = {
        "workflow": name,
        "run_id": run_id,
        "started_at": now_iso(),
        "completed_at": now_iso(),
        "status": "skipped",
        "items_processed": 0,
        "trigger_output_file": None,
        "skip_reason": reason,
    }

    fd, tmp = tempfile.mkstemp(dir=sdir, prefix=".tmp_")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(state, f, indent=2)
        os.rename(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    return path


def evaluate_schedule(fm, latest_state_path, latest_state):
    """Check if a workflow is due based on its schedule.

    Returns True/False.
    """
    schedule = fm.get("schedule")
    if not schedule:
        # No schedule — will rely on trigger alone
        return True

    # Determine last run time from latest state file
    if latest_state and latest_state.get("completed_at"):
        last_run = datetime.datetime.fromisoformat(latest_state["completed_at"])
    elif latest_state and latest_state.get("started_at"):
        last_run = datetime.datetime.fromisoformat(latest_state["started_at"])
    else:
        # Never run — always due
        return True

    try:
        cron = croniter.croniter(schedule, last_run)
        next_run = cron.get_next(datetime.datetime)
        now = datetime.datetime.now(datetime.timezone.utc)
        # Handle timezone-aware v.s. naive
        if next_run.tzinfo is None and now.tzinfo is not None:
            next_run = next_run.replace(tzinfo=now.tzinfo)
        elif next_run.tzinfo is not None and now.tzinfo is None:
            next_run = next_run.replace(tzinfo=None)
        return now >= next_run
    except (ValueError, KeyError):
        return False


def execute_trigger(fm):
    """Execute a trigger command.

    Returns (output, error_reason, empty_reason):
      output: stdout text (or None if no trigger / error / empty)
      error_reason: string if command failed to execute (timeout, crash);
                    None if trigger ran normally (fired, empty, or non-zero exit)
      empty_reason: string if trigger ran but produced no event
                    (empty stdout or non-zero exit); None if fired or error
    """
    trigger = fm.get("trigger")
    if not trigger:
        return None, None, None

    timeout_s = TRIGGER_TIMEOUT_DEFAULT
    env_val = os.environ.get(TRIGGER_TIMEOUT_ENV_VAR)
    if env_val:
        try:
            timeout_s = int(env_val)
        except ValueError:
            pass

    try:
        r = subprocess.run(
            trigger,
            shell=True,
            executable=TRIGGER_SHELL,
            capture_output=True,
            text=True,
            timeout=timeout_s,
            cwd=project_root(),
        )
    except subprocess.TimeoutExpired:
        return None, f"trigger command timed out after {timeout_s}s", None
    except Exception as e:
        return None, f"trigger command failed: {e}", None

    if r.returncode != 0:
        stderr = r.stderr.strip()
        reason = f"trigger exit code {r.returncode}"
        if stderr:
            reason += f": {stderr}"
        return None, None, reason  # normal non-due

    output = r.stdout.strip()
    if not output:
        return None, None, "trigger produced empty output"  # normal non-due

    return output, None, None  # fired


def save_trigger_output(name, trigger_output_file, text):
    """Save trigger output to a temp file. Returns the file path."""
    sdir = get_state_dir(name)
    os.makedirs(sdir, exist_ok=True)

    path = os.path.join(sdir, trigger_output_file)
    fd, tmp = tempfile.mkstemp(dir=sdir, prefix=".tmp_")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(text)
        os.rename(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    return path


def process_workflow(fp, fm, body, force_name, dry_run):
    """Process one workflow. Returns a dispatch entry dict or None."""
    name = fm.get("name")
    if not name:
        return {
            "type": "error",
            "name": os.path.basename(fp),
            "reason": "missing 'name' in front-matter",
        }

    # Verify name matches filename slug
    expected_slug = slugify(name)
    actual_slug = os.path.splitext(os.path.basename(fp))[0]
    if actual_slug != expected_slug:
        return {
            "type": "error",
            "name": name,
            "reason": f"filename '{actual_slug}' doesn't match name slug '{expected_slug}'",
        }

    # Must have at least schedule or trigger
    has_schedule = bool(fm.get("schedule"))
    has_trigger = bool(fm.get("trigger"))
    if not has_schedule and not has_trigger:
        return {
            "type": "not_due",
            "name": name,
            "reason": "no schedule and no trigger configured",
        }

    # Force-run
    if force_name and name == force_name:
        pass  # skip due checks, force dispatch
    elif force_name:
        # Not the requested workflow — still report execution failures
        has_sched = bool(fm.get("schedule"))
        has_trig = bool(fm.get("trigger"))
        if has_trig:
            _, err, _ = execute_trigger(fm)
            if err:
                return {"type": "error", "name": name, "reason": err}
        return {"type": "not_due", "name": name, "reason": "skipped (--run focused on different workflow)"}

    # --- Due evaluation ---
    latest_path, latest_state = get_latest_state_file(name)

    # Check collision: is workflow currently running?
    if latest_state and latest_state.get("status") == "scheduled" and not latest_state.get("completed_at"):
        if force_name and name == force_name:
            # Force-run even if running — let the agent handle it
            pass
        else:
            skip_reason = "workflow is already in progress (status: scheduled, no completed_at)"
            if not dry_run:
                create_skipped_state_file(name, skip_reason)
            return {
                "type": "not_due",
                "name": name,
                "reason": skip_reason,
            }

    # Evaluate trigger
    trigger_output = None
    trigger_output_file = None
    trigger_error = None
    trigger_empty_reason = None

    if has_trigger:
        output, err, empty = execute_trigger(fm)
        if err:
            trigger_error = err  # timeout, crash — script error
        elif empty:
            trigger_empty_reason = empty  # normal non-due
        elif output is not None:
            trigger_output = output

    # AND semantics: if both schedule and trigger, BOTH must be satisfied
    schedule_due = True
    if has_schedule and not (force_name and name == force_name):
        schedule_due = evaluate_schedule(fm, latest_path, latest_state)

    trigger_fired = trigger_output is not None

    is_due = False
    if force_name and name == force_name:
        is_due = True
    elif has_schedule and has_trigger:
        is_due = schedule_due and trigger_fired
    elif has_schedule:
        is_due = schedule_due
    elif has_trigger:
        is_due = trigger_fired

    # Record trigger execution failure (timeout, crash) as script error
    if trigger_error:
        return {
            "type": "error",
            "name": name,
            "reason": trigger_error,
        }

    if not is_due:
        reasons = []
        if has_schedule and not schedule_due:
            reasons.append("schedule not due")
        if has_trigger and not trigger_fired:
            if trigger_empty_reason:
                reasons.append(trigger_empty_reason)
        return {
            "type": "not_due",
            "name": name,
            "reason": "; ".join(reasons) if reasons else "not due",
        }

    # --- Dispatch ---
    if trigger_output is not None:
        tf_name = f"trigger-{today_prefix()}-{next_nnn(name):03d}.txt"
        if not dry_run:
            save_trigger_output(name, tf_name, trigger_output)
        trigger_output_file = os.path.join(get_state_dir(name), tf_name)

    if not dry_run:
        state_file = create_state_file(name, trigger_output_file)
    else:
        state_file = None

    return {
        "type": "due",
        "name": name,
        "trigger_output_file": trigger_output_file,
        "state_file": state_file,
    }


def write_dispatch_log(dispatch):
    """Write complete dispatch log to .state/dispatch/<date>.json."""
    log_dir = os.path.join(project_root(), DISPATCH_DIR)
    os.makedirs(log_dir, exist_ok=True)

    # Find next NNN for dispatch logs
    prefix = today_prefix() + "-"
    max_n = 0
    if os.path.isdir(log_dir):
        for f in os.listdir(log_dir):
            if f.startswith(prefix) and f.endswith(".json"):
                parts = f[len(prefix):-5]
                if parts.isdigit():
                    max_n = max(max_n, int(parts))
    nnn = max_n + 1
    filename = f"{prefix}{nnn:03d}.json"
    path = os.path.join(log_dir, filename)

    log_entry = {
        "invoked_at": now_iso(),
        "due": dispatch.get("due", []),
        "script_errors": dispatch.get("script_errors", []),
        "not_due": dispatch.get("not_due", []),
    }

    fd, tmp = tempfile.mkstemp(dir=log_dir, prefix=".tmp_")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(log_entry, f, indent=2)
        os.rename(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    return path


# --- CLI ---

def build_parser():
    p = argparse.ArgumentParser(description="Loop Creation Kit — workflow dispatch scanner")
    p.add_argument("--run", metavar="NAME", help="Force-run a specific workflow by name")
    p.add_argument("--list", action="store_true", help="List all workflows and their status")
    p.add_argument("--dry-run", action="store_true", help="Show what would run without executing")
    return p


def cmd_list_only(workflows):
    """Handle --list: print workflow info and exit."""
    rows = []
    for fp, fm, body in workflows:
        name = fm.get("name", os.path.splitext(os.path.basename(fp))[0])
        schedule = fm.get("schedule", "—")
        trigger = fm.get("trigger", "—")
        if "error" in fm.get("_error", ""):
            schedule = "[parse error]"
            trigger = "[parse error]"

        _, latest = get_latest_state_file(name)
        if latest:
            last_run = latest.get("started_at", "unknown")
            last_status = latest.get("status", "unknown")
        else:
            last_run = "never"
            last_status = "—"

        rows.append({
            "name": name,
            "schedule": schedule,
            "trigger": trigger,
            "last_run": last_run,
            "last_status": last_status,
        })

    print(json.dumps({"workflows": rows}, indent=2))
    sys.exit(0)


def main():
    args = build_parser().parse_args()

    root = project_root()
    workflows_root = os.path.join(root, WORKFLOWS_DIR)

    if not os.path.isdir(workflows_root):
        output = {"due": [], "script_errors": [], "not_due": []}
        print(json.dumps(output))
        sys.exit(0)

    all_workflows = read_all_workflows()

    if args.list:
        cmd_list_only(all_workflows)

    dispatch = {
        "due": [],
        "script_errors": [],
        "not_due": [],
    }

    for fp, fm, body in all_workflows:
        if "_error" in fm:
            name = os.path.splitext(os.path.basename(fp))[0]
            dispatch["script_errors"].append({
                "name": name,
                "reason": fm["_error"],
                "state_file": None,
            })
            continue

        result = process_workflow(fp, fm, body, args.run, args.dry_run)
        if result is None:
            continue

        if result["type"] == "due":
            dispatch["due"].append({
                "name": result["name"],
                "trigger_output_file": result["trigger_output_file"],
                "state_file": result["state_file"],
            })
        elif result["type"] == "error":
            dispatch["script_errors"].append({
                "name": result["name"],
                "reason": result["reason"],
                "state_file": result.get("state_file"),
            })
        elif result["type"] == "not_due":
            dispatch["not_due"].append({
                "name": result["name"],
                "reason": result["reason"],
            })

    # Write dispatch log (skip during dry-run)
    if not args.dry_run:
        write_dispatch_log(dispatch)

    # Output to stdout
    print(json.dumps(dispatch, indent=2))


if __name__ == "__main__":
    main()