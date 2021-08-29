
---
title: 'TiDB 5.2 发布，分布式 NewSQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1607'
author: 开源中国
comments: false
date: Sun, 29 Aug 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1607'
---

<div>   
<div class="content">
                                                                                            <p>TiDB 5.2 现已发布。在该版本中，你可以获得以下关键特性：</p> 
<ul> 
 <li>支持基于部分函数创建表达式索引 (Expression index)，极大提升查询的性能。</li> 
 <li>提升优化器的估算准确度 (Cardinality Estimation)，有助于选中最优的执行计划。</li> 
 <li>锁视图 (Lock View) 成为 GA 特性，提供更直观方便的方式观察事务加锁情况以及排查死锁问题。</li> 
 <li>新增 TiFlash I/O 限流功能，提升 TiFlash 读写稳定性。</li> 
 <li>为 TiKV 引入新的流控机制代替之前的 RocksDB write stall 流控机制，提升 TiKV 流控稳定性。</li> 
 <li>简化 Data Migration (DM) 工具运维，降低运维管理的成本。</li> 
 <li>TiCDC 支持 HTTP 协议 OpenAPI 对 TiCDC 任务进行管理，在 Kubernetes 以及 On-Premises 环境下提供更友好的运维方式。(实验特性)</li> 
</ul> 
<h3>兼容性更改</h3> 
<blockquote> 
 <p><strong>注意：</strong></p> 
 <p>当从一个早期的 TiDB 版本升级到 TiDB 5.2 时，如需了解所有中间版本对应的兼容性更改说明，请查看对应版本的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Frelease-notes" target="_blank">Release Note</a>。</p> 
</blockquote> 
<h4>系统变量</h4> 
<table cellspacing="0"> 
 <tbody> 
  <tr> 
   <th>变量名</th> 
   <th>修改类型</th> 
   <th>描述</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23default_authentication_plugin" target="_blank"><code>default_authentication_plugin</code></a></td> 
   <td>新增</td> 
   <td>设置服务器对外通告的默认身份验证方式，默认值为 <code>mysql_native_password</code>。</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_auto_increment_in_generated" target="_blank"><code>tidb_enable_auto_increment_in_generated</code></a></td> 
   <td>新增</td> 
   <td>控制是否允许在创建生成列或者表达式索引时引用自增列，默认值为<code>OFF</code>。</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_opt_enable_correlation_adjustment" target="_blank"><code>tidb_opt_enable_correlation_adjustment</code></a></td> 
   <td>新增</td> 
   <td>控制优化器是否开启交叉估算，默认值为<code>ON</code>。</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_opt_limit_push_down_threshold" target="_blank"><code>tidb_opt_limit_push_down_threshold</code></a></td> 
   <td>新增</td> 
   <td>设置将 Limit 和 TopN 算子下推到 TiKV 的阈值，默认值为<code>100</code>。</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_stmt_summary_max_stmt_count-%25E4%25BB%258E-v40-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_stmt_summary_max_stmt_count</code></a></td> 
   <td>修改</td> 
   <td>表示 statement summary 在内存中保存的语句的最大数量。默认值从 <code>200</code> 修改为 <code>3000</code>。</td> 
  </tr> 
  <tr> 
   <td><code>tidb_enable_streaming</code></td> 
   <td>废弃</td> 
   <td>系统变量 <code>enable-streaming</code>已废弃，不建议再使用。</td> 
  </tr> 
 </tbody> 
