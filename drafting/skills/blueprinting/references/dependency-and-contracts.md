# Dependency and Contract Planning

## Feasibility pre-screen

Classify major design choices:

| Rating | Meaning | Action |
|---|---|---|
| Feasible | fits scope and constraints | continue |
| Moderate | risk exists but manageable | add mitigation |
| Redesigned | constraints or scope cannot hold | return to Shape |

## Contract-first planning

Use for boundary changes: APIs, schemas, interfaces, data models, document structures, review criteria.

1. Name inputs, outputs, invariants, and consumers.
2. Inventory dependents before changing existing contracts.
3. Choose break-fix, deprecate-remove, adapter, or no-change.
4. Map contract checks to increments.

## Dependency graph

For each increment, record:
- predecessors
- artifacts changed
- verification method
- rollback path

Start with least-dependent increments unless risk requires a spike first.
