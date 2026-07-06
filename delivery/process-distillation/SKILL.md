---
name: process-distillation
description: Use when recurring phase friction, repeated review feedback, or resolved phase cycles suggest skill or process improvements.
license: MIT
metadata:
  author: kenpusney
  version: "0.4.0"
---

# Process Distillation

## Process

1. **Gather context**: phase executed, artifacts produced, review feedback report, fix outcomes, execution observations.
   If context insufficient, explore agent session logs or memory stores as fallback — not core, not required.

2. **Analyze gaps**:

   | Dimension | Question |
   |---|---|
   | Coverage gap | Step skill should describe but didn't? |
   | False guidance | Skill misled executor? |
   | Missing guardrail | Review caught something skill should prevent? |
   | Repeated improvisation | Executor re-invented same helper? |
   | Atomic extraction | Clear bounded sub-process worth its own skill? |
   | Context overhead | Skill too large, wasting context? |
   | Trigger misfire | Description caused wrong trigger behavior? |

3. **Evaluate options**: small fix / new reference / new atomic skill / no change.

   **Decision gate**: If the gap can be resolved by changing 1–5 lines in an existing skill, prefer a small fix. Only create a new skill when the sub-process is clearly bounded, reusable across contexts, and has its own independent triggering signal. New skill creation always requires user approval regardless of autonomy mode.

4. **Self-review and verify claims**:
   - Every claim in the distillation report must cite file evidence (line number, section, or grep result).
   - Before applying a terminology rename, inventory all affected files: `grep -rn "<old-term>" ./ --include="*.md" --include="*.json"`
   - After applying changes, re-grep to confirm zero remaining hits.
   - Use `references/rename-checklist.md` for cross-family renames.
   - Classify any remaining hits: intentional / false positive / needs fix.

5. **Apply under constraints** (see AGENTS.md):
   - Agent neutral, size controlled, scope limited, atomic, user-centric, English.
   - **SKILL.md is for the agent**: precise instructions, no verbose rationale.
   - When creating new skills, pass these constraints into the new skill's instructions.

6. **Output**: distillation report using `references/distillation-template.md`.

7. **Approval**:
   - Default: user approval per proposed change.
   - `full-autonomy` mode: auto-approve safe improvements. New skill creation always requires user approval.

## Subagents

Available: use reviewer for gap analysis, writer for drafting changes. Separate analysis from authoring.
Unavailable: self-perform, record limitation.

## Related

Typically follows `review-feedback`. In `solution-delivery-loop`, auto-triggers after each resolved review-feedback cycle under `full-autonomy` policy.