</table> 
<h4>配置文件参数</h4> 
<table cellspacing="0"> 
 <tbody> 
  <tr> 
   <th>配置文件</th> 
   <th>配置项</th> 
   <th>修改类型</th> 
   <th>描述</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td>TiDB 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23deadlock-history-collect-retryable" target="_blank"><code>pessimistic-txn.deadlock-history-collect-retryable</code></a></td> 
   <td>新增</td> 
   <td>控制 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Finformation-schema-deadlocks" target="_blank"><code>INFORMATION\_SCHEMA.DEADLOCKS</code></a> 表中是否收集可重试的死锁错误信息。</td> 
  </tr> 
  <tr> 
   <td>TiDB 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23auto-tls" target="_blank"><code>security.auto-tls</code></a></td> 
   <td>新增</td> 
   <td>控制 TiDB 启动时是否自动生成 TLS 证书，默认值为 <code>false</code>。</td> 
  </tr> 
  <tr> 
   <td>TiDB 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23max-stmt-count" target="_blank"><code>stmt-summary.max-stmt-count</code></a></td> 
   <td>修改</td> 
   <td>表示 statement summary tables 中保存的 SQL 种类的最大数量。默认值从 <code>200</code> 修改为 <code>3000</code>。</td> 
  </tr> 
  <tr> 
   <td>TiDB 配置文件</td> 
   <td><code>experimental.allow-expression-index</code></td> 
   <td>废弃</td> 
   <td>废弃 TiDB 配置文件中<code>allow-expression-index</code> 配置项</td> 
  </tr> 
  <tr> 
   <td>TiKV 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23cmd-batch" target="_blank"><code>raftstore.cmd-batch</code></a></td> 
   <td>新增</td> 
   <td>对请求进行攒批的控制开关，开启后可显著提升写入性能。默认值为 <code>true</code>。</td> 
  </tr> 
  <tr> 
   <td>TiKV 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23inspect-interval" target="_blank"><code>raftstore.inspect-interval</code></a></td> 
   <td>新增</td> 
   <td>TiKV 每隔一段时间会检测 Raftstore 线程的延迟情况，该配置项设置检测的时间间隔。默认值为 <code>500ms</code>。</td> 
  </tr> 
  <tr> 
   <td>TiKV 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23max-peer-down-duration" target="_blank"><code>raftstore.max-peer-down-duration</code></a></td> 
   <td>修改</td> 
   <td>表示副本允许的最长未响应时间，超过将被标记为 <code>down</code>，后续 PD 会尝试将其删掉。默认值从 <code>5m</code> 修改为 <code>10m</code>。</td> 
  </tr> 
  <tr> 
   <td>TiKV 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23raft-client-queue-size" target="_blank"><code>server.raft-client-queue-size</code></a></td> 
   <td>新增</td> 
   <td>指定 TiKV 中发送 Raft 消息的缓冲区大小。默认值为 8192。</td> 
  </tr> 
  <tr> 
   <td>TiKV 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23enable" target="_blank"><code>storage.flow-control.enable</code></a></td> 
   <td>新增</td> 
   <td>表示是否开启 TiKV 流量控制机制。默认值为 <code>true</code>。</td> 
  </tr> 
  <tr> 
   <td>TiKV 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23memtables-threshold" target="_blank"><code>storage.flow-control.memtables-threshold</code></a></td> 
   <td>新增</td> 
   <td>当 KvDB 的 memtable 的个数达到该阈值时，流控机制开始工作。默认值为 5。</td> 
  </tr> 
  <tr> 
   <td>TiKV 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23l0-files-threshold" target="_blank"><code>storage.flow-control.l0-files-threshold</code></a></td> 
   <td>新增</td> 
   <td>当 KvDB 的 L0 文件个数达到该阈值时，流控机制开始工作。默认值为 9。</td> 
  </tr> 
  <tr> 
   <td>TiKV 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23soft-pending-compaction-bytes-limit" target="_blank"><code>storage.flow-control.soft-pending-compaction-bytes-limit</code></a></td> 
   <td>新增</td> 
   <td>当 KvDB 的 pending compaction bytes 达到该阈值时，流控机制开始拒绝部分写入请求并报错。默认值为 "192GB"。</td> 
  </tr> 
  <tr> 
   <td>TiKV 配置文件</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23hard-pending-compaction-bytes-limit" target="_blank"><code>storage.flow-control.hard-pending-compaction-bytes-limit</code></a></td> 
   <td>新增</td> 
   <td>当 KvDB 的 pending compaction bytes 达到该阈值时，流控机制开始拒绝所有写入请求并报错。默认值为 "1024GB"。</td> 
  </tr> 
 </tbody> 
