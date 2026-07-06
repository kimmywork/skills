# Chinese Text Style Extraction: Language-Specific Rules

When the source text is Chinese, apply these rules and write the style profile in Chinese.

## Chinese Output Section Names

Use the same template structure as `output-example.md`, with these Chinese section names:

| English | Chinese |
|---------|---------|
| 1. Style Overview | 1. 风格总览 |
| 2. Quantitative Baseline | 2. 核心量化基线 |
| 2.1 Volume & Sentence Baseline | 2.1 体量与句式基线 |
| 2.2 Function Word Density | 2.2 功能词密度基线 |
| 2.3 Punctuation Density | 2.3 标点密度基线 |
| 3. Language Style Rules | 3. 语言风格规则 |
| 3.1-3.5 sub-sections | 3.1 词汇规范 / 3.2 功能词行为 / 3.3 句式 / 3.4 标点排版 / 3.5 修辞 |
| 4. Structure & Narrative | 4. 结构与叙事范式 |
| 4.1-4.3 sub-sections | 4.1 开头范式 / 4.2 主体逻辑 / 4.3 结尾方式 |
| 5. Deep Tone & Stance | 5. 深层调性与立场 |
| 5.1-5.3 sub-sections | 5.1 情感基调 / 5.2 思维框架 / 5.3 专属印记 |
| 6. Taboos & Anti-Rules | 6. 禁忌与反向规则 |
| 7. Reference Examples | 7. 参考样例库 |
| 7.1-7.2 sub-sections | 7.1 正面典型 / 7.2 反面错误 |
| 8. Feature Stability | 8. 特征稳定性评估 |

## Chinese Function Word Reference

Count frequency per 1000 chars for:

- **Structural particles**: de (的), di (地), de (得)
- **Aspect particles**: le (了), zhe (着), guo (过)
- **Copula**: shi (是)
- **Prepositions**: zai (在), ba (把), bei (被), rang (让), xiang (向), wang (往), cong (从)
- **Conjunctions**: he (和), yu (与), er (而), dan (但), huo (或), que (却), qie (且), ji (及)
- **Adverbs**: jiu (就), cai (才), ye (也), dou (都), hai (还), you (又), zai (再), geng (更), hen (很), zhi (只)
- **Negation**: bu (不), mei (没), bie (别)
- **Modal particles**: ba (吧), ne (呢), a (啊), ma (嘛), ba (罢), bale (罢了), eryi (而已), lie (咧), ya (呀), ma (吗)

## Classical vs Modern Gradient

Formality is a spectrum from classical to vernacular. Quantify with classical function words per 1000 chars: zhi (之), qi (其), yu (于), ji (即), jie (皆), gu (故), nai (乃), yi (亦), fang (方).

## Chinese Punctuation Specifics

- Mixing pattern with Western punctuation is a strong style marker
- Key dimensions: English vs Chinese quotes, half-width vs full-width commas, tilde usage
- Dunhao (、) frequency correlates directly with author style

## Chinese-English Mixing

During extraction, record frequency and method of English embedding (inline / bracketed / emphasized). Exclude unavoidable technical terms; record deliberate bilingual style only.

## Word Segmentation

Chinese lacks space delimiters. Use jieba/pkuseg or let AI annotate function words directly.
