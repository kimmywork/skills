# 全面 Review 报告：tracks/ 文档 + delivery/ 技能模式提取

## 0. 元数据

- **分析日期**: 2026-07-06
- **分析范围**: `tracks/` 172 个文件 (39,428 行) + `delivery/` 8 个 SKILL.md
- **分析模式**: 全面扫描，无抽样
- **分析技能**: process-distillation (delivery/process-distillation/SKILL.md)

---

## 一、tracks/ 文档全景

### 1.1 项目分布 (9 个独立项目)

| 项目 | 文件数 | 行数 | 性质 |
|------|--------|------|------|
| **constype-track** | 36 | 11,044 | 交易所平台，从 v1 演进到 v3 |
| **ng-design** | 33 | 5,839 | 编程语言 NG 的设计提案集 |
| **mono-services-docs** | 45 | 4,981 | 微服务后端，RFC + track 演进 |
| **myz-track** | 25 | 3,916 | myz-agent 持续迭代 (v1→v23) |
| **agent47** | 9 | 5,171 | Decision Workspace，3 个设计 + 3 个计划 + 3 个报告 |
| **crm (yuanlu)** | 8 | 3,145 | 缘录，3 个 PRD 迭代 (v1→v2→v3) |
| **claude-code-plans** | 5 | 1,792 | 独立计划文档 |
| **zlf** | 5 | 1,949 | 图数据库，PRD + 方案设计 |
| **Nekopie** | 4 | 489 | 游戏项目，PROJECT + CHANGELOG |
| **其他** | 2 | 1,102 | clearsight-prd, ng-refactoring |

### 1.2 文档类型分布

| 类型 | 占比 | 典型用途 |
|------|------|---------|
| **PRD/需求** | ~15% | 定义背景、用户、场景、范围、非目标 |
| **方案设计** | ~20% | 架构图、数据模型、组件拆分、合约定义 |
| **实施计划** | ~25% | Task 分解、测试策略、验收标准、提交规范 |
| **状态/报告** | ~15% | 完成度审查、Gap 分析、修复记录 |
| **RFC** | ~10% | 技术决策、权衡分析、Deprecation 说明 |
| **CHANGELOG** | ~5% | 按时间排布的实施记录 |
| **其他** | ~10% | 配置、索引、README |

---

## 二、跨项目提取的通用流程模式

### 模式 1：需求-设计-实施-验收 四阶段循环

**出现频率**: 9/9 项目

每个项目都遵循了相同的四阶段结构：

```
需求发现 (PRD) → 方案设计 (Design) → 实施计划 (Plan) → 验收确认 (Completion/Delivery)
```

**关键约束**:
- 每个阶段产出必须经过审查才能进入下一阶段（对应 `review-feedback` 技能）
- 阶段可回退：实施发现问题 → 回到设计甚至需求阶段
- 后一阶段累加审查前一阶段的所有产出

**可复用规则**:
> 任何交付工作必须经过四个阶段：需求清晰 → 方案评审 → 增量实施 → 验收证据。阶段间不可跳过评审。

### 模式 2：TDD 优先的增量实施

**出现频率**: 5/9 项目 (agent47, constype, myz, clearsight, 部分 mono-services)

**流程**:
```
1. 写失败测试 → 2. 确认测试失败 → 3. 实现最小代码 → 4. 验证测试通过 → 5. 提交
```

**具体体现**:
- agent47 的每个 Task 都明确写 "Write failing test → Run → Implement → Run → Commit"
- constype 的修复报告明确列出 RED 证据和 GREEN 证据
- myz-track 的 v23 需求有追溯矩阵 (Req ID → 测试 → 代码路径)

**可复用规则**:
> 每个 Task 必须先从测试开始。无测试覆盖的代码不得提交。测试失败是开始实施的唯一许可。

### 模式 3：架构演进的三阶段 (Monolith → Split → Reunify)

**出现频率**: 3/9 项目 (constype, myz-agent, agent47)

**典型路径**:
```
Phase 1: 单块快速验证 (MVP monolith)
Phase 2: 功能扩展后拆分 (multi-service/package)
Phase 3: 发现拆分成本高 → 重构为单进程多模块 (library crate pattern)
```

