# Showcase Requirements

These documents reverse-engineer the requirements behind the HTML artifacts in `docs/showcases/`. The HTML is the current implementation and visual source of truth; these files capture intent, constraints, and acceptance so a redesign or review does not lose context.

## How to use

- Read the case requirement before changing the case.
- Treat the HTML as the current implementation. If it and the requirement disagree, record the conflict; do not silently choose one.
- Requirements are inferred from the artifact. They are not a claim that the artifact is complete or that every value is intentional.
- Keep the requirement short enough to use. Put token values, scene details, and verification in the case document, not in the gallery.

## Review verdict

**Still suitable as System-mode showcase artifacts.** They cover a useful spread of surfaces and demonstrate the design-system work that the `design` skill is meant to produce: host-owned palettes, whole screens, game HUDs, and fixed print canvases.

**Not sufficient as a full demonstration of the current `design` skill's output contract.** The current System mode requires a showcase, a separate specification, and a drift check. These are showcase artifacts only; the rules and token tables are embedded in the page. The gallery should say that explicitly.

Other gaps:

- The gallery (`index.html`) is now the **web landing-page case**: responsive layout, light/dark themes, keyboard focus, and semantic HTML. It is not a full product web app (routing, deep links, IME, data states), so a separate web-app case may still be useful.
- The terminal case includes a small web dashboard, but it does not exercise the `web-app-surfaces.md` requirements at full strength.
- No **Review-mode** case. The gallery demonstrates System mode; the `design` skill's Review mode is not represented.
- `print` is a **print system**, not a report-authoring example. Report and deck authoring belongs to `presentation`; keep the boundary visible.
- `game-anime` uses **44 px** touch targets in a landscape layout, while the mobile/handheld convention is **48 dp**. Decide whether 44 is an intentional game exception or should be raised.

Recommendation: keep the gallery as the **web landing page and System-mode showcase index**; add a product web-app case and a review case later, and use these requirements to keep redesigns honest.

## Coverage

| Case | File | Surface | Mode | What it proves | Gap |
|---|---|---|---|---|---|
| web — this page | `index.html` | Web landing page | System showcase + advocacy | Responsive web surface, theme switch, semantic HTML, 44px controls | Not a product web app |
| orbit | `terminal.html` | TUI + web dashboard | Greenfield | Host-owned palette, ANSI roles, advisory contrast, monochrome HC, surface isolation | Web is secondary; no full web app |
| relay | `cli.html` | CLI | Greenfield | stdout/stderr grammar, runtime color and width, exit codes, `--json` | No schema versioning |
| pulse | `mobile.html` | Mobile app | Rebuild | Whole screens, independent schemes, 48 dp, 2.0× text, motion tokens | No tablet/landscape |
| drift | `game.html` | Game UI (console + handheld) | Greenfield | Safe zones, controller prompts, redundant status, motion/flash safety | Touch target size not stated |
| emberhold | `game-rpg.html` | Game UI (fantasy RPG) | Greenfield | Three type registers, dialogue measure, rarity by frame + label | No handheld proof |
| asteria | `game-anime.html` | Game UI (anime gacha, landscape) | Greenfield | Bright world/dark panels, EN/JP, rarity frames | 44 px touch targets; portrait chat not shown |
| sugarfall | `game-casual.html` | Game UI (casual puzzle, mobile) | Greenfield | Shape-coded pieces, bounded motion, no dark patterns | None material |
| fieldstation | `print.html` | Print/document | Greenfield | Fixed canvas, shared grid, CMYK assumptions, grayscale, page types | Not a report-authoring example |

## Index

- [web — this page](index.html)
- [orbit — terminal](terminal.html)
- [relay — CLI](cli.html)
- [pulse — mobile](mobile.html)
- [drift — game UI](game.html)
- [emberhold — fantasy RPG](game-rpg.html)
- [asteria — anime gacha](game-anime.html)
- [sugarfall — casual puzzle](game-casual.html)
- [fieldstation — print](print.html)

## Source of truth

- Gallery: [`../index.html`](../index.html)
- Each case's requirement links to its HTML file. The HTML wins for current visual values; the requirement wins for intent when a redesign is being planned.
