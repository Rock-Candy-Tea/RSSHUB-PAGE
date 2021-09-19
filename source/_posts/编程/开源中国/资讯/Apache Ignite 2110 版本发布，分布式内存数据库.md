
---
title: 'Apache Ignite 2.11.0 版本发布，分布式内存数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8785'
author: 开源中国
comments: false
date: Sun, 19 Sep 2021 09:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8785'
---

<div>   
<div class="content">
                                                                                            <h1>Apache Ignite 版本发布说明：</h1> 
<h2>Apache Ignite 分布式内存数据库 2.11.0</h2> 
<p>Ignite:</p> 
<ul> 
 <li>新增通过Java API或者命令行脚本在运行的集群上从快照中恢复缓存组的功能；</li> 
 <li>新增快照的校验过程，可以校验快照的一致性等；</li> 
 <li>新增集群的元数据存储，用于快照的创建过程；</li> 
 <li>控制脚本新增性能统计的管理功能；</li> 
 <li>新增CLOCK和Segmented-LRU两种页面替换算法；</li> 
 <li>新增关联并置副本过滤器的节点属性；</li> 
 <li>新增数据结构的系统视图；</li> 
 <li>新增基线节点属性的系统视图；</li> 
 <li>新增用于监控SQL索引内存页面数的指标；</li> 
 <li>新增WAL写入和压缩字节数的指标；</li> 
 <li>新增SSL连接指标；</li> 
 <li>控制脚本的输出中新增无法强制重建的索引列表；</li> 
 <li>IgniteWalConverter中新增"pages"参数，用于在WAL中检索页面；</li> 
 <li>在反向连接协议中支持IGNITE_ENABLE_FORCIBLE_NODE_KILL标志；</li> 
 <li>为检查点间隔的随机化添加了"checkpoint.deviation"属性。它通过控制脚本设置检查点频率（以百分比为单位）：<code>control.sh --property set --name checkpoint.develation --val 25</code>；</li> 
 <li>通过Spring Boot auto starter新增了对Spring数据存储库初始化的支持；</li> 
 <li>修复了集群重新激活后缓存、缓存组、数据区指标不正确的问题；</li> 
 <li>修复了节点回退的错误。现在，如果历史再平衡失败，节点将正确地回退到完全再平衡；</li> 
 <li>修复了并发缓存数据存储初始化、交换初始化和检查点启动中可能出现的死锁；</li> 
 <li>修复了由于二进制流中的整数溢出而导致的潜在JVM崩溃问题；</li> 
 <li>修复了停止节点时在检查点末尾删除DurableBackgroundTask导致节点故障的问题；</li> 
 <li>修复了一个导致忽略作为复合主键一部分的列的NOT NULL约束验证的问题；</li> 
 <li>修复了在修改包含对其自身内部集合（集合的二进制句柄）的引用的二进制对象时导致错误的问题；</li> 
 <li>修复了远程过滤器部署期间静态初始值设定项中的异常可能导致服务端节点故障的问题；</li> 
 <li>修复了持续查询的部署问题。它们不会部署到客户端节点，因为客户端不存储任何数据；</li> 
 <li>修复了写入分布式元存储时的行为。现在，若客户端未连接到拓扑，则在客户端上会抛出异常；</li> 
 <li>修复了UriDeploymentSpi未找到类时会导致节点故障的问题；</li> 
 <li>修复了一个导致主键索引树损坏的问题，即如果表是通过SQL API创建的，并且主键中多个字段的顺序与表字段列表中指定的顺序不同，则会导致主键索引树损坏；</li> 
 <li>修复了连接到节点时出现的故障，如果使用成对连接，将导致连接Future冻结；</li> 
 <li>修复了检查点失败情况下删除索引后可能出现的索引分区损坏；</li> 
 <li>修复了集群二次激活后缓存组重新加密的问题；</li> 
 <li>修复了导致基线自动调整在某些情况下未触发的问题；</li> 
 <li>修复了自动回滚段和WAL冻结之间的争用；</li> 
 <li>修复了由于连接问题导致数据流刷新可能冻结的问题；</li> 
 <li>修复了节点无法获取要连接的IP地址时无法启动的问题；</li> 
 <li>修复了重建索引的问题，在缓存停止时同步停止重建索引，以避免节点故障；</li> 
 <li>修复了节点可能忽略OutOfMemoryError并无法停止的情况；</li> 
 <li>修复了一个节点关闭的连接可能导致在另一个节点上进行无限次连接尝试的问题；</li> 
 <li>修复了（减少了）独占检查点锁定时间；</li> 
 <li>修复了CPU检查点线程池大小未初始化时的问题；</li> 
 <li>修复了上次记录日志后自动段存档用完时出现的空指针问题；</li> 
 <li>修复了在建立新通信连接期间套接字读取冻结时可能出现的集群故障问题；</li> 
 <li>修复了启用自动调整后节点无法加入基线拓扑的问题；</li> 
 <li>修复了在不稳定拓扑上更改状态时WAL模式状态不一致的问题；</li> 
 <li>修复了持久化节点上内存数据区的已分配RAM指标不正确的问题；</li> 
 <li>修复了WAL存档从禁用切换到启用时节点的安全重启问题；</li> 
 <li>修复了在冻结的集群上删除索引期间导致JVM崩溃的问题；</li> 
 <li>修复了在Tcp通信SPI完全初始化之前更新消息传递相关指标时出现的错误；</li> 
 <li>修复了分区验证器的行为，即使更新计数器不同，它也会检查大小，并在分区处于不一致状态时输出有关所有副本的信息；</li> 
 <li>修复了原生客户端重新连接时可能发生异常的问题；</li> 
 <li>修改了IO发现指标名，现在它们从指标注册表名开始；</li> 
 <li>实现了持久后台任务的异步执行；</li> 
 <li>将Spring Cache集成迁移至Ignite扩展库；</li> 
 <li>将Spring-transactions模块迁移至Ignite扩展库；</li> 
 <li>优化了再平衡统计数据的收集，这对再平衡时间有积极影响；</li> 
 <li>删除了节点ping操作的延迟；</li> 
 <li>Spring Data Repository中不再必需Ignite bean名。</li> 
