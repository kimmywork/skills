---
name: loopify
description: Create a workflow spec from a natural language description. Agent-assisted iterative refinement — grills for clarity, drafts the spec, writes `workflows/<name>.md` on user confirmation.
---

# loopify — Workflow Creation Skill

## When to invoke

User describes a recurring task they want automated (e.g. "check stale PRs every morning").

## Process

1. **Grill for clarity**: one question at a time. Use `references/grilling-checklist.md` as a baseline — but also watch for domain-specific gaps beyond it.
2. **Draft** after 2-3 rounds (or when all checklist items are covered).
3. **Present draft** for user confirmation.
4. **Write file**: `workflows/<name>.md`
5. **Verify**: run `python3 <loopy-skill-root>/scripts/loopy.py --dry-run` and confirm the workflow appears in the output without errors.

## Slug rules

`name` is lowercased, spaces→hyphens, special characters stripped, max 64 chars. The front-matter `name` must match the filename.

## Output validation

Before writing, verify:
- `name` field exists and matches filename
- At least one of `schedule` or `trigger` is present
- Body includes a verifiable success condition
- Each step is concrete enough for an agent to execute without guessing
- Edge cases addressed: 0 items, errors, what NOT to do

## References

- `references/grilling-checklist.md` — baseline clarity probes