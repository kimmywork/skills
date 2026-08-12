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
claude plugin install loop@kimmywork-skills
claude plugin install utility@kimmywork-skills
```

---

## Skills

### Drafting (9 skills)

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

#### `restraint`
> Do what the user actually wants, and nothing more; avoid over-engineering.

---

### Loop (2 skills)

Create, validate, and execute permission-bounded recurring workflows.

#### `loopify`
> Create a workflow spec from natural language and write `workflows/<name>.md` after confirmation.

#### `loopy`
> Validate and execute scheduled or triggered workflows with explicit permissions, atomic leases, and deterministic state updates.

---

### Utility (4 skills)

#### `agent-facing-doc`
> Create, update, or review agent-facing documentation including AGENTS.md, SKILL.md files, and prompt templates.

#### `cloudconvert`
> Convert approved non-text documents to Markdown through the external CloudConvert service.

#### `rationale`
> Explain agent-optimized artifacts, code changes, concepts, and design decisions for human comprehension.

#### `style-calibration`
> Extract, validate, compare, and apply a writing style profile from samples.
