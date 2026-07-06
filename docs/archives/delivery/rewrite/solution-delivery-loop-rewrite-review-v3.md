# Solution Delivery Loop Rewrite Review v3

Date: 2026-07-06

## Scope

Third-pass review after `tracks/sdl-rewrite-self-review-v2.md`.

Focus:

- Verify the self-review v2 claims against current `delivery/` files.
- Assess the rewritten `structured-investigation` references for completeness, comprehensiveness, and constraint strength.
- Confirm whether the family is now consistent as generic `delivery/solution-delivery-loop`.

Per user instruction, `delivery/solution-delivery-loop/evals/` is intentionally deleted and **not reviewed**.

No subagents were used.

## Executive summary

The rewrite is now **substantially improved** and much closer to a coherent generic solution-delivery skill family. The most important improvements since v2 are real:

- `solution-design` now uses `verifiable increments` and no longer has generic E2E/test-first defaults.
- Delivery record template no longer has a bash block or duplicated `Format Fit` heading.
- Implementation checklist is largely generic.
- Frontmatter descriptions now start with `Use when...`.
- `structured-investigation/references/workflow.md` and `traps-and-examples.md` were meaningfully rewritten to be domain-agnostic.

However, self-review v2’s “100% / no residual issues” is still too strong. There are remaining consistency/polish issues, and the `structured-investigation` rewrite, while much better, has two important risks:

1. It **diluted some of the old code-investigation hard checks** without preserving them in a code-specific mode reference.
2. `templates.md` still heavily assumes code/data-flow/entity analysis and was not rewritten to match the new generic investigation model.

Recommended status: **near-complete, but not 100%; one focused cleanup pass remains**.

Estimated completion: **~90%**.

## Self-review v2 claim audit

| Self-review v2 claim | Actual result | Notes |
|---|---:|---|
| All descriptions start with `Use when...` | True | 8/8 SKILL descriptions now start with `Use when...`. Some still include process summaries after trigger, but much improved. |
| No `Code Fit` outside `format-software.md` | True | Scan found no remaining `Code Fit`. |
| No `vertical slice` in SKILL/process/template files | Mostly true | Only README comparison table remains; current `solution-design` uses `verifiable increments`. |
| No `module landing` in generic skill files | Mostly true | Remaining generic-ish leak is `implementation-execution/SKILL.md` software-specific signal plus `solution-design-template.md` software-mode note. Acceptable if scoped. |
| No `TDD`/`E2E`/`test-first` in generic contexts | Mostly true | `solution-design/SKILL.md` refers to software-mode for E2E/test-first; acceptable. README software-mode mentions remain. |
| No `Verification commands` in templates | Mostly true | Exact phrase removed. `acceptance-checklist.md` still says `Verification command/manual scenario`. |
| Cold-start non-code-safe | Mostly true | First step is generic; numbering is still broken. |
| Delivery record template no bash/hard-coded commands | True | Bash block removed. Some placeholders still say files/modules. |
| Implementation checklist generic | Mostly true | Much improved; software is conditional. |
| Residual issues: none | False | Remaining issues listed below. |

## Structured Investigation reference assessment

### Overall assessment

The rewrite is a **significant improvement** over the prior state. `workflow.md` is now genuinely generic at the top level, and `traps-and-examples.md` now teaches source tracing, outdated-information detection, confidence labels, and cross-source verification without being only about code.

But it is not fully comprehensive yet. The rewrite replaced a highly constrained code-investigation methodology with a broad generic investigation workflow. That is directionally correct for `structured-investigation`, but some old high-value safeguards were not preserved anywhere.

The best final structure would be:

- generic `workflow.md` — current generic workflow, with small additions below;
- generic `templates.md` — source-agnostic templates;
- `code-mode.md` or a code-specific section — preserves old detailed code/data-flow constraints;
- optional domain/web/data/expert sub-sections — source-specific criteria.

### What improved

Current `delivery/structured-investigation/references/workflow.md` now includes important generic investigation constraints:

- scope before gathering (`workflow.md:7-16`)
- source inventory with metadata (`workflow.md:23-36`)
- multiple source types: code, web/domain, data, expert interviews (`workflow.md:27-35`)
- cross-reference requirement (`workflow.md:43-49`)
- explicit confidence labels (`workflow.md:47-53`)
- gray-zone handling (`workflow.md:55`)
- bias/cherry-picking warnings (`workflow.md:58-62`)
- source-backed self-check (`workflow.md:77-83`)
- multi-perspective review including devil’s advocate (`workflow.md:86-95`)

Current `traps-and-examples.md` is also much more generic than before:

- Shallow exploration → primary source tracing.
- Doc-driven conclusions → secondary sources as hypotheses.
- Single-source tunnel vision → independent cross-reference.
- Outdated information → latest-state verification.
- Unvalidated proposals → executable precondition check.
- Optimism bias → edge cases/conflicts.
- Confidence label table matches the main skill’s label set.

