---
name: distillation
description: Convert repeated execution friction, review feedback, coverage gaps, false guidance, missing guardrails, trigger errors, or successful reusable patterns into process, template, or skill improvements. Use after phase-review cycles, process audits, delivery, or repeated loops.
---

# Distillation

Improve the framework only from concrete evidence.

## Load

- `references/distillation-template.md`
- `../drafting-loop/references/phase-review-and-process-audit.md`
- `../drafting-loop/references/failure-paths.md`
- `../drafting-loop/references/anti-patterns.md`

## Triggers

- Same review issue repeats.
- A phase-review rollback exposes missing guidance.
- A process audit finds a coverage gap, false guidance, missing guardrail, repeated improvisation, context overhead, trigger misfire, or atomic extraction candidate.
- A template was missing or misleading.
- User feedback reveals reusable process friction.

## Workflow

1. Collect evidence from the run: artifacts, review issues, fixes, decisions, and user feedback.
2. Classify the gap using `references/distillation-template.md` dimensions.
3. Identify the general pattern; ignore one-off weak signals.
4. Decide whether to change a skill, reference, template, script, routing description, propose a new skill, or make no change.
5. Check duplication and bundle scope.
6. Draft the smallest durable improvement.
7. Verify cross-references, language, and SKILL.md line limit.
8. Record why the improvement should help future runs.

## Output

Use `references/distillation-template.md`.

Do not add process weight unless it prevents real recurring failure or improves reusable execution.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
