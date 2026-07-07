# Skill Creation Principles

When creating or modifying skills in this workspace, follow these principles.

## Definitions

- **Plugin bundle**: one plugin directory (`.claude-plugin/plugin.json` or `.codex-plugin/plugin.json`) and all SKILLs under it. These install together, so cross-referencing within a plugin bundle is allowed.
- **Skill bundle**: one skill's directory + `references/` + `scripts/`. Each skill owns its own bundle.

## Design principles

- **Agent first**: SKILL.md is for agents, not human documentation. Agents are smarter than humans. Agents need simple, direct, accurate, unambiguous instructions — not verbose rationale. Give precise commands over explanations. If an agent needs details, point to `references/`; don't inline them.
- **Agent neutral**: No dependency on any specific agent implementation, subagent runtime, or harness. Use standard `agentskills.io` format (YAML frontmatter + Markdown body + optional `references/` directory).
- **Focused**: Each skill owns one capability with a clear triggering signal and well-defined output. Prefer many small, focused skills over one monolithic skill. Don't let a skill grow beyond its defined workflow boundary.
- **Size controlled**: SKILL.md must not exceed 100 lines. Extract bulk reference material into `references/`. Compress without losing semantics — condense, don't delete. This 100-line limit is a hard final constraint for `SKILL.md` only, not a drafting constraint and not a reference-file limit: when creating or substantially revising a skill, first draft the complete instruction set if needed, then extract, factor, and condense it into a ≤100-line SKILL.md plus supporting references. Reference files have no 100-line cap; keep them as long as needed to preserve full semantics, while avoiding duplication.
- **User-centric**: Start from user scenarios, personas, and real needs. Don't add ceremony without demonstrated value. Base improvements on actual execution evidence.
- **Experience-driven**: Working experience over comprehensive knowledge. Skills are distilled from concrete project execution, not from theoretical completeness. Every rule in a skill should trace back to a real failure or friction point.

## Language rules

- **English**: Write all skill content in English unless project convention specifies otherwise.
- **Output language**: Agent-facing artifacts (tracks, references, skill bodies) stay in English. Human-facing output (explanations, analysis, reports) must match the user's prompt language.

## Structural rules

- **Bundle scope**: SKILLs may only cross-reference content within the same plugin bundle. No references to skills, files, or features outside the plugin bundle scope. If a dependency is missing, verify: (1) does this violate scope boundaries? (2) is the skill too large? (3) does it overlap with another plugin's skill? (4) does the needed content warrant a new in-bundle skill? (5) does it deliver sufficient user value? Only add a new skill if all five checks pass.

## Post-Creation Checklist

After writing or modifying a SKILL.md, verify:

1. **Language**: `grep -Pn '[\x{4e00}-\x{9fff}]' SKILL.md` returns nothing — no Chinese characters outside frontmatter.
2. **Size**: `wc -l SKILL.md` returns ≤100.
3. **Coverage**: If distilled from a source document, diff the new skill's sections against the original to confirm nothing critical was lost.
4. **Dedup**: Check that new reference files don't duplicate existing ones. If a template or rule exists in one file, reference it — don't copy.
5. **Cross-refs**: Ensure referenced files actually exist. Verify bidirectional links (SKILL.md → references, references → each other).
6. **Bundle scope**: No references to skills, files, or features outside the plugin bundle.
7. **Output language**: If the skill produces user-facing output, verify it includes language adaptation guidance.
