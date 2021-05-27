
---
title: '5、深潜KafkaProducer——Sender线程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c94db9b56a540a5a2cabee05341974f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 19:29:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c94db9b56a540a5a2cabee05341974f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>通过上一课时的介绍我们了解到，业务线程通过 KafkaProducer.send() 方法将 message 放入 RecordAccumulator 中进行能缓冲，并没有进行实际的网络 I/O 操作，真正的网络 I/O 操作是由 Sender 线程完成。</p>
<p>首先我们回到 KafkaProducer 的构造方法中，我们可以看到：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 创建Sender对象，Sender实现了Runnable接口</span>
<span class="hljs-keyword">this</span>.sender = newSender(logContext, kafkaClient, <span class="hljs-keyword">this</span>.metadata);
<span class="hljs-comment">// 创建IO线程并启动，由该线程来执行Sender.run()方法中逻辑</span>
<span class="hljs-keyword">this</span>.ioThread = <span class="hljs-keyword">new</span> KafkaThread(ioThreadName, <span class="hljs-keyword">this</span>.sender, <span class="hljs-keyword">true</span>);
<span class="hljs-keyword">this</span>.ioThread.start();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">runOnce() 方法</h2>
<p>既然 Sender 是一个 Runnable 对象，那整个 Sender 线程执行的核心逻辑就在 run() 方法中，run() 方法中的第一段代码就是循环调用 runOnce() 方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">while</span> (running) &#123; <span class="hljs-comment">// running字段用来标识当前Sender线程是否正常执行</span>
    <span class="hljs-keyword">try</span> &#123;
        runOnce(); 
    &#125; <span class="hljs-keyword">catch</span> (Exception e) &#123;
        log.error(<span class="hljs-string">"Uncaught error in kafka producer I/O thread: "</span>, e);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 runOnce() 方法是 Sender 线程一个执行的周期，在这个周期中会进行一次批量的请求发送，也会进行一次响应的处理，核心实现如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">runOnce</span><span class="hljs-params">()</span> </span>&#123;
    ... <span class="hljs-comment">// 省略事务消息相关的处理逻辑</span>
    <span class="hljs-keyword">long</span> currentTimeMs = time.milliseconds();
    <span class="hljs-comment">// 创建发送到kafka集群的请求</span>
    <span class="hljs-keyword">long</span> pollTimeout = sendProducerData(currentTimeMs);
    <span class="hljs-comment">// 真正执行网络IO的地方，会将上面的请求发送出去，同时处理收到的响应</span>
    client.poll(pollTimeout, currentTimeMs);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在开始深入分析 runOnce() 方法之前，我们先来说明一下其中涉及的基础组件以及它们之间是如何协同工作的，如下图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c94db9b56a540a5a2cabee05341974f~tplv-k3u1fbpfcp-watermark.image" alt="2、Sender基础组建.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">sendProducerData() 方法</h2>
