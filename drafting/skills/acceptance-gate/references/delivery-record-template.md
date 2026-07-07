# Delivery Record Template

Use for Record phase. Keep records append-only when delivery changes over time.

```markdown
# Delivery Record: <title>

Verdict: delivered | partial | blocked | needs-review | rolled-back
Kind:
Mode:
Date:
Parent / stage:

## Delivered artifacts

| Artifact | Path/location | Status | Notes |
|---|---|---|---|

## Acceptance evidence

| Criterion | Status | Evidence | Notes |
|---|---|---|---|

Status values: pass, fail, deferred, blocked, not-applicable.

## Verification performed

- Review verdict:
- Checks/commands:
- Fact verification:
- Compliance/integrity gate:
- Manual inspection:

## Format fit

Loaded format reference:
Result:

## Deferred / blocked items

| Item | Reason | Approval / next action |
|---|---|---|

## Scope changes

Link change notes. If none, state none.

## Risks and limitations

## Child stage coverage

Use for parent records.

| Stage | Verdict | Evidence | Deferred |
|---|---|---|---|

## Next action

stop | continue next increment | revise | split | escalate
```

## Rules

- Do not claim delivered without evidence.
- Do not omit failed or deferred criteria.
- For partial delivery, name the usable subset and the missing subset.
- For rolled-back work, record reason and remaining state.
