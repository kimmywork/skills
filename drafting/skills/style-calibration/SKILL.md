---
name: style-calibration
description: Extract, validate, compare, and apply a writing style profile from samples. Use when the user wants to match voice, preserve authorial habits, build a style guide, diagnose style mismatch, or rewrite content into a target style.
---

# Style Calibration

Use style as a soft production guide, not a reason to violate truth, domain standards, or user constraints.

## Load by mode

- Extract: `references/computational-stylistics.md`, `references/extraction-workflow.md`, `references/output-template.md`, `references/accuracy-tips.md`
- Chinese samples: also load `references/chinese-style-rules.md`
- Validate/apply: `references/calibration-protocol.md`

## Modes

### Extract

1. Check input quality: sample count, genre, author consistency, non-author material, total length.
2. Quantify before qualifying: sentence, paragraph, function word, and punctuation baselines.
3. Extract surface language, structure, tone, thinking patterns, taboos, positive examples, and negative examples.
4. Every conclusion must cite original text evidence.
5. Prefer differentiating, stable, executable rules over vague adjectives.
6. Mark small-sample or single-genre findings as tentative.

### Validate

Use hold-out or cross-genre calibration when samples permit. Revise overfit or missing profile rules.

### Compare

Identify stable similarities, decisive differences, and likely transfer risks between two styles or between a draft and a target voice.

### Apply

1. User instructions, domain rules, factuality, and compliance outrank style.
2. Preserve safe style dimensions: rhythm, transitions, modifier density, hedging, register, punctuation habits.
3. Treat risky dimensions carefully: persona, unsupported claims, excessive informality, identity imitation.
4. Log conflicts once and choose the higher-priority rule.
5. When rewriting, preserve content intent and mark any style-versus-truth conflict.

## Output

Use `references/output-template.md` for profiles or calibration notes. The result may support a style guide, rewrite, or later drafting work.

## Language

Human-facing output follows the user's language. Durable skill artifacts stay English.
