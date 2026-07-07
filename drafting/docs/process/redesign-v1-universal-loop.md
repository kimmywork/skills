---
title: Universal Solution Delivery Loop — Redesign v1
status: design (seeking confirmation)
version: 0.8.0
breaking_change: true
last_updated: 2026-07-07
---

# Universal Solution Delivery Loop — Redesign v1

A single orchestration layer for ALL deliverable types: software, research, documents, reviews, presentations, creative writing, and more.

---

## 1. Design Principles

| # | Principle | Source | Meaning |
|---|---|---|---|
| 1 | **Iron Law: NO PHASE SKIPPING** | academic-pipeline | Each gate must pass before the next phase begins |
| 2 | **Evidence, not confidence** | delivery-acceptance | Acceptance requires fresh verification evidence |
| 3 | **Copilot, not auto** | kong-255-l1 | Human controls every state transition |
| 4 | **Disclosure, not detection** | ARS positioning | Transparency over concealment |
| 5 | **Honest documentation** | artifact-reproducibility | Document configuration, don't claim replay |
| 6 | **Advisory never blocks** | collaboration-depth-rubric | Observational feedback never gates progression |
| 7 | **Anti-sycophancy** | kong-274 | Don't retreat from correct findings under pressure |
| 8 | **Concise output** | kong-274 | Brief but complete; cut redundancy, not substance |
| 9 | **Scope discipline** | academic-paper | Only address approved scope; new scope requires change note |
| 10 | **Process over heroics** | academic-pipeline | Standardized process beats ad-hoc brilliance |

---

## 2. Universal Phases (8 Phases)

```
Sense → Clarify → Shape → Design → Build → Verify → Record → Continue/Stop
  ↑                                                              |
  └──────────────────────────────────────────────────────────────┘
```

| Phase | Name | Purpose | Input | Output |
|---|---|---|---|---|
| 1 | **Sense** | Understand initial context, detect work type, assess available materials | User request, workspace state | Work type assessment, material inventory |
| 2 | **Clarify** | Resolve ambiguity, align intent, confirm routing | Sense output | Confirmed work type + phase plan |
| 3 | **Shape** | Structure intent into scoping document (requirements, research questions, outline, brief) | Clarified intent | Track doc with scope, non-goals, criteria |
| 4 | **Design** | Turn scoping into executable plan (architecture, methodology, outline, review protocol) | Track doc | Solution design / plan |
| 5 | **Build** | Execute the plan (code, write, research, analyze, review) | Solution design | Draft deliverable |
| 6 | **Verify** | Independent quality review (fact-check, code review, peer review, compliance check) | Draft deliverable + rubric | Review report |
| 7 | **Record** | Accept or reject with evidence, record delivery | Review report + verification evidence | Delivery record |
| 8 | **Continue/Stop** | Decide: next increment, iterate, or stop | Delivery record | Next action or completion |

---

## 3. Work Type Taxonomy

### 3.1 Work Types

| Work Type | Description | Example Requests |
|---|---|---|
| `software` | Code delivery: features, fixes, refactors, migrations | "fix the login bug", "add dark mode", "refactor auth module" |
| `research` | Academic/scientific research: literature review, methodology, analysis | "research AI impact on education", "systematic review of X" |
| `document` | Document creation: reports, proposals, briefs, analysis | "write a market analysis", "create a project proposal" |
| `review` | Document/content review: audit, fact-check, compliance, quality | "review this contract", "audit this report", "fact-check this" |
| `technical-review` | Code/architecture review: design review, security audit, code review | "review this PR", "audit the architecture" |
| `investigation` | Deep investigation: root cause, system mapping, reverse engineering | "trace this bug", "map this system", "understand how X works" |
| `tech-doc` | Technical documentation: API docs, guides, manuals, runbooks | "write API docs", "create a setup guide" |
| `presentation` | Presentation creation: slides, talks, demos, pitches | "create slides for this talk", "design a pitch deck" |
| `creative-design` | Creative/design work: UI/UX, branding, visual design, experience design | "design a landing page", "create a brand identity" |
| `creative-writing` | Creative writing: fiction, poetry, scripts, narratives | "write a short story", "draft a screenplay" |
| `report` | Structured report: analysis report, status report, incident report | "write the quarterly report", "create an incident postmortem" |

