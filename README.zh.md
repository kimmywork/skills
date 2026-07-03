# kimmywork/skills

一个面向软件交付和日常工作效率的 AI agent 技能（Skills）集合。

## 安装方式

### 通过 `npx skills`

```bash
npx skills add kimmywork/skills
```

安装指定技能：

```bash
npx skills add kimmywork/skills --skill <skill-name> [<skill-name> ...]
```

### 通过 Claude plugin

```bash
# 添加市场源
claude plugin marketplace add kimmywork/skills

# 安装插件
claude plugin install software-delivery-loop@kimmywork-skills
claude plugin install utility@kimmywork-skills
```

---

## 技能列表

### Software Delivery Loop（软件交付循环 | 6 个技能）

一个面向软件交付的、agent-neutral 的轻量技能族：

`感知 → 塑形 → 设计 → 构建 → 验证 → 记录 → 继续/停止`

#### `software-delivery-loop`
> 入口与阶段路由。对请求进行分诊，路由到正确的阶段技能，协调从请求到验收结果的端到端交付。支持手动、协作和自主执行模式。

#### `requirement-discovery`
> 将模糊的软件请求塑形为清晰的需求。定义用户、场景、范围、非目标、验收标准和验证预期，在任何设计或实现开始之前完成需求澄清。

#### `solution-design`
> 产出包含取舍分析、架构决策、契约优先设计、实现切片和验证计划的设计方案。接收清晰的需求，产出可执行的计划。

#### `code-investigation`
> 代码级调查与分析的标准化方法论。理解不熟悉的代码库、跨系统映射数据模型、追踪数据流、通过阅读源码分析协议或消息格式。当你需要从代码而非文档中获取真相时使用。

#### `implementation-execution`
> 以 TDD/E2E 驱动的垂直切片方式进行实现。实现功能、修复 Bug、重构或执行维护任务，并集成验证。假设范围、设计和验证预期已经明确。

#### `delivery-acceptance`
> 基于证据的已完成工作审查。评估 Spec Fit（是否满足需求？）和 Code Fit（是否构建良好？），记录验证证据，决定是否发布、继续迭代、回滚或请求用户审查。

---

### Utility（实用工具 | 1 个技能）

#### `cloudconvert`
> 通过 CloudConvert CLI 将非文本文档（PDF、DOC/DOCX、EPUB）转换为 Markdown 格式。通过向 AI agent 投喂干净的 Markdown 而非原始文档格式来节省处理 Token。跳过已可读格式（`.txt`、`.md`、`.json`、`.csv`）。