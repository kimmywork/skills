# Transition Reinforcement

At phase transitions, include a compact reminder to prevent context drift.

```text
Transition: [from] -> [to]
Relevant iron rule: [rule]
Relevant anti-pattern: [avoid]
Quality trajectory: [same/better/worse/unknown]
Checkpoint: [none/slim/full/mandatory]
```

## Focus table

| Transition | Reinforce |
|---|---|
| Sense -> Clarify | Do not guess ambiguous intent. |
| Clarify -> Shape | Do not invent users, criteria, or scope. |
| Shape -> Design | Acceptance criteria must be verifiable. |
| Design -> Build | No build before approved design or recorded fast-pass. |
| Build -> Verify | Freeze deliverable before review. |
| Verify -> Build | Fix only review findings unless change note is approved. |
| Verify -> Record | No delivery without fresh evidence. |
| Record -> ContinueStop | Next action must be explicit. |
