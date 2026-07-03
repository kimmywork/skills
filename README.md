# kimmywork/skills

A collection of AI agent skills for software delivery and daily productivity.

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
claude plugin install software-delivery-loop@kimmywork-skills
claude plugin install utility@kimmywork-skills
```

---

## Skills

### Software Delivery Loop (6 skills)

A compact, agent-neutral skill family for end-to-end software delivery:

`Sense → Shape → Design → Build → Verify → Record → Continue/Stop`

#### `software-delivery-loop`
> Entry point and phase router. Triage requests, route to the right phase skill, and coordinate end-to-end delivery from request to accepted outcome. Supports manual, collaborative, and autonomous loops.

#### `requirement-discovery`
> Shape ambiguous software requests into clear requirements. Define users, scenarios, scope, non-goals, acceptance criteria, and verification expectations before any design or implementation begins.

#### `solution-design`
> Produce solution design with trade-off analysis, architecture decisions, contract-first design, implementation slicing, and verification planning. Takes clear requirements and produces actionable plans.

#### `code-investigation`
> Structured methodology for code-level investigation and analysis. Understand unfamiliar codebases, map data models across systems, trace data flows, analyze protocols or message formats by reading source code. Use when you need to derive truth from code, not documentation.

#### `implementation-execution`
> Execute software plans with TDD/E2E-driven vertical-slice implementation. Implement features, fix bugs, refactor, or perform maintenance with integrated verification. Assumes scope, design, and verification expectations are already clear.

#### `delivery-acceptance`
> Evidence-based review of completed work. Evaluate Spec Fit (does it meet requirements?) and Code Fit (is it well-built?), record verification evidence, and decide whether to ship, continue iterating, roll back, or ask for user review.

---

### Utility (1 skill)

#### `cloudconvert`
> Convert non-text documents (PDF, DOC/DOCX, EPUB) to Markdown via CloudConvert CLI. Saves processing tokens by feeding agents clean Markdown instead of raw document formats. Skips already-readable formats (`.txt`, `.md`, `.json`, `.csv`).