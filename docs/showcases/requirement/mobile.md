# pulse — Mobile App Requirements

> Source: [`../mobile.html`](../mobile.html) · Surface: mobile app (Compose) · Mode: Rebuild · Case 03
> Purpose: prove whole screens, two first-class schemes, real ergonomics, and states in the form they actually take.

## 1. Problem and context

**Who:** people checking a chronic condition several times a day, often at night.

**Jobs:** see the current status, run a guided session, review a weekly report.

**Constraints:** one hand, variable light, OS font scaling, and two schemes that are both first-class. The system governs whole screens and states; component samples alone would hide how they meet on a phone.

## 2. Experience requirements

Six whole-screen scenes, each 360×760:

1. **Home / status** — the first screen answers one question: “how am I today?” Status is color + number + word.
2. **Immersive session** — content centered, no navigation, one escape hatch. Leaving early is always allowed and saves to history. The screen never scrolls.
3. **Report** — data explains itself: label, chart, and a plain-language sentence.
4. **Whole-screen empty state** — distinct from the inline placeholder. A report needs at least three sessions; they take ten minutes and the first one counts tomorrow morning.
5. **Onboarding** — one idea per screen, progress visible, skip always available.
6. **Bottom sheet** — stacked on a real screen with a scrim; interruption in context, not a floating sample.

## 3. Visual requirements

### Color

Two designed palettes, measured independently; dark is not an inversion.

| Role | Light | Dark |
|---|---|---|
| app-bg | `#f7f8fa` | `#0c1214` |
| app-surface | `#ffffff` | `#151d20` |
| app-text | `#14171c` | `#e8eef0` |
| app-subtle | `#5f6673` | `#9aa8ad` |
| app-accent | `#0f766e` | `#2dd4bf` |
| app-accent-soft | `#d7ecea` | `#10312e` |
| app-border | `#e4e7ec` | `#243034` |
| app-ok | `#15803d` | `#4ade80` |
| app-warn | `#b45309` | `#fbbf24` |
| app-bad | `#b91c1c` | `#f87171` |

Semantic colors follow the mode, never the scheme. Chart colors are data, not decoration.

### Typography

The system owns the face (SF Pro on iOS, Roboto on Android); the app owns the scale.

| Role | Size / line-height | Use |
|---|---|---|
| display | 34/40 | hero numbers |
| title | 20/26 | screen titles |
| body | 15/22 | rows, actions |
| caption | 12/16 | metadata |
| tabular | — | statistics |

- Weights carry hierarchy: 700 title / 600 action / 400 body.
- A second face is not the answer.
- Text scales with the OS to 2.0×; layouts reflow instead of truncating meaning.

### Layout and targets

- Every control is at least 48×48 dp.
- Primary actions sit in thumb reach; destructive or rare actions stay out of it.
- Status bar and home indicator are reserved bands; the bottom bar never overlaps them.
- At 2.0× the screens reflow: tiles wrap, labels truncate with an ellipsis, buttons grow, nothing clips.
- One primary action per screen; primary carries the accent.

## 4. Components and states

- **Actions:** primary, secondary, ghost; all ≥48 px tall.
- **Inline states:** inline chart placeholder inside a populated screen, distinct from the whole-screen empty state.
- **Rows and pills.**
- **Icon scale:** every inline SVG has a default size and is overridden per context — 16/20/24/32/48/64.

## 5. Motion

| Token | Duration | Used for | Never |
|---|---|---|---|
| fast | 120 ms | state change, pressed feedback | data values |
| base | 200 ms | sheet and overlay entrance | scrolling content |
| slow | 320 ms | screen transitions, scene change | interruptions |
| breathe | 6 s loop | guided breathing pace | anything not breathing |

- Discrete data changes discretely: a score, count, or health state never tweens; it cuts.
- Motion is reserved for guidance and transitions; the breathing guide is the loudest thing on screen.
- Under `prefers-reduced-motion`, transitions cross-fade and the guide is a static ring.

## 6. Accessibility

- Every control is at least 48×48 dp; annotations can reveal the boxes.
- System scaling to 2.0× with reflow, not truncation.
- Status is color + icon + word; the chart carries labels and a sentence, not only a hue.
- Icon-only controls carry labels; overlays trap and restore focus; headings follow reading order.
- Contrast is measured per scheme; both tables must pass independently.

## 7. Verification requirements

- Icon sizes: every inline SVG renders at a nonzero, on-scale size.
- Per-frame overflow: `scrollWidth ≤ viewport` at the target width.
- Equal frame heights across the six scenes.
- Reduced-motion support is asserted.
- Contrast is computed independently for light and dark.
- The system must define empty, loading, error, and populated states. The showcase demonstrates the whole-screen empty state and the inline placeholder, not every loading or error variant; add those proofs before claiming full state coverage.

## 8. Non-goals

- Do not treat dark mode as an inversion.
- Do not use a second typeface for hierarchy.
- Do not shrink text to fit; reflow instead.
- Do not hide the empty state behind the inline placeholder.

## 9. Open questions

- Tablet and landscape are not shown; decide whether they are in scope.
- The report chart has a plain-language sentence; decide whether every chart needs one or only the primary chart.
