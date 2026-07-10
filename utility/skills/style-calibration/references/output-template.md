# Adaptive Style Profile Formats

Choose the smallest format that supports the user's next action. Do not generate unused sections. For Chinese output, use the relevant labels from `chinese-style-rules.md` rather than forcing every mapped section.

## Compact profile

Default for small samples, quick diagnosis, or a profile intended for one rewrite.

```markdown
# Style Profile
## Scope and confidence
Sample coverage, genre, limitations.
## Distinctive rules
3-7 executable rules, each with evidence.
## Avoid
High-confidence anti-rules or common mismatches.
## Application notes
What to preserve and what must yield to truth, domain, or user constraints.
```

Include only the quantitative observations that materially support the rules.

## Full profile

Use when the user requests a reusable style guide, provides enough representative material, or needs formal calibration. Select relevant sections from:

```markdown
# [Author or corpus] Style Profile
## Scope, samples, and confidence
## Quantitative baseline
## Vocabulary and function-word behavior
## Sentence rhythm and punctuation
## Structure and transitions
## Tone, stance, and recurring reasoning moves
## Taboos and anti-rules
## Representative examples
## Stability by sample or genre
## Application and conflict rules
## Calibration results
```

Possible quantitative tables include sentence and paragraph distributions, punctuation density, function-word frequency, and cross-sample variation. Derive stability from the actual samples; do not copy fixed scores or assume a feature is stable across genres.

## Comparison

Use for two authors, two corpora, or a draft versus a target profile.

```markdown
# Style Comparison
## Scope and comparability
## Stable similarities
## Decisive differences
## Evidence
## Transfer risks
## Recommended changes
```

Focus on differences that affect the user's decision or rewrite.

## Application note

Use when the primary task is rewriting rather than profile creation.

```markdown
# Style Application Note
## Rules applied
## Content preserved
## Conflicts and higher-priority constraints
## Deviations and uncertainty
```

The rewritten artifact may be the main output; keep the note brief unless the user asks for analysis.

## Evidence rules

- Tie qualitative rules to excerpts or measured patterns.
- Keep quotations no longer than needed to demonstrate the feature.
- Mark genre-specific and small-sample conclusions as tentative.
- Omit sections that the evidence cannot support.
- Never imply that a rewritten text was authored, endorsed, or published by the source author.
