
---
title: '通过产品运营驱动SRE落地'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/e37d85b7622fbd20124236c2b67104ea.png'
author: Dockone
comments: false
date: 2021-05-29 05:47:58
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/e37d85b7622fbd20124236c2b67104ea.png'
---

<div>   
<br>这几年SRE越来越火，几乎成了保障可用性的“银弹”，Google SRE已经是目前稳定性领域的最佳实践，SRE也成为稳定性的代名词。SRE这么厉害，那么我们应该如何在企业落地SRE呢？<br>
<br>去年在极客时间学习了赵成老师的《SRE实战手册》课程受益匪浅，做好系统可用性保障是一个很复杂的事情，指望某个岗位的人具备所有的知识和技能显然是不太现实的，所以我们要做的是让合适的人做合适的事情。<br>
<br>接下来就给大家分享一下我们如何通过产品运营的方式来保障系统可用性的。<br>
<h3>设定系统可用性目标</h3>谈运营首先就要谈目标，前面已经说了我们要让合适的人做合适的事，所以目标分为了三个：<br>
<ol><li>99%的工程月可用性>99.95%</li><li>工程月可用性>99.95%（非基础设施故障）</li><li>基础设施月可用性>99.99%</li></ol><br>
<br>第一个目标是给我们IT运营团队的，他们的核心目标是保障平台的整体稳定性；<br>
<br>第二个目标是给到工程负责人的，解铃还须系铃人，工程的问题只有工程负责人最清楚；<br>
<br>第三个目标是给运维团队的，他们需要保障基础设施和基础组件的稳定性。<br>
<h3>可用性产品设计</h3>目标确定了，我们就需要一款产品来量化这些指标，这里就要提到SLI（Service Level Indicator），本质就是我们选择哪些指标来衡量系统的稳定性。<br>
<br>Google提供了一套基于VALET设计出来的SLI和SLO的Dashboard样例：<a href="https://landing.google.com/sre/workbook/chapters/slo-document" rel="nofollow" target="_blank">https://landing.google.com/sre ... ument</a><br>
<br>这个原则比较复杂，因为我们的业务都是http服务，所以选择了比较简单和直接的两个指标来衡量：<br>
<ol><li>状态码（5xx表示服务不可用）</li><li>响应时长（响应时长>x ms）</li></ol><br>
<br>有了SLI还不够，我们还需要明确可用性的主体，以及对于不可用的接受度。<br>
<br>对于工程，我们以域名为主体，分析每个域名的不可用状态码和响应超时的请求，根据程度不同我们定义了四个等级：<br>
<ul><li>P3：不可用次数/总次数>a%</li><li>P2：不可用次数/总次数>b%</li><li>P1：不可用次数/总次数>c%</li><li>P0：不可用次数/总次数>d%</li></ul><br>
<br>计算周期为一分钟一次，对过去一分钟的请求日志进行分析（这里我们使用的ElasticSearch）P1-P3等级仅进行告警，达到P0则表示此分钟服务不可用。<br>
<br>当我们用这个逻辑跑完数据的时候发现，60%的域名至少会触发P3及以上告警，20%的域名会触发P0告警。工程的可用性难道真的如此差劲吗？<br>
<br>我们对这些告警进行了分析，主要有以下几类情况导致：<br>
<ol><li>请求总量小，恰巧遇到慢或者5xx；</li><li>安全扫描触发大量5xx；</li><li>使用了长连接（websocket）；</li><li>超时阈值使用的response_time（这个时间包含网络耗时）；</li><li>对于超时阈值设置过低；</li><li>流量陡增导致响应变慢；</li><li>个别域名或接口逻辑复杂请求耗时较长；</li><li>同一个工程使用多个域名提供服务（重复告警）。</li></ol><br>
<br>针对这些情况，我们对产品进行了大量的优化，具体有：<br>
<ol><li>域名分级治理，我们把域名按照访问量分为4个等级（核心、重要、一般、普通），普通域名仅使用5xx数量来衡量；</li><li>针对安全扫描一方面我们把安全团队扫描器的IP加入白名单，另外我们在排查的时候发现公司某些团队使用的框架路由有问题，当访问不存在的路由的时候就会出现5xx，所以协调资源对相关框架进行了优化，大幅减少了扫描导致的5xx；</li><li>引入白名单机制，对于一些正常的超时进行白名单设置，白名单支持IP、域名、URL_PAHT、超时长等维度；</li><li>前期阈值较低，实际情况并不理想，所以我们适当提高了超时阈值。（过多的告警无法让运营团队开展工作）；</li><li>使用upstream_response_time替代response_time计算耗时，排除网络不稳定导致的超时；</li><li>针对流量陡增导致的超时，我们将限流功能的配置权限开放给到工程负责人，他们根据自己的压测情况合理的设置限流策略，同时把服务器资源配置权限也给到他们，他们可以根据情况自助完成扩缩容操作。</li></ol><br>
<br>经过这一系列的优化和白名单配置，整体告警数量有了非常明显的下降。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/e37d85b7622fbd20124236c2b67104ea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/e37d85b7622fbd20124236c2b67104ea.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>基础设施监控和故障自愈</h3>运维部门是监控最多的部门，但是告警的准确率并不是很高，在每次复盘的时候经常会发现基础设施有告警但是由于告警较多或者告警等级过低被忽略。<br>
<br>所以为了完成目标，需要重新梳理关键指标并设置合理的告警等级。<br>
<br>对于基础设置监控重点4个方面：<br>
<ul><li>网络，对于公网网络最常用的检测手段就是拨测，我们使用第三方拨测服务对出口IP进行ping检查，当2个以上节点丢包超过一定阈值或者可用性不是100%的时候，通过DNSPod自动切换备用线路IP。所以网络故障我们基本可以在2分钟内完成切换，但受限于DNS缓存影响，真实的用户影响往往比这个时间略长。</li><li>资源，我们目前大量使用容器，所以重要关注宿主的CPU、内存、IO等监控就可以了，对于应用的Pod，我们所有应用都是多个节点，即使宿主故障也可以通过工具快速迁移到其他节点，单节点故障Kubernetes会有自动驱逐和重建机制，基本很少故障或者人工介入。</li><li>中间件，我们使用的中间件主要由Redis、RabbitMQ、Kafka，针对这些中间件除了监控基础指标以为还监控了很多具体的指标，比如服务端口状态、同步状态、线程数、gc情况、消费积压（我们基于小米开源的Open-Falcon，二次开发的组件进行监控）</li><li>数据库，对数据库单个实例的连接数、QPS、show processlist运行中的数量、主从延迟、实例重启等标进行监控。并对重启和运行中数量设置较高等级（数据库挂了或者有慢SQL）如果数据库故障会自动触发HA负载到没有故障的实例，如果出现大量积压SQL，DBA会介入，使用工具批量KILL（服务降级，无数次的经验告诉我们不kill都得死）</li></ul><br>
<br>从运维的角度来讲，这些故障是不可控的，所以在故障发生的时候需要有快速的恢复手段来减少不可用时长。我们内部对于故障恢复称之为“故障恢复三扳斧，回滚、重启、切流量”。<br>
<h3>持续运营</h3>经过2个月的产品优化，告警基本比较准确的反应了真实的可用性情况。所以接下来就开始了运营工作，推进业务整改。<br>
<br>为了让整改可以落地，IT运营部门制定了《可用性告警处理规范》对相关要求和处罚做了明确的规定，把可用性是否达标作为技术人员的考核指标，如果长期可用性不达标会对技术人员的绩效和职级晋升产生影响。对于考核我们引入了一套较为复杂的扣分规则，一方面可以保证有效的推动大家整改，另外也不至于很多人因此受到影响而产生反感。<br>
<br>IT运营人员按周关注可用性较差的项目，进行通报督促各业务单元进行整改，还会对故障的原因进行事故复盘，避免同一类故障重复出现。<br>
<br>可用性周报如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/378e04bcb8040ef95a3b555318882f1a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/378e04bcb8040ef95a3b555318882f1a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最近一个月告警情况如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/60d9c4e73e8aba7360462c3d75feb812.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/60d9c4e73e8aba7360462c3d75feb812.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>产品工具赋能</h3>如果只是单纯的告警，不给研发人员提供相应故障分析和排查工具，他们也无法快速定位和解决这些问题。针对这个情况，我们的业务运维和开发人员进行多次沟通、并总结过去的排查故障的经验，总结了一套比较通用的问题排查方法。<br>
<br>1、通过可用性告警确定故障的类型和路径；（一方面通过告警直接发送相关信息，另外也可以通过ELK自助查询和分析）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/33af10b9db3cc7c8525de721ae0fb04b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/33af10b9db3cc7c8525de721ae0fb04b.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
2、通过APM分析调用链路（早在2016年公司就引入了基于Pinpoint的APM系统）<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/f454c17d16f2c42501791f034c9caee2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/f454c17d16f2c42501791f034c9caee2.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通过APM就可以定位到是哪个应用的那个接口出现了异常。多数情况下通过这个方式就能找到原因并解决。但是由于APM使用的20%的采样，当一个低频率的功能有异常的时候，使用此方法有可能并没有相关记录。所以我们还需要进一步赋能研发来解决这个场景下的问题。  <br>
<br>3、在线诊断平台<br>
<br>年初的时候中间件团队上线了在线诊断产品（基于Arthas二次开发），平台提供JVM关于线程使用量、TOP线程榜、GC瞬时耗时和次数、JVM参数等查看，同时可以进行线程的堆栈查看、方法追踪、方法监控、添加动态日志、以及进行在线Debug。可以方便开发人员在线动态调试和分析应用故障，极大的提高了故障排查效率。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/49603b4ad717baa2ff3ef8a5fcc8241e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/49603b4ad717baa2ff3ef8a5fcc8241e.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
（更多工具的相关介绍感兴趣的可以留言后续中间件相关同学进一步分享）  <br>
<br>4、谁的工程谁负责<br>
<br>前面也提到我们把工程的很多配置管理权限交给工程负责人，当故障发生的时候他们可以自主的完成相关操作，比如：回滚、重启、重建、扩容、限流、切流量等等。<br>
<h3>不足和改进</h3>通过目标驱动、产品赋能、持续运营系统可用性基本趋于稳定，很多历史的“坑”也都被找出来并优化了，但是依然存在一些故障需要我们持续关注：<br>
<br>主要有两方面：<br>
<ol><li>个别核心功能偶尔无法使用；</li><li>是否出现大面积故障。</li></ol><br>
<br>一方面我们引入了域名拨测，通过对核心域名的核心入口地址进行拨测。来判断是否出现了不可用。<br>
<br>另外我们通过全局监控5xx和超时的请求总数，如果出现大量异常IT运营就会联合运维介入分析。（这个情况很多时候都是基础设施故障）<br>
<br>经过我们半年多的运营和产品升级，目前95%+的故障都能够通过我们的产品进行准确的感知，85%+的故障可以通过我们提供的工具进行分析和定位。<br>
<br>应用确实存在很多历史原因所以还是会有一些问题无法排查和解决，但是有了好的衡量方式和运营机制，我们相信这些问题都会被逐一解决。<br>
<br>通过运营来落地SRE是离不开很多系统的支持的，我们之所以能够落地很大程度上离不开多年基础运维工作和建立的一套完善的系统，运营只是通过目标驱动，让这些系统更加有效的运行起来并持续迭代以达到我们设定的目标。<br>
<br>SRE并不想象的那么难，大家应该结合企业实际情况尽可能利用好已有的资源，明确各方目标，一起让系统更加稳定。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/LsyqeHKBwP20GIJY2hnZHw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/LsyqeHKBwP20GIJY2hnZHw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            