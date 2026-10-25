# Design Landing Page — Web Requirements

> Source: [`../index.html`](../index.html) · Surface: web landing page · Mode: System showcase + advocacy · Case: web
> Purpose: present the Design skill and the eight cases as a realistic web surface, not a static poster.

## 1. Problem and context

**Who:** designers and engineers evaluating the skill; people who need to see what it produces before installing it.

**Jobs:** understand what the skill does, inspect the evidence, open a case, read the requirements, and install or read the skill.

**Constraints:** one self-contained HTML page; no build step; system-font fallbacks; light and dark themes; keyboard and touch; no horizontal overflow at the narrowest target width.

**Boundary:** this is a **web landing page**, not a full product web app. It demonstrates responsive layout, theme switching, semantic HTML, and focus behavior. It does not exercise routing, deep links, IME, or product data states; those remain open for a dedicated web-app case.

## 2. Principles

| Rule | Rationale |
|---|---|
| Show, don't tell | The page itself must demonstrate the web surface it claims: tokens, themes, focus, targets, and responsive layout. |
| Evidence over decoration | Every case card states what the case proves; the proof grid names the claim, not a vague benefit. |
| One page, many proofs | The gallery is both the index and the Web case; it should not require a second artifact to be credible. |
| Advocacy without inflation | The copy says what the skill does and what it does not do. It does not claim a full web-app case or a complete spec/drift deliverable. |
| Accessible by construction | Semantic landmarks, skip link, visible focus, 44px controls, contrast, and reduced-motion support. |

## 3. Experience requirements

### Header

- Brand link to the top.
- Primary navigation: Cases, System, Review, Requirements.
- Install anchor and a theme toggle.
- Header remains usable at narrow widths; secondary navigation may collapse.

### Hero

- State the skill's promise in one headline and one short paragraph.
- Offer two actions: explore the cases, read the skill.
- Show a compact collage of surfaces: terminal, mobile, game, print.
- Label the page as the Web surface.
- Show the scale: 2 modes, 8 cases, 6 surface classes, 1 self-contained page.

### System / Review

- Explain the two directions of the skill and their outputs.
- System: extract, rebuild, greenfield, govern; showcase, specification, drift check.
- Review: product, artifact, system; review report, issue register, fix plan, guard rules.

### Cases

- Eight case cards, each with a preview, surface label, mode, description, facts, case link, and requirements link.
- Cards must be readable without the preview; the preview is decorative.
- Keep case numbers aligned with the source case files.

### Proof grid

- Name the specific claim each case proves.
- Link each proof to its case.

### Requirements

- Explain that each case has an inferred requirements document.
- Link to the requirements README and each case document.
- Include the Web case itself.

### Install

- Show the `npx` install command and the Claude plugin command.
- Provide a copy button with a visible result.
- Link to SKILL.md, GitHub, and requirements.

### Footer

- State the bundle and the web-case claim.
- Repeat the primary links.

## 4. Visual requirements

### Color and themes

- Light theme: warm paper background, ink text, deep green accent.
- Dark theme: near-black background, warm white text, bright teal accent.
- The install panel is an inverted surface with its own scoped tokens; it must remain readable in both themes.
- Accent is used for links, labels, and one primary action; it is not a decorative wash.

### Typography

- Serif display for headlines; sans for body and UI; mono for labels, commands, and metadata.
- Type scale: hero `clamp(48px, 7.2vw, 92px)`, section headings `clamp(32px, 4.6vw, 56px)`, body 16–18px.
- No external webfonts; system faces keep the page offline-readable.

### Layout

- Max width 1180px; fluid gutters.
- Hero: two columns above 960px; one column below.
- Cases: `auto-fit` grid, minimum 330px; one column on narrow screens.
- Requirements: two columns above 960px; one column below.
- Install: two columns above 960px; one column below.
- No horizontal overflow at 360px, 390px, 768px, or 1280px.

### Interaction

- Theme toggle persists the choice and updates `aria-pressed` and the accessible label.
- Copy button uses the clipboard API with a fallback; it announces success textually.
- Hover and focus states are visible; focus is never removed.
- Touch controls are at least 44×44; inline prose links are the exception.

## 5. Accessibility requirements

- Semantic `header`, `nav`, `main`, `section`, `footer`; one `h1`; logical heading order.
- Skip link to `#main`.
- Visible `:focus-visible` outline.
- Theme toggle has an accessible name and pressed state.
- Case previews are decorative (`aria-hidden`, not tabbable); the title and action links carry the task.
- Contrast: body and muted text at least 4.5:1; large text at least 3:1; install panel measured in both themes.
- Respect `prefers-reduced-motion`; no animation is required to understand the page.
- No meaning depends on color alone.
- Page remains usable at 200% zoom and 360px width.

## 6. Verification requirements

- No console errors; no 404 for the favicon or local links.
- No horizontal overflow at 360, 390, 768, and 1280px.
- All local links resolve: eight cases, eight requirement docs, gallery, skill doc, GitHub.
- Theme toggle switches both ways and persists.
- Copy button copies the install command and reports success.
- Primary controls are at least 44×44; focus is visible.
- Contrast passes for body, muted, accent, and the inverted install panel in both themes.
- The page works offline with system fonts.

## 7. Non-goals

- Do not turn the page into a full product web app.
- Do not add a build step, framework, or external font dependency.
- Do not claim the cases include a separate specification or drift check; they are showcase artifacts.
- Do not hide the requirements behind the cases; link them directly.

## 8. Open questions

- Should the page include a dedicated "Web" case card, or is the page itself enough? Current choice: the page itself is the Web case, labeled in the surface strip.
- Should the page add a product web app case later for routing, IME, and data states? Recommended if the skill needs to prove `web-app-surfaces.md` at full strength.
- Should the gallery show a "Requirements" link on every card, or only in the requirements section? Current choice: both.
