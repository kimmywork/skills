# Drafting Bundle Improvement Plan

Status: applied
Date: 2026-07-07

## Goals

1. Preserve the v2 universal work-loop structure while restoring delivery-grade operational depth.
2. Keep every `SKILL.md` short, agent-facing, and under 100 lines.
3. Move detailed procedures into in-bundle references only.
4. Avoid references to external bundles; distill reference-skill patterns locally.

## Work packages

### WP1 — Delivery coverage restoration

- Add state machine, legal transitions, material dependencies, transition reinforcement, and stronger track structure.
- Restore parent/stage track semantics and parser commands: extract, index, validate, children, kanban.
- Restore requirement syntax: User Story, EARS, Given/When/Then, splitting, overlap checks.
- Restore software execution mode: TDD, E2E/integration seams, contract-change inventory, blocker handling.
- Restore acceptance format rubrics for software, reports, plans, and investigations.

### WP2 — Review and rollback routing

- Add issue taxonomy with origin phase, severity, type, evidence, suggested fix, and resolution.
- Add cumulative review protocol and fix-in-place vs rollback routing.
- Add multi-pass review: Accuracy, Validity, Consistency.

### WP3 — Reference-skill absorption

- Add audit state schemas inspired by structured document review: sections, claims, issues, root-cause linkage.
- Add claim verification protocol: extraction, source tracing, cross-reference, verdict taxonomy.
- Add source quality hierarchy and methodology patterns for deep research.
- Add integrity/compliance protocol for failure modes and override handling.

### WP4 — Style-calibration completion

- Fully absorb style-extraction workflow into style-calibration.
- Add computational stylistics, 8-step extraction, output template, Chinese-specific rules, and calibration protocol.
- Keep `SKILL.md` concise and move details to references.

## Verification

- `SKILL.md` files remain under 100 lines.
- Durable skill artifacts are English-only.
- All referenced files exist inside the drafting bundle.
- Plugin JSON remains parseable.
- Track parser help and commands run.
