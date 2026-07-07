---
name: intent-routing
description: Detect work kind, current phase, and correct workflow when user intent or provided materials span multiple phases. Use before drafting-loop proceeds if the user provides mixed artifacts, vague requests, unclear goals, or asks for routing, workflow selection, resume, or direct dispatch.
---

# Intent Routing

Resolve ambiguity before substantive work begins.

## Load when needed

- `../drafting-loop/references/handoff-schemas.md`
- `../drafting-loop/references/mode-spectrum.md`

## Detection

1. Extract action verbs and object.
2. Classify primary kind:
   - build, fix, implement, configure -> Crafting
   - write, draft, summarize, compose -> Composing
   - review, audit, assess, check -> Evaluating
   - research, investigate, trace, analyze, map -> Investigating
   - ideate, imagine, create a story/brand/concept -> Creating
3. Detect phase of materials:
   - vague idea -> Sense/Clarify
   - requirements, brief, research question -> Shape
   - architecture, outline, method -> Design
   - draft, code, findings -> Build
   - comments, tests, review notes -> Verify
   - delivery record, acceptance notes -> Record
4. Detect conflicts: multiple kinds, multiple phases, missing goal, or ambiguous "create".

## Direct-mode

If the prompt starts with `[direct-mode]`, strip it and route directly to the requested skill/phase. Still warn if safety, compliance, or destructive action risk exists.

## Clarification prompt

Use this shape:

```text
I see <materials>. Which workflow do you want?
(a) Full loop from current materials to verified delivery
(b) Resume at <phase> to <goal>
(c) Review/evaluate the provided artifact
(d) Something else: describe the target
```

Ask the fewest questions needed. If the user is blocked, offer a recommendation.

## Output

Return:

```yaml
routing_decision:
  kind: <kind|mixed>
  phase: <entry phase>
  confidence: high|medium|low
  recommended_skill: <skill>
  mode: Fidelity|Balanced|Originality
  needs_user_choice: true|false
  questions: []
```

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
