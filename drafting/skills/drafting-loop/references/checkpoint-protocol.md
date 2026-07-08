# Adaptive Checkpoint Protocol

Checkpoints keep long work honest without making every turn heavy. A checkpoint occurs only after the current phase artifact has passed phase review and process audit.

## Types

| Type | Use when | Required content |
|---|---|---|
| FULL | First checkpoint, major transition, quality concern, after 4 slim continues | kind, phase, deliverables, evidence, flagged issues, choices |
| SLIM | User has continued through non-critical phases twice | one-line status, next phase, continue/pause prompt |
| MANDATORY | scope change, blueprint approval, inspect verdict, acceptance-gate, compliance override | explicit decision request; do not proceed until user answers |

## FULL template

```text
--- Phase [N] [Name] complete ---
Kind: [kind]
Deliverables: [paths or summaries]
Evidence: [fresh verification]
Flagged: [issues or None]
Next: [phase]
Options: continue / adjust / review details / pause
```

## Self-check before showing FULL

- Quality trajectory: output is not worse than the prior phase.
- Scope discipline: no undisclosed additions.
- Completeness: required deliverables exist.
- Evidence: material claims have support.

If any answer is weak, surface it in `Flagged` and make the checkpoint MANDATORY. If phase review has unresolved critical or major issues, do not present an advancement checkpoint; route to fix or rollback first.
