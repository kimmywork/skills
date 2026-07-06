# Solution Delivery Loop Rewrite Review

Date: 2026-07-06

## Scope

Reviewed the rewrite from `development/software-delivery-loop` to `delivery/solution-delivery-loop` against `tracks/solution-delivery-loop-improvement-plan-v2.md`.

Per request, the review focused on:

- The semantic diff between the old `development/` family and the new `delivery/` family.
- Consistency of the final skill family under `delivery/`.
- Plan completion for the generic `delivery/solution-delivery-loop` direction.

Ignored unrelated analysis/reference material outside `delivery/` and `development/`, except the plan document used as the acceptance source.

## Review method

- Reconstructed the deleted `development/` tree from `HEAD` and compared it to `delivery/` with expected renames applied:
  - `development/` → `delivery/`
  - `software-delivery-loop/` → `solution-delivery-loop/`
  - `code-investigation/` → `structured-investigation/`
  - `prd-template.md` → `requirements-template.md`
- Scanned `delivery/` for legacy terms: `software-delivery-loop`, `code-investigation`, `prd-v1`, `Code Fit`, `software work`, `architecture/module`, `verification commands`, etc.
- Checked all `SKILL.md` names/descriptions, Markdown line counts, and JSON validity for eval/plugin files.
- Did not use subagents.

## Executive summary

The rewrite is **substantially started but not complete**. Directory-level migration and several P0/P1 changes are present, but the family is still internally split between the new generic “solution delivery” model and the old “software delivery” model.

Estimated completion by plan intent: **~70%**.

What is in good shape:

- `development/` has been replaced by `delivery/` in the working tree.
- `solution-delivery-loop` exists and the old entry name is removed from the skill frontmatter.
- `implementation-execution` now has a generic execution loop and extracted `references/software-mode.md`.
- `delivery-acceptance` has the intended Spec Fit + Format Fit model and format-specific review references.
- `structured-investigation` exists and is invoked by `requirement-discovery` for deep research.
- `requirements-v1.md` path naming is present in the core track layout.

Main blockers before considering the rewrite done:

1. Public README docs still describe SDL as software-only in multiple places, especially `README.zh.md`.
2. `solution-design/SKILL.md` remains software-centric despite the plan’s P2 rewrite target.
3. Acceptance templates/evals still use `Code Fit`, not `Format Fit`.
4. `structured-investigation` support references are still largely code-investigation references.
5. `structured-investigation` is part of the planned family but is missing from install/family/eval lists.
6. There are no generic non-code eval cases, so the new scope is not validated.

## Plan completion matrix

| Plan item | Status | Evidence / notes |
|---|---:|---|
| P0: `software-delivery-loop/` → `solution-delivery-loop/` | Mostly done | Directory and frontmatter renamed. Some README prose still says Software Delivery Loop / software work. |
| P0: all `SKILL.md` descriptions remove software limitation | Mostly done | Main phase descriptions are more generic. `structured-investigation`, `review-feedback`, and `process-distillation` descriptions still violate the project’s description style by summarizing workflow instead of only trigger conditions. |
| P0: implementation-execution generic loop | Done with minor residue | Generic loop present; `software-mode.md` extracted. Residual terms: slice/module landing/Code Fit in subagent roles and after-phase text. |
| P0: verification framework abstraction | Partially done | `delivery-acceptance/SKILL.md` has deliverable-type evidence and Format Fit references. Templates/evals still say Code Fit / verification commands. |
| P1: structured-investigation rewrite | Partially done | Main `SKILL.md` is generic. References remain code/data-model focused. |
| P1: `prd-v1.md` → `requirements-v1.md` | Partially done | Track paths changed. Many artifacts still use PRD terminology and `requirements-template.md` is still titled “PRD Template”. |
| P2: solution-design generic rewrite | Not done enough | Template changed, but `SKILL.md` process and plan content still specify architecture/modules/files/routes/tests. |
| P2: requirement-discovery research call | Done | Step 7 calls `structured-investigation`; research storage path present. |
| P3: format templates | Done structurally | `format-software/report/plan/investigation.md` files exist. Need integration cleanup in delivery record/checklists/evals. |
| P3: composable loop variants deferred | OK | No extra variants created. |
| J1: non-code cold start does not assume codebase | Not done | `cold-start.md` still starts by inspecting code layout, tests, package scripts, CI. |

