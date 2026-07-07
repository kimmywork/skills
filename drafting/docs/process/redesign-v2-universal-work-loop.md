---
title: Drafting Loop — Universal Work Orchestration
status: design (confirmed)
version: 1.0.0
breaking_change: true
last_updated: 2026-07-07
---

# Drafting Loop — Universal Work Orchestration

A single orchestration layer for ALL kinds of knowledge work: crafting, composing, evaluating, investigating, and creating.

---

## 1. Design Principles

| # | Principle | Source | Meaning |
|---|---|---|---|
| 1 | **No phase skipping** | academic-pipeline | Each gate must pass before the next phase begins |
| 2 | **Evidence, not confidence** | delivery-acceptance | Acceptance requires fresh verification evidence |
| 3 | **Human owns state** | kong-255-l1 | Human controls every state transition |
| 4 | **Transparency over concealment** | ARS positioning | Disclosure, not detection |
| 5 | **Honest documentation** | artifact-reproducibility | Document configuration, don't claim replay |
| 6 | **Advisory never blocks** | collaboration-depth-rubric | Observational feedback never gates progression |
| 7 | **Pressure is not evidence** | kong-274 | Don't retreat from correct findings under pressure |
| 8 | **Concise but complete** | kong-274 | Cut redundancy, not substance |
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
| 1 | **Sense** | Understand initial context, detect work kind, assess materials | User request, workspace | Kind assessment, material inventory |
| 2 | **Clarify** | Resolve ambiguity, align intent, confirm routing | Sense output | Confirmed kind + phase plan |
| 3 | **Shape** | Structure intent into scoping artifact | Clarified intent | Scope doc (requirements, brief, RQ, premise) |
| 4 | **Design** | Turn scope into executable plan | Scope doc | Blueprint (architecture, methodology, outline, protocol) |
| 5 | **Build** | Execute the plan | Blueprint | Draft deliverable |
| 6 | **Verify** | Independent quality review | Draft + rubric | Review report |
| 7 | **Record** | Accept or reject with evidence | Review + evidence | Delivery record |
| 8 | **Continue/Stop** | Decide: next increment, iterate, or stop | Delivery record | Next action or completion |

---

## 3. Work Kinds

### 3.1 Kinds (not types)

Work kinds describe the **primary cognitive mode**, not the specific deliverable. A single request may involve multiple kinds.

| Kind | Primary Mode | Description | Examples |
|---|---|---|---|
| **Crafting** | Making | Producing artifacts from requirements: code, prototypes, systems, infrastructure, configurations | Build a feature, fix a bug, create a tool, set up CI/CD, design a system |
| **Composing** | Synthesizing | Creating structured outputs from information: documents, reports, presentations, documentation, proposals | Write a report, create slides, draft a proposal, write API docs, write a postmortem |
| **Evaluating** | Assessing | Examining existing work against criteria: reviews, audits, fact-checks, compliance checks, quality assessments | Review a PR, audit a contract, fact-check claims, check compliance, assess quality |
| **Investigating** | Exploring | Researching, discovering, analyzing: root cause analysis, literature review, market research, system mapping | Trace a bug, research a topic, analyze a system, map dependencies, do due diligence |
| **Creating** | Imagining | Open-ended creative work: ideation, concept design, fiction, poetry, scripts, visual design, experience design | Design a concept, write a story, create a brand, draft a screenplay, design an experience |

### 3.2 Kind Detection (Sense Phase)

