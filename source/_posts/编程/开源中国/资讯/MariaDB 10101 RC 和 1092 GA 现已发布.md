
---
title: 'MariaDB 10.10.1 RC 和 10.9.2 GA 现已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=135'
author: 开源中国
comments: false
date: Wed, 24 Aug 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=135'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">MariaDB 10.10.1 RC 和 10.9.2 GA 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmariadb.org%2Fmariadb-10-10-1-rc-and-10-9-2-ga-now-available%2F" target="_blank">推出</a>。MariaDB 基金会宣布了 MariaDB 10.10.1 的可用性，这是 MariaDB 10.10 系列中的第一个候选版本，而 MariaDB 10.9.2 则是 MariaDB 10.9 系列中的第一个普遍可用的版本。这些都是短期支持系列，在 GA 后维护一年。</span></p> 
<p><span style="color:#000000">一些亮点更新内容包括：</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>InnoDB</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>由于缺少文件锁定而导致 InnoDB 损坏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28495" target="_blank">MDEV-28495</a> )</li> 
 <li>带撇号和强制字词的 FULLTEXT search ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-20797" target="_blank">MDEV-20797</a> )</li> 
 <li>ALTER TABLE IMPORT TABLESPACE 损坏了加密表 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28779" target="_blank">MDEV-28779</a> )</li> 
 <li>ALTER TABLE 错误结果修复 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-26294" target="_blank">MDEV-26294</a> )</li> 
 <li>崩溃恢复修复 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28668" target="_blank">MDEV-28668</a> , <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28731" target="_blank">MDEV-28731</a> )</li> 
 <li>DDL 崩溃恢复修复（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28752" target="_blank">MDEV-28752</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28802" target="_blank">MDEV-28802</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28864" target="_blank">MDEV-28864、MDEV-28870</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28923" target="_blank">MDEV-28923</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28977" target="_blank">MDEV-28977</a>）</li> 
 <li>避免损坏数据崩溃（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-13542" target="_blank">MDEV-13542</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-18519" target="_blank">MDEV-18519</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-21098" target="_blank">MDEV-21098</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-22388" target="_blank">MDEV-22388</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28457" target="_blank">MDEV-28457</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28950" target="_blank">MDEV-28950</a>）</li> 
 <li>批量加载错误修复 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28242" target="_blank">MDEV-28242</a> , <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28679" target="_blank">MDEV-28679</a> )</li> 
 <li>性能修复（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28708" target="_blank">MDEV-28708</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28766" target="_blank">MDEV-28766</a>）</li> 
 <li>删除 innodb_version ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28554" target="_blank">MDEV-28554</a> )</li> 
 <li>弃用并忽略参数 innodb_prefix_index_cluster_optimization ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28540" target="_blank">MDEV-28540</a> )</li> 
 <li>SHOW ENGINE INNODB STATUS 中的无用输出 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28542" target="_blank">MDEV-28542</a> )</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Replication</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>ER_SLAVE_INCIDENT 错误现在被指定在 slave 上，以便通过 SHOW-SLAVE-STATUS 看到 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-21087" target="_blank">MDEV-21087</a>)</li> 
 <li>当正在记录的事务可以安全回滚时，INCIDENT_EVENT 不再被 binlogged <span style="background-color:#ffffff; color:#333333">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-21443" target="_blank">MDEV-21443</a><span style="background-color:#ffffff; color:#333333">)</span></li> 
 <li>序列相关的行格式事件对应于 binlog_row_image ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28487" target="_blank">MDEV-28487</a> )</li> 
 <li>消除了 FLUSH BINARY LOGS 挂起的可能原因 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28948" target="_blank">MDEV-28948</a> )</li> 
 <li>修复循环半同步设置中的 out-of-order gtid 错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28609" target="_blank">MDEV-28609</a> )</li> 
 <li>为 SQL 线程添加了 global.slave_max_statement_time 选项，以限制每个查询复制的最大执行时间 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-27161" target="_blank">MDEV-27161</a> )</li> 
 <li>CHANGE MASTER 的 MASTER_USE_GTID=Current_Pos 已弃用，以支持新的 MASTER_DEMOTE_TO_SLAVE 选项 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-20122" target="_blank">MDEV-20122</a> )</li> 
 <li>CHANGE MASTER TO 和 RESET SLAVE 的 MASTER_USE_GTID 默认值已更改为与 GTID-based replication 兼容 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-19801" target="_blank">MDEV-19801</a> )</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Galera</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>在 read_only=ON 而不是 SUPER 权限的情况下，有可能 write/update ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28546" target="_blank">MDEV-28546</a> )</li> 
 <li>节点崩溃，传输端点未连接 mysqld 得到 signal 6 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-25068" target="_blank">MDEV-25068</a> )</li> 
 <li>Galera4 无法报告正确的 wsrep_incoming_addresses ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-20627" target="_blank">MDEV-20627</a> )</li> 
 <li>Galera 应该在 INCREMENT <> 0 的序列中复制与 nextval() 相关的更改，至少是 engine=InnoDB 的 NOCACHE 序列 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-27862" target="_blank">MDEV-27862</a> )</li> 
 <li>在 Galera 中添加对 OpenSSL 3.0 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-25949" target="_blank">( MDEV-25949</a> ) </li> 
 <li>实现一种方法，将 IP 添加到可以发出 SST/IST 请求的 Galera Cluster 节点地址的允许列表 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-27246" target="_blank">MDEV-27246</a> )</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Optimizer</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>JOIN_CACHE::free 或 copy_fields 中的服务器崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-23809" target="_blank">MDEV-23809</a> ) 
  <ul> 
   <li>使用 DISTINCT 和像 COLLATION(aggegate_func(...)) 这样的常量函数的查询可能会导致服务器崩溃。请注意，COLLATION() 是一个特殊函数 - 即使它的参数不是常数，它的值也是常数。</li> 
  </ul> </li> 
 <li>在 GROUP BY 子句中使用带有冗余子查询的 ANY 谓词时崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-29139" target="_blank">MDEV-29139</a> ) 
  <ul> 
   <li>带有这种形式的子查询的查询可能会导致崩溃：</li> 
  </ul> </li> 
