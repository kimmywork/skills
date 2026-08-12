
## 指南网站

### 1. 🤖 AI 原生基础与交互接口 (AI-Native Foundations & Interfaces)
**核心目标**：定义 Agent 如何“认识”项目、如何“连接”外部世界，以及如何通过标准化接口执行操作。
*   **[agents.md](https://agents.md/)**：AI Agent 的“项目说明书”。为 Agent 提供代码库的结构、规范和上下文，是 Agent 进入项目的第一步。
*   **[modelcontextprotocol.io](https://modelcontextprotocol.io/)**：MCP 协议。AI 时代的核心标准，规范了 LLM/Agent 与外部数据源、工具的连接方式，是 Agent 感知世界的桥梁。
*   **[agentskills.io](https://agentskills.io/)**：Agent 技能与能力规范。标准化 Agent 可调用的技能，便于多 Agent 编排、复用和能力评估。

### 2. 🏗️ 领域建模与分布式系统架构 (Domain Modeling & Distributed Architecture)
**核心目标**：构建能够承载高并发、异步 Agent 流量，且业务逻辑清晰的系统架构。
*   **[eventstorming.com](https://www.eventstorming.com/)**：事件风暴。非常适合人类与 Agent 共同梳理业务逻辑，Agent 可通过 Event 模型和领域事件（Domain Events）精准理解业务全貌。
*   **[microservices.io](https://microservices.io/)**：微服务架构模式。多 Agent 协作通常依赖微服务边界，每个 Agent 或 Agent 组负责独立的微服务，降低上下文耦合。
*   **[enterpriseintegrationpatterns.com](https://www.enterpriseintegrationpatterns.com/)**：企业集成模式 (EIP)。Agent 之间的消息传递、事件路由和系统级联离不开这些经典的异步通信和集成模式。
*   **[reactivemanifesto.org](https://www.reactivemanifesto.org/)** & **[reactiveprinciples.org](https://www.reactiveprinciples.org/)**：响应式系统原则。AI Agent 的调用通常是异步、高并发且不可预测的，系统必须具备响应性、弹性、消息驱动等特质才能承载 Agent 流量。
*   **[12factor.net](https://12factor.net/)**：十二要素应用宣言。无论应用是人类主导还是 Agent 编排，12-Factor 保证了服务的高可用、环境一致性和易于自动化部署。
*   **[clig.dev](https://clig.dev/)**：命令行应用设计指南。

### 3. 🧠 知识沉淀与代码库组织 (Knowledge Management & Codebase Organization)
**核心目标**：管理代码和架构决策，确保 Agent 不会“重蹈覆辙”，理解代码背后的“Why”。
*   **[adr.github.io](https://adr.github.io/)**：架构决策记录 (ADR)。**极其重要！** Agent 必须读取 ADR 才能理解“为什么选择这个技术栈”或“为什么这样设计”，从而避免生成与架构初衷相悖的“正确但无用”的代码。
*   **[monorepo.tools](https://monorepo.tools/)**：Monorepo 工程实践。在大型项目中，统一管理多模块有助于 Agent 获取全局上下文，进行跨模块的代码重构和依赖分析。

### 4. ⚙️ 机器可读标准与自动化流水线 (Machine-Readable Standards & Automation Pipelines)
**核心目标**：建立人类和 Agent 都能精准解析的严格格式，确保 CI/CD 流水线的确定性。
*   **[datatracker.ietf.org/doc/html/rfc2119](https://datatracker.ietf.org/doc/html/rfc2119)**：RFC 需求级别关键字（MUST, SHOULD, MAY 等）。这是 Prompt 工程、Agent 约束规则和需求文档的“语法基石”，彻底消除模棱两可的指令。
*   **[rfc-editor.org/info/rfc2026/](https://www.rfc-editor.org/info/rfc2026/)**：互联网标准制定流程。借鉴其严谨的流程，规范团队内部（包括 Agent 生成代码）的 API 协议和系统标准演进。
*   **[semver.org](https://semver.org/)**：语义化版本控制。确保 Agent 在自动升级依赖或发布 API 时，能准确识别 Breaking Changes，防止自动化灾难。
*   **[conventionalcommits.org](https://www.conventionalcommits.org/)**：约定式提交。让 Agent 能够精准解析 Git 历史，自动生成代码分析报告和趋势总结。
*   **[keepachangelog.com](https://keepachangelog.com/)**：维护更新日志。人类和 Agent 都能轻松阅读的结构化发版说明。
*   **[continuousdelivery.com](https://continuousdelivery.com/)**：持续交付原则。构建人机协作的终极自动化流水线，确保 Agent 生成的代码能安全、自动、持续地部署到生产环境。

### 5. 🛡️ 质量门禁与审查协议 (Quality Gates & Review Protocols)
**核心目标**：规范“人 Review Agent 代码”和“Agent Review 人代码”的双向审查机制。
*   **[google.github.io/eng-practices/review/](https://google.github.io/eng-practices/review/)**：Google 代码审查最佳实践。确立了人类与 Agent 之间互相 Review 的标准流程、速度和礼仪。
*   **[owasp.org/www-project-code-review-guide/](https://owasp.org/www-project-code-review-guide/)**：安全审查指南。Agent 生成的代码极易出现隐蔽的逻辑漏洞，必须经过严格的安全扫描和审查。
*   **[conventionalcomments.org](https://conventionalcomments.org/)**：约定式评论（如 `suggestion:`, `issue:`, `nitpick:`）。让 Agent 能够结构化地解析人类的 Review 意见，从而自动定位并修复代码；同时也规范 Agent 给出的评论格式。
*   **[epicweb.dev/principles](https://www.epicweb.dev/principles)**：Web 工程原则。为前端和复杂交互界面提供高质量的架构指导，确保 Agent 生成的前端代码符合现代工程规范。

### 6. ⚖️ 生态治理与行为契约 (Ecosystem Governance & Behavioral Covenants)
**核心目标**：在开源或多人多 Agent 协作的生态中，确立法律边界、归属权和行为底线。
*   **[choosealicense.com](https://choosealicense.com/)**：开源许可证选择。明确 Agent 生成代码的版权归属、商用边界和传染性问题。
*   **[producingoss.com](https://producingoss.com/)**：开源软件制作指南。指导如何运营一个包含人类开发者和自动化 Agent（Bot）贡献者的开源生态。
*   **[contributor-covenant.org](https://www.contributor-covenant.org/)**：贡献者公约 (CoC)。规范社区交流准则，不仅约束人类，也可引申为约束 Agent 在开源社区发言、提 Issue 或 PR 时的“礼貌程度与攻击性限制”。
*   **[allcontributors.org](https://allcontributors.org/)**：全贡献者规范。量化并记录所有形式的贡献（包括人类的设计、Agent 的自动化测试和文档生成）。

## 核心原则

### 一、 🧠 Tasking 
**核心目标**：规范人类如何给 Agent“派活”，将模糊的人类意图转化为 Agent 可精确执行的确定性指令。

*   **SMART (Specific, Measurable, Achievable, Relevant, Time-bound)**
    *   *AI 时代新解*：**Prompt / Issue 编写标准。** Agent 无法理解“优化一下这段代码”这种模糊指令。必须使用 SMART 原则：“（Specific）将列表渲染改为虚拟列表，（Measurable）支持 10000 条数据不卡顿，（Achievable）使用 `react-window` 库，（Relevant）解决当前页面内存溢出问题”。
*   **INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable)**
    *   *AI 时代新解*：**Agent 任务拆解原则。** Agent 处理长上下文和复杂逻辑时极易失败或产生幻觉。必须将大需求拆解为符合 INVEST 的“原子任务”。特别是 **Small（小）** 和 **Testable（可测试）**，让 Agent 每次只写一个小模块，并立即让另一个 Test Agent 运行测试验证。
*   **Occam's Razor (奥卡姆剃刀 - 如无必要，勿增实体)**
    *   *AI 时代新解*：**方案选择原则。** 当 Agent 给出多种架构方案时，或者在编写 Prompt 时，永远优先选择假设最少、依赖最少、最直接的路径。避免 Agent 引入冷门的第三方库或过度复杂的算法。
*   **Pareto Principle (80/20 帕累托法则)**
    *   *AI 时代新解*：**迭代原则。** 让 Agent 先实现 20% 的核心逻辑（覆盖 80% 的正常场景），边缘的 Corner Case 由人类后续补充，而不是让 Agent 陷入处理无限边缘情况的死循环。

### 二、 🧱 代码设计与生成原则 (Code & Architecture)
**核心目标**：约束 Agent 的代码生成行为，防止其写出“能跑但无法维护”的“面条代码”或“过度工程”。

*   **SOLID (面向对象设计五大原则)**
    *   *AI 时代新解*：**模块隔离的基石。** 特别是 **SRP（单一职责）**。Agent 最容易把控制器、业务逻辑、数据库操作写在一个文件里。强制 Agent 遵循 SRP，能让人类在 Review 时迅速定位问题，也方便后续让 Agent 单独重构某一个类。
*   **YAGNI (You Aren't Gonna Need It - 你不需要它)**
    *   *AI 时代新解*：**反过度工程利器。** LLM 非常喜欢“预判”人类的需求，从而生成大量当前用不到的扩展接口和抽象层。必须在 Prompt 或系统约束中严格注入 YAGNI：“只实现当前需求，不要预测未来，不要提前抽象”。
*   **KISS (Keep It Simple, Stupid - 保持简单)**
    *   *AI 时代新解*：**人类 Review 的底线。** Agent 有时会使用极其晦涩的高级语法或设计模式来炫技。人类 Reviewer 必须挥舞 KISS 大棒，要求 Agent 用“最直白、最笨、但最容易读懂”的方式重写。
*   **SoC (Separation of Concerns - 关注点分离)**
    *   *AI 时代新解*：**上下文隔离。** 确保 UI 渲染、状态管理、网络请求严格分离。这样当 UI 需要修改时，Agent 只需要读取 UI 层的上下文，而不会干扰到数据层的逻辑。
*   **LoD (Law of Demeter - 迪米特法则/最少知识原则)**
    *   *AI 时代新解*：**降低依赖深度。** 限制 Agent 生成 `a.getB().getC().doSomething()` 这种深层调用代码。要求 Agent 封装好接口，这能大幅降低 Agent 在修改代码时“牵一发而动全身”的破坏力。

### 三、 🔄 系统演进与重构原则 (Evolution & Refactoring)
**核心目标**：指导 Agent 在维护旧代码、重构系统时的行为边界，防止 Agent 的“自作聪明”引发灾难。

*   **Chesterton's Fence (切斯特顿栅栏)** 🌟 *[AI时代最核心原则]*
    *   *AI 时代新解*：**防幻觉重构准则。** 栅栏原理指：在不知道栅栏为什么建在这里之前，永远不要拆掉它。Agent 看到一段看似“冗余或奇怪”的老代码时，倾向于直接重写。**必须强制约束 Agent：在重构任何代码前，必须先阅读该代码的 Git Blame、关联的 Issue 和 ADR（架构决策记录），理解其历史背景后，方可提出修改建议。**
*   **DRY (Don't Repeat Yourself) vs. WET (Write Everything Twice)**
    *   *AI 时代新解*：**适度 DRY，警惕过度抽象。** 传统开发极度推崇 DRY。但在 AI 时代，**过度 DRY（高度抽象、多重继承、复杂的泛型）对 LLM 来说极难理解**，因为这需要跨越多个文件拼凑上下文。有时，适度的 **WET（平铺直叙、复制粘贴）** 反而能让 Agent 在有限的上下文窗口内，更准确地修改局部逻辑而不破坏全局。
*   **Boy Scout Rule (童子军军规 - 离开营地时比发现时更干净)**
    *   *AI 时代新解*：**自动化代码净化。** 在 Agent 的 Workflow 中配置一个步骤：每次 Agent 修改某个文件时，自动顺手修复该文件的 Lint 警告、更新过期的注释或补充缺失的类型定义。
*   **Fail Fast (快速失败)**
    *   *AI 时代新解*：**防御性编程。** 要求 Agent 在生成的函数入口处进行严格的参数校验。一旦输入异常立即抛出明确错误，而不是带着错误状态继续运行，这能极大降低人类 Debug Agent 生成代码时的痛苦。

### 四、 🌐 交互与系统级原则 (Interaction & Systems)
**核心目标**：规范 Agent 与外部 API、第三方服务以及其他 Agent 之间的通信契约。

*   **Postel's Law (Robustness Principle - 鲁棒性原则)**
    *   *AI 时代新解*：**API 交互准则。** “发送时要保守，接收时要开放”。Agent 在调用外部 API 时，必须严格遵循协议（保守）；在接收外部（甚至人类输入的脏数据）时，Agent 生成的代码必须做好极强的兼容、容错和降级处理（开放）。
*   **Gall's Law (加尔定律 - 系统演进定律)**
    *   *AI 时代新解*：**系统构建路径。** 一个复杂的系统如果想一次性让 Agent 生成，必定失败。必须从一个“能工作的简单系统（MVP）”开始，让 Agent 逐步迭代、扩展。
*   **Conway's Law (康威定律 - 组织结构决定系统架构)**
    *   *AI 时代新解*：**人机团队拓扑。** 你的系统架构边界，应该与你的“人类开发者 + Agent 代理”的职责边界相匹配。比如，前端 Agent 和后端 Agent 之间必须有明确的 API 契约（如 OpenAPI），就像两个不同的人类团队一样。

### 五、 🛡️ 审查与质量门禁原则 (Review & Quality Gates)
**核心目标**：建立防范 Agent 错误的最后一道防线。

*   **Linus's Law (林纳斯定律 - 只要有足够多的眼睛，所有bug都是浅薄的)**
    *   *AI 时代新解*：**多 Agent 交叉验证。** 不要只让一个 Agent 写代码。引入“Coder Agent（写代码）”、“Reviewer Agent（挑刺）”、“Security Agent（查漏洞）”。让不同 Prompt 设定的 Agent 互相 Review，能发现单一个体（人或Agent）的盲区。
*   **Murphy's Law (墨菲定律 - 凡是可能出错的事就必定会出错)**
    *   *AI 时代新解*：**穷尽异常分支。** Agent 生成代码通常只考虑 Happy Path（快乐路径/正常流程）。人类在 Review 时，必须专门针对 Error Path、Network Timeout、Null/Undefined 等异常路径进行拷问，并要求 Agent 补充处理逻辑。
