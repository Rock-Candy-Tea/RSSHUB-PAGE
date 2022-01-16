
---
title: 'Apache Ignite 2.12.0 版本发布，分布式内存数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5962'
author: 开源中国
comments: false
date: Sun, 16 Jan 2022 08:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5962'
---

<div>   
<div class="content">
                                                                                            <h1>Apache Ignite 版本发布说明：</h1> 
<h2>Apache Ignite 分布式内存数据库 2.12.0</h2> 
<p>(!) 警告：</p> 
<ul> 
 <li>社区在未来的版本中会废弃如下的功能：CacheMode#LOCAL、CacheAtomicityMode#TRANSACTIONAL_SNAPSHOT、CacheConfiguration#rebalanceDelay；</li> 
 <li>GCE、AWS、Azure模块，CacheSpringStoreSessionListener和TcpDiscoveryZookeeperIpFinder移植到了Ignite扩展库；</li> 
 <li>现有的服务网格实现在下一版本中会被删除。</li> 
</ul> 
<p>Ignite：</p> 
<ul> 
 <li>新增分布式环境测试能力；</li> 
 <li>新增IndexQuery API，KV接口支持索引查询；</li> 
 <li>新增KubernetesConnectionConfiguration.discoveryPort；</li> 
 <li>分布式缓存查询汇总支持MergeSort；</li> 
 <li>控制脚本新增在特定分区上的读修复；</li> 
 <li>GridRestProcessor新增追踪请求处理的能力；</li> 
 <li>新增一个显式的方法，以支持注册基于类的二进制类型；</li> 
 <li>新增批量缓存处理直方图指标；</li> 
 <li>新增缓存查询的基准测试，包括扫描查询、索引查询和文本查询；</li> 
 <li>新增s390x的Docker镜像；</li> 
 <li>新增快照恢复操作的事件；</li> 
 <li>在启动的缓存日志中新增过期策略信息；</li> 
 <li>任意的读修复尝试都会触发事件（如果发现一致性冲突），原子化缓存也是支持的；</li> 
 <li>新增读取和分析索引文件的离线工具；</li> 
 <li>新增了具有相应WAL记录的重命名索引树操作；</li> 
 <li>新增了SharedPageLockTracker的资源释放；</li> 
 <li>新增了快照的线程池配置；</li> 
 <li>新增支持创建没有索引名的IndexQuery；</li> 
 <li>新增取消一致性恢复命令（通过控制脚本的读修复）；</li> 
 <li>控制脚本的一致性检查冲突支持记录到其他的日志文件；</li> 
 <li>新增在不同的拓扑中恢复快照的能力；</li> 
 <li>新增对加密缓存执行快照的能力；</li> 
 <li>控制脚本新增缓存销毁命令；</li> 
 <li>IgniteMXBean新增强制冻结标志；</li> 
 <li>IgniteCache#getAllOutTx新增时间指标和统计；</li> 
 <li>WAL中新增了无条件的事务状态日志，以确保在节点故障后仍能恢复事务；</li> 
 <li>将IGNITE_PDS_WAL_REBALANCE_THRESHOLD由节点级参数变更为分布式参数；</li> 
 <li>废弃CacheConfiguration#rebalanceDelay；</li> 
 <li>废弃CacheMode#LOCAL；</li> 
 <li>废弃CacheAtomicityMode#TRANSACTIONAL_SNAPSHOT；</li> 
 <li>废弃IGNITE_THRESHOLD_WAL_ARCHIVE_SIZE_PERCENTAGE系统属性；</li> 
 <li>修复了AssertionError： Unexpected rebalance on rebalanced cluster；</li> 
 <li>修复了CacheObjectAdapter#put方法不正确的偏移量处理；</li> 
 <li>修复了开启安全功能之后，在远程监听器中注册空的远程过滤器时的空指针异常；</li> 
 <li>修复了PagesWriteSpeedBasedThrottle的阈值计算；</li> 
 <li>修复了REST和Zookeeper模块的日志记录：使用SLF4j来记录第三方日志库；</li> 
 <li>修复了当使用缓存节点过滤器时REST请求错误；</li> 
 <li>修复了SSL读取错误；</li> 
 <li>修复了由于超过DataStorageConfiguration#getMaxWalArchiveSize而启动节点时出现的错误；</li> 
 <li>修复了azure-blob-storage依赖版本；</li> 
 <li>修复了在使用maven 3.8.1+版本时的构建问题；</li> 
 <li>修复了当达到最大WAL存档大小时取消WAL段保留的问题；</li> 
 <li>修复了在GridRestProcessor中创建/销毁缓存所需的更改权限；</li> 
 <li>修复了SERVICE_DEPLOY权限的检查；</li> 
 <li>修复了仅在服务器节点上过时的检查统计信息；</li> 
 <li>修复了客户端节点开启安全功能后的重连问题；</li> 
 <li>修复了系统工作进程在阻塞部分时并发心跳更新的问题；</li> 
 <li>修复了PDS损坏场景的诊断信息；</li> 
 <li>修复了有关索引的B+树锁定重试的错误扩展；</li> 
 <li>修复了检查点标记读取错误的异常；</li> 
 <li>修复了关闭GridCloseableIteratorAdapter的异常消息；</li> 
 <li>修复了守护节点执行操作需要权限认证的问题；</li> 
 <li>修复了在历史再平衡失败的情况下完全再平衡的回退问题；</li> 
 <li>修复了空闲验证和快照检查错误信息模糊的问题；</li> 
 <li>修复了当启用查询并行度时单分区查询返回多个结果的问题；</li> 
 <li>修复了开启安全后在维护模式节点重启的问题；</li> 
 <li>修复了性能提示指向过期的文档地址的问题；</li> 
 <li>修复了预配置的服务部署认证问题；</li> 
 <li>修复了缓存事件的安全上下文传播；</li> 
 <li>修复了计算任务的安全上下文传播；</li> 
 <li>修复了任意基线节点元数据丢失时的快照恢复错误；</li> 
 <li>修复了并非所有关联分区都物理存在的快照还原问题；</li> 
 <li>修复了服务端套接字的SocketTimeoutException（JDK-8247750）；</li> 
 <li>修复了DurableBackgroundCleanupIndexTreeTask中物理页面ID的存储问题；</li> 
 <li>修复了当JmxMetricExporterSpi注销一个已过滤的指标注册表时的AssertionError；</li> 
 <li>修复了未激活的集群启动时数据结构系统视图注册问题；</li> 
 <li>修复了重启节点后建立新索引的一致性问题；</li> 
 <li>修复了同步和异步方法中删除指标值不同的问题；</li> 
 <li>修复了检查点元信息的三次刷新问题；</li> 
 <li>修复了无条件创建Lucene索引的问题；</li> 
 <li>修复了不必要的套接字关闭和关闭日志输出；</li> 
 <li>修复了WAL存档关闭时错误报告的WALTOALSIZE；</li> 
 <li>实现了CDC指标；</li> 
 <li>实现了变更数据捕获；</li> 
 <li>实现了IndexQuery过滤操作；</li> 
 <li>实现了Yardstick多缓存事务操作的基准测试；</li> 
 <li>实现了CREATE INDEX语句中禁止重复字段；</li> 
 <li>实现了对等类加载错误信息的记录；</li> 
 <li>改进了快照过程的日志记录；</li> 
 <li>将CacheSpringStoreSessionListener移植到Ignite扩展库；</li> 
 <li>将TcpDiscoveryZookeeperIpFinder移植到Ignite扩展库；</li> 
 <li>将GCE、AWS、Azure模块移植到Ignite扩展库；</li> 
 <li>更新依赖版本（修复CVE-2020-15522、CVE-2020-0187、CVE-2020-26939）；</li> 
 <li>更新log4j2版本到2.17.1（修复CVE-2021-44228、CVE-2021-44832、CVE-2021-45046、CVE-2021-45105）；</li> 
 <li>更新PostgreSQL JDBC驱动版本（修复CVE-2020-13692）；</li> 
 <li>更新httpclient、httpcore版本（修复CVE-2020-13956）；</li> 
 <li>更新Jackson依赖版本（修复CVE-2019-16942、CVE-2019-16943、CVE-2019-17531）；</li> 
 <li>更新MySql驱动版本（修复CVE-2019-2692）；</li> 
 <li>更新Netty依赖版本（修复CVE-2021-21295）。</li> 
