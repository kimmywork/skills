# Skill Creation Principles

When creating or modifying skills in this workspace, follow these principles:

- **Agent neutral**: No dependency on any specific agent implementation, subagent runtime, or harness. Use standard `agentskills.io` format (YAML frontmatter + Markdown body + optional `references/` directory).
- **Size controlled**: SKILL.md under 500 lines. Extract bulk reference material into `references/`. Prefer concise instructions over verbose rationale — the SKILL.md is for the agent, not human documentation.
- **Scope limited**: Each skill owns one capability. Don't let a skill grow beyond its defined workflow boundary.
- **Atomic**: Prefer many small, focused skills over one monolithic skill. Each skill should have a clear triggering signal and produce a well-defined output.
- **User-centric**: Start from user scenarios, personas, and real needs. Don't add ceremony without demonstrated value. Base improvements on actual execution evidence.
- **English**: Write all skill content in English unless project convention specifies otherwise.