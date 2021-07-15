
---
title: 'Pulsar 2.8.0 新增特性概览：独占 Producer、事务等'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1635'
author: 开源中国
comments: false
date: Thu, 15 Jul 2021 19:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1635'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <h3><strong>关于 Apache Pulsar</strong></h3> 
 <p>Apache Pulsar 是 Apache 软件基金会顶级项目，是集消息、存储、轻量化函数式计算为一体的下一代云原生分布式消息流平台，采用了计算与存储分离架构设计，支持多租户、持久化存储、多机房跨区域数据复制，具有强一致性、高吞吐、低延时及高可扩展性等流数据存储特性。<br> GitHub 地址：http://github.com/apache/pulsar/</p> 
</blockquote> 
<blockquote> 
 <p>转载与作者信息：<br> 本文翻译自 StreamNative 博客，原作者 Matteo Merli、郭斯杰。原文地址：https://streamnative.io/en/blog/release/2021-06-15-apache-pulsar-launches-2-8-unified-messaging-and-streaming-with-transactions</p> 
</blockquote> 
<h3><strong>导语</strong></h3> 
<p>Apache Pulsar 2.8.0 版本正式发布，新版本中新增许多社区期待的性能优化与新功能。本篇博客深入探讨了 2.8.0 版本的更新。下面一起来看看吧！</p> 
<blockquote> 
 <p>备注：一般而言，Pulsar 每 3 个月发布一次大版本。由于 2.8.0 在开发事务 API 时投入了较多时间和精力，在 2.7.0 发布后的 6 个月，2.8.0 正式发布。</p> 
</blockquote> 
<h3><strong>2.8.0 版本更新概述</strong></h3> 
<p>新版本中的主要功能和更新如下：</p> 
<ul> 
 <li>独占 Producer；</li> 
 <li>包管理 API；</li> 
 <li>简化的客户端内存限制设置；</li> 
 <li>Broker Entry Metadata；</li> 
 <li>新 Protobuf 代码生成器；</li> 
 <li>事务</li> 
