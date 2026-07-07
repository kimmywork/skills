---
name: fact-verification
description: Verify factual claims against sources with evidence chains. Use for fact-checking, citation checks, claim/source alignment, reports, investigations, audits, compliance artifacts, or any deliverable making factual assertions.
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
3. Trace each claim to primary or strongest available evidence.
4. Cross-check high-impact claims with independent sources when available.
5. Use exact calculation for numerical consistency; do not do mental math.
6. Check quote accuracy, numbers, dates, causality, and scope qualifiers.
7. Assign verdict: supported, partially_supported, unsupported, contradicted, unverifiable.
8. Recommend fix: cite, qualify, remove, correct, or mark unknown.

## Output

Use a claim table with Claim, Location, Verdict, Evidence, Confidence, Required fix, Residual uncertainty.

Never convert unverifiable claims into confident prose.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