</table> 
<h4>其他</h4> 
<ul> 
 <li> <p>升级前，请检查系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_evolve_plan_baselines-%25E4%25BB%258E-v40-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_evolve_plan_baselines</code></a> 的值是否为 <code>ON</code>。如果为 <code>ON</code>，需要将其改成 <code>OFF</code>，否则会导致升级失败。</p> </li> 
 <li> <p>v4.0 集群升级到 v5.2 集群后，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_multi_statement_mode-%25E4%25BB%258E-v4011-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_multi_statement_mode</code></a> 变量的默认值由 <code>WARN</code> 变为 <code>OFF</code>。</p> </li> 
 <li> <p>升级前，请检查 TiDB 配置项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23feedback-probability" target="_blank"><code>feedback-probability</code></a> 的值。如果不为 0，升级后会触发 "panic in the recoverable goroutine" 报错，但不影响升级。</p> </li> 
 <li> <p>兼容 MySQL 5.7 的 noop 变量 <code>innodb_default_row_format</code>，配置此变量无实际效果 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F23541" target="_blank">#23541</a>。</p> </li> 
 <li> <p>从 TiDB 5.2 起，为了提高系统安全性，建议（但不要求）对来自客户端的连接进行传输层加密，TiDB 提供 Auto TLS 功能在 TiDB 服务器端自动配置并开启加密。要使用 Auto TLS 功能，请在 TiDB 升级前将 TiDB 配置文件中的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23auto-tls" target="_blank"><code>security.auto-tls</code></a> 设置为 <code>true</code>。</p> </li> 
</ul> 
<h3>新功能</h3> 
<h4>SQL</h4> 
<ul> 
 <li> <p><strong>支持基于部分函数创建表达式索引 (Expression index)</strong></p> <p>表达式索引是一种特殊的索引，能将索引建立于表达式上。创建了表达式索引后，TiDB 支持基于表达式的查询，极大提升查询的性能。</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsql-statement-create-index" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25150" target="_blank">#25150</a></p> </li> 
 <li> <p><strong>支持 Oracle 中的 <code>translate</code>函数</strong></p> <p><code>translate</code> 函数可以将字符串中出现的所有指定字符替换为其它字符， TiDB 中的 <code>translate</code> 函数不会像 Oracle 一样将空字符串视为<code>NULL</code>。</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fstring-functions" target="_blank">用户文档</a></p> </li> 
 <li> <p><strong>支持 Spilling HashAgg</strong></p> <p>支持 HashAgg 的落盘。当包含 HashAgg 算子的 SQL 语句引起 OOM 时，可以尝试设置算子的并发度为 1 来触发落盘，缓解 TiDB 内存压力。</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fconfigure-memory-usage%23tidb-server-%25E5%2585%25B6%25E5%25AE%2583%25E5%2586%2585%25E5%25AD%2598%25E6%258E%25A7%25E5%2588%25B6%25E7%25AD%2596%25E7%2595%25A5" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25882" target="_blank">#25882</a></p> </li> 
 <li> <p><strong>提升优化器的估算准确度 (Cardinality Estimation)</strong></p> 
  <ul> 
   <li> <p>提升 TiDB 对 TopN/Limit 估算的准确度。例如，对于包含 <code>order by col limit x</code> 的大表分页查询，TiDB 可以更容易地选对索引，降低查询响应时间。</p> </li> 
   <li> <p>提升对越界估算的准确度。例如，在当天统计信息尚未更新的情况下，对于包含 <code>where date=Now()</code> 的查询，TiDB 也能准确地选中对应索引。</p> </li> 
   <li> <p>引入变量 <code>tidb_opt_limit_push_down_threshold</code> 控制优化器对 Limit/TopN 的下推行为，可以解决部分情况下因为估算误差导致 Limit/TopN 不能下推的问题。</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_opt_limit_push_down_threshold" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26085" target="_blank">#26085</a></p> </li> 
  </ul> </li> 
 <li> <p><strong>提升优化器的索引过滤规则 (Index Selection)</strong></p> <p>新增加了一些索引选择的裁剪规则，在通过统计信息进行对比之前，通过规则进一步对可能的选择的索引范围进行缩小。从而减小各种情况下选到不优索引的概率。</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fchoose-index" target="_blank">用户文档</a></p> </li> 
