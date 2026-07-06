---
name: implementation-execution
description: Use when executing a plan, implementing a feature, fixing a bug, refactoring, performing maintenance, producing a deliverable, or running an autonomous delivery loop after scope, design, and verification expectations are clear.
license: MIT
metadata:
  author: kenpusney
  version: "0.7.0"
---

# Implementation Execution

Build one verified increment at a time.

## Before editing

1. Read track/requirements/plan/delivery record, `.agents/loop-state.md`, `docs/knowledge`, logs, code, tests.
2. Reconfirm increment, contracts, acceptance criteria, verification method.
3. If `scope_type: stage`, confirm parent scope-map status is consistent.
4. Unclear intent/design → `requirement-discovery` or `solution-design`.

## Execution loop

For each increment:
1. Define expected outcome and verification evidence.
2. Produce the increment.
3. Verify against evidence.
4. Refine if needed.
5. Record evidence per `references/increment-record-and-save.md`.

For software: `references/software-mode.md`. Checklist: `references/implementation-checklist.md`.

## Scope-map updates

After completing each stage, update the parent's scope-map. Parent track done only when all stages done.

## Autonomy

Use subagents (explorer, maker, checker) when available. If unavailable, self-review and record limitation.

## Stop conditions

| Signal | Detection | Rollback to |
|---|---|---|
| Scope drift | New requirement not in approved plan | requirement-discovery |
| Contract break | Interface/data model mismatch | solution-design |
| Verification failure | Previously passing check now fails | fix in current increment |
| Verification gap | Cannot define verification for increment | solution-design |
| Risk threshold | Increment affects too broad a scope | pause, notify user |

Write change note before resuming.

## Blocker handling

1. **Record**: Problem, Impact, Options (2–3 paths with effort/risk).
2. **Decide**: Choose option. Scope/contract/design impact → write change note.
3. **Resume**: Next unblocked increment or revise plan.

## Change control

> **Iron Law**: NO UNDOCUMENTED DRIFT.

Write change note when: expected outcome changes, scope/fields/steps added, requirement weakened, verification method no longer applies, naming conflicts with conventions. Scope additions (new sections, new reference docs) count as drift — write change note BEFORE the edit.

Template: `../solution-delivery-loop/references/change-note-template.md`.

## Contract changes

When changing an existing interface: inventory dependents → choose strategy (break-fix or deprecate-remove) → execute → verify → document.

## Anti-patterns

- Claiming done without fresh evidence.
- Compatibility shims to hide drift instead of change notes.
- Starting before design passed review-feedback.
- Fixing without checking all references to modified content.

## Related

- Previous: `solution-design`. Next: `delivery-acceptance`.
- Return to `requirement-discovery` when implementation reveals unclear intent.
