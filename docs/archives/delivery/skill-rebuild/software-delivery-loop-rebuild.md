# Software Delivery Loop Skill Rebuild

## Status

Initial draft created.

## Source Material Reviewed

- `myz-skills/workspace-delivery-loop/`
- `legacy-wdl/`
- `reference-skills/tashan-development-loop/`
- `reference-skills/using-superpowers/`
- Superpowers planning, TDD, verification, code review, and execution skills
- Matt Pocock engineering/productivity skills: PRD, TDD, codebase design, domain modeling, code review, prototype, research, grilling, handoff
- `reference-docs/loop-engineering.md` by Addy Osmani
- Representative historical tracks from `tracks/`: Constype, CRM/Yuanlu, MyZ agent, Mono Services Notes, Agent47, NG design, Heros
- Frequency scan over all markdown files in `tracks/`

## Historical Lessons

1. Useful delivery docs repeatedly include scope, non-goals, acceptance criteria, verification plan, risks/rollback, and status/progress.
2. Over-engineering must be challenged early; Constype v1 architecture review and ECN showed the value of narrowing scope and deployment modes.
3. Track docs should be feature-scoped, not scattered flat under `docs/track`.
4. PRDs remain useful for broad, user-facing, multi-module, ambiguous, or long-lived work.
5. Simple work still needs a compact track note when it changes behavior or preserves delivery knowledge.
6. Schema-first should generalize to contract-first: data, API, route, UI, CLI, storage, and module contracts.
7. Verification evidence is mandatory before completion claims.
8. ADR/CONTEXT are conditional tools, not mandatory ceremony.
9. Cross-feature durable knowledge should live under `docs/knowledge`, while operational logs should live under `docs/logs/YYYY-MM-DD.md`.
10. Agent autonomy is allowed when evidence is sufficient; human input is required for unclear software intent, trade-offs, scope, risk, or acceptance.

## Design Decisions

### Skill family over monolith

Created an atomic family:

- `software-delivery-loop`
- `requirement-discovery`
- `solution-design`
- `implementation-execution`
- `delivery-acceptance`

Rationale: smaller context footprint, clearer trigger conditions, reusable phases.

### Loop model

Adopted:

`Sense → Shape → Plan → Build → Verify → Record → Continue/Stop`

Rationale: incorporates Addy Osmani's loop engineering while preserving collaborative, inspectable delivery.

### Automation stance

Autonomous execution is allowed for obvious bugfixes, maintenance, planned tasks, test repairs, and documentation sync when sufficient evidence exists. The loop stops for user input when software intent, risk, scope, or acceptance judgment is required.

### Subagents

Subagents are supported but not required. Recommended roles: explorer, maker, checker/reviewer. If unavailable, the agent performs a fresh self-review and records the limitation.

### Worktrees

Not required by default. They are optional for parallel work or environment-provided isolation.

### Track layout

Normal feature:

```text
docs/track/<feature-name>/
  prd-v1.md
  plan-v1.md
  delivery-record-v1.md
  loop-state.md
  changes/change-note-0001.md
```

Multi-project:

```text
docs/track/<project-name>/<feature-name>/...
```

Simple work:

```text
docs/track/features/<feature-name>.md
docs/track/bugfix/<bug-description>.md
```

### Cross-feature knowledge and logs

Use `docs/knowledge` for ADRs, architecture notes, domain terms, reusable contracts, and durable decisions. Use `docs/logs/YYYY-MM-DD.md` for operational work logs. Docs may be stale; when docs conflict with code/tests/runtime behavior, verify the truth and update docs.

## Rejected Approaches

### Directly use Tashan

Rejected because it is too heavy and mandates patterns not desired for all work.

### Directly use Superpowers

Rejected because it carries global invocation strictness and worktree/subagent assumptions that do not match this repository's desired defaults.

### Directly use Matt Pocock skills

Rejected because issue tracker setup, ADR, and CONTEXT are valuable but too opinionated as defaults.

### Single giant WDL skill

Rejected because it would increase context footprint and mix routing, discovery, planning, implementation, and acceptance into one file.

## Created Files

- `myz-skills/software-delivery-loop/SKILL.md`
- `myz-skills/software-delivery-loop/README.md`
- `myz-skills/software-delivery-loop/references/loop-state.md`
- `myz-skills/software-delivery-loop/references/track-template.md`
- `myz-skills/software-delivery-loop/references/prd-template.md`
- `myz-skills/software-delivery-loop/references/plan-template.md`
- `myz-skills/software-delivery-loop/references/change-note-template.md`
- `myz-skills/software-delivery-loop/references/delivery-record-template.md`
- `myz-skills/software-delivery-loop/references/acceptance-checklist.md`
- `myz-skills/requirement-discovery/SKILL.md`
- `myz-skills/solution-design/SKILL.md`
- `myz-skills/implementation-execution/SKILL.md`
- `myz-skills/delivery-acceptance/SKILL.md`

## Deprecated Files

- `myz-skills/workspace-delivery-loop/SKILL.md` marked Legacy / Deprecated and pointed to `software-delivery-loop`.

## Open Questions

- Whether simple bugfix path should be `docs/track/bugfix/` or `docs/track/bugfixes/`.
- Whether a future runnable script should generate track folder skeletons from templates.
- Whether eval prompts should be added for skill-trigger testing after user review.

## Change Log

- 2026-07-03: Initial software-delivery-loop skill family drafted from historical WDL, tracks, Superpowers, Tashan, Matt Pocock skills, cross-feature knowledge/logging, and loop-engineering references.

## Review Iteration 2026-07-03

User feedback applied:

