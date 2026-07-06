# Tips: Accuracy Improvement & Calibration

## Key Techniques

1. **Batch extraction + cross-validation**: If sample size is large, extract single-piece styles first, then compare across pieces — keep only shared traits, discard one-off anomalies. This is "feature stability analysis" in practice.

2. **Quantify before qualifying**: Always run Step 1 stats first, then qualitative analysis (Steps 2-4). Function word and punctuation density data are your "anchor" — if qualitative conclusions contradict quantitative data, trust the numbers.

3. **Focus on differentiation**: Prioritize features that differ from average writers. Common traits (everyone uses periods) have near-zero style value. Core logic of stylometry: only differences are diagnostic.

4. **Function word priority**: In feature ranking: function words > punctuation > sentence patterns > rhetoric > content preferences. Get function words wrong and the whole profile tilts. Get them right and even with downstream deviations, the writing direction stays correct.

5. **Multi-round calibration**: After extraction, give the AI a new text by the same author (not used in extraction) and have it compare against the generated profile to find gaps and errors. Don't skip this — an uncalibrated profile is just "internal fitting" that may be memorizing samples rather than extracting style.

6. **Genre normalization**: If a feature appears only in a single genre, label it "genre-related" not "author feature." Only features stable across genres qualify as author "style DNA."

7. **Overfitting warning**: With small samples (<=3), limit extraction to quantifiable features (function words, punctuation, sentence length) + high-confidence taboos. Don't attempt complex rhetoric or thinking-pattern extraction — reliability is insufficient for small samples.

## Prompt Template

Use this template to kick off extraction:

> Perform a complete style extraction on the provided text samples following the 8-step workflow. Output a structured "Author Writing Style Profile."
>
> **Methodology reminders** (apply throughout):
> - Function words are the most stable style markers — CV < 12% across genres
> - Punctuation density is a strong style signal, extract independently
> - Taboo patterns (what's absent) are as diagnostic as presence patterns
> - Different feature types must be extracted and normalized independently
>
> **Execution requirements**:
> 1. Every conclusion must cite original text as evidence
> 2. No vague adjectives — only executable, concrete rules
> 3. Specifically extract function word behavior (Step 2.2) and taboo/anti-rules (Step 5)
> 4. Output must follow the standard template exactly (including the stability assessment table)
> 5. If a hold-out validation sample is provided, perform external calibration in Step 8
>
> [Text genre]:
> [Text samples to analyze]:
> [Hold-out validation sample (optional)]:
