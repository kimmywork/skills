# Drafting Coverage Matrix

Status: active verification artifact
Date: 2026-07-07

Coverage statuses:
- Covered: implemented in drafting skill/reference with usable instructions.
- Partial: concept exists but execution semantics are not complete.
- Deferred: intentionally not implemented because it is low-value, tool-specific, or outside bundle scope.

## Delivery framework coverage

| Source capability | Drafting target | Status | Evidence / notes | Follow-up |
|---|---|---:|---|---|
| End-to-end loop routing | `drafting-loop/SKILL.md`, `state-machine.md` | Covered | 8 phases, legal/illegal transitions, material dependencies | Keep semantic checklist current |
| No phase skipping | `iron-rules.md`, `state-machine.md` | Covered | IR-1 plus illegal transitions | None |
| Review after each phase | `phase-review-and-process-audit.md`, `quality-review` | Covered | Phase review insertion and advancement rule | None |
| Process audit after review cycles | `phase-review-and-process-audit.md`, `distillation` | Covered | Process audit triggers and distillation handoff | None |
| Track docs | `track-document-structure.md`, `track_parser.py` | Covered | parent/stage/standalone and parser commands | None |
| Multi-stage scope-map | `multi-stage-tracks.md`, parser | Covered | parent derives status from child records | None |
| Requirement syntax | `scope-shaping/references/requirement-syntax.md` | Covered | User Story, EARS, Given/When/Then | None |
| Requirement scope templates | `scope-templates.md` | Covered | kind-specific scope templates | None |
| Design feasibility pre-screen | `dependency-and-contracts.md` | Covered | Feasible/Moderate/Redesigned | None |
| Contract-first design | `dependency-and-contracts.md`, `blueprint-templates.md` | Covered | contracts, dependents, strategies | None |
| Dependency graph | `dependency-and-contracts.md` | Covered | increment predecessor fields | None |
| Software execution mode | `software-mode.md` | Covered | TDD, E2E/integration seam, contract changes | None |
| Increment evidence record | `increment-record.md` | Covered | commands/checks/failures/drift | None |
| Change notes | `change-note-template.md` | Covered | affected phase, criteria, options, approval rule | None |
| Review-feedback issue schema | `issue-taxonomy.md` | Covered | origin phase, severity, type, evidence, resolution | None |
| Review rollback routing | `review-routing.md` | Covered | fix-in-place vs rollback to earliest phase | None |
| Multi-pass review | `review-routing.md` | Covered | Accuracy, Validity, Consistency | None |
| Delivery acceptance | `acceptance-gate`, `delivery-record-template.md` | Covered | criteria/evidence/verdict mapping | None |
| Format-specific acceptance | `format-*.md` | Covered | software/report/plan/investigation | None |
| Structured investigation | `deep-research`, `investigation-workflow.md` | Covered | quick/full/systematic, trace chain, confidence labels | None |
| Process distillation gap dimensions | `distillation-template.md`, `distillation/SKILL.md` | Covered | coverage gap, false guidance, missing guardrail, repeated improvisation, atomic extraction, context overhead, trigger misfire | None |
| Rename-specific checklist | none | Deferred | not generally valuable for drafting-loop; use only if rename workflow recurs | Add later only with evidence |
| Subagent roles | none | Deferred | framework must stay agent-neutral | Do not add runtime dependency |

## Redesign v2 coverage

