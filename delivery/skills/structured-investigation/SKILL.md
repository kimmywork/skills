---
name: structured-investigation
description: Use when a question requires investigation, research, source tracing, system mapping, root cause analysis, or deriving truth from primary sources. Also use when the user mentions "investigate", "trace", "research", "analyze", "reverse engineer", "deep dive", "find root cause", or "understand how X works."
license: MIT
metadata:
  author: kenpusney
  version: "0.4.1"
---

# Structured Investigation

A universal investigation methodology for any domain. Produces traceable, verifiable findings with explicit confidence levels, sourced claims, and known gaps.

## Principles

1. **Primary sources are truth.** Docs, comments, and summaries are leads, not conclusions. Every claim must be traced to a verifiable source (code, document, data, URL, expert statement).
2. **Follow the chain end-to-end.** Trace from origin → transformation → delivery → storage → consumption. Never stop at one link.
3. **Verify, don't speculate.** If a claim cannot be verified, mark it with the appropriate confidence level. "Inferred" is not "confirmed."
4. **Confidence is explicit.** Every finding is tagged: confirmed / cross-referenced / inferred / asserted / from-agent-knowledge.
5. **Multiple perspectives catch blind spots.** Review findings from relevant angles: technical, domain, security, usability, feasibility.

## Process

### Phase 1: Scope

1. Define the investigation question(s) and scope boundaries.
2. Identify primary source types: code, documents, web, data, expert interviews, logs.
3. Plan the investigation approach: what to read, in what order, what to verify against.
4. Confirm scope with the user before proceeding.

### Phase 2: Gather

1. Collect primary sources systematically. For each source, record: type, origin, access date, relevance.
2. For code investigations: read source code, tests, build configs, CI, logs.
3. For web/domain research: use web search, knowledge base retrieval, document analysis.
4. For data analysis: examine schemas, data samples, transformation pipelines.
5. Save raw material and intermediate findings to `docs/track/<feature>/research/`.

### Phase 3: Analyze

1. Trace the chain end-to-end: source → transformation → delivery → consumption → impact. Never stop at one link. For code/data systems: producer → serialization → transport → consumer → storage.
2. Map the landscape: components, entry points, dependencies, data flow, interfaces.
3. Cross-reference findings across multiple independent sources.
4. Tag each finding with confidence level:
   - **confirmed**: directly verified from primary source
   - **cross-referenced**: verified from 2+ independent sources
   - **inferred**: logically deduced but not directly verifiable
   - **asserted**: claimed without verifiable source
   - **from-agent-knowledge**: based on the agent's training data, not independently verified
5. Document gaps, uncertainties, and conflicting evidence.

### Phase 4: Document

1. Structure findings: clear separation of confirmed vs. inferred vs. open questions.
2. Cite every claim to its source. "Gray zone" items (cannot verify) are excluded from conclusions or clearly marked.
3. Save the final report to the track folder. Use `references/templates.md` for format guidance.
4. Preserve all raw material and intermediate findings under `docs/track/<feature>/research/`.

### Phase 5: Review

1. Self-check: are all claims sourced? Are confidence levels assigned? Are gaps documented?
2. Multi-perspective review: assess findings from technical, domain, security, and feasibility angles.
3. Present findings to the user for confirmation. Revise based on feedback.

## Quick Mode (< 1 Hour)

For small, focused tasks:

1. **Locate** — find the relevant source(s)
2. **Trace** — follow one level up and one level down
3. **Confirm** — verify against at least one independent reference point
4. **State confidence** — tell the user whether this is confirmed, cross-referenced, or inferred

No directory structure, no work log, no multi-perspective review needed.

## Interaction with the user

- For full investigations, confirm with the user at each phase transition before proceeding.
- In Quick Mode or when the user requested autonomous work, proceed without repeated confirmation but record assumptions and stop on scope or risk ambiguity.
- Record user feedback, clarifications, and decision points in `docs/track/<feature>/research/`.
- When the user's question is vague, use Socratic-style probing to narrow the scope before investigating.

## Relationship with other skills

- **requirement-discovery**: Call this skill when deep investigation is needed to clarify requirements. Results feed into `docs/track/<feature>/research/`.
- **solution-design**: Call this skill when technical feasibility needs investigation before design decisions.
- **delivery-acceptance**: Investigation findings are verified using `../delivery-acceptance/references/format-investigation.md` criteria.

## Quality Criteria

- **Traceable**: every conclusion points to a source
- **Verifiable**: readers can confirm independently
- **Confidence-bounded**: confirmed vs. inferred vs. asserted is explicit
- **Gap-aware**: uncovered areas and assumptions listed
- **Internally consistent**: no contradictions across findings
- **Multi-dimensional**: covers relevant angles (technical, domain, security, operability)