# Streaming event ingestion at Meridian — Presentation Requirements

> Source: [`../architecture-review.html`](../architecture-review.html) · Type: Architecture review · Audience: Staff engineers and architecture board · Mode: Live + Q&A · Time: 25 min + 10 Q&A
> Fictional case. The deck is the current implementation; this file captures the brief, structure, and acceptance.

## 1. Audience and intent

Staff engineers and the architecture board.

**Intent:** Approve phase 1 of the streaming migration.

**Decision or action:** Approve phase 1; fund two engineers and a game day.

**Success:** The board can state the trade-off and the one-hour rollback.

## 2. Narrative

Context → requirements → options → trade-offs → recommendation → migration → risks → decision.

### Slide sequence

| # | Slide | Budget | Purpose / speaker cue |
|---:|---|---:|---|
| 1 | Streaming event ingestion at Meridian | 1 | State the decision first: this is a review, not a survey. |
| 2 | Context | 2 | The freshness requirement is a product constraint, not an engineering preference. |
| 3 | Requirements | 2 | Four constraints. |
| 4 | Options | 3 | Name the options fairly. |
| 5 | Trade-offs | 3 | The trade-off is not freshness versus cost; it is freshness versus on-call maturity. |
| 6 | Recommendation | 2 | One recommendation. |
| 7 | Migration | 3 | The rollback point is P3. |
| 8 | Risks | 2 | Risks are operational. |
| 9 | Decision | 2 | Ask for phase 1 only. |
| 10 | Appendix | 10 | Q&A. |

## 3. Evidence and fact-check

2.4B events/day, six-hour freshness, cost ceiling, 90-day replay. Metrics are fictional; validate against current telemetry and cost data.

**Fact-check gate:** confirm names, numbers, dates, and comparisons before layout. A precise number without a date and source is a liability.

## 4. Language and delivery

Technical and precise; define exactly-once and replay; no vendor marketing.

## 5. Visual and accessibility

Dark blue, cyan accent; one table or diagram per slide; monospace for constraints. Cover uses an engineering review photograph, not a data-center rack.

## 6. Time and structure

25 minutes plus 10 Q&A. Must-cut: option C detail and vendor comparison; protect trade-offs, migration, risks, and the decision. (total budget: 30 minutes)

**Q&A:** prepare the ten most likely questions and one honest answer for each. Do not improvise a fact.

## 7. Verification

- **Titles-only read:** read the slide titles in order. The argument must hold without the body.
- **Timed run:** rehearse to a hard stop, record it, and cut from the must-cut list.
- **Evidence:** every number and comparison has a source, date, and range where relevant.
- **Visual:** check at presentation size, in grayscale, and in the exported file.
- **Accessibility:** alt text, reading order, contrast, color-not-alone, reduced motion, captions/transcript.
- **Print:** one slide per page, notes hidden, no clipped content.
- Check the trade-off table against the requirements; walk the rollback; rehearse the decision ask.

## 8. Non-goals and open questions

**Risks:** Straw-man options; ignoring on-call load; no rollback.

**Open:** Replace fictional metrics; confirm vendor constraints; add the real topology diagram.
