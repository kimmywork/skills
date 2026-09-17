# Mobile App Surfaces

Touch-first, portrait-baseline, and dependent on OS chrome and sensors. Read this with the main skill and the checklist; it adds binding constraints and derivation prompts, not a separate process. For handheld games, read the Game UI supplement too.

## Frame and scenes

- Show whole screens, not only components: a set of device frames (360×760 is a reasonable baseline) running real scenarios.
- Frames share one height; the content area flexes and scrolls internally; top and bottom bars stay fixed; immersive pages center their content.
- Overlays (dialogs, sheets) are stacked on a whole screen with a scrim, not isolated in a box. That is what proves interruption and context.
- Status bar, gesture bar, and safe areas are represented, not cropped away.
- Show each empty, loading, and error state in the form it actually appears: inline placeholder and whole-screen state are different designs, and a product may have both.

## Derivation prompts

- Dark mode is a feature, not a theme toggle: measure both schemes independently, never as an inversion, and verify whole scenes in both rather than token contrast alone.
- The first screen answers one question fast — the user's current status, not a dashboard of everything.
- Status is redundantly encoded (color + icon + text), never color alone.
- One primary action per screen; interruptions must relate to the core value and be reversible.
- Discrete data changes discretely; never tween a value that is not continuous. Reserve motion for guidance and transitions.
- Touch targets are at least 48×48; primary actions sit in thumb reach; the bottom bar is the stable navigation slot.
- Support system font scaling to 2.0× without truncation; do not assume the desktop type rules hold.
- Orientation is a declared decision: which screens support landscape, and what changes.
- External content (legal, medical disclaimers, third-party embeds) is named as owned by someone else and not silently restyled.

## Showcase layout

- Samples take their width from the container (`width: 100%` plus a max), never a fixed width; sample grids use `minmax(min(100%, 300px), 1fr)`.
- Whole screens stay at the phone width; grid items are allowed to shrink (`min-width: 0`); wide tables scroll inside their own container; the page itself never scrolls horizontally at the narrowest target width.
- Inline SVG carries an explicit default size; usage sites override it from the icon scale (16/20/24/32/48/64). No bare `<svg>`.
- Derived colors (alpha, overlays) are computed at runtime from base tokens; do not depend on a CSS function the environment may not support.

## Verification probes

- Icon probe: every inline SVG renders at a nonzero, on-scale size.
- Overflow probe: at two or more widths down to the target minimum, `scrollWidth ≤ viewport`.
- Frame probe: all scene frames render at the same height.
- Mode probe: each scene is rendered in light and dark and checked for layout, not only tokens.
- Motion probe: under `prefers-reduced-motion`, decorative motion is static.
