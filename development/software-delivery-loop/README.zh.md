# Software Delivery Loop（软件交付循环）

[English](README.md) | 中文

一个面向软件交付的、agent-neutral 的轻量技能族：

```text
Sense → Shape → Design → Build → Verify → Record → Continue/Stop
```

它可以由人手动执行，也可以在人机协作中执行；当证据充分且不需要用户判断时，也可以自主执行。

## 安装

```bash
npx skills add kimmywork/skills --skill software-delivery-loop requirement-discovery solution-design implementation-execution delivery-acceptance
```

## 技能族

- `software-delivery-loop` — 入口与阶段路由。
- `requirement-discovery` — 用户、场景、范围、非目标、需求、验收。
- `solution-design` — 原则、备选方案、架构、契约、测试策略、计划。
- `implementation-execution` — TDD/E2E 驱动的垂直切片实现。
- `delivery-acceptance` — 基于证据的评审、验证和交付决策。

## Track 文档布局

常规功能：

```text
docs/track/<feature-name>/
  prd-v1.md
  solution-design-v1.md
  plan-v1.md
  delivery-record-v1.md
  changes/change-note-0001.md
```

多项目工作：

```text
docs/track/<project-name>/<feature-name>/...
```

简单工作：

```text
docs/track/features/<feature-name>.md
docs/track/bugfix/<bug-description>.md
```

工作区级循环连续性：

```text
.agents/loop-state.md
```

## 跨功能知识与日志

使用 `docs/knowledge` 保存跨功能的长期知识：

```text
docs/knowledge/adr/
docs/knowledge/architecture/
docs/knowledge/domain/
docs/knowledge/contracts/
docs/knowledge/decisions/
```

使用 `docs/logs/YYYY-MM-DD.md` 保存操作性工作日志。

文档可能过期。当文档、代码、测试和运行时行为互相冲突时，先用源头证据验证真实状态，再更新不准确的文档。

## 自动化立场

当不需要用户输入时，可以自主执行：明显 bugfix、已计划切片、依赖维护、测试修复、文档同步和维护工作。

当意图、取舍、风险、范围或验收需要人类判断时，自动化必须停止。

`.agents/loop-state.md` 可以设置工作区 Autonomy 策略。安全的 skill/template 自我改进默认 ask-first，除非 Autonomy 是 `full-autonomy`。

## 对比与设计取舍

SDL 不是为了替代所有工程工作流。它是一个紧凑的、agent-neutral 的软件交付循环：把请求塑形为需求，设计解决方案，实现可验证切片，并记录交付证据。

### 框架对比

| 框架 | 最适用范围 | 优点 | 成本与限制 | SDL 的设计取舍 |
|---|---|---|---|---|
| **Software Delivery Loop (SDL)** | 从请求到验收结果的软件工作：需求、设计、实现、验证、验收、交付记录，以及继续已有 track work。 | 小型阶段技能；入口路由明确；feature-scoped track docs；验收基于证据；证据充分时支持自主执行；不要求 issue tracker；不强制 worktree；模板局部化；cold-start 路径清晰。 | 没有严格 TDD-only 循环那么强约束；不会自动安装项目基础设施；触发效果仍依赖 skill discovery；不是通用 productivity suite；意图/风险/验收不清时仍需要人类判断。 | 优化“最小但持久”的交付仪式：足够防止漂移，但不变成流程平台。把 SDL 作为交付主干，需要时调用更专门的技能或工具。 |
| **Superpowers** | 跨会话的通用 agent 纪律：skill invocation、brainstorming、systematic debugging、TDD、verification、planning、code review、branch finishing。 | 反自我合理化能力强；非常适合约束 agent 先按流程再行动；覆盖 debugging、TDD、review、plan、verification、branch hygiene；可以作为广义 agent 行为操作系统。 | 全局 invocation 纪律较重；小任务可能显得严格；process skills 可能压过软件交付上下文；包含比 SDL 更广的强制 skill check 和 review checkpoint 假设。 | 借鉴 evidence、TDD、verification、review 和 anti-rationalization，但不让 SDL 的每一步都依赖全局 Superpowers 协议。SDL 更窄，只服务软件交付。 |
| **Tashan Development Loop** | 高压力实现工作，主要风险是跳过分析、设计、计划、测试、验证、commit 或 push。 | 工程纪律很强；明确 Analysis → Design → Plan → TDD → 红绿证据 → Review → Ship；能抵抗时间/范围/沉没成本压力；适合 repo-local implementation rigor。 | 有意设计得很严格；每个工程计划验收后强制 `commit`/`push`；计划任务粒度可能很细；不强调需求发现；中文 repo-specific workflow tone；对轻量塑形或仅验收任务偏重。 | 借鉴红绿证据、小切片和压力抵抗；移除强制 commit/push 和 repo-specific 仪式。SDL 到交付证据为止，是否 commit/push/merge/release 由用户或项目约定决定。 |
| **Matt Pocock Skills** | 围绕 issue tracker、PRD、grilling、domain modeling、deep modules、TDD、code review、research、prototype 和 architecture improvement 的真实工程工作流。 | 模块化工程 skills 质量高；通过 `CONTEXT.md` 强化领域语言；有 issue tracker 集成；PRD、TDD、code review、codebase design、architecture improvement 实践成熟；区分 user-invoked orchestration 与 model-invoked discipline。 | 假设已配置 issue tracker、triage labels、`CONTEXT.md`、ADR、slash-command flows；PRD/issue workflow 对轻量场景可能过重；不专注于一个最小交付记录循环。 | 借鉴 PRD 质量、领域语言、seam/test 思维、deep-module design、two-axis review。不默认要求 issue tracker、triage labels、`CONTEXT.md` 或 ADR；用 `docs/knowledge` 和 track notes 作为更轻的持久记忆。 |

