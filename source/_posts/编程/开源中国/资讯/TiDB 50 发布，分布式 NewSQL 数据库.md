
---
title: 'TiDB 5.0 发布，分布式 NewSQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5549'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5549'
---

<div>   
<div class="content">
                                                                                            <p>TiDB 5.0 现已发布，该版本专注于帮助企业基于 TiDB 数据库快速构建应用程序，使企业在构建过程中无需担心数据库的性能、性能抖动、安全、高可用、容灾、SQL 语句的性能问题排查等问题。</p> 
<p>在 5.0 版本中，你可以获得以下关键特性：</p> 
<ul> 
 <li>TiDB 通过 TiFlash 节点引入了 MPP 架构。这使得大型表连接类查询可以由不同 TiFlash 节点分担共同完成。当 MPP 模式开启后，TiDB 将会根据代价决定是否应该交由 MPP 框架进行计算。MPP 模式下，表连接将通过对 JOIN Key 进行数据计算时重分布（Exchange 操作）的方式把计算压力分摊到各个 TiFlash 执行节点，从而达到加速计算的目的。经测试，TiDB 5.0 在同等资源下，MPP 引擎的总体性能是 Greenplum 6.15.0 与 Apache Spark 3.1.1 两到三倍之间，部分查询可达 8 倍性能差异。</li> 
 <li>引入聚簇索引功能，提升数据库的性能。例如，TPC-C tpmC 的性能提升了 39%。</li> 
 <li>开启异步提交事务功能，降低写入数据的延迟。例如：Sysbench 设置 64 线程测试 Update index 时, 平均延迟由 12.04 ms 降低到 7.01ms ，降低了 41.7%。</li> 
 <li>通过提升优化器的稳定性及限制系统任务对 I/O、网络、CPU、内存等资源的占用，降低系统的抖动。例如：测试 8 小时，TPC-C 测试中 tpmC 抖动标准差的值小于等于 2%。</li> 
 <li>通过完善调度功能及保证执行计划在最大程度上保持不变，提升系统的稳定性。</li> 
 <li>引入 Raft Joint Consensus 算法，确保 Region 成员变更时系统的可用性。</li> 
 <li>优化 <code>EXPLAIN</code> 功能、引入不可见索引等功能帮助提升 DBA 调试及 SQL 语句执行的效率。</li> 
 <li>通过从 TiDB 备份文件到 Amazon S3、Google Cloud GCS，或者从 Amazon S3、Google Cloud GCS 恢复文件到 TiDB，确保企业数据的可靠性。</li> 
 <li>提升从 Amazon S3 或者 TiDB/MySQL 导入导出数据的性能，帮忙企业在云上快速构建应用。例如：导入 1TiB TPC-C 数据性能提升了 40%，由 254 GiB/h 提升到 366 GiB/h。</li> 
</ul> 
<h2>兼容性变化</h2> 
<h3>系统变量</h3> 
<ul> 
 <li> <p>新增系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_executor_concurrency-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_executor_concurrency</code></a>，用于统一控制算子并发度。原有的 tidb_*_concurrency（例如 <code>tidb_projection_concurrency</code>）设置仍然生效，使用过程中会提示已废弃警告。</p> </li> 
 <li> <p>新增系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_skip_ascii_check-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_skip_ascii_check</code></a>，用于决定在写入 ASCII 字符集的列时，是否对字符的合法性进行检查，默认为 OFF。</p> </li> 
 <li> <p>新增系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_strict_double_type_check-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_enable_strict_double_type_check</code></a>，用于决定类似“double(N)”语法是否允许被定义在表结构中，默认为 OFF。</p> </li> 
 <li> <p>系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_dml_batch_size" target="_blank"><code>tidb_dml_batch_size</code></a> 的默认值由 20000 修改为 0，即在 LOAD/INSERT INTO SELECT ... 等语法中，不再默认使用 Batch DML，而是通过大事务以满足严格的 ACID 语义。</p> 
  <blockquote> 
   <p><strong>注意：</strong></p> 
   <p>该变量作用域从 session 改变为 global，且默认值从 20000 修改为 0，如果应用依赖于原始默认值，需要在升级之后使用 <code>set global</code> 语句修改该变量值为原始值。</p> 
  </blockquote> </li> 
 <li> <p>临时表的语法兼容性受到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_noop_functions-%25E4%25BB%258E-v40-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_enable_noop_functions</code></a> 系统变量的控制：当 <code>tidb_enable_noop_functions</code> 为 <code>OFF</code> 时，<code>CREATE TEMPORARY TABLE</code> 语法将会报错。</p> </li> 
 <li> <p>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_gc_concurrency-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_gc_concurrency</code></a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_gc_enable-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_gc_enable</code></a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_gc_life_time-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_gc_life_time</code></a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_gc_run_interval-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_gc_run_interval</code></a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_gc_scan_lock_mode-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_gc_scan_lock_mode</code></a> 系统变量，用于直接通过系统变量调整垃圾回收相关参数。</p> </li> 
 <li> <p>系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fpd-configuration-file%23enable-joint-consensus-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>enable-joint-consensus</code></a> 默认值由 <code>false</code> 改成 <code>ture</code>，默认开启 Joint consensus 功能。</p> </li> 
 <li> <p>系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_amend_pessimistic_txn-%25E4%25BB%258E-v407-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_enable_amend_pessimistic_txn</code></a> 的值由数字 0 或者 1 变更成 ON 或者 OFF。</p> </li> 
 <li> <p>系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_clustered_index-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_enable_clustered_index</code></a> 默认值由 OFF 改成 INT_ONLY 且含义有如下变化：</p> 
  <ul> 
   <li> <p>ON：开启聚簇索引，支持添加或者删除非聚簇索引。</p> </li> 
   <li> <p>OFF：关闭聚簇索引，支持添加或者删除非聚簇索引。</p> </li> 
   <li> <p>INT_ONLY：默认值，行为与 v5.0 以下版本保持一致，与 <code>alter-primary-key = false</code> 一起使用可控制 INT 类型是否开启聚簇索引。</p> 
    <blockquote> 
     <p><strong>注意：</strong></p> 
     <p>5.0 GA 中 <code>tidb_enable_clustered_index</code> 的 INT_ONLY 值和 5.0 RC 中的 OFF 值含义一致，从已设置 OFF 的 5.0 RC 集群升级至 5.0 GA 后，将展示为 INT_ONLY。</p> 
    </blockquote> </li> 
  </ul> </li> 
