#!/usr/bin/env python3
"""Validate, schedule, and record agent-executed workflows."""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import yaml
from croniter import croniter

STATE_REL = Path("workflows/.state")
DISPATCH_REL = STATE_REL / "dispatch"
TRIGGER_TIMEOUT_DEFAULT = 30
LEASE_SECONDS_DEFAULT = 86400
SHELL = "/bin/sh"
STATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(\d+)\.json$")
SUCCESS_RE = re.compile(r"^#{1,6}\s+Success condition\s*$", re.IGNORECASE | re.MULTILINE)


def now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def now_iso() -> str:
    return now_utc().isoformat()


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=path.parent, prefix=".tmp_")
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
        os.replace(tmp, path)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def atomic_json(path: Path, data: dict) -> None:
    atomic_write(path, json.dumps(data, indent=2) + "\n")


def read_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except (OSError, json.JSONDecodeError):
        return None


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9-]", "-", name.lower())
    return re.sub(r"-+", "-", slug).strip("-")[:64]


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)
    if not match:
        raise ValueError("missing or malformed YAML frontmatter")
    frontmatter = yaml.safe_load(match.group(1))
    if not isinstance(frontmatter, dict):
        raise ValueError("frontmatter must be a mapping")
    return frontmatter, match.group(2).strip()