```
1. Parse user intent → extract action verbs + object
   - "build/make/fix/implement/set up/configure" → Crafting
   - "write/draft/compose (docs/report/slides/proposal/API docs)" → Composing
   - "review/audit/check/verify/assess/evaluate/fact-check" → Evaluating
   - "research/investigate/trace/analyze/map/understand/due diligence" → Investigating
   - "design/ideate/imagine/create (fiction/story/brand/screenplay/concept)" → Creating

   Disambiguation for "create":
   - "create + code/tool/system/config" → Crafting
   - "create + document/report/slides/docs" → Composing
   - "create + fiction/story/poem/screenplay/brand/concept" → Creating
   - Ambiguous "create X" → route to Clarify

2. Detect multi-kind requests
   - Multiple kinds detected → present options:
     (a) Full loop covering all kinds sequentially
     (b) Prioritize one kind (recommend primary)
     (c) Separate loop per kind
   - "research AND write up" → Investigating (primary) + Composing (secondary)
   - "review AND fix" → Evaluating (primary) + Crafting (secondary)

3. Detect available materials → confirm or adjust kind
   - Code files + tests → likely Crafting
   - Existing documents → could be Composing (extend) or Evaluating (review)
   - Research sources → Investigating
   - Blank canvas → Creating or Composing

3. If ambiguous → route to Clarify with options
```

### 3.3 Phase Skip Table

| Kind | Sense | Clarify | Shape | Design | Build | Verify | Record | C/S |
|---|---|---|---|---|---|---|---|---|
| **Crafting** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Composing** | ✓ | ✓ | ✓ | ✓~ | ✓ | ✓ | ✓ | ✓ |
| **Evaluating** | ✓ | ✓ | ✓~ | — | ✓ | ✓ | ✓ | ✓ |
| **Investigating** | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| **Creating** | ✓ | ✓ | ✓~ | — | ✓ | ✓ | ✓ | ✓ |

Legend: ✓ = required, ✓~ = lightweight fast-pass, — = skipped

**Fast-pass rules:**
- Composing Design: outline/structure is brief, not a full architecture document
- Evaluating Shape: review scope + criteria only, no requirements engineering
- Investigating Design: methodology is implied by the question, not separately planned
- Creating Shape: premise + constraints only, no detailed structure plan

### 3.4 Kind → Default Behaviors

```
Crafting:
  Scope syntax: User Stories + acceptance criteria + constraints
  Design: architecture, interfaces, data models, increment plan
  Build: code, tests, configs
  Verify: tests pass, lint clean, code review, integration check
  Mode: Balanced (→ Fidelity for fixes, → Originality for architecture)

Composing:
  Scope syntax: brief + audience + message + structure outline
  Design: document architecture, section flow, evidence map
  Build: writing, formatting, citation
  Verify: fact-check, consistency, readability, completeness
  Mode: Balanced (→ Fidelity for compliance docs, → Originality for creative briefs)

Evaluating:
  Scope syntax: review scope + criteria + severity definitions
  Design: — (use review protocol)
  Build: audit, fact-check, evidence collection
  Verify: evidence chain, cross-reference, confidence tagging
  Mode: Fidelity (checklist-driven, always)

Investigating:
  Scope syntax: question + scope boundaries + source types
  Design: — (methodology implied by question type)
  Build: source gathering, analysis, synthesis
  Verify: evidence chain, confidence levels, multi-perspective check
  Mode: Originality (exploratory, always)

Creating:
  Scope syntax: premise + constraints + style direction + reference works
  Design: — (concept emerges during build)
  Build: ideation, drafting, iteration
  Verify: against brief/constraints, style consistency, impact assessment
  Mode: Originality (exploratory, always)
```

---

## 4. Skill Set

### 4.1 Naming Philosophy

Skill names describe **what the skill does**, not which deliverable it produces. No skill is named after a specific work type (no "code-review", "paper-writer", etc.). Names are short, verb-like, and universal.

### 4.2 Skill Inventory

