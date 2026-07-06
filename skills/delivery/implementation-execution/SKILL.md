---
name: implementation-execution
description: Use when executing a plan, implementing a feature, fixing a bug, refactoring, performing maintenance, producing a deliverable, or running an autonomous delivery loop after scope, design, and verification expectations are clear.
license: MIT
metadata:
  author: kenpusney
  version: "0.6.1"
---

# Implementation Execution

Build one verified increment at a time.

## Before editing

1. Read the current track/requirements/plan/delivery record, `.agents/loop-state.md` if present, `docs/knowledge`, relevant logs, code, and tests.
2. Reconfirm current increment, structure, contracts, acceptance criteria, and verification method.
3. If intent, design, or verification is unclear, stop and use `requirement-discovery` or `solution-design`.

## Execution loop

For each increment:

1. Define expected outcome and verification evidence.
2. Produce the increment.
3. Verify against evidence.
4. Refine based on verification results.
5. Record evidence and save the increment per `references/increment-record-and-save.md`.

For software deliverables, see `references/software-mode.md` for TDD-driven slice execution with automated verification.

Use `references/implementation-checklist.md` for the increment checklist.

## Autonomy and subagents

Autonomous execution is allowed when the plan and evidence are sufficient. Use subagents when available:
- explorer: gather facts without editing
- maker: produce the increment
- checker/reviewer: verify spec fit

If unavailable, perform a fresh review pass yourself and state that review was self-performed.

## Stop conditions

Pause and determine the correct rollback point when any of these signals occur:

| Signal | Detection | Rollback to |
|---|---|---|
| Scope drift | New requirement, element, or step not in approved plan | requirement-discovery |
| Contract break | Interface, input, output, or data model mismatch | solution-design |
| Verification failure | A check that previously passed now fails | fix in current increment |
| Verification gap | Cannot define or run verification for an increment | solution-design |
| Risk threshold | Increment affects more than a manageable scope | pause, notify user |

Before resuming, write a change note recording what changed and why.

## Blocker handling

When an increment is blocked:

1. **Record**: Problem (what happened), Impact (what is blocked), Options (2–3 resolution paths with effort/risk estimate).
2. **Decide**: Choose an option. If the decision affects scope, contract, or design, write a change note.
3. **Resume**: Continue from the next unblocked increment, or revise the plan.

## Change control

> **Iron Law**: NO UNDOCUMENTED DRIFT.

Stop and write a change note before continuing when any of these occur:
- The expected outcome changes mid-increment.
- You need to add scope, fields, or steps not in the approved plan.
- You skip or weaken a requirement or non-goal.
- The verification method no longer applies.
- Terminology or naming used in the increment conflicts with the approved conventions.

Software-specific signals (see `references/software-mode.md`): test expectation changes, unapproved fields/components/routes, or architecture/contract/model changes.

Template: `solution-delivery-loop/references/change-note-template.md`.

## Contract changes

When an increment changes an existing interface, contract, or established pattern:

1. **Inventory**: List every dependent that must be updated.
2. **Strategy**: "Break once, fix all" (small scope) or "Deprecate then remove" (large scope).
3. **Execute**: Update all identified dependents in the same increment.
4. **Verify**: Confirm no regressions.
5. **Document**: Record the change with affected items list.

## Anti-patterns

- Skipping verification — claiming done without fresh evidence.
- Using compatibility shims or workarounds to hide drift instead of writing a change note.
- Starting before design has passed review-feedback.
- Fixing an artifact without checking all references to the modified content.

## Related

- Previous: `solution-design` when plan is missing. Next: `delivery-acceptance` before claiming done.
- Return to `requirement-discovery` when implementation reveals unclear intent or acceptance.
