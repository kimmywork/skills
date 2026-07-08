# Failure Paths

Use this table when a loop stalls, quality drops, or a gate fails.

| Scenario | Trigger | Recovery | Return phase |
|---|---|---|---|
| Intent will not converge | more than 5 clarification turns | Offer 3 candidate scopes and ask user to choose. | Clarify |
| Cross-phase confusion | materials span requirements, design, draft, review | Use triage and ask full loop vs resume vs review. | Clarify |
| Scope expands during build | new requirement, artifact, field, or audience appears | Stop, write change note, ask for approval. | Shape |
| Design infeasible | blueprint marks a choice Redesigned | Return with alternatives and constraints. | Shape |
| Contract drift | interface, schema, data model, section contract changes | Inventory dependents and revise blueprint. | Design |
| Verification fails | planned check fails or evidence contradicts claim | Fix current increment or rollback if design/scope is wrong. | Build/Design |
| Evidence missing | claim cannot be verified | Mark unknown, remove claim, request source, or revise scope. | Build/Verify |
| Critical review issue | critical/major issue remains | Fix, rollback, or defer only with explicit approval. | Earliest affected |
| Quality regression | later artifact weaker than prior artifact | Pause, reload scope/design, narrow increment. | Prior phase |
| Revision loop stalls | 3 rounds without meaningful delta | Recommend stop, split, or escalate to user decision. | ContinueStop |
| Compliance override repeats | same gate repeatedly overridden | Apply override ladder and append rationale. | Compliance/Record |
| User stops mid-loop | explicit stop or no approval | Save state and re-entry instructions. | ContinueStop |
| Process overhead grows | process step adds work without quality gain | Run process audit and distill or remove. | Distillation |

## Recovery record

```markdown
## Failure Recovery
- Scenario:
- Evidence:
- Earliest affected phase:
- Options:
- Chosen path:
- Verification after recovery:
```
