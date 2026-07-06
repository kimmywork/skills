# Compact Track Note Template

Use for simple features, bugfixes, maintenance, or small behavior changes that do not need a full requirements doc.

~~~~markdown
# <Feature or Bugfix Title>

## Status

draft | planned | in-progress | blocked | delivered | rolled-back

## Problem / Goal

<real user/system problem and desired outcome>

## Scope

- <included>

## Non-Goals

- <explicitly not included>

## Requirements / Acceptance Criteria

- [ ] Given <context>, when <action>, then <observable binary result>.

## Solution / Plan

- [ ] <verifiable increment or fix step>

## Verification Plan

- `<verification method>` or <manual check>

## Delivery Record

### Changed Areas

- <affected artifacts / components / sections>

### Verification Evidence

- `<verification method>` → <result>

### Final Status

pending | delivered | partial | blocked | needs-user-review

## Change Log

- <date>: <change>
~~~~

Path examples:

- `docs/track/features/<feature-name>.md`
- `docs/track/bugfix/<bug-description>.md`

If the note reveals reusable cross-feature knowledge, update `docs/knowledge`. If work spans multiple sessions, update `.agents/loop-state.md` when present.
