
---
title: 'Apache Ignite 2.13.0 版本发布，全新的基于 Calcite 的 SQL 引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1861'
author: 开源中国
comments: false
date: Thu, 28 Apr 2022 09:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1861'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span>Apache Ignite 版本发布说明</span></p> 
<div> 
 <h2>Apache Ignite 分布式内存数据库 2.13.0</h2> 
 <p>(!) 警告:</p> 
 <ul> 
  <li>之前已被废弃的服务网络功能被删除。</li> 
 </ul> 
 <h2>Ignite：</h2> 
 <ul> 
  <li>新增'snapshotTransferRate'分布式属性来限制创建快照文件的速率；</li> 
  <li>启动时新增CDC硬链接检查；</li> 
  <li>在Calcite查询引擎中新增JDBC和ODBC的批处理支持；</li> 
  <li>在快照恢复操作过程中新增JMX的管理接口和指标输出；</li> 
  <li>新增重建损坏索引的维护任务；</li> 
  <li>新增SNAPSHOT系统视图来显示本地的快照；</li> 
  <li>新增ServiceCallContext，在服务调用时可以隐式传递额外的参数；</li> 
  <li>新增一个选项，使用control.sh可以执行同步的快照命令；</li> 
  <li>插件新增以扩展的方式执行拓扑验证的能力；</li> 
  <li>新增加密快照的动态恢复；</li> 
  <li>在Ignite的发布周期中新增ignite-parent构件；</li> 
  <li>新增试验性的基于Calcite的SQL引擎；</li> 
  <li>CDC中新增支持非默认的页面大小；</li> 
  <li>事务监控的配置支持保存到磁盘；</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fignite-cdc.sh" target="_blank">ignite-cdc.sh</a> 和 ignite.sh支持不同的JVM选项参数；</li> 
  <li>系统数据区新增支持不同的配置；</li> 
  <li>将分区映射序列化到磁盘，来避免节点启动时间长的问题；</li> 
  <li>新增服务方法调用持续时间直方图指标；</li> 
  <li>新增支持JDK17；</li> 
  <li>在控制脚本的一致性检查命令中新增支持IGNITE_TO_STRING_INCLUDE_SENSITIVE选项；</li> 
  <li>在控制脚本的一致性检查命令中新增status选项；</li> 
  <li>线程池新增任务执行时间指标；</li> 
  <li>在本地事件监听器中新增支持LifecycleAware接口；</li> 
  <li>如果配置了PriorityQueueCollisionSpi新增支持修改计算任务的优先级；</li> 
  <li>废弃了IgniteServices#service(String)和IgniteServices#services(String)；</li> 
  <li>废弃了IGNITE_WAIT_FOR_BACKUPS_ON_SHUTDOWN系统属性；</li> 
  <li>废弃ignite-log4j模块；</li> 
  <li>修复了当记录中包含多个DataEntry时CDC状态恢复方面的问题；</li> 
  <li>修复了在客户端节点创建GeoSpatial索引的问题；</li> 
  <li>修复了IndexQuery无法正确处理_val字段索引的问题；</li> 
  <li>修复了JmxSystemViewExporterSpi中列类型为空时导致的空指针问题；</li> 
  <li>修复了PersistenceTask中的空指针问题；</li> 
  <li>修复了并发执行缓存销毁和激活事务时的空指针问题；</li> 
  <li>修复了消息解组的分布式处理过程中的空指针问题；</li> 
  <li>修复了使用BinaryObjects执行invokeAsync时的NoClassDefFound错误问题；</li> 
  <li>修复了在com.sun.management.OperatingSystemMXBean不存在时的NoClassDefFoundError错误问题；</li> 
  <li>修复了ODBC连接超时问题；</li> 
  <li>修复了客户端中执行隐式事务提交时导致PME故障的问题；</li> 
  <li>修复了握手过程中TLS 1.3冻结的问题；</li> 
  <li>修复了一个如果请求是从另一个副本发起的，则在近缓存/副本中更新TTL的罕见问题；</li> 
  <li>修复了部分JMX命令失败时报告反序列化错误的问题；</li> 
  <li>修复了一个会导致集群冻结失败的问题；</li> 
  <li>修复了一个导致基于速度的写入限制无法保护检查点缓冲区不被耗尽的问题；</li> 
  <li>修复了一个客户端重连后导致IgniteLock处理不正确的问题；</li> 
  <li>修复了一个在缓存启动时导致"Failed to get page store for the given cache ID"错误的问题；</li> 
  <li>修复了在Karaf容器内导致新节点加入集群失败的一个问题；</li> 
  <li>修复了由于关联赋值历史短导致的服务端节点故障的问题；</li> 
  <li>修复了带有“IN”条件的查询和子查询返回乘法数据时的问题；</li> 
  <li>修复了使用IgniteAtomicSequence中导致AssertionError错误的问题；</li> 
  <li>修复了原始对象中包含多个集合或引用字段的情况下生成二进制对象的问题；</li> 
  <li>修复了持久化原子缓存时的一致性问题；</li> 
  <li>修复了重新激活时过期处理故障的问题；</li> 
  <li>修复了表并发删除时的查询故障问题；</li> 
  <li>修复了DECIMAL和VARCHAR列类型索引碎片整理失败的问题；</li> 
  <li>修复了配置了本地标志和使用POJO参数时，SqlFieldsQuery无法使用索引扫描数据的问题；</li> 
  <li>修复了日志记录过程中出现ClosedChannelException异常的问题；</li> 
  <li>修复了IgniteStripedThreadPoolExecutor中指标处理不正确的问题；</li> 
  <li>修复了读修复中值检查缺失的问题；</li> 
  <li>修复了WAL Reader解析groupId/cacheId不正确的问题；</li> 
  <li>修复了ClosedChannelException异常导致的节点故障问题；</li> 
  <li>修复了ClassNotFoundException: wrong validation for Object type导致的节点故障问题；</li> 
  <li>修复了在错误的CRC上执行页面恢复时无法将页面标记为脏页面的问题；</li> 
  <li>修复了对等类加载错误处理方面的问题；</li> 
  <li>修复了基于速度的限流中可能出现的资源耗尽问题；</li> 
  <li>修复了由恶意或垃圾数据导致的瘦客户端协议处理过程中的潜在OOM问题；</li> 
  <li>修复了快速删除和更新操作中潜在的数据损坏问题；</li> 
  <li>修复了查询引擎允许插入逻辑上相等的联合主键数据行的问题；</li> 
  <li>修复了客户端节点加入集群时水平再平衡重新赋值导致的数据平衡问题；</li> 
  <li>修复了CdcLoader导致的SpringContext实例化问题；</li> 
  <li>修复了使用wrap_key和value_type引起的表操作失败问题；</li> 
  <li>修复了启用分区裁剪和查询并行化之后执行查询时副本数计算不正确的问题；</li> 
  <li>实现了内存缓存的CDC；</li> 
  <li>实现了Ignite固化内存的NUMA感知分配；</li> 
  <li>实现了读修复策略；</li> 
  <li>实现了服务中基于注解的ServiceContext注入；</li> 
  <li>实现了二进制对象内的数组类型支持；</li> 
  <li>实现了按原始列类型生成创建表sql键类型；</li> 
  <li>实现了控制脚本读修复命令的命名参数支持；</li> 
  <li>实现了CDC的监控和日志输出；</li> 
  <li>改进了IndexQuery的索引行过滤；</li> 
  <li>改进了内存数据区的持久化数据结构消息的日志相关处理；</li> 
  <li>改进了节点启动时从WAL日志恢复数据分区状态的处理；</li> 
  <li>改进了快照分区移动；</li> 
  <li>删除了共享内存通信客户端；</li> 
  <li>删除了旧的服务网格实现；</li> 
  <li>更新JNR POSIX依赖至3.1.15；</li> 
  <li>更新Mesos依赖至1.11.0；</li> 
  <li>更新hadoop-yarn-client依赖至3.3.1；</li> 
  <li>更新sfl4j依赖至1.7.33；</li> 
  <li>更新Spring依赖至5.2.21.RELEASE；</li> 
  <li>更新zookeeper依赖至3.8.0。</li> 
 </ul> 
 <h2>Java瘦客户端：</h2> 
 <ul> 
  <li>新增了在错误消息中附加服务端异常堆栈的选项；</li> 
  <li>新增了周期性心跳消息来提高连接可靠性。</li> 
 </ul> 
 <h2>JDBC/ODBC：</h2> 
 <ul> 
  <li>修复了空结果集时的不正确查询处理；</li> 
  <li>修复了调用SQLConnect时的链接失败问题；</li> 
  <li>修复了执行set streaming on/off方面的问题；</li> 
  <li>修复了SSL密钥存储不是强制参数的问题；</li> 
  <li>修复了SQLGetStmtAttr(SQL_ATTR_ROW_ARRAY_SIZE)处理不正确的问题；</li> 
 </ul> 
 <h2>.Net：</h2> 
 <ul> 
  <li>瘦客户端服务新增了GetServiceDescriptors；</li> 
  <li>新增了ThinClientConfiguration.SendServerExceptionStackTraceToClient；</li> 
  <li>新增了服务相关的指标；</li> 
  <li>修复了Alpine Linux环境中抛出EntryPointNotFoundException异常的问题；</li> 
  <li>修复了当类型中删除字段时二进制模式缺失的问题；</li> 
  <li>修复了节点重启后平台缓存没有从持久化存储中恢复数据的问题；</li> 
  <li>修复了'System.Enum'字段的序列化问题。</li> 
 </ul> 
 <h2>.Net瘦客户端：</h2> 
 <ul> 
  <li>新增了IClientRetryPolicy接口，用于控制由于连接问题导致操作失败时的重试行为；</li> 
  <li>新增了周期性心跳消息来提高连接可靠性。</li> 
 </ul> 
 <h2>C++：</h2> 
 <ul> 
  <li>CacheEntryEvent中新增了EventType字段；</li> 
  <li>修复了OpenSSL共享库顺序，新增了OpenSSL 3.0.x支持；</li> 
  <li>新增了IClientRetryPolicy接口，用于控制由于连接问题导致操作失败时的重试行为；</li> 
  <li>新增了ClientServices#serviceDescriptors；</li> 
  <li>改进了内存使用来避免额外的缓冲区复制。</li> 
 </ul> 
 <h2>C++瘦客户端：</h2> 
 <ul> 
  <li>修复了SSL密钥存储不是强制参数的问题；</li> 
  <li>实现了异步网络事件处理；</li> 
  <li>实现了持续查询。</li> 
 </ul> 
 <h2>SQL：</h2> 
 <ul> 
  <li>CREATE TABLE语句中新增了指定主键和关联键索引内联值的功能；</li> 
  <li>修复了子查询常量优化方面的问题。</li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            