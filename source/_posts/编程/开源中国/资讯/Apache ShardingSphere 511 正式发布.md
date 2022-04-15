
---
title: 'Apache ShardingSphere 5.1.1 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static001.geekbang.org/infoq/32/323fb4445f6d77909531a8867b8ec0dc.png'
author: 开源中国
comments: false
date: Fri, 15 Apr 2022 08:41:00 GMT
thumbnail: 'https://static001.geekbang.org/infoq/32/323fb4445f6d77909531a8867b8ec0dc.png'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p>在 Apache ShardingSphere 5.1.0 发布后不足两个月的时间里，ShardingSphere 合并了来自全球的团队或个人的累计 698 个 PR，为大家带来 5.1.1 新版本。该版本在功能、性能、测试、文档、示例等方面均有不少优化。</p> 
 <p>特别是性能方面，采用业界标准的 TPC-C 测试模型，在 16 台物理服务器上运行 Apache ShardingSphere 5.1.1 与国产数据库 openGauss 3.0，取得超过 1000 万 tpmC 的优异成绩，行业同等规模下性能最好！</p> 
 <p>本文将给大家介绍 ShardingSphere 5.1.1 版本更新内容。</p> 
</blockquote> 
<p><strong>作者介绍：</strong>吴伟杰，SphereEx 基础设施研发工程师，Apache ShardingSphere PMC。目前专注于 Apache ShardingSphere 接入端及 ShardingSphere 子项目 ElasticJob 的研发。</p> 
<p><strong>本次 Apache ShardingSphere 5.1.1 版本更新主要是对 5.1.0 版本的功能与性能进行优化及问题修复，接下来将介绍部分更新内容。</strong></p> 
<h2>内核相关</h2> 
<p>内核是 ShardingSphere 的基础，打造功能完备、稳定、高性能的内核是 ShardingSphere 不变的目标。在 5.1.1 中，ShardingSphere 在内核层面优化了很多逻辑，修复了数据分片、读写分离、数据加密等场景在上一版本中发现的问题，并使各个场景在性能方面均有不同程度的提升。</p> 
<p>在数据库方言方面，内核增加了对 MySQL 表空间的支持，并提升了对 Oracle、SQL Server、PostgreSQL、openGauss 等数据库的 SQL 支持度。另外，ShardingSphere 内核也实现了对 PostgreSQL/openGauss 的 schema 这类三层结构的初步支持，后续版本会持续完善。</p> 
<h2>接入端</h2> 
<p>本次更新修复了 ShardingSphere-JDBC 的一个潜在性能问题风险点，优化了 ShardingSphere-JDBC 内部与数据库连接池非必需的交互逻辑，减少了 ShardingSphere-JDBC 的性能开销。</p> 
<p>在 ShardingSphere-Proxy 方面，MySQL/PostgreSQL 数据类型的支持度有所提升。ShardingSphere-Proxy MySQL 偶发性的 ResultSet closed 报错问题被修复，除此之外，ShardingSphere-Proxy MySQL 在协议层也初步支持执行多语句以提升批量操作性能。</p> 
<p>在客户端支持度方面，ShardingSphere-Proxy PostgreSQL 提升了对 PostgreSQL JDBC Driver 42.3.x 的支持度，ShardingSphere-Proxy openGauss 提升了对 openGauss JDBC Driver 3.0 的支持度。</p> 
<h2>弹性伸缩</h2> 
<p>在本次更新中，除了修复迁移作业报错后无法通过 DistSQL 重启的问题外，弹性伸缩的健壮性有所提升，并且实现了源端停写及恢复写、部分表扩缩容的新特性。对于不符合迁移条件的情况，弹性伸缩能够快速失败，及时发现抛出问题，避免用户付出额外的时间成本。</p> 
<h2>DistSQL</h2> 
<p>DistSQL 在用户体验方面进行了优化，增加了更多的校验，减少了用户在使用 DistSQL 中配置出错的可能性。同时修复了部分用户输入与 DistSQL 关键字冲突的问题。</p> 
<h2>分布式治理</h2> 
<p>在读写分离与数据库发现方面，除了原有的 MGR，MySQL 新增了通过查询主从延时实现的数据库发现方式，可以通过获取从库延时自动切换读写分离数据源，减少用户使用动态读写分离的门槛。</p> 
<p>在集群模式下，元数据存储结构进行了一定的优化与重构，因 ZooKeeper 会话超时、表名大小写不匹配等原因导致的问题均已被修复。</p> 
<h2>分布式事务</h2> 
<p>在事务方面，ShardingSphere-JDBC 新增了对 Savepoint 的支持，ShardingSphere-Proxy 则在原有对 LOCAL 事务 Savepoint 支持的基础上，增加了在 XA 场景下对 Savepoint 的支持。</p> 
<p>使用 Narayana 作为 XA 的实现时，ShardingSphere 能够配置 Narayana，让用户使用 XA 更方便。</p> 
<p>使用 PostgreSQL/openGauss 时，当在事务中发生异常，ShardingSphere 能够正确中止事务并自动回滚。</p> 
<p>以上是对 Apache ShardingSphere 5.1.1 部分更新内容的介绍，详细内容可以参考更新日志，后续 ShardingSphere 社区会发布对部分功能特性的详细解读，敬请期待。<strong>ShardingSphere 5.1.1 在 API 层面没有变动，在功能、性能方面均有不少提升，欢迎大家升级使用。</strong></p> 
<h1>更新日志</h1> 
<h2>新特性</h2> 
<ul> 
 <li> <p>内核：PostgreSQL 支持 <code>alter materialized view</code></p> </li> 
 <li> <p>内核：PostgreSQL 支持 <code>declare</code> 语法</p> </li> 
 <li> <p>内核：PostgreSQL 支持 <code>discard</code> 语法</p> </li> 
 <li> <p>内核：PostgreSQL 支持 <code>$$</code> 标识</p> </li> 
 <li> <p>内核：支持 MySQL 创建表空间语句</p> </li> 
 <li> <p>弹性伸缩：实现源端停写及恢复写</p> </li> 
 <li> <p>弹性伸缩：支持部分表扩缩容</p> </li> 
 <li> <p>DistSQL：新增语法 <code>SHOW UNUSED RESOURCES</code></p> </li> 
 <li> <p>分布式治理：治理中心新增持久化 XA Recovery Id</p> </li> 
 <li> <p>分布式治理：数据库发现新增延迟主从延迟功能</p> </li> 
 <li> <p>分布式事务：ShardingSphere-Proxy 支持 savepoint</p> </li> 
 <li> <p>分布式事务：PostgreSQL & openGauss 事务块内异常，自动回滚</p> </li> 
 <li> <p>分布式事务：Narayana XA 事务易用性</p> </li> 
 <li> <p>分布式事务：ShardingSphere-JDBC 支持 savepoint</p> </li> 