<p>Sender.sendProducerData() 方法是 Sender 线程创建请求的核心，其大致流程是这样的：</p>
<ol>
<li>Sender 线程首先查询 RecordAccumulator 中数据的缓冲情况，知晓目前可以向哪些 topic-partition 发送 message。</li>
<li>之后，Sender 线程会通过 NetworkClient 获取当前客户端与各个 Node 节点的连接情况，进一步过滤为哪些 Node 创建请求。</li>
<li>然后，生成相应的 ClientRequest 请求。</li>
<li>最后调用 NetWorkClient.send() 方法将 ClientRequest 请求写入到 NetworkClient，后续由 NetworkClient 进行网络 IO。</li>
</ol>
<p>上面描述的只是一个粗略的请求发送过程，我们下面就深入到具体的实现中进行详细分析，首先来看 sendProducerData() 方法，下面是其详细的流程图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff1cba84a7bd435091955a8c0a783e76~tplv-k3u1fbpfcp-watermark.image" alt="1、Sender流程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1</strong>、请求 ProducerMetadata 获取 Cluster，也就是拿到 Kafka 集群的元数据。</p>
<p><strong>2</strong>、然后调用上一课时介绍的 RecordAccumulator.ready() 方法，了解 RecordAccumulator 的缓存情况，选出可以向哪些Node 节点发送请求。</p>
<p><strong>3</strong>、在步骤 2 中返回的 ReadyCheckResult 中，如果 unknownLeadersExist 不为空，表示待发送 message 中存在未知 topic 或 leader，则调用 Metadata.requestUpdate方法更新 needFullUpdate 标记，表示需要更新 Kafka 集群的元数据。（只是打个标记，不会阻塞进行更新元数据的操作）</p>
<p><strong>4</strong>、接下来处理 ReadyCheckResult 返回值中的 readyNodes 集合，主要操作是循环调用 NetworkClient.ready() 方法，确定能否向 Node 发送请求：</p>
<ul>
<li>检查当前 KafkaProducer 是否与目标 Node 建立了网络连接，如果没有建立，则尝试初始化网络连接，如果初始化失败，则直接返回 false，表示此时不适合向该 Node 发送请求。</li>
<li>其次就是检查当前已发送但未响应的请求是否已经达到上限，要是有很多这种请求存在，可能是 broker 宕机了或是 broker 处理能力不足，此时也不适合继续发送请求。</li>
<li>除了进行网络方面的检查之外，还会检查 kafka 元数据是否需要更新，如果需要更新的话，也不能发送请求。毕竟使用过期的或是错误的元数据来发送数据，请求也不会发送成功。</li>
</ul>
<p><strong>5</strong>、经过上述过滤，不适合发送请求的 Node 节点会从 readyNodes 集合中删除。</p>
<p><strong>6</strong>、调用 RecordAccumulator.drain() 方法，获取待发送的 message 集合，拿到的是个 <code>Map<Integer, List<ProducerBatch>></code> 集合，其中的 Key 是目标的 NodeId，Value 是发往目标 Node 的 ProducerBatch 集合。</p>
<p><strong>7</strong>、调用 addToInflightBatches() 方法将步骤 6 中待发送的 ProducerBatch 发送记录到 inFlightBatches 集合中，这个集合中记录了已发送但是未响应的 ProducerBatch。</p>
<p><strong>8</strong>、这里有个小细节，这里会检查 guaranteeMessageOrder 字段，它与 <code>max.in.flight.requests.per.connection</code> 配置相关。从名字就可以看出，<code>max.in.flight.requests.per.connection</code> 是用来控制每个网络连接用来 inflight （发送但未响应）的请求个数。如果该配置设置为 1 的话，就会实现 KafkaProducer 逐个发送请求的效果，此时的 guaranteeMessageOrder 就为 true，此时，Sender 线程发送完一个请求之后，就会将目标 partition 加入到 RecordAccumulator.muted 集合中，之后再调用 ready() 方法以及 drain() 方法的时候，都会忽略发往 muted 集合 partition 的数据。当请求返回的时候，KafkaProducer 会将相关 partition 从 muted 集合中删除，也就可以继续向目标 partition 发送数据了。</p>
<p><strong>9</strong>、接下来分别调用 getExpiredInflightBatches() 方法和 expiredBatches() 方法，其中：</p>
<ul>
<li>
<p>getExpiredInflightBatches() 方法获取 inFlightBatches 集合中已经过期的 ProducerBatch 集合。</p>
</li>
<li>
<p>expiredBatches() 方法用来获取 RecordAccumulator 中已经过期的 ProducerBatch 集合。</p>
<p>这两个方法在发现过期 ProducerBatch 对象的时候，直接将这些过期的 ProducerBatch 对象从  RecordAccumulator 中删除（inFlightBatches 中的不删除），并记录到返回的结果集中。如果碰到未过期的 ProducerBatch 时，则调用 maybeUpdateNextBatchExpiryTime() 方法更新 RecordAccumulator.nextBatchExpiryTimeMs 字段，该字段记录了最近过期的 ProducerBatch 过期时间戳。</p>
<p>最后需要说明的是，这里的过期时长是 <code>delivery.timeout.ms</code> 配置项指定的，它表示的是调用 KafkaProducer.send() 方法之后的过期时长，它应该大于等于 <code>request.timeout.ms</code> 和 <code>ling.ms</code> 两配置之和。 <code>request.timeout.ms</code> 是 NetworkClient 等待响应的最大时长，后面会说。 <code>ling.ms</code> 是 message 在 KafkaProducer 缓存的最大时长。</p>
</li>
</ul>
<p><strong>10</strong>、拿到步骤 9 返回的超时 ProducerBatch 集合之后，Sender 线程会循环调用 failBatch() 方法来处理这些超时的 ProducerBatch 对象。failBatch() 方法中会调用 ProducerBatch.done() 方法来完成 ProducerBatch（即更新 ProducerBatch 的状态并触发其中所有 Record 的Callback）。</p>
<ul>
<li>如果 done() 返回 true（即当前线程是第一个修改该 ProducerBatch 的 finalState），且 ProducerBatch 是  inFlightBatches 集合中的 ProducerBatch，则会在这里尝试删除。之所以这样是因为可能会并发收到响应，出现并发从 inFlightBatches 删除数据的情况。</li>
</ul>
<p><strong>11</strong>、接下来计算 pollTimeout，该时长是最近一个 ProducerBatch 的过期时长，也是后面 NetworkClient.poll() 方法的最长等待时间，因为有 ProducerBatch 过期的时候，需要 Sender 线程来执行步骤 10 进行处理，所以 Sender 线程不能长时间阻塞在 poll() 方法上。NetworkClient 的实现后面详细介绍。</p>
<p><strong>12</strong>、调用 Sender.sendProduceRequests() 方法将每组 ProducerBatch（按照目标 Node 进行分组）封装成相应的 ClientRequest 请求（通过 NetworkClient.newClientRequest() 方法创建，通知注册处理响应的回调）。</p>
<p><strong>13</strong>、最后调用 NetworkClient.send() 方法发送 ClientRequest 请求。</p>
<p>到此为止，整个 sendProducerData() 方法的内容就介绍完了，其中包含了很多细节和配置，再高度概括一下：</p>
<ul>
<li>步骤 1~8 是通过 kafka 集群元数据、当前 KafkaProducer 网络状态、KafkaProducer 配置等信息，来确定当前待发送的 ProducerBatch 集合。</li>
<li>步骤 9~10 是处理 inFlightBatches、RecordAccumulator 中过期的 ProducerBatch 对象，触发过期 Record 的 Callback。</li>
<li>步骤 11~13 是将待发送 ProducerBatch 集合封装成 ClientRequest 并交给 NetworkClient 发送。</li>
</ul>
<p>也不是很复杂，对吧，希望胖友们好好梳理。</p>
<h2 data-id="heading-2">ClientRequest</h2>
<p>在 Sender.sendProducerData() 方法的最后，会将待发送的 ProducerBatch 封装成 ClientRequest 请求发送发送出去，ProducerBatch 集合怎么转换成 ClientRequest 请求呢？ClientRequest 请求又是什么格式呢？下面我们就来介绍一下这些问题。</p>
<p>我们首先来到 Sender.sendProduceRequests() 方法中，其中会循环调用 sendProduceRequest() 方法处理发往每个 Node 的 ProducerBatch 集合。在 sendProduceRequest() 方法中：</p>
<ul>
<li>
<p>按照 TopicPartition 维度对传入的 ProducerBatch 进行分类，得到 Map<TopicPartition, ProducerBatch> 集合（recordsByPartition 变量），这个集合是在收到响应的时候用的。在构造这个 recordsByPartition 集合的时候，会同时构造一个 ProduceRequestData.TopicProduceDataCollection 对，其中也是按照 topic->partition->MemoryRecords 的格式组织数据的。</p>
<p>这里的 MemoryRecords 是 MemoryRecordsBuilder.build() 方法中创建出来的，两者底层复用同一个 ByteBuffer。build() 方法中，MemoryRecordsBuilder 除了关闭 appendStream 这个写入流，还会将 RecordBatch 的 Header 写入到底层 ByteBuffer 头部（参考上一课时 kafka message 的格式），同时还会更新 ByteBuffer 的指针，切换成读模式。这里逻辑具体实现在 MemoryRecordsBuilder.close() 方法中。</p>
</li>
<li>
<p>接下来创建 ProduceRequest.Builder 对象，它用来创建 ProduceRequest 请求，ProduceRequest 请求才是真正发送到 broker 的请求，其具体格式如下：</p>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/772ca95066d048138a45d0fea0441172~tplv-k3u1fbpfcp-watermark.image" alt="3、ProduceRequest结构.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Request Header 中各个字段的含义如下，这个 Request Header 也是整个 <a href="https://xxxlxy2008.github.io/kafka/5%E3%80%81%E6%B7%B1%E6%BD%9Ckafka-producer3/#more" target="_blank" rel="nofollow noopener noreferrer">Kafka Protocol</a> 中所有请求的通用请求头：</p>






























<table><thead><tr><th align="center">api_key</th><th align="center">short</th><th>API标识</th></tr></thead><tbody><tr><td align="center">request_api_key</td><td align="center">short</td><td>API标识</td></tr><tr><td align="center">request_api_version</td><td align="center">short</td><td>API版本号</td></tr><tr><td align="center">correlation_id</td><td align="center">int</td><td>序号，由客户端产生的、单调递增的，服务端不做任何修改，在Response中会回传给客户端</td></tr><tr><td align="center">client_id</td><td align="center">String</td><td>客户端ID，可为null</td></tr></tbody></table>
<p>Produce Request 中的各个字段含义如下：</p>


















































