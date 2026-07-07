# Loop Plugin

Create and execute recurring automated workflows from natural language descriptions.

## Skills

### `loopify` — Workflow Creation

Grill the user for clarity, draft a workflow spec, and write `workflows/<name>.md`.

**Trigger**: User describes a recurring task (e.g. "check stale PRs every morning").

**Process**:
1. Grill for clarity — one question at a time, covering schedule/trigger, steps, success condition, edge cases
2. Draft after 2-3 rounds (or when all checklist items are covered)
3. Present draft for user confirmation
4. Write `workflows/<name>.md`
5. Verify with `python3 <loopy-skill-root>/scripts/loopy.py --dry-run`

### `loopy` — Workflow Execution

Scan due workflows, execute each sequentially with full state tracking.

**Trigger**: Periodic invocation (cron, agent automation, `/loop`, or manual).

**Commands**:
- `python3 scripts/loopy.py` — scan and execute all due workflows
- `python3 scripts/loopy.py --dry-run` — preview without executing
- `python3 scripts/loopy.py --list` — list all registered workflows
- `python3 scripts/loopy.py --run <name>` — force-run a specific workflow

## Workflow Format

Workflows live in `workflows/<name>.md` with YAML front-matter:

```yaml
---
name: <string>              # Required, filename slug
schedule: "<cron expr>"     # Optional, 5-field (e.g. "0 9 * * *")
trigger: "<shell command>"  # Optional, fires when stdout non-empty + exit 0
---
```

At least one of `schedule` or `trigger` must be present. Both present = AND semantics.

Body is free-form Markdown with a verifiable success condition.

## Getting Started

```bash
# 1. Install dependencies
pip install croniter

# 2. Create a workflow
#    (have the agent run loopify and describe your task)

# 3. Verify
python3 scripts/loopy.py --dry-run

# 4. Run
python3 scripts/loopy.py
```

## Requirements

- Python 3.8+
- PyYAML (usually pre-installed)
- `croniter` — `pip install croniter`

## References

- `skills/loopy/references/workflow-format.md` — full workflow spec
- `skills/loopy/references/setup.md` — cron setup, env vars, gitignore
- `skills/loopify/references/grilling-checklist.md` — clarity probes used during workflow creation