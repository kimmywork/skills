---
name: cross-validation
description: Obtain a second perspective on a claim, design, review, or conclusion to reduce blind spots and resolve uncertainty. Use when the user wants an independent check, adversarial review, multiple perspectives, or more confidence before acting.
---

# Cross Validation

Use another perspective to reduce blind spots. Advisory feedback does not block by itself.

## Load

- `references/cross-validation-protocol.md`
- `../drafting-loop/references/ground-truth-isolation.md`
- `../quality-review/SKILL.md`

## When to use

- High-stakes factual, compliance, safety, or architecture decisions.
- Conflicting evidence.
- User requests second opinion.
- A review or conclusion is technically acceptable but still uncertain.

## Workflow

1. Freeze the artifact, decision, or conclusion under question.
2. Select validation mode and perspectives from `references/cross-validation-protocol.md`.
3. Keep each perspective focused on evidence-backed findings.
4. Compare consensus, divergence, unique findings, false positives, and unresolved risks.
5. Recommend action; do not silently average conflicting judgments.

## If no separate model or reviewer exists

Run a self-adversarial pass in a fresh section:
- hide prior recommendations while listing possible failure modes;
- inspect evidence again;
- record that validation was not truly independent.

## Output

```markdown
# Cross Validation
## Setup
## Consensus findings
## Divergences
## Unique findings
## Unresolved risks
## Recommendation
## Independence limitations
```

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
