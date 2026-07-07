# Audit State Schema

Use for structured audits of documents, plans, code reviews, compliance checks, and evidence packages.

## Section

```yaml
section:
  id: section:1
  name: <logical unit>
  location: <page/sheet/file/range>
  scope: <what this section covers>
```

## Claim

```yaml
claim:
  id: claim:1
  type: public_data|numerical_consistency|internal_consistency|policy|technical
  original_text: <verbatim or precise summary>
  section: <section id>
  location: <anchor>
  status: unverified|verified|refuted|inconclusive
  evidence: []
```

## Issue

```yaml
issue:
  id: issue:1
  type: spelling_grammar|narrative_logic|non_public_info|public_data|numerical_consistency|technical|policy
  severity: high|medium|low
  original_text: <verbatim when available>
  context: <surrounding context>
  description: <direct explanation>
  suggested_fix: <replacement or action>
  location: <anchor>
  root_issue_id: <optional cascading root>
```

## Rules

- Create issues for every refuted or inconclusive claim.
- Link cascading errors to `root_issue_id`.
- Never fabricate URLs or sources.
- Use exact calculations for numerical consistency; do not do mental math.
