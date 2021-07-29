
---
title: 'TiDB 4.0.14 发布，分布式 NewSQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1176'
author: 开源中国
comments: false
date: Thu, 29 Jul 2021 07:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1176'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TiDB 4.0.14 现已发布，该版本具体更新内容如下：</p> 
<h4>兼容性更改</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>在 v4.0 中将 <code>tidb_multi_statement_mode</code> 的默认值从 <code>WARN</code> 更改为 <code>OFF</code>。建议使用客户端库的多语句功能，参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Fsystem-variables%23tidb_multi_statement_mode-%25E4%25BB%258E-v4011-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B%25E5%25BC%2595%25E5%2585%25A5" target="_blank"><code>tidb_multi_statement_mode</code> 文档</a>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25749" target="_blank">#25749</a></li> 
   <li>将 Grafana 从 v6.1.16 升级到 v7.5.7 以解决两个安全漏洞，参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fblog%2F2020%2F06%2F03%2Fgrafana-6.7.4-and-7.0.2-released-with-important-security-fix%2F" target="_blank">Grafana 博文</a>。</li> 
   <li>将系统变量 <code>tidb_stmt_summary_max_stmt_count</code> 的默认值从 <code>200</code> 修改为 <code>3000</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25872" target="_blank">#25872</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>将 <code>merge-check-tick-interval</code> 配置项的默认值从 <code>10</code> 修改为 <code>2</code> 以加快 Region 合并的速度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9676" target="_blank">#9676</a></li> 
  </ul> </li> 
</ul> 
<h4>功能增强</h4> 
<ul> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>添加监控项 <code>pending</code> 用以监控 pending PD 心跳，帮助定位 PD 线程变慢的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10008" target="_blank">#10008</a></li> 
   <li>支持 virtual-host 风格的地址来让 BR 兼容类 S3 储存 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10242" target="_blank">#10242</a></li> 
  </ul> </li> 
 <li> <p>TiDB Dashboard</p> 
  <ul> 
   <li>新增 OIDC SSO 支持。通过设置兼容 OIDC 标准的 SSO 服务（例如 Okta、Auth0 等），用户可以在不输入 SQL 密码的情况下登录 TiDB Dashboard <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb-dashboard%2Fpull%2F960" target="_blank">#960</a></li> 
   <li>新增 <strong>Debug API</strong> 界面用于高级调试，通过该界面可以替代命令行方式来调用 TiDB 和 PD 的内部调试性 API <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb-dashboard%2Fpull%2F927" target="_blank">#927</a></li> 
  </ul> </li> 