<table><thead><tr><th align="center">字段名称</th><th align="center">类型</th><th>字段含义</th></tr></thead><tbody><tr><td align="center">transactional_id</td><td align="center">String</td><td>事务标识，如果不是事务消息的话，该字段为 null</td></tr><tr><td align="center">acks</td><td align="center">short</td><td>服务端响应此请求之前，需要有多少Replica成功复制了此请求的消息。可选值有：<br>0 表示 KafkaProducer 不关心请求响应，<br>1 表示返回响应时至少 leader replica 存储了该消息  <br>-1 表示整个ISR都完成了复制</td></tr><tr><td align="center">timeout_ms</td><td align="center">int</td><td>等待响应的最长时间</td></tr><tr><td align="center">topic_data</td><td align="center"></td><td>发往每个 topic 的数据</td></tr><tr><td align="center">name</td><td align="center">String</td><td>topic 名称</td></tr><tr><td align="center">partition_data</td><td align="center"></td><td>发往每个 partition 的数据</td></tr><tr><td align="center">index</td><td align="center">int</td><td>partition 编号</td></tr><tr><td align="center">records</td><td align="center"></td><td>Record 集合</td></tr></tbody></table>
<p>kafka protocol 的其他请求，可以参考这个<a href="https://xxxlxy2008.github.io/kafka/5%E3%80%81%E6%B7%B1%E6%BD%9Ckafka-producer3/#more" target="_blank" rel="nofollow noopener noreferrer">文档</a>，目前已经 Version 9 了。</p>
<ul>
<li>最后，调用 NetworkClient.newClientRequest() 方法创建 ClientRequest 请求，并交给 NetworkClient 进行发送（调用其 send() 方法）。</li>
</ul>
<h2 data-id="heading-3">Selector</h2>
<p>通过上面的小节，我们已经了解了 RecordAccumulator 中的数据转换成 ClientRequest 的流程。下面我们开始介绍NetworkClient 的相关内容，下图展示了 NetworkClient 依赖的核心组件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/549e7e5581974914b555f0daa54ab3bd~tplv-k3u1fbpfcp-watermark.image" alt="4、NetworkClient依赖组件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中我们看到有个 Selector 类，注意，这个 Selector 并不是 JDK 内的 java.nio.channels.Selector，而是org.apache.kafka.common.network.Selector（为了区分两者，这里将 org.apache.kafka.common.network.Selector 称为 KSelect）。</p>
<p>KSelector 实现了 Selectable 接口，底层 JDK Selector （nioSelector 字段）实现异步的网络 IO 操作。KSelector 支持的是客户端类型的应用，所以没有复杂的多线程操作，其中只使用单线程的方式来可以管理多条个 Channel 上的网络 IO 操作。KSelector 中处理的网络连接全部维护在一个 <code>Map<String, KafkaChannel></code> 集合（channels 字段）中，其中的 Key 是 NodeId，Value 是 KafkaChannel 对象，它表示当前 KafkaProducer 与对应 Node之间的网络连接。</p>
<p>KafkaChannel 是底层依赖 SocketChannel 完成数据的读写，下图展示了其三个关键依赖，NetworkSend 和NetworkReceive 是读写操作的真实数据所在，底层通过ByteBuffer实现。KafkaChannel 中的 send 字段用来记录暂存当前待发送的 NetworkSend 对象（即请求数据），receive 字段用来暂存当前待处理的 NetworkReceive 对象（即响应数据）。TransportLayer 封装 SocketChannel 及SelectionKey，TransportLayer 根据不同网络协议提供不同的策略实现，例如图中 PlaintextTransportLayer 实现就是普通的网络连接，SslTransportLayer 就是使用 SSL 加密的网络连接。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/765582eacdc140259702a3d343eac82f~tplv-k3u1fbpfcp-watermark.image" alt="5、KSelector依赖.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">创建网络连接</h3>
<p>了解了 KSelector 的数据结构之后，我们来看其核心方法，首选是 connect() 方法，从名字就能看出它是用来创建网络里连接的，就非常典型的 NIO 操作，直接看代码吧（下面省略了try/catch代码块）：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">connect</span><span class="hljs-params">(String id, InetSocketAddress address, <span class="hljs-keyword">int</span> sendBufferSize, <span class="hljs-keyword">int</span> receiveBufferSize)</span> <span class="hljs-keyword">throws</span> IOException </span>&#123;
    ensureNotRegistered(id); <span class="hljs-comment">// 检查是否与Node重复建立连接</span>
    <span class="hljs-comment">// 创建SocketChannel对象</span>
    SocketChannel socketChannel = SocketChannel.open();
    <span class="hljs-comment">// 配置SocketChannel对象，将SocketChannel设置为非阻塞模式，keeplive设置为true，</span>
    <span class="hljs-comment">// 指定SO_RCVBUF、SO_SNDBUF两个Buffer的大小</span>
    configureSocketChannel(socketChannel, sendBufferSize, receiveBufferSize);
    <span class="hljs-comment">// 因为是非阻塞方式，这里调用的SocketChannel.connect()方法是发起一个连接，</span>
    <span class="hljs-comment">// connect方法在连接正式建立之前就可能返回，在后面会通过channel.finishConnect()方法</span>
    <span class="hljs-comment">// 确认连接是否真正建立</span>
    <span class="hljs-keyword">boolean</span> connected = doConnect(socketChannel, address);
    <span class="hljs-comment">// 将这个socketChannel注册到nioSelector上，并关注OP_CONNECT事件，这里返回的SelectionKey中attach了关联的KafkaChannel对象</span>
    SelectionKey key = registerChannel(id, socketChannel, SelectionKey.OP_CONNECT);

    <span class="hljs-keyword">if</span> (connected) &#123;
        <span class="hljs-comment">// 如果立即建立了连接，则connected为true，且OP_CONNECT事件不会再被触发，这里情况这里直接</span>
        immediatelyConnectedKeys.add(key);
        key.interestOps(<span class="hljs-number">0</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">数据准备</h3>
<p>创建完 KafkaChannel 网络连接之后，下面就要发送数据了。下面先来到 KSelector.send() 方法，我们从 RecordAccumulator 拿到数据并形成 ClientRequest 请求之后，就立刻调用了 NetworkClient.send() 方法，而 NetworkClient.send() 方法最底层实际上就调用了 KSelector.send() 方法，具体实现如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">send</span><span class="hljs-params">(NetworkSend send)</span> </span>&#123;
    <span class="hljs-comment">// 获取请求的目标NodeId</span>
    String connectionId = send.destinationId();
    <span class="hljs-comment">// 从channels中查询目标Node对应的KafkaChannel，如果是正在关闭的KafkaChannel，</span>
    <span class="hljs-comment">// 会在KSelector.close()方法中从channels集合转移到closingChannels集合中，</span>
    <span class="hljs-comment">// 此时只能从正在关闭的KafkaChannel中读取数据，不能再发送数据了</span>
    KafkaChannel channel = openOrClosingChannelOrFail(connectionId);
    <span class="hljs-keyword">if</span> (closingChannels.containsKey(connectionId)) &#123;
        <span class="hljs-keyword">this</span>.failedSends.add(connectionId); <span class="hljs-comment">// 记录发送失败了</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 将NetworkSend交给KafkaChannel进行处理</span>
        channel.setSend(send);
        <span class="hljs-comment">// 这里省略了try/catch代码块，要是setSend()方法发生异常，这里直接关闭当前Channel</span>
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setSend</span><span class="hljs-params">(NetworkSend send)</span> </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">this</span>.send != <span class="hljs-keyword">null</span>) <span class="hljs-comment">// 一次只能暂存一个NetworkSend对象</span>
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalStateException(<span class="hljs-string">"..."</span>);
    <span class="hljs-comment">// 将待发送的数据（NetworkSend）记录到send字段中，等待Channel可写</span>
    <span class="hljs-keyword">this</span>.send = send; 
    <span class="hljs-comment">// 关注的事件集合中，添加OP_WRITE事件</span>
    <span class="hljs-keyword">this</span>.transportLayer.addInterestOps(SelectionKey.OP_WRITE);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有个断层，就是前面 NetworkClient.send() 方法传入的不是 ClientRequest 对象吗？怎么到了KSelector.send() 方法中就变成了 NetworkSend 对象了呢？那指定是进行了系列转换啊，来简单看看这个转换吧，来到 NetworkClient.doSend() 方法中：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">doSend</span><span class="hljs-params">(ClientRequest clientRequest, <span class="hljs-keyword">boolean</span> isInternalRequest, <span class="hljs-keyword">long</span> now, AbstractRequest request)</span> </span>&#123;
    String destination = clientRequest.destination();
    <span class="hljs-comment">// 创建请求头，其中就是我们前面介绍的Kafka Protocol通用请求头</span>
    RequestHeader header = clientRequest.makeHeader(request.version());
    <span class="hljs-comment">// 将ProduceRequest对象转换成Send对象</span>
    Send send = request.toSend(header);
    <span class="hljs-comment">// 将上述一坨请求相关的，包括ClientRequest、ProduceRequest、RequestHeader、Send封装成InFlightRequest</span>
    InFlightRequest inFlightRequest = <span class="hljs-keyword">new</span> InFlightRequest(
            clientRequest,
            header,
            isInternalRequest,
            request,
            send,
            now);
    <span class="hljs-comment">// 将InFlightRequest记录到inFlightRequests集合中，表示该请求已发送但是未收到响应</span>
    <span class="hljs-keyword">this</span>.inFlightRequests.add(inFlightRequest);
    <span class="hljs-comment">// Send外面套一层NetworkSend，交给KSelector.send()方法了</span>
    selector.send(<span class="hljs-keyword">new</span> NetworkSend(clientRequest.destination(), send));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从这段代码中，看到了 AbstractRequest 到 Send 的转换，AbstractRequest 不仅是 ProduceRequest 的父类，而且还是 <a href="https://xxxlxy2008.github.io/kafka/5%E3%80%81%E6%B7%B1%E6%BD%9Ckafka-producer3/#more" target="_blank" rel="nofollow noopener noreferrer">Kafka Protocol</a> 请求的父类，其 toSend() 方法会最终会调用 SendBuilder.buildSend() 方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Send <span class="hljs-title">buildSend</span><span class="hljs-params">(Message header, <span class="hljs-keyword">short</span> headerVersion, Message apiMessage, 
<span class="hljs-keyword">short</span> apiVersion)</span> </span>&#123;
    ObjectSerializationCache serializationCache = <span class="hljs-keyword">new</span> ObjectSerializationCache();
    <span class="hljs-comment">// 计算请求总长度，不同版本请求长度不同</span>
    MessageSizeAccumulator messageSize = <span class="hljs-keyword">new</span> MessageSizeAccumulator();
    header.addSize(messageSize, serializationCache, headerVersion);
    apiMessage.addSize(messageSize, serializationCache, apiVersion);
    <span class="hljs-comment">// 创建SendBuilder对象</span>
    SendBuilder builder = <span class="hljs-keyword">new</span> SendBuilder(messageSize.sizeExcludingZeroCopy() + <span class="hljs-number">4</span>);
    <span class="hljs-comment">// 向SendBuilder中写入请求总长度</span>
    builder.writeInt(messageSize.totalSize());
    <span class="hljs-comment">// 写入请求头</span>
    header.write(builder, serializationCache, headerVersion);
    <span class="hljs-comment">// 写入请求体</span>
    apiMessage.write(builder, serializationCache, apiVersion);
    <span class="hljs-keyword">return</span> builder.build();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到 SendBuilder 是能写入数据的，没错，它底层也维护了一个 ByteBuffer（buffer 字段），但是它还维护了一个 <code>List<ByteBuffer></code> 集合（buffers 字段），buffer 字段用来写入长度、Header 头这种基础类型的数据，<code>List<ByteBuffer></code> 集合用来直接复用 MemoryRecords 中的 ByteBuffer，这也叫 "zero-copy"，其实就是复用 ByteBuffer。这里说一下 SendBuilder.writeRecords() 方法的实现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56dbdeeac4964d1e9483ab5a0a650bd5~tplv-k3u1fbpfcp-watermark.image" alt="6、SendBuilder结构图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们从上图中可以看出，SendBuilder 中的 buffer 只是个工具 buffer，写入简单类型数据之后，可以通过 slice() 方法切分成很多段，然后添加 buffers 中合适的位置，接下来追加的是 MemoryRecords 中存储有效负载的大 ByteBuffer。写入数据相关实现可以参考 write*() 方法，尤其是写入 MemoryRecords 的 writeRecords() 方法。</p>
<p>最后来看 SendBuilder.build() 方法，它首先调用 flushPendingSend() 方法将 buffers 集合封装成 ByteBufferSend 对象添加到 sends 集合中，接下来 build() 方法会检查 sends 集合长度，如果 sends 集合中只有单个 Send 对象，则直接返回该 Send 对象，即上面创建的 ByteBufferSend 对象，如果有多个 Send 对象的话，会将他们封装成 MultiRecordsSend 对象返回。正如前面所说，build() 方法返回的 Send 对象外面会再封装一层 NetworkSend，然后就交给 KSelector.send() 方法，等待发送了。</p>
<h3 data-id="heading-6">读写数据</h3>
<p>准备完数据之后，下面就是进行真正的网络 IO 了，这个实现在 KSelector.poll() 方法中，KSelector 会调用nioSelector.select() 方法等待 IO 事件发生。下面就是 poll() 方法发核心逻辑：</p>
<p><strong>1、</strong> 首先调用 clear() 方法清理上次 poll() 方法调用的全部状态信息，为此次调用做准备。</p>
<p><strong>2、</strong> 当我们接收响应的时候，是需要占用内存空间的，从响应中读取的数据自然也是放到 ByteBuffer 中（NetworkReceive.readFrom() 中分配），而这些 ByteBuffer 则是从 MemoryPool 申请的。</p>
<ul>
<li>在 KafkaChannel 读取响应的时候，会尝试从 MemoryPool 中获取足够大的 ByteBuffer 对象来存储响应数据，如果分配不到足够大的 ByteBuffer，则将 KafkaChannel 设置成 mute 状态，也不再关注 OP_READ 事件，即不再继续读取响应的数据。</li>
<li>在这里（KSelector.select() 方法第 2 步）就会检查当前 MemoryPool 的状态，如果 MemoryPool 有足够的空间，则更新所有 KafkaChannel 的 muteState 状态，并开始关注所有 KafkaChannel 上的 OP_READ 事件，让所有 KafkaChannel 可以继续读取响应数据。</li>
</ul>
<p>这里多说点 MemoryPool 的内容，下图展示了 MemoryPool 接口的实现类：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3265b10fedd74021b6b550e4c00456a8~tplv-k3u1fbpfcp-watermark.image" alt="7、MemoryPool类图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>SimpleMemoryPool 实现只是维护了一个 AtomicLong 来记录当前剩余的空闲字节数（availableMemory 字段），其中并没有预分配任何 ByteBuffer 空间，在其 tryAllocate() 方法直接创建新的 ByteBuffer，release() 方法也只是递增 availableMemory，然后 GC 来回收 ByteBuffer。</li>
<li>GarbageCollectedMemoryPool 是 SimpleMemoryPool 的子类，它使用 WeakReference + ReferenceQueue 来监听 ByteBuffer 被 GC 回收的事件（同时配合 SimpleMemoryPool 留下的 bufferToBeReturned()、bufferToBeReleased() 两个钩子方法），从而避免使用方不调用 release() 方法造成 MemoryPool 内存泄漏。</li>
<li>BatchMemoryPool 与前面介绍的 BufferPool 有点类似，但是简单很多，其中只会缓存固定大小的 ByteBuffer（batchSize 字段指定），申请过大的 ByteBuffer 直接报错。通过 release() 方法释放的 ByteBuffer 也暂存到 BatchMemoryPool.free 集合中暂存，也是只收 batchSize 大小的 ByteBuffer。</li>
<li>MemoryPool.NONE 这是没有大小限制的 MemoryPool 实现。</li>
</ul>
<p><strong>3、</strong> 计算 nioSelector.select() 方法的 timeout 时长。这里会 immediatelyConnectedKeys 集合，如果 immediatelyConnectedKeys 不为空，则 timeout 设置为 0，调用 selectNow() 方法，不会有任何阻塞。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">if</span> (!immediatelyConnectedKeys.isEmpty() || (madeReadProgressLastCall && dataInBuffers))
    timeout = <span class="hljs-number">0</span>; <span class="hljs-comment">// 更改timeout值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>KSelector.poll() 传入的 timeout 已经考虑了很多方面，它是在 Sender.sendProducerData() 方法最后那段代码以及 NetworkClient.poll() 方法中进行计算的：</p>
<ul>
<li>当前有数据要发送，poll() 的 timeout 就设置成 0，让数据尽快发送出去。</li>
<li>如果 RecordAccumulator 中有部分数据，但发送条件没有 ready，则 timeout 为消息的超时时长。</li>
<li>如果 RecordAccumulator 没有数据，则 timeout 为 kafka 元数据过期的时长。</li>
</ul>
<p>在 KSelector.poll() 方法中呢，又添加了对 immediatelyConnectedKeys 考虑，immediatelyConnectedKeys 集合就是在 connect() 方法创建网络连接时，立刻建立的那部分连接，既然连接都建立了，我们就要快速为</p>
<p><strong>4、</strong> 调用 nioSelector.select(timeout) 方法（或 selectNow() 方法）等待网络 IO 事件。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">if</span> (timeoutMs == <span class="hljs-number">0L</span>) <span class="hljs-comment">// 如果timeout为0，不会阻塞</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.nioSelector.selectNow();
<span class="hljs-keyword">else</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.nioSelector.select(timeoutMs);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5、</strong> 通过 nioSelector.selectedKeys() 方法获取 SelectionKey 集合，并执行 pollSelectionKeys() 方法处理步骤 5 得到的 SelectionKey 集合。</p>
<p><strong>7、</strong> 再次执行 pollSelectionKeys() 方法处理 immediatelyConnectedKeys 集合。</p>
<p>8、执行 IdleExpiryManager() 方法关闭长时间空闲的 KafkaChannel 。</p>
<p>经过上面的一系列分析，KSelector.pollSelectionKeys() 方法是处理 I/O 操作的核心方法，简单来说，就是干了三件事：处理 OP_ CONNECT、处理 OP_ READ、处理 OP_WRITE事件。下面是精简后的代码：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">pollSelectionKeys</span><span class="hljs-params">(Set<SelectionKey> selectionKeys,<span class="hljs-keyword">boolean</span> isImmediatelyConnected, <span class="hljs-keyword">long</span> currentTimeNanos)</span> </span>&#123;
    <span class="hljs-comment">// 遍历收到到的全部网络IO事件</span>
    <span class="hljs-keyword">for</span> (SelectionKey key : determineHandlingOrder(selectionKeys)) &#123;
        <span class="hljs-comment">// 从SelectionKey的attach中获取KafkaChannel</span>
        KafkaChannel channel = channel(key);
        String nodeId = channel.id();
        <span class="hljs-keyword">if</span> (idleExpiryManager != <span class="hljs-keyword">null</span>) <span class="hljs-comment">// 更新连接操作时间，防止因空闲被关闭</span>
            idleExpiryManager.update(nodeId, currentTimeNanos);

        <span class="hljs-keyword">if</span> (isImmediatelyConnected || key.isConnectable()) &#123;
            <span class="hljs-comment">// 如果是新建的连接，调用finishConnect()方法更新关注的网络IO事件，</span>
            <span class="hljs-comment">// 这里会取消对OP_CONNECT事件关注，开始关注OP_READ事件</span>
            <span class="hljs-keyword">if</span> (channel.finishConnect()) &#123; 
                <span class="hljs-keyword">this</span>.connected.add(nodeId);
                SocketChannel socketChannel = (SocketChannel) key.channel();
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">continue</span>;
            &#125;
        &#125;

        ...<span class="hljs-comment">// 网络连接已经建立，但是还没有进行SSL握手、鉴权等操作的话，会在这里进行，这部分逻辑省略</span>

        <span class="hljs-keyword">if</span> (channel.ready() && channel.state() == ChannelState.NOT_CONNECTED)
            channel.state(ChannelState.READY); <span class="hljs-comment">// 更新KafkaChannel状态</span>

        <span class="hljs-keyword">if</span> (channel.ready()
            && (key.isReadable() || channel.hasBytesBuffered()) <span class="hljs-comment">// 收到OP_READ事件</span>
            && !hasCompletedReceive(channel) <span class="hljs-comment">// 是否有未处理的响应</span>
              && !explicitlyMutedChannels.contains(channel)) &#123; <span class="hljs-comment">// 检查Channel是否处于muted状态</span>
            attemptRead(channel); <span class="hljs-comment">// 读取数据</span>
        &#125;

        <span class="hljs-keyword">long</span> nowNanos = channelStartTimeNanos != <span class="hljs-number">0</span> ? channelStartTimeNanos : currentTimeNanos;
        <span class="hljs-keyword">try</span> &#123;
            attemptWrite(key, channel, nowNanos); <span class="hljs-comment">// 发送请求</span>
        &#125; <span class="hljs-keyword">catch</span> (Exception e) &#123;
            sendFailed = <span class="hljs-keyword">true</span>;
            <span class="hljs-keyword">throw</span> e;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 attemptRead() 方法中，会调用 KafkaChannel 中的 read() 方法读取数据，读取得到的 NetworkReceive 对象会记录到 KafkaChannel.receive 字段中。在从连接读取数据的时候，是先读取响应头，其中封装了消息长度，再按照其长度创建合适大小的 ByteBuffer（参考 NetworkReceive.readFrom() 方法），然后读取消息体。完成读取之后，attempRead() 方法hi调用 addToCompletedReceives() 方法将 KafkaChannel 与 NetworkReceive 对象的映射关系记录到 completedReceives 集合中。</p>
<p>在 attemptWrite() 方法中，会调用 KafkaChannel 中的 write() 方法将 send 字段中的 NetworkSend 数据发送出去，发送完成之后，将 send 字段置空，方便下一个 NetworkSend 对象的到来。同时，还会将发送成功的 NetworkSend 对象记录到 completedSends 集合中，等待后续处理。这里比 attemptRead() 方法多的一步操作是，取消对该 KafkaChannel 上 OP_WRITE 事件的关注，毕竟数据发送完了。</p>
<h2 data-id="heading-7">NetworkClient</h2>
<p>NetworkClient 的入口和底层依赖基本上介绍完了，下面我们回头来看 NetworkClient 本身。</p>
<h3 data-id="heading-8">核心数据结构</h3>
<h4 data-id="heading-9">ClusterConnectionStates</h4>
<p>首先，NetworkClient 中所有 KafkaChannel 的状态都维护在 ClusterConnectionStates 中，其底层使用 <code>Map<String, NodeConnectionState></code> 集合实现，其中的 Key 是 NodeId，value 是 NodeConnectionState 对象。NodeConnectionState 中不仅记录了连接状态（ConnectionState 枚举），还记录了最近一次尝试连接的时间戳。在前面介绍的 ready() 方法中，使用到了 ClusterConnectionStates 来判断连接状态以及决定是否尝试重连。</p>
<h4 data-id="heading-10">InFlightRequests</h4>
<p>NetworkClient 中另一个关键字段 inFlightRequests，InFlightRequests 队列的主要作用是缓存了已经发出去但没收到响应的请求，前面也简单提到过。InFlightRequests 底层是通过一个 <code>Map<String, Deque<NetworkClient.InFlightRequest>></code> 集合实现的，其中 Key 是 NodeId，Value 是发送到对应 Node 的请求集合。NetworkClient.InFlightRequest 中记录了请求头、请求体、关联的 Send 对象、callback等等一系列与请求相关的内容。</p>
<p>这里着重看一下 InFlightRequests.canSendMore() 方法，NetworkClient.ready() 方法就是依赖该方法以及 ClusterConnectionStates 的连接状态来判断当前是否能向指定 Node 发送请求的，进一步与 RecordAccumulator.ready() 方法的返回值共同决定此次发送的数据：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">canSendMore</span><span class="hljs-params">(String node)</span> </span>&#123;
    <span class="hljs-comment">// 获取目标Node对应的InFlightRequest集合</span>
    Deque<NetworkClient.InFlightRequest> queue = requests.get(node);
    <span class="hljs-keyword">return</span> queue == <span class="hljs-keyword">null</span> || queue.isEmpty() ||   <span class="hljs-comment">// 没有InFlight请求发送</span>
            <span class="hljs-comment">// 检查当前队列头部的第一个请求是否已经发送完成，如果队头的请求一直发送不出去，可能是网络出现问题，</span>
      <span class="hljs-comment">// 则不能继续向此Node发送请求。另外，队首请求其实就是KafkaChannel.send字段指向请求，通过前面的</span>
      <span class="hljs-comment">// 介绍我们知道，发送数据的时候要将请求设置到KafkaChannel.send字段，这个判断也是为防止未发送</span>
      <span class="hljs-comment">// 完的请求被后续覆盖。</span>
            (queue.peekFirst().send.completed() 
<span class="hljs-comment">// 下面这个判断InFlightRequests队列中是否堆积过多请求，导致堆积的原因可能网络问题、生产速度过</span>
             <span class="hljs-comment">// 快、broker集群处理能力跟不上，此时都应该暂停发送请求。</span>
            && queue.size() < <span class="hljs-keyword">this</span>.maxInFlightRequestsPerConnection);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">DefaultMetadataUpdater</h4>
<p>NetworkClient 中的 metadataUpdater 字段（DefaultMetadataUpdater 类型）主要负责 Metadata（kafka 集群元数据）的更新。</p>
<p>DefaultMetadataUpdater.maybeUpdate()方法用来判断当前的 Metadata 是否需要更新：</p>
<p>**1、**首先会通过 Metadata.timeToNextUpdate() 方法检查 Metadata 中的 needFullUpdate、needPartialUpdate 两个标记，如果这两个标记为 true，表示 Metadata 需要立即更新。如果都不为 true，则根据 Metadata 过期时间（metadataExpireMs）和网络退避时间（refreshBackoffMs）来计算下次更新的时间间隔。</p>
<p>**2、**接下来检查当前是有已经发过 Metadata 更新请求，这是通过 inProgress 字段进行判断的，其中记录了发送的 Metadata 更新请求。如果没发送，则返回步骤 1 的结果，如果已经发送了，则返回请求超时时长。</p>
<p><strong>3、</strong> 经过上述两步处理之后，发现需要立刻更新 Metadata 的话，则会：</p>
<pre><code class="copyable">- 通过 leastLoadedNode() 方法选择一个负载最小的 Node，后续会将 Metadata 更新请求发送到该 Node。leastLoadedNode() 方法判断各个 Node 负载的方法就是检查每个 Node 对应的 InFightRequest 队列长度，长度越小，对应 Node 负载越小。
- 执行 maybeUpdate(long,Node) 重载，向选出的 Node 发送 Metadata 更新请求（MetadataRequest）。具体的发送方式是调用 sendInternalMetadataRequest() 方法，其底层核心逻辑是调用前面介绍的 NetworkClient.doSend() 方法，即将 MetadataRequest 封装成 Send 对象并设置到 KafkaChannel.send 字段中等待发送，同时也会将请求添加到 InFlightRequests 集合中。
- 发送完 Metadata 更新请求之后，会将请求版本等信息记录到 inProgress 字段中。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>了解了 Metadata 更新的逻辑之后，我们需要再深入一步，了解一下 MetadataRequest 的具体格式：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/059ec5c101004fe99e2563074e7ffa4f~tplv-k3u1fbpfcp-watermark.image" alt="8、MetadataRequest请求格式.png" loading="lazy" referrerpolicy="no-referrer"></p>






























<table><thead><tr><th>字段名称</th><th>字段类型</th><th>字段描述</th></tr></thead><tbody><tr><td>topic_id</td><td>String</td><td>topic唯一标识</td></tr><tr><td>topic_name</td><td>String</td><td>topic名称</td></tr><tr><td>allow_auto_topic_creation</td><td>boolean</td><td>是否自动创建不存在的topic</td></tr><tr><td>include_topic_authorized_operations</td><td>boolean</td><td>是否包含鉴权操作</td></tr></tbody></table>
<p>创建 MetadataRequest 请求的地方是在 Metadata.newMetadataRequestAndVersion() 方法：如果是部分更新请求（needPartialUpdate = true），则只会将 ProducerMetadata.newTopics 添加到 MetadataRequest 中；如果是全量更新请求（needFullUpdate = true），则会将  ProducerMetadata.topics 添加到 MetadataRequest 中。对这  ProducerMetadata 中这两个 topic 集合的操作，我们前面已经介绍过了，这里不再重复。</p>
<p>分析完 DefaultMetadataUpdater 发送 MetadataRequest 的逻辑之后，我们再来看其 handleSuccessfulResponse() 方法，也就是处理 MetadataResponse 响应的逻辑。下面先来了解一下 MetadataResponse 的格式：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/319cd0f2f7024781b3ff1d27325e4a25~tplv-k3u1fbpfcp-watermark.image" alt="9、MetadataResponse格式.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每个字段的含义，参考这里 <a href="https://xxxlxy2008.github.io/uncategorized/kafka%E6%B6%88%E6%81%AF%E6%A0%BC%E5%BC%8F/#more" target="_blank" rel="nofollow noopener noreferrer">Kafka Protocol</a>，搜索 <code>Metadata Response (Version: 11)</code> 即可。</p>
<p>下面来到 DefaultMetadataUpdater.handleSuccessfulResponse() 方法，从名字就能看出它是处理 MetadataResponse 的，最底层会调用 Metadata.handleMetadataResponse() 方法，调用栈如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94c75d34f9444564a1c17b710ea12c2f~tplv-k3u1fbpfcp-watermark.image" alt="10、处理MetadataResponse.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 Metadata.handleMetadataResponse() 方法中会解析 MetadataResponse，并最终填充到 MetadataCache 中，最核心的代码片段如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">if</span> (isPartialUpdate) <span class="hljs-comment">// 部分更新的时候，调用原MetadataCache的mergeWith()方法将新旧两组元数据进行合并，并生成新的MetadataCache对象</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.cache.mergeWith(metadataResponse.clusterId(), nodes, partitions,
        unauthorizedTopics, invalidTopics, internalTopics, metadataResponse.controller(),
        (topic, isInternal) -> !topics.contains(topic) && retainTopic(topic, isInternal, nowMs));
