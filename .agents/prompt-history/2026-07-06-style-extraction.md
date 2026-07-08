---
agent: "mimocode"
model: "mimo-v2.5-flash"
---

/skill-creator 整理 @style-extraction.md 里的内容，总结成一个全新的skill，放在 utility 下面。统一升级 utility plugin（@utility/.claude-plugin/plugin.json ) 和下面 SKILL 的版本。

---

首先，skill是英文编写没问题，但是里面不要中英混杂。你可以直接指定一个中文内容的alternative或者是reference，把中文特定的规则放在里面，而在 SKILL.md 或者通用文档里只使用英文。类似“如果文本是中文，style profile也应该用中文，相对应的规则参考 rules-zh.md”这种表述（英文）。
