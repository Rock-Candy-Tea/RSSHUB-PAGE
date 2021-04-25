
---
title: 'Flink在唯品会的实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/841f4a270aa9eec4a6107b645ace7bc7.png'
author: Dockone
comments: false
date: 2021-04-25 12:10:21
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/841f4a270aa9eec4a6107b645ace7bc7.png'
---

<div>   
<br>唯品会自2017年开始基于Kubernetes深入打造高性能、稳定、可靠、易用的实时计算平台，支持唯品会内部业务在平时以及大促的平稳运行。现平台支持Flink、Spark、Storm等主流框架。本文主要分享Flink的容器化实践应用以及产品化经验。<br>
<h3>发展概览</h3>平台支持公司内部所有部门的实时计算应用。主要的业务包括实时大屏，推荐，实验平台，实时监控和实时数据清洗等。<br><br>
<h4>集群规模</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/841f4a270aa9eec4a6107b645ace7bc7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/841f4a270aa9eec4a6107b645ace7bc7.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
平台现有异地双机房双集群，具有2000多的物理机节点，利用Kubernetes的namespaces，labels和taints等实现业务隔离以及初步的计算负载隔离。目前线上实时应用有大概1000个，平台最近主要支持Flink SQL任务的上线。<br>
<h4>平台架构</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/f35669ffe19559ebaf0979db9ec37beb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/f35669ffe19559ebaf0979db9ec37beb.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图所示，是唯品会实时计算平台的整体架构。<br>
<ul><li>最底层是计算任务节点的资源调度层，实际以deployment的模式运行Kubernetes上，平台虽然是支持yarn调度，但是yarn调度是与批任务共享资源，所以主流任务还是运行在Kubernetes上。</li><li>存储层这一层，支持公司内部基于Kafka实时数据VMS，基于BinLog的VDP数据和原生Kafka作为消息总线，状态存储在HDFS上，数据主要存入Redis，MySQL，HBase，Kudu，Clickhouse等。</li><li>计算引擎层，平台支持Flink，Spark，Storm主流框架容器化，提供了一些框架的封装和组件等。每个框架会都会支持几个版本的镜像满足不同的业务需求。</li><li>平台层提供作业配置、调度、版本管理、容器监控、job监控、告警、日志等功能，提供多租户的资源管理（quota，label管理），提供Kafka监控。在Flink 1.11版本之前，平台自建元数据管理系统为Flink SQL管理schema，1.11版本开始，通过Hive Metastore与公司元数据管理系统融合。</li><li>最上层就是各个业务的应用层。</li></ul><br>
<br><h3>Flink容器化实践</h3><h4>容器化实践</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/567763675d16eb5cf6aa7c6ba564a331.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/567763675d16eb5cf6aa7c6ba564a331.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图所示，是实时平台Flink容器化的架构。Flink容器化是基于Standalone模式部署的。<br>
<ul><li>部署模式共有Client，JobManager和TaskManager三个角色，每一个角色都由一个deployment控制。</li><li>用户通过平台上传任务jar包，配置等，存储于HDFS上。同时由平台维护的配置，依赖等也存储在HDFS上，当Pod启动时，会进行拉取等初始化操作。</li><li>Client中主进程是一个由Go开发的agent，当Client启动时，会首先检查集群状态，当集群ready后，从HDFS上拉取jar包向Flink集群提交任务，Client的主要功能还有监控任务状态，做savepoint等操作。</li><li>通过部署在每台物理机上的smart-agent采集容器的指标写入m3，以及通过Flink暴漏的接口将Metrics写入Prometheus，结合Grafana展示。同样通过部署在每台物理机上的Filebeat采集挂载出来的相关日志写入ES，在DragonFly可以实现日志检索。</li></ul><br>
<br><strong>Flink平台化</strong><br>
<br>在实践过程中，结合具体场景以及易用性考虑，做了平台化工作。<br>
<ul><li>平台的任务配置与镜像，Flink配置，自定义组件等解耦合，现阶段平台支持1.7、1.9、1.11、1.12等版本。  </li><li>平台支持流水线编译或上传jar，作业配置，告警配置，生命周期管理等，从而减少用户的开发成本。  </li><li>平台开发了容器级别的如火焰图等调优诊断的页面化功能，以及登陆容器的功能，支持用户进行作业诊断。  </li></ul><br>
<br><strong>Flink稳定性</strong><br>
<br>在应用部署和运行过程中，不可避免的会出现异常。平台保证任务在出现异常状况后的稳定性做的策略。<br>
<ul><li>Pod的健康和可用，由livenessProbe和readinessProbe检测，同时指定Pod的重启策略。</li><li><br>Flink任务异常时：<br>
<ul><li>Flink原生的restart策略和failover机制，作为第一层的保证。  </li><li>在client中会定时监控Flink状态，同时将最新的checkpoint地址更新到自己的缓存中，并汇报到平台，固化到MySQL中。当Flink无法再重启时，由Client重新从最新的成功Checkpoint提交任务。作为第二层保证。这一层将Checkpoint固化到MySQL中后，就不再使用Flink HA机制了，少了ZooKeeper的组件依赖。</li><li>当前两层无法重启时或集群出现异常时，由平台自动从固化到MySQL中的最新chekcpoint重新拉起一个集群，提交任务，作为第三层保证。</li></ul></li><li><br>机房容灾：  <br>
<ul><li>用户的jar包，Checkpoint都做了异地双HDFS存储</li><li>异地双机房双集群</li></ul></li></ul><br>
<br><h4>Kafka监控方案</h4>Kafka监控是我们的任务监控里相对重要的一部分，整体监控流程如下所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/02bb38c3840a133f7c860d967c6e8986.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/02bb38c3840a133f7c860d967c6e8986.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
平台提供监控Kafka堆积，消费message等配置信息，从MySQL中将用户Kafka监控配置提取后，通过JMX监控Kafka，写入下游Kafka，再通过另一个Flink任务实时监控，同时将这些数据写入ck，从而展示给用户。<br>
<h3>Flink SQL平台化建设</h3>基于Kubernetes的Flink容器化实现以后，方便了Flink API应用的发布，但是对于Flink SQL的任务仍然不够便捷。于是平台提供了更加方便的在线编辑发布、SQL管理等一栈式开发平台。<br>
<h4>Flink SQL方案</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/72dd44d5718b0820398d8e3b36322041.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/72dd44d5718b0820398d8e3b36322041.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
平台的Flink SQL方案如上图所示，任务发布系统与元数据管理系统完全解耦。<br>
<br><strong>Flink SQL任务发布平台化</strong><br>
<br>在实践过程中，结合易用性考虑，做了平台化工作，主操作界面如下图所示：<br>
<ul><li>Flink SQL的版本管理，语法校验，拓扑图管理等；</li><li>UDF通用和任务级别的管理，支持用户自定义UDF；</li><li>提供参数化的配置界面，方便用户上线任务。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/cd2ac0a259e7cb0c0795e5997cf0d1fd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/cd2ac0a259e7cb0c0795e5997cf0d1fd.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/be7c8fa5d3611342cc908c3260c63799.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/be7c8fa5d3611342cc908c3260c63799.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>元数据管理</strong><br>
<br>平台在1.11之前通过构建自己的元数据管理系统UDM，MySQL存储Kafka，Redis等Schemas，通过自定义catalog打通Flink与UDM，从而实现元数据管理。1.11之后，Flink集成hive逐渐完善，平台重构了FlinkSQL框架，通过部署一个SQL-gateway service服务，中间调用自己维护的sql-client jar包，从而与离线元数据打通，实现了实时离线元数据统一，为之后的流批一体做好工作。在元数据管理系统创建的Flink表操作界面如下所示，创建Flink表的元数据，持久化到hive里，Flink SQL启动时从hive里读取对应表的table schema信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/fe377f2e4db7000da4fdd931b473d361.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/fe377f2e4db7000da4fdd931b473d361.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Flink SQL相关实践</h4>平台对于官方原生支持或者不支持的Connector进行整合和开发，镜像和Connector，Format等相关依赖进行解耦，可以快捷的进行更新与迭代。<br>
<br><strong>Flink SQL 相关实践</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/0c1ab4e55a74637027dcbd1895d25f99.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/0c1ab4e55a74637027dcbd1895d25f99.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>Connector层，现阶段平台支持官方支持的Connector，并且构建了Redis，Kudu，Clickhouse，VMS，VDP等平台内部的Connector。平台构建了内部的pb format，支持Protobuf实时清洗数据的读取。平台构建了Kudu，VDP等内部Catalog，支持直接读取相关的Schema，不用再创建DDL。</li><li>平台层主要是在UDF、常用运行参数调整、以及升级Hadoop 3。</li><li>Runtime层主要是支持拓扑图执行计划修改、维表关联keyBy cache优化等。</li></ul><br>
<br><strong>拓扑图执行计划修改</strong><br>
<br>针对现阶段SQL生成的stream graph并行度无法修改等问题，平台提供可修改的拓扑预览修改相关参数。平台会将解析后的FlinkSQL的excution plan json提供给用户，利用uid保证算子的唯一性，修改每个算子的并行度，chain策略等，也为用户解决反压问题提供方法。例如针对clickhouse sink 小并发大批次的场景，我们支持修改clickhouse sink并行度，source并行度=72，sink并行度=24，提高clickhouse sink tps。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/5167f221561dedd0ec872fee39668620.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/5167f221561dedd0ec872fee39668620.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>维表关联keyBy优化cache</strong><br>
<br>针对维表关联的情况，为了降低IO请求次数，降低维表数据库读压力，从而降低延迟，提高吞吐，有以下几种措施：<br><br>
<ul><li>当维表数据量不大时，通过全量维表数据缓存在本地，同时ttl控制缓存刷新的时候，这可以极大的降低IO请求次数，但会要求更多但内存空间。</li><li>当维表数据量很大时，通过async和LRU cache策略，同时ttl和size来控制缓存数据的失效时间和缓存大小，可以提高吞吐率并降低数据库的读压力。</li><li>当维表数据量很大同时主流QPS很高时，可以开启把维表join的key作为hash的条件，将数据进行分区，即在calc节点的分区策略是hash，这样下游算子的subtask的维表数据是独立的，不仅可以提高命中率，也可降低内存使用空间。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/cc54f6c56ed5154fd450a9fc25be1c6a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/cc54f6c56ed5154fd450a9fc25be1c6a.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
优化之前维表关联LookupJoin算子和正常算子chain在一起。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/925f698a688c3a711ae54db917ce9387.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/925f698a688c3a711ae54db917ce9387.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
优化之间维表关联LookupJoin算子和正常算子不chain在一起，将join key 作为hash策略的key。采用这种方式优化之后，例如原先3000W 数据量的维表，10个TM节点，每个节点都要缓存3000W的数据，总共需要缓存3000W*10=3亿的量。而经过keyBy优化之后，每个TM节点只需要缓存3000W/10 =300W的数据量，总共缓存的数据量只有3000W，大大减少缓存数据量。<br>
<br><strong>维表关联延迟join</strong><br>
<br>维表关联中，有很多业务场景，在维表数据新增数据之前，主流数据已经发生join操作，会出现关联不上的情况。因此，为了保证数据的正确，将关联不上的数据进行缓存，进行延迟join。<br>
<ul><li>最简单的做法是，在维表关联的function里设置重试次数和重试间隔，这个方法会增大整个流的延迟，但主流qps不高的情况下，可以解决问题。  </li><li>增加延迟join的算子，当join维表未关联时，先缓存起来，根据设置重试次数和重试间隔从而进行延迟的join。</li></ul><br>
<br><h3>应用案例</h3><h4>实时数仓</h4><strong>实时数据入仓</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/4f90b82ed5276fda9594ae2eac268281.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/4f90b82ed5276fda9594ae2eac268281.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>流量数据一级Kafka通过实时清洗之后，写到二级清洗Kafka，主要是Protobuf格式，再通过Flink SQL写入hive 5min表，以便做后续的准实时ETL，加速ods层数据源的准备时间。</li><li>MySQL业务库的数据，通过VDP解析形成binlog cdc消息流，再通过Flink SQL写入hive 5min表。</li><li>业务系统通过VMS API产生业务Kafka消息流，通过Flink SQL解析之后写入hive 5min表。支持string、json、csv等消息格式。</li><li>使用Flink SQL做流式数据入仓，非常的方便，而且1.12版本已经支持了小文件的自动合并，解决了小文件的痛点。</li><li>我们自定义分区提交策略，当前分区ready时候会调一下实时平台的分区提交API，在离线调度定时调度通过这个API检查分区是否ready。</li></ul><br>
<br>采用Flink SQL统一入仓方案以后，我们可以获得的收益：可解决以前Flume方案不稳定的问题，而且用户可自助入仓，大大降低入仓任务的维护成本。提升了离线数仓的时效性，从小时级降低至5min粒度入仓。<br>
<br><strong>实时指标计算</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/9d464f224b1cc5ff27ab7a32f39fa748.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/9d464f224b1cc5ff27ab7a32f39fa748.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>实时应用消费清洗后Kafka，通过Redis维表、API等方式关联，再通过Flink window增量计算UV，持久化写到Hbase里。</li><li>实时应用消费VDP消息流之后，通过Redis维表、API等方式关联，再通过Flink SQL计算出销售额等相关指标，增量upsert到Kudu里，方便根据range分区批量查询，最终通过数据服务对实时大屏提供最终服务。</li></ul><br>
<br>以往指标计算通常采用Storm方式，需要通过API定制化开发，采用这样Flink方案以后，我们可以获得的收益：将计算逻辑切到Flink SQL上，降低计算任务口径变化快，修改上线周期慢等问题。切换至Flink SQL可以做到快速修改，快速上线，降低维护成本。<br>
<br><strong>实时离线一体化ETL数据集成</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/d43ceb7256d0d11bab2982e0a2048d38.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/d43ceb7256d0d11bab2982e0a2048d38.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>Flink SQL在最近的版本中持续强化了维表join的能力，不仅可以实时关联数据库中的维表数据，现在还能关联Hive和Kafka中的维表数据，能灵活满足不同工作负载和时效性的需求。</li><li>基于Flink强大的流式 ETL的能力，我们可以统一在实时层做数据接入和数据转换，然后将明细层的数据回流到离线数仓中。</li><li>我们通过将presto内部使用的HyperLogLog（后面简称HLL）实现引入到Spark UDAF函数里，打通HLL对象在Spark SQL与presto引擎之间的互通，如Spark SQL通过prepare函数生成的HLL对象，不仅可以在Spark SQL里merge查询而且可以在presto里进行merge查询。具体流程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/5f08dd39124492770ab06d6cdcd6bfdd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/5f08dd39124492770ab06d6cdcd6bfdd.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
</li></ul><br>
<br>UV近似计算示例：<br>
<br>Step 1：Spark SQL生成HLL对象<br>
<pre class="prettyprint">insert overwrite dws_goods_uv partition (dt='$&#123;dt&#125;',hm='$&#123;hm&#125;') AS select goods_id, estimate_prepare(mid) as pre_hll from dwd_table_goods group by goods_id where dt = $&#123;dt&#125; and hm = $&#123;hm&#125; <br>
</pre><br>
Step 2：Spark SQL通过goods_id维度的HLL对象merge成品牌维度<br>
<pre class="prettyprint">insert overwrite dws_brand_uv partition (dt='$&#123;dt&#125;',hm='$&#123;hm&#125;') AS select b.brand_id, estimate_merge(pre_hll) as merge_hll from dws_table_brand A left join dim_table_brand_goods B on A.goods_id = B.goods_id where dt = $&#123;dt&#125; and hm = $&#123;hm&#125; <br>
</pre><br>
Step 3：Spark SQL查询品牌维度的UV<br>
<pre class="prettyprint">select brand_id, estimate_compute(merge_hll ) as uv from dws_brand_uv where dt = $&#123;dt&#125; <br>
</pre><br>
Step 4：presto merge查询Spark生成的HLL对象<br>
<pre class="prettyprint">select brand_id,cardinality(merge(cast(merge_hll AS HyperLogLog))) uv from dws_brand_uv group by brand_id<br>
</pre><br>
所以基于实时离线一体化ETL数据集成的架构，我们能获得的收益：<br>
<ul><li>统一了基础公共数据源；</li><li>提升了离线数仓的时效性；</li><li>减少了组件和链路的维护成本。</li></ul><br>
<br><h4>实验平台（Flink实时数据入OLAP）</h4>唯品会实验平台是通过配置多维度分析和下钻分析，提供海量数据的A/B-test实验效果分析的一体化平台。一个实验是由一股流量（比如用户请求）和在这股流量上进行的相对对比实验的修改组成。实验平台对于海量数据查询有着低延迟、低响应、超大规模数据(百亿级)的需求。整体数据架构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/ef3aae76f49a7b84675ec0ec0454af49.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/ef3aae76f49a7b84675ec0ec0454af49.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通过Flink SQL将Kafka里的数据清洗解析展开等操作之后，通过Redis维表关联商品属性，通过分布式表写入到Clickhouse，然后通过数据服务adhoc查询。业务数据流如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210423/3bd6790f17cb420cdf7404c8735a4449.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210423/3bd6790f17cb420cdf7404c8735a4449.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们通过Flink SQL redis connector，支持Redis的sink 、source维表关联等操作，可以很方便的读写Redis，实现维表关联，维表关联内可配置cache，极大提高应用的TPS。通过Flink SQL 实现实时数据流的Pipeline，最终将大宽表sink到CK 里，并按照某个字段粒度做murmurHash3_64存储，保证相同用户的数据都存在同一shard节点组内，从而使得ck大表之间的join变成local本地表之间的join，减少数据shuffle操作，提升join查询效率。<br>
<h3>未来规划</h3><h4>提高Flink SQL易用性</h4>当前我们的Flink SQL调试起来很有很多不方便的地方，对于做离线Hive用户来说还有一定的使用门槛，例如手动配置Kafka监控、任务的压测调优，如何能让用户的使用门槛降低至最低，是一个比较大的挑战。将来我们考虑做一些智能监控告诉用户当前任务存在的问题，尽可能自动化并给用户一些优化建议。<br>
<h4>数据湖CDC分析方案落地</h4>目前我们的VDP binlog消息流，通过Flink SQL写入到hive ods层，以加速ods层数据源的准备时间，但是会产生大量重复消息去重合并。我们会考虑Flink +数据湖的cdc入仓方案来做增量入仓。此外，像订单打宽之后的Kafka消息流、以及聚合结果都需要非常强的实时upsert能力，目前我们主要是用kudu，但是kudu集群，比较独立小众，维护成本高，我们会调研数据湖的增量upsert能力来替换Kudu增量upsert场景。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/gQRyD4igKHUCqEh4gRvZjw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/gQRyD4igKHUCqEh4gRvZjw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            