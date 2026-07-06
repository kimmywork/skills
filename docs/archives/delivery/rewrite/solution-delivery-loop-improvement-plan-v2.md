# Solution Delivery Loop — 最终改进方案

## 已确认的决策

| 编号 | 决策 | 值 |
|---|---|---|
| A2 | 目录名 | `solution-delivery-loop/` 直接替换 `software-delivery-loop/` |
| B3 | investigation 与 discovery 的关系 | requirement-discovery 中调用 investigation 作为深度调研子技能 |
| C4 | change control 信号 | 通用化，同时保留软件专用信号 |
| E1 | prd.md → requirements.md | 确认改名 |
| G1 | Draft-Review-Revise-Finalize 子循环 | 不显式，隐式存在即可 |
| J1 | 非代码 cold start | 改为不假设代码库存在 |

---

## 参考文档的关键汲取

### 从 Deep Research Skills

| 模式 | 对 SDL 的启示 |
|---|---|
| 两阶段模型（outline → deep investigation） | `structured-investigation` 可以采用类似结构：先出大纲/框架，确认后深入 |
| 人机交互在每个阶段切换点 | 已存在于 `review-feedback`，但可以在 investigation 中增加更多用户确认点 |
| 来源验证 + 引用追踪 | 非代码验证的核心机制：每个 claim 必须引用来源 |
| 领域特定的搜索模块（academic, tech, Chinese） | `structured-investigation` 的搜索策略可以按领域模块化 |

### 从 Academic Research Skills (deep-research)

| 模式 | 对 SDL 的启示 |
|---|---|
| 13-agent 团队，角色分离（RQ 设计师、方法架构师、文献检索、来源验证、综合、编辑、魔鬼代言人、伦理审查） | 验证框架可以借鉴多重角色审查：编辑审查（质量）、魔鬼代言人（对抗性）、伦理审查（合规） |
| FINER 标准评估研究问题 | `structured-investigation` 和 `requirement-discovery` 的问题评估可以借鉴 |
| 来源验证：证据层级、掠食性期刊检测、利益冲突标记 | 非代码交付物的验证标准：来源分级、可信度评估 |
| "Gray zone = FAIL" — 无法确认的引用不能进入报告 | 交付物验证的硬性规则：不可验证的声明必须标记 |
| 手写协议：research → paper 有明确的材料传输格式 | 阶段间的手写协议可以借鉴 |
| Socratic 模式：引导用户而不是直接给答案 | `requirement-discovery` 的交互模式可以借鉴 |

### 从 POMASA

| 模式 | 对 SDL 的启示 |
|---|---|
| 模式语言 + 生成器（pattern catalog + generator） | 我们的 `process-distillation` 实际上就是 SDL 的"生成器"——分析执行后发现模式并改进 |
| 三层架构：Definition → Execution → Data | SDL 天然对应：skills（Definition）→ phase execution（Execution）→ track docs（Data） |
| 数据渐进式精炼：Materials → Drafts → Final | `research/` → `requirements.md` → `solution-design.md` → `delivery-record.md` 就是这条链 |
| 模式的必要性分级（Required / Recommended / Optional） | 我们的 PRD template section selection guide（P0/P1/P2）也是这个思路 |
| 可验证数据溯源作为核心质量模式 | 交付物中每个 claim 到 source 的追溯链 |

### 从 Superpowers Skills

| 技能 | 对应 SDL 阶段 | 关系 |
|---|---|---|
| `brainstorming` | `requirement-discovery` | 互补。brainstorming 是"理清想法"，discovery 是"产出可执行的需求" |
| `systematic-debugging` | `structured-investigation`（debug 模式） | 互补。debugging 是 investigation 的子集 |
| `test-driven-development` | `implementation-execution`（软件模式） | 互补。TDD 是 execution 的软件专用验证方法 |
| `verification-before-completion` | `delivery-acceptance` | 互补。verification 是 acceptance 的核心原则 |
| `requesting-code-review` | `review-feedback` | 互补。code-review 是 review-feedback 的子集（代码专用） |
| `writing-plans` | `solution-design` | 互补。writing-plans 是 design 的产出物之一 |
| `skill-creator` | `process-distillation` | 对齐。skill-creator 是创建新技能的流程，process-distillation 是分析现有技能并改进的流程 |

