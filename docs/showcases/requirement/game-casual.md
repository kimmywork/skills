# sugarfall — Casual Puzzle Requirements

> Source: [`../game-casual.html`](../game-casual.html) · Surface: game UI (casual puzzle, mobile) · Mode: Greenfield · Case 08
> Purpose: prove shape-coded play, bounded juice, large touch targets, and a game that does not use dark patterns.

## 1. Problem and context

**Who:** commuters and parents, playing one level at a time, sound often off.

**Jobs:** clear a level in 1–3 minutes, feel good, stop cleanly.

**Constraints:** one thumb, bright environments, color-vision variety, and a young audience that must never be pushed into a purchase.

## 2. Principles

| Rule | Rationale |
|---|---|
| Three registers: play, operate, explain | Luckiest Guy for moments, Baloo 2 for controls and counters, Nunito Sans for anything a player must actually read. |
| Pieces differ by shape, not only hue | The board is the game; colorblind players and grayscale screens must still parse it instantly. |
| Juice is bounded | Pop 150 ms, cascade 250 ms, popup 400 ms; nothing blocks input, and reduce motion turns juice into fades. |
| No dark patterns | No timer by default, lives regenerate predictably, and every purchase is an explicit, reversible choice. |

## 3. Experience requirements

### Level play

- The board is the game; each piece is a color and a shape: circle, square, diamond, triangle, star, hexagon.
- Moves and score use tabular numerals in the UI face; they never jitter while animating.
- The pop layer never blocks input; a tap during a popup still plays the next move.
- Objectives show progress as “8 / 12”, not a mood ring; the number is the truth.

### Level complete and failure

- Level cleared and out-of-moves states are clear and non-punitive.
- Retry and exit are explicit; the player is not trapped.

### Level map

- States carry stars, labels, and the current pulse — not only gold versus gray.
- Locked levels state their unlock condition when selected.

### Settings and help

- Help and settings are the only places with paragraphs; set in Nunito Sans at a comfortable measure.
- The popup face is never used for instructions.

## 4. Visual requirements

### Typography

| Register | Face | Use |
|---|---|---|
| display | Luckiest Guy | popups, score moments |
| UI | Baloo 2 | controls, counters, nav |
| text | Nunito Sans | help, settings, store terms |

- The popup face is all-caps by design and cannot be read in a sentence.
- Buttons and counters share the UI face, so “tap me” and “read me” look different.
- Any text a player must act on (settings, purchases, help) is at least 14 px equivalent.

### Color and pieces

| Role | Value |
|---|---|
| berry | `#e0487a` |
| lemon | `#e8a819` |
| mint | `#2f9e77` |
| blue | `#3f7fd2` |
| grape | `#8a4fd0` |
| orange | `#dd6b25` |
| gold | `#e3b341` |
| ink-soft | `#5e5669` |

Six candy hues, six shapes. The shape is the contract; the color is the delight.

## 5. Components and states

- Buttons: primary, secondary, tertiary; all ≥48 px tall; one primary per screen; no disguised close buttons.
- Booster states: available, count, locked.
- Star meter: filled gold, empty outlined; the count is also written as “2 stars”.
- Toasts and popups: never cover the board or the primary action; never require dismissal to continue.

## 6. Motion and accessibility

- Pop 150 ms, cascade 250 ms, popup 400 ms; nothing exceeds half a second and input is never blocked.
- Score counts up in ≤300 ms, but the final number is committed immediately; the value is never mid-animation when the next move starts.
- Reduce motion replaces pops with fades and stops the map's current-node bounce.
- Pieces are shape-coded at all times; colorblind mode is the default build, not a hidden setting.
- Touch targets are ≥48 px; boosters and the board sit in thumb reach for one-handed play.
- Counters can be enlarged without breaking the board; every value has a text form.
- No timer on standard levels; where a timed mode exists it is opt-in and clearly labeled.

## 7. Verification requirements

- Check board pieces as UI graphics at ≥3:1 against the board.
- Each piece also carries a shape, so a failing hue is never the only signal.
- Assert grayscale readability of the board.
- Assert input is not blocked by the pop layer.
- Assert no timer on standard levels and that any timed mode is opt-in and labeled.

## 8. Non-goals

- Do not use color as the only piece encoding.
- Do not block input during juice.
- Do not use a timer by default.
- Do not use dark patterns in purchases, lives, or level gating.

## 9. Open questions

- The store/purchase flow is mentioned in the copy, but not shown. If purchases are in scope, add a proof for price, currency, confirmation, and refund/cancel.
- Define the booster economy and whether boosters can be bought; the showcase only shows states.
