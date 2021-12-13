
---
title: 'Apache Hudi 0.10.0 版本重磅发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=109'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 10:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=109'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#3f3f3f; margin-left:8px; margin-right:8px">在发布的Apache Hudi 0.10.0版本中共解决了<strong style="color:#0f4c81">388个</strong>issue，包括众多重磅特性支持以及Bug修复。</p> 
<h2 style="margin-left:auto; margin-right:auto">1. 重点特性</h2> 
<h3 style="text-align:left">1.1 Kafka Connect（Kafka连接器）</h3> 
<p style="text-align:left">在0.10.0 中我们为 Hudi 添加了一个 <strong style="color:#0f4c81">Kafka Connect Sink</strong>，为用户提供了从 Apache Kafka 直接向 Hudi 表摄取/流式传输记录的能力。虽然用户已经可以使用 Deltastreamer/Spark/Flink 将 Kafka 记录流式传输到 Hudi 表中，但 Kafka Connect Sink为当前用户提供了好的灵活性，如果不部署和运维Spark/Flink的用户，也可以通过Kafka Connect Sink将他们的数据写入数据湖。<strong style="color:#0f4c81">Kafka Connect</strong>目前处于实验阶段，用户可以参考<span style="color:#576b95">README-Hudi-Kafka-Connect[1]</span>的详细步骤快速上手，对内部实现感兴趣的用户可以参考<span style="color:#576b95">RFC-32_Kafka Connect Sink For Hudi[2]</span>。除了Kafka Connect外，Apache Pulsar和RocketMQ也都提供了直接将Pulsar和RocketMQ数据写入Hudi数据湖的能力扩展，并提供了对应的Hudi Connector，详情可参考<span style="color:#576b95">Pulsar-to-Hudi[3]</span>和<span style="color:#576b95">RocketMQ-to-Hudi[4]</span></p> 
<h3 style="text-align:left">1.2 Z-Ordering，Hilbert Curves 和 Data Skipping</h3> 
<p style="text-align:left">在 0.10.0 中支持基于空间填充曲线排序的索引，首先支持了 <span style="color:#576b95">Z-Ordering[5]</span>和 <span style="color:#576b95">Hilbert Curves[6]</span>。</p> 
<p style="text-align:left">数据跳过对于优化查询性能至关重要，通过启用包含单个数据文件的列级统计信息（如最小值、最大值、空值数等）的列统计索引，对于某些查询允许对不包含值的文件进行快速裁剪，而仅仅返回命中的文件，当数据按列全局排序时，数据跳过最有效，允许单个 Parquet 文件包含不相交的值范围，从而实现更有效的裁剪。</p> 
<p style="text-align:left">使用空间填充曲线（如 Z-order、Hilbert 等）允许基于包含多列的排序键有效地对表数据进行排序，同时保留非常重要的属性：在多列上使用空间填充曲线对行进行排序列键也将在其内部保留每个单独列的排序，在需要通过复杂的多列排序键对行进行排序的用例中，此属性非常方便，这些键需要通过键的任何子集（不一定是键前缀）进行有效查询，从而使空间填充曲线对于简单的线性（或字典序）多列排序性能更优。如果应用得当，在此类用例中使用空间填充曲线可能会显着减少搜索空间，从而大幅度提高查询性能。</p> 
<p style="text-align:left">这些功能目前处于实验阶段，我们计划很快在博客文章中深入研究更多细节，展示空间填充曲线的实际应用。</p> 
<h3 style="text-align:left">1.3 Debezium Deltastreamer数据源</h3> 
<p style="text-align:left">在0.10.0中我们在 Deltastreamer 生态系统中添加了两个新的 debezium 源，Debezium 是一个用于变更数据捕获 (CDC) 的开源分布式平台。我们添加了 <strong style="color:#0f4c81">PostgresDebeziumSource</strong> 和 <strong style="color:#0f4c81">MysqlDebeziumSource</strong> 以分别将Postgres和MySQL数据库通过 Deltastreamer 将 CDC 日志写入 Apache Hudi，借助此功能我们可以连续捕获行级更改，将这些更改插入、更新和删除摄取到 Hudi数据湖中。</p> 
<h3 style="text-align:left">1.4 外部配置文件支持</h3> 
<p style="text-align:left">0.10.0版本运行用户通过配置文件 hudi-default.conf 传递配置，而不是直接将配置传递给每个 Hudi 作业。默认情况下，Hudi 会加载 /etc/hudi/conf 目录下的配置文件，用户可以通过设置 HUDI_CONF_DIR 环境变量来指定不同的配置目录位置，这对于简化需要经常重复执行相同的配置（如 Hive 同步设置、写入/索引调整参数）非常有用。</p> 
<h3 style="text-align:left">1.5 元数据表增强</h3> 
<p style="text-align:left">在 0.10.0 中我们通过同步更新而非异步更新对元数据表进行了更多基础性修复，以简化整体设计并用于构建未来更高级的功能，用户可以使用 <code>hoodie.metadata.enable=true</code> 开启元数据表。默认情况下基于元数据表的文件列表功能被禁用，我们希望在 0.11.0发布之前修复的一些其他遗留的后续工作，用户可以关注 <span style="color:#576b95">HUDI-1292[7]</span> 了解更多详情，<strong style="color:#0f4c81">在打开元数据表之前，请参阅迁移指南部分</strong>。</p> 
<h3 style="text-align:left">1.6 官网文档重构改版</h3> 
<p style="text-align:left">该重构对于想了解Hudi内部实现、特性的用户非常重要，在0.10.0中为以前缺少文档但存在的功能添加了文档，同时我们重新组织了官网文档布局以帮助新用户提高发现和使用Hudi的特性，同时我们根据社区反馈对文档进行了许多改进，请参阅最新文档：<span style="color:#576b95">https://hudi.apache.org[8]</span></p> 
<h2 style="margin-left:auto; margin-right:auto">2. 写入端改进</h2> 
<p style="margin-left:auto; margin-right:auto">提交即时时间（instant time）从秒级格式升级到毫秒级格式，该修改对于用户透明，用户无需修改任何配置即可顺利进行升级。</p> 
<p style="margin-left:auto; margin-right:auto"><strong style="color:#0f4c81">Deltastreamer增强</strong></p> 
<ul> 
 <li style="color: rgb(63, 63, 63); margin-left: 0px; margin-right: 0px; text-align: left;"><span>添加 <code>ORCDFSSource</code> 以支持 ORC 文件</span><span><span>•</span><code>S3EventsHoodieIncrSource</code> 现在可以从单个 S3 元数据表中写出多张表</span></li> 
