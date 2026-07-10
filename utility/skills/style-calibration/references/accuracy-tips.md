# Style Extraction Accuracy Tips

## Rules

1. Batch extraction first when many samples exist: profile each sample, then keep stable shared traits.
2. Quantify before qualifying. If qualitative impressions conflict with counts, trust the counts until evidence explains the conflict.
3. Focus on differentiating features. Common traits have low style value.
4. Feature priority: function words > punctuation > sentence patterns > rhetoric > content preferences.
5. Use multi-round calibration with a hold-out sample when possible.
6. Normalize by genre. Single-genre traits are not style DNA.
7. With small samples, limit conclusions to quantifiable features and high-confidence taboos.

## Extraction prompt pattern

```text
Perform complete style extraction on the provided samples.
Apply computational-stylistics principles.
Every conclusion must cite original text evidence.
Extract quantitative baselines before qualitative rules.
Produce executable writing rules, positive examples, negative examples, and stability assessment.
If a hold-out sample exists, run calibration.
```
