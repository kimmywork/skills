# Track Document Structure

Use tracks for multi-turn, multi-file, risky, or user-visible work.

## Location

Default path: `tracks/<YYYY-MM-DD-NN>-<slug>/`.
If a project already uses `docs/track/`, follow the project convention.

## Frontmatter

```yaml
---
status: pending|in_progress|blocked|done
kind: crafting|composing|evaluating|investigating|creating|mixed
phase: Sense|Clarify|Shape|Design|Build|Verify|Record|ContinueStop
scope_type: parent|stage|standalone
created: YYYY-MM-DD
version: 1
parent_id: <folder-name>   # stage only
---
```

## Files

| Scope | Recommended files |
|---|---|
| standalone | `track.md` or `requirements-v1.md` |
| parent | `requirements-v1.md`, `scope-map.md`, delivery records |
| stage | child folder with its own `requirements-v1.md`, plan, records |

## Scope-map

Large work uses a parent folder plus stage subfolders.

```markdown
| Stage ID | Summary | Status | Evidence |
|---|---|---|---|
```

Rules:
- Parent is done only when all child stages are done.
- Each stage must be independently executable and verifiable.
- Parent non-goals apply to every child stage.
- `parent_id` must match the parent folder name.

## Parser

`scripts/track_cli.py` supports: `extract`, `index`, `validate`, `children`, `kanban`.
Use parser output for quick state checks before reading full track contents.
