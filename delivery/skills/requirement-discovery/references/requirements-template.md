# Requirements Template (PRD-compatible)

Use for broad, user-facing, multi-module, ambiguous, or long-lived work.

**Section selection guide**:
- P0 (always include): Elevator Pitch, Background/Problem, Scope, Non-Goals, Requirements, Risks/Rollback.
- P1 (include for broad work): User Persona, Contracts/Data Model, Constraints, Open Questions.
- P2 (include for complex multi-stakeholder work): Business/Value Canvas, User Journey, User Story Map, Metadata.

Omit P2 sections for simple features. Omit P1 sections when the compact track note is sufficient.

~~~~markdown
# Requirements v<N>: <Topic>

## 0. Metadata

- Owner:
- Status: draft | review | approved | superseded
- Last updated:

## 1. Elevator Pitch

<one short paragraph: for whom, what problem, what outcome>

## 2. Background / Problem

- Current pain:
- Why now:
- Existing constraints:

## 3. User Persona

| Persona | Situation | Need | Constraint |
|---|---|---|---|
| | | | |

## 4. Business / Value Canvas

- User value:
- Business/project value:
- Success signal:
- Adoption risk:
- Cost/risk:

## 5. User Journey

| Stage | User action | System response | Pain / risk |
|---|---|---|---|
| | | | |

## 6. User Story Map

| Activity | User Story | Priority |
|---|---|---|
| | As a <persona>, I want <capability>, so that <benefit>. | P0/P1/P2 |

## 7. Scope

- In scope:
- Out of scope:

## 8. Non-Goals

| ID | Non-Goal | Reason |
|---|---|---|
| NG1 | | |

## 9. Requirements

Use EARS or Given/When/Then for detailed requirements.

| Req ID | Requirement | Acceptance Criteria | Verification | Priority | Dependencies |
|---|---|---|---|---|---|
| REQ-001 | When <trigger>, the system shall <response>. | Given/When/Then | | P0 | |

## 10. Contracts / Data Model

<schemas, interfaces, route contracts, UI contracts, storage boundaries, compatibility>

## 11. Constraints

- Performance / scale:
- Security / permissions:
- Platform / compatibility:

## 12. Risks / Rollback

| Risk | Impact | Mitigation / Rollback |
|---|---|---|
| | | |

## 13. Open Questions

- [ ] <question>
~~~~
