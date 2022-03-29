
---
title: 'Apache IoTDB v0.13.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://mmbiz.qpic.cn/mmbiz_png/BgbbbeHYrp6nM4d2re5B1MG3CLkniauEWxK25qEicicvvVb5EfiaoOU4ohQfbn54NOFkc9WZn0kib1iaTXPxWQgUpVcQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1'
author: 开源中国
comments: false
date: Tue, 29 Mar 2022 17:44:00 GMT
thumbnail: 'https://mmbiz.qpic.cn/mmbiz_png/BgbbbeHYrp6nM4d2re5B1MG3CLkniauEWxK25qEicicvvVb5EfiaoOU4ohQfbn54NOFkc9WZn0kib1iaTXPxWQgUpVcQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0">Apache IoTDB v0.13.0 已经发布，此版本新增对齐序列存储模型，增加了对触发器等功能的支持；优化了现有 SQL 语法，并增加了新的语法支持；提升了查询功能，增加了对连续查询、嵌套表达式等的支持；优化了数据写入的过程，提升了系统文件合并的性能；拓展了与外部系统的兼容，新增 Grafana 插件、REST API 等。</p> 
<p><img alt="图片" src="https://mmbiz.qpic.cn/mmbiz_png/BgbbbeHYrp6nM4d2re5B1MG3CLkniauEWxK25qEicicvvVb5EfiaoOU4ohQfbn54NOFkc9WZn0kib1iaTXPxWQgUpVcQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#5f9cef">新功能</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-924] 支持一条 SQL 插入多行时间戳的数据</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-959] 增加 Create Storage Group 语法 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1037] 支持在 JDBC URL 参数中设置 rpc_compression （是否开启 RPC 压缩） </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1059] 支持 SQL 插入数据不带时间戳，使用服务器当前时间 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1143] 支持连续查询功能。连续查询在某些系统中又被称为连续聚集。具体的，它允许用户在系统中定义定时查询任务，定时将聚合查询的结果物化到指定的序列中。通过定义持续查询，可避免在大数据量、高复杂聚合场景下产生的时间开销。 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1199] 支持对齐时间序列和元数据模板 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1319] 支持触发器功能 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1391] 支持新的聚合函数 extreme (绝对值的最大值) </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1399] 支持 Session 连接多个节点，失败自动重定向 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1400] 在 Select 语句中支持算术表达式 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1403] 为 TEXT 类型的数据增加 Dictionary 编码方法 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1490] 增加了内置的 UDTF ，包括 sinh, conh, tanh </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1514] 在 InsertTablet 中支持空值 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1524] 新增语法支持：SELECT … INTO … </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1647] 支持在原始数据查询中对 Select 子句使用嵌套表达式 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1673] 客户端（CLI）升级为 JLine3 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1739] 新增时间序列生成函数，包括 const （常量）、pi 或 e 函数 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1760] 在 group by fill 查询中增加对 avg, count, extreme, first_value, last_value, max_time, max_value, min_time, min_value, sum 等聚合函数的支持 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1761] 新增了指标监控框架 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1775] 新增 CAST 函数来进行数据类型的转换 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1823] 新增根据多个元数据层级的局和操作，即 group by multi level </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1844] 在查询中可以使用前缀或后缀匹配，例如：root.*sg* </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1859] 新增 REST API 的支持 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1860] 新增 Grafana 插件 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1886] 在 Select 子句中增加了对 Constant Expressions （常量表达式）的支持 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1973] 支持在聚合查询中对 Select 子句使用嵌套表达式 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1986] 可在 Select UDF 子句中对其使用别名 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1989] 数据写入增加对 Spark-IoTDB-connector 的支持 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2131] 在 Fill子句中增加对 previous、linear 及常量填充的支持 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2593] 增加 IoTDB 对 JDK17 的兼容 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[ISSUE-3811] 在 last query 的结果集中新增表示数据类型的列 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增了 RabbitMQ 的示例</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><span style="color:#5f9cef"><strong>  改进</strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1280] 重写了 Antlr 语法定义文件 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1372] 提升了对 TsFileResource 的管理 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1428] 优化了查询超时的管理 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1450] 优化了删除操作，删除操作将仅涉及相关的时间分区 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1463] 为 Session and SessionPool 实现了 Builder 模式 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1477] 优化了方法 generateAlignByDevicePlan() 的实现逻辑 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1559] 重构了集成测试框架 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1564] 将心跳和选举超时时间置为可配置参数 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1581] 优化了 TsFileResource 的恢复过程，增加了对未结束的tsfile的考虑 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1607] 优化了 Tracing ，增加对查询追踪的细节 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1639] 重构了集群的代码框架，使其与 server 包保持一致 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1730] 在 client-cpp中提升了 session::insertTablet() 等方法的性能 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1852] 使用统计信息来加速查询执行 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1857] 在集群模式的非查询执行操作中移除了 CountPlan 相关的无效代码 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1884] 在 sum 聚合中对 0 和空值进行了区分 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1924] 在合并结束后移除了清理缓存的操作 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-1950] 对查询增加了布隆过滤器缓存 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2001] 移除了重复的 StorageGroupNotReadyException </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2011] 优化了 show latest timeseries query 中的缓存管理 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2022] 为 SessionDataSet 实现对 AutoCloseable 接口的支持 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2075] 使用线程池来加速 insertTablets 的执行 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2119] 优化了 IoTDB 的 CSV 导出工具中对时间精度的控制 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2162] 简化了文件合并流程 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2176] 在执行内部空间合并时，增加了对目标 chunk 大小的限制 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2193] 通过减少 RaftLogManager 中不必要的锁操作来提高写入性能 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2195] 优化了查询中并发线程的控制 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[IOTDB-2632] 将参数 compaction_write_throughput_mb_per_sec to 的默认值设置为16 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[ISSUE-3445] 实现了新的合并执行和调度策略 </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">[ISSUE-3856] 对 RaftLogManager 的 commitTo 进行了异常处理优化 [Cluster] 优化了集群模式下节点重启的握手策略</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">下载最新版本:</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#007aaa">https://iotdb.apache.org/Download/</span></p> 
<p style="margin-left:0; margin-right:0">完整的 Release Notes 可参考此处:</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#337ab7">https://raw.githubusercontent.com/apache/iotdb/v0.13.0/RELEASE_NOTES.md</span></p> 
<p style="margin-left:0; margin-right:0">当前 release 可在此处下载：</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#007aaa">http://iotdb.apache.org/Download</span></p> 
<p style="margin-left:0; margin-right:0; text-align:left">JDBC driver, session SDK, TsFile SDK, Spark-connector, Hadoop-connector, Hive-connector 以及 Flink-connector 可在此处查询:</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#007aaa">https://search.maven.org/search?q=3Dg:org.apache.iotdb</span></p> 
<p style="margin-left:0; margin-right:0">IoTDB server 的 Docker image 在此处查找：</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#007aaa">https://hub.docker.com/r/apache/iotdb</span></p> 
<p style="margin-left:0; margin-right:0">Python API 可在此处查找:</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#007aaa">https://pypi.org/project/apache-iotdb/</span></p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            