---
name: implementation-execution
description: Use when executing a plan, implementing a feature, fixing a bug, refactoring, performing maintenance, producing a deliverable, or running an autonomous delivery loop after scope, design, and verification expectations are clear.
license: MIT
metadata:
  author: kenpusney
  version: "0.4.0"
---

# Implementation Execution

Build one verified increment at a time.

## Before editing

1. Read the current track/requirements/plan/delivery record, `.agents/loop-state.md` if present, `docs/knowledge`, relevant logs, code, and tests.
2. Reconfirm current increment, structure, contracts, acceptance criteria, and verification method.
3. If intent, design, or verification is unclear, stop and use `requirement-discovery` or `solution-design`.

## Execution loop

For each increment:

1. Define expected outcome and verification evidence.
2. Produce the increment.
3. Verify against evidence.
4. Refine based on verification results.
5. Record evidence and deltas.

For software deliverables, see `references/software-mode.md` for TDD-driven slice execution with automated verification.

Use `references/implementation-checklist.md` for the increment checklist.

## Autonomy and subagents

Autonomous execution is allowed when the plan and evidence are sufficient. Use subagents when available and valuable:

- explorer: gather facts without editing
- maker: produce the increment
- checker/reviewer: verify spec fit and code fit

If unavailable, perform a fresh review pass yourself and state that review was self-performed.

## Change control

> **Iron Law**: NO UNDOCUMENTED DRIFT.

Stop and write a change note before continuing when any of these occur:
- The expected outcome changes mid-increment.
- You need to add scope, fields, or steps not in the approved plan.
- You skip or weaken a requirement or non-goal.
- The verification method no longer applies.
- Terminology or naming used in the increment conflicts with the approved conventions.

Software-specific signals (see `references/software-mode.md`):
- A test expectation changes because behavior differs from the plan, not because the test is wrong.
- You need to add a field, column, parameter, route, or component not in the plan.
- Approved architecture, contract, data model, or module landing changes.

Template: `solution-delivery-loop/references/change-note-template.md`.

## Anti-patterns

- Skipping verification — claiming done without fresh evidence.
- Using compatibility shims or workarounds to hide drift instead of writing a change note.
- Starting implementation before the design has passed review-feedback.

## Related skills

- Previous: use `solution-design` when the solution or plan is missing.
- Next: use `delivery-acceptance` before claiming done or shipping.
- Return to `requirement-discovery` when implementation reveals unclear intent, behavior, or acceptance.

## After this phase

After all slices complete, output inspected by `review-feedback` (cumulative with prior phases: Requirements + design + implementation). Resolution:
- Fix in place: correct issues, re-review.
- Roll back: return to earliest affected phase, correct there, re-execute forward.

After resolved, `process-distillation` may follow (auto under `full-autonomy`).
