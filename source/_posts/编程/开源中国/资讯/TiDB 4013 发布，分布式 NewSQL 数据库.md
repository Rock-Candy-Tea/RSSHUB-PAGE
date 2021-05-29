
---
title: 'TiDB 4.0.13 发布，分布式 NewSQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4674'
author: 开源中国
comments: false
date: Sat, 29 May 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4674'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TiDB 4.0.13 现已发布，该版本具体更新内容如下：</p> 
<h4>新功能</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>支持将列属性 <code>AUTO_INCREMENT</code> 变更为 <code>AUTO_RANDOM</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24608" target="_blank">#24608</a></li> 
   <li>引入 <code>infoschema.client_errors_summary</code> 表，用以追踪返回给客户端的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23267" target="_blank">#23267</a></li> 
  </ul> </li> 
</ul> 
<h4>提升改进</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>当内存中的统计信息缓存是最新的时，避免后台作业频繁读取 <code>mysql.stats_histograms</code> 表造成高 CPU 使用率 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24352" target="_blank">#24352</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>提高 <code>store used size</code> 计算过程的准确性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9904" target="_blank">9904</a></li> 
   <li>在 <code>EpochNotMatch</code> 消息中返回更多的 Region 以降低 Region miss 的发生 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9731" target="_blank">9731</a></li> 
   <li>加快释放长期运行集群中堆积的内存 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10035" target="_blank">10035</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>优化 TSO 处理时间的统计指标，帮助用户判断 PD 侧的 TSO 处理时间是否过长 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3524" target="_blank">#3524</a></li> 
   <li>更新 Dashboard 的版本至 v2021.03.12.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3469" target="_blank">#3469</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>自动清除过期历史数据以释放磁盘空间</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>支持备份恢复系统库 <code>mysql</code> 下的用户表 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1077" target="_blank">#1077</a></li> 
     <li>更新 <code>checkVersion</code> 以检查集群版本和备份数据版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1090" target="_blank">#1090</a></li> 
     <li>容忍在备份期间集群中出现少数 TiKV 节点宕机 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1062" target="_blank">#1062</a></li> 
    </ul> </li> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>为内部处理单元增加流程控制，避免出现内存溢出问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1751" target="_blank">#1751</a></li> 
     <li>增加 Unified Sorter 清理陈旧临时文件的功能，禁止多个 <code>cdc</code> 服务共享 <code>sort-dir</code> 目录 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1741" target="_blank">#1741</a></li> 
     <li>给 Failpoint 增加 HTTP 接口调用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1732" target="_blank">#1732</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h4>Bug 修复</h4> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>修复带有子查询的 <code>UPDATE</code> 语句更新生成列时会 panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24658" target="_blank">#24658</a></li> 
   <li>修复使用多列索引读取数据时返回结果重复的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24634" target="_blank">#24634</a></li> 
   <li>修复在 DIV 表达式中使用 <code>BIT</code> 类型常量作为除数造成查询结果错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24266" target="_blank">#24266</a></li> 
   <li>修复 <code>NO_ZERO_IN_DATE</code> SQL 模式对 DDL 语句中设置的列默认值无效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24185" target="_blank">#24185</a></li> 
   <li>修复 <code>BIT</code> 类型列与整型列进行 <code>UNION</code> 并集运算时，查询结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24026" target="_blank">#24026</a></li> 
   <li>修复 <code>BINARY</code> 类型与 <code>CHAR</code> 类型比较时，错误地生成了 <code>TableDual</code> 执行计划的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23917" target="_blank">#23917</a></li> 
   <li>修复 <code>insert ignore on duplicate</code> 非预期的删除表记录的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23825" target="_blank">#23825</a></li> 
   <li>修复 Audit 插件导致 TiDB panic 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23819" target="_blank">#23819</a></li> 
   <li>修复 <code>HashJoin</code> 算子未正确处理排序规则的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23812" target="_blank">#23812</a></li> 
   <li>修复悲观事务中，<code>batch_point_get</code> 处理异常值出错导致连接断开的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23778" target="_blank">#23778</a></li> 
   <li>修复 <code>tidb_row_format_version</code> 配置项的值被设置为 <code>1</code>，且 <code>enable_new_collation</code> 的值被设置为 <code>true</code> 时，数据索引不一致的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23772" target="_blank">#23772</a></li> 
   <li>修复整型列与字符串类型常量比较时，查询结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23705" target="_blank">#23705</a></li> 
   <li>修复 <code>approx_percent</code> 函数中传入 <code>BIT</code> 类型列时出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23702" target="_blank">#23702</a></li> 
   <li>修复执行 TiFlash 批量请求时，TiDB 误报 <code>TiKV server timeout</code> 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23700" target="_blank">#23700</a></li> 
   <li>修复 <code>IndexJoin</code> 在前缀列索引上计算结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23691" target="_blank">#23691</a></li> 
   <li>修复由于 <code>BINARY</code> 类型列上排序规则处理不当导致查询结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23598" target="_blank">#23598</a></li> 
   <li>修复当 <code>UPDATE</code> 语句中存在含 <code>HAVING</code> 子句的连接查询时，执行崩溃的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23575" target="_blank">#23575</a></li> 
   <li>修复比较类型表达式中使用 <code>NULL</code> 常量导致 TiFlash 计算结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23474" target="_blank">#23474</a></li> 
   <li>修复 <code>YEAR</code> 类型列与字符类型常量比较结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23335" target="_blank">#23335</a></li> 
   <li>修复 <code>session.group_concat_max_len</code> 被设置得过小时，<code>group_concat</code> 执行崩溃的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23257" target="_blank">#23257</a></li> 
   <li>修复 <code>TIME</code> 类型列上使用 <code>BETWEEN</code> 表达式计算结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23233" target="_blank">#23233</a></li> 
   <li>修复 <code>DELETE</code> 语句中出现的权限检查问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23215" target="_blank">#23215</a></li> 
   <li>修复往 <code>DECIMAL</code> 列中插入非法字符串时不报错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23196" target="_blank">#23196</a></li> 
   <li>修复往 <code>DECIMAL</code> 类型列插入数据时解析出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23152" target="_blank">#23152</a></li> 
   <li>修复 <code>USE_INDEX_MERGE</code> hint 无法生效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22924" target="_blank">#22924</a></li> 
   <li>修复使用 <code>ENUM</code> 或 <code>SET</code> 类型列作为 <code>WHERE</code> 过滤条件时，查询结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22814" target="_blank">#22814</a></li> 
   <li>修复 Clustered Index 与 New Collation 同时使用时，查询结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F21408" target="_blank">#21408</a></li> 
   <li>修复 <code>enable_new_collation</code> 开启时，<code>ANALYZE</code> 出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F21299" target="_blank">#21299</a></li> 
   <li>修复视图处理默认 ROLE 时，未正确处理相关 DEFINER 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24531" target="_blank">#24531</a></li> 
   <li>修复取消 DDL Job 时卡住的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24445" target="_blank">#24445</a></li> 
   <li>修复 <code>concat</code> 函数错误处理排序规则的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24300" target="_blank">#24300</a></li> 
   <li>修复当 <code>SELECT</code> 域中包含 <code>IN</code> 子查询且子查询外侧表含有空值元组时，查询结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24022" target="_blank">#24022</a></li> 
   <li>修复逆序扫表时，TiFlash 被优化器错误选用的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23974" target="_blank">#23974</a></li> 
   <li>修复点查的返回结果中，列名与 MySQL 不一致的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23970" target="_blank">#23970</a></li> 
   <li>修复在数据库名含有大写字母的库中执行 <code>show table status</code> 结果为空的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23958" target="_blank">#23958</a></li> 
   <li>修复不同时拥有 <code>INSERT</code> 及 <code>DELETE</code> 权限的用户可以执行 <code>REPLACE</code> 操作的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23938" target="_blank">#23938</a></li> 
   <li>修复由于未正确处理排序规则导致的 <code>concat</code>/<code>make_set</code>/<code>insert</code> 表达式计算结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23878" target="_blank">#23878</a></li> 
   <li>修复在含有 RANGE 分区的表上查询时，查询崩溃的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23689" target="_blank">#23689</a></li> 
   <li>修复如下问题：在旧版本的集群中，若 <code>tidb_enable_table_partition</code> 被设置为 <code>false</code>，含有分区的表会被当作普通表处理。此时由旧版本升级至新版本时，在该表上执行 <code>batch point get</code> 查询会导致连接崩溃 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23682" target="_blank">#23682</a></li> 
   <li>修复配置了 TiDB 监听 TCP 连接及 UNIX 套接字时，TCP 连接中远程主机未被正确验证的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23513" target="_blank">#23513</a></li> 
   <li>修复由于非默认的排序规则导致查询结果出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22923" target="_blank">#22923</a></li> 
   <li>修复 Grafana 的 <strong>Coprocessor Cache</strong> 面板不显示数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22617" target="_blank">#22617</a></li> 
   <li>修复优化器访问统计信息缓存时出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22565" target="_blank">#22565</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>修复因磁盘写满后 <code>file_dict</code> 写入不完全导致 TiKV 无法重启的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9963" target="_blank">9963</a></li> 
   <li>限制 TiCDC 默认的扫描速度为 128MB/s <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9983" target="_blank">9983</a></li> 
   <li>减少 TiCDC 进行初次扫描的内存使用量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10133" target="_blank">10133</a></li> 
   <li>为 TiCDC 扫描的速度添加背压 (back pressure) 功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10142" target="_blank">10142</a></li> 
   <li>通过避免不必要的读取来获取 TiCDC 旧值以解决潜在的 OOM 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10031" target="_blank">10031</a></li> 
   <li>修复了由于读取旧值而导致的 TiCDC OOM 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10197" target="_blank">10197</a></li> 
   <li>为 S3 存储添加超时机制以避免 S3 客户端没有任何响应地挂起 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10132" target="_blank">10132</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>修复未向 Prometheus 报告 <code>delta-merge-tasks</code> 数量的问题</li> 
   <li>修复 <code>Segment Split</code> 期间发生进程崩溃的问题</li> 
   <li>修复 Grafana 中 <code>Region write Duration</code> 面板位置错误的问题</li> 
   <li>修复了存储引擎无法删除数据的潜在问题</li> 
   <li>修复 <code>TIME</code> 类型转换为 <code>INT</code> 类型时产生错误结果的问题</li> 
   <li>修复 <code>bitwise</code> 算子和 TiDB 行为不一致的问题</li> 
   <li>修复字符串转换为 <code>INT</code> 时产生错误结果的问题</li> 
   <li>修复连续快速写入可能导致 TiFlash 内存溢出的问题</li> 
   <li>修复 Table GC 时会引发空指针的问题</li> 
   <li>修复向已被删除的表写数据时 TiFlash 进程崩溃的问题</li> 
   <li>修复当使用 BR 恢复数据时 TiFlash 进程可能崩溃的问题</li> 
   <li>修复当使用通用 CI 排序规则时字符权重错误的问题</li> 
   <li>修复被逻辑删除的表可能丢失数据的问题</li> 
   <li>修复比较包含空字符的字符串时产生错误结果的问题</li> 
   <li>修复输入列包含空常量时逻辑函数返回错误结果的问题</li> 
   <li>修复逻辑函数仅接受数字类型输入的问题</li> 
   <li>修复时间戳值为 <code>1970-01-01</code> 且时区偏移为负时计算结果不正确的问题</li> 
   <li>修复 <code>Decimal256</code> 的哈希值计算结果不稳定的问题</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>修复当 Sorter 的输入通道卡住时，流控导致的死锁问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1779" target="_blank">1779</a></li> 
     <li>修复 TiCDC changefeed 断点卡住导致 TiKV GC safe point 不推进的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1756" target="_blank">#1756</a></li> 
     <li>回滚 <code>explicit_defaults_for_timestamp</code> 的改动，确保不用 <code>SUPER</code> 权限也可以同步数据到 MySQL <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1749" target="_blank">#1749</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>修复在 autocommit 关闭的情况下，TiDB Lightning TiDB-backend 无法导入数据的问题</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Frelease-4.0.13" target="_blank">https://docs.pingcap.com/zh/tidb/stable/release-4.0.13</a> </p>
                                        </div>
                                      
</div>
            