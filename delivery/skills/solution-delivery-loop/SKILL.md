---
name: solution-delivery-loop
description: "Use when work needs end-to-end delivery, phase triage, or continuation from request to accepted outcome: requirements, design, implementation planning, coding, bugfixes, refactors, maintenance, validation, delivery records, autonomous loops, or existing track/plan work."
license: MIT
metadata:
  author: kenpusney
  version: "0.7.0"
---

# Solution Delivery Loop

`Sense → Shape → Design → Build → Verify → Record → Continue/Stop`

## Work type triage

| Work type | Entry point | Skip |
|---|---|---|
| New work | requirement-discovery | — |
| Investigation | structured-investigation or requirement-discovery | — |
| Fix | implementation-execution or requirement-discovery | solution-design for trivial fixes |
| Restructure | solution-design (from current-state analysis) | requirement-discovery |
| Migrate | solution-design (from mapping table) | requirement-discovery |
| Enhance | requirement-discovery or solution-design | — |

## Loop state

`.agents/loop-state.md` declares workspace structure:

```yaml
projects:
  - id: <project-id>
    name: <display name>
    track_root: <path>         # default: docs/track
active_project: <project-id>
autonomy: full | supervised    # default: supervised
```

Single-project may omit `projects`. Multi-project must declare all projects.

## First move

1. Inspect `.agents/loop-state.md`, track docs, requirements, plans, delivery records, `docs/knowledge`, `docs/logs`.
2. Right-size: stop when more context won't change the next action.
3. Route: unclear need → `requirement-discovery`; clear requirements → `solution-design`; executable plan → `implementation-execution`; done → `delivery-acceptance`.

## Process gates

> **Iron Law**: NO PHASE SKIPPING. Each gate must pass before the next phase begins.

| Gate | Before | Must have | Check |
|---|---|---|---|
| Track doc | any editing | `requirements-v1.md` with `status: in_progress` | file exists with frontmatter |
| Design review | implementation | `solution-design-v1.md` + review-feedback passed | feedback report shows no critical/major |
| Impl review | delivery-acceptance | implementation complete + review-feedback passed | feedback report shows no critical/major |
| Acceptance | claiming done | delivery-record with fresh verification evidence | all acceptance criteria verified |

"Start implementing" or "go ahead" means scope is confirmed — still create track doc first, then proceed through the full cycle. Never skip to coding.

## Review and feedback

Invoke `review-feedback` after each phase. Cumulative: inspects all prior artifacts + current output.

| Review at | Inspects | Rollback to |
|---|---|---|
| solution-design | Requirements + design | requirement-discovery |
| implementation-execution | Requirements + design + implementation | requirement-discovery |
| delivery-acceptance | all prior + delivery record | requirement-discovery |

Write change note if scope/contract/design changed.

## Autonomy and continuity

`.agents/loop-state.md` may define full-autonomy. Autonomy does not waive track notes, verification, delivery records. Use subagents when available. On resume: read loop-state, latest delivery record, track docs. No loop-state → infer from track docs.

## Track documentation

All track docs use `<YYYY-MM-DD-NN>-<name>` naming, YAML frontmatter, and nested scope-map structure. See `references/track-document-structure.md` for schema, paths, and nesting rules. Parser: `scripts/track_parser.py`.

## Loop improvement

Repeated issues → `process-distillation`. New skill creation requires user approval.
