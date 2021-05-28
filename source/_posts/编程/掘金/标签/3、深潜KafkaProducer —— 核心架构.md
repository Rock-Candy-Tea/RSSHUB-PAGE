
---
title: '3、深潜KafkaProducer —— 核心架构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d297648d7fb8496bb363a9c0d46d8133~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 18:24:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d297648d7fb8496bb363a9c0d46d8133~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>kafka 自定义了一套网络协议，我们可以使用任意语言来实现这套协议，实现向 kafka 集群 push message 以及从 kafka 集群 pull message 的效果。在 kafka 2.8.0 版本的源码中的 clients 模块就是官方默认提供的 Java 版本 producer、consumer 实现，我们本课时重点关注其中的 producer 部分实现。</p>
<h2 data-id="heading-0">kafka producer 示例演示</h2>
<p>按照国际惯例，先来一个 demo 示例，带同学们了解一下 kafka Producer 的基本使用，示例的具体代码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ProducerDemo</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
        Properties config = <span class="hljs-keyword">new</span> Properties();
        config.put(<span class="hljs-string">"client.id"</span>, <span class="hljs-string">"ProducerDemo"</span>);
        <span class="hljs-comment">// 指定kafka broker集群的地址</span>
        config.put(<span class="hljs-string">"bootstrap.servers"</span>, <span class="hljs-string">"localhost:9092"</span>);
        <span class="hljs-comment">// 配置kafka集群响应之前，需要有多少replica成功复制了该message，all表示整个ISR集合都复制完成</span>
        config.put(<span class="hljs-string">"acks"</span>, <span class="hljs-string">"all"</span>);
        <span class="hljs-comment">// 指定message key和value的序列化器，它负责将KV序列化成字节数组</span>
        config.put(<span class="hljs-string">"key.serializer"</span>, StringSerializer.class);
        config.put(<span class="hljs-string">"value.serializer"</span>, StringSerializer.class);
        KafkaProducer<String, String> producer = <span class="hljs-keyword">new</span> KafkaProducer<>(config);

        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
            <span class="hljs-comment">// 消息的value</span>
            <span class="hljs-keyword">long</span> startTime = System.currentTimeMillis();
            <span class="hljs-comment">// 构造ProducerRecord对象，其中记录了该message的目标topic以及key和value</span>
            ProducerRecord<String, String> record =
                    <span class="hljs-keyword">new</span> ProducerRecord<>(<span class="hljs-string">"test_topic"</span>, String.valueOf(i), <span class="hljs-string">"YangSizheng_"</span> + startTime);

            <span class="hljs-comment">// 第二个参数是一个匿名的CallBack对象，当producer接收到kafka集群发来的ACK确认消息的时候，</span>
            <span class="hljs-comment">// 会调用其onCompletion()方法完成回调</span>
            Future<RecordMetadata> future = producer.send(record, <span class="hljs-keyword">new</span> Callback() &#123;
                <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCompletion</span><span class="hljs-params">(RecordMetadata metadata, Exception e)</span> </span>&#123;
                    <span class="hljs-keyword">if</span> (e != <span class="hljs-keyword">null</span>)
                        System.out.println(<span class="hljs-string">"Send failed for record:"</span> + record + <span class="hljs-string">", error message:"</span> + e.getMessage());
                &#125;
            &#125;);
            <span class="hljs-comment">// send()方法是异步发送message，返回的是一个Future对象。如果需要同步发送，可以调用其get()方法，</span>
            <span class="hljs-comment">// 返回的RecordMetadata中包含了该message落到了哪个partition上，以及分配的offset多少</span>
            RecordMetadata recordMetadata = future.get();
            System.out.println(<span class="hljs-string">"partition:"</span> + recordMetadata.partition()
                    + <span class="hljs-string">", offset:"</span> + recordMetadata.offset());
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在执行 ProducerDemo 之前，我们执行<code>kafka-console-consumer.sh</code>命令启动命令行 consumer：</p>
<pre><code class="hljs language-shell copyable" lang="shell">./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test_topic
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行 ProducerDemo 可以在控制台看到如下输出：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d297648d7fb8496bb363a9c0d46d8133~tplv-k3u1fbpfcp-watermark.image" alt="1、ProducerDemo输出.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <code>kafka-console-consumer.sh</code>命令行中看到如下输出：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8daf1e9e8b241f78dc6abc2e738dd18~tplv-k3u1fbpfcp-watermark.image" alt="2、consumer输出.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">kafka producer 架构概述</h2>
<p>了解了 kafka producer 的基本使用之后，我们开始深入 producer 的架构进行介绍，千言万语不及不急一张图，下图就是 kafka producer 的核心架构：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3a32bde99af47099b6e324bf7f1468d~tplv-k3u1fbpfcp-watermark.image" alt="3、producer完整架构图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里描述一下上图中涉及到的核心组件在，这里涉及到两个线程，一个是我们的业务线程(也就是图中的主线程)，另一个是 Sender 线程，我们一个个来说。
首先是主线程的逻辑：</p>
<ol>
<li>首先是 ProducerInterceptors 对 message 进行过滤或是修改。</li>
<li>使用 Serializer 对 message 的 key 和 value 进行序列化。</li>
<li>Partitioner 为根据一定策略为 message 选择合适的 partition。</li>
<li>将 message 封装成 ProducerRecord 写入到 RecordAccumulator 中暂存，RecordAccumulator 对象中维护了多个队列，可以看做是 message 的缓冲区，用来实现 message 的批量发送。</li>
</ol>
<p>下面来看 Sender 线程的逻辑：</p>
<ol>
<li>Sender 线程从 RecordAccumulator 中批量获取 message 数据，构造 ClientRequest。</li>
<li>将构造好的 ClientRequest 交给 NetworkClient 客户端发送。</li>
<li>NetworkClient 客户端将请求放入KafkaChannel的缓存。</li>
<li>NetworkClient 执行网络 I/O，完成请求的发送。</li>
<li>NetworkClient 收到响应，调用 ClientRequest 的回调函数，最终触发每个 message 上注册的回调函数。</li>
</ol>
<h2 data-id="heading-2">KafkaProducer.send() 核心</h2>
<p>介绍完 kafka producer 的核心架构和流程之后，我们开始深入分析 KafkaProducer.send() 方法，即主线程的核心逻辑，还是开局一张图，后面都好说：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef98db9c153b43cfa7f66673417ddf69~tplv-k3u1fbpfcp-watermark.image" alt="4、kafkaproducer_send.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面来描述一下 KafkaProducer.send() 方法的核心逻辑，也就是上图的核心步骤：</p>
<ol>
<li>主线程首先会调用 ProducerInterceptors.onSend() 方法，对 message 进行拦截或是修改。这里</li>
<li>然后，通过 waitOnMetadata()方法更新 Kafka 集群的信息，其底层实际上是通过唤醒 Sender 线程来更新 Metadata，Metadata 中保存的是 Kafka 集群元数据。</li>
<li>接下来，执行 Serializer.serialize()方法完成 message key 和 value 的序列化。</li>
<li>随后调用 partition() 为 message 选择合适的 partition。</li>
<li>调用 append()方法，将 message 写入到 RecordAccumulator 中暂存。</li>
<li>最后，唤醒 Sender 线程，后续就由 Sender 线程从 RecordAccumulator 中批量发送 message 到 kafka 集群。</li>
</ol>
<h3 data-id="heading-3">ProducerInterceptor</h3>
<p>首先来看 ProducerInterceptors，其中维护了一个 ProducerInterceptor 集合，其 onSend()方法、onAcknowledgement()方法、onSendError()方法，实际上，是循环调用 ProducerInterceptor 集合的方法。
我们可以通过实现 ProducerInterceptor 接口的 onSend() 方法来拦截或修改待发送的 message，也可以通过实现 onAcknowledgement()方法、onSendError()方法先于用户的 Callback，对kafka集群响应进行预处理。</p>
<h3 data-id="heading-4">Kafka Metadata</h3>
<p>在我们通过 KafkaProducer 发送 message 的时候，我们只明确指定了 message 要写入哪个 topic ，并没有明确指定要写入的 partition。</p>
<p>但是同一个 topic 的 partition 可能位于 kafka 的不同 broker 上，所以 producer 需要明确的知道该 topic 下所有 partition 的元信息(即所在 broker 的 IP、端口等信息)，这样才能与 partition 所在 broker 建立网络连接并发送 message。</p>
<p>在 KafkaProducer 中，使用 Node、TopicPartition、PartitionInfo 三个类来记录 Kafka 集群元数据：</p>
<ul>
<li>Node 表示 kafka 集群中的一个节点，其中维护了节点的 host、ip、port 等基础信息。</li>
<li>TopicPartition 用来抽象一个 topic 中的的一个 partition，其中维护 topic 的名称以及 partition 的编号信息。</li>
<li>PartitionInfo 用来抽象一个 partition 的信息，其中：
<ul>
<li>leader 字段记录了 leader replica 所在节点的 id</li>
<li>replica 字段记录了全部 replica 所在的节点信息</li>
<li>inSyncReplicas 字段记录了ISR集合中所有replica 所在的节点信息。</li>
</ul>
</li>
</ul>
<p>kafka producer 会将上述三个维度的基础信息封装成 Cluster 对象使用，下面是 Cluster 包含的信息：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f43eefafc7a4d96a64f8003a0bbf274~tplv-k3u1fbpfcp-watermark.image" alt="5、Cluster截图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再向上一层，Cluster对象会被维护到Metadata中，Metadata同时还维护了Cluster的版本号、过期时间、监听器等等信息，如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f829eaca87d49ec8a9cadb6e74f317a~tplv-k3u1fbpfcp-watermark.image" alt="6、Metadata核心字段.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>经过上面的分析，我们可以得到下面这张简图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bea912a140e84ba2bafc8fa40625451c~tplv-k3u1fbpfcp-watermark.image" alt="7、元数据对应关系.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>静态数据结构分析完了之后，我们来看 KafkaProducer.waitOnMetadata()方法是如何工作的：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> ClusterAndWaitTime <span class="hljs-title">waitOnMetadata</span><span class="hljs-params">(String topic, Integer partition, <span class="hljs-keyword">long</span> nowMs, <span class="hljs-keyword">long</span> maxWaitMs)</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
    <span class="hljs-comment">// 获取MetadataCache当前缓存的Cluster对象</span>
    Cluster cluster = metadata.fetch();
    <span class="hljs-keyword">if</span> (cluster.invalidTopics().contains(topic))
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> InvalidTopicException(topic);
    <span class="hljs-comment">// 更新ProducerMetadata的缓存</span>
    metadata.add(topic, nowMs);

    <span class="hljs-comment">// 从partitionsByTopic集合中获取目标topic的partition数量</span>
    Integer partitionsCount = cluster.partitionCountForTopic(topic);
    <span class="hljs-comment">// 要是没有目标topic的元数据存在，则直接返回ClusterAndWaitTime对象，无需下面的更新操作</span>
    <span class="hljs-keyword">if</span> (partitionsCount != <span class="hljs-keyword">null</span> && (partition == <span class="hljs-keyword">null</span> || partition < partitionsCount))
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ClusterAndWaitTime(cluster, <span class="hljs-number">0</span>);

    <span class="hljs-keyword">long</span> remainingWaitMs = maxWaitMs;
    <span class="hljs-keyword">long</span> elapsed = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">do</span> &#123;
        <span class="hljs-comment">// 更新ProducerMetadata缓存</span>
        metadata.add(topic, nowMs + elapsed);
        <span class="hljs-comment">// 更新获取当前updateVersion，并设置相应标识，尽快触发元数据更新</span>
        <span class="hljs-keyword">int</span> version = metadata.requestUpdateForTopic(topic);
        <span class="hljs-comment">// 唤醒Sender线程，由Sender线程去完成元数据的更新</span>
        sender.wakeup();
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 阻塞等待元数据更新，停止阻塞的条件是：更新后的updateVersion大于当前version，超时的话会直接抛出异常</span>
            metadata.awaitUpdate(version, remainingWaitMs);
        &#125; <span class="hljs-keyword">catch</span> (TimeoutException ex) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> TimeoutException(。。。);
        &#125;
        cluster = metadata.fetch(); <span class="hljs-comment">// 获取最新的Cluster</span>
        elapsed = time.milliseconds() - nowMs;
        <span class="hljs-keyword">if</span> (elapsed >= maxWaitMs) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> TimeoutException(partitionsCount == <span class="hljs-keyword">null</span> ?
                    String.format(<span class="hljs-string">"Topic %s not present in metadata after %d ms."</span>,
                            topic, maxWaitMs) :
                    String.format(<span class="hljs-string">"Partition %d of topic %s with partition count %d is not present in metadata after %d ms."</span>,
                            partition, topic, partitionsCount, maxWaitMs));
        &#125;
        metadata.maybeThrowExceptionForTopic(topic);
        remainingWaitMs = maxWaitMs - elapsed; <span class="hljs-comment">// 计算元数据更新耗时</span>
        partitionsCount = cluster.partitionCountForTopic(topic); <span class="hljs-comment">// 获取partition数</span>
    &#125; <span class="hljs-keyword">while</span> (partitionsCount == <span class="hljs-keyword">null</span> || (partition != <span class="hljs-keyword">null</span> && partition >= partitionsCount));

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ClusterAndWaitTime(cluster, elapsed);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里具体如何更新元数据，我们将在介绍 Sender 线程工作流程的时候，详细分析。</p>
<h3 data-id="heading-5">序列化器</h3>
<p>分布式系统中各个节点相互通信，必然涉及到内存对象与字节流之间的转换，也就是序列化与反序列化。</p>
<p>kafka 中的序列化器接口是 Serializer，负责将对象转换成字节数组；反序列化器是 Deserializer 接口，负责将字节数组转换成内存中的对象。</p>
<p>下面展示了 Serializer 和 Deserializer 接口的实现类：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad7efbd13d3d4d9c872ad9ce64d6deba~tplv-k3u1fbpfcp-watermark.image" alt="9、Serializer接口.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad7efbd13d3d4d9c872ad9ce64d6deba~tplv-k3u1fbpfcp-watermark.image" alt="10、Deserializer接口.png" loading="lazy" referrerpolicy="no-referrer">
从上图中我们可以看出，kafka 自带了常用 Java 类型的 Serializer 实现和 Deserializer 实现，当然，我们也可以自定义Serializer和Deserializer实现来处理复杂类型。</p>
<p>下面我们以 StringSerializer 实现为例说明一下 Serializer 的核心实现：</p>
<ol>
<li>configure()方法是在执行序列化操作之前的配置，例如，在StringSerializer.configure()方法中会选择合适的编码类型（encoding），默认是UTF-8</li>
<li>serializer()方法是真正进行序列化的地方，将传入的Java对象序列化为byte[]。</li>
</ol>
<h3 data-id="heading-6">partition选择</h3>
<p>在 waitOnMetadata() 方法拿到最新的集群元数据之后，下面就要开始确定待发送的 message 要发送到哪个 partition 了。</p>
<p>如果我们明确指定了目标 partition，则以用户指定的为准，但是一般情况下，业务并不会指定 message 需要写入到哪个 partition，此时就会通过 Partitioner 结合 集群元数据计算出一个目标 partition。</p>
<p>下图展示了 Partitioner 接口的全部实现：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5413426d237244f69303d2548bac5c46~tplv-k3u1fbpfcp-watermark.image" alt="11、partitioner接口.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从名字也能看出，DefaultPartitioner 是默认实现，其中的 partition() 方法中：</p>
<ol>
<li>如果 message 存在的 key 的话，则取 key 的 hash 值（使用的是murmur2这种高效率低碰撞的Hash算法），然后与 partition 总数取模，得到目标 partition 编号，这样可以保证同一 key 的 message 进入同一 partition。</li>
<li>如果 message 没有 key，则通过 StickyPartitionCache.partition() 方法计算目标 partition。</li>
</ol>
<p>这里解释一下 StickyPartitionCache 的功能。我们前面介绍整个 KafkaProducer 流程的时候说过，RecordAccumulator 是一个缓冲区，主线程发送的 message 会先进入 RecordAccumulator，然后 Sender 线程攒够了 message 的时候进行批量发送。</p>
<p>触发 Sender 线程批量发送堆积 message 的条件主要有两方面：</p>
<ol>
<li>message 的延迟时间到了，也就是说，我们的业务场景对 message 发送有延迟要求，message 不能一直在 producer 端缓存。我们可以通过 linger.ms 配置降低 message 的发送延迟。</li>
<li>message 堆积的足够多，达到了一定阈值，才适合批量发送，这样有效负载较高。批量发送的 batch.size 默认值是 16KB。</li>
</ol>
<p>StickyPartitionCache 主要实现的是"黏性选择"，就是尽可能的先往一个 partition 发送 message，让发往这个 partition 的缓冲区快速填满，这样的话，就可以降低 message 的发送延迟。我们不用担心出现 partition 数据量不均衡的情况，因为只要业务运行时间足够长，message 还是会均匀的发送到每个 partition 上的。</p>
<p>下面来看 StickyPartitionCache 的实现，其中维护了一个 ConcurrentMap(indexCache字段)，key 是 topic，value 是当前黏住了哪个 partition。</p>
<p>在 partition() 方法中，StickyPartitionCache 会先从 indexCache 字段中获取黏住的 partition，如果没有，则调用 nextPartition() 方法向 indexCache 中写入一个。在 nextPartition() 方法中，会先获取目标 topic 中可用的 partition，并从中随机选择一个写入 indexCache。</p>
<p>最后，同学们可能问，什么时候更新黏住的 partition 呢？我们看一下 KafkaProducer.doSend()方法中，有这么一个片段：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 尝试向RecordAccumulator中追加message</span>
RecordAccumulator.RecordAppendResult result = accumulator.append(tp, timestamp, serializedKey,
            serializedValue, headers, interceptCallback, remainingWaitMs, <span class="hljs-keyword">true</span>, nowMs);
<span class="hljs-comment">// 由于目标partition的当前batch没有空间了，需要更换一个partition，再次尝试</span>
<span class="hljs-keyword">if</span> (result.abortForNewBatch) &#123;
    <span class="hljs-keyword">int</span> prevPartition = partition;
    <span class="hljs-comment">// 更换目标partition，同时也会更换StickyPartitionCache黏住的partition</span>
    partitioner.onNewBatch(record.topic(), cluster, prevPartition);
    <span class="hljs-comment">// 计算新的目标partition</span>
    partition = partition(record, serializedKey, serializedValue, cluster);
    tp = <span class="hljs-keyword">new</span> TopicPartition(record.topic(), partition);
    interceptCallback = <span class="hljs-keyword">new</span> InterceptorCallback<>(callback, <span class="hljs-keyword">this</span>.interceptors, tp);
    <span class="hljs-comment">// 再次调用append()方法向RecordAccumulator写入message，如果该partition缓冲区中的batch也没有空间，</span>
    <span class="hljs-comment">// 则创建新batch了，不会再次尝试了</span>
    result = accumulator.append(tp, timestamp, serializedKey,
        serializedValue, headers, interceptCallback, remainingWaitMs, <span class="hljs-keyword">false</span>, nowMs);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>RecordAccumulator.append()方法我们后面分析。</p>
<p>UniformStickyPartitioner 这个 Partitioner 底层也是依赖 StickyPartitionCache 实现黏性发送的，不再展开介绍。</p>
<p>再来看 RoundRobinPartitioner 实现，从名字也可以看出，它是按照轮训的策略来计算目标 partition，其中也维护了一个 ConcurrentMap 集合（topicCounterMap字段），其中的 key 是 topic 的名称，value 是一个递增的 AtomicInteger。</p>
<p>在 RoundRobinPartitioner.partition() 方法中，会先查找目标 topic 的 partition 总数，然后自增上述 AtomicInteger 值并与 partition 总数取模，得到目标 partition 的编号。</p>
<h2 data-id="heading-7">总结</h2>
<p>本课时我们首先介绍了 KafkaProducer 的基础使用，然后介绍了 KafkaProducer 的核心架构，最后介绍了 KafkaProducer.send() 方法中主线程的核心操作。</p>
<p>下一课时，我们将开始介绍 KafkaProducer 中 RecordAccumulator 相关的内容。</p>
<p>本课时的文章和视频讲解，还会放到：</p>
<ul>
<li>微信公众号：杨四正</li>
<li>B 站搜索：杨四正</li>
</ul></div>  
</div>
            