### 设计维度矩阵

| 维度 | SDL | Superpowers | Tashan | Matt Pocock Skills |
|---|---|---|---|---|
| 主要单位 | Feature/bugfix delivery track | Agent 行为纪律 / task workflow | 工程实现计划 | Issue/PRD/skill workflow |
| 范围 | 仅软件交付 | 广义 agent 流程 | 非平凡 repo 实现 | 工程 + productivity suite |
| 触发方式 | Model-invoked 阶段技能 | 相关时强制 skill invocation | Model-invoked discipline loop | slash/user-invoked 与 model-invoked 混合 |
| 需求塑形 | `requirement-discovery`；按规模选择 compact note 或 PRD | Brainstorming/planning skills | Analysis phase、成功标准 | Grilling、to-PRD、domain modeling |
| 方案设计 | `solution-design`；备选方案、契约、切片、验证 | 独立 planning/design skills | 2–3 个方案的显式设计 | Codebase design、seams、PRD decisions |
| 实现 | `implementation-execution`；一个已验证垂直切片 | TDD / executing-plans / subagent-driven development | 严格 TDD red → green → refactor | `/implement` + `/tdd` at agreed seams |
| 验收 | `delivery-acceptance`；Spec Fit + Code Fit + delivery record | Verification 和 code review skills | 红绿证据与 review | Two-axis code review: Standards + Spec |
| 文档 | Feature track docs、`docs/knowledge`、`docs/logs` | 计划、review、branch records 按需 | `docs/plans/...` 和 review notes | Issue tracker、PRDs、`CONTEXT.md`、ADRs |
| 自主性 | Evidence-backed；`.agents/loop-state.md` 可设置策略 | 取决于具体 skill；通常 checkpoint 更严格 | 严格循环；计划验收后强制 commit/push | 常通过 user-invoked commands 和 issue tracker state 编排 |
| Subagents | 有价值时推荐，不强制 | 某些流程强依赖 | 非核心 | 用于 review/research/design comparisons |
| Worktrees | 用户/环境决定；无内置策略 | 相关技能中可用 | 非核心 | 非核心 |
| Commit/push | 除非用户/项目约定，否则不强制 | branch finishing skill 可指导 | 验收后强制 | `/implement` commits current branch |
| 仪式成本 | 低到中，按任务规模伸缩 | 中到高，取决于 skill | 高，且有意如此 | 中到高，尤其在 issue tracker setup 下 |

### SDL 的设计取舍

- **Agent-neutral over platform-specific**：SDL 不依赖 slash commands、issue trackers、worktrees 或某个 harness，因此更可移植，但不会开箱即自动化所有基础设施。
- **Track notes over mandatory issues**：SDL 使用 `docs/track/...`，让交付记录留在 repo 中。已有 GitHub/Linear 流程的团队仍可把 track docs 映射到 issues。
- **Evidence over confidence**：SDL 要求交付声明前有验证证据，但具体命令交给 repo 和阶段文档决定。
- **Small skills over monolith**：阶段技能降低上下文占用、提升路由清晰度，但要求入口 skill 正确判断下一阶段。
- **Autonomy with stop conditions**：证据充分时允许自主工作；范围、验收、契约、架构或风险不清时停止。
- **Durable knowledge without mandatory ADRs**：`docs/knowledge` 可保存 ADR、架构说明、领域术语、契约和决策，但 SDL 不要求每次变更都写 ADR 或 `CONTEXT.md`。
- **Review semantics, not review bureaucracy**：SDL 保留 Spec Fit 和 Code Fit，因为它们能防止常见交付失败；但不强制 parallel reviewers、issue labels 或 branch workflows。
- **Right-sized inspection**：SDL 要求先读现有上下文再问用户，但一旦更多上下文不太可能改变下一步行动，就停止继续搜索。

### 什么时候选哪个

| 场景 | 默认推荐 |
|---|---|
| 端到端软件请求、阶段不清、或继续已有 track work | SDL |
| 需要在广义会话中严格约束 agent 行为 | Superpowers |
| 高压力实现，主要风险是跳过 TDD/验证/commit | Tashan |
| Repo 已使用 issue tracker、PRD-to-issues、domain glossary、ADR 和 slash-command orchestration | Matt Pocock Skills |
| 单纯 bug diagnosis、TDD mechanics、branch finishing 或软件交付之外的 code review | 直接使用专门技能；如果交付记录重要，SDL 可引用其结果 |