</ul> 
<p style="color:#3f3f3f; margin-left:0; margin-right:0; text-align:left"><strong style="color:#0f4c81">Clustering增强</strong></p> 
<ul> 
 <li style="color: rgb(63, 63, 63); margin-left: 0px; margin-right: 0px; text-align: left;"><span>增加了保留相同文件组的支持以满足外部索引的要求，同时为处于pending状态的Clustering操作添加了增量时间线支持。</span></li> 
</ul> 
<h3 style="text-align:left">2.1 DynamoDB锁提供器</h3> 
<p style="text-align:left">Hudi 在 0.8.0 中增加了对并发写入的支持，作为功能使用的一部分用户需要配置锁服务提供者。在 0.10.0 中我们添加了用户可以使用的 DynamoDBBased 锁提供程序。要配置此锁提供程序，用户必须设置以下配置：</p> 
<pre style="margin-left:8px; margin-right:8px; text-align:left"><code>hoodie.write.lock.provider=org.apache.hudi.aws.transaction.lock.DynamoDBBasedLockProvider
Hoodie.write.lock.dynamodb.table
Hoodie.write.lock.dynamodb.partition_keyhoodie.write.lock.dynamodb.region</code></pre> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">此外要设置访问 AWS 资源的凭证，用户可以设置以下属性：</p> 
<pre style="margin-left:8px; margin-right:8px; text-align:left"><code>hoodie.aws.access.key
hoodie.aws.secret.key
hoodie.aws.session.token</code></pre> 
<p style="color:#3f3f3f; margin-left:8px; margin-right:8px; text-align:left">有关并发控制的更多详细信息请参考<span style="color:#576b95">并发控制[9]</span></p> 
<h3 style="text-align:left">2.2 默认配置修改</h3> 
<p style="text-align:left">在0.10.0中我们将 hudi 中所有 shuffle 并行性配置的默认值从 <code>1500</code> 调整为 <code>200</code>。相关配置是 <code>hoodie.insert.shuffle.parallelism</code>、<code>hoodie.bulkinsert.shuffle.parallelism</code>、<code>hoodie.upsert.shuffle.parallelism</code> 和 <code>hoodie.delete.shuffle.parallelism</code> 。用户如果依赖默认设置，请在升级时注意这些配置。不过我们已经在一些规模数据集上测试了这些配置。</p> 
<p style="text-align:left">我们已启用基于列表的标记的回滚策略，我们还将基于时间线服务器的标记作为此版本的默认标记，用户可以在<span style="color:#576b95">Marker机制[10]</span>阅读有关基于时间线服务器的标记的更多信息。</p> 
<p style="text-align:left">Clustering: 默认计划策略更改为 <code>SparkSizeBasedClusteringPlanStrategy</code>。默认情况下Clustering将保留提交元数据，这对于在时间轴中的Replace提交的增量查询支持非常有用。</p> 
<h3 style="text-align:left">2.3 Spark SQL改进</h3> 
<p style="text-align:left">0.10.0中我们对 spark-sql 进行了更多改进，例如添加了对非主键的 <code>MERGE INTO</code> 支持，并新支持了 <code>SHOW PARTITIONS</code> 和 <code>DROP PARTITIONS</code> 等操作命令。</p> 
<p style="text-align:left">同时在0.10.0中支持了Spark 3.1.2版本。</p> 
<h2 style="margin-left:auto; margin-right:auto">3. 查询端改进</h2> 
<p style="margin-left:auto; margin-right:auto">为 MOR 表添加了 Hive 增量查询支持和快照查询的分区修剪，添加了对Clustering的增量读取支持。</p> 
<p style="margin-left:auto; margin-right:auto">我们改进了列表逻辑，在查询时间上获得了 65% 的提升，在针对 Hudi 表的 Presto 查询上获得了 2.8 倍的并行度。</p> 
<p style="margin-left:auto; margin-right:auto">总的来说，我们在此版本中进行了大量错误修复（多作者、存档、回滚、元数据、集群等）和稳定性修复，并改进了我们围绕元数据和集群命令的 CLI，希望用户在 hudi 0.10.0 可以更顺畅地使用。</p> 
<h3 style="text-align:left">3.1 Flink集成改进</h3> 
<p style="text-align:left">Flink Reader现在支持增量读取，设置 <code>hoodie.datasource.query.type=incremental</code> 以启用批量执行模式，配置选项 <code>read.start-commit</code> 指定读取开始提交，配置选项 <code>read.end-commit</code> 指定结束提交（两者都包含）。流式读取还可以使用相同的选项 <code>read.start-commit</code> 指定起始偏移量。</p> 
<p style="text-align:left">支持批量执行模式下的 Upsert 操作，使用 INSERT INTO 语法更新现有数据集。</p> 
<p style="text-align:left">对于日志数据等非更新数据集，Flink Writer现在支持直接追加新的数据集而不合并，这是带有INSERT操作的Copy On Write表类型的默认模式，默认情况下 Writer不合并现有的小文件，设置 <code>write.insert.cluster=true</code> 以启用小文件的合并。</p> 
<p style="text-align:left"><code>write.precombine.field</code> 现在成为 flink writer 的可选（不是必需选项），当未指定字段时，如果表模式中有名为 ts 的字段，则 writer 将其用作 preCombine 字段，或 writer 按处理顺序比较记录：总是选择后面的记录。</p> 
<p style="text-align:left">小文件策略更加稳定，新策略中每个bucket分配任务单独管理一个文件组子集，这意味着bucket分配任务的并行度会影响小文件的数量。</p> 
<p style="text-align:left">Flink的写入和读取也支持元数据Metadata表，元数据表可以明显减少写入和读取是对于底层存储的分区查找和文件List。配置 <code>metadata.enabled=true</code>以启用此功能。</p> 
<h2 style="margin-left:auto; margin-right:auto">4. 生态</h2> 
<h3 style="text-align:left">4.1 DBT支持</h3> 
<p style="text-align:left">通过与非常流行的数据转换工具 <span style="color:#576b95">dbt[11]</span>集成，并已经在dbt 1.0.latest 版本中发布，用户可以更方便地创建派生的 Hudi 数据集。使用 0.10.0用户可以使用 dbt 创建增量 Hudi 数据集，详情请参阅 <span style="color:#576b95">dbt-spark#issue187[12]</span></p> 
<h3 style="text-align:left">4.2 监控</h3> 
<p style="text-align:left">Hudi 现在支持将指标发布到 Amazon CloudWatch。可以通过设置<code>hoodie.metrics.reporter.type=CLOUDWATCH</code>以启用，要使用的静态 AWS 凭证可以使用 <code>hoodie.aws.access.key</code>、<code>hoodie.aws.secret.key</code>、<code>hoodie.aws.session.token</code> 属性进行配置，在没有配置静态 AWS 凭证的情况下，<code>DefaultAWSCredentialsProviderChain</code> 将用于通过检查环境属性来获取凭证。可以在<code>HoodieMetricsCloudWatchConfig</code>调整的其他 Amazon CloudWatch配置。</p> 
<h3 style="text-align:left">4.3 DevEx</h3> 
<p style="text-align:left">因为默认的 maven spark3 版本没有升级到 3.1，因此使用<code>maven profile -Dspark3</code> 对 Spark 3.1.2 和 0.10.0 构建 Hudi。使用 <code>-Dspark3.0.x</code> 来构建 Spark 3.0.x 版本</p> 
<h3 style="text-align:left">4.4 悬空数据文件修复工具</h3> 
<p style="text-align:left">有时由于各种原因，从回滚中途失败到 cleaner 未能清理所有数据文件，或者spark 任务失败创建的数据文件没有被正确清理，可能会出现悬空的数据文件。因此我们添加了一个修复工具来清理任何不属于已完成提交的悬空数据文件，如果您在 0.10.0 版本中遇到问题，请通过 hudi-utilities 包中的 <code>org.apache.hudi.utilities.HoodieRepairTool</code> 试用该工具。同时该工具也具有试运行模式，可以打印悬空文件而不实际删除它，该工具可从 0.11.0-SNAPSHOT on master 获取。</p> 
<h2 style="margin-left:auto; margin-right:auto">5. 迁移指南</h2> 
<ul> 
 <li style="color: rgb(63, 63, 63); margin-left: 0px; margin-right: 0px; text-align: left;"><span>如果从旧版本迁移，请同时查看下面每个版本的迁移指南。</span></li> 
 <li style="color: rgb(63, 63, 63); margin-left: 0px; margin-right: 0px; text-align: left;"><span>在 0.10.0 中，我们对元数据表进行了一些基础性修复，因此作为升级的一部分，任何现有的元数据表都会被清理。每当 Hudi 使用更新的表版本启动时，即 3（或从更早版本升级到 0.10.0），升级步骤将自动执行，由于 <code>hoodie.table.version</code> 将在升级完成后在属性文件中更新，因此每个 Hudi 表只会进行一次自动升级步骤。</span></li> 
 <li style="color: rgb(63, 63, 63); margin-left: 0px; margin-right: 0px; text-align: left;"><span>同样如果某些用户想要将 Hudi 从表版本 3 降级到 2 或从 Hudi 0.10.0降级到 0.10.0 之前，则添加了用于降级命令行工具（Command - downgrade）。可以从 0.10.0的 hudi-cli 执行上述命令。</span></li> 
 <li style="color: rgb(63, 63, 63); margin-left: 0px; margin-right: 0px; text-align: left;"><span>我们围绕元数据表对 0.10.0 版本进行了一些重大修复，并建议用户尝试元数据以从优化的文件列表中获得更好的性能。作为升级的一部分，请按照以下步骤启用元数据表。</span></li> 
