# Loop Operations

Operational rules for cold start, resume, autonomy, and continuity.

## First move

1. Inspect active loop state, track docs, requirements, plans, delivery records, review feedback, change notes, knowledge/log material, and relevant artifacts.
2. Identify current phase and missing prerequisites.
3. Right-size context: stop reading when more context will not change the next action.
4. Route:
   - unclear need -> Clarify or Shape;
   - clear scope -> Design;
   - executable plan -> Build;
   - built artifact -> Verify;
   - passed review -> Record;
   - delivered work -> Continue/Stop or Distillation.

## Autonomy

Autonomy level changes checkpoint frequency, not evidence requirements.

| Mode | Meaning | Limits |
|---|---|---|
| supervised | ask at mandatory checkpoints and when ambiguity blocks | default |
| full | proceed through non-critical slim checkpoints | cannot skip mandatory checkpoints, phase review, or evidence gates |

## Continuity

On resume:

1. Read resume ledger if present.
2. Read latest track state and delivery/review records.
3. Verify artifacts still exist.
4. Reconstruct next action from artifacts, not memory.
5. Ask user if mandatory decision or ambiguity remains.

## Gate rule

Autonomy does not waive:
- track notes for multi-phase work;
- phase review;
- change notes for drift;
- verification evidence;
- delivery records;
- user approval for mandatory decisions.
