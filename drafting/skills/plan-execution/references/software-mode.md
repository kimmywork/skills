# Software Mode

Use when the deliverable is code, configuration, migration, infrastructure, or automation.

## Execution loop

For each slice:
1. Define expected behavior and evidence.
2. Prefer TDD when practical: write or adjust a test, observe failure, implement minimal code, observe pass.
3. For user flows, prefer E2E or integration checks at the highest reliable seam.
4. Refactor only after green; keep behavior stable.
5. Run relevant verification: tests, build, lint, typecheck, smoke check, or manual QA.
6. Review for spec fit and architecture fit.
7. Record commands, outputs, failures, and limitations.

## Contract changes

When changing an existing interface:
1. Inventory dependents.
2. Choose break-fix, deprecate-remove, adapter, or postpone.
3. Update all affected references.
4. Verify consumers.
5. Record the change and rollback path.

## Blocker record

```markdown
## Blocker
- Problem:
- Impact:
- Options:
- Recommended path:
- User decision needed:
```
