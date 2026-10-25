# kimmywork/skills

A collection of agent-neutral skills for knowledge work, workflow automation, and daily productivity.

## Installation

### via `npx skills`

```bash
npx skills add kimmywork/skills
```

To install specific skills:

```bash
npx skills add kimmywork/skills --skill <skill-name> [<skill-name> ...]
```

### via Claude plugin

```bash
# Add the marketplace source
claude plugin marketplace add kimmywork/skills

# Install plugins
claude plugin install drafting@kimmywork-skills
claude plugin install design@kimmywork-skills
claude plugin install loop@kimmywork-skills
claude plugin install utility@kimmywork-skills
```

---

## Skills

### Drafting (11 skills)

[Drafting skills](drafting/README.md).

Independent, general-purpose skills for exploring, planning, executing, researching, challenging, and verifying work. There is no top-level orchestrator or required phase protocol.

#### `probing`
> Explore an uncertain goal with the user until a useful direction, decision, or target emerges.

#### `deep-research`
> Investigate questions through source-based evidence, tracing, comparison, synthesis, and explicit uncertainty.

#### `increment`
> Reach agreement on requirements, create a plan of verifiable increments, and optionally execute it one increment at a time.

#### `challenge`
> Pressure-test an existing artifact, plan, idea, conclusion, or decision.

#### `vnv`
> Verify and validate existing work for plan adherence, correctness, acceptance, compliance, factuality, review readiness, or second-perspective confidence.

#### `align`
> Keep project documentation aligned when implementation, requirements, decisions, or research evidence changes.

#### `distillation`
> Summarize and retrospect on work, then decide whether the lessons justify extracting or updating a skill.

#### `worklog`
> Record completed workspace changes as traceable daily log entries and maintain a current workstate snapshot.

#### `parkinglot`
> Park out-of-scope issues in `PARKING_LOT.md` instead of fixing them immediately, then review them in batches to find shared causes.

#### `restraint`
> Do what the user actually wants, and nothing more; avoid over-engineering.

#### `prune`
> Subtract what is unnecessary — obsolete workspace clutter and overgrowth in a drafted design or plan — keeping the smallest necessary and sufficient set.

---

### Design (2 skills)

[Design skills](design/README.md).

Build or govern a design system, review a product or design artifact with evidence, and present ideas to an audience.

#### `design`
> Build, extract, rebuild, or govern a design system; review a product or design artifact and produce an issue register, fix plan, and guard rules.

#### `presentation`
> Create a live, written, or hybrid presentation — talk, sharing session, demo, panel, pitch, workshop, report, or one-pager — with narrative, language, timing, visual, and accessibility discipline.

---

### Loop (2 skills)

[Loop skills](loop/README.md).

Create, validate, and execute permission-bounded recurring workflows.

#### `loopify`
> Create a workflow spec from natural language and write `workflows/<name>.md` after confirmation.

#### `loopy`
> Validate and execute scheduled or triggered workflows with explicit permissions, atomic leases, and deterministic state updates.

---

### Utility (5 skills)

[Utility skills](utility/README.md).

#### `agent-facing-doc`
> Create, update, or review agent-facing documentation including AGENTS.md, SKILL.md files, and prompt templates.

#### `cloudconvert`
> Convert approved non-text documents to Markdown through the external CloudConvert service.

#### `bootstrapping`
> Start a new project — establish conventions, principles, structure, and infrastructure; generate the agreed artifacts.

#### `rationale`
> Explain agent-optimized artifacts, code changes, concepts, and design decisions for human comprehension.

#### `style-calibration`
> Extract, validate, compare, and apply a writing style profile from samples.

---

## Showcases

Example outputs of the `design` skill, one per surface class. Each is a single self-contained HTML file; typography demos load webfonts with system fallbacks:

| Case | Surface | Demonstrates |
|---|---|---|
| [terminal](docs/showcases/terminal.html) | TUI + Web | Host-owned palette, ANSI roles, monochrome high-contrast fallback, surface isolation check |
| [cli](docs/showcases/cli.html) | CLI | stdout/stderr grammar, exit codes, TTY/`NO_COLOR`/CI modes, runtime width |
| [mobile](docs/showcases/mobile.html) | Mobile app | Whole-screen scenes, independent light/dark, touch and safe-area annotations, live probes |
| [game](docs/showcases/game.html) | Game UI · sci-fi action | Safe zones, controller prompts, colorblind and motion proofs, handheld orientations |
| [game-rpg](docs/showcases/game-rpg.html) | Game UI · fantasy RPG | Display/UI/text type registers, dialogue measure, parchment surfaces, rarity by frame |
| [game-anime](docs/showcases/game-anime.html) | Game UI · anime gacha | Landscape world + dark menu panels, live EN/日本語 toggle, inventory/achievements/summon screens, rarity by frame + stars + label |
| [game-casual](docs/showcases/game-casual.html) | Game UI · casual puzzle | Shape-coded pieces, bounded motion, one-thumb targets, no dark patterns |
| [print](docs/showcases/print.html) | Print | Fixed canvas, shared grid, grayscale proof, print color values |

Gallery: [`docs/showcases/index.html`](docs/showcases/index.html). Install the skill: `npx skills add kimmywork/skills --skill design` · Skill doc: [SKILL.md](https://skills.kimmy.fun/design/skills/design/SKILL.html).

### Presentation decks

Eight fictional decks from the `presentation` skill: academic defense, Series A pitch, incident postmortem, architecture review, keynote, workshop, business review, and product launch. Each is a self-contained HTML deck with speaker notes, a time budget, and an inferred requirements document.

[Presentation deck gallery](docs/presentations/index.html).
