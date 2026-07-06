---
name: solution-design
description: Use when clear requirements, a requirements/track note, bug report, or approved discovery needs solution design, trade-offs, deliverable structure, contract-first decisions, implementation slicing, and verification planning.
license: MIT
metadata:
  author: kenpusney
  version: "0.7.0"
---

# Solution Design

Turn approved intent into a designed, executable delivery plan.

## Process

1. Read the requirements doc/track note, `docs/knowledge`, relevant logs, code, tests, and existing conventions.
2. Confirm users, scope, non-goals, requirements, and acceptance are sufficient. If not, return to `requirement-discovery`.
3. If `scope_type: stage`, read the parent's scope-map and non-goals to ensure alignment.
4. Pre-screen feasibility: for each major design choice, assess Feasible / Moderate / Redesigned. If Redesigned, return to `requirement-discovery`.
5. State design principles for this work.
6. Compare 2–3 approaches when choices matter; recommend one with trade-offs.
7. Map deliverable structure before tasks: components, modules, interfaces, dependencies.
8. Challenge the design: over-engineering, technology sprawl, unrealistic targets, excessive scope. Simplify if possible without losing required behavior. Assess each increment's risk level (low / medium / high).
9. Plan verifiable increments. Each must be reviewable and independently verifiable.
10. Write/update the solution and plan in the track folder.

## Plan content

- Goal and source requirements
- Design principles
- Design decisions and rationale (chosen / rejected and why / deferred and under what condition to revisit)
- Deliverable structure / components
- Contract-first changes (interfaces, inputs, outputs)
- Verification methods
- Task increments
- Acceptance mapping
- Risks / rollback

## Planning rules

- Prefer contract-first for boundary changes.
- Each increment must have a defined verification method.
- When increments have dependencies, draw the dependency graph and start from the least-dependent. An increment must not begin until all predecessors pass verification.
- Do not create speculative scaffolding. Do not require issue trackers or ADRs.
- For software deliverables, refer to `../implementation-execution/references/software-mode.md` for E2E/integration seams and test-first guidance.
- Use subagents when helpful; for automation/subagents, design maker/checker roles and stop conditions so the loop can run without guessing.

## Anti-patterns

- Over-engineering: designing for scale that won't be needed.
- Premature optimization: optimizing before verifying the design is correct.
- Skipping the challenge step: accepting the first design without questioning it.

## Related

- Previous: `requirement-discovery` when intent, users, or scope are unclear.
- Next: `implementation-execution` when the plan is executable.
- Return here when implementation changes the design, contracts, or verification.

> <HARD-GATE> Do NOT start implementation until design has passed review-feedback. </HARD-GATE>

See `solution-delivery-loop` for review-feedback resolution protocol.
