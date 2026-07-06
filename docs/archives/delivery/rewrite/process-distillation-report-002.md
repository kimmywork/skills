# Process Distillation Summary 002

## Metadata

- **Phase analyzed**: historical track analysis (subagent-assisted)
- **Skills involved**: all SDL phase skills + references
- **Review feedback**: N/A
- **Analysis date**: 2026-07-06
- **Mode**: user-approval

## Summary

- **Gaps found**: 7 (6 new + 1 cross-cutting)
- **Improvements proposed**: 4 (P0-P1), 2 optional (P2), 1 cross-cutting
- **New skills proposed**: 0
- **Pending approval**: 7

## Gaps and improvements

### Gap 1 — Architecture challenge step missing (P0)

**Evidence**: Constype v1 architecture was over-engineered (HFT latency targets, 6 protocols, 4 frontend apps, ScyllaDB/Kafka). The architecture review cut scope to crypto spot MVP, simplified tech stack, adjusted targets. This review was critical but was a one-off — no reusable pattern exists in any SDL phase.

**Proposed change**: Add a "Challenge the design" step to `solution-design/SKILL.md` after the architecture mapping step. Explicitly check: over-engineering, technology sprawl, realistic latency targets, deployment modes, minimal viable scope. This repeats the constype review pattern proactively.

**Target**: `solution-design/SKILL.md` Process section.

### Gap 2 — Deployment modes absent (P0)

**Evidence**: Constype's review added 3 deployment modes (standalone/single-machine/cluster) as a critical artifact. No SDL artifact template asks for deployment modes.

**Proposed change**: Add a "Deployment" section to `solution-design/references/solution-design-template.md`. Cover: development/standalone, demo/single-machine, production/cluster. Not required for all work, but an explicit consideration.

**Target**: `solution-design/references/solution-design-template.md`.

### Gap 3 — Scope reduction pattern missing (P1)

**Evidence**: When constype cut scope, they independently invented 3 documents: ECN (engineering change note), revised-scope, deferred-decisions. No SDL phase has a reusable pattern for tracking what was cut and why.

**Proposed change**: Add a "Scope reduction" section to `software-delivery-loop/references/change-note-template.md`: what was cut, original scope, reason, impact on later phases, deferred decisions. The change note template already exists — just extend it.

**Target**: `software-delivery-loop/references/change-note-template.md`.

### Gap 4 — Discussion records unaddressed (P2)

**Evidence**: CRM project produced 4+ pages of rich interview context: personas, journeys, discussion summaries, value propositions. SDL's `requirement-discovery` has no guidance for preserving raw discussion context — it jumps straight to PRD/track note.

**Proposed change**: Add a note in `requirement-discovery/SKILL.md` Process: "Preserve raw discussion context (personas, scenarios, pain points, user quotes) in a research note under `docs/track/<feature>/research/` before shaping into PRD." This is optional for simple work.

**Target**: `requirement-discovery/SKILL.md` Process section.

### Gap 5 — Quality gates invented twice (P2)

**Evidence**: Mono-services and constype independently created DoD/Doc QA checklists with identical structure (binary pass/fail per item, categories like "scope clear", "verification defined"). The existing `implementation-checklist.md` doesn't have a pre-implementation "readiness gate."

**Proposed change**: Add a "Readiness gate" section to `implementation-checklist.md` before Pre-flight: scope clear, acceptance criteria binary, verification command known, dependencies resolved. This formalizes what both projects independently invented.

**Target**: `implementation-execution/references/implementation-checklist.md`.

### Gap 6 — code-investigation not referenced (P2, false guidance)

**Evidence**: `code-investigation` exists as a standalone skill but no SDL phase references it. `solution-design` says "Read the PRD/track note, docs/knowledge, relevant logs, code, and tests" but doesn't suggest using `code-investigation` for structured code analysis before design.

**Proposed change**: Add a line to `solution-design/SKILL.md` Process step 1: "Use `code-investigation` when the codebase is unfamiliar or the design depends on understanding existing code structure."

**Target**: `solution-design/SKILL.md` Process section.

### Cross-cutting — PRD template too heavy (context overhead)

**Evidence**: No historical project used 6 of 14 PRD template sections (Business Canvas, User Journey, User Story Map, Metadata table, Constraints table, Open Questions table). The full template is appropriate for broad work but the agent has no guidance on when to use which sections.

**Proposed change**: Add a "Section selection guide" to `requirement-discovery/references/prd-template.md`: P0 sections always required, P1 optional for broad work, P2 only for complex multi-stakeholder work. This prevents the agent from generating a 14-section PRD for a 2-day feature.

**Target**: `requirement-discovery/references/prd-template.md`.

## Cross-cutting observations

- All gaps are addressable with small changes to existing skills. No new skill needed.
- Gaps 1-3 address the constype architecture review pattern — the most valuable process improvement observed across all tracks.
- Gap 6 (`code-investigation` referencing) is the simplest fix and has the lowest risk.
- The PRD template heaviness (cross-cutting) is a recurring theme — the template is good but needs a "what to use when" guide.