**实例**:
- constype: v1 多服务 HTTP → v2 单进程 → v3 单进程多领域 crate
- myz-agent: v22 单包 → v22 多包 (@myz/agent-core, agent-providers, agent-tui)
- agent47: 单体 → 三列布局 workbench

**可复用模式**:
> 架构演进路径：快速单体 → 按领域拆分 → 物理合并但逻辑分离。不要过早拆分，不要在拆分后长期维持 RPC 通信。

### 模式 4：Scope First, Non-Goals Second

**出现频率**: 8/9 项目

每个设计文档都包含显式的 "Scope" 和 "Non-Goals" 部分。Non-Goals 的作用是防止范围蔓延。

**最佳实践实例**:
- `crm/PRD-yuanlu-v3.md` 在每个功能模块中明确标注 P0/P1/P2 优先级
- `constype-track/v1-architecture.md` 的 Non-Goals 明确列出 v1 不做什么
- `myz-track/v23-agentic-loop.md` 的 Non-Goals 多到 7 条

**可复用规则**:
> 所有设计文档必须有 Non-Goals。Non-Goals 必须用"为什么不做"来解释，而不是仅仅列举。

### 模式 5：Change Note / 变更通知单 机制

**出现频率**: 2/9 项目 (constype ECN, myz-track)

**实例**:
- `constype-track/ECN-0001-architecture-simplification.md` — 完整的变更通知单
- myz 的 "Iron Law: NO UNDOCUMENTED DRIFT" (来自 `implementation-execution` SKILL)

**可复用规则**:
> 任何与已批准计划不一致的变更必须产出一份 Change Note，记录原设计、发现问题、新设计、影响评估。变更 Note 必须经过审批。

---

## 三、跨项目提取的关键约束

### 约束 1：数据模型先行 (Schema-First)

**出现频率**: 7/9 项目

每个设计文档都包含 "Data Model (schema-first)" 或类似部分。类型定义先于实现。

**实例**:
- zlf 的 `solution-design-v1.md` 中所有 crate 的 module landing 和 public types
- myz-track/v23 的 `TodoItem`, `PermissionRule`, `AgentDefinition` 等接口定义
- constype 的 `v1-data-model.md` 完整 SQL 定义

**可复用规则**:
> 实现前必须先定义数据模型。接口和类型是合约，合约稳定后才可以开始实现。

### 约束 2：验收标准需要二元判定 + 证据

**出现频率**: 8/9 项目

**通用模式**:
```
验收标准 ID | 描述 | 二元判定方法 | 证据
```

**实例**:
- `mono-services-docs/track/v1-http-htmx-foundation.md` 的 AC-001 到 AC-006
- `constype-track/v1-completion-status.md` 的验收标准检查表
- `myz-track/v23-agentic-loop.md` 的需求清单 + 追溯矩阵

**可复用规则**:
> 每个验收标准必须可二元判定 (通过/失败)，必须有明确的验证方法，证据必须来自工具输出而非主观判断。

### 约束 3：版本化文档 + 演进追踪

**出现频率**: 6/9 项目

**实例**:
- constype 的 ARCHIVED/DEPRECATED/SUPERSEDED 状态标记
- `crm/PRD-yuanlu.md` → `v2` → `v3` 三次迭代
- `ng-design/README.md` 的 Gap 提案有 Feasibility 评级
- mono-services-docs 的 RFC 编号 (0001-0017)

**可复用规则**:
> 文档必须标注版本状态 (draft/review/active/deprecated/archived)。废弃的文档不能删除，必须标注为 DEPRECATED 并指向替代文档。

### 约束 4：阶段不可跳跃

**出现频率**: 贯穿所有 delivery SKILL

**核心规则**:
```
requirement-discovery → solution-design → implementation-execution → delivery-acceptance
                                 ↓
                          review-feedback (每阶段后)
                                 ↓
                          process-distillation (可选，修复后)
```

**具体体现**:
- `solution-delivery-loop/SKILL.md` 的 Review 和 Feedback 循环表
- `solution-design/SKILL.md` 的 `<HARD-GATE>` 标记
- `implementation-execution/SKILL.md` 的 "Iron Law"

