# Style Calibration Protocol

## Leave-one-out validation

When enough samples exist:
1. Hold out one sample.
2. Build the style profile from the remaining samples.
3. Compare the held-out sample against profile predictions.
4. Mark missed or overfit features.
5. Revise the profile.

## Cross-genre validation

For style DNA claims:
- Require presence across multiple genres.
- Label single-genre traits as genre-specific.
- Do not promote topic preferences to author style.

## Application priority

1. User's explicit instructions.
2. Domain, venue, legal, or compliance rules.
3. Factual correctness and source fidelity.
4. Author style profile.
5. Aesthetic preference.

## Conflict log

```yaml
style_conflict:
  profile_rule: <rule>
  higher_priority_rule: <rule>
  decision: <how resolved>
```
