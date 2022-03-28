
---
title: '从零开始搭建SRE'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/c7b34079aa49da375fb3c97a46d4791b.png'
author: Dockone
comments: false
date: 2022-03-28 02:28:26
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/c7b34079aa49da375fb3c97a46d4791b.png'
---

<div>   
<br>【编者的话】Google 在 10 年前创造了SRE这个工种。SRE，Site Reliability Engineering 的缩写。其中 site 是指 Website，可以翻译为网站可靠性工程。几年前资深 Google SRE Chris Jones 等人联合撰写了《Google SRE: How Google runs production systems》，首次向外界解密了Google的生产环境以及整个SRE的方法论。那么如何从零搭建一套SRE体系呢？下文本文主要介绍站点可靠性工程 (SRE) 以及如何在系统扩展时监控和保持系统快速可靠。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220327/c7b34079aa49da375fb3c97a46d4791b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/c7b34079aa49da375fb3c97a46d4791b.png" class="img-polaroid" title="1_3Hn-OiFm27eP6bMfSiClKQ.png" alt="1_3Hn-OiFm27eP6bMfSiClKQ.png" referrerpolicy="no-referrer"></a>
</div>
<br>
图1 构建SRE架构思维导图<br>
<br>        在云时代，客户体验是任何重要企业的新口号，即使命宣言。客户体验、可用性和可访问性是在端决定的，在这里站点应当始终可用 [24/7/365]。对用户来说，可靠性才是最重要的; 一个未使用的应用程序对用户和企业毫无价值。<br>
        而如今，每家公司都在努力推动科技变革。公司业务战略都围绕云功能构建。这对他们来说是一项重大的运营挑战。站点性能下降、客户体验的下降都将导致现金、收入和竞争力的损失，并导致传统运营无法应对可观察性的大问题（包括实时监控和告警）。<br>
