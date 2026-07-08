# Two-Stage Review Protocol

Use for high-stakes deliverables, large revisions, external feedback, or any artifact where the first review may trigger substantial changes.

## Stage 1: Full review

Goal: find all material issues before revision.

Inputs:
- frozen artifact;
- scope and acceptance criteria;
- blueprint or review protocol;
- relevant rubrics;
- prior delivery records if any.

Output:
- full issue list using `issue-taxonomy.md`;
- verdict;
- revision roadmap grouped by priority;
- rollback target for issues rooted in earlier phases.

## Revision roadmap

```yaml
revision_item:
  id: R-001
  source_issue: QR-001
  priority: critical|major|minor
  action: fix|rollback|defer|reject
  target_phase: Shape|Design|Build|Verify
  acceptance_check: <how this fix will be verified>
```

## Stage 2: Verification review

Goal: verify the revision response, not re-review everything from scratch unless new drift appears.

Inputs:
- revised artifact;
- Stage 1 issue list;
- revision roadmap;
- response/change log;
- fresh evidence.

Checks:
1. Every Stage 1 issue is addressed, deferred with approval, or explicitly rejected with evidence.
2. Fixes did not introduce contradictions, scope drift, or contract drift.
3. High-risk areas receive focused re-check.
4. Any new critical/major issue routes normally through `review-routing.md`.

## Persona panel option

Use when the artifact benefits from multiple perspectives. Keep personas functional, not theatrical.

| Lens | Best for | Questions |
|---|---|---|
| Correctness | crafting, factual reports, audits | Is it true and does it work? |
| Evidence | investigation, reports, compliance | Are claims supported by strong evidence? |
| Usability | docs, UX, process, tools | Can the intended audience use it? |
| Maintainability | code, plans, processes | Will this remain understandable and safe? |
| Risk/compliance | legal, security, policy | What can cause harm or violation? |
| Editorial/craft | composing, creating | Does it cohere and land with the audience? |

## Stop rule

If Stage 2 finds only minor polish and no unresolved critical/major issues, mark STABLE. Do not loop indefinitely for taste.
