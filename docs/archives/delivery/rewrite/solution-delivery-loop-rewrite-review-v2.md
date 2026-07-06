# Solution Delivery Loop Rewrite Review v2

Date: 2026-07-06

## Scope

Second-pass review after the agent’s follow-up changes and its self-review in `tracks/sdl-rewrite-self-review.md`.

Reviewed:

- Current `delivery/` skill family.
- Prior plan intent from `tracks/solution-delivery-loop-improvement-plan-v2.md`.
- The agent’s self-review claims.

Ignored unrelated reference/analysis material outside the delivery/development rewrite scope.

No subagents were used.

## Review method

Fresh checks run in this pass:

- Listed all `delivery/` files.
- Scanned for legacy/genericization-sensitive terms:
  - `software-delivery-loop`, `code-investigation`, `prd-v1`, `Code Fit`, `software work`, `Software Delivery Loop`, `verification commands`, `module landing`, `vertical slice`, `PRD`, `software`, `code`, `TDD`, `E2E`, `architecture`, etc.
- Read key updated files:
  - `delivery/solution-delivery-loop/README.md`
  - `delivery/solution-delivery-loop/README.zh.md`
  - `delivery/solution-delivery-loop/SKILL.md`
  - `delivery/solution-design/SKILL.md`
  - `delivery/solution-design/references/plan-template.md`
  - `delivery/delivery-acceptance/references/delivery-record-template.md`
  - `delivery/structured-investigation/SKILL.md`
  - `delivery/structured-investigation/references/workflow.md`
  - `delivery/structured-investigation/references/traps-and-examples.md`
  - eval JSON files
- Validated JSON syntax for plugin/eval files.
- Checked `SKILL.md` line counts and frontmatter descriptions.

## Executive summary

The follow-up pass **materially improved** the rewrite, especially:

- README top-level naming and install commands.
- Addition of `structured-investigation` to README install/family lists.
- `Code Fit` → `Format Fit` in several core places.
- Requirements path/template naming.
- Cold-start first step is now non-code-safe.
- `solution-design` is partially genericized.

However, the self-review overstates completion. The rewrite is **not complete yet**. Several claims marked ✅ Complete are contradicted by current files.

Estimated completion now: **~82%**.

Recommendation: **Do not accept as complete** until the remaining P0/P1 issues below are fixed.

## Self-review accuracy audit

| Self-review claim | Actual result | Evidence |
|---|---:|---|
| “P0/P2 solution-design 通用化 ✅ Complete” | Partially false | `solution-design/SKILL.md` still says “Plan vertical slices” and has `Verification commands`; planning rules still E2E/test-first by default. |
| “P1 evals software→solution ✅ Complete” | False | Main evals and trigger evals still contain parser regression, API contract, software change, PRD/module landing, vertical slice, tests, architecture fit. |
| “P1 descriptions trigger-only ✅ Complete” | False | `review-feedback`, `process-distillation`, `structured-investigation` descriptions still start with workflow/definition text, not trigger-only `Use when...`. |
| “P1 structured-investigation in install list + evals candidate skills ✅ Complete” | Half false | README install/family list includes it, but `trigger-evals.json` candidate list still omits `structured-investigation`. |
| “No vertical slice in generic skills ✅” | False | `solution-design/SKILL.md` uses vertical slices directly. |
| “No module landing in generic contexts ✅” | Partially false | `implementation-checklist.md` still has module landing and architecture/code fit in generic checklist; trigger evals still mention module landing. |
| “No PRD in non-comparison contexts ✅” | False | README review tables, trigger evals, README.zh matrix, and skill body still include PRD outside pure historical comparison. |
| “No non-code evals added” treated as acceptable | Not acceptable for this rewrite | The rewrite’s core purpose is generic solution delivery; current evals mostly validate software behavior. |
| “Cold start non-code-safe ✅” | Mostly true, but polish needed | First step is generic; numbering is broken and later line still says discovered commands. |

## Completion matrix vs plan

