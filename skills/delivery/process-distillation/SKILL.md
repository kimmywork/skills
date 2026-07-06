---
name: process-distillation
description: Use when recurring phase friction, repeated review feedback, or resolved phase cycles suggest skill or process improvements.
license: MIT
metadata:
  author: kenpusney
  version: "0.5.1"
---

# Process Distillation

## Process

1. **Gather context**: phase executed, artifacts produced, review feedback report, fix outcomes, execution observations. If context insufficient, explore agent session logs or memory stores as fallback.

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

3. **Evaluate options**: small fix / new reference / new atomic skill / no change. Prefer small fix (1–5 lines) over new skill. New skill creation always requires user approval.

4. **Self-review**: every claim must cite file evidence. Before rename, inventory affected files with grep. After changes, re-grep to confirm zero remaining hits. Use `references/rename-checklist.md` for cross-family renames. Classify remaining hits: intentional / false positive / needs fix.

5. **Apply under AGENTS.md constraints**: agent neutral, size controlled, scope limited, atomic, user-centric, English. SKILL.md is for the agent: precise instructions, no verbose rationale. When creating new skills, pass these constraints into the new skill's instructions.

6. **Output**: distillation report using `references/distillation-template.md`.

7. **Approval**: default is user approval. `full-autonomy` mode: auto-approve safe improvements. New skill creation always requires user approval.

## Subagents

Available: use reviewer for gap analysis, writer for drafting. Separate analysis from authoring. Unavailable: self-perform, record limitation.

## Related

Typically follows `review-feedback`. In `solution-delivery-loop`, auto-triggers after resolved review-feedback cycles under `full-autonomy`.