### 3.2 Phase Skip Table

| Work Type | Sense | Clarify | Shape | Design | Build | Verify | Record | Continue/Stop |
|---|---|---|---|---|---|---|---|---|
| `software` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `research` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `document` | ✓ | ✓ | ✓ | ✓~ | ✓ | ✓ | ✓ | ✓ |
| `review` | ✓ | ✓ | ✓~ | — | ✓ | ✓ | ✓ | ✓ |
| `technical-review` | ✓ | ✓ | ✓~ | — | ✓ | ✓ | ✓ | ✓ |
| `investigation` | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| `tech-doc` | ✓ | ✓ | ✓ | ✓~ | ✓ | ✓ | ✓ | ✓ |
| `presentation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `creative-design` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `creative-writing` | ✓ | ✓ | ✓~ | — | ✓ | ✓ | ✓ | ✓ |
| `report` | ✓ | ✓ | ✓ | ✓~ | ✓ | ✓ | ✓ | ✓ |

Legend: ✓ = required, ✓~ = lightweight/fast-pass, — = skipped

### 3.3 Work Type → Default Behavior Mapping

```
Work Type Detection (Sense phase):
  1. Parse user intent keywords → map to work type
  2. Detect available materials → confirm/suggest work type
  3. If ambiguous → route to Clarify with options

Default Behaviors per Work Type:
  software     → requirements syntax: User Stories + EARS; design: architecture; build: code; verify: tests+lint
  research     → requirements syntax: RQ Brief + FINER; design: methodology; build: research; verify: citation check
  document     → requirements syntax: brief + outline; design: structure; build: writing; verify: fact-check+consistency
  review       → requirements syntax: review scope + criteria; design: — (use review protocol); build: audit; verify: evidence chain
  tech-doc     → requirements syntax: audience + scope; design: outline; build: writing; verify: accuracy check
  presentation → requirements syntax: audience + message; design: narrative arc; build: slides; verify: message clarity
  creative-design → requirements syntax: brief + constraints; design: concept; build: design; verify: criteria check
  creative-writing → requirements syntax: premise + style; design: —; build: writing; verify: criteria check
  investigation → requirements syntax: question + scope; design: —; build: investigation; verify: evidence check
  report       → requirements syntax: brief + audience; design: outline; build: writing; verify: fact+consistency
```

---

## 4. Skill Set (15 Skills)

### 4.1 Skill Inventory

| # | Skill | Phase(s) | Purpose |
|---|---|---|---|
| 1 | `delivery-loop` | All | Top-level orchestrator: triage, routing, state tracking, checkpoints |
| 2 | `intent-clarification` | Clarify | Detect cross-phase materials, resolve ambiguity, structured clarification |
| 3 | `socratic-discovery` | Clarify/Shape | Deep guided exploration when intent is vague |
| 4 | `requirement-discovery` | Shape | Shape intent into structured scoping doc (requirements, brief, RQ) |
| 5 | `structured-investigation` | Shape/Build | Research methodology: primary sources, evidence chains, confidence levels |
| 6 | `solution-design` | Design | Turn scoping into executable plan with verification methods |
| 7 | `implementation-execution` | Build | Execute plan: code, write, research, analyze |
| 8 | `review-feedback` | Verify | Independent quality review with structured feedback |
| 9 | `delivery-acceptance` | Record | Evidence-based acceptance with delivery record |
| 10 | `process-distillation` | Continue/Stop | Learn from execution: improve skills, templates, processes |
| 11 | `document-architecture` | Design | Document/outline structure design for non-software work |
| 12 | `review-protocol` | Build | Domain-specific review execution (contract, compliance, audit) |
| 13 | `fact-verification` | Verify | Claim verification against sources with evidence chains |
| 14 | `style-calibration` | Build | Learn author's writing voice, apply as soft guide |
| 15 | `cross-model-verification` | Verify | Optional second-opinion verification via different model |

### 4.2 Skill Decomposition Diagram

```
delivery-loop (orchestrator)
├── intent-clarification (routing)
├── socratic-discovery (deep exploration)
├── requirement-discovery (scoping)
├── structured-investigation (research)
├── solution-design (planning)
├── document-architecture (doc structure)
├── implementation-execution (execution)
├── review-protocol (review execution)
├── review-feedback (quality review)
├── fact-verification (fact-checking)
├── style-calibration (voice matching)
├── cross-model-verification (second opinion)
├── delivery-acceptance (acceptance)
└── process-distillation (learning)
```

---

## 5. Adaptive Checkpoint System

### 5.1 Checkpoint Types

| Type | When Used | Content |
|---|---|---|
| **FULL** | First checkpoint; after major phase transitions; before finalization | Full deliverable list + decision dashboard + all options |
| **SLIM** | After 2+ consecutive "continue" responses on non-critical phases | One-line status + explicit continue/pause prompt |
| **MANDATORY** | Design review; impl review; acceptance; scope changes | Cannot be skipped; requires explicit user input |

### 5.2 Decision Dashboard (FULL Checkpoints)

```
━━━ Phase [N] [Name] Complete ━━━

