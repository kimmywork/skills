---
name: agent-facing-doc
description: Create, update, or review agent-facing documentation, including AGENTS.md, instructions and references under .agents/, SKILL.md files, skill references, and prompt templates. Use whenever a task creates or modifies instructions that guide agent behavior, even when the user asks for another task such as documentation alignment or skill maintenance.
---

# Agent-Facing Documents

Read `references/document-guide.md` before creating, modifying, or reviewing an agent-facing document.

## Workflow

1. Identify the documents that guide agent behavior and the change that requires them to change.
2. Inspect applicable repository rules, bundle boundaries, existing instructions, and references before editing.
3. Preserve the document's purpose while making the smallest change that gives agents clear, executable guidance.
4. Keep facts, assumptions, decisions, evidence, instructions, and historical context distinct.
5. When modifying a skill, check its trigger, boundary, output, references, metadata, and repository integration points.
6. Validate the changed documents against the guide. Check language, size limits that apply, references, bundle scope, and any relevant discovery or metadata paths.
7. Report evidence, unresolved conflicts, and checks not performed. Do not claim compliance without the relevant check.

## Output

Adapt human-facing output to the user's language. State the documents reviewed or changed, the rule or evidence supporting each material change, validation results, and unresolved gaps.