</ul> 
<p>Java瘦客户端：</p> 
<ul> 
 <li>瘦客户端的SQL错误消息中新增SQLSTATE；</li> 
 <li>为OptimizedMarshaller类名称添加了客户端缓存；</li> 
 <li>为具有指定分区的ScanQuery添加了分区感知；</li> 
 <li>新增了请求线程池监控；</li> 
 <li>修复了故障后服务调用出现ClassNotFoundException的问题；</li> 
 <li>修复了显式配置二进制类型配置后出现异常的问题；</li> 
 <li>修复了超时后的事务故障。</li> 
</ul> 
<p>.Net：</p> 
<ul> 
 <li>修复了由于记录器配置程序延迟而导致客户端FailoverSocket中的空指针；</li> 
 <li>修复了开启安全功能后持续查询中出现的空指针异常；</li> 
 <li>修复了SslStreamFactory.CertificatePath空值的问题；</li> 
 <li>修复了TypeNameParser忽略编译器生成的类型名中的转义字符的问题；</li> 
 <li>修复了TypeResolver中的动态程序集处理；</li> 
 <li>修复了瘦客户端数据流不创建SQL表项的问题；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxn--ykq07af4rzqcku0g.NET" target="_blank">修复了安装.NET</a> 5时verify-nuget.ps1的故障问题。</li> 
</ul> 
<p>Ignite C++：</p> 
<ul> 
 <li>新增支持计算任务；</li> 
 <li>新增支持关联字段；</li> 
 <li>修复了VisualStudio上的编译问题；</li> 
 <li>实现了在Windows上通过CMake构建安装ODBC驱动的问题；</li> 
 <li>删除了单独的JNI模块并将其移入Core模块。</li> 
</ul> 
<p>SQL：</p> 
<ul> 
 <li>新增了对可变二进制类型的精度支持；</li> 
 <li>修复了SQL AST遍历中的主键标志顺序；</li> 
 <li>修复了在单节点集群查询关联不正确的问题；</li> 
 <li>修复了关联字段配置别名的问题；</li> 
 <li>实现了表统计功能。</li> 
</ul>
                                        </div>
                                      
</div>
            