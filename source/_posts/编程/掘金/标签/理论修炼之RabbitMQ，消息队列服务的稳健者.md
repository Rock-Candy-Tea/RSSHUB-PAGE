
---
title: '理论修炼之RabbitMQ，消息队列服务的稳健者'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71f13f9933824c61974a397b132c470e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 06:44:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71f13f9933824c61974a397b132c470e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>在ETCD节有讲过，对于架构师来说，对中间件的理论研究和熟悉不是过分的要求，以前大意了，主要偏向应用层了，今天就来学习RabbitMQ，这个消息队列服务的稳健者。</p>
<p>当然由于RabbitMQ内容比较丰富，因此这里先阐述下消息组件的几种模式，然后注重于连接管理。其他章节后续也许会进一步学习，有所得必和大家分享。</p>
<h1 data-id="heading-1">🎏 01. RabbitMQ支持的几种队列模式</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71f13f9933824c61974a397b132c470e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
还是这个图精简，一下子就看完了6种模式。</p>
<h1 data-id="heading-2">🎏 01.1 简单队列模式</h1>
<p>1个生产者，1个消费者。这种模式下消费者是按照消息的生产顺序严格进行消费的，可以看作是严格顺序消息队列。</p>
<h1 data-id="heading-3">🎏 01.2 工作队列</h1>
<p>1个生产者，多个消费者，消费者按照次序逐次把消息排放到各个消费者。因此默认情况下，消费的调度并不是按照工作量来的，而是按照顺序公平调度来的。</p>
<p>幸运的是RabbitMQ提供了参数，可以修改使用带有prefetch_count=1设置的Channel#basic_qos方法 。这使用basic.qos协议方法告诉 RabbitMQ 一次不要给一个工人多个消息。或者，换句话说，在处理并确认前一条消息之前，不要向工作人员发送新消息。相反，它会将它分派给下一个不忙的工人。</p>
<pre><code class="hljs language-shell copyable" lang="shell">channel.basic_qos(prefetch_count= 1 )
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">🎏 01.3 发布、订阅模式</h1>
<p>也是1个生产者，多个消费者，不过与上面方案不同的是每一个消费者都有自己的一个队列。</p>
<p>生产者将消息直发送到交换机，每个队列都要绑定到交换机。有几种可用的交换类型：<strong>direct</strong>、<strong>topic</strong>、<strong>headers</strong> <strong>和fanout</strong>。我们将关注最后一个——它就是广播(fanout)</p>
<p>因此无论交换机绑定多少队列，交换机总会保证消息被广播给每一个队列。</p>
<h1 data-id="heading-5">🎏 01.4 路由模式</h1>
<p>仍然是多个消费者，生产者嘛，就不一定了。 这里生产者把消息发送到 direct类型的交换机上。该交换机按照绑定的Key路由消息到固定的队列。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d429a9cd03bf4d3daf35afc72ed0e4f1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">🎏 01.5 主题模式</h1>
<p>主题模式相比路由模式，其更灵活，按照订阅的主题建立相关队列，交换机按照主题路由消息到各个队列。</p>
<p>这里一条消息如果负责多个队列的规则，则消息被路由分发到多个队列。当然如果多个规则都匹配一条消息，在一个队列内这条消息也仅被路由1次。</p>
<p>主题可以支持通配符*和#。</p>
<h1 data-id="heading-7">🎏 01.6 RPC模式</h1>
<p>大家都知道RPC是远程过程调用，其可以返回调用后执行的结果值，因此通过RPC模式，可以利用RabbitMQ构建一个基于RPC通讯的分布式微服务系统。</p>
<h1 data-id="heading-8">🎏 02 客户端连接</h1>
<p>这里的连接介绍基于.net client sdk，当然java的客户端也是类似。但其他客户端sdk可能会不太一样，因此谨慎参考。</p>
<p>RabbitMQ 支持的所有协议都是基于 TCP 的，并维持长连接（每个协议操作不打开新连接）以提高效率。</p>
<p>当不再需要连接时，应用程序必须关闭它们以节省资源。否则可能出现连接泄露问题，有最终耗尽其目标资源节点的风险。</p>
<p>如果我们使用rabbitmq的监控面板，请注意:RabbitMQ 记录所有发送至少 1 字节数据的入站客户端连接。不会记录在没有任何活动的情况下打开的连接。</p>
<p>利用监控面板，可以轻松监控连接的泄露情况。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21995d04aa934ea48a936ad0074d171e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然如果频繁打开关闭连接，对系统的性能也会造成影响，我们也可以监控是否频繁打开关闭连接。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9c3003d4f024dfc815a5e6d2e702216~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发布消息的连接可能速度很快，但读和处理消息可能很慢，导致速度不匹配。这时，会自动触发背压式流，这时候读消息不受影响，但写受到流控控制，导致速度放慢。</p>
<p>.net client 和 java client的sdk均支持连接故障自动恢复，因此编程者几乎不用做太多工作。</p>
<p>虽然标准的sdk提供了连接池管理，但并非最优。而 spring 框架提供了丰富的连接池二次封装，其可以管理单链接多通道或多连接多通道模式的连接池，也提供了发布确认等相关封装。</p>
<p>作为.net 开发者，我们只有羡慕的份了，当然仿照其写个.net版的也应该可以，不过这个能力要求有点高，我试试写一个看看。</p>
<h1 data-id="heading-9">🎏 03 强一致性方案</h1>
<p>为了保证消息中间件的强一致性，RabbitMQ提供了集群镜像功能，交换机和队列持久化，以及发布和订阅消息的确认（ack）机制，因此我们如果需要强一致性，那么避免不了和这些技术打打交道。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4740259fcc494e428b76d9230f36171a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过发送消息、推送消息的确认ack方案，虚线表示，的确提升了消息投递、消费的准确性。</p>
<p>并且确认ack均支持异步批量方案，因此数据的读写吞吐量不用担心受到影响。</p>
<p>生产者在采用批量ack时，可以适当开启缓存，缓存待确认的消息，可以完美解决ack确认问题。</p>
<h1 data-id="heading-10">🎏 04. 小结</h1>
<p>RabbitMQ的内容非常多，这里仅仅介绍了一些很小的要点，后续有时间仍需要继续学习！</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            