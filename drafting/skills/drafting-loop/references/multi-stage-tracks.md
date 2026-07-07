# Multi-Stage and Multi-Deliverable Protocol

Use when work is too broad for one verifiable increment or when one request contains multiple deliverables.

## When to split

Split when the work has any of these:
- multiple independently valuable deliverables;
- multiple user scenarios or audiences;
- multiple risk levels or review criteria;
- multiple modules/systems/documents;
- an increment that cannot be verified in one pass.

## Parent/stage model

- Parent track owns shared goal, non-goals, global constraints, and scope-map.
- Stage track owns local scope, criteria, blueprint, build, review, and record.
- Parent status is derived from child stages; parent is done only when all required children are done.
- Parent non-goals apply to every child unless a change note overrides them.

## Scope-map fields

```markdown
| Stage ID | Kind | Summary | Depends on | Status | Evidence | Record |
|---|---|---|---|---|---|---|
```

## Stage lifecycle

Each stage runs the full loop it needs:
Sense/Clarify snapshot -> Shape -> Design or fast-pass -> Build -> Verify -> Record.
Every stage must pass phase review before updating parent status.

## Multi-deliverable rules

- Prefer sequential stages when outputs depend on one another.
- Parallel work is allowed only when stages are independent and have separate verification/record artifacts.
- Merge at parent Continue/Stop with a parent delivery record summarizing child records.
- If a child reveals new parent scope, pause child, write parent change note, then resume.

## Completion

Parent completion requires:
- all required child stages delivered or explicitly deferred;
- no unresolved critical/major child review issues;
- parent acceptance record with child coverage table;
- next action: stop, next stage, iterate, or split further.
