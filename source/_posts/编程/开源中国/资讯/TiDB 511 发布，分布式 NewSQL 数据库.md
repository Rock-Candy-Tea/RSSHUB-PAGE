
---
title: 'TiDB 5.1.1 发布，分布式 NewSQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1160'
author: 开源中国
comments: false
date: Sun, 01 Aug 2021 08:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1160'
---

<div>   
<div class="content">
                                                                                            <p>TiDB 5.1.1 现已发布，该版本具体更新内容如下：</p> 
<h4>兼容性更改</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>对于从 v4.0 升级至 v5.1 的集群，<code>tidb_multi_statement_mode</code> 的默认值为 <code>OFF</code>。建议使用客户端库的多语句功能，参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_multi_statement_mode-%25E4%25BB%258E-v4011-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_multi_statement_mode</code> 文档</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25751" target="_blank">#25751</a></li> 
   <li>将系统变量 <code>tidb_stmt_summary_max_stmt_count</code> 的默认值从 <code>200</code> 修改为 <code>3000</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25874" target="_blank">#25874</a></li> 
   <li>访问 <code>table_storage_stats</code> 表需要 <code>SUPER</code> 权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26352" target="_blank">#26352</a></li> 
   <li>访问 <code>information_schema.user_privileges</code> 表需要 <code>mysql.user</code> 上的 <code>SELECT</code> 权限来显示其他人的权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26311" target="_blank">#26311</a></li> 
   <li>访问 <code>information_schema.cluster_hardware</code> 需要 <code>CONFIG</code> 权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26297" target="_blank">#26297</a></li> 
   <li>访问 <code>information_schema.cluster_info</code> 表需要 <code>PROCESS</code> 权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26297" target="_blank">#26297</a></li> 
   <li>访问 <code>information_schema.cluster_load</code> 表需要 <code>PROCESS</code> 权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26297" target="_blank">#26297</a></li> 
   <li>访问 <code>information_schema.cluster_systeminfo</code> 表需要 <code>PROCESS</code> 权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26297" target="_blank">#26297</a></li> 
   <li>访问 <code>information_schema.cluster_log</code> 表需要 <code>PROCESS</code> 权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26297" target="_blank">#26297</a></li> 
   <li>访问 <code>information_schema.cluster_config</code> 表需要 <code>CONFIG</code> 权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26150" target="_blank">#26150</a></li> 
  </ul> </li> 
</ul> 
<h4>功能增强</h4> 
<ul> 
 <li> <p>TiDB Dashboard</p> 
  <ul> 
   <li>新增 OIDC SSO 支持。通过设置兼容 OIDC 标准的 SSO 服务（例如 Okta、Auth0 等），用户可以在不输入 SQL 密码的情况下登录 TiDB Dashboard <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fpull%2F3883" target="_blank">#3883</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>支持 DAG 请求中的 <code>HAVING()</code> 函数</li> 
  </ul> </li> 