| Plan item | Current status | Notes |
|---|---:|---|
| P0: entry rename + directory migration | Mostly complete | `solution-delivery-loop` exists; README top titles fixed. Some PRD/software wording remains. |
| P0: SKILL descriptions genericized | Partial | Main descriptions are more generic, but three descriptions still violate trigger-only style. |
| P0: implementation-execution generic loop | Mostly complete | Generic loop exists; checklist remains software-shaped. |
| P0: verification framework abstraction | Partial | Skill body uses Format Fit; delivery record/checklist still mix commands/software wording and duplicate Format Fit heading. |
| P1: structured-investigation rewrite | Partial | Main skill generic; support references are still code-investigation oriented. |
| P1: output rename `prd-v1` → `requirements-v1` | Mostly complete | Paths updated; PRD remains in review tables/evals/README matrix. |
| P2: solution-design rewrite | Partial | Some generic terms added; core process still contains vertical-slice/software verification residue. |
| P2: requirement-discovery research call | Complete | `structured-investigation` call exists. |
| P3: format templates | Structurally complete | Files exist; integration needs cleanup. |
| Cold start non-code-safe | Mostly complete | First step fixed; numbering/commands need cleanup. |
| Evals genericized | Not complete | Existing evals remain software-centric; no non-code eval coverage. |

## Findings

### P0 — Evals still validate the old software loop, not generic solution delivery

**Impact:** High. The self-review says eval terminology was updated, but the actual eval corpus still largely tests software-specific behavior. This is important because the rewrite’s purpose is broader delivery.

Evidence:

- `delivery/solution-delivery-loop/evals/evals.json:12-13` is still a parser regression test and expects “one vertical slice”.
- `delivery/solution-delivery-loop/evals/evals.json:24-25` is still an API compatibility fallback scenario.
- `delivery/solution-delivery-loop/evals/evals.json:30-31` still says “multi-project software change”.
- `delivery/solution-delivery-loop/evals/trigger-evals.json:44` still says “The PRD is approved. Decide module landing, API contracts, trade-offs, task slices, and verification commands.”
- `delivery/solution-delivery-loop/evals/trigger-evals.json:59` still says “one vertical slice, update tests”.
- `delivery/solution-delivery-loop/evals/trigger-evals.json:79` still says “tests, architecture fit, and release decision”.

Recommendation:

- Keep some software evals as software-mode coverage, but add/replace with non-code evals:
  - report/analysis deliverable with citations → `delivery-acceptance` Format Fit report.
  - competitive/domain research → `structured-investigation`.
  - proposal/plan from clear requirements → `solution-design`.
  - documentation-only delivery record → `implementation-execution` / `delivery-acceptance` without shell-command assumptions.
- Add `structured-investigation` to `candidate_skills` in trigger evals.

### P0 — `solution-design` remains partly software-centric and contradicts the plan

**Impact:** High. `solution-design` is central to the family. The plan asked for “deliverable structure” and “verifiable increments”; the current skill still includes old execution semantics.

Evidence:

- `delivery/solution-design/SKILL.md:24` says: “Plan vertical slices. Each slice must be reviewable and independently verifiable.”
- `delivery/solution-design/SKILL.md:37` still includes “Verification commands” after “Verification methods”.
- `delivery/solution-design/SKILL.md:44-45` says to prefer E2E/integration seams and test-first behavior changes without scoping this to software mode.
- `delivery/solution-design/SKILL.md:54` says return here when implementation changes “architecture”.
- README family list still describes `solution-design` as “architecture, deployment modes, contracts, test strategy” (`README.md:23`, `README.zh.md:23`).

Recommendation:

- Change `vertical slices` → `verifiable increments` in the skill body.
- Remove `Verification commands` from generic plan content; keep only `Verification methods/evidence`.
- Move E2E/test-first guidance to a software-mode note/reference.
- Make README family summary generic: “deliverable structure, alternatives, interfaces/contracts, verification strategy, plan”.

### P0 — Delivery record template is internally inconsistent

**Impact:** High. This template shapes final outputs. It currently mixes the new Format Fit model with old command/file assumptions and has a duplicated heading.