<span class="hljs-keyword">else</span> <span class="hljs-comment">// 如果是完整更新，则直接创建MetadataCache对象来记录最新的元数据</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MetadataCache(metadataResponse.clusterId(), nodes, partitions,
        unauthorizedTopics, invalidTopics, internalTopics, metadataResponse.controller());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>元数据更新完成之后，Metadata 还会：</p>
<ul>
<li>重置 needPartialUpdate、needFullUpdate 等标志字段</li>
<li>更新updateVersion、 lastRefreshMs、lastSuccessfulRefreshMs 等版本号和时间戳</li>
<li>触发 clusterResourceListeners 监听器。</li>
</ul>
<p>最后DefaultMetadataUpdater 就会将 inProgress 字段置空，标志整个 MetadataResponse 处理完成。</p>
<h3 data-id="heading-12">核心方法</h3>
<p>了解了 NetworkClient 中核心数据结构之后，我们开始看一下 NetworkClient 的核心方法。</p>
<p>首先来看其 ready() 方法，其核心逻辑已经在 Sender.sendProducerData() 方法中的步骤 4 中，详细分析过了，这里不再重复。</p>
<p>NetworkClient.doSend() 方法在 <code>Selector数据准备</code>小节介绍过了，这里不再重复。</p>
<p>接下来看 NetworkClient.poll() 方法，其中最核心的就是调用 KSelector.poll() 方法，KSelector.poll() 方法的核心逻辑在前面已经深入分析过了，这里不再重复。除此之外，NetworkClient.poll() 中还会调用多个 handle*() 方法来处理发送完成的请求、读取到的响应等，我们一个一个来看：</p>
<h4 data-id="heading-13">handleCompletedSends</h4>
<p>首先回看一下KSelector.attemptWrite() 方法，其中会将发送成功的 Send 对象记录到  completedSends 集合中，handleCompletedSends() 方法紧跟在 KSelector.poll() 方法之后被调用，用来处理最近一次 poll() 方法中发送成功的请求。另外我们知道，InFlightRequests 中记录已发送但是未响应，其中最后添加的就是 completedSends 集合对应的请求，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ba75fad2cca4c23bd1c088a7780c7a0~tplv-k3u1fbpfcp-watermark.image" alt="11、completeSends结构.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 handleCompletedSends() 方法中会遍历 completedSends 集合，如果对应的 InFlightRequest 集合首个请求不需要响应，则直接将其结束掉并添加到 responses 集合中：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handleCompletedSends</span><span class="hljs-params">(List<ClientResponse> responses, <span class="hljs-keyword">long</span> now)</span> </span>&#123;
    <span class="hljs-keyword">for</span> (NetworkSend send : <span class="hljs-keyword">this</span>.selector.completedSends()) &#123; 
    <span class="hljs-comment">// 关注此次poll()发送的InFlightRequest队列</span>
        InFlightRequest request = <span class="hljs-keyword">this</span>.inFlightRequests.lastSent(send.destinationId());
        <span class="hljs-keyword">if</span> (!request.expectResponse) &#123; <span class="hljs-comment">// 请求不需要响应</span>
        <span class="hljs-comment">// 将请求从InFlightRequests集合中删除</span>
            <span class="hljs-keyword">this</span>.inFlightRequests.completeLastSent(send.destinationId()); 
         <span class="hljs-comment">// 创建该请求对应的响应，并添加到responses集合中</span>
            responses.add(request.completed(<span class="hljs-keyword">null</span>, now));
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">handleCompletedReceives</h4>
<p>前面介绍的的 attemptRead() 方法会在读取到 NetworkReceive 对象之后，将其记录到 completedReceives 集合中，NetworkClient.handleCompleteReceives() 方法就会遍历 completedReceives 队列，从 InFlightRequests 中删除请求，然后根据响应类型进行分类处理：</p>
<ul>
<li>如果是 MetadataResponse，则会通过调用 DefaultMetadataUpdater.handleSuccessfulResponse() 方法更新 MetadataCache。</li>
<li>如果是 ApiVersionsResponse（对应 ApiVersionsRequest，用来获取 kafka 集群中各个 API 的协议版本），则交给 handleApiVersionsResponse() 方法处理，更新 NetworkClient.apiVersions 集合（其中维护了 NodeId → ApiKey → ApiVersion 之间的映射关系）。在 NetworkClient.doSend() 方法创建请求的时候，会通过 apiVersions 确定不同 Node 的协议版本来创建同版本的请求。</li>
<li>如果是其他响应，则将响应封装成 ClientResponse 后添加到 responses 集合中，等待后续处理。</li>
</ul>
<h4 data-id="heading-15">handleDisconnections</h4>
<p>在前面介绍的 NetworkClient.send() 方法以及关闭 KafkaChannel 的时候，会将对应的 NodeId 记录到  disconnected 集合中。handleDisconnections() 方法就会遍历 disconnected 集合，将 InFlightRequests 中对应的队列清空，同时为每个请求都创建 ClientResponse 并添加到 responses 集合中。这里创建的 ClientResponse 会标识 disconnected 标记，也就是响应是因为关闭连接或是网络问题产生的。</p>
<p>如果碰到 MetadataRequest，先会清理 DefaultMetadataUpdater 中的 inProgress 等状态字段，然后通过 handleServerDisconnect() 方法再次将 needFullUpdate 设置为true，标识需要更新 kafka 集群元数据。</p>
<h4 data-id="heading-16">handleConnections</h4>
<p>在 KSelector.pollSelectionKeys() 处理新建连接的时候，除了会调用 finishConnect() 方法设置对 OP_READ 事件的关注，还会将对应的 NodeId 添加到 connected 集合中。这里的 handleConnections() 方法会根据 connected 集合，将ConnectionStates 中的连接状态修改为 CONNECTED。</p>
<h4 data-id="heading-17">handleTimedOutRequests</h4>
<p>handleTimedOutRequests()方法比较简单，就是遍历 InFlightRequests 集合，kafka有没有超时的请求，之后的处理逻辑与 handleDisconnections()方法一样，代码就不贴出来了。</p>
<h4 data-id="heading-18">handleTimedOutConnections</h4>
<p>handleTimedOutConnections() 方法会检查 ClusterConnectionStates，从中找出建立连接超时的 NodeId，直接关闭连接，然后走 handleDisconnections() 方法一样的处理。</p>
<h4 data-id="heading-19">handleInitiateApiVersionRequests</h4>
<p>在 handleConnections() 方法处理新建连接的同时，会将 NodeId 添加到 nodesNeedingApiVersionsFetch 集合中。在 handleInitiateApiVersionRequests() 方法中遍历 nodesNeedingApiVersionsFetch 集合，并调用 doSend() 方法发送 ApiVersionsRequest 请求，响应在上面介绍的 handleCompletedReceives() 方法中处理。</p>
<h4 data-id="heading-20">completeResponses</h4>
<p>经过上述一系列 handle*() 方法的处理之后，NetworkClient.poll() 方法中产生的全部 ClientResponse 已经被收集到了responses 集合中。在 completeResponses() 方法中会遍历 responses 集合，调用每个对应 ClientRequest 中的 callback（RequestCompletionHandler 类型）。</p>
<p>RequestCompletionHandler 与 ClientRequest 的绑定可以回顾 Sender.sendProduceRequest() 中创建 ClientRequest 对象的逻辑，这里使用的 RequestCompletionHandler 对象是个匿名对象，实际的 callback 逻辑位于 Sender.handleProduceResponse() 方法。</p>
<p>无论是正常响应还是异常响应，handleProduceResponse() 方法都会调用 completeBatch() 方法进行处理，Sender.completeBatch() 方法中会根据 response.error 中的错误码进行分类处理：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">completeBatch</span><span class="hljs-params">(ProducerBatch batch, ProduceResponse.PartitionResponse response, <span class="hljs-keyword">long</span> correlationId,<span class="hljs-keyword">long</span> now)</span> </span>&#123;
    Errors error = response.error;
    <span class="hljs-keyword">if</span> (error == Errors.MESSAGE_TOO_LARGE && batch.recordCount > <span class="hljs-number">1</span> && !batch.isDone() &&
            (batch.magic() >= RecordBatch.MAGIC_VALUE_V2 || batch.isCompressed())) &#123; <span class="hljs-comment">// ---(3)</span>
        <span class="hljs-comment">// 省略事务消息的相关代码和日志</span>
        <span class="hljs-comment">// MESSAGE_TOO_LARGE错误码表示ProducerBatch过大，这里会进行切分并重新写入RecordAccumulator</span>
      <span class="hljs-comment">// 进行重试</span>
        <span class="hljs-keyword">this</span>.accumulator.splitAndReenqueue(batch);
        <span class="hljs-comment">// 从InFlightRequests中删除该发送失败的ProducerBatch</span>
        maybeRemoveAndDeallocateBatch(batch);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (error != Errors.NONE) &#123;
        <span class="hljs-keyword">if</span> (canRetry(batch, response, now)) &#123; <span class="hljs-comment">// ----（2）</span>
            <span class="hljs-comment">// 发生了异常，但是未达到重试次数上限且消息未超时，则可以重试，</span>
            <span class="hljs-comment">// 这里通过reenqueueBatch()方法将ProducerBatch重新写入RecordAccumulator队首，尽快发送</span>
            reenqueueBatch(batch, now);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (error == Errors.DUPLICATE_SEQUENCE_NUMBER) &#123;
            completeBatch(batch, response); <span class="hljs-comment">// 序号放生问题</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 其他无法处理的异常，直接调用failBatch()方法</span>
            failBatch(batch, response, exception, batch.attempts() < <span class="hljs-keyword">this</span>.retries);
        &#125;
        <span class="hljs-keyword">if</span> (error.exception() <span class="hljs-keyword">instanceof</span> InvalidMetadataException) &#123;
            <span class="hljs-comment">// 如果是元数据的异常，则设置needFullUpdate，继续更新Metadata</span>
            metadata.requestUpdate();
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 正常响应的处理 ---（1）</span>
        completeBatch(batch, response);
    &#125;
    <span class="hljs-keyword">if</span> (guaranteeMessageOrder) <span class="hljs-comment">// 单条发送消息的场景中，会解开发送限制，准备发送后续ProducerBatch</span>
        <span class="hljs-keyword">this</span>.accumulator.unmutePartition(batch.topicPartition);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先来看（1）处这个分支，它用来处理正常响应或不需要响应的情况，这里会执行 ProducerBatch.done()方法更改 ProducerBatch.finalState 状态（CAS操作）并通过 Tunks 集合找到每个 Record 上的 Callback 进行触发，最后释放 从 RecordAccumulator 中删除 ProducerBatch 并释放底层的 ByteBuffer。</p>
