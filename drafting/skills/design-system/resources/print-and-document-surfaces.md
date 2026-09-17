# Print and Document Surfaces

The canvas is fixed and the artifact cannot respond. Posters, reports, one-pagers, and exports such as PDF share this surface. Read this with the main skill and the checklist.

## Canvas and grid

- Fix the canvas first — A4, A2, a slide, or a named pixel size — and design to it. Nothing may reflow.
- Margins, trim, and bleed are part of the tokens. Text never enters the trim, fold, or staple zones; state the assumption when the artifact will be trimmed.
- Use one typographic grid with a declared measure (characters per line) for body text, shared across pages.
- Pages are the repeated unit: define what repeats (header, folio, caption style) and what varies by page type (cover, body, full-bleed image, table).

## Typography and color

- Type sizes are chosen for the viewing distance (arm's length for a report, meters for a poster) and stated as such.
- Hierarchy is size and weight first; color is secondary and must survive grayscale.
- Print color is not screen color: state the color space, keep tints above the threshold where thin type stays legible, avoid transparency effects that a print pipeline will flatten, and declare paper and ink assumptions when they change the palette.
- Data colors carry the same meaning as in the interactive system; do not let a print conversion change a semantic role.

## No interaction, but states exist

- There are no hover or focus states. Specify page types and data extremes instead: long titles, empty cells, overflow tables, missing figures.
- Every figure has a caption and alternative text for the tagged, accessible export.
- Reading order and tagged structure are part of accessibility, not an export detail.

## Showcase

- Show whole pages at true proportion, plus an overview grid; a component sampler alone cannot prove a print system.
- Render sheets at their true aspect ratio and size internal detail relative to the sheet width, so the proof scales without reflowing.
- Keep annotations inside the canvas; anything placed outside the sheet is clipped by the page bounds.
- Provide a grayscale proof and a grid overlay as showcase controls.
- Display each color token with its print values, label the screen preview as a preview, and mark conversions as profile-dependent.