</ul> 
<h3 style="text-align:left">5.1 启用元数据表的先决条件</h3> 
<p style="text-align:left">Hudi 写入和读取必须在文件系统上执行<code>列表文件</code>操作才能获得系统的当前视图。这在云存储中可能非常昂贵，同时可能会根据数据集的规模/大小限制请求，因此我们早在 0.7.0版本中就引入了元数据表来缓存Hudi表的文件列表。在 0.10.0 中我们通过同步更新而不是异步更新对元数据表进行了基础性修复，以简化整体设计并协助构建多模式索引等未来高级功能，可以使用配置 <code>hoodie.metadata.enable=true</code> 开启。默认情况下基于元数据表的文件列表功能被禁用。根据不同的部署模型会有不同的迁移要求，具体如下：</p> 
<ul> 
 <li style="color: rgb(63, 63, 63); margin-left: 0px; margin-right: 0px; text-align: left;"><span>部署模型1：如果当前部署模型是单写入器并且所有表服务（清理、集群、压缩）都配置为内联，那么您可以打开元数据表而无需任何额外配置。</span></li> 
 <li style="color: rgb(63, 63, 63); margin-left: 0px; margin-right: 0px; text-align: left;"><span>部署模型2：如果当前部署模型是多写入器并配置了锁提供程序，那么您可以打开元数据表而无需任何额外配置。</span></li> 
 <li style="color: rgb(63, 63, 63); margin-left: 0px; margin-right: 0px; text-align: left;"><span>部署模型3：如果当前部署模型是单写入器并配置了异步表服务（例如Cleaning、Clustering、Compaction），那么在打开元数据表之前必须配置锁提供程序。即使您已经打开了元数据表，并且部署模型使用了异步表服务，那么在升级到此版本之前必须配置锁提供程序。</span></li> 
