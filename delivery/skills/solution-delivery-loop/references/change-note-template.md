# Change Note Template

Use when implementation invalidates or changes approved scope, architecture, contract, acceptance, or verification.

~~~~markdown
# Change Note <NNNN>: <Topic>

## Linked Work

- Requirements / track:
- Solution design:
- Plan:
- Delivery record:

## Discovery Phase

sense | shape | design | build | verify | record

## Original Decision

<summary or path + section>

## Problem Found

<what made the original design invalid or insufficient>

## New Decision

<new design/scope/contract/acceptance>

## Impact

- User behavior:
- Modules/files:
- Data/contracts:
- Tests/verification:
- Cross-feature knowledge to update in `docs/knowledge`:
- Risks:

## Approval / Rationale

<who/what approved it, or why autonomous change was safe>

## Verification Update

- <new/changed verification>

## Scope Reduction

Use when approved scope is reduced or deferred. Document what was cut, why, and when it may be revisited.

- Original scope items removed:
- Reason:
- Impact on later phases:
- Deferred decisions:
- Revisit trigger:
~~~~
