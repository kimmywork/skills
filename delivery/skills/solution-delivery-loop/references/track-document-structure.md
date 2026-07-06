# Track Document Structure

## Naming convention

All new track docs: `<YYYY-MM-DD-NN>-<name>` where:
- `YYYY-MM-DD` = creation date (never changes)
- `NN` = zero-padded sequence within the same date
- Existing docs keep their old names

## Frontmatter schema

```yaml
---
status: pending | in_progress | done | blocked
scope_type: parent | stage | standalone
created: YYYY-MM-DD
parent_id: <folder-name>       # stage only; omit for parent/standalone
version: <integer>             # starts at 1
---
```

## Paths

| Scope | Path |
|---|---|
| Single-project | `docs/track/<track-name>/` |
| Multi-project | `<project.track_root>/<track-name>/` |
| Standalone | `docs/track/<YYYY-MM-DD-NN>-<name>.md` |

## Nesting via scope-map

Large work → parent folder (`scope_type: parent`) with `scope-map.md` + stage sub-folders (`scope_type: stage`).

```
docs/track/2026-07-07-01-delivery-enhancement/
  requirements-v1.md           # scope_type: parent
  scope-map.md                 # stage ID | summary | status
  2026-07-07-01-multi-project/ # scope_type: stage
    requirements-v1.md
  2026-07-07-02-track-naming/
    requirements-v1.md
```

### Rules

- Parent done only when all stages done.
- Each stage is independently executable and verifiable.
- Parent inherits non-goals to all stages; stages may add their own.
- Parent_id in stage frontmatter must match parent folder name.

### Scope-map format

```markdown
| Stage ID | Summary | Status |
|---|---|---|
| <YYYY-MM-DD-NN>-<name> | <one-line description> | pending |
```

## Parser

`scripts/track_parser.py` supports: `extract`, `index`, `validate`, `children`, `kanban`.

Use to query track state without reading full files. Validation enforces parent/child consistency.
