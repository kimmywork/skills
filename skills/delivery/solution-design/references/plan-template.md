# Plan Template

~~~~markdown
# Plan v<N>: <Feature>

## Goal

<one sentence>

## Source Artifacts

- Requirements doc / track:
- Solution design:
- Prior delivery records:
- Change notes:

## Constraints and Non-Goals

- <binding constraint>

## Verifiable Increments

### Increment 1: <name>

**Acceptance covered:** AC/REQ IDs

**Deliverable components / affected artifacts:**
- Create:
- Modify:
- Verify:

**Verification:**
- `<verification method>` → expected result

**Steps:**
- [ ] Define or update verification.
- [ ] Verify failing state when applicable.
- [ ] Produce the increment.
- [ ] Run verification.
- [ ] Refine if needed.
- [ ] Record evidence.

## Acceptance Mapping

| Acceptance / Req | Increment | Verification |
|---|---|---|
| | | |

## Stop Conditions

Pause and revise if:

- unplanned changes to structure, components, or artifacts are required
- contract changes
- touched components or artifacts exceed estimate by ~2x
- acceptance becomes invalid or untestable
- shim/fallback/deprecated alias is needed but not planned
- user-facing behavior changes beyond scope

## Risks / Rollback

| Risk | Mitigation | Rollback |
|---|---|---|
| | | |
~~~~