**核心结论：Superpowers 和 SDL 没有 overlap。** Superpowers 是"在什么条件下做什么事"的行为纪律，SDL 是"当前在哪个阶段、下一步去哪"的交付流程。它们互补，可以无缝叠加使用。

---

## 更新后的改进方案

### P0: 入口重命名 + 描述通用化

- `software-delivery-loop/` → `solution-delivery-loop/`
- 所有 SKILL.md 的 description 去掉 "software" 限定
- `software-delivery-loop` 作为 `solution-delivery-loop` 的 symlink 或别名片（已有用户确认无别名，直接替换）

### P0: implementation-execution 通用化

当前执行循环（软件专用）：
```
1. Define expected behavior and verification evidence
2. Prefer TDD: write test, fail, implement, pass
3. Prefer E2E or integration verification
4. Refactor after green
5. Run verification
6. Review for spec fit and architecture fit
7. Update track docs
```

通用化后：
```
1. Define expected outcome and verification evidence
2. Produce the deliverable increment
3. Verify against evidence
4. Refine based on verification results
5. Record evidence and deltas
```

软件模式提取到 `references/software-mode.md`：
```
Software mode (use when deliverable is code):
- Step 2: Prefer TDD: write test, fail, implement, pass
- Step 3: Run build, test, lint, typecheck
- Verification: automated tests, CI, manual QA
```

### P0: 验证框架抽象化

**代码验证（确定性）：**
- Source of truth: 代码本身
- 方法：编译、类型检查、单元测试、集成测试、端到端测试
- 结果：pass / fail（二元）

**非代码验证（概率性）：**
- Source of truth: 引用来源（文档、数据、专家、URL）
- 方法：
  - 每个声明必须引用来源
  - 来源分级（一级：官方文档/同行评审 / 二级：预印本/权威博客 / 三级：社区/灰色文献）
  - 交叉引用一致性检查
  - 不可验证的声明标记为 "assertion" 或 "from-agent-knowledge"
- 结果：verified / cross-referenced / partially-supported / unverifiable / conflicting-sources

**交付物类型的验证重点：**

| 类型 | 验证重点 | 方法 |
|---|---|---|
| 代码 | 行为正确性 | 自动化测试 |
| 报告 | 事实准确性 + 可追溯性 | 来源交叉引用 |
| 调研 | 方法严谨性 + 证据充分性 | 多来源验证 + 置信度标记 |
| 方案 | 可行性 + 需求覆盖 | 对需求矩阵 + 风险评估 |
| Slides | 叙述完整性 | 人工审核 |
| 合同 | 条款覆盖 + 一致性 | 逐条对需求 + 法律审核 |

### P1: structured-investigation 全面重写

从 `code-investigation` 改名为 `structured-investigation`，从 code-focused 扩展为通用深度调研方法论：

**核心能力：**
1. 多源检索：web search、知识库、文档、代码、数据分析、专家访谈
2. 人机交互：outline 确认 → 深入 → 结论确认，每个阶段有用户确认点
3. 来源验证：证据层级、可信度评估、冲突标记
4. 置信度体系：confirmed / cross-referenced / inferred / asserted / from-agent-knowledge
5. 强制 research template 和 raw material 记录
6. 多角色 review：技术审核、领域审核、对抗性审核

**requirement-discovery 调用 investigation：**
- 当需求探索需要深度调研时，`requirement-discovery` 可以调用 `structured-investigation` 作为子技能
- 调研结果保存到 `docs/track/<feature>/research/`

### P1: delivery-acceptance 重写

**Spec Fit + Format Fit 抽象化：**

当前：Spec Fit（behavior, non-goals, scope）+ Code Fit（architecture, contracts, tests）

通用化后：Spec Fit（覆盖需求、无 scope creep）+ Format Fit（符合交付物类型的质量标准）

