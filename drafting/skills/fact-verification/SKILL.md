---
name: fact-verification
description: Check factual claims, citations, quotations, numbers, and source alignment against evidence. Use for fact-checking drafts, reports, decks, investigations, audits, compliance artifacts, or any deliverable that makes factual assertions.
---

# Fact Verification

Turn factual claims into checked evidence.

## Load

- `references/claim-verification-protocol.md`
- `../drafting-loop/references/ground-truth-isolation.md`
- `../deep-research/references/source-quality-hierarchy.md`

## Workflow

1. Extract checkable claims. Ignore pure opinion unless presented as fact.
2. Classify each claim: public data, numerical consistency, quotation, attribution, causal, legal/policy, technical.
3. Prioritize high-impact or risky claims first when full coverage is impractical.
4. Trace each claim to primary or strongest available evidence.
5. Cross-check high-impact claims with independent sources when available.
6. Use exact calculation for numerical consistency; do not do mental math.
7. Check quote accuracy, numbers, dates, causality, and scope qualifiers.
8. Assign verdict: supported, partially_supported, unsupported, contradicted, unverifiable.
9. Recommend fix: cite, qualify, remove, correct, or mark unknown.

## Output

Use a claim table with Claim, Location, Verdict, Evidence, Confidence, Required fix, Residual uncertainty.

If only partial coverage was possible, say which claims were checked and why.
Never convert unverifiable claims into confident prose.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
