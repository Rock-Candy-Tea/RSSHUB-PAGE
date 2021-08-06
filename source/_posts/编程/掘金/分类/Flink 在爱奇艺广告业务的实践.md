
---
title: 'Flink 在爱奇艺广告业务的实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8973402763854c74a526f23db94065fe~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 18:52:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8973402763854c74a526f23db94065fe~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>简介： 5 月 22 日北京站 Flink Meetup 分享的议题。</p>
<blockquote>
<p>本文整理自爱奇艺技术经理韩红根在 5 月 22 日北京站 Flink Meetup 分享的议题《Flink 在爱奇艺广告业务的实践》，内容包括：</p>
<p>业务场景业务实践Flink 使用过程中的问题及解决未来规划</p>
</blockquote>
<h1 data-id="heading-0">一、业务场景</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8973402763854c74a526f23db94065fe~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>实时数据在广告业务的使用场景主要可以分为四个方面：</p>
<ul>
<li>**数据大屏：**包括曝光、点击、收入等核心指标的展示，以及故障率等监控指标；</li>
<li>**异常监测：**因为广告投放的链路比较⻓，所以如果链路上发生任何波动的话，都会对整体的投放效果产生影响。除此之外，各个团队在上线过程中是否会对整体投放产生影响，都是通过异常监测系统能够观测到的。我们还能够观测业务指标走势是否合理，比如在库存正常的情况下，曝光是否有不同的波动情况，这可以用来实 时发现问题;</li>
<li>**数据分析：**主要用于数据赋能业务发展。我们可以实时分析广告投放过程中的一些异常问题，或者基于当前的投放效果去研究怎样优化，从而达到更好的效果;</li>
<li>**特征工程：**广告算法团队主要是做一些模型训练，用于支持线上投放。技术特征最初大部分是离线，随着实时的发展，开始把一些工程转到实时。</li>
</ul>
<h1 data-id="heading-1">二、业务实践</h1>
<p>业务实践主要分为两类，第一个是实时数仓，第二个是特征工程。</p>
<p><strong>1. 实时数仓</strong></p>
<p>1.1 实时数仓 - 目标</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ad6b2ab9498483c9acf033f71f219de~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>实时数仓的目标包括数据完整性、服务稳定性和查询能力。</p>
<ul>
<li>**数据完整性：**在广告业务里，实时数据主要是用于指导决策，比如广告主需要根据当前投放的实时数据，指导后面的出价或调整预算。另外，故障率的监控需要数据本身是稳定的。如果数据是波动的，指导意义就非常差，甚至没有什么指导意义。因此完整性本身是对时效性和完整性之间做了一个权衡；</li>
<li>**服务稳定性：**生产链包括数据接入、计算（多层）、数据写入、进度服务和查询服务。除此之外还有数据质量，包括数据的准确性以及数据趋势是否符合预期；</li>
<li>**查询能力：**在广告业务有多种使用场景，在不同场景里可能使用了不同的 OLAP 引擎，所以查询方式和性能的要求不一致。另外，在做数据分析的时候，除了最新最稳定的实时数据之外，同时也会实时 + 离线做分析查询，此外还包括数据跨源和查询性能等要求。</li>
</ul>
<p>1.2 实时数仓 - 挑战</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd4593fd481f4376956b9b1b6ebf9e83~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>**数据进度服务：**需要在时效性和完整性之间做一个权衡。</li>
<li>**数据稳定性：**由于生产链路比较长，中间可能会用到多种功能组件，所以端到端的服务稳定性对整体数据准确性的影响是比较关键的。</li>
<li>**查询性能：**主要包括 OLAP 分析能力。在实际场景中，数据表包含了离线和实时，单表规模达上百列，行数也是非常大的。</li>
</ul>
<p>1.3 广告数据平台架构</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ced2efe742e24350a636f7aeac6e87af~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图为广告数据平台基础架构图，从下往上看：</p>
<ul>
<li>底部是数据采集层，这里与大部分公司基本一致。业务数据库主要包含了广告主的下单数据以及投放的策略；埋点日志和计费日志是广告投放链路过程中产生的日志；</li>
<li>中间是数据生产的部分，数据生产的底层是大数据的基础设施，这部分由公司的一个云平台团队提供，其中包含 Spark / Flink 计算引擎，Babel 统一的管理平台。Talos 是实时数仓服务，RAP 和 OLAP 对应不同的实时分析以及 OLAP 存储和查询服务。数据生产的中间层是广告团队包含的一些服务，例如在生产里比较典型的离线计算和实时计算。离线是比较常见的一个分层模型，调度系统是对生产出的离线任务做有效的管理和调度。实时计算这边使用的引擎也比较多，我们的实时化是从 2016 年开始，当时选的是 Spark Streaming，后面随着大数据技术发展以及公司业务需求产生了不同场景，又引入了计算引擎 Flink。实时计算底层调度依赖于云计算的 Babel 系统，除了计算之外还会伴随数据治理，包括进度管理，就是指实时计算里一个数据报表当前已经稳定的进度到哪个时间点。离线里其实就对应一个表，有哪些分区。血缘管理包括两方面，离线包括表级别的血缘以及字段血缘。实时主要还是在任务层面的血缘。至于生命周期管理，在离线的一个数仓里，它的计算是持续迭代的。但是数据保留时间非常长的话，数据量对于底层的存储压力就会比较大。数据生命周期管理主要是根据业务需求和存储成本之间做一个权衡。质量管理主要包括两方面，一部分在数据接入层，判断数据本身是否合理；另外一部分在数据出口，就是结果指标这一层。因为我们的数据会供给其他很多团队使用，因此在数据出口这一层要保证数据计算没有问题。</li>
<li>再上层是统一查询服务，我们会封装很多接口进行查询。因为数据化包括离线和实时，另外还有跨集群，所以在智能路由这里会进行一些选集群、选表以及复杂查询、拆分等核心功能。查询服务会对历史查询进行热度的统一管理。这样一方面可以更应进一步服务生命周期管理，另一方面可以去看哪些数据对于业务的意义非常大。除了生命周期管理之外，它还可以指导我们的调度系统，比如哪些报表比较关键，在资源紧张的时候就可以优先调度这些任务。</li>
<li>再往上是数据应用，包括报表系统、Add - hoc 查询、数据可视化、异常监控和下游团队。</li>
</ul>
<p>1.4 实时数仓 - 生产链路</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e947e129dd524f44b9f3be39138cf813~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>数据生产链路是从时间粒度来讲的，我们最开始是离线数仓链路，在最底层的这一行，随着实时化需求推进，就产生了一个实时链路，整理来说，是一个典型的 Lambda 架构。</p>
<p>另外，我们的一些核心指标，比如计费指标，因为它的稳定性对下游比较关键，所以我们这边采用异路多活。异路多活是源端日志产生之后，在计算层和下游存储层做了完全的冗余，在后面的查询里做统一处理。</p>
<p>1.5 实时数仓 - 进度服务</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1875d0490ab64483bbd823204ca3f83d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上文介绍了我们要求提供出去的实时数据的指标是稳定不变的，进度服务实现的核心点包括时间窗口里指标的变化趋势，同时结合了实时计算任务本身的状态，因为在实时数仓里，很多指标是基于时间窗口做聚合计算。</p>
<p>比如一个实时指标，我们输出的指标是 3 分钟，也就是说 4：00 这个时间点的指标的就包括了 4：00～4：03 的数据，4：03 包括了 4：03～4：06 的数据，其实就是指一个时间窗口的数据，什么时候是对外可见的。因为在实时计算里，数据不断进来， 4：00 的时间窗口的数据从 4：00 开始，指标就已经开始产生了。随着时间叠加，指标不断上升，最后趋于稳定。我们基于时间窗口指标的变化率，来判断它是否趋于稳定。</p>
<p>但如果只是基于这个点来看，那么它还存在一定的弊端。</p>
<p>因为这个结果表的计算链会依赖很多个计算任务，如果这个链路上面哪个任务出现问题，可能会导致当前的指标虽然走势已经趋于正常，但是最终并不完整。所以在这基础之上，我们又引入了实时计算任务状态，在指标趋于稳定的时候，同时去看生产链路上这些计算任务是否正常，如果是正常的话，表示任务本身时间点的指标已经稳定，可以对外提供服务。</p>
<p>如果计算有卡顿、堆积，或者已经有异常在重启过程中，就需要继续等待迭代处理。</p>
<p>1.6 实时数仓 - 查询服务</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6c3edbffbc646c1a4d8f0ba109053cd~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图为查询服务架构图。</p>
<p>最下方是数据，里面有实时存储引擎，包括 Druid 等。在离线中，数据在 Hive 里边，但是在做查询的时候，会把它们进行 OLAP 的同步，在这边使用的是两种引擎。为了和 Kudu 做 union 查询，会把它同步到 OLAP 引擎，然后上面去统一使用 Impala 做查询。另外，对于使用场景里比较固定的方式，可以导到 Kylin 里，然后在上面做数据分析。</p>
<p>基于这些数据，会有多个查询节点，再上面是一个智能路由层。从最上面查询网关，当有一个查询请求进来，首先判断它是不是一个复杂场景。比如在一个查询里，如果它的时长同时跨越了离线和实时，这里就会同时使用到离线表和实时表。</p>
<p>另外，离线表里还有更复杂的选表逻辑，比如小时级别，天级别。经过复杂场景分析之后，就会把最终选择的表大概确定下来。其实在做智能路由的时候，才会去参考左边的一些基础服务，比如元数据管理，当前这些表的进度到哪个点了。</p>
<p>对于查询性能的优化，在数据里，底层扫描的数据量对最终性能的影响是非常大的。所以会有一个报表降维，根据历史的查询去做分析。比如在一个降维表包含哪些维度，可以覆盖到百分之多少的查询。</p>
<p>1.7 数据生产 - 规划</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06b5103fc71f4e4390804fabc192d040~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>之前在实时数据报表生产里提到，它主要是基于 API 的方式实现的。Lambda 架构本身有一个问题就是实时跟离线是两个计算团队，对于同一个需求，需要两个团队同时去开发，这样会带来几个问题。</p>
<ul>
<li>一方面是他们的逻辑可能会发生差异，最终导致结果表不一致；</li>
<li>另一方面是人力成本，同时需要两个团队进行开发。</li>
</ul>
<p>因此我们的诉求是流批一体，思考在计算层是否可以使用一个逻辑来表示同一个业务需求，比如可以同时使用流或者批的计算引擎来达到计算的效果。</p>
<p>在这个链路里边，原始数据通过 Kafka 的方式接入进来，经过统一的 ETL 逻辑，接着把数据放在数据湖里。因为数据湖本身可以同时支持流和批的方式进行读写，而且数据湖本身可以实时消费，所以它既可以做实时计算，也可以做离线计算，然后统一把数据再写回数据湖。</p>
<p>前文提到在做查询的时候，会使用离线跟实时做统一整合，所以在数据湖里写同一个表，在存储层面可以省去很多工作，另外也可以节省存储空间。</p>
<p>1.8 数据生产 - SQL 化</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/888abf5a55ae4d08bbb5e9f658ba4e98~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>SQL 化是 Talos 实时数仓平台提供的能力。</p>
<p>从页面上来看，它包括了几个功能，左边是项目管理，右边包括 Source、Transform 和 Sink。</p>
<ul>
<li>有一些业务团队本身对于计算引擎算子非常熟，那么他们便可以做一些代码开发；</li>
<li>但是很多业务团队可能对引擎并不是那么了解，或者没有强烈的意愿去了解，他们就可以通过这种可视化的方式，拼接出一个作业。</li>
</ul>
<p>例如，可以拖一个 Kafka 的数据源进来，在上面做数据过滤，然后就可以拖一个 Filter 算子达到过滤逻辑，后面可以再去做一些 Project，Union 的计算，最后输出到某个地方就可以了。</p>
<p>对于能力稍微高一些的同学，可以去做一些更高层面的计算。这里也可以实现到实时数仓的目的，在里面创建一些数据源，然后通过 SQL 的方式，把逻辑表示出来，最终把这个数据输出到某种存储。</p>
<p>上面是从开发层面来讲，在系统层面上，它其实还提供了一些其他的功能，比如规则校验，还有开发/测试/上线，在这里可以统一管理。此外还有监控，对线上跑的实时任务有很多实时指标，可以通过查看这些指标来判断当前的任务是不是正常的状态。</p>
<p><strong>2. 特征工程</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f2660cfb7ff4e928316a047c393d4f2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>特征工程有两方面的需求：</p>
<ul>
<li>第一个需求是实时化，因为数据价值随着时间的递增会越来越低。比如某用户表现出来的观影行为是喜欢看儿童内容，平台就会推荐儿童相关的广告。另外，用户在看广告过程中，会有一些正/负反馈的行为，如果把这些数据实时迭代到特征里，就可以有效提升后续的转化效果。</li>
<li>实时化的另一个重点是准确性，之前很多特征工程是离线的，在生产环节里面存在计算时的数据跟投放过程中的特征有偏差，基础特征数据不是很准确，因此我们要求数据要更实时、更准确。</li>
<li>特征工程的第二个需求是服务稳定性。首先是作业容错，比如作业在异常的时候能否正常恢复；另外是数据质量，在实时数据里追求端到端精确一次。</li>
</ul>
<p>2.1 点击率预估</p>
<p>下面是在特征实时化里的实践，首先是点击率预估的需求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be691874da22446ea4ebb68a74468b75~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击率预估案例的背景如上所示，从投放链路上来说，在广告前端用户产生观影行为，前端会向广告引擎请求广告，然后广告引擎在做广告召回粗排/精排的时候会拿到用户特征和广告特征。把广告返回给前端之后，后续用户行为可能产生曝光、点击等行为事件，在做点击率预估的时候，需要把前面请求阶段的特征跟后续用户行为流里的曝光和点击关联起来，形成一个 Session 数据，这就是我们的数据需求。</p>
<p>落实到具体实践的话包括两方面：</p>
<ul>
<li>一方面是 Tracking 流里曝光、点击事件的关联；</li>
<li>另一方面是特征流跟用户行为的关联。</li>
</ul>
<p>在实践过程中有哪些挑战？</p>
<ul>
<li>第一个挑战是数据量；</li>
<li>第二个挑战是实时数据乱序和延迟；</li>
<li>第三个挑战是精确性要求高。</li>
</ul>
<p>在时序上来说，特征肯定是早于 Tracking，但是两个流成功关联率在 99% 以上的时候，这个特征需要保留多久？因为在广告业务中，用户可以离线下载一个内容，在下载的时候就已经完成了广告请求和返回了。但是后续如果用户在没有网的情况下观看，这个事件并不会立马返回，只有当状态恢复的时候，才会有后续曝光和点击事件回传。</p>
<p>所以这个时候，其实特征流和 Tracking 的时间概括是非常长的。我们经过离线的数据分析，如果两个流的关联率达 99% 以上，那么特征数据就需要保留比较长的时间，目前是保留 7 天，这个量级还是比较大的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a011d74a8914496487cbf20403b1c709~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图为点击率预测的整体架构，刚才我们提到关联包括两部分：</p>
<ul>
<li>第一个部分是用户行为流里曝光跟点击事件的关联，这里通过 CEP 实现。</li>
<li>第二个部分是两个流的关联，前面介绍特征需要保留 7 天，它的状态较大，已经是上百 TB。这个量级在内存里做管理，对数据稳定性有比较大的影响，所以我们把特征数据放在一个外部存储 (Hbase) 里，然后和 HBase 特征做一个实时数据查询，就可以达到这样一个效果。</li>
</ul>
<p>但是因为两个流的时序本身可能是错开的，就是说，当曝光、点击出现的时候，可能这个特征还没有到，那么就拿不到这个特征。所以我们做了一个多级重试队列，保证最终两个流关联的完整性。</p>
<p>2.2 点击率预估 - 流内事件关联</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/488a98dcba5841b1ac13e2066704cbb1~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图右边是更细的讲解，阐述了流内事件关联为什么选择 CEP 方案。业务需求是把用户行为流里属于同一次广告请求，并且是同一个广告的曝光跟点击关联起来。曝光之后，比如 5 分钟之内产生点击，作为一个正样本，5 分钟之后出现的点击则抛弃不要了。</p>
<p>可以想象一下，当遇到这样的场景，通过什么样的方案可以实现这样的效果。其实在一个流里多个事件的处理，可以用窗口来实现。但窗口的问题是：</p>
<ul>
<li>如果事件序列本身都在同一个窗口之内，数据没有问题；</li>
<li>但是当事件序列跨窗口的时候，是达不到正常关联效果的。</li>
</ul>
<p>所以当时经过很多技术调研后，发现 Flink 里的 CEP 可以实现这样的效果，用类似政策匹配的方式，描述这些序列需要满足哪些匹配方式。另外它可以指定一个时间窗口，比如曝光和点击间隔 15 分钟。</p>
<p>上图左边是匹配规则的描述，begin 里定义一个曝光，实现曝光之后 5 分钟之内的点击，后面是描述一个可以出现多次的点击，within 表示关联窗口是多长时间。</p>
<p>在生产实践过程中，这个方案大部分情况下可以关联上，但是在做数据对比的时候，才发现存在某些曝光点击没有正常关联到。</p>
<p>经过数据分析，发现这些数据本身的特点是曝光跟点击的时间戳都是毫秒级别，当它们有相同毫秒时间戳的时候，这个事件就不能正常匹配。于是我们采用一个方案，人为地对于点击事件加一毫秒，进行人工错位，这样就保证曝光跟点击能够成功关联上。</p>
<p>2.3 点击率预估-双流关联</p>
<p>前文提到特征数据需要保留 7 天，所以状态是上百 TB。需要把数据放在一个外部存储里，因此在做技术选型时对外部存储有一定的要求：</p>
<ul>
<li>首先支持比较高的读写并发能力；</li>
<li>另外它的时效性需要非常低；</li>
<li>同时因为数据要保留 7 天，所以它最好具备生命周期管理能力。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/557827cb5a1b42819711b8e7264ed1cc~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>基于以上几个点，最终选择了 HBase，形成上图的解决方案。</p>
<p>上面一行表示通过 CEP 之后把曝光点击序列关联在一起，最下面是把特征流通过 Flink 写到 HBase 里，去做外部状态存储，中间核心模块是用于达到两个流的关联。拿到曝光点击关联之后去查 HBase 数据，如果能够正常查到，就会把它输出到一个正常结果流里。而对于那些不能构成关联的数据，做了一个多级重试队列，在多次重试的时候会产生队列降级，并且在重试的时候为了减轻对 HBase 的扫描压力，重试 Gap 会逐级增加。</p>
<p>另外还有一个退出机制，因为重试不是无限进行的。退出机制的存在原因主要包括两个点：</p>
<ul>
<li>第一点是特征数据保留了 7 天，如果对应特征是在 7 天之前，那么它本身是关联不到的。</li>
<li>另外在广告业务里，存在一些外部的刷量行为，比如刷曝光或刷点击，但它本身并没有真实存在的广告请求，所以这种场景也拿不到对应特征。</li>
</ul>
<p>因此，退出机制意味着在重试多次之后就会过期，然后会到重试过期的数据里。</p>
<p>2.4 有效点击</p>
<p>在有效点击场景里，其实也是两个流的关联，但是两个场景里的技术选型是完全不一样的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d30778714db44ce28088d5afaf0edde5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先看一下项目背景，在网大场景里，影片本身就是一个广告。用户在点击之后，就会进入到一个播放页面。在播放页面里，用户可以免费观看 6 分钟，6 分钟之后想要继续观看，需要是会员或者购买才行，在这里需要统计的数据是有效点击，定义是在点击之后观影时长超过 6 分钟即可。</p>
<p>这种场景落实到技术上是两个流的关联，包括了点击流和播放心跳流。</p>
<ul>
<li>点击流比较好理解，包括用户的曝光和点击等行为，从里面筛选点击事件即可。</li>
<li>播放行为流是在用户观看的过程，会定时地把心跳信息回传，比如三秒钟回传一个心跳，表明用户在持续观看。在定义时长超过 6 分钟的时候，需要把这个状态本身做一些处理，才能满足 6 分钟的条件。</li>
</ul>
<p>在这个场景里，两个流动 Gap 相对比较小，而在电影里时长一般是两个多小时，所以点击之后的行为，Gap 基本是在三个小时以内才能完成，因此这里本身的状态是相对比较小的，使用 Flink 的状态管理可以达到这样的效果。</p>
<p>接下来我们看一个具体的方案。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52ccb65a003c438ea59375d6cfa4987d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从流上来看，绿色部分是点击流，蓝色部分是播放心跳流。</p>
<ul>
<li>在左边的状态里面，一个点击事件进来之后，会对这个点击做一个状态记录，同时会注册一个定时器做定期清理，定时器是三个小时。因为大部分影片的时长在三小时以内，如果这个时候对应的播放事件还没有一个目标状态，点击事件基本就可以过期了。</li>
<li>在右边的播放心跳流里，这个状态是对时长做累计，它本身是一个心跳流，比如每三秒传一个心跳过来。我们需要在这里做一个计算，看它累计播放时长是不是达到 6 分钟了，另外也看当前记录是不是到了 6 分钟。对应 Flink 里的一个实现就是把两个流通过 Connect 算子关系在一起，然后可以制定一个 CoProcessFunction，在这里面有两个核心算子。第一个算子是拿到状态 1 的流事件之后，需要做一些什么样的处理；第二个算子是拿到第 2 个流事件之后，可以自定义哪些功能。算子给用户提供了很多灵活性，用户可以在里面做很多逻辑控制。相比很多的 Input Join，用户可发挥的空间比较大。</li>
</ul>
<p>2.5 特征工程 - 小结</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de3a29c8f5c746cbba05308d13a22a23~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>针对以上案例做一个小结。现在双流管理已经非常普遍，有许多方案可以选择，比如 Window join，Interval join，还有我们使用的 Connect + CoProcessFunction。除此之外，还有一些用户自定义的方案。</p>
<p>在选型的时候，建议从业务出发，去做对应的技术选型。首先要思考多个流之间的事件关系，然后判断出状态是什么规模，一定程度上可以从上面很多方案里排除不可行的方案。</p>
<h1 data-id="heading-2">三、Flink 使用过程中的问题及解决</h1>
<p><strong>1. 容错</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/314fd4149f454d64b12118a451f1778b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 Flink 内部主要是通过 Checkpoint 做容错，Checkpoint 本身是对于 Job 内部的 Task 级别的容错，但是当 Job 主动或异常重启时，状态无法从历史状态恢复。</p>
<p>因此我们这边做了一个小的改进，就是一个作业在启动的时候，它也会去 Checkpoint 里把最后一次成功的历史状态拿到，然后做初始化管理，这样就达到状态恢复的效果。</p>
<p><strong>2. 数据质量</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3eeeb08a2bb4491ba22fdcfab0b5eac2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Flink 本身实现端到端精确一次，首先需要开启 Checkpoint 功能，并且在 Checkpoint 里指定精确一次的语义。另外，如果在下游比如 Sink 端，它本身支持事务，就可以结合两阶段提交与 Checkpoint 以及下游的事务做联动，达到端到端精确一次。</p>
<p>在上图右边就是描述了这个过程。这是一个预提交的过程，就是 Checkpoint 协调器在做 Checkpoint 的时候，会往 Source 端注入一些 Barrier 数据，每个 Source 拿到 Barrier 之后会做状态存储，然后把完成状态反馈给协调器。这样每个算子拿到 Barrier，其实是做相同的一个功能。</p>
<p>到 Sink 端之后，它会在 Kafka 里提交一个预提交标记，后面主要是 Kafka 本身事务机制来保证的。在所有的算子都完成 Checkpoint 之后，协调器会给所有的算子发一个 ACK，发送一个确认状态，这时候 Sink 端做一个提交动作就可以了。</p>
<p><strong>3. Sink Kafka</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/070ccd0b689843e99bd12d635e818430~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在之前的实践中我们发现，下游 Kafka 增加分区数时，新增分区无数据写入。</p>
<p>原理是 FlinkKafkaProducer 默认使用 FlinkFixedPartitioner，每个 Task 只会发送到下游对应的一个 Partition 中，如果下游 Kafka 的 Topic 的 Partition 大于当前任务的并行度，就会出现该问题。</p>
<p>解决办法有两个：</p>
<ul>
<li>第一个办法是用户自定义一个 FlinkKafkaPartitioner；</li>
<li>另一个办法是默认不配置，默认轮询写入各个 Partition。</li>
</ul>
<p><strong>4. 监控加强</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0a10f964f8a48b2ab8667dcad9a18e6~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于运行中的 Flink 作业，我们需要查看它本身的一些状态。比如在 Flink UI 里面，它的很多指标都是在 Task 粒度，没有整体的效果。</p>
<p>平台这边对这些指标做了进一步的聚合，统一在一个页面里面展示。</p>
<p>从上图可以看到，展示信息包括反压状态，时延情况以及运行过程中 JobManager 和 TaskManage 的 CPU / 内存的利用率。另外还有 Checkpoint 的监控，比如它是否超时，最近是否有 Checkpoint 已经失败了，后面我们会针对这些监控指标做一些报警通知。</p>
<p><strong>5. 监控报警</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23b3f27afc5a4a1ca02c8d16d5ab6891~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当实时任务运营异常的时候，用户是需要及时知道这个状态的，如上图所示，有一些报警项，包括报警订阅人、报警级别，下面还有一些指标，根据前面设置的指标值，如果满足这些报警策略规则，就会给报警订阅人推送报警，报警方式包括邮件、电话以及内部通讯工具，从而实现任务异常状态通知。</p>
<p>通过这种方式，当任务异常的时候，用户可以及时知晓这个状态，然后进行人为干预。</p>
<p><strong>6. 实时数据生产</strong></p>
<p>最后总结一下爱奇艺广告业务在实时链路生产上面的关键节点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb27eb4b3ac647809fd8fc38ad52495d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>我们的实时是从 2016 年开始起步，当时主要功能点是做一些指标实时化，使用的是 SparkStreaming；</li>
<li>2018 年上线了点击率实时特征；</li>
<li>2019 年上线了 Flink 的端到端精确到一次和监控强化。</li>
<li>2020 年上线了有效点击实时特征；</li>
<li>同年10月，逐步推进实时数仓的改进，把 API 生产方式逐渐 SQL 化；</li>
<li>2021 年 4 月，进行流批一体的探索，目前先把流批一体放在 ETL 实现。</li>
</ul>
<p>之前我们的 ETL 实时跟离线是分别做的，通过批处理的方式，然后换到 Hive 表里边，后面跟的是离线数仓。在实时里，经过实时 ETL，放到 Kafka 里边，然后去做后续的实时数仓。</p>
<p>先在 ETL 做流批一体的第一个好处是离线数仓时效性提升，因为数据需要做反作弊，所以我们给广告算法提供基础特征的时候，反作弊之后的时效性对于后续整体效果的提升是比较大的，所以如果把 ETL 做成统一实时化之后，对于后续的指导意义非常大。</p>
<p>ETL 做到流批一体之后，我们会把数据放在数据湖里面，后续离线数仓和实时数仓都可以基于数据湖实现。流批一体可以分为两个阶段，第一阶段是先把 ETL 做到一体，另外报表端也可以放在数据湖里边，这样我们的查询服务可以做到一个更新的量级。因为之前需要离线表跟实时表做一个 Union 的计算，在数据湖里面，我们通过离线和实时写一个表就可以实现了。</p>
<h1 data-id="heading-3">四、未来规划</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6996707614d42499cbff4574f0ed9f8~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>关于未来规划：</p>
<ul>
<li>首先是流批一体，这里包括两个方面：第一个是 ETL 一体，目前已经是基本达到可线上的状态。第二个是实时报表 SQL 化和数据湖的结合。</li>
<li>另外，现在的反作弊主要是通过离线的方式实现，后面可能会把一些线上的反作弊模型转成实时化，把风险降到最低。</li>
</ul>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000287901%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000287901/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            