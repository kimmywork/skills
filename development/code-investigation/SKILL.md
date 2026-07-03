---
name: code-investigation
description: Structured methodology for code-level investigation and analysis tasks. Use when the user needs to understand an unfamiliar codebase, map data models across systems, trace data flows, analyze protocols or message formats, or investigate how a system actually works by reading its source code. Also use when user mentions "investigate", "trace", "analyze code", "reverse engineer", "understand the codebase", "data migration mapping", "schema analysis", or any task that requires deriving truth from source code rather than documentation.
---

# Code Investigation Methodology

A structured approach to understanding systems by reading their source code. Produces traceable, verifiable documentation with explicit confidence levels and known gaps.

**References** (read as needed):
- `references/workflow.md` — Detailed 4-phase process (Discovery → Deep Dive → Documentation → Verification) with step-by-step instructions and anti-patterns
- `references/traps-and-examples.md` — 9 common traps with corrections, worked examples of tracing untyped fields and detecting schema evolution
- `references/templates.md` — Directory structure, document templates, work log format, review templates

---

## Principles

1. **Code is the single source of truth.** Docs/Wiki/comments are leads, not conclusions. Every claim must be verified against actual code.
2. **Follow the data end-to-end.** Trace from producer → serialization → transport → consumer → storage. Never stop at one module.
3. **Verify, don't speculate.** Dynamic/untyped fields must be traced to their actual assignment site. If unverifiable, mark as "inferred."
4. **Multiple perspectives catch blind spots.** Review from PO/PM, QA, SRE, and security angles after completing technical analysis.
5. **Proposals must be executable.** Plans (especially rollback and time estimates) must have validated technical feasibility.

---

## Process Overview

```
Discovery → Deep Dive → Documentation → Verification
    │            │             │               │
    │            │             │               ├─ Self-check (all claims sourced?)
    │            │             │               └─ Multi-perspective review (PO/PM, Arch, SRE, QA)
    │            │             │
    │            │             └─ Structure findings: confirmed vs. inferred, cite sources
    │            │
    │            └─ Trace data end-to-end: producer → serialization → consumer → storage
    │
    └─ Map the landscape: modules, entry points, dependencies, data type inventory
```

For the full step-by-step workflow with detailed instructions and anti-patterns, read `references/workflow.md`.

---

## Quick Mode (< 1 Hour)

For small, focused tasks, skip the full ceremony:

1. **Locate** — find the relevant file(s)
2. **Trace** — follow one level up (producer) and one level down (consumer)
3. **Confirm** — verify against at least one other reference point (a test, a caller, or actual output)
4. **State confidence** — tell the user whether this is confirmed or inferred

No directory structure, no work log, no multi-perspective review needed.

---

## Quality Criteria

A high-quality output is:

- **Traceable** — every conclusion points to a source file
- **Verifiable** — readers can confirm independently
- **Bounded** — confirmed vs. inferred is explicit
- **Gap-aware** — uncovered areas and assumptions listed
- **Internally consistent** — no contradictions across documents
- **Executable** — proposals have validated feasibility
- **Versioned** — corrections visible in work log
- **Multi-dimensional** — covers operability, security, verifiability, not just technical depth
