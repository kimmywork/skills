---
name: acceptance-gate
description: Evidence-based delivery acceptance for any completed work. Use when deciding whether to ship, hand off, close a task, record verification, accept conditional delivery, roll back, or ask the user for final review.
---

# Acceptance Gate

Acceptance is a record of evidence, not a feeling that work is done.

## Load

- `references/acceptance-checklist.md`
- `references/delivery-record-template.md`
- Format reference: `references/format-software.md`, `references/format-report.md`, `references/format-plan.md`, or `references/format-investigation.md`
- `../drafting-loop/references/iron-rules.md`

## Preconditions

- Build output exists.
- Quality review is PASS or CONDITIONAL, or user explicitly requests acceptance of risk.
- Verification evidence is fresh enough for the claim being made.

## Workflow

1. Enumerate acceptance criteria.
2. Check spec fit and relevant format fit.
3. Map each criterion to evidence.
4. Mark status: pass, fail, deferred, blocked, not-applicable.
5. Check scope changes, contract drift, review routing, and unresolved risks.
6. Decide verdict: delivered, partial, blocked, needs-review, or rolled-back.
7. Write a delivery record.
8. Ask for user approval when verdict is partial, risky, subjective, or requires override.

## Rules

Do not commit, push, release, mark done, or imply completion unless project/user convention allows it and evidence supports it.

## Output

Use `references/delivery-record-template.md`. End with next action: stop, continue next increment, revise, or escalate.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