Work Type: [detected type]
Phase: [N/8] [name]

Metrics:
- [type-specific metric 1]: [value] [status]
- [type-specific metric 2]: [value] [status]

Deliverables:
- [deliverable 1]
- [deliverable 2]

Flagged: [issues detected, or "None"]

Ready to proceed to [Next Phase]? You can also:
1. View progress (say "status")
2. Adjust settings
3. Pause loop
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.3 Self-Check Questions (at every FULL checkpoint)

Before presenting checkpoint to user:

1. **Quality trajectory**: Is output ≥ quality of previous phase? If declining, PAUSE.
2. **Scope discipline**: Did the phase add content not in the approved scope?
3. **Completeness**: Are all required deliverables present?
4. **Evidence**: Does the output have verifiable evidence for claims?

If ANY answer raises concern, include it in the checkpoint.

### 5.4 Adaptive Rules

1. First checkpoint → always FULL
2. After 2+ consecutive "continue" → SLIM (with awareness prompt after 4+)
3. Design/Review/Acceptance gates → always MANDATORY
4. All other phases → start FULL, downgrade to SLIM if user says "continue"

---

## 6. Handoff Schemas

### 6.1 Universal Handoff Contract

Every phase-to-phase handoff MUST include:

```yaml
handoff:
  from_phase: <phase name>
  to_phase: <phase name>
  work_type: <detected type>
  deliverables: [list of artifacts]
  verification_status: VERIFIED | UNVERIFIED | STALE
  version_label: <version>
  content_hash: sha256:...
  upstream_dependencies: [list of prior artifact versions]
  change_notes: [any scope/design/contract changes]
```

### 6.2 Phase-Specific Schemas

#### Sense → Clarify

```yaml
sense_output:
  detected_work_type: <work_type>
  confidence: high | medium | low
  available_materials: [list]
  material_phases: [which phases the materials belong to]
  ambiguous: boolean
  clarification_needed: [specific questions]
```

#### Clarify → Shape

```yaml
clarified_intent:
  confirmed_work_type: <work_type>
  phase_plan: [phases to execute, with skip table applied]
  user_preferences: {mode: full | quick | guided, ...}
  constraints: [time, scope, quality constraints]
```

#### Shape → Design

```yaml
scoping_output:
  work_type: <work_type>
  scope: {in_scope: [], out_of_scope: []}
  users: [target audience/personas]
  requirements: [structured requirements]
  acceptance_criteria: [verifiable criteria]
  verification_plan: [how to verify each criterion]
  risks: [identified risks]
  open_questions: [unresolved items]
```

#### Design → Build

```yaml
design_output:
  work_type: <work_type>
  design_principles: [principles for this work]
  approach: {chosen: <description>, rejected: [], deferred: []}
  deliverable_structure: [components/modules/sections]
  contracts: [interfaces/data models/text structures]
  verification_methods: [per-increment verification]
  increments: [ordered list of work increments]
  acceptance_mapping: [increment → criteria mapping]
```

#### Build → Verify

```yaml
build_output:
  work_type: <work_type>
  deliverable: <the artifact produced>
  deliverable_path: <file path or location>
  completion_status: complete | partial | blocked
  verification_evidence: [evidence produced during build]
  scope_drift: [any drift detected]
  known_limitations: [items not addressed]
```

#### Verify → Record

