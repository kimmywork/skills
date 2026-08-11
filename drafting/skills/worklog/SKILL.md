---
name: worklog
description: Record completed logical workspace changes as traceable daily log entries and maintain a current workstate snapshot. Use after a logical change that edits, creates, deletes, or reconfigures workspace files. Also use when the user asks to check progress, review recent changes, or see what is planned next.
---

# Worklog

After each completed logical workspace change, record what changed, why, and what remains current.

## Rules

- Follow an existing repository worklog convention when it is explicit. Otherwise use the default convention below.
- Create one entry per logical change, not per command or individual file edit. Keep entries concise.
- Store default entries in one daily file: `.agents/worklog/YYYY-MM-DD.md`. Append same-day entries to that file; do not create numbered or rolling same-day files.
- Before writing every entry, run `date '+%F %T %Z'`. Use the returned local calendar date for the filename and entry timestamp.
- Compare the returned date with the current log filename. If it differs, start a new daily file; never append across dates or add a suffix because the session continues.
- Log what changed and why, not intermediate attempts or command transcripts. Link relevant decisions, evidence, or related entries when they help recovery.
- Maintain `.agents/workstate.md` as a compact current snapshot, not an append-only history.
- Use version history where available for detailed change history. Keep the daily log focused on operational continuity.
- Apply one convention consistently throughout the repository.

## Entry and workstate content

Each daily entry records a timestamp, a concise change summary, its reason, and useful references or remaining gaps.

Keep the workstate limited to current focus, current status or blocker, recent completed changes, next steps, and useful references. Replace stale content instead of preserving a timeline there.

## Bootstrapping

If no explicit repository convention exists, create `.agents/worklog/` as needed and use this skill's default paths and entry content. Record a different durable convention in the repository's agent-facing context entry point only when the repository needs one shared across future sessions.

If the `date` command is unavailable or its timezone cannot be determined, report that limitation instead of guessing the log date.

## Output

In the user's language, state which log or workstate files were created or updated, the logical change recorded, and any unavailable timestamp, reference, or convention information.
