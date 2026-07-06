---
name: delivery-acceptance
description: Use when reviewing completed work, checking whether a feature/bugfix/refactor/deliverable is done, preparing delivery, recording verification evidence, or deciding whether to ship, continue, roll back, or ask for user review.
license: MIT
metadata:
  author: kenpusney
  version: "0.4.0"
---

# Delivery Acceptance

> **Iron Law**: NO DELIVERY CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.

Acceptance is evidence, not confidence.

## Gate

Before any completion claim:

1. Read source requirements: requirements doc, solution/plan, change notes, loop state.
2. Identify required evidence — depends on deliverable type:
   - Code: tests, build output, lint, typecheck, manual QA
   - Report/analysis: source citations, cross-references, factual review
   - Plan/proposal: feasibility check, requirement coverage, risk assessment
   - Investigation: confidence tags, source quality, methodology documentation
3. Run fresh verification or inspect fresh evidence.
4. Compare results against acceptance criteria.
5. Record the outcome in the delivery record. For complex work, use `references/delivery-record-template.md` and `references/acceptance-checklist.md`. For simple work, record as 3–5 bullet points.

## Two-axis review

Check both axes separately, using format-specific criteria from `references/`:

- **Spec fit**: requested requirements, non-goals, acceptance criteria, no missing work, no scope creep.
- **Format fit**: quality standards appropriate to the deliverable type. Load criteria from:
  - `references/format-software.md` for code deliverables
  - `references/format-report.md` for reports, analysis, documentation
  - `references/format-plan.md` for plans, proposals, designs
  - `references/format-investigation.md` for research, investigation findings

Use a checker/reviewer subagent when available for risky or cross-cutting changes. If unavailable, perform a fresh self-review pass and record that limitation.

## Delivery record paths

- `docs/track/<feature-name>/delivery-record-v1.md`
- `docs/track/<project-name>/<feature-name>/delivery-record-v1.md`
- Simple work: append `Delivery Record` to the feature/bugfix track note.

**Delivery record scale**:
- Complex work (multi-slice, cross-cutting, high-risk): use the full `references/delivery-record-template.md`.
- Simple work: 3–5 bullet points covering what changed, what evidence exists, what is deferred or blocked. Append to the track note.

## Final decision

- `delivered`: all required acceptance evidence passes.
- `partial`: useful work exists, but accepted scope remains incomplete.
- `blocked`: cannot proceed without external input or failing dependency.
- `needs-user-review`: subjective user, risk, or acceptance decision remains.
- `rolled-back`: implementation was reverted or abandoned with reason.

Do not commit, push, merge, release, or mark done unless project/user convention allows it and verification evidence supports it.

## Related skills

- Previous: use `implementation-execution` when implementation or verification is incomplete.
- Return to `solution-design` when acceptance reveals design/contract drift.
- Return to `requirement-discovery` when acceptance reveals scope or behavior ambiguity.

## Anti-patterns

- Expressing satisfaction before verification ("Great!", "Perfect!", "Done!").
- Accepting based on confidence rather than fresh evidence.
- Skipping change note checks for drifted scope or design.
- Using the full delivery record template when 3-5 bullet points suffice.

## After this phase

Output inspected by `review-feedback` (cumulative with all prior phases). Resolution:
- Fix in place: correct issues, re-review.
- Roll back: return to earliest affected phase, correct there, re-execute forward.

After resolved, `process-distillation` may follow (auto under `full-autonomy`).
