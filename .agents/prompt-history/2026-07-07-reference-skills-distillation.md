/solution-delivery-loop 请你继续探索 @reference-skills/ 下面的内容，这些都是跟调查研究、报告撰写、深度研究、文档审阅、研究管线等等相关的技能和文档，请深入分析他们的内容，找出其中可以复用的模式，集成到我们的 @delivery/skills/ 里。

我能直接识别到的： 研究管线构建、深度研究方法和各领域的专用流程、State-Challenge-Reflect protocol (Socratic Mentoring）、shared document包含了很多schema、contract、rubric rules等等。

academic-research-skills 还包含了完整的 docs/design 里的历史记录。这是我们 working experience over comprehensive knowledge 的一个关键来源，简直就是知识金矿。

请完整、详尽分析这些skills，全面综合性地提取他们的可复用点，重新设计和融合我们的delivery loop。

---

- 名称方面，不要受现有skill的限制，可以进行突破。比如这个时候 delivery-loop 是不是已经不够通用了？ drafting-loop 是不是更好？其他的技能是不是也可以对应进行调整。
- 技能覆盖方面， @utility/skills/style-extraction 似乎也包含了一部分 style-calibration 的能力？是需要合并进来还是怎么做调整吗？
- worktype 方面，不要限制的这么死，其实还有很多种可能性，所以集中把这些worktype分成几种类型？crafting / composing / auditing / creativity 诸如此类的，然后按照这个类型/kind来指定shiptable、spectrum、review protocol等等。我上面的类型可能补全，但是你可以补充更多。
- 不要过多考虑consistency和backward compatibility

---

稍微再调整一下名称，然后再给我review一下。skill名称尽可能两个词链接，避免与可能存在的 Agent command 冲突。另外，8个Phase的对应关系是什么样的跟这些skill，你再给我确认一下，然后，work-loop有点难看，有没有什么高级点的词汇。

---

2 / 3 不用改， 6 / 7 考虑是否简单调整，不要只有一个词。 14 直接换成 distillation，这是AI常用说法。 1. 4. 5. 9. 的新名字可以。10、11、12 新名字有点脱离其原意了。13勉强可以，跟15成对。

我是让你改进，不是所有都重造。

---

当前workspace是我正在创建skill的一个工作区，其中我设计了一组新的skill用于升级 @delivery/ 这个框架，目标是 @drafting/ 设计文档参见
@delivery/skills/solution-delivery-loop/references/redesign-v2-universal-work-loop.md （同目录下还有review之前的 v1 的版本）现在另外一个Agent只做了一半的工作，很多设计都没有完整落地。

其中的一个原因是能力问题，另外就是我希望能完整提升这个的能力，并且与 reference-skills 下面的引用设计 align。你来审阅一下这个设计，然后重新实现了。对于已经进行的工作请不要保留，直接抛弃。

有任何问题，请使用 grilling 追问我。

---

不做迁移，现在给我回答下面几个问题：
1. drafting/ 是否能覆盖 delivery/ 的所有内容，是否有缺失，是否有砍掉哪些能力，是否未能承载全部的需求。
2. drafting/ 与设计是否有偏差。
3. drafting/ 还能从 reference-skills 里吸收和合并哪些内容进来。
4. style-calibration 有没有完全吸收 @utility/skills/style-extraction/ 的内容。

---

> 另外，skill.md 的 100 行限制虽然是 hard limit，我们可以先创作然后再提取的方式来达成，而不是必须限制在100行。

把我前面提到的这条，更新进 AGENTS.md，作为 size 约束的补充。你后面创作的时候也可以参考。

然后再次review一下我之前的要求。

---

> - delivery/process-distillation 的 rename-checklist / grep inventory / trigger misfire audit 还没完全搬进 distillation。

这个并不一定要做，看价值。distillation只是提升skill能力，如果不能泛用可以不做。

完整的 phase 中间插入 review / process audit 流程需要完全吸收。多 stage 完全吸收，style-calibration 完全合并， v2 设计完全落地，这些是必须的。其他能力在保持 SKILL 和 framework 完备的情况下充分吸收。

---
