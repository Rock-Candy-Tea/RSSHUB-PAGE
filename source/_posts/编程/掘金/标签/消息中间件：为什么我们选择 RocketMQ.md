
---
title: '消息中间件：为什么我们选择 RocketMQ'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e55af45a7d70439e96caccdae97d520e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 19:10:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e55af45a7d70439e96caccdae97d520e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e55af45a7d70439e96caccdae97d520e~tplv-k3u1fbpfcp-zoom-1.image" alt="6.13头图.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者：李伟</p>
<p>说起消息队列，ActiveMQ、RabbitMQ、RocketMQ、Kafka、Pulsar 等纷纷涌入我们的脑海中， 在如此众多的开源消息队列产品中，作为一名合格的架构师如何给出高性价比的方案呢？商业化的产品暂不纳入选项中。</p>
<p>接下来我将从<strong>选型要素、RocketMQ 的优势</strong>两个方面解释为什么选择 RocketMQ 。
​</p>
<h1 data-id="heading-0">选型要素</h1>
<p>​
首先从公司、消息队列服务提供者（一般是中间件团队）、最终用户三个角度来简单总结分析。
​</p>
<h2 data-id="heading-1">一、从公司层面看， 关注如下几点：</h2>
<p>​
<strong>1. 技术成本</strong>
​
技术成本，一般包含服务器成本、二次开发成本、后期维护成本等，言而总之：都是钱。</p>
<p>服务器目前基本都使用云服务器，不同的云厂商的相同配置的服务器性能也有一定差异， 服务器成本一般需要了解：云厂商机器性能、云厂商优惠、所需服务器配置、服务器台数、单台服务器目前的价格、单台服务器优惠后的价格等。
​
<strong>2. 人力成本</strong>
​
人力成本，一般包含现有技术人员成本、新人招聘成本。
​
新的技术选型对于目前的技术人员接受程度怎么样，学习的难易程度怎样等，都是需要考虑的。如果太难的话，上线周期会变长、业务需求实现速度慢，甚至有人直接离职。</p>
<p>新人招聘成本，一般招聘一个新人有如下几个过程：简历筛选、预约面试、数轮面试、发 offer 、接受 offer 、正式入职、试用期、转正。这中间涉及到猎头成本、人力资源沟通成本、面试成本、新人入职后环境适应成本等等。
​
<strong>3. 其他</strong>
​
目前处于不同阶段的互联网公司对于技术成本、人力成本有着不一样的要求，但是很多有一定规模的公司实际上还是用“买买买”的心态来对待的：只要业务发展快速，买服务器、招人都不是问题，如果成本高了就做技术降成本、裁员。这不仅是员工之痛，也是业务之痛，更是公司之痛。
​</p>
<h2 data-id="heading-2">二、从中间件组层面看， 关注如下几点：</h2>
<p>​
<strong>1. 稳定</strong>
​
公司级的服务首要的一点就是稳定。拥有稳定的组件、稳定的服务，业务才能有条不紊的进行。所以说，无论什么时候， 稳定都是王道。
​
<strong>2. 功能支持</strong></p>
<p>不同的业务场景需要的功能也不尽相同，通常我们会考虑重试、死信机制，位点重置，定时延迟消息、事物消息，主从切换，权限控制等方面。
​
<strong>3. 性能</strong>
​
目前包含写入延迟和吞吐。
​
<strong>4. 管理平台</strong>
​
首先需要满足最终用户接入、查看、排障，管理员管控 topic 、消费者方便等。管理平台有现成的最好，方便二次开发 。
​
<strong>5. 监控、报警</strong>
​
监控报警是否完善、是否方便接入公司内部自研体系，或者行业的事实标准  Prometheus 。
​
<strong>6. 运维 & 支持 & 开源社区</strong>
​
如果产品上线后， 大部分时间，我们都是在做运维&支持。运维包含服务部署、迁移、服务升级、解决系统 Bug 、用户使用答疑、管理平台和监控报警平台升级等。
​
<strong>7. 其他</strong>
​
我们除了依赖自身以外，也可以借助社区的力量，同一个问题可能别人遇到过并且提交过 PR ，已经得到解决，我们就可以以此作为借鉴。所以社区的活跃情况也是非常重要的考虑。
​</p>
<h2 data-id="heading-3">三、从最终用户（一般包含业务后端研发以及他们的 Leader ）看</h2>
<p>​
<strong>1. 稳定性</strong>
​
对于业务的研发和他们的 Leader ，他们的核心任务是实现业务逻辑。如果一个服务三天两头总是有问题， 对于他们来说是比较致命的，所以稳定性是比较核心的一部分。
​
<strong>2. 改造现有项目的难度</strong>
​
旧项目改造其实是业务研发接入新中间件实际操作最多的部分。
​
<strong>3. 新项目接入是否便捷</strong>
​
是否便捷接入跟他们的工作量有着直接的关联。
​
<strong>4. 与目前的 App 微服务框架兼容怎样</strong>
​
新项目的接入和公司微服务框架兼容都比较容易。一般中间件在提供服务时都会考虑业务研发接入的便利性。
​</p>
<h1 data-id="heading-4">RocketMQ 的优势</h1>
<p>​
下面将按照选项要素的要求， 分析 RocketMQ 在这方面的优势。
​</p>
<h2 data-id="heading-5">一、RocketMQ 如何解决和友好面对公司层面的诉求</h2>
<p>​
<strong>1. 技术成本</strong>
​
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaa6299d4de84b269a867d253e358902~tplv-k3u1fbpfcp-zoom-1.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>就技术成熟度而言，在经历阿里双十一数万亿洪峰、微众银行、民生银行、蚂蚁金服、平安、字节跳动、快手、美团、京东、网易等各种行业大厂的考验后，就不言而喻了。
​
RocketMQ 对于服务器的配置要求不高， 普通的云主机都可以。曾经我们验证 8C 16G 500G SSD 的 2 主 2 从的集群，发送 tps 可以到 4～5w ，消费 tps 峰值 20w +，稳定在 8w～9w 。并且，还能根据业务实际的需求无感的横向扩展。
​
综合而言， 技术成本相对可控且人才多。
​
<strong>2. 人力成本</strong>
​
人力成本主要是现有的技术人员的学习成本、招新人的成本。
​
RocketMQ 是 java 开发的，代码也非常稳定、有条理，各个版本之间除了功能有差异之外，Api 、传输协议几乎没有太多变化，对于升级而言也更加方便。
​
java 也是目前中间件采用的比较主流的语言，使用的技术人员非常广泛。RocketMQ 在金融行业比如：微众银行、民生银行、蚂蚁金服、平安； 其他行业公司，比如阿里、字节跳动、快手、美团、京东、网易等与大量中小企业都在使用，候选人范围相对较大。
​
RocketMQ 社区也比较活跃，钉钉群、微信群、QQ 群众多，社区文档非常丰富和完善，原理剖析视频、文档也非常多，非常易于学习和入门。
​
下面是钉钉群，欢迎大家加群留言、答疑。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd74ce6f970d4b51ab8e8aff4acc3c22~tplv-k3u1fbpfcp-zoom-1.image" alt="3F8FC69E-02B9-4A45-B842-B4C3A0D94FEA.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于 java 方面的消息队列方面的人才相比 C/C++、C#、Python、Go 等还是更多的：主流的 Kafka 是 scala + java、pulsar 是 java ，对于招聘也有极大的优势。
​
综合而言，RocketMQ 技术员对于人力成本比较友好。
​</p>
<h2 data-id="heading-6">二、从中间件组层面看，RocketMQ 是如何提供优秀的能力，为业务保驾护航呢？</h2>
<p>​
<strong>1. 稳定性</strong>
​
金融级可靠、阿里双十一稳定支持万亿级消息洪峰，<strong>在笔者之前所在公司也有过 2 年+零事故的佳绩</strong>。
​
<strong>2. 功能丰富，支持的场景众多</strong>
​</p>
<ul>
<li>重试、死信机制，友好、无感的业务重试机制。</li>
<li>顺序消息、事物消息</li>
<li>万级 Topic 数量支持</li>
<li>消息过滤</li>
<li>消息轨迹追踪</li>
<li>主从自动切换</li>
<li>原生支持 Prometheus 监控</li>
<li>原生支持易用管理平台：RocketMQ Console</li>
<li>访问权限控制（ACL）</li>
</ul>
<p><strong>3. 性能</strong>
​</p>
<ul>
<li>RocketMQ 可以支持 99.9% 的写入延迟在 2 ms ，其他的开源消息队列中间件基本都是大于 5 ms ；目前大部分消息队列中间间都支持横向扩展，吞吐上横向扩展几乎都可以满足。RocketMQ 的在滴滴做的性能测试: _<a href="https://developer.aliyun.com/article/664608" target="_blank" rel="nofollow noopener noreferrer">developer.aliyun.com/article/664…</a> _, 大家参考。</li>
<li>发送、消费 tps 和 kafka 一个数量级，Topic 数量剧增对于性能影响较小。</li>
</ul>
<p><strong>4. 管理平台</strong>
​
RocketMQ Console 原生支持：
<em><a href="https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a></em>
​
<strong>5. 监控、报警</strong>
​
RocketMQ Exporter 原生支持 Prometheus：
<em><a href="https://github.com/apache/rocketmq-exporter" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a></em>
​
<strong>6. 运维 & 支持 & 开源社区</strong>
​</p>
<ul>
<li>无 zk 等第三方依赖，开箱即用</li>
<li>社区钉钉群、微信群、QQ 群非常活跃，钉钉群、微信群有问必答。</li>
<li>社区最近新来一位小姐姐 Commiter ，团队也在不断壮大。</li>
</ul>
<p>综合看来，RocketMQ 稳定、可靠、性能好，开箱即用，不依赖 Zookeeper ，系统的稳定性更高，复杂度更小。监控报警等周边设施完善，场景支持全，社区活跃、文档丰富，是中间件团队的不二之选。
​</p>
<h2 data-id="heading-7">三、对于最终用户：业务研发、业务研发 Leader，他们的核心担忧是提供的技术是否稳定可靠、是否快速方便的接入</h2>
<p>​
从中间件组层面看这个问题时，RocketMQ 稳定、可靠，那对于接入是否友好呢？
​
RocketMQ 提供 java 原生客户端、Spring 客户端，C++ 客户端、Python 客户端、Go 客户端等多类型、多语言的客户端，对于各种项目都可以统一接入。
​
微服务框架中 Spring Cloud 基本已经成为事实标准，RocketMQ 支持 Spring boot Starter 和 Spring Cloud Function 等多种方式融合入微服务框架，对于 Spring 体系支持更加方便快捷。
​</p>
<h1 data-id="heading-8">Kafka vs RocketMQ</h1>
<p>​
实际中，很多人应该面临过 RocketMQ vs Kafka ，Kafka 适合对于延迟不敏感、批量型、Topic 数量可控、对于消息丢失不敏感的场景。比如大数据场景的 MySQL-2Hive、MySQL-2-Flink 的数据流通道，日志数据流通道等。</p>
<p>RocketMQ 适用于金融转账消息、订单状态变更消息、手机消息 Push 等业务场景。这些场景 Topic 数量通常过万，对于消息延迟和丢失极度敏感，数据通常是论条处理。对于海量数据的问题，一般地横向扩容完全可以解决。</p>
<p>合适的场景选择合适的产品，万能的产品是不存在的，都是折中，都是取舍。</p>
<h1 data-id="heading-9">作者介绍</h1>
<p>​
李伟，Apache RocketMQ 社区 Commiter ，Python 客户端项目负责人, Apache RocketMQ 北京社区联合发起人，Apache Doris Contributor 。目前就职于腾讯，主要负责 OLAP 数据库开发，对分布式存储系统设计和研发有丰富经验，也热衷于知识分享和社区活动。</p>
<h1 data-id="heading-10">RocketMQ 学习资料</h1>
<p>​
阿里云知行实验室提供一系列的 RocketMQ 在线实操环境，包含操作文档、ubuntu 实验环境，大家随时尝试玩玩：
​</p>
<ul>
<li>Apache RocketMQ 开源入门最佳实践：</li>
</ul>
<p><em><a href="https://start.aliyun.com/course?spm=a2ck6.17690074.0.0.53c52e7dSi19ML&id=eAz6VTK5" target="_blank" rel="nofollow noopener noreferrer">start.aliyun.com/course?spm=…</a></em></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/610a5fe0487a49ac8281fc3e640fd4ea~tplv-k3u1fbpfcp-zoom-1.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>《RocketMQ 分布式消息中间件：核心原理与最佳实践》随书实战：<em><a href="https://start.aliyun.com/course?spm=a2ck6.17690074.0.0.7aec2e7dCPMDFG&id=ASeJlmpX" target="_blank" rel="nofollow noopener noreferrer">start.aliyun.com/course?spm=…</a></em></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bd13bbaf31f40afa9dbb548944f00f5~tplv-k3u1fbpfcp-zoom-1.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在 Spring 生态中玩转 RocketMQ：</li>
</ul>
<p><a href="https://start.aliyun.com/course?spm=a2ck6.17690074.0.0.241e2e7d0aEIxJ&id=hzidp9W1" target="_blank" rel="nofollow noopener noreferrer">start.aliyun.com/course?spm=…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d134b231e3594aba8c1be80c1b4c280c~tplv-k3u1fbpfcp-zoom-1.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实验预览图如下：
​
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea6ef795b9ac47e2994f2ef99c005b22~tplv-k3u1fbpfcp-zoom-1.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">其他资源</h1>
<p>​</p>
<ul>
<li>RocketMQ vs. ActiveMQ vs. Kafka：</li>
</ul>
<p>_    <a href="http://rocketmq.apache.org/docs/motivation/" target="_blank" rel="nofollow noopener noreferrer">rocketmq.apache.org/docs/motiva…</a>_</p>
<ul>
<li>RocketMQ 源码：</li>
</ul>
<p>_   <a href="https://github.com/apache/rocketmq" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a>_</p>
<ul>
<li>RocketMQ Exporter 源码：</li>
</ul>
<p>_    <a href="https://github.com/apache/rocketmq-exporter" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a>_</p>
<ul>
<li>RocketMQ Spring 源码：</li>
</ul>
<p>_   <a href="https://github.com/apache/rocketmq-spring" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a>_</p>
<ul>
<li>RocketMQ C++ 客户端源码：</li>
</ul>
<p>_   <a href="https://github.com/apache/rocketmq-client-cpp" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a>_</p>
<ul>
<li>RocketMQ Python 客户端源码：</li>
</ul>
<p>_    <a href="https://github.com/apache/rocketmq-client-python" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a>_</p>
<ul>
<li>RocketMQ Go 客户端源码：</li>
</ul>
<p>_   <a href="https://github.com/apache/rocketmq-client-go" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a>_</p>
<ul>
<li>RocketMQ Console 源码：</li>
</ul>
<p>_    <a href="https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a>_</p>
<ul>
<li>RocketMQ Flink Connector 源码：</li>
</ul>
<p>_     <a href="https://github.com/apache/rocketmq-externals/tree/master/rocketmq-flink" target="_blank" rel="nofollow noopener noreferrer">github.com/apache/rock…</a>_</p>
<ul>
<li>
<p>RocketMQ 如何保证消息可靠：</p>
<pre><code class="copyable">[https://mp.weixin.qq.com/s/imLTVwgm8MOiY1_5s3rdFQ](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247502152&idx=1&sn=3c356a4b65d50e964f0350a13ba08df3&scene=21#wechat_redirect)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>大揭秘！RocketMQ 如何管理消费进度：</p>
<pre><code class="copyable">[https://mp.weixin.qq.com/s/rHs9L1gTuFs05Cs2F4JXOw](https://mp.weixin.qq.com/s?__biz=MjM5NTk0NjMwOQ==&mid=2651114644&idx=1&sn=fa93f0264989b536153dc683a246601a&scene=21#wechat_redirect)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            