Evidence:

- `delivery/delivery-acceptance/references/delivery-record-template.md:19` still says `<files/modules/user-visible behavior>`.
- `delivery/delivery-acceptance/references/delivery-record-template.md:25` still says `command/manual evidence`.
- `delivery/delivery-acceptance/references/delivery-record-template.md:27-31` has a dedicated `Verification Commands` bash block.
- `delivery/delivery-acceptance/references/delivery-record-template.md:47-49` has duplicate headings:
  - `### Format Fit`
  - `### Format Fit (<software/report/plan/investigation/other>)`

Recommendation:

- Replace with:
  - `## Changed / Produced Artifacts`
  - `## Verification Evidence`
  - `| Acceptance / Req | Result | Evidence type | Evidence reference |`
  - `### Format Fit (<type>)`
- Remove the unconditional bash block. If commands exist, record them as one evidence type.

### P1 — `structured-investigation` references remain code-investigation references

**Impact:** Medium-high. The main skill is generic, but detailed references are likely to be loaded when agents need help; those references still force code/data-flow assumptions.

Evidence:

- `delivery/structured-investigation/references/workflow.md:11-15` starts with project structure, build configs, modules, entry points, and type/schema inventory.
- `workflow.md:29-37` focuses on type definitions, untyped fields, serialization, consumers, storage behavior, numeric precision, enums, arrays.
- `workflow.md:65-72` requires code-backed references, dynamic field tracing, pipeline hops, enum domains, timestamps, and pseudocode matching code.
- `delivery/structured-investigation/references/traps-and-examples.md:11-19` is still code/data-system trap guidance.
- `traps-and-examples.md:90-93` uses `Confirmed / Inferred / Assumed / Unknown`, which conflicts with the main skill’s `confirmed / cross-referenced / inferred / asserted / from-agent-knowledge` labels.

Self-review says this is intentional/future work. That is acceptable only if the rewrite is not declared complete. For a complete generic family, the reference mismatch remains a real gap.

Recommendation:

- Rename current code-specific references to an explicit code mode file, e.g. `references/code-investigation.md`.
- Create a generic `workflow.md` with source-agnostic steps.
- Add short domain/web/data modes or at least a source-type matrix.
- Normalize confidence labels across all references.

### P1 — `trigger-evals.json` still omits `structured-investigation`

**Impact:** Medium. The self-review explicitly claims this was fixed in install command + family list + eval candidate skills, but only the README side is fixed.

Evidence:

- `delivery/solution-delivery-loop/evals/trigger-evals.json:4-10` candidate skills are only:
  - `solution-delivery-loop`
  - `requirement-discovery`
  - `solution-design`
  - `implementation-execution`
  - `delivery-acceptance`
- `structured-investigation` is missing.

Recommendation:

- Add `structured-investigation` to candidate skills.
- Add direct trigger evals for “investigate”, “research”, “analyze sources”, “competitive research”, and “trace claim to sources”.

### P1 — Frontmatter descriptions are still not trigger-only

**Impact:** Medium. This workspace’s skill-writing guidance requires descriptions to start with `Use when...` and avoid workflow summaries. The self-review says this is complete, but it is not.

Evidence:

- `delivery/review-feedback/SKILL.md:3` starts “Independent review of phase/workflow outputs. Use after...”, then summarizes inspection/tagging/recommendation workflow.
- `delivery/process-distillation/SKILL.md:3` starts “Extract durable improvements...” and summarizes analysis/update behavior.
- `delivery/structured-investigation/SKILL.md:3` starts “Universal investigation methodology for any domain. Use when...”.

Recommendation:

- Rewrite these as trigger-only descriptions, e.g.:
  - `review-feedback`: `Use when any phase artifact has been produced and needs independent review before proceeding...`
  - `process-distillation`: `Use when recurring phase friction, repeated review feedback, or resolved phase cycles suggest skill/process improvements...`
  - `structured-investigation`: `Use when a question requires investigation, research, source tracing, system mapping, root cause analysis, or deriving truth from primary sources...`

