# Phase Review and Process Audit Protocol

Every phase output is reviewed before the loop advances. This is separate from the main Verify phase: phase review checks whether the current phase artifact is safe to hand off; Verify checks the built deliverable before acceptance.

## Phase review insertion point

For each phase from Clarify through Record:

1. Freeze the phase artifact.
2. Load the phase input, current output, prior handoff, open issues, and relevant criteria.
3. Run `inspect` using cumulative context.
4. Classify issues as fix-in-place, rollback, or defer.
5. Fix and re-review until no critical or major issue remains, or rollback to the earliest affected phase.
6. Only then present the checkpoint for user transition.

## Review scope by phase

| Phase output | Review focus | Rollback target |
|---|---|---|
| Clarify | kind, route, phase plan, assumptions | Sense or Clarify |
| Shape | scope, non-goals, acceptance criteria, verification plan | Clarify or Shape |
| Design | feasibility, contracts, increments, dependency graph | Shape or Design |
| Build | deliverable, scope fit, evidence, drift | Shape, Design, or Build |
| Verify | issue quality, verdict support, evidence chain | Build or Verify |
| Record | acceptance evidence, verdict, deferred risk | Build, Verify, or Record |

## Process audit insertion point

After each resolved phase-review cycle, run a lightweight process audit:

- Did the phase skill omit guidance needed to prevent the issue?
- Did a reference/template cause confusion?
- Did the agent repeatedly improvise a reusable sub-process?
- Did trigger wording route to the wrong skill?
- Did the framework add overhead without improving outcome?

If the answer is yes and evidence is concrete, hand off to `distillation`. If not, record "no process change" and continue. Process audit must not create process work from a single weak signal.

## Advancement rule

A phase may advance only when:

- phase artifact exists;
- phase review is passed or stable;
- rollback findings are resolved;
- deferred issues have user approval;
- process audit has either no action or a concrete distillation handoff.
