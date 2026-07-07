# Chinese Style Rules

Use when source samples are Chinese or Chinese-English mixed. Keep analysis prose clear and preserve exact text evidence.

## Chinese output section names

| English section | Chinese section |
|---|---|
| Style Overview | 风格总览 |
| Quantitative Baseline | 核心量化基线 |
| Volume and Sentence Baseline | 体量与句式基线 |
| Function Word Density | 功能词密度基线 |
| Punctuation Density | 标点密度基线 |
| Language Style Rules | 语言风格规则 |
| Structure and Narrative | 结构与叙事范式 |
| Deep Tone and Stance | 深层调性与立场 |
| Taboos and Anti-Rules | 禁忌与反向规则 |
| Reference Examples | 参考样例库 |
| Feature Stability Assessment | 特征稳定性评估 |

## Function words to count

- Structural particles: 的, 地, 得
- Aspect particles: 了, 着, 过
- Copula: 是
- Prepositions: 在, 把, 被, 让, 向, 往, 从
- Conjunctions: 和, 与, 而, 但, 或, 却, 且, 及
- Adverbs: 就, 才, 也, 都, 还, 又, 再, 更, 很, 只
- Negation: 不, 没, 别
- Modal particles: 吧, 呢, 啊, 嘛, 罢, 罢了, 而已, 咧, 呀, 吗

## Classical-modern gradient

Count classical markers per 1000 chars: 之, 其, 于, 即, 皆, 故, 乃, 亦, 方.

## Punctuation

Track Chinese vs Western punctuation, quote style, comma density, dash usage, tilde usage, and dunhao frequency.

## Chinese-English mixing

Record deliberate English embedding separately from unavoidable technical terms. Note inline, parenthetical, title-case, or emphasis patterns.

## Segmentation

If no tokenizer is available, count obvious function words directly and mark segmentation-sensitive numbers as approximate.
