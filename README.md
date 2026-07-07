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
claude plugin install solution-delivery-loop@kimmywork-skills
claude plugin install utility@kimmywork-skills
claude plugin install loop@kimmywork-skills
```

---

## Skills

### Solution Delivery Loop (8 skills)

A compact, agent-neutral skill family for solution delivery:

`Sense → Shape → Design → Build → Verify → Record → Continue/Stop`

#### `solution-delivery-loop`
> Entry point and phase router. Triage requests, route to the right phase skill, and coordinate end-to-end delivery from request to accepted outcome.

#### `requirement-discovery`
> Shape ambiguous requests into clear requirements. Define users, scenarios, scope, non-goals, acceptance criteria, and verification expectations before any design or implementation begins.

#### `solution-design`
> Produce solution design with trade-off analysis, contract-first decisions, implementation slicing, and verification planning.

#### `implementation-execution`
> Execute plans with TDD-driven vertical-slice implementation. Implement features, fix bugs, refactor, or perform maintenance with integrated verification.

#### `delivery-acceptance`
> Evidence-based review of completed work. Evaluate Spec Fit and Code Fit, record verification evidence, and decide whether to ship, continue, roll back, or ask for user review.

#### `review-feedback`
> Independent cumulative review of phase artifacts. Completeness, correctness, consistency, clarity, and scope adherence checks.

#### `process-distillation`
> Extract process improvements from repeated friction or resolved review cycles.

#### `structured-investigation`
> Universal investigation methodology for research, tracing, root cause analysis, and deriving truth from primary sources.

---

### Loop (2 skills)

Create and execute recurring automated workflows.

#### `loopify`
> Create a workflow spec from natural language. Grills for clarity, drafts the spec, writes `workflows/<name>.md` on user confirmation.

#### `loopy`
> Execute scheduled or triggered workflows. Scans due workflows, runs each sequentially with full state tracking, failure handling, and atomic state updates.

---

### Utility (3 skills)

#### `cloudconvert`
> Convert non-text documents (PDF, DOC/DOCX, EPUB) to Markdown via CloudConvert CLI. Saves processing tokens by feeding agents clean Markdown instead of raw document formats.

#### `rationale`
> Decode agent-optimized artifacts (skill rules, code changes, design decisions) into human-comprehensible explanations. Trigger on "explain", "why", "rationale", or when reviewing dense agent outputs.

#### `style-extraction`
> Extract a structured writing style profile from an author's sample texts. Quantifiable features + executable rules + positive/negative examples. Supports both English and Chinese source texts.
