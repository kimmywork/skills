# Investigation Workflow

Detailed step-by-step process for each phase. Read this when executing a full investigation.

---

## Phase 1: Discovery

Build a high-level map before diving into details.

1. Survey project structure — module boundaries, dependencies, layering
2. Read build configs for module relationships
3. Identify entry points (APIs, consumers, schedulers, main functions)
4. Sketch module dependency graph and data flow diagram
5. Scan data definition directories for a full type/schema inventory

**Avoid:**
- Concluding from early schema scripts (evolution may have changed them)
- Treating docs as ground truth without code verification
- Writing final conclusions before establishing the full landscape
- Analyzing only one module of a multi-module system

---

## Phase 2: Deep Dive

Precisely understand fields, types, transformations, and storage behavior.

1. **Start from data definitions** — type definitions, structs, schema files, interface definitions
2. **Chase untyped/dynamic fields** — trace generics and `any` types to their actual assignment site
3. **Trace every pipeline hop:**
   - Producer: who creates it, with what values?
   - Serialization: what framework, what field-name rules?
   - Consumer: who reads it, what type does it become?
4. **Capture precision details** — numeric scale/offset, date timezone/format, enum domains, array serialization
5. **Note what's NOT stored** — transient fields, skipped values, in-memory-only state
6. **Cover ALL data types** — edge cases and extensions are where omissions happen most

**Avoid:**
- Only reading consumer side without checking the producer
- Using creation scripts as current state (ignoring incremental evolution)
- Assuming field names equal semantics without checking annotations and mapping rules
- Ignoring non-persisted data that may matter for cross-system analysis
- Focusing only on happy-path and common data types

---

## Phase 3: Documentation

Convert findings into structured, verifiable documents.

- Organize top-down: overview → detail (readers drill in as needed)
- Cite source files for every conclusion (module + filename minimum)
- Mark each finding: **Confirmed** / **Inferred** / **Assumed** / **Unknown**
- Document edge cases: invalid markers, truncation, null handling, overflow
- Call out unobservable parts: binary deps without source, external services

For directory structure and document templates, see `references/templates.md`.

---

## Phase 4: Verification

**Self-check before delivering:**
- Every claim has a code-backed source reference
- Dynamic-typed fields traced to runtime types
- All pipeline hops inspected (including caches, queues, middleware)
- Full data type inventory covered (not just main flow)
- Enum domains complete with boundary/invalid handling
- Timestamps have verified timezone assumptions
- Numeric precision differences noted
- Pseudocode naming matches actual code exactly
- Cross-document references are consistent
- Proposed plans have validated technical feasibility

**Multi-perspective review** (for important deliverables):

| Perspective | Focus |
|-------------|-------|
| PO/PM (Product Owner / Project Manager) | MECE coverage, timeline realism, stakeholder alignment, external dependencies |
| Architecture/Design | Correctness, consistency guarantees, performance, security/compliance |
| Development/SRE | Feasibility, operational readiness, observability, rollback specifics |
| QA/Operations | Quantified verification criteria, acceptance conditions, business continuity, edge cases |

Each reviewer provides: a 1-10 score with justification, issues classified by severity (P0/P1/P2), and concrete improvement suggestions.

**Revision loop:**
1. Fix all P0 issues immediately
2. Resolve conflicts between perspectives — document trade-off reasoning
3. Consistency sweep: update ALL documents that reference changed information
4. Re-run self-check on revised content
5. Log what was changed and why in the work log
