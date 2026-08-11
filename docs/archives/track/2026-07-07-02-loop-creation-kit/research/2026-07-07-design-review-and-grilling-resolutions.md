# Design Review & Grilling Resolutions

Date: 2026-07-07
Participants: Kimmy Liu (designer), pi (reviewer)

## Structure

This document records two rounds of critique and resolution:

1. **Design review** (9 issues raised against solution-design-v1.md)
2. **Grilling session** (7 structural questions resolved with the designer)

The grilling resolved most review issues and made several design changes. See §3 for a diff against the original design.

---

## 1. Design Review: Issues Raised

Reference: solution-design-v1.md, requirements-v1.md
Reviewer: pi

| # | Severity | Issue | Resolution (via grilling) |
|---|---|---|---|
| 1 | Critical | `loopy` execution architecture: cron cannot invoke a skill; the design claims agent neutrality but also says users configure cron/systemd to invoke `loopy`. Three statements that cannot hold together. | **Dismissed.** Misunderstanding of the loop engineering paradigm. `loopy` is a skill — the agent is the runtime. Cron/automation triggers the agent (via platform mechanisms: Codex Automations, Claude Code `/loop`, cron → agent CLI), which invokes the `loopy` skill. The skill's script outputs a dispatch list; the agent reads it and executes. Agent neutrality means the SKILL.md doesn't assume a specific CLI — the user's agent platform handles scheduling. |
| 2 | Major | Cron parsing requires a non-stdlib library (stdlib has no cron parser). Design claims "Python with no external dependencies." | **Resolved:** Add `croniter` dependency. Document in `references/setup.md`. The "no external dependencies" constraint only applies to cross-skill references, not the script's runtime dependencies. |
| 3 | Major | Trigger command execution context undefined: $PATH, $HOME, cwd, shell, timeout. | **Resolved:** Hard-coded contract in the script: `/bin/sh -c`, project root cwd, 30s timeout, inherits parent process env. Document in `references/setup.md`. |
| 4 | Major | State file NNN sequence algorithm undefined — how to compute the counter? Race condition if two instances write simultaneously? | **Resolved:** Script creates state files atomically (temp + rename). No separate lock file — the state file's existence IS the lock. Script writes `status: "scheduled"`, agent updates to final status. Collision detection: script checks if latest state file has no `completed_at` (i.e., `status: "scheduled"`) — if so, creates a new file with `status: "skipped"` and does not dispatch. |
| 5 | Major | `loopify` grilling protocol + `loopy` execution protocol will exceed SKILL.md 100-line limit (AGENTS.md constraint). | **Resolved:** Core flow stays in SKILL.md (~30-60 lines), detailed instructions (grilling checklist, execution protocol) extracted to `references/`. |
| 6 | Minor | `workflows/.state/` needs `.gitignore` entry — state files are runtime artifacts. | **Resolved:** Best-practice note to add `workflows/.state/` to `.gitignore`. |
| 7 | Minor | Workflow name → filename slug rules undefined. | **Resolved:** `loopify` enforces slug rules: lowercase, spaces → hyphens, strip special chars, max 64 chars. |
| 8 | Minor | New `loop/` plugin needs registration in both marketplace.json files (`.agents/plugins/` and `.claude-plugin/`). | **Resolved:** Deployment step includes marketplace registration. |
| 9 | Minor | Script I/O contract incomplete — no exit codes, no error handling contract, no guarantee `due`/`not_due` are always arrays. | **Resolved:** Script always outputs valid JSON with guaranteed array fields. Errors per workflow don't block others. All results logged to `workflows/.state/dispatch/<YYYY-MM-DD-NNN>.json`. |

---

## 2. Grilling Session: Resolved Questions

### Q1: `loopy` execution architecture — who invokes the agent?

**Design claim:** Agent neutrality + "users configure cron/systemd to invoke `loopy`" + script outputs JSON for agent to read.

**Resolution:** The contradiction is resolved by the loop engineering paradigm. The skill doesn't schedule itself — the agent platform does. Codex Automations, Claude Code `/loop`, or cron → agent CLI all serve as scheduling mechanisms. The `loopy` skill provides the workflow DSL and the dispatch script; the agent (which invoked the skill) reads the JSON and executes workflows. No change needed to the design.

### Q2: Cron expression parsing dependency

**Context:** Design says "Python with minimal dependencies (no external packages beyond stdlib)." Stdlib has no cron parser.

**Resolution:** Add `croniter` (pure Python, ~800 lines). Document installation in `references/setup.md`. The "no external dependencies" constraint only applies to cross-skill references within a plugin bundle, not to runtime script dependencies.

### Q3: Trigger command execution environment

**Context:** A trigger like `gh pr list --state open` needs $PATH, $HOME, cwd, shell type, timeout defined to work reliably in cron/headless environments.

**Resolution:** Hard-code the contract in `loopy.py`:

| Parameter | Value |
|---|---|
| Shell | `/bin/sh -c` |
| CWD | Project root (auto-detected) |
| Timeout | 30s default, overridable via env var `LOOPY_TRIGGER_TIMEOUT` |
| Env | Inherits parent process environment |

Documented in `references/setup.md`. User is responsible for ensuring cron/launchd has the correct env configured.

### Q4: State file format and collision detection

**Context:** Original design: `<YYYY-MM-DD-NNN>.json` per run. Design review asked about NNN sequence algorithm, race conditions, and whether a single `state.json` or JSONL would be better.

