# Claim Verification Protocol

## E1: Claim extraction

Extract only checkable factual claims. Preserve exact text when possible.
Classify: public data, numerical consistency, quotation, attribution, causal claim, legal/policy claim, technical claim.

## E2: Source tracing

For each claim, identify the strongest available source:
- primary source or source artifact
- official documentation or data
- peer-reviewed or authoritative secondary source
- reputable expert source
- weak/context-only source

## E3: Cross-reference

Use at least two independent sources for high-impact claims when available.
For calculations, use exact values from the artifact and compute mechanically.

## Verdict taxonomy

| Verdict | Meaning |
|---|---|
| supported | evidence directly supports claim |
| partially_supported | core is true but qualifiers, scope, or numbers need change |
| unsupported | no adequate evidence found |
| contradicted | reliable evidence conflicts with claim |
| unverifiable | cannot verify with available evidence |

## Output fields

Claim, location, verdict, evidence, confidence, required fix, residual uncertainty.
