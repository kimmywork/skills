---
name: loopy
description: Execute scheduled or triggered workflows defined in `workflows/*.md`. Run `scripts/loopy.py` to scan due workflows, then execute each sequentially with full context.
---

# loopy — Workflow Execution Skill

## When to invoke

- Called by the agent (directly or via periodic scheduling mechanism like cron → agent CLI, `/loop`, automations)
- Use `--run <name>` for manual force-run, `--list` for status, `--dry-run` for preview

## Execution process

1. **Run the script**: `python3 scripts/loopy.py` (from project root, relative to this SKILL.md)
   - For flags: `--run <name>`, `--list`, `--dry-run`
2. **Read stdout**: parse the JSON dispatch list
   - `due`: workflows ready to execute
   - `script_errors`: workflows that failed trigger/YAML parsing — **investigate and resolve these setup issues before executing due workflows**
   - `not_due`: workflows that didn't fire — normal, recorded in dispatch log
3. **For each due workflow** (sequentially):
   a. Read the workflow body from `workflows/<name>.md`. Refer to `references/workflow-format.md` for body conventions and success condition expectations.
   b. Read the state file (`state_file` path from dispatch) — it has `status: "scheduled"`, no `completed_at`
   c. Read trigger output from `trigger_output_file` (if present)
   d. Execute steps — use tools, subagents, or direct execution. Do not prompt the user.
   e. Update state file: set `status: success|failed|partial`, `completed_at`, `items_processed`, and optionally `failure` details
      **Atomic update protocol**: read the JSON state file → modify fields → write to a temp file → rename over the original. This ensures updates survive crashes and partial writes never land on the final path.

## Key rules

- **Sequential**: one workflow at a time. Do not start the next until the current is done.
- **Autonomous**: no user input. Obtain data from trigger output, state files, or external commands.
- **State is history**: read prior state files from `workflows/.state/<name>/` for dedup/comparison/retry decisions.
- **Failure handling**: write failure detail to state file. On next run, read prior state and decide retry/skip/restart.
- **Verify success condition**: before marking a run complete, verify the workflow body's success condition has been met. Use tools to confirm (check file exists, test passes, CI green, etc.).

## References

- `references/workflow-format.md` — workflow front-matter and body conventions
- `references/setup.md` — dependencies installation and cron environment setup