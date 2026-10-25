# Visual Production

Read this before laying out diagrams, image rows, or a dark showcase. It covers the geometry and asset defects that survive token review.

## SVG geometry

- Do not put a gradient on a zero-height `<line>`; `objectBoundingBox` degenerates and the line disappears. Use `gradientUnits="userSpaceOnUse"`.
- `overflow: visible` lets content escape its viewBox into another column. Remove it, or expand the viewBox to cover everything drawn.
- Compute the inline maximum height before placing the block; do not update it while placing, or the first row gets a negative y.
- CJK text is roughly font size × character count, about 30% wider than English. A 68-unit box does not hold "合并 → 1250 万"; size the box or wrap the text.

## Flex arithmetic

- For a row of images, sum image widths, gaps, and the text column and compare with the content width before rendering. If it exceeds, remove an image; do not shrink the type.
- Do not rely on `flex-shrink` to hide an overflow; it compresses the wrong element.

## Content versus container

- If the content fills less than roughly 80% of its region, it reads as unfinished. Either enlarge the content or add a bottom line that closes the point.
- Do not center a small block in a large empty frame and call it layout.

## Light images on a dark surface

- Choose one: a plate with a 1px border and a controlled background, or a full cutout. A half-treated image leaves a rectangle brighter than the page.
- For a cutout, supersample about 3×, flood-fill the corners, then downscale; this keeps the edge clean.
- Black line art becomes graphite gray; keep semantic colors such as ED yellow and aspheric blue.
- Crop the original legend and re-typeset it in the deck's type.

## Verification

Render the diagram at its real size and at the narrowest target. Check overflow, negative coordinates, text clipping, and image edges against the actual page background, not a swatch.

## Anti-patterns

- A gradient or clip path that only works at one aspect ratio.
- A row that "fits" only because the font became smaller.
- A large empty band above or below the content.
- A light image pasted on a dark page without a plate or a clean cutout.
