# emberhold — Fantasy RPG Requirements

> Source: [`../game-rpg.html`](../game-rpg.html) · Surface: game UI (fantasy RPG) · Mode: Greenfield · Case 06
> Purpose: prove a three-register type system, dialogue as a reading surface, and rarity that survives grayscale.

## 1. Problem and context

**Who:** players on a TV or monitor, long sessions, one hand on the controller.

**Jobs:** track quests while fighting, read dialogue as prose, compare loot, level up.

**Constraints:** ornate is a feature, but never at the cost of contrast, minimum size, or colorblind safety. Lore text is long, so the reading face must be comfortable.

## 2. Principles

| Rule | Rationale |
|---|---|
| Three faces, three registers | Titles and damage are display; controls and counters are UI; dialogue and lore are text. Mixing registers breaks both mood and readability. |
| The setting is in the ornament, not the legibility | Parchment panels and gold rules carry the fantasy; contrast and minimum sizes stay at system standard. |
| Counters never move | Tabular numerals for health, mana, gold, and XP, so ticking values do not jitter. |
| Rarity is shape, color, and label | Item rarity survives colorblind modes and grayscale through frame style and text. |

## 3. Experience requirements

### HUD

- Damage numbers are the display face at its loudest; the combat log is the text face at working size.
- Resource bars carry a label and a number; the palette is mood, not meaning.
- State overlays (safe zone, reduce motion) are visible.
- Health, mana, stamina, and XP counters are tabular and right-aligned.

### Dialogue

- Dialogue is a reading surface: prose in the text face at a real measure.
- Choices are set in the UI face; the speaker's name is in the display face.
- Dialogue has adjustable size and identifies the speaker.

### Inventory and level-up

- Inventory rarity is frame + written tier + hue.
- Level-up shows resource increases and a talent point.
- Hotbar slots have ready, available, cooldown, and locked states; the cooldown shade is a value, not decoration.
- Quest states are distinguishable without color.

## 4. Visual requirements

### Typography

| Register | Face | Use |
|---|---|---|
| display | Cinzel 700 | titles, damage, level-up |
| UI | Alegreya Sans | labels, counters, choices, buttons |
| text | Spectral | dialogue, lore, logs, explanatory tooltips |

- The three faces are tokens; a scene may use at most two registers.
- Lore never borrows the display face.
- Cinzel capitals are display-only; sentence-length text in the display face is unreadable at TV distance.
- Alegreya Sans carries every interactive label, so controls look like controls across every menu.
- Spectral is the only face for prose and tooltip explanations, at a 60–70 character measure.

### Color

| Role | Value |
|---|---|
| parchment | `#e9dcc0` |
| parchment-2 | `#dccfae` |
| ink | `#241d13` |
| gold | `#c9a227` |
| blood | `#a8342c` |
| mana | `#3f6bc4` |
| stamina | `#4f8f3f` |
| xp | `#b98a2e` |
| hud text | `#f3ead6` |
| hud dim | `#b3a88d` |
| hud scrim | `rgba(14,11,7,.72)` |

Parchment, ink, gold, and the three resources. Every resource bar also carries its label and number, so the palette is mood, not meaning.

## 5. Components and states

- Buttons: primary, secondary, unavailable (with reason).
- Menu item states: default, focused, selected, disabled.
- Hotbar slots: ready, available, cooldown, locked.
- Quest states.
- Rarity frames and written tiers.

## 6. Motion and accessibility

- Damage numbers rise once (1.5 s) and vanish; the value itself cuts, it never counts up.
- Cameras, panels, and menus move with purpose; nothing loops decoratively in the frame.
- Reduce motion stops rising numbers and screen shake; reduce flash bounds the damage vignette.
- Dialogue has a proper reading measure and adjustable size; subtitles identify the speaker.
- Rarity is frame + written tier + hue, never hue alone; the same holds for damage types.
- Menus are controller- and keyboard-navigable with a focus state that survives grayscale.
- Safe-zone containment is verified as a probe, not eyeballed.

## 7. Verification requirements

- Measure HUD text against its scrim.
- Measure bars as UI components against their track.
- Assert safe-zone containment.
- Assert grayscale-distinct rarity and damage types.
- Assert the display face is not used for sentence-length text.

## 8. Non-goals

- Do not use the display face for lore or instructions.
- Do not let color alone carry rarity or damage type.
- Do not animate a value that is not continuous.
- Do not trade contrast for ornament.

## 9. Open questions

- The case is TV/monitor-focused; handheld and controller-at-distance proofs are not shown. Decide whether they are in scope.
- The rarity palette has three tiers in the showcase; define the full rarity ladder and its frame/label rules before extending.
