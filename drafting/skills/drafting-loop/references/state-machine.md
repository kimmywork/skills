# Drafting Loop State Machine

## States

| State | Meaning | Required material |
|---|---|---|
| Sense | request/material intake | user request and material inventory |
| Clarify | routing and ambiguity resolution | sense output or user clarification |
| Shape | scope and acceptance definition | clarified intent |
| Design | executable plan or fast-pass rationale | scope output |
| Build | deliverable production or audit execution | blueprint or approved fast-pass |
| Verify | independent quality check | build output and criteria |
| Record | evidence-based acceptance | verify output and fresh evidence |
| ContinueStop | next increment, iteration, stop, or distillation | delivery record |

## Legal transitions

- Sense -> Clarify -> Shape -> Design -> Build -> Verify -> Record -> ContinueStop.
- Each phase transition includes phase review and lightweight process audit before checkpoint advancement.
- Clarify may route directly to a later phase only when prerequisite artifacts are present and named.
- Design may fast-pass for Evaluating, Investigating, or Creating only when the handoff records why full design is unnecessary.
- Verify -> Build is legal for fix-in-place revisions.
- Verify -> Shape or Verify -> Design is legal for rollback findings.
- Record -> Build is legal for the next increment after a delivery record.

## Illegal transitions

- Any phase -> Record without Verify evidence.
- Shape -> Build for Crafting without Design approval.
- Build -> Record without inspect or explicit user risk acceptance.
- Any phase -> ContinueStop while critical open questions remain unnamed.
- Any scope expansion without a change note.
- Any phase advancing with unresolved critical/major phase-review issues.

## Material dependency matrix

| Target phase | Must have |
|---|---|
| Shape | clarified goal, kind, constraints or blocking questions |
| Design | scope, non-goals, acceptance criteria, verification plan |
| Build | design or fast-pass rationale, active increment, checks |
| Verify | frozen deliverable, scope criteria, evidence access |
| Record | review verdict, fresh verification, limitations |

## Transition check

Before transition, state source phase, target phase, artifacts, phase-review verdict, process-audit result, evidence status, unresolved risks, and whether user approval is mandatory.
