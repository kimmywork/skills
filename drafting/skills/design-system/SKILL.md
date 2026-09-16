---
name: design-system
description: Build, extract, or rebuild a design system and deliver it as a showcase plus a token-complete specification. Use when the user wants a design system, a shared visual and interaction language across surfaces, design tokens or themes, a written design spec, or a system to steer a refactor.
---

# Design System

Turn scattered UI into one system, delivered as two artifacts: a runnable showcase and a specification that a human or agent can implement from.

## Modes

Pick the mode first; it changes how you gather evidence, not what you produce.

- **Extract** — recover the system that already exists in the software, then name and write it down.
- **Rebuild** — start from existing features plus real user scenarios and principles, and produce a corrected target system.
- **Greenfield** — design from the user's description with no existing implementation.

## Approach

1. **Establish the ground before styling.** Who uses it, which jobs they do, how often, on which platforms, and which constraints are fixed. In Extract and Rebuild, read the real sources — style files, configs, component code, plans — and quote actual values and paths. Never invent a value you could read.
2. **Define scope.** Decide which surfaces and which layers this system governs, and which it explicitly leaves alone. Fix that boundary before styling anything; every later rule depends on it. Content owned by someone else is the common case that must be named here, not silently restyled.
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
- **Contrast is computed.** Measure every foreground/background pair in every scheme and mode; report the numbers and fix the tokens that fail.
- **Accessibility is a section, not a footnote.** Contrast, focus, hit targets, reduced motion, color-not-alone, and zoom are part of the deliverable.

## Principles

Check the draft against established interaction principles rather than inventing a private list:

- Nielsen's ten usability heuristics
- Shneiderman's eight golden rules
- Norman's design psychology — affordance, signifier, mapping, feedback, constraint, conceptual model, slips versus mistakes
- Gestalt grouping — proximity, similarity, common region, continuity, closure, figure/ground, common fate
- WCAG's POUR — perceivable, operable, understandable, robust

Do not reproduce these in the deliverable. Use `resources/checklist.md` to sweep coverage and keep only the principles that change decisions in this product; state each kept principle in the product's own words.

## Foundations and verification

`resources/checklist.md` holds the principle sweep (framework principles plus general aspects), the foundations coverage checklist, and the verification steps. It is reference material for deriving your own decisions, not a script to run through.

## Output

Two files, always both:

- **Showcase** — a single self-contained HTML file that opens without a build step: live theme and scheme switching, a table of contents, live samples of every component, and an automatically computed contrast table.
- **Specification** — a Markdown file that opens with the product context and scenarios, then the principles, the foundations with complete token tables per scheme and mode, the component specs, and the copy table.

Both artifacts must agree. Add a check that parses both and fails on drift. Keep the two files together, in whatever location the user's project uses for documentation.

## Boundary

This skill produces a system, not a product change. Implementing it in the codebase is a separate, plannable effort; reviewing an existing artifact is a verification task; attacking a proposal is a critique task. If the user wants any of those, say so and hand off rather than expanding scope here.