**可复用规则**:
> 不能跳过阶段。设计未通过评审前不能开始实施。实施未通过验收前不能声称完成。

---

## 四、跨项目提取的模式

### 模式 A：文档结构统一模式

**最佳实践结构** (来自多个项目的共识):
```
# <Title>

## Vision / 背景动机
## Scope / Non-Goals
## Data Model (schema-first)
## UX / 流程
## 依赖与边界
## 验收标准
## 风险与回退方案
## 用例与边界条件
```

### 模式 B：MECE 拆分原则

**实例**:
- constype 的 crates 拆分 (types, matching-engine, account, order, kyc, risk, ...)
- myz-agent 的包拆分 (agent-core, agent-providers, agent-tui)
- ng-design 的 Gap 分类 (P0 Foundation, P1 Ecosystem, P2 Advanced)

**可复用规则**:
> 模块拆分必须 MECE (Mutually Exclusive, Collectively Exhaustive)。每个模块有单一职责，模块间通过接口交互，不共享内部状态。

### 模式 C：依赖图优先的风险管理

**实例**:
- constype 的依赖图 (S3 领域间交互矩阵)
- ng-design 的交叉提案依赖图
- crm 的多个技术栈迭代 (云 → Tauri → PWA)

**可复用规则**:
> 依赖图中高风险依赖 (外部工具、未验证库、多语言 FFI) 必须优先验证。验证通过后才可以构建依赖它的模块。

### 模式 D：增量提交 + 原子提交

**实例**:
- agent47 的每个 Task 有独立的 git commit，格式统一
- constype 的提交规范 `refactor(<component>): <description>`
- ng-refactoring 的提交规范

**可复用规则**:
> 每个提交必须原子化 (可构建、可测试)。提交消息格式统一: `<type>(<scope>): <description>`。每个 Task 对应一个提交。

### 模式 E：三层知识管理

**实例**:
- 缘录 `crm/discussion-summary.md` 的事实三层模型 (概念层/行为层/结构层)
- myz-track 的 4 层知识管理 (conceptual/structural/behavioral/operational)

**可复用规则**:
> 知识组织应分层：概念层 (不变)、结构层 (慢变)、行为层 (中速)、操作层 (快变)。不同层有不同的持久化策略和过期策略。

---

## 五、delivery/ 技能中可提取的独立流程

### 5.1 从 solution-delivery-loop 提取的流程

**Sense → Shape → Design → Build → Verify → Record → Continue/Stop**

这是一个通用的闭环框架，可以独立成库。

**独立可复用组件**:
- `.agents/loop-state.md` — 工作区级别的连续性追踪
- `references/progress-template.md` — 多 slice 进度追踪
- `references/change-note-template.md` — 变更通知单
- `references/track-template.md` — 功能 track 文档

### 5.2 从 review-feedback 提取的独立流程

**结构化评审标记系统**:
```
Origin phase: <phase>
Severity: critical | major | minor
Type: missing | incorrect | inconsistent | unclear | scope
Description: <what is wrong>
Evidence: <reference to artifact>
Suggested fix: <concrete next action>
Resolution: fix-in-place | roll-back
```

**可复用规则**:
> 评审反馈必须结构化。不能只有"这个不好"，必须指明来源阶段、严重度、类型、证据、建议修复方案和修复路径。

### 5.3 从 structured-investigation 提取的独立流程

**调查方法论**:
```
Phase 1: Scope → Phase 2: Gather → Phase 3: Analyze → Phase 4: Document → Phase 5: Review
```

**置信度标签**:
```
confirmed | cross-referenced | inferred | asserted | from-agent-knowledge
```

**可复用规则**:
> 任何调查结论必须标记置信度。未经标记的结论视为 assertion，不可作为决策依据。

### 5.4 从 delivery-acceptance 提取的两轴审查

**Spec fit (规格符合) + Format fit (质量符合)** 独立审查。

**可复用规则**:
> 验收必须检查两个维度：规格符合度 (做了该做的事) 和质量符合度 (做对了该做的事)。两个维度都通过才能交付。

---

## 六、复用建议

### 建议 1：创建统一的 Track 文档模板

