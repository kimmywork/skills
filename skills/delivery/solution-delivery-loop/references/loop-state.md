# Loop State Template

Workspace-level state. Default path: `.agents/loop-state.md`.

Use when work spans multiple turns, agents, days, or automation runs. Keep it short.

~~~~markdown
# Loop State

## Workspace Policy

- Autonomy: ask-first | evidence-backed-autonomy | full-autonomy

## Current Focus

- Goal:
- Feature track:
- Current phase: sense | shape | design | build | verify | record | blocked | delivered

## Source Artifacts

- Requirements doc:
- Plan:
- Delivery record:
- Change notes:

## Decisions

- <decision and reason>

## Open Questions

- <question blocking progress or acceptance>

## Active Tasks

- [ ] <next task>

## Verification Evidence

- `<command or manual check>` → <result/date>

## Recurring Loop Issues

- <phase/problem/frequency/evidence>

## Next Action

<the single next action the loop should take>
~~~~

Rules:

- Read at loop start when present.
- Update after phase transitions, blocked states, autonomous runs, or policy changes.
- Do not duplicate requirements/plan content; reference paths.
- If absent, mention it as optional workspace continuity, not a prerequisite.
- Self-improvement is ask-first unless Autonomy is `full-autonomy`.
