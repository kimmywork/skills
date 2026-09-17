# TUI Enhancement Proposal — `design-system` skill

> **Status:** draft, awaiting review. **No skill file has been changed.**
> **Scope:** proposed additions to `.agents/skills/design-system/SKILL.md` and `.agents/skills/design-system/resources/checklist.md`.
> **Origin:** the Agilegend TUI + WebUI design-system task (spec at `docs/design/DESIGN_SYSTEM.md`, showcase at `docs/design/showcase.html`, drift check at `docs/design/check-tokens.mjs`), including the defect the user found where the Web theme (`dawn`) changed TUI text color.
>
> **How to review:** approve or reject each edit `E1`–`E6`. `E1`–`E4` are the minimum justified set; `E5`–`E6` are optional and add a terminal-specific reference section.

---

## 1. Context

The `design-system` skill is capable and was usable, but it is written as if every surface is a DOM page the system fully controls. It has:

- no notion of a surface whose palette the **host owns** (a terminal, an OS high-contrast mode, a third-party embed);
- no rule preventing one surface's theme from leaking into another's samples;
- contrast language ("measure every pair, fix the tokens") that is unsatisfiable for a terminal, where the app cannot read or set RGB;
- verification language that does not require enumerating the pairs components **actually** render, nor negatively testing the checker itself.

The Agilegend task hit each of these in practice. The proposals below are derived from observed failures, not hypothetical ones.

## 2. Gap analysis (evidence-backed)

| # | Current skill text | What happened in the task | Proposed fix |
| --- | --- | --- | --- |
| G1 | `SKILL.md:35` "Contrast is computed. Measure every foreground/background pair…" | Terminal palette is unknowable; no single ANSI role is legible on both light and dark backgrounds (measured: white 1.26 on light; blue 1.77, red 2.85 on dark). The rule as written cannot be met. | `E1` |
| G2 | No surface-isolation rule anywhere | `tui-text` was mapped to `inherit`, so switching the Web theme to `dawn` made TUI text dark-on-black. | `E2` |
| G3 | `checklist.md:68` Color foundation | Does not say that host-owned palettes require **roles, not values**, nor that a high-contrast choice must declare the background it assumes. | `E3` |
| G4 | `checklist.md:78` Verification → Contrast | The measured pair set was chosen, not enumerated; it missed a real 4.41:1 failure in `dawn` standard. | `E4a` |
| G5 | `SKILL.md:33` "no hardcoded style values"; `checklist.md:79` Drift | The spec claimed the checker tested lengths; it only tested colors, and the showcase had 18 raw lengths. The check was green while its stated coverage was false. | `E4b` |
| G6 | Generic aspect list (`checklist.md:45-62`) | Axis names `scheme`/`mode` collided with the product's existing `permissionMode` and `/mode`; the skill gives no naming-collision warning. | optional `E5` |
| G7 | No terminal reference material | Every TUI principle had to be derived from scratch (roles vs values, monochrome high-contrast, glyph table, cell-unit layout). | optional `E6` |

## 3. Candidate TUI design principles

Reusable principles distilled from the task. These are surface-agnostic enough to belong in the skill's reference material, not just in one project's spec.

1. **Roles, not values.** A host-owned palette cannot be read or set; name roles (`cyan`, `bold`, `dim`), never RGB.
2. **Meaning never depends on an uncontrolled color.** Every colored element also carries a word or glyph.
3. **The redundant label must itself use the default foreground.** Otherwise the "color is redundant" mitigation is void when the label is painted in a low-contrast role.
4. **Provide a monochrome high-contrast path.** Because no ANSI role is legible on both a light and a dark background, high contrast uses the host default foreground plus weight, not a "brighter" color.
5. **Scope each high-contrast choice to the background it assumes.** `white` is only valid on a dark background; if the host scheme cannot be detected, state the assumption or do not ship it.
6. **Host-owned palette ⇒ advisory measurement.** Measure against a named reference palette, label it advisory, and enforce legibility structurally.
7. **The cell is the layout unit.** Fixed-row gaps, N-cell indents, `…` truncation, status line collapsing from the outside in, never horizontal scroll.
8. **Type control is weight, dim, italic only.** There is no font axis.
9. **Emoji are not an icon system.** Variable width; use a glyph table with ASCII fallbacks.
10. **Surfaces stay isolated.** Shared vocabulary, never shared tokens; one theme must not move another surface's pixels.

## 4. Candidate general lessons

1. Contrast must be enumerated from **what components actually render** (foreground × every plane it lands on, plus focus rings and meaningful boundaries), not from a hand-picked sample.
2. A focus ring must be measured against the plane it lands on, and no ancestor may clip it (`overflow: hidden` on a control group is a defect).
3. Token-axis names must not reuse vocabulary the product already uses.
4. A verification claim must match the checker's actual coverage, and the checker must be **negatively tested** (mutate a value, confirm failure).
5. Two artifacts should be generated from one token source to make drift structurally impossible; otherwise drift is only detectable after the fact.

---

## 5. Proposed edits

