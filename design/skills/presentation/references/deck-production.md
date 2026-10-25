# Deck Production

Read this when producing an HTML deck, not when choosing the argument. It covers the production loop, the slide data model, and the QA that catches what reading the slides cannot.

## Pipeline

1. Fix the stage and tokens first: 1600×900 or the target ratio, type scale, color roles, safe margins.
2. Write the deck's CSS and interaction script, plus a skeleton and one sample slide. Settle the layout rules before writing thirty more slides.
3. Write slides in batches from the outline; keep each slide's data in the markup.
4. Render all slides headlessly; assemble a contact sheet, for example twelve-up; inspect the sheet before opening individual slides.
5. Fix only the changed slides and their immediate neighbors. A full re-read invites unrelated edits.
6. Export the deck and the notes from the same source; verify offline and in print.

## Slide data

- One `<section>` per slide, with `data-title`, `data-budget` in minutes, and `data-notes`.
- Generate the table of contents, page numbers, total time, and speaker notes from those attributes. Do not maintain parallel lists.
- Sum `data-budget` after any add or remove. Keep the must-cut list in the notes.
- Rebuild and reorder by anchoring on `<section`, never on HTML comments. A comment can be eaten by an edit; the section boundary is structural.
- Keep one source for the talk: `data-notes` → `notes.md`. Do not hand-write a second copy.

## QA

- Batch screenshots plus a contact sheet is the highest-yield check: it finds most layout defects in seconds. Inspect individual slides only after the sheet.
- If a headless render is blank, suspect capture timing before the code. A tiny file with the deck chrome present is a hint; re-render once. If needed, compress large images and await `img.decode()` before capture.
- On each iteration, check the changed slides and their neighbors, not the whole deck.
- Verify at presentation size, in grayscale, and in the exported file.

## Assets and facts

- Source priority: official schematic, then official sample, then photograph, then self-drawn diagram. If an official image exists, use it; do not redraw it.
- The comparison must match the claim. A 58mm prime cannot prove what a 24–240mm zoom can; choose the object that makes the argument valid.
- Prices and specifications carry a range, a capture date, and a link. A precise number without a date is a liability.
- Fact-check before layout: confirm names, numbers, dates, and claims once, then write. Fixing facts after layout changes the design, not just the text.
- Treat user-supplied images as intentional. Ask before cropping, masking, or "fixing" a blemish.

## Anti-patterns

- Writing thirty-four slides before settling one sample.
- Hand-maintaining the table of contents, page numbers, and notes.
- Anchoring a reorder script on comments or text markers.
- Reviewing the whole deck after every small change.
- Redrawing an official diagram.
- Shipping a price or specification without a date and source.
