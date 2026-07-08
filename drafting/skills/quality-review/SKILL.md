---
name: quality-review
description: Independent review of an existing draft, build, or deliverable to find issues, judge readiness, and guide revision. Use when the user wants feedback, a quality gate, an adversarial pass, or a "is this good enough?" check; prefer formal audit work when the review itself must be the deliverable, and acceptance work when the main question is whether it can be shipped or closed.
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
2. Load the current artifact, relevant criteria, source scope/brief, prior feedback, and known constraints. If criteria are missing, establish a temporary review lens and label it as inferred.
3. Choose review depth: quick, full, adversarial, or regression.
4. Review cumulatively: current output plus prior obligations that define what good looks like.
5. For multi-part deliverables, run Accuracy, Validity, and Consistency passes.
6. Tag each issue with origin stage, severity, type, evidence, suggested fix, and resolution path.
7. Distinguish fix-in-place issues from earlier-stage issues; point back to the earliest affected stage when needed.
8. Use two-stage review for high-stakes work or substantial revisions.
9. Set verdict: PASS, CONDITIONAL, REVISION, FAIL, or STABLE.

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
