
---
title: 'TiDB 5.0.2 发布，分布式 NewSQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2674'
author: 开源中国
comments: false
date: Sat, 12 Jun 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2674'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TiDB 5.0.2 现已发布，该版本具体更新内容如下：</p> 
<h4>兼容性更改</h4> 
<ul> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>在 <code>cdc cli changefeed</code> 命令中废弃 <code>--sort-dir</code> 参数，用户可在 <code>cdc server</code> 命令中设定 <code>--sort-dir</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1795" target="_blank">#1795</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h4>新功能</h4> 
<ul> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>默认开启 Hibernate Region 特性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10266" target="_blank">#10266</a></li> 
  </ul> </li> 
</ul> 
<h4>提升改进</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>当内存中的统计信息缓存是最新的时，避免后台作业频繁读取 <code>mysql.stats_histograms</code> 表造成高 CPU 使用率 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24317" target="_blank">#24317</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>BR 支持 S3 兼容的存储（基于 virtual-host 寻址模式）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10243" target="_blank">#10243</a></li> 
   <li>为 TiCDC 扫描的速度添加背压 (back pressure) 功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10151" target="_blank">#10151</a></li> 
   <li>减少 TiCDC 进行初次扫描的内存使用量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10133" target="_blank">#10133</a></li> 
   <li>提升了悲观事务中 TiCDC Old Value 的缓存命中率 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10089" target="_blank">#10089</a></li> 
   <li>让 Region 分裂更均匀，缓解有写入热点时 Region 大小的增长速度超过分裂速度的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F9785" target="_blank">#9785</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>优化锁操作以避免 DDL 语句和读数据相互阻塞</li> 
   <li>支持 <code>INTEGER</code> 和 <code>REAL</code> 类型转化为 <code>REAL</code> 类型</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>添加关于数据表内存使用情况的监控 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1885" target="_blank">#1885</a></li> 
     <li>优化排序阶段的内存和 CPU 使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1863" target="_blank">#1863</a></li> 
     <li>删除了一些可能让用户困惑的无用日志信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1759" target="_blank">#1759</a></li> 
    </ul> </li> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>优化了一些含糊的报错信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1132" target="_blank">#1132</a></li> 
     <li>支持检查备份的版本信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1091" target="_blank">#1091</a></li> 
     <li>支持备份和恢复 <code>mysql</code> schema 下的系统表 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1143" target="_blank">#1143</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1078" target="_blank">#1078</a></li> 
    </ul> </li> 
   <li> <p>Dumpling</p> 
    <ul> 
     <li>修复备份失败却没有错误输出的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fpull%2F280" target="_blank">#280</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h4>Bug 修复</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>修复了在某些情况下，使用前缀索引和 Index Join 导致的 panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24547" target="_blank">#24547</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24716" target="_blank">#24716</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24717" target="_blank">#24717</a></li> 
   <li>修复了 <code>point get</code> 的 prepare plan cache 被事务中的 <code>point get</code> 语句不正确使用的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24741" target="_blank">#24741</a></li> 
   <li>修复了当排序规则为 <code>ascii_bin</code> 或 <code>latin1_bin</code> 时，写入错误的前缀索引值的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24569" target="_blank">#24569</a></li> 
   <li>修复了正在执行的事务被 GC worker 中断的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24591" target="_blank">#24591</a></li> 
   <li>修复了当 <code>new-collation</code> 开启且 <code>new-row-format</code> 关闭的情况下，点查在聚簇索引下可能出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24541" target="_blank">#24541</a></li> 
   <li>为 Shuffle Hash Join 重构分区键的转换功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24490" target="_blank">#24490</a></li> 
   <li>修复了当查询包含 <code>HAVING</code> 子句时，在构建计划的过程中 panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24045" target="_blank">#24045</a></li> 
   <li>修复了列裁剪优化导致 <code>Apply</code> 算子和 <code>Join</code> 算子执行结果错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F23887" target="_blank">#23887</a></li> 
   <li>修复了从 Async Commit 回退的主锁无法被清除的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24384" target="_blank">#24384</a></li> 
   <li>修复了一个统计信息 GC 的问题，该问题可能导致重复的 fm-sketch 记录 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24357" target="_blank">#24357</a></li> 
   <li>当悲观锁事务收到 <code>ErrKeyExists</code> 错误时，避免不必要的悲观事务回滚 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F23799" target="_blank">#23799</a></li> 
   <li>修复了当 sql_mode 包含 <code>ANSI_QUOTES</code> 时，数值字面值无法被识别的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24429" target="_blank">#24429</a></li> 
   <li>禁止如 <code>INSERT INTO table PARTITION (<partitions>) ... ON DUPLICATE KEY UPDATE</code> 的语句从 non-listed partitions 读取数据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24746" target="_blank">#24746</a></li> 
   <li>修复了当 SQL 语句包含 <code>GROUP BY</code> 以及 <code>UNION</code> 时，可能会出现的 <code>index out of range</code> 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24281" target="_blank">#24281</a></li> 
   <li>修复了 <code>CONCAT</code> 函数错误处理排序规则的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24296" target="_blank">#24296</a></li> 
   <li>修复了全局变量 <code>collation_server</code> 对新会话无法生效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24156" target="_blank">#24156</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>修复了由于读取旧值而导致的 TiCDC OOM 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F9996" target="_blank">#9996</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F9981" target="_blank">#9981</a></li> 
   <li>修复了聚簇主键列在次级索引上的 <code>latin1_bin</code> 字符集出现空值的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24548" target="_blank">#24548</a></li> 
   <li>新增 <code>abort-on-panic</code> 配置，允许 TiKV 在 panic 时生成 core dump 文件。用户仍需正确配置环境以开启 core dump。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10216" target="_blank">#10216</a></li> 
   <li>修复了 TiKV 不繁忙时 <code>point get</code> 查询性能回退的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10046" target="_blank">#10046</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>修复在 store 数量多的情况下，切换 PD Leader 慢的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3697" target="_blank">#3697</a></li> 
   <li>修复删除不存在的 evict leader 调度器时出现 panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3660" target="_blank">#3660</a></li> 
   <li>修复 offline peer 在合并完后未更新统计的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3611" target="_blank">#3611</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>修复并发复制共享 Delta 索引导致结果错误的问题</li> 
   <li>修复当存在数据缺失的情况下 TiFlash 无法启动的问题</li> 
   <li>修复旧的 dm 文件无法被自动清理的问题</li> 
   <li>修复 TiFlash 在 Compaction Filter 特性开启时可能崩溃的问题</li> 
   <li>修复 <code>ExchangeSender</code> 可能传输重复数据的问题</li> 
   <li>修复了从 Async Commit 回退的锁无法被 TiFlash 清除的问题</li> 
   <li>修复当 <code>TIMEZONE</code> 类型的转换结果包含 <code>TIMESTAMP</code> 类型时返回错误结果的问题</li> 
   <li>修复 TiFlash 在 Segment Split 期间异常退出的问题</li> 
   <li>修复非根节点 MPP 任务的执行信息显示不正确的问题</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>修复 Avro 输出中丢失时区信息的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1712" target="_blank">#1712</a></li> 
     <li>支持清理 Unified Sorter 过期的文件并禁止共享 <code>sort-dir</code> 目录 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1742" target="_blank">#1742</a></li> 
     <li>修复存在大量过期 Region 信息时 KV 客户端可能锁死的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1599" target="_blank">#1599</a></li> 
     <li>修复 <code>--cert-allowed-cn</code> 参数中错误的帮助消息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1697" target="_blank">#1697</a></li> 
     <li>修复因更新 <code>explicit_defaults_for_timestamp</code> 而需要 MySQL <code>SUPER</code> 权限的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1750" target="_blank">#1750</a></li> 
     <li>添加 sink 流控以降低内存溢出的风险 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1840" target="_blank">#1840</a></li> 
     <li>修复调度数据表时可能发生的同步终止问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1828" target="_blank">#1828</a></li> 
     <li>修复 TiCDC changefeed 断点卡住导致 TiKV GC safe point 不推进的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1759" target="_blank">#1759</a></li> 
    </ul> </li> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>修复 log restore 时丢失删除事件的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1063" target="_blank">#1063</a></li> 
     <li>修复 BR 发送过多无用 RPC 请求到 TiKV 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1037" target="_blank">#1037</a></li> 
     <li>修复备份失败却没有错误输出的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1043" target="_blank">#1043</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>修复在生成 KV 数据时可能发生的 panic 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1127" target="_blank">#1127</a></li> 
     <li>修复 TiDB-backend 模式下因没有开启 autocommit 而无法加载数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1104" target="_blank">#1104</a></li> 
     <li>修复数据导入期间 Batch Split Region 因键的总大小超过 Raft 条目限制而可能失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F969" target="_blank">#969</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Frelease-5.0.2" target="_blank">https://docs.pingcap.com/zh/tidb/stable/release-5.0.2</a></p>
                                        </div>
                                      
</div>
            