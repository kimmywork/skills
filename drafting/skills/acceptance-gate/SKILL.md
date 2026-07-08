---
name: acceptance-gate
description: "Make an evidence-based delivery decision for completed or near-complete work: delivered, partial, blocked, needs-review, or rolled-back. Use when the user wants to know whether work can be shipped, handed off, closed, or accepted; if the main need is issue-finding or formal assessment, do that first."
---

# Acceptance Gate

Acceptance is a record of evidence, not a feeling that work is done.

## Load

- `references/acceptance-checklist.md`
- `references/delivery-record-template.md`
- Format reference: `references/format-software.md`, `references/format-report.md`, `references/format-plan.md`, or `references/format-investigation.md`
- `../drafting-loop/references/iron-rules.md`

## Preconditions

- A build, draft, report, review result, or other candidate deliverable exists.
- Evidence may be complete or incomplete, but missing review or missing evidence must be recorded as a blocker or conditional risk rather than waved away.

## Workflow

1. Enumerate acceptance criteria.
2. Check spec fit and relevant format fit.
3. Map each criterion to evidence.
4. Mark status: pass, fail, deferred, blocked, not-applicable.
5. Check scope changes, contract drift, review routing, and unresolved risks.
6. Decide verdict: delivered, partial, blocked, needs-review, or rolled-back.
7. If evidence is insufficient, state what additional review, verification, or decision input is needed.
8. Write a delivery record.
9. Ask for user approval when verdict is partial, risky, subjective, or requires override.

## Rules

Do not commit, push, release, mark done, or imply completion unless project/user convention allows it and evidence supports it.

## Output

Use `references/delivery-record-template.md`. End with next action: stop, continue next increment, revise, or escalate.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
