---
name: audit-trail
description: Produce a formal audit or assessment report on an existing artifact using stated or inferred criteria, evidence tracing, and scoped findings. Use when the review itself is the deliverable; prefer revision-oriented review when the main goal is to improve a draft, and final acceptance work when the main goal is ship/close decisions.
---

# Audit Trail

Run an evaluation with traceable evidence.

## Load

- `references/audit-state-schema.md`
- `../drafting-loop/references/ground-truth-isolation.md`
- `../fact-verification/SKILL.md` for factual claims
- `../compliance-gate/SKILL.md` when compliance or override rules apply

## Workflow

1. Identify artifact, scope, criteria, and severity definitions.
2. If criteria are missing or incomplete, infer a provisional review frame and label what was user-supplied versus inferred.
3. Divide large artifacts into sections or review units.
4. Extract claims that need verification or calculation.
5. Verify claims and convert refuted/inconclusive claims into issues.
6. Inspect each section for requested issue types and root-cause links.
7. Record location, evidence, impact, and recommended action for every finding.
8. Distinguish defects, risks, suggestions, questions, and unaudited areas.
9. Produce a verdict only for the approved scope.
10. Note whether further validation, compliance checking, or delivery decision work is still needed.

## Finding schema

Use `references/audit-state-schema.md` for sections, claims, and issues.

## Output

Audit Report sections: Scope and criteria, Method, Sections, Claims, Findings, Evidence matrix, Verdict, Limitations.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
