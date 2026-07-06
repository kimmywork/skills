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

# Install plugin
claude plugin install kimmywork-skills@kimmywork-skills
```

---

## Skills

### Solution Delivery (8 skills)

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

### Utility (2 skills)

#### `cloudconvert`
> Convert non-text documents (PDF, DOC/DOCX, EPUB) to Markdown via CloudConvert CLI.

#### `style-extraction`
> Extract a structured writing style profile from an author's sample texts. Quantifiable features + executable rules + positive/negative examples. Supports English and Chinese.
