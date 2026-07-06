---
status: done
scope_type: standalone
created: 2026-07-07
version: 1
---

# Process Discipline: Track-First Workflow

## Problem

Agent skips the Sense → Shape → Design → Build → Verify → Record cycle. When user says "start implementing", agent jumps to coding without creating track docs, making review-feedback impossible to invoke.

## Root cause

1. "Start implementing" interpreted as permission to skip process, not as "scope confirmed, proceed formally"
2. No track doc = no artifact to review = review-feedback has nothing to inspect
3. Review and acceptance only happen when user manually invokes them

## Requirements

### R1: Track-first rule
No code/edit/implementation before `requirements-v1.md` exists with `scope_type` and `status: in_progress`.

### R2: Phase gate enforcement
Each phase transition requires review-feedback. The loop skill must check: did the previous phase output get reviewed?

### R3: Acceptance not skipped
delivery-acceptance runs automatically after implementation completes, not only on user invocation.

## Acceptance Criteria

- Agent creates track doc before any file edits
- review-feedback is invoked between each phase pair
- delivery-acceptance runs after implementation without user prompting
