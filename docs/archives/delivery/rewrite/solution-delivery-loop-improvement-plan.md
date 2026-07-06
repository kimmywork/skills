# Solution Delivery Loop — 完整改进方案 Review

## 概述

从 `software-delivery-loop` 扩展到 `solution-delivery-loop`，覆盖所有知识工作交付物（代码、报告、方案、调研、评审、slides、合同等）。方向 A（轻量改造），不改核心结构。

---

## 问题清单

### A. 命名与结构

| # | 问题 | 当前状态 | 建议 | 决策 |
|---|---|---|---|---|
| A1 | 入口技能重命名 | `software-delivery-loop` | → `solution-delivery-loop`，无别名 | ✅ 已定 |
| A2 | 目录名 | `development/software-delivery-loop/` | → `development/solution-delivery-loop/` | ⬜ |
| A3 | code-investigation 改名 | `code-investigation` | → `structured-investigation` | ✅ 已定 |
| A4 | 子技能目录结构 | 9 个平铺目录 | 不变，仍平铺在 `development/` 下 | ⬜ |
| A5 | README 文件名 | `README.md`, `README.zh.md` | 保留在 `solution-delivery-loop/` 下 | ⬜ |

### B. Structured Investigation 全面重写

| # | 问题 | 当前问题 | 建议 |
|---|---|---|---|
| B1 | 检索范围 | 只提了 code、tests、docs | 扩到：web search、knowledge base、document analysis、expert interview、data analysis |
| B2 | 用户交互 | 没有提及如何与用户交互式确认 | 加：investigation 过程中用户确认、疑问记录、路径选择记录 |
| B3 | 与 requirement-discovery 的 overlap | 没有明确边界 | 界定：requirement-discovery 的 research 是"为了明确需求"，investigation 是"为了产出调研报告"。两者可以互相调用。 |
| B4 | 交流记录保存 | 无 | 加：`docs/track/<feature>/research/` 下保存原始交流记录、用户反馈、中间结论 |
| B5 | 多角色 review | 只提了 PO/PM/QA/SRE/security | 扩到：domain expert、stakeholder、peer。不预设角色类型 |
| B6 | 强制 research template | 无 | 加：research 产出必须使用 `references/research-template.md`，含置信度、来源、gap |
| B7 | 置信度体系 | 只有 "confirmed" vs "inferred" | 扩到：confirmed / inferred / cross-referenced / asserted / from-agent-knowledge |

### C. Implementation Execution 通用化

| # | 问题 | 当前状态 | 建议 |
|---|---|---|---|
| C1 | 执行循环描述 | "Build one verified vertical slice" | "Produce one verifiable increment at a time" |
| C2 | 步骤 2-3 太软件 | "Prefer TDD: write test, fail, implement, pass" | 通用：define expected outcome → produce → verify | 软件模式提取到 `references/software-mode.md` |
| C3 | 验证方式 | 默认 tests/build/lint | 通用：check against acceptance criteria using appropriate method |
| C4 | change control 信号 | 部分软件特定（test expectation, compatibility shim） | 需要通用化，或分 software / non-software 两组 |
| C5 | 子技能模式 | explorer/maker/checker | 通用，可保留。maker 可以写代码也可以写报告 |

### D. 非代码交付物的验证

这是最核心的问题。代码有确定性的验证（编译、测试 pass/fail），非代码验证是概率性的。

| # | 问题 | 分析 |
|---|---|---|
| D1 | 非代码的 source of truth 是什么？ | 代码：代码本身。报告：引用来源（文档、数据、专家陈述）。方案：需求 + 约束。合同：法律要求 + 谈判结果。 |
| D2 | 非代码的自动化验证怎么做？ | 不能"自动通过/不通过"。可以做：交叉引用检查（claim → source 一致性）、内部一致性检查、完整性检查、来源可信度评估。 |
| D3 | 交叉引用到多少够？ | 每个事实性声明必须引用来源。无来源的声明标记为 "assertion"。关键声明需要 2+ 独立来源。来源冲突必须标注。 |
| D4 | 如何验证 agent 的产出（hallucination 风险）？ | 引用链越长，hallucination 风险越高。策略：每步产出附带来源链、agent 自检（claim → source 引用是否正确）、人工审核 gate。 |
| D5 | 验证结论的置信度表达 | 不只是 pass/fail，而是：verified / cross-referenced / partially-supported / unverifiable / conflicting-sources |

**建议的验证框架（通用）：**

```
每个交付物单元（claim、statement、conclusion）必须标注：
  来源: <document URL / expert / data / agent-knowledge>
  置信度: confirmed | cross-referenced | inferred | asserted | from-agent-knowledge
```

**对于不同交付物类型，验证重点不同：**

| 类型 | 验证重点 | 方法 |
|---|---|---|
| 代码 | 行为正确性 | 自动化测试、类型检查、构建 |
| 报告 | 事实准确性 + 可追溯性 | 来源交叉引用 + 一致性检查 |
| 方案 | 可行性 + 完整性 | 对需求矩阵 + 风险评估 |
| Slides | 叙述完整性 + 清晰度 | 人工审核 |
| 合同 | 覆盖度 + 一致性 | 条款逐条对需求 + 法律审核 |

### E. 阶段产出物改名与重设计

| # | 问题 | 当前 | 建议 |
|---|---|---|---|
| E1 | PRD 改名 | `prd-v1.md` | → `requirements-v1.md`（更通用，不限于 product） |
| E2 | solution-design.md | 保持名称 | 内部结构重设计：去掉过多的软件概念（deployment modes、architecture mapping），改为更通用的 deliverables structure 描述 |
| E3 | plan.md | 保持名称 | 内部结构重设计：task slices 保留（概念通用），但 verification commands 改为通用表达（"verification method" 而不是 shell 命令） |
| E4 | delivery-record.md | 保持名称 | 内容已通用，基本不动 |
| E5 | research/ 目录 | 新建 | 已加，需要明确写入所有模板 |

