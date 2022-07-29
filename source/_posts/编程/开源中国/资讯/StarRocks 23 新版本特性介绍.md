
---
title: 'StarRocks 2.3 新版本特性介绍'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5774'
author: 开源中国
comments: false
date: Fri, 29 Jul 2022 14:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5774'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">各位 StarRocks 的新老用户：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">StarRocks 近期发布了 2.3 版本，核心更新有：<strong>主键模型支持完整的 DELETE WHERE 语句，异步执行 CTAS，资源组的大查询防御，资源组的监控，JDBC 外表，数据目录 Catalog，集群部署与管理工具 StarGo 等。</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">欢迎体验新版本功能，若喜欢我们的项目，大家可以在 GitHub 上 Star 一下✨ 体验地址：</span><u><em>https://github.com/StarRocks/starrocks</em></u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">以下是具体介绍，欢迎您升级使用、多多反馈！</span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span><strong><span>#01</span></strong></span></h1> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong><span>StarRocks 2.3 版本介绍</span></strong></h1> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#338393">—</span></strong></h1> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="background-color:#ffffff; color:#222222">StarRocks 是新一代极速全场景 MPP 数据库，致力于让用户无需经过复杂的预处理，就可以支持多种数据分析场景的极速分析。</span><span style="background-color:#ffffff; color:#222222">StarRocks 相信数据科学的创新将全面驱动业务发展，希望能帮助企业建立 “极速统一” 的数据分析新范式，助力企业全面数字化经营。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="background-color:#ffffff; color:#222222">2.3 版本是 StarRocks 稳定性和易用性大幅补强的一个版本：Primary Key 模型支持持久化主键索引，可以合理控制内存使用，同时通过完善 Delete 语法，可以支持复杂逻辑的删除操作。数据湖分析支持 External Catalog ，可以大幅降低用户使用外表的门槛。JDBC 外表可以帮助用户方便的连接各类 TP 数据库。此外，资源组管理和运维部署工具也做了诸多改进。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"> </p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span><strong><span>#02</span></strong></span></h1> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong><span>StarRocks 2.3 新增功能详解</span></strong></h1> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#338393">—</span></strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><strong>1、</strong></span><span style="color:#000000">主键模型支持完整 DELETE WHERE 语义</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">从 2.3 版本开始，StarRocks 对于主键数据模型（Primary Key）支持完整的 DELETE 语法：WHERE 条件支持完整的比较运算符 (=、>、!= 等) 和逻辑运算符 (AND、OR)，并且完全支持用子查询来进行过滤删除。有了完整的 DELETE WHERE 支持后，用户可以更加方便地直接使用 SQL 命令完成带有复杂逻辑的数据删除操作，从而支持更加丰富的更新需求。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2、</strong><span style="color:#000000">异步执行 CTAS</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">在 Apache Spark 生态中，部分场景下用户需要通过异步的方式，提交大批量的数据分析处理作业，并根据作业的唯一标志符来实时查看作业的进度或者最终结果。针对这一场景，在 StarRocks 中，我们提供了如下的异步查询能力：通过任务提交框架，以异步的方式提交一个 CREATE TABLE AS SELECT 任务，将查询结果写入一张新的表；并通过创建任务时指定的唯一标识符来查看任务的执行进展。借助这种异步模式，用户在执行大批量数据分析处理任务时候无需同步等待执行结果，进一步提升开发体验。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>3、</strong><span style="color:#000000">资源组的大查询防御</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">自 2.2 版本起，StarRocks 提供了资源隔离功能，通过设置资源组的方式限制查询对资源的消耗，实现多租户之间的资源隔离与合理利用。</span><span style="background-color:#ffffff; color:#222222">在此基础上，从 2.3 版本起，用户可进一步控制大查询对资源的消耗，避免系统资源耗尽对稳定性产生影响。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">具体来说：用户指定资源组当中能够运行查询的扫描行数 / 内存大小 / CPU 运行时间的上限。对超过阈值上限的查询，系统会对其进行拦截并终止执行。借助此能力，如果用户侧的异常查询负载可以通过 扫描行数 / 内存大小 / CPU 运行时间等维度组合来进行表征，那么用户就可以自行按照业务需求来拦截，从而保证系统整体负载的稳定。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>4、</strong><span style="color:#000000">JDBC 外表</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">StarRocks 在 2.3 版本提供了 JDBC 外表。用户可以借助 JDBC 外表在 StarRocks 中直接进行查询</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">MySQL、PostgreSQL、Oracle、ClickHouse 等数据源，并且无需迁移数据。此外，在查询过程中，通过算子下推能力提供了查询性能优化。借助 JDBC 外表，用户可以更加轻松的将 StarRocks 打造为数据生态中的统一查询入口，并拓展更加丰富的联合查询能力。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>5、</strong><span style="color:#000000">数据目录 Catalog</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">一方面，StarRocks 为了更好地支撑湖仓一体的管理场景，面向内部数据和外部数据带来统一管理和轻松访问的用户体验，提供了外部数据目录（External Catalog）功能：通过外部数据目录来绑定某个数据源后，用户无需创建外表即可直接分析其中的数据（例如 Apache Hive 等）；</span><span style="background-color:#ffffff; color:#222222">另一方面，我们在实现各类数据源的 Catalog 时，使用了重新抽象的代码框架 （Datasource Connector），为后续社区开发者针对各类数据源进行接入时提供了更加轻松的开发体验。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="background-color:#ffffff; color:#222222">相比于原外表的使用方式，用户无需手动配置表名以及结构信息，大幅度简化了数据接入成本；同时数据目录可以让仓中数据（StarRocks）和湖中数据（如 Apache Hive 等）的访问管理一体化，使用更加便捷。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>6、</strong><span style="color:#000000">集群部署与管理工具 StarGo</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">在 2.3 版本之前，对于 StarRocks 社区版用户，只能通过手动的方式部署和管理集群，这带来了如下痛点：1）用户需要登录不同的服务器来管理多个 StarRocks 实例；2）在维护多套集群时，我们需要通过手工记录的方式来维护集群与机器的关系。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#222222">StarGo 是 StarRocks 社区孵化的多集群管理工具，从 2.3 版本开始以开源方式发布了预览版，帮助用户在中控机上管理维护不同的 StarRocks 集群。StarGo 使用 Golang 编写，不依赖于其他的组件，无需安装，下载解压即可用。在 StarGo 中，用户使用命令行 + 配置文件的使用模式，即可快速完成集群的部署、启动、停止、销毁、弹性扩缩容、升级以及管理 StarRocks 集群参数。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>7、</strong><span style="color:#000000">其他特性与优化</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">默认开启 Pipeline 执行引擎</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">主键模型支持持久化主键索引，避免主键索引占用过大内存空间</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">全局低基数字典优化支持实时数据导入，实时场景下低基数的字符串类型数据的查询性能提升一倍</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">优化 Compaction 机制，对较大的元数据进行 Compaction 操作，避免因数据高频更新而导致短时间内元数据挤压、占用较多磁盘空间</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">优化导入 Parquet 文件和压缩文件格式的性能</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">优化创建物化视图的性能，在部分场景下创建速度提升近 10 倍</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">支持监控资源组，可在审计日志中查看查询所属的资源组，并通过相关 API 获取资源组的监控信息</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">Apache Iceberg 外表功能，创建 Iceberg 资源时支持使用自定义 Catalog</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">ElasticSearch 外表功能，支持取消探测 ElasticSearch 集群数据节点的地址</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">当 sum () 中输入的值为 String 类型且为数字时，则自动进行隐式转换</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">year、month、day 函数支持 DATE 数据类型</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">新增如下函数：</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="background-color:#ffffff; color:#222222">  - window_funnel</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="background-color:#ffffff; color:#222222">  - ntile</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="background-color:#ffffff; color:#222222">  - bitmap_union_count 、array_to_bitmap、base64_to_bitmap</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="background-color:#ffffff; color:#222222">  - time_slice</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">week 函数完善</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span style="background-color:#ffffff; color:#222222">支持在 AWS 上使用 CloudFormation 快速创建 StarRocks 集群</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#338393"><strong><span>在这个版本中，</span></strong></span><span style="color:#fccd4d"><strong><span style="color:#fccd4d">91 </span></strong></span><span style="color:#338393"><strong><span>位贡献者共提交 </span></strong></span><span style="color:#fccd4d"><strong><span>787 </span></strong></span><span style="color:#338393"><strong><span style="color:#338393">个 Commits，感谢他们：</span></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#338393">@stdpain,@HangyuanLiu,@zhuxt2015,@decster,@stephen-shelby,@sevev,@trueeyu,@DorianZheng,@Linkerist,@Astralidea,@Youngwb,@xiaoyong-z,@mofeiatwork,@ZiheLiu,@Seaven,@rickif,@kangkaisen,@liuyehcf,@gengjun-git,@meegoo,@waittttting,@harui7890,@imay,@xlwh,@hongli-my,@wyb,@sduzh,@satanson,@caneGuy,@dirtysalt,@Pslydhh,@blackstar-baba,@silverbullet233,@RowenWoo,@zombee0,@mxdzs0612,@ABingHuang,@adzfolc,@mchades,@even986025158,@padmejin,@chen9t,@choury,@hiliuxg,@sym-liuyang,@chaoyli,@abc982627271,@MonsterChenzhuo,@xuzifu666,@wangxiaobaidu11,@only2yangcao,@miomiocat,@happut,@aaawuanjun,@wangruin,@Zhangruichao,@Crystal-LiuJing,@dreamay,@shyamrox,@itweixiang,@zddr,@zdsg1024,@goodqiang,@ylcq,@laotan332,@zbtzbtzbt,@long2ice,@liuqian1990,@wuleistarrocks,@dufeng1010,@mklzl,@chenyjsr,@DeepThinker666,@johndinh391,@karan-kap00r,@wanpengfei-git,@creatstar,@Gabriel39,@Ielihs,@hffariel,@SaintBacchus,@bigdata-kuxingseng,@staman96,@Johnsonginati,@Gri-ffin,@jsinwell,@DebayanSen96,@RishiKumarRay,@Ccuurryy,@wuqiao,@screnwei</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            