合并所有项目中找到的最佳实践，形成一个统一的 track 文档模板：

```
# <Project>/<Feature> Track v<N>

## Metadata
- Status: draft | active | review | completed | deprecated | archived
- Supersedes: <path to previous version>
- Superseded by: <path to next version>

## Vision / Background
## Persona / User / Scenario
## Scope / Non-Goals
## Data Model (schema-first)
## Architecture / Module Landing
## UX / Flow
## 验收标准 (二元判定 + 证据方法)
## 风险与回退方案
## 用例与边界条件 (主路径 + 边界1 + 边界2)
## 依赖关系图
## 实施拆分 (Task X.X)
## 变更记录
```

### 建议 2：创建统一的变更通知单模板

基于 constype 的 ECN 格式：

```
# Change Note: <title>

## 元信息
- 日期: 
- 类型: 架构简化 | 范围变更 | 技术替代 | 设计修正
- 影响范围: 全局 | 模块 <name> | 仅文档
- 原计划/文档引用: 

## 原设计
## 发现问题
## 新设计/变更方案
## 影响评估
## 审批状态
```

### 建议 3：创建验证证据指南

基于 `delivery-acceptance` 和 constype 的完成状态报告：

```
## 证据类型与格式
- 命令输出: 完整命令 + exit code + 输出摘要
- 测试结果: 通过/失败/总数 + 关键测试名
- 人工验证: 检查项 + 通过/失败
- 性能基准: 指标 + 前值/后值 + 变化百分比

## 禁止
- 表达满意 ("Great!", "Perfect!", "Done!") 而不附证据
- 用 "感觉没问题" 替代工具输出
- 跳过测试运行直接声称通过
```

### 建议 4：创建架构演进模式文档

从 constype, myz, agent47 中提取的通用演进模式：

```
## 阶段 1: 单体快速验证
- 目的: 最小可工作产品，验证核心假设
- 特征: 单个进程/包，内存存储，最少基础设施

## 阶段 2: 按领域拆分
- 触发条件: 单体规模 > 5000 行，团队 > 2 人
- 策略: 按业务领域拆分，HTTP/RPC 通信

## 阶段 3: 物理合并但逻辑分离
- 触发条件: RPC 成本 > 模块内聚收益
- 策略: library crate 模式，单进程多模块，共享类型库
```

---

## 七、GRASP 复用清单

| 模式/规则 | 来源 | 可复用范围 | 复用形式 |
|-----------|------|-----------|---------|
| 四阶段交付循环 | 所有项目 + delivery SKILLs | 通用 | 技能流程 |
| TDD 增量实施 | 5 个项目 | 软件交付 | 技能流程 |
| Schema-First 设计 | 7 个项目 | 通用 | 设计原则 |
| Scope + Non-Goals | 8 个项目 | 通用 | 文档模板字段 |
| 验收二元判定 | 8 个项目 | 通用 | 验收标准格式 |
| 评审结构化标记 | review-feedback SKILL | 通用 | 评审格式 |
| 置信度标签 | structured-investigation SKILL | 调查/分析 | 标记系统 |
| 变更通知单 | constype ECN | 计划变更 | 文档模板 |
| 文档版本化 | 6 个项目 | 通用 | 文档元数据 |
| 架构演进三阶段 | 3 个项目 | 软件架构 | 演进模式 |
| 知识管理三层 | crm + myz | 知识系统 | 架构模式 |
| 原子提交 + 统一格式 | 4 个项目 | 版本控制 | 提交规范 |
| 两轴审查 | delivery-acceptance SKILL | 验收 | 审查维度 |
| 阶段不可跳跃 | 所有 delivery SKILLs | 通用 | 硬约束 |
| 数据模型先行 | 7 个项目 | 通用 | 设计步骤 |
| 依赖图优先 | constype + ng-design | 架构 | 依赖管理 |
| 事故回退方案 | 4 个项目 | 通用 | 风险管理 |
| 调查五阶段 | structured-investigation SKILL | 调查 | 流程 |
| 三列 Workbench 布局 | agent47 | UI 架构 | 布局模式 |
| 轻量级 PWA 存储 | crm v3 | 离线优先 | 技术选型 |