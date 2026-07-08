# Skill Creation Principles

When creating or modifying skills in this workspace, follow these principles.

## Definitions

- **Plugin bundle**: one plugin directory (`.claude-plugin/plugin.json` or `.codex-plugin/plugin.json`) and all SKILLs under it. These install together, so cross-referencing within a plugin bundle is allowed.
- **Skill bundle**: one skill directory plus its `references/` and `scripts/`. Each skill owns its own bundle.

## Design principles

- **Agent first**: Write SKILL.md for agents, not humans. Prefer direct, accurate instructions over rationale. Put detail in `references/`; do not inline it.
- **Agent neutral**: Do not depend on a specific agent, runtime, or harness. Use standard `agentskills.io` structure: YAML frontmatter, Markdown body, optional `references/`.
- **Focused**: Each skill owns one capability with a clear trigger and output. Prefer small skills. Do not let a skill expand past its workflow boundary.
- **Size controlled**: `SKILL.md` must stay within 100 lines. Draft fully if needed, then extract bulk detail into `references/`. Keep references as long as necessary, but avoid duplication.
- **User-centric**: Start from real user scenarios. Do not add ceremony without evidence that it helps.
- **Experience-driven**: Distill from concrete execution, failures, friction, and feedback, not theoretical completeness.

## Independent skill design

- **Description first**: Independent-skill work starts with frontmatter `description`. Describe the direct user task first; do not lead with phase-only language such as before/after/during a framework stage.
- **Semantic, not structural**: Independence is a trigger-and-boundary problem, not a formatting problem. Do not force uniform sections, wording, or output shapes across all skills.
- **Local boundary handling**: Resolve conflicts only where real overlap exists. Do not make every skill depend on a central router or maintain a full neighbor graph.
- **Soft next steps**: When suggesting what comes next, prefer stage names or task types over hard references to skill names or file paths unless explicit linkage is necessary.
- **Natural expansion only**: When making a skill standalone, broaden it only along what users would naturally expect from its name and function. Do not turn leaf skills into mini-orchestrators.
- **Cross-skill review**: When revising a skill or distilling lessons, also check cross-skill overlap, duplication, naming conflict, boundary conflict, and trigger confusion.

## Language rules

- **English**: Write all skill content in English unless project convention says otherwise.
- **Output language**: Agent-facing artifacts stay in English. Human-facing output must match the user's prompt language.

## Structural rules

- **Bundle scope**: A skill may reference only content within its plugin bundle. Do not reference skills, files, or features outside bundle scope. If something is missing, verify all five before adding a new skill: (1) this does not violate scope boundaries, (2) the current skill is not simply too large, (3) the need does not overlap another plugin's skill, (4) the missing content justifies a new in-bundle skill, and (5) it delivers sufficient user value.

## Post-creation checklist

After writing or modifying a `SKILL.md`, verify:

1. **Language**: `rg -n '[一-龥]' SKILL.md` returns nothing — no Chinese characters outside frontmatter.
2. **Size**: `wc -l SKILL.md` returns `<=100`.
3. **Coverage**: If distilled from a source document, compare against the source and confirm nothing critical was lost.
4. **Dedup**: New reference files do not duplicate existing ones. Reference shared rules; do not copy them.
5. **Cross-refs**: Referenced files exist, and links between `SKILL.md` and references remain valid.
6. **Bundle scope**: No references escape the plugin bundle.
7. **Output language**: If the skill produces user-facing output, it includes language-adaptation guidance.
