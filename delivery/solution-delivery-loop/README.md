# Solution Delivery Loop

A compact, agent-neutral skill family for solution delivery. Inspired by [Addy Osmani's Loop Engineering](https://addyosmani.com/blog/loop-engineering/) — the five primitives (automations, worktrees, skills, connectors, sub-agents) plus state. SDL focuses on the **skills** and **state** primitives while staying agent-neutral and independent of any specific tool or runtime.

```text
Sense → Shape → Design → Build → Verify → Record → Continue/Stop
```

It can run manually, collaboratively, or autonomously when enough evidence exists.

## Install

```bash
npx skills add kimmywork/skills --skill solution-delivery-loop requirement-discovery solution-design implementation-execution delivery-acceptance review-feedback process-distillation structured-investigation
```

## Skill family

- `solution-delivery-loop` — entry point and router. Routes to the correct phase, manages the review-feedback loop, and triggers process distillation.
- `requirement-discovery` — users, scenarios, scope, non-goals, requirements, acceptance. Preserves research raw material under `docs/track/<feature>/research/`.
- `solution-design` — principles, alternatives, deliverable structure, interfaces/contracts, verification strategy, plan. Includes a mandatory "challenge the design" step.
- `implementation-execution` — produces verifiable increments. Generic execution loop; software mode supports TDD-driven slice execution. Concrete change-control signals guard against undocumented drift.
- `delivery-acceptance` — evidence-based review, verification, delivery decision. Supports both full and lightweight delivery records.
- `review-feedback` — independent reviewer invoked after each phase.
- `process-distillation` — after each review-feedback cycle, optionally analyzes the completed phase for skill improvements.
- `structured-investigation` — universal investigation methodology for any domain (code, systems, data, research, analysis).

## Loop Engineering alignment

[Loop Engineering](https://addyosmani.com/blog/loop-engineering/) defines five primitives for autonomous agent loops: automations, worktrees, skills, connectors, and sub-agents, plus state. SDL implements the **skills**, **sub-agents**, and **state** primitives while leaving automations, worktrees, and connectors to the agent runtime.

SDL extends Loop Engineering with two capabilities it does not describe:

- **Cumulative review**: `review-feedback` inspects the full chain of artifacts from the start, not just the current output. The later the review happens, the more artifacts are inspected and the farther issues may need to roll back. This is a stronger version of the maker/checker split.
- **Self-improving skills**: `process-distillation` analyzes completed phase cycles and updates the skill instructions themselves. Loop Engineering says "you design it one time." SDL says "you design it, and then it designs itself better."

## Review and self-improvement loop

After each phase produces its output, `review-feedback` inspects it cumulatively with all prior artifacts. Issues are tagged by origin phase, severity, and type. Resolution:

- **Fix in place**: correct issues in the current phase output, re-review.
- **Roll back**: return to the earliest affected phase, correct the artifact there, re-execute forward.

After review-feedback resolves, `process-distillation` may optionally analyze the cycle for skill improvements. Under `full-autonomy`, this triggers automatically.

| Review at | Inspects | Rollback to |
|---|---|---|
| solution-design | Requirements + design | requirement-discovery |
| implementation-execution | Requirements + design + implementation | requirement-discovery |
| delivery-acceptance | all prior + delivery record | requirement-discovery |

## Track document layout

Normal feature:

```text
docs/track/<feature-name>/
  requirements-v1.md
  solution-design-v1.md
  plan-v1.md
  delivery-record-v1.md
  changes/change-note-0001.md
  research/            # raw material from requirement-discovery
```

Multi-project work:

```text
docs/track/<project-name>/<feature-name>/...
```

Simple work:

```text
docs/track/features/<feature-name>.md
docs/track/bugfix/<bug-description>.md
```

Workspace-level loop continuity:

```text
.agents/loop-state.md
```

## Cross-feature knowledge and logs

Use `docs/knowledge` for cross-feature durable knowledge:

```text
docs/knowledge/adr/
docs/knowledge/architecture/
docs/knowledge/domain/
docs/knowledge/contracts/
docs/knowledge/decisions/
```

Use `docs/logs/YYYY-MM-DD.md` for operational work logs.

Docs can become stale. When docs, code, tests, and runtime behavior disagree, verify against source-of-truth artifacts and update the inaccurate docs.

## Automation stance

Autonomous work is allowed when user input is not needed: obvious bugfixes, planned slices, dependency hygiene, test repairs, documentation sync, and maintenance. Autonomy stops when intent, trade-offs, risk, scope, or acceptance requires human judgment.

`.agents/loop-state.md` can set the workspace Autonomy policy. Safe skill/template self-improvement is ask-first unless Autonomy is `full-autonomy`.

**Risk awareness**: Autonomous execution accelerates delivery but creates comprehension debt — the faster the loop ships code you did not write, the less you understand the codebase. Review the loop's output with the same rigor you apply to human contributions. The "cognitive surrender" trap — accepting whatever the loop produces because it's easier than forming an opinion — is the real cost of automation, not the token bill.

## Comparison and design trade-offs

SDL is not intended to replace every engineering workflow. It is a compact, agent-neutral delivery loop for solution work: shaping a request, designing a solution, producing verifiable increments, and recording delivery evidence.

### Framework comparison

| Framework | Best fit / scope | Strengths | Costs and limits | SDL design choice |
|---|---|---|---|---|
| **Solution Delivery Loop (SDL)** | Solution work from request to accepted outcome: requirements, design, implementation, verification, acceptance, delivery records, and continuing track work. | Small phase skills; explicit router; cumulative review; self-improving skills; feature-scoped track docs; evidence-based acceptance; supports autonomous work; no required issue tracker or worktrees; clear cold-start path. | Less prescriptive than strict TDD-only loops; does not itself install project infrastructure; trigger behavior still depends on skill discovery; not a general productivity suite; human judgment still required for unclear intent/risk/acceptance. | Optimize for minimum durable ceremony: enough structure to prevent drift, but not a process platform. Use SDL as the delivery spine and call specialized skills/tools when needed. |
| **Loop Engineering** | Autonomous agent loop design: five primitives (automations, worktrees, skills, connectors, sub-agents) plus state. | Clear conceptual model; covers the full loop lifecycle; addresses comprehension debt and cognitive surrender; product-agnostic between Codex and Claude Code. | Assumes a runtime that supports automations, worktrees, and MCP connectors; does not prescribe phase structure or delivery artifacts; does not address self-improving instructions. | Borrow the maker/checker split, state-as-spine, and risk awareness. SDL adds phase structure, cumulative review, and self-improving skills. |
| **Superpowers** | General agent discipline across conversations: skill invocation, brainstorming, systematic debugging, TDD, verification, planning, code review, branch finishing. | Strong anti-rationalization rules; excellent for enforcing process before action; good coverage of debugging, TDD, reviews, plans, verification, and branch hygiene; works as a broad operating system for agent behavior. | Heavy global invocation discipline; can feel strict for small tasks; process skills may dominate software-delivery context; includes workflow assumptions such as mandatory skill checks and review checkpoints that are broader than SDL. | Borrow the discipline of evidence, TDD, verification, review, and anti-rationalization, but avoid making every SDL action depend on a global superpower protocol. SDL is narrower and software-delivery-specific. |
| **Tashan Development Loop** | High-pressure implementation work where the risk is skipping analysis, design, planning, tests, verification, commit, or push. | Very strong engineering discipline; explicit Analysis → Design → Plan → TDD → red/green evidence → review → ship; resists time/scope/sunk-cost pressure; excellent for repo-local implementation rigor. | Intentionally strict; mandates `commit`/`push` after each engineering plan; plan tasks can be very granular; less discovery-oriented; repo-specific Chinese workflow tone; heavier than desired for lightweight shaping or acceptance-only tasks. | Borrow red/green evidence, small slices, and pressure resistance, but remove mandatory commit/push and repo-specific ceremony. SDL stops at delivery evidence unless user/project convention says to commit, push, merge, or release. |
| **Matt Pocock Skills** | Real engineering workflows around issue trackers, PRDs, grilling, domain modeling, deep modules, TDD, code review, research, prototypes, and architecture improvement. | Excellent modular engineering skills; strong domain-language focus via `CONTEXT.md`; issue tracker integration; high-quality PRD, TDD, code-review, codebase-design, and architecture-improvement practices; good separation between user-invoked orchestration and model-invoked discipline. | Assumes setup and conventions such as issue tracker configuration, triage labels, `CONTEXT.md`, ADRs, and slash-command flows; PRD and issue workflows can be heavier than needed; less focused on a single minimal delivery record loop. | Borrow PRD quality, domain language, seam/test thinking, deep-module design, and two-axis review. Do not require issue trackers, triage labels, `CONTEXT.md`, or ADRs by default; use `docs/knowledge` and track notes as lighter durable memory. |

### Design dimension matrix

| Dimension | SDL | Loop Engineering | Superpowers | Tashan | Matt Pocock Skills |
|---|---|---|---|---|---|
| Primary unit | Feature/bugfix delivery track | Autonomous agent loop | Agent behavior discipline / task workflow | Engineering implementation plan | Issue/PRD/skill workflow |
| Scope | Solution delivery only (code, reports, investigations, plans, documentation) | Agent loop design | Broad agent process | Non-trivial repo implementation | Engineering + productivity suite |
| Trigger style | Model-invoked phase skills | Scheduled + goal-driven | Mandatory skill invocation when relevant | Model-invoked discipline loop | Mix of slash/user-invoked and model-invoked skills |
| Requirements shaping | `requirement-discovery`; compact note or PRD by scope | Triaged by automation | Brainstorming/planning skills | Analysis phase, success criteria | Grilling, to-PRD, domain modeling |
| Solution design | `solution-design`; alternatives, contracts, slices, verification, challenge step | Implicit in sub-agent work | Planning/design via separate skills | Explicit design with 2–3 options | Codebase design, seams, PRD decisions |
| Implementation | `implementation-execution`; one verified vertical slice | Sub-agent maker | TDD/executing-plans/subagent-driven development | Strict TDD red → green → refactor | `/implement` + `/tdd` at agreed seams |
| Review | `review-feedback` (cumulative, independent) | Maker/checker split | Verification and code review skills | Red/green evidence and review | Two-axis code review: Standards + Spec |
| Acceptance | `delivery-acceptance`; Spec Fit + Format Fit + delivery record | Verification via sub-agent | Verification and code review skills | Red/green evidence and review | Two-axis code review: Standards + Spec |
| Self-improvement | `process-distillation` (built-in) | Not addressed | Not addressed | Not addressed | Not addressed |
| Documentation | Feature track docs, `docs/knowledge`, `docs/logs`, research/ | State file (markdown) | Plans, reviews, branch records as needed | `docs/plans/...` plus review notes | Issue tracker, PRDs, `CONTEXT.md`, ADRs |
| Autonomy | Evidence-backed; `.agents/loop-state.md` may set policy | Scheduled + goal-driven autonomy | Depends on skill; often strict checkpoints | Strict loop; commit/push required after accepted plan | Often orchestrated through user-invoked commands and issue tracker state |
| Subagents | Recommended when valuable; not required | Core primitive (maker/checker) | Strongly used in some workflows | Not central | Used for review/research/design comparisons |
| Worktrees | User/environment decision; no policy | Core primitive | Available in related skills | Not central | Not central |
| Commit/push | Not required unless user/project convention allows | Not specified | Branch finishing skill can guide | Mandatory after accepted engineering plan | `/implement` commits current branch |
| Ceremony level | Low to medium, scaled by task | Medium (requires runtime) | Medium to high depending skill | High by design | Medium to high, especially with issue tracker setup |

### SDL trade-offs

- **Agent-neutral over platform-specific**: SDL avoids depending on slash commands, issue trackers, worktrees, or one harness. This makes it portable, but less automated out of the box. Loop Engineering's automations, worktrees, and connectors are valuable but require a specific runtime — SDL deliberately leaves these to the agent system.
- **Track notes over mandatory issues**: SDL uses `docs/track/...` so the delivery record lives with the repo. Teams that already rely on GitHub/Linear can still mirror track docs into issues.
- **Evidence over confidence**: SDL requires verification evidence before delivery claims, but leaves exact commands to the repo and phase docs.
- **Small skills over monolith**: Phase skills reduce context and improve routing, but require the top-level skill to choose the right next phase.
- **Cumulative review over single-pass check**: `review-feedback` inspects the full chain of artifacts from the start. This catches issues that a single-phase check would miss, but review cost increases with each phase. The trade-off is explicit: catch issues early or pay the rollback cost later.
- **Self-improving instructions over static design**: `process-distillation` updates the skill instructions based on real execution evidence. Loop Engineering says "you design it one time." SDL says the design improves as the loop runs.
- **Autonomy with stop conditions**: SDL allows autonomous work when evidence is sufficient, but stops on unclear scope, acceptance, contracts, architecture, or risk.
- **Durable knowledge without mandatory ADRs**: `docs/knowledge` can hold ADRs, architecture notes, domain terms, contracts, and decisions, but SDL does not require ADRs or `CONTEXT.md` for every change.
- **Review semantics, not review bureaucracy**: SDL keeps Spec Fit and Format Fit because they prevent common failures; it does not require parallel reviewers, issue labels, or branch workflows unless valuable.
- **Right-sized inspection**: SDL reads existing context before asking the user, but now explicitly stops searching once more context is unlikely to change the next action.

### When to choose which

| Situation | Recommended default |
|---|---|
| End-to-end solution request (software, report, investigation, plan), unclear phase, or continuing track work | SDL |
| Designing an autonomous agent loop with scheduled discovery and triage | Loop Engineering (use SDL for the skill/state layer) |
| Need strict agent discipline before any action in a broad session | Superpowers |
| High-pressure implementation where skipping TDD/verification/commit is the main risk | Tashan |
| Repo already uses issue trackers, PRD-to-issues flow, domain glossary, ADRs, and slash-command orchestration | Matt Pocock Skills |
| Pure bug diagnosis, TDD mechanics, branch finishing, or code review outside a delivery loop | Use the specialized skill directly; SDL can reference its result if delivery records matter |