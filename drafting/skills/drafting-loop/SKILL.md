---
name: drafting-loop
description: Orchestrate complex multi-step knowledge work from unclear intent through verified delivery. Use when the user wants end-to-end management across clarification, planning, execution, review, and acceptance, especially when they do not want to choose the next step themselves.
---

# Drafting Loop

Use this as the top-level control layer when the user wants managed progress across multiple stages. It coordinates skills; direct entry into a leaf skill is still valid when the immediate task is already clear.

## Load first

- `references/iron-rules.md`
- `references/state-machine.md`
- `references/checkpoint-protocol.md`
- `references/handoff-schemas.md`
- `references/mode-spectrum.md`
- `references/phase-review-and-process-audit.md`
- `references/loop-operations.md`
- `references/multi-stage-tracks.md` for split or multi-deliverable work
- `references/resume-ledger.md` for long-running or paused work
- `references/transition-reinforcement.md` for long work
- `references/failure-paths.md` when blocked or looping

## Phases

Sense -> Clarify -> Shape -> Design -> Build -> Verify -> Record -> Continue/Stop.

1. **Sense**: detect work kind, materials, current phase, risks, and whether the user needs a single task or a managed loop.
2. **Clarify**: use `../triage/SKILL.md` only when the path, resume point, or workflow choice is genuinely ambiguous.
3. **Shape**: use `../scope-shaping/SKILL.md` unless a complete scope already exists.
4. **Design**: use `../blueprinting/SKILL.md` when execution needs a plan; fast-pass only when recorded.
5. **Build**: use `../plan-execution/SKILL.md`, `../deep-research/SKILL.md`, `../audit-trail/SKILL.md`, or `../style-calibration/SKILL.md` according to kind.
6. **Verify**: use `../inspect/SKILL.md`; add `../fact-verification/SKILL.md`, `../compliance-gate/SKILL.md`, or `../cross-validation/SKILL.md` when relevant.
7. **Record**: use `../acceptance-gate/SKILL.md`.
8. **Continue/Stop**: use `../distillation/SKILL.md` when repeated friction or process learning appears.

## Work kinds

- **Crafting**: build/fix/implement/configure systems or artifacts.
- **Composing**: write/synthesize documents, reports, docs, proposals, slides.
- **Evaluating**: review/audit/check/assess existing work.
- **Investigating**: research/trace/analyze/map/root-cause questions.
- **Creating**: ideate/imagine/design fiction, brands, concepts, experiences.

For mixed work, choose the primary kind and record secondary tracks. For broad or multi-deliverable work, use `references/multi-stage-tracks.md`.

## Skip table

| Kind | Shape | Design | Build |
|---|---|---|---|
| Crafting | required | required | required |
| Composing | required | lightweight allowed | required |
| Evaluating | lightweight allowed | skip allowed | audit execution |
| Investigating | required | skip allowed | research execution |
| Creating | lightweight allowed | skip allowed | creative execution |

Sense, Clarify, Verify, Record, and Continue/Stop are always represented, even if compact.

## Checkpoint rules

- Present a FULL checkpoint after Sense on non-trivial work and before major transitions.
- Use MANDATORY checkpoints for scope changes, blueprint approval, review verdicts, acceptance, or compliance overrides.
- Do not continue past a MANDATORY checkpoint without explicit user direction.
- If user says "just continue", use SLIM checkpoints for non-critical phases but restore FULL after 4 continues or any risk.

## State and output

For multi-turn work, create or update a track using `references/track-document-structure.md`.
Every phase handoff must include status, deliverables, evidence state, changes, and next action. Every phase output must pass the phase-review protocol before advancing.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
