# Process Distillation Summary

## Metadata

- **Phase analyzed**: historical track analysis (multi-project, post-hoc)
- **Skills involved**: requirement-discovery, solution-design, implementation-execution, delivery-acceptance, software-delivery-loop
- **Review feedback**: N/A (new skills not yet deployed)
- **Fix outcomes**: N/A (analysis only)
- **Analysis date**: 2026-07-06
- **Mode**: user-approval

## Summary

- **Gaps found**: 4
- **Improvements proposed**: 3
- **New skills proposed**: 0
- **Auto-approved**: 0
- **Pending approval**: 3

## Gaps and improvements

### Improvement 1: Progress tracking is a repeated improvisation

| Field | Value |
|---|---|
| **Gap type** | repeated-improvisation |
| **Evidence** | Every project tracked progress differently: myz-track/v23-agentic-loop.md has inline "Progress Update" sections with commit hashes per phase; constype-track/v1-final-status.md has a standalone final status doc; crm/ has PRD version increments; skill-rebuild/ has eval reports. None followed a template. The executor repeatedly invents a progress tracking format. |
| **Proposed change** | Add a lightweight `references/progress-template.md` under `software-delivery-loop/references/`. The template should capture: phase/version completed, items done/blocked/pending, verification evidence per item, decisions made, open questions. One page, not a heavy artifact. Update `software-delivery-loop/SKILL.md` to mention this as an optional track note. |
| **Target** | `software-delivery-loop/references/progress-template.md` (new) + `software-delivery-loop/SKILL.md` "Track documentation" section (update) |
| **Principles satisfied** | scope limited (single reference file), user-centric (observed from real execution), atomic (one template, one job) |
| **Approval** | pending |

### Improvement 2: Change note instruction is too abstract

| Field | Value |
|---|---|
| **Gap type** | missing-guardrail |
| **Evidence** | `implementation-execution/SKILL.md` says "Stop and write a change note before continuing when approved scope, architecture, contract, data model, acceptance criteria, or planned module landing changes." Despite this, NO historical track has a single change note — even when clear scope drifts happened (constype architecture review reduced scope from HFT to MVP; myz v23 PRD scope changed mid-implementation). The instruction exists but lacks concrete "when exactly to stop" signals. |
| **Proposed change** | In `implementation-execution/SKILL.md`, strengthen the change control section with observable signals that trigger the stop: "Stop when: (a) a test expectation changes because behavior differs from PRD, not because implementation is wrong; (b) you need to add a field/column/parameter not in the plan; (c) you skip a non-goal from the PRD; (d) a verification command from the plan no longer makes sense." Also add a one-line note in `delivery-acceptance` acceptance checklist: "Verify change notes exist for any drift from original scope/design." |
| **Target** | `implementation-execution/SKILL.md` "Change control" section; `delivery-acceptance/references/acceptance-checklist.md` "Spec Fit" section |
| **Principles satisfied** | size controlled (add 4-5 lines, not a new document), user-centric (real observed failure), scope limited (tighter guardrails, no new ceremony) |
| **Approval** | pending |

### Improvement 3: Delivery record template exists but has zero adoption

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `delivery-acceptance/references/delivery-record-template.md` exists but ZERO historical tracks created a `delivery-record-*.md`. constype wrote `v1-final-status.md` instead; myz-track wrote inline progress in the track doc; crm has no delivery record. The template is too heavy for what teams actually produce: they write a compact summary with test results and remaining items, not a formal multi-section record. The current template may be intimidating for the agent to generate. |
| **Proposed change** | Add a "lightweight delivery record" option to `delivery-acceptance/SKILL.md` that is: 3-5 bullet points: what changed, what evidence exists, what's deferred. If the agent detects the scope is complex (multiple slices, cross-cutting changes), use the full template. Otherwise, the light variant is sufficient. This matches observed real behavior. |
| **Target** | `delivery-acceptance/SKILL.md` "Delivery record paths" section |
| **Principles satisfied** | user-centric (matches observed real behavior), size controlled (small addition to existing skill), scope limited (delivery record only) |
| **Approval** | pending |

### Improvement 4 (deferred): Track path convention not consistently applied

| Field | Value |
|---|---|
| **Gap type** | no-change |
| **Evidence** | Projects placed track docs at inconsistent paths: constype uses `tracks/constype-track/v1-*.md`, mono-services uses `tracks/mono-services-docs/track/v*.md`, myz uses `tracks/myz-track/v*-*.md`. The SDL convention (`docs/track/<feature>/*.md`) was not used because these projects started before the skill family existed. No change needed — this is an adoption issue, not a skill gap. |
| **Proposed change** | No change. The cold-start guide already covers this. |
| **Target** | — |
| **Approval** | — |

## Skills modified

No skills modified yet — awaiting approval.

## New skills created

None proposed. All gaps are addressable with small changes to existing skills.

## Deferred items

- Creating a standalone `progress-tracking` skill: observed as repeated improvisation, but a single reference template under `software-delivery-loop` is sufficient. If progress tracking grows into its own workflow (e.g., multi-agent progress reporting), extract it later.
- Change note auto-generation: could be a script in the future, but for now better guardrails suffice.

## Recommendations for future cycles

1. After applying these three changes, run the historical track docs again (especially constype and myz) to see if the updated instructions would have produced different artifacts.
2. Consider adding a `code-investigation` integration point in `solution-design` — constype's architecture review showed real value, and `code-investigation` exists but is never referenced from the design phase.