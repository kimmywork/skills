---
name: align
description: Keep project documentation aligned when implementation, requirements, decisions, or research evidence changes, or when document moves and renames require reference remapping. Use to create, update, archive, or remap plans, architecture notes, research reports, and current references.
---

# Project Knowledge Alignment

Use this skill when project knowledge changes require documentation updates, or when document moves or renames require reference remapping. Do not use it for standalone document drafting, resolving a substantive design dispute, or giving a formal verification or acceptance verdict.

## Workflow

1. Inspect the changed implementation, requirements, decisions, evidence, and existing documents before editing.
2. Identify each affected document as a current specification, implementation plan, architecture decision, algorithm note, research source, derived summary, or historical material.
3. Determine the authoritative basis by fact type: implementation for actual behavior, approved requirements or decisions for intended behavior, and traceable sources for research claims. Do not infer authority from recency alone.
4. Keep one current reference for each decision or factual claim. Update it and link to it rather than copying the same content into several reports.
5. Update affected documents with concrete evidence. Distinguish implemented, partial, planned, research-only, historical, and unknown; do not mark a broad capability complete because a finite subset exists.
6. Archive duplicate, obsolete, or superseded material only when its replacement is clear. Preserve provenance, context, status, and a link to the replacement.
7. When sources conflict without sufficient evidence to reconcile them, preserve and label the conflict; do not silently choose a result or turn an unresolved conflict into an archival decision.
8. After a move or rename, remap inbound and outbound references to the new source, or leave each historical reference explicitly marked.
9. Check that the resulting documents, references, status claims, and cited evidence agree. Limit this check to alignment; use a dedicated review when a formal verdict is needed.

## Output

In the user's language, record the alignment decision, changed documents, archive or remapping rationale, evidence, unresolved gaps, and any explicitly preserved conflicts.