This is a real improvement.

### What may have been lost or weakened

#### SI-1 — Code-specific hard checks were removed instead of preserved as a mode

**Impact:** Medium-high. The new generic workflow is appropriate, but code investigations were an important use case. The old references had precise checks that prevent common code-analysis failures; most are no longer present except as broad language.

Old high-value checks that are now missing or weakened:

- Full type/schema inventory before deep dive.
- Chase untyped/dynamic fields to runtime assignment site.
- Inspect producer, serialization, consumer, and storage with field-name/serialization rules.
- Capture numeric scale/offset, timezone/format, enum domains, array serialization.
- Identify transient/skipped/in-memory-only fields.
- Cover all data types, including edge cases/extensions.
- Inspect caches, queues, middleware as pipeline hops.
- Ensure pseudocode naming matches actual code exactly.
- Call out binary dependencies/external services as unobservable.

Evidence:

- Old `workflow.md` had these explicit checks around code/data flow investigation.
- New `workflow.md:28` compresses code investigations into one line: “read source code, tests, build configs, CI, logs. Trace producer → serialization → transport → consumer → storage.”
- New `workflow.md:77-83` generic self-check no longer requires dynamic field tracing, pipeline-hop completeness, enum/timestamp/numeric precision checks, or pseudocode-name consistency.

Recommendation:

- Add a `## Code/system investigation addendum` section to `workflow.md`, or create `references/code-mode.md`.
- Preserve the old detailed checklist there, explicitly scoped to code/data-flow investigations.
- Link from `structured-investigation/SKILL.md` and `workflow.md`: “For code/data-flow investigations, apply the code-mode checklist in addition to the generic workflow.”

#### SI-2 — `templates.md` is still code/entity-flow shaped and not aligned with the generic rewrite

**Impact:** Medium-high. `workflow.md` says use `references/templates.md` for format guidance, but templates still push investigators toward code/data entity outputs.

Evidence:

- `delivery/structured-investigation/references/templates.md:14` says `03-analysis` is “code structure, data models, protocols, flows”.
- `templates.md:42` says the analysis template is “for each data entity or flow”.
- `templates.md:47-58` uses `Source: module/path/filename`, `Persistence/Transport`, a `Field | Type | Source` table, serialization edge cases, and skipped fields.
- `templates.md:71` says completed work includes “which modules read”.

Risk:

A non-code investigation, such as market research or policy analysis, will receive a code/data-schema shaped template. This can degrade output quality or cause irrelevant structure.

Recommendation:

- Split templates by investigation output type:
  - `Source Record Template` — works for any source.
  - `Claim Matrix Template` — claim, confidence, supporting sources, conflicting sources, gaps.
  - `Synthesis Report Template` — question, method, findings, implications, recommendations.
  - `Code/Data Flow Template` — preserve current field/type/serialization table as mode-specific.
- Change directory comments from “code structure, data models” to “per-source/per-domain analysis, evidence tables, claim matrices, flow maps”.

#### SI-3 — Confidence-level policy is good, but “confirmed” vs “cross-referenced” semantics need tightening

**Impact:** Medium. The current labels are useful, but `confirmed` and `cross-referenced` can be misused.

Current definitions:

- `confirmed`: directly verified from primary source
- `cross-referenced`: verified from 2+ independent sources

Potential ambiguity:

A claim verified by one primary source and one secondary source could be called cross-referenced, even if the secondary source depends on the primary. “Independent” is stated in `workflow.md:43`, but the confidence label table should repeat independence requirements.

Recommendation:

- Define independence explicitly:
  - `cross-referenced`: verified by 2+ independent sources that do not merely quote the same origin.
- Add a trap for citation laundering: multiple sources that all repeat the same unsupported claim do not count as cross-reference.

#### SI-4 — Source quality and hierarchy are underdeveloped for non-code research

**Impact:** Medium. The plan emphasized source verification, evidence hierarchy, and gray-zone handling. The new references mention source metadata and cross-reference, but lack concrete source-quality criteria.

Missing pieces for robust non-code investigations:

- Source type hierarchy: official docs / primary data / peer-reviewed / authoritative expert / secondary analysis / community / marketing.
- Recency and version checks.
- Conflict-of-interest / author credibility checks.
- Distinguishing primary measurement from interpretation.
- Handling unavailable or paywalled sources.
- Citation requirements for external claims.

Recommendation:

Add a `Source Quality Matrix` to `workflow.md` or `templates.md`:

