
---
title: 'Apache ShardingSphere 5.1.0 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b34e7245e8ca88744ab1376e23f519176b5.jpg'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 15:10:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b34e7245e8ca88744ab1376e23f519176b5.jpg'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p style="margin-left:0; margin-right:0">新年伊始，<strong>Apache ShardingSphere 迎来了今年的第一个版本的更新，5.1.0 版本正式发布。</strong>自去年 11 月 Apache ShardingSphere 5.0.0 GA 版本发布以来，ShardingSphere 正式开启了包含数据分片、分布式事务、数据脱敏、SQL 审计、数据库网关等为核心功能的分布式生态打造之路，同时自发布至今的 3 个多月时间里，ShardingSphere 社区也收到了来自各个领域的开发者、合作者以及用户等多方面的反馈，这些反馈为我们持续打磨产品带来了很大的帮助。本文将和大家详细介绍 Apache ShardingSphere 5.1.0 版本包含的更新内容。</p> 
</blockquote> 
<p style="color:#000000; margin-left:0px; margin-right:0px; text-align:left"><img alt height="225" src="https://oscimg.oschina.net/oscnet/up-b34e7245e8ca88744ab1376e23f519176b5.jpg" width="225" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">孟浩然，SphereEx 高级研发工程师，Apache ShardingSphere PMC。曾就职于京东科技，负责数据库产品研发，热爱开源，关注数据库生态，目前专注于 ShardingSphere 数据库中间件开发以及开源社区建设。</p> 
</blockquote> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">本次 5.1.0 版本的发布基于用户对 5.0.0 GA 版本的反馈以及 ShardingSphere 社区对生态打造的规划来共同推进，<strong>在内核以及各个功能模块都进行了重大的优化：</strong></p> 
<ul> 
 <li><strong>内核层面</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">打造强大且稳定的内核是 ShardingSphere 一直以来的目标，本次更新修复了大量包括 PostgreSQL 以及 openGauss SQL 解析的支持问题，开始支持函数解析、binlog 语句解析，优化改写引擎、大量单表加载效率，进一步提升内核整体性能，同时开始支持 SQL Hint 功能，为用户使用强制路由功能提供了更便捷的方式。</p> 
<ul> 
 <li><strong>接入端</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">在代理端，除了修复 MySQL/PostgreSQL 协议解析的问题之外，为 openGauss 新增 SCRAM SHA-256 认证方式支持，优化 openGauss 批量插入协议，提升数据批量插入性能；在 JDBC 端，移除对空规则的校验，在无规则情况下依然可以使用 JDBC，同时优化仅加载指定 schemaName 的逻辑数据库的元数据，提升启动速度。</p> 
<ul> 
 <li><strong>弹性伸缩</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">弹性伸缩在本次版本做了很大程度的调整，首先，原 scaling 模块调整为 kernel 下的 data-pipeline 模块，该模块未来将提供除数据迁移之外的其它的数据处理能力，其次 scaling 的配置也从<span> </span><code>server.yaml</code><span> </span>移动至<span> </span><code>config-sharding.yaml</code><span> </span>配置文件中，弹性伸缩将和数据分片一起配合使用，为用户提供更加完善的分库分表服务。</p> 
<ul> 
 <li><strong>DistSQL</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新增大量实用语法的实现，为用户管理 ShardingSphere 分布式数据库生态提供了更多的工具，同时优化了部分分布式集群治理的能力，如通过 instance_id 启用/禁用实例，当只有一个从库时，提示用户不能进行禁用等，大大提升了用户体验。</p> 
<ul> 
 <li><strong>读写分离和高可用</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">读写分离和高可用功能 API 均进行了优化，读写分离支持静态和动态 2 种配置类型，动态配置需要和高可用配合使用。高可用配置则进行了配置和算法分离，让配置更统一简洁，同时增加了 Spring Boot 和 Spring Namespace 对高可用功能的配置支持以及 openGauss 高可用功能的实现。</p> 
<ul> 
 <li><strong>影子库</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">影子库功能在本版本中也做了部分优化，支持逻辑数据源传递，为列匹配影子算法增加不支持数据类型校验器，注解影子算法重构为 HINT 影子算法，移除配置中的 enable 属性，同时优化了影子算法判定逻辑，提升性能。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">以上介绍的只是部分功能的部分更新内容，5.1.0 版本包含了来自社区 1000+ 的提交，<strong>在 5.0.0 GA 的基础上，对内核能力、核心功能、整体性能以及用户体验上都做了很大的提升，欢迎大家更新使用。</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">5.1.0 具体版本发布信息如下：</p> 