## Findings

### P0 — README family docs still advertise the old software-only scope

**Impact:** High. These are the user-facing installation and conceptual docs. They currently contradict the new `solution-delivery-loop` name and will teach users/agents that SDL is still software-only.

Evidence:

- `delivery/solution-delivery-loop/README.md:112` says SDL is “for software work”.
- `delivery/solution-delivery-loop/README.md:129` says scope is “Software delivery only”.
- `delivery/solution-delivery-loop/README.md:161` recommends SDL for “End-to-end software request”.
- `delivery/solution-delivery-loop/README.zh.md:1` title is still `Software Delivery Loop（软件交付循环）`.
- `delivery/solution-delivery-loop/README.zh.md:5` describes it as “面向软件交付”.
- `delivery/solution-delivery-loop/README.zh.md:114`, `:120`, `:131`, `:163` all preserve the software-only framing.

Recommendation:

- Rewrite both READMEs around “solution delivery” as the default.
- Keep software as one supported deliverable type, not the family’s scope.
- Replace table cells like “Software delivery only” with “Solution delivery across code, reports, investigations, plans, documentation, and other verifiable deliverables”.
- Update the “when to choose” rows to include non-code examples.

### P0 — `solution-design/SKILL.md` did not receive the planned generic rewrite

**Impact:** High. `solution-design` is one of the central phase skills. The plan explicitly called for replacing architecture/module landing with deliverable structure and verifiable increments. The current skill still routes agents into software architecture mode.

Evidence:

- `delivery/solution-design/SKILL.md:16` tells the agent to read code/tests by default.
- `delivery/solution-design/SKILL.md:20` says: “Map architecture/module landing before tasks: files, packages, contracts, schemas, routes, UI surfaces, tests.”
- `delivery/solution-design/SKILL.md:32-37` plan content still uses “Architecture / module landing”, “routes”, “storage”, “UI contracts”, “Test strategy”, and “Verification commands”.
- `delivery/solution-design/SKILL.md:44-45` prioritizes E2E/integration seams and test-first behavior changes without scoping that to software mode.

Recommendation:

- Apply the plan’s wording directly:
  - “Map deliverable structure: components, sections, modules, interfaces, dependencies.”
  - “Plan verifiable increments.”
  - “Verification methods” rather than “verification commands”.
- Move software-specific architecture/test language into a software-mode reference or conditional block.
- Align `plan-template.md` with the same generic vocabulary.

### P0 — acceptance templates/evals still use `Code Fit` instead of `Format Fit`

**Impact:** High. The acceptance skill body now says Spec Fit + Format Fit, but the generated delivery record and eval expectations still encode the old Code Fit axis. This can cause agents to output the wrong review shape.

Evidence:

- `delivery/delivery-acceptance/references/delivery-record-template.md:47` has `### Code Fit`.
- `delivery/solution-delivery-loop/README.md:135` has `Spec Fit + Code Fit + delivery record`.
- `delivery/solution-delivery-loop/README.md:154` says SDL keeps “Spec Fit and Code Fit”.
- `delivery/solution-delivery-loop/README.zh.md:137` and `:156` have the same issue.
- `delivery/solution-delivery-loop/evals/evals.json:19` expects “Spec Fit and Code Fit”.

Recommendation:

- Rename `Code Fit` to `Format Fit` everywhere except inside `format-software.md`, where code deliverables can define software-specific fit.
- In `delivery-record-template.md`, include:
  - `### Spec Fit`
  - `### Format Fit (<software/report/plan/investigation/other>)`
- Update eval expectations to verify Format Fit selection by deliverable type.

### P0 — `structured-investigation` references are still mostly code-investigation references

**Impact:** High. `requirement-discovery` now calls `structured-investigation` for market analysis, technical feasibility, and domain exploration. But the detailed workflow references still strongly assume code/data-model analysis.

Evidence:

- `delivery/structured-investigation/references/workflow.md:11-15` starts by surveying project structure, build configs, modules, entry points, and data definitions.
- `delivery/structured-investigation/references/workflow.md:29-37` focuses on type definitions, untyped/dynamic fields, serialization, consumers, storage, and all data types.
- `delivery/structured-investigation/references/workflow.md:64-75` requires code-backed source references, dynamic field tracing, pipeline hops, enum domains, timestamps, and pseudocode matching actual code.
- `delivery/structured-investigation/references/traps-and-examples.md` was only lightly renamed and still contains code-specific traps/examples.
- Confidence labels are inconsistent: main skill uses `confirmed / cross-referenced / inferred / asserted / from-agent-knowledge`, while `workflow.md:54` uses `Confirmed / Inferred / Assumed / Unknown`.

