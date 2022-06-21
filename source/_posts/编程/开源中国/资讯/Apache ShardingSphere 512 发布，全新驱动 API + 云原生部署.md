
---
title: 'Apache ShardingSphere 5.1.2 发布，全新驱动 API + 云原生部署'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-301296854faa5b9f146326b716fea5f1c12.png'
author: 开源中国
comments: false
date: Tue, 21 Jun 2022 03:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-301296854faa5b9f146326b716fea5f1c12.png'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p style="margin-left:0px; margin-right:0px; text-align:start"><span><span> </span>在 Apache ShardingSphere 5.1.1 发布后，ShardingSphere 合并了来自全球的团队或个人的累计 1028 个 PR，为大家带来 5.1.2 新版本。该版本在功能、性能、测试、文档、示例等方面均有不少优化。</span></p> 
</blockquote> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-left:5px; margin-right:10px"> 
  <div style="margin-left:0; margin-right:0; text-align:start"> 
   <div style="margin-left:0; margin-right:0; text-align:justify"> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>值得一提的是，本次更新带来了以下全新功能：</span></p> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><strong><span style="color:#e36c09">ShardingSphere-Proxy Helm Chart</span></strong></p> </li> 
    </ul> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><strong><span style="color:#e36c09">SQL 方言翻译</span></strong></p> </li> 
    </ul> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><strong><span style="color:#e36c09">以 Driver 形式使用 ShardingSphere-JDBC</span></strong></p> </li> 
    </ul> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><strong><span>这些全新的能力让 ShardingSphere 的数据网关能力得到了质的提升，助力 ShardingSphere 在云上部署，优化用户体验。</span></strong></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>除了上述新功能，本次更新大量提升了 SQL 解析支持度，内核、运行模式、弹性伸缩都完善了对 PostgreSQL / openGauss schema 的支持，弹性伸缩、事务、DistSQL 在健壮性与用户体验方面也有不少提升。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>本篇将给大家介绍 ShardingSphere 5.1.2 版本更新内容。</span></p> 
    <h3><strong><span>新功能介绍</span></strong></h3> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li> <h4 style="margin-left:5px; margin-right:5px; text-align:justify"><span style="color:#e36c09"><strong><span>使用 Helm 部署 ShardingSphere-Proxy</span></strong></span></h4> </li> 
    </ul> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>ShardingSphere-Proxy 提供了 Docker 镜像以便于用户容器化部署。不过，对于需要在 Kubernetes 部署 ShardingSphere-Proxy 的用户，还需要自行处理数据库驱动挂载、配置挂载、自定义算法挂载等必要步骤，部署过程相对繁琐，运维成本相对较高。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>ShardingSphere 本次更新带来了全新的 ShardingSphere-Proxy Helm Chart。</span><strong><span>这项新功能由企业级、云原生数据增强计算产品及解决方案提供商 SphereEx 向 Apache ShardingSphere 社区捐赠，</span></strong><span>推动 Apache ShardingSphere 在云原生方向前进。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:center"><img alt height="388" src="https://oscimg.oschina.net/oscnet/up-301296854faa5b9f146326b716fea5f1c12.png" width="700" referrerpolicy="no-referrer"><img alt="Image" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" referrerpolicy="no-referrer"></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>ShardingSphere 在集群模式下依赖注册中心存储元数据，ShardingSphere-Proxy 的 Helm Chart 能够自动部署 ZooKeeper 集群，帮助用户快速搭建 ShardingSphere-Proxy 集群。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>受限于开源协议，ShardingSphere-Proxy 的二进制发布包、Docker 镜像受限于开源协议，无法打包 MySQL JDBC 驱动，用户需要手动添加 MySQL JDBC 驱动到 classpath 才能使用 MySQL 作为 ShardingSphere 的存储节点。对于这类情况，ShardingSphere-Proxy Helm Chart 能够在 Pod 的 Init 容器自动获取 MySQL JDBC 驱动，降低了用户的部署操作成本。</span></p> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li> <h4 style="margin-left:5px; margin-right:5px; text-align:justify"><strong><span style="color:#e36c09">全新 SQL 方言翻译能力</span></strong></h4> </li> 
    </ul> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>随着数据库碎片化趋势的不可逆转，多种类型数据库的共存已渐成常态。使用一种 SQL 方言访问异构数据库的场景在不断增加。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>多样化的数据库的存在，使访问数据库的 SQL 方言难于标准化，工程师需要针对不同种类的数据库使用不同的方言，缺乏统一化的查询平台。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>将不同类型的数据库方言自动翻译为后端数据库所使用的方言，让工程师可以使用任意一种数据库方言访问所有的后端异构数据库，可以极大地降低开发和维护成本。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>Apache ShardingSphere 5.1.2 在打造极具生产力的数据网关的路途中迈出了重要的一步。本次更新带来了全新的 SQL 方言翻译能力，能够支持主流开源数据库之间的方言转换。例如，用户可以使用 MySQL 客户端连接 ShardingSphere-Proxy 并发送基于 MySQL 方言的 SQL，ShardingSphere 能自动识别用户协议与存储节点类型，自动完成 SQL 方言转换，访问 PostgreSQL 等异构存储节点，反之亦然。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:center"><img alt height="250" src="https://oscimg.oschina.net/oscnet/up-652c8ab0a0c90d724b8e2ebec56e41e71c1.png" width="800" referrerpolicy="no-referrer"></p> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li> <h4 style="margin-left:5px; margin-right:5px; text-align:justify"><strong><span style="color:#e36c09">以 Driver 的形式使用 ShardingSphere-JDBC</span></strong></h4> </li> 
    </ul> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>在过去的 ShardingSphere 版本中，ShardingSphere-JDBC 以 DataSource 的形式向用户提供服务。对于不使用 DataSource 的项目或工具，需要进行改造才能引入 ShardingSphere-JDBC，增加了用户的使用成本。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>在 Apache ShardingSphere 5.1.2 中，ShardingSphere-JDBC 实现了标准的 JDBC Driver 接口，用户可以通过 Driver 的形式引入 ShardingSphere-JDBC。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>用户可以直接通过 DriverManager 获取 Connection：</span></p> 
    <pre><code class="language-java">Class.forName("org.apache.shardingsphere.driver.ShardingSphereDriver");