<p>接下来看（2）处这个分支，canRetry() 方法会检查下面几个条件，决定是否进行重试：</p>
<ul>
<li>ProducerBatch 是否已经超时（deliveryTimeoutMs）。</li>
<li>ProducerBatch 重试次数是否已经达到上限。</li>
<li>ProducerBatch 的状态是否处于未完成的状态。</li>
</ul>
<p>决定重试之后，在 reenqueueBatch() 方法中会将 ProducerBatch 添加到 RecordAccumulator 中相应队列的队首，同时将其从 InFlightRequests 中删除（后续 NetworkClient 还会给它加回来）。</p>
<p>最后来看（3）处这个分支，它是用来处理 ProducerBatch 过大的问题，在前面介绍写入 Record 的过程中，已经通过 MemoryRecordsBuilder.hasRoomFor() 方法确定了是否有足够空间呀，为啥还可能会出现无法处理的大 ProducerBatch 呢？这主要是因为压缩算法的原因，我们来看 estimatedBytesWritten() 方法，其中估算已写入字节数的时候，乘以了一个 estimatedCompressionRatio （预估压缩率），它起始值是 1。在<code>数据准备</code>的过程中，在 RecordAccumulator.drain() 方法中不仅会导出此次发送的 ProducerBatch 对象，还会调用它们的 close() 方法将 ProducerBatch 设置为只读状态，此时就会计算该 ProducerBatch 的压缩率，调用栈如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d591a5af2c1b4770b6977fb72023c673~tplv-k3u1fbpfcp-watermark.image" alt="12、计算压缩率.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>CompressionRatioEstimator 中维护了每个 topic 下不同压缩算法的压缩率（COMPRESSION_RATIO 字段，ConcurrentMap<String, float[]>），这里计算出来的压缩率就会小于 1。后续创建 MemoryRecordsBuilder 的时候，就会从 CompressionRatioEstimator 获取最新的压缩率进行预估，相关调用栈如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef5961b88b9140a3b1cf909c324231f8~tplv-k3u1fbpfcp-watermark.image" alt="13、使用压缩率2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ProducerBatch 构造方法中相关的代码片段如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">ProducerBatch</span><span class="hljs-params">(TopicPartition tp, MemoryRecordsBuilder recordsBuilder, <span class="hljs-keyword">long</span> createdMs, <span class="hljs-keyword">boolean</span> isSplitBatch)</span> </span>&#123;
    ... <span class="hljs-comment">// 初始化其他字段</span>
    <span class="hljs-comment">// 获取目标topic下指定压缩算法的压缩率</span>
    <span class="hljs-keyword">float</span> compressionRatioEstimation = CompressionRatioEstimator.estimation(topicPartition.topic(),
        recordsBuilder.compressionType());
  <span class="hljs-comment">// 更新MemoryRecordsBuilder记录的压缩率，这个MemoryRecordsBuilder的估算就依据该压缩率进行计算了</span>
    recordsBuilder.setEstimatedCompressionRatio(compressionRatioEstimation);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>了解了超大 ProducerBatch 产生的原因之后，我们回到（3）处的 splitAndReenqueue() 方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">splitAndReenqueue</span><span class="hljs-params">(ProducerBatch bigBatch)</span> </span>&#123;
    <span class="hljs-comment">// 重置压缩率</span>
    CompressionRatioEstimator.setEstimation(bigBatch.topicPartition.topic(), compression,
                      Math.max(<span class="hljs-number">1.0f</span>, (<span class="hljs-keyword">float</span>) bigBatch.compressionRatio()));
    <span class="hljs-comment">// 按照batchSize切分超大ProducerBatch，这样就得到了多个小ProducerBatch对象</span>
    Deque<ProducerBatch> dq = bigBatch.split(<span class="hljs-keyword">this</span>.batchSize);
    <span class="hljs-keyword">int</span> numSplitBatches = dq.size();
    <span class="hljs-comment">// 将切分后的ProducerBatch按序添加到目标Deque<ProducerBatch>的队首，尽快发送</span>
    Deque<ProducerBatch> partitionDequeue = getOrCreateDeque(bigBatch.topicPartition);
    <span class="hljs-keyword">while</span> (!dq.isEmpty()) &#123;
        ProducerBatch batch = dq.pollLast();
        incomplete.add(batch); <span class="hljs-comment">// 记录未发送的ProducerBatch</span>
        <span class="hljs-keyword">synchronized</span> (partitionDequeue) &#123;
            ... <span class="hljs-comment">// 省略事务相关的处理逻辑</span>
            partitionDequeue.addFirst(batch); <span class="hljs-comment">// 添加到队首</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> numSplitBatches;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">总结</h2>
<p>本课时更新重点介绍了 KafkaProducer 中 Sender 线程的相关内容，详细的分析了 Sender、KSelector、NetworkClient 等核心类的数据结构和方法，深入介绍了 KafkaProducer 发送请求、处理响应的内容。</p>
<p>下一课时我们将开始介绍 Kafka Consumer 的相关内容。</p>
<p>相关文章还会更新到，微信公众号：杨四正
原文地址：<a href="https://xxxlxy2008.github.io/kafka/5%E3%80%81%E6%B7%B1%E6%BD%9Ckafka-producer3/" target="_blank" rel="nofollow noopener noreferrer">xxxlxy2008.github.io/kafka/5%E3%…</a></p>
<p><img src="https://juejin.cn/post/%E4%BA%8C%E7%BB%B4%E7%A0%81.jpg" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            