Recommendation:

- Split references into generic core + mode-specific guidance, for example:
  - `workflow.md`: universal outline → gather → analyze → synthesize → review.
  - `modes/code.md`: current code/data-flow details.
  - `modes/domain-research.md`: source credibility, citations, conflicting sources.
  - `modes/data-analysis.md`: schemas, samples, transformations.
- Normalize confidence labels across all files.
- Ensure non-code investigations do not inherit mandatory code-backed checks.

### P1 — `structured-investigation` is referenced but not installed/listed as part of the family

**Impact:** Medium-high. A user following README installation may not install a skill that `requirement-discovery` explicitly calls.

Evidence:

- `delivery/requirement-discovery/SKILL.md:23` calls `structured-investigation`.
- `delivery/solution-delivery-loop/README.md:16` install command omits `structured-investigation`.
- `delivery/solution-delivery-loop/README.zh.md:16` also omits it.
- `delivery/solution-delivery-loop/README.md:20-27` family list omits it.
- `delivery/solution-delivery-loop/evals/trigger-evals.json:4-10` candidate skills omit it.

Recommendation:

- Add `structured-investigation` to install commands, family lists, and trigger eval candidates.
- Add at least one trigger eval for “research / investigate / competitive analysis / source-backed report”.

### P1 — `requirements-v1.md` rename is incomplete because PRD terminology still dominates templates and routing

**Impact:** Medium. The path rename is visible, but agents will still produce PRD-shaped artifacts by default and may use inconsistent names.

Evidence:

- `delivery/requirement-discovery/references/requirements-template.md:1` is `# PRD Template`.
- `delivery/requirement-discovery/references/requirements-template.md:13` is `# PRD v<N>: <Product / Feature>`.
- `delivery/requirement-discovery/SKILL.md:33` says broad work is “PRD required”.
- `delivery/solution-delivery-loop/SKILL.md:37-38` review table says `PRD + design`.
- `delivery/solution-delivery-loop/references/loop-state.md:22` still has `- PRD:`.
- `delivery/solution-design/references/plan-template.md:12` has `- PRD / track:`.
- `delivery/delivery-acceptance/references/delivery-record-template.md:12` has `- PRD / track:`.

Recommendation:

- Use “requirements doc” as the default term.
- If PRD is retained as a product-specific subtype, define that explicitly:
  - “For product-style work, the requirements doc may be PRD-shaped.”
- Rename template title to “Requirements Template” and output title to `Requirements v<N>`.

### P1 — cold start still assumes a code repository

**Impact:** Medium. This directly conflicts with the plan’s J1 decision: non-code cold start should not assume a codebase exists.

Evidence:

- `delivery/solution-delivery-loop/references/cold-start.md:7` starts with “Inspect existing project docs, code layout, tests, package scripts, CI, and conventions.”
- `delivery/solution-delivery-loop/references/cold-start.md:20` records “discovered commands”, again skewing toward code.

Recommendation:

- Change cold start to inspect available workspace sources generically:
  - project docs, existing artifacts, source repositories if present, data/doc stores, external references, conventions, verification mechanisms.
- Make code layout/tests/package scripts/CI a conditional software-mode branch.

### P1 — compact track and plan templates are still software-shaped

**Impact:** Medium. Even if phase skills are generic, templates shape agent output. Current templates will push non-code work into files/modules/commands/slices language.

Evidence:

- `delivery/solution-delivery-loop/references/track-template.md:30` says `<vertical slice or fix step>`.
- `delivery/solution-delivery-loop/references/track-template.md:34` says ``<command>`` or manual scenario.
- `delivery/solution-delivery-loop/references/track-template.md:40` says `<files/modules/behavior>`.
- `delivery/solution-design/references/plan-template.md:27-30` has `Files / modules` with `Create / Modify / Test`.
- `delivery/solution-design/references/plan-template.md:36-40` hard-codes test/red/green/refactor steps.
- `delivery/solution-design/references/plan-template.md:53-57` stop conditions are module/package/shim-oriented.