</ul> 
<h4>改进提升</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>Stale Read 成为正式功能 (GA)</li> 
   <li>避免对 <code>paramMarker</code> 的分配以加快数据插入速度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26076" target="_blank">#26076</a></li> 
   <li>支持稳定结果模式，使查询结果更稳定 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25995" target="_blank">#25995</a></li> 
   <li>支持将函数 <code>json_unquote()</code> 下推到 TiKV <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26265" target="_blank">#26265</a></li> 
   <li>支持 MPP 查询的重试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26480" target="_blank">#26480</a></li> 
   <li>对于 <code>point get</code> 或 <code>batch point get</code> 算子，在唯一索引写入过程中，将悲观锁 <code>LOCK</code> 记录转化为 <code>PUT</code> 记录 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26225" target="_blank">#26225</a></li> 
   <li>禁止使用 Stale 查询来进行创建视图 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26225" target="_blank">#26225</a></li> 
   <li>在 MPP 模式下彻底下推 <code>COUNT(DISTINCT)</code> 聚合函数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26194" target="_blank">#26194</a></li> 
   <li>在发起 MPP 查询之前检查 TiFlash 的可用性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26192" target="_blank">#26192</a></li> 
   <li>不允许将读时间戳设置为将来的时间 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25763" target="_blank">#25763</a></li> 
   <li>当聚合函数在 <code>EXPLAIN</code> 语句中不能被下推时打印警告日志 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25737" target="_blank">#25737</a></li> 
   <li>增加 <code>statements_summary_evicted</code> 表来记录集群的驱逐数量信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25587" target="_blank">#25587</a></li> 
   <li>提升内置函数 <code>str_to_date</code> 在格式指定器中 <code>%b/%M/%r/%T</code> 的 MySQL 兼容性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25768" target="_blank">#25768</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>提升 prewrite 请求的幂等性以减少不确定性错误的概率 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10586" target="_blank">#10586</a></li> 
   <li>预防处理多个过期命令时出现栈溢出的风险 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10502" target="_blank">#10502</a></li> 
   <li>不使用 Stale Read 请求的 <code>start_ts</code> 更新 <code>max_ts</code> 以避免过多不必要的 commit 请求重试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10451" target="_blank">#10451</a></li> 
   <li>分离处理读写的 ready 状态以减少读延迟 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10592" target="_blank">#10592</a></li> 
   <li>降低 I/O 限流器开启后对数据导入速度的影响 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10390" target="_blank">#10390</a></li> 
   <li>提升 Raft gRPC 连接的负载均衡 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10495" target="_blank">#10495</a></li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>移除 <code>file sorter</code> 文件排序器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2327" target="_blank">#2327</a></li> 
     <li>优化连接 PD 时缺少证书情况下的报错提示 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1973" target="_blank">#1973</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>为恢复 schema 添加重试机制 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1294" target="_blank">#1294</a></li> 
    </ul> </li> 
   <li> <p>Dumpling</p> 
    <ul> 
     <li>上游是 TiDB v3.x 集群时，使用 <code>_tidb_rowid</code> 来切分表以减少 TiDB 的内存使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fissues%2F295" target="_blank">#295</a></li> 
     <li>减少访问数据库元信息的频率以提升性能和稳定性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fpull%2F315" target="_blank">#315</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h4>Bug 修复</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>修复了 <code>tidb_enable_amend_pessimistic_txn=on</code> 下更改列类型可能出现数据丢失的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26203" target="_blank">#26203</a></li> 
   <li>修复了 <code>last_day</code> 函数的行为在 SQL 模式下不兼容的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26001" target="_blank">#26001</a></li> 
   <li>修复 <code>LIMIT</code> 位于窗口函数之上时可能出现的 panic 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25344" target="_blank">#25344</a></li> 
   <li>修复了提交悲观事务可能会导致写冲突的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25964" target="_blank">#25964</a></li> 
   <li>修复关联子查询中 Index Join 的结果不正确问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25799" target="_blank">#25799</a></li> 
   <li>修复了成功提交的悲观事务可能会报提交失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10468" target="_blank">#10468</a></li> 
   <li>修复在 <code>SET</code> 类型列上 Merge Join 结果不正确的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25669" target="_blank">#25669</a></li> 
   <li>修复了在悲观事务中索引键值可能会被重复提交的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26359" target="_blank">#26359</a></li> 
   <li>修复了优化器在定位分区时存在整数溢出的风险 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26227" target="_blank">#26227</a></li> 
   <li>修复了将 <code>DATE</code> 类型转换成时间戳时可能会写入无效值的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26292" target="_blank">#26292</a></li> 
   <li>修复了 Coprocessor Cache 监控项未在 Grafana 中显示的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26338" target="_blank">#26338</a></li> 
   <li>修复了遥测引起的干扰日志 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25760" target="_blank">#25760</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25785" target="_blank">#25785</a></li> 
   <li>修复了索引前缀的查询范围问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26029" target="_blank">#26029</a></li> 
   <li>修复了并发 truncate 同一个 partition 会导致 DDL 执行卡住的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26229" target="_blank">#26229</a></li> 
   <li>修复了 <code>EMUN</code> 元素重复的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25955" target="_blank">#25955</a></li> 
   <li>修复了 CTE 迭代器没有正确关闭的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26112" target="_blank">#26112</a></li> 
   <li>修复 <code>LOAD DATA</code> 语句可能不正常导入非 utf8 数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25979" target="_blank">#25979</a></li> 
   <li>修复在无符号整数列上使用窗口函数可能导致崩溃的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25956" target="_blank">#25956</a></li> 
   <li>修复了清除 Async Commit 锁时可能会导致 TiDB panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25778" target="_blank">#25778</a></li> 
   <li>修复了 Stale Read 不完全兼容 <code>PREPARE</code> 语句的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25800" target="_blank">#25800</a></li> 
   <li>修复 ODBC 类常数（例如 <code>&#123;d '2020-01-01'&#125;</code>）不能被用作表达式的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25531" target="_blank">#25531</a></li> 
   <li>修复了单独运行 TiDB 时出现的一个错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25555" target="_blank">#25555</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>修复特定平台上的 duration 计算可能崩溃的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10569" target="_blank">#10569</a></li> 
   <li>修复 Load Base Split 误用 <code>batch_get_command</code> 中未编码键的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10542" target="_blank">#10542</a></li> 
   <li>修复在线变更 <code>resolved-ts.advance-ts-interval</code> 配置无法立即生效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10426" target="_blank">#10426</a></li> 
   <li>修复在超过 4 副本的罕见场景下 Follower 元信息损坏的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10225" target="_blank">#10225</a></li> 
   <li>修复开启加密后再次生成同样的 snapshot 会出现 panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F9786" target="_blank">#9786</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10407" target="_blank">#10407</a></li> 
   <li>修正 <code>tikv_raftstore_hibernated_peer_state</code> 监控指标项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10330" target="_blank">#10330</a></li> 
   <li>修复 coprocessor 中 <code>json_unquote()</code> 函数错误的参数类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10176" target="_blank">#10176</a></li> 
   <li>修复悲观事务中索引键被重复 commit 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10468%23issuecomment-869491061" target="_blank">#10468</a></li> 
   <li>修复 <code>ReadIndex</code> 请求在 leader 迁移后返回过期数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F9351" target="_blank">#9351</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>修复多个调度器产生调度冲突时无法生产预期调度的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3807" target="_blank">#3807</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3778" target="_blank">#3778</a></li> 
   <li>修复当调度器被删除后，可能会再度运行的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F2572" target="_blank">#2572</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>修复执行扫表任务时出现进程崩溃的潜在问题</li> 
   <li>修复处理 DAG 请求时出现 <code>duplicated region</code> 报错的问题</li> 
   <li>修复读负载高的情况下进程崩溃的问题</li> 
   <li>修复执行 <code>DateFormat</code> 函数时出现进程崩溃的潜在问题</li> 
   <li>修复执行 MPP 任务时出现内存泄漏的潜在问题</li> 
   <li>修复执行 <code>COUNT</code> 或 <code>COUNT DISTINCT</code> 函数时出现非预期结果的问题</li> 
   <li>修复多盘部署时出现数据无法恢复的潜在问题</li> 
   <li>修复 TiDB Dashboard 无法正确显示 TiFlash 磁盘信息的问题</li> 
   <li>修复析构 <code>SharedQueryBlockInputStream</code> 时出现进程崩溃的潜在问题</li> 
   <li>修复析构 <code>MPPTask</code> 时出现进程崩溃的潜在问题</li> 
   <li>修复通过快照同步数据后可能出现的数据不一致的问题</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>修复对 New Collation 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F2301" target="_blank">#2301</a></li> 
     <li>修复了运行时因非同步访问共享 map 可能导致 panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2300" target="_blank">#2300</a></li> 
     <li>修复了 DDL 语句执行时 owner 崩溃可能导致的 DDL event 遗漏的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2290" target="_blank">#2290</a></li> 
     <li>修复了试图过早在 TiDB 中解锁的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F2188" target="_blank">#2188</a></li> 
     <li>修复了表迁移后节点崩溃可能导致数据丢失的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2033" target="_blank">#2033</a></li> 
     <li>修复了 <code>changefeed update</code> 对 <code>--sort-dir</code> and <code>--start-ts</code> 的处理逻辑 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1921" target="_blank">#1921</a></li> 
    </ul> </li> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>修复了错误计算待恢复数据的大小的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1270" target="_blank">#1270</a></li> 
     <li>修复了从 cdclog 恢复数据时会遗漏 DDL event 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F870" target="_blank">#870</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>修复 TiDB Lightning 解析 Parquet 文件中 <code>DECIMAL</code> 类型数据失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1275" target="_blank">#1275</a></li> 
     <li>修复了计算 key 区间时出现整数型溢出的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1291" target="_blank">#1291</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1290" target="_blank">#1290</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Frelease-5.1.1" target="_blank">https://docs.pingcap.com/zh/tidb/stable/release-5.1.1</a></p>
                                        </div>
                                      
</div>
            