# Delivery SKILL.md Coverage Matrix

Status: active source-to-target verification
Date: 2026-07-07

This matrix compares each `delivery/skills/*/SKILL.md` body against its drafting counterpart. It tracks SKILL-level semantics, not just reference-file coverage.

| Delivery SKILL.md | Drafting target | Coverage | Missing / moved semantics | Fix status |
|---|---|---:|---|---|
| `solution-delivery-loop` | `drafting-loop` | Covered | loop phases, review gates, track docs, first move, autonomy, continuity covered | `loop-operations.md` added |
| `requirement-discovery` | `scope-shaping` | Covered | material scan, intent shaping, challenge pass, approach options, output scale, syntax, splitting covered | `discovery-process.md` added |
| `solution-design` | `blueprinting` | Covered | feasibility, contracts, increments covered; parent scope-map alignment in references | No immediate gap |
| `implementation-execution` | `plan-execution` | Covered | before-editing scan, parent stage consistency, scope-map updates, stop conditions, blocker handling, detailed change-control signals covered | `execution-control.md` added |
| `review-feedback` | `quality-review` | Covered | cumulative review, issue tags, fix/rollback routing, multi-pass review covered | No immediate gap |
| `delivery-acceptance` | `acceptance-gate` | Covered | gate, two-axis review, verdicts, delivery record, no release claim without evidence covered | No immediate gap |
| `structured-investigation` | `deep-research` | Covered | core workflow, raw-material preservation, interaction checkpoints, quick mode, confidence, source trace covered | investigation workflow extended |
| `process-distillation` | `distillation` | Covered | gap dimensions covered; rename checklist intentionally deferred; subagent roles omitted for agent-neutrality | No immediate gap |

## Required fixes from this pass

All required fixes from this pass have been applied:

1. Added `plan-execution/references/execution-control.md` and updated `plan-execution/SKILL.md`.
2. Added `scope-shaping/references/discovery-process.md` and updated `scope-shaping/SKILL.md`.
3. Extended `deep-research/references/investigation-workflow.md` with raw material preservation and interaction checkpoints.
4. Added `drafting-loop/references/loop-operations.md` and updated `drafting-loop/SKILL.md`.

## Intentional omissions

- Subagent roles from delivery skills: omitted to preserve agent-neutral framework.
- Rename-specific checklist: deferred unless rename failures recur.
- `.agents/loop-state.md` exact path: generalized into track/loop state references rather than copied exactly.
