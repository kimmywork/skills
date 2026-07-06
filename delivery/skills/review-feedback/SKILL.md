---
name: review-feedback
description: Use when any phase artifact has been produced and needs independent, cumulative review before the next step proceeds.
license: MIT
metadata:
  author: kenpusney
  version: "0.6.1"
---

# Review & Feedback

## Process

1. **Load context**: current phase output + all prior phase outputs + existing review feedback + relevant criteria. Standalone use (no parent workflow): ask user what artifact to review, against what criteria, with what prior context.

2. **Review independently**: completeness, correctness, consistency, clarity, verifiability, scope adherence.

3. **Tag each issue**:

   ```
   Origin phase: <phase>
   Severity: critical | major | minor
   Type: missing | incorrect | inconsistent | unclear | scope
   Description: <what is wrong>
   Evidence: <reference>
   Suggested fix: <next action>
   Resolution: fix-in-place | roll-back
   ```

4. **Output**: structured feedback report using `references/feedback-template.md`.

5. **Route**: all fix-in-place → deliver to producer, wait for fixes, re-review. Any roll-back → recommend returning to earliest affected phase.

6. **Close**: all issues resolved or deferred with user approval → passed. If no critical or major issues remain and only minor polish items are open → stable (further reviews optional). Critical/major remain → fail, re-review after fixes.

For multi-part deliverables, perform distinct review passes:
1. **Accuracy**: verify facts, citations, claims against primary sources.
2. **Validity**: check logic, argument structure, causal chains. Watch for strawman arguments.
3. **Consistency**: verify cross-reference integrity, no contradictions, fixes didn't introduce new breaks.

## Subagents

Available: use reviewer subagent (read-only). Pass only artifacts + criteria — never full execution history. Unavailable: self-perform, record limitation.

## Related

Typically follows any phase skill. See `solution-delivery-loop` for resolution protocol.
