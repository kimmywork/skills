---
name: audit-trail
description: Execute evaluation work as the deliverable: audits, reviews, compliance checks, contract checks, PR/design assessments, evidence inspections, and rubric-based assessment of existing artifacts. Use during Build for Evaluating kind.
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
2. Divide large artifacts into sections or review units.
3. Extract claims that need verification or calculation.
4. Verify claims and convert refuted/inconclusive claims into issues.
5. Inspect each section for requested issue types and root-cause links.
6. Record location, evidence, impact, and recommended action for every finding.
7. Distinguish defects, risks, suggestions, and questions.
8. Produce a verdict only for the approved scope.
9. Hand off to quality-review for meta-review if high-stakes.

## Finding schema

Use `references/audit-state-schema.md` for sections, claims, and issues.

## Output

Audit Report sections: Scope and criteria, Method, Sections, Claims, Findings, Evidence matrix, Verdict, Limitations.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
