---
name: rationale
description: Explain context-dependent artifacts, concepts, code changes, rules, or design decisions for human understanding. Use when explanation, reasoning, mechanics, or trade-offs are the primary deliverable; do not use it as a correctness review, readiness verdict, or broad evidence investigation.
---

# Rationale

Explain what something is, why it exists, how it works, and which trade-offs shaped it.

## Approach

1. Identify the specific subject and what the user is trying to understand.
2. Inspect the relevant artifact, surrounding files, and available history before explaining context-dependent details.
3. Separate documented facts, evidence-backed interpretation, and unresolved uncertainty.
4. Explain the purpose and mechanics before secondary detail.
5. Include alternatives and trade-offs only when they clarify a decision.
6. Match the user's language, familiarity, and requested depth while preserving identifiers and technical terms.
7. Stop when the question is answered; offer adjacent detail instead of adding it automatically.

Use external sources only when the explanation depends on context absent from the workspace, and cite the sources used.

## Output

Adapt the structure rather than filling a fixed template. A substantial explanation may include:

- what it is and its boundary;
- why it exists;
- how it works;
- key decisions and trade-offs;
- evidence and relevant connections.

For a brief question, answer directly. Create a standalone rationale file only when the user asks for an artifact; use their requested location or confirm a suitable path before writing.
