---
name: plan-execution
description: Execute a defined task, plan, or constrained deliverable while preserving scope, evidence, and change awareness. Use when the user wants the work done and the target is clear enough to start, even if some lightweight decomposition or blocker handling is still needed.
---

# Plan Execution

Build the requested thing without losing scope control or verification evidence.

## Load

- `references/increment-record.md`
- `references/execution-control.md`
- `references/software-mode.md` for code/config/infrastructure work
- `../drafting-loop/references/change-note-template.md`
- `../drafting-loop/references/iron-rules.md`

## Preconditions

- Goal or scope is clear enough to start.
- A blueprint exists for non-trivial or risky work; for simple work, create a lightweight execution plan inline.
- Acceptance criteria and a reasonable verification method are known.

If those conditions are not met, stop and tighten the task definition instead of inventing it.

## Workflow

1. Perform the before-editing scan from `references/execution-control.md`.
2. Restate the active task, constraints, acceptance criteria, and evidence plan.
3. If the task is large, decompose it into the smallest verifiable increment before changing anything.
4. Execute the smallest verifiable increment.
5. Record changed artifacts, assumptions, and evidence.
6. Run planned checks or the closest available checks.
7. Apply stop conditions, blocker handling, scope-map updates, and change control from `references/execution-control.md`.
8. If the task turns into review-only or investigation-only work, say so and switch to that task type instead of forcing generic execution.
9. End with completion status, limitations, and the next stage.

## Kind-specific execution

- Crafting: use software-mode when relevant; verify dependents and contracts.
- Composing: draft against brief, sources, audience, and style constraints.
- Creating: produce draft options, then converge against constraints.

## Output

End with an increment record and a completion note ready for independent review or delivery decision.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
