# Guard Rules

Read this when a system or review needs to stay fixed after the current task. A rule that cannot fail is documentation, not a guard.

## Drift types

- **Value drift** — a color, size, radius, duration, or type value that is not in the token source.
- **Component drift** — a native or ad-hoc component that bypasses the system, or a component used without its specified states.
- **Semantic drift** — copy that contradicts the term table, a screen with more than one accent family, or a behavior that contradicts a stated principle.

## Ratchet

Register known violations in a `KNOWN` list with a rule id, file, and a short text fingerprint. The check reports them as pending and fails only on new violations. When a known violation is fixed, remove its line; the rule then becomes a hard failure. A ratchet lets a legacy codebase adopt the guard without a flag day.

## Mutation self-test

For every rule, include a test that injects a violation into a temporary copy and asserts that the check fails. If the check stays green, the rule has no coverage. The self-test must pass wherever the check runs; wiring it into CI is implementation work, not part of authoring the guard. A green check with untested coverage is not evidence.

## Rule examples

- No raw color literals outside the theme file.
- No native dialog or button where the system defines one.
- Every clickable size is at least the declared target (44×44 web, 48×48 mobile), never below the WCAG 24×24 floor, or declares an expanded hit area.
- Every full-screen overlay registers a back action.
- Every term in the copy table appears in the implementation.
- A color palette row fits the available width.
- A screen uses at most one accent family.

These are examples, not a fixed list. Derive the rules from the defects the review actually found.

## From review to rule

For each durable finding, ask: what would have caught this before release? Write the smallest rule that would fail on the defect, add a mutation test, and include it in the guard deliverable. Do not write a rule for a one-off preference; do write one for a class of defect.

## Anti-patterns

- A rule that only checks documentation, never the implementation.
- A rule with no negative test.
- A `KNOWN` list that grows and is never reduced.
- A guard that fails on style while the interaction remains broken.
- A rule so broad that every change requires an exception.

## Sources

The ratchet and drift-check pattern is a general practice; adapt the rule set to the project rather than copying it.
