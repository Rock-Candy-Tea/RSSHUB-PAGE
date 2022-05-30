
---
title: 'Apache Pulsar 2.10.0 版本介绍'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6754'
author: 开源中国
comments: false
date: Mon, 30 May 2022 16:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6754'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p style="color:#999999; margin-left:0; margin-right:0">本文翻译自 StreamNative 博客《What’s New in Apache Pulsar 2.10》，作者为李鹏辉、Dave Duggins，原文地址为 https://streamnative.io/blog/release/2022-05-12-whats-new-in-apache-pulsar-210/。</p> 
</blockquote> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">倍受期待的 Apache Pulsar 2.10.0 版本近期已发布！新版本涵盖 99 位贡献者提供的改进和错误修复，并提交了 800 余次变更。除了之前为大家介绍的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUyMjkzMjA1Ng%3D%3D%26mid%3D2247490737%26idx%3D1%26sn%3D1551d4a31ae062909ce05ee04a6b0541%26scene%3D21%23wechat_redirect" target="_blank">减轻 ZooKeeper 依赖</a> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUyMjkzMjA1Ng%3D%3D%26mid%3D2247490861%26idx%3D1%26sn%3D3b0e15533216e6237050d2ffe37706aa%26scene%3D21%23wechat_redirect" target="_blank">自动化集群故障转移</a> 特性外，Pulsar 2.10.0 版本还包含十余项重大特性的更改。本博客为你浓缩了 Pulsar 2.10.0 版本发布亮点，一起来看看新版本还有哪些值得关注的特性吧，方便开发者和用户参考。</p> 
<h1 style="margin-left:auto; margin-right:auto; text-align:center !important">版本亮点：</h1> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・PR-13316：在主集群和备份集群之间提供自动故障恢复。（原 PIP：<span style="color:#1994fc !important">PR-13315[1]</span>）</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・PR-10279：通过向 <code>PartitionedProducer</code> 添加延迟加载功能，仅需更少的生产者即可更有效地使用 broker 内存。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・PR-12838：通过接收到的消息中的键值，使用新的 <code>TableView</code> 类型添加主题映射支持。</p> </li> 
</ul> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">本博客按项目功能更新情况分组，介绍了 2.10.0 版本最值得关注的进展，如需了解所有性能升级和 bug 修复的完整列表，请查阅 <span style="color:#1994fc !important">Pulsar 2.10.0 发布注记<span> </span>[2]</span>。</p> 
<h1 style="margin-left:auto; margin-right:auto; text-align:center !important">Bug 修复和功能增强</h1> 
<h2 style="margin-left:auto; margin-right:auto; text-align:center">客户端（仅 Java Client 支持）</h2> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-13316: 实现客户端上的 Pulsar 集群级自动故障转移。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：Pulsar 管理员必须手动对集群进行故障转移。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：添加 Pulsar 集群级别的自动故障转移功能。当检测到故障转移事件时，它会自动无缝地从主集群切换到一个或多个辅助集群；当主集群恢复时，客户端会自动切换回来。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-12517: 支持设置跨多个集群的主题策略。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：主题策略只对本地集群生效 </p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：增加支持设置可以应用给多个集群的主题策略。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 为本地主题策略设置消息的 <code>replicateTo</code> 属性以避免被复制到远程。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 留存支持设置全局参数。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 为 <code>SystemTopicBasedTopicPoliciesService</code> 添加全局主题策略。</p> </li> 
</ul> 
<h2 style="margin-left:auto; margin-right:auto; text-align:center">生产者</h2> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-10279: 为分区生产者添加延迟加载功能。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：分区数量是根据最高速率生产者设置的，最低速率生产者并不总是需要连接到每个分区，因此额外的生产者会占用 broker 内存。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：通过为分区生产者引入延迟加载，减少生产者数量以更有效地使用 broker 内存；添加轮询路由模式类来限制分区的数量。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-12403: 引入 chunk message ID。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：发送分块消息时，生产者返回最后一个分块的 message-id 会导致某些进程出现错误。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：引入了新的 <code>ChunkMessage-ID</code> 类型。为继承自 <code>MessageIdImpl</code> 的 chunk message-id 增加了两个新方法：<code>getFirstChunkMessageId</code> 和 <code>getLastChunkMessageID</code>。对于其他方法实现，直接调用 <code>lastChunkMessageID</code>，兼容现有的业务逻辑。</p> 
<h2 style="margin-left:auto; margin-right:auto; text-align:center">Broker</h2> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-12536：扩展 broker，为企业级集群的运维人员提供更多可控性和灵活性。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：企业级 Pulsar 集群运维人员需要更大的灵活性和控制力来拦截 broker 事件（包括 ledger 写入 / 读取），以进行模板验证、可观测性和访问控制。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 增强 org.apache.pulsar.broker.intercept.BrokerInterceptor 接口以包含用于跟踪的附加事件</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 创建了一个新接口 org.apache.pulsar.common.intercept.MessagePayloadProcessor，允许拦截 ledger 读写操作</p> </li> 
</ul> 
<h2 style="margin-left:auto; margin-right:auto; text-align:center">消费者</h2> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-10478：重新投递命令添加 epoch。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：在旧版本中，拉取和重新投递的操作是异步的，因此客户端消费者可能会收到一条新消息，并根据新的 messageID 执行累积 ack 且无法消费旧消息。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：Pulsar 客户端通过服务器和客户端消费者的增量 epoch 来同步重新投递和拉取消息操作。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-12269：支持 Dispatcher 中的可插入 Entry 过滤器。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：旧版本不支持原生消息标记。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：在 broker 级别实现 Entry 过滤器框架，并在后续即将发布的版本中支持命名空间和主题级别。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-13355：在向死信队列发送消息之前创建初始化订阅。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：无需命名空间的数据留存策略或死信队列订阅，未处理消息中的死信队列数据即会自动删除。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：在向死信队列发送消息之前创建初始订阅。当 <code>deadLetterProducer</code> 初始化时，消费者根据 <code>DeadLetterPolicy</code> 设置初始订阅。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-13707：为确认超时添加重新投递退避策略。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：在 <span style="color:#1994fc !important">PIP-106[3]</span> 中引入的重新投递退避策略仅适用于否定确认 API。如果使用 ack 超时而不是否定确认 API 来触发消息重新投递，则绕过退避策略。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 为确认超时添加消息重新投递策略。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 向 <code>RedeliveryBackoff</code> 添加警报 <code>NegativeAckBackoff</code> 接口。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 在 <code>ConsumerBuilder</code> 中暴露 <code>AckTimeoutRedeliveryBackoff</code>。</p> </li> 
</ul> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-13599：（目前修改仅涵盖 Java 客户端）解决设置主题级别 maxMessageSize 时产生分块消息失败的问题。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：在旧版本中，如果主题级别 maxMessageSize 设置为 [1]，则分块消息生成失败。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：在 <code>PublishContext</code> 中添加 <code>isChunked</code>。如被分块，则跳过 <code>maxMessageSize</code> 检查。</p> 
<h2 style="margin-left:auto; margin-right:auto; text-align:center">Function</h2> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-13205：Pulsar Functions 预加载和释放外部资源。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：外部资源初始化和释放或手动完成，或通过使用复杂的初始化逻辑完成。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：引入 <code>RichFunction</code> 接口，通过提供 setup 和 tearDown API 来扩展 <code>Function</code>。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-12104：更新身份验证接口来包含异步身份验证方法。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：Pulsar 当前的 AuthenticationProvider 接口只暴露了用于验证连接的同步方法。在没有任何依赖网络调用的提供商的情况下，目前功能虽足够使用，但是在某些情况下查看 OAuth2.0 规范时，需要网络调用来验证 token。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">AuthenticationProvider</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 添加 <code>AuthenticationProvider#authenticateAsync</code>。引入一个调用认证方法的默认实现。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 弃用 <code>AuthenticationProvider#authenticate</code>。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 添加 <code>AuthenticationProvider#authenticateHttpRequestAsync</code>。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 弃用 <code>AuthenticationProvider#authenticateHttpRequest</code>。</p> </li> 
</ul> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">AuthenticationState</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 添加 <code>AuthenticationState#authenticateAsync</code>。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 弃用 <code>AuthenticationState#authenticate</code><span> </span>并推荐使用 <code>AuthenticationState#authenticateAsync</code><span> </span>方法。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 弃用 <code>AuthenticationState#isComplete</code>。可以通过从 <code>AuthenticationState#authenticateAsync</code> 的结果推断身份验证完整性来避免此方法。</p> </li> 
</ul> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">AuthenticationDataSource</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 弃用 <code>AuthenticationDataSource#authenticate</code>。不需要此方法的异步版本。</p> </li> 
</ul> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-12838：初始化 TableView 提交。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：在许多场景中，应用程序使用 Pulsar 消费者或 reader 从主题中获取所有更新，并使用接收到消息的每个键的最新值构造一个映射。这个操作在构建数据的本地缓存时很常见。社区不提供对 Pulsar 客户端 API 中未包含此访问模式的支持。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：添加新的 <code>TableView</code> 类型并更新 Pulsar Client。</p> 
<h2 style="margin-left:auto; margin-right:auto; text-align:center">主题</h2> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-12818：支持主题元数据（第一部分）—— 创建具有属性的主题。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：无法存储主题元数据。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 在 topics.java 中添加新的存储方法。</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 添加两个新的 REST API 路径以减少兼容性问题。</p> </li> 
</ul> 
<h2 style="margin-left:auto; margin-right:auto; text-align:center">元数据存储</h2> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">PR-13225：添加了 Etcd MetadataStore 实现。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">问题：社区正在努力添加支持非 ZooKeeper 实现的元数据后端。</p> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">解决方案：添加对以下的 Etcd 支持：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 批处理读 / 写请求</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">・ 会话监视点</p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0">• Lease manager</p> </li> 
</ul>
                                        </div>
                                      
</div>
            