</ul> 
<pre><span>...</span> <strong>ANY</strong> <span>(</span><strong>SELECT</strong> <span>...</span> <strong>GROUP</strong> <strong>BY</strong> <span>(</span><strong>SELECT</strong> <span>redundant_subselect_here</span><span>))</span> <span>...</span></pre> 
<ul> 
 <li>MariaDB Server SEGV on INSERT .. SELECT ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-26427" target="_blank">MDEV-26427</a> ) 
  <ul> 
   <li>“INSERT ... SELECT with_aggregate_or_window_func”形式的某些查询可能会导致崩溃。</li> 
  </ul> </li> 
 <li>restore_prev_nj_state() 没有正确更新 cur_sj_inner_tables ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28749" target="_blank">MDEV-28749</a> ) 
  <ul> 
   <li>子查询半连接优化可能会错过某些查询的 LooseScan 或 FirstMatch 策略。</li> 
  </ul> </li> 
 <li>升级到 10.3 后优化器使用所有分区 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28246" target="_blank">MDEV-28246</a> ) 
  <ul> 
   <li>对于多表 UPDATE 或 DELETE 查询，优化器未能对更新或删除的表应用分区修剪优化。</li> 
  </ul> </li> 
 <li>key IN (const, ....) 的 Range optimizer 回归 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-25020" target="_blank">MDEV-25020</a> ) 
  <ul> 
   <li>该问题可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmariadb.com%2Fkb%2Fen%2Fmariadb-1059-release-notes%2F" target="_blank">MariaDB 10.5.9</a> 及更高版本中观察到，这些版本具有针对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-9750" target="_blank">MDEV-9750</a> 的修复程序。该修复引入了 optimizer_max_sel_arg_weight。</li> 
   <li>如果将 optimizer_max_sel_arg_weight 设置为非常高的值或零（这意味着“无限”）并运行生成 heavy-weight graphs，他们可以观察到性能下降，例如：</li> 
  </ul> </li> 
</ul> 
<pre><strong>table</strong><span>.</span><span>keyXpartY</span> <span>[</span><strong>NOT</strong><span>]</span> <strong>IN</strong> <span>(</span> <span>...</span> <span>)</span></pre> 
<ul> 
 <li>与 not_null_range_scan 结合使用的表消除错误结果 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28858" target="_blank">MDEV-28858</a> ) 
  <ul> 
   <li>如果使用 optimizer_switch='not_null_range_scan=on' （默认情况下未启用）运行，则执行连接并具有 const 表的查询可能会产生错误的结果。</li> 
  </ul> </li> 
 <li>best_access_path 中的断言 `tmp >= 0' 失败 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28882" target="_blank">MDEV-28882</a> ) 
  <ul> 
   <li>如果使用 histogram_type=JSON_HB，收集了该类型的直方图并运行查询，选择直方图末端附近的一个非常窄的范围，则由于直方图中的舍入错误导致负选择性，他们可能会在优化器中命中断言。</li> 
  </ul> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>General</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmariadb.com%2Fkb%2Fen%2Fjson_extract%2F" target="_blank">JSON_EXTRACT</a> 中的崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-29188" target="_blank">MDEV-29188</a> ) </li> 
 <li>ALTER TABLE ALGORITHM=NOCOPY 在升级后不起作用 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28727" target="_blank">MDEV-28727</a> )</li> 
 <li>CREATE VIEW 在 ON condition 下有未知列时，服务器崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-29088" target="_blank">MDEV-29088</a> )</li> 
 <li>password_reuse_check 插件混合了用户名和密码 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mariadb.org%2Fbrowse%2FMDEV-28838" target="_blank">MDEV-28838</a> )</li> 
 <li>根据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmariadb.com%2Fkb%2Fen%2Fdeprecation-policy%2F" target="_blank">MariaDB 弃用政策</a>，这将是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmariadb.com%2Fkb%2Fen%2Fwhat-is-mariadb-1010%2F" target="_blank">MariaDB 10.10</a><span style="background-color:#ffffff; color:#333333"><span> </span>for Debian 10 "Buster" for ppc64el</span> 的最后一个版本</li> 
</ul> 
<p>更多详情可分别查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmariadb.com%2Fkb%2Fen%2Fmariadb-10101-release-notes%2F" target="_blank">MariaDB 10.10.1 Release Note</a>s 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmariadb.com%2Fkb%2Fen%2Fmariadb-1092-release-notes%2F" target="_blank">MariaDB 10.9.2 Release Notes</a>。 </p> 
<p> </p>
                                        </div>
                                      
</div>
            