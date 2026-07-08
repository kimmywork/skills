# kimmywork/skills

A collection of AI agent skills for knowledge work, workflow automation, and daily productivity.

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
claude plugin install drafting-loop@kimmywork-skills
claude plugin install loop@kimmywork-skills
claude plugin install utility@kimmywork-skills
```

---

## Skills

### Drafting Loop (16 skills)

Universal work orchestration for crafting, composing, evaluating, investigating, and creating.

```text
Sense → Clarify → Shape → Design → Build → Verify → Record → Continue/Stop
```

A compact, agent-neutral skill family that upgrades the older delivery workflow into a general-purpose work loop. Short `SKILL.md` files with detailed references for progressive disclosure.

#### `drafting-loop`
> Top-level orchestrator: phases, routing, checkpoints, state transitions, and handoffs across all work kinds.

#### `triage`
> Detect work kind, phase, ambiguity level, and correct workflow entry point from mixed artifacts and unclear next steps.

#### `probing`
> Socratic clarification for vague or exploratory work. Surface the real target, narrow competing directions, and frame hard decisions.

#### `scope-shaping`
> Convert existing intent, notes, requirements, or partial materials into an executable scope, brief, criteria set, or research question.

#### `blueprinting`
> Design an executable approach, architecture, methodology, outline, or staged plan before implementation or delivery.

#### `plan-execution`
> Execute a defined task, plan, or constrained deliverable while preserving scope, evidence, and change awareness.

#### `acceptance-gate`
> Evidence-based delivery decision: delivered, partial, blocked, needs-review, or rolled-back.

#### `inspect`
> Independent review of existing artifacts to find issues, judge readiness, and guide revision.

#### `audit-trail`
> Formal audit or assessment report on an existing artifact using stated or inferred criteria, evidence tracing, and scoped findings.

#### `fact-verification`
> Check factual claims, citations, quotations, numbers, and source alignment against evidence.

#### `deep-research`
> Investigate questions through source-based research, tracing, synthesis, and uncertainty management.

#### `challenge`
> Stress-test plans, designs, drafts, or conclusions by exposing hidden assumptions, edge cases, failure modes, and unresolved trade-offs.

#### `cross-validation`
> Obtain a second perspective on a claim, design, review, or conclusion to reduce blind spots and resolve uncertainty.

#### `compliance-gate`
> Assess compliance, constraint fit, disclosures, and override risk for policy, legal, audit, safety, or integrity work.

#### `style-calibration`
> Extract, validate, compare, and apply a writing style profile from samples. Voice matching, style diagnosis, and style-guided rewriting.

#### `distillation`
> Turn repeated friction, failures, review feedback, or successful patterns into durable workflow, template, script, or skill improvements.

---

### Loop (2 skills)

Create and execute recurring automated workflows.

#### `loopify`
> Create a workflow spec from natural language. Grills for clarity, drafts the spec, writes `workflows/<name>.md` on user confirmation.

#### `loopy`
> Execute scheduled or triggered workflows. Scans due workflows, runs each sequentially with full state tracking, failure handling, and atomic state updates.

---

### Utility (2 skills)

#### `cloudconvert`
> Convert non-text documents (PDF, DOC/DOCX, EPUB) to Markdown via CloudConvert CLI. Saves processing tokens by feeding agents clean Markdown instead of raw document formats.

#### `rationale`
> Decode agent-optimized artifacts (skill rules, code changes, design decisions) into human-comprehensible explanations. Trigger on "explain", "why", "rationale", or when reviewing dense agent outputs.