</ul> 
<h3>配置文件参数</h3> 
<ul> 
 <li>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23index-limit-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>index-limit</code></a> 配置项，默认值为 64，取值范围是 [64, 512]。MySQL 一张表最多支持 64 个索引，如果该配置超过默认值并为某张表创建超过 64 个索引，该表结构再次导入 MySQL 将会报错。</li> 
 <li>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23enable-enum-length-limit-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>enable-enum-length-limit</code></a> 配置项，用于兼容 MySQL ENUM/SET 元素长度并保持一致（ENUM 长度 < 255），默认值为 true。</li> 
 <li>删除 <code>pessimistic-txn.enable</code> 配置项，通过环境变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_txn_mode" target="_blank">tidb_txn_mode</a> 替代。</li> 
 <li>删除 <code>performance.max-memory</code> 配置项，通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23server-memory-quota-%25E4%25BB%258E-v409-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank">performance.server-memory-quota</a> 替代。</li> 
 <li>删除 <code>tikv-client.copr-cache.enable</code> 配置项，通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23capacity-mb" target="_blank">tikv-client.copr-cache.capacity-mb</a> 替代，如果配置项的值为 0.0 代表关闭此功能，大于 0.0 代表开启此功能，默认：1000.0。</li> 
 <li>删除 <code>rocksdb.auto-tuned</code> 配置项，通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23rate-limiter-auto-tuned-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank">rocksdb.rate-limiter-auto-tuned</a> 替代。</li> 
 <li>删除 <code>raftstore.sync-log</code> 配置项，默认会写入数据强制落盘，之前显式关闭 <code>raftstore.sync-log</code>，成功升级 v5.0 版本后，会强制改为 <code>true</code>。</li> 
 <li><code>gc.enable-compaction-filter</code> 配置项的默认值由 <code>false</code> 改成 <code>true</code>。</li> 
 <li><code>enable-cross-table-merge</code> 配置项的默认值由 <code>false</code> 改成 <code>true</code>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23rate-limiter-auto-tuned-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>rate-limiter-auto-tuned</code></a> 配置项的默认值由 <code>false</code> 改成 <code>true</code>。</li> 
</ul> 
<h3>其他</h3> 
<ul> 
 <li>为了避免造成数据正确性问题，列类型变更不再允许 <code>VARCHAR</code> 类型和 <code>CHAR</code> 类型的互相转换。</li> 
</ul> 
<h2>新功能</h2> 
<h3>SQL</h3> 
<h4>List 分区表 (List Partition)（<strong>实验特性</strong>）</h4> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fpartitioned-table%23list-%25E5%2588%2586%25E5%258C%25BA" target="_blank">用户文档</a></p> 
<p>采用 List 分区表后，你可以高效地查询、维护有大量数据的表。</p> 
<p>List 分区表会按照 <code>PARTITION BY LIST(expr) PARTITION part_name VALUES IN (...)</code> 表达式来定义分区，定义如何将数据划分到不同的分区中。分区表的数据集合最多支持 1024 个值，值的类型只支持整数型，不能有重复的值。可通过 <code>PARTITION ... VALUES IN (...)</code> 子句对值进行定义。</p> 
<p>你可以设置 session 变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_list_partition-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_enable_list_partition</code></a> 的值为 <code>ON</code>，开启 List 分区表功能。</p> 
<h4>List COLUMNS 分区表 (List COLUMNS Partition)（<strong>实验特性</strong>）</h4> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fpartitioned-table%23list-columns-%25E5%2588%2586%25E5%258C%25BA" target="_blank">用户文档</a></p> 
<p>List COLUMNS 分区表是 List 分区表的变体，主要的区别是分区键可以由多个列组成，列的类型不再局限于整数类型，也可以是字符串、DATE 和 DATETIME 等类型。</p> 
<p>你可以设置 session 变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_list_partition-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_enable_list_partition</code></a> 的值为 <code>ON</code>，开启 List COLUMNS 分区表功能。</p> 
<h4>不可见索引（Invisible Indexes）</h4> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsql-statement-alter-index" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F9246" target="_blank">#9246</a></p> 
<p>DBA 调试和选择相对最优的索引时，可以通过 SQL 语句将某个索引设置成 <code>Visible</code> 或者 <code>Invisible</code>，避免执行消耗资源较多的操作，如 <code>DROP INDEX</code> 或 <code>ADD INDEX</code>。</p> 
<p>DBA 通过 <code>ALTER INDEX</code> 语句可以修改某个索引的可见性。修改后，查询优化器会根据索引的可见性决定是否将此索引加入到索引列表中。</p> 
<h4><code>EXCEPT</code> 和 <code>INTERSECT</code> 操作符</h4> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fset-operators" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18031" target="_blank">#18031</a></p> 
<p><code>INTERSECT</code> 操作符是一个集合操作符，返回两个或者多个查询结果集的交集。一定程度上可以替代 <code>Inner Join</code> 操作符。</p> 
<p><code>EXCEPT</code> 操作符是一个集合操作符，返回两个查询结果集的差集，即在第一个查询结果中存在但在第二个查询结果中不存在的结果集。</p> 
<h3>事务</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_amend_pessimistic_txn-%25E4%25BB%258E-v407-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18005" target="_blank">#18005</a></p> 
<p>悲观事务模式下，如果事务所涉及到的表存在并发的 DDL 操作或者 SCHEMA VERSION 变更，系统自动将该事务的 SCHEMA VERSION 更新到最新版本，以此确保事务会提交成功，避免事务因并发的 DDL 操作或者 SCHEMA VERSION 变更而中断时客户端收到 <code>Information schema is changed</code> 的错误信息。</p> 
<p>系统默认关闭此功能，你可以通过修改 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_amend_pessimistic_txn-%25E4%25BB%258E-v407-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_enable_amend_pessimistic_txn</code></a> 系统变量开启此功能，此功能从 4.0.7 版本开始提供，5.0 版本主要修复了以下问题：</p> 
<ul> 
 <li>TiDB Binlog 在执行 Add column 操作的兼容性问题</li> 
 <li>与唯一索引一起使用时存在的数据不一致性的问题</li> 
 <li>与添加索引一起使用时存在的数据不一致性的问题</li> 
