# fieldstation — Print Requirements

> Source: [`../print.html`](../print.html) · Surface: print and document · Mode: Greenfield · Case 05
> Purpose: prove a fixed-canvas system for a poster and a report, with a shared grid, print color assumptions, and grayscale survival.

## 1. Problem and context

**Who:** researchers presenting at a conference and readers of the printed report.

**Jobs:** read the argument from two meters (poster) and from arm's length (report); cite and archive the PDF.

**Constraints:** one fixed canvas, no hover or focus, no reflow, a print pipeline that flattens transparency and converts color. One system covers both formats through a shared grid, type scale, and ink palette.

**Boundary:** this is a print system, not a report-authoring example. The argument and narrative of the report belong to `presentation`; this case owns the fixed-canvas visual system.

## 2. Principles

| Rule | Rationale |
|---|---|
| Fix the canvas, then design to it | Nothing reflows; margins, trim, and bleed are tokens, and text never enters the trim or fold. |
| One grid serves every page type | Cover, body, figure, and table pages differ in pattern, not in underlying structure. |
| Hierarchy is size and weight first | Color is secondary; the argument must survive a grayscale print and a black-and-white photocopy. |
| Type is sized for the viewing distance | Poster type is read at two meters, report type at arm's length; stating the distance makes the scale checkable. |
| Print color is a production decision | CMYK ranges, tint thresholds, and paper assumptions are declared; screen preview is labeled as a preview. |

## 3. Experience requirements

### Poster

- A2 at true proportion: one screen-size proof, not a sampler.
- Headline read at two meters; body at one meter.
- Shared 3-column grid; a grid overlay can show it.
- Reader path: title → figure 1 → “3.1 cm” → conclusion. Everything else is depth for the specialist.

### Report pages

- A4 pages at true proportion: cover and body.
- Body carries the declared measure, a table, a figure caption, and a folio — the repeating units of the system.
- Table cells with no data show an em dash, never a zero.
- Wide tables move to a landscape page rather than compressing.
- A 140-character title wraps to three lines without entering the trim.

### Page furniture

- Running head, folio, caption, callout, table rule, and pull quote.
- Each is defined once and reused across both formats.
- The folio never carries content.
- A callout carries one number and one claim; the figure must also read without the callout.
- A caption states the takeaway, not only the axes, and is numbered in one sequence across both formats.

## 4. Visual requirements

### Canvas and grid

- Poster: A2, 6.5% padding, 3 columns.
- Report: A4, 9% padding, 1 column.
- Margins, trim, and bleed are tokens.
- Pages are the repeated unit; page types are cover, body, full-bleed figure, table, colophon.

### Typography

One serif family, Newsreader, with optical sizes; weight rather than hue carries hierarchy.

| Role | Face | Print size | Use |
|---|---|---|---|
| Poster title | Newsreader 600 | 72–96 pt | read at 2 m |
| Poster body | Newsreader 400 | 24–28 pt | read at 1 m |
| Report heading | Newsreader 600 | 18–24 pt | page structure |
| Report body | Newsreader 400 | 10.5 pt / 1.45 | arm's length, 62-character measure |
| Kicker, labels, folios | Newsreader 600 · tracked caps | 8–9 pt | captions, folios, running heads |
| Print metadata | Mono | 7.5 pt | colophon, profile, revision |

### Color and print

| Role | Value |
|---|---|
| paper | `#fbf9f4` |
| ink | `#17181a` |
| ink-soft | `#4d4a44` |
| rule | `#c9c3b6` |
| brand | `#0b5d4f` |
| signal | `#b45309` |

- Every color token carries its print values; conversions are naive preview values, and the printer's profile is authoritative.
- Check the palette for grayscale separation before shipping.
- Body text stays below the 80% tint line at text sizes.
- No semantic role depends on a hue that disappears in grayscale.

## 5. Interaction, motion, accessibility

- There are no hover, focus, press, or disabled states on paper. Their equivalent is the page-type grammar: cover, body, figure, and table are distinguishable at a glance.
- Clear cross-references replace affordances.
- No motion; page-turn and reveal behavior belongs to the reader or the PDF viewer.
- States become page types and data extremes: cover, body, full-bleed figure, table, colophon; long titles, empty cells, wide tables.
- Reading order is tagged: title, authors, abstract, sections, captions, footnotes.
- Every figure carries alternative text and a caption that states the takeaway.
- Ink-on-paper contrast is measured for the actual paper stock.
- The PDF export preserves tags, reading order, and document language.

## 6. Verification requirements

- Grayscale proof: hierarchy and the figure remain readable without color.
- Grid overlay: every page shares one grid and one margin; text never enters the trim.
- Print values: every token lists hex and naive CMYK; the printer's profile is declared in the colophon.
- Proportion: sheets render at true aspect ratio, so a wrong canvas is visible immediately.
- Tagged export: reading order, alt text, and language are preserved.

## 7. Non-goals

- Do not reflow the canvas.
- Do not rely on color alone for hierarchy.
- Do not use transparency effects that a print pipeline will flatten unpredictably.
- Do not treat the screen preview as the final color.

## 8. Open questions

- Poster and report share one grid and type scale; decide whether the poster's 3-column grid is a variant of the report's 1-column grid or a separate page-type rule.
- The showcase uses naive CMYK values; define the actual output profile and paper stock before production.
- The report content is a sample; the narrative and citation requirements belong to the `presentation` skill.
