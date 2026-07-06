# Skill Creation Principles

When creating or modifying skills in this workspace, follow these principles:

- **Agent first**: SKILL.md is for agents, not human documentation. Agents are smarter than humans. Agents need simple, direct, accurate, unambiguous instructions — not verbose rationale. Give precise commands over explanations. If an agent needs details, point to `references/`; don't inline them.
- **Agent neutral**: No dependency on any specific agent implementation, subagent runtime, or harness. Use standard `agentskills.io` format (YAML frontmatter + Markdown body + optional `references/` directory).
- **Size controlled**: SKILL.md must not exceed 100 lines. Extract bulk reference material into `references/`. Compress without losing semantics — condense, don't delete.
- **Scope limited**: Each skill owns one capability. Don't let a skill grow beyond its defined workflow boundary.
- **Atomic**: Prefer many small, focused skills over one monolithic skill. Each skill should have a clear triggering signal and produce a well-defined output.
- **User-centric**: Start from user scenarios, personas, and real needs. Don't add ceremony without demonstrated value. Base improvements on actual execution evidence.
- **Experience-driven**: Working experience over comprehensive knowledge. Skills are distilled from concrete project execution, not from theoretical completeness. Every rule in a skill should trace back to a real failure or friction point.
- **English**: Write all skill content in English unless project convention specifies otherwise.

## Post-Creation Checklist

After writing or modifying a SKILL.md, verify:

1. **Language**: `grep -Pn '[\x{4e00}-\x{9fff}]' SKILL.md` returns nothing — no Chinese characters outside frontmatter.
2. **Size**: `wc -l SKILL.md` returns ≤100.
3. **Coverage**: If distilled from a source document, diff the new skill's sections against the original to confirm nothing critical was lost.
4. **Dedup**: Check that new reference files don't duplicate existing ones. If a template or rule exists in one file, reference it — don't copy.
5. **Cross-refs**: Ensure referenced files actually exist. Verify bidirectional links (SKILL.md → references, references → each other).