# Review Routing

Quality review is cumulative: inspect the current artifact plus prior phase outputs that define its obligations.

## Passes for multi-part deliverables

1. Accuracy: facts, citations, calculations, code behavior, direct claims.
2. Validity: logic, causal chains, argument structure, design reasoning, absence of strawmen.
3. Consistency: cross-references, naming, requirements alignment, no contradictions, fixes did not break earlier work.

## Routing

| Finding | Route |
|---|---|
| All issues fix-in-place | Return to producer for revision, then re-review. |
| Any rollback issue | Return to earliest affected phase. |
| Scope ambiguity | Return to Shape. |
| Contract/design drift | Return to Design. |
| Evidence gap only | Return to Build or Verify depending on missing evidence. |
| Only minor polish | Mark stable; further review optional with user approval. |

Do not hide rollback findings as local edits. Routing is part of the review output.