</ul> 
<h2>优化</h2> 
<ul> 
 <li> <p>内核：重构内核功能代码提升性能</p> </li> 
 <li> <p>接入端：减少 ShardingSphere-Proxy Docker 镜像体积</p> </li> 
 <li> <p>接入端：ShardingSphere-Proxy 支持使用 <code>set names</code> 等语句设置字符编码</p> </li> 
 <li> <p>接入端：ShardingSphere-Proxy MySQL 支持批量语句</p> </li> 
 <li> <p>接入端：ShardingSphere-Proxy 支持 openGauss JDBC Driver 3.0 客户端</p> </li> 
 <li> <p>弹性伸缩：在 ShardingSphere-Proxy 集群中只有一个 Proxy 节点需要做完成检测</p> </li> 
 <li> <p>弹性伸缩：优化 input 和 output 配置里面的字段类型，从 int 改为 Integer，方便通过 DistSQL 配置为空</p> </li> 
 <li> <p>弹性伸缩：优化 MySQL 校验和 SQL</p> </li> 
 <li> <p>弹性伸缩：优化进度删除和进度检查</p> </li> 
 <li> <p>弹性伸缩：优化 FinishedCheckJob 在错误状态下不能做完成检测</p> </li> 
 <li> <p>弹性伸缩：如果存在不符合迁移条件的表，尽快报错</p> </li> 
 <li> <p>弹性伸缩：PipelineAPIFactory 创建 GovernanceRepositoryAPI 的时候复用 ClusterPersistRepository</p> </li> 
 <li> <p>弹性伸缩：升级 jobId 生成算法；jobId 支持幂等性</p> </li> 
 <li> <p>DistSQL：<code>CREATE/ALTER ENCRYPT RULE</code>语法支持配置数据类型和长度</p> </li> 
 <li> <p>DistSQL：统一 <code>SHOW ALL VARIABLES</code>与 <code>SHOW VARIABLE</code> 语法的展示结果</p> </li> 
 <li> <p>DistSQL：<code>DROP BINDING TABLE RULES</code>语法消除绑定顺序对删除结果的影响</p> </li> 
 <li> <p>DistSQL：<code>SHOW INSTANCE LIST</code> 语法增加 <code>mode_type</code> 字段的展示</p> </li> 
 <li> <p>DistSQL：<code>ENABLE/DISABLE INSTANCE</code>语法增加对模式的校验</p> </li> 
 <li> <p>DistSQL：删除读写分离规则时，增加对规则是否正在使用的校验</p> </li> 
 <li> <p>DistSQL：创建读写分离规则时，增加 Resource 重名的校验</p> </li> 
 <li> <p>DistSQL：<code>SHOW READWRITE_SPLITTING READ RESOURCES</code>增加延迟时间的展示</p> </li> 
 <li> <p>DistSQL：<code>DROP RULE</code> 语法支持 <code>IF EXISTS</code> 进行预判断</p> </li> 
 <li> <p>DistSQL：优化 <code>ADD/ALTER RESOURCE</code>连接失败的提示信息</p> </li> 
 <li> <p>分布式治理：增加 schema version 版本号支持批量执行 DistSQL</p> </li> 
 <li> <p>分布式治理：集群模式下持久化元数据优化</p> </li> 
 <li> <p>分布式治理：数据库发现创建 JOB 增加 schemaName 标识</p> </li> 
