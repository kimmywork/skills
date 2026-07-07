# Ground-Truth Isolation

Ground-truth isolation separates generation from evaluation so outputs are not tailored to hidden answer keys or review rubrics.

## Layers

| Layer | Content | Builder access | Reviewer access |
|---|---|---|---|
| L1 Raw | user request, source material, drafts, unverified claims | yes | yes |
| L2 Verified | outputs that passed review, accepted decisions, delivery records | yes | yes |
| L3 Rubric | acceptance criteria, scoring keys, hidden tests, adversarial checks | no before draft | yes |

## Rules

1. Builder works from L1/L2 and visible user constraints.
2. Reviewer may load L3 and produce natural-language feedback.
3. Builder receives review findings, not hidden scoring keys, unless user made the rubric shared.
4. If rubric is shared, mark `shared_rubric: true` in handoff.
5. Freeze draft before loading reviewer-only criteria.
6. Do not rewrite while reviewing; revise only after feedback exists.
7. Record exceptions in delivery record.

## Single-agent implementation

When no separate reviewer exists:

1. Finish and freeze the draft.
2. Start a separate review section.
3. Load criteria/rubric only after freezing.
4. Produce a review report without editing the draft.
5. Start a separate revision pass using findings.

## By kind

| Kind | L3 examples |
|---|---|
| Crafting | hidden tests, performance thresholds, security checklist |
| Composing | style guide, citation policy, word-count target, required structure |
| Evaluating | severity definitions, compliance standards, audit rubric |
| Investigating | evidence hierarchy, confidence threshold, source protocol |
| Creating | brief, constraints, style direction, reference works |

## Failure signals

- Review finds output parroting rubric language without evidence.
- Builder changes criteria mid-build.
- Acceptance criteria are weakened after failure.
- Reviewer and builder reasoning are mixed in one unstructured pass.

If any signal appears, pause and re-run from the earliest contaminated phase.
