# Implementation Checklist

Use per vertical slice.

## Pre-flight

- [ ] Current track/PRD/plan was read.
- [ ] Current slice and acceptance criteria are clear.
- [ ] Module landing and contracts are clear.
- [ ] Verification command/manual check is known.

## Readiness gate

- [ ] Scope is clear and non-goals are respected.
- [ ] Acceptance criteria are binary (pass/fail).
- [ ] Verification command is known and runnable.
- [ ] Dependencies and blocked items are resolved or documented.

## TDD / Verification

- [ ] Behavior change has a failing test first, when practical.
- [ ] Failure reason was checked and matches the missing behavior.
- [ ] User flow change has E2E or integration verification at the highest reliable seam.
- [ ] If test-first is impractical, reason and manual/command verification are recorded before editing.

## Build

- [ ] Implemented the smallest change for the slice.
- [ ] No speculative scaffolding.
- [ ] No unapproved compatibility shim, fallback, or deprecated alias.
- [ ] Contract/data/API/UI/storage changes match the plan or have a change note.

## Refactor

- [ ] Refactor only after green verification.
- [ ] Refactor preserves behavior.
- [ ] Verification re-run after refactor.

## Review

- [ ] Spec fit checked.
- [ ] Architecture/code fit checked.
- [ ] Checker/reviewer subagent used when available for risky or multi-file work.
- [ ] Self-review limitation recorded when no checker exists.

## Record

- [ ] Evidence recorded in track/log/delivery record.
- [ ] Loop state updated if present.
- [ ] Docs corrected if stale or contradicted by code/tests.
- [ ] Change note written if scope, design, contract, data model, acceptance, or planned module landing drifted.
