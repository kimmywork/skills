# Checkout outage — 47 minutes — Presentation Requirements

> Source: [`../incident-postmortem.html`](../incident-postmortem.html) · Type: Incident postmortem · Audience: Engineering and operations leadership · Mode: Hybrid readout + written report · Time: 15 min + 10 Q&A
> Fictional case. The deck is the current implementation; this file captures the brief, structure, and acceptance.

## 1. Audience and intent

Engineering and operations leadership; incident responders.

**Intent:** Learn, agree actions, and restore trust without assigning blame.

**Decision or action:** Approve the six actions and owners; accept the residual risk until closed.

**Success:** The room can explain the trigger, the amplifier, and the systemic gap.

## 2. Narrative

Impact → timeline → root cause → contributing factors → strengths → actions → metrics → lesson.

### Slide sequence

| # | Slide | Budget | Purpose / speaker cue |
|---:|---|---:|---|
| 1 | Checkout outage — 47 minutes | 1 | Set the frame: blameless, evidence-first, actions over blame. |
| 2 | Impact | 1 | Lead with impact, not the deploy. |
| 3 | Timeline | 2 | Walk the timeline in 90 seconds. |
| 4 | Root cause | 3 | Separate trigger from amplifier. |
| 5 | Contributing factors | 2 | Four factors, each with a consequence. |
| 6 | What went well | 1 | Name the strengths. |
| 7 | Actions | 3 | Do not read every row. |
| 8 | Detection and response | 1 | The gap is mitigation, not detection. |
| 9 | The lesson | 1 | One lesson, one sentence. |
| 10 | Appendix | 10 | Q&A. |

## 3. Evidence and fact-check

Timeline, logs, config diff, gateway trace. The incident and numbers are fictional; reconcile with the written report before delivery.

**Fact-check gate:** confirm names, numbers, dates, and comparisons before layout. A precise number without a date and source is a liability.

## 4. Language and delivery

Blameless, plain, past tense; separate trigger from amplifier; no euphemism.

## 5. Visual and accessibility

Light, red accent, monospace timeline; one timeline and one action table; readable in print. Cover uses a night operations photograph, not a server room.

## 6. Time and structure

15 minutes plus 10 Q&A. Must-cut: log detail and individual action rows; protect impact, root cause, and actions. (total budget: 25 minutes)

**Q&A:** prepare the ten most likely questions and one honest answer for each. Do not improvise a fact.

## 7. Verification

- **Titles-only read:** read the slide titles in order. The argument must hold without the body.
- **Timed run:** rehearse to a hard stop, record it, and cut from the must-cut list.
- **Evidence:** every number and comparison has a source, date, and range where relevant.
- **Visual:** check at presentation size, in grayscale, and in the exported file.
- **Accessibility:** alt text, reading order, contrast, color-not-alone, reduced motion, captions/transcript.
- **Print:** one slide per page, notes hidden, no clipped content.
- Check every claim against the written report; read the timeline aloud; confirm owners and dates.

## 8. Non-goals and open questions

**Risks:** Blame framing; actions without owners; hiding a contributing factor.

**Open:** Replace fictional data; confirm legal and communications review; decide whether to include customer quotes.
