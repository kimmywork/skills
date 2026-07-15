---
name: worklog
description: Record workspace changes as traceable log entries and maintain a current workstate file. Use after any file edit, creation, deletion, or configuration change in the workspace. Also use when the user asks to check progress, review recent changes, or see what's planned next.
---

# Worklog

After every workspace change, create a record so all changes are traceable by time.

## Rules

- Every entry is anchored to a timestamp.
- One entry per logical change. If it would be one commit, it is one entry.
- Log what changed and why, not how. Keep entries concise.
- Never append to a previous entry. Create a new one and reference the original if needed.
- Maintain a workstate file: current focus, recent changes, next steps, references.
- Rotate log files so no single file grows unbounded. The rotation cadence (daily, weekly, by size) is part of the repo convention.
- All logs in the same repo follow the same conventions.

## Bootstrapping

If the repo already has a worklog convention (in AGENTS.md or similar), follow it. If not, define a concrete convention — file layout, entry format, naming — and write it into the context entry point (e.g. AGENTS.md) so every future session inherits it.
