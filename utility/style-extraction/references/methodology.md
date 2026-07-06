# Methodology: Computational Stylistics Foundations

## Core Insights

### 1. Unconscious habits are more reliable than conscious choices
Computational stylistics doesn't care *what* an author wrote, but *how* — the unthinking word choices, sentence breaks, and punctuation habits that authors can't consciously control. These are far more reliable for style analysis than content-level features.

**Classic case**: FBI's pursuit of the Unabomber (Kaczynski) — the key evidence wasn't his political views (carefully designed), but his abnormal frequency of "the" and "and" — words too trivial for anyone to intentionally design.

### 2. Function words are "style DNA"
**Function words** (articles, prepositions, conjunctions, pronouns, auxiliaries — words that provide grammatical structure rather than semantic content) are the most stable style markers across all feature categories in stylometry.

**Data**: Same author, different genres — function word coefficient of variation (CV) is typically **< 12%**, while content words have CV **> 45%**. The same person's content words may vary wildly across contexts, but function word frequencies remain nearly constant.

**Evidence**: In the *Dream of the Red Chamber* authorship study, Li Xianping (1987) successfully distinguished the first 80 vs last 40 chapters using only 47 function word frequencies — proving the signal is equally strong across languages.

### 3. Punctuation density is a strong style signal
Punctuation is not grammar — it's breathing rhythm. Comma density, period frequency, dash habits, semicolon preferences — these reveal an author's thinking rhythm more than word choice. For texts that mix Chinese and Western punctuation, the mixing pattern itself is a high-discrimination style marker.

### 4. Features need "divide and conquer"
Different feature types have completely different scales and stability. Mixing everything together gets drowned by dominant features. Correct approach: function words, content words, sentence patterns, punctuation — each extracted independently, normalized independently, combined for interpretation. This is the most important engineering lesson from stylometry.

## Positioning

Computational stylistics aims at *authorship attribution* (who wrote this). This skill aims at *style replication* (how to write like this person). The relationship: **computational stylistics provides quantifiable, verifiable feature extraction methodology; this skill adapts it into an executable workflow for AI writing.** The output "author style profile" is essentially: quantifiable text features + executable writing rules + positive/negative examples.

## Feature Stability Hierarchy

| Feature Category | Stability | Cross-genre? | Notes |
|------------------|-----------|--------------|-------|
| Function word habits | 5/5 | Yes | Same author different genres CV < 12% |
| Punctuation density | 4/5 | Mostly | Less affected by genre than content |
| Sentence length | 3/5 | Partial | Medium genre influence |
| Rhetoric habits | 2/5 | No | High genre/topic influence |
| Content preferences | 1/5 | No | Varies most with topic |