</ul> 
<p>.Net:</p> 
<ul> 
 <li>LINQ提供者中新增string.Compare支持；</li> 
 <li>新增了瘦客户端DataStreamer API；</li> 
 <li>新增了一个自动检查，确保客户端二进制配置与客户端启动时的服务端二进制配置兼容；</li> 
 <li>新增了Java和.NET之间服务异常的互操作性；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxn--ykqw9v10k.NET" target="_blank">新增了.NET</a> Core的示例，可以在任何操作系统上从CLI或任何IDE运行。可以使用dotnet-new命令从NuGet下载示例；</li> 
 <li>修复了指定NamespaceToLower或NamespacePrefix时的二进制类型处理；</li> 
 <li>修复了元素共享对同一对象的引用时的数组和集合反序列化问题;</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxn--ykq07af4r.NET" target="_blank">修复了.NET</a> 5上单文件部署中的DllNotFoundException问题；</li> 
 <li>修复了启用分区感知时字符串和数组缓存键的处理；</li> 
 <li>删除了在Linux和macOS系统上安装bash的要求；</li> 
 <li>改进了DataStreamer API：添加FlushAsync，弃用并替换混乱的方法和属性，修复资源清理；</li> 
 <li>扩展了ConfigurationManager依赖版本范围。</li> 
</ul> 
<p>Java瘦客户端：</p> 
<ul> 
 <li>新增了持续查询的支持；</li> 
 <li>新增了containsKeys、clearKey、clearKeys和getAndPutIfAbsent方法；</li> 
 <li>新增了Ignite瘦客户端Spring bean。</li> 
</ul> 
<p>瘦客户端：</p> 
<ul> 
 <li>默认启用分区感知（Java, .NET, C++）；</li> 
</ul> 
<p>SQL：</p> 
<ul> 
 <li>LOCAL_SQL_RUNNING_QUERIES系统视图中新增了一个新的INITIATOR_ID字段，该字段表示查询的发起方，包括瘦客户端、JDBC/ODBC和计算任务；</li> 
 <li>安全插件中新增执行修改/删除/创建SQL命令的功能；</li> 
 <li>SQL跟踪中新增sql.query.id标记；</li> 
 <li>修复了在IGNITE_TO_STRING_INCLUDE_SENSITIVE=false模式下，日志中SQL常量隐藏的问题。</li> 
</ul>
                                        </div>
                                      
</div>
            