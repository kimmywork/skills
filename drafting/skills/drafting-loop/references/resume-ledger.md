# Resume Ledger

Use for long-running loops, context resets, paused work, or multi-session continuation. This generalizes passport/reset-boundary ideas without depending on a specific runtime.

## Purpose

A resume ledger lets a future session continue from a verified boundary without trusting stale conversation memory.

## Boundary entry

Append a boundary entry at FULL or MANDATORY checkpoints, after phase review passes.

```yaml
ledger_entry:
  kind: boundary
  id: <date-time-or-sequence>
  phase: Sense|Clarify|Shape|Design|Build|Verify|Record|ContinueStop
  kind_of_work: crafting|composing|evaluating|investigating|creating|mixed
  artifacts: []
  handoff: <path-or-summary>
  phase_review: PASS|STABLE
  process_audit: no_change|distillation_needed|distillation_done
  pending_decision: null|<question>
  next_options:
    - label: <option>
      next_phase: <phase>
      risks: []
  hash: sha256:<optional>
```

## Resume command shape

A user may say:

```text
resume from <ledger id or hash>
```

The agent must:
1. Load the ledger entry and linked artifacts.
2. Verify no later entry supersedes it.
3. If `pending_decision` exists, ask that decision first.
4. Reconstruct loop state from artifacts, not memory.
5. Continue at the recorded next phase or user-selected option.

## Append-only rules

- Do not rewrite old boundary entries.
- Add a new `kind: resume` entry when a boundary is consumed.
- Add a new boundary after the next successful phase review.
- If artifacts conflict with ledger state, trust artifacts and record repair.

## What this does not do

- It does not make work reproducible by itself.
- It does not replace delivery records.
- It does not allow skipping mandatory decisions.
- It does not require any particular runtime or subagent system.
