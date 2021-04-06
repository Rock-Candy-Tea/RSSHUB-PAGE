
---
title: 'TiDB 4.0.12 发布，分布式 NewSQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=45'
author: 开源中国
comments: false
date: Tue, 06 Apr 2021 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=45'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TiDB 4.0.12 现已发布，该版本具体更新内容如下：</p> 
<p><strong>新功能</strong></p> 
<ul> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>新增工具用于检测当前 <code>tiflash replica</code> 的状态</li> 
  </ul> </li> 
</ul> 
<p><strong>改进提升</strong></p> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>优化 <code>EXPLAIN</code> 语句在 <code>batch cop</code> 模式下的输出信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23164" target="_blank">#23164</a></li> 
   <li>在 <code>EXPLAIN</code> 语句的输出中，为无法下推到存储层的表达式增加告警信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23020" target="_blank">#23020</a></li> 
   <li>调整 DDL 包中部分 <code>Execute</code>/<code>ExecRestricted</code> 的使用为安全 API (2) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22935" target="_blank">#22935</a></li> 
   <li>调整 DDL 包中部分 <code>Execute</code>/<code>ExecRestricted</code> 的使用为安全 API (1) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22929" target="_blank">#22929</a></li> 
   <li>添加 <code>optimization-time</code> 和 <code>wait-TS-time</code> 到慢日志中 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22918" target="_blank">#22918</a></li> 
   <li>支持从 <code>infoschema.partitions</code> 表中查询 <code>partition_id</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22489" target="_blank">#22489</a></li> 
   <li>添加 <code>last_plan_from_binding</code> 以帮助用户了解 SQL 执行计划是否与 binding 的 hint 相匹配 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F21430" target="_blank">#21430</a></li> 
   <li>支持在没有 <code>pre-split</code> 选项时也能执行 <code>TRUNCATE</code> 表操作 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22872" target="_blank">#22872</a></li> 
   <li>为 <code>str_to_date</code> 表达式添加三种新的格式限定符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22812" target="_blank">#22812</a></li> 
   <li>在 metrics 监控中记录 <code>PREPARE</code> 执行失败的问题为 <code>Failed Query OPM</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22672" target="_blank">#22672</a></li> 
   <li>当设置了 <code>tidb_snapshot</code> 时，不对 <code>PREPARE</code> 语句的执行报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22641" target="_blank">#22641</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>消除短时间内大量重连接的现象 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9879" target="_blank">#9879</a></li> 
   <li>对多 Tombstones 场景下的写操作和 Batch Get 进行优化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9729" target="_blank">#9729</a></li> 
   <li>将 <code>leader-transfer-max-log-lag</code> 的默认值改为 <code>128</code>，以增加切换 leader 的成功率 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9605" target="_blank">#9605</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>只有当 <code>pending-peer</code> 或 <code>down-peer</code> 变更时才更新 Region Cache，减少心跳更新压力 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3471" target="_blank">#3471</a></li> 
   <li>防止 <code>split-cache</code> 中的 Region 成为合并的目标 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3459" target="_blank">#3459</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>优化配置文件并删除无用项</li> 
   <li>减小 TiFlash 二进制文件大小</li> 
   <li>使用自适应的 GC 策略以减少内存使用</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>若任务的暂停同步时间超过 1 天，再次启动该任务时需要二次确认 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1497" target="_blank">#1497</a></li> 
     <li>为 Old Value 功能添加监控面板 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1571" target="_blank">#1571</a></li> 
    </ul> </li> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>记录 <code>HTTP_PROXY</code> 和 <code>HTTPS_PROXY</code> 环境变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F827" target="_blank">#827</a></li> 
     <li>提升多表场景下的备份性能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F745" target="_blank">#745</a></li> 
     <li>在 service safe point 检查失败时报告错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F826" target="_blank">#826</a></li> 
     <li>在 <code>backupmeta</code> 中记录集群版本和 BR 版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F803" target="_blank">#803</a></li> 
     <li>遇到外部存储错误时，重试备份以便提高备份成功率 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F851" target="_blank">#851</a></li> 
     <li>减少 BR 备份的内存使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F886" target="_blank">#886</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>运行 TiDB Lightning 前检查 TiDB 集群版本以防止未知错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F787" target="_blank">#787</a></li> 
     <li>在遇到 cancel 错误时及时退出 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F867" target="_blank">#867</a></li> 
     <li>添加 <code>tikv-importer.engine-mem-cache-size</code> 和 <code>tikv-importer.local-writer-mem-cache-size</code> 参数以便调整内存占用和性能之间的平衡 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F866" target="_blank">#866</a></li> 
     <li>Local-backend 并发运行 <code>batch split region</code> 以提高导入速度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F868" target="_blank">#868</a></li> 
     <li>从 S3 存储导入数据时，TiDB Lightning 不再要求 <code>s3:ListBucket</code> 权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F919" target="_blank">#919</a></li> 
     <li>从 checkpoint 恢复时，TiDB Lightning 会继续使用之前的导入引擎 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F924" target="_blank">#924</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>修复当变量为十六进制字面量时，<code>get</code> 表达式出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23372" target="_blank">#23372</a></li> 
   <li>修复生成 <code>Enum</code> 和 <code>Set</code> 类型的快速执行计划时使用了错误 Collation 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23292" target="_blank">#23292</a></li> 
   <li>修复 <code>nullif</code> 和 <code>is-null</code> 表达式一起使用时可能出现结果错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23279" target="_blank">#23279</a></li> 
   <li>修复自动搜集统计信息在规定时间窗口外被触发的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23219" target="_blank">#23219</a></li> 
   <li>修复 <code>point-get</code> 计划中 <code>CAST</code> 函数可能忽略错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23211" target="_blank">#23211</a></li> 
   <li>修复 <code>CurrentDB</code> 为空时 SPM 可能不生效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23209" target="_blank">#23209</a></li> 
   <li>修复 IndexMerge 执行计划中可能出现错误过滤条件的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23165" target="_blank">#23165</a></li> 
   <li>修复 <code>NULL</code> 常量的返回类型中可能出现 <code>NotNullFlag</code> 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23135" target="_blank">#23135</a></li> 
   <li>修复 Text 类型可能遗漏处理 Collation 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23092" target="_blank">#23092</a></li> 
   <li>修复 Range 分区表处理 <code>IN</code> 表达式可能出错的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23074" target="_blank">#23074</a></li> 
   <li>修复将 TiKV 标记为 Tombstone 后，在相同地址和端口启动不同 StoreID 的新 TiKV 会持续返回 <code>StoreNotMatch</code> 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23071" target="_blank">#23071</a></li> 
   <li>INT 类型为 <code>NULL</code> 且和 <code>YEAR</code> 进行比较时不进行类型调整 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22844" target="_blank">#22844</a></li> 
   <li>修复当表含有 <code>auto_random</code> 列 load data 时失去连接的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F22736" target="_blank">#22736</a></li> 
   <li>修复取消 DDL 操作 panic 时可能阻塞其他 DDL 操作的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23297" target="_blank">#23297</a></li> 
   <li>修复进行 <code>NULL</code> 和 <code>YEAR</code> 比较时可能生成错误 key range 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23104" target="_blank">#23104</a></li> 
   <li>修复创建视图成功但是使用时可能失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23083" target="_blank">#23083</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>修复 <code>IN</code> 表达式没有正确处理有符号和无符号整型数的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9850" target="_blank">#9850</a></li> 
   <li>修复 Ingest 操作不可重入问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9779" target="_blank">#9779</a></li> 
   <li>修复 TiKV 在处理 JSON 向字符串转换时空格缺失的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9666" target="_blank">#9666</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>修复在 store 缺失 label 的情况下隔离级别错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3474" target="_blank">#3474</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>修复当 <code>binary</code> 列的默认值前后包含 <code>0</code> 字节时查询结果错误的问题</li> 
   <li>修复当数据库名称中包含特殊字符时无法同步数据的问题</li> 
   <li>修复 <code>IN</code> 表达式中出现 <code>Decimal</code> 列时查询结果错误的问题</li> 
   <li>修复 Grafana 中已打开文件数指标过高的问题</li> 
   <li>修复当表达式中包含 <code>Timestamp</code> 类型时查询结果错误的问题</li> 
   <li>修复处理 <code>FROM_UNIXTIME</code> 表达式时可能发生的无响应的问题</li> 
   <li>修复字符串转换为整数结果不正确的问题</li> 
   <li>修复 <code>like</code> 表达式可能返回错误结果的问题</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>修复 <code>resolved ts</code> 时间乱序的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1464" target="_blank">#1464</a></li> 
     <li>修复终止 processor 时不能及时释放资源的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1547" target="_blank">#1547</a></li> 
     <li>修复因事务计数器未正确更新而导致下游数据库链接可能泄露的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1524" target="_blank">#1524</a></li> 
     <li>修复因 PD 抖动时多个 owner 共存可能导致数据表丢失的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1540" target="_blank">#1540</a></li> 
     <li>修复由于网络不稳定而导致的表调度出错引发的数据丢失问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1508" target="_blank">#1508</a></li> 
    </ul> </li> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>修复 <code>WalkDir</code> 在目标为 bucket name 的时候无返回值的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F733" target="_blank">#733</a></li> 
     <li>修复 <code>status</code> 端口无 TLS 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F839" target="_blank">#839</a></li> 
    </ul> </li> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>修复 TiKV Importer 可能忽略文件已存在的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F848" target="_blank">#848</a></li> 
     <li>修复 TiDB Lightning 可能使用错误的时间戳而读到错误数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F850" target="_blank">#850</a></li> 
     <li>修复 TiDB Lightning 非预期退出时可能造成 checkpoint 文件损坏的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F889" target="_blank">#889</a></li> 
     <li>修复由于忽略 <code>cancel</code> 错误而可能导致的数据错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F874" target="_blank">#874</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>更新说明： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Frelease-4.0.12" target="_blank">https://docs.pingcap.com/zh/tidb/stable/release-4.0.12</a></p>
                                        </div>
                                      
</div>
            