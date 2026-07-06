# Change Note 002: Process distillation guardrails

## Linked Work

- Requirements / track: `docs/track/2026-07-07-01-delivery-skills-enhancement/requirements-v1.md`
- Solution design: none
- Plan: none
- Delivery record: `docs/track/2026-07-07-01-delivery-skills-enhancement/delivery-record-v1.md`

## Discovery Phase

record (process-distillation triggered after delivery)

## Original Decision

Implementation-execution change control listed drift triggers but didn't explicitly cover scope additions (new sections, new reference docs). Requirement-discovery had no check for redundant track doc creation.

## Problem Found

1. Agent added Process gates section + extracted track-document-structure.md without writing change note — these are scope additions that drifted from the approved plan.
2. Agent created a separate `2026-07-07-02-process-discipline` track doc when the requirements were already covered by R7/R8 in the main feature.

## New Decision

1. Add to implementation-execution change control: "Scope additions (new sections, new reference docs) count as drift — write change note BEFORE the edit."
2. Add to requirement-discovery step 7: "Before creating a new track doc, search existing track docs for overlapping scope. Extend existing docs — don't duplicate."

## Impact

- User behavior: agents must write change note before any scope addition during build
- Modules/files: implementation-execution/SKILL.md (+1 line), requirement-discovery/SKILL.md (+1 line)
- Data/contracts: none
- Tests/verification: line counts verified (both ≤100)
- Cross-feature knowledge: none
- Risks: minimal — guardrails are lightweight

## Approval / Rationale

User-approved via process-distillation. Both improvements are 1-line additions.

## Verification Update

- implementation-execution/SKILL.md change control section includes scope addition trigger
- requirement-discovery/SKILL.md step 7 includes redundant work check
