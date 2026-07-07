---
name: guided-inquiry
description: Socratic clarification for vague, high-stakes, exploratory, creative, or poorly bounded work. Use when the user needs help thinking, cannot define the target, or Shape would otherwise invent requirements.
---

# Guided Inquiry

Use dialogue to converge on a usable scope without over-questioning.

## Five layers

1. **Outcome**: What decision, artifact, or understanding should exist after this?
2. **Audience/use**: Who uses it and in what situation?
3. **Boundaries**: What is in, out, constrained, risky, or sensitive?
4. **Evidence/style**: What inputs, references, standards, or examples matter?
5. **Done**: How will the user know it succeeded?

## Rules

- Ask at most 3 questions per turn.
- Prefer multiple-choice options when the user is stuck.
- Do not force all five layers if the scope becomes clear early.
- After 5 rounds without convergence, propose 3 candidate scopes and ask the user to choose.
- Capture assumptions explicitly; do not bury them in prose.

## Output

When ready, produce a compact Shape handoff:

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

Then hand off to `../scope-shaping/SKILL.md` or directly to `../blueprinting/SKILL.md` if scope is already complete.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
