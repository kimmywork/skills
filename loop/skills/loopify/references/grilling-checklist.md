# Grilling Checklist

Use during `loopify` workflow creation. Cover all items before drafting. Also watch for domain-specific gaps beyond this list.

## Checklist

- [ ] ✅ **Trigger/schedule conditions**: When does this run? (cron time, event/command trigger, or both)
- [ ] ✅ **Step boundaries**: What are the concrete steps? Each must be executable by an agent without guessing.
- [ ] ✅ **Success condition**: What counts as done? Must be verifiable (file exists, test passes, CI green, etc.).
- [ ] ✅ **Empty/error handling**: What happens when there are 0 items? What happens when a step fails?
- [ ] ✅ **What NOT to do**: What actions should the agent avoid? (don't delete, don't modify, don't notify)

## Additional probes

Based on the user's domain, also consider:

- **Scope limits**: How many items to process? Any filters?
- **Output format**: Where should results go? (file, PR comment, Slack, stdout?)
- **Rate limits**: Any API rate limits or cooldowns between steps?
- **Auth requirements**: Does the workflow need credentials? How to obtain them without user input?
- **Rollback**: If something goes wrong, how does the agent undo partial work?
- **Trigger semantics**: What does a trigger exit code mean? Exit 0 + output → fire. Exit 0 + empty → normal skip. Non-zero exit → normal skip (command determined nothing to do). Exceptions/timeout → error (check setup).