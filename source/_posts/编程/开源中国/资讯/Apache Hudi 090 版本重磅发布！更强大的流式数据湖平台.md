
---
title: 'Apache Hudi 0.9.0 版本重磅发布！更强大的流式数据湖平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3910'
author: 开源中国
comments: false
date: Wed, 01 Sep 2021 10:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3910'
---

<div>   
<div class="content">
                                                                                            <h2>1. 重点特性</h2> 
<h3>1.1 Spark SQL支持</h3> 
<p>0.9.0 添加了对使用 Spark SQL 的 DDL/DML 的支持，朝着使所有角色（非工程师、分析师等）更容易访问和操作 Hudi 迈出了一大步。用户现在可以使用 <code>CREATE TABLE....USING HUDI</code> 和 <code>CREATE TABLE .. AS SELECT</code> 语句直接在 Hive 等目录中创建和管理表。然后用户可以使用 <code>INSERT</code>、<code>UPDATE</code>、<code>MERGE INTO</code> 和 <code>DELETE</code> 语句来操作数据。此外，<code>INSERT OVERWRITE</code> 语句可用于覆盖现有批处理 ETL 管道的表或分区中的现有数据。有关更多信息，请在此处单击 SparkSQL [1]查看文档。有关更多实现细节，请参阅 RFC-25[2]。</p> 
<h3>1.2 Flink集成</h3> 
<ul> 
 <li>Flink写入支持 <code>CDC Format</code>的 MOR 表，打开选项 <code>changelog.enabled</code>时，Hudi 会持久化每条记录的所有更改标志，使用 Flink 的流读取器，用户可以根据这些更改日志进行有状态的计算。请注意当使用异步压缩时，所有中间更改都合并为一个（最后一条记录），仅具有 UPSERT 语义。</li> 
 <li>支持Bulk insert来加载现有表，可以将 <code>write.operation</code> 设置为 <code>bulk_insert</code> 来使用。</li> 
 <li>Flink支持流式读取 COW 表。</li> 
 <li>删除消息默认在流式读取模式下发出，当 <code>changelog.enabled</code> 为 <code>false</code> 时，下游接收 <code>DELETE</code> 消息作为带有空负载的 Hudi 记录。</li> 
 <li>Flink写入现在可以更新历史分区，即删除历史分区中的旧记录然后在当前分区插入新记录，打开 <code>index.global.enabled</code> 使用。</li> 
 <li>通过支持不同的 Hive 版本（1.x、2.x、3.x），大大改善了 Hive 同步。</li> 
 <li>Flink 支持纯日志追加模式，在这种模式下没有记录去重，对于 <code>COW</code> 和 <code>MOR</code> 表，每次刷新都直接写入 parquet，关闭 <code>write.insert.deduplicate</code> 以开启这种模式。</li> 
</ul> 
<h3>1.3 查询端改进</h3> 
<ul> 
 <li>Hudi 现在可以在 Spark 中注册为数据源表。</li> 
 <li>基于Metadata Table的 Spark 读取改进。</li> 
 <li>添加了对时间旅行查询的支持。请参考时间旅行[3]。</li> 
</ul> 
<h3>1.4 写入端改进</h3> 
<ul> 
 <li>添加了虚拟键支持，用户可以避免将元字段添加到 Hudi 表并利用现有的字段来填充记录键和分区路径。请参考 具体配置[4]来开启虚拟键。</li> 
 <li><strong>Clustering改进</strong></li> 
 <li>DeltaStreamer 和 Spark Streaming 都添加了异步Clustering支持。可以在这篇博客文章[5]中找到更多细节。</li> 
 <li>增量读取也适用于Clustering数据。</li> 
 <li>添加了 HoodieClusteringJob[6] 以作为独立作业来构建和执行Clustering计划。</li> 
 <li>添加了一个配置（<code>hoodie.clustering.plan.strategy.daybased.skipfromlatest.partitions</code>）以在创建Clustering计划时跳过最近的 N 个分区。</li> 
 <li>增强 Bulk_Insert模式（新增行写入器模式），并缺省打开，用户可以使用行写入器模式以获得更好的性能。</li> 
 <li>在 HiveSyncTool 中添加了对 HMS 的支持。HMSDDLExecutor 是一个 DDLExecutor 实现，基于使用 HMS 的 HMS apis 直接用于执行所有 DDL 。</li> 
 <li>Spark 引擎中添加了预提交验证器框架[7]。用户可以利用该框架来添加验证给定提交的文件是否都存在，或是否已经删除所有无效文件等。</li> 
 <li>org.apache.hudi.client.validator.SqlQueryEqualityPreCommitValidator[8] 可用于验证提交前后行的数据行相同</li> 
 <li>org.apache.hudi.client.validator.SqlQueryInequalityPreCommitValidator[9] 可用于验证提交前后的数据行不相同</li> 
 <li>org.apache.hudi.client.validator.SqlQuerySingleResultPreCommitValidator[10] 可用于验证表是否产生特定值这些可以通过设置 <code>hoodie.precommit.validators=<逗号分隔的验证器类名称列表> 来配置</code>。用户还可以通过扩展抽象类 <code>SparkPreCommitValidator</code> 并覆盖此方法来提供自己的实现。</li> 
 <li>用户可以选择删除用于生成分区路径的字段（<code>hoodie.datasource.write.drop.partition.columns</code>），以支持使用BigQuery系统查询Hudi快照。</li> 
 <li>支持<strong>华为云、百度云、金山云</strong>对象存储。</li> 
 <li>添加了对<code>delete_partition</code>操作的支持，用户可以在需要时利用它删除旧分区。</li> 
 <li>ORC格式支持，现在用户可以指定存储格式为ORC，注意现在暂时只支持Spark查询。</li> 
 <li>Hudi 使用不同类型的可溢出映射，用于内部处理合并（压缩、更新甚至 MOR 快照查询）。在 0.9.0 中，我们添加了对 bitcask默认选项的压缩支持，并引入了由 RocksDB 支持，它可以在大批量更新或处理大型基本文件时性能更高。</li> 
 <li>增强对未提交的数据的自动清理，该增强在云存储上性能更优，具体来说是新增了一种新的标记机制，利用时间线服务器对底层存储执行集中协调的文件标记批量读/写，你可以使用这个配置[11]来启用，并在这个博客[12]上了解更多。</li> 