<blockquote><br>为什么存在站点可靠性工程（SRE）？敏捷运动提升了跨职能团队之间协作的重要性，这催生了 DevOps。 DevOps 是关于深入研究自己组织的具体问题和挑战。它还与速度、效率和质量有关。从本质上讲，它是一种以实现组织的预期结果的文化、一种运动、一种价值观、原则、方法和实践。这种速度也造成了一定的不稳定性，开发人员的行动速度比以往任何时候都快了，但却给运营团队带来了挑战。 IT 运营团队没有能力应对这样的速度，这给他们造成了严重的瓶颈和积压，导致生产中产生了不稳定的因素，结果使系统变得不可靠。因此，Google创建了对 SRE ：“一群能够将工程专业知识应用于运营问题的开发人员。”</blockquote>SRE 是一种规范的 DevOps 方式。 它是系统管理任务的一种思维方式，侧重于通过缩短交付周期和事件管理生命周期，并通过减少工作量来支持开发人员和运营人员来运营服务的原则。 SRE 团队的日常任务包括：<br>
<ul><li>可用性</li><li>延迟</li><li>性能</li><li>效率</li><li>变更管理</li><li>监控和告警</li><li>应急响应</li><li>事件响应</li><li>准备工作</li><li>容量规划</li></ul><br>
<br><h2>那么，什么是站点可靠性工程(SRE)?</h2>SRE团队的角色是运营在生产“关键任务系统”中应用程序，并执行任何必要的事情来保持站点正常运行。它通常被定义为从事运维工作的软件工程师。SRE团队负责维护和建立其系统的服务水平指标(SLI)、目标(SLO)、协议(SLA)和错误预算，并确保满足这些指标。他们预计将花费一定的时间进行运营工作（确保系统按期工作）并改进他们管理的系统。SRE专注于编写软件来自动化流程并减少"脏活累活"的工作量。这个"脏活累活"就是目前还未实现系统自动化并且需要手动处理的工作。<br>
SRE 的战略目标是：<br>
<ul><li>使部署更加容易</li><li>提高或维持正常运行时间 </li><li>针对应用性能去建设可视化能力 </li><li>设置 SLI's和 SLO's 以及错误预算</li><li>通过承担计算风险来提高速度 </li><li>消除手动操作任务 </li><li>降低故障成本以缩短新功能的周期时间。</li></ul><br>
<br><h2>SLI 和 SLO</h2>服务水平目标 (SLO) 只是 SRE 团队与产品所有者或业务线 (LOB) 之间的协议。指标在很大程度上取决于团队管理的系统的性质。服务水平指标(SLIs)是为系统定义的量化指标，也称为 “我们正在度量的内容”。这些指标取决于所管理的系统。对于典型的 Web 应用程序，这些指标可能是可用性、请求延迟或错误率。但是，例如Hyperledger Fabric 区块链应用程序可能会使用每秒背书和分类帐提交率来衡量网络的吞吐量。<br>
<br>SRE 团队最终将管理多个系统。跨各种应用程序定义一组标准的 <code class="prettyprint">服务水平指标</code>将帮助团队标准化整个堆栈的监控、日志记录和自动化。<br>
SLO 是系统应该运行的目标值或范围 “应该有多好。” 这些是之前定义的 SLI 的预期操作值。例如，区块链网络必须以不到 5 秒的端到端延迟来维持 50 到 100 个事务提交速率的事务吞吐量。当然这也有可能存在过度设计 SLI 和 SLO 的倾向。一开始就让它们保持简单是很重要的。随着您对系统的了解随着时间的推移而增长，您可以设定更严格的目标。<br>
<br><h2>SLA 关键业务价值</h2>当客户对所提供的服务不满意，未能按照相关协议交付时，服务水平协议 (SLA) 就会发挥作用；它可能是一个系统的可靠性。SLA 是产品与其最终用户之间的协议，是与客户就服务可靠性签订的合同，简单表述为 “SLA = SLO + consequences” 。SRE 团队可能不参与定义 SLA 的过程，但是他们需要确保满足 SLO。<br>
<br>SLA 通常包含一段时间内服务正常运行时间的计算。99.9%是三个 9 的正常运行时间，允许每天有 100 万 44s 的停机时间。如上表所示，每周、每月和每年的停机时间分别为 10.1 分钟、43.8分钟和 8.78 小时。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220327/7f06e8ddf5e3c42a162cadd12adfcb66.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/7f06e8ddf5e3c42a162cadd12adfcb66.png" class="img-polaroid" title="2_S8Dhf012E0TOdDCdZ3ANaA.png" alt="2_S8Dhf012E0TOdDCdZ3ANaA.png" referrerpolicy="no-referrer"></a>
</div>
<br>
图二 用9展示SRE<br>
<br>例如，SLA可以保证电信线路 99.9%的正常运行时间；因此，服务只能减少 0.1%的停机时间，超过这一时间将被视为违反SLA，后果将是罚款。<br>
<br><h2>减轻工作负担并控制 SRE 团队的工作量</h2>SRE 团队中总会存在一些手动、乏味的事情需要执行。在您的日常工作中，无论您是软件开发人员还是架构师，您都需要完成自己不喜欢的这类任务。这些通常是手动的、无聊的和重复的任务也可能会导致错误。SRE 团队也必须执行类似的任务。这是 SRE 可以使用他们的开发技能并尽可能消除手动流程的一个实例。让 SRE 花费多达 50% 的时间来改进他们管理的系统是一种很好的做法。<br>
<br><h2>错误预算</h2>错误预算是 SRE 团队用来平衡服务可靠性的工具，计算如下：<br>
<br><pre class="prettyprint">Availability = (Number of good events / Total events) * 100Error budget = (100 — Availability) = failed requests / (successful requests + failed requests)<br>
</pre><br>
误差预算是 100 减去服务的 SLO。99.99%的 SLO 服务有 0.01%的误差预算。<br>
<br>错误预算是 SLO 的另一个例子，其中每个服务都受其带有惩罚条款的服务级别协议的约束。它衡量你有多少空间来满足你的另一个 SLO。例如，如果您有一个服务级别指示器，它显示99.99%的交易必须在 5 秒内提交记账，则只有 0.01%的交易可以超过 5 秒。一个主要版本发布后，你可能会意识到系统运行开始缓慢，突然耗尽你所有的错误预算。请记住，变更是中断的最重要原因，发布是变更的主要来源。如果你一直超出你的误差预算，你将需要重新审视你的一些 SLO 和过程。<br>
<ul><li>您是否在单个版本中引入了太多更改？请保持简单，并将您的版本分成更小的需求变更。</li><li>SLO 是否过于严格？您可能需要协商并放宽 SLO。</li><li>您的发布过程中是否有任何导致问题的手动步骤？尝试引入自动化和测试。</li><li>系统的架构是否容错？硬件故障、网络包丢失、上游或下游应用程序可能会出现异常行为。您的系统架构应该能够容忍这些故障。</li><li>开发团队是否解决了技术债问题？在急于发布新功能时，技术债常常被忽视。</li><li>您的监控和告警是否抓住了主要指标？不断增长的队列规模、网络速度变慢、潜在客户变更过多等都可能导致下游事件。</li><li>您是否定期监控日志并保持其清洁？您的日志中可能存在不会立即导致问题的警告。但是，再加上其他基础设施问题，这些告警可能会导致重大事故。</li></ul><br>
<br><h2>监控分布式系统的四个黄金指标</h2>SRE 的四个黄金指标是构建成功的监控和告警系统的一些基本原则和最佳实践。它们是大型生产应用程序的服务级别目标 (SLO) 的关键部分。他们的目标是帮助识别和修复您系统中的任何潜在问题。他们主动解决您的基础架构问题。<br>
<br>每当您的运维团队需要快速了解问题，并需要近乎实时地跟踪所有服务的延迟、流量、错误和饱和度时。<br>
让我们简要描述每个信号，然后看看如何利用四个关键指标来监控您的系统：<br>
<ul><li><strong>延迟</strong>:延迟是信息发送方和接收方之间的时间延迟，以毫秒(ms)为单位。而原因往往是由于数据包丢失网络拥塞和网络抖动造成的，称为“数据包延迟差异”延迟对客户体验有直接影响，转化为成功请求的延迟和失败请求的延迟。</li><li><strong>流量</strong>: 流量是系统工作量带来的压力。它通过每秒查询数(QPS)或每秒事务数(TPS)来衡量。<br>
企业通过数量来衡量这一点:关键绩效指标(KPI)是在给定时间来到站点的人数。这与商业<br>
价值有直接关系。</li><li><br><strong>错误</strong>: 错误是根据整个系统中发生的错误来衡量的。被认为是服务错误率的重要指标！有两类错误，显式错误，如失败的 HTTP 请求(500 个错误代码，例如)。隐含的错误是成功的响应，但内容错误或响应时间长。</li><li><br><strong>饱和度</strong>: 饱和度定义了服务的过载程度。它衡量系统利用率，强调服务的资源和整体容量。这通常适用于 CPU 利用率、内存使用、磁盘容量和每秒操作数等资源。仪表板和监控警报是帮助您密切关注这些资源并帮助您在容量饱和之前主动调整容量的理想工具。<br>
利用率: 虽然不是公认的“四大黄金信号”的一部分，但值得一提；利用率表明资源或系统有多忙。它以百分比表示，范围从 0 到 100%。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220327/8004a6123458455d030728995dc1cf45.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/8004a6123458455d030728995dc1cf45.png" class="img-polaroid" title="3_liwtmgdyId9mdCvlGeN4iQ.png" alt="3_liwtmgdyId9mdCvlGeN4iQ.png" referrerpolicy="no-referrer"></a>
</div>
<br>
图三 黄金信号<br>
<br>我们都同意这些信号很重要，必须加以监控。那么如何开始？为简单起见，让我们创建一个非常基本的矩阵，首先考虑非常基本和传统的资源，例如 CPU、磁盘、网络和 RAM。<br>
<br>黄金指标的优势在于它能够发出告警、排除故障以及调整和容量规划：<br>
<ul><li>告警可以通知您出现问题</li><li>故障排除可以帮助找到并解决问题的根本原因</li><li>调整和容量规划可以帮助随着时间的推移使用正确的指标、日志和从监控系统收集的跟踪来改善问题<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220327/7d7dadec38de01b78177c78009e422b4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/7d7dadec38de01b78177c78009e422b4.png" class="img-polaroid" title="4_7LOejyAyewQbGHS4CXledw.png" alt="4_7LOejyAyewQbGHS4CXledw.png" referrerpolicy="no-referrer"></a>
</div>
<br>
图四 黄金信号之网络和延迟</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220327/0b7504a557ecba1d6858f4222b64c820.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/0b7504a557ecba1d6858f4222b64c820.png" class="img-polaroid" title="5_r0ehVCHGSakThTtXHVkqZw.png" alt="5_r0ehVCHGSakThTtXHVkqZw.png" referrerpolicy="no-referrer"></a>
</div>
<br>
图五 黄金信号之错误和饱和<br>
<br><h2>风险分析</h2>风险分析定义如下：可能导致违反 SLO 的项目列表<br>
<ul><li>TDD: 检测时间 (time-to-detect)</li><li>TTR: 修复时间 (time-to-resolve)</li><li>Freq/Yr: 每年的错误频率 (frequency of error per year)</li><li>Users: 受影响的用户</li><li>Bad/Yr: 每年有异常的分钟数，相当于错误预算</li></ul><br>
<br>SRE 通过使用错误预算来控制可接受的风险级别和风险并做出明智的决策，从而以受控方式接受风险关于何时应结合 SLI 和 SLO 进行更改。如果需要，SRE 团队可以控制发布周期。<br>
<pre class="prettyprint">Risk = TTD * TTR * (Freq /Yr) * (% of users)<br>
If TTD = 0,<br>
Risk = TTR * (Freq /Yr) * (% of users)<br>
</pre><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220327/9e91020d359f4716a8f6326ddb5b92bf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/9e91020d359f4716a8f6326ddb5b92bf.png" class="img-polaroid" title="6_eXRVj52sgFQf6FylSHOV-w.png" alt="6_eXRVj52sgFQf6FylSHOV-w.png" referrerpolicy="no-referrer"></a>
</div>
<br>
图六 风险分析和度量<br>
<br><h2>监控和告警</h2>监控是观察系统运行方式的一种好方法，告警是系统崩溃或即将崩溃时可以触发的事件。因此，SRE 团队必须构建可靠且有意义的监控系统。我们可以使用一些工具来构建良好的监控系统。Prometheus 是一个开源应用程序，用于事件监控和告警。它在使用 HTTP 拉模型构建的时间序列数据库中记录实时指标。例如，Prometheus 可以配置为从 Hyperledger Fabric 区块链节点提取指标。<br>
您可以配置 Grafana 来构建可视化和仪表板来查询 Prometheus。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220327/73fb4b15f6919c156debc21038fd9d0c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/73fb4b15f6919c156debc21038fd9d0c.png" class="img-polaroid" title="7_n0PLKZ6tiIjySjdlVkZZNQ.png" alt="7_n0PLKZ6tiIjySjdlVkZZNQ.png" referrerpolicy="no-referrer"></a>
</div>
<br>
图七 监控和告警<br>
<br><h2>促进事后分析</h2>当您在组织中构建 SRE 角色时，一个重要但经常被遗忘的方面是事后分析，“事后分析意味着无可指责”。它可以被定义为一个组织从它所犯的错误中吸取教训的机会。故障解决后应尽快进行事后分析以及复盘。在复杂的企业 IT 环境中，组件和应用程序最终会失败，这些失败可能是由于部署错误，最近版本中引入的软件 bug 或 仅仅是硬件故障。将事件的根本原因和短长期修复方案一起归档，并在开发和 SRE 团队中进行传播，对于知识在企业的传承显得很重要。故障的发现可以用作其他系统的预防性修复，也可以作为未来类似事件的参考点。时候分析如果做的好，这些分析应该很容易访问，并且可保留为将来访问的存储库，用于建设内部知识库。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220327/b18020cd8897f8fe8fb7b003468fdee9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220327/b18020cd8897f8fe8fb7b003468fdee9.png" class="img-polaroid" title="8_IA3l1KvBFHN8dNyLlKgzuw.png" alt="8_IA3l1KvBFHN8dNyLlKgzuw.png" referrerpolicy="no-referrer"></a>
</div>
<br>
图 八 使用“四个黄金信号”监控服务的示例 Grafana 仪表板<br>
<br><h2>如何获取一个可靠的服务？</h2>SRE 团队的角色是运营应用程序并通过执行必要的操作来保持系统正常运行。以下是 SRE 在各个阶段执行日常活动的一些策略和工具：<br>
 ### 阶段1: Development ###<br>
