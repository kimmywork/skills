# Investigation Workflow

Detailed step-by-step process for each phase. Read this when executing a full investigation.

---

## Phase 1: Scope

Before gathering evidence, define what you're looking for and where to find it.

1. Define the investigation question(s) and scope boundaries.
2. Identify primary source types: code, documents, web, data, expert interviews, logs, experiments.
3. Plan the investigation approach: what to read, in what order, what to verify against.
4. Confirm scope with the user before proceeding. Save the scope record to `docs/track/<feature>/research/`.

**Avoid:**
- Starting to gather before knowing what you're looking for
- Treating secondary sources (docs, comments, summaries) as ground truth
- Drawing conclusions before collecting cross-references

---

## Phase 2: Gather

Collect primary sources systematically. Record source metadata for every item.

1. **Collect source inventory.** For each source, record: type, origin, access date, relevance.
2. **For code investigations:** read source code, tests, build configs, CI, logs. Trace producer → serialization → transport → consumer → storage.
3. **For web/domain research:** use web search, knowledge base retrieval, document analysis. Search across multiple independent sources.
4. **For data analysis:** examine schemas, data samples, transformation pipelines, storage formats.
5. **For expert interviews:** record questions, answers, and areas of uncertainty.
6. Save all raw material to `docs/track/<feature>/research/`.

**Avoid:**
- Only collecting from one type of source
- Skipping source metadata (origin, date, access method)
- Relying on a single source for critical claims

### Code/System Investigation Addendum

When investigating code or data systems, apply these additional checks after the generic gather phase:
- Build a full type/schema inventory before deep diving.
- Chase untyped or dynamic fields to their runtime assignment site.
- Inspect producer, serialization layer, consumer, and storage independently.
- Capture: numeric scale/offset, timezone/format, enum domains, array serialization rules.
- Identify transient, skipped, or in-memory-only fields.
- Cover all data types including edge cases and extensions.
- Inspect caches, queues, and middleware as complete pipeline hops.
- Ensure pseudocode naming matches actual code exactly.
- Call out binary dependencies or external services as unobservable.

---

## Phase 3: Analyze

Cross-reference findings and assign confidence levels.

1. **Trace the chain end-to-end:** source → transformation → delivery → consumption → impact. Never stop at one link. For code/data systems: producer → serialization → transport → consumer → storage.
2. **Cross-reference** findings across multiple independent sources.
3. **Tag each finding** with a confidence level:
   - **confirmed**: directly verified from primary source
   - **cross-referenced**: verified from 2+ independent sources (not merely quoting the same origin)
   - **inferred**: logically deduced but not directly verifiable
   - **asserted**: claimed without verifiable source
   - **from-agent-knowledge**: based on training data, not independently verified; do not use as final evidence without confirmation

**Trap — citation laundering**: multiple sources repeating the same unsupported claim do not count as cross-reference. Verify independence.
4. Document gaps, uncertainties, and conflicting evidence.
5. Mark "gray zone" items (cannot verify) as such — do not include in conclusions.

**Avoid:**
- Confirmation bias: only finding evidence that supports your hypothesis
- Cherry-picking: citing one supportive study while ignoring contradicting ones
- Treating "difficult to verify" as acceptable — gray zone = excluded or clearly marked
- Assuming field/section names equal semantics without checking actual usage

### Source quality matrix

| Source type | Trust default | Required checks |
|---|---|---|
| Primary data/log/source code | High | Provenance, date/version, completeness |
| Official docs/specs | Medium-high | Version, implementation reality, known drift |
| Peer-reviewed / audited | Medium-high | Method, sample, date, conflicts of interest |
| Expert interview | Medium | Role, access, uncertainty, corroboration |
| Blog/community/marketing | Low-medium | Corroborate before using as factual basis |
| Agent knowledge | Lowest | Mark `from-agent-knowledge`; do not use as final evidence without confirmation |

---

## Phase 4: Document

Structure findings into a traceable, verifiable report.

1. Organize top-down: overview → detail (readers drill in as needed).
2. Cite sources for every conclusion.
3. Separate confirmed findings from inferred/asserted ones.
4. Document edge cases, gaps, and open questions explicitly.
5. Save the final report to the track folder. For format guidance, see `references/templates.md`.
6. Preserve all raw material under `docs/track/<feature>/research/`.

---

## Phase 5: Verify

**Self-check before delivering:**
- Every claim has a source reference
- Confidence levels are assigned to every finding
- Gaps and open questions are documented
- No "asserted" claims are presented as facts
- Cross-document references are consistent
- Proposed plans have validated feasibility

**Multi-perspective review** (for important deliverables):

| Perspective | Focus |
|-------------|-------|
| Domain/Subject expert | Accuracy of domain-specific claims, terminology, completeness |
| Technical reviewer | Feasibility, correctness, edge cases, implementation viability |
| Stakeholder/Decision maker | Coverage, clarity, actionable recommendations, risk awareness |
| Devil's advocate | Alternative explanations, confirmation bias, logical fallacies |

Each reviewer provides: key findings, issues by severity (P0/P1/P2), and concrete suggestions.

**Revision loop:**
1. Fix all P0 issues immediately.
2. Resolve conflicts between perspectives — document trade-off reasoning.
3. Consistency sweep: update ALL documents that reference changed information.
4. Re-run self-check on revised content.
5. Log what was changed and why.