</ul> 
<h3>1.5 DeltaStreamer改进</h3> 
<ul> 
 <li>JDBC Source[13] 可以采用提取 SQL 语句并从支持 JDBC 的源中增量获取数据。这对于例如从 RDBMS 源读取数据时很有用。请注意，这种方法可能需要定期重新引导以确保数据一致性，尽管在基于 CDC 的方法上操作要简单得多。</li> 
 <li>SQLSource[14] 使用 Spark SQL 语句从现有表中提取数据，对于基于 SQL 的简单回填用例非常有用，例如：过去 N 个月只回填一列。</li> 
 <li>S3EventsHoodieIncrSource[15] 和 S3EventsSource[16] 有助于从 S3 读取数据，可靠且高效地将数据摄取到 Hudi。现有使用 DFSSource 的方法是使用文件的最后修改时间作为检查点来拉入新文件，但是如果大量文件具有相同的修改时间，则可能会遇到丢失一些要从源读取的文件的问题。这两个源（S3EventsHoodieIncrSource 和 S3EventsSource）通过利用从源存储桶订阅文件事件的 AWS SNS 和 SQS 服务，共同确保将数据从 S3 可靠地摄取到 Hudi。</li> 
 <li>除了使用 DeltaStreamer 使用常规偏移格式（topic_name,partition_num:offset,partition_num:offset,....），我们还为 kafka 源提取数据添加了两种新格式，即基于时间戳和组消费者偏移量。</li> 
 <li>添加了在 deltastreamer 中使用模式提供程序在模式注册表提供程序 url 中传递基本身份验证凭据的支持。</li> 
 <li> 对<code>hudi-cli</code> 的一些改进，例如<code>SCHEDULE COMPACTION</code>和<code>RUN COMPACTION</code>语句，以便轻松在 Hudi 表上调度和运行Compaction、Clustering。</li> 
</ul> 
<h2>2. 迁移指南</h2> 
<ul> 
 <li>如果从 0.5.3 之前的版本迁移，还请检查下面每个后续版本的升级说明。</li> 
 <li>Hudi 在 0.9.0 中添加了更多表属性，以帮助将现有的 Hudi 表与 spark-sql 结合使用。为了顺利地迁移，这些属性添加到 <code>hoodie.properties</code> 文件中。每当 Hudi 使用较新的表版本启动时，即 2（或从 0.9.0 之前移动到 0.9.0），升级步骤将自动执行。这个自动升级步骤对于每个 Hudi 表只会发生一次，因为<code>hoodie.table.version</code> 将在升级完成后在属性文件中更新。</li> 
 <li>同样如果某些用户想要将 Hudi 从表版本 2 降级到 1 或从 Hudi 0.9.0 移动到 0.9.0 之前，则添加了用于降级的命令行工具（command - <code>downgrade</code>），需要使用0.9.0版本中的<code>hudi-cli</code>工具。</li> 
 <li>在此版本中我们添加了一个新框架来跟踪代码中的配置属性，不再使用包含属性名称和值的字符串变量。这一举措有助于我们自动生成配置文档。虽然我们仍然支持旧的字符串变量，但鼓励用户使用新的 <code>ConfigProperty</code> 配置项。在大多数情况下，它就像在相应的替代方法上调用 <code>.key()</code> 和 <code>.defaultValue()</code> 一样简单。例如 <code>RECORDKEY_FIELD_OPT_KEY</code> 可以替换为 <code>RECORDKEY_FIELD_NAME.key()</code>。</li> 
