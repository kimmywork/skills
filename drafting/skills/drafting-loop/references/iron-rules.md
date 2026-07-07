# Iron Rules

Iron rules are framework invariants. They apply across every skill, work kind, phase, and fast-pass path.

| ID | Rule | Meaning | Enforcement |
|---|---|---|---|
| IR-1 | No phase skipping | Required phase obligations must be satisfied or explicitly fast-passed with rationale. | Check `state-machine.md` before transition. |
| IR-2 | Evidence, not confidence | Acceptance and review claims require fresh evidence. | Delivery record maps criteria to evidence. |
| IR-3 | Human owns state | Mandatory checkpoints require explicit user direction. | Do not advance past mandatory checkpoints silently. |
| IR-4 | No scope creep | New scope, weakened criteria, or changed assumptions need a change note. | Write change note before execution. |
| IR-5 | No rubric leakage | Builder should not see hidden evaluation keys before drafting. | Use `ground-truth-isolation.md`. |
| IR-6 | Pressure is not evidence | User pressure or model certainty cannot override contrary evidence. | Preserve findings unless evidence changes. |
| IR-7 | No concealed drift | Deviations from scope, design, source, format, or contract must be disclosed. | Record drift in handoff and delivery record. |
| IR-8 | No partial completion claims | Unverified or incomplete criteria must be marked deferred, blocked, or failed. | Acceptance table must include every criterion. |
| IR-9 | No unresolved phase review | Critical/major phase-review issues block transition. | Fix, rollback, or defer with approval. |
| IR-10 | No process theater | Process steps must improve correctness, clarity, or evidence. | Process audit can record no-op when no improvement exists. |

## Gate check

Before handoff, checkpoint, or final response, answer:

1. Which phase obligations are complete?
2. Which criteria have fresh evidence?
3. Which criteria are deferred, blocked, or failed?
4. Did the work add scope, alter contracts, or weaken requirements?
5. Did phase review pass or route rollback?
6. Is user approval mandatory now?

If any answer is unknown, do not claim completion.