1. Moved templates from `software-delivery-loop/references` to the relevant phase skills:
   - PRD and requirement syntax → `requirement-discovery/references/`
   - solution design and plan templates → `solution-design/references/`
   - implementation checklist → `implementation-execution/references/`
   - delivery record and acceptance checklist → `delivery-acceptance/references/`
   - shared track, change-note, loop-state, cold-start remain under `software-delivery-loop/references/`.
2. Renamed phase skills:
   - `product-discovery` → `requirement-discovery`
   - `product-planning` → `solution-design`
   - `product-implementation` → `implementation-execution`
   - `product-acceptance` → `delivery-acceptance`
3. Added lightweight cross-skill `Related skills` sections.
4. Enhanced requirement discovery with Elevator Pitch, Persona, Business/Value Canvas, User Journey, User Story Map, User Story format, EARS, and Given/When/Then.
5. Enhanced solution design with design principles, alternatives, trade-offs, contracts, testing seams, and E2E strategy.
6. Enhanced implementation execution with TDD, E2E/integration-driven verification, refactor-after-green, maker/checker review, and an implementation checklist.
7. Added loop self-improvement protocol: detect recurring failure → summarize history → propose concrete improvements → ask user → execute after approval. If loop-state permits autonomous safe self-improvement, the loop may apply safe skill/template refinements and record the change.
8. Removed layered documentation references. Replaced with `docs/knowledge` for cross-feature durable knowledge and `docs/logs/YYYY-MM-DD.md` for operational logs.
9. Added cold-start guidance and set workspace-level loop state default path to `.agents/loop-state.md`.

Decision: `.agents/loop-state.md` is workspace-level state, not feature-level state. Feature-specific facts remain in `docs/track/...`; durable cross-feature knowledge goes in `docs/knowledge`; daily operational records go in `docs/logs/YYYY-MM-DD.md`.

## Review Iteration 2026-07-03 — Policy Simplification and Fence Fixes

User feedback applied:

1. Fixed markdown templates that used nested triple-backtick code fences by switching outer template fences to tilde fences where needed.
2. Simplified `.agents/loop-state.md` Workspace Policy to a single option:
   - `Autonomy: ask-first | evidence-backed-autonomy | full-autonomy`
3. Removed separate Self-improvement, Subagents, and Worktrees policy knobs.
4. Clarified that self-improvement is ask-first unless Autonomy is `full-autonomy`; under `full-autonomy`, safe skill/template refinements may be applied and recorded.
5. Kept subagents allowed by default where useful. Worktree decisions are left to the user/environment and are no longer part of loop policy.

## Validation and Trigger Eval Completion — 2026-07-03

Validation report written to:

- `tracks/skill-rebuild/software-delivery-loop-eval-report.md`

Final validation summary:

| Validation | Result |
|---|---:|
| Static structure checks | 47/47 |
| Semantic static coverage | 18/18 |
| Iteration 1 explicit behavior eval, default model, with-skill | 18/18 |
| Iteration 1 baseline | 7/18 |
| Iteration 2 explicit behavior eval, `sensenova/deepseek-v4-flash`, with-skill | 18/18 |
| Iteration 2 baseline | 8/18 |
| Trigger description eval 2 | 18/18 |

Optimization applied after validation:

1. Added right-sized context inspection guidance to avoid over-exploration while preserving inspect-before-ask behavior.
2. Strengthened `software-delivery-loop` description for end-to-end delivery, phase triage, continuation from request to shipment, and existing track/PRD/plan work.
3. Bumped `software-delivery-loop` to version `0.2.2`.
4. Added `myz-skills/software-delivery-loop/evals/trigger-evals.json` with 18 trigger-routing cases.

Operational notes:

- `sensenova/deepseek-v4-flash` hit provider RPM limits under parallel eval; serial execution completed successfully.
- Trigger eval 1 scored 17/18 because T01 routed to `requirement-discovery`; after description optimization, trigger eval 2 scored 18/18.
- Remaining limitation: trigger eval was description-routing simulation, not full runtime implicit skill-loading from an installed skill directory.


## Final Review and Comparative README — 2026-07-03

Final review additions:

1. Expanded `myz-skills/software-delivery-loop/README.md` with a comprehensive comparison against:
   - SDL itself
   - Superpowers
   - Tashan Development Loop
   - Matt Pocock Skills
   - Legacy WDL
2. Added comparison tables covering:
   - best fit / scope
   - strengths
   - costs and limits
   - SDL design choices
   - design dimensions such as trigger style, docs, autonomy, subagents, worktrees, commit/push, and ceremony level
   - when to choose each workflow
3. Found and fixed a final consistency issue: README listed `solution-design-v1.md` in the normal feature track layout while the main SKILL single-project example omitted it.
4. Bumped `software-delivery-loop` to version `0.2.3` for the post-review consistency patch.


## Rename to Software Delivery Loop — 2026-07-03

User clarified that the loop applies beyond product-feature delivery, including bugfixes, refactors, maintenance, internal tools, verification, acceptance, and delivery records. Applied direct rename without keeping a deprecated alias:

- Former product-scoped skill directory → `myz-skills/software-delivery-loop/`
- Former product-scoped skill slug → `software-delivery-loop`
- Former product-scoped title → `Software Delivery Loop`
- README acronym changed to SDL.
- Persistent reports/logs renamed under `tracks/skill-rebuild/software-delivery-loop-*`.
- Old WDL deprecation pointer updated to `software-delivery-loop`.
- Main skill version bumped to `0.3.0`.

Scope wording changed from product-oriented language to software-oriented language:

- `request to shipment` → `request to accepted outcome`
- `product intent/product shape/product scope` → software intent, behavior, scope, or acceptance
- README comparison now describes SDL as software delivery rather than product delivery.

No deprecated alias for the former product-scoped name was kept, per user instruction.

