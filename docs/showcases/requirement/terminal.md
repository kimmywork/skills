# orbit — Terminal + Web Requirements

> Source: [`../terminal.html`](../terminal.html) · Surface: TUI + web dashboard · Mode: Greenfield · Case 01
> Purpose: prove a host-owned terminal surface and a web surface can share vocabulary without sharing tokens.

## 1. Problem and context

**Who:** developers running an agent in a terminal, plus the same sessions reviewed in a browser.

**Jobs:** start a task, watch tool calls, approve or deny actions, resume work later.

**Constraints:** the terminal emulator owns background, foreground, and the ANSI palette. The app controls roles, weight, and layout only. The TUI and the web app share one vocabulary, not one token set.

## 2. Scope and sharing boundary

**Shared (declared):** the term table — session, turn, tool call, permission, plan, checkpoint. One action keeps one word across both surfaces.

**Not shared:** tokens, components, and layout. The TUI never references a web token. The drift check must fail on an undeclared cross-surface reference.

## 3. Principles

| Rule | Rationale |
|---|---|
| Roles, not values | The host palette cannot be read or set; naming an RGB value would be a lie the app cannot keep. |
| Color is never the only carrier | Every colored state also carries a word or glyph, so a failed or overridden ANSI role cannot hide meaning. |
| High contrast is the default foreground plus weight | No ANSI role is legible on both light and dark hosts; “brighter color” cannot be the escape hatch. |
| The cell is the layout unit | Gaps, indents, truncation, and status collapse are counted in cells, never in pixels. |
| Surfaces stay decoupled at the token layer | A web theme choice that reached the TUI once produced dark text on a dark terminal; the boundary is now a checked rule. |

## 4. Experience requirements

### TUI scene

- Render a whole session: transcript, inline permission panel, and status line.
- Status content collapses from the outside in as width drops; show the 40 / 26 / 18 cell states.
- Every state must remain legible on dark, light, and monochrome hosts.
- Focus is inverse video; it is visible with color disabled.
- Unavailable actions stay visible with their reason; do not hide them.

### Monochrome fallback

- Provide a shipped monochrome high-contrast mode, not a user-invented fallback.
- Use the host's default foreground plus weight; never a “brighter” ANSI color.
- Every role has an ASCII glyph fallback; meaning survives without the glyph.

### Surface isolation

- The web dashboard has its own tokens and its own theme switch.
- Changing the web theme must move the dashboard and must not move a TUI pixel.
- The check asserts both directions, so a no-op cannot pass.

## 5. Visual requirements

### Color roles

TUI tokens are roles. The showcase uses this reference palette; measurement against it is advisory:

| Role | Dark host | Light host | Monochrome |
|---|---|---|---|
| cyan | `#2ad4d4` | `#0e6f6f` | `#ffffff` |
| green | `#4ec46a` | `#2f7d32` | `#ffffff` |
| yellow | `#d9b04a` | `#7a5c00` | `#ffffff` |
| red | `#f06a6a` | `#a3231c` | `#ffffff` |
| blue | `#6f8ff0` | `#2743c9` | `#ffffff` |
| magenta | `#d47adb` | `#7c2483` | `#ffffff` |

- Contrast is advisory; label the reference palette.
- Structural legibility is the guarantee: color is redundant, and the monochrome path exists.
- The web surface uses separate `--web-*` roles; do not map them into TUI roles.

### Typography

- The host owns the font; the TUI owns weight, dim, and alignment.
- There is exactly one size; hierarchy comes from emphasis and position, never a type scale.
- Columns are counted in cells; truncation uses a visible ellipsis.
- Emoji are excluded from the glyph set — variable width breaks alignment.
- Numeric columns are right-aligned and tabular.

### Glyphs

| Meaning | Primary | ASCII fallback | Requirement |
|---|---|---|---|
| running | `⠿` | `*` | Braille spinner; frozen under reduced motion. |
| done | `✓` | `ok` | Word form survives fonts without the glyph. |
| failed | `✗` | `x` | Always paired with the failing check. |
| pending | `◌` | `..` | Distinct from dim text alone. |
| needs attention | `◆` | `!` | Used for permission and plan state. |

## 6. Components and states

- Transcript line types: running, done, failed, pending, attention.
- Panel with a focused action.
- Status line segments, collapsed from the outside in.
- Disabled and unavailable states, with the reason visible.
- Every state has a monochrome rendering.

## 7. Motion and accessibility

- One spinner cadence while work is running; it stops when the result lands.
- `prefers-reduced-motion` and dumb terminals freeze the spinner at a static glyph.
- No transitions, no scroll effects.
- Focus is inverse video and visible without color.
- The screen is a linear text stream; screen readers get the same order as the eye.
- Every keybinding is discoverable from a status line or help overlay.
- The monochrome high-contrast path is shipped.

## 8. Verification requirements

- Enumerate the pairs rendered by components, per host background; do not sample by hand.
- Label advisory numbers with the reference palette they assume.
- Assert a no-color rendering, a monochrome rendering, and an ASCII glyph set for every role.
- Reject any TUI token that resolves to a web token unless the sharing is declared.
- Prove the isolation check by mutating an artifact and confirming failure.

## 9. Non-goals

- Do not emulate a specific terminal emulator.
- Do not add a pixel-based type scale.
- Do not use emoji as an icon system.
- Do not let the web theme own the TUI palette.

## 10. Open questions

- The web dashboard is a secondary surface here. If the system grows a full web app, give it its own case and requirements.
- The reference palette is one assumption; decide whether to test a second named palette.
