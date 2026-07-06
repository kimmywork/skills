# Acceptance Checklist

Use before claiming work is complete.

## Spec Fit

- [ ] Source PRD/track/plan was re-read.
- [ ] Every acceptance criterion has pass/fail/partial/skipped status.
- [ ] Non-goals were not implemented accidentally.
- [ ] No unapproved user-facing behavior was added.
- [ ] Open questions are resolved or marked as blocking/follow-up.
- [ ] Change notes exist for any drift from original scope, design, acceptance, contract, data model, or verification. Template: `software-delivery-loop/references/change-note-template.md`.

## Code Fit

- [ ] Code landed in planned modules/paths or change note explains why.
- [ ] Contract/data/schema/API/UI/storage changes are documented.
- [ ] No unapproved compatibility shim, fallback, deprecated alias, or dual path remains.
- [ ] Tests or manual checks exercise the changed behavior.
- [ ] Project conventions and existing patterns were followed.

## Evidence

- [ ] Verification command/manual scenario was run fresh.
- [ ] Output was read, not assumed.
- [ ] Failures/warnings are recorded.
- [ ] Delivery record contains evidence.

## Decision

- [ ] Final status is one of: delivered, partial, blocked, needs-user-review, rolled-back.
