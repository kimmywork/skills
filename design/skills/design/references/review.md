# Review

Read this in Review mode. It covers what to inspect, how to grade, and how to report. Use it as a prompt; derive the product-specific questions.

## Dimensions

Use only what matters, but state what you skipped:

1. Reachability and task completion — can the user start, finish, and recover?
2. States and feedback — empty, loading, error, partial, over-full; what the system says it is doing.
3. Consistency — components, copy, tokens, platform conventions.
4. Hierarchy and information architecture — what competes, what is buried, what is named.
5. Interaction correctness — displayed order matches behavior; destructive paths; gestures; undo.
6. Platform context — touch, keyboard, IME, safe areas, back, orientation, font scaling.
7. Accessibility — use `references/accessibility.md`.
8. Content and copy — term parity, plain language, error messages.
9. Visual craft — type scale, spacing scale, dark mode as a redesign, density, motion.
10. Trust and ethics — dark patterns, destructive confirmation, privacy, data ownership, system effects.

## Severity

- **P0 — blocking or data risk.** A core task cannot be completed, data can be lost or corrupted, a destructive action is unrecoverable, a critical surface is unreadable, or the product crashes or hangs.
- **P1 — important.** Efficiency or accessibility is materially reduced, a platform convention is broken, a state is missing, or an inconsistency causes errors.
- **P2 — polish.** Consistency, copy, density, and minor accessibility.

Grade by impact, frequency, recoverability, and reach. Do not grade by how easy the fix looks.

## Evidence

Label every finding: `[S]` static, `[D]` dynamic, `[R]` real device or reader, `[M]` measured, `[C]` cited standard, `[I]` inference. A finding without evidence is a hypothesis; say so.

## Issue register

Every finding has: id, location (file:line, URL, screen, frame), observation, evidence class, impact, severity, acceptance criterion, and suggested action. The acceptance criterion must fail today and pass when fixed.

## Report

Open with scope, method, and the decision the review supports. Then: root causes, strengths to keep, findings by severity, conflict adjudication, fix plan, guard rules, and an independence and coverage statement. A review that only lists defects is incomplete.

## Conflict adjudication

Where specification and implementation disagree, decide which is wrong — specification, implementation, or an outdated specification — and record why. Do not default to either side.

## Fix plan

Order increments by risk and dependency. For each: output, preconditions, actions, verification, done-definition. Pre-mortem the riskiest fix: what could it break, and how would you know?

## Independence and bias

State whether this was self-review, AI-assisted, automated, or independent. Name what was not tested. Check for confirmation bias, recency, anecdote, expert blind spot, curse of knowledge, novelty bias, sunk cost, and HIPPO. Counter with disconfirming evidence, an independent view, or a steelman of the alternative.

## Anti-patterns

- Taste presented as a criterion.
- An exhaustive list of preferences with no priority.
- Severity assigned by fix effort.
- A review with no strengths, no method, or no limits.
- A fix plan with no acceptance criterion.