</ul> 
<h4>事务</h4> 
<ul> 
 <li> <p><strong>锁视图 (Lock View) 成为 GA 特性</strong></p> <p>Lock View 用于提供关于悲观锁的锁冲突和锁等待的更多信息，方便 DBA 通过锁视图功能来观察事务加锁情况以及排查死锁问题等。</p> <p>在 5.2 中，Lock View 新增以下特性：</p> 
  <ul> 
   <li> <p>对于 Lock View 所属的各张表中的 SQL Digest 列， v5.2 额外增加了一列显示对应的归一化的 SQL 语句文本，无需手动查询 SQL Digest 对应的语句。</p> </li> 
   <li> <p>增加了 <code>TIDB_DECODE_SQL_DIGESTS</code> 函数用于在集群中查询一组 SQL Digest 所对应的 SQL 语句的归一化形式（即去除格式和参数后的形式），简化了查询某一事务历史执行过的语句的操作</p> </li> 
   <li> <p>在 <code>DATA_LOCK_WAITS</code> 和 <code>DEADLOCKS</code> 系统表中，增加一列显示 key 中解出的表名、row id、索引值等信息，简化了定位 key 所属的表、解读 key 的内容等信息的操作。</p> </li> 
   <li> <p>支持在 <code>DEADLOCKS</code> 表中收集可重试的死锁错误的信息，以便于排查因可重试的死锁引发的问题。默认不收集，可通过配置选项 <code>pessimistic-txn.deadlock-history-collect-retryable</code> 启用 。</p> </li> 
   <li> <p><code>TIDB_TRX</code> 系统表支持区分正在执行查询的事务和闲置中的事务，即将原来的 <code>Normal</code> 状态拆分成 <code>Running</code> 和 <code>Idle</code> 状态。</p> <p>用户文档：</p> </li> 
   <li> <p>查看集群中所有 TiKV 节点上当前正在发生的悲观锁等锁：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Finformation-schema-data-lock-waits" target="_blank"><code>DATA_LOCK_WAITS</code></a></p> </li> 
   <li> <p>查看 TiDB 节点上最近发生的若干次死锁错误：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Finformation-schema-deadlocks" target="_blank"><code>DEADLOCKS</code></a></p> </li> 
   <li> <p>查看 TiDB 节点上正在执行的事务的信息：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Finformation-schema-tidb-trx" target="_blank"><code>TIDB_TRX</code></a></p> </li> 
  </ul> </li> 
 <li> <p>对带有 <code>AUTO_RANDOM</code> 或者 <code>SHARD_ROW_ID_BITS</code> 属性的表，优化其大部分添加索引操作的场景。</p> </li> 
