
---
title: 'Apache Pulsar 2.7.2 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7151'
author: 开源中国
comments: false
date: Sun, 30 May 2021 08:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7151'
---

<div>   
<div class="content">
                                                                    
                                                        <h1>关于 Apache Pulsar</h1> 
<p>Apache Pulsar 是 Apache 软件基金会顶级项目，是下一代云原生分布式消息流平台，集消息、存储、轻量化函数式计算为一体，采用计算与存储分离架构设计，支持多租户、持久化存储、多机房跨区域数据复制，具有强一致性、高吞吐、低延时及高可扩展性等流数据存储特性。 <br> GitHub 地址：http://github.com/apache/pulsar/</p> 
<p>在 Apache Pulsar 2.7.1 版本发布后的 2 个月，2021 年 5 月 13 日，Apache Pulsar 正式发布了 2.7.2 版本！</p> 
<p>Apache Pulsar 2.7.2 版本新增诸多优化改进，亮点包括优化了 consumer 功能（例如，在 Docker 环境中，多次接收到重试消息后，consumer 不会受到阻塞；使用 <code>Key_Shared</code> 订阅类型时，consumer 可以读取非持久化 topic 中的消息等）。另外，该版本还修复了大量漏洞，覆盖 Broker、Proxy、Pulsar admin、Pulsar SQL、Client、Function、Pulsar IO 和 Tiered Storage 等方面，进一步丰富和完善 Apache Pulsar 作为云原生流数据平台的能力。</p> 
<p>Apache Pulsar 2.7.2 版本总共接受了来自社区 38 位小伙伴的贡献，合并了约 85 个 commits，越来越多的小伙伴开始参与到 Pulsar 社区建设中，成为 contributor 的一员。不少代码和文档贡献来自于中国开发者，中国力量越发迅猛。</p> 
<p>以下为你详细解读 Apache Pulsar 2.7.2 版本重要的优化改进和漏洞修复。</p> 
<h1>bug 修复</h1> 
<p>本节主要介绍 Pulsar 2.7.2 在 broker、bookie、proxy、Pulsar admin、Pulsar SQL 和客户端方面实现的主要改进。</p> 
<h2>Broker</h2> 
<p>• PR-9763[1]：修复 PersistentReplicator 中的 NPE 和线程安全问题。</p> 
<p>旧版本的 PersistentReplicator 中可能会出现 NPE 问题，PR-9763 进行了更新：</p> 
<p>  •设置 <code>cursor</code> 字段为 <code>volatile</code>，因为该字段可以在其他线程中异步更新。 •移除 <code>openCursorAsync</code> 方法中的非必要的 <code>synchronization</code>。•在访问 <code>cursor</code> 字段前检查 Null，因为可能在 cursor 可用前更新统计信息。</p> 
<p>• PR-9826[2]：修复非持久订阅中 <code>Key_Shared</code> 订阅模式下未发送消息的问题。</p> 
<p>旧版本中，使用非持久 topic 时，在 topics 统计信息中显示消息已发送，但采用 <code>Key_Shared</code> 订阅模式的 consumer 无法消费这些消息（采用其他订阅模式的 consumer 可以正常消费消息）。PR-9826 修复了这一问题。</p> 
<p>• PR-10078[3]：修复接收重试消息后 consumer 被阻塞的问题。</p> 
<p>在 Docker 环境中使用旧版本 Pulsar 时，如果 consumer 启用重试功能并在 <code>DeadLetterPolicy</code> 中设置了重试 topic，consumer 会在多次收到重试消息后因为 <code>hasMessageAvaliable</code> 错误的检查导致阻塞。PR-10078 修复了这一问题。</p> 
<p>• PR-9853[4]：修复订阅不含 schema 的空 topic 时，无法添加 schema 的问题。</p> 
<p>旧版本 Pulsar 中，有 schema 的 consumer 订阅没有 schema 的空 topic 时，会使用 <code>isActive</code> 检查，但只检查是否可以删除 topic。实际上应该检查是否与有此 topic 连接的 producer 或 consumer。即使 topic 中没有活跃 producer 或 consumer，topic 订阅列表仍不为空，且 <code>isActive</code> 返回值为 <code>true</code>。Consumer 的 schema 无法 attach 到 topic 并返回 <code>IncompatibleSchemaException</code> 异常。</p> 
<p>PR-9853 实现了检查 topic 中是否有活跃 producer 或 consumer，而不是检查是否可以删除 topic。</p> 
<p>•PR-10367[5]：修复使用 <code>ALWAYS_COMPATIBLE</code> 策略时，检查 schema 类型的问题。使用 <code>ALWAYS_COMPATIBLE</code> 策略检查 schema 类型时，PR-10367 支持以下检查：•对于非传递策略，<code>ALWAYS_COMPATIBLE</code> 策略仅检查最后一个 schema 的类型。•对于传递策略，<code>ALWAYS_COMPATIBLE</code> 策略检查全部 schema 的类型。•通过 schema 数据获取 schema 时，<code>ALWAYS_COMPATIBLE</code> 策略参考多个 schema 类型。</p> 
<p>•PR-10337[6]：修复删除命名空间时 CPU 占满的问题。</p> 
<p>使用旧版本 Pulsar 删除命名空间时，命名空间 <code>Policies</code> 被标记为已删除，触发 topic 上的 <code>onPoliciesUpdate</code> 参数。但在 <code>onPoliciesUpdate</code> 中读取了 ZooKeeper 上 <code>Policies</code> 节点中的数据，如 <code>checkReplicationAndRetryOnFailure</code>。由于已删除命名空间，ZooKeeper 节点可能已不存在，读取数据失败会触发无限重试，PR-10337 修复了这一问题。</p> 
<h2>Bookie</h2> 
<p>• PR-9621[7]：如果未定义 <code>BOOKIE_GC</code>，则退回到 <code>PULSAR_GC</code>。</p> 
<p>该 PR 指定在未定义 <code>BOOKIE_GC</code>时，<code>PULSAR_MEM</code> 退回到 <code>PULSAR_GC</code>。</p> 
<p>•PR-10397[8]：如果未定义 <code>BOOKIE_EXTRA_OPTS</code>，则退回到 <code>PULSAR_EXTRA_OPTS</code>。</p> 
<p>PR-10397 定义在设置 <code>PULSAR_EXTRA_OPTS</code> 或 <code>BOOKIE_EXTRA_OPTS</code> 时，与 <code>PULSAR_EXTRA_OPTS</code> 行为一致，即不传递 <code>-Dio.netty.* system</code> 属性，避免属性重复。该 PR 还定义在未设置 <code>BOOKIE_EXTRA_OPTS</code> 时，添加 <code>-Dio.netty.leakDetectionLevel=disabled</code>，默认情况下 <code>PULSAR_EXTRA_OPTS</code> 不包括该设置。</p> 
<h2>Proxy</h2> 
<p>•PR-10226[9]：修复使用 proxy 和 <code>Prefix</code> 订阅认证模式时的授权错误。在旧版本 Pulsar 中使用 Pulsar proxy 和 <code>Prefix</code> 订阅认证模式时，<code>org.apache.pulsar.broker.authorization.PulsarAuthorizationProvider#canConsumeAsync</code>会抛出异常，引发 consumer 错误。</p> 
<p>PR-10226 更新了 <code>org.apache.pulsar.broker.authorization.PulsarAuthorizationProvider#allowTopicOperationAsync</code>逻辑，首先检查 <code>isSuperUser</code>，再返回 <code>isAuthorizedFuture</code>。</p> 
<h2>Pulsar admin</h2> 
<p>•PR-9975[10]：为 REST API、pulsar-admin 和 Pulsar 客户端添加 <code>get version</code> 命令。</p> 
<h2>Pulsar SQL</h2> 
<p>•PR-9910[11]：修复 <code>BKNoSuchLedgerExistsException</code> 问题。</p> 
<p>使用旧版本 Pulsar SQL 查询消息时，修改 ZooKeeper ledger 根目录会引发 <code>BKNoSuchLedgerExistsException</code> 异常。PR-9910 修复了这一问题。</p> 
<h2>Client</h2> 
<p>Pulsar 2.7.2 为 Java、Python、C++ 和 WebSocket 客户端进行了如下更新。</p> 
<h3>Java</h3> 
<p>•PR-10091[12]：修复 ClientConfigurationData 对象不平等的问题。</p> 
<p>该 PR 修复了这一问题，并且默认使用已有的 <code>AuthenticationDisabled.INSTANCE</code> 参数，而非创建新参数。</p> 
<p>•PR-10089[13]：修复 AutoConsumeSchema KeyValue 编码问题。</p> 
<p>该 PR 保证在自动消费 KeyValue schema 时，保留 KeyValueEncodingType。</p> 
<p>•PR-9981[14]：修复在使用 <code>KeyValue<GenericRecord, GenericRecord></code> 时出现的 <code>OutOfMemoryError</code> 错误。</p> 
<p>由于 <code>HttpLookupService</code> schema 编码的问题，旧版本 Pulsar 不支持消费使用 <code>KeyValue<GenericRecord, GenericRecord></code>schema 的 topic。<code>HttpLookupService</code> 会以 JSON 格式下载 schema，但 <code>KeyValue</code> schema 应以二进制形式编码。</p> 
<p>该 PR 使用现有 function 将 JSON 格式的 <code>KeyValue</code> schema 转换为所需格式。</p> 
<p>•PR-10436[15]：修复客户端在处理 producer epoch 时出现的并发问题。</p> 
<p>该 PR 使用 volatile 字段来增加 epoch 和 <code>AtomicLongFieldUpdater</code> 的值。</p> 
<p>•PR-8979[16]：在收到对已关闭 producer 的 ACK 时，处理 NPE。•PR-9855[17]：修复从字节数组反序列化时，未设置批处理大小的问题。</p> 
<p>旧版本 Pulsar 将批索引消息 ACK 添加到 seek 方法中，支持使用 ACK 集实现更高精度的查找。但在使用序列化或反序列化的消息进行 seek 时，<code>batchSize</code> 值为 0，导致 seek 之前的传入 messageId 和 seek 之后返回的 messageId 不同。PR-9855 修复了这一问题。</p> 
<p>•PR-9849[18]：修复无法关闭单 topic consumer 的问题。</p> 
<h3>Python</h3> 
<p>•PR-10265[19]：支持为 Python Avro schema 设置默认值。</p> 
<p>旧版本 Pulsar 不支持为 Python Avro schema 自定义默认值，导致无法更新 Python schema。</p> 
<p>该 PR 解决了这一问题，并添加了以下更新：</p> 
<p>•添加 <code>required</code> 字段限制可以设置为 <code>null</code> 的 schema 类型。•添加 <code>required_default</code> 字段，用于确认 schema 是否具有默认属性。•添加 <code>default</code> 字段，存储 schema 的默认值。</p> 
<p><br> •PR-9548[20]：修复 schema 中嵌套 <code>Map</code> 或 <code>Array</code> 无效的问题。</p> 
<p>旧版本 Pulsar 的 Python 客户端无法很好地处理内嵌 <code>Map</code> 或 <code>Array</code>，导致生成的 schema 字符串无效，因为当 <code>Map/Array</code> 的 <code>schema()</code> 方法为 schema 字符串设置 <code>values</code> 时，仅忽略 <code>Record</code> 类型（不会忽略 <code>Map</code> 和 <code>Array</code>）。</p> 
<p>此 PR 修复了这一问题，并且为 <code>Map<Map></code>、<code>Map<Array></code>、<code>Array<Array></code>和 <code>Array<Map></code> 分别添加了测试，保证测试的全面性。</p> 
<p>•PR-8957[21]：为 Python 和 C++ 客户端增加 TLS SNI 支持。</p> 
<p>该 PR 为 Python 和 C++ 客户端添加了 TLS SNI 支持，用户可以通过 proxy 连接到 broker。</p> 
<h3>C++</h3> 
<p>•PR-10363[22]：修复无法在 Windows 系统搭建 C++ 客户端的问题。</p> 
<p>该 PR 将 <code>PULSAR_PUBLIC</code> 放在变量类型前，并将 <code>LIB_NAME</code> 作为共享库的名称（如删除 dll 后缀）。</p> 
<p>•PR-10036[23]：修复暂停消费的零队列 consumer 预读取消息的问题。</p> 
<p>使用旧版本 Pulsar 时，在调用 <code>pauseMessageListener</code> 后，零队列 consumer（consumer 的接收队列大小为 0）会预读取消息。因为 <code>ConsumerImpl::increaseAvailablePermits</code>没有检查 <code>messageListenerRunning_</code> 这一布尔变量，在调用 <code>pauseMessageListener</code>后，<code>messageListenerRunning_</code> 值变为 <code>false</code>，因此当零队列 consumer 暂停消费时，仍继续发送 FLOW 命令，预读取消息到内部无限长度队列 <code>incomingMessages_</code>中。</p> 
<p>这一行为可能导致某些消息看似丢失，例如，某存储 10 条消息的 topic 启动一个共享 consumer，消费 3 条消息后，暂停消费行为。当对同一订阅启动新的共享 consumer 时，由于第 4 条消息已缓存在先前的 consumer 中，新 consumer 从第 5 条消息开始读取。</p> 
<p>PR-10036 修复了这一问题，同时合并了以下修改：</p> 
<p>•为 <code>increaseAvailablePermits</code> 方法添加 <code>messageListenerRunning_</code> 检查，使此实现与 Java 客户端的 <code>ConsumerImpl#increaseAvailablePermits</code> 一致。将 <code>availablePermits_</code> 的类型修改为 <code>std::atomic_int</code>。•为 <code>resumeMessageListener</code> 增加 <code>increaseAvailablePermits</code> 调用。由于 <code>pauseMessageListener</code> 不再预读取消息，所以需要 consumer 在恢复后发送 FLOW 命令。</p> 
<p> </p> 
<p>•PR-10006[24]：修复当通过接收到的消息 ID 获取 topic 名称时，出现 segmentation 错误的问题。</p> 
<p>旧版本 Pulsar C++ 客户端支持通过接收到的消息或其 ID 获取 topic 名称，但如果 consumer 订阅了非分区 topic，则在使用消息 ID 获取 topic 名称时会出现 segmentation 错误。</p> 
<p>此 PR 合并的修改保证当 consumer 接收到新的批处理消息时，对所有消息使用 <code>setTopicName</code> 方法设置对应的 topic 名字，并为所有类型的 consumer 增加相关测试（包括 <code>ConsumerImpl</code>、<code>MultiTopicsConsumerImpl</code>和 <code>PartitionedConsumerImpl</code>）。</p> 
<p>•PR-9702[25]：修复 <code>SinglePartitionMessageRouter</code> 一直选择同一个分区的问题。</p> 
<p><code>SinglePartitionMessageRouter</code> 参数应该为 producer 随机选择一个分区并且仅使用此分区。但是 C 语言中的 <code>rand()</code> 调用仅使用 seed 0，导致多个进程始终只使用同一分区。此 PR 解决了这一问题。</p> 
<p>•PR-10094[26]：降低 ack 分组追踪器的日志级别。</p> 
<p>使用旧版本 Pulsar 时，如果 ack 分组追踪器在连接关闭后发送 ack，则返回警告日志。此 PR 的修改保证了当连接不支持 <code>AckGroupingTrackerEnabled::flush</code> 参数时，将日志级别更改为调试。</p> 
<h3>WebSocket</h3> 
<p>•PR-10187[27]：优化 URL token 参数值。</p> 
<p>此 PR 移除了 WebSocket URL token 参数值的 <code>Bearer</code> 前缀。</p> 
<p>•PR-9886[28]：为浏览器客户端增加 token 认证。</p> 
<p>旧版本 Pulsar WebSocket 客户端使用 HTTP 请求 header 传递验证参数，但浏览器 JavaScript WebSocket 客户端无法添加新 header。</p> 
<p>此 PR 使用查询参数 token 为浏览器 JavaScript WebSocket 客户端传递验证 token，解决了这一问题。</p> 
<h2>Function 和 connector</h2> 
<p>•PR-10389[29]：支持自定义 function 日志。</p> 
<p>Pulsar 原本在 jar 包中进行 function 日志配置，因此不支持自定义值。</p> 
<p>此 PR 将 function 日志配置文件转存在配置文件夹中，实现自定义 function 日志。</p> 
<p>•PR-9943[30]：支持从 Pulsar 资源传递记录属性。•PR-10160[31]：修改 Pulsar Go Functions 中的时间单位。</p> 
<p>此 PR 将进程的平均延迟时间单位从纳秒（ns）改为毫秒（ms）。</p> 
<p>•PR-10420[32]：修复 Kinesis sink 不能重试发送消息的问题。</p> 
<p>使用旧版本 Pulsar 时，Kinesis sink connector 发送消息失败后不会重试，但会启用 <code>retainOrdering</code>，中断后续消息的发送。此 PR 为 Kinesis sink connector 增加了重试逻辑，当消息发送失败后，自动重试发送。</p> 
<p>•PR-10416[33]：修复 Kinesis sink onFailure 异常中的 Null 错误消息问题。</p> 
<p>旧版本 Pulsar 中，如果 Kinesis producer 发送消息失败，<code>onFailure</code> 异常中的错误消息为 null。此 PR 提取 <code>UserRecordFailedException</code> 信息并保存实际错误消息。</p> 
<h2>Tiered storage</h2> 
<h2>分层存储</h2> 
<p>•PR-9878[34]：避免类 offloader 泄漏，恢复 offloader 目录的覆盖写入功能。</p> 
<p>旧版本 Pulsar 存在类 offloader泄露问题。此 PR 为 <code>PulsarService</code> 类和 <code>PulsarConnectorCache</code> 类使用从目录字符串到 offloader 的映射。</p> 
<p>•PR-9852[35]：为清理已卸载数据操作增加日志。</p> 
<p>旧版本 Pulsar 中，没有用于存储清理已卸载数据操作的日志，用户难以分析分层存储中数据丢失的原因。此 PR 为清理卸载数据的操作增加了日志，解决了这一问题。</p> 
<h1>参考信息</h1> 
<p>想上手试试 Apache Pulsar 2.7.2？在此<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpulsar.apache.org%2Fen%2Fdownload%2F" target="_blank">下载新版本</a>。完整版 Apache Pulsar 2.7.2 版本说明，参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpulsar.apache.org%2Fen%2Frelease-notes%2F" target="_blank">版本说明</a>。Apache Pulsar 2.7.2 PR 列表，参<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar%2Fpulls%3Fq%3Dis%253Apr%2Blabel%253Arelease%252F2.7.2%2Bis%253Aclosed" target="_blank">阅PR 列表</a>。</p> 
<p>期待你为 Pulsar 的发展添砖加瓦！</p>
                                        </div>
                                      
</div>
            