---
name: compliance-gate
description: Assess compliance, constraint fit, disclosures, and override risk for work governed by policy, legal, audit, safety, integrity, or explicit requirements. Use when the user asks whether something is compliant, wants to proceed under exceptions, or needs an auditable constraint decision.
---

# Compliance Gate

Make compliance status explicit and auditable.

## Load

- `references/integrity-protocol.md`
- `../drafting-loop/references/iron-rules.md`
- `../fact-verification/SKILL.md` when claims need source checks

## Dimensions

Check only dimensions relevant to the task:
- scope adherence
- contract/interface compliance
- policy or legal standard
- evidence completeness
- citation/source integrity
- integrity failure modes
- disclosure requirements
- formatting or venue rules
- safety/security constraints

## Override ladder

Track overrides per decision run and compliance dimension.

| Count | Requirement |
|---:|---|
| 1 | Warn user; rationale optional. |
| 2 | Require a rationale string. |
| 3+ | Require rationale of at least 100 characters and explicit confirmation. |

Overrides are append-only. Never delete prior compliance history.

## Workflow

1. Name applicable standards and evidence sources; if standards are unclear, identify the most plausible ones and mark uncertainty.
2. Check each dimension with evidence.
3. Run integrity failure-mode checks when risk is factual, methodological, compliance, safety, or release-related.
4. Classify result: pass, warn, fail, not-applicable, unknown.
5. If the user wants to proceed despite warn/fail, apply the override ladder.
6. Add disclosure language and a proceed/pause/escalate recommendation when required.

## Output

Compliance Gate sections: Standards checked, Results, Failures/warnings, Integrity issues, Override history, Required disclosures, Recommendation.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