### P1 — Generic checklists/templates still leak software execution assumptions

**Impact:** Medium. These references are used during execution and acceptance, so they can pull agents back toward code-specific behavior.

Evidence:

- `delivery/implementation-execution/references/implementation-checklist.md:8-10` says current slice, module landing, verification command.
- `implementation-checklist.md:19-31` is TDD/build/software API/storage oriented.
- `implementation-checklist.md:42` says “Architecture/code fit checked.”
- `delivery/solution-design/references/plan-template.md:53-57` stop conditions are module/package/files/shim oriented.
- `delivery/solution-delivery-loop/references/track-template.md:40` says `<files/modules/affected artifacts>`.
- `delivery/delivery-acceptance/references/acceptance-checklist.md:24` says “Verification command/manual scenario was run fresh.”

Recommendation:

- Split checklist into generic checklist + software-mode checklist, or make software items conditional.
- Replace:
  - `slice` → `increment`
  - `module landing` → `planned structure / affected artifacts`
  - `verification command` → `verification method/evidence`
  - `Architecture/code fit` → `Format Fit` or `deliverable-structure fit`

### P1 — README.zh still has old software-only rows in the non-historical matrix

**Impact:** Medium. The top of README.zh is now good, but the design matrix and chooser table still say software-only in places that appear to describe the current SDL, not only historical comparison.

Evidence:

- `delivery/solution-delivery-loop/README.zh.md:132` says SDL scope is `仅软件交付`.
- `README.zh.md:136` says implementation is `一个已验证垂直切片`.
- `README.zh.md:164` says `端到端软件请求、阶段不清、或继续已有 track work | SDL`.

Recommendation:

- Mirror the English README’s updated generic scope in the zh design matrix and chooser table.
- Replace “垂直切片” with “可验证增量”.

### P2 — Cold-start file is improved but has a numbering defect and minor command residue

**Impact:** Low-medium. Not semantically blocking, but visible quality issue.

Evidence:

- `delivery/solution-delivery-loop/references/cold-start.md:7-10` has two numbered `2.` items.
- `cold-start.md:21` still says “Record discovered commands and conventions”; commands should be “verification methods/commands” or conditional on software.

Recommendation:

- Fix numbering.
- Use “verification methods, reusable commands, and conventions” or split software-specific commands conditionally.

## Positive changes since the previous review

The follow-up changes are real and useful:

- README titles and first paragraphs now mostly present Solution Delivery Loop correctly.
- `structured-investigation` is now included in README install commands and family list.
- `delivery-acceptance/SKILL.md` and many docs use `Format Fit` instead of `Code Fit`.
- Requirements path naming is improved.
- `solution-design` now includes “deliverable structure” and “Verification methods”.
- Cold start no longer starts by assuming code layout.
- `requirements-template.md` is now titled `Requirements Template (PRD-compatible)`, which is an acceptable compromise if PRD remains a subtype.
- JSON files are syntactically valid.
- All `SKILL.md` files remain under 500 lines.

## Updated suggested fix order

1. Fix evals first: add non-code coverage and include `structured-investigation` in candidates.
2. Finish `solution-design` genericization: vertical slice/commands/E2E/test-first should be generic or software-mode conditional.
3. Clean delivery record template: remove duplicate Format Fit heading and unconditional bash command block.
4. Split or clearly label `structured-investigation` code-specific references.
5. Rewrite three frontmatter descriptions as trigger-only `Use when...` descriptions.
6. Genericize implementation checklist and plan/track/acceptance templates.
7. Sync README.zh matrix/chooser with the English generic wording.
8. Fix cold-start numbering and command wording.

## Final conclusion

The rewrite is **much closer** than the previous review, but the self-review is too optimistic. The current state is not yet a consistent, fully generic `delivery/solution-delivery-loop` family.

The remaining issues are not just wording polish: evals, design instructions, acceptance templates, and detailed investigation references still encode software-delivery behavior. These are exactly the files agents will use to decide what to do and what shape to output.

Recommended status: **partial / needs another cleanup pass before marking complete**.
