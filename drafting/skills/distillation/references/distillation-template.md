# Distillation Template

Use when phase review, process audit, delivery, or repeated execution reveals reusable process improvement.

## Gap dimensions

Classify the process gap before proposing a change.

| Dimension | Question | Typical fix |
|---|---|---|
| Coverage gap | Should a skill/reference have described this step but did not? | Add or expand reference; add SKILL pointer. |
| False guidance | Did existing guidance mislead the executor? | Correct or remove misleading rule. |
| Missing guardrail | Did review catch something the workflow should prevent earlier? | Add gate, checklist, or anti-pattern. |
| Repeated improvisation | Did the executor reinvent the same helper or procedure? | Extract a template, script, or reference. |
| Atomic extraction | Is there a clear bounded sub-process worth its own skill? | Propose a new skill only with user approval. |
| Context overhead | Is the skill too large or loading irrelevant detail? | Move detail to references or narrow trigger. |
| Trigger misfire | Did description/routing cause wrong skill activation or missed activation? | Adjust description or triage. |
| Scope boundary | Does the fix belong outside this plugin bundle? | Do not add; record limitation. |
| User-specific preference | Is this only one user's taste, not reusable process? | Do not change framework; record preference elsewhere. |

## Distillation report

```markdown
# Process Distillation: <title>

## Trigger

What happened? Include phase, artifact, review issue, or user feedback.

## Evidence

| Evidence | Source | Why it matters |
|---|---|---|

## Gap classification

| Dimension | Present? | Evidence | Fix candidate |
|---|---|---|---|
| Coverage gap | yes/no | | |
| False guidance | yes/no | | |
| Missing guardrail | yes/no | | |
| Repeated improvisation | yes/no | | |
| Atomic extraction | yes/no | | |
| Context overhead | yes/no | | |
| Trigger misfire | yes/no | | |
| Scope boundary | yes/no | | |
| User-specific preference | yes/no | | |

## Pattern

What general failure or reusable success does this show?

## Options considered

| Option | Change type | Pros | Risks | Decision |
|---|---|---|---|---|

Change types: skill edit, reference edit, template edit, script, routing description, new skill proposal, no change.

## Proposed improvement

Smallest durable change. Avoid overfitting.

## Bundle-scope check

- In-bundle only:
- No duplication:
- Skill still focused:
- SKILL.md remains under 100 lines:
- References hold detailed semantics:

## Verification

How future runs will know this helped.

## Applied files

## Residual risks
```

## Decision rule

Make no process change when evidence is weak, one-off, outside bundle scope, or better handled as user-specific preference.