</ul> 
<p>当前此功能存在以下不兼容性问题：</p> 
<ul> 
 <li>并发事务场景下事务的语义可能发生变化的问题</li> 
 <li>与 TiDB Binlog 一起使用时，存在已知的兼容性问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F20996" target="_blank">#20996</a></li> 
 <li>与 change column 功能不兼容 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F21470" target="_blank">#21470</a></li> 
</ul> 
<h3>字符集和排序规则</h3> 
<ul> 
 <li>支持 <code>utf8mb4_unicode_ci</code> 和 <code>utf8_unicode_ci</code> 排序规则。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fcharacter-set-and-collation%23%25E6%2596%25B0%25E6%25A1%2586%25E6%259E%25B6%25E4%25B8%258B%25E7%259A%2584%25E6%258E%2592%25E5%25BA%258F%25E8%25A7%2584%25E5%2588%2599%25E6%2594%25AF%25E6%258C%2581" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F17596" target="_blank">#17596</a></li> 
 <li>支持字符集比较排序时不区分大小写。</li> 
</ul> 
<h3>安全</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Flog-redaction" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18566" target="_blank">#18566</a></p> 
<p>为满足各种安全合规（如《通用数据保护条例》(GDPR)）的要求，系统在输出错误信息和日志信息时，支持对敏感信息（例如，身份证信息、信用卡号）进行脱敏处理，避免敏感信息泄露。</p> 
<p>TiDB 支持对输出的日志信息进行脱敏处理，你可以通过以下开关开启此功能：</p> 
<ul> 
 <li>全局系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_redact_log" target="_blank"><code>tidb_redact_log</code></a>：默认值为 0，即关闭脱敏。设置变量值为 1 开启 tidb-server 的日志脱敏功能。</li> 
 <li>配置项 <code>security.redact-info-log</code>：默认值为 false，即关闭脱敏。设置配置项值为 true 开启 tikv-server 的日志脱敏功能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F2852" target="_blank">#2852</a></li> 
 <li>配置项 <code>security.redact-info-log</code>：默认值为 false，即关闭脱敏。设置配置项值为 true 开启 pd-server 的日志脱敏功能。</li> 
 <li>配置项 <code>security.redact_info_log</code>（对于 tiflash-server）和配置项 <code>security.redact-info-log</code>（对于 tiflash-learner）：两个配置项的默认值均为 false，即关闭脱敏。设置配置项值为 true 开启 tiflash-server 及 tiflash-learner 的日志脱敏功能。</li> 
</ul> 
<p>此功能从 5.0 版本中开始提供，使用过程中必须开启以上所有系统变量及配置项。</p> 
<h2>性能优化</h2> 
<h3>MPP 架构</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fuse-tiflash" target="_blank">用户文档</a></p> 
<p>TiDB 通过 TiFlash 节点引入了 MPP 架构。这使得大型表连接类查询可以由不同 TiFlash 节点分担共同完成。</p> 
<p>当 MPP 模式开启后，TiDB 会通过代价决策是否应该交由 MPP 框架进行计算。MPP 模式下，表连接将通过对 JOIN Key 进行数据计算时重分布（Exchange 操作）的方式把计算压力分摊到各个 TiFlash 执行节点，从而达到加速计算的目的。更进一步，加上之前 TiFlash 已经支持的聚合计算，MPP 模式下 TiDB 可以将一个查询的计算都下推到 TiFlash MPP 集群，从而借助分布式环境加速整个执行过程，大幅度提升分析查询速度。</p> 
<p>经过 Benchmark 测试，在 TPC-H 100 的规模下，TiFlash MPP 提供了显著超越 Greenplum，Apache Spark 等传统分析数据库或数据湖上分析引擎的速度。借助这套架构，用户可以直接针对最新的交易数据进行大规模分析查询，且性能超越传统离线分析方案。经测试，TiDB 5.0 在同等资源下，MPP 引擎的总体性能是 Greenplum 6.15.0 与 Apache Spark 3.1.1 两到三倍之间，部分查询可达 8 倍性能差异。</p> 
<p>当前 MPP 模式不支持的主要功能如下（详细信息请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fuse-tiflash" target="_blank">用户文档</a>）：</p> 
<ul> 
 <li>分区表</li> 
 <li>Window Function</li> 
 <li>Collation</li> 
 <li>部分内置函数</li> 
 <li>读取 TiKV 数据</li> 
 <li>OOM Spill</li> 
 <li>Union</li> 
 <li>Full Outer Join</li> 
