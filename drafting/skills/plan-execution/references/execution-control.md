# Execution Control

This reference restores delivery-grade execution controls for Build phase.

## Before editing or producing

1. Read active track, scope, blueprint, previous delivery record, review findings, and loop state.
2. Inspect relevant source artifacts, existing conventions, logs, tests, documents, or prior outputs.
3. Reconfirm active increment, contracts, acceptance criteria, and verification method.
4. If this is a child stage, read parent scope-map and inherited non-goals.
5. If intent, design, contract, or verification is unclear, return to Shape or Design.

## Execution loop

For each increment:

1. Define expected outcome and verification evidence.
2. Produce the smallest useful increment.
3. Verify against evidence.
4. Refine if needed.
5. Record evidence in `increment-record.md`.
6. Run phase review before advancing.

## Scope-map updates

After completing a child stage:

- update child delivery record;
- update parent scope-map status and evidence;
- do not mark parent done until all required children are done or explicitly deferred;
- if child scope changes parent assumptions, pause and write parent change note.

## Stop conditions

| Signal | Detection | Route |
|---|---|---|
| Scope drift | new requirement not in approved scope | Shape |
| Contract break | interface/data/section contract mismatch | Design |
| Verification failure | planned check fails | Build fix or Design rollback |
| Verification gap | cannot define evidence | Design |
| Risk threshold | increment touches too broad a surface | pause and checkpoint |
| Parent mismatch | child conflicts with parent non-goals | parent Shape/change note |

## Blocker handling

```markdown
## Blocker
- Problem:
- Impact:
- Options: 2-3 paths with effort/risk
- Recommended option:
- Scope/design/contract impact:
- Decision needed:
```

## Change-control signals

Write a change note before resuming when:

- expected outcome changes;
- scope, fields, sections, steps, routes, parameters, components, or data models are added;
- a requirement is weakened;
- verification method no longer applies;
- naming or structure conflicts with conventions;
- a compatibility shim hides drift instead of resolving it.

## Anti-patterns

- Claiming done without fresh evidence.
- Starting before design passed review.
- Fixing without checking references and dependents.
- Updating parent status before child evidence exists.
- Treating blocker resolution as approval for unrelated scope.