| Source type | Trust default | Required checks |
|---|---|---|
| Primary data/log/source code | High | provenance, date/version, completeness |
| Official docs/specs | Medium-high | version, implementation reality, known drift |
| Peer-reviewed / audited | Medium-high | method, sample, date, conflicts |
| Expert interview | Medium | role, access, uncertainty, corroboration |
| Blog/community/marketing | Low-medium | corroborate before using as factual basis |
| Agent knowledge | Lowest | mark from-agent-knowledge, do not use as final evidence without confirmation |

#### SI-5 — Interaction rules may be too rigid for quick/autonomous investigations

**Impact:** Low-medium. Main `SKILL.md` says confirm with user at each phase transition (`structured-investigation/SKILL.md:78`). That is appropriate for full investigations, but may conflict with Quick Mode and autonomous delivery loops.

Recommendation:

- Clarify: “For full investigations, confirm at phase transitions. In Quick Mode or when the user requested autonomous work, proceed without repeated confirmation but record assumptions and stop on scope/risk ambiguity.”

#### SI-6 — Main `structured-investigation/SKILL.md` still has some code/data-flow default wording

**Impact:** Low-medium. References are now generic, but the main skill still says:

- `Analyze` step traces “producer → serialization → transport → consumer → storage” (`structured-investigation/SKILL.md:41`).
- Quick Mode says trace “one level up and one level down” (`structured-investigation/SKILL.md:70`).

This is acceptable for systems analysis, but less natural for market/domain research.

Recommendation:

- Change main skill wording to:
  - “Trace the relevant chain end-to-end: source → transformation/interpretation → delivery/use → decision/impact. For code/data systems, use producer → serialization → transport → consumer → storage.”

## Remaining family consistency issues outside structured-investigation

### FAM-1 — `cold-start.md` numbering is still broken

Evidence:

- `delivery/solution-delivery-loop/references/cold-start.md:7-21` has numbered items `1,2,3,4,4,5,7`.

Recommendation: renumber to `1-7`.

### FAM-2 — Some generic templates still use `files/modules`

Evidence:

- `delivery/delivery-acceptance/references/delivery-record-template.md:19` says `<files/modules/deliverable artifacts>`.
- `delivery/solution-delivery-loop/references/track-template.md:40` says `<files/modules/affected artifacts>`.
- `delivery/solution-design/references/plan-template.md:55` says “touched files/modules exceed estimate by ~2x”.

Recommendation:

- Use `affected artifacts/components/sections` for generic templates.
- Mention files/modules only under software mode.

### FAM-3 — PRD remains in active routing/README contexts

Evidence:

- `delivery/solution-delivery-loop/SKILL.md:20` reads track docs, `PRDs`, plans.
- `delivery/requirement-discovery/SKILL.md:16` reads track docs, `PRDs`, delivery records.
- `delivery/solution-delivery-loop/README.md:50-51` review table says `PRD + design`.
- `delivery/solution-delivery-loop/README.zh.md:50-51` same issue.

This may be acceptable if PRD is an explicit subtype, but it contradicts the self-review claim “No PRD as primary artifact name” unless described as compatibility/subtype language.

Recommendation:

- Prefer “requirements docs/PRDs” or “requirements artifacts”.
- Update README review tables to `Requirements + design`.

### FAM-4 — Acceptance checklist still says verification command/manual scenario

Evidence:

- `delivery/delivery-acceptance/references/acceptance-checklist.md:24` says “Verification command/manual scenario was run fresh.”

Recommendation:

- Change to “Verification method/evidence was performed or inspected fresh.”

### FAM-5 — Descriptions start with `Use when...`, but some still summarize workflow

Evidence:

- `review-feedback` description includes “Tags issues...” and “Recommends...”.
- `process-distillation` description includes “Analyzes deviations...” and “proposes updates...”.

This is less severe than before because the trigger is first, but if strictly following the workspace’s skill-description guidance, these should be trigger-only.

Recommendation:

- Remove workflow summary clauses after the trigger, or keep only trigger conditions.

## Overall conclusion

This is now a strong near-final rewrite, but not yet perfect.

The `structured-investigation` reference rewrite is a **net improvement** for generic solution delivery. It successfully removes most software-only assumptions and adds broadly useful evidence discipline. But it should not be considered fully complete until either:

1. the old code-investigation hard checks are preserved in a code-specific mode/addendum, and
2. `templates.md` is rewritten/split so non-code investigations are not forced into entity/field/serialization templates.

Recommended status: **near-complete / needs focused cleanup**.

Suggested final cleanup sequence:

1. Add code-mode addendum for old detailed code/data-flow safeguards.
2. Rewrite or split `structured-investigation/references/templates.md` into generic + mode-specific templates.
3. Add source-quality/evidence-hierarchy guidance for non-code research.
4. Fix remaining family polish: cold-start numbering, files/modules placeholders, PRD wording, acceptance checklist wording.
5. Optionally tighten descriptions to be trigger-only with no workflow summary.