</ul> 
<h4>改进提升</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>对于 <code>point get</code> 或 <code>batch point get</code> 算子，在唯一索引写入过程中，将悲观锁 <code>LOCK</code> 记录转化为 <code>PUT</code> 记录 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26223" target="_blank">#26223</a></li> 
   <li>支持 MySQL 的系统变量 <code>init_connect</code> 及其相关功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26031" target="_blank">#26031</a></li> 
   <li>支持稳定结果模式，使查询结果更稳定 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26003" target="_blank">#26003</a></li> 
   <li>支持将函数 <code>json_unquote()</code> 下推到 TiKV <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F25721" target="_blank">#25721</a></li> 
   <li>使 SQL 计划管理 (SPM) 不受字符集的影响 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23295" target="_blank">#23295</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>关闭 TiKV 时，优先关闭 status server 来确保客户端可以正确检测关闭状态 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10504" target="_blank">#10504</a></li> 
   <li>响应过期副本的消息，以确保过期副本被更快清除 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10400" target="_blank">#10400</a></li> 
   <li>限制 TiCDC sink 的内存消耗 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10147" target="_blank">#10147</a></li> 
   <li>当 Region 太大时，使用均匀分裂来加快分裂速度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10275" target="_blank">#10275</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>减少各调度器在同时工作时产生的冲突 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fpull%2F3854" target="_blank">#3854</a></li> 
  </ul> </li> 
 <li> <p>TiDB Dashboard</p> 
  <ul> 
   <li>更新 TiDB Dashboard 版本至 v2021.07.17.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3882" target="_blank">#3882</a></li> 
   <li>支持将当前会话分享为只读的会话，禁止对分享的会话进行修改操作 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb-dashboard%2Fpull%2F960" target="_blank">#960</a></li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>恢复数据时合并小文件以提升恢复速度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F655" target="_blank">#655</a></li> 
    </ul> </li> 
   <li> <p>Dumpling</p> 
    <ul> 
     <li>上游是 TiDB v3.x 集群时，使用 <code>_tidb_rowid</code> 来切分表以减少 TiDB 的内存使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fdumpling%2Fpull%2F306" target="_blank">#306</a></li> 
    </ul> </li> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>优化 PD 节点缺失证书时的报错信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2184" target="_blank">#2184</a></li> 
     <li>优化 sorter I/O 报错信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1976" target="_blank">#1976</a></li> 
     <li>在 KV client 中新增 Region 增量扫描的并发度上限，减小 TiKV 的压力 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1926" target="_blank">#1926</a></li> 
     <li>新增表内存使用量的监控项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1884" target="_blank">#1884</a></li> 
     <li>新增 TiCDC 服务端配置项 <code>capture-session-ttl</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2169" target="_blank">#2169</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h4>Bug 修复</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>修复当连接一个带 <code>WHERE</code> 条件的子查询（值为 <code>false</code>）时 <code>SELECT</code> 的结果与 MySQL 不兼容的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24865" target="_blank">#24865</a></li> 
   <li>修复当参数是 <code>ENUM</code> 或 <code>SET</code> 类型时 <code>ifnull</code> 函数计算错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24944" target="_blank">#24944</a></li> 
   <li>修复某些情况下错误的聚合函数消除 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25202" target="_blank">#25202</a></li> 
   <li>修复 Merge Join 运算中当列为 <code>SET</code> 类型时可能产生错误结果的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25669" target="_blank">#25669</a></li> 
   <li>修复 Cartesian Join 运算返回错误结果的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25591" target="_blank">#25591</a></li> 
   <li>修复 <code>SELECT ... FOR UPDATE</code> 语句进行连接运算且连接使用分区表时，可能产生异常退出情况的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F20028" target="_blank">#20028</a></li> 
   <li>修复缓存的 <code>prepared</code> 计划被错误用于 <code>point get</code> 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24741" target="_blank">#24741</a></li> 
   <li>修复 <code>LOAD DATA</code> 语句可以不正常导入非 utf8 数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25979" target="_blank">#25979</a></li> 
   <li>修复通过 HTTP API 访问统计信息时，可能导致内存泄露的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24650" target="_blank">#24650</a></li> 
   <li>修复执行 <code>ALTER USER</code> 语句时出现的安全性问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25225" target="_blank">#25225</a></li> 
   <li>修复系统表 <code>TIKV_REGION_PEERS</code> 不能正确处理 <code>DOWN</code> 状态的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F24879" target="_blank">#24879</a></li> 
   <li>修复解析 <code>DateTime</code> 时不截断非法字符串的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F22231" target="_blank">#22231</a></li> 
   <li>修复 <code>select into outfile</code> 语句在列类型是 <code>YEAR</code> 时，可能无法产生结果的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F22159" target="_blank">#22159</a></li> 
   <li>修复 <code>UNION</code> 子查询中出现 <code>NULL</code> 时可能导致查询结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F26532" target="_blank">#26532</a></li> 
   <li>修复某些情况下投影算子在执行时可能造成 panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F26534" target="_blank">#26534</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>修复特定平台上的 duration 计算可能崩溃的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fissues%2F86470%23issuecomment-877557654" target="_blank">#related-issue</a></li> 
   <li>修复将 <code>DOUBLE</code> 类型转换为 <code>DOUBLE</code> 的错误函数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25200" target="_blank">#25200</a></li> 
   <li>修复使用 async logger 时 panic 日志可能会丢失的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F8998" target="_blank">#8998</a></li> 
   <li>修复开启加密后再次生成同样的 snapshot 会出现 panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F9786" target="_blank">#9786</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10407" target="_blank">#10407</a></li> 
   <li>修复 coprocessor 中 <code>json_unquote()</code> 函数错误的参数类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10176" target="_blank">#10176</a></li> 
   <li>修复关机期间出现的可疑警告和来自 Raftstore 的非确定性响应 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10353" target="_blank">#10353</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10307" target="_blank">#10307</a></li> 
   <li>修复备份线程泄漏的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10287" target="_blank">#10287</a></li> 
   <li>修复 Region split 过慢以及进行 Region merge 时，Region split 可能会损坏 metadata 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F8456" target="_blank">#8456</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F8783" target="_blank">#8783</a></li> 
   <li>修复特定情况下 Region 心跳会导致 TiKV 不进行 split 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F10111" target="_blank">#10111</a></li> 
   <li>修复 TiKV 和 TiDB 间 CM Sketch 格式不一致导致统计信息错误问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fissues%2F25638" target="_blank">#25638</a></li> 
   <li>修复 <code>apply wait duration</code> 指标的错误统计 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fissues%2F9893" target="_blank">#9893</a></li> 
   <li>修复使用 Titan 时 <code>delete_files_in_range</code> 以后可能会产生 "Missing Blob" 报错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10232" target="_blank">#10232</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>修复调度器在执行删除操作后可能再次出现的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F2572" target="_blank">#2572</a></li> 
   <li>修复调度器在临时配置加载完毕前启动可能导致数据争用的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3771" target="_blank">#3771</a></li> 
   <li>修复打散 Region 操作可能导致 PD panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3761" target="_blank">#3761</a></li> 
   <li>修复部分 Operator 未被正确设置优先级的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3703" target="_blank">#3703</a></li> 
   <li>修复从不存在的 Store 上删除 <code>evict-leader</code> 调度器时可能导致 PD panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3660" target="_blank">#3660</a></li> 
   <li>修复了当集群内 Store 非常多时，PD 切换 Leader 慢的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Fpd%2Fissues%2F3697" target="_blank">#3697</a></li> 
  </ul> </li> 
 <li> <p>TiDB Dashboard</p> 
  <ul> 
   <li>修复实例性能分析界面无法获取全部 TiDB 实例信息的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb-dashboard%2Fpull%2F944" target="_blank">#944</a></li> 
   <li>修复 SQL 语句分析界面不显示执行“计划数”的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb-dashboard%2Fpull%2F939" target="_blank">#939</a></li> 
   <li>修复在升级集群后慢查询界面可能显示 "unknown field" 错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb-dashboard%2Fissues%2F902" target="_blank">#902</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>修复编译 DAG 请求时出现进程崩溃的潜在问题</li> 
   <li>修复读负载高的情况下进程崩溃的问题</li> 
   <li>修复因列存中 split 失败导致 TiFlash 不断重启的问题</li> 
   <li>修复无法删除 Delta 历史数据的潜在问题</li> 
   <li>修复并发复制共享 Delta 索引导致结果错误的问题</li> 
   <li>修复当数据缺失时 TiFlash 无法重启的问题</li> 
   <li>修复旧的 dm 文件无法被自动清理的问题</li> 
   <li>修复 <code>SUBSTRING</code> 函数包含特殊参数时引起进程崩溃的潜在问题</li> 
   <li>修复将 <code>INT</code> 类型转换为 <code>TIME</code> 类型时产生错误结果的问题</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>修复不能恢复 <code>mysql</code> 库内的用户表的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1142" target="_blank">#1142</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>修复 TiDB Lightning 解析 Parquet 文件中 <code>DECIMAL</code> 类型数据失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1276" target="_blank">#1276</a></li> 
     <li>修复 TiDB Lightning 导入大文件拆分时遇到的 EOF 报错问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F1133" target="_blank">#1133</a></li> 
     <li>修复 TiDB Lightning 导入含 <code>auto_increment</code> 的 <code>DOUBLE</code> 或 <code>FLOAT</code> 类型列的表时生成极大 base 值的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1185" target="_blank">#1185</a></li> 
     <li>修复在生成超过 4 GB 的 KV 数据时可能发生的 panic 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1128" target="_blank">#1128</a></li> 
    </ul> </li> 
   <li> <p>Dumpling</p> 
    <ul> 
     <li>使用 Dumpling 导出至 S3 存储时，不再要求 <code>s3:ListBucket</code> 权限覆盖整个 Bucket，只需要覆盖导出的前缀即可 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fissues%2F898" target="_blank">#898</a></li> 
    </ul> </li> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>修复分区表新增分区后的处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2205" target="_blank">#2205</a></li> 
     <li>修复 TiCDC 无法读取 <code>/proc/meminfo</code> 导致崩溃的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2023" target="_blank">#2023</a></li> 
     <li>减少 TiCDC 运行时的内存使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F2011" target="_blank">#2011</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1957" target="_blank">#1957</a></li> 
     <li>修复 MySQL sink 遇到错误或暂停时，MySQL 连接会泄漏的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1945" target="_blank">#1945</a></li> 
     <li>修复当 start TS 小于 current TS 减去 GC TTL 时无法创建 TiCDC changefeed 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1839" target="_blank">#1839</a></li> 
     <li>减少 sort heap 的内存 <code>malloc</code>，以降低 CPU 开销 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fissues%2F1853" target="_blank">#1853</a></li> 
     <li>修复调度数据表时可能发生的同步终止问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1827" target="_blank">#1827</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Frelease-4.0.14" target="_blank">https://docs.pingcap.com/zh/tidb/stable/release-4.0.14</a> </p>
                                        </div>
                                      
</div>
            