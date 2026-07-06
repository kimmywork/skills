# Solution Design: Universalize delivery/ Skills

## Design Principles

- Agent neutral: no agent-specific tooling assumptions
- Size controlled: all SKILL.md files stay under 500 lines
- Scope limited: each improvement addresses one gap
- Atomic: improvements are independent, can be applied one at a time
- User-centric: all improvements reduce friction (fewer restarts, clearer signals)
- English: all content in English

## Deliverable Structure

4 skills modified, 0 new skills created:

| Skill | Changes | Lines added |
|---|---|---|
| solution-delivery-loop | 6 sections modified/added | +50 |
| solution-design | 4 sections modified | +3 net |
| implementation-execution | 4 sections modified/added | +14 |
| review-feedback | 1 section added | +5 |

## Design Decisions

### D1: Work type triage goes in solution-delivery-loop, not as a separate skill
- Chosen: inline table in solution-delivery-loop
- Rejected: separate triage skill (too lightweight to justify its own skill)
- Why: the triage table is 10 lines, fits naturally before First move

### D2: Stop conditions rewritten, not extended
- Chosen: replace single sentence with structured table
- Rejected: keep original and add table below (redundant)
- Why: the original sentence provides no actionable guidance

### D3: Contract changes, not "breaking changes"
- Chosen: "Contract changes" as section name
- Rejected: "Breaking changes" (software-specific)
- Why: contracts exist in non-software contexts (APIs, data formats, established patterns)

### D4: Multi-pass review as optional guidance, not required
- Chosen: add as guidance paragraph after the main process
- Rejected: make it a required step (adds overhead for simple work)
- Why: simple work doesn't need 3-pass review; complex multi-part deliverables do

### D5: Feasibility pre-screening as a new step, not inline check
- Chosen: new step 3 in solution-design process
- Rejected: add as a check item in existing step 2 (overloads the step)
- Why: feasibility is a distinct activity from confirming scope

## Deferred Features

- Increment granularity heuristics (Improvement 9): current language sufficient
- Acceptance traceability format (Improvement 13): belongs in reference template
- Proposal splitting (Improvement 14): covered by existing increment planning
