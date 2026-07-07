# Loop State

Use loop state whenever work spans multiple turns, files, stages, or decisions.

## State record

```yaml
loop_state:
  id: <date-slug>
  kind: crafting|composing|evaluating|investigating|creating|mixed
  phase: Sense|Clarify|Shape|Design|Build|Verify|Record|ContinueStop
  mode: Fidelity|Balanced|Originality
  status: pending|in_progress|blocked|done
  parent_track: <optional>
  active_stage: <optional>
  artifacts: []
  handoffs: []
  open_questions: []
  phase_review:
    verdict: PASS|STABLE|REVISION|FAIL|none
    unresolved_major: 0
  process_audit:
    result: no_change|distillation_needed|distillation_done
  last_checkpoint: <summary>
  next_action: <what happens next>
```

## Update moments

Update loop state after:
- routing decision;
- scope creation or split;
- blueprint approval;
- each build increment;
- every phase review;
- process audit result;
- delivery record;
- pause/resume.

## Resume procedure

1. Read loop state.
2. Read latest handoff and delivery/review records.
3. Verify active phase and unresolved issues.
4. Reconstruct next action.
5. Ask user only if state is ambiguous or a mandatory decision is pending.

## State integrity

- Do not mark parent done until children are done or deferred with approval.
- Do not overwrite old delivery records; append new records.
- If state conflicts with artifacts, trust artifacts and repair state.
