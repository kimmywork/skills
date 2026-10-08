---
name: parkinglot
description: Park out-of-scope issues, improvement ideas, and tangents found during a task in PARKING_LOT.md instead of acting on them, then review parked items in batches to find shared causes and decide each item's fate. Use when you notice something worth improving outside the current task, when the user says to park or note something for later, or when the user asks to review, triage, or process the parking lot.
---

# Parking Lot

Keep the current task focused without losing worthwhile observations. Record out-of-scope items now; act on them later as a batch. A batch exposes patterns that single fixes miss: several local symptoms often share one cause and one better solution.

## Capture

Park an item when it is worth revisiting but outside the current task's scope: a code smell, refactoring opportunity, inconsistency, missing test, doc gap, or open question.

- Do not fix, refactor, or expand scope to address a parked item. Record it and return to the task.
- Do not park work the current task requires. If an item blocks the task, or poses a correctness, security, or data-loss risk, report it to the user now; park it only if the user defers it.
- Skip trivial noise. If unsure whether an item is worth parking, park it briefly; review removes unneeded items cheaply.
- Before adding an item, check for an existing open item about the same issue; extend that item instead of duplicating it.
- Write a synopsis that someone without this session's context can verify later: location, observed evidence, and why it matters.
- Run `date +%F` for the item date. Assign the next unused `P-<n>` ID.

## File

Follow an explicit repository convention for deferred issues when one exists. Otherwise use `PARKING_LOT.md` at the repository or workspace root, created on first use:

```markdown
# Parking Lot

Out-of-scope items deferred for batch review.

## Open

### P-1 (YYYY-MM-DD) One-line synopsis
- Where: `path/to/file:line`, section, or artifact
- Observed: concrete evidence or symptom
- Why it matters: expected impact
- Found during: task that surfaced it

## Assigned

### P-2 (YYYY-MM-DD) One-line synopsis
- Decision: defer | delegate
- Who: owner, subgroup, or future task
- What: agreed next action
- When: date, milestone, or trigger
```

Keep the file current, not historical. Remove deleted and resolved items; version history and commit messages preserve their record. Agent-written entries are in English unless the project convention differs.

## Closing a task

Before reporting the current task as complete, state in the user's language how many items were parked during it, with their IDs and synopses. Do not start working on them without approval. If the parking lot has many open items, suggest a review instead of starting one.

## Review

Run a review when the user asks, or at a milestone the user has agreed to.

1. Read all open items. Re-check each against the current state; mark items that no longer reproduce or apply.
2. Group items by shared cause, pattern, or affected area before you consider individual fixes. For each group, look for one solution that resolves the cause, not one patch per symptom.
3. Propose a decision for each item or group:
   - **Delete**: no longer relevant, invalid, or not worth the cost.
   - **Resolve**: act now, preferably as one change per group.
   - **Defer**: keep for a later session, milestone, or trigger.
   - **Delegate**: hand off to a specific owner, issue tracker, plan, or separate task.
4. Present the groups, proposed solutions, and decisions. Wait for the user's confirmation before changing anything beyond the parking lot file.
5. Apply the confirmed decisions. Record who, what, and when for every deferred or delegated item under `Assigned`. Remove deleted and resolved items after verifying the resolution.

Do not leave a review without a decision for every item; an unprocessed parking lot stops being trusted and stops being used.

## Output

In the user's language, report the items added or changed, their IDs, the groups and shared causes found during review, the decision for each item, and the verification for any resolved items.
