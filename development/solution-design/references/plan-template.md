# Plan Template

~~~~markdown
# Plan v<N>: <Feature>

## Goal

<one sentence>

## Source Artifacts

- PRD / track:
- Solution design:
- Prior delivery records:
- Change notes:

## Constraints and Non-Goals

- <binding constraint>

## Task Slices

### Slice 1: <name>

**Acceptance covered:** AC/REQ IDs

**Files / modules:**
- Create:
- Modify:
- Test:

**Verification:**
- `<command or manual check>` → expected result

**Steps:**
- [ ] Define or update test/verification.
- [ ] Verify red/failing state when applicable.
- [ ] Implement minimal change.
- [ ] Run verification.
- [ ] Refactor if green.
- [ ] Record evidence.

## Acceptance Mapping

| Acceptance / Req | Slice | Verification |
|---|---|---|
| | | |

## Stop Conditions

Pause and revise if:

- unplanned module/package changes are required
- contract changes
- touched files/modules exceed estimate by ~2x
- acceptance becomes invalid or untestable
- shim/fallback/deprecated alias is needed but not planned
- user-facing behavior changes beyond scope

## Risks / Rollback

| Risk | Mitigation | Rollback |
|---|---|---|
| | | |
~~~~