</ul> 
<h3>聚簇索引</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fclustered-indexes" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F4841" target="_blank">#4841</a></p> 
<p>DBA、数据库应用开发者在设计表结构时或者分析业务数据的行为时，如果发现有部分列经常分组排序、返回某范围的数据、返回少量不同的值的数据、有主键列及业务数据不会有读写热点时，建议选择聚簇索引。</p> 
<p>聚簇索引 (Clustered Index)，部分数据库管理系统也叫索引组织表，是一种和表的数据相关联的存储结构。创建聚簇索引时可指定包含表中的一列或多列作为索引的键值。这些键存储在一个结构中，使 TiDB 能够快速有效地找到与键值相关联的行，提升查询和写入数据的性能。</p> 
<p>开启聚簇索引功能后，TiDB 性能在一些场景下会有较大幅度的提升。例如，TPC-C tpmC 的性能提升了 39%。聚簇索引主要在以下场景会有性能提升：</p> 
<ul> 
 <li>插入数据时会减少一次从网络写入索引数据。</li> 
 <li>等值条件查询仅涉及主键时会减少一次从网络读取数据。</li> 
 <li>范围条件查询仅涉及主键时会减少多次从网络读取数据。</li> 
 <li>等值或范围条件查询涉及主键的前缀时会减少多次从网络读取数据。</li> 
</ul> 
<p>每张表既可以采用聚簇索引排序存储数据，也可以采用非聚簇索引，两者区别如下：</p> 
<ul> 
 <li>创建聚簇索引时，可指定包含表中的一列或多列作为索引的键值，聚簇索引根据键值对表的数据进行排序和存储，每张表只能有一个聚簇索引，当某张表有聚簇索引时，该表称为聚簇索引表。相反如果该表没有聚簇索引，称为非聚簇索引表。</li> 
 <li>创建非聚簇索引时，表中的数据存储在无序结构中，用户无需显式指定非聚簇索引的键值，系统会自动为每一行数据分配唯一的 ROWID，标识一行数据的位置信息，查询数据时会用 ROWID 定位一行数据。查询或者写入数据时至少会有两次网络 I/O，因此查询或者写入数据的性能相比聚簇索引会有所下降。</li> 
</ul> 
<p>当修改表的数据时，数据库系统会自动维护聚簇索引和非聚簇索引，用户无需参与。</p> 
<p>系统默认采用非聚簇索引，用户可以通过以下两种方式选择使用聚簇索引或非聚簇索引：</p> 
<ul> 
 <li> <p>创建表时在语句上指定 <code>CLUSTERED | NONCLUSTERED</code>，指定后系统将按照指定的方式创建表。具体语法如下：</p> <pre><code>CREATE TABLE `t` (`a` VARCHAR(255), `b` INT, PRIMARY KEY (`a`, `b`) CLUSTERED);</code></pre> <p>或者：</p> <pre><code>CREATE TABLE `t` (`a` VARCHAR(255) PRIMARY KEY CLUSTERED, `b` INT);</code></pre> <p>通过 <code>SHOW INDEX FROM tbl-name</code> 语句可查询表是否有聚簇索引。</p> </li> 
 <li> <p>设置 <code>tidb_enable_clustered_index</code> 控制聚簇索引功能，取值：ON|OFF|INT_ONLY</p> 
  <ul> 
   <li>ON：开启聚簇索引，支持添加或者删除非聚簇索引。</li> 
   <li>OFF：关闭聚簇索引，支持添加或者删除非聚簇索引。</li> 
   <li>INT_ONLY：默认值，行为与 5.0 以下版本保持一致，与 <code>alter-primary-key = false</code> 一起使用可控制 INT 类型是否开启聚簇索引。</li> 
  </ul> </li> 
</ul> 
<p>优先级方面，建表时有指定 <code>CLUSTERED | NONCLUSTERED</code> 时，优先级高于系统变量和配置项。</p> 
<p>推荐创建表时在语句上指定 <code>CLUSTERED | NONCLUSTERED</code> 的方式使用聚簇索引和非聚簇索引，此方式对业务更加灵活，业务可以根据需求在同一个系统同时使用所有数据类型的聚簇索引和非聚簇索引。</p> 
<p>不推荐使用 <code>tidb_enable_clustered_index = INT_ONLY</code>，原因是 INT_ONLY 是满足兼容性而临时设置的值，不推荐使用，未来会废弃。</p> 
<p>聚簇索引功能有如下限制：</p> 
<ul> 
 <li>不支持聚簇索引和非聚簇索引相互转换。</li> 
 <li>不支持删除聚簇索引。</li> 
 <li>不支持通过 <code>ALTER TABLE</code> SQL 语句增加、删除、修改聚簇索引。</li> 
 <li>不支持重组织和重建聚簇索引。</li> 
 <li>不支持启用、禁用索引，也就是不可见索引功能对聚簇索引不生效。</li> 
 <li>不支持 <code>UNIQUE KEY</code> 作为聚簇索引。</li> 
 <li>不支持与 TiDB Binlog 一起使用。开启 TiDB Binlog 后 TiDB 只允许创建单个整数列作为主键的聚簇索引；已创建的聚簇索引表的数据插入、删除和更新动作不会通过 TiDB Binlog 同步到下游。</li> 
 <li>不支持与 <code>SHARD_ROW_ID_BITS</code> 和 <code>PRE_SPLIT_REGIONS</code> 属性一起使用。</li> 
 <li>集群升级回滚时，存量的表不受影响，新增表可以通过导入、导出数据的方式降级。</li> 
