# Agent-Facing Document Guide

This guide applies when creating, modifying, or reviewing any document that guides agent behavior. This includes `AGENTS.md`, instruction and reference files under `.agents/`, `SKILL.md`, skill references, prompt templates, and instructions distributed with a skill. File location does not limit the guide's scope.

## Principles

- **Agent first**: Write for agents. Prefer direct, accurate, executable instructions over rationale. State scope, trigger, required action, output, and prohibition whenever they matter.
- **Agent neutral**: Do not depend on a particular agent, runtime, harness, or tool unless that dependency is the capability being provided. Skill bundles use the standard `agentskills.io` structure: YAML frontmatter, Markdown body, and optional bundled resources.
- **Self-describing names**: Name files so their purpose is clear from the name alone. Agents discover and select resources by path and filename; a descriptive name reduces lookup cost and prevents misuse. Prefer `workflow-format.md` over `reference-1.md`, `clarification-checklist.md` over `questions.md`.
- **Proportionate**: Keep every agent-facing document as short as its role permits. The `<=100` line limit applies specifically to `SKILL.md`; move skill detail to references instead of expanding its main body.
- **Focused**: Give each document one purpose implied by its name and role. A skill has one capability with a distinct trigger, boundary, and output. A reference covers one topic. A checklist addresses one workflow phase. Do not turn a leaf skill into an orchestrator or require a fixed workflow when the task does not need one.
- **Experience-driven**: Add constraints when execution evidence, failures, friction, or user feedback shows that they prevent recurring problems. Avoid ceremony added only for theoretical completeness.
- **Collective ownership**: Treat project knowledge, skills, and documentation as collectively maintained artifacts. Preserve provenance and version history for traceability; do not assign personal ownership or use documentation as a blame mechanism.

## Skill rules

- Put the direct user task and trigger conditions first in frontmatter `description`; do not lead with phase-only language.
- Keep `SKILL.md` at `<=100` lines. References may be longer when their detail is needed, but must remain focused and must not duplicate their main skill or this guide.
- Keep references, scripts, and assets inside the plugin bundle. Use relative paths and verify every referenced path exists.
- State facts, assumptions, preferences, decisions, unknowns, and evidence distinctly when the task depends on them.
- Make output language explicit: agent-facing artifacts remain in English unless project convention says otherwise; human-facing output follows the user's language.
- When a skill changes files, state the observable result and the check that supports completion. Do not claim completion without that evidence.

## Maintenance checks

When creating or modifying an agent-facing document:

1. Confirm the document's purpose, scope, trigger, action, output, and prohibitions remain explicit where relevant.
2. Confirm agent-facing instructions remain in English unless project convention explicitly differs.
3. For each modified `SKILL.md`, run `rg -n '[一-龥]' SKILL.md` and `wc -l SKILL.md`; confirm no Chinese characters occur outside permitted conventions and the result is `<=100`.
4. If guidance was distilled from a source, compare it with that source and confirm no critical behavior was lost.
5. Check for duplicated guidance, valid cross-references, and references that stay within bundle scope.
6. When a skill changes, validate relevant plugin metadata, README inventories, and repository discovery links.
7. Record unavailable checks, unresolved conflicts, and the evidence supporting completion.
