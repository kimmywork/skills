# Solution Delivery Loop Rewrite Review v4

Date: 2026-07-06

## Scope

Fourth-pass review after the updated `tracks/sdl-rewrite-self-review-v2.md` and fixes for `tracks/solution-delivery-loop-rewrite-review-v3.md`.

Reviewed:

- Current `delivery/` skill family.
- The v3 feedback areas, especially `structured-investigation` references.
- Current self-review v2 claims.

Explicitly not reviewed:

- `delivery/solution-delivery-loop/evals/` — these were intentionally deleted and are out of scope per user instruction.

No subagents were used.

## Executive summary

This version is **near final**. The v3 feedback was mostly corrected, and the biggest concern from v3 — genericizing `structured-investigation` references without losing code-investigation rigor — is now substantially addressed.

Recommended status: **acceptable with minor cleanup**, not “perfect/100%”.

Estimated completion: **~95%**.

The remaining issues are mostly consistency/polish, with one important content mismatch:

1. `structured-investigation/references/workflow.md` is now generic and includes a code/system addendum, but `structured-investigation/SKILL.md` still has the old code-centric analyze step (`producer → serialization → transport → consumer → storage`).
2. `traps-and-examples.md` confidence-label table is slightly weaker than `workflow.md` on source independence / citation laundering.
3. A few descriptions still include workflow summaries after the trigger.
4. Some README comparison-table wording still says `vertical slice` / `PRD` in historical framework-comparison context; this is acceptable if intentionally historical.

No major blocker remains for using this as a generic `solution-delivery-loop` family.

## Self-review claim audit

| Self-review claim | Result | Notes |
|---|---:|---|
| SI-1: Code-specific hard checks preserved | Mostly true | `workflow.md` now has `Code/System Investigation Addendum` with the old hard checks. Good. |
| SI-2: `templates.md` genericized | True | Templates now include Source Record, Claim Matrix, Synthesis Report, plus mode-specific Code/Data Flow Template. |
| SI-3: confidence ambiguity fixed | Mostly true | `workflow.md` has independence requirement and citation laundering trap; `traps-and-examples.md` label table should mirror it. |
| SI-4: source quality criteria added | True | `workflow.md` now has Source quality matrix. |
| SI-5: interaction rules clarified | True | `structured-investigation/SKILL.md` now distinguishes full investigations vs Quick/Autonomous mode. |
| SI-6: main SKILL code-centric wording fixed | False | `structured-investigation/SKILL.md:41` still says `producer → serialization → transport → consumer → storage`. |
| FAM-1: cold-start numbering fixed | True | `cold-start.md` is now numbered 1–7. |
| FAM-2: `files/modules` placeholders replaced | Mostly true | Track, plan, and delivery-record templates use generic artifact/component wording. |
| FAM-3: PRD in routing/README updated | Mostly true | Core routing now uses `requirements/PRDs`; README tables use `Requirements + design`. Historical comparison rows still mention PRD, acceptable. |
| FAM-4: acceptance checklist wording fixed | True | Now says `Verification method/evidence`. |
| Residual issues: none | Too strong | Minor issues remain; see below. |

## Structured Investigation assessment

### Overall result

`structured-investigation` references are now **substantially complete and significantly better than v3**.

The rewrite now preserves both sides of the intended capability:

- **Generic investigation discipline**: source inventory, source metadata, source-quality matrix, confidence labels, cross-references, gray-zone exclusion, bias traps, and multi-perspective review.
- **Code/data-system rigor**: code/system addendum preserves dynamic field tracing, pipeline hops, serialization/storage, precision/timezone/enum checks, caches/queues/middleware, pseudocode naming, and unobservable dependency callouts.

This resolves the major v3 concern that genericization had reduced constraint strength.

### Strengths in current `structured-investigation/references/workflow.md`

Positive changes now present:

- Generic source types include code, documents, web, data, expert interviews, logs, experiments.
- Source metadata is required for every source.
- Code/system addendum preserves the old code-investigation hard checks.
- Analyze phase uses a generic chain: `source → transformation → delivery → consumption → impact`.
- Code/data systems get a scoped chain: `producer → serialization → transport → consumer → storage`.
- Confidence labels include direct primary-source confirmation, independent cross-reference, inferred, asserted, and from-agent-knowledge.
- Citation laundering is explicitly called out.
- Source-quality matrix gives trust defaults and required checks.
- Multi-perspective review includes domain expert, technical reviewer, stakeholder/decision maker, and devil’s advocate.

This is a solid generic investigation reference.

### Strengths in current `structured-investigation/references/templates.md`

The previous template problem is mostly fixed:

- Directory structure is no longer code-first.
- `Source Record Template` works across source types.
- `Claim Matrix Template` is appropriate for evidence-backed investigation.
- `Synthesis Report Template` is generic and useful for final deliverables.
- `Code/Data Flow Template` preserves mode-specific structure without forcing all investigations into it.

