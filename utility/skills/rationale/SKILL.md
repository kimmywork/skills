---
name: rationale
description: "Explain any context-dependent content for human comprehension: SKILL.md rules, AGENTS.md principles, code changes, project concepts, design decisions, or agent outputs. Use when a human needs to understand WHY something exists, HOW it works, or WHAT a decision's trade-offs are. Trigger on 'explain', 'rationale', 'why', 'how does X work', 'what's the reasoning', or when reviewing dense agent-optimized artifacts."
license: MIT
metadata:
  author: kenpusney
  version: "0.1.0"
---

# Rationale

Decode agent-optimized artifacts into human-comprehensible explanations. Agents write for agents; this skill translates for humans.

## Intent detection

Read the user's phrasing to determine depth:

| Signal | Mode | Output scope |
|---|---|---|
| "what is X", "what does this do" | Brief | 1-2 paragraphs: identity + purpose |
| "explain X", "how does X work" | Standard | Structured sections (see template) |
| "rationale for X", "why", "analyze", "justify" | Deep | Standard + evidence + alternatives + change history |

Adapt to user's language: **match the user's language** — Chinese prompt → Chinese output, English prompt → English output. Keep code identifiers, file paths, skill names, and technical terms in their original form. Also match density: terse prompt → concise output; detailed prompt → more elaboration.

## Output structure

Standard and deep modes use this skeleton:

### What this is
One sentence: identity, scope, boundary.

### Why it exists
The problem or context that motivated it. Ground in concrete facts (file refs, git history, user requirements).

### How it works
Core mechanics. One subsection per logical unit. Each section states one core point.

### Key decisions and trade-offs
What was chosen, what was rejected, why. Cite evidence (code, commits, specs).

### Connections
Relation to surrounding context: other skills, dependent rules, affected files.

Skip sections that don't apply — don't fill with filler. Brief mode: compress to "What" + "Why" only.

## Exploration protocol

1. **Workspace first**: Read relevant files, git log, project structure. This is primary evidence.
2. **References**: If the subject references external things (libraries, standards), fetch those docs.
3. **External on demand**: Web search only when explanation requires context absent from workspace. Max 3 fetches per session. Always cite sources.

Never explore speculatively. Every fetch must serve the user's question.

## Termination

Stop when any fires:
- **Question answered**: Core question addressed; no new ground to cover.
- **Diminishing returns**: Further exploration yields mostly redundant or peripheral information.
- **Depth cap**: 3 levels of "why" recursion reached.

Summarize unexplored related areas and offer to continue on request.

## Document mode

When user asks for a formal rationale artifact (not inline explanation), produce a standalone document. Trigger examples: "generate a rationale doc for X" → document mode; "explain X" → inline mode.

```
# Rationale: [Subject]
## Context
## Decision
## Alternatives considered
## Evidence
## Trade-offs
## Related
```

Save to the location the user specifies, or `docs/rationale/` by default.