| # | Skill Name | Phase(s) | What It Does |
|---|---|---|---|
| 1 | **drafting-loop** | All | Orchestrator: triage, routing, state tracking, checkpoints |
| 2 | **intent-routing** | Clarify | Detect cross-material routing, resolve ambiguity |
| 3 | **guided-inquiry** | Clarify/Shape | 5-layer Socratic dialogue for vague intentions |
| 4 | **scope-shaping** | Shape | Turn intent into structured scope artifact |
| 5 | **deep-research** | Shape/Build | Systematic investigation: sources, evidence, confidence |
| 6 | **blueprinting** | Design | Turn scope into executable plan with verification |
| 7 | **plan-execution** | Build | Produce the deliverable (code, text, analysis, design) |
| 8 | **audit-trail** | Build | Domain-specific evaluation execution (contract, compliance, review) |
| 9 | **quality-review** | Verify | Independent quality review with structured feedback |
| 10 | **fact-verification** | Verify | Fact-check claims against sources with evidence chains |
| 11 | **style-calibration** | Build | Extract + apply author's writing voice (absorbs style-extraction) |
| 12 | **cross-validation** | Verify | Optional cross-model or cross-perspective verification |
| 13 | **acceptance-gate** | Record | Evidence-based acceptance with delivery record |
| 14 | **distillation** | C/S | Learn from execution: improve processes, templates, skills |
| 15 | **compliance-gate** | Verify | Override ladder, disclosure, append-only compliance history |

### 4.3 Skill Decomposition

```
drafting-loop (orchestrator)
├── intent-routing (routing)
├── guided-inquiry (Socratic deep dive)
├── scope-shaping (requirements/brief/RQ)
├── deep-research (research/investigation)
├── blueprinting (architecture/methodology/outline)
├── plan-execution (produce deliverable)
├── audit-trail (domain-specific evaluation)
├── quality-review (quality assessment)
├── fact-verification (fact checking)
├── style-calibration (style extract + apply)
├── cross-validation (cross-model verification)
├── acceptance-gate (delivery gate)
├── distillation (learning)
└── compliance-gate (override + disclosure)
```

### 4.4 Relationship to Existing Skills

| New Skill | Absorbs/Replaces | Notes |
|---|---|---|
| `drafting-loop` | `solution-delivery-loop` | Universal orchestration |
| `intent-routing` | (new) | From academic-pipeline's intent clarification protocol |
| `guided-inquiry` | (new) | From academic-research-skills' Socratic mentor |
| `scope-shaping` | `requirement-discovery` | Generalized for all kinds |
| `deep-research` | `structured-investigation` | Enhanced with academic-research methodology |
| `blueprinting` | `solution-design` | Generalized: includes doc-architecture, methodology design |
| `plan-execution` | `implementation-execution` | Generalized: code, writing, research, analysis |
| `audit-trail` | (new) | From document-review's 6-phase pipeline |
| `quality-review` | `review-feedback` | Enhanced with multi-perspective review |
| `fact-verification` | (new) | From document-review's claim/issue schema |
| `style-calibration` | `style-extraction` (utility) + `style-calibration` (ARS) | Unified: extract from samples + apply during writing |
| `cross-validation` | (new) | From ARS cross-model verification |
| `acceptance-gate` | `delivery-acceptance` | Enhanced with evidence chain |
| `distillation` | `process-distillation` | Enhanced with ARS process documentation |
| `compliance-gate` | (new) | From ARS compliance checkpoint protocol |

### 4.5 Phase → Skill Mapping

| Phase | Primary Skill(s) | Secondary Skill(s) | Entry Criteria | Exit Criteria |
|---|---|---|---|---|
| **Sense** | drafting-loop | — | User request received | Kind detected, materials inventoried |
| **Clarify** | intent-routing | guided-inquiry | Ambiguous kind or cross-phase materials | Kind confirmed, phase plan set |
| **Shape** | scope-shaping | deep-research | Clarified intent | Scope doc with requirements + AC |
| **Design** | blueprinting | deep-research | Scope doc complete | Executable plan with increments |
| **Build** | plan-execution | audit-trail, style-calibration, deep-research | Blueprint approved | Draft deliverable + evidence |
| **Verify** | quality-review | fact-verification, compliance-gate, cross-validation | Draft deliverable | Review verdict |
| **Record** | acceptance-gate | — | Review passed (or deferred with user approval) | Delivery record |
| **C/S** | distillation | — | Delivery record complete | Next action decided |

