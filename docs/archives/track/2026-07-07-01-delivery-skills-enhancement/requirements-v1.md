---
status: done
scope_type: standalone
created: 2026-07-07
version: 1
---

# Delivery Skills Enhancement

## Requirements

### R1: Multi-project workspace support
Loop-state declares projects with id/name/track_root. Track paths resolve per project.

### R2: Track naming convention
All new track docs use `<YYYY-MM-DD-NN>-<name>` prefix. Date = creation date, NN = zero-padded sequence. Existing docs unchanged.

### R3: Scope splitting
Large requirements split into independently executable stages during discovery. Parent holds scope-map. Each stage gets own sub-folder with `scope_type: stage`.

### R4: Frontmatter schema
All track docs use: status, scope_type, created, parent_id (stage only), version.

### R5: Python parser
Shared parser supporting extract/index/validate/children/kanban. Per-skill wrappers.

### R6: Cross-skill reference fix
Fix 3 broken relative paths (missing `../` prefix).

## Acceptance Criteria

- All 5 modified SKILL.md files under 100 lines
- No Chinese characters in skill content
- Parser validates all 5 commands correctly
- Cross-skill references resolve to existing files