<h2>新特性</h2> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">支持 SQL Hint 功能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：新增限流配置及默认实现（rateLimiter）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：新增全量数据匹配校验算法（DATA_MATCH）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：新增数据读取批次大小自定义（readBatchSize）避免可能的 OOME</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：新增 sourceWritingStopAlgorithm SPI 接口及默认空实现，新增 sourceWritingStopper</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：新增 checkoutLockAlgorithm SPI 接口及默认空实现，新增配置 checkoutLocker</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：<code>config-encrypt.yaml</code><span> </span>新增<span> </span><code>dataConverters</code><span> </span>配置</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW AUTHORITY RULE</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW TRANSACTION RULE</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>ALTER TRANSACTION RULE</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW SQL_PARSER RULE</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>ALTER SQL_PARSER RULE</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>ALTER DEFAULT SHARDING STRATEGY</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>DROP DEFAULT SHARDING STRATEGY</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>CREATE DEFAULT SINGLE TABLE RULE</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW SINGLE TABLES</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW SINGLE TABLE RULES</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW SHARDING TABLE NODES</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>CREATE/ALTER/DROP SHARDING KEY GENERATOR</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW SHARDING KEY GENERATORS</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>REFRESH TABLE METEDATA</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>PARSE SQL</code>，输出解析 SQL 得到的抽象语法树</p> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW UNUSED SHARDING ALGORITHMS</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW UNUSED SHARDING KEY GENERATORS</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>CREATE/DROP SHARDING SCALING RULE</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>ENABLE/DISABLE SHARDING SCALING RULE</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW SHARDING SCALING RULES</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>SHOW INSTANCE MODE</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 DistSQL 语法：<code>COUNT SCHEMA RULES</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据库发现支持 Spring Boot 配置方式</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据库发现支持 Spring Namespace 配置方式</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据库发现新增支持 openGauss</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">影子库功能支持逻辑数据源传递</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">列匹配影子算法添加不支持数据类型校验器</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">脱敏单数据源场景下，提供 xa start/end/prepare/commit/recover 支持</p> </li> 
</ul> 
<h2>API 变更</h2> 
<ul> 
 <li>弹性伸缩：scaling 配置从<span> </span><code>server.yaml</code>移到<span> </span><code>config-sharding.yaml</code></li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：ScalingClusterAutoSwitchAlgorithm 接口重命名、方法参数重构</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：数据一致性校验 API 方法重命名及返回类型修改</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：重新设计数据库发现相关的 DistSQL 语法</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：GENERATED_ KEY 关键字调整为 KEY_ GENERATE_STRATEGY</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Native authority provider 已标记为弃用，将在未来版本中移除</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据库发现模块 API 重构，配置和算法分离</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">读写分离模块 API 重构，增加静态和动态配置</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">影子库 API 变更，移除<span> </span><code>enable</code><span> </span>属性</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">影子库 API 变更， 影子算法类型变更</p> </li> 