| Design requirement | Drafting target | Status | Notes |
|---|---|---:|---|
| Work kinds, not deliverable types | `drafting-loop/SKILL.md`, `design-spec.md` | Covered | Crafting/Composing/Evaluating/Investigating/Creating |
| 8 universal phases | `drafting-loop/SKILL.md`, `state-machine.md` | Covered | Sense through Continue/Stop |
| Adaptive checkpoints | `checkpoint-protocol.md` | Covered | FULL/SLIM/MANDATORY and phase-review gate |
| Handoff envelope and payloads | `handoff-schemas.md` | Covered | phase review and process audit added |
| Ground-truth isolation | `ground-truth-isolation.md` | Covered | L1/L2/L3 rules and single-agent mode |
| Iron rules | `iron-rules.md` | Covered | expanded to include phase review and process theater |
| Failure paths | `failure-paths.md` | Covered | rollback targets and recovery record |
| Multi-stage / multi-deliverable | `multi-stage-tracks.md` | Covered | parent/stage, child records, parallel rules |
| Compliance gate | `compliance-gate`, `integrity-protocol.md` | Covered | override ladder and integrity failures |
| Cross-validation | `cross-validation/SKILL.md`, `cross-validation/references/cross-validation-protocol.md` | Covered | agent-neutral validation modes, perspectives, comparison, divergence rules; concrete runner deferred | None |
| Style calibration unified system | `style-calibration` refs | Covered | extraction, validation, application, Chinese rules |

## Style-extraction coverage

| Source capability | Drafting target | Status | Notes |
|---|---|---:|---|
| Input requirements | `extraction-workflow.md` | Covered | sample count, length, genre, non-author material |
| Quantitative baseline | `extraction-workflow.md`, `output-template.md` | Covered | sentence, paragraph, function word, punctuation |
| Function words as style DNA | `computational-stylistics.md` | Covered | priority and stability hierarchy |
| Punctuation density | `computational-stylistics.md`, `output-template.md` | Covered | density and pattern fields |
| Surface language features | `extraction-workflow.md` | Covered | vocabulary/function words/sentences/punctuation/rhetoric |
| Structure and narrative | `extraction-workflow.md`, `output-template.md` | Covered | openings/body/closing/transitions |
| Tone and thinking patterns | `extraction-workflow.md`, `output-template.md` | Covered | text-derived only |
| Taboos and anti-rules | `extraction-workflow.md`, `output-template.md` | Covered | evidence basis and table |
| Positive/negative examples | `extraction-workflow.md`, `output-template.md` | Covered | both required |
| Self-check | `extraction-workflow.md` | Covered | evidence, executable rules, stability |
| External calibration | `calibration-protocol.md` | Covered | leave-one-out and cross-genre |
| Chinese function words | `chinese-style-rules.md` | Covered | Chinese token list preserved |
| Chinese output section names | `chinese-style-rules.md` | Covered | mapping preserved |
| Accuracy tips | `accuracy-tips.md` | Covered | batch extraction, quantify first, differentiation |

## Selected reference-skills absorption

| Source area | Drafting target | Status | Notes |
|---|---|---:|---|
| Academic pipeline state machine | `state-machine.md` | Covered | adapted to universal phases |
| Pipeline transition reinforcement | `transition-reinforcement.md` | Covered | universal transition reminders |
| Claim verification | `claim-verification-protocol.md` | Covered | extraction, tracing, cross-reference, verdicts |
| Integrity failure modes | `integrity-protocol.md` | Covered | 7 failure modes adapted |
| Document review schemas | `audit-state-schema.md` | Covered | section/claim/issue/root issue |
| Source quality hierarchy | `source-quality-hierarchy.md` | Covered | levels and grading dimensions |
| Methodology patterns | `methodology-patterns.md` | Covered | systematic, case study, RCA, system mapping |
| Two-stage peer review | `quality-review/references/two-stage-review.md` | Covered | full review, revision roadmap, verification review, and functional persona lenses | None |
| Passport reset boundary | `drafting-loop/references/resume-ledger.md` | Covered | generalized append-only resume ledger without runtime dependency | None |
| Annotation scripts | none | Deferred | document-specific tooling outside universal framework | Add only as a document-review specialization |

## SKILL.md coverage verification

This section verifies that each `SKILL.md` itself carries enough routing and execution intent, while detailed semantics live in references.

