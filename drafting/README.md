# Drafting Loop

Universal work orchestration for crafting, composing, evaluating, investigating, and creating.

`drafting/` is a skill bundle that upgrades the older delivery workflow into a general-purpose work loop:

```text
Sense -> Clarify -> Shape -> Design -> Build -> Verify -> Record -> Continue/Stop
```

The bundle is agent-neutral, reference-driven, and designed for progressive disclosure: `SKILL.md` files stay short, while detailed procedures live in each skill's `references/` directory.

## What this bundle provides

- Universal phase orchestration with explicit state transitions.
- Work-kind routing for Crafting, Composing, Evaluating, Investigating, and Creating.
- Phase review and lightweight process audit before advancement.
- Multi-stage and multi-deliverable track support.
- Evidence-based acceptance and delivery records.
- Ground-truth isolation for build/review separation.
- Deep research, fact verification, audit trails, compliance gates, and cross-validation.
- Full style extraction, calibration, validation, and application workflow.

## Skill inventory

| Skill | Purpose |
|---|---|
| `drafting-loop` | Top-level orchestrator: phases, routing, checkpoints, state, handoffs. |
| `intent-routing` | Detect kind, phase, ambiguity, and correct workflow entry. |
| `guided-inquiry` | Socratic clarification for vague or exploratory work. |
| `scope-shaping` | Convert intent into scope, criteria, and verification plan. |
| `blueprinting` | Turn scope into executable design, contracts, increments, and checks. |
| `plan-execution` | Execute approved plans and record increment evidence. |
| `audit-trail` | Run evaluation/audit work as the deliverable. |
| `quality-review` | Review artifacts, route fixes/rollback, support two-stage review. |
| `fact-verification` | Verify claims against evidence and source chains. |
| `deep-research` | Investigate questions with source quality and confidence labels. |
| `style-calibration` | Extract, validate, and apply writing style profiles. |
| `cross-validation` | Run independent or adversarial second-perspective validation. |
| `compliance-gate` | Check compliance/integrity and manage overrides. |
| `acceptance-gate` | Decide delivery status from evidence and format-specific criteria. |
| `distillation` | Convert process friction into durable skill/framework improvements. |

## Core references

Key references live under `skills/drafting-loop/references/`:

- `state-machine.md` — legal/illegal phase transitions.
- `phase-review-and-process-audit.md` — review and process audit between phases.
- `multi-stage-tracks.md` — parent/stage and multi-deliverable protocol.
- `handoff-schemas.md` — phase-to-phase handoff contracts.
- `checkpoint-protocol.md` — FULL / SLIM / MANDATORY checkpoints.
- `ground-truth-isolation.md` — build/review rubric separation.
- `resume-ledger.md` — append-only continuation protocol for long work.
- `track-document-structure.md` — track frontmatter, scope-map, and parser use.

## Scripts

`drafting-loop` includes a small track parser:

```bash
python drafting/skills/drafting-loop/scripts/track_cli.py --help
```

Supported commands:

- `extract`
- `validate`
- `index`
- `children`
- `kanban`

## Process archive

Procedural implementation artifacts are archived under `docs/process/`:

- `improvement-plan.md`
- `coverage-matrix.md`
- `delivery-skill-coverage.md`
- `process-audit.md`
- `redesign-v1-universal-loop.md`
- `redesign-v2-universal-work-loop.md`

These documents are for maintainers and audits. Normal skill execution should rely on `SKILL.md` and in-skill `references/` files.

## Validation checklist

Before packaging or publishing:

```bash
for f in drafting/skills/*/SKILL.md; do test $(wc -l < "$f") -le 100 || echo "$f too long"; done
python drafting/skills/drafting-loop/scripts/track_cli.py --help
```

Also verify:

- `SKILL.md` files contain no Chinese characters outside frontmatter.
- `SKILL.md` internal references exist.
- Plugin JSON files parse.
- No generated artifacts such as `__pycache__/` are included.

## Deferred by design

The core bundle intentionally does not hard-code:

- runtime-specific subagent orchestration;
- concrete cross-model runner scripts;
- PDF/DOCX/PPTX/XLSX annotation tooling;
- web-search agent modules;
- APA/IRB/venue-specific academic rules;
- rename-specific process checklists.

Add those only as separate specializations or adapters when concrete usage evidence justifies them.
