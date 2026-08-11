# Software Mode

Use when the deliverable is code. Overrides the generic execution loop with TDD-driven verification.

## Execution loop (overrides generic steps 2-4)

For each slice:

1. Define expected behavior and verification evidence.
2. Prefer TDD: write/adjust the test, watch it fail, implement minimal code, watch it pass.
3. For user flows, prefer E2E or integration-driven verification at the highest reliable seam.
4. Refactor only after green; keep behavior stable.
5. Run relevant verification (build, test, lint, typecheck).
6. Review for spec fit and architecture fit.
7. Update track docs, loop state, logs, or delivery record with evidence and deltas.

## Change control signals (supplements generic signals)

- A test expectation changes because behavior differs from the plan, not because the test is wrong.
- You need to add a field, column, parameter, route, or component not in the plan.
- Approved architecture, contract, data model, or module landing changes.

## Subagent roles

- maker: implement the slice
- checker/reviewer: verify spec fit and code fit