Format Fit 按类型加载不同的审核标准：
- 代码：architecture, contracts, tests, conventions（当前 Code Fit 内容）
- 报告：factual accuracy, citations, structure, clarity
- 方案：feasibility, risk coverage, actionability
- 调研：methodology rigor, evidence sufficiency, confidence levels
- Slides：narrative flow, visual clarity, key messages

### P1: 阶段产出物改名

- `prd-v1.md` → `requirements-v1.md`（描述、SKILL.md、template 统一改）
- `solution-design-v1.md` → 保持名称，内部结构重新设计
- `plan-v1.md` → 保持名称，verification commands → verification method

### P2: solution-design 重写

当前 Process 中的步骤 5-7 太软件：
- 5. Map architecture/module landing: files, packages, contracts, schemas, routes, UI surfaces, tests
- 6. Challenge the design (保留，通用检查)
- 7. Plan vertical slices (保留，通用)

改为：
- 5. Map deliverable structure: components, sections, modules, interfaces, dependencies
- 6. Challenge the design (保留)
- 7. Plan verifiable increments (保留，用词通用化)

### P2: requirement-discovery 微调

- 描述通用化
- 加 research 调用提示：当需要深度调研时调用 `structured-investigation`
- Process 加 research 保存步骤（已有）
- output scale 改 `requirements.md`

### P3: 按交付物类型的审核标准模板

在 `delivery-acceptance/references/` 下创建：
- `format-software.md` — 软件审核标准（当前 Code Fit 内容）
- `format-report.md` — 报告审核标准
- `format-plan.md` — 方案审核标准
- `format-investigation.md` — 调研审核标准

### P3: 可组合 loop 变体

暂不创建。`solution-delivery-loop` 作为通用路由器。`software-delivery-loop` 等 V2 按需添加。

---

## 与 Superpowers 的关系图

```
                    Superpowers（行为纪律层）
                    ┌──────────────────────────────┐
                    │  brainstorming               │
                    │  systematic-debugging         │
                    │  test-driven-development      │
                    │  verification-before-completion│
                    │  requesting-code-review       │
                    │  writing-plans                │
                    │  skill-creator                │
                    └──────────────────────────────┘
                               │ 调用
                               ▼
         Solution Delivery Loop（交付流程层）
         ┌──────────────────────────────────────────┐
         │  requirement-discovery                   │
         │    └─ 可调用 structured-investigation     │
         │  solution-design                         │
         │  implementation-execution                │
         │    ├─ 通用模式                           │
         │    └─ 软件模式 (references/software-mode) │
         │  delivery-acceptance                     │
         │    ├─ Spec Fit                           │
         │    └─ Format Fit (按类型)                 │
         │  review-feedback (累积审查)               │
         │  process-distillation (自我改进)           │
         │  structured-investigation (深度调研)       │
         └──────────────────────────────────────────┘
```

两者不重叠。Superpowers 说"做事前必须先 invoke 相关技能"，SDL 说"你现在在 requirement-discovery 阶段，做这件事"。叠加使用效果最佳。

---

## 执行顺序

```
Phase 1 (P0): 入口重命名 + 描述通用化
  ├── 重命名目录
  └── 更新所有 SKILL.md description

Phase 2 (P0): implementation-execution 通用化
  ├── 通用执行循环
  └── 提取 software-mode.md

Phase 3 (P0): 验证框架抽象化
  ├── delivery-acceptance Spec Fit + Format Fit 重写
  └── 非代码验证方法论

Phase 4 (P1): structured-investigation 重写
  └── 从 code-focused 到通用深度调研

Phase 5 (P1): 阶段产出物改名
  ├── prd.md → requirements.md
  └── template 更新

Phase 6 (P2): solution-design 重写
  └── 通用化内部结构

Phase 7 (P2): requirement-discovery 微调
  └── 加 research 调用提示

Phase 8 (P3): 按交付物类型的审核标准模板
  └── format-software.md, format-report.md, format-plan.md, format-investigation.md
```