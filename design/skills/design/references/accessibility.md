# Accessibility

Read this when building or reviewing any interactive surface. It is a foundation, not a final checklist. Use the prompts below and expand them for the product; do not reproduce WCAG clause by clause.

## Target

State the target and the exceptions: WCAG 2.2 AA unless the product or jurisdiction requires otherwise. Record known exceptions with owner and date. "Best effort" is not a target.

## Target sizes

- WCAG 2.2 AA 2.5.8 sets a **24×24 CSS px floor**.
- Platform conventions are stricter: **48×48 dp on mobile**, **44×44 CSS px on touch web**.
- Declare the product target per surface. It must be at least the floor and normally the stricter applicable convention.
- Where a surface is both (mobile web, hybrid app), take the stricter applicable target.
- A 24×24 control can pass WCAG and still fail a declared 44/48 target. That is a product decision, not a contradiction; state which rule applies.

## Building

**Token roles.** Define accessible pairs for every scheme and mode: text on surface, text on action, text on overlay, border, focus ring, disabled, error, and on-color. Where a host owns the palette (terminal, OS high contrast, third-party embed), tokens name roles, not values, and meaning never depends on a host color.

**Components.** Every component specifies keyboard behavior, focus order, visible focus, semantics and name, hit target, disabled state, error state, loading state, and a non-color cue for status. A component without states is not specified.

**Content.** Form labels, error identification, link text, alt text, captions and transcripts, and plain language. Error messages say what happened and what to do next.

**Platform context.** 2× text, 200% and 400% zoom/reflow, reduced motion, high contrast, screen reader, orientation, IME, and safe areas. A layout that only works at the default setting is incomplete.

## Reviewing

Ask, in this order:

- Can every task be completed with a keyboard only, with visible focus and no trap?
- Does a screen reader announce role, name, state, and change?
- Does 2× text or 400% zoom keep content and actions reachable without horizontal scrolling?
- Are contrast pairs measured as rendered, including focus, disabled, overlay, and non-text boundaries?
- Is color ever the only carrier of meaning?
- Does reduced motion stop what it claims to stop?
- Can errors be identified, understood, and corrected?
- Do captions, transcripts, and alt text exist where the content needs them?

## Verification probes

Enumerate the pairs components actually render and compute them; walk the task with a keyboard; run one screen reader; test at 2× text and 400% zoom; toggle reduced motion and high contrast; inspect the accessibility tree. For a review, keep the probe script or the reproduction steps.

## Common failures

Focus traps; invisible focus; missing or generic labels; icon-only buttons with no name; color-only status; targets below the declared product target (the WCAG floor is 24×24; mobile and touch-web conventions are 44–48); hover-only affordances; motion that ignores the preference; timeouts that cannot be extended; errors announced only visually; custom controls with no semantics.

## Anti-patterns

- Measuring contrast on paper but not as rendered.
- Treating an automated scan as a complete audit.
- Adding ARIA that contradicts native semantics.
- Fixing the announced label but not the visible instruction.
- Putting accessibility in an appendix after the design is fixed.

## Sources

WCAG 2.2 (POUR, 1.4.3, 1.4.10, 1.4.11, 2.1.1, 2.4.7, 2.5.8); WAI-ARIA Authoring Practices; platform accessibility guidance.
