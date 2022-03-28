
---
title: '从零开始搭建SRE'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/19e06e38170247cda716a074a1db9692.png'
author: Dockone
comments: false
date: 2022-03-28 10:10:23
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/19e06e38170247cda716a074a1db9692.png'
---

<div>   
<br>【编者的话】Google在10年前创造了SRE这个工种。SRE，Site Reliability Engineering的缩写。其中site是指Website，可以翻译为网站可靠性工程。几年前资深Google SRE Chris Jones等人联合撰写了《Google SRE: How Google runs production systems》，首次向外界解密了Google的生产环境以及整个SRE的方法论。那么如何从零搭建一套SRE体系呢？下文本文主要介绍站点可靠性工程（SRE）以及如何在系统扩展时监控和保持系统快速可靠。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220328/19e06e38170247cda716a074a1db9692.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/19e06e38170247cda716a074a1db9692.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1 构建SRE架构思维导图</em><br>
<br>在云时代，客户体验是所有重要企业的新口号，即使命宣言。客户体验、可用性和可访问性是在端决定的，在这里站点应当始终可用 [24/7/365]。对用户来说，可靠性才是最重要的；一个未使用的应用程序对用户和企业毫无价值。<br>
<br>而如今，每家公司都在努力推动科技变革。公司业务战略都围绕云功能构建。这对他们来说是一项重大的运营挑战。站点性能下降、客户体验的下降都将导致现金、收入和竞争力的损失，并导致传统运营无法应对可观察性的大问题（包括实时监控和告警）。<br>
<br>为什么存在站点可靠性工程（SRE）？敏捷运动提升了跨职能团队之间协作的重要性，这催生了DevOps。DevOps是关于深入研究自己组织的具体问题和挑战。它还与速度、效率和质量有关。从本质上讲，它是一种以实现组织的预期结果的文化、一种运动、一种价值观、原则、方法和实践。这种速度也造成了一定的不稳定性，开发人员的行动速度比以往任何时候都快了，但却给运营团队带来了挑战。IT运营团队没有能力应对这样的速度，这给他们造成了严重的瓶颈和积压，导致生产中产生了不稳定的因素，结果使系统变得不可靠。因此，Google提出了对SRE的要求：“一群能够将工程专业知识应用于运营问题的开发人员。” <br>
<br>SRE是一种规范的DevOps方式。 它是系统管理任务的一种思维方式，侧重于通过缩短交付周期和事件管理生命周期，并通过减少工作量来支持开发人员和运营人员来运营服务的原则。 SRE团队的日常任务包括：<br>
<ul><li>可用性</li><li>延迟</li><li>性能</li><li>效率</li><li>变更管理</li><li>监控和告警</li><li>应急响应</li><li>事件响应</li><li>准备工作</li><li>容量规划</li></ul><br>
<br><h3>那么，什么是站点可靠性工程（SRE）？</h3>SRE团队的角色是运营在生产“关键任务系统”中应用程序，并执行任何必要的事情来保持站点正常运行。它通常被定义为从事运维工作的软件工程师。SRE团队负责维护和建立其系统的服务水平指标（SLI）、目标（SLO）、协议（SLA）和错误预算，并确保满足这些指标。他们预计将花费一定的时间进行运营工作（确保系统按期工作）并改进他们管理的系统。SRE专注于编写软件来自动化流程并减少“脏活累活”的工作量。这个“脏活累活”就是目前还未实现系统自动化并且需要手动处理的工作。<br>
<br>SRE 的战略目标是：<br>
<ul><li>使部署更加容易</li><li>提高或维持正常运行时间</li><li>针对应用性能去建设可视化能力</li><li>设置SLI's和SLO's以及错误预算</li><li>通过承担计算风险来提高速度</li><li>消除手动操作任务</li><li>降低故障成本以缩短新功能的周期时间</li></ul><br>
<br><h3>SLI和SLO</h3>服务水平目标（SLO）只是SRE团队与产品所有者或业务线（LOB）之间的协议。指标在很大程度上取决于团队管理的系统的性质。服务水平指标（SLIs）是为系统定义的量化指标，也称为“我们正在度量的内容”。这些指标取决于所管理的系统。对于典型的Web应用程序，这些指标可能是可用性、请求延迟或错误率。但是，例如Hyperledger Fabric区块链应用程序可能会使用每秒背书和分类帐提交率来衡量网络的吞吐量。<br>
<br>SRE团队最终将管理多个系统。跨各种应用程序定义一组标准的<code class="prettyprint">服务水平指标</code>将帮助团队标准化整个堆栈的监控、日志记录和自动化。<br>
<br>SLO是系统应该运行的“应该有多好”的目标值或范围。这些是之前定义的SLI的预期操作值。例如，区块链网络必须以不到5秒的端到端延迟来维持50到100个事务提交速率的事务吞吐量。当然这也有可能存在过度设计SLI和SLO的倾向。一开始就让它们保持简单是很重要的。随着你对系统的了解随着时间的推移而增长，你可以设定更严格的目标。<br>
<h3>SLA关键业务价值</h3>当客户对所提供的服务不满意，未能按照相关协议交付时，服务水平协议（SLA）就会发挥作用；它可能是一个系统的可靠性。SLA是产品与其最终用户之间的协议，是与客户就服务可靠性签订的合同，简单表述为“SLA = SLO + consequences”。SRE团队可能不参与定义SLA的过程，但是他们需要确保满足SLO。<br>
<br>SLA通常包含一段时间内服务正常运行时间的计算。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220328/933f5622a81f9d64bc4e188fddf4c08a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/933f5622a81f9d64bc4e188fddf4c08a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图二 用9展示SRE</em><br>
<br>99.9%是三个9的正常运行时间，允许每天有1.44s的停机时间。如上表所示，每周、每月和每年的停机时间分别为10.1分钟、43.8分钟和8.78小时。<br>
<br>例如，SLA可以保证电信线路99.9%的正常运行时间；因此，服务只能减少0.1%的停机时间，超过这一时间将被视为违反SLA，后果将是罚款。<br>
<h3>减轻工作负担并控制SRE团队的工作量</h3>SRE团队中总会存在一些手动、乏味的事情需要执行。在你的日常工作中，无论你是软件开发人员还是架构师，你都需要完成自己不喜欢的这类任务。这些通常是手动的、无聊的和重复的任务也可能会导致错误。SRE团队也必须执行类似的任务。这是SRE可以使用他们的开发技能并尽可能消除手动流程的一个实例。让SRE花费多达50%的时间来改进他们管理的系统是一种很好的做法。<br>
<h3>错误预算</h3>错误预算是SRE团队用来平衡服务可靠性的工具，计算如下：<br>
<pre class="prettyprint">Availability = (Number of good events / Total events) * 100<br>
<br>
Error budget = (100 — Availability) = failed requests / (successful requests + failed requests)<br>
</pre><br>
误差预算是100减去服务的SLO。99.99%的SLO服务有0.01%的误差预算。<br>
<br>错误预算是SLO的另一个例子，其中每个服务都受其带有惩罚条款的服务级别协议的约束。它衡量你有多少空间来满足你的另一个SLO。例如，如果你有一个服务级别指示器，它显示99.99%的交易必须在5秒内提交记账，则只有0.01%的交易可以超过5秒。一个主要版本发布后，你可能会意识到系统运行开始缓慢，突然耗尽你所有的错误预算。请记住，变更是中断的最重要原因，发布是变更的主要来源。如果你一直超出你的误差预算，你将需要重新审视你的一些SLO和过程。<br>
<ul><li>你是否在单个版本中引入了太多更改？请保持简单，并将你的版本分成更小的需求变更。</li><li>SLO是否过于严格？你可能需要协商并放宽SLO。</li><li>你的发布过程中是否有任何导致问题的手动步骤？尝试引入自动化和测试。</li><li>系统的架构是否容错？硬件故障、网络包丢失、上游或下游应用程序可能会出现异常行为。你的系统架构应该能够容忍这些故障。</li><li>开发团队是否解决了技术债问题？在急于发布新功能时，技术债常常被忽视。</li><li>你的监控和告警是否抓住了主要指标？不断增长的队列规模、网络速度变慢、潜在客户变更过多等都可能导致下游事件。</li><li>你是否定期监控日志并保持其清洁？你的日志中可能存在不会立即导致问题的警告。但是，再加上其他基础设施问题，这些告警可能会导致重大事故。</li></ul><br>
<br><h3>监控分布式系统的四个黄金指标</h3>SRE的四个黄金指标是构建成功的监控和告警系统的一些基本原则和最佳实践。它们是大型生产应用程序的服务级别目标（SLO）的关键部分。他们的目标是帮助识别和修复你系统中的任何潜在问题。他们主动解决你的基础架构问题。<br>
<br>每当你的运维团队需要快速了解问题，并需要近乎实时地跟踪所有服务的延迟、流量、错误和饱和度时。<br>
<br>让我们简要描述每个信号，然后看看如何利用四个关键指标来监控你的系统：<br>
<ul><li><strong>延迟</strong>：延迟是信息发送方和接收方之间的时间延迟，以毫秒（ms）为单位。而原因往往是由于数据包丢失网络拥塞和网络抖动造成的，称为“数据包延迟差异”延迟对客户体验有直接影响，转化为成功请求的延迟和失败请求的延迟。</li><li><strong>流量</strong>：流量是系统工作量带来的压力。它通过每秒查询数（QPS）或每秒事务数（TPS）来衡量。企业通过数量来衡量这一点：关键绩效指标（KPI）是在给定时间来到站点的人数。这与商业价值有直接关系。</li><li><strong>错误</strong>：错误是根据整个系统中发生的错误来衡量的。被认为是服务错误率的重要指标！有两类错误，：显式错误，如失败的HTTP请求（500个错误代码，例如）；隐含错误是成功的响应，但内容错误或响应时间长。</li><li><strong>饱和度</strong>：饱和度定义了服务的过载程度。它衡量系统利用率，强调服务的资源和整体容量。这通常适用于CPU利用率、内存使用、磁盘容量和每秒操作数等资源。仪表板和监控警报是帮助你密切关注这些资源并帮助你在容量饱和之前主动调整容量的理想工具。</li><li><strong>利用率</strong>：虽然不是公认的“四大黄金信号”的一部分，但值得一提；利用率表明资源或系统有多忙。它以百分比表示，范围从0到100%。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220328/7407602af370ce2e1931bd457469e312.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/7407602af370ce2e1931bd457469e312.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图三 黄金信号</em><br>
<br>我们都同意这些信号很重要，必须加以监控。那么如何开始？为简单起见，让我们创建一个非常基本的矩阵，首先考虑非常基本和传统的资源，例如CPU、磁盘、网络和RAM。<br>
<br>黄金指标的优势在于它能够发出告警、排除故障以及调整和容量规划：<br>
<ul><li>告警可以通知你出现问题</li><li>故障排除可以帮助找到并解决问题的根本原因</li><li>调整和容量规划可以帮助随着时间的推移使用正确的指标、日志和从监控系统收集的跟踪来改善问题</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220328/c01d6666b34a792ff3aafb99fd5f189f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/c01d6666b34a792ff3aafb99fd5f189f.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图四 黄金信号之网络和延迟</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220328/d67cd2eff9e04e85f93fd778f5949a88.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/d67cd2eff9e04e85f93fd778f5949a88.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
图五 黄金信号之错误和饱和<br>
<h3>风险分析</h3>风险分析定义如下：可能导致违反SLO的项目列表<br>
<ul><li>TDD：检测时间（time-to-detect）</li><li>TTR：修复时间（time-to-resolve）</li><li>Freq/Yr：每年的错误频率（frequency of error per year）</li><li>Users：受影响的用户</li><li>Bad/Yr：每年有异常的分钟数，相当于错误预算</li></ul><br>
<br>SRE通过使用错误预算来控制可接受的风险级别和风险并做出明智的决策，从而以受控方式接受风险关于何时应结合SLI和SLO进行更改。如果需要，SRE团队可以控制发布周期。<br>
<pre class="prettyprint">Risk = TTD * TTR * (Freq /Yr) * (% of users)<br>
<br>
If TTD = 0,<br>
<br>
Risk = TTR * (Freq /Yr) * (% of users)<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220328/92ff87e5b75dbe843b82c1a9889c2a54.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/92ff87e5b75dbe843b82c1a9889c2a54.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图六 风险分析和度量</em><br>
<h3>监控和告警</h3>监控是观察系统运行方式的一种好方法，告警是系统崩溃或即将崩溃时可以触发的事件。因此，SRE团队必须构建可靠且有意义的监控系统。我们可以使用一些工具来构建良好的监控系统。Prometheus是一个开源应用程序，用于事件监控和告警。它在使用HTTP拉模型构建的时间序列数据库中记录实时指标。例如，Prometheus可以配置为从Hyperledger Fabric区块链节点提取指标。<br>
你可以配置Grafana来构建可视化和仪表板来查询Prometheus。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220328/a1aed475c496b21e571ffb1884e7033c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/a1aed475c496b21e571ffb1884e7033c.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图七 监控和告警</em><br>
<h3>促进事后分析</h3>当你在组织中构建SRE角色时，一个重要但经常被遗忘的方面是事后分析，“事后分析意味着无可指责”。它可以被定义为一个组织从它所犯的错误中吸取教训的机会。故障解决后应尽快进行事后分析以及复盘。在复杂的企业IT环境中，组件和应用程序最终会失败，这些失败可能是由于部署错误，最近版本中引入的软件bug或仅仅是硬件故障。将事件的根本原因和短长期修复方案一起归档，并在开发和SRE团队中进行传播，对于知识在企业的传承显得很重要。故障的发现可以用作其他系统的预防性修复，也可以作为未来类似事件的参考点。事后分析如果做的好，这些分析应该很容易访问，并且可保留为将来访问的存储库，用于建设内部知识库。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220328/986a781babc8765b05b40c6c9d2292cf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220328/986a781babc8765b05b40c6c9d2292cf.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图八 使用“四个黄金信号”监控服务的示例Grafana仪表板</em><br>
<h3>如何获取一个可靠的服务？</h3>SRE团队的角色是运营应用程序并通过执行必要的操作来保持系统正常运行。以下是SRE在各个阶段执行日常活动的一些策略和工具：<br>
<h4>阶段1：Development</h4><ul><li>流水线（Pipelining（</li><li>负载和容量考量（load and scale）</li></ul><br>
<br><h4>阶段2：Pilot</h4><ul><li>监控（Monitoring）</li><li>轮值和无指责的时候分析（On-call + blameless postmortems）</li><li>聚合和可检索的日志系统（Consolidated + searchable logging）</li><li>和产品负责人定期审查 SLI/SLO</li><li>基础设施即代码（Infrastructure as code）</li></ul><br>
<br><h4>阶段3：Production</h4><ul><li>灰度部署和自动回滚（Canary deployment + automated rollbacks）</li><li>负载和扩展执行（Load and scale implementation）</li><li>应用性能监控（APM）</li><li>混沌引擎（Chaos engineering）</li></ul><br>
<br><h3>结论</h3>所以，可靠运行是什么意思？这篇博文试图涵盖构建成功SRE团队所需的基本概念和技术。讨论了如何通过改进的指标、日志、跟踪和仪表板关注可观察性来主动识别和补救事件以及什么是SLO、SLI和SLA。了解如何使用错误预算和风险分析等基本工具来指导必要的决策，以平衡你对可靠性的投入与对应用程序功能或其他业务优先级的投入。最后文中详细阐述了监控分布式系统的四个黄金指标。<br>
<br><strong>原文链接：<a href="https://ernesenorelus.medium.com/building-sre-from-scratch-485e23985bbd">Building SRE from Scratch</a>（翻译：张亚龙）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            