**Notes:**
- `deep-research` is primary in Shape (when research informs design) AND secondary in Build (when investigation IS the deliverable)
- `audit-trail` is secondary in Build for Evaluating kind (the "build" phase IS the audit execution)
- `style-calibration` is secondary in Build for Composing/Creating kinds
- `fact-verification`, `compliance-gate`, `cross-validation` are all optional enhancers in Verify, invoked based on kind and user request

---

## 5. Adaptive Checkpoint System

### 5.1 Checkpoint Types

| Type | When Used | Content |
|---|---|---|
| **FULL** | First checkpoint; major transitions; before finalization | Deliverable list + dashboard + all options |
| **SLIM** | After 2+ consecutive "continue" on non-critical phases | One-line status + continue/pause prompt |
| **MANDATORY** | Blueprinting review; quality-review gates; acceptance-gate; scope changes | Cannot skip; explicit user input required |

### 5.2 Decision Dashboard (FULL)

```
━━━ Phase [N] [Name] Complete ━━━

Kind: [detected kind]
Phase: [N/8] [name]

Metrics:
- [kind-specific metric]: [value] [OK/WARN]

Deliverables:
- [deliverable 1]
- [deliverable 2]

Flagged: [issues, or "None"]

Ready to proceed? You can also:
1. Status — view progress
2. Adjust — change settings
3. Pause — stop here
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.3 Self-Check (at every FULL checkpoint)

1. **Quality trajectory**: Is output ≥ previous phase? If declining → PAUSE.
2. **Scope discipline**: Any content outside approved scope?
3. **Completeness**: All required deliverables present?
4. **Evidence**: Verifiable evidence for claims?

If ANY raises concern → include in checkpoint.

### 5.4 Adaptive Rules

1. First checkpoint → FULL
2. 2+ consecutive "continue" → SLIM
3. blueprinting / quality-review / acceptance-gate gates → MANDATORY
4. Other phases → FULL, downgrade to SLIM on "continue"

---

## 6. Handoff Schemas

### 6.1 Universal Handoff Envelope

Every phase-to-phase handoff carries this metadata envelope:

```yaml
handoff:
  from: <phase>
  to: <phase>
  kind: <work kind>
  deliverables: [artifacts]
  status: VERIFIED | UNVERIFIED | STALE
  version: <label>
  hash: sha256:...
  depends_on: [prior artifact versions]
  changes: [scope/design/contract changes]
```

### 6.2 Phase-Specific Payloads

Each phase produces a **payload** that rides inside the envelope. The envelope is metadata; the payload is the substantive handoff data.

#### Sense → Clarify

```yaml
sense_output:
  kind: <detected kind>
  confidence: high | medium | low
  materials: [list]
  material_phases: [which phases materials belong to]
  ambiguous: boolean
  questions: [clarification needed]
```

#### Clarify → Shape

```yaml
clarify_output:
  kind: <confirmed kind>
  phases: [phases to execute per skip table]
  preferences: {mode: full | quick | guided}
  constraints: [time, scope, quality]
```

#### Shape → Design

```yaml
shape_output:
  in_scope: []
  out_of_scope: []
  audience: [target personas]
  requirements: [structured list]
  acceptance_criteria: [verifiable criteria]
  verification_plan: [how to verify each]
  risks: []
  open_questions: []
```

#### Design → Build

```yaml
design_output:
  principles: [design principles]
  approach: {chosen: <>, rejected: [], deferred: []}
  structure: [components/sections/modules]
  contracts: [interfaces/data models/text structures]
  verification: [per-increment methods]
  increments: [ordered work items]
  acceptance_map: [increment → criteria]
```

#### Build → Verify

```yaml
build_output:
  deliverable: <artifact>
  path: <location>
  status: complete | partial | blocked
  evidence: [produced during build]
  drift: [detected scope drift]
  limitations: [unaddressed items]