def validate_workflow(path: Path) -> dict:
    record = {"path": path, "name": path.stem, "frontmatter": {}, "body": "", "errors": []}
    try:
        fm, body = parse_frontmatter(path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        record["errors"].append(str(exc))
        return record

    record["frontmatter"] = fm
    record["body"] = body
    name = fm.get("name")
    if not isinstance(name, str) or not name.strip():
        record["errors"].append("name must be a non-empty string")
    else:
        record["name"] = name
        expected = slugify(name)
        if not expected:
            record["errors"].append("name does not produce a valid slug")
        elif path.stem != expected:
            record["errors"].append(f"filename '{path.stem}' does not match name slug '{expected}'")

    schedule = fm.get("schedule")
    trigger = fm.get("trigger")
    if not schedule and not trigger:
        record["errors"].append("at least one of schedule or trigger is required")
    if schedule is not None:
        if not isinstance(schedule, str) or len(schedule.split()) != 5 or not croniter.is_valid(schedule):
            record["errors"].append("schedule must be a valid five-field cron expression")
        timezone = fm.get("timezone")
        if not isinstance(timezone, str) or not timezone:
            record["errors"].append("scheduled workflows require an IANA timezone")
        else:
            try:
                ZoneInfo(timezone)
            except ZoneInfoNotFoundError:
                record["errors"].append(f"unknown timezone '{timezone}'")
    if trigger is not None and (not isinstance(trigger, str) or not trigger.strip()):
        record["errors"].append("trigger must be a non-empty shell command")

    permissions = fm.get("permissions")
    if not isinstance(permissions, list) or not permissions or not all(isinstance(x, str) and x for x in permissions):
        record["errors"].append("permissions must be a non-empty list of authorized capabilities")

    concurrency = fm.get("concurrency", "forbid")
    if concurrency != "forbid":
        record["errors"].append("concurrency currently supports only 'forbid'")

    for field in ("max_items", "retry_limit", "timeout_minutes"):
        value = fm.get(field)
        if value is not None and (not isinstance(value, int) or value < 0):
            record["errors"].append(f"{field} must be a non-negative integer")
    if fm.get("timeout_minutes") == 0:
        record["errors"].append("timeout_minutes must be greater than zero")

    if not body:
        record["errors"].append("workflow body is empty")
    elif not SUCCESS_RE.search(body):
        record["errors"].append("body must contain a '## Success condition' heading")
    return record


def load_workflows(root: Path) -> list[dict]:
    return [validate_workflow(Path(path)) for path in sorted(glob.glob(str(root / "workflows/*.md")))]


def state_dir(root: Path, name: str) -> Path:
    return root / STATE_REL / slugify(name)


def state_sort_key(path: Path) -> tuple[str, int]:
    match = STATE_RE.match(path.name)
    return (match.group(1), int(match.group(2))) if match else ("", -1)


def state_files(root: Path, name: str) -> list[Path]:
    directory = state_dir(root, name)
    return sorted((p for p in directory.glob("*.json") if STATE_RE.match(p.name)), key=state_sort_key)


def latest_state(root: Path, name: str) -> tuple[Path | None, dict | None]:
    files = state_files(root, name)
    if not files:
        return None, None
    path = files[-1]
    return path, read_json(path)


def next_run_id(root: Path, name: str) -> str:
    today = dt.date.today().isoformat()
    numbers = [state_sort_key(path)[1] for path in state_files(root, name) if state_sort_key(path)[0] == today]
    return f"{today}-{(max(numbers, default=0) + 1):03d}"


def parse_timestamp(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        parsed = dt.datetime.fromisoformat(value)
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=dt.timezone.utc)
    except ValueError:
        return None


def schedule_due(root: Path, workflow: dict) -> bool:
    fm = workflow["frontmatter"]
    schedule = fm.get("schedule")
    if not schedule:
        return True
    _, latest = latest_state(root, workflow["name"])
    last = parse_timestamp(latest.get("completed_at") if latest else None)
    if last is None:
        last = parse_timestamp(latest.get("started_at") if latest else None)
    if last is None:
        return True
    timezone = ZoneInfo(fm["timezone"])
    local_last = last.astimezone(timezone)
    next_run = croniter(schedule, local_last).get_next(dt.datetime)
    if next_run.tzinfo is None:
        next_run = next_run.replace(tzinfo=timezone)
    return dt.datetime.now(timezone) >= next_run


def env_positive_int(name: str, default: int) -> int:
    try:
        value = int(os.environ.get(name, str(default)))
        return value if value > 0 else default
    except ValueError:
        return default


def execute_trigger(root: Path, workflow: dict) -> dict:
    trigger = workflow["frontmatter"].get("trigger")
    if not trigger:
        return {"status": "absent", "output": None, "reason": None}
    timeout = env_positive_int("LOOPY_TRIGGER_TIMEOUT", TRIGGER_TIMEOUT_DEFAULT)
    try:
        result = subprocess.run(
            trigger,
            shell=True,
            executable=SHELL,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=root,
        )
    except subprocess.TimeoutExpired:
        return {"status": "error", "output": None, "reason": f"trigger timed out after {timeout}s"}
    except Exception as exc:
        return {"status": "error", "output": None, "reason": f"trigger failed: {exc}"}
    if result.returncode != 0:
        reason = f"trigger exit code {result.returncode}"
        if result.stderr.strip():
            reason += f": {result.stderr.strip()}"
        return {"status": "not_fired", "output": None, "reason": reason}
    output = result.stdout.strip()
    if not output:
        return {"status": "not_fired", "output": None, "reason": "trigger produced empty output"}
    return {"status": "fired", "output": output, "reason": None}


def lock_path(root: Path, name: str) -> Path:
    return state_dir(root, name) / ".lock"


def lease_seconds(workflow: dict) -> int:
    minutes = workflow["frontmatter"].get("timeout_minutes")
    if isinstance(minutes, int) and minutes > 0:
        return max(minutes * 60, 60)
    return env_positive_int("LOOPY_LEASE_SECONDS", LEASE_SECONDS_DEFAULT)


def acquire_lock(root: Path, workflow: dict) -> tuple[dict | None, dict | None]:
    path = lock_path(root, workflow["name"])
    path.parent.mkdir(parents=True, exist_ok=True)
    token = uuid.uuid4().hex
    acquired = now_utc()
    lock = {
        "workflow": workflow["name"],
        "token": token,
        "acquired_at": acquired.isoformat(),
        "expires_at": (acquired + dt.timedelta(seconds=lease_seconds(workflow))).isoformat(),
        "state_file": None,
    }
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        existing = read_json(path) or {"workflow": workflow["name"], "invalid": True}
        expires = parse_timestamp(existing.get("expires_at"))
        existing["stale"] = expires is None or now_utc() >= expires
        return None, existing
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        json.dump(lock, handle, indent=2)
        handle.write("\n")
    return lock, None


def release_lock(root: Path, name: str, token: str | None = None, state_file: str | None = None) -> bool:
    path = lock_path(root, name)
    current = read_json(path)
    if current is None:
        return False
    if token is not None and current.get("token") != token:
        return False
    if state_file is not None and current.get("state_file") != state_file:
        return False
    path.unlink(missing_ok=True)
    return True


def create_run(root: Path, workflow: dict, lock: dict, trigger_output: str | None) -> tuple[Path, Path | None]:
    directory = state_dir(root, workflow["name"])
    run_id = next_run_id(root, workflow["name"])
    path = directory / f"{run_id}.json"
    trigger_path = directory / f"trigger-{run_id}.txt" if trigger_output is not None else None
    if trigger_path is not None:
        atomic_write(trigger_path, trigger_output + "\n")
    state = {
        "workflow": workflow["name"],
        "run_id": run_id,
        "started_at": now_iso(),
        "completed_at": None,
        "status": "scheduled",
        "items_processed": None,
        "trigger_output_file": str(trigger_path.resolve()) if trigger_path else None,
        "lease_expires_at": lock["expires_at"],
        "limits": {
            "max_items": workflow["frontmatter"].get("max_items"),
            "retry_limit": workflow["frontmatter"].get("retry_limit"),
        },
    }
    atomic_json(path, state)
    lock["state_file"] = str(path.resolve())
    atomic_json(lock_path(root, workflow["name"]), lock)
    return path.resolve(), trigger_path.resolve() if trigger_path else None


def dispatch_one(root: Path, workflow: dict, force: bool = False) -> dict:
    name = workflow["name"]
    if not force and workflow["frontmatter"].get("schedule") and not schedule_due(root, workflow):
        return {"type": "not_due", "name": name, "reason": "schedule not due"}

    lock, existing = acquire_lock(root, workflow)
    if lock is None:
        if existing and existing.get("stale"):
            return {"type": "error", "name": name, "reason": "stale workflow lease; run the recover command before dispatching"}
        return {"type": "not_due", "name": name, "reason": "workflow is already in progress"}

    try:
        trigger_output = None
        if not force and workflow["frontmatter"].get("trigger"):
            trigger = execute_trigger(root, workflow)
            if trigger["status"] == "error":
                release_lock(root, name, token=lock["token"])
                return {"type": "error", "name": name, "reason": trigger["reason"]}
            if trigger["status"] != "fired":
                release_lock(root, name, token=lock["token"])
                return {"type": "not_due", "name": name, "reason": trigger["reason"]}
            trigger_output = trigger["output"]
        state, trigger_path = create_run(root, workflow, lock, trigger_output)
        return {
            "type": "due",
            "name": name,
            "state_file": str(state),
            "trigger_output_file": str(trigger_path) if trigger_path else None,
        }
    except Exception:
        release_lock(root, name, token=lock["token"])
        raise


def write_dispatch_log(root: Path, dispatch: dict) -> Path:
    directory = root / DISPATCH_REL
    directory.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    numbers = []
    for path in directory.glob(f"{today}-*.json"):
        match = STATE_RE.match(path.name)
        if match:
            numbers.append(int(match.group(2)))
    path = directory / f"{today}-{(max(numbers, default=0) + 1):03d}.json"
    atomic_json(path, {"invoked_at": now_iso(), **dispatch})
    return path


def ensure_state_path(root: Path, value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = root / path
    path = path.resolve()
    allowed = (root / STATE_REL).resolve()
    try:
        path.relative_to(allowed)
    except ValueError as exc:
        raise ValueError("state file must be under the project workflows/.state directory") from exc
    return path


def update_run(root: Path, state_value: str, status: str, items: int | None, failure: dict | None = None) -> dict:
    path = ensure_state_path(root, state_value)
    state = read_json(path)
    if state is None:
        raise ValueError(f"invalid or missing state file: {path}")
    if state.get("status") != "scheduled" or state.get("completed_at"):
        raise ValueError("only an active scheduled run can be finalized")
    if items is not None and items < 0:
        raise ValueError("items processed cannot be negative")
    max_items = state.get("limits", {}).get("max_items")
    if max_items is not None and items is not None and items > max_items:
        raise ValueError(f"items processed exceeds workflow max_items ({max_items})")
    state["status"] = status
    state["completed_at"] = now_iso()
    state["items_processed"] = items
    state.pop("lease_expires_at", None)
    if failure:
        state["failure"] = failure
    atomic_json(path, state)
    released = release_lock(root, state["workflow"], state_file=str(path))
    return {"state_file": str(path), "status": status, "lock_released": released}


def heartbeat(root: Path, state_value: str, seconds: int) -> dict:
    path = ensure_state_path(root, state_value)
    state = read_json(path)
    if state is None or state.get("status") != "scheduled":
        raise ValueError("heartbeat requires an active scheduled state")
    lock_file = lock_path(root, state["workflow"])
    lock = read_json(lock_file)
    if lock is None or lock.get("state_file") != str(path):
        raise ValueError("active lock does not match the state file")
    expires = now_utc() + dt.timedelta(seconds=seconds)
    lock["expires_at"] = expires.isoformat()
    state["lease_expires_at"] = expires.isoformat()
    atomic_json(path, state)
    atomic_json(lock_file, lock)
    return {"state_file": str(path), "lease_expires_at": expires.isoformat()}


def recover(root: Path, name: str, force: bool) -> dict:
    path = lock_path(root, name)
    lock = read_json(path)
    if lock is None:
        raise ValueError(f"no active lock for workflow '{name}'")
    expires = parse_timestamp(lock.get("expires_at"))
    stale = expires is None or now_utc() >= expires
    if not stale and not force:
        raise ValueError("workflow lease is still active; use --force only after confirming the run is abandoned")
    state_value = lock.get("state_file")
    if state_value:
        state_path = ensure_state_path(root, state_value)
        state = read_json(state_path)
        if state and state.get("status") == "scheduled":
            state["status"] = "failed"
            state["completed_at"] = now_iso()
            state["items_processed"] = state.get("items_processed")
            state["failure"] = {"step": "lease", "error": "run recovered after an abandoned or stale lease"}
            state.pop("lease_expires_at", None)
            atomic_json(state_path, state)
    path.unlink(missing_ok=True)
    return {"workflow": name, "recovered": True, "state_file": state_value}


def error_record(workflow: dict) -> dict:
    return {"name": workflow["name"], "reason": "; ".join(workflow["errors"]), "state_file": None}


def static_preview(root: Path, workflows: list[dict], evaluate_triggers: bool) -> dict:
    output = {"validated": [], "script_errors": []}
    for workflow in workflows:
        if workflow["errors"]:
            output["script_errors"].append(error_record(workflow))
            continue
        due = schedule_due(root, workflow)
        trigger_status = "absent"
        trigger_reason = None
        if workflow["frontmatter"].get("trigger"):
            if evaluate_triggers and due:
                trigger = execute_trigger(root, workflow)
                trigger_status = trigger["status"]
                trigger_reason = trigger["reason"]
            else:
                trigger_status = "not_evaluated"
        output["validated"].append({
            "name": workflow["name"],
            "schedule_due": due,
            "trigger_status": trigger_status,
            "trigger_reason": trigger_reason,
        })
    return output


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate and dispatch agent workflows")
    parser.add_argument("--project-root", default=".", help="Project containing workflows/ (default: current directory)")
    parser.add_argument("--run", metavar="NAME", help="Force-dispatch one workflow without schedule or trigger evaluation")
    parser.add_argument("--list", action="store_true", help="List workflows and latest status")
    parser.add_argument("--dry-run", action="store_true", help="Validate and preview without executing triggers or writing state")
    parser.add_argument("--evaluate-triggers", action="store_true", help="With --dry-run, explicitly execute trigger commands")
    parser.add_argument("--validate", nargs="?", const="*", metavar="NAME", help="Statically validate all workflows or one name")
    parser.add_argument("--test-trigger", metavar="NAME", help="Explicitly execute one workflow trigger without dispatching")

    commands = parser.add_subparsers(dest="command")
    complete = commands.add_parser("complete", help="Finalize an active run")
    complete.add_argument("state_file")
    complete.add_argument("--status", choices=("success", "partial"), default="success")
    complete.add_argument("--items", type=int, default=0)

    fail = commands.add_parser("fail", help="Mark an active run failed")
    fail.add_argument("state_file")
    fail.add_argument("--error", required=True)
    fail.add_argument("--step", default="workflow")
    fail.add_argument("--partial-results")
    fail.add_argument("--items", type=int, default=0)

    beat = commands.add_parser("heartbeat", help="Extend an active run lease")
    beat.add_argument("state_file")
    beat.add_argument("--lease-seconds", type=int, default=LEASE_SECONDS_DEFAULT)

    recovery = commands.add_parser("recover", help="Release an abandoned or stale workflow lease")
    recovery.add_argument("name")
    recovery.add_argument("--force", action="store_true")
    return parser


def select_by_name(workflows: list[dict], name: str) -> dict | None:
    return next((workflow for workflow in workflows if workflow["name"] == name), None)


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.project_root).expanduser().resolve()

    try:
        if args.command == "complete":
            print(json.dumps(update_run(root, args.state_file, args.status, args.items), indent=2))
            return 0
        if args.command == "fail":
            failure = {"step": args.step, "error": args.error}
            if args.partial_results:
                failure["partial_results"] = args.partial_results
            print(json.dumps(update_run(root, args.state_file, "failed", args.items, failure), indent=2))
            return 0
        if args.command == "heartbeat":
            if args.lease_seconds <= 0:
                raise ValueError("lease seconds must be positive")
            print(json.dumps(heartbeat(root, args.state_file, args.lease_seconds), indent=2))
            return 0
        if args.command == "recover":
            print(json.dumps(recover(root, args.name, args.force), indent=2))
            return 0
    except ValueError as exc:
        print(json.dumps({"error": str(exc)}, indent=2))
        return 1

    workflows = load_workflows(root)

    if args.validate is not None:
        selected = workflows if args.validate == "*" else [w for w in workflows if w["name"] == args.validate]
        if args.validate != "*" and not selected:
            print(json.dumps({"valid": [], "errors": [{"name": args.validate, "reason": "workflow not found"}]}, indent=2))
            return 1
        errors = [error_record(workflow) for workflow in selected if workflow["errors"]]
        valid = [workflow["name"] for workflow in selected if not workflow["errors"]]
        print(json.dumps({"valid": valid, "errors": errors}, indent=2))
        return 1 if errors else 0

    if args.list:
        rows = []
        for workflow in workflows:
            _, latest = latest_state(root, workflow["name"])
            rows.append({
                "name": workflow["name"],
                "valid": not workflow["errors"],
                "errors": workflow["errors"],
                "schedule": workflow["frontmatter"].get("schedule"),
                "timezone": workflow["frontmatter"].get("timezone"),
                "has_trigger": bool(workflow["frontmatter"].get("trigger")),
                "last_status": latest.get("status") if latest else None,
                "last_run": latest.get("started_at") if latest else None,
            })
        print(json.dumps({"workflows": rows}, indent=2))
        return 0

    if args.test_trigger:
        workflow = select_by_name(workflows, args.test_trigger)
        if workflow is None:
            print(json.dumps({"error": "workflow not found", "name": args.test_trigger}, indent=2))
            return 1
        if workflow["errors"]:
            print(json.dumps(error_record(workflow), indent=2))
            return 1
        print(json.dumps({"name": workflow["name"], **execute_trigger(root, workflow)}, indent=2))
        return 0

    if args.evaluate_triggers and not args.dry_run:
        print(json.dumps({"error": "--evaluate-triggers requires --dry-run"}, indent=2))
        return 1
    if args.dry_run:
        print(json.dumps(static_preview(root, workflows, args.evaluate_triggers), indent=2))
        return 0

    dispatch = {"due": [], "script_errors": [], "not_due": []}
    selected = workflows
    if args.run:
        workflow = select_by_name(workflows, args.run)
        if workflow is None:
            dispatch["script_errors"].append({"name": args.run, "reason": "workflow not found", "state_file": None})
            print(json.dumps(dispatch, indent=2))
            return 1
        selected = [workflow]

    for workflow in selected:
        if workflow["errors"]:
            dispatch["script_errors"].append(error_record(workflow))
            continue
        result = dispatch_one(root, workflow, force=bool(args.run))
        bucket = "due" if result["type"] == "due" else "script_errors" if result["type"] == "error" else "not_due"
        result.pop("type")
        dispatch[bucket].append(result)

    write_dispatch_log(root, dispatch)
    print(json.dumps(dispatch, indent=2))
    return 1 if dispatch["script_errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