```yaml
verify_output:
  verdict: PASS | CONDITIONAL_PASS | FAIL | NEEDS_REVISION
  issues: [structured issue list]
  quality_dimensions: {dimension: score}
  recommendation: proceed | revise | rollback
  confidence: high | medium | low
```

#### Record → Continue/Stop

```yaml
delivery_record:
  verdict: delivered | partial | blocked | needs-user-review | rolled-back
  acceptance_evidence: [evidence for verdict]
  scope_coverage: {total: N, completed: M}
  deliverables: [final deliverable list]
  next_action: continue-increment | iterate | stop
  process_observations: [what worked, what didn't]
```

---

## 7. Intent Clarification Protocol

### 7.1 Trigger Conditions

| Condition | Action |
|---|---|
| User provides clear trigger keyword for one work type | Route directly |
| User provides materials spanning ≥ 2 phases | **Clarify** with options |
| User provides no materials and no clear request | **Clarify** with options |
| User uses `[direct-mode]` prefix | Strip prefix, route directly |

### 7.2 Phase Detection Heuristics

| Artifact Indicator | Likely Phase |
|---|---|
| Empty request, vague idea | Sense/Clarify |
| User stories, requirements, brief | Shape |
| Architecture, outline, methodology | Design |
| Code, draft, research findings | Build |
| Review comments, test results | Verify |
| Delivery record, acceptance | Record |

### 7.3 Clarification Template

```
I see you've provided <materials summary>. To route correctly, which workflow do you want?

(a) **Full pipeline** — from materials through to complete deliverable. Use `delivery-loop` full mode.
(b) **<Phase-specific 1>** — <description>. Use `<skill>`.
(c) **<Phase-specific 2>** — <description>. Use `<skill>`.
(d) **Something else** — tell me what you're trying to do.

Pick a-d, or describe the target deliverable. For direct agent dispatch, prefix with `[direct-mode]`.
```

---

## 8. Mode Spectrum

### 8.1 Spectrum Definition

| Mode | Template Load | When to Use | Example |
|---|---|---|---|
| **Fidelity** | Heavy | Predictable output, checklist-driven | Contract review, citation check, format conversion |
| **Balanced** | Medium | Default, structured but flexible | Feature implementation, report writing, investigation |
| **Originality** | Light | Exploratory, creative, guided thinking | Socratic discovery, creative writing, architecture design |

### 8.2 Work Type → Default Mode

| Work Type | Default Mode | Override Available |
|---|---|---|
| `software` | Balanced | → Fidelity for fixes; → Originality for architecture |
| `research` | Balanced | → Fidelity for systematic review; → Originality for Socratic |
| `document` | Balanced | → Fidelity for compliance docs; → Originality for creative briefs |
| `review` | Fidelity | Always checklist-driven |
| `technical-review` | Fidelity | Always rubric-driven |
| `investigation` | Originality | Always exploratory |
| `tech-doc` | Balanced | → Fidelity for API reference; → Originality for guides |
| `presentation` | Balanced | → Originality for creative pitches |
| `creative-design` | Originality | Always exploratory |
| `creative-writing` | Originality | Always exploratory |
| `report` | Balanced | → Fidelity for compliance reports |

---

## 9. Review Protocol (Universal)

### 9.1 Review Types by Work Type

| Work Type | Review Type | Reviewers | Output |
|---|---|---|---|
| `software` | Code review | reviewer (AI or human) | Issues + suggestions |
| `research` | Peer review simulation | 5 reviewer personas | Review report + editorial decision |
| `document` | Editorial review | EIC + reviewers | Issues + revision roadmap |
| `review` | Quality audit | Self-review + evidence check | Audit report |
| `technical-review` | Architecture/security review | Specialist reviewers | Findings + recommendations |
| `investigation` | Multi-perspective review | Technical + domain + feasibility | Confidence assessment |
| `tech-doc` | Accuracy + usability review | Technical + audience review | Issues + improvements |
| `presentation` | Message + delivery review | Content + design review | Feedback + revision plan |
| `creative-design` | Criteria-based review | Against brief + constraints | Feedback + iteration plan |
| `creative-writing` | Craft review | Style + structure + impact | Feedback + revision notes |
| `report` | Fact + consistency review | Accuracy + completeness check | Issues + corrections |

### 9.2 Universal Review Structure

Every review produces:

