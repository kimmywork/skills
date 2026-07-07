---
name: compliance-gate
description: Compliance and override gate for work with standards, policy, legal, audit, safety, integrity, or explicit constraints. Use for evaluating kind, compliance checks, repeated user overrides, disclosure requirements, and append-only decision history.
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

Track overrides per loop run and compliance dimension.

| Count | Requirement |
|---:|---|
| 1 | Warn user; rationale optional. |
| 2 | Require a rationale string. |
| 3+ | Require rationale of at least 100 characters and explicit confirmation. |

Overrides are append-only. Never delete prior compliance history.

## Workflow

1. Name applicable standards and evidence sources.
2. Check each dimension with evidence.
3. Run integrity failure-mode checks when risk is factual, methodological, compliance, safety, or release-related.
4. Classify result: pass, warn, fail, not-applicable, unknown.
5. If user wants to proceed despite warn/fail, apply override ladder.
6. Add disclosure language when required.

## Output

Compliance Gate sections: Standards checked, Results, Failures/warnings, Integrity issues, Override history, Required disclosures, Recommendation.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
