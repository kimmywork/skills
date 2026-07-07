# Workflow Format Reference

Workflows are markdown files in `workflows/<name>.md`.

## Front-matter

```yaml
---
name: <string>              # Required, must match filename slug
description: <string>       # Optional
schedule: "<cron expr>"     # Optional, 5-field cron (requires croniter)
trigger: "<shell command>"  # Optional, fires when stdout non-empty and exit 0
---
```

### Rules

- `name` is required. Must match the filename (without `.md`). Slug rules: lowercase, spaces→hyphens, strip special chars, max 64 chars.
- At least one of `schedule` or `trigger` must be present.
- **Both present (AND semantics)**: workflow fires only when schedule is due AND trigger produces non-empty output.

### Schedule

5-field cron: `MIN HOUR DOM MONTH DOW`. Examples:
- `0 9 * * *` — daily at 09:00
- `*/15 * * * *` — every 15 minutes
- `0 0 1 */3 *` — first of every quarter

### Trigger

A shell command executed via `/bin/sh -c` from project root. Fires when:
- Exit code is 0
- stdout is non-empty (after stripping whitespace)

## Body

Free-form markdown after the front-matter. Must include a success condition the agent can verify.

Good body:
```markdown
Check all PRs with no activity for 7 days.
Post a summary comment on each.
Success condition: All stale PRs have a comment.
```

Goal-only body (agent figures out steps):
```markdown
Summarize yesterday's CI failures and post to #eng channel.
Success condition: Summary posted.
```

## State files

Each run creates `workflows/.state/<name>/<YYYY-MM-DD-NNN>.json`:

```json
{
  "workflow": "<name>",
  "run_id": "YYYY-MM-DD-NNN",
  "started_at": "<ISO-8601>",
  "completed_at": null,
  "status": "scheduled | success | failed | partial | skipped",
  "items_processed": null,
  "trigger_output_file": "<path or null>",
  "skip_reason": "<string, only when status=skipped>",
  "failure": {
    "step": "<step identifier>",
    "error": "<error message>",
    "partial_results": "<what was completed>"
  }
}
```

- Script creates with `status: "scheduled"`. Agent updates to final status.
- `skupped` status: script writes when workflow is in progress and next schedule fires.
- Atomic writes: temp file then rename. No separate lock file — state file existence IS the lock.