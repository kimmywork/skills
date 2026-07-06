# Increment Record and Save

Use at the end of each increment in the execution loop.

## Evidence recording

Each increment's verification record must include:

| Field | Description |
|---|---|
| What was checked | The verification method or criterion applied |
| Result | The finding, output, or observation |
| Conclusion | pass/fail or confirmed/unconfirmed |

Format: `Verification: <what> → <result> → <conclusion>`

Examples:
- `Verification: run tests → 12/12 pass → pass`
- `Verification: check claim against source X → confirmed → confirmed`
- `Verification: review section for consistency → no contradictions → pass`

Record evidence in the delivery record, track note, or work log — wherever the increment's outcome is documented.

## Save the increment

Each increment must be independently saveable and reversible.

### Version-controlled deliverables

Commit with the format: `<type>(<scope>): <description>`

Common types:
- `feat`: new capability
- `fix`: bug or error correction
- `refactor`: restructure without behavior change
- `docs`: documentation only
- `test`: add or update tests

Rules:
- All existing tests must pass before committing.
- Each commit must not break prior commits.
- One commit per increment. Do not batch unrelated changes.

### Other deliverables

Save to the track folder with a version marker:
- Append `-v<N>` suffix (e.g., `design-v2.md`).
- Or use dated suffix (e.g., `design-2026-07-06.md`).
- Each saved version must not break prior versions.

### Reversal

Every increment must be reversible:
- Version-controlled: `git revert` or `git checkout` to prior commit.
- Track folder: restore previous version from version marker.
- If an increment cannot be reversed, document why and add a rollback plan.
