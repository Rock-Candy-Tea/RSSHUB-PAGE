
---
title: '蚂蚁集团 SOFATracer 原理与实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbe872c5b61847d5a1bc8e777586d2fb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 21:41:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbe872c5b61847d5a1bc8e777586d2fb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>微服务架构带来很多好处的同时也让系统的复杂度提升了，传统的单体应用按照不同的维度拆分成一个一个分布式微服务，不同的微服务甚至可能采用不同的语言编写；此外，服务的部署往往都是分布式的，可能有几千台服务器，横跨多个不同的城市数据中心。下图是一个典型的微服务架构，图中的节点数还比较少，在支付宝，一个线下支付整体交易付款链路，涉及上百个节点。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbe872c5b61847d5a1bc8e777586d2fb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>图片来源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.splunk.com%2Fen_us%2Fdata-insider%2Fwhat-is-distributed-tracing.html%23benefits-of-distributed-tracing" target="_blank" rel="nofollow noopener noreferrer" title="https://www.splunk.com/en_us/data-insider/what-is-distributed-tracing.html#benefits-of-distributed-tracing" ref="nofollow noopener noreferrer">www.splunk.com/en_us/data-…</a></p>
<p>微服务化引入了以下几个典型问题：</p>
<ol>
<li>
<p>故障定位难，一次请求往往需要涉及到多个服务，排查问题甚至需要拉上多个团队</p>
</li>
<li>
<p>完整调用链路梳理难，节点调用关系分析</p>
</li>
<li>
<p>性能分析难，性能短板节点</p>
</li>
</ol>
<p>以上这几个问题其实都是应用的可观测性问题：</p>
<ol>
<li>
<p>log</p>
</li>
<li>
<p>Trace</p>
</li>
<li>
<p>metrics</p>
</li>
</ol>
<p>本文将会专注于 Trace 方面，完整地说是分布式链路跟踪 (Distributed tracing)。2010 年谷歌发表了 Dapper 的论文，分享了他们的解决方案，算是业界比较早的分布式链路追踪系统。之后各大互联网公司纷纷参照 Dapper 的思想推出各自的链路跟踪系统，包括 Twitter 的 Zipkin、阿里的鹰眼，还有 PinPoint，Apache 的 HTrace 和 Uber 的 Jaeger；当然，也有我们的本文的主角：SOFATracer。分布式链路的实现有多种多样，因此也催生了分布式链路追踪的规范：OpenTracing，2019 年 OpenTracing 和 OpenCensus 合并成为了 OpenTelemetry。</p>
<h3 data-id="heading-1">OpenTracing</h3>
<p>在深入 SOFATracer 之前先简单解释一下 OpenTracing，因为 SOFATTracer 是基于 OpenTracing 规范（基于 0.22.0 的 OpenTracing，新版的规范 API 有所不同）构建的。一个 Trace 由服务调用生成的 Span 及其之间的引用构成，一个 Span 是一个时间跨度，一次服务调用创建一个新 Span，分为调用 Span 和被调 Span，每个 Span 包含：</p>
<ol>
<li>
<p>TraceId and SpanId</p>
</li>
<li>
<p>操作名称</p>
</li>
<li>
<p>耗时</p>
</li>
<li>
<p>服务调用结果</p>
</li>
</ol>
<p>一个 Trace 链路中一般会有多个服务调用，那么也就会有多个 Span，Span 之间的关系由引用声明，引用从调用者指向服务提供者，OpenTracing 中指定了两个引用类型：</p>
<ol>
<li>
<p>ChildOf，同步服务调用，客户端需要服务端的结果返回才能进行后续处理；</p>
</li>
<li>
<p>FollowsFrom，异步服务调用，客户端不等待服务端结果。</p>
</li>
</ol>
<p>一个 Trace 是一个有向无环图，一次调用的拓扑可以如下展示：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d99f4936f9e64ddfb3df0b88e8e6bec8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>图中的 SpanContext 是一次请求中会共享的数据，因此叫做 Span 上下文，一个服务节点在上下文中放入的数据对于后续的所有节点都可见，因此可以用来做信息传递。</p>
<h2 data-id="heading-2">SOFATracer</h2>
<h3 data-id="heading-3">TraceId 生成</h3>
<p>TraceId 收集一次请求中的所有服务节点。其生成规则需要避免不同 TraceId 之间的冲突，并且开销不能很高，毕竟 Trace 链路的生成是业务逻辑之外的额外开销。SOFATracer 中的 TraceId 生成规则是：服务器 IP + 产生 ID 时候的时间 + 自增序列 + 当前进程号，比如：</p>
<pre><code class="hljs language-bash copyable" lang="bash">0ad1348f1403169275002100356696
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前 8 位 0ad1348f 即产生 TraceId 的机器的 IP，这是一个十六进制的数字，每两位代表 IP 中的一段，我们把这个数字，按每两位转成 10 进制即可得到常见的 IP 地址表示方式 10.209.52.143，大家也可以根据这个规律来查找到请求经过的第一个服务器。 后面的 13 位 1403169275002 是产生 TraceId 的时间。 之后的 4 位 1003 是一个自增的序列，从 1000 涨到 9000，到达 9000 后回到 1000 再开始往上涨。 最后的 5 位 56696 是当前的进程 ID，为了防止单机多进程出现 TraceId 冲突的情况，所以在 TraceId 末尾添加了当前的进程 ID。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aada72b7f3ea4cedadcf16eadb30438f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>伪代码如下：</p>
<pre><code class="hljs language-java copyable" lang="java">TraceIdStr.append(ip).append(System.currentTimeMillis())
append(getNextId()).append(getPID());
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">SpanId 生成</h3>
<p>SpanId 记录服务调用拓扑，在 SOFATracer 中：</p>
<ol>
<li>
<p>点代表调用深度</p>
</li>
<li>
<p>数字代表调用顺序</p>
</li>
<li>
<p>SpanId 由客户端创建</p>
</li>
</ol>
<blockquote>
<p>SOFATracer 中 TraceId 和 SpanId 的生成规则参考了阿里的鹰眼组件</p>
</blockquote>
<p>合并调用 Span 和被调 Span，结合 TraceId 和 SpanId 就能构建完整的服务调用拓扑：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bafa77190cbc433895bb89b908980418~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h3 data-id="heading-5">Trace 埋点</h3>
<p>但是，我们如何生成并获取到 Trace 数据呢？这就得 Trace 采集器（Instrumentation Framework）登场了，其负责：</p>
<ol>
<li>
<p>Trace 数据的生成、传递和上报</p>
</li>
<li>
<p>Trace 上下文的解析和注入</p>
</li>
</ol>
<p>并且 Trace 采集器还要做到自动、低侵入和低开销等。典型的 Trace 采集器结构如下，其在业务逻辑之前埋点：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a2c083a80274db699dfd62ed18997ca~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<ol>
<li>
<p>Server Received (SR), 创建一个新的父 Span 或者从上下文中提取</p>
</li>
<li>
<p>调用业务代码</p>
</li>
<li>
<p>业务代码再次发起远程服务调用</p>
</li>
<li>
<p>Client Send (CS) 创建一个子 Span，传递 TraceId、SpanId 和透传数据</p>
</li>
<li>
<p>Client Received (CR), 结束当前子 Span，记录/上报 Span</p>
</li>
<li>
<p>Server Send (SS) 结束父 Span，记录/上报 Span</p>
</li>
</ol>
<p>步骤 3-5 可能没有，也可能重复多次。</p>
<p>埋点逻辑的实现多种多样，目前主流的有如下几种方式：</p>
<ol>
<li>
<p>Filter，请求过滤器 (dubbo, SOFARPC, Spring MVC)</p>
</li>
<li>
<p>AOP 切面 (DataSource, Redis, MongoDB)</p>
</li>
</ol>
<p>a.Proxy</p>
<p>b.ByteCode generating</p>
<ol start="3">
<li>Hook 机制 (Spring Message, RocketMQ)</li>
</ol>
<p>Java 语言中，SkyWalking 和 PinPoint 都使用 javaagent 方式做到自动、无侵入埋点。典型的，SOFATracer 实现 Spring MVC 的 Trace 埋点如下：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bed7fd30bde04de696150db1c9cda377~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>SOFATracer 的 Span 100% 创建，只是 log/report 支持采样，相对来说，log/report 的 overhead 更高，更容易在大流量/负载下成为性能瓶颈。而其他 Trace 系统，Span 是采样生成的，但为了在调用出错的情况下能 100% 有 Trace，他们采用了逆向采样的策略。</p>
<p>SOFATracer 默认把 Trace 信息打印到日志文件中</p>
<ol>
<li>
<p>client-digest：调用 Span</p>
</li>
<li>
<p>server-digest：被调用 Span</p>
</li>
<li>
<p>client-stat：一分钟内调用 Span 的数据聚合</p>
</li>
<li>
<p>server-stat：一分钟内被调用 Span 的数据聚合</p>
</li>
</ol>
<p>默认日志格式是 JSON，但是可以定制。</p>
<h2 data-id="heading-6">APM</h2>
<p>一个典型的 Trace 系统，除了 Trace 的采集上报之外，还会有收集器（Collector）、存储（Storage）和展示（API & UI）：Application Performance Management，简称 APM，如下图所示：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3104aff06ba945eb98daf685c6474348~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>图片来源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpinpoint-apm.github.io%2Fpinpoint%2Foverview.html" target="_blank" rel="nofollow noopener noreferrer" title="https://pinpoint-apm.github.io/pinpoint/overview.html" ref="nofollow noopener noreferrer">pinpoint-apm.github.io/pinpoint/ov…</a></p>
<p>Trace 数据上报一般要求包括实时性、一致性等，SOFATracer 默认支持  Zipkin 上报；在存储之前涉及到流式计算，调用 Span 和被调用 Span 的合并，一般采用 Alibaba JStorm 或者 Apache Flink；在处理完成之后会放到 Apache HBase 中，由于 Trace 数据只是短时间有用，因此一般会采取过期数据自动淘汰机制，过期时间一般是 7~10 天左右。最后的展示部分，从 HBase 中查询、分析需要支持：</p>
<ol>
<li>
<p>有向无环图的图形化展示</p>
</li>
<li>
<p>按照 TraceId 查询</p>
</li>
<li>
<p>按照调用者查询</p>
</li>
<li>
<p>按照被调用者查询</p>
</li>
<li>
<p>按照 IP 查询</p>
</li>
</ol>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/605f06fd2fb44d37955ab65f16be5d0a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>图片来源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpinpoint-apm.github.io%2Fpinpoint%2Fimages%2Fss_server-map.png" target="_blank" rel="nofollow noopener noreferrer" title="https://pinpoint-apm.github.io/pinpoint/images/ss_server-map.png" ref="nofollow noopener noreferrer">pinpoint-apm.github.io/pinpoint/im…</a></p>
<p>在蚂蚁集团内部，我们没有采用 Span 上报，而是 Span 打印到日志之后按需采集，其架构如下：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96c82fad1620496ab786519ba6b5b54b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>（其中 Relic 和 Antique 不是真实的系统名。）</p>
<p>宿主机上有 DaemonSet Agent 用于采集 Trace 日志，digest 日志用于问题排查 & stat 日志用于业务监控，也就是要采集的日志内容。日志数据采集之后，会经过 Relic 系统处理：单机日志数据清理、聚合；再之后经过 Antique 系统的进一步的整合，通过 Spark 将 Trace 的服务数据做应用和服务纬度的聚合。最后，我们将处理过后的 Trace 数据存到时序数据库 CeresDB 中，提供给 Web Console 查询和分析。这个系统还可以配置监控和报警，以便提前预警应用系统的异常。目前以上监控和报警可以做到准实时，有 1 分钟左右的延迟。</p>
<p>全链路追踪的发展一直在不断完善，功能不断丰富，现阶段涉及到的 Application Performance Management 不仅包含了全链路追踪的的完整能力，还包括：</p>
<ol>
<li>
<p>存储 & 分析，丰富的终端特性</p>
</li>
<li>
<p>全链路压测</p>
</li>
<li>
<p>性能剖析</p>
</li>
<li>
<p>监控 & 报警：CPU、内存和 JVM 信息等</p>
</li>
</ol>
<p>在蚂蚁集团内部，我们有专门的压测平台，平台发起压测流量的时候，会自带人为构造的 TraceId、SpanId 和透传数据（压测标志），实现日志分开打印。欢迎选用 SOFATracer 作为全链路追踪工具，SOFATracer 的快速开始指南 Link：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a306521da9a24406ac4f8f273722fc5a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h2 data-id="heading-7">展望</h2>
<p>SOFATracer 的未来发展规划如下，欢迎大家参与贡献！项目 Github 链接。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10399eef467346e1a57203ddb4e5360c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h2 data-id="heading-8">相关链接</h2>
<p>SOFATracer 快速开始：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-Tracer%2Fcomponent-access%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.sofastack.tech/projects/sofa-Tracer/component-access/" ref="nofollow noopener noreferrer">www.sofastack.tech/projects/so…</a></p>
<p>SOFATracer Github 项目：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-Tracer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sofastack/sofa-Tracer" ref="nofollow noopener noreferrer">github.com/sofastack/s…</a></p>
<p>OpenTracing：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopentracing.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://opentracing.io/" ref="nofollow noopener noreferrer">opentracing.io/</a></p>
<p>OpenTelemetry：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopentelemetry.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://opentelemetry.io/" ref="nofollow noopener noreferrer">opentelemetry.io/</a></p>
<h3 data-id="heading-9">本周推荐阅读</h3>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247491634%26idx%3D1%26sn%3D8359805abd97c598c058c6b5ad573d0d%26chksm%3Dfaa30fe8cdd486fe421da66237bdacb11d83c956b087823808ddaaff52c1b1900c02dbf80c07%26token%3D870420281" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247491634&idx=1&sn=8359805abd97c598c058c6b5ad573d0d&chksm=faa30fe8cdd486fe421da66237bdacb11d83c956b087823808ddaaff52c1b1900c02dbf80c07&token=870420281" ref="nofollow noopener noreferrer">KCL：声明式的云原生配置策略语言</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247491409%26idx%3D1%26sn%3Dd6c0722d55b772aedb6ed8e34979981d%26chksm%3Dfaa0f08bcdd7799dabdb3b934e5068ff4e171cffb83621dc08b7c8ad768b8a5f2d8668a4f57e%26token%3D870420281" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247491409&idx=1&sn=d6c0722d55b772aedb6ed8e34979981d&chksm=faa0f08bcdd7799dabdb3b934e5068ff4e171cffb83621dc08b7c8ad768b8a5f2d8668a4f57e&token=870420281" ref="nofollow noopener noreferrer">蚂蚁集团万级规模 k8s 集群 etcd 高可用建设之路</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247491198%26idx%3D1%26sn%3Da4607e6a8492e8749f31022ea9e22b80%26chksm%3Dfaa0f1a4cdd778b214403e36fb4322f91f3d1ac47361bf752c596709f8453b8482f582fe7e2e%26token%3D154358414" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247491198&idx=1&sn=a4607e6a8492e8749f31022ea9e22b80&chksm=faa0f1a4cdd778b214403e36fb4322f91f3d1ac47361bf752c596709f8453b8482f582fe7e2e&token=154358414" ref="nofollow noopener noreferrer">我们做出了一个分布式注册中心</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247490574%26idx%3D1%26sn%3D791b8d49759131ea1feb5393e1b51e7c%26chksm%3Dfaa0f3d4cdd77ac2316b179a24b7c3ac90a08d3768379795d97c18b14a9c69e4b82012c3c097" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247490574&idx=1&sn=791b8d49759131ea1feb5393e1b51e7c&chksm=faa0f3d4cdd77ac2316b179a24b7c3ac90a08d3768379795d97c18b14a9c69e4b82012c3c097" ref="nofollow noopener noreferrer">还在为多集群管理烦恼吗？OCM来啦！</a></p>
</li>
</ul>
<p>更多文章请扫码关注“金融级分布式架构”公众号</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0c7840a52ff48e4add881ac882a96f6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote></div>  
</div>
            