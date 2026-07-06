---
name: solution-design
description: Use when clear requirements, a requirements/track note, bug report, or approved discovery needs solution design, trade-offs, deliverable structure, contract-first decisions, implementation slicing, and verification planning.
license: MIT
metadata:
  author: kenpusney
  version: "0.4.0"
---

# Solution Design

Turn approved intent into a designed, executable delivery plan.

## Process

1. Read the requirements doc/track note, `docs/knowledge`, relevant logs, code, tests, and existing conventions.
2. Confirm users, scope, non-goals, requirements, and acceptance are sufficient. If not, return to `requirement-discovery`.
3. State design principles for this work: simplicity, locality, contract stability, UX constraints, risk posture.
4. Compare 2–3 approaches when choices matter; recommend one with trade-offs.
5. Map deliverable structure before tasks: components, sections, modules, interfaces, dependencies.
6. Challenge the design:
   - Check for: over-engineering, technology sprawl, unrealistic targets, missing deployment modes, excessive scope.
   - If the design can be simplified without losing required behavior, simplify.
7. Plan verifiable increments. Each increment must be reviewable and independently verifiable.
8. Write/update the solution and plan in the feature track folder. Use `references/solution-design-template.md` and `references/plan-template.md`.

## Plan content

- Goal and source requirements
- Design principles
- Alternatives and trade-offs
- Deliverable structure / components
- Contract-first changes (interfaces, inputs, outputs)
- Verification methods (how each increment will be checked)
- Task increments
- Acceptance mapping
- Risks / rollback
- Stop conditions

## Planning rules

- Prefer contract-first for boundary changes.
- Plan verifiable increments. Each increment must have a defined verification method.
- Do not create speculative scaffolding.
- Do not require issue trackers or ADRs.
- For software deliverables, refer to `software-mode.md` for E2E/integration seams and test-first guidance.
- Use subagents when helpful; for automation/subagents, design maker/checker roles and stop conditions so the loop can run without guessing.

## Related skills

- Previous: use `requirement-discovery` when intent, users, scope, or acceptance are unclear.
- Next: use `implementation-execution` when the plan is executable.
- Return here when implementation changes the design, contracts, or verification.

## Anti-patterns

- Over-engineering: designing for scale that won't be needed.
- Premature optimization: optimizing before verifying the design is correct.
- Skipping the challenge step: accepting the first design without questioning it.

## After this phase

> <HARD-GATE> Do NOT start implementation until design has passed review-feedback. </HARD-GATE>

Output inspected by `review-feedback` (cumulative with prior phases: Requirements + design + plan). Resolution:
- Fix in place: correct issues, re-review.
- Roll back: return to earliest affected phase (may be `requirement-discovery`), correct there, re-execute forward.

After resolved, `process-distillation` may follow (auto under `full-autonomy`).