</ul> 
<h4><strong>稳定性</strong></h4> 
<ul> 
 <li> <p><strong>新增 TiFlash I/O 限流功能</strong></p> <p>TiFlash I/O 限流功能主要针对磁盘带宽较小且明确知道磁盘带宽大小的云盘场景，默认关闭。</p> <p>TiFlash I/O Rate Limiter 提供了一个新的防止“读/写”任务之间过度竞争系统 IO 资源的机制，可以平衡系统对“读”和“写”任务的响应，并且可以根据读/写负载的情况自动限速。</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftiflash-configuration" target="_blank">用户文档</a></p> </li> 
 <li> <p><strong>提升 TiKV 流控稳定性</strong></p> <p>TiKV 引入了新的流控机制代替之前的 RocksDB write stall 流控机制。相比于 write stall 机制，新的流控机制通过以下改进减少了流控对前台写入稳定性的影响：</p> 
  <ul> 
   <li> <p>当 RocksDB compaction 压力堆积时，通过在 TiKV scheduler 层进行流控而不是在 RocksDB 层进行流控，避免 RocksDB write stall 造成的 raftstore 卡顿并造成 Raft 选举超时导致发生节点 leader 迁移的问题。</p> </li> 
   <li> <p>改善流控算法，有效降低大写入压力下导致 QPS 下降的问题</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23storageflow-control" target="_blank">用户文档</a>， <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10137" target="_blank">#10137</a></p> </li> 
  </ul> </li> 
 <li> <p><strong>自动检测并恢复集群中单个 TiKV 变慢带来的影响</strong></p> <p>在 TiKV 中引入了慢节点检测机制，通过检测 TiKV Raftstore 的快慢来计算出一个分数，并通过 Store Heartbeat 上报给 PD。并且在 PD 上增加了 <code>evict-slow-store-scheduler</code> 调度器，能够自动驱逐单个变慢的 TiKV 节点上的 Leader，以降低其对整个集群性能的影响。同时，还增加了慢节点相关的报警项，帮助用户快速发现并处理问题。</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23inspect-interval" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10539" target="_blank">#10539</a></p> </li> 
</ul> 
<h4><strong>数据迁移</strong></h4> 
<ul> 
 <li> <p><strong>简化 Data Migration (DM) 工具运维</strong></p> <p>DM v2.0.6 支持自动识别使用 VIP 的数据源实例切换事件（failover/计划切换），自动连接上新的数据源实例，减少数据复制的延迟和减少运维操作步骤</p> </li> 
 <li> <p>TiDB Lightning 支持自定义 CSV 数据的终止符，兼容 MySQL LOAD DATA CSV 数据格式 。使得 TiDB Lightning 可以直接使用在用户数据流转架构体系中。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1297" target="_blank">#1297</a></p> </li> 
