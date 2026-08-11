# Utility

A bundle of lightweight, agent-neutral utility skills for daily work with documents, agent-facing instructions, explanations, and writing style.

## Skill inventory

| Skill | Purpose |
|---|---|
| `agent-facing-doc` | Create, update, or review agent-facing documentation including AGENTS.md, SKILL.md files, and prompt templates. |
| `cloudconvert` | Convert approved non-text documents to Markdown through the external CloudConvert service. |
| `rationale` | Explain agent-optimized artifacts, code changes, concepts, and design decisions for human comprehension. |
| `style-calibration` | Extract, validate, compare, and apply a writing style profile from samples. |

## Design

- **Agent-neutral:** no dependency on a particular agent, runtime, or tool.
- **Lightweight:** minimal SKILL.md with references only when detail is needed.
- **Focused:** each skill has a distinct trigger and bounded outcome.