</ul> 
<h4><strong>独占 Producer</strong></h4> 
<h4>默认情况下，Pulsar producer API 提供 “ 多 writer” 语义来将消息写入到 topic。但是，部分场景需要单个 writer 的独占访问权限，例如确保消息的非交错的线性历史或提供 leader 选举机制。</h4> 
<p>这个新功能允许应用程序请求访问独占producer，以实现 “单个 writer”。它保证在任何状况下都应该只有 1 个 writer。如果 producer 失去其独占访问权，则无法在该 topic 上发布更多消息。</p> 
<p>此功能的一个用例是 Pulsar Functions 中的元数据控制器。为了编写所有 functions 元数据更新的单一线性历史（single linear history），元数据控制器需要选举一个 leader，并且这个 leader 做出的所有 “决策” 都写在元数据的 topic 上。通过利用独占 producer 功能，Pulsar 保证每个连续的 leader 上，都有元数据 topic 包含的不同的片段更新，并且不同 leader 之间没有交错。有关更多详细信息，请参阅 PIP-68: Exclusive Producer[1]。</p> 
<h4><strong>包管理 API</strong></h4> 
<p>自从在 2.0 版本中引入 Pulsar Functions 以来，该功能就备受欢迎。在新版本中，我们在其优势的基础上优化了用户体验。在旧版本中，如果一个 function 被多次部署，则 function 包会被多次上传；此外，Pulsar 中没有针对 Functions 和 IO connerctor 的版本管理。新引入的包管理 API 提供更简单管理 Functions 和 IO connerctor 包的方法，并显著简化了升级和回滚过程。阅读 Package Management API[2] 以获取更多详细信息。</p> 
<h4><strong>简化的客户端内存限制设置</strong></h4> 
<h4>在 2.8.0 版本之前，producer 和 consumer 中有多个设置可以控制内部消息队列的大小。这些设置最终控制了 Pulsar 客户端使用的内存量。但是，这种方法存在个别问题使得选择控制内存总使用量的整体配置复杂。</h4> 
<p>举例来说，由于这些设置基于“消息数量”，必须针对每个 producer 或 consumer 调整预期的消息大小。如果应用程序有大量（或未知）数量的 producer 或 consumer，则很难为队列大小选择合适的值。具有许多分区的 topic 也存在这样的问题。</p> 
<p>在 2.8.0 中，我们引入了一个新的 API 来设置内存限制。此单一的 memoryLimit 设置指定给定 Pulsar 客户端上的最大内存量，producer 和 consumer 竞争分配的内存，以确保 Pulsar 客户端使用的内存不会超出设置的限制。阅读 PIP-74: Pulsar client memory limits[3] 了解详情。</p> 
<h4><strong>Broker Entry Metadata</strong></h4> 
<h4>Pulsar 消息定义了一组非常全面的元数据属性。但是，要添加新属性，必须更改 Pulsar 协议中的 <code>MessageMetadata</code> 定义以通知 broker 和客户端新引入的属性。</h4> 
<p>但在某些情况下，可能需要从 broker 端添加元数据属性，或者需要由 broker 以非常低的成本检索。为了防止属性在消息元数据中被反序列化，我们在 2.8.0 中引入了“Broker Entry Metadata”，以提供一种轻量级的方法来添加额外的元数据属性，而无需序列化和反序列化 protobuf 编码的 <code>MessageMetadata</code>。</p> 
<p>此特性为 Pulsar 解锁了一组新功能。例如，我们可以通过 broker entry metadata 为附加到 Pulsar topic 的消息生成 broker 发布时间；也可以为 Pulsar topic 的消息生成单调递增的序列 ID。我们也在 Kafka-on-Pulsar(KoP) 中使用这个特性来实现 Kafka offset。</p> 
<h4><strong>新 Protobuf 代码生成器</strong></h4> 
<p>Pulsar 使用 Google Protobuf 来执行客户端和 broker 之间交换的命令的序列化和反序列化。由于常规 Protobuf 部署涉及的开销，我们一直在使用 Protobuf 2.4.1 的修改版本。修改是为了确保更高效的序列化代码，该代码将线程本地缓存用于进程中的使用对象。</p> 
<p>这种方法存在一些问题。例如，Protobuf 代码生成器的补丁仅基于 Protobuf 2.4.1 版本，无法升级到更新的 Protobuf 版本。在 2.8.0 中，我们将代码生成器从修改后的 Protobuf 2.4.1 切换为 Splunk LightProto。新的代码生成器可以为 Protobuf SerDe 尽可能快地生成 Java 代码，与 proto2 定义和 Pulsar 协议 100% 兼容，并使用 Netty ByteBuf 提供零拷贝反序列化。</p> 
<h4><strong>事务</strong></h4> 
<p>在 Pulsar 2.8.0 之前，Pulsar 仅通过幂等 Producer 支持单个 topic 的精确一次（ exactly-once）语义。虽然功能强大，但幂等 producer 只能解决 exactly-once 语义下的一小部分问题。例如，当 producer 尝试向多个 topic 生产消息时缺少 <code>原子性</code>。当为其中一个 topic 提供服务的 broker 崩溃时，可能会产生发布错误。如果 producer 不重试发布消息，则会导致一些消息被单次持久化并丢失其他消息；如果 producer 重试，则会导致一些消息被多次持久化。</p> 
<p>为了解决上述问题，我们引入 Pulsar 事务 API 来支持跨多个 topic 的原子写入和确认，从而加强了 Pulsar 的交付语义。将事务 API 添加到 Apache Pulsar 完成了我们将 Pulsar 打造为一个完整的统一消息和流平台的愿景。</p> 
<p>Pulsar PMC 成员、StreamNative 工程师团队负责人李鹏辉近期在博客<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUyMjkzMjA1Ng%3D%3D%26mid%3D2247488332%26idx%3D1%26sn%3Df1d1cc1c5edeff971ed67380845b7ea3%26scene%3D21%23wechat_redirect" target="_blank">基于 Pulsar 事务实现 Exactly-Once 语义</a>详细介绍了这个功能。点击链接可了解更多关于 Pulsar 中 exactly-once 语义支持的信息。</p> 
<h3><strong>更多信息</strong></h3> 
<ul> 
 <li>下载 Pulsar 2.8.0[4]。</li> 
 <li>了解更多新版本详情，参阅 2.8.0 release note[5]</li> 
 <li>观看视频[6]，深入了解 Pulsar 2.8.0。</li> 
</ul> 
<h4><strong>引用链接</strong></h4> 
<p><code>[1]</code> PIP-68: Exclusive Producer: <em>https://github.com/apache/pulsar/wiki/PIP-68%3A-Exclusive-Producer</em><br> <code>[2]</code> Package Management API: <em>http://pulsar.apache.org/docs/en/admin-api-packages/</em><br> <code>[3]</code> PIP-74: Pulsar client memory limits: <em>https://github.com/apache/pulsar/wiki/PIP-74%3A-Pulsar-client-memory-limits</em><br> <code>[4]</code> 下载 Pulsar 2.8.0: <em>https://pulsar.apache.org/en/versions/</em><br> <code>[5]</code> 2.8.0 release note: <em>https://pulsar.apache.org/release-notes/#2.8.0</em><br> <code>[6]</code> 视频: <em>https://www.bilibili.com/video/BV1zb4y1Q7gT</em></p>
                                        </div>
                                      
</div>
            