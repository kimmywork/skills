---
name: blueprinting
description: Turn a complete scope into an executable blueprint: architecture, methodology, outline, review protocol, increments, contracts, and verification mapping. Use before Build when choices, sequencing, interfaces, or validation are non-trivial.
---

# Blueprinting

Design the path before execution.

## Load

- `references/blueprint-templates.md`
- `references/dependency-and-contracts.md`
- `../drafting-loop/references/mode-spectrum.md`
- `../drafting-loop/references/iron-rules.md`

## Preconditions

A Shape artifact exists or the user has supplied equivalent scope. If not, use `../scope-shaping/SKILL.md` first.

## Workflow

1. Restate scope and acceptance criteria.
2. Identify design decisions, contracts, dependencies, and constraints.
3. Pre-screen feasibility: Feasible, Moderate, or Redesigned.
4. Propose the smallest viable approach.
5. Challenge over-engineering, dependency sprawl, unverifiable steps, and scope drift.
6. Record chosen, rejected, and deferred alternatives.
7. Slice into independently verifiable increments and draw dependencies.
8. Map each increment to acceptance criteria and checks.
9. Ask for MANDATORY user approval when blueprint affects scope, architecture, methodology, or cost.

## Kind-specific blueprint

- Crafting: architecture, interfaces, data/contracts, migration, tests.
- Composing: document architecture, evidence map, section flow.
- Evaluating: review protocol only; no full design unless criteria are complex.
- Investigating: methodology only when formal; otherwise fast-pass.
- Creating: concept direction only when useful; avoid over-structuring.

## Output

Blueprint sections: Scope source, Design principles, Chosen approach, Alternatives, Structure, Dependency graph, Verification map, Risks, Decisions needed.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
