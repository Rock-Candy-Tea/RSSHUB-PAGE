
---
title: '微服务的终极目标，Mecha分布式运行时之Dapr'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01464bfaecb8415c9659635456543e98~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 07:40:43 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01464bfaecb8415c9659635456543e98~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第25天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">1. Mecha 是啥？</h1>
<p>微服务发展到今天，已经有很多公司多年前已经改造完毕，也有些公司还在路上，微服务的优势，有过了解的朋友应该也都能说出个一二三来，经历过微服务改造的，应该都知道其中的艰辛。</p>
<p>单体服务有着很多优势，结构简单、事务的ACID保证，系统内的无缝调用，一旦改造为微服务，必然是分布式服务构造，服务间的不稳定性，通讯的复杂性都使得整个系统的复杂性提升。</p>
<p>随着大量的三方服务的引入，也带来了网络、绑定、状态、生命周期管理等的各方面膨胀的需求，Red Hat的首席架构师Bilgin Ibryam从自己的经验出发，提出了未来的发展方向——多运行时微服务架构。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01464bfaecb8415c9659635456543e98~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>他简要的概括了微服务的在四个维度的基本需求。</p>
<p>为了满足这些需求，或者换句话说，应该有个 机甲装备-Macha，穿上它，就能实现微服务。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6231cb703ad4334b78a8616fc5af55b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是的，从蛮荒走向科技，必然会形成的科技天梯。</p>
<p>业务人员在未来的某一天，可以不需要考虑这些基础设施服务，只需要一张清单，Mecha就能满足你。</p>
<h1 data-id="heading-1">2.微软开源的世界第一个分布式运行时Dapr</h1>
<p>顺时而生的Dapr，是不是那个赢家？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c8146f41c364c789e9d0a30af85f3d4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>官方介绍：Dapr 是一个可移植的、无服务器的、事件驱动的运行时，它使开发人员可以轻松构建在云和边缘运行的弹性、无状态和有状态的微服务，并包含语言和开发人员框架的多样性。</p>
<p>Dapr 将构建微服务应用程序的<em>最佳实践</em>编码为开放、独立的构建块，使您能够使用您选择的语言和框架构建可移植的应用程序。每个构建块都是独立的，您可以在应用程序中使用其中的一个、部分或全部。</p>
<p>是的，Dapr制定了和各个基础服务通讯的标准，并对我开放Api以实现编码语言的弱依赖。其提供了众多语言的HTTP、GRPC协议的SDK，使得你可以使用薄薄的SDK层，就可以和所有基础设施服务进行通讯。</p>
<p>Dapr部署方式可以是SideCar，或者Node方式，其来自云原生，和Kuberbetes配合极好；在没有K8s的环境也可以运行，部署灵活而不限制。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/529cb70635354ec4b294943bcfa2570b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了能够和其他基础设施服务进行通信外，其还提供了状态管理、pub/sub消息、Actors、可观测、安全存储等特性。</p>
<p>哦哦哦，令我遗憾的是它竟然是Go语言写的，好吧，又是Go语言从业者的狂欢。</p>
<h1 data-id="heading-2">3.dapr特性</h1>
<ul>
<li>事件驱动的发布订阅系统，具有可插入的提供者和至少一次语义</li>
<li>与可插入提供程序的输入和输出绑定</li>
<li>具有可插拔数据存储的状态管理</li>
<li>一致的服务到服务发现和调用</li>
<li>选择加入有状态模型：强/最终一致性，先写/最后写获胜</li>
<li>跨平台虚拟演员</li>
<li>从安全密钥库中检索秘密的秘密管理</li>
<li>速率限制</li>
<li>内置<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.dapr.io%2Fconcepts%2Fobservability-concept%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.dapr.io/concepts/observability-concept/" ref="nofollow noopener noreferrer">可观察性</a>支持</li>
<li>使用专用的 Operator 和 CRD 在 Kubernetes 上本地运行</li>
<li>通过 HTTP 和 gRPC 支持所有编程语言</li>
<li>来自 Azure、AWS、GCP 的多云、开放组件（绑定、发布-订阅、状态）</li>
<li>在任何地方运行，作为一个进程或容器化</li>
<li>轻量级（58MB 二进制，4MB 物理内存）</li>
<li>作为 sidecar 运行 - 无需特殊 SDK 或库</li>
<li>专用 CLI - 易于调试的开发人员友好体验</li>
<li>Java、.NET Core、Go、Javascript、Python、Rust 和 C++ 的客户端</li>
</ul>
<h1 data-id="heading-3">4. 底层服务已经支持</h1>
<p>可以到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.dapr.io%2Freference%2Fcomponents-reference%2Fsupported-bindings%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.dapr.io/reference/components-reference/supported-bindings/" ref="nofollow noopener noreferrer">这里</a>查看支持列表。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/075f96959fee4f97a9d8ceec1297efb0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前版本1.30，有微服务改造需求的童鞋，可以重点考虑该技术。</p>
<h1 data-id="heading-4">🎏 5. 小结</h1>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            