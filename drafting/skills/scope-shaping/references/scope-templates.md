# Scope Templates

Use these templates to produce a Shape artifact. Keep the final artifact as small as possible while preserving acceptance and verification.

## Universal fields

- Goal:
- Kind and mode:
- Source materials:
- Audience/users:
- In scope:
- Out of scope:
- Assumptions:
- Acceptance criteria:
- Verification plan:
- Risks:
- Open questions:
- Stage split needed: yes/no

## Crafting

- Users / actors:
- Problem and current pain:
- Jobs or user stories:
- Behavior requirements:
- Boundary contracts: inputs, outputs, schemas, APIs, data models:
- Non-functional constraints:
- Non-goals:
- Acceptance criteria:
- Test or verification plan:
- Rollback / migration concerns:

## Composing

- Audience:
- Purpose:
- Core message:
- Required inputs/sources:
- Claims that need verification:
- Structure:
- Style constraints:
- Length/format constraints:
- Acceptance criteria:

## Evaluating

- Artifact under review:
- Review purpose:
- Criteria and severity definitions:
- Issue taxonomy:
- Evidence required:
- Out-of-scope checks:
- Verdict taxonomy:
- Required output format:

## Investigating

- Question:
- Decision the research should support:
- Boundaries:
- Source types:
- Evidence hierarchy:
- Methodology pattern:
- Confidence labels:
- Expected synthesis:

## Creating

- Premise:
- Audience / experience:
- Style direction:
- Reference works:
- Constraints:
- Success criteria:
- Iteration preference:

## Split-stage scope

For each child stage:

```yaml
stage:
  id: <stage id>
  kind: <kind>
  summary: <one line>
  depends_on: []
  local_scope: []
  local_acceptance: []
  verification: []
```
