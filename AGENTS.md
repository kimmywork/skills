# Skill Creation Principles

This repository contains independent, agent-neutral skill bundles. When creating or modifying any agent-facing document, including `AGENTS.md`, instruction or reference files under `.agents/`, any `SKILL.md`, skill references, or prompt templates, read and apply the shared rules in [`utility/skills/agent-facing-doc/references/document-guide.md`](utility/skills/agent-facing-doc/references/document-guide.md). The guide is distributed with the optional `agent-facing-doc` skill; its rules apply throughout this workspace when that skill is installed.

## Definitions

- **Plugin bundle**: one plugin directory (`.claude-plugin/plugin.json` or `.codex-plugin/plugin.json`) and all SKILLs under it. These install together, so cross-referencing within a plugin bundle is allowed.
- **Skill bundle**: one skill directory plus its `references/` and `scripts/`. A skill bundle contains the resources installed with that skill.

## Repository-specific scope

- A skill may reference only content within its plugin bundle. Do not reference skills, files, or features outside bundle scope.
- Before adding in-bundle content, verify that it is not a scope violation, an oversized existing skill, an overlap with another plugin, an unjustified new skill, or a low-value addition.
- After modifying an agent-facing document, run the applicable checks in `utility/skills/agent-facing-doc/references/document-guide.md` and confirm that plugin metadata, inventories, references, and local discovery links remain consistent.
