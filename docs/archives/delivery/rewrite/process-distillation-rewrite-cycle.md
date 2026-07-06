# Process Distillation: SDL Rewrite Cycle

## Metadata

- **Phase analyzed**: `software-delivery-loop` → `solution-delivery-loop` rewrite (full cycle)
- **Skills involved**: all 8 phase skills, 4 review cycles (v1-v4), 2 self-reviews
- **Review feedback**: 4 external review documents + 2 self-reviews
- **Fix outcomes**: ~50 individual fixes across 8 phases of work
- **Analysis date**: 2026-07-06

## Summary

- **Gaps found**: 6 (3 skill-level, 3 process-level)
- **Improvements proposed**: 5
- **New skills proposed**: 0
- **Pending approval**: 5

## Gaps and improvements

### Gap 1 — Self-review consistently overestimates completion

| Field | Value |
|---|---|
| **Gap type** | repeated-improvidation |
| **Evidence** | Self-review v1 claimed ~95%, actual was ~70%. Self-review v2 claimed ~96%, actual was ~90%. Each external review found issues the self-review missed. Pattern: self-review checks files but does not verify claims against file contents (e.g., "No vertical slice in generic skills" claimed ✅ but `solution-design/SKILL.md` still had `vertical slices`). |
| **Proposed change** | Add a verification step to `process-distillation/SKILL.md`: after a self-review, run a command to grep for all claimed-terminology removals and confirm zero hits. Self-review claims must cite file evidence, not just intent. |
| **Target** | `process-distillation/SKILL.md` Analyze step |
| **Approval** | pending |

### Gap 2 — No systematic terminology-change tracking

| Field | Value |
|---|---|
| **Gap type** | missing-guardrail |
| **Evidence** | The rename (Code Fit→Format Fit, vertical slice→increment, PRD→requirements, module landing→structure) had to be applied across 30+ files. Each review found missed spots from the same rename. The renames were correct but coverage was incomplete because there was no inventory of "all files containing term X" before starting. |
| **Proposed change** | Before a terminology rename in a skill family, run `grep -rn "<old-term>" ./` to inventory all affected files. Fix them all in one pass, then re-grep to confirm zero. Add this as a step in `process-distillation/SKILL.md` when the proposed change involves renaming. |
| **Target** | `process-distillation/SKILL.md` Apply step |
| **Approval** | pending |

### Gap 3 — `solution-delivery-loop` SKILL.md change control signals lack a "terminology" trigger

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | The 5 change-control signals (expected outcome changes, adding scope, skipping requirements, verification method changes) cover behavioral/scope drift. But they don't cover terminology drift — the most common error in this rewrite was using old terms in new contexts. A "terminology inconsistency" signal would have caught the `PRD + design` table entries and `files/modules` placeholders earlier. |
| **Proposed change** | Add a 6th change-control signal: "Terminology used in this increment conflicts with the approved naming conventions." This applies to both software and non-code deliverables. |
| **Target** | `implementation-execution/SKILL.md` Change control |
| **Approval** | pending |

### Gap 4 — External reviews detected issues that self-reviews missed, but had no structured handoff

| Field | Value |
|---|---|
| **Gap type** | repeated-improvidation |
| **Evidence** | Each external review (v1-v4) essentially re-ran the same grep-based checks that the self-review claimed to have run. The overlap was ~70%: external reviews found real issues, but many were the same class as issues the self-review had already fixed elsewhere. A "checklist of things to verify after a rename" would have caught these in the self-review. |
| **Proposed change** | Create a `references/rename-checklist.md` under `solution-delivery-loop/references/` — a reusable checklist for any future rename or terminology change in the family. Items: (1) grep all SKILL.md for old term, (2) grep all references/ for old term, (3) grep all README/template files for old term, (4) grep all evals for old term, (5) grep all JSON/config for old term, (6) confirm zero hits. |
| **Target** | `solution-delivery-loop/references/rename-checklist.md` (new) + `process-distillation/SKILL.md` reference |
| **Approval** | pending |

### Gap 5 — `process-distillation` should distinguish between "improve existing skill" and "create new skill" paths

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | The rewrite never created a new skill, but the `process-distillation` skill equally weights "update existing" and "create new" as outcomes. Every proposed improvement in this cycle was a small fix to an existing skill. The "new skill creation" path carries more risk (requires user approval, needs trigger evals, needs install commands) but the current skill doesn't help the agent decide which path to take. |
| **Proposed change** | Add a decision gate in `process-distillation/SKILL.md` before the Evaluate step: "Is this gap fixable by changing 1-5 lines in an existing skill, or does it require a new skill with its own SKILL.md, triggers, and references?" If 1-5 lines, prefer small fix. Only create new skill when the sub-process is clearly bounded, reusable across contexts, and has its own triggering signal. |
| **Target** | `process-distillation/SKILL.md` Evaluate step |
| **Approval** | pending |

### Gap 6 (process-level) — Review cycles converged but no convergence criteria were defined

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | The rewrite went through 4 external review cycles + 2 self-reviews. Each cycle found fewer issues (v1: ~15, v2: ~10, v3: ~11, v4: ~5). But there was no explicit "done" criterion — each review was initiated by the reviewer, not by a convergence threshold. This risks either stopping too early (missed issues) or over-iterating (diminishing returns). |
| **Proposed change** | In `review-feedback/SKILL.md`, add a convergence rule: "If the previous review's issues were all resolved and the current review finds < 3 new issues, the artifact can be marked as stable. New reviews at this point are optional and should be triggered by new changes, not repeated scrutiny." |
| **Target** | `review-feedback/SKILL.md` Close step |
| **Approval** | pending |

## Skills modified

No skills modified yet — awaiting approval.

## New skills created

None proposed. All gaps are addressable with small changes to existing skills.

## Deferred items

None.

## Recommendations for future cycles

1. Before any terminology rename, inventory all files first (Gap 2 fix).
2. After a self-review, verify claims with grep before publishing (Gap 1 fix).
3. Use the rename-checklist.md for any cross-family rename.
4. Apply the convergence rule to avoid over-iteration.