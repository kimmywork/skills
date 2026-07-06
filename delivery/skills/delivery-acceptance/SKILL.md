---
name: delivery-acceptance
description: Use when reviewing completed work, checking whether a feature/bugfix/refactor/deliverable is done, preparing delivery, recording verification evidence, or deciding whether to ship, continue, roll back, or ask for user review.
license: MIT
metadata:
  author: kenpusney
  version: "0.6.0"
---

# Delivery Acceptance

> **Iron Law**: NO DELIVERY CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.

Acceptance is evidence, not confidence.

## Gate

Before any completion claim:

1. Read source requirements: requirements doc, solution/plan, change notes, loop state.
2. If `scope_type: parent`, verify all stages in scope-map are "done" before claiming parent delivered.
3. Identify required evidence — depends on deliverable type:
   - Code: tests, build output, lint, typecheck, manual QA
   - Report/analysis: source citations, cross-references, factual review
   - Plan/proposal: feasibility check, requirement coverage, risk assessment
   - Investigation: confidence tags, source quality, methodology documentation
4. Run fresh verification or inspect fresh evidence.
5. Compare results against acceptance criteria.
6. Record the outcome in the delivery record. For complex work, use `references/delivery-record-template.md` and `references/acceptance-checklist.md`. For simple work, record as 3–5 bullet points.

## Two-axis review

Check both axes separately, using format-specific criteria from `references/`:

- **Spec fit**: requested requirements, non-goals, acceptance criteria, no missing work, no scope creep.
- **Format fit**: quality standards appropriate to the deliverable type. Load criteria from:
  - `references/format-software.md` for code deliverables
  - `references/format-report.md` for reports, analysis, documentation
  - `references/format-plan.md` for plans, proposals, designs
  - `references/format-investigation.md` for research, investigation findings

Use a checker/reviewer subagent when available for risky or cross-cutting changes. If unavailable, perform a fresh self-review pass and record that limitation.

## Delivery record

- Path: `delivery-record-v1.md` in the track folder (see `../solution-delivery-loop/references/track-document-structure.md` for paths).
- Complex work: use `references/delivery-record-template.md`.
- Simple work: 3–5 bullet points appended to the track note.

## Final decision

- `delivered`: all required acceptance evidence passes.
- `partial`: useful work exists, but accepted scope remains incomplete.
- `blocked`: cannot proceed without external input or failing dependency.
- `needs-user-review`: subjective user, risk, or acceptance decision remains.
- `rolled-back`: implementation was reverted or abandoned with reason.

Do not commit, push, merge, release, or mark done unless project/user convention allows it and verification evidence supports it.

## Anti-patterns

- Expressing satisfaction before verification ("Great!", "Perfect!", "Done!").
- Accepting based on confidence rather than fresh evidence.
- Skipping change note checks for drifted scope or design.
- Using the full delivery record template when 3-5 bullet points suffice.

## Related

- Previous: `implementation-execution` when implementation is incomplete.
- Return to `solution-design` when acceptance reveals design/contract drift.
- Return to `requirement-discovery` when acceptance reveals scope ambiguity.

See `solution-delivery-loop` for review-feedback resolution protocol.