Connection conn = DriverManager.getConnection("jdbc:shardingsphere:classpath:config.yaml");</code></pre> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>也可以使用 DataSource 获取 Connection：</span></p> 
    <pre><code class="language-java">// 以 HikariCP 为例
HikariDataSource dataSource = new HikariDataSource();
dataSource.setDriverClassName("org.apache.shardingsphere.driver.ShardingSphereDriver");
dataSource.setJdbcUrl("jdbc:shardingsphere:classpath:config.yaml");
Connection conn = dataSource.getConnection();</code></pre> 
    <h3><strong><span>对已有能力的提升</span></strong></h3> 
    <h4><span><strong>内核</strong></span></h4> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>本次更新，ShardingSphere 合并了大量提升 SQL 解析支持度的 PR，在更新日志中可见 SQL 解析的优化项占了较大篇幅。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>ShardingSphere 在 5.1.1 对 PostgreSQL / openGauss 的 schema 提供了初步支持，在本次 5.1.2 更新，内核、集群模式、弹性伸缩对 PostgreSQL / openGauss 的 schema 的支持度也有所提升，例如元数据对增加了对 schema 结构的支持，内核、弹性伸缩支持自定义 schema。</span></p> 
    <h4><span><strong>ShardingSphere-Proxy</strong></span></h4> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>随着使用 ARM 架构 CPU 的服务器市场渐成气候，ShardingSphere-Proxy 在 Docker 方面也提供了适用于 arm64 架构的镜像。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>在 MySQL 方面，ShardingSphere-Proxy 修复了无法接收长度超过 8 MB 数据包的问题，并支持接收总长度超过 16 MB 的数据。</span></p> 
    <h4><span><strong>弹性伸缩</strong></span></h4> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩在除了支持 PostgreSQL 自定义 schema 外，也实现了迁移 PostgreSQL 时自动建表的功能，并修复了 PostgreSQL 增量迁移遇到 `null` 字段值会报错的问题。除功能方面，弹性伸缩还减少了迁移过程中的资源占用，以及对 openGauss 3.0 增量迁移提供了支持。</span></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>欢迎大家使用或升级 ShardingSphere 5.1.2，ShardingSphere 社区期待您的反馈！</span></p> 
    <h3><strong><span>更新日志</span></strong></h3> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>以下为 ShardingSphere 5.1.2 的全部更新日志。需要注意的是，本次更新调整了少量 API，调整项请参考本文更新日志的 API 调整部分。</span></p> 
    <h4><span><strong>新特性</strong></span></h4> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 MySQL 和 PostgreSQL 的 SQL 方言转换的 alpha 版本</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 PostgreSQL 和 openGauss 自定义 schema</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 PostgreSQL 和 openGauss create/alter/drop view 语句</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 openGauss cursor 语句</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持使用自定义系统库</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持获取 openGauss 和 MySQL 的创建表语句</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持获取 PostgreSQL 的创建表语句</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：正式支持使用 Helm 在 Kubernetes 中快速部署一个包含 ZooKeeper 集群的 ShardingSphere-Proxy 集群</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：支持 ShardingSphere JDBC Driver</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：支持 PostgreSQL 自动建表</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：支持 PostgreSQL 和 openGauss 自定义 schema 的表迁移</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：支持字符串主键表迁移</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>运行模式：治理中心支持 PG/openGauss 三级结构</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>运行模式：治理中心支持 Database 级别的分布式锁</span></p> </li> 
    </ul> 
    <h4><span><strong>优化</strong></span></h4> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 PostgreSQL 和 openGauss copy 语句</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 PostgreSQL 的 alter/ drop index 语句</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 MySQL update force index 语句</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 openGauss create/alter/drop schema 语句</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:left"><span>内核：优化 RoundRobinReplicaLoadBalanceAlgorithm 和 RoundRobinTrafficLoadBalanceAlgorithm 算法逻辑</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：优化在前端驱动数据库类型和后端不一致时元数据加载逻辑</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：重构元数据加载逻辑</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：show processlist 语句功能性能优化</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：提升大量表场景下的加载性能</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 comment 语句的执行</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 PostgreSQL 和 openGauss 分片场景下的 view 语句的执行</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持 ORACLE 的 CREATE ROLLBACK SEGMENT 语句</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss DROP TYPE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss ALTER TYPE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle DROP DISKGROUP</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE DISKGROUP</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle DROP FLASHBACK ARCHIVE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss CHECKPOINT</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE FLASHBACK ARCHIVE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL Close</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss DROP CAST</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss CREATE CAST</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE CONTROL FILE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss DROP DIRECTORY</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss ALTER DIRECTORY</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss CREATE DIRECTORY</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL Checkpoint</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss DROP SYNONYM</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss CREATE SYNONYM</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 openGauss ALTER SYNONYM</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL CALL Statement</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE PFILE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE SPFILE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle ALTER SEQUENCE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE CONTEXT</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle ALTER PACKAGE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE SEQUENCE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle ALTER ATTRIBUTE DIMENSION</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle ALTER ANALYTIC VIEW</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：使用 ShardingSphere Spi 加载 SQLVisitorFacade</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：使用 ShardingSphere Spi 加载 DatabaseTypedSQLParserFacade</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle ALTER OUTLINE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle DROP OUTLINE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle drop edition</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 SQLServer WITH Common Table Expression</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：优化 SubquerySegment 在 with 语句中的开始和结束索引</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：重构 JoinTableSegment</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle DROP SYNONYM</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE DIRECTORY</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE SYNONYM</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 SQLServer XmlNamespaces Clause</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle Alter Database Dictionary</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 SQLServer Clause of SELECT Statement</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle ALTER DATABASE LINK</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle CREATE EDITION</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle ALTER TRIGGER</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 SQLServer REVERT Statement</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL DROP TEXT SEARCH</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL drop server</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle ALTER VIEW</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL drop access method</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL DROP ROUTINE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 SQLServer DROP USER</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle DROP TRIGGER</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL Drop subscription</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL drop operator class</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL DROP PUBLICATION</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle DROP VIEW</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL DROP TRIGGER</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 Oracle DROP DIRECTORY</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL DROP STATISTICS</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL drop type</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL DROP RULE</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 SQLServer ALTER LOGIN</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL DROP FOREIGN DATA WRAPPER</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：支持解析 PostgreSQL DROP EVENT TRIGGER statement</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：ShardingSphere-Proxy MySQL 支持接收长度超过 16 MB 的请求数据包</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：ShardingSphere-Proxy 增加 SO_BACKLOG 配置项</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：ShardingSphere-Proxy 默认启用 SO_REUSEADDR</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：ShardingSphere-Proxy Docker image 增加 aarch64 支持</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：ShardingSphere-Proxy MySQL 支持配置默认 MySQL 版本号</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：ShardingSphere-Proxy PostgreSQL / openGauss 支持更多字符集</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：ShardingSphere-Proxy 增加默认端口配置项</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：openGauss 3.0 启用 thread_pool 时，Scaling 兼容 HA port 进行数据同步</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：优化 PipelineJobExecutor 中 Zookeeper 事件处理的逻辑，避免 zk 阻塞事件</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：Scaling 数据同步不区分表名大小写</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：改进 PostgreSQL/openGauss 复制槽清理</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：改进准备阶段锁保护</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：改进 PostgreSQL 同一记录删除后重建场景下的数据同步</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：Scaling 创建的数据源在底层不缓存</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：尽量复用数据源，减少数据库连接占用</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>DistSQL：REFRESH TABLE METADATA 支持指定 PostgreSQL's schema</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>DistSQL：ALTER SHARDING TABLE RULE 时增加对绑定表的校验</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>运行模式：ShardingSphere-JDBC 支持配置数据库连接名</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>分布式事务：事务中禁止执行 DistSQL</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>分布式事务：autocommit = 0, DDL 部分 DML 会自动开启事务</span></p> </li> 
    </ul> 
    <h4><span><strong>问题修复</strong></span></h4> 
    <div> 
     <div> 
      <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：修复 PostgreSQL 和 openGauss show 语句解析异常</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：修复 PostgreSQL 和 openGauss time extract function 解析异常</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：修复 PostgreSQL 和 openGauss select mod fucntion 解析异常</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：修复读写分离场景下多 schema join 语句的执行异常</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：修复加密场景下执行 create schema 语句的路由异常</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：修复 drop schema if exist 语句的异常</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：修复执行 LAST_INSERT_ID() 路由错误</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：修复 use database 在无数据源状态下执行异常的问题</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>内核：修复带有 set var 的 fucntion 创建语句</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：修复 ShardingSphere-Proxy PostgreSQL / openGauss Describe PreparedStatement 因字段大小写不匹配导致的空指针</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>接入端：修复 ShardingSphere-Proxy PostgreSQL / openGauss 执行 schema DDL 后没有返回正确 tag 的问题</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：修复 MySQL unsigned 类型在 Scaling 过程中出错</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：修复一致性检查创建数据源失败时产生连接泄漏的问题</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：修复 ShardingSphereDataSource 初始化忽略分片以外规则的问题</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：支持 job 在准备阶段被关闭</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：修复数据源 url 和 jdbcurl 兼容性问题</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：修复 openGauss 数据复制槽创建时机问题，避免可能的增量数据丢失</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：改进 job 状态持久化，确保特殊情况下不会被覆盖为老状态</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：修复 PostgreSQL 使用 TestDecoder 进行增量迁移时无法正确解析 `null`</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>DistSQL：修复单机和内存模式下，SET VARIABLE 修改不生效的问题</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>DistSQL：修复 SHOW INSTANCE LIST 与实际数据不一致的问题</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>DistSQL：修复分片规则大小写敏感的问题</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>运行模式：修复 Scaling 功能更改分表规则后新版本元数据丢失数据</span></p> </li> 
       <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>分布式事务：修复根据 catalog 获取 indexinfo 为空问题</span></p> </li> 
      </ul> 
     </div> 
    </div> 
    <h4><span><strong>重构</strong></span></h4> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>弹性伸缩：重构 jobConfig，方便新类型 job 复用及扩展</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>运行模式：优化注册中心计算节点存储结构</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>运行模式：使用 uuid 替代 ip@port 作为实例唯一标识</span></p> </li> 
    </ul> 
    <h4><span><strong>API 调整</strong></span></h4> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>DistSQL：EXPORT SCHEMA CONFIG 调整为 EXPORT DATABASE CONFIG</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>DistSQL：IMPORT SCHEMA CONFIG 调整为 IMPORT DATABASE CONFIG</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>运行模式：调整 db-discovery 算法配置</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>DistSQL：SHOW SCHEMA RESOURCES 调整为 SHOW DATABASE RESOURCES</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>DistSQL：COUNT SCHEMA RULES 调整为 COUNT DATABASE RULES</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:left"><span>权限：权限提供者 `ALL_PRIVILEGES_PERMITTED` 更新为 `ALL_PERMITTED`</span></p> </li> 
     <li> <p style="margin-left:5px; margin-right:5px; text-align:left"><span>权限：权限提供者 `SCHEMA_PRIVILEGES_PERMITTED` 更新为 `DATABASE_PERMITTED`</span></p> </li> 
    </ul> 
    <h3><strong><span>相关链接</span></strong></h3> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>🔗<span> </span></span><strong><span>下载链接：</span></strong></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2Fdocument%2Fcurrent%2Fcn%2Fdownloads%2F" target="_blank"><span>https://shardingsphere.apache.org/document/current/cn/downloads/</span></a></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>🔗</span><strong><span><span> </span>更新日志：</span></strong></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fshardingsphere%2Fblob%2Fmaster%2FRELEASE-NOTES.md" target="_blank"><span>https://github.com/apache/shardingsphere/blob/master/RELEASE-NOTES.md</span></a></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>🔗</span><strong><span><span> </span>项目地址：</span></strong></p> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2F" target="_blank"><span>https://shardingsphere.apache.org/</span></a></p> 
    <h3><strong><span>社区建设</span></strong></h3> 
    <p style="margin-left:0; margin-right:0; text-align:justify"><span>此次 Apache ShardingSphere 5.1.2 版本的发布，共有 54 位 Contributor 提交了 1028 个 PR，感谢社区伙伴们的大力支持。</span></p> 
    <p style="margin-left:0px; margin-right:0px; text-align:center"><img alt height="600" src="https://oscimg.oschina.net/oscnet/up-42721064e4d09b40e3e68749cfb462d34e2.png" width="800" referrerpolicy="no-referrer"></p> 
    <h1 style="margin-left:5px; margin-right:5px; text-align:justify"><strong><span>作者</span></strong></h1> 
    <p style="margin-left:5px; margin-right:5px; text-align:justify"><span>吴伟杰，SphereEx 基础设施研发工程师，Apache ShardingSphere PMC。专注于 Apache ShardingSphere 接入端及 ShardingSphere 子项目 ElasticJob 的研发。<span> </span></span></p> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            