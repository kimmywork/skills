---
name: implementation-execution
description: Use when executing a software plan, implementing a feature, fixing a bug, refactoring, performing maintenance, or running an autonomous delivery loop after scope, design, and verification expectations are clear.
license: MIT
metadata:
  author: kenpusney
  version: "0.4.0"
---

# Implementation Execution

Build one verified vertical slice at a time.

## Before editing

1. Read the current track/PRD/plan/delivery record, `.agents/loop-state.md` if present, `docs/knowledge`, relevant logs, code, and tests.
2. Reconfirm current slice, module landing, contracts, acceptance criteria, and verification command.
3. If intent, design, or verification is unclear, stop and use `requirement-discovery` or `solution-design`.

## Execution loop

For each slice:

1. Define expected behavior and verification evidence.
2. Prefer TDD: write/adjust the test, watch it fail, implement minimal code, watch it pass.
3. For user flows, prefer E2E or integration-driven verification at the highest reliable seam.
4. Refactor only after green; keep behavior stable.
5. Run relevant verification.
6. Review for spec fit and architecture fit.
7. Update track docs, loop state, logs, or delivery record with evidence and deltas.

Use `references/implementation-checklist.md` for the slice checklist.

## Autonomy and subagents

Autonomous execution is allowed when the plan and evidence are sufficient. Use subagents when available and valuable:

- explorer: gather facts without editing
- maker: implement the slice
- checker/reviewer: verify spec fit and code fit

If unavailable, perform a fresh review pass yourself and state that review was self-performed.

## Change control

Stop and write a change note before continuing when any of these occur:
- A test expectation changes because behavior differs from the PRD/plan, not because the test is wrong.
- You need to add a field, column, parameter, route, or component not in the plan.
- You skip or weaken a non-goal from the requirements.
- A verification command from the plan no longer makes sense or produces unrelated output.
- Approved scope, architecture, contract, data model, acceptance criteria, or planned module landing changes.

Template: `software-delivery-loop/references/change-note-template.md`.

Do not hide drift with compatibility shims unless explicitly accepted as a migration strategy.

## Related skills

- Previous: use `solution-design` when the solution or plan is missing.
- Next: use `delivery-acceptance` before claiming done or shipping.
- Return to `requirement-discovery` when implementation reveals unclear software intent, behavior, or acceptance.

## After this phase

After all slices complete, output inspected by `review-feedback` (cumulative with prior phases: PRD + design + implementation). Resolution:
- Fix in place: correct issues, re-review.
- Roll back: return to earliest affected phase, correct there, re-execute forward.

After resolved, `process-distillation` may follow (auto under `full-autonomy`).