**Resolution:** Keep per-run JSON files. Key design decisions:

- **No separate lock file.** The state file's existence IS the atomic check-and-set. Script creates the file atomically (write temp, rename) with `status: "scheduled"`.
- **Collision detection:** Next schedule check reads the latest state file. If its `status` is `"scheduled"` and `completed_at` is missing → workflow is still running → script creates a NEW state file with `status: "skipped"` + `skip_reason`, and does NOT put this workflow in the dispatch list.
- **NNN sequence:** Daily zero-padded counter. Script lists existing state files for today, takes max NNN + 1, pads to 3 digits. No file → `001`.
- **No JSONL.** JSONL's append-only advantage is negated by the need to check-and-set run status atomically.

**State file status values:** `scheduled` (script creates) → `success | failed | partial` (agent writes on completion) | `skipped` (script writes directly on collision).

### Q5: Script dispatch output contract

**Context:** What exactly does `loopy.py` output, and how does the agent consume it?

**Resolution:**

```json
{
  "due": [
    {
      "name": "<workflow name>",
      "trigger_output_file": "workflows/.state/<name>/trigger-YYYY-MM-DD-NNN.txt",
      "state_file": "workflows/.state/<name>/YYYY-MM-DD-NNN.json"
    }
  ],
  "script_errors": [
    {
      "name": "<workflow name>",
      "reason": "trigger command failed / YAML parse error / timeout",
      "state_file": "workflows/.state/<name>/YYYY-MM-DD-NNN.json"
    }
  ]
}
```

- `trigger_output_file`: stdout of the trigger command saved to a temp file (to avoid bloating the dispatch JSON)
- Errors per workflow are independent — one workflow failure doesn't block others
- Every `loopy` invocation writes a full log to `workflows/.state/dispatch/<YYYY-MM-DD-NNN>.json` (including `not_due` entries with reasons), so there's a complete audit trail even for non-firing workflows
- Script always exits 0 with valid JSON; serious script-level errors (can't find workflows/ dir, permission issues) exit 1 with stderr

### Q6: SKILL.md line budget

**Context:** AGENTS.md: SKILL.md ≤ 100 lines. Both `loopify` and `loopy` have significant instruction content.

**Resolution:** Core flow goes in SKILL.md (~40-60 lines). Detailed protocols (grilling checklist, execution steps, state file schema) go in `references/` files. SKILL.md references them with precise instructions on when and how to consult them. Neither skill will need to exceed the line limit.

### Q7: `loopify` grilling protocol — structured vs. free-form

**Context:** Should `loopify` use a rigid questionnaire, free-form conversation, or something in between?

**Resolution:** Mixed approach. A baseline checklist lives in `references/grilling-checklist.md` covering:
  1. Trigger/schedule conditions
  2. Step boundaries
  3. Success criteria
  4. Empty/error case handling
  5. What NOT to do

The agent uses free-form conversation, but after each user response mentally checks the checklist. If any item is uncovered, the agent asks. The agent is ALSO explicitly instructed to watch for domain-specific gaps beyond the checklist and ask about those too.

---

## 3. Design Changes vs solution-design-v1.md

| Area | Original Design | After Grilling |
|---|---|---|
| **State file status enum** | `success / failed / partial / skipped` | `scheduled / success / failed / partial / skipped` |
| **Dispatch output trigger field** | `"trigger_output": "<string or null>"` (inline) | `"trigger_output_file": "<path to temp file>"` (file-based) |
| **Error handling** | Undefined per-workflow isolation | Independent per-workflow errors in `"script_errors"` array; one failure doesn't block others |
| **Dispatch logging** | Not specified | Every invocation logged to `workflows/.state/dispatch/<YYYY-MM-DD-NNN>.json`, including non-firing workflows |
| **State file collision** | REQ-019: "skip + record" without mechanism | Script creates `status: "scheduled"` → later check detects missing `completed_at` → writes `skipped` |
| **Cron parser dependency** | "No external dependencies" | `croniter` + `references/setup.md` |
| **Skill instructions** | All in SKILL.md | Core in SKILL.md ≤100 lines, details in `references/` |
| **loopify grilling** | Protocol described inline | Checklist in `references/grilling-checklist.md` + agent instructed to add domain-specific probes |
| **Trigger execution context** | Not specified | Hard-coded contract (`/bin/sh -c`, cwd, 30s timeout, inherits env) in script + documented in `references/setup.md` |
| **Slug rules** | `name` must match filename, no rules given | lowercase, spaces→hyphens, strip special chars, max 64 chars |

## 4. New Design Conventions Established

These emerged from discussion and should be recorded as design conventions:

1. **State file as lock.** No separate lock file. The existence of a `status: "scheduled"` state file IS the atomic claim. Collision is detected by reading the latest state file's status.
2. **Trigger output via temp file.** Trigger stdout is saved to a `.state/<name>/trigger-<date>.txt` file; the dispatch list only carries the file path. This keeps the dispatch JSON lean and the full output available to the agent.
3. **Per-workflow error isolation.** A workflow that fails to parse/trigger should not prevent other workflows from being dispatched. Errors go in a separate `script_errors` array.
4. **Global dispatch log.** Every `loopy` invocation writes a complete audit trail to `.state/dispatch/`. This is separate from per-workflow run history in `.state/<name>/`.