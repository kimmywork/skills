---
name: solution-delivery-loop
description: "Use when work needs end-to-end delivery, phase triage, or continuation from request to accepted outcome: requirements, design, implementation planning, coding, bugfixes, refactors, maintenance, validation, delivery records, autonomous loops, or existing track/plan work."
license: MIT
metadata:
  author: kenpusney
  version: "0.6.1"
---

# Solution Delivery Loop

`Sense → Shape → Design → Build → Verify → Record → Continue/Stop`

## Work type triage

| Work type | Entry point | Skip |
|---|---|---|
| New work | requirement-discovery | — |
| Investigation | structured-investigation or requirement-discovery | — |
| Fix | implementation-execution or requirement-discovery | solution-design for trivial fixes |
| Restructure | solution-design (from current-state analysis) | requirement-discovery |
| Migrate | solution-design (from mapping table) | requirement-discovery |
| Enhance | requirement-discovery or solution-design | — |

## First move

1. Inspect existing context: `.agents/loop-state.md`, track docs, requirements, plans, delivery records, `docs/knowledge`, `docs/logs`.
2. Right-size inspection: read enough to resolve the current phase; stop when more context won't change the next action.
3. Route to the next phase — process first, then execute:
   - unclear need, users, behavior, or scope → `requirement-discovery`
   - clear requirements needing solution/plan → `solution-design`
   - executable plan or evidence-backed small fix → `implementation-execution`
   - implementation done, completion claim, or review → `delivery-acceptance`

Read docs/code first. Ask the user only after context search leaves real ambiguity. Ask one focused question at a time.

## Review and feedback loop

After each phase output, invoke `review-feedback` before next phase. Cumulative review: `review-feedback` inspects all prior artifacts + current output.

| Review at | Inspects | Rollback to |
|---|---|---|
| solution-design | Requirements + design | requirement-discovery |
| implementation-execution | Requirements + design + implementation | requirement-discovery |
| delivery-acceptance | all prior + delivery record | requirement-discovery |

After resolved, write a change note if scope/contract/design changed. See `process-distillation` skill for improvement cycles.

## Autonomy policy

Autonomous execution is allowed when evidence is sufficient. `.agents/loop-state.md` may define full-autonomy for this workspace. Autonomy does not waive track notes, verification, delivery records, or change notes.

Use subagents when available: explorer, maker, checker, reviewer. For risky changes, separate maker and checker.

## Session continuity

When resuming in a new session:
1. Read `.agents/loop-state.md` (if exists), latest delivery record, and track docs.
2. Determine: active phase, last verification result, next goal.
3. If no loop-state exists, infer from track documents.
4. Confirm before proceeding: current phase, pending increments, open blockers.

## Track documentation

Prefer feature-scoped track folders under `docs/track/<feature-name>/`:
- `requirements-v1.md`, `solution-design-v1.md`, `plan-v1.md`, `delivery-record-v1.md`
- Simple work: `docs/track/features/<name>.md` or `docs/track/bugfix/<name>.md`

Every behavior-changing work needs a track note. Distinguish internal working docs (under `research/` or `drafts/`) from deliverables (track root). Use `docs/knowledge` for cross-feature knowledge. Use `docs/logs/YYYY-MM-DD.md` for work logs. Docs can be stale; when docs and reality disagree, verify the truth and write it back to docs.

## Loop improvement

Repeated issues in a phase → use `process-distillation`. New skill creation always requires user approval.
