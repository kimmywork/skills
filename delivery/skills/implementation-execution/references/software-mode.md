# Software Mode

Use when the deliverable is code. Overrides the generic execution loop with a layered quality gate for verification.

## Execution loop (overrides generic steps 2-4)

For each slice:

1. Define expected behavior and verification evidence.
2. Establish the quality gate for the slice: the automated checks that must pass before it is done.
3. Implement the slice, pinning behavior with multi-level automated tests — unit, integration, and E2E at the highest reliable seam for user flows.
4. Refactor only while the current quality gate passes; keep behavior stable.
5. Run the full quality gate: build, multi-level automated tests, static analysis, linter, style check, type check.
6. Review for spec fit and architecture fit.
7. Update track docs, loop state, logs, or delivery record with evidence and deltas.

## Change control signals (supplements generic signals)

- A test expectation changes because behavior differs from the plan, not because the test is wrong.
- You need to add a field, column, parameter, route, or component not in the plan.
- Approved architecture, contract, data model, or module landing changes.

## Subagent roles

- maker: implement the slice
- checker/reviewer: verify spec fit and code fit