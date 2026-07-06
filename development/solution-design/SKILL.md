---
name: solution-design
description: Use when clear software requirements, a PRD, track note, bug report, or approved discovery needs solution design, trade-offs, architecture/module landing, contract-first decisions, implementation slicing, and verification planning.
license: MIT
metadata:
  author: kenpusney
  version: "0.2.0"
---

# Solution Design

Turn approved intent into a designed, executable delivery plan.

## Process

1. Read the PRD/track note, `docs/knowledge`, relevant logs, code, tests, and existing conventions.
2. Confirm users, scope, non-goals, requirements, and acceptance are sufficient. If not, return to `requirement-discovery`.
3. State design principles for this work: simplicity, locality, contract stability, UX constraints, risk posture.
4. Compare 2–3 approaches when choices matter; recommend one with trade-offs.
5. Map architecture/module landing before tasks: files, packages, contracts, schemas, routes, UI surfaces, tests.
6. Challenge the design:
   - Check for: over-engineering, technology sprawl, unrealistic targets, missing deployment modes, excessive scope.
   - If the design can be simplified without losing required behavior, simplify.
7. Plan vertical slices. Each slice must be reviewable and independently verifiable.
8. Write/update the solution and plan in the feature track folder. Use `references/solution-design-template.md` and `references/plan-template.md`.

## Plan content

- Goal and source requirements
- Design principles
- Alternatives and trade-offs
- Architecture / module landing
- Contract-first changes: schemas, interfaces, routes, storage, CLI, UI contracts
- Test strategy: unit, integration, E2E, manual where needed
- Task slices
- Acceptance mapping
- Verification commands
- Risks / rollback
- Stop conditions

## Planning rules

- Prefer contract-first for boundary changes.
- Prefer E2E or integration seams for user flows.
- Prefer test-first for behavior changes; if impractical, define verification before editing.
- Do not create speculative scaffolding.
- Do not require issue trackers or ADRs.
- Use subagents when helpful; for automation/subagents, design maker/checker roles and stop conditions so the loop can run without guessing.

## Related skills

- Previous: use `requirement-discovery` when intent, users, scope, or acceptance are unclear.
- Next: use `implementation-execution` when the plan is executable.
- Return here when implementation changes architecture, contracts, or verification.

## After this phase

Output inspected by `review-feedback` (cumulative with prior phases: PRD + design + plan). Resolution:
- Fix in place: correct issues, re-review.
- Roll back: return to earliest affected phase (may be `requirement-discovery`), correct there, re-execute forward.

After resolved, `process-distillation` may follow (auto under `full-autonomy`).
