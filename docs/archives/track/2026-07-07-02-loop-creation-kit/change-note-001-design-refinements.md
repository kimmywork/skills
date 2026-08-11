# Change Note 001: Loop Creation Kit Design Refinements

## Linked Work

- Requirements / track: `docs/track/2026-07-07-02-loop-creation-kit/requirements-v2.md`
- Solution design: `docs/track/2026-07-07-02-loop-creation-kit/solution-design-v2.md`
- Plan: Not yet created
- Delivery record: Not yet created

## Discovery Phase

sense → shape → design → build → verify → record

## Original Decision

Solution design v1 specified:
- State file statuses: `success | failed | partial | skipped`
- Dispatch output with inline `trigger_output` and `state_dir`
- No explicit collision detection mechanism beyond REQ-019's "skip + record"
- Script has "no external packages beyond stdlib"
- Trigger execution context undefined
- No dispatch logging
- Per-workflow error handling undefined
- `loopify` grilling protocol inline in SKILL.md
- No slug rules for workflow names
- No gitignore consideration

## Problem Found

A design review identified 9 issues (1 critical, 4 major, 4 minor). A grilling session with the designer resolved 7 structural questions, leading to refinements across the architecture, contracts, and implementation approach.

## New Decision

See `research/2026-07-07-design-review-and-grilling-resolutions.md` for full discussion.

Key changes:

| Area | v1 | v2 |
|---|---|---|
| **State status enum** | `success / failed / partial / skipped` | `scheduled / success / failed / partial / skipped` |
| **Collision detection** | Undefined mechanism | State file as lock: script creates `status: "scheduled"`; missing `completed_at` = in progress |
| **Dispatch output trigger** | `trigger_output` inline string | `trigger_output_file` path to temp file |
| **Dispatch output format** | Flat `due`/`not_due` | Added `script_errors` array, per-workflow independence |
| **Dispatch logging** | Not specified | Every invocation logged to `.state/dispatch/<date>.json` |
| **Cron parser** | "No external deps" | `croniter` via pip; documented in `references/setup.md` |
| **Trigger execution ctx** | Undefined | Hard-coded: `/bin/sh -c`, project root cwd, 30s timeout, inherits env |
| **Skill instructions** | All in SKILL.md | Core in SKILL.md ≤100 lines, details in `references/` |
| **loopify grilling** | Protocol inline | Checklist in `references/grilling-checklist.md` + domain-specific probes |
| **Slug rules** | None | lowercase, spaces→hyphens, special chars stripped, max 64 chars |
| **Workflow name collisions** | Not addressed | script enumerates state files, max NNN + 1, atomic temp+rename write |

## Impact

- **User behavior**: No change — same skill invocation flow
- **Modules/files**:
  - `loopify/` gains `references/grilling-checklist.md`
  - `loopy/` gains `references/setup.md`
  - `loopy.py` gains: collision detection, trigger output file saving, dispatch logging, croniter dependency
- **Data/contracts**: State file schema updated (`scheduled` status, `trigger_output_file`, nullable fields). Dispatch output schema updated (`script_errors`, `trigger_output_file`, `state_file` instead of `state_dir`)
- **Tests/verification**: REQ-019 verification updated to reflect explicit collision detection mechanism; REQ-006 updated for status transition; §9 Script Dispatch Output schema updated (REQ-004 unchanged — already high-level enough)
- **Cross-feature knowledge to update in `docs/knowledge`**: None
- **Risks**: Trigger command user env configuration — documented in `setup.md` with examples

## Approval / Rationale

Approved via design review + grilling session on 2026-07-07. Designer confirmed all decisions.

## Verification Update

- REQ-006: Now verifies state file transitions through `scheduled` → final status
- REQ-019: Now verifies collision detection via `status: "scheduled"` + missing `completed_at`
- New: Verify dispatch log created at `.state/dispatch/<date>.json` with correct structure
- New: Verify per-workflow error isolation (one failing trigger doesn't block others)