### F. 阶段 SKILL 文档重写范围

| # | 技能 | 改动量 | 说明 |
|---|---|---|---|
| F1 | `requirement-discovery` | 🟡 中等 | 描述通用化，加 research 调用提示，process 部分微调。output scale 改 requirements.md |
| F2 | `solution-design` | 🟠 大 | Process 和 template 都需重写。去掉 architecture/module landing、deployment modes 等软件概念，替换为通用设计结构。Challenge the design 保留。 |
| F3 | `implementation-execution` | 🔴 最大 | 通用化执行循环 + 软件模式提取。change control 需分两组信号。 |
| F4 | `delivery-acceptance` | 🟠 大 | Spec Fit + Format Fit 抽象化。加按类型的审核标准。 |
| F5 | `structured-investigation` | 🔴 最大 | 全新重写。从 code-focused 扩到全面 investigation 方法论。 |
| F6 | `review-feedback` | 🟢 小 | 已通用。可能只需在 description 中加 delivery type 提示。 |
| F7 | `process-distillation` | 🟢 小 | 已通用。不动。 |
| F8 | `solution-delivery-loop` (router) | 🟡 中等 | 重命名。描述通用化。路由逻辑调整。templates 目录结构不变。 |

### G. Draft → Review → Revise → Finalize 子循环

| # | 问题 | 分析 |
|---|---|---|
| G1 | 这个子循环是否应该显式化？ | 当前隐式存在于 `implementation-execution` 的 slice loop + `review-feedback`。显式化可以让所有交付物类型共享同一个模式。 |
| G2 | 放在哪？ | 建议放在 `implementation-execution` 的通用执行循环中，作为 step 1-6 的抽象描述。`review-feedback` 负责 review 步骤。 |
| G3 | 非代码的 "revise" 怎么做？ | 和代码一样：修改内容 → 重新验证 → 重新 review。没有区别。 |

**建议：** 在 `implementation-execution/SKILL.md` 中显式描述这个子循环，但不说 "TDD"。

### H. 可组合性

| # | 问题 | 分析 |
|---|---|---|
| H1 | 不同 loop 怎么共享技能？ | 所有阶段技能是通用的。loop 技能只是轻量路由器 + 预设配置。`solution-delivery-loop` 是通用路由器，`software-delivery-loop` 是预设了软件模式的变体，`research-delivery-loop` 是预设了调研模式的变体。 |
| H2 | 维护成本如何？ | 每个 loop 技能 10-20 行。核心技能改动一次，所有 loop 受益。**维护成本很低。** |
| H3 | 启动时需要创建几个 loop 技能？ | 先只创建 `solution-delivery-loop`。`software-delivery-loop` 和 `research-delivery-loop` 等 V2 按需添加。 |

### I. 与 Superpowers 的重叠评估

| 维度 | Superpowers | SDL → Solution-Delivery-Loop | 重叠 |
|---|---|---|---|
| 作用层 | Agent 行为纪律（"做事前先 invoke skill"） | 交付流程（"你现在在哪个阶段、要产出什么"） | 0 |
| 解决 | 什么时候该用什么技能、先验证再声称 | 当前阶段是什么、产出物是什么、下一步去哪 | 0 |
| 重叠点 | verifying-before-completion, TDD, code-review | delivery-acceptance（验证证据）、review-feedback（审查） | 功能互补，领域不同 |
| 关系 | 可以一起用 | 可以一起用 | 互补 |

**结论：零 overlap。Superpowers 管行为纪律，SDL 管交付流程。**

### J. 其他关键问题

| # | 问题 | 分析 |
|---|---|---|
| J1 | 非代码的 cold start 怎么做？ | 当前 cold-start 假设有代码库。改为：inspect existing context（docs、data、prior work、user input）。没有代码库就跳过。 |
| J2 | Track 文档路径是否变？ | `docs/track/<feature>/` 结构不变，但 `prd-v1.md` → `requirements-v1.md`。 |
| J3 | 非代码的 "slice" 概念是什么？ | 报告：章节。方案：工作流。调研：发现维度。仍然是"可独立验证的小增量"。 |
| J4 | 验证命令的通用化 | Plan template 中 `Verification commands` 改为 `Verification method`，不假设 shell 命令。可以是 checklist、review procedure、cross-reference step。 |
| J5 | 非软件场景的 autonomy 边界 | 代码有确定性验证，可以更自主。非代码需要更频繁的人工审核 gate。autonomy policy 是否需要按类型区分？ |

---

## 变更优先级排序

| 优先级 | 变更项 | 工作量 | 依赖 |
|---|---|---|---|
| P0 | 入口重命名 + 描述通用化 | 小 | 无 |
| P0 | `implementation-execution` 通用化 | 中 | 无 |
| P0 | 验证框架抽象化（非代码验证） | 中 | 无 |
| P1 | `structured-investigation` 重写 | 大 | 验证框架完成 |
| P1 | `delivery-acceptance` 重写（Spec Fit + Format Fit） | 中 | 验证框架完成 |
| P1 | 阶段产出物改名（prd → requirements） | 小 | 无 |
| P2 | `solution-design` 重写 | 中 | 无 |
| P2 | `requirement-discovery` 微调 | 小 | 无 |
| P2 | Draft-Review-Revise-Finalize 显式化 | 小 | implementation-execution 通用化完成 |
| P3 | 按交付物类型的审核标准模板 | 中 | delivery-acceptance 重写完成 |
| P3 | 可组合 loop 变体（research-delivery-loop 等） | 小 | 核心技能完成 |