</ul> 
<h2>3. 感谢</h2> 
<p>感谢参与0.9.0版本的所有贡献者，欢迎广大数据湖爱好者加入Apache Hudi社区，欢迎star & fork https://github.com/apache/hudi</p> 
<h2>4. 源码下载</h2> 
<ul> 
 <li>源码下载 : Apache Hudi 0.9.0 Source Release[17]</li> 
 <li>Maven仓库包地址： 地址[18]</li> 
</ul> 
<h4><strong>引用链接</strong></h4> 
<p><code>[1]</code> SparkSQL : <em>http://hudi.apache.org/docs/quick-start-guide</em><br> <code>[2]</code> RFC-25: <em>(https://cwiki.apache.org/confluence/display/HUDI/RFC+-+25%3A+Spark+SQL+Extension+For+Hudi)</em><br> <code>[3]</code> 时间旅行: <em>http://hudi.apache.org/docs/quick-start-guide#time-travel-query</em><br> <code>[4]</code> 配置: <em>http://hudi.apache.org/docs/configurations#hoodiepopulatemetafields</em><br> <code>[5]</code> 博客文章: <em>http://hudi.apache.org/blog/2021/08/23/async-clustering</em><br> <code>[6]</code> HoodieClusteringJob: <em>https://github.com/apache/hudi/blob/bf5a52e51bbeaa089995335a0a4c55884792e505/hudi-utilities/src/main/java/org/apache/hudi/utilities/HoodieClusteringJob.java</em><br> <code>[7]</code> 预提交验证器框架: <em>https://github.com/apache/hudi/blob/bf5a52e51bbeaa089995335a0a4c55884792e505/hudi-client/hudi-spark-client/src/main/java/org/apache/hudi/client/validator/SparkPreCommitValidator.java</em><br> <code>[8]</code> org.apache.hudi.client.validator.SqlQueryEqualityPreCommitValidator: <em>https://github.com/apache/hudi/blob/bf5a52e51bbeaa089995335a0a4c55884792e505/hudi-client/hudi-spark-client/src/main/java/org/apache/hudi/client/validator/SqlQueryEqualityPreCommitValidator.java</em><br> <code>[9]</code> org.apache.hudi.client.validator.SqlQueryInequalityPreCommitValidator: <em>https://github.com/apache/hudi/blob/bf5a52e51bbeaa089995335a0a4c55884792e505/hudi-client/hudi-spark-client/src/main/java/org/apache/hudi/client/validator/SqlQueryInequalityPreCommitValidator.java</em><br> <code>[10]</code> org.apache.hudi.client.validator.SqlQuerySingleResultPreCommitValidator: <em>https://github.com/apache/hudi/blob/bf5a52e51bbeaa089995335a0a4c55884792e505/hudi-client/hudi-spark-client/src/main/java/org/apache/hudi/client/validator/SqlQuerySingleResultPreCommitValidator.java</em><br> <code>[11]</code> 配置: <em>http://hudi.apache.org/docs/configurations#hoodiewritemarkerstype</em><br> <code>[12]</code> 博客: <em>http://hudi.apache.org/blog/2021/08/18/improving-marker-mechanism</em><br> <code>[13]</code> JDBC Source: <em>https://github.com/apache/hudi/blob/bf5a52e51bbeaa089995335a0a4c55884792e505/hudi-utilities/src/main/java/org/apache/hudi/utilities/sources/JdbcSource.java</em><br> <code>[14]</code> SQLSource: <em>https://github.com/apache/hudi/blob/bf5a52e51bbeaa089995335a0a4c55884792e505/hudi-utilities/src/main/java/org/apache/hudi/utilities/sources/SqlSource.java</em><br> <code>[15]</code> S3EventsHoodieIncrSource: <em>https://github.com/apache/hudi/blob/bf5a52e51bbeaa089995335a0a4c55884792e505/hudi-utilities/src/main/java/org/apache/hudi/utilities/sources/S3EventsHoodieIncrSource.java</em><br> <code>[16]</code> S3EventsSource: <em>https://github.com/apache/hudi/blob/bf5a52e51bbeaa089995335a0a4c55884792e505/hudi-utilities/src/main/java/org/apache/hudi/utilities/sources/S3EventsSource.java</em><br> <code>[17]</code> Apache Hudi 0.9.0 Source Release: <em>https://downloads.apache.org/hudi/0.9.0/hudi-0.9.0.src.tgz</em><br> <code>[18]</code> 地址: <em>https://repository.apache.org/#nexus-search;quick~hudi</em></p>
                                        </div>
                                      
</div>
            