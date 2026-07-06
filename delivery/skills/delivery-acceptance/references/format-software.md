# Format Fit: Software Deliverables

Use when reviewing code deliverables. Check against these criteria in addition to Spec Fit.

## Architecture / Module Landing

- [ ] Code landed in planned modules/paths or change note explains why.
- [ ] Contract/data/schema/API/UI/storage changes are documented.
- [ ] No unapproved compatibility shim, fallback, deprecated alias, or dual path remains.
- [ ] Project conventions and existing patterns were followed.

## Verification

- [ ] Tests or automated checks exercise the changed behavior.
- [ ] Build, lint, typecheck pass.
- [ ] Manual verification evidence is recorded where automation is impractical.

## Maintainability

- [ ] No speculative scaffolding or dead code.
- [ ] Dependencies are appropriate and necessary.
- [ ] Error handling is consistent with project patterns.