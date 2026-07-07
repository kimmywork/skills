---
name: quality-review
description: Independent quality review for any draft deliverable before acceptance. Use after Build, after revisions, for review feedback, quality gates, adversarial checks, rollback routing, and deciding whether work needs revision before delivery.
---

# Quality Review

Review the deliverable against scope, prior artifacts, and evidence.

## Load

- `references/feedback-template.md`
- `references/issue-taxonomy.md`
- `references/review-routing.md`
- `references/two-stage-review.md` for high-stakes or revision-heavy work
- `../drafting-loop/references/ground-truth-isolation.md`
- `../drafting-loop/references/iron-rules.md`

## Workflow

1. Freeze the deliverable under review.
2. Load current artifact, source scope, blueprint, prior feedback, and relevant criteria.
3. Review cumulatively: current output plus prior phase obligations.
4. For multi-part deliverables, run Accuracy, Validity, and Consistency passes.
5. Tag each issue with origin phase, severity, type, evidence, suggested fix, and resolution.
6. Route fix-in-place issues to producer; route rollback issues to earliest affected phase.
7. Use two-stage review for high-stakes work or substantial revisions.
8. Set verdict: PASS, CONDITIONAL, REVISION, FAIL, or STABLE.

## Kind-specific checks

- Crafting: correctness, tests, integration, maintainability, regressions, contract fit.
- Composing: factuality, structure, audience fit, completeness, clarity.
- Evaluating: evidence chain, severity calibration, scope adherence.
- Investigating: source quality, confidence labels, contradictions, gaps.
- Creating: brief fit, coherence, originality, constraints, impact.

## Ground-truth rule

If you built the deliverable, create a separate review section. Do not edit while reviewing. Revise only after the review report exists.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
