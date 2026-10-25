# asteria — Anime Gacha Requirements

> Source: [`../game-anime.html`](../game-anime.html) · Surface: game UI (anime gacha, landscape) · Mode: Greenfield · Case 07
> Purpose: prove a bright world with dark menu panels, bilingual EN/JP layout, and rarity that survives grayscale.

## 1. Problem and context

**Who:** players in portrait chat moments and landscape play sessions — the game is used mostly landscape, with menus that fill the wide frame.

**Jobs:** explore and read quests, manage weapons, chase achievements, pull and share gacha results, inspect characters.

**Constraints:** bright outdoor scenes with white text over them, dark menu panels for long sessions, and two languages that must both fit without truncation.

## 2. Principles

| Rule | Rationale |
|---|---|
| The world is bright; the menus are dark | Scenery and gameplay stay colorful; long-reading and inventory surfaces switch to dark panels for focus and for the art to read against. |
| Rarity is frame + stars + label | Color is the first signal, never the only one; grayscale keeps the same information through borders and star counts. |
| Text over scenery needs a scrim or a shadow | White dialogue over a bright field is measured against its worst-case backdrop, not a flat color. |
| EN and JP are both first-class | The same screen ships in both languages; buttons, quests, and item names are checked for fit and line height in each. |
| Reveals are anticipation, not a toll gate | Summons can be replayed and skipped; nothing blocks the player from the result. |

## 3. Experience requirements

### World screen

- Bright scenery with a full HUD.
- Quest tracker and dialogue remain legible over the brightest and darkest parts of the scene.
- Language toggle switches every UI string between English and Japanese.

### Character screen

- Attributes in the left rail, character in the center, stats and lore on the right.
- The dark teal wash is the character's element, not a theme.

### Inventory

- The dark panel is the point: item art and rarity frames need a controlled background.
- Rarity shows as border, stars, and label; “New” is a badge, not a color.
- Item detail states the effect in text.

### Achievements

- Dark gallery: gold frames, one emblem, one name, one number.
- A red dot is the only alert, and it also appears as a count in the header.

### Summon results

- Ten cards, one row, landscape.
- Rarity is the frame and the stars; every card can be reviewed before dismissing.
- The reveal is replayable and skippable; nothing is gated.

## 4. Visual requirements

### Typography

| Register | Face | Use |
|---|---|---|
| display | Kaisei Decol | titles, rarity, events |
| UI | Zen Maru Gothic | buttons, nav, counters, quests |
| text | Zen Kaku Gothic New | dialogue, lore, item text |

- Each register has a JP-capable stack.
- JP uses taller line height and looser tracking than EN; the same components must fit both.
- Dialogue uses no italic; JP does not use it for emphasis.
- Counters are tabular in both locales.

### Color

| Role | Value |
|---|---|
| gold | `#c9971f` |
| gold-bright | `#e3b341` |
| violet | `#8a4fd0` |
| azure | `#3f7fd2` |
| hp | `#5cc46a` |
| panel | `#1b2438` |
| panel-2 | `#212c46` |
| panel-line | `rgba(227,179,65,.35)` |

Two environments share one palette: bright world hues for scenery and world HUD, dark panel neutrals for menus, and a rarity scale that carries meaning in both.

## 5. Components and states

- Actions: primary, secondary, locked (character in expedition).
- Rarity frames: 3★, 4★, 5★; border color + brightness + written star count.
- Item states: new, owned, empty slot.
- Badges and alerts: counted, not just colored.

## 6. Motion and accessibility

- Summon reveal staggers 60 ms per card and finishes under a second.
- The replay button re-runs the reveal; nothing is gated.
- Clouds drift slowly in the world screen; menus do not animate at all.
- Reduce motion stops the drift, the reveal stagger, and any idle loops.
- Rarity and alerts use frame, stars, and written labels, never hue alone.
- White text over scenery is measured against the scrim's worst case; a shadow is a secondary aid.
- Touch targets stay at least 44 px in this landscape layout; the action cluster sits in the lower-right thumb arc.
- EN and JP both fit their containers; line heights and tracking are per-locale tokens.

## 7. Verification requirements

- Measure world HUD text against the panel scrim.
- Measure menu text against the dark panel.
- Assert rarity accents are supplemented by frame and stars.
- Assert grayscale readability.
- Assert EN and JP fit at the same widths without clipping or truncation.
- Assert touch targets meet the declared landscape target.

## 8. Non-goals

- Do not make the whole game dark; the bright world is the product.
- Do not use color alone for rarity or alerts.
- Do not gate the summon result behind an unskippable reveal.
- Do not let English string widths set the button minimums for both locales.

## 9. Open questions

- **Touch target conflict:** the showcase uses 44 px in landscape, while the mobile/handheld convention is 48 dp. Decide whether 44 is an intentional game-UI exception or raise it to 48.
- Portrait chat is mentioned in the context but not shown. Decide whether it is a supported surface and, if so, add a portrait proof.
- Define the complete rarity ladder and the label/frame rules beyond 3★–5★.