```

#### Verify → Record

```yaml
verify_output:
  verdict: PASS | CONDITIONAL | FAIL | REVISION
  issues: [structured list]
  dimensions: {dim: score}
  recommendation: proceed | revise | rollback
  confidence: high | medium | low
```

#### Record → Continue/Stop

```yaml
record_output:
  verdict: delivered | partial | blocked | needs-review | rolled-back
  evidence: [for verdict]
  coverage: {total: N, done: M}
  deliverables: [final list]
  next: continue | iterate | stop
  observations: [what worked, what didn't]
```

---

## 7. Intent Clarification Protocol

### 7.1 Triggers

| Condition | Action |
|---|---|
| Clear trigger keyword for one kind | Route directly |
| Materials spanning ≥ 2 phases | **Clarify** |
| No materials + vague request | **Clarify** |
| `[direct-mode]` prefix | Strip, route directly |

### 7.2 Material Phase Detection

| Artifact | Likely Phase |
|---|---|
| Empty / vague idea | Sense/Clarify |
| Requirements, brief, RQ | Shape |
| Architecture, outline, methodology | Design |
| Code, draft, research findings | Build |
| Review comments, test results | Verify |
| Delivery record | Record |

### 7.3 Clarification Template

```
I see <materials>. Which workflow?

(a) **Full loop** — materials to complete deliverable
(b) **<Phase-specific>** — <description>
(c) **<Phase-specific>** — <description>
(d) **Something else** — tell me what you need

Pick a-d, or describe the target. Prefix with `[direct-mode]` for direct dispatch.
```

---

## 8. Mode Spectrum

| Mode | Template Load | When |
|---|---|---|
| **Fidelity** | Heavy | Predictable, checklist-driven output |
| **Balanced** | Medium | Default, structured but flexible |
| **Originality** | Light | Exploratory, creative, guided thinking |

### Kind → Default Mode

| Kind | Default | Override |
|---|---|---|
| Crafting | Balanced | → Fidelity (fixes) / → Originality (architecture) |
| Composing | Balanced | → Fidelity (compliance) / → Originality (creative) |
| Evaluating | Fidelity | Always checklist-driven |
| Investigating | Originality | Always exploratory |
| Creating | Originality | Always exploratory |

---

## 9. Review Protocol (Universal)

### 9.1 Review by Kind

| Kind | Review Type | Reviewers | Output |
|---|---|---|---|
| Crafting | Technical review | Specialist(s) | Issues + suggestions |
| Composing | Editorial review | Multi-perspective panel | Issues + revision roadmap |
| Evaluating | Quality audit | Self + cross-check | Audit report + evidence |
| Investigating | Confidence review | Technical + domain | Findings + confidence |
| Creating | Craft review | Against brief + criteria | Feedback + iteration plan |

### 9.2 Universal Review Output

```yaml
review:
  kind: <kind>
  type: <review type>
  dimensions: [reviewed dimensions]
  scores: {dim: score}
  issues: [structured list with severity + evidence]
  strengths: [what works]
  recommendations: [prioritized]
  verdict: pass | conditional | revision | fail
```

### 9.3 Ground-Truth Isolation

```
Layer 1 — Raw: user request, unverified material
Layer 2 — Verified: output that passed review
Layer 3 — Rubric: acceptance criteria, review rubrics

Rules:
- Builder (L1/L2) never sees rubric (L3) before output
- Reviewer sees rubric + output → natural language feedback
- Builder sees output + feedback → fixes without rubric
```

**Layer 3 (Rubric) by Kind:**

| Kind | Layer 3 Content | Example |
|---|---|---|
| Crafting | Test expectations, acceptance criteria, performance thresholds | "Login must complete in <2s", "All tests pass" |
| Composing | Style guide, fact sources, structure requirements, word count | "APSA format", "All claims cited", "3000-5000 words" |
| Evaluating | Review criteria, severity definitions, compliance standards | "Check all 8 compliance dimensions", "Severity = high if legal exposure" |
| Investigating | Methodology standards, confidence thresholds, evidence hierarchy | "Cross-reference 2+ sources for 'confirmed'", "PRISMA protocol" |
| Creating | Brief, constraints, style direction, reference works | "Minimalist aesthetic", "Tone: literary fiction", "10-15 pages" |

---

## 10. Iron Rules

| # | Rule | Enforcement |
|---|---|---|
| IR-1 | **No phase skipping** | Gate check before each phase |
| IR-2 | **No delivery without evidence** | Fresh verification required |
| IR-3 | **No autonomous state transition** | User at MANDATORY checkpoints |
| IR-4 | **No scope creep** | Change note for any scope addition |
| IR-5 | **No rubric leakage** | Ground-truth isolation |
| IR-6 | **Pressure is not evidence** | Evidence-standard: pushback ≠ correct |
| IR-7 | **No concealed drift** | Change note before undiscussed changes |
| IR-8 | **No partial claims** | All criteria verified or explicitly deferred |

---

## 11. Anti-Patterns

| # | Pattern | Why It Fails | Correct |
|---|---|---|---|
| AP-1 | Skip to Build before Shape/Design | Wrong deliverable | Complete Shape + Design first |
| AP-2 | Confidence as evidence | "Looks good" ≠ verified | Fresh evidence required |
| AP-3 | Silent scope addition | Drift compounds | Change note first |
| AP-4 | Single-perspective review | Blind spots | Multi-perspective review |
| AP-5 | Vague criteria | "Better" is not verifiable | Specific, testable criteria |
| AP-6 | Skip the challenge | First design rarely best | Challenge: over-engineering, sprawl |
| AP-7 | Monolithic scope | Too large to verify | Split into verifiable stages |
| AP-8 | Docs as delivery | Incomplete | Docs supplement, not replace |
| AP-9 | Re-invent the wheel | Ignore conventions | Check existing first |
| AP-10 | Heroics over process | Fails at scale | Standard process + escalation |

---

## 12. Failure Paths

| Scenario | Trigger | Recovery |
|---|---|---|
| Intent won't converge | Clarify > 5 rounds | 3 candidate directions or suggest deep-research |
| Design infeasible | blueprinting shows approach infeasible | Return to Shape, suggest alternatives |
| Build exceeds scope | Increment too broad | Pause, change note, split |
| Critical verification issue | Critical in review | Must fix; rollback if needed |
| User stops mid-process | Explicit stop | Save progress, re-entry path |
| Cross-phase confusion | Multi-phase materials | Intent clarification |
| Quality regression | Output < previous phase | PAUSE, reload principles |
| Revision loop stuck | 3+ rounds no convergence | Stop (converged) or escalate |

---

## 13. Style Calibration (Unified Style System)

Absorbs `style-extraction` (utility) and `style-calibration` (ARS) into one skill with two modes:

### Mode A: Extract (Analysis)

From 3-10 sample texts, produce a structured style profile:
- Quantitative baseline (sentence length, vocabulary, punctuation)
- Surface features (hedging, transitions, register)
- Structure patterns (openings, body logic, closings)
- Deep tone (emotional baseline, analytical framework)
- Taboos (what's absent)
- Executable rules for AI writing

### Mode B: Apply (Production)

During composing/creating, consume a style profile as soft guide:
- Priority: discipline conventions > journal/venue norms > personal style
- Safe dimensions: transitions, hedging, citation style, modifier density
- Risky dimensions: voice, paragraph length, person, formality
- Conflict resolution: norm wins, log conflict, notify user once

### Integration with drafting-loop

- Opt-in at Sense/Clarify phase: "Do you have writing samples to learn from?"
- Profile carried via handoff schema as optional field
- Consumed during Build phase for Composing/Creating kinds
- Extract mode available standalone (not inside loop)

---

## 14. Compliance Gate

### 14.1 When to Invoke

- Evaluating kind: always
- Any kind with compliance requirements: when detected
- User requests compliance check: always

### 14.2 Dimensions

- Scope adherence (within bounds?)
- Contract compliance (interfaces satisfied?)
- Quality standards (criteria met?)
- Evidence completeness (evidence for all claims?)

### 14.3 Override Ladder

| Round | Behavior |
|---|---|
| 1st | Warn user. Rationale optional. Allowed. |
| 2nd | Require rationale string. |
| 3rd | Require rationale ≥ 100 chars. Confirm to release. |

Per-kind, per-loop-run count. Append-only history.

---

## 15. Implementation Plan

### Phase 1: Core (P0)

| Skill | Action | Effort |
|---|---|---|
| `drafting-loop` | Write SKILL.md: universal phases + adaptive checkpoints + kind routing | Large |
| `intent-routing` | New: routing + clarification protocol | Medium |
| `scope-shaping` | Rewrite: generalize for all kinds | Medium |
| `blueprinting` | Rewrite: generalize + doc-architecture + methodology | Medium |
| `plan-execution` | Rewrite: generalize for code/writing/research/analysis | Medium |
| `quality-review` | Rewrite: enhance with multi-perspective + ground-truth isolation | Medium |
| `acceptance-gate` | Rewrite: enhance with evidence chain | Small |

### Phase 2: Supporting (P1)

| Skill | Action | Effort |
|---|---|---|
| `guided-inquiry` | New: 5-layer Socratic dialogue | Medium |
| `deep-research` | Enhance: academic research methodology | Small |
| `distillation` | Enhance: process documentation patterns | Small |
| `audit-trail` | New: domain-specific review execution | Medium |
| `fact-verification` | New: fact verification with evidence chains | Medium |
| `style-calibration` | New: unified style extract + apply | Medium |

### Phase 3: Advanced (P2)

| Skill | Action | Effort |
|---|---|---|
| `cross-validation` | New: cross-model verification | Large |
| `compliance-gate` | New: override ladder + disclosure | Medium |

### References to Write

| Reference | Purpose |
|---|---|
| `handoff-schemas.md` | All handoff data contracts |
| `mode-spectrum.md` | Fidelity/Balanced/Originality mapping |
| `anti-patterns-catalog.md` | Unified anti-patterns |
| `failure-paths.md` | Failure scenarios + recovery |
| `iron-rules.md` | All IRs with enforcement |
| `ground-truth-isolation.md` | Layer model + rules |
| `checkpoint-protocol.md` | Adaptive checkpoint system |

---

## 16. Open Questions

| # | Question | Current Recommendation |
|---|---|---|
| Q1 | Should `audit-trail` be a separate skill or part of `quality-review`? | Separate — audit executes reviews, quality-review evaluates quality |
| Q2 | Multi-deliverable work (paper + slides)? | Single loop, multiple Build tracks. Initial implementation: sequential (one Build track at a time). Future: parallel Build tracks with independent Verify/Record per track. |
| Q3 | Concurrent Build phases? | Yes, for multi-deliverable work. Each track has its own Build → Verify → Record cycle. drafting-loop merges records at C/S. |
| Q4 | `style-calibration` opt-in or always? | Opt-in — not all kinds need it. Activated at Sense/Clarify when user provides writing samples. |
| Q5 | `cross-validation` built-in or standalone? | Standalone — optional enhancement layer. Invoked explicitly by user or auto-invoked for high-stakes Evaluating. |
| Q6 | Kind that doesn't fit (e.g., "help me think")? | Map to Investigating with guided-inquiry. |
| Q7 | How to handle kind transitions mid-loop? (e.g., investigation reveals need for code) | Write change note. Nested loop: inner drafting-loop for new kind with its own phases. Outer loop pauses until inner completes. |
