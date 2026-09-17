# Design System Checklists

Three sweeps to run before calling a design system finished. Everything here is **reference material for deriving your own decisions** — none of it is meant to be copied into the deliverable or applied mechanically.

## 1. Principles sweep

Walk the established frameworks below. **Treat every line as a reference, not a script.** The point is to understand what the principle protects and then derive questions that fit this product — they will usually be more specific and more useful than the examples here. Do not march through the list asking each one in turn.

For each principle: derive the product-specific question, and record an answer as a rule only when it changes a decision. Write the rule in the product's own words, and merge duplicates across frameworks (consistency appears in several; keep one).

| Framework | Principle | Example question to ask |
| --- | --- | --- |
| Nielsen | Visibility of system status | Does the UI always say what it is doing and what just changed? |
| Nielsen | Match to the real world | Do terms and orderings match the user's domain, not the code's? |
| Nielsen | User control and freedom | Can the user undo, exit, and take back control at every step? |
| Nielsen | Consistency and standards | Does the same action have the same shape, name, and place everywhere? |
| Nielsen | Error prevention | Are invalid states made impossible rather than reported? |
| Nielsen | Recognition over recall | Are available options and syntax visible instead of remembered? |
| Nielsen | Flexibility and efficiency | Do frequent users have a faster path without hurting newcomers? |
| Nielsen | Aesthetic and minimalist design | Is anything on screen not needed for the current task? |
| Nielsen | Help users recover from errors | Does every failure say what happened and what to do next? |
| Nielsen | Help and documentation | Is guidance available at the point of need? |
| Shneiderman | Consistency | Same as Nielsen above; merge, do not duplicate. |
| Shneiderman | Universal usability | Does it work for varied input, language, and ability? |
| Shneiderman | Informative feedback | Is feedback immediate and proportional to the action? |
| Shneiderman | Dialog closure | Does a multi-step task confirm completion? |
| Shneiderman | Easy reversal | Is undo easy enough that users will explore? |
| Shneiderman | Internal locus of control | Do users initiate actions rather than react to the system? |
| Shneiderman | Reduce memory load | Is information carried by the interface instead of the user's head? |
| Norman | Affordance and signifier | Does a clickable thing look clickable, including in dark mode? |
| Norman | Mapping | Are controls placed next to or on the thing they affect? |
| Norman | Feedback | Does the system answer every action, without animation theatre? |
| Norman | Constraint | Are the wrong choices unavailable rather than punished? |
| Norman | Conceptual model | Is the mental model consistent enough to predict behavior? |
| Norman | Slips vs mistakes | Are frequent slips prevented by layout, mistakes by explanation? |
| Gestalt | Proximity and common region | Do spacing and grouping express the real relationships? |
| Gestalt | Similarity and common fate | Do like things look alike, and do they move together? |
| Gestalt | Continuity and closure | Are sequences readable without decorative connectors? |
| Gestalt | Figure/ground | Does the main content win over chrome and background? |
| POUR | Perceivable | Is information available without relying on one sense? |
| POUR | Operable | Is everything reachable by keyboard and pointer? |
| POUR | Understandable | Is behavior predictable and wording plain? |
| POUR | Robust | Does it hold up across hosts, zoom, and assistive tech? |

### General aspects

Beyond the frameworks, every design system has to answer these aspects. They name **areas to examine, not questions to ask** — derive the actual questions from the product, and add aspects this list misses.

- **States** — empty, loading, error, partial, over-full, each shown in the form it actually appears (inline, whole panel, whole screen), never one generic box. Usually the states that get skipped, and the ones users hit first.
- **Extremes** — one item, thousands, a single unbroken string, a huge number, missing media.
- **Data versus decoration** — which values belong to the user's records and must not move when the theme changes.
- **Interaction states** — default, hover, focus, active, disabled, for every clickable thing.
- **Primary action** — how many compete per view.
- **Elevation** — the default, and the conditions for breaking it.
- **Dark mode** — whether hierarchy survives the switch or is only inverted.
- **Density** — who decides it, and how variants are named.
- **Motion** — what is allowed to move, and what never moves.
- **Long-form reading** — how it differs from interface chrome.
- **Reversibility** — which destructive actions can be undone and which need confirmation.
- **Naming parity** — the same concept across code, specification, and screen; axis names (scheme, mode, density) must not reuse vocabulary the product already uses for something else.
- **Extensibility** — what it costs to absorb a new surface or host.
- **Host-owned surfaces** — terminals and OS high-contrast modes where the app cannot read or set the palette; state what the app still controls (weight, dim, layout, glyphs) and how meaning survives without color.
- **Non-visual use** — color, motion, and pointer independence.

## 2. Foundations coverage

Each foundation must state both its tokens and its rules.

- **Color** — schemes and modes as separate axes; surface and elevation tokens; borders; semantic roles (warning, error, success, info) that follow mode rather than scheme; an explicit note on which colors are data rather than decoration. When a host owns the palette (terminal, OS, third party), tokens are roles, not values; no meaning may depend on a host color; any high-contrast choice declares the background it assumes; and the escape hatch is the host's default foreground plus weight, never a brighter host color.
- **Typography** — UI face versus long-form face; locale-dependent faces; a fixed type scale with role names; reading size tiers exposed as variables. Where the surface has expressive moments, a display/effect face is a separate token with a stated register — it never carries instructions or body text, and changing values use tabular numerals.
- **Copy** — the term table; tone; empty, loading, and error phrasing.
- **Layout** — base unit; page gutters; reading measure; column widths; breakpoints and exactly what collapses.
- **Components** — ordered atomic → layout → interactive; each with a properties table, its rules, and its rationale; density variants named.
- **Motion** — duration tokens with their roles; what must never animate.
- **Accessibility** — the requirements plus the measured results that prove them.

## 3. Verification

- **Contrast** — for controlled surfaces, enumerate the pairs components actually render: every foreground against every plane it lands on, plus focus rings and meaningful boundaries, for every scheme × mode. Report the numbers and fix the tokens that fail. For host-owned palettes, report advisory numbers against a named reference palette and prove the structural fallback instead.
- **Drift** — parse the specification and the showcase and fail the check when a token name or value disagrees, or when a surface references another surface's token that was not declared shared.
- **Coverage** — a check covers exactly the classes it claims (tokens, colors, lengths, cross-surface references). Where possible, generate the specification and the showcase from one token source so drift is impossible rather than merely detectable.
- **Checkers are tested** — mutate the artifact and confirm the check fails; a green check with untested coverage is not evidence.
- **Blur** — mark designed values as designed. Mark recovered values with the file they came from.
- **Interactions** — exercise the showcase's real controls (theme, scheme, tabs, navigation), not just its rendering.
- **Structure** — the table of contents and section ids come from what actually rendered, not from a list maintained beside it; no hidden placeholders or string-level structural edits.
- **Fit** — the showcase does not overflow horizontally at its narrowest target width; wide tables scroll inside their container; inline assets carry explicit sizes; derived colors are computed from tokens.
- **Scenes** — every whole-use scene renders in every scheme and mode; check layout, not only token values.
- **Naming** — if the stylesheet is injected into pages you do not own, prefix every variable and never emit root-level declarations; if tokens are mapped onto a framework's theme, avoid keys the framework already defines and confirm the emitted CSS.
- **Scale** — check the type scale, radii, hit targets, and durations for values that are off the declared scale.
