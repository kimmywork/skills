---
name: triage
description: Diagnose the right workflow, stage, or resume point when the user has mixed artifacts, an unclear next step, or needs help choosing how to proceed. Use when the main problem is path selection, not target definition or task execution.
---

# Triage

Diagnose the task before committing to a path.

## Load when needed

- `../drafting-loop/references/handoff-schemas.md`
- `../drafting-loop/references/mode-spectrum.md`

## Detection

1. Extract the requested outcome, not just the verbs.
2. Classify the primary task type:
   - build, fix, implement, configure -> Crafting
   - write, draft, summarize, compose -> Composing
   - review, audit, assess, check -> Evaluating
   - research, investigate, trace, analyze, map -> Investigating
   - ideate, imagine, create a story/brand/concept -> Creating
3. Estimate material maturity:
   - vague idea -> Sense/Clarify
   - requirements, brief, research question -> Shape
   - architecture, outline, method -> Design
   - draft, code, findings -> Build
   - comments, tests, review notes -> Verify
   - delivery record, acceptance notes -> Record
4. Detect conflicts: multiple plausible task types, mixed-stage materials, missing target, or ambiguous "create".
5. Decide whether the user mainly needs workflow selection, stage selection, task-type selection, or resume guidance. If the real problem is target formation rather than path choice, say so.

## Guidance

- If one path is clearly best, recommend it and say why.
- If 2-3 paths are plausible, present them with the trade-off of each.
- Ask the fewest questions needed. If the user is blocked, make a recommendation instead of reflecting the ambiguity back unchanged.
- Recommend a broader end-to-end loop only when the user wants managed progression across stages.

## Clarification prompt

Use this shape when a short decision prompt is necessary:

```text
I see <materials>. The most likely paths are:
(a) <path 1>
(b) <path 2>
(c) <path 3, if needed>
Which target do you want?
```

## Output

Return a compact routing note with:
- interpreted goal
- primary task type
- current material stage
- confidence
- recommended path
- missing prerequisites or blocking questions
- practical next step phrased as a stage or task type, not a skill name

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
