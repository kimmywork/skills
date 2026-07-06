---
name: review-feedback
description: Use when any phase artifact has been produced and needs independent, cumulative review before the next step proceeds.
license: MIT
metadata:
  author: kenpusney
  version: "0.4.0"
---

# Review & Feedback

## Process

1. **Load context**: current phase output + all prior phase outputs + existing review feedback + relevant criteria.
   Standalone use (no parent workflow): ask user what artifact to review, against what criteria, with what prior context.

2. **Review independently**: check completeness, correctness, consistency, clarity, verifiability, scope adherence.

3. **Tag each issue**:

   ```
   Origin phase: <phase that produced the flawed artifact>
   Severity: critical | major | minor
   Type: missing | incorrect | inconsistent | unclear | scope
   Description: <what is wrong>
   Evidence: <reference to artifact>
   Suggested fix: <concrete next action>
   Resolution: fix-in-place | roll-back
   ```

4. **Output**: structured feedback report using `references/feedback-template.md`.

5. **Route**:
   - All fix-in-place → deliver to current phase producer, wait for fixes, re-review.
   - Any roll-back → deliver report and recommend returning to earliest affected phase.

6. **Close**: all issues resolved or deferred with user approval → mark passed. Next phase proceeds.

## Subagents

Available: use reviewer subagent (read-only) to inspect artifacts and produce report. Pass only the artifacts + review criteria — never the full execution history. Producer handles fixes, reviewer re-checks.
Unavailable: self-perform, record limitation.

## Related

Typically follows any phase skill (`requirement-discovery`, `solution-design`, `implementation-execution`, `delivery-acceptance`). After resolved, `process-distillation` may follow.