Exact anchors and before/after text. Quoted text is the proposed replacement.

### E1 — `SKILL.md`, Non-negotiables, line 35 (required)

**Before**

```
- **Contrast is computed.** Measure every foreground/background pair in every scheme and mode; report the numbers and fix the tokens that fail.
```

**After**

```
- **Contrast is computed where it can be.** For surfaces whose palette the system controls, measure every pair a component actually renders, in every scheme and mode, and fix the tokens that fail. For surfaces whose palette the host owns (terminal, OS high-contrast, third-party embed), tokens name roles rather than values; measurement against a named reference palette is advisory, and legibility is enforced structurally — meaning never depends on a color, and a monochrome high-contrast path uses the host's default foreground.
```

### E2 — `SKILL.md`, Non-negotiables, after line 36 (required)

**Add**

```
- **Surfaces stay isolated.** A system may share vocabulary across surfaces, but tokens, components, and layout stay per-surface. One surface's theme must never alter another's pixels, and the drift check fails on any cross-surface token reference.
```

### E3 — `checklist.md`, Foundations → Color, line 68 (required)

**Before**

```
- **Color** — schemes and modes as separate axes; surface and elevation tokens; borders; semantic roles (warning, error, success, info) that follow mode rather than scheme; an explicit note on which colors are data rather than decoration.
```

**After**

```
- **Color** — schemes and modes as separate axes; surface and elevation tokens; borders; semantic roles (warning, error, success, info) that follow mode rather than scheme; an explicit note on which colors are data rather than decoration. When a surface's palette is owned by its host (terminal, OS, third party), tokens are **roles, not values**, no meaning may depend on a host color, any high-contrast choice declares the background it assumes, and the escape hatch is the host's default foreground plus weight — not a brighter host color.
```

### E4 — `checklist.md`, Verification, lines 78–79 (required)

**Before**

```
- **Contrast** — compute every foreground/background pair for every scheme × mode combination. Report the numbers; fix the tokens that fail rather than the report.
- **Drift** — parse the specification and the showcase and fail the check when a token name or value disagrees.
```

**After**

```
- **Contrast** — for controlled surfaces, enumerate the pairs components actually render: every foreground against every plane it lands on, plus focus rings and meaningful boundaries, for every scheme × mode. Report the numbers and fix the tokens that fail. For host-owned palettes, report advisory numbers against a named reference palette and prove the structural fallback instead.
- **Drift** — parse the specification and the showcase and fail the check when a token name or value disagrees, or when a surface references another surface's token.
- **Checkers are tested** — a drift, literal, or contrast check must cover exactly the classes it claims (tokens, colors, lengths, cross-surface references), and must be proven by mutating the artifact and confirming the check fails.
```

### E5 — `checklist.md`, General aspects (optional)

**Add one bullet to the list at lines 49–62**

```
- **Host-owned surfaces** — terminals and OS high-contrast modes where the app cannot read or set the palette; state what the app still controls (weight, dim, layout, glyphs) and how meaning survives without color.
```

### E6 — `checklist.md`, new section 4 "Terminal surfaces" (optional)

Append the section from §3 above as reference material, so terminal principles are available without re-deriving them. This is the largest optional change; it adds ~12 lines.

---

## 6. Non-goals (deliberately excluded)

- Agilegend-specific values, the `dusk`/`dawn` palette, the pair list, and the `theme`/`contrast` naming are **project decisions**, not skill material. Only the abstract rules are proposed.
- No restructuring of the skill, no new modes, no change to the two-artifact output contract.
- No new skill. A separate `terminal-ui-design` skill would overlap this skill's trigger ("a shared visual and interaction language across surfaces") and split one capability.

## 7. Approval checklist

- [ ] `E1` Contrast for host-owned palettes
- [ ] `E2` Surface isolation
- [ ] `E3` Color foundation: roles not values
- [ ] `E4` Verification: enumerate rendered pairs + test the checker
- [ ] `E5` (optional) General aspect: host-owned surfaces
- [ ] `E6` (optional) New "Terminal surfaces" reference section

If approved, the change is 4–6 text edits; skill boundaries, triggers, and output stay unchanged.

## Appendix — evidence index

| Evidence | Location |
| --- | --- |
| Design system spec | `docs/design/DESIGN_SYSTEM.md` |
| Live showcase (token source of truth, TUI panels) | `docs/design/showcase.html` |
| Drift / literal / cross-surface check | `docs/design/check-tokens.mjs` |
| TUI role table and monochrome high-contrast | `DESIGN_SYSTEM.md` §5.1 |
| Measured contrast, 59 pairs × 4 combinations | `DESIGN_SYSTEM.md` §6.1 |
| ANSI reference palette (white 1.26 light; blue 1.77, red 2.85 dark) | `DESIGN_SYSTEM.md` §6.1 advisory table |
| Naming collision (`permissionMode`, `/mode`) | `packages/agent-core/src/harness.ts:180`, `commands.ts:316-317` |
| Theme-leak fix and guard | `showcase.html` `parseAnsi`, `check-tokens.mjs` rule 5 |
