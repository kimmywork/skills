# Minimal Visual System

This is an example, not a fixed template. Use it when no design system exists and the work still needs to look coherent; adapt the grid, type, color, density, and tone to the topic, setting, audience, and medium (projection, screen, print, hybrid). It is a floor, not a brand: keep it small and consistent, but do not apply it mechanically.

## Canvas

- **Projection:** 16:9; choose 1280×720 or 1920×1080. Keep a 64–96 px safe margin.
- **Page:** A4 or Letter; 20–25 mm margins; one grid for all pages.
- **Grid:** 12 columns for projection, 6 columns for a page; align text and figures to it.

## Type

- One sans-serif family for UI and body; a second face only for display if needed.
- **Projection:** display 40–56 px, body 24–28 px, caption 18–20 px.
- **Page:** body 10–12 pt, heading 18–24 pt, caption 9–10 pt; leading 1.4–1.6.
- No more than three sizes per artifact; use weight for emphasis, not a new size.
- Changing values use tabular numerals.

## Color

Six roles are enough:

| Role | Use |
|---|---|
| surface | background |
| text | primary text |
| muted | secondary text and captions |
| accent | one emphasis color |
| border | dividers and boundaries |
| focus | focus ring and selected state |

Contrast at least 4.5:1 for normal text and 3:1 for large text. One accent per artifact. Meaning never depends on color alone.

## Charts

State axis, baseline, source, sample, and units. No truncated axes, no 3D, no chartjunk. Label the point the audience should see. If a table is clearer, use a table.

## Accessibility floor

Alt text for meaningful images; reading order follows the argument; captions or transcript for media; grayscale check; respect reduced motion; body text large enough for the room or the page.

## Anti-patterns

- A new palette for every deck.
- Ten type sizes and three accent colors.
- Decoration that competes with the evidence.
- Tiny text to fit more content.
- A chart without a source or a baseline.

This file is intentionally short. Do not treat these numbers as universal: a conference keynote, a small sharing session, a board readout, a printed report, and a recorded demo have different constraints. Choose the values that fit the occasion, state the assumption, and expand this into a real design system only when the work needs one.
