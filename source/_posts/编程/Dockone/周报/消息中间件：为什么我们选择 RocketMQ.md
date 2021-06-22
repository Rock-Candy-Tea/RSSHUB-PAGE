
---
title: '消息中间件：为什么我们选择 RocketMQ'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/88cc336a82434a38a24231825168733a.jpg'
author: Dockone
comments: false
date: 2021-06-22 04:08:49
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/88cc336a82434a38a24231825168733a.jpg'
---

<div>   
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/88cc336a82434a38a24231825168733a.jpg" alt="6.13头图.jpg" referrerpolicy="no-referrer"><br>
<br>作者：李伟<br>
<br>说起消息队列，ActiveMQ、RabbitMQ、RocketMQ、Kafka、Pulsar 等纷纷涌入我们的脑海中， 在如此众多的开源消息队列产品中，作为一名合格的架构师如何给出高性价比的方案呢？商业化的产品暂不纳入选项中。<br>
<br>接下来我将从<strong>选型要素、RocketMQ 的优势</strong>两个方面解释为什么选择 RocketMQ 。<br>
​<br>
<h1>选型要素</h1>​<br>
首先从公司、消息队列服务提供者（一般是中间件团队）、最终用户三个角度来简单总结分析。<br>
​<br>
<h2>一、从公司层面看， 关注如下几点：</h2>​<br>
<strong>1. 技术成本</strong><br>
​<br>
技术成本，一般包含服务器成本、二次开发成本、后期维护成本等，言而总之：都是钱。 <br>
<br>服务器目前基本都使用云服务器，不同的云厂商的相同配置的服务器性能也有一定差异， 服务器成本一般需要了解：云厂商机器性能、云厂商优惠、所需服务器配置、服务器台数、单台服务器目前的价格、单台服务器优惠后的价格等。<br>
​<br>
<strong>2. 人力成本</strong><br>
​<br>
人力成本，一般包含现有技术人员成本、新人招聘成本。<br>
​<br>
新的技术选型对于目前的技术人员接受程度怎么样，学习的难易程度怎样等，都是需要考虑的。如果太难的话，上线周期会变长、业务需求实现速度慢，甚至有人直接离职。<br>
<br>新人招聘成本，一般招聘一个新人有如下几个过程：简历筛选、预约面试、数轮面试、发 offer 、接受 offer 、正式入职、试用期、转正。这中间涉及到猎头成本、人力资源沟通成本、面试成本、新人入职后环境适应成本等等。<br>
​<br>
<strong>3. 其他</strong><br>
​<br>
目前处于不同阶段的互联网公司对于技术成本、人力成本有着不一样的要求，但是很多有一定规模的公司实际上还是用“买买买”的心态来对待的：只要业务发展快速，买服务器、招人都不是问题，如果成本高了就做技术降成本、裁员。这不仅是员工之痛，也是业务之痛，更是公司之痛。<br>
​<br>
<h2>二、从中间件组层面看， 关注如下几点：</h2>​<br>
<strong>1. 稳定</strong><br>
​<br>
公司级的服务首要的一点就是稳定。拥有稳定的组件、稳定的服务，业务才能有条不紊的进行。所以说，无论什么时候， 稳定都是王道。<br>
​<br>
<strong>2. 功能支持</strong><br>
<br>不同的业务场景需要的功能也不尽相同，通常我们会考虑重试、死信机制，位点重置，定时延迟消息、事物消息，主从切换，权限控制等方面。<br>
​<br>
<strong>3. 性能</strong><br>
​<br>
目前包含写入延迟和吞吐。<br>
​<br>
<strong>4. 管理平台</strong><br>
​<br>
首先需要满足最终用户接入、查看、排障，管理员管控 topic 、消费者方便等。管理平台有现成的最好，方便二次开发 。<br>
​<br>
<strong>5. 监控、报警</strong><br>
​<br>
监控报警是否完善、是否方便接入公司内部自研体系，或者行业的事实标准  Prometheus 。<br>
​<br>
<strong>6. 运维 & 支持 & 开源社区</strong><br>
​<br>
如果产品上线后， 大部分时间，我们都是在做运维&支持。运维包含服务部署、迁移、服务升级、解决系统 Bug 、用户使用答疑、管理平台和监控报警平台升级等。<br>
​<br>
<strong>7. 其他</strong><br>
​<br>
我们除了依赖自身以外，也可以借助社区的力量，同一个问题可能别人遇到过并且提交过 PR ，已经得到解决，我们就可以以此作为借鉴。所以社区的活跃情况也是非常重要的考虑。<br>
​<br>
<h2>三、从最终用户（一般包含业务后端研发以及他们的 Leader ）看</h2>​<br>
<strong>1. 稳定性</strong><br>
​<br>
对于业务的研发和他们的 Leader ，他们的核心任务是实现业务逻辑。如果一个服务三天两头总是有问题， 对于他们来说是比较致命的，所以稳定性是比较核心的一部分。<br>
​<br>
<strong>2. 改造现有项目的难度</strong><br>
​<br>
旧项目改造其实是业务研发接入新中间件实际操作最多的部分。<br>
​<br>
<strong>3. 新项目接入是否便捷</strong><br>
​<br>
是否便捷接入跟他们的工作量有着直接的关联。<br>
​<br>
<strong>4. 与目前的 App 微服务框架兼容怎样</strong><br>
​<br>
新项目的接入和公司微服务框架兼容都比较容易。一般中间件在提供服务时都会考虑业务研发接入的便利性。<br>
​<br>
<h1>RocketMQ 的优势</h1>​<br>
下面将按照选项要素的要求， 分析 RocketMQ 在这方面的优势。<br>
​<br>
<h2>一、RocketMQ 如何解决和友好面对公司层面的诉求</h2>​<br>
<strong>1. 技术成本</strong><br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/54209329ad004bedbb34038045b85d73.png" alt="2.png" referrerpolicy="no-referrer"><br>
<br>就技术成熟度而言，在经历阿里双十一数万亿洪峰、微众银行、民生银行、蚂蚁金服、平安、字节跳动、快手、美团、京东、网易等各种行业大厂的考验后，就不言而喻了。<br>
​<br>
RocketMQ 对于服务器的配置要求不高， 普通的云主机都可以。曾经我们验证 8C 16G 500G SSD 的 2 主 2 从的集群，发送 tps 可以到 4～5w ，消费 tps 峰值 20w +，稳定在 8w～9w 。并且，还能根据业务实际的需求无感的横向扩展。<br>
​<br>
综合而言， 技术成本相对可控且人才多。<br>
​<br>
<strong>2. 人力成本</strong><br>
​<br>
人力成本主要是现有的技术人员的学习成本、招新人的成本。<br>
​<br>
RocketMQ 是 java 开发的，代码也非常稳定、有条理，各个版本之间除了功能有差异之外，Api 、传输协议几乎没有太多变化，对于升级而言也更加方便。<br>
​<br>
java 也是目前中间件采用的比较主流的语言，使用的技术人员非常广泛。RocketMQ 在金融行业比如：微众银行、民生银行、蚂蚁金服、平安； 其他行业公司，比如阿里、字节跳动、快手、美团、京东、网易等与大量中小企业都在使用，候选人范围相对较大。<br>
​<br>
RocketMQ 社区也比较活跃，钉钉群、微信群、QQ 群众多，社区文档非常丰富和完善，原理剖析视频、文档也非常多，非常易于学习和入门。<br>
​<br>
下面是钉钉群，欢迎大家加群留言、答疑。<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/3acde903acc641e68d86a348839e5aed.png" alt="3F8FC69E-02B9-4A45-B842-B4C3A0D94FEA.png" referrerpolicy="no-referrer"><br>
<br>对于 java 方面的消息队列方面的人才相比 C/C++、C#、Python、Go 等还是更多的：主流的 Kafka 是 scala + java、pulsar 是 java ，对于招聘也有极大的优势。<br>
​<br>
综合而言，RocketMQ 技术员对于人力成本比较友好。<br>
​<br>
<h2>二、从中间件组层面看，RocketMQ 是如何提供优秀的能力，为业务保驾护航呢？</h2>​<br>
<strong>1. 稳定性</strong><br>
​<br>
金融级可靠、阿里双十一稳定支持万亿级消息洪峰，<strong>在笔者之前所在公司也有过 2 年+零事故的佳绩</strong>。<br>
​<br>
<strong>2. 功能丰富，支持的场景众多</strong><br>
​<br>
- 重试、死信机制，友好、无感的业务重试机制。<br>
- 顺序消息、事物消息<br>
- 万级 Topic 数量支持<br>
- 消息过滤<br>
- 消息轨迹追踪<br>
- 主从自动切换<br>
- 原生支持 Prometheus 监控<br>
- 原生支持易用管理平台：RocketMQ Console<br>
- 访问权限控制（ACL）<br>
<br><strong>3. 性能</strong><br>
​<br>
- RocketMQ 可以支持 99.9% 的写入延迟在 2 ms ，其他的开源消息队列中间件基本都是大于 5 ms ；目前大部分消息队列中间间都支持横向扩展，吞吐上横向扩展几乎都可以满足。RocketMQ 的在滴滴做的性能测试: _<a href="https://developer.aliyun.com/article/664608" rel="nofollow" target="_blank">https://developer.aliyun.com/article/664608</a> _, 大家参考。<br>
- 发送、消费 tps 和 kafka 一个数量级，Topic 数量剧增对于性能影响较小。<br>
<br><strong>4. 管理平台</strong><br>
​<br>
RocketMQ Console 原生支持：<br>
_<a href="https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console_" rel="nofollow" target="_blank">https://github.com/apache/rock ... sole_</a><br>
​<br>
<strong>5. 监控、报警</strong><br>
​<br>
RocketMQ Exporter 原生支持 Prometheus：<br>
_<a href="https://github.com/apache/rocketmq-exporter_" rel="nofollow" target="_blank">https://github.com/apache/rocketmq-exporter_</a><br>
​<br>
<strong>6. 运维 & 支持 & 开源社区</strong><br>
​<br>
- 无 zk 等第三方依赖，开箱即用<br>
- 社区钉钉群、微信群、QQ 群非常活跃，钉钉群、微信群有问必答。<br>
- 社区最近新来一位小姐姐 Commiter ，团队也在不断壮大。<br>
<br>综合看来，RocketMQ 稳定、可靠、性能好，开箱即用，不依赖 Zookeeper ，系统的稳定性更高，复杂度更小。监控报警等周边设施完善，场景支持全，社区活跃、文档丰富，是中间件团队的不二之选。<br>
​<br>
<h2>三、对于最终用户：业务研发、业务研发 Leader，他们的核心担忧是提供的技术是否稳定可靠、是否快速方便的接入</h2>​<br>
从中间件组层面看这个问题时，RocketMQ 稳定、可靠，那对于接入是否友好呢？<br>
​<br>
RocketMQ 提供 java 原生客户端、Spring 客户端，C++ 客户端、Python 客户端、Go 客户端等多类型、多语言的客户端，对于各种项目都可以统一接入。<br>
​<br>
微服务框架中 Spring Cloud 基本已经成为事实标准，RocketMQ 支持 Spring boot Starter 和 Spring Cloud Function 等多种方式融合入微服务框架，对于 Spring 体系支持更加方便快捷。<br>
​<br>
<h1>Kafka vs RocketMQ</h1>​<br>
实际中，很多人应该面临过 RocketMQ vs Kafka ，Kafka 适合对于延迟不敏感、批量型、Topic 数量可控、对于消息丢失不敏感的场景。比如大数据场景的 MySQL-2Hive、MySQL-2-Flink 的数据流通道，日志数据流通道等。<br>
<br>RocketMQ 适用于金融转账消息、订单状态变更消息、手机消息 Push 等业务场景。这些场景 Topic 数量通常过万，对于消息延迟和丢失极度敏感，数据通常是论条处理。对于海量数据的问题，一般地横向扩容完全可以解决。<br>
<br>合适的场景选择合适的产品，万能的产品是不存在的，都是折中，都是取舍。<br>
<br><h1>作者介绍</h1>​<br>
李伟，Apache RocketMQ 社区 Commiter ，Python 客户端项目负责人, Apache RocketMQ 北京社区联合发起人，Apache Doris Contributor 。目前就职于腾讯，主要负责 OLAP 数据库开发，对分布式存储系统设计和研发有丰富经验，也热衷于知识分享和社区活动。<br>
<br><h1>RocketMQ 学习资料</h1>​<br>
阿里云知行实验室提供一系列的 RocketMQ 在线实操环境，包含操作文档、ubuntu 实验环境，大家随时尝试玩玩：<br>
​<br>
- Apache RocketMQ 开源入门最佳实践：<br>
<br>_<a href="https://start.aliyun.com/course?spm=a2ck6.17690074.0.0.53c52e7dSi19ML&id=eAz6VTK5_" rel="nofollow" target="_blank">https://start.aliyun.com/cours ... VTK5_</a><br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/89c6779854df42b5aebf4e3b1fb34d6f.png" alt="4.png" referrerpolicy="no-referrer"><br>
<ul><li><br>《RocketMQ 分布式消息中间件：核心原理与最佳实践》随书实战：_<a href="https://start.aliyun.com/course?spm=a2ck6.17690074.0.0.7aec2e7dCPMDFG&id=ASeJlmpX_" rel="nofollow" target="_blank">https://start.aliyun.com/cours ... lmpX_</a><br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/ea9e413e49d24d1398b4153b2a491591.png" alt="5.png" referrerpolicy="no-referrer"></li><li><br>在 Spring 生态中玩转 RocketMQ：</li></ul><br>
<br><a href="https://start.aliyun.com/course?spm=a2ck6.17690074.0.0.241e2e7d0aEIxJ&id=hzidp9W1" rel="nofollow" target="_blank">https://start.aliyun.com/cours ... dp9W1</a><br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/3576851dbf4e478497f094bbeae6fdb7.png" alt="6.png" referrerpolicy="no-referrer"><br>
<br>实验预览图如下：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/3523fb6df3494a7c8ab32f974d52751c.png" alt="7.png" referrerpolicy="no-referrer"><br>
<br><h1>其他资源</h1>​<br>
- RocketMQ vs. ActiveMQ vs. Kafka：<br>
<br>_    <a href="http://rocketmq.apache.org/docs/motivation/_" rel="nofollow" target="_blank">http://rocketmq.apache.org/docs/motivation/_</a><br>
<ul><li>RocketMQ 源码：</li></ul><br>
<br>_   <a href="https://github.com/apache/rocketmq_" rel="nofollow" target="_blank">https://github.com/apache/rocketmq_</a><br>
<ul><li>RocketMQ Exporter 源码：</li></ul><br>
<br>_    <a href="https://github.com/apache/rocketmq-exporter_" rel="nofollow" target="_blank">https://github.com/apache/rocketmq-exporter_</a><br>
<ul><li>RocketMQ Spring 源码：</li></ul><br>
<br>_   <a href="https://github.com/apache/rocketmq-spring_" rel="nofollow" target="_blank">https://github.com/apache/rocketmq-spring_</a><br>
<ul><li>RocketMQ C++ 客户端源码：</li></ul><br>
<br>_   <a href="https://github.com/apache/rocketmq-client-cpp_" rel="nofollow" target="_blank">https://github.com/apache/rocketmq-client-cpp_</a><br>
<ul><li>RocketMQ Python 客户端源码：</li></ul><br>
<br>_    <a href="https://github.com/apache/rocketmq-client-python_" rel="nofollow" target="_blank">https://github.com/apache/rocketmq-client-python_</a><br>
<ul><li>RocketMQ Go 客户端源码：</li></ul><br>
<br>_   <a href="https://github.com/apache/rocketmq-client-go_" rel="nofollow" target="_blank">https://github.com/apache/rocketmq-client-go_</a><br>
<ul><li>RocketMQ Console 源码：</li></ul><br>
<br>_    <a href="https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console_" rel="nofollow" target="_blank">https://github.com/apache/rock ... sole_</a><br>
<ul><li>RocketMQ Flink Connector 源码：</li></ul><br>
<br>_     <a href="https://github.com/apache/rocketmq-externals/tree/master/rocketmq-flink_" rel="nofollow" target="_blank">https://github.com/apache/rock ... link_</a><br>
<ul><li><br>RocketMQ 如何保证消息可靠：<br>
<br>  <a href="https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247502152&idx=1&sn=3c356a4b65d50e964f0350a13ba08df3&scene=21#wechat_redirect"></a><a href="https://mp.weixin.qq.com/s/imLTVwgm8MOiY1_5s3rdFQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/imLTVwgm8MOiY1_5s3rdFQ</a></li><li><br>大揭秘！RocketMQ 如何管理消费进度：<br>
<br>  <a href="https://mp.weixin.qq.com/s?__biz=MjM5NTk0NjMwOQ==&mid=2651114644&idx=1&sn=fa93f0264989b536153dc683a246601a&scene=21#wechat_redirect"></a><a href="https://mp.weixin.qq.com/s/rHs9L1gTuFs05Cs2F4JXOw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/rHs9L1gTuFs05Cs2F4JXOw</a></li></ul>
                                
                                                              
</div>
            