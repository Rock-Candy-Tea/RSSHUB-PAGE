
---
title: 'AI和大数据结合，智能运维平台助力流利说提升核心竞争力'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23a3c18c9e304d2192ac2cee030ab1c8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 19:44:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23a3c18c9e304d2192ac2cee030ab1c8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>简介： 简介：本文整理自数智创新行——智能运维专场（上海站），流利说最佳实践演讲：《基于SLS千万级在线教育平台统一监控运营实践》</p>
<p>作者：<br>
孙文杰 流利说运维总监<br>
元乙 阿里云智能技术专家</p>
<p><strong>优质的内容与定制化服务，提升企业核心竞争力</strong></p>
<p>2020年受疫情影响，在“停课不停学”的口号下，在线教育市场规模快速增加，市场规模达4858亿元。在线教育行业经过前几年的快速奔跑后，市场已相对成熟，用户对于各家不同类型的在线教育机构，也提出了不同需求，因此单靠流量已无法换来忠实用户。但对于教育行业来说，核心竞争力仍然是优质的内容和服务。只有高质量的课程内容、根据客户学习习惯和基础制定个性化计划、优质产品体验与稳定性，结合更高业务运营效率，企业才能赢得长远的发展。纵观整个在线教育行业，在不断调整中，最终存活下来的企业也必然要回归教育本质，以优质产品、内容与服务等赢得长远发展。</p>
<p><strong>结合人工智能，特色教学独树一帜</strong></p>
<p>在行业近一步调整之后，在线教育赛道中的企业也逐渐将由注重增量回归内容建设。但在整体大环境下，教学大纲千篇一律，教学方式也大相径庭。虽课程有差异，但仍无惊艳可言，大部分企业无法依靠内容来突出重围。</p>
<p>但流利说却不同，在这个人工智能时代，流利说凭借特色的智能教学课程，依托人工智能AI等创新技术，为用户提供个性化教学课程，帮助更多用户提升英语水平。截止2021年3月31日，流利说累计注册用户超2亿，而其拥有的巨型“中国人英语语音数据库”，可以根据每一位学员的实际情况进行评测，学员在流利说发音学习的过程中，可以通过智能口型识别纠音系统动态去捕捉学员嘴部关键点，从而以先进技术进行比对，找到学员发音的问题所在。这样就可以提出针对性的指导意见来解决口语表达方面的问题，从根本上帮助学员提升口语水平。</p>
<p><strong>产品体验是关键，如何提升系统稳定成难题</strong></p>
<p>流利说业务的快速发展，用户数大幅度增长，从最初的几百万用户，已经增长过2亿业务的高低峰期的数据流量变化、业务复杂度和分析难度都给运维工作来了巨大的挑战。在整体互联网大环境中，体验是最关键的竞争力之一，根据统计结果，每1秒的延迟，平均会带来7%的用户流失。</p>
<p>作为一个没有单独运维部门的公司，流利说基础平台的运维系统主要由cloud-infra团队的研发来完成，而团队的核心诉求也不仅仅是SLA、性能的监控、告警和提供问题定位的相关数据，还包括cloud-infra的技术价值运营，例如利用率、成本节约、业务关系网络等。<br>
在这些核心诉求下，对于智能化运维平台的要求：</p>
<p>1.采集、监控各种异构数据源，包括K8s、ECS上的机器指标、利用率、Istio相关的调用日志、自建中间件相关指标、云服务提供的指标、业务的Trace数据等，此外还要包括各类成本数据的实时采集。</p>
<p>2.各类资源的动态发现与动态采集，包括组织关系等部门相关的数据也需要实时更新，以便能够实时反馈出最准确的相关指标和归属关系。</p>
<p>3.大规模的数据存储与分析，由于流利说的业务规模大，使用的各类云资源以及业务产生的数据量非常巨大，每天在数十TB，方案需要满足在此规模上的实时分析和展现的能力。</p>
<p>4.监控平台负责的是稳定性问题，本身的稳定性也需要做好，因此需要消除各个部分的单点问题，并且具备异常快速恢复的能力。</p>
<p><strong>一站式智能运维解决方案，打通数据收集到计算全链路</strong></p>
<p>流利说构建的智能运维平台，需要处理的不仅仅是时序相关的数据，其中非常核心的业务可用性数据也需要通过各类日志进行计算和分析，因此整体上需要选择Logs和Metrics两种数据方案。对于这两类数据都分别有不同的社区方案或商业方案，例如ES、Loki、SLS、Prometheus、OpenTSDB、InfluxDB等。最终日志方案选择了阿里云SLS，时序方案选择了Prometheus+SLS，主要的原因如下：</p>
<p>1.SLS具备各类数据统一存储、分析的能力，能够在SLS上去关联到Metrics、Logs数据，这是其他平台所不具备的</p>
<p>2.SLS平台能够适应非常大的数据规模，相比ES来说性能要好很多，也是免运维的服务，省去了自己维护ES高可靠的问题</p>
<p>3.时序方案以Prometheus为主，Prometheus的生态非常完善，而且PromQL使用起来也简洁。SLS的时序库可以作为Prometheus的远端高可靠存储，能够解决Prometheus的可靠性问题</p>
<p>4.SLS的方案中有数据加工的功能，可以和外部的数据源去做Join分析和加工，能够更好的来处理各种复杂的日志，把日志加上catalog相关的信息</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23a3c18c9e304d2192ac2cee030ab1c8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时为了最大程度实现自动化，阿里云日志服务SLS开发了一套适用于云上场景的IaaS、PaaS资源动态发现的机制，能够实时将新购买、创建的资源加入到监控、采集中，避免大部分的人工操作。</p>
<p>并且在每个数据场景下，阿里云日志服务SLS也针对流利说的需求做了特殊化的定制：</p>
<p><strong>1、日志方面</strong></p>
<ul>
<li>不同业务的日志直接通过SLS的Logtail采集到不同的日志库中</li>
<li>并不是所有的日志都需要长时间存储和索引，因此我们对于日志进行归类，对于其中需要有审计需求的，会投递到OSS上做长期存储；业务排查问题的日志只保存2周，并开启全文索引；AccessLog只开启部分字段的索引，可以节省很多的索引费用。</li>
<li>对于需要计算SLA、PXX指标的NGINX访问日志，会使用数据加工，配合已经在RDS中存储的一些映射规则、部门、应用等Catalog信息，将NGINX访问日志中的URL映射成对应的部门、应用、方法等。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45ed8be1a9314cbaa33356a925b5024d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2、数据监控方面</strong></p>
<ul>
<li>监控方案选择了Prometheus，针对于流利说的场景，我们开发了一些Exporter用于从各类云上产品、自建组件中获取Metrics</li>
<li>同时为了更好的使用Prometheus，和内部的CICD系统集成，我们在Prometheus上增加了一个Sidecar，监听Git仓库的变更，并根据变更动态的Reload Prometheus配置</li>
<li>Prometheus上为了提高查询速度，配置了各类Recording Rule，这些都统一使用Git管理</li>
<li>AlertManager的告警直接对接内部的告警中心，可以做排版、升级等高级功能</li>
<li>为了解决Prometheus单点的问题以及后面和Catalog进行关联分析的问题，我们使用SLS的时序库，直接让Prometheus Remote Write到SLS的时序库中</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2ca76b9335a41eba18122ff938fa19c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3、指标计算方面</strong></p>
<ul>
<li>核心指标的计算一部分来源于NGINX的AccessLog，从入口就可以拿到各个业务的QPS、错误率、Latency（平均、PXX等），对于业务没有任何的侵入性</li>
<li>资源利用率、中间件、基础设施等指标来源于Prometheus写入的时序库，基于Catalog可以聚合计算出每个部门、业务的相关指标</li>
<li>计算完成后的指标信息，由于数据量非常小，可以很容易的存储在MySQL、ES中，并且投递一份到OSS上备份</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdaf975849664fa089ed39a47cf78a4e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>构建统一的智能运维平台，从成本中心变为创新生产力工具</strong></p>
<p>目前这套智能运维平台系统几乎承载了公司所有的核心运维，在上线后一直稳定运行，并且在各类活动期间也能够非常轻松的应对数据量的突增。整体的业务价值主要体现在：</p>
<ul>
<li>监控：监控的第一价值是做各类的监控和告警，尤其是SLA相关，由于将数据已经关联到了具体的部门和业务应用，可以很容易的得到每个部门、应用的SLA，并进行公司范围内统一的推进和改进</li>
<li>问题排查与故障隔离：基于Istio的访问日志，配合Catalog信息，可以计算出每个应用的调用关系，因此可以实时的生成业务关系网格，并能够知道每个关系（边）的质量情况。了解到业务的关系后，在出现问题的时候也可以快速的定位根源和故障隔离</li>
<li>FinOps：在Cloud Infra部门，被挑战最多的就是开销问题。因此成本优化也是我们的一个核心工作，主要的做法是：计算每个部门、团队的资源利用率，包括平均利用率以及各类PXX的利用率（入下表格所示），以此能够判断每个部门的资源使用情况，推进各部门优化成本。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22e30fb8bc954c049920c3bcfdba5181~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>写到最后</strong></p>
<p>在云原生时代，数字化正在各行业推动业务创新。只有提升用户体验、加速创新、更新基础设施与架构、利用好多样化的数据，才能在整体大环境中脱颖而出。阿里云推出的智能运维平台，不仅仅是要帮助工程师减少工作量，更多的是希望让运维工程师们从各种机械化的工作中解脱。我们将会包揽所有的“脏活累活”，让故障的时间大幅缩小，让运维人将更多创造力，放在数字创新以及企业业务创新上，为企业提供提供更优的竞争力。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000284762%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000284762/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            