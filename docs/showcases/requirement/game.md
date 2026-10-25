# drift — Game UI Requirements

> Source: [`../game.html`](../game.html) · Surface: game UI (console + handheld) · Mode: Greenfield · Case 04
> Purpose: prove input-first HUD design, safe-zone containment, redundant status, and motion/flash safety.

## 1. Problem and context

**Who:** players on a TV at three meters, on a monitor at one meter, and on a handheld at thirty centimeters.

**Jobs:** read status at a glance, act without looking away, pause and adjust without losing the thread.

**Constraints:** real-time input, overscan and cutouts, color-vision variety, photosensitivity. Menus are the calm surface of the same system.

## 2. Principles

- **Input first.** Controller prompts are primary; touch controls are placed for the thumb zone.
- **Readable at distance.** Minimum text size is tested at the smallest supported resolution.
- **Status is redundant.** Color never carries state alone; pair it with a glyph and a word.
- **Motion is feedback.** Discrete states cut; nothing tweens a value that is not continuous.
- **Menus are calm.** Pause, settings, and accessibility share one layout grammar and one focus model.

## 3. Experience requirements

### HUD

- Health is color + length + number.
- “Burning” is a glyph + word; the reticle never carries state on its own.
- Status chips (shield, burning, bleeding, sprint) keep a fixed anchor in the safe zone.
- The only flashing element is simulation-labeled and removed under reduce-flash.
- HUD containment inside the action-safe area is asserted, not eyeballed.

### Menus

- Pause and settings share one layout grammar and one focus model.
- The focused row is visible without color and always keeps its label.
- Menus are keyboard- and controller-navigable.

### Handheld

- A handheld game is also a mobile surface: touch ergonomics, device safe areas, and orientation come from the mobile supplement.
- Portrait is the layout for menus and inventory; landscape for play.
- HUD priority and input prompts stay game rules.

## 4. Visual requirements

### Typography

Three roles:

- **display / effect** — Chakra Petch 700 for titles and moments; never instructions; never below the minimum readable size for its distance.
- **UI** — Chakra Petch 600, tabular numerals, for controls and counters.
- **text** — IBM Plex Sans 400 for dialogue, codex, and help at proper measure.

Reading text stays out of the HUD. Numerals are tabular wherever a value can change.

### Color

The HUD palette is the whole color system: three status hues, one objective hue, one loot hue, and neutrals.

| Role | Value |
|---|---|
| HUD text | `#f2f5f9` |
| HUD dim | `#aeb6c4` |
| HUD scrim | `rgba(8,10,14,.62)` |
| health | `#4ade80` |
| shield | `#60a5fa` |
| danger | `#f87171` |
| warn | `#fbbf24` |
| objective | `#5eead4` |
| loot | `#c084fc` |

Every status also carries a glyph and a word, so colorblind modes change the palette, not the meaning.

## 5. Components and states

- **HUD elements:** bar, chip, ability, prompt, reticle, subtitle; each has a fixed safe-zone anchor.
- **Menu item states:** default, focused, selected, disabled.
- **Touch button states:** default, pressed, cooldown; press is feedback, cooldown is a value; neither depends on color.
- **Subtitles and callouts:** speaker identified by name, size adjustable, background legible over gameplay.

## 6. Motion and accessibility

- Press feedback 80 ms, hit confirmation 100 ms, menu transitions 200 ms.
- Feedback is immediate and proportional.
- Discrete states cut; nothing tweens a value that is not continuous.
- Reduce motion and reduce flash stop every decorative loop, including the minimap sweep and health vignette.
- Flash frequency and area are bounded by default; the flash in the scene is an opt-in, labeled simulation.
- Subtitles are on by default where voice carries plot, with speaker names and adjustable size.
- Remappable controls and a full colorblind mode that swaps the palette while glyphs and words stay.
- UI text scales where the platform allows; minimum size is tested at the smallest supported resolution.
- Menus are keyboard- and controller-navigable with a focus state that does not rely on color.

## 7. Verification requirements

- Assert HUD containment inside the action-safe area.
- Assert minimum text size at the smallest supported resolution.
- Assert a grayscale-distinct path for every status.
- Compute contrast against the dark HUD scrim.
- Confirm reduce-motion and reduce-flash stop the effects they control.
- Confirm the flash simulation is opt-in and labeled.

## 8. Non-goals

- Do not let the reticle carry state on its own.
- Do not use color as the only status encoding.
- Do not loop decorative motion in the frame.
- Do not put reading text in the HUD.

## 9. Open questions

- The showcase does not state a touch target size for the handheld build; apply the mobile supplement's 48 dp or document an intentional game exception.
- The safe-zone percentages are asserted in the page; confirm they match the target platform's certification guidance.
