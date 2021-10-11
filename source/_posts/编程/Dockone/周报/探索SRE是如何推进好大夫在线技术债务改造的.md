
---
title: '探索SRE是如何推进好大夫在线技术债务改造的'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/2c23807b247a7b18448f5eef8b594e78.png'
author: Dockone
comments: false
date: 2021-10-11 11:06:54
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/2c23807b247a7b18448f5eef8b594e78.png'
---

<div>   
<br>你是否正面临着产品迭代在不断提速（催进度、要deadline）的同时，服务产线BUG/故障也在变多、有大量用户投诉要响应，每天都要花大把时间去处理突发情况、去救火，而无法把主要精力都投入到正常项目中的糟糕的工作状态？<br>
<br>如何保障网站的高可用是行业内的痛点，也是工程师焦虑源头之一。大家都在积极尝试去解决这类问题，好大夫在线参考Google SRE思想，结合国内其他公司的经验和我们自身的特点，努力落地SRE，并取得了一定的进展。<br>
<br>接下来我们带着问题一起探索SRE：<br>
<ul><li>如何去衡量服务的稳定性？</li><li>服务接口平均耗时30多ms，为何单机QPS提升不上去呢？</li><li>容量规划扩缩容，熔断限流，主要参考的指标是什么？</li><li>频繁处理用户投诉意见建议，先于用户提前发现问题？</li><li>随着时间推移服可用性逐渐下滑，产线BUG频出，如何监控服务可用性？</li><li>技术债务是如何产生的，如何一步步让工程师陷入绝望的困境？</li><li>重要不紧急的技术债务，何去何从，SRE是如何推进技术债务改进？</li><li>是否能提前识别潜在风险，提前解决，让服务保持健康？</li><li>……</li></ul><br>
<br>本系列文章，将尝试带着这些疑问，结合好大夫在线面临的实际问题，一起来探索SRE的落地过程，以及如何用SRE来转变大家的工作思路。<br>
<h3>SRE基础认知</h3><h4>SRE职责</h4>SRE是一个岗位吗？是救火专员吗？需要成为全栈工程师，还是只用盯着监控面板的值班人员？<br>
<br>SRE的职责主要是保障网站的可用性，是一种认知共识，有一套相关方法论，是一种系统化的思维方式。从故障预防，到故障处理，再到故障复盘，形成一个闭环。[注1]<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/2c23807b247a7b18448f5eef8b594e78.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/2c23807b247a7b18448f5eef8b594e78.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从图中可以看出，SRE涵盖不同的阶段，细分的职责也不相同。涉及日志收集，分析，风险识别，熔断限流，告警，通知。同时每个部分又都是相关依赖的，涉及不同的部门和岗位。是一个整体系统，需要各个方向联动保障。我们可以提供一些抓手，让整个体系运转起来，从而保障了整体的可用性。<br>
<h3>SRE体系工作流</h3><ul><li>故障预防：随着微服务的推进，业务模块被划分到不同的独立的服务中。链路请求越来越复杂，依赖的中间件也越来越多。这给服务治理带来了不少的挑战，同时对工程师编程能力要求也越来越高。一方面需要加强工程师面向失败编程的意识，一方面增强框架的治理能力。比如关心RPC请求异常的Code码，失败重试，允许数据中间态的存在，考虑分布式事务一致性，合理的熔断限流策略。</li><li>故障发现：包括框架通用埋点日志（RPC链路/中间件依赖），业务核心链路埋点日志（订单状态流转事件）。日志收集到ClickHouse，通过不同的分析规则生成相应的指标，然后基于Prometheus触发告警，通知到相应的业务方开发。</li><li>故障处理：SRE职能成员（业务开发或系统架构组）收到告警，配合Grafana看板快速定位问题，部分操作可以基于治理平台完成。我们采用预先配置截图的交互方式，将常见的排查问题思路固化到看板截图上，方便后期其他SRE当值人员故障处理。</li><li>故障复盘：及时复盘将排障经验固化到看板中，方便下次告警的时候配合看板截图快速定位问题。针对常见的处理措施，需要集成到治理平台上。</li></ul><br>
<br><h3>SRE面临的挑战</h3><h4>如何衡量服务可用性？</h4>第一种从时长考虑：<br>
<br>MTTR、MTTF、MTBF是体现系统可靠性的重要指标[注2]：<br>
<ul><li>MTTF（Mean Time To Failure，平均无故障时间），指系统无故障运行的平均时间，取所有从系统开始正常运行到发生故障之间的时间段的平均值。MTTF =∑T1/ N；</li><li>MTTR（Mean Time To Repair，平均修复时间），指系统从发生故障到维修结束之间的时间段的平均值。MTTR =∑(T2+T3)/ N；</li><li>MTBF（Mean Time Between Failure，平均失效间隔），指系统两次故障发生时间之间的时间段的平均值。MTBF =∑(T2+T3+T1)/ N</li></ul><br>
<br>很明显：MTBF= MTTF+ MTTR<br>
<br>衡量稳定性：AO = MTBF / (MTBF + MTTF)<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/082c20a66d51ea33f720300045473c49.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/082c20a66d51ea33f720300045473c49.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
第二种从服务质量来看： 请求维度：成功率 = 成功请求数 / 总请求数<br>
<br>这里不能统计单个请求，而是看一段时间的概率分布，比如5xx占比，计算一段时间的5xx占比达到5%，持续10min。这块一般用几个9来衡量，比如3个9，4个9。[注3]<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/c486e0b51aba8bcd910077b41e7b5b2c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/c486e0b51aba8bcd910077b41e7b5b2c.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
设置稳定性目标一般需要考虑：成本，业务容忍度，当前业务的现状。大部分时候4个9目标比3个9目标投入成本要高很多。有些底层的服务，稳定性要求就比一般配套服务的高。比如doctor医生服务的稳定性就需要99.99，它一旦有问题很可能就是波及全站的范围。由于很多历史原因，“大泥球”的服务积累的技术债务会很多。这时候针对这个服务定一个合理的指标，比定一个标准的指标要好很多。  <br>
<br>选择稳定性目标涉及到了测量方法和判断方法的问题，包含三个要素：<br>
<ul><li>衡量指标，比如5xx比例；</li><li>衡量目标，总访问量(QPM)code=200占比小于95%；</li><li>影响时长，QPM其实就是一个聚合指标，也就是说不能简单的计算单次。这在设置告警规则的时候尤为重要，比如持续5分钟，服务sentry报错大于10。</li></ul><br>
<br>这里的衡量指标就是SLI，衡量的目标就是SLO，如果针对服务质量的还有一个SLA。<br>
<br>接下来的问题就是：如何选择合适的SLI，设置合理的SLO。<br>
<br><strong>五大“黄金指标”</strong><br>
<br>前面也谈到了选择衡量指标的问题，服务相关的指标很多，比如CPU负载高了要不要关系，线程数高了要不要关心，QPS量上涨了要不要关心等等。指标不能多，要设置的合理，比如cpu负载高，服务依然能提供稳定的服务，那可以认为服务依然正常。<br>
<br>参照SRE，Google运维解密和赵诚老师的课程，一般参考以下五大“黄金指标”，这些指标常用来制定扩缩容，熔断限流，服务降级的策略：<br><br>
<ol><li>容量，主要有服务QPS/QPM；核心链路QPS/QPM；单机QPS；服务最低存活实例数，资源利用率如CPU负载。</li><li>可用性，主要是指核心链路是否异常；每分钟服务sentry数；服务端6xx/5xx/429/430（限流）占比。</li><li>时延，由于存在长尾效应，平均耗时不一定能反映当前的现状，一般用耗时分布的95线/99线（T95/99）。</li><li>错误率，主要针对用户侧链路，入口网关流量，如Nginx/Kong请求Request的5xx/4xx占比。</li><li>人工介入次数，主要是指程序的鲁棒性；支持自动故障转移；支持幂等；支持失败重试（注意防止雪崩）；减少人工干预的次数。</li></ol><br>
<br>下面给出一些示例：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/c735dd38823d0c3024541bb82f08e2a1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/c735dd38823d0c3024541bb82f08e2a1.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>如果及时发现问题？</h4>选择好了指标，接下来就是要采集数据提炼出想要的指标，绘制监控面板，设置告警规则，触发告警了。这部分组件近几年在快速发展，周边的生态也非常的丰富。我们也经历了从人工 -> 工具化 -> 系统化 -> 平台化进化过程。这部分可以参考之前的文章：《<a href="http://dockone.io/article/1302997">微服务治理平台化探索</a>》。<br>
<br><strong>SRE生态及工具集</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/049dcc227ed06289713464db32d83383.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/049dcc227ed06289713464db32d83383.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
SRE工具集主要从数据源采集，分析生成监控指标，判定这些指标阈值触发告警后，及时响应。主要包括以下6个部分：<br>
<ol><li>数据采集，Java体系的性能消耗比较大，我们选择的是Fluent-bit和gohangout，将收集的数据发布到Kafka。</li><li>数据分析，主要有流式分析和离线分析。我们也是两者相结合的，链路分析基于我们自研的一套TracerLog。我们会分析链路的依赖拓扑关系，找出循环调用，慢接口，慢SQL，双向依赖等常见的风险点。</li><li>数据存储，监控体系用的Prometheus，由于Prometheus原生不支持分布式存储，我们采用ClickHouse做远程存储。针对存储时间长的会采用稀疏存储模式，大量采用物化视图聚合数据。</li><li>监控画像，日志查询主要基于ELK体系，Grafana用于分析后的指标聚合展示，慢慢也衍生出了公司的看板文化。</li><li>告警通知，基于AlertManager的hock模式，我们研发了电话/短信/企业微信通知，让整个处理流程移动化。</li><li>告警响应，为了让日常处理平台化，解放运维成本，我们推出了PaaS云平台，辅助开发日常运维。</li></ol><br>
<br><h3>SRE的切入点：推进技术债务改造</h3>技术债务是如何产生的？ 一般技术债务可以分为三类：<br>
<h4>不良代码积累</h4>这类技术债务很容易想到。随着服务的不断迭代，服务越来越复杂，需求的变更，烂代码的引入，建模的不合理，不可避免的就带来一些技术债务。技术债务增加，服务稳定性越差，越容易写出烂代码，越容易积累更多的技术债务，服务稳定性也就越来越差，从而形成了一个正反馈回路。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/15c1efb31528acd701abf0d5e8e3cc6e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/15c1efb31528acd701abf0d5e8e3cc6e.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
出现这种现象的主要原因有：<br>
<ol><li>工程师的过度自信。认为以后会有时间解决，以完成当前项目功能为导向。然而大部分情况下，项目结束后就没有下文了，加TODO的地方后续也都没人过问。</li><li>工程师过度依赖搜索引擎。有些工程师秉承够用就行，面向“搜索引擎编程”，遇到问题先Google，ctrl+c & ctrl+v 让编程变成了体力劳动。表面上看貌似没啥问题，但不确定性往往就隐藏在这里面。先不说这些第三方的代码质量本身就参差不齐，更可能是破坏最小依赖原则，往往只需要一个组件的某个功能，却引入了整个组件，而这个组件又依赖其他组件。更糟糕的是后续这些依赖没人记得当初是怎么引进来的，不敢去修改，又没人负责升级迭代，从而变成了不定时炸弹（祖传代码）。</li><li>错误的理解敏捷开发。只剩下了表面上的“快速”，需求粗糙、变更过快，疲于应付，没有安排后续重构（整理）时间。</li></ol><br>
<br>程序上的墨菲定律：<br>
<br><blockquote><br>程序的规模会一直不断地增长下去，直到解决线上问题将有限编码时间填满为止。</blockquote>直到这个庞然大物不停的出问题，直到解决一个难题却引入另外一个的难题，才意识到重要的难题一直没时间去做，从而把工程师带入泥潭。<br>
<br>艾森豪威尔矩阵：<br>
<br><blockquote><br>我有两种难题：紧急的和重要的，而紧急的难题永远是不重要的，重要的难题永远是不紧急。——艾森豪威尔[注4]</blockquote><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/fba1b4166c9b303f14f043dc3e446304.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/fba1b4166c9b303f14f043dc3e446304.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
业务部门与研发人员经常犯的共同错误就是将第三优先级的事情提到第一优先级去做。换句话说，他们没有把真正紧急并且重要的功能和紧急但是不重要的功能分开。这个错误导致了重要的事被忽略了，重要的系统架构问题让位给了不重要的系统行为功能。<br>
<br>成效的软件研发团队会迎难而上，毫不掩饰地与所有其他的系统相关方进行平等的争吵。请记住，作为一名软件开发人员，你也是相关者之一。软件系统的可维护性需要由你来保护，这是你角色的一部分，也是你职责中不可缺少的一部分。公司雇你的很大一部分原因就是需要有人来做这件事。<br>
<h4>业务建模 & 业务架构设计</h4>其实更难解决的技术债务往往是来自于业务建模的不合理和业务架构设计缺陷，主要原因有：<br>
<br><strong>1、未理解SOLID设计原则</strong><br>
<ul><li>SRP：单一职责原则；</li><li>OCP：开闭原则；</li><li>LSP：里氏替换原则；</li><li>ISP：接口隔离原则；</li><li>DIP：依赖反转原则。</li></ul><br>
<br>这块就不展开了，下次有机会再讨论。<br>
<br><strong>2、过早的引入不需要的设计</strong><br>
<br>虽然SOA微服务架构是当下主流，新项目一开始就拆分成不同的服务，大家为了适应这个庞杂的服务调用流程不得不额外付出巨大人力成本。好的系统架构是支持渐进式的，沉淀出特定领域逻辑，等到合适的时候再拆分，或者随业务的发展变化还得支持聚合。对采用什么数据库，什么框架不要提前限定死，应该留有更多的余地。<br>
<br><strong>3、边界划分不合理</strong><br>
<br>软件架构设计本身就是一门划分边界的艺术。边界的作用是将软件分割成各种元素，以便约束边界两侧之间的依赖关系。关于边界划分可以参考[注5]。<br>
<br><strong>4、依赖不合理</strong><br>
<br>高层策略依赖低层组件等，这块可以采用DIP设计原则解决。微服务间调用依赖不合理，耦合度高。<br>
<h4>我们的尝试：技术债务识别及优化追踪</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/11bc8f9246c50958bc708f466cecdec9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/11bc8f9246c50958bc708f466cecdec9.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
基于链路分析找出潜在的风险：<br>
<ul><li>慢接口：慢，会严重影响整个服务的吞吐量，最终反映到用户体验上，造成客户流失。这里不采用平均耗时是因为接口延迟满足长尾效应，延迟越大危害越大，所以优先优化延迟高的接口。一般采用接口的延迟百分位第99位(P99)来衡量。目前我们希望优化后端服务P99<100ms，前端服务P99<600ms。</li><li>异常接口：接口错误率，实时反映服务可用性。一般用作熔断降级的指示灯。根据业务容忍度可用性可以设置成3个9或4个9。</li><li>慢SQL：随着业务的迭代，未经优化的SQL可能会产生雪崩。2019年初，由于搜索引擎蜘蛛的抓取大分页数据导致数据库雪崩，影响全站的故障。目前我们会分析慢SQL，收集SQL指纹，给出相应的优化建议。</li><li><br>稳定依赖：依赖关系必须要指向更稳定的方向。根据最小依赖原则，能不依赖就不依赖，能少依赖就少依赖，高层策略不能依赖低层组件。当然完全没依赖那就变成孤岛了没有意义。当下微服务依然是主流， 各服务对依赖的稳定性要求也不一样，基础服务要求比前台服务高。我们可以参考一个指标：<br>
<ul><li>Fan-in：入向依赖，这个指标指代了组件外部类依赖于组件内部类的数量；</li><li>Fan-out：出向依赖，这个指标指代了组件内部类依赖于组件外部类的数量；</li><li>I：不稳定性，I=Fan-out/（Fan-in+Fan-out）。该指标的范围是[0,1],I=0意味着组件是最稳定的，I=1意味着组件是最不稳定的。[注6]</li></ul></li></ul><br>
<br>常见的服务依赖风险点有：<br>
<ul><li>多次依赖，同一条链路下游服务多次调用上游服务不同的接口；</li><li>循环依赖，同一条链路下游服务多次调用上游服务同一个接口；</li><li>双向依赖：同一条链路两个服务互为上下游，相互耦合调用。</li></ul><br>
<br>如果对这部分感兴趣可以查看我们之前的一篇文章： <a href="https://mp.weixin.qq.com/s?__biz=MzUxOTg4NDAxMg==&mid=2247483825&idx=1&sn=2b7b77f81b7dd27c9e0b1180755ac990&chksm=f9f39c32ce841524bc934de8280757aa227d67b725f231a6194414fd342338409343339a382e&mpshare=1&scene=21&srcid=0923DcPSwO9xPKYPpfG9DsZk&sharer_sharetime=1632397680071&sharer_shareid=4a2b708e2f0fccaed635228731ef77a2&version=3.1.8.90238&platform=mac#wechat_redirect">线上系统优化秘笈(Ⅰ) -- 慢接口分析</a>。后续，我们还会对具体如何识别和计算技术债务这块做深入探索，敬请期待。<br>
<h3>小结</h3>这次主要分享SRE基础认知，以及SRE如何以技术债务作为切入点尝试推进系统健康度建设。技术债务一直都是工程师背负的包袱，而这部分对工程师的要求非常高，需要具备长期抗衡意识，这部分的经验积累才是成就架构梦的原始基石，唯有坚持方能蜕变。<br>
<br>参考文献：<br><br>
<ul><li>[注1] 赵诚《SRE实战手册》第01|SRE迷思</li><li>[注2] MTTR/MTTF/MTBF图解</li><li>[注3] 赵诚《SRE实战手册》第02|系统可用性</li><li>[注4] 《架构整洁之道》第2章 艾森豪威尔矩阵</li><li>[注5] 《架构整洁之道》第17章 划分边界</li><li>[注6] 《架构整洁之道》第14章 稳定依赖原则</li></ul><br>
<br>作者简介：方勇，好大夫基础架构部高级工程师，专注于 SRE，微服务、中间件的稳定性和可用性建设，整体负责好大夫服务治理云平台的设计和搭建。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/VMNjQ2T6uhUa21VJrJrwMw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/VMNjQ2T6uhUa21VJrJrwMw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            