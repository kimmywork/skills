---
name: guided-inquiry
description: Use dialogue to surface the real target, narrow competing directions, and frame hard decisions when the user cannot yet state what they want clearly enough to scope, plan, or execute.
---

# Guided Inquiry

Use dialogue to converge on a workable target, decision, or brief when the user needs thinking help before formal scoping.

## Five layers

1. **Outcome**: What decision, artifact, or understanding should exist after this?
2. **Audience/use**: Who uses it and in what situation?
3. **Boundaries**: What is in, out, constrained, risky, or sensitive?
4. **Evidence/style**: What inputs, references, standards, or examples matter?
5. **Done**: How will the user know it succeeded?

## Rules

- Ask at most 3 questions per turn.
- If a blocking fact can be recovered from materials or the workspace, inspect it instead of asking.
- Prefer multiple-choice options when the user is stuck.
- Do not force all five layers if the target becomes clear early.
- Resolve upstream decisions before exploring dependent branches.
- For tightly coupled or high-stakes decisions, ask one question at a time and resolve dependencies before branching further.
- If the user is choosing among directions, compare options instead of continuing pure questioning.
- Do not turn tentative discussion into scope, planning, or execution until the target is stable enough for shared understanding.
- After 5 rounds without convergence, propose 3 candidate directions and ask the user to choose.
- Capture assumptions explicitly; do not bury them in prose.

## Output

When ready, produce one of: a clarified objective, candidate directions, or a compact scope seed.

```yaml
guided_scope:
  kind: <kind>
  goal: <outcome>
  audience: []
  in_scope: []
  out_of_scope: []
  constraints: []
  success_criteria: []
  assumptions: []
  open_questions: []
```

The result should be ready for shaping, planning, or direct execution, depending on completeness.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
