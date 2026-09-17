---
name: design-system
description: Build, extract, or rebuild a design system and deliver it as a showcase plus a token-complete specification. Use when the user wants a design system, a shared visual and interaction language across web, terminal, mobile, game, or print surfaces, design tokens or themes, a written design spec, or a system to steer a refactor.
---

# Design System

Turn scattered UI into one system, delivered as two artifacts: a runnable showcase and a specification that a human or agent can implement from.

## Modes

Pick the mode first; it changes how you gather evidence, not what you produce.

- **Extract** — recover the system that already exists in the software, then name and write it down.
- **Rebuild** — start from existing features plus real user scenarios and principles, and produce a corrected target system.
- **Greenfield** — design from the user's description with no existing implementation.

## Approach

1. **Establish the ground before styling.** Who uses it, which jobs they do, how often, on which surfaces, and which constraints are fixed — including who owns each surface's palette (you, or a host such as a terminal, an OS high-contrast mode, or a third-party embed). In Extract and Rebuild, read the real sources — style files, configs, component code, plans — and quote actual values and paths. Never invent a value you could read.
2. **Define scope.** Decide which surfaces and which layers this system governs, which it explicitly leaves alone, and what is deliberately shared across surfaces versus kept per-surface. Fix that boundary before styling anything; every later rule depends on it. Content owned by someone else is the common case that must be named here, not silently restyled.
3. **Draft principles with rationale.** Aim for a handful of rules that actually decide arguments. Each states the rule and why it holds, so a future proposal can be judged against it.
4. **Lay the foundations in a fixed order.** Color → typography → copy → layout → components → motion → accessibility. Later layers may only use names from earlier ones.
5. **Write the specification and the showcase together.** The spec is the source of truth; the showcase proves it and hosts the verification. Neither may drift from the other.
6. **Verify by measurement, not by eye.** Compute contrast, check token drift, exercise the interactions.
7. **Hand over the decision list.** Anything you could not determine belongs in an explicit "to confirm" list, not in a silent assumption.

## Non-negotiables

- **Evidence over invention.** Recovered values carry their file path. Designed values are marked as designed.
- **Every rule has a rationale.** A rule without a reason cannot be applied to a new case.
- **The spec is a target, not a description.** Do not narrate the current implementation; state what should be true. Existing code may motivate a decision, but it is not the standard.
- **The showcase obeys its own system.** It consumes its own tokens and contains no hardcoded style values. If the showcase needs an exception, the system is wrong.
- **One action, one word.** Keep a single copy table (term → use → avoid → why) and reuse it across the whole system.
- **Contrast is computed where the system owns the palette.** For controlled surfaces, measure every pair a component actually renders, in every scheme and mode, and fix the tokens that fail. Where a host owns the palette (terminal, OS high contrast, third-party embed), tokens are roles, not values; legibility is structural — meaning never depends on a color, and the high-contrast path is the host's default foreground plus weight. Measurement against a named reference palette is advisory.
- **The sharing boundary is explicit.** Surfaces may share vocabulary, and they may deliberately share tokens, but the shared set is a declared decision. A theme or scheme choice on one surface must never alter another surface's pixels, and every cross-surface token reference is named as intentional.
- **Accessibility is a section, not a footnote.** Contrast, focus, hit targets, reduced motion, color-not-alone, and zoom are part of the deliverable.

## Principles

Check the draft against established interaction principles rather than inventing a private list:

- Nielsen's ten usability heuristics
- Shneiderman's eight golden rules
- Norman's design psychology — affordance, signifier, mapping, feedback, constraint, conceptual model, slips versus mistakes
- Gestalt grouping — proximity, similarity, common region, continuity, closure, figure/ground, common fate
- WCAG's POUR — perceivable, operable, understandable, robust

Do not reproduce these in the deliverable. Use `resources/checklist.md` to sweep coverage and keep only the principles that change decisions in this product; state each kept principle in the product's own words.

## Surface supplements

The process is surface-independent; the medium is not. Read the supplement for every surface class in scope before laying foundations. Each adds binding constraints and derivation prompts for its medium and never replaces this process or the two-artifact output. When two apply — a mobile game, a terminal inside a desktop app — read both and keep each rule attributed to its source.

- **Terminal** (TUI and CLI) — `resources/terminal-surfaces.md`
- **Mobile app** — `resources/mobile-app-surfaces.md`
- **Game UI** (console, desktop, handheld) — `resources/game-ui-surfaces.md`
- **Print and document** — `resources/print-and-document-surfaces.md`

## Foundations and verification

`resources/checklist.md` holds the principle sweep (framework principles plus general aspects), the foundations coverage checklist, and the verification steps. It is reference material for deriving your own decisions, not a script to run through.

## Output

Two files, always both:

- **Showcase** — a single self-contained HTML file that opens without a build step: live theme and scheme switching, a table of contents built from the rendered sections, live samples of every component, whole-use scenes on the target canvas (app screens, terminal sessions, command transcripts, print pages), and an automatically computed contrast table. It must not overflow horizontally at its narrowest target width, and every inline asset carries an explicit size.
- **Specification** — a Markdown file that opens with the product context and scenarios, then the principles, the foundations with complete token tables per scheme and mode, the component specs, and the copy table.

Both artifacts must agree; the strongest form is both generated from one token source. Add a check that parses both and fails on drift, including undeclared cross-surface references, and prove the check by mutating an artifact and confirming it fails. Keep the two files together, in whatever location the user's project uses for documentation.

## Boundary

This skill produces a system, not a product change. Implementing it in the codebase is a separate, plannable effort; reviewing an existing artifact is a verification task; attacking a proposal is a critique task. If the user wants any of those, say so and hand off rather than expanding scope here.
