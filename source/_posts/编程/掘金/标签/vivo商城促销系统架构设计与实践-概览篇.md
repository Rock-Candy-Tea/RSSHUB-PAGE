
---
title: 'vivo商城促销系统架构设计与实践-概览篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3593789a9604feaba1049c5cc8d2809~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 28 Jun 2021 00:13:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3593789a9604feaba1049c5cc8d2809~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、前言</h1>
<p>随着商城业务渠道不断扩展，促销玩法不断增多，原商城v2.0架构已经无法满足不断增加的活动玩法，需要进行促销系统的独立建设，与商城解耦，提供纯粹的商城营销活动玩法支撑能力。</p>
<p>我们将分系列来介绍vivo商城促销系统建设的过程中遇到的问题和解决方案，分享架构设计经验。</p>
<h1 data-id="heading-1">二、系统框架</h1>
<h2 data-id="heading-2">2.1 业务梳理</h2>
<p>在介绍业务架构前我们先简单了解下vivo商城促销系统业务能力建设历程，对现促销能力进行梳理回顾。在商城v2.0中促销功能存在以下问题：</p>
<p><strong>1. 促销模型不够抽象，维护混乱，没有独立的活动库存；</strong></p>
<p><strong>2. 混乱的活动共融互斥关系管理，缺乏统一的促销计价能力。</strong></p>
<p>商城核心交易链路中商详页、购物车、下单这三块关于计价逻辑是分开独立维护的，没有统一，如下图所示。显然随着促销优惠的增加或者玩法的变动，商城侧业务重复开发量会显著加大。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3593789a9604feaba1049c5cc8d2809~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图2-1. 促销计价统一前）</p>
<p><strong>3. 促销性能无法满足活动量级，往往会影响商城主站的性能。</strong></p>
<p>因与商城系统耦合，无法提供针对性的性能优化，造成系统无法支撑越来越频繁的大流量场景下大促活动。</p>
<p>基于这些痛点问题，我们一期完成促销系统的独立，与商城解耦，搭建出促销系统核心能力：</p>
<p><strong>优惠活动管理</strong></p>
<p>对所有优惠活动抽象出统一的优惠模型和配置管理界面，提供活动编辑、修改、查询及数据统计等功能。并独立出统一的活动库存管理，便于活动资源的统一把控。</p>
<p><strong>促销计价</strong></p>
<p>基于高度灵活、抽象化的计价引擎能力，通过定义分层计价的促销计价模型，制定统一的优惠叠加规则与计价流程，实现vivo商城促销计价能力的建设。推动完成vivo商城所有核心链路接入促销计价，实现全链路优惠价格计算的统一，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7778ec4dc6ee4d8aa2241cbb15d258d7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图2-2. 促销计价统一后）</p>
<p>随着一期促销系统核心能力的完成，极大的满足了业务需要，各类优惠玩法随之增多。但伴随而来的就是各种运营痛点：</p>
<ul>
<li>
<p>维护的促销活动无法提前点检，检查活动效果是否符合预期；</p>
</li>
<li>
<p>随着优惠玩法的增多，一个商品所能享受的优惠越来越多，配置也越来越复杂，极易配置错误造成线上事故；</p>
</li>
</ul>
<p>为此我们开始促销系统二期的能力建设，着重解决以上运营痛点：</p>
<ul>
<li>
<p>提供时光穿越功能，实现用户能够“穿越”至未来某个时间点，从而实现促销活动的提前点检；</p>
</li>
<li>
<p>提供价格监控功能，结合「商城营销价格能力矩阵」规划的能力，通过事前/事中/事后多维度监控措施，来“降低出错概率，出错能及时止损”。</p>
</li>
</ul>
<h2 data-id="heading-3">2.2 促销与优惠券</h2>
<p>促销的主要目的就是向用户传递商品的各种优惠信息，提供优惠利益，吸引用户购买，从而起到促活拉新、提高销量的目的。从这种角度来看，优惠券也属于促销的一部分。</p>
<p>但因一些原因vivo商城促销系统独立过程中，并没有与促销系统放一块：</p>
<ul>
<li>
<p>首先，优惠券系统在商城v2.0时就已独立，已经对接很多上游业务，已经是成熟的中台系统；</p>
</li>
<li>
<p>再者，就是优惠券也有相较与其它促销优惠的业务特殊性，如有发券、领券能力。</p>
</li>
</ul>
<p>在考虑设计改造成本就未将优惠券包括在促销系统能力范畴，但优惠券毕竟也是商品价格优惠的一部分，因此促销计价需要依赖优惠券系统提供券优惠的能力。</p>
<h2 data-id="heading-4">2.3 业务架构&流程</h2>
<p>至此我们也就梳理出整个促销系统的大概能力矩阵，整体架构设计如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d75afd3c74da4e4793f5b0b1ba5c578f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图2-3. 促销系统架构）</p>
<p>而随着促销系统独立，整个商城购物流程与促销系统的关系如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/770c505f0e6249fb9d3f89d600188c70~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图2-4. 最新商城购物流程）</p>
<h1 data-id="heading-5">三、技术挑战</h1>
<p>作为中台能力系统，促销系统面临的技术挑战包括以下几方面：</p>
<ul>
<li>
<p>面对复杂多变的促销玩法、优惠叠加规则，如何让系统具备可扩展性，满足日益多变的优惠需求，提升开发与运营效率。</p>
</li>
<li>
<p>面对新品发布、双11大为客户等大流量场景，如何满足高并发场景下的高性能要求。</p>
</li>
<li>
<p>面对来自上游业务方的不可信调用，以及下游依赖方的不可靠服务等复杂系统环境，如何提升系统整体的稳定性，保障系统的高可用。</p>
</li>
</ul>
<p>我们结合自身业务特点，梳理出一些技术解决方案。</p>
<h2 data-id="heading-6">3.1 可扩展性</h2>
<p>扩展性提升主要体现在两块：</p>
<ul>
<li>
<p>优惠模型的定义，对所有优惠活动抽象出统一的优惠模型和配置管理界面；</p>
</li>
<li>
<p>促销计价引擎的建立，计价模型的统一。</p>
</li>
</ul>
<p>相关的详细设计内容，会有后续文章进行说明。</p>
<h2 data-id="heading-7">3.2 高并发/高性能</h2>
<p><strong>缓存</strong></p>
<p>缓存几乎就是解决性能问题的“银弹”，在促销系统中也大量使用缓存进行性能提升，包括使用redis缓存与本地缓存。而使用缓存就需要关注数据一致性问题，redis缓存还好解决，但本地缓存不就好处理了。因此本地缓存的使用要看业务场景，尽量是数据不经常变更且业务上能接受一定不一致的场景。</p>
<p><strong>批量化</strong></p>
<p>促销系统的业务场景属于典型的读多写少场景，而读的过程中对性能影响最大的就是IO操作，包括db、redis以及第三方远程调用。而对这些IO操作进行批量化改造，以空间换时间，减少IO交互次数也是性能优化的一大方案。</p>
<p><strong>精简化/异步化</strong></p>
<p>简化功能实现，将非核心任务进行异步化改造。如活动编辑后的缓存处理、资源预占后的消息同步、拼团状态流转的消息通知等等。</p>
<p><strong>冷热分离</strong></p>
<p>对于读多写少场景对性能影响最大的除了IO操作，还有就是数据量，在促销系统中也存在一些用户态数据，如优惠资源预占记录、用户拼团信息等。这些数据都具备时间属性，存在热尾效应，大部分情况下需要的都是最近的数据。针对这类场景对数据进行冷热分离是最佳选择。</p>
<h2 data-id="heading-8">3.3 系统稳定性</h2>
<p><strong>限流降级</strong></p>
<p>基于公司的限流组件，对非核心的服务功能进行流量限制与服务降级，高并发场景下全力保障整体系统的核心服务</p>
<p><strong>幂等性</strong></p>
<p>所有接口均具备幂等性，避免业务方的网络超时重试造成的系统异常</p>
<p><strong>熔断</strong></p>
<p>使用Hystrix组件对外部系统的调用添加熔断保护，防止外部系统的故障造成整个促销系统的服务崩溃</p>
<p><strong>监控和告警</strong></p>
<p>通过配置日志平台的错误日志报警、调用链的服务分析告警，再加上公司各中间件和基础组件的监控告警功能，让我们能够第一时间发现系统异常</p>
<h1 data-id="heading-9">四、踩过的坑</h1>
<h2 data-id="heading-10">4.1 Redis SCAN命令使用</h2>
<p>在Redis缓存数据清除的处理过程中，存在部分缓存key是通过模糊匹配的方式进行查找并清除操作，底层依赖Redis SCAN命令。</p>
<blockquote>
<p>SCAN命令是一个基于游标的迭代器，每次被调用之后都会向用户返回一个新的游标， 用户在下次迭代时需要使用这个新游标作为 SCAN 命令的游标参数， 以此来延续之前的迭代过程。</p>
</blockquote>
<p>对于使用KEYS命令，SCAN命令并不是一次性返回所有匹配结果，减少命令操作对Redis系统的阻塞风险。但并不是说SCAN命令就可以随便用，其实在大数据量场景下SCAN存在与KEYS命令一样的风险问题，极易造成Redis负载升高，响应变慢，进而影响整个系统的稳定性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4217c7907a50450ebd36b9bf2a0595e7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图4-1 Redis负载升高）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/102a19ddb60a4e5994532b724bff2e48~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>(图4-2 Redis响应出现尖刺)</p>
<p>而解决方案就是：</p>
<ul>
<li>
<p>优化Redis key设计，减少不必要的缓存key；</p>
</li>
<li>
<p>移除SCAN命令使用，通过精确匹配查找进行清除操作。</p>
</li>
</ul>
<h2 data-id="heading-11">4.2 热点key问题</h2>
<p>在促销系统中普遍使用redis缓存进行性能提升，缓存数据很多都是SKU商品维度。在新品发布、特定类型手机大促等业务场景下极容易产生热点Key问题。</p>
<p>热点Key具有聚集效应，会导致Redis集群内节点负载出现不均衡，进而造成整个系统不稳定。该问题是普通的机器扩容无法解决的。如下图某次线上摸排压测时redis负载情况：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a212b339f4c04549ba48cea3e91edbd3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>常用的解决方案有两种：</p>
<ul>
<li>
<p>散列方案：对Redis Key进行散列，平均分散到RedisCluster Nodes中，解决热点Key的聚集效应。</p>
</li>
<li>
<p>多级缓存方案：对热点Key增加使用本地缓存，最大限度加速访问性能，降低Redis节点负载。</p>
</li>
</ul>
<p>我们是采用多级缓存方案，参照优秀的开源热点缓存框架，定制化扩展出一整套热点解决方案，支持热点探测 、本地缓存 、集群广播以及热点预热功能，做到准实时热点探测并将热点Key通知实例集群进行本地缓存，极大限度避免大量重复调用冲击分布式缓存，提升系统运行效率。</p>
<h1 data-id="heading-12">五、总结</h1>
<p>本篇属于vivo商城促销系统概览介绍篇，简单回顾了vivo商城促销系统业务能力建设历程及系统架构，并分享遇到的技术问题与解决方案。后续我们会对促销系统的核心功能模块（优惠活动管理、促销计价、价格监控和时光穿越）的设计实践进行逐个分享，敬请期待。</p>
<blockquote>
<p>作者：vivo互联网官方商城开发团</p>
</blockquote></div>  
</div>
            