</ul> 
<h3>异步提交事务（Async Commit)</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_enable_async_commit-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F8316" target="_blank">#8316</a></p> 
<p>数据库的客户端会同步等待数据库系统通过两阶段 (2PC) 完成事务的提交，事务在第一阶段提交成功后就会返回结果给客户端，系统会在后台异步执行第二阶段提交操作，降低事务提交的延迟。如果事务的写入只涉及一个 Region，则第二阶段可以直接被省略，变成一阶段提交。</p> 
<p>开启异步提交事务特性后，在硬件、配置完全相同的情况下，Sysbench 设置 64 线程测试 Update index 时, 平均延迟由 12.04 ms 降低到 7.01ms ，降低了 41.7%。</p> 
<p>开启异步提交事务特性时，数据库应用开发人员可以考虑将事务的一致性从线性一致性降低到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftransaction-overview%23%25E5%259B%25A0%25E6%259E%259C%25E4%25B8%2580%25E8%2587%25B4%25E6%2580%25A7%25E4%25BA%258B%25E5%258A%25A1" target="_blank">因果一致性</a>，减少 1 次网络交互降低延迟，提升数据写入的性能。开启因果一致性的 SQL 语句为 <code>START TRANSACTION WITH CAUSAL CONSISTENCY</code>。</p> 
<p>开启因果一致性后，在硬件和配置完全相同的情况下，Sysbench 设置 64 线程测试 oltp_write_only 时，平均延迟由 11.86ms 降低到 11.19ms，降低了 5.6%。</p> 
<p>事务的一致性从线性一致性降低到因果一致性后，如果应用程序中多个事务之间没有相互依赖关系时，事务没有全局一致的顺序。</p> 
<p><strong>新创建的 5.0 集群默认开启异步提交事务功能。</strong></p> 
<p>从旧版本升级到 5.0 的集群，默认不开启该功能，你可以执行 <code>set global tidb_enable_async_commit = ON;</code> 和 <code>set global tidb_enable_1pc = ON;</code> 语句开启该功能。</p> 
<p>异步提交事务功能有如下限制：</p> 
<ul> 
 <li>不支持直接降级</li> 
