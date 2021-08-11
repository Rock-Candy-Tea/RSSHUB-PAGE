
---
title: 'dubbo 浅入浅出'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9a15c810265480195f952f2ae18923f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 16:36:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9a15c810265480195f952f2ae18923f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">1. Dubbo是什么？</h2>
<p>Dubbo是一个分布式服务框架，致力于提供高性能和透明化的RPC远程服务调用方案，以及SOA服务治理方案。简单的说，dubbo就是个服务框架，如果没有分布式的需求，其实是不需要用的，只有在分布式的时候，才有dubbo这样的分布式服务框架的需求，并且本质上是个服务调用的东东，说白了就是个远程服务调用的分布式框架（告别Web Service模式中的WSdl，以服务者与消费者的方式在dubbo上注册）
其核心部分包含:</p>
<ol>
<li>远程通讯: 提供对多种基于长连接的NIO框架抽象封装，包括多种线程模型，序列化，以及“请求-响应”模式的信息交换方式。</li>
<li>集群容错: 提供基于接口方法的透明远程过程调用，包括多协议支持，以及软负载均衡，失败容错，地址路由，动态配置等集群支持。</li>
<li>自动发现: 基于注册中心目录服务，使服务消费方能动态的查找服务提供方，使地址透明，使服务提供方可以平滑增加或减少机器。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9a15c810265480195f952f2ae18923f~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">Dubbo 分层</h2>
<p>Dubbo 是一款高性能 Java RPC 架构。它实现了面向接口代理的 RPC 调用，服务注册和发现，负载均衡，容错，扩展性等等功能。</p>
<p>Dubbo 大致上分为三层，分别是：</p>
<ul>
<li><strong>业务层</strong></li>
<li><strong>RPC 层</strong></li>
<li><strong>Remoting 层</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ddd34eac9b246e9b22589c56f3b2b3f~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Dubbo的主要应用场景</h2>
<p>透明化的远程方法调用，就像调用本地方法一样调用远程方法，只需简单配置，没有任何API侵入。</p>
<p>软负载均衡及容错机制，可在内网替代F5等硬件负载均衡器，降低成本，减少单点。（F5负载均衡器我也是百度来的）。</p>
<p>服务自动注册与发现，不再需要写死服务提供方地址，注册中心基于接口名查询服务提供者的IP地址，并且能够平滑添加或删除服务提供者。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c13e3ff237c2452dbcf2a2d431f8c1fb~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">Dubbo 调用工作流</h2>
<p>Dubbo 框架是用来处理分布式系统中，服务发现与注册以及调用问题的，并且管理调用过程。</p>
<p>工作流涉及到服务提供者（Provider），注册中心（Registration），网络（Network）和服务消费者（Consumer）：</p>
<ul>
<li>
<p>服务提供者在启动的时候，会通过读取一些配置将服务实例化。</p>
</li>
<li>
<p>Proxy 封装服务调用接口，方便调用者调用。客户端获取 Proxy 时，可以像调用本地服务一样，调用远程服务。</p>
</li>
<li>
<p>Proxy 在封装时，需要调用 Protocol 定义协议格式，例如：Dubbo Protocol。</p>
</li>
<li>
<p>将 Proxy 封装成 Invoker，它是真实服务调用的实例。</p>
</li>
<li>
<p>将 Invoker 转化成 Exporter，Exporter 只是把 Invoker 包装了一层，是为了在注册中心中暴露自己，方便消费者使用。</p>
</li>
<li>
<p>将包装好的 Exporter 注册到注册中心。</p>
</li>
<li>
<p>服务消费者建立好实例，会到服务注册中心订阅服务提供者的元数据。元数据包括服务 IP 和端口以及调用方式（Proxy）。</p>
</li>
<li>
<p>消费者会通过获取的 Proxy 进行调用。通过服务提供方包装过程可以知道，Proxy 实际包装了 Invoker 实体，因此需要使用 Invoker 进行调用。</p>
</li>
<li>
<p>在 Invoker 调用之前，通过 Directory 获取服务提供者的 Invoker 列表。在分布式的服务中有可能出现同一个服务，分布在不同的节点上。</p>
</li>
<li>
<p>通过路由规则了解，服务需要从哪些节点获取。</p>
</li>
<li>
<p>Invoker 调用过程中，通过 Cluster 进行容错，如果遇到失败策略进行重试。</p>
</li>
<li>
<p>调用中，由于多个服务可能会分布到不同的节点，就要通过 LoadBalance 来实现负载均衡。</p>
</li>
<li>
<p>Invoker 调用之前还需要经过 Filter，它是一个过滤链，用来处理上下文，限流和计数的工作。</p>
</li>
<li>
<p>生成过滤以后的 Invoker。</p>
</li>
<li>
<p>用 Client 进行数据传输。</p>
</li>
<li>
<p>Codec 会根据 Protocol 定义的协议，进行协议的构造。</p>
</li>
<li>
<p>构造完成的数据，通过序列化 Serialization 传输给服务提供者。</p>
</li>
<li>
<p>Request 已经到达了服务提供者，它会被分配到线程池（ThreadPool）中进行处理。</p>
</li>
<li>
<p>Server 拿到请求以后查找对应的 Exporter（包含有 Invoker）。</p>
</li>
<li>
<p>由于 Export 也会被 Filter 层层包裹</p>
</li>
<li>
<p>通过 Filter 以后获得 Invoker</p>
</li>
<li>
<p>最后，对服务提供者实体进行调用。</p>
</li>
</ul>
<p>上面调用步骤经历了这么多过程，其中出现了 Proxy，Invoker，Exporter，Filter。</p>
<p>实际上都是调用实体在不同阶段的不同表现形式，本质是一样的，在不同的使用场景使用不同的实体。</p>
<p>例如 Proxy 是用来方便调用者调用的。Invoker 是在调用具体实体时使用的。Exporter 用来注册到注册中心的等等。</p></div>  
</div>
            