</ul> 
<h3 style="text-align:left">5.2 升级步骤</h3> 
<p style="text-align:left">对于部署模型1，使用 0.10.0 重新启动即可。</p> 
<p style="text-align:left">对于部署模型2，如果打算使用元数据表，则必须在所有编写器中启用元数据配置，否则会导致不一致写入器的数据丢失。</p> 
<p style="text-align:left">对于部署模型3，重新启动单个写入器和异步服务即可。如果将异步服务配置为与编写器分开运行，则必须在所有编写器和异步作业之间具有一致的元数据配置，如果启用元数据表，请记住按照上面的详细说明配置锁提供程序，关于锁提供程序的配置可参考<span style="color:#576b95">concurrency_control[13]</span></p> 
<p style="text-align:left">要利用基于元数据表的文件列表，读取时必须在查询时显式打开元数据配置，否则读取时将不会利用元数据表中的文件列表。</p> 
<h3 style="text-align:left">5.3 Spark-SQL主键要求</h3> 
<p style="text-align:left">Hudi中的Spark SQL需要在sql语句中通过tblproperites或options指定primaryKey。对于更新和删除操作还需要指定 <code>preCombineField</code>。这些要求与 Hudi DataSource 写入保持一致，这解决了以前版本中报告的许多行为差异。</p> 
<p style="text-align:left">要指定 <code>primaryKey</code>、<code>preCombineField</code> 或其他 Hudi 配置，与options方式相比，tblproperties方式是首选方式。Spark SQL 如Create Table语法详情参考<span style="color:#576b95">Create-table-datasource[14]</span>。总之任何在 0.10.0 之前创建的没有主键的 Hudi 表都需要使用带有 0.10.0 的主键字段重新创建，另外我们计划在未来版本中去掉对主键的限制。</p> 
<h2 style="margin-left:auto; margin-right:auto">6. 源码下载</h2> 
<p style="margin-left:auto; margin-right:auto">源码下载 : <span style="color:#576b95">Apache Hudi 0.10.0 Source Release[15]</span></p> 
<p style="margin-left:auto; margin-right:auto">Maven仓库包地址： <span style="color:#576b95">地址[16]</span></p> 
<h2 style="margin-left:auto; margin-right:auto">7. 感谢</h2> 
<p style="margin-left:auto; margin-right:auto">感谢参与0.10.0版本的所有贡献者，欢迎广大数据湖爱好者加入Apache Hudi社区，欢迎star & fork https://github.com/apache/hudi</p> 
<div style="margin-left:0; margin-right:0; text-align:left"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <div style="margin-left:0; margin-right:0"> 
    <div style="margin-left:0; margin-right:0"> 
     <p><strong>引用链接</strong></p> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<p style="color:#3f3f3f; margin-left:.5em; margin-right:.5em; text-align:left"><code>[1]</code> README-Hudi-Kafka-Connect: <em>https://github.com/apache/hudi/blob/master/hudi-kafka-connect/README.md</em><br> <code>[2]</code> RFC-32_Kafka Connect Sink For Hudi: <em>https://cwiki.apache.org/confluence/display/HUDI/RFC-32+Kafka+Connect+Sink+for+Hudi</em><br> <code>[3]</code> Pulsar-to-Hudi: <em>https://github.com/streamnative/pulsar-io-hudi</em><br> <code>[4]</code> RocketMQ-to-Hudi: <em>https://github.com/apache/rocketmq-externals/tree/master/rocketmq-connect-hudi</em><br> <code>[5]</code> Z-Ordering: <em>https://en.wikipedia.org/wiki/Z-order_curve</em><br> <code>[6]</code> Hilbert Curves: <em>https://en.wikipedia.org/wiki/Hilbert_curve</em><br> <code>[7]</code> HUDI-1292: <em>https://issues.apache.org/jira/browse/HUDI-1292</em><br> <code>[8]</code> https://hudi.apache.org: <em>https://hudi.apache.org/docs/overview</em><br> <code>[9]</code> 并发控制: <em>https://hudi.apache.org/docs/next/concurrency_control</em><br> <code>[10]</code> Marker机制: <em>https://hudi.apache.org/blog/2021/08/18/improving-marker-mechanism</em><br> <code>[11]</code> dbt: <em>https://github.com/dbt-labs/</em><br> <code>[12]</code> dbt-spark#issue187: <em>https://github.com/dbt-labs/dbt-spark/pull/210</em><br> <code>[13]</code> concurrency_control: <em>https://hudi.apache.org/docs/concurrency_control</em><br> <code>[14]</code> Create-table-datasource: <em>https://spark.apache.org/docs/latest/sql-ref-syntax-ddl-create-table-datasource.html</em><br> <code>[15]</code> Apache Hudi 0.10.0 Source Release: <em>https://www.apache.org/dyn/closer.lua/hudi/0.10.0/hudi-0.10.0.src.tgz</em><br> <code>[16]</code> 地址: <em>https://hudi.apache.org/releases/release-0.10.</em></p>
                                        </div>
                                      
</div>
            