</ul> 
<h3>默认开启 Coprocessor cache 功能</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23tikv-clientcopr-cache-%25E4%25BB%258E-v400-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank">用户文档</a></p> 
<p>5.0 GA 默认开启 Coprocessor cache 功能。开启此功能后，TiDB 会在 tidb-server 中缓存算子下推到 tikv-server 计算后的结果，降低读取数据的延时。</p> 
<p>要关闭 Coprocessor cache 功能，你可以修改 <code>tikv-client.copr-cache</code> 的 <code>capacity-mb</code> 配置项为 0.0。</p> 
<h3>提升 <code>delete * from table where id < ? limit ?</code> 语句执行的性能</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18028" target="_blank">#18028</a></p> 
<p><code>delete * from table where id < ? limit ?</code> 语句执行的 p99 性能提升了 4 倍。</p> 
<h3>优化 load base 切分策略，解决部分小表热点读场景数据无法切分的性能问题</h3> 
<h2>稳定性提升</h2> 
<h3>优化因调度功能不完善引起的性能抖动问题</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18005" target="_blank">#18005</a></p> 
<p>TiDB 调度过程中会占用 I/O、网络、CPU、内存等资源，若不对调度的任务进行控制，QPS 和延时会因为资源被抢占而出现性能抖动问题。</p> 
<p>通过以下几项的优化，测试 8 小时，TPC-C 测试中 tpm-C 抖动标准差的值小于等于 2%。</p> 
<h4>引入新的调度算分公式，减少不必要的调度，减少因调度引起的性能抖动问题</h4> 
<p>当节点的总容量总是在系统设置的水位线附近波动或者 <code>store-limit</code> 配置项设置过大时，为满足容量负载的设计，系统会频繁地将 Region 调度到其他节点，甚至还会调度到原来的节点，调度过程中会占用 I/O、网络、CPU、内存等资源，引起性能抖动问题，但这类调度其实意义不大。</p> 
<p>为缓解此问题，PD 引入了一套新的调度算分公式并默认开启，可通过 <code>region-score-formula-version = v1</code> 配置项切换回之前的调度算分公式。</p> 
<h4>默认开启跨表合并 Region 功能</h4> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fpd-configuration-file%23enable-cross-table-merge" target="_blank">用户文档</a></p> 
<p>在 5.0 之前，TiDB 默认关闭跨表合并 Region 的功能。从 5.0 起，TiDB 默认开启跨表合并 Region 功能，减少空 Region 的数量，降低系统的网络、内存、CPU 的开销。你可以通过修改 <code>schedule.enable-cross-table-merge</code> 配置项关闭此功能。</p> 
<h4>默认开启自动调整 Compaction 压缩的速度，平衡后台任务与前端的数据读写对 I/O 资源的争抢</h4> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftikv-configuration-file%23rate-limiter-auto-tuned-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank">用户文档</a></p> 
<p>在 5.0 之前，为了平衡后台任务与前端的数据读写对 I/O 资源的争抢，自动调整 Compaction 的速度这个功能默认是关闭的；从 5.0 起，TiDB 默认开启此功能并优化调整算法，开启之后延迟抖动比未开启此功能时的抖动大幅减少。</p> 
<p>你可以通过修改 <code>rate-limiter-auto-tuned</code> 配置项关闭此功能。</p> 
<h4>默认开启 GC in Compaction filter 功能，减少 GC 对 CPU、I/O 资源的占用</h4> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fgarbage-collection-configuration%23gc-in-compaction-filter-%25E6%259C%25BA%25E5%2588%25B6" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18009" target="_blank">#18009</a></p> 
<p>TiDB 在进行垃圾回收和数据 Compaction 时，分区会占用 CPU、I/O 资源，系统执行这两个任务过程中存在数据重叠。</p> 
<p>GC Compaction Filter 特性将这两个任务合并在同一个任务中完成，减少对 CPU、I/O 资源的占用。系统默认开启此功能，你可以通过设置 <code>gc.enable-compaction-filter = false</code> 关闭此功能。</p> 
<h4>TiFlash 限制压缩或整理数据占用 I/O 资源（<strong>实验特性</strong>）</h4> 
<p>该特性能缓解后台任务与前端的数据读写对 I/O 资源的争抢。</p> 
<p>系统默认关闭该特性，你可以通过 <code>bg_task_io_rate_limit</code> 配置项开启限制压缩或整理数据 I/O 资源。</p> 
<h4>增强检查调度约束的性能，提升大集群中修复不健康 Region 的性能</h4> 
<h3>保证执行计划在最大程度保持不变，避免性能抖动</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsql-plan-management" target="_blank">用户文档</a></p> 
<h4>SQL BINDING 支持 <code>INSERT</code>、<code>REPLACE</code>、<code>UPDATE</code>、<code>DELETE</code> 语句</h4> 
<p>在数据库性能调优或者运维过程中，如果发现因为执行计划不稳定导致系统性能不稳定时，你可以根据自身的经验或者通过 <code>EXPLAIN ANALYZE</code> 测试选择一条人为优化过的 SQL 语句，通过 SQL BINDING 将优化过的 SQL 语句与业务代码执行的 SQL 语句绑定，确保性能的稳定性。</p> 
<p>通过 SQL BINDING 语句手动的绑定 SQL 语句时，你需要确保优化过的 SQL 语句的语法与原来 SQL 语句的语法保持一致。</p> 
<p>你可以通过 <code>SHOW &#123;GLOBAL | SESSION&#125; BINDINGS</code> 命令查看手工、系统自动绑定的执行计划信息。输出信息基本跟 5.0 之前的版本保持一致。</p> 
<h4>自动捕获、绑定执行计划</h4> 
<p>在升级 TiDB 时，为避免性能抖动问题，你可以开启自动捕获并绑定执行计划的功能，由系统自动捕获并绑定最近一次执行计划然后存储在系统表中。升级完成后，你可以通过 <code>SHOW GLOBAL BINDINGS</code> 导出绑定的执行计划，自行分析并决策是否要删除绑定的执行计划。</p> 
<p>系统默认关闭自动捕获并绑定执行计划的功能，你可以通过修改 Server 或者设置全局系统变量 <code>tidb_capture_plan_baselines = ON</code> 开启此功能。开启此功能后，系统每隔 <code>bind-info-lease</code> (默认 3 秒）从 Statement Summary 抓取出现过至少 2 次的 SQL 语句并自动捕获、绑定。</p> 
<h3>TiFlash 查询稳定性提升</h3> 
<p>新增系统变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_allow_fallback_to_tikv-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_allow_fallback_to_tikv</code></a>，用于决定在 TiFlash 查询失败时，自动将查询回退到 TiKV 尝试执行，默认为 OFF。</p> 
<h3>TiCDC 稳定性提升，缓解同步过多增量变更数据的 OOM 问题</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fmanage-ticdc%23unified-sorter-%25E5%258A%259F%25E8%2583%25BD" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1150" target="_blank">#1150</a></p> 
<p>自 v4.0.9 版本起，TiCDC 引入变更数据本地排序功能 Unified Sorter。在 5.0 版本，默认开启此功能以缓解类似场景下的 OOM 问题：</p> 
<ul> 
 <li>场景一：TiCDC 数据订阅任务暂停中断时间长，其间积累了大量的增量更新数据需要同步。</li> 
 <li>场景二：从较早的时间点启动数据订阅任务，业务写入量大，积累了大量的更新数据需要同步。</li> 
</ul> 
<p>Unified Sorter 整合了老版本提供的 memory、file sort-engine 配置选择，不需要用户手动配置变更的运维操作。</p> 
<p>限制与约束：</p> 
<ul> 
 <li>用户需要根据业务数据更新量提供充足的磁盘空间，推荐使用大于 128G 的 SSD 磁盘。</li> 
</ul> 
<h2>高可用和容灾</h2> 
<h3>提升 Region 成员变更时的可用性</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fpd-configuration-file%23enable-joint-consensus-%25E4%25BB%258E-v50-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18079" target="_blank">#18079</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F7587" target="_blank">#7587</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F2860" target="_blank">#2860</a></p> 
<p>Region 在完成成员变更时，由于“添加”和“删除”成员操作分成两步，如果两步操作之间有故障发生会引起 Region 不可用并且会返回前端业务的错误信息。</p> 
<p>TiDB 引入的 Raft Joint Consensus 算法将成员变更操作中的“添加”和“删除”合并为一个操作，并发送给所有成员，提升了 Region 成员变更时的可用性。在变更过程中，Region 处于中间的状态，如果任何被修改的成员失败，系统仍然可以使用。</p> 
<p>系统默认开启此功能，你可以通过 <code>pd-ctl config set enable-joint-consensus</code> 命令设置选项值为 false 关闭此功能。</p> 
<h3>优化内存管理模块，降低系统 OOM 的风险</h3> 
<p>跟踪统计聚合函数的内存使用情况，系统默认开启该功能，开启后带有聚合函数的 SQL 语句在执行时，如果当前查询内存总的使用量超过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23mem-quota-query" target="_blank"><code>mem-quota-query</code></a> 阈值时，系统自动采用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftidb-configuration-file%23oom-action" target="_blank"><code>oom-action</code></a> 定义的相应操作。</p> 
<h3>提升系统在发生网络分区时的可用性</h3> 
<h2>数据迁移</h2> 
<h3>从 S3/Aurora 数据迁移到 TiDB</h3> 
<p>数据迁移类工具支持 Amazon S3（也包含支持 S3 协议的其他存储服务）作为数据迁移的中间转存介质，同时支持将 Aurora 快照数据直接初始化 TiDB 中，丰富了数据从 Amazon S3/Aurora 迁移到 TiDB 的选择。</p> 
<p>该功能使用方法可以参照以下文档：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fdumpling-overview%23%25E5%25AF%25BC%25E5%2587%25BA%25E5%2588%25B0-amazon-s3-%25E4%25BA%2591%25E7%259B%2598" target="_blank">将 MySQL/Aurora 数据导出到 Amazon S3</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fissues%2F8" target="_blank">#8</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fmigrate-from-aurora-using-lightning" target="_blank">从 Amazon S3 将 Aurora Snapshot 数据初始化到 TiDB</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb-lightning%2Fissues%2F266" target="_blank">#266</a></li> 
</ul> 
<h3>TiDB Cloud 数据导入性能优化</h3> 
<p>数据导入工具 TiDB Lightning 针对 TiDB Cloud AWS T1.standard 配置（及其等同配置）的 TiDB 集群进行了数据导入性能优化，测试结果显式使用 TiDB Lightning 导入 1TB TPC-C 数据到 TiDB，性能提升了 40%，由 254 GiB/h 提升到了 366 GiB/h。</p> 
<h2>TiDB 数据共享订阅</h2> 
<h3>TiCDC 集成第三方生态 Kafka Connect (Confluent Platform)（<strong>实验特性</strong>）</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fintegrate-confluent-using-ticdc" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F660" target="_blank">#660</a></p> 
<p>为满足将 TiDB 的数据流转到其他系统以支持相关的业务需求，该功能可以把 TiDB 数据流转到 Kafka、Hadoop、 Oracle 等系统。</p> 
<p>Confluent 平台提供的 kafka connectors 协议支持向不同协议关系型或非关系型数据库传输数据，在社区被广泛使用。TiDB 通过 TiCDC 集成到 Confluent 平台的 Kafka Connect，扩展了 TiDB 数据流转到其他异构数据库或者系统的能力。</p> 
<h3>TiCDC 支持 TiDB 集群之间环形同步（<strong>实验特性</strong>）</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fmanage-ticdc%23%25E7%258E%25AF%25E5%25BD%25A2%25E5%2590%258C%25E6%25AD%25A5" target="_blank">用户文档</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F471" target="_blank">#471</a></p> 
<p>由于地理位置差异导致的通讯延迟等问题，存在以下场景：用户部署多套 TiDB 集群到不同的地理区域来支撑其当地的业务，然后通过各个 TiDB 之间相互复制，或者汇总复制数据到一个中心 TiDB hub，来完成诸如分析、结算等业务。</p> 
<p>TiCDC 支持在多个独立的 TiDB 集群间同步数据。比如有三个 TiDB 集群 A、B 和 C，它们都有一个数据表 test.user_data，并且各自对它有数据写入。环形同步功能可以将 A、B 和 C 对 test.user_data 的写入同步到其它集群上，使三个集群上的 test.user_data 达到最终一致。</p> 
<p>该功能适用于以下场景：</p> 
<ul> 
 <li>多套 TiDB 集群之间相互进行数据备份，灾难发生时业务切换到正常的 TiDB 集群</li> 
 <li>跨地域部署多套 TiDB 集群支撑当地业务，TiDB 集群之间的同一业务表之间数据需要相互复制</li> 
</ul> 
<p>限制与约束：</p> 
<ul> 
 <li>无法支持业务在不同集群写入使用自增 ID 的业务表，数据复制会导致业务数据相互覆盖而造成数据丢失</li> 
 <li>无法支持业务在不同集群写入相同业务表的相同数据，数据复制会导致业务数据相互覆盖而造成数据丢失</li> 
</ul> 
<h2>问题诊断</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsql-statement-explain%23explain" target="_blank">用户文档</a></p> 
<p>在排查 SQL 语句性能问题时，需要详细的信息来判断引起性能问题的原因。5.0 版本之前，<code>EXPLAIN</code> 收集的信息不够完善，DBA 只能通过日志信息、监控信息或者盲猜的方式来判断问题的原因，效率比较低。</p> 
<p>5.0 版本中，通过以下几项优化提升排查问题的效率：</p> 
<ul> 
 <li>支持对所有 DML 语句使用 <code>EXPLAIN ANALYZE</code> 语句以查看实际的执行计划及各个算子的执行详情。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18056" target="_blank">#18056</a></li> 
 <li>支持对正在执行的 SQL 语句使用 <code>EXPLAIN FOR CONNECTION</code> 语句以查看实时执行状态，例如各个算子的执行时间、已处理的数据行数等。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18233" target="_blank">#18233</a></li> 
 <li><code>EXPLAIN ANALYZE</code> 语句显示的算子执行详情中新增算子发送的 RPC 请求数、处理锁冲突耗时、网络延迟、RocksDB 已删除数据的扫描量、RocksDB 缓存命中情况等。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F18663" target="_blank">#18663</a></li> 
 <li>慢查询日志中自动记录 SQL 语句执行时的详细执行状态，输出的信息与 <code>EXPLAIN ANALYZE</code> 语句输出信息保持一致，例如各个算子消耗的时间、处理数据行数、发送的 RPC 请求数等。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F15009" target="_blank">#15009</a></li> 
</ul> 
<h2>部署及运维</h2> 
<h3>优化集群部署操作逻辑，帮助 DBA 更快地部署一套标准的 TiDB 生产集群</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fproduction-deployment-using-tiup" target="_blank">用户文档</a></p> 
<p>DBA 在使用 TiUP 部署 TiDB 集群过程发现环境初始化比较复杂、校验配置过多，集群拓扑文件比较难编辑等问题，导致 DBA 的部署效率比较低。5.0 版本通过以下几个事项提升 DBA 部署 TiDB 的效率：</p> 
<ul> 
 <li>TiUP Cluster 支持使用 <code>check topo.yaml</code> 命令，进行更全面一键式环境检查并给出修复建议。</li> 
 <li>TiUP Cluster 支持使用 <code>check topo.yaml --apply</code> 命令，自动修复检查过程中发现的环境问题。</li> 
 <li>TiUP Cluster 支持 <code>template</code> 命令，获取集群拓扑模板文件，供 DBA 编辑且支持修改全局的节点参数。</li> 
 <li>TiUP 支持使用 <code>edit-config</code> 命令编辑 <code>remote_config</code> 参数配置远程 Prometheus。</li> 
 <li>TiUP 支持使用 <code>edit-config</code> 命令编辑 <code>external_alertmanagers</code> 参数配置不同的 AlertManager。</li> 
 <li>在 tiup-cluster 中使用 <code>edit-config</code> 子命令编辑拓扑文件时允许改变配置项值的数据类型。</li> 
</ul> 
<h3>提升升级稳定性</h3> 
<p>TiUP v1.4.0 版本以前，DBA 使用 tiup-cluster 升级 TiDB 集群时会导致 SQL 响应持续长时间抖动，PD 在线滚动升级期间集群 QPS 抖动时间维持在 10~30s。</p> 
<p>TiUP v1.4.0 版本调整了逻辑，优化如下：</p> 
<ul> 
 <li>升级 PD 时，会主动判断被重启的 PD 节点状态，确认就绪后再滚动升级下一个 PD 节点。</li> 
 <li>主动识别 PD 角色，先升级 follower 角色 PD 节点，最后再升级 PD Leader 节点。</li> 
</ul> 
<h3>优化升级时长</h3> 
<p>TiUP v1.4.0 版本以前，DBA 使用 tiup-cluster 升级 TiDB 集群时，对于节点数比较多的集群，整个升级的时间会持续很长，不能满足部分有升级时间窗口要求的用户。</p> 
<p>从 v1.4.0 版本起，TiUP 进行了以下几处优化：</p> 
<ul> 
 <li>新版本 TiUP 支持使用 <code>tiup cluster upgrade --offline</code> 子命令实现快速的离线升级。</li> 
 <li>对于使用滚动升级的用户，新版本 TiUP 默认会加速升级期间 Region Leader 的搬迁速度以减少滚动升级 TiKV 消耗的时间。</li> 
 <li>运行滚动升级前使用 <code>check</code> 子命令，对 Region 监控状态的检查，确保集群升级前状态正常以减少升级失败的概率。</li> 
</ul> 
<h3>支持断点功能</h3> 
<p>TiUP v1.4.0 版本以前，DBA 使用 tiup-cluster 升级 TiDB 集群时，如果命令执行中断，那么整个升级操作都需重新开始。</p> 
<p>新版本 TiUP 支持使用 tiup-cluster <code>replay</code> 子命令从断点处重试失败的操作，以避免升级中断后所有操作重新执行。</p> 
<h3>增强运维功能</h3> 
<p>新版本 TiUP 进一步强化了 TiDB 集群运维的功能：</p> 
<ul> 
 <li>支持对已停机的 TiDB 和 DM 集群进行升级或 patch 操作，以适应更多用户的使用场景。</li> 
 <li>为 tiup-cluster 的 <code>display</code> 子命令添加 <code>--version</code> 参数用于获取集群版本。</li> 
 <li>在被缩容的节点中仅包含 Prometheus 时不执行更新监控配置的操作，以避免因 Prometheus 节点不存在而缩容失败</li> 
 <li>在使用 TiUP 命令输入结果不正确时将用户输入的内容添加到错误信息中，以便用户更快定位问题原因。</li> 
</ul> 
<h2>遥测</h2> 
<p>TiDB 在遥测中新增收集集群的使用指标，包括数据表数量、查询次数、新特性是否启用等。</p> 
<p>若要了解所收集的信息详情及如何禁用该行为，可参见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Ftelemetry" target="_blank">遥测</a>文档。</p> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Frelease-5.0.0" target="_blank">https://docs.pingcap.com/zh/tidb/stable/release-5.0.0</a></p>
                                        </div>
                                      
</div>
            