| Skill | Required SKILL.md coverage | Status | Reference depth |
|---|---|---:|---|
| `drafting-loop` | phases, work kinds, skip table, checkpoints, state/output, phase-review requirement | Covered | state machine, handoff, checkpoint, multi-stage, phase review |
| `intent-routing` | kind detection, material phase detection, direct-mode, clarification output | Covered | uses handoff/mode refs |
| `guided-inquiry` | 5-layer inquiry, convergence cap, candidate scopes | Covered | no extra reference needed |
| `scope-shaping` | materials inventory, overlap check, stage split, criteria, verification plan | Covered | scope templates, requirement syntax, multi-stage |
| `blueprinting` | feasibility, contracts, challenge pass, dependency increments, approval gate | Covered | blueprint templates, dependency/contracts |
| `plan-execution` | preconditions, increment loop, change notes, software-mode pointer | Covered | increment record, software mode |
| `audit-trail` | section/claim/issue audit flow, fact/compliance handoff, verdict | Covered | audit-state schema |
| `quality-review` | freeze artifact, cumulative review, multi-pass review, issue tagging, routing, two-stage review | Covered | feedback template, issue taxonomy, review routing, two-stage review |
| `fact-verification` | claim extraction, source tracing, cross-check, numerical exactness, verdicts | Covered | claim verification protocol |
| `style-calibration` | extract/validate/apply modes, quantitative-first, evidence, Chinese/style refs | Covered | computational stylistics, workflow, template, Chinese rules, calibration, tips |
| `cross-validation` | validation modes, perspectives, comparison, divergence rules, independence limitation | Covered | cross-validation protocol; concrete cross-model runner intentionally absent |
| `acceptance-gate` | evidence acceptance, spec/format fit, verdicts, delivery record | Covered | checklist, format refs, record template |
| `distillation` | process audit triggers, gap dimensions, option selection, bundle checks | Covered | distillation template |
| `compliance-gate` | dimensions, integrity checks, override ladder, disclosure | Covered | integrity protocol |
| `deep-research` | quick/formal research, source plan, trace chain, confidence labels | Covered | investigation workflow, source hierarchy, methodology patterns |

## Not hard-inserted / deferred list

These are intentionally not forced into the framework now. Add only if future evidence shows they are valuable and sufficiently general.

| Capability | Source | Reason not hard-inserted | Possible future home |
|---|---|---|---|
| Rename-specific checklist | delivery/process-distillation | Useful for rename tasks, not universal process improvement. | `distillation/references/rename-checklist.md` only if rename failures recur |
| Subagent role orchestration | delivery skills / pi runtime | Violates agent-neutral goal; runtime-specific. | Optional runtime adapter, not core skill |
| Concrete cross-model runner | academic cross-validation scripts | Runtime/tool-specific; current skill remains protocol-level. | `cross-validation/scripts/` if tool support is standardized |
| Full domain-specific peer-review persona panel | academic-paper-reviewer | Functional two-stage review and generic lenses are included; domain-specific academic personas are not universal. | academic specialization if needed |
| Runtime-specific passport/reset commands | academic-pipeline | General resume ledger is included; runtime command semantics are not universal. | runtime adapter if needed |
| PDF/DOCX/PPTX/XLSX annotation scripts | document-review | Document-type tooling, not universal framework. | separate document-review specialization |
| Web-search agent modules | Deep-Research-skills | Tool/runtime-specific; keep source-quality and methodology only. | `deep-research/scripts/` or adapter if search tooling is standardized |
| APA/IRB/venue-specific academic rules | academic-paper/deep-research | Domain-specific and would bloat universal drafting. | academic specialization bundle |

## Current semantic gaps

1. Concrete cross-model runner is not included; agent-neutral cross-validation protocol is included.
2. Domain-specific peer-review personas are not included; generic two-stage review and functional lenses are included.
3. Runtime-specific passport commands are not included; generalized resume ledger is included.
4. Document annotation workflows are intentionally not included.

These gaps are acceptable unless the framework needs those concrete modes.