</ul> 
<h4><strong>TiDB 数据共享订阅</strong></h4> 
<p>TiCDC 支持 HTTP 协议 OpenAPI 对 TiCDC 任务进行管理，在 Kubernetes 以及 On-Premises 环境下提供更友好的运维方式。(实验特性）</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F2411" target="_blank">#2411</a></p> 
<h4><strong>部署及运维</strong></h4> 
<p>支持在使用 Apple M1 芯片的本地 Mac 机器上使用 <code>tiup playground</code> 命令。</p> 
<h3>功能增强</h3> 
<ul> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>新增专为 TiDB 设计的比基于 JSON 的开放协议更紧凑的二进制 MQ 格式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1621" target="_blank">#1621</a></li> 
     <li>移除对 file sorter 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2114" target="_blank">#2114</a></li> 
     <li>支持日志轮替配置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2182" target="_blank">#2182</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>支持 CSV 文件中除 <code>\r</code> 和 <code>\n</code> 之外的自定义行尾 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1297" target="_blank">#1297</a></li> 
     <li>支持表达式索引和依赖于虚拟生成列的索引 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1407" target="_blank">#1407</a></li> 
    </ul> </li> 
   <li> <p>Dumpling</p> 
    <ul> 
     <li>支持备份兼容 MySQL 但不支持 <code>START TRANSACTION ... WITH CONSISTENT SNAPSHOT</code> 和 <code>SHOW CREATE TABLE</code> 语句的数据库 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fpull%2F311" target="_blank">#311</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h3>提升改进</h3> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>支持将内置函数 <code>json_unquote()</code> 下推到 TiKV <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24415" target="_blank">#24415</a></li> 
   <li>支持在 Dual 表上移除 <code>Union</code> 算子的优化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25614" target="_blank">#25614</a></li> 
   <li>优化聚合算子的代价常数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25241" target="_blank">#25241</a></li> 
   <li>允许 MPP outer join 根据表行数选择构建表 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25142" target="_blank">#25142</a></li> 
   <li>支持 MPP 查询任务按 Region 均衡到不同 TiFlash 节点上 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24724" target="_blank">#24724</a></li> 
   <li>支持执行 MPP 查询后将缓存中过时的 Region 无效化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24432" target="_blank">#24432</a></li> 
   <li>提升内置函数 <code>str_to_date</code> 在格式指定器中 <code>%b/%M/%r/%T</code> 的 MySQL 兼容性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25767" target="_blank">#25767</a></li> 
   <li>修复因对同一条查询重复创建不同 binding 可能导致的多个 TiDB 上 binding cache 不一致的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26015" target="_blank">#26015</a></li> 
   <li>修复升级可能会导致的 binding 无法被加载到缓存的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23295" target="_blank">#23295</a></li> 
   <li>对 <code>SHOW BINDINGS</code> 结果按照 (original_sql, update_time) 有序输出 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26139" target="_blank">#26139</a></li> 
   <li>改进使用 binding 优化查询的逻辑，减少对查询的优化次数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26141" target="_blank">#26141</a></li> 
   <li>支持标记为删除状态的 binding 进行自动垃圾回收 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26206" target="_blank">#26206</a></li> 
   <li>在 <code>EXPLAIN VERBOSE</code> 的结果中显示查询优化是否使用了某个 binding <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26930" target="_blank">#26930</a></li> 
   <li>增加新的状态变量 <code>last_plan_binding_update_time</code> 用于查看当前 TiDB 实例中 binding cache 对应的时间戳 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26340" target="_blank">#26340</a></li> 
   <li>在打开 binding 演进或者执行 <code>admin evolve bindings</code> 时提供报错，避免自动演进绑定（目前为试验特性，已在当前 TiDB 版本关闭）影响到其他功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26333" target="_blank">#26333</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>热点调度增加对 QPS 维度的支持，同时支持调整维度的优先级顺序<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3869" target="_blank">#3869</a></li> 
   <li>热点调度支持对 TiFlash 的写热点进行调度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fpull%2F3900" target="_blank">#3900</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>新增若干运算符的支持：<code>MOD / %</code>, <code>LIKE</code></li> 
   <li>新增若干字符串函数的支持：<code>ASCII()</code>, <code>COALESCE()</code>, <code>LENGTH()</code>, <code>POSITION()</code>, <code>TRIM()</code></li> 
   <li>新增若干数学函数的支持：<code>CONV()</code>, <code>CRC32()</code>, <code>DEGREES()</code>, <code>EXP()</code>, <code>LN()</code>, <code>LOG()</code>, <code>LOG10()</code>, <code>LOG2()</code>, <code>POW()</code>, <code>RADIANS()</code>, <code>ROUND(decimal)</code>, <code>SIN()</code>, <code>MOD()</code></li> 
   <li>新增若干日期函数的支持： <code>ADDDATE(string, real)</code>, <code>DATE_ADD(string, real)</code>, <code>DATE()</code></li> 
   <li>新增更多的函数支持：<code>INET_NTOA()</code>, <code>INET_ATON()</code>, <code>INET6_ATON</code>, <code>INET6_NTOA()</code></li> 
   <li>当 new collation 打开时，支持 MPP 模式下的 Shuffled Hash Join 和 Shuffled Hash Aggregation 运算</li> 
   <li>优化基础代码提升 MPP 性能</li> 
   <li>支持将 <code>STRING</code> 类型转换为 <code>DOUBLE</code> 类型</li> 
   <li>通过多线程优化右外连接中的非连接数据</li> 
   <li>支持在 MPP 查询中自动清理过期的 Region 信息</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>为 kv client 增量扫添加并发限制 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1899" target="_blank">#1899</a></li> 
     <li>始终在 TiCDC 内部拉取 old value <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2271" target="_blank">#2271</a></li> 
     <li>当遇到不可恢复的 DML 错误，TiCDC 快速失败并退出 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1928" target="_blank">#1928</a></li> 
     <li>在 Region 初始化后不立即执行 resolve lock <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2235" target="_blank">#2235</a></li> 
     <li>优化 workerpool 以降低在高并发情况下 goroutine 的数量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2201" target="_blank">#2201</a></li> 
    </ul> </li> 
   <li> <p>Dumpling</p> 
    <ul> 
     <li>通过 <code>tidb_rowid</code> 对 TiDB v3.x 的表进行数据划分以节省 TiDB 的内存 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fpull%2F301" target="_blank">#301</a></li> 
     <li>减少 Dumpling 对 <code>information_schema</code> 库的访问以提高稳定性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fpull%2F305" target="_blank">#305</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h3>Bug 修复</h3> 
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
   <li>修复 <code>tidb_snapshot</code> 被允许设置为非预期的过大值，而可能造成事务隔离性被破坏的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25680" target="_blank">#25680</a></li> 
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
   <li>修复多个调度器之间存在调度冲突时无法产生预期调度的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3807" target="_blank">#3807</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3778" target="_blank">#3778</a></li> 
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
     <li>修复 changefeed 创建成功后立即失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F2113" target="_blank">#2113</a></li> 
     <li>修复不合法格式的 rules filter 导致 changefeed 失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1625" target="_blank">#1625</a></li> 
     <li>修复 TiCDC Owner 崩溃时潜在的 DDL 丢失问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1260" target="_blank">#1260</a></li> 
     <li>修复 CLI 在默认的 sort-engine 选项上与 4.0.x 集群的兼容性问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F2373" target="_blank">#2373</a></li> 
     <li>修复 TiCDC 遇到 <code>ErrSchemaStorageTableMiss</code> 错误时可能导致 changefeed 被意外重置的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F2422" target="_blank">#2422</a></li> 
     <li>修复 TiCDC 遇到 <code>ErrGCTTLExceeded</code> 错误时 changefeed 不能被 remove 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F2391" target="_blank">#2391</a></li> 
     <li>修复 TiCDC 同步大表到 cdclog 失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1259" target="_blank">#1259</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F2424" target="_blank">#2424</a></li> 
     <li>修复 TiCDC 在重新调度 table 时多个 processors 可能向同一个 table 写数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F2230" target="_blank">#2230</a></li> 
    </ul> </li> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>修复 BR 恢复中忽略了所有系统表的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1197" target="_blank">#1197</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1201" target="_blank">#1201</a></li> 
     <li>修复 BR 恢复 cdclog 时漏掉 DDL 操作的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F870" target="_blank">#870</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>修复 TiDB Lightning 解析 Parquet 文件中 <code>DECIMAL</code> 类型数据失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1272" target="_blank">#1272</a></li> 
     <li>修复 TiDB Lightning 恢复 table schema 时报错 "Error 9007: Write conflict" 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1290" target="_blank">#1290</a></li> 
     <li>修复 TiDB Lightning 因 int handle 溢出导致导入数据失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1291" target="_blank">#1291</a></li> 
     <li>修复 TiDB Lightning 在 local backend 模式下因数据丢失可能遇到 checksum 不匹配的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1403" target="_blank">#1403</a></li> 
     <li>修复 TiDB Lightning 恢复 table schema 时与 clustered index 不兼容的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1362" target="_blank">#1362</a></li> 
    </ul> </li> 
   <li> <p>Dumpling</p> 
    <ul> 
     <li>修复 Dumpling GC safepoint 设置过晚导致数据导出失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fpull%2F290" target="_blank">#290</a></li> 
     <li>修复 Dumpling 在特定 MySQL 版本下获取上游表名时卡住的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fissues%2F322" target="_blank">#322</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>更新说明： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Frelease-5.2.0" target="_blank">https://docs.pingcap.com/zh/tidb/stable/release-5.2.0</a></p>
                                        </div>
                                      
</div>
            