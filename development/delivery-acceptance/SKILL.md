---
name: delivery-acceptance
description: Use when reviewing completed software work, checking whether a feature/bugfix/refactor is done, preparing delivery, recording verification evidence, or deciding whether to ship, continue, roll back, or ask for user review.
license: MIT
metadata:
  author: kenpusney
  version: "0.2.0"
---

# Delivery Acceptance

Acceptance is evidence, not confidence.

## Gate

Before any completion claim:

1. Read source requirements: track note, PRD, solution/plan, change notes, loop state.
2. Identify required evidence: tests, build, lint, manual scenario, screenshot, logs, review.
3. Run fresh verification or inspect fresh evidence.
4. Compare results against acceptance criteria.
5. Record the outcome in the delivery record. Use `references/delivery-record-template.md` and `references/acceptance-checklist.md`.

## Two-axis review

Check both axes separately:

- Spec fit: requested behavior, non-goals, acceptance criteria, no missing work, no scope creep.
- Code fit: architecture/module landing, contracts, tests, maintainability, project conventions, no unapproved shims.

Use a checker/reviewer subagent when available for risky or multi-file changes. If unavailable, perform a fresh self-review pass and record that limitation.

## Delivery record paths

- `docs/track/<feature-name>/delivery-record-v1.md`
- `docs/track/<project-name>/<feature-name>/delivery-record-v1.md`
- Simple work: append `Delivery Record` to the feature/bugfix track note.

## Final decision

- `delivered`: all required acceptance evidence passes.
- `partial`: useful work exists, but accepted scope remains incomplete.
- `blocked`: cannot proceed without external input or failing dependency.
- `needs-user-review`: subjective user, risk, or acceptance decision remains.
- `rolled-back`: implementation was reverted or abandoned with reason.

Do not commit, push, merge, release, or mark done unless project/user convention allows it and verification evidence supports it.

## Related skills

- Previous: use `implementation-execution` when implementation or verification is incomplete.
- Return to `solution-design` when acceptance reveals design/contract drift.
- Return to `requirement-discovery` when acceptance reveals software scope or behavior ambiguity.
