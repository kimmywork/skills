# Web App Surfaces

Read this for browser-based products. The browser owns chrome, zoom, input, and sometimes the palette; the app owns the page, the flow, and the semantics. Read it with the main skill and the checklist.

## Frame and viewport

- The viewport is a runtime fact. Define the minimum supported width and what collapses, scrolls, or hides below it.
- The page itself never scrolls horizontally; wide tables and code scroll inside their own container.
- Browser chrome, safe areas, and the virtual keyboard are part of the frame. A fixed bottom action must survive the keyboard and the mobile URL bar.
- Routing is part of the interface: URLs are shareable, back/forward work, deep links restore state, and a refresh does not lose the task.

## Input and focus

- Keyboard and pointer are both first-class. Every action is reachable without a mouse; focus is visible and never trapped.
- Hover is an enhancement, not the only path. Touch targets are at least 44×44 on touch web; when the page is a primary mobile surface, use 48×48. The WCAG 2.5.8 floor is 24×24; the stricter declared target wins.
- Forms identify errors at the field, keep values on failure, and do not rely on color alone.
- Modals and menus manage focus, Escape, and focus return; a dialog is not a div with a high z-index.

## Rendering and states

- Specify empty, loading, error, partial, and over-full states for each data surface, in the place they actually appear.
- Loading is honest: skeletons for structure, progress for duration, and no infinite spinner without a timeout or retry.
- Dark mode is a separate scheme, not an inversion; test whole pages, not only tokens.
- Zoom to 200% and 400% reflows without hiding content or actions.

## Performance and trust

- The first screen answers one question fast. State the performance budget and measure it on a low-end device and a slow network.
- Third-party embeds, consent banners, and analytics are named as owned by someone else; do not silently restyle them.
- Errors say what happened, what to do next, and how to recover data.

## Showcase

Render whole pages at the target widths, with browser chrome and the keyboard shown where they change layout. Show the empty, loading, error, and over-full states as pages, not as isolated boxes.

## Verification probes

- Overflow: `scrollWidth ≤ viewport` at the minimum width.
- Focus: every interactive element reachable, visible, and trapped only where intended.
- Zoom/reflow: no clipped content at 200% and 400%.
- Keyboard: the primary task completes without a pointer.
- State: each data surface renders all five states.
- Performance: the declared budget is measured, not assumed.
