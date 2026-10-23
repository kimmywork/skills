---
name: design
description: Build, extract, rebuild, or govern a design system, and review a product, interface, or design artifact against design quality criteria. Use for design systems, tokens, themes, visual and interaction language, UX/UI audits, heuristic evaluations, accessibility reviews, design critiques, dark-pattern checks, pre-release design gates, or when someone asks what is wrong with an interface and what to fix first.
---

# Design

Design is decision-making under constraint. This skill builds the system that makes design coherent, and reviews whether the experience actually honors it. The same standards govern both directions.

## Modes

- **System** — extract, rebuild, greenfield, or govern a design system.
- **Review** — judge a running product, a design artifact, or a design system, and produce a fix plan.

Pick the mode first; it changes the evidence and the output, not the standards.

## Thinking model

1. **Frame the promise.** Who is it for, which jobs, in which context, under which constraints; what success and failure look like. In review, the promise is the criterion.
2. **Take a stance.** State what good means here and what you refuse. In review, use the product's stance; if it has none, infer it from the promise. Select two or three lenses from `references/design-philosophy.md`; do not apply every lens.
3. **Choose methods by uncertainty.** Read `references/design-methods.md`. Name the biggest uncertainty and the method that answers it; record what you did not learn.
4. **Derive or apply principles.** Keep three to seven that decide arguments. Each has a rationale, a trade-off, and a test case. In review, use the product's principles; if it has none, derive them from the promise.
5. **Record decisions.** Context, options, criteria, decision, consequences, and the condition that would reopen it. In review, record the conflict adjudication and the recommended option.
6. **Make it traceable.** Principle → rule → token or behavior → check. In review, finding → criterion → evidence → acceptance criterion.

## System work

1. Define scope: surfaces, layers, ownership, and what is deliberately shared.
2. Read every surface supplement in scope (see References) and `references/checklist.md`. Both are binding: the supplement adds the medium's constraints, the checklist is the coverage and verification sweep.
3. Lay foundations in order: information architecture and key flows → color → typography → copy → layout → components → states → motion → accessibility → platform context.
4. Cover empty, loading, error, partial, and over-full states; touch, keyboard, IME, safe areas, back, orientation, and font scaling.
5. Write the specification and the showcase together; the spec is the source of truth, the showcase proves it.
6. Verify by measurement: contrast, token drift, interactions, whole scenes; use the checklist's verification section.
7. Author the drift check and ratchet configuration as part of the deliverable; do not install it into CI or fix existing violations unless the user also asks for implementation. Prove every rule with a mutation self-test.
8. Hand over what you could not determine as an explicit "to confirm" list.

## Review work

1. Pin down the object, version, and the question the review supports.
2. Read every source of truth that exists: tokens, specification, requirements, plans, implementation.
3. Audit statically, probe dynamically, and walk through on the real surface; keep the probe scripts.
4. Triangulate; separate observation, inference, and recommendation.
5. Find structural roots with five whys and affinity mapping.
6. Read `references/review.md`; grade P0/P1/P2 using its definitions and register every finding with location, evidence, impact, and an acceptance criterion.
7. Adjudicate specification-versus-implementation conflicts explicitly.
8. Plan increments by risk and dependency; pre-mortem the riskiest fix.
9. Propose guard rules and a ratchet plan; implementing them is separate unless the user also asks for it.
10. Declare method, independence, coverage, and what was not tested.

## Non-negotiables

- **Evidence over invention.** Recovered values carry their path; designed values are marked designed; findings cite evidence.
- **Every rule has a rationale, a trade-off, and a test case.**
- **The reasoning is traceable.** Stance → principle → rule → token/behavior → check; finding → criterion → evidence → acceptance.
- **The spec is a target, not a description.**
- **The showcase obeys its own system.**
- **One action, one word.**
- **Contrast is computed where the system owns the palette.** Where a host owns it, tokens are roles, not values.
- **The sharing boundary is explicit.** Shared tokens are a declared decision; one surface's theme never moves another surface's pixels.
- **Accessibility is a foundation, not an appendix.** Read `references/accessibility.md`.
- **Adopt before inventing.** Prefer a mature system or platform convention; record the source and every deviation.
- **States and platform context are first-class.**
- **Protect what works.** A review that only lists defects is incomplete.
- **Question the brief.** The interface may be faithfully implementing the wrong problem.

## References

Required reads: `references/design-philosophy.md` and `references/design-methods.md` at framing; `references/checklist.md` and every surface supplement in scope in System mode; `references/review.md` and `references/accessibility.md` in Review mode; `references/guard-rules.md` when leaving guards.

- `references/design-philosophy.md` — stance, lenses, principles, tension pairs.
- `references/design-methods.md` — method selection, classic methods, decision records.
- `references/accessibility.md` — build rules and review hints.
- `references/review.md` — dimensions, severity, evidence, report and register templates.
- `references/guard-rules.md` — drift rules, ratchet, mutation self-test.
- `references/checklist.md` — coverage sweep.
- `references/terminal-surfaces.md` — terminal and CLI.
- `references/mobile-app-surfaces.md` — mobile app.
- `references/game-ui-surfaces.md` — game UI.
- `references/print-and-document-surfaces.md` — print and fixed canvas.
- `references/web-app-surfaces.md` — web app.

## Output

**System mode** — three artifacts, always all three:

- **Showcase** — a single self-contained HTML file that opens offline; webfonts declare system fallbacks and degrade readably; live theme and scheme switching; a table of contents built from the rendered sections; live component samples; whole-use scenes on the target canvas; a computed contrast table. It must not overflow horizontally at its narrowest target width, and every inline asset carries an explicit size.
- **Specification** — the problem, stance, principles, method log, decision records, scenarios, token tables per scheme and mode, component and state specs, copy table, platform-context rules, and traceability matrix.
- **Drift check** — parses the specification, showcase, and implementation; fails on token, component, and semantic drift; includes a ratchet and a mutation self-test.

**Review mode** — review report, issue register, fix plan, guard rules. Both modes keep the source of truth and the rendered artifact together.

## Boundary

This skill builds and judges design quality; it does not implement the fixes it recommends, wire its checks into CI, run a formal verification verdict, or create presentations. Implementing is separate work; a formal verdict is a separate verification task; presenting or reporting is a separate communication task.
