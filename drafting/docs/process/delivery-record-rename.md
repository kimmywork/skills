# Delivery Record: Rename 3 drafting skills

Verdict: delivered
Kind: Composing
Mode: rename + refactor
Date: 2026-07-08
Parent / stage: N/A

## Delivered artifacts

| Artifact | Path/location | Status | Notes |
|---|---|---|---|
| guided-inquiry → probing | `drafting/skills/probing/` | delivered | directory renamed, SKILL.md updated |
| quality-review → inspect | `drafting/skills/inspect/` | delivered | directory renamed, SKILL.md + references/ updated |
| intent-routing → triage | `drafting/skills/triage/` | delivered | directory renamed, SKILL.md updated |
| symlinks | `.agents/skills/{probing,inspect,triage}` | delivered | old symlinks removed, new ones created |
| README.md | `drafting/README.md` | delivered | table updated |
| cross-references | 6 skills files + 4 references/ files | delivered | all paths and concept names updated |

## Acceptance evidence

| Criterion | Status | Evidence | Notes |
|---|---|---|---|
| Directory names changed | pass | `ls` confirms 3 new dirs, 0 old dirs | |
| SKILL.md frontmatter `name:` | pass | `head -3` shows `probing`, `inspect`, `triage` | |
| No stale references in `skills/` | pass | `rg "quality-review\|intent-routing\|guided-inquiry"` returns exit 1 (no matches) | |
| H1 titles updated | pass | `rg "^# "` shows `# Probing`, `# Inspect`, `# Triage` | |
| references/ files clean | pass | probing/triage have no references/ subdir; inspect/references/ has 0 stale refs | |
| symlinks updated | pass | 3 new links to correct paths, 0 old links | |
| README.md clean | pass | `rg` returns exit 1 (no matches) | |

## Verification performed

- Review verdict: N/A (self-acceptance)
- Checks/commands: `rg`, `ls`, `head` across all affected files
- Fact verification: N/A
- Compliance/integrity gate: N/A
- Manual inspection: each change was verified by reading the actual file content

## Format fit

N/A — no format reference applies to a rename operation.

## Deferred / blocked items

| Item | Reason | Approval / next action |
|---|---|---|
| `docs/process/` stale refs (24 matches) | Archival documents for maintainers/audits per README | Deferred unless user explicitly requests update |

## Scope changes

None.

## Risks and limitations

- docs/process/ files retain old names; not a functional risk since they are not loaded by any active skill.
- No other bundles or external artifacts reference these skills.

## Next action

stop