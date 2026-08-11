# Change Note 001: Process gates + track structure extraction

## Linked Work

- Requirements / track: `docs/track/2026-07-07-01-delivery-skills-enhancement/requirements-v1.md`
- Solution design: none (implemented directly)
- Plan: none
- Delivery record: `docs/track/2026-07-07-01-delivery-skills-enhancement/delivery-record-v1.md`

## Discovery Phase

build → verify (caught during review)

## Original Decision

5 SKILL.md files modified with inline track documentation details (naming, frontmatter schema, paths, nesting). No process enforcement section.

## Problem Found

1. Agent repeatedly skips the requirements → design → review → implement → review → accept cycle. User caught this multiple times across sessions. No enforcement mechanism in the skill itself.
2. Track structure details (naming, frontmatter, paths, nesting) duplicated across solution-delivery-loop, requirement-disolution, and delivery-acceptance SKILL.md files. Violates DRY; wastes 100-line budget.

## New Decision

1. Add `## Process gates` section to solution-delivery-loop SKILL.md: 4-row table (track doc → design review → impl review → acceptance) with check conditions. "Start implementing" = scope confirmed, still create track doc first.
2. Extract all track structure details to `references/track-document-structure.md`. Replace inline details in 3 skills with one-line references.

## Impact

- User behavior: agents must now create track doc before any editing, invoke review-feedback between phases
- Modules/files: solution-delivery-loop/SKILL.md (+process gates, -19 lines inline), requirement-discovery/SKILL.md (-6 lines), delivery-acceptance/SKILL.md (-4 lines), new references/track-document-structure.md (45 lines)
- Data/contracts: frontmatter schema, naming convention unchanged
- Tests/verification: line counts verified (all ≤100), cross-skill references checked
- Cross-feature knowledge: project MEMORY.md updated with track-first rule and process skipping trap
- Risks: process gates may feel heavy for trivial fixes; work type triage already skips solution-design for trivial fixes, process gates should follow same skip logic

## Approval / Rationale

User-identified issue ("你自己总是不按照规矩"). Process enforcement is scope-relevant to this feature. Autonomous change safe: no behavior change to existing skills, only additions.

## Verification Update

- Process gates table present in solution-delivery-loop/SKILL.md
- `references/track-document-structure.md` exists and contains naming, frontmatter, paths, nesting rules
- 3 skills reference the doc (grep `track-document-structure`)
- Project MEMORY.md contains track-first rule