</ul> 
<h2>增强</h2> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">提升大量单表加载性能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">删除自动添加的<span> </span><code>order by</code><span> </span>子句</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化绑定表关联查询不带分片关联条件的路由逻辑</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持路由结果不变时 update 语句更新分片键</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化改写引擎执行性能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用 federation 引擎支持<span> </span><code>select union/union all ...</code>语句</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持路由结果不变时<span> </span><code>insert on duplicate key update</code><span> </span>语句更新分片键</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用<span> </span><code>UNION ALL</code><span> </span>改写简单查询语句的 SQL 路由结果以提升性能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Proxy 支持 autocommit 状态</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">ShardingSphere-Proxy openGauss 支持 SCRAM SHA-256 认证方式</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">从 Proxy 启动脚本移除属性 java.net.preferIPv4Stack=true</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JDBC 端去掉对空规则的校验</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 openGauss 批量插入协议性能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">默认禁用 Netty 泄漏探测器</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">PostgreSQL / openGauss Proxy 支持 Describe Prepared Statement</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">PostgreSQL Proxy 数据批量插入性能优化</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：DataConsistencyChecker 初步支持流式数据校验</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：<code>SHOW INSTANCE LIST</code><span> </span>的结果中增加 instance_id</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：启用/禁用 proxy 实例时可使用 instance_id 进行操作</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：<code>CREATE SHARDING TABLE RULE</code>时支持自动创建算法，减少创建 RULE 步骤</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">DistSQL：<code>CREATE SHARDING TABLE RULE</code>时支持指定已存在的 KeyGenerator</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">DistSQL：<code>DROP DATABASE</code><span> </span>支持 IF EXISTS 选项</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">DistSQL：<code>SHARDING TABLE RULE</code><span> </span>中的 DATANODES 支持枚举形式的 inline 表达式</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">DistSQL：<code>CREATE/ALTER SHARDING TABLE RULE</code>支持复合分片算法</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">DistSQL：<code>SHOW SHARDING TABLE NODES</code>支持非 inline 场景（范围、时间等）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：当读写分离规则中仅存一个读库时，不允许禁用</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">影子算法判定逻辑优化，提升性能</p> </li> 
</ul> 
<h2>重构</h2> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">重构 Federation 引擎内部流程</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用预备语句请求 Proxy 时避免事务语句被解析多次</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：scaling 模块重构到 pipeline 模块</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：scaling job 配置结构多处调整</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：预计算任务拆分并保存到 job 配置，简化实现</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：pipeline-core 初步支持 encrypt 复用流程</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：初步支持 scaling 和 encrypt 同时进行</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：新增 input 和 output 配置，workerThread 和 rateLimiter 移入其中</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：blockQueueSize 移入 streamChannel</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：jobId 类型从整型调整为字符型</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 JDBC 只加载指定逻辑库</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化注册中心原数据存储结构</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">注解影子算法重构为 HINT 影子算法</p> </li> 
</ul> 
<h2>漏洞修复</h2> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">支持函数解析</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 alter table drop constrian 语句</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 optimize table 语句路由</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持 resource group 语句的路由</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持解析 binlog 语句</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持 PostgreSQL / openGauss '与'和'或' 运算</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持解析 openGauss insert on duplicate key 语法</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持 PostgreSQL / openGauss union 解析</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复查询字段中包含关键字的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 function 解析参数的异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复子查询没有别名查询异常的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 utc timestamp 函数解析异常的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 alter column 加解密异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持 alter column with position encrypt column 的加解密异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 PostgreSQL 支持 delete with schema</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 Oracle 解析歧义导致的路由结果异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复使用分片、加解密功能时 projection count 错误问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复使用影子库、读写分离出现的 NPE 问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复真实表大小写敏感导致的元数据错误</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复加解密多表关联查询改写异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复加解密表级别 queryWithCipherColumn 参数导致的改写异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复中文解析</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 exists 子查询加密异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复分片条件中出现 MySQL BINARY 关键字导致的全路由</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复使用 JDBCMemoryQueryResult 处理的语句时，getResultSet 方法结果为空异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复创建存储函数/过程时，错误的分片表校验逻辑</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复部分客户端连接 PostgreSQL Proxy 报 Charset 为 null 的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 MySQL 使用 PreparedStatement 执行 commit 导致事务状态不正确的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 PostgreSQL 以非英文语言返回错误信息会导致 Proxy 无法返回正确的数据给客户端</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复在 Windows 环境下，Proxy 加载路径包含空格的配置文件会报错</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 Proxy flush 时机过早导致事务状态不正确的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 Proxy 无法正确返回二进制无符号数值的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 MySQL Proxy PreparedStatement 协议实现不正确的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复非事务中 openGauss 执行批量插入协议持有过多连接的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：修复 XA 初始化连接泄露问题，数据校验会触发</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：PostgreSQL 多数据源情况下复制流绑定异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：PostgreSQL 增量同步阶段 update 记录导致同步报错</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：修复 MySQL 5.5 检查 BINLOG<em>ROW</em>IMAGE 报错</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">弹性伸缩：DataConsistencyChecker 修复 PostgreSQL xml 数据类型校验失败</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：修复数据库发现和读写分离共用时，SHOW READWRITE_SPLITTING RULES 数据缺失问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：修复数据库发现和读写分离共用时，<code>SHOW READWRITE_SPLITTING READ RESOURCES</code>数据缺失的问题</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">DistSQL：修复<span> </span><code>CREATE SHARDING TABLE RULE</code><span> </span>语句未指定分库、分表策略时的空指针异常</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">DistSQL：修复<span> </span><code>PREVIEW SQL by schema.table</code><span> </span>时发生 NPE 的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：修复 DISABLE 语句在某些情况下可能禁用读写分离主库的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DistSQL：修复 DISABLE INSTANCE 在某些情况可能禁用当前实例的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复当 provider 为 SCHEMA<em>PRIVILEGES</em>PERMITTED 时，用户可能查询到未授权的逻辑库的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复当 authority provider 未配置时，发生 NPE 的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复数据库发现无法修改 cron 配置</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复读写分离权重算法单读节点时异常</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复非 Memory 模式下创建多余数据源问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复列值匹配影子算法数据类型转换异常</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">🔗<span> </span><strong>下载链接：</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2Fdocument%2Fcurrent%2Fcn%2Fdownloads%2F" target="_blank">https://shardingsphere.apache.org/document/current/cn/downloads/</a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">🔗<span> </span><strong>更新日志：</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fshardingsphere%2Fblob%2Fmaster%2FRELEASE-NOTES.md" target="_blank">https://github.com/apache/shardingsphere/blob/master/RELEASE-NOTES.md</a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">🔗<span> </span><strong>项目地址：</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2F" target="_blank">https://shardingsphere.apache.org/</a></p> 
<h2>社区建设</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此次 Apache ShardingSphere 5.1.0 版本的发布，共有<span> </span><strong>66 位 Contributor 提交了 1148 个 PR，</strong>感谢社区伙伴们的大力支持。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">欢迎大家测试使用 ShardingSphere 5.1.0，同时欢迎大家参与社区讨论！</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img align="left" alt height="225" src="https://oscimg.oschina.net/oscnet/up-faa09c2b26e9b752f1656ea1a89e98aceba.png" width="300" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            