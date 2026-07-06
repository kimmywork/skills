---
name: style-extraction
description: "Extract a structured writing style profile from an author's sample texts. Use when the user wants to analyze writing style, clone an author's voice, create a style guide from existing texts, or prepare a style reference for AI writing. Trigger on mentions of 'style extraction', 'writing style', 'author voice', 'style profile', 'style guide', or when user provides text samples and asks to identify writing patterns."
metadata:
  author: "Kimmy Liu"
  version: "1.1"
---

# Style Extraction

Extract a structured writing style profile from an author's representative texts: quantifiable features + executable rules + positive/negative examples.

## Rules

1. Every conclusion must cite original text — no unsupported claims.
2. Prioritize differentiating features over common traits.
3. No vague adjectives ("elegant", "fluent") — only executable rules.
4. For Chinese source text, use `references/rules-zh.md` for function word lists, punctuation rules, and output template.

## Input

- 3-10 texts, same author, same genre, 5000-20000 chars total
- Label genre (tech review, fiction, newsletter, etc.). Different genres require different extraction focus: poetry → rhythm/line breaks; tech docs → term density/structure; etc.
- For cross-genre stable features ("style DNA"): provide at least 2 genres, each with 2+ samples
- Mark quoted/dialogue/translated content as non-author material
- For Chinese texts: annotate any Chinese-English mixed paragraphs (distinguish intentional bilingual style from unavoidable technical terms)

## Workflow

Execute these 8 steps in order. Each step's output must include original text evidence.

### Step 1: Quantitative Baseline
- Volume: sample count, total chars, total sentences, total paragraphs, avg paragraph length (sentences + chars)
- Sentence stats: avg length, variance, longest/shortest, long/short ratio, length distribution (buckets: 0-10, 11-20, 21-30, 31-50, 50+ chars)
- Function words: frequency per 1000 chars (Chinese: use list in `rules-zh.md`; English: articles, prepositions, conjunctions, pronouns, auxiliaries). Flag outliers.
- Vocabulary: pronoun ratio (1st/2nd/3rd person), formalness, content word distribution
- Punctuation: frequency ranking of all marks, special usage patterns, CN vs EN punctuation ratio

### Step 2: Surface Language Features
Each dimension requires 1 original sentence as evidence.
- 2.1 Vocabulary: term types, modifier intensity, signature expressions, avoided words
- 2.2 Function words: top 3-5 differentiating words + usage patterns, modal particles, conjunction preferences (contrast: but/however/yet; causal: therefore/thus; parallel: and/along with)
- 2.3 Sentences: type ratios (declarative/rhetorical/question/imperative), rhythm logic, comma-chaining habits
- 2.4 Punctuation/formatting: special mark usage, paragraph splitting, format preferences
- 2.5 Rhetoric: metaphor/analogy/irony frequency, restraint vs intensity

### Step 3: Structure & Narrative
- Opening patterns (2-4 types: hook, question/suspense, thesis-first, story, quote, personal anecdote — with examples)
- Body logic (argument/narrative structure: parallel, progressive, contrast, problem-solution, timeline)
- Closing patterns (2-3 types: summary, call-to-action, closing quote, cliffhanger — with examples)
- Info density, rhythm, transitions
- POV and stance

### Step 4: Deep Tone & Thinking Patterns
Text-derived only, no speculation about author's views.
- Emotional baseline (2-3 descriptors + intensity boundaries)
- Analytical framework (entry angle, judgment criteria, logic chains)
- Personal signature (unique expressions, cognitive patterns)

### Step 5: Taboo & Anti-Rules
What's absent is as diagnostic as what's present.
- Expression taboos (never-used vocab, sentence types, punctuation, rhetoric)
- Content taboos (never-addressed topics, stances)
- Tone redlines (impossible attitudes)
Detection: features absent across 70%+ of samples are likely taboos.

### Step 6: Example Annotation
- Positive: 2-3 representative paragraphs with style trait annotations
- Negative: wrong-way examples for each core feature + correction direction

### Step 7: Self-Check
1. Evidence check — every claim backed by original text?
2. Stability check — feature in 70%+ samples? Mark sporadic traits. If function word or punctuation conclusions are unstable, the samples may be problematic.
3. Usability check — every rule executable by AI writer?

### Step 8: External Calibration (Recommended)
- Leave-one-out: hold 1 sample, validate profile blind
- Cross-genre: validate across genres if targeting cross-genre features

## Output

See `references/output-example.md` for the full template. For Chinese output, see `references/rules-zh.md`.

## Tips

- Function word priority: function words > punctuation > sentences > rhetoric > content. See `references/tips.md`.
- Small samples (<=3): limit to quantifiable features + high-confidence taboos only.
- Cross-genre DNA: only genre-stable features qualify as "style DNA".

## References

- `references/methodology.md` — Computational stylistics foundations
- `references/tips.md` — Accuracy improvement, calibration, prompt template
- `references/rules-zh.md` — Chinese function word lists, punctuation, output template
- `references/output-example.md` — Full English output template
