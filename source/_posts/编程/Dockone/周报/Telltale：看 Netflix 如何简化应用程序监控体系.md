
---
title: 'Telltale：看 Netflix 如何简化应用程序监控体系'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210619/e4dd358d5423da36a283f789db9cddba.png'
author: Dockone
comments: false
date: 2021-06-19 07:10:51
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210619/e4dd358d5423da36a283f789db9cddba.png'
---

<div>   
<br>【编者的话】本文阐述了 Netflix 的系统监控实践：自研 Telltale，成功运行并监控着 Netflix 100 多个生产应用程序的运行状况。<br><br>
<h3>难忘的经历</h3>相信很多运维人都有过这样的经历：监控系统某个指标超过阈值，触发告警。大半夜里，你被紧急召唤。  <br>
<br>半睁着眼，你满脸疑惑：“系统真出问题了吗，还是仅仅需要调整下告警？上一次有人调整我们的告警阈值是在什么时候？有没有可能是上游或者下游的服务出现了问题？”  <br>
<br>鉴于这是一次非常重要的应用告警，因此你不得不从床上爬起来，迅速打开电脑，然后浏览监控仪表盘来追踪问题源头。  <br>
<br>忙了半天，你还没确认这个告警是来自于系统的问题，但也意识到，从海量数据中寻找线索时，时间正在流逝。你必须尽快定位告警的原因，并祈祷系统稳定运行。<br>
<br>对我们的用户来讲，稳健的 Netflix 服务至关重要。当你坐下来看《养虎为患》时，你肯定希望它能顺利播放。<br>
<br>多年来，我们从经常在深夜被召唤的工程师那里了解到应用程序监控的痛点：<br><br>
<ul><li>过多的告警</li><li>太多滚动浏览的仪表盘  </li><li>太多的配置  </li><li>过多的维护</li></ul><br>
<br><h3>Telltale</h3>我们的流媒体团队需要一个全新的监控系统，可以让团队成员快速地诊断和修复问题；因为在系统告警的紧急情况下，每一秒都至关重要！  <br>
<br>我们的 Node 团队 需要一个仅需一小撮人就能运维大型集群的系统。因此，我们构建了 Telltale。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210619/e4dd358d5423da36a283f789db9cddba.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210619/e4dd358d5423da36a283f789db9cddba.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Telltale 监控时间轴</em><br>
<br>Telltale 的特性如下：<br>
<br><strong>汇集监控数据源，创建整体监控视图</strong>：Telltale 汇集了各种监控数据源，从而能创建关于应用程序运行状况的整体监控视图。<br>
<br><strong>多维度判断应用程序的健康状况</strong>：Telltale 可以通过多个维度判断一个应用程序的健康情况，而无需根据单一指标频繁调整告警阈值。<br>
<br><strong>及时告警</strong>：因为我们知道应用程序在什么情况下是正常的，所以能在应用程序有异常趋势时及时通知应用程序的所有者。<br>
<br><strong>显示关键数据</strong>：指标是了解应用程序运行状态的关键。但很多时候，你拥有太多的指标、太多的图表以及太多的监控仪表盘。而 Telltale 仅显示应用程序中有用的相关数据及其上游和下游服务的数据。<br>
<br><strong>用颜色区分问题的严重程度</strong>：我们使用不同的颜色来表示问题的严重程度（除选择颜色之外，还可以让 Telltale 显示不同的数字），以便运维人员一眼就能判断出应用程序的运行状况。<br>
<br><strong>高亮提示</strong>：我们还会对一些监控事件进行高亮提示，比如局部区域的网络流量疏散及就近的 服务部署，这些信息对于全面了解服务的健康情况至关重要，尤其是在真正发生系统故障的情况下。<br>
<br>这就是我们的 Telltale 监控。它现已成功运行并提供监控服务，监控着 Netflix 100 多个生产应用程序的运行状况。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210619/74b462260a65f345fb6332e64d587ceb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210619/74b462260a65f345fb6332e64d587ceb.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>应用程序健康评估模型</h3>微服务并非是孤立存在和运行的。它需要特定的依赖，与其他服务进行数据交互，甚至位于不同的 AWS 区域。<br>
<br>上面的调用图是一个相对简单的图，其中涉及许多服务，实际的调用链可能会更深更复杂。  <br>
<br>一个应用程序是系统生态的一部分，它的运行状态可能会受到相关属性变化的微弱影响，也有可能会受到区域范围内某些事件的影响从而发生根本性改变。  <br>
<br>canary 的启动可能会对应用程序产生一定影响。在一定程度上，上游或下游服务的部署同样也可以带来一定的影响。  <br>
<br>Telltale 通过使用多个维度的数据源构建一个不断自我优化的模型来监控应用程序的健康度：<br>
<ul><li>Atlas 时序指标</li><li>区域网络流量疏散</li><li>Mantis 实时流数据</li><li>基础架构变更事件</li><li>Canary 部署及使用</li><li>上、下游服务的运行状况</li><li>表征 QoE 的相关指标</li><li>告警平台发出的报警</li></ul><br>
<br>不同的数据源对应用程序健康度的影响权重不同。例如，与错误率增加相比，响应时间的增加对应用程序的影响要小很多。  <br>
<br>错误代码有很多，但是某些特定的错误代码的影响要比其他错误代码的影响大。在服务下游部署 canary 可能不如在上游部署带来的效果明显。  <br>
<br>区域网络流量转移意味着某个区域的网络流量降为零而另一个区域的网络流量会加倍。  <br>
<br>你可以感受下不同的指标对于监控的影响。监控指标的具体含义决定了我们应该如何科学有效地使用它来进行监控。  <br>
<br>在构建应用程序健康状况视图时，Telltale 考虑了所有这些因素。应用程序健康评估模型是 Telltale 的核心。<br><br>
<h3>智能监控</h3>每个服务运维人员都知道告警阈值调整的难度。将阈值设置得太低，你会收到大量虚假告警。  <br>
<br>如果过度补偿并放宽告警阈值，就会错过重要的异常警告。这样导致的最终结果是对告警缺乏信任。Telltale 可以帮助你免除不断调整相关配置的繁琐工作。  <br>
<br>通过提供准确的和严格管理的数据源，我们能让应用程序所有者的设置和配置过程变得更加容易。  <br>
<br>这些数据源通过按照一定的组合应用到程序的配置中，以实现最常见的服务类型配置。  <br>
<br>Telltale 可以自动追踪服务之间的依赖关系，以构建应用程序健康评估模型中的拓扑。  <br>
<br>通过数据源管理以及拓扑监测，在不用付出很大的努力情况下就能使配置保持最新状态。那些需要手动实践的一些场景仍然支持手动配置和调整。  <br>
<br>没有任何一个独立的算法可以适用我们所有的监控场景。因此，我们采用了混合算法，包括统计算法、基于规则的算法和机器学习算法。  <br>
<br>不久后，我们将在 Netflix Tech Blog 上发表一篇针对我们监控算法的文章。  <br>
<br>Telltale 还具有分析器，可用于趋势探测或内存泄漏监测。智能监控意味着我们的用户可以信赖我们的监控结果。  <br>
<br>这表明故障发生时，用户能更快地定位和解决系统异常问题。<br><br>
<h3>智能告警</h3>智能监控必然会促进智能告警。当 Telltale 检测到应用程序中的运行异常时，就会产生异常事件。  <br>
<br>团队可以选择通过 Slack、电子邮件或 PagerDuty（均由我们的内部告警系统提供支持）进行告警。  <br>
<br>如果该异常问题是由上游或下游系统引起的，则 Telltale 的上下文感知路由会提醒服务对应的维护团队。  <br>
<br>智能告警还意味着运维团队针对特定异常只会收到一个通知，也就是说，告警风暴已经成为过去式。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210619/9dd13b52063ac05522ef55f51917bd0b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210619/9dd13b52063ac05522ef55f51917bd0b.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Slack 中的 Telltale 通知示例</em><br>
<br>在系统出现问题时，掌握准确的信息至关重要。我们的 Slack 告警程序还会启动一个包含有关事件上下文信息的线程，提供 Telltale 识别到的异常问题信息及问题产生的原因。  <br>
<br>正确的上下文可以方便我们了解应用程序的当前状态，以便值班运维的工程师能有针对性的定位和修复问题。  <br>
<br>异常告警事件会不断发展而且拥有自己的生命周期，因此及时更新事件状态至关重要。告警异常是好转了还是恶化了？是否要考虑新的监控信息或事件？  <br>
<br>Telltale 在当前事件发生改变时会更新 Slack 线程。系统返回正常状态后，该线程将被标记为“已解决”，因此用户一眼就能知道哪些异常事件正在处理中，哪些异常事件已成功修复。  <br>
<br>这些 Slack 线程不仅仅适用于 Telltale。团队还可以用它们来共享有关事件的其他数据，方便进一步观察、理论分析和讨论。  <br>
<br>异常信息数据和讨论全部集中在一个线程中，方便达成针对当前异常的共识，有利于更快提出问题的解决方案以及异常事件的事后分析。  <br>
<br>我们致力于提高 Telltale 告警的质量。一种方法是向我们的用户学习。因此，我们在 Slack 消息中提供了反馈按钮。  <br>
<br>用户可以告诉我们以后某些情况不需要再发生告警，或提供某些告警不合理的原因。智能告警意味着用户可以信赖我们的告警。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210619/98c1bea7f0ae7d67db399ad7244898c9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210619/98c1bea7f0ae7d67db399ad7244898c9.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>在 Slack 的 Telltale 通知中描述异常详细信息的一个示例</em><br>
<br>为什么我的应用服务运行状态欠佳？各种类型的监控数据、应用程序相关知识以及跨多种服务数据的相关性，有助于 Telltale 检测分析应用程序运行健康度降低的原因。  <br>
<br>这些原因包括实例异常、相关依赖的监测和部署异常、数据库异常或者网络流量高峰等。突出高亮显示这些可能的原因可以帮助运维人员节省大量宝贵的时间。<br><br>
<h3>异常事件管理</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210619/8231c4e8ef20f94697c40ad7bb25375e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210619/8231c4e8ef20f94697c40ad7bb25375e.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Telltale 异常事件摘要的一个示例</em><br>
<br>当 Telltale 发送告警时，它还会创建一个快照，其中引用了不正常的监控信号数据。随着新监控信息的到来，会将其添加到此快照中。  <br>
<br>这简化了团队的很多事后审查流程。当需要复查过去的异常问题时，“应用程序事件摘要”功能可以从各个方面显示当前的问题，包括一些关键指标，比如总停机时间和 MTTR（平均解决时间）。  <br>
<br>我们希望帮助我们的团队了解更多的异常事件的模式，以便提高我们服务的整体可用性。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210619/ce79d2ac47082c0ddfb556733f5c3b38.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210619/ce79d2ac47082c0ddfb556733f5c3b38.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>集群视图下将相似异常事件分组</em><br>
<h3>部署监控</h3>可以看出，Telltale 的应用程序健康评估模型及其智能监控功能非常强大，所以我们也会将其应用于安全部署方面。我们从开放源码交付平台 Spinnaker 开始测试。  <br>
<br>随着 Spinnaker 逐渐推出新版本，我们使用 Telltale 连续监监控运行新版本实例的运行状态。  <br>
<br>持续监控意味着新部署在问题出现时能自行停止并进行回滚操作。这意味着部署存在问题时的影响半径较小，持续时间更短。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210619/e836281ccd658cdb826fd0bb5cb47f35.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210619/e836281ccd658cdb826fd0bb5cb47f35.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>持续优化</h3>在复杂的系统中，运行微服务非常具有挑战性。Telltale 的智能监控和告警功能可以帮助我们运维人员提高系统可用性、降低运维人员的劳动强度并减少工作人员大半夜被叫醒的频率。  <br>
<br>我们为 Telltale 做到的这些功能提升感到高兴。但是远没有结束，我们仍在不断探索新算法，以提高告警的准确性。  <br>
<br>我们将在以后的 Netflix Tech Blog 文章中详细介绍我们的工作进展。我们仍然在对应用程序健康评估模型进行进一步评估和改进。  <br>
<br>我们相信服务运行日志和跟踪数据中会包含更多有价值的信息，这样我们就能采集到更有用的指标数据。我们很期待与平台其他团队进行合作，共同开发这些新功能。  <br>
<br>将新应用监控引入 Telltale 可以享受到很好的服务体验，但是无法很好的进行扩展，所以我们绝对可以优化和提高自服务的用户界面。  <br>
<br>我们确信，有更好的启发式方法能帮助用户找出影响服务健康度的一些因素。Telltale 简化了应用程序的监控。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/ZnpYMy2rupJS9hHA5WWyew" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/ZnpYMy2rupJS9hHA5WWyew</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            