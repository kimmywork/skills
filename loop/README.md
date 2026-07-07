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

## Example: greeting-notification

A real-world worked example demonstrating the full loopify → loopy flow.

### Scenario

The user wanted a macOS notification with a creative agent-generated greeting every 10 minutes.

### Creation (via loopify)

1. **loopify grilled**: notification style (free-form creative), mechanism (`osascript display notification`), greeting source (LLM-generated each run), schedule (`*/10 * * * *`)
2. **Draft confirmed** → `workflows/greeting-notification.md` written
3. **Dry-run**: `loopy.py --dry-run` confirmed parseability

### Workflow

Full content of `workflows/greeting-notification.md`:

~~~~markdown
---
name: greeting-notification
description: Every 10 minutes, generate a creative greeting and show it as a macOS notification
schedule: "*/10 * * * *"
---

Generate a creative non-offensive greeting (max 80 characters) and display it as a macOS system notification.

## Steps

1. **Generate greeting** — Write a short original greeting. Style can be funny, poetic, warm, quirky, or any creative direction. Do not repeat greetings used in previous state files (check `workflows/.state/greeting-notification/`). Keep it under 80 characters. No offensive content.

2. **Display notification** — Run:
   ```bash
   osascript -e 'display notification "<greeting>" with title "👋 Greeting"'
   ```
   If the greeting contains single quotes, escape them properly.

3. **Verify** — Confirm osascript exit code is 0.

## Error handling

- **Greeting generation fails**: use fallback `"Hello there!"` and proceed.
- **osascript fails**: write failure details to state file, set status to `failed`.
- **Do not**: modify any project files, write persistent logs outside state file, or block the next scheduled run.

## Success condition

`osascript` returned exit code 0 — notification was delivered to the user's screen.
~~~~

### Execution Results (4 runs via `--run`)

| Run | Message |
|-----|---------|
| 1 | "May your code compile on the first try and your coffee be ever hot. ☕" |
| 2 | "Life is short — take a break, stretch, and smile. You are doing great. 🌟" |
| 3 | "The stars are aligning — or maybe that is just your screen. Either way, you are awesome. ✨" |
| 4 | "If you are reading this, you are breathing. If you are breathing, you are winning. Keep it up. 🏆" |

All runs: `status: success`, `items_processed: 1`. Each greeting was unique (state dedup via prior state file checks).

### Key Takeaways

- **`--run` vs schedule**: `--run` bypasses cron for testing; bare `loopy.py` marks workflow `not_due` when schedule hasn't elapsed.
- **State dedup**: Workflow body checks prior state to avoid repeating content.
- **Atomic state updates**: Read → modify → write tmp → rename to prevent partial writes.
- **Autonomous**: No user input required during execution.

## References

- `skills/loopy/references/workflow-format.md` — full workflow spec
- `skills/loopy/references/setup.md` — cron setup, env vars, gitignore
- `skills/loopify/references/grilling-checklist.md` — clarity probes used during workflow creation"}]