This is a good final shape.

### Remaining structured-investigation issues

#### SI-v4-1 — Main `SKILL.md` still has old code-centric analyze wording

**Impact:** Medium. The references are correct, but agents may act from `SKILL.md` without loading `workflow.md`. The main skill should not contradict the generic reference.

Evidence:

- `delivery/structured-investigation/SKILL.md:41` says:
  - `Trace the chain end-to-end: producer → serialization → transport → consumer → storage.`

This is exactly the code/data-system chain that v3 asked to scope as code mode.

Recommended fix:

Replace with the wording already used in `workflow.md`:

```markdown
Trace the chain end-to-end: source → transformation → delivery → consumption → impact. Never stop at one link. For code/data systems: producer → serialization → transport → consumer → storage.
```

Also consider updating line 17 similarly:

```markdown
Trace from origin → transformation → delivery/use → decision/impact. For code/data systems, also trace storage and consumption.
```

#### SI-v4-2 — Confidence label table in `traps-and-examples.md` should mirror workflow strictness

**Impact:** Low-medium. `workflow.md` has the stricter correct definition; `traps-and-examples.md` is slightly looser.

Evidence:

- `workflow.md` defines cross-referenced as `2+ independent sources (not merely quoting the same origin)` and includes citation laundering.
- `traps-and-examples.md` table says only `Verified from 2+ independent sources`, without the “not quoting same origin” warning.
- `traps-and-examples.md` says `From-agent-knowledge` is used when agent knowledge is the only source, but does not repeat “do not use as final evidence without confirmation.”

Recommended fix:

Update the label table in `traps-and-examples.md`:

- `Cross-referenced`: `Verified from 2+ independent sources that do not merely repeat the same origin`.
- `From-agent-knowledge`: `Only as a temporary label; not final evidence without confirmation`.

This keeps all reference files aligned.

#### SI-v4-3 — Code/Data Flow Template could restore `Persistence/Transport`

**Impact:** Low. The code/system addendum covers this, but the mode-specific template no longer has the old `Persistence/Transport` line.

Evidence:

- Current `Code/Data Flow Template` has `Source` and `Confidence`, then field table.
- Old template included `Persistence/Transport: {how it's serialized, stored, or sent}`.

Recommendation:

Add this line back to the mode-specific template:

```markdown
> Persistence/Transport: <how it is serialized, transported, stored, or consumed>
```

This strengthens code/data-flow outputs without affecting generic investigations.

## Remaining family-level observations

### FAM-v4-1 — Descriptions start with `Use when...`, but two still summarize workflow

**Impact:** Low. Much better than previous versions; not blocking. But if strictly following the workspace’s skill-writing guidance, descriptions should describe trigger conditions only.

Evidence:

- `review-feedback` description includes: `Tags issues... Recommends fix-in-place or roll-back.`
- `process-distillation` description includes: `Analyzes deviations... proposes updates...`.

Recommendation:

Optional cleanup: keep only trigger conditions and move behavior summaries to the body.

### FAM-v4-2 — README comparison matrix still uses old software terms in historical comparison rows

**Impact:** Low. Mostly acceptable because these are comparison/historical rows, not core instructions.

Examples:

- English README comparison table still has `one verified vertical slice` in the `Implementation` matrix row.
- English/Chinese comparison rows still mention PRD in comparison with other frameworks.

Recommendation:

No required change if intentionally historical. If you want full consistency, mark these as comparison terms or replace SDL’s own matrix cell with `one verified increment` while leaving other frameworks unchanged.

### FAM-v4-3 — Some generic routing still mentions code/tests in context search

**Impact:** Low. Acceptable because code/tests can be available sources, but for maximum non-code neutrality it could say “code/tests if relevant.”

Evidence:

- `solution-delivery-loop/SKILL.md:20` includes code/tests in initial context inspection.
- `requirement-discovery/SKILL.md:16` includes code/tests in initial context inspection.

Recommendation:

Optional wording:

```markdown
... relevant source artifacts such as docs, data, code/tests when applicable, logs, prior decisions...
```

## Final assessment

This version is good enough to treat as the first complete generic `solution-delivery-loop` candidate, with minor cleanup recommended before final polish.

The structured-investigation references are now broadly complete and no longer appear to lose the important old code-investigation constraints. The only significant miss is that the main `structured-investigation/SKILL.md` still has one code-centric analyze step that should be changed to match the new generic `workflow.md` wording.

Recommended status: **accept / minor follow-up cleanup**.

Suggested final fixes:

1. Update `structured-investigation/SKILL.md:41` to the generic chain wording from `workflow.md`.
2. Tighten `traps-and-examples.md` confidence label table to match `workflow.md`.
3. Optionally restore `Persistence/Transport` in the code/data-flow template.
4. Optionally remove workflow summaries from `review-feedback` and `process-distillation` descriptions.
5. Optionally soften code/tests wording in generic context-search steps.