</ul> 
<h2>重构</h2> 
<ul> 
 <li> <p>内核：重构加解密测试用例</p> </li> 
 <li> <p>内核：重构元数据模型，适配 PostgreSQL database 和 schema 模型</p> </li> 
 <li> <p>弹性伸缩：pipeline 模块移除 HikariCP 依赖</p> </li> 
 <li> <p>分布式治理：重构治理中心存储节点结构</p> </li> 
 <li> <p>分布式治理：重构治理中心 metadata 结构</p> </li> 
 <li> <p>分布式治理：调整数据库发现 MGR 模块为 MySQL 模块</p> </li> 
</ul> 
<h2>问题修复</h2> 
<ul> 
 <li> <p>内核：修复函数无法获取变量的异常</p> </li> 
 <li> <p>内核：修复 <code>InsertValueContext.getValue</code> 转换异常</p> </li> 
 <li> <p>内核：修复 distinct 聚合函数列异常</p> </li> 
 <li> <p>内核：修复带有 schema 的加解密算法改写异常</p> </li> 
 <li> <p>内核：修复读写分离场景下不返回列的异常</p> </li> 
 <li> <p>内核：修复 <code>show tables</code> 语句丢失部分表的异常</p> </li> 
 <li> <p>内核：修复相同结尾的分表路由的异常</p> </li> 
 <li> <p>内核：修复 assignment 短语某些场景下的解析异常</p> </li> 
 <li> <p>内核：修复分片特定配置下的数字转换异常</p> </li> 
 <li> <p>内核：修复单数据源读写分离的元数据异常</p> </li> 
 <li> <p>内核：修复批量执行语句 statement 关闭异常</p> </li> 
 <li> <p>内核：修复某些语句包含 * 时的改写异常</p> </li> 
 <li> <p>内核：修复某些情况下内存模式 ShardingSphere-Proxy 的启动异常</p> </li> 
 <li> <p>接入端：修复 ShardingSphere-Proxy PostgreSQL/openGauss 可能会误替换 SQL 中非参数占位符的字面量</p> </li> 
 <li> <p>接入端：修复 PostgreSQL JDBC Driver 42.3.x 无法连接配置了多个 schema 的 PostgreSQL Proxy 的问题</p> </li> 
 <li> <p>接入端：修复 ShardingSphere-Proxy MySQL timestamp 类型时间精度丢失问题</p> </li> 
 <li> <p>接入端：修复 ShardingSphere-Proxy PostgreSQL 二进制 numeric 编码不正确的问题</p> </li> 
 <li> <p>接入端：修复 ShardingSphere-JDBC 潜在的性能问题及 OOM 风险</p> </li> 
 <li> <p>接入端：修复 ShardingSphere-Proxy MySQL 偶发读取已关闭结果集错误的问题</p> </li> 
 <li> <p>接入端：修复 ShardingSphere-JDBC 没有参数的情况调用 executeBatch 导致空指针的问题</p> </li> 
 <li> <p>弹性伸缩：修复 job 报错之后无法通过 DistSQL 重启</p> </li> 
 <li> <p>DistSQL：修复 <code>CREATE SHARDING TABLE RULE</code> 时 inline 表达式解析错误</p> </li> 
 <li> <p>DistSQL：修复当密码为关键字 password 时，<code>ADD RESOURCE</code> 解析异常</p> </li> 
 <li> <p>分布式治理：修复由于 ZooKeeper session 超时导致计算节点丢失问题</p> </li> 
 <li> <p>分布式治理：修复治理中心表名大小写问题</p> </li> 
 <li> <p>分布式治理：DistSQL 启用禁用实例刷新内存计算节点状态</p> </li> 
 <li> <p>分布式治理：修复数据库发现无法通过 DistSQL 创建 Rule</p> </li> 
</ul> 
<p>🔗 <strong>下载链接：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2Fdocument%2Fcurrent%2Fcn%2Fdownloads%2F" target="_blank">https://shardingsphere.apache.org/document/current/cn/downloads/</a></p> 
<p>🔗 <strong>更新日志：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fshardingsphere%2Fblob%2Fmaster%2FRELEASE-NOTES.md" target="_blank">https://github.com/apache/shardingsphere/blob/master/RELEASE-NOTES.md</a></p> 
<p>🔗 <strong>项目地址：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2F" target="_blank">https://shardingsphere.apache.org/</a></p> 
<h2>社区建设</h2> 
<p>此次 Apache ShardingSphere 5.1.1 版本的发布，共有 64 位 Contributor 提交了 698 个 PR，感谢社区伙伴们的大力支持。</p> 
<p style="text-align:center"><img src="https://static001.geekbang.org/infoq/32/323fb4445f6d77909531a8867b8ec0dc.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><strong>同时，我们将于 5 月 14 日举办『Apache ShardingSphere 2022 Meetup 北京站』，敬请期待，欢迎大家届时报名参与。</strong>🤩🤩</p> 
<p style="text-align:center"><img src="https://static001.geekbang.org/infoq/0b/0bb7194d5879bb333cd6a26409848e6e.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            