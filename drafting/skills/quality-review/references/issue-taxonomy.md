# Issue Taxonomy

Use this schema for every review issue.

```yaml
issue:
  id: QR-001
  origin_phase: Sense|Clarify|Shape|Design|Build|Verify|Record|ContinueStop
  severity: critical|major|minor
  type: missing|incorrect|inconsistent|unclear|scope|evidence|format|risk
  description: <what is wrong>
  evidence: <file/path/quote/check>
  suggested_fix: <next action>
  resolution: fix-in-place|roll-back|defer
  rollback_to: <phase if resolution is roll-back>
```

## Severity

- critical: blocks acceptance or can cause harm, data loss, wrong decision, security/compliance failure.
- major: materially affects correctness, scope, usability, or verifiability.
- minor: polish, local clarity, or low-risk improvement.

## Closure

- Passed: no open critical or major issues.
- Stable: only minor polish remains and user accepts deferment.
- Failed: any critical/major issue remains unresolved.
