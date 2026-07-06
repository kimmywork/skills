# Review Feedback Report

## Metadata

- **Reviewer**: <subagent / self-performed>
- **Phase reviewed**: <phase name>
- **Artifacts inspected**: <paths or descriptions>
- **Prior phases considered**: <list>
- **Review date**: <date>

## Summary

- **Total issues**: <count>
- **Critical**: <count>
- **Major**: <count>
- **Minor**: <count>
- **Fix-in-place**: <count>
- **Roll-back**: <count>
- **Verdict**: pass | conditional-pass | fail

## Issues

### Issue <N>: <short title>

| Field | Value |
|---|---|
| **Origin phase** | <phase name> |
| **Severity** | critical / major / minor |
| **Type** | missing / incorrect / inconsistent / unclear / scope |
| **Description** | <what is wrong> |
| **Evidence** | <reference to artifact, line, section> |
| **Suggested fix** | <concrete next action> |
| **Resolution** | fix-in-place / roll-back |

### Issue <N+1>: ...

## Fix-in-place items

Items the current phase producer can resolve. After fixes, re-review is needed.

## Roll-back items

Items that require returning to an earlier phase. List the earliest affected phase and which subsequent phases must re-execute.

## Positive observations

What the reviewed artifact did well. Useful for `process-distillation` and team learning.

## Open questions

Any unresolved questions that the producer should address.