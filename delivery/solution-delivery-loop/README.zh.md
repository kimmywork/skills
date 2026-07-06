# Solution Delivery Loop（解决方案交付循环）

[English](README.md) | 中文

一个面向各类交付物（代码、报告、调研、方案、文档等）的、agent-neutral 的轻量技能族。受到 [Addy Osmani 的 Loop Engineering](https://addyosmani.com/blog/loop-engineering/) 启发 —— 五个原语（automations、worktrees、skills、connectors、sub-agents）加 state。SDL 专注于 **skills** 和 **state** 两个原语，保持 agent-neutral，不依赖任何特定工具或运行时。

```text
Sense → Shape → Design → Build → Verify → Record → Continue/Stop
```

它可以由人手动执行，也可以在人机协作中执行；当证据充分且不需要用户判断时，也可以自主执行。

## 安装

```bash
npx skills add kimmywork/skills --skill solution-delivery-loop requirement-discovery solution-design implementation-execution delivery-acceptance review-feedback process-distillation structured-investigation
```

## 技能族

- `solution-delivery-loop` — 入口与阶段路由。路由到正确阶段、管理 review-feedback 循环、触发 process-distillation。
- `requirement-discovery` — 用户、场景、范围、非目标、需求、验收。原始调研材料保留在 `docs/track/<feature>/research/` 下。
- `solution-design` — 原则、备选方案、交付物结构、接口/契约、验证策略、计划。包含强制的 "challenge the design" 步骤。
- `implementation-execution` — 产生可验证增量。通用的执行循环，软件模式支持 TDD 驱动。具体的 change-control 信号防止未经记录的 drift。
- `delivery-acceptance` — 基于证据的评审、验证和交付决策。支持完整模板和轻量两种交付记录。
- `review-feedback` — 每个阶段结束后执行的独立审查者。
- `process-distillation` — 每个 review-feedback 周期修复完成后，可选分析已完成的阶段以改进技能。
- `structured-investigation` — 通用调研方法论，适用于任何领域（代码、系统、数据、研究、分析）。

## 与 Loop Engineering 的对齐

[Loop Engineering](https://addyosmani.com/blog/loop-engineering/) 定义了五个自主 agent 循环的原语：automations、worktrees、skills、connectors、sub-agents，外加 state。SDL 实现了 **skills**、**sub-agents** 和 **state** 三个原语，将 automations、worktrees 和 connectors 留给 Agent 运行时。

SDL 在此基础上扩展了两个 Loop Engineering 未描述的能力：

- **累积审查（Cumulative review）**：`review-feedback` 审查从第一个阶段开始的所有产出物，而不仅仅是当前阶段的。越晚执行 review，需要审查的产出物越多，可能回退的距离越远。这是 maker/checker 分离的增强版。
- **自我改进技能（Self-improving skills）**：`process-distillation` 分析已完成阶段的执行过程，并更新技能指令本身。Loop Engineering 说"你设计一次就够了"，SDL 说"你设计它，然后它会自己变得更好。"

## Review 与自我改进循环

每个阶段产出后，`review-feedback` 对所有历史产出物做累积审查。问题按归属阶段、严重程度、类型标注。解决方案：

- **Fix in place**：当前阶段产出物修正问题，重新审查。
- **Roll back**：回到最早受影响阶段，修正那里的产出物，然后重新执行后续阶段。

review-feedback 修复完成后，`process-distillation` 可选分析该阶段循环以改进技能。在 `full-autonomy` 下自动触发。

| Review 时机 | 审查内容 | 可能回退至 |
|---|---|---|
| solution-design | Requirements + 设计方案 | requirement-discovery |
| implementation-execution | Requirements + 设计方案 + 实现 | requirement-discovery |
| delivery-acceptance | 所有前序 + 交付记录 | requirement-discovery |

## Track 文档布局

常规功能：

```text
docs/track/<feature-name>/
  requirements-v1.md
  solution-design-v1.md
  plan-v1.md
  delivery-record-v1.md
  changes/change-note-0001.md
  research/            # requirement-discovery 阶段的原始调研材料
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

**风险意识**：自主执行加速了交付，但产生了 comprehension debt（理解债务）—— 循环交付你不曾写过的代码越快，你对代码库的理解越少。审查循环输出时要像审查人类产出一样严格。认知投降（cognitive surrender）—— 因为形成意见比接受循环产出更难，所以放任不管 —— 这是自动化的真正成本，不是 token 账单。

## 对比与设计取舍

SDL 不是为了替代所有工程工作流。它是一个紧凑的、agent-neutral 的交付循环：把请求塑形为需求，设计方案，产生可验证增量，并记录交付证据。

### 框架对比

| 框架 | 最适用范围 | 优点 | 成本与限制 | SDL 的设计取舍 |
|---|---|---|---|---|
| **Solution Delivery Loop (SDL)** | 从请求到验收结果的各种交付工作：需求、设计、实现、验证、验收、交付记录，以及继续已有 track work。 | 小型阶段技能；入口路由明确；累积审查；自我改进技能；feature-scoped track docs；验收基于证据；支持自主工作；不要求 issue tracker 或 worktree；cold-start 路径清晰。 | 没有严格 TDD-only 循环那么强约束；不会自动安装项目基础设施；触发效果仍依赖 skill discovery；不是通用 productivity suite；意图/风险/验收不清时仍需要人类判断。 | 优化"最小但持久"的交付仪式：足够防止漂移，但不变成流程平台。把 SDL 作为交付主干，需要时调用更专门的技能或工具。 |
| **Loop Engineering** | 自主 agent 循环设计：五个原语（automations、worktrees、skills、connectors、sub-agents）加 state。 | 概念模型清晰；覆盖完整循环生命周期；指出了 comprehension debt 和 cognitive surrender 风险；不绑定 Codex 或 Claude Code。 | 假设运行时支持 automations、worktrees 和 MCP connectors；不规定阶段结构或交付产物；没有自我改进指令的能力。 | 借鉴 maker/checker 分离、state 作为骨架、风险意识。SDL 增加了阶段结构、累积审查和自我改进技能。 |
| **Superpowers** | 跨会话的通用 agent 纪律：skill invocation、brainstorming、systematic debugging、TDD、verification、planning、code review、branch finishing。 | 反自我合理化能力强；非常适合约束 agent 先按流程再行动；覆盖 debugging、TDD、review、plan、verification、branch hygiene；可以作为广义 agent 行为操作系统。 | 全局 invocation 纪律较重；小任务可能显得严格；process skills 可能压过软件交付上下文；包含比 SDL 更广的强制 skill check 和 review checkpoint 假设。 | 借鉴 evidence、TDD、verification、review 和 anti-rationalization，但不让 SDL 的每一步都依赖全局 Superpowers 协议。SDL 更窄，只服务软件交付。 |
| **Tashan Development Loop** | 高压力实现工作，主要风险是跳过分析、设计、计划、测试、验证、commit 或 push。 | 工程纪律很强；明确 Analysis → Design → Plan → TDD → 红绿证据 → Review → Ship；能抵抗时间/范围/沉没成本压力；适合 repo-local implementation rigor。 | 有意设计得很严格；每个工程计划验收后强制 `commit`/`push`；计划任务粒度可能很细；不强调需求发现；中文 repo-specific workflow tone；对轻量塑形或仅验收任务偏重。 | 借鉴红绿证据、小切片和压力抵抗；移除强制 commit/push 和 repo-specific 仪式。SDL 到交付证据为止，是否 commit/push/merge/release 由用户或项目约定决定。 |
| **Matt Pocock Skills** | 围绕 issue tracker、PRD、grilling、domain modeling、deep modules、TDD、code review、research、prototype 和 architecture improvement 的真实工程工作流。 | 模块化 engineering skills 质量高；通过 `CONTEXT.md` 强化领域语言；有 issue tracker 集成；PRD、TDD、code review、codebase design、architecture improvement 实践成熟；区分 user-invoked orchestration 与 model-invoked discipline。 | 假设已配置 issue tracker、triage labels、`CONTEXT.md`、ADR、slash-command flows；PRD/issue workflow 对轻量场景可能过重；不专注于一个最小交付记录循环。 | 借鉴 PRD 质量、领域语言、seam/test 思维、deep-module design、two-axis review。不默认要求 issue tracker、triage labels、`CONTEXT.md` 或 ADR；用 `docs/knowledge` 和 track notes 作为更轻的持久记忆。 |

### 设计维度矩阵

| 维度 | SDL | Loop Engineering | Superpowers | Tashan | Matt Pocock Skills |
|---|---|---|---|---|---|
| 主要单位 | Feature/bugfix delivery track | 自主 agent 循环 | Agent 行为纪律 / task workflow | 工程实现计划 | Issue/PRD/skill workflow |
| 范围 | 各类交付物交付（代码、报告、调研、方案、文档等） | Agent 循环设计 | 广义 agent 流程 | 非平凡 repo 实现 | 工程 + productivity suite |
| 触发方式 | Model-invoked 阶段技能 | 定时调度 + goal-driven | 相关时强制 skill invocation | Model-invoked discipline loop | slash/user-invoked 与 model-invoked 混合 |
| 需求塑形 | `requirement-discovery`；按规模选择 compact note 或 PRD | 由 automation triage 发现 | Brainstorming/planning skills | Analysis phase、成功标准 | Grilling、to-PRD、domain modeling |
| 方案设计 | `solution-design`；备选方案、契约、切片、验证、challenge 步骤 | 隐含在 sub-agent 工作中 | 独立 planning/design skills | 2–3 个方案的显式设计 | Codebase design、seams、PRD decisions |
| 实现 | `implementation-execution`；一个可验证增量 | Sub-agent maker | TDD / executing-plans / subagent-driven development | 严格 TDD red → green → refactor | `/implement` + `/tdd` at agreed seams |
| 审查 | `review-feedback`（累积、独立） | Maker/checker 分离 | Verification 和 code review skills | 红绿证据与 review | Two-axis code review: Standards + Spec |
| 验收 | `delivery-acceptance`；Spec Fit + Format Fit + delivery record | 通过 sub-agent 验证 | Verification 和 code review skills | 红绿证据与 review | Two-axis code review: Standards + Spec |
| 自我改进 | `process-distillation`（内置） | 未提及 | 未提及 | 未提及 | 未提及 |
| 文档 | Feature track docs、`docs/knowledge`、`docs/logs`、research/ | State 文件（markdown） | 计划、review、branch records 按需 | `docs/plans/...` 和 review notes | Issue tracker、PRDs、`CONTEXT.md`、ADRs |
| 自主性 | Evidence-backed；`.agents/loop-state.md` 可设置策略 | 定时调度 + goal-driven 自主 | 取决于具体 skill；通常 checkpoint 更严格 | 严格循环；计划验收后强制 commit/push | 常通过 user-invoked commands 和 issue tracker state 编排 |
| Subagents | 有价值时推荐，不强制 | 核心原语（maker/checker） | 某些流程强依赖 | 非核心 | 用于 review/research/design comparisons |
| Worktrees | 用户/环境决定；无内置策略 | 核心原语 | 相关技能中可用 | 非核心 | 非核心 |
| Commit/push | 除非用户/项目约定，否则不强制 | 未指定 | branch finishing skill 可指导 | 验收后强制 | `/implement` commits current branch |
| 仪式成本 | 低到中，按任务规模伸缩 | 中（需要运行时支持） | 中到高，取决于 skill | 高，且有意如此 | 中到高，尤其在 issue tracker setup 下 |

### SDL 的设计取舍

- **Agent-neutral over platform-specific**：SDL 不依赖 slash commands、issue trackers、worktrees 或某个 harness，因此更可移植，但不会开箱即自动化所有基础设施。Loop Engineering 的 automations、worktrees 和 connectors 很有价值但需要特定运行时 —— SDL 有意将这些留给 Agent 系统。
- **Track notes over mandatory issues**：SDL 使用 `docs/track/...`，让交付记录留在 repo 中。已有 GitHub/Linear 流程的团队仍可把 track docs 映射到 issues。
- **Evidence over confidence**：SDL 要求交付声明前有验证证据，但具体命令交给 repo 和阶段文档决定。
- **Small skills over monolith**：阶段技能降低上下文占用、提升路由清晰度，但要求入口 skill 正确判断下一阶段。
- **Cumulative review over single-pass check**：`review-feedback` 审查从第一个阶段开始的所有产出物。这能捕获单阶段审查遗漏的问题，但审查成本随阶段增加而上升。取舍很清楚：要么尽早发现问题，要么后面承担回退成本。
- **Self-improving instructions over static design**：`process-distillation` 基于真实执行证据更新技能指令。Loop Engineering 说"你设计一次就够了"，SDL 说随着循环运行，设计方案会不断改进。
- **Autonomy with stop conditions**：证据充分时允许自主工作；范围、验收、契约、架构或风险不清时停止。
- **Durable knowledge without mandatory ADRs**：`docs/knowledge` 可保存 ADR、架构说明、领域术语、契约和决策，但 SDL 不要求每次变更都写 ADR 或 `CONTEXT.md`。
- **Review semantics, not review bureaucracy**：SDL 保留 Spec Fit 和 Format Fit，因为它们能防止常见交付失败；但不强制 parallel reviewers、issue labels 或 branch workflows。
- **Right-sized inspection**：SDL 要求先读现有上下文再问用户，但一旦更多上下文不太可能改变下一步行动，就停止继续搜索。

### 什么时候选哪个

| 场景 | 默认推荐 |
|---|---|
| 端到端交付请求（软件、报告、调研、方案）、阶段不清、或继续已有 track work | SDL |
| 设计一个带定时调度和三方接入的自主 agent 循环 | Loop Engineering（使用 SDL 作为 skills/state 层） |
| 需要在广义会话中严格约束 agent 行为 | Superpowers |
| 高压力实现，主要风险是跳过 TDD/验证/commit | Tashan |
| Repo 已使用 issue tracker、PRD-to-issues、domain glossary、ADR 和 slash-command orchestration | Matt Pocock Skills |
| 单纯 bug diagnosis、TDD mechanics、branch finishing 或软件交付之外的 code review | 直接使用专门技能；如果交付记录重要，SDL 可引用其结果 |