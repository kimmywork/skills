# Game UI Surfaces

Real-time, input-first, and viewed at a distance or in the hand. HUD, menus, overlays, and touch controls are one system. A handheld game is also a mobile surface: read the Mobile App supplement for device ergonomics and OS safe areas; the Game UI rules win for gameplay-critical overlays, and each rule stays attributed to its source.

## Layout and input

- Respect safe zones: keep critical HUD inside the title-safe area; expect overscan on TVs and cutouts and rounded corners on handhelds.
- Controller and keyboard prompts come first. Show the glyph for the active input device and update it when the device changes; never show two prompt sets at once.
- Placement follows the input: status near the eye line, action prompts near the hand, touch controls in the thumb zones with adjustable size and position.
- Orientation is a first-class axis for handheld play: portrait and landscape each get their own layout rules and whole-scene proofs.
- HUD density is budgeted: gameplay stays legible underneath; hide what the current context does not need.
- Menu-heavy mobile games are landscape-first: keep the world screen bright and move item grids, achievements, and summons onto dark panels, so art and rarity frames read against a controlled background.

## Readability and feedback

- Text must be readable at the intended distance; define one minimum size rule and test it at the smallest supported screen.
- Status is encoded redundantly (color + shape + icon + motion), never color alone. Test the common color-vision deficiencies and grayscale.
- Feedback is immediate and proportional: damage, cooldown, and objective state change with the event, never on a decorative delay.
- Discrete states change discretely; do not tween what is not continuous.
- Motion has an intensity budget; decorative motion never obscures gameplay-critical information.

## Typography

- Give the system three registers: **display/effect** (titles, damage, score moments), **UI** (controls, counters, labels), and **text** (dialogue, lore, help). Each has one job; display is never used for prose and text is never used for counters.
- Numerals are tabular wherever a value can change, so counters do not jitter.
- If the game ships more than one script (for example JP and EN), declare the face pairing and line height per register and re-check truncation in every locale.

## Safety and accessibility

- Photosensitivity limits: bound flash frequency and area, and provide a reduce-motion/reduce-flash option that the system honors everywhere.
- Provide remappable controls, subtitles and captions with speaker identification, and scalable UI text where the platform allows.
- Menus are the calm surface of the system: pause, settings, and accessibility share one layout grammar and one focus model.

## Verification

- Render each HUD state (exploration, combat, low health, menu, dialog) as a whole scene in every supported orientation.
- State the safe-zone percentages the system assumes, and assert containment of every critical HUD element inside the action-safe area as a probe.
- Assert minimum text size at the smallest supported resolution.
- Prove the no-color path: every status remains distinguishable in grayscale and under simulated color-vision deficiency.
- Confirm reduce-motion and reduce-flash settings stop the effects they control; flashing effects appear only as labeled, default-off simulations in the showcase.
