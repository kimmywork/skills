# Change Note Template

Use before executing new scope, changed assumptions, contract drift, weakened criteria, or verification changes.

```markdown
## Change Note: <short title>

- Date:
- Trigger:
- Earliest affected phase:
- Original scope/design/contract:
- Proposed change:
- Reason:
- Impacted artifacts:
- Impacted acceptance criteria:
- Verification update:
- Risks:
- Options:
  1. Approve change
  2. Defer change
  3. Replace original scope/design
  4. Roll back to <phase>
  5. Stop and re-shape
- Recommendation:
- User decision:
```

## When mandatory

A change note is mandatory when:
- scope, audience, deliverable, API, schema, field, route, section, or data model changes;
- acceptance criteria are weakened or replaced;
- verification method changes;
- a fix requires touching unrelated areas;
- a child stage alters parent assumptions.

## Rule

A change note is not approval. Wait for user decision when the change affects scope, cost, timeline, compliance, acceptance, or risk.