<ul><li>流水线 (Pipelining)</li><li>负载和容量考量 (load and scale)</li></ul><br>
<br><h3>阶段2: Pilot</h3><ul><li>监控 (Monitoring)</li><li>轮值和无指责的时候分析 (On-call + blameless postmortems)</li><li>聚合和可检索的日志系统 (Consolidated + searchable logging)</li><li>和产品负责人定期审查 SLI/SLO</li><li>基础设施即代码 (Infrastructure as code)</li></ul><br>
<br><h3>阶段3: Production</h3><ul><li>灰度部署和自动回滚 (Canary deployment + automated rollbacks)</li><li>负载和扩展执行 (Load and scale implementation)</li><li>应用性能监控 (APM) </li><li>混沌引擎 (Chaos engineering)</li></ul><br>
<br><h2>结论</h2>所以，可靠运行是什么意思？<br>
这篇博文试图涵盖构建成功 SRE 团队所需的基本概念和技术。它讨论了如何通过改进的指标、日志、跟踪和仪表板关注可观察性来主动识别和补救事件以及什么是 SLO、SLI 和 SLA。文中了解如何使用错误预算和风险分析等基本工具来指导必要的决策，以平衡您对可靠性的投入与对应用程序功能或其他业务优先级的投入。<br>
最后文中详细阐述了监控分布式系统的四个黄金指标。<br>
<br><strong>原文地址：<a href="https://ernesenorelus.medium.com/building-sre-from-scratch-485e23985bbd">building-sre-from-scratch</a>   翻译：张亚龙</strong>
                                
                                                              
</div>
            