
---
title: 'TiDB 5.0.3 发布，分布式 NewSQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5829'
author: 开源中国
comments: false
date: Sun, 04 Jul 2021 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5829'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TiDB 5.0.3 现已发布，该版本具体更新内容如下：</p> 
<h2>兼容性更改</h2> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>v4.0 集群升级到 v5.0 或更高版本（dev 和 v5.1）的集群后，<code>tidb_multi_statement_mode</code> 变量的默认值由 <code>WARN</code> 变为 <code>OFF</code></li> 
   <li>兼容 MySQL 5.7 的 noop 变量 <code>innodb_default_row_format</code>，配置此变量无实际效果 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F23541" target="_blank">#23541</a></li> 
  </ul> </li> 
</ul> 
<h2>功能增强</h2> 
<ul> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>增加 HTTP API 获取 TiCDC changefeed 信息和节点健康信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1955" target="_blank">#1955</a></li> 
     <li>为 kafka 下游增加 SASL/SCRAM 支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1942" target="_blank">#1942</a></li> 
     <li>使 TiCDC 在 server 级别支持 <code>--data-dir</code> 配置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2070" target="_blank">#2070</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h2>提升改进</h2> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>支持将 <code>TopN</code> 算子下推到 TiFlash <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25162" target="_blank">#25162</a></li> 
   <li>支持将内置函数 <code>json_unquote()</code> 下推到 TiKV <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24415" target="_blank">#24415</a></li> 
   <li>支持在 Dual 表上移除 <code>Union</code> 算子的优化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25614" target="_blank">#25614</a></li> 
   <li>支持将内置函数 <code>replace()</code> 下推到 TiFlash <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25565" target="_blank">#25565</a></li> 
   <li>支持将内置函数 <code>unix_timestamp()</code>、<code>concat()</code>、<code>year()</code>、<code>day()</code>、<code>datediff()</code>、<code>datesub()</code>、<code>concat_ws()</code> 下推到 TiFlash <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25564" target="_blank">#25564</a></li> 
   <li>优化聚合算子的代价常数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25241" target="_blank">#25241</a></li> 
   <li>支持将 <code>Limit</code> 算子下推到 TiFlash <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25159" target="_blank">#25159</a></li> 
   <li>支持将内置函数 <code>str_to_date()</code> 下推到 TiFlash <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25148" target="_blank">#25148</a></li> 
   <li>允许 MPP outer join 根据表行数选择构建表 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25142" target="_blank">#25142</a></li> 
   <li>支持将内置函数 <code>left()</code>、<code>right()</code>、<code>abs()</code> 下推到 TiFlash <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25133" target="_blank">#25133</a></li> 
   <li>支持将 Broadcast Cartesian Join 下推到 TiFlash <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25106" target="_blank">#25106</a></li> 
   <li>支持将 <code>Union All</code> 算子下推到 TiFlash <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25051" target="_blank">#25051</a></li> 
   <li>支持 MPP 查询任务按 Region 均衡到不同 TiFlash 节点上 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24724" target="_blank">#24724</a></li> 
   <li>支持执行 MPP 查询后将缓存中过时的 Region 无效化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24432" target="_blank">#24432</a></li> 
   <li>提升内置函数 <code>str_to_date</code> 在格式指定器中 <code>%b/%M/%r/%T</code> 的 MySQL 兼容性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25767" target="_blank">#25767</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>限制 TiCDC sink 的内存消耗 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10305" target="_blank">#10305</a></li> 
   <li>为 TiCDC old value 缓存增加基于内存使用量的上限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10313" target="_blank">#10313</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>将 TiDB Dashboard 升级至 v2021.06.15.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3798" target="_blank">#3798</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>支持将 <code>STRING</code> 类型转换为 <code>DOUBLE</code> 类型</li> 
   <li>支持 <code>STR_TO_DATE()</code> 函数</li> 
   <li>通过多线程优化右外连接中的非连接数据</li> 
   <li>支持笛卡尔积 Join</li> 
   <li>支持 <code>LEFT()</code> 和 <code>RIGHT()</code> 函数</li> 
   <li>支持在 MPP 查询中自动清理过期的 Region 信息</li> 
   <li>支持 <code>ABS()</code> 函数</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>优化 gRPC 的重连逻辑，提升 KV client 的吞吐 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1586" target="_blank">#1586</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1501%23issuecomment-820027078" target="_blank">#1501</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1682" target="_blank">#1682</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1393" target="_blank">#1393</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1847" target="_blank">#1847</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1905" target="_blank">#1905</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1904" target="_blank">#1904</a></li> 
     <li>优化 sorter I/O 报错信息</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h2>Bug 修复</h2> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>修复在 <code>SET</code> 类型列上 Merge Join 结果不正确的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25669" target="_blank">#25669</a></li> 
   <li>修复 <code>IN</code> 表达式参数的数据腐蚀问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25591" target="_blank">#25591</a></li> 
   <li>避免 GC 的 session 受全局变量的影响 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24976" target="_blank">#24976</a></li> 
   <li>修复了在窗口函数查询中使用 <code>Limit</code> 时出现 panic 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25344" target="_blank">#25344</a></li> 
   <li>修复查询分区表时使用 <code>Limit</code> 返回错误值的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24636" target="_blank">#24636</a></li> 
   <li>修复了 <code>IFNULL</code> 在 <code>ENUM</code> 或 <code>SET</code> 类型上不能正确生效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24944" target="_blank">#24944</a></li> 
   <li>修复了 Join 子查询中的 <code>count</code> 被改写为 <code>first_row</code> 导致结果不正确的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24865" target="_blank">#24865</a></li> 
   <li>修复了 <code>TopN</code> 算子下使用 <code>ParallelApply</code> 查询时卡住的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24930" target="_blank">#24930</a></li> 
   <li>修复了使用含有多列的前缀索引查询时出现多余结果的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24356" target="_blank">#24356</a></li> 
   <li>修复了操作符 <code><=></code> 不能正确生效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24477" target="_blank">#24477</a></li> 
   <li>修复并行 <code>Apply</code> 算子的数据竞争问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F23280" target="_blank">#23280</a></li> 
   <li>修复对 PartitionUnion 算子的 IndexMerge 结果排序时出现 <code>index out of range</code> 错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F23919" target="_blank">#23919</a></li> 
   <li>修复 <code>tidb_snapshot</code> 被允许设置为非预期的过大值，而可能造成事务隔离性被破坏的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25680" target="_blank">25680</a></li> 
   <li>修复 ODBC 类常数（例如 <code>&#123;d '2020-01-01'&#125;</code>）不能被用作表达式的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25531" target="_blank">#25531</a></li> 
   <li>修复 <code>SELECT DISTINCT</code> 被转化为 Batch Get 而导致结果不正确的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25320" target="_blank">#25320</a></li> 
   <li>修复无法触发将查询从 TiFlash 回退到 TiKV 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F23665" target="_blank">#23665</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24421" target="_blank">#24421</a></li> 
   <li>修复在检查 <code>only_full_group_by</code> 时的 <code>index-out-of-range</code> 错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F23839" target="_blank">#23839</a></li> 
   <li>修复关联子查询中 Index Join 的结果不正确问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25799" target="_blank">#25799</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>修复错误的 <code>tikv_raftstore_hibernated_peer_state</code> 监控指标 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10330" target="_blank">#10330</a></li> 
   <li>修复 coprocessor 中 <code>json_unquote()</code> 函数错误的参数类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10176" target="_blank">#10176</a></li> 
   <li>正常关机时跳过清理 Raftstore 的回调从而避免在某些情况下破坏事务的 ACID <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10353" target="_blank">#10353</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10307" target="_blank">#10307</a></li> 
   <li>修复在 Leader 上 Replica Read 共享 Read Index 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10347" target="_blank">#10347</a></li> 
   <li>修复 coprocessor 转换 <code>DOUBLE</code> 到 <code>DOUBLE</code> 的错误函数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25200" target="_blank">#25200</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>修复在 scheduler 启动之后，加载 TTL 配置产生的数据竞争问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3771" target="_blank">#3771</a></li> 
   <li>修复 <code>is_learner</code> 字段在 TiDB 的 <code>TIKV_REGION_PEERS</code> 表中显示异常的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3372" target="_blank">#3372</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24293" target="_blank">#24293</a></li> 
   <li>修复在一个 zone 内所有 TiKV 节点下线或宕机的情况下，PD 不往其他 zone 调度数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3705" target="_blank">#3705</a></li> 
   <li>修复在添加 scatter range 调度器后导致 PD 挂掉的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fpull%2F3762" target="_blank">#3762</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>修复因 split 失败而不断重启的问题</li> 
   <li>修复无法删除 Delta 历史数据的潜在问题</li> 
   <li>修复在 <code>CAST</code> 函数中为非二进制字符串填充错误数据的问题</li> 
   <li>修复处理包含复杂 <code>GROUP BY</code> 列的聚合查询时结果不正确的问题</li> 
   <li>修复写入压力过大时出现进程崩溃的问题</li> 
   <li>修复右连接键不为空且左连接键可为空时进程崩溃的问题</li> 
   <li>修复 <code>read-index</code> 请求耗时长的潜在问题</li> 
   <li>修复读负载高的情况下进程崩溃的问题</li> 
   <li>修复 <code>Date_Format</code> 函数在参数类型为 <code>STRING</code> 且包含 <code>NULL</code> 值时可能导致 TiFlash server 崩溃的问题</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>修复 TiCDC owner 在刷新 checkpoint 时异常退出的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1902" target="_blank">#1902</a></li> 
     <li>修复写 MySQL 下游出错暂停时 MySQL 连接泄漏的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1946" target="_blank">#1946</a></li> 
     <li>修复 TiCDC 读取 <code>/proc/meminfo</code> 失败时出现的 panic 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2024" target="_blank">#2024</a></li> 
     <li>减少 TiCDC 运行时的内存使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2012" target="_blank">#2012</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1958" target="_blank">#1958</a></li> 
     <li>修复 resolved ts 计算慢导致 TiCDC panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1576" target="_blank">#1576</a></li> 
     <li>修复 processor 潜在的死锁问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2142" target="_blank">#2142</a></li> 
    </ul> </li> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>修复 BR 恢复中忽略了所有系统表的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1197" target="_blank">#1197</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1201" target="_blank">#1201</a></li> 
     <li>修复在 Backup & Restore 数据恢复期间开启 TDE 会报出文件已存在的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1179" target="_blank">#1179</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>修复 TiDB Lightning 在特殊数据下 panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1213" target="_blank">#1213</a></li> 
     <li>修复 TiDB Lightning 导入大文件拆分时遇到的 EOF 报错问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1133" target="_blank">#1133</a></li> 
     <li>修复 TiDB Lightning 导入含 <code>auto_increment</code> 的 <code>DOUBLE</code> 或 <code>FLOAT</code> 类型列的表时生成极大 base 值的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1186" target="_blank">#1186</a></li> 
     <li>修复 TiDB Lightning 解析 Parquet 文件中 <code>DECIMAL</code> 类型数据失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1277" target="_blank">#1277</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>更新说明： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fv5.1%2Frelease-5.0.3" target="_blank">https://docs.pingcap.com/zh/tidb/v5.1/release-5.0.3</a></p>
                                        </div>
                                      
</div>
            