
---
title: '一款成熟的RPC框架应该具有的基本素养'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/007d676e59d54f898c5025fef52e6899~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 00:40:29 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/007d676e59d54f898c5025fef52e6899~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第3篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<h3 data-id="heading-0">编者按</h3>
<p>本篇技术的分享是微服务技术碎碎念的开篇，为什么取名碎碎念呢，因为这个专栏的内容都是作者本人在工作以及学习中关于一些常用微服务技术的整理，非官方，不正式，纯粹的自我认知以及理解，难免有疏漏或者不对的地方，不喜勿喷。</p>
<h3 data-id="heading-1">RPC框架简介</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/007d676e59d54f898c5025fef52e6899~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>什么是RPC框架，用一个比较专业的语句来概括就是一种跨进程的服务调用方式,在提供远程调用能力的同时不损失本地调用语义的简洁性。</p>
<p>RPC框架的的工作机制本质上都是相似的，大体上分为数据的序列化以及反序列化、服务接口、服务具体的实现、服务消费方、服务提供方以及服务之间网络通信这几个方面，并且根据不同的角色(服务消费者、服务提供者)实现的功能也不一致。</p>
<p>接下来，我们重点分析一下RPC框架服务提供方以及服务消费方在实现的时候应该重点考虑的功能并且站在RPC框架整体的角度考虑一下框架应该支持的高级特性。</p>
<h3 data-id="heading-2">服务提供方重点功能解析</h3>
<p>服务提供方也就是对外提供服务者，对内实现接口功能，对外暴露接口，供消费方来进行调用以完成业务功能。</p>
<p>站在RPC框架实现者的角度，考虑应该为服务提供方提供怎样的功能支持。</p>
<h4 data-id="heading-3">队列/线程池</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc57210ad2df4434a708ac7f9031dcd6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当消费者的请求过来后，IO线程对请求进行相应的编解码后，需要将请求进行封装，并放入到业务队列中，IO线程不进行业务的处理，仅仅做IO线程相关的事情，避免阻塞影响后后续的请求。</p>
<p>业务线程池从队列中获取请求数据进行业务逻辑的处理，处理完成后的响应数据由IO线程写回客户端。</p>
<p>关于队列以及线程池的关系，还需要重点考虑队列与线程的匹配关系。是单一队列多线程还是多队列多线程，需要具体问题具体分析。单一队列多线程模式有资源竞争性能的开销。多队列多线程模式在资源竞争这方面导致性能的开销小，但是不一定效率就高，需要进行压力测试观察情况。</p>
<p>在设计时，一方面需要考虑根据业务的重要程度，队列是否需要划分优先级，队列资源的隔离，另一方面也需要考虑进行线程资源的隔离，多线程池处理不同的业务请求。</p>
<h4 data-id="heading-4">超时丢弃</h4>
<p>超时的请求不再进行处理，快速的失败，缓解请求队列的堆积。</p>
<p>进入队列的请求数据要设置入队的时间节点，在出队的时候需要对设置的时间节点进行判断，超时之后就不再进行处理了。</p>
<h4 data-id="heading-5">过载保护</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ffb46785f014ef3bb321139e146df24~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>服务提供方主动放弃超过自己处理能力之外的请求，对自身的服务进行保护。</p>
<p>通知设置请求队列的长度，将超过队列长度之外的请求丢弃，不再进行处理。但是这种情况会造成请求的丢失，需要进行告警的通知并进行记录，事后进行追偿。</p>
<h4 data-id="heading-6">优雅关闭</h4>
<p>直接kill -9 暴力的关闭系统会影响正在处理的业务,可能会造成错误数据,非常影响用户体验。</p>
<p>服务端的优雅关闭指的是服务方在进行关闭之前将未处理完的请求数据处理完成，并通知业务消费方本服务即将关闭，不要继续向本服务发起请求。后续业务消费方不再向本服务发起请求，本服务请求流量逐渐下降为 0,即可关闭本服务。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d37156e77b2461c9a9fa1376cd594ac~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfcb8ce585164cdaa9f0068127579c1f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在服务即将关闭时如何通知服务消费方是一个需要解决的问题，一般有两种解决方案，一个是返回的数据带有关闭的协议，属于服务消费方被动的带回，一个是服务提供方主动的通知服务消费者，属于主动试的通知，这两种方案各有各的优劣，可以视情况而定。</p>
<h3 data-id="heading-7">服务消费方重点功能解析</h3>
<h4 data-id="heading-8">连接管理</h4>
<p>服务消费方维护者与其相关的服务提供方一系列的网络连接，需要对这些连接进行管理，以保障系统交互的稳定性。</p>
<p><strong>连接初始化的时机</strong>。一般情况下，连接初始化的时机分为两种情况，一种是在模块初始化时就进行连接的初始化，另一种是在第一次调用时进行连接的初始化，第一种情况适用于业务模块下游节点不多的情况下进行，第二种情况适用于下游节点众多，不然服务启动将会耗费很长时间，网关模块就比较适合第二种情况。</p>
<p><strong>连接数</strong> RPC框架所涉及的连接大部分都是长连接，一般一个地址维护一条连接就行，连接是全双工通道，双方均可发送数据。</p>
<p><strong>连接模式</strong> 服务之间的连接模式可以大体分为两种，一种是独占式的一种是共享式的，一般RPC框架的连接模式是共享式的，服务单元之间交互共享一个连接，而数据库连接则是独占式的，一个请求用完之后别的请求才能使用。</p>
<p><strong>心跳/重连</strong> 心跳是为了维护服务消费方与服务提供方建立的连接，保持连接不会中断。重连是在连接断开时，主动重新建立与服务提供方的连接，连接的断开一般是异常的中断或者是对方进行了优雅的关闭。</p>
<h4 data-id="heading-9">负载均衡</h4>
<p>负载均衡模块能够根据选择的负载策略让下游的多个服务提供方节点流量合理，同时也能够应对下游服务节点扩容缩容等情况的发生。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aab2c8a323d4cb4afee63d2bb64a01d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一般的负载策略包括轮询、随机、取模、一致性hash、权重。一般选用负载策略时，建议选用轮询加上权重的策略来实现，这样能够更好的维护服务的稳定性。</p>
<p>权重的取值范围可以设定为0-10，值越大权重越高，权重越高分配的流量比例就越大。</p>
<p>采用轮询加权重的策略来实现负载均衡的实现思路是先轮询到一个下游节点，然后进行权重的计算过滤，若符合则进行调用，不符合则轮询下一个节点继续进行计算。</p>
<h4 data-id="heading-10">请求路由</h4>
<p>请求路由易于负载均衡弄混淆，其实这两个功能点涉及不同的方面，一般情况是先进行请求的路由，根据一系列规则过滤出服务提供方节点列表，然后在进行负载均衡。</p>
<p>一般请求路由可以用于应用的隔离、灰度发布、读写分离等场景。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4859a65f902b4c8ea9a2f7aa5a4b9804~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体的实现方式就是定义规则实例，然后用链表的方式串接起来，最终得出要负载的服务提供方节点列表，然后由负载均衡模块进行服务的调用。</p>
<h4 data-id="heading-11">超时处理</h4>
<p>除了服务提供方要进行超时处理之外，服务消费方也需要进行超时的处理。</p>
<p>对于长时间没有返回的请求，需要做出异常的处理，及时的释放资源，避免影响其他服务的调用。</p>
<h3 data-id="heading-12">框架高级功能设计</h3>
<h4 data-id="heading-13">服务熔断</h4>
<p>服务熔断指的是服务调用出现不可用或者超时,为了防止整个系统出现雪崩,暂停对该服务的调用。</p>
<p>服务熔断的具体实现采用了一种叫做断路器的设计方式，断路器一方面能够及时的短路，另一方面也能够进行检测恢复。</p>
<p>断路器一般有三种状态，一种是关闭状态，指的是执行成功次数超过预设值，服务正常。一种是打开，指的是周期内失败次数超过阈值或者定期尝试执行，成功次数未超过预设值。一种是半开，指的是定时器到期，尝试半开。</p>
<p>关于断路器更加详细的分析可以参考其他的资料。</p>
<h4 data-id="heading-14">服务降级</h4>
<p>服务降级总体概念就是对业务降级,跳过异常调用，返回关键数据，确保服务可用。</p>
<p>一般情况下就是调用出现异常时，根据不同的服务场景，可以返回一些预定义的数据，保障服务的可用性。</p>
<h4 data-id="heading-15">动态权重</h4>
<p>动态权重指的是可以动态的调整服务节点的权重比例，用来控制服务节点流量比例。
一方面可以用于为刚启动的节点分配较低权重,然后逐步升高。另一方面可以及时管控存在问题的节点。</p>
<h4 data-id="heading-16">限流</h4>
<p>通过对调用流量的限制，实现对服务提供方的保护。限流可以是服务模块内部主动触发限流，也可以是人工触发限流。</p>
<p>在扩展一点就是可以动态的统计流量情况，然后上报到服务管理平台，及时的告警通知。</p>
<p>在设计时，是不是也可以做到本服务节点主动通知服务调用方减少对本节点的调用，自动的实现一种自我保护策略。</p>
<h3 data-id="heading-17">结尾总结</h3>
<p>其实要想设计好一款能够应用于生产环境的RPC框架还是比较复杂的，需要考虑的要素还是挺多的，不过市面上开源了一些优秀的RPC框架，也就避免了大家重复的造轮子，可以拿来即用，如果要自研RPC框架的话，需要结合自己公司的情况，具体问题具体分析吧。</p></div>  
</div>
            