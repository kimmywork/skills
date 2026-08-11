# Workstate

## Current Focus

Refine the skill framework from observed use while keeping skills independent and bundle-scoped.

## Current Status

The `align` and `agent-facing-doc` split is implemented. The `worklog` skill now uses daily entries, an explicit date-rotation check, and a snapshot workstate.

## Recent Completed Changes

- Added `utility/skills/agent-facing-doc/` and its shared document guide.
- Kept `align` focused on project knowledge and documentation alignment, with separate triggers for knowledge changes and reference remapping.
- Updated agent-facing document rules, plugin metadata, skill inventories, and local discovery links.
- Revised `drafting/skills/worklog/SKILL.md` to use daily logs, a current snapshot, and an explicit `date` check before each entry.

## Next Steps

Review the revised skills in use and adjust only from observed friction or failures.

## References

- `AGENTS.md`
- `utility/skills/agent-facing-doc/SKILL.md`
- `drafting/skills/align/SKILL.md`
- `drafting/skills/worklog/SKILL.md`
