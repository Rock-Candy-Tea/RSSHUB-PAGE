
---
title: 'Kafka 3.0重磅发布，都更新了些啥？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/7326ad4f872b2fc805cbe252e8510fc8.jpg'
author: Dockone
comments: false
date: 2021-09-26 11:07:01
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/7326ad4f872b2fc805cbe252e8510fc8.jpg'
---

<div>   
<br>【编者的话】Apache Kafka 是一个分布式开源流平台，被广泛应用于各大互联网公司。<br>
<br>Kafka 设计之初被用于消息队列，自 2011 年由 LinkedIn 开源以来，Kafka 迅速从消息队列演变为成熟的事件流处理平台。<br>
<br>Kafka 具有四个核心 API，借助这些 API，Kafka 可以用于以下两大类应用：<br>
<ul><li>建立实时流数据管道，可靠地进行数据传输，在系统或应用程序之间获取数据。</li><li>构建实时流媒体应用程序，以改变系统或应用程序之间的数据或对数据流做出反应。  </li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/7326ad4f872b2fc805cbe252e8510fc8.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/7326ad4f872b2fc805cbe252e8510fc8.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
近日，Apache Kafka 3.0.0 正式发布，这是一个重要的版本更新，其中包括许多新的功能。<br>
<br>例如：<br><br>
<ul><li>已弃用对 Java 8 和 Scala 2.12 的支持，对它们的支持将在 4.0 版本中彻底移除，以让开发者有时间进行调整。</li><li>Kafka Raft 支持元数据主题的快照，以及 self-managed quorum 方面的其他改进。</li><li>废弃了消息格式 v0 和 v1。</li><li>默认情况下为 Kafka Producer 启用更强的交付保证。</li><li>优化了 OffsetFetch 和 FindCoordinator 请求。</li><li>更灵活的 MirrorMaker 2 配置和 MirrorMaker 1 的弃用。</li><li>能够在 Kafka Connect 的一次调用中重新启动连接器的任务。</li><li>连接器日志上下文和连接器客户端覆盖现在是默认启用的。</li><li>增强了 Kafka Streams 中时间戳同步的语义。</li><li>修改了 Stream 的 TaskId 的公共 API。</li><li>在 Kafka Streams 中，默认的 serde 变成了 null，还有一些其他的配置变化。</li></ul><br>
<br>接下来，我们来看看新版本具体在哪些地方进行了更新。根据官方资料介绍，Apache Kafka 3.0 引入了各种新功能、突破性的 API 更改以及对 KRaft 的改进——Apache Kafka 的内置共识机制将取代 Apache ZooKeeper™。  <br>
<br>虽然 KRaft 尚未被推荐用于生产（已知差距列表），但对 KRaft 元数据和 API 进行了许多改进。Exactly-once 和分区重新分配支持值得强调。鼓励大家查看 KRaft 的新功能并在开发环境中试用它。<br>
<br>从 Apache Kafka 3.0 开始，生产者默认启用最强的交付保证（acks=all， enable.idempotence=true）。这意味着用户现在默认获得排序和持久性。<br>
<br>此外，不要错过 Kafka Connect 任务重启增强、KStreams 基于时间戳同步的改进以及 MirrorMaker2 更灵活的配置选项。<br>
<h3>常规变化</h3><h4>KIP-750（第一部分）：弃用 Kafka 中对 Java 8 的支持</h4>在 3.0 中，Apache Kafka 项目的所有组件都已弃用对 Java 8 的支持。这将使用户有时间在下一个主要版本（4.0）之前进行调整，届时 Java 8 支持将被取消。<br>
<h4>KIP-751（第一部分）：弃用 Kafka 中对 Scala 2.12 的支持</h4>对 Scala 2.12 的支持在 Apache Kafka 3.0 中也已弃用。与 Java 8 一样，我们给用户时间来适应，因为计划在下一个主要版本（4.0）中删除对 Scala 2.12 的支持。<br>
<h3>Kafka 代理、生产者、消费者和管理客户端</h3><h4>KIP-630：Kafka Raft 快照</h4>我们在 3.0 中引入的一个主要功能是 KRaft 控制器和 KRaft 代理能够为名为 __cluster_metadata 的元数据主题分区生成、复制和加载快照。<br>
<br>Kafka 集群使用此主题来存储和复制有关集群的元数据信息，如代理配置、主题分区分配、领导等。<br>
<br>随着此状态的增长，Kafka Raft Snapshot 提供了一种有效的方式来存储、加载和复制此信息。<br>
<h4>KIP-746：修改 KRaft 元数据记录</h4>自第一版 Kafka Raft 控制器以来的经验和持续开发表明，需要修改一些元数据记录类型，当 Kafka 被配置为在没有 ZooKeeper（ZK）的情况下运行时使用这些记录类型。<br>
<h4>KIP-730：KRaft 模式下的生产者 ID 生成</h4>在 3.0 和 KIP-730 中，Kafka 控制器现在完全接管了生成 Kafka 生产者 ID 的责任。<br>
<br>控制器在 ZK 和 KRaft 模式下都这样做。这让我们更接近桥接版本，这将允许用户从使用 ZK 的 Kafka 部署过渡到使用 KRaft 的新部署。<br>
<h4>KIP-679：Producer 将默认启用最强的交付保证</h4>从 3.0 开始，Kafka 生产者默认开启幂等性和所有副本的交付确认。这使得默认情况下记录交付保证更强。<br>
<h4>KIP-735：增加默认消费者会话超时</h4>Kafka Consumer 的配置属性的默认值 session.timeout.ms 从 10 秒增加到 45 秒。<br>
<br>这将允许消费者在默认情况下更好地适应暂时的网络故障，并在消费者似乎只是暂时离开组时避免连续重新平衡。<br>
<h4>KIP-709：扩展 OffsetFetch 请求以接受多个组 ID</h4>请求 Kafka 消费者组的当前偏移量已经有一段时间了。但是获取多个消费者组的偏移量需要对每个组进行单独的请求。<br>
<br>在 3.0 和 KIP-709 中，fetch 和 AdminClient API 被扩展为支持在单个请求/响应中同时读取多个消费者组的偏移量。<br>
<h4>KIP-699：更新 FindCoordinator 以一次解析多个 Coordinator</h4>支持可以以有效方式同时应用于多个消费者组的操作在很大程度上取决于客户端有效发现这些组的协调者的能力。<br>
<br>这通过 KIP-699 成为可能，它增加了对通过一个请求发现多个组的协调器的支持。<br>
<br>Kafka 客户端已更新为在与支持此请求的新 Kafka 代理交谈时使用此优化。<br>
<h4>KIP-724：删除对消息格式 v0 和 v1 的支持</h4>自 2017 年 6 月随 Kafka 0.11.0 推出四年以来，消息格式 v2 一直是默认消息格式。<br>
<br>因此，在桥下流过足够多的水（或溪流）后，3.0 的主要版本为我们提供了弃用旧消息格式（即 v0 和 v1）的好机会。<br>
<br>这些格式今天很少使用。在 3.0 中，如果用户将代理配置为使用消息格式 v0 或 v1，他们将收到警告。<br>
<br>此选项将在 Kafka 4.0 中删除（有关详细信息和弃用 v0 和 v1 消息格式的影响，请参阅 KIP-724）。<br>
<h4>KIP-707：KafkaFuture 的未来</h4>当 KafkaFuture 引入该类型以促进 Kafka AdminClient 的实现时，Java 8 之前的版本仍在广泛使用，并且 Kafka 正式支持 Java 7。<br>
<br>快进几年后，现在 Kafka 运行在支持CompletionStage和 CompletableFuture 类类型的 Java 版本上。<br>
<br>使用 KIP-707，KafkaFuture 添加了一种返回 CompletionStage 对象的方法，并以 KafkaFuture 向后兼容的方式增强了可用性。<br>
<h4>KIP-466：添加对 List<T> 序列化和反序列化的支持</h4>KIP-466为泛型列表的序列化和反序列化添加了新的类和方法——这一特性对 Kafka 客户端和 Kafka Streams 都非常有用。<br>
<h4>KIP-734：改进 AdminClient.listOffsets 以返回时间戳和具有最大时间戳的记录的偏移量</h4>用户列出 Kafka 主题/分区偏移量的功能已得到扩展。使用 KIP-734，用户现在可以要求 AdminClient 返回主题/分区中具有最高时间戳的记录的偏移量和时间戳。<br>
<br>这是不是与什么的 AdminClient 收益已经为最新的偏移，这是下一个记录的偏移，在主题/分区写入混淆。<br>
<br>这个扩展现有 ListOffsets API 允许用户探测生动活泼的通过询问哪个是最近写入的记录的偏移量以及它的时间戳是什么来分区。<br>
<h3>Kafka Connect</h3><h4>KIP-745：连接 API 以重新启动连接器和任务</h4>在 Kafka Connect 中，连接器在运行时表示为一组Connector类实例和一个或多个Task类实例，并且通过 Connect REST API 可用的连接器上的大多数操作都可以应用于整个组。<br>
<br>从一开始，一个值得注意的例外 restart 是 Connector 和 Task 实例的端点。要重新启动整个连接器，用户必须单独调用以重新启动连接器实例和任务实例。<br>
<br>在 3.0 中，KIP-745 使用户能够通过一次调用重新启动所有或仅失败的连接器 Connector 和 Task 实例。此功能是附加功能，restartREST API 的先前行为保持不变。<br>
<h4>KIP-738：删除 Connect 的内部转换器属性</h4>在之前的主版本（Apache Kafka 2.0）中弃用它们之后，internal.key.converter 并 internal.value.converter 在 Connect 工作器的配置中作为配置属性和前缀被删除。<br>
<br>展望未来，内部 Connect 主题将专门使用 JsonConverter 来存储没有嵌入模式的记录。<br>
<br>任何使用不同转换器的现有 Connect 集群都必须将其内部主题移植到新格式（有关升级路径的详细信息，请参阅 KIP-738）。<br>
<h4>KIP-722：默认启用连接器客户端覆盖</h4>从 Apache Kafka 2.3.0 开始，可以配置连接器工作器以允许连接器配置覆盖连接器使用的 Kafka 客户端属性。<br>
<br>这是一个广泛使用的功能，现在有机会发布一个主要版本，默认启用覆盖连接器客户端属性的功能（默认 connector.client.config.override.policy 设置为 All）。<br>
<h4>KIP-721：在连接 Log4j 配置中启用连接器日志上下文</h4>另一个在 2.3.0 中引入但到目前为止尚未默认启用的功能是连接器日志上下文。这在 3.0 中发生了变化，连接器上下文默认添加 Log4j 到 Connect 工作器的日志模式中。<br>
<br>从以前的版本升级到 3.0 将 log4j 通过在适当的情况下添加连接器上下文来更改导出的日志行的格式。<br>
<h3>Kafka Streams</h3><h4>KIP-695：进一步改进 Kafka Streams 时间戳同步</h4>KIP-695 增强了 Streams 任务如何选择获取记录的语义，并扩展了配置属性的含义和可用值 max.task.idle.ms。<br>
<br>此更改需要 Kafka 消费者 API 中的一种新方法，currentLag 如果本地已知且无需联系 Kafka Broker，则能够返回特定分区的消费者滞后。<br>
<h4>KIP-715：在流中公开提交的偏移量</h4>3.0 开始，三个新的方法添加到 TaskMetadata 接口：committedOffsets，endOffsets 和 timeCurrentIdlingStarted。这些方法可以允许 Streams 应用程序跟踪其任务的进度和运行状况。<br>
<h4>KIP-740：清理公共 API TaskId</h4>KIP-740 代表了 TaskId 该类的重大革新。有几种方法和所有内部字段已被弃用，新的 subtopology() 和 partition() 干将替换旧 topicGroupId 和 partition 字段（参见 KIP-744 的相关变化和修正 KIP-740）。<br>
<h4>KIP-744：迁移 TaskMetadata，并 ThreadMetadata 与内部实现的接口</h4>KIP-744 将 KIP-740 提出的更改更进一步，并将实现与许多类的公共 API 分开。<br>
<br>为了实现这一点，引入了新的接口 TaskMetadata、ThreadMetadata 和 StreamsMetadata，而弃用了具有相同名称的现有类。<br>
<h4>KIP-666：添加 Instant 基于方法到 ReadOnlySessionStore</h4>交互式查询 API 扩展了 ReadOnlySessionStore 和 SessionStore 接口中的一组新方法，这些方法接受 Instant 数据类型的参数。此更改将影响需要实现新方法的任何自定义只读交互式查询会话存储实现。<br>
<h4>KIP-622：添加 currentSystemTimeMs 和 currentStreamTimeMs 到 ProcessorContext</h4>该 ProcessorContext 增加在 3.0 两个新的方法，currentSystemTimeMs 和 currentStreamTimeMs。<br>
<br>新方法使用户能够分别查询缓存的系统时间和流时间，并且可以在生产和测试代码中以统一的方式使用它们。<br>
<h4>KIP-743：删除 0.10.0-2.4Streams 内置指标版本配置的配置值</h4>3.0 中取消了对 Streams 中内置指标的旧指标结构的支持。KIP-743 正在 0.10.0-2.4 从配置属性中删除该值 built.in.metrics.version。<br>
<br>这 latest 是目前此属性的唯一有效值（自 2.5 以来一直是默认值）。<br>
<h4>KIP-741：将默认 SerDe 更改为 null</h4>删除了默认 SerDe 属性的先前默认值。流过去默认为 ByteArraySerde。<br>
<br>用 3.0 开始，没有缺省，和用户需要任一组其的 SerDes 根据需要在 API 中或通过设置默认 DEFAULT_KEY_SERDE_CLASS_CONFIG 和 DEFAULT_VALUE_SERDE_CLASS_CONFIG 在它们的流配置。<br>
<br>先前的默认值几乎总是不适用于实际应用程序，并且造成的混乱多于方便。<br>
<h4>KIP-733：更改 Kafka Streams 默认复制因子配置</h4>有了主要版本的机会，Streams 配置属性的默认值 replication.factor 会从 1 更改为 -1。<br>
<br>这将允许新的 Streams 应用程序使用在 Kafka 代理中定义的默认复制因子，因此在它们转移到生产时不需要设置此配置值。请注意，新的默认值需要 Kafka Brokers 2.5 或更高版本。<br>
<h4>KIP-732：弃用 eos-alpha 并用 eos-v2 替换 eos-beta</h4>在 3.0 中不推荐使用的另一个 Streams 配置值是 exactly_once 作为属性的值 processing.guarantee。<br>
<br>该值 exactly_once 对应于 Exactly Once Semantics（EOS）的原始实现，可用于连接到 Kafka 集群版本 0.11.0 或更高版本的任何 Streams 应用程序。<br>
<br>此 EOS 的第一实现已经通过流第二实施 EOS 的，这是由值表示取代 exactly_once_beta 在 processing.guarantee 性质。<br>
<br>展望未来，该名称 exactly_once_beta 也已弃用并替换为新名称 exactly_once_v2。<br>
<br>在下一个主要版本（4.0）中，exactly_once 和 exactly_once_beta 都将被删除，exactly_once_v2 作为 EOS 交付保证的唯一选项。<br>
<h4>KIP-725：优化 WindowedSerializer 和 WindowedDeserializer 的配置</h4>配置属性 default.windowed.key.serde.inner 和 default.windowed.value.serde.inner 已弃用。<br>
<br>取而代之的是 windowed.inner.class.serde 供消费者客户端使用的单个新属性。<br>
<br>建议 Kafka Streams 用户通过将其传递到 SerDe 构造函数来配置他们的窗口化 SerDe，然后在拓扑中使用它的任何地方提供 SerDe。<br>
<h4>KIP-633：弃用 Streams 中宽限期的 24 小时默认值</h4>在 Kafka Streams 中，允许窗口操作根据称为宽限期的配置属性处理窗口外的记录。<br>
<br>以前，这个配置是可选的，很容易错过，导致默认为 24 小时。这是 Suppression 运营商用户经常感到困惑的原因，因为它会缓冲记录直到宽限期结束，因此会增加 24 小时的延迟。<br>
<br>在 3.0 中，Windows 类通过工厂方法得到增强，这些工厂方法要求它们使用自定义宽限期或根本没有宽限期来构造。已弃用默认宽限期为 24 小时的旧工厂方法，以及与 grace() 已设置此配置的新工厂方法不兼容的相应 API。<br>
<h4>KIP-623：internal-topics 为流应用程序重置工具添加“ ”选项</h4>通过 kafka-streams-application-reset 添加新的命令行参数，应用程序重置工具的 Streams 使用变得更加灵活：--internal-topics。<br>
<br>新参数接受逗号分隔的主题名称列表，这些名称对应于可以使用此应用程序工具安排删除的内部主题。<br>
<br>将此新参数与现有参数相结合，--dry-run 允许用户在实际执行删除操作之前确认将删除哪些主题并在必要时指定它们的子集。<br>
<h3>MirrorMaker</h3><h4>KIP-720：弃用 MirrorMaker v1</h4>在 3.0 中，不推荐使用 MirrorMaker 的第一个版本。展望未来，新功能的开发和重大改进将集中在 MirrorMaker 2（MM2）上。<br>
<h4>KIP-716：允许使用 MirrorMaker2 配置偏移同步主题的位置</h4>在 3.0 中，用户现在可以配置 MirrorMaker2 创建和存储用于转换消费者组偏移量的内部主题的位置。<br>
<br>这将允许 MirrorMaker2 的用户将源 Kafka 集群维护为严格只读的集群，并使用不同的 Kafka 集群来存储偏移记录（即目标 Kafka 集群，甚至是源和目标集群之外的第三个集群）。<br>
<br>Apache Kafka 3.0 是 Apache Kafka 项目向前迈出的重要一步。<br>
<br>更多详情可查看：<a href="https://blogs.apache.org/kafka" rel="nofollow" target="_blank">https://blogs.apache.org/kafka</a><br>
<br>出处：内容来源于OSC开源社区（ID：oschina2013）、Flink（ID：Apache_Flink）
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            