```yaml
review_output:
  review_type: <type>
  dimensions: [list of dimensions reviewed]
  scores: {dimension: score}
  issues: [structured issue list with severity + evidence]
  strengths: [what works well]
  recommendations: [prioritized improvements]
  verdict: pass | conditional_pass | needs_revision | fail
```

### 9.3 Ground-Truth Isolation

```
Layer 1 — Raw Inputs: user request, source material, unverified claims
Layer 2 — Verified Artifacts: output that passed review
Layer 3 — Ground Truth: acceptance criteria, review rubrics, scoring keys

Rules:
- Builder (L1/L2) never sees rubric (L3) before producing output
- Reviewer sees rubric (L3) + output → produces natural language feedback
- Builder sees output + feedback → fixes without seeing rubric
- data_access_level declared in each SKILL.md frontmatter
```

---

## 10. Iron Rules

| # | Rule | Scope | Enforcement |
|---|---|---|---|
| IR-1 | **NO PHASE SKIPPING** | All phases | Gate check before each phase |
| IR-2 | **NO DELIVERY WITHOUT EVIDENCE** | Record phase | Fresh verification evidence required |
| IR-3 | **NO AUTONOMOUS STATE TRANSITION** | All phases | User confirmation at MANDATORY checkpoints |
| IR-4 | **NO SCOPE CREEP** | Build phase | Change note required for any scope addition |
| IR-5 | **NO RUBRIC LEAKAGE** | Verify → Build | Ground-truth isolation enforced |
| IR-6 | **NO SYCOPHANTIC RETREAT** | Verify phase | Evidence-standard: pressure ≠ evidence |
| IR-7 | **NO CONCEALED DRIFT** | Build phase | Write change note before any undiscussed change |
| IR-8 | **NO PARTIAL CLAIMS** | Record phase | All criteria must be verified or explicitly deferred |

---

## 11. Anti-Patterns (Universal)

| # | Anti-Pattern | Why It Fails | Correct Behavior |
|---|---|---|---|
| AP-1 | **Skipping to Build before Shape/Design** | Unscoped work produces wrong deliverable | Complete Shape + Design before Build |
| AP-2 | **Accepting confidence as evidence** | "Looks good" ≠ verified | Fresh verification evidence required |
| AP-3 | **Silent scope addition** | Undocumented drift compounds | Change note before any scope addition |
| AP-4 | **One-reviewer review** | Single perspective misses blind spots | Multi-perspective or cross-check review |
| AP-5 | **Vague acceptance criteria** | "Better UX" is not verifiable | Specific, measurable, testable criteria |
| AP-6 | **Skipping the challenge step** | First design is rarely best | Challenge: over-engineering, tech sprawl, scope |
| AP-7 | **Monolithic requirements** | Too large to verify or implement | Split into independently verifiable stages |
| AP-8 | **Documentation as delivery** | Docs without working code/design is incomplete | Documentation supplements, not replaces |
| AP-9 | **Re-inventing the wheel** | Ignoring existing patterns/conventions | Check existing conventions first |
| AP-10 | **Heroics over process** | Works once, fails at scale | Standardized process with escalation paths |

---

## 12. Failure Paths

| Failure Scenario | Trigger | Recovery |
|---|---|---|
| RQ/concept cannot converge | Clarify exceeds 5 rounds | Provide 3 candidate directions or suggest structured investigation |
| Design infeasible | Solution design shows Redesigned | Return to Shape, suggest alternative approaches |
| Build exceeds scope | Increment affects too broad a scope | Pause, write change note, split or narrow scope |
| Verification finds critical issue | Critical issue in review | Must fix before proceeding; rollback if needed |
| User abandons mid-process | Explicit stop request | Save progress, provide re-entry path |
| Cross-phase confusion | Materials span multiple phases | Intent clarification with structured options |
| Quality regression | Output quality < previous phase | PAUSE, reload core principles, reassess |
| Stuck in revision loop | 3+ revision rounds without convergence | Suggest stopping (converged) or escalating to user |

---

## 13. Implementation Plan

### Phase 1: Core Skills (P0)