Recommendation:

- Replace `Task Slices` with `Verifiable Increments`.
- Replace `Files / modules` with `Deliverable components / affected artifacts`.
- Replace verification command defaults with “verification method/evidence”.
- Keep TDD/red-green/refactor as software-mode guidance only.

### P1 — evals still validate software delivery, not solution delivery

**Impact:** Medium. The rewrite changes intended behavior, but the eval corpus still mostly proves the old behavior.

Evidence:

- `delivery/solution-delivery-loop/evals/evals.json:6` says “Use the software delivery loop”.
- `delivery/solution-delivery-loop/evals/evals.json:30` is a multi-project software change.
- `delivery/solution-delivery-loop/evals/trigger-evals.json:3` purpose says “software delivery requests”.
- `delivery/solution-delivery-loop/evals/trigger-evals.json:44`, `:49`, `:59`, `:79`, `:89`, `:99` are software/code-oriented.

Recommendation:

Add evals for non-code deliverables, for example:

- Source-backed market/competitor investigation → `structured-investigation` / `requirement-discovery`.
- Draft a decision memo or proposal from clear requirements → `solution-design`.
- Produce a report increment with citation verification → `implementation-execution`.
- Accept a completed report/plan/investigation using Format Fit → `delivery-acceptance`.
- Negative eval: “format a table / translate docs only” should still not trigger the loop unless delivery decision is involved.

### P2 — skill description quality is inconsistent with this workspace’s skill-authoring rules

**Impact:** Medium-low for functionality, but relevant to triggering accuracy and family consistency.

The workspace’s `writing-skills` guidance says frontmatter descriptions should start with `Use when...` and describe triggering conditions only, not summarize workflow.

Evidence:

- `delivery/structured-investigation/SKILL.md:3` starts with “Universal investigation methodology...” before “Use when...”.
- `delivery/review-feedback/SKILL.md:3` summarizes the workflow before the trigger.
- `delivery/process-distillation/SKILL.md:3` summarizes workflow and behavior extensively before trigger conditions.

Recommendation:

- Rewrite descriptions as trigger-only descriptions.
- Avoid process summaries in descriptions, especially for `review-feedback` and `process-distillation`, because these are likely to shortcut skill loading behavior.

## Positive observations

- All `SKILL.md` files are well under the 500-line guideline.
- `delivery/.claude-plugin/plugin.json`, `evals.json`, and `trigger-evals.json` are valid JSON.
- `delivery/implementation-execution/SKILL.md` is a meaningful improvement over the old software-only loop; the generic five-step increment loop is clear.
- `delivery/delivery-acceptance/SKILL.md` captures the right conceptual model for generic acceptance: evidence depends on deliverable type, and Spec Fit / Format Fit are separate.
- The new format-specific files under `delivery/delivery-acceptance/references/` are a good scaffold for the generic acceptance framework.
- `delivery/structured-investigation/SKILL.md` itself has the right high-level generic principles; the main remaining problem is its support references.

## Suggested fix order

1. **Fix terminology blockers in READMEs and delivery record template**:
   - Software Delivery Loop → Solution Delivery Loop.
   - software work → solution work / deliverable work.
   - Code Fit → Format Fit.
2. **Finish `solution-design` genericization**:
   - Update `SKILL.md`, `solution-design-template.md`, and `plan-template.md` together.
3. **Normalize requirements terminology**:
   - requirements doc by default; PRD only as optional subtype.
4. **Make cold start non-code-safe**:
   - no codebase assumptions unless software deliverable is detected.
5. **Refactor `structured-investigation` references**:
   - generic workflow plus mode-specific code/domain/data references.
6. **Add `structured-investigation` to installation/family/eval metadata**.
7. **Add non-code eval coverage** before marking the rewrite complete.
8. **Clean frontmatter descriptions** for trigger-only SDO consistency.

## Final assessment

Do **not** mark this rewrite complete yet.

It is safe to say the structural rename and first-pass genericization are mostly done, but the family is not yet semantically consistent as `delivery/solution-delivery-loop`. The main risk is that agents using the family will still behave as if this is a software delivery loop because the README, design skill, templates, and evals continue to encode software assumptions.

A focused cleanup pass on the P0/P1 findings above should be enough to get the rewrite to a consistent generic solution-delivery family.
