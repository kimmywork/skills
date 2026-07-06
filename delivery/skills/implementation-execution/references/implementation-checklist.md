# Implementation Checklist

Use per verifiable increment.

## Pre-flight

- [ ] Current track/requirements/plan was read.
- [ ] Current increment and acceptance criteria are clear.
- [ ] Planned structure and interfaces are clear.
- [ ] Verification method is known.

## Readiness gate

- [ ] Scope is clear and non-goals are respected.
- [ ] Acceptance criteria are binary (pass/fail).
- [ ] Verification method is defined and actionable.
- [ ] Dependencies and blocked items are resolved or documented.

## Production

- [ ] Produced the smallest change for the increment.
- [ ] No speculative scaffolding or unapproved scope.
- [ ] Changes match the plan or have a change note.
- [ ] For software deliverables: TDD/build/test steps per `software-mode.md`.

## Refinement

- [ ] Refined only after verification passed.
- [ ] Refinement preserves intended behavior.
- [ ] Verification re-run after refinement.

## Review

- [ ] Spec fit checked.
- [ ] Format fit checked (load criteria from `delivery-acceptance/references/format-*.md`).
- [ ] Checker/reviewer subagent used when available.
- [ ] Self-review limitation recorded when no checker exists.

## Record

- [ ] Evidence recorded in track/log/delivery record.
- [ ] Loop state updated if present.
- [ ] Docs corrected if stale or contradicted by sources.
- [ ] Change note written if scope, design, contracts, acceptance, or planned structure drifted.