| Skill | Action | Effort |
|---|---|---|
| `delivery-loop` | Rewrite SKILL.md with universal phases + adaptive checkpoints | Large |
| `intent-clarification` | New skill: routing + clarification protocol | Medium |
| `requirement-discovery` | Generalize for all work types | Medium |
| `solution-design` | Generalize + add document-architecture patterns | Medium |
| `implementation-execution` | Generalize for all build types | Medium |
| `review-feedback` | Add ground-truth isolation + multi-perspective review | Medium |
| `delivery-acceptance` | Add evidence chain + delivery record schema | Small |

### Phase 2: Supporting Skills (P1)

| Skill | Action | Effort |
|---|---|---|
| `socratic-discovery` | New skill: 5-layer guided exploration | Medium |
| `structured-investigation` | Minor updates (already good) | Small |
| `process-distillation` | Minor updates | Small |
| `handoff-schemas` | New reference: all handoff data contracts | Medium |
| `mode-spectrum` | New reference: fidelity/originality mapping | Small |
| `anti-patterns-catalog` | New reference: unified anti-patterns | Small |

### Phase 3: Advanced Features (P2)

| Skill | Action | Effort |
|---|---|---|
| `fact-verification` | New skill: claim verification with evidence chains | Medium |
| `style-calibration` | New skill: author voice learning | Medium |
| `cross-model-verification` | New skill: second-opinion verification | Large |
| `review-protocol` | New skill: domain-specific review execution | Medium |
| `collaboration-depth-rubric` | New reference: 4-dimension observation | Medium |
| `compliance-protocol` | New reference: override ladder + history | Medium |

---

## 14. Migration Path

### Breaking Changes

1. **SKILL.md files**: All existing SKILL.md files will be rewritten
2. **Phase names**: Some phase names change (e.g., Build replaces part of implementation-execution)
3. **Track doc format**: New Material Passport fields in frontmatter
4. **Review format**: New structured review output format

### Backward Compatibility

- `loop-state.md` format: **compatible** (no change needed)
- Track doc naming (`<YYYY-MM-DD-NN>-<name>`): **compatible**
- `docs/track/` directory structure: **compatible**
- Existing delivery records: **compatible** (read-only)

### Migration Steps

1. Write new SKILL.md files (all 15 skills)
2. Write new reference documents (handoff-schemas, mode-spectrum, etc.)
3. Update AGENTS.md if needed
4. Test with a sample work item of each type
5. Archive old SKILL.md files

---

## 15. Open Questions

| # | Question | Options | Recommendation |
|---|---|---|---|
| Q1 | Should `document-architecture` be a separate skill or merged into `solution-design`? | Separate / merged | Separate — document structure design is distinct from software architecture |
| Q2 | Should `review-protocol` be a separate skill or part of `review-feedback`? | Separate / merged | Separate — review execution is distinct from review evaluation |
| Q3 | How to handle work types that don't fit neatly (e.g., "help me think about X")? | Map to investigation / create "thinking" type | Map to investigation with Socratic mode |
| Q4 | Should style-calibration be opt-in or always available? | Opt-in / always | Opt-in — not all work types need it |
| Q5 | Should cross-model-verification be built into review-feedback or standalone? | Built-in / standalone | Standalone — it's an optional enhancement layer |
| Q6 | How to handle multi-deliverable work (e.g., "write a paper AND create slides")? | Single loop with multiple outputs / separate loops | Single loop with multiple output tracks |
| Q7 | Should the loop support concurrent phases (e.g., parallel Build tracks)? | Yes / no | Yes — for multi-deliverable work, parallel Build is valuable |
| Q8 | How aggressive should the skip table be? (e.g., should creative-writing skip Design entirely?) | Aggressive skipping / lightweight fast-pass | Lightweight fast-pass — even creative work benefits from brief structure |

---

## 16. Verification

After implementation:

1. **Phase coverage**: Every work type can complete all required phases
2. **Skip table accuracy**: Skipped phases are truly unnecessary for that work type
3. **Handoff integrity**: Every handoff follows the schema; no data loss between phases
4. **Checkpoint effectiveness**: MANDATORY checkpoints catch real issues; FULL dashboards are informative
5. **Anti-pattern prevention**: Each anti-pattern has a detection mechanism or gate check
6. **Failure path coverage**: Every failure scenario has a documented recovery path
7. **Ground-truth isolation**: Review rubrics never appear in builder context before output
8. **Iron rule enforcement**: Every IR has a gate check or structural guarantee
