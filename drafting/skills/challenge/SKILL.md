---
name: challenge
description: Stress-test an existing scope, plan, design, draft, review, conclusion, or decision by relentlessly exposing hidden assumptions, fragile dependencies, edge cases, failure modes, and unresolved trade-offs. Use when the user asks to challenge, grill, poke holes in, red-team, pressure-test, adversarially probe, or check for hidden risks before proceeding.
---

# Challenge

Pressure-test an existing object before commitment. Challenge does not create from scratch; it attacks what already exists to expose weakness, ambiguity, and hidden risk.

## Preconditions

A concrete object exists to challenge: scope, brief, plan, design, draft, review, conclusion, decision, or recurring process. If the user cannot name a specific artifact, plan, or decision to examine, do not challenge — guide toward forming a concrete target first.

## Workflow

1. Freeze the object under challenge and name the decision it supports.
2. Choose intensity: quick weakness scan or full adversarial walk-through. Default to quick unless the decision is high-risk or the user asks for depth.
3. Select the most relevant challenge lenses: assumptions, dependencies, trade-offs, edge cases, failure modes, reversibility, evidence quality, decision readiness.
4. Recover facts from materials or the workspace instead of asking when they are inspectable.
5. Resolve upstream decisions before probing dependent branches.
6. For tightly coupled or high-stakes decisions, ask one question at a time and wait for the answer before branching. After 2-3 rounds of single-question probing, summarize and ask whether to continue deeper.
7. Distinguish facts, assumptions, user choices, and unknowns.
8. Surface the weakest points, why they matter, and what would break if they fail.
9. Separate defects, open decisions, acceptable risks, and items needing deeper validation.
10. Recommend one next move: proceed, revise, re-scope, validate, or pause.

## Object-specific emphasis

- Scope/brief: hidden ambiguity, contradictory goals, unverifiable success criteria.
- Plan/design: missing decisions, fragile dependencies, weak trade-offs, failure paths.
- Draft/deliverable: brittle claims, edge cases, weak reasoning, likely reviewer objections.
- Review/audit/conclusion: weak evidence, false confidence, blind spots, unresolved contradictions.
- Acceptance/decision: unproven readiness, missing evidence, underestimated downside.
- Process/execution pattern: repeated friction, diminishing returns, hidden inefficiency, premature optimization.

## Output

Use this structure:

```markdown
# Challenge
## Object under challenge
## Decision at stake
## Strongest assumptions
## Weak points and failure modes
## Dependency and edge-case risks
## Open decisions
## Acceptable risks
## Recommendation
```

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
