# Superpowers 模式提取 — 可以吸收到 SDL 的部分

## 最有价值的 5 个模式

### 模式 1: Iron Law（铁律）

Superpowers 用短小、不可协商的命令表达最关键的规则：

| 来源 | 铁律 |
|---|---|
| `systematic-debugging` | "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST" |
| `verification-before-completion` | "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE" |
| `test-driven-development` | "If you didn't watch the test fail, you don't know if it tests the right thing" |
| `receiving-code-review` | "Verify before implementing. Ask before assuming. Technical correctness over social comfort." |

**SDL 中可以吸收的 Iron Law：**
- `delivery-acceptance`：已有一条很好的核心原则 "Acceptance is evidence, not confidence"，但没有铁律化。可以加：**"NO DELIVERY CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE"**
- `implementation-execution` change control：加：**"NO UNDOCUMENTED DRIFT"** — 比现在的 "Stop and write a change note" 更强烈、更易记

### 模式 2: Hard Gate（硬门）

Superpowers 用 `<HARD-GATE>...</HARD-GATE>` 块阻止跨过关键步骤：

```xml
<HARD-GATE>
Do NOT invoke any implementation skill, write any code, scaffold any project,
or take any implementation action until you have presented a design and the
user has approved it.
</HARD-GATE>
```

**SDL 中可以吸收的 Hard Gate：**
- 在 `solution-design` 和 `implementation-execution` 之间：Hard Gate 阻止在 design 通过 review-feedback 之前开始执行
- 在 `requirement-discovery` 完成之前：Hard Gate 阻止进入 solution-design

当前 SDL 的 "After this phase" 用自然语言描述了这个逻辑，但没有 Hard Gate 那种"不可绕过"的语气。

### 模式 3: 精确上下文隔离（最实用的模式）

`requesting-code-review` 的做法：

> "The reviewer gets precisely crafted context for evaluation — never your session's history. This keeps the reviewer focused on the work product."

`subagent-driven-development` 也强调同样的原则：

> "You delegate tasks to specialized agents with isolated context. By precisely crafting their instructions and context, you ensure they stay focused and succeed at their task. They should never inherit your session's context or history — you construct exactly what they need."

**SDL 中的 `review-feedback` 已经支持 subagent，但缺少这个关键细节。** 当前只说 "use reviewer subagent to inspect artifacts and produce report"，没有说"只给 artifacts + criteria，不给 execution history"。这个细节能让 review 质量提升很多。

### 模式 4: Anti-Pattern 清单

Superpowers 多个 skill 都有明确的 anti-pattern 列表：

| Skill | Anti-Pattern |
|---|---|
| `brainstorming` | "This Is Too Simple To Need A Design" |
| `test-driven-development` | "You never saw it catch the bug" |
| `verification-before-completion` | "Expressing satisfaction before verification ('Great!', 'Perfect!', 'Done!')" |
| `writing-plans` | 占位符、模糊描述、缺失文件路径 |

**SDL 的 `requirement-discovery` 已有 anti-patterns，但其他 stages 没有。** 可以为以下阶段各加一组：
- `solution-design`：过度设计、过早优化、忽视 non-goals
- `implementation-execution`：跳过 verification 就声称完成、用 shim 隐藏 drift
- `delivery-acceptance`：凭信心验收、跳过 change note 检查

### 模式 5: 流程优先排序

`using-superpowers` 明确规定了技能调用顺序：

> "Process skills come first — they set the approach, then implementation skills carry it out."

**SDL 的 router 已经做了阶段排序，但可以更明确地说：** "Figure out what's needed before designing. Design before implementing. Verify before delivering." 当前这个逻辑是隐式的（路由到对应阶段），没有作为原则声明出来。

---

## 建议吸收的变更

| 模式 | 目标文件 | 改动量 |
|---|---|---|
| Iron Law 1 | `delivery-acceptance/SKILL.md` | 加一行：`> **Iron Law**: NO DELIVERY CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE` |
| Iron Law 2 | `implementation-execution/SKILL.md` Change control | 加：`> **Iron Law**: NO UNDOCUMENTED DRIFT` |
| Hard Gate | `solution-design/SKILL.md` 末尾 | 加：`> <HARD-GATE> Do NOT start implementation until design has passed review-feedback. </HARD-GATE>` |
| 精确上下文 | `review-feedback/SKILL.md` Subagents 部分 | 加：当使用 subagent 审查时，只传递 artifacts + 审查标准，不传递完整的执行历史 |
| Anti-Patterns | `solution-design`, `implementation-execution`, `delivery-acceptance` | 各加 2-4 条 anti-patterns |
| 流程优先 | `solution-delivery-loop/SKILL.md` First move | 加一句流程优先的原则声明 |

总共改动量很小（每处 1-3 行），但能显著强化关键节点的执行力。