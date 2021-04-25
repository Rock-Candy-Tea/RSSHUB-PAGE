
---
title: 'TiDB 5.0.1 发布，分布式 NewSQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3281'
author: 开源中国
comments: false
date: Sun, 25 Apr 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3281'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TiDB 5.0.1 现已发布，该版本具体更新内容如下：</p> 
<p><strong>改进提升</strong></p> 
<ul> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>使用 <code>zstd</code> 压缩 Region Snapshot <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10005" target="_blank">#10005</a></li> 
  </ul> </li> 
 <li> <p>PD</p> 
  <ul> 
   <li>调整 Region 分数公式使其更适用于异构集群 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F3605" target="_blank">#3605</a></li> 
   <li>避免在添加 <code>scatter region</code> 调度器后出现的非预期统计行为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fpd%2Fpull%2F3602" target="_blank">#3602</a></li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>删除 Summary 日志中一些容易被误解的信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1009" target="_blank">#1009</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li> <p>TiDB</p> 
  <ul> 
   <li>修复投影消除在投影结果为空时执行结果可能错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24093" target="_blank">#24093</a></li> 
   <li>修复列包含 <code>NULL</code> 值时查询结果在某些情况下可能错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24063" target="_blank">#24063</a></li> 
   <li>当有虚拟列参与扫描时不允许生成 MPP 计划 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24058" target="_blank">#24058</a></li> 
   <li>修复 Plan Cache 中对 <code>PointGet</code> 和 <code>TableDual</code> 错误的重复使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24043" target="_blank">#24043</a></li> 
   <li>修复优化器在为聚簇索引构建 <code>IndexMerge</code> 执行计划时出现的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24042" target="_blank">#24042</a></li> 
   <li>修复 BIT 类型相关错误的类型推导 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24027" target="_blank">#24027</a></li> 
   <li>修复某些优化器 Hint 在 <code>PointGet</code> 算子存在时无法生效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23685" target="_blank">#23685</a></li> 
   <li>修复 DDL 遇到错误回滚时可能失败的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24080" target="_blank">#24080</a></li> 
   <li>修复二进制字面值常量的索引范围构造错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24041" target="_blank">#24041</a></li> 
   <li>修复某些情况下 <code>IN</code> 语句的执行结果可能错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24023" target="_blank">#24023</a></li> 
   <li>修复某些字符串函数的返回结果错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23879" target="_blank">#23879</a></li> 
   <li>执行 <code>REPLACE</code> 语句需要用户同时拥有 <code>INSERT</code> 和 <code>DELETE</code> 权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23939" target="_blank">#23939</a></li> 
   <li>修复点查时出现的的性能回退 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F24070" target="_blank">#24070</a></li> 
   <li>修复因错误比较二进制与字节而导致的 <code>TableDual</code> 计划错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Ftidb%2Fpull%2F23918" target="_blank">#23918</a></li> 
  </ul> </li> 
 <li> <p>TiKV</p> 
  <ul> 
   <li>修复了 Coprocessor 未正确处理 <code>IN</code> 表达式有符号整数或无符号整数类型数据的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10018" target="_blank">#10018</a></li> 
   <li>修复了在批量 ingest SST 文件后产生大量空 Region 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F10015" target="_blank">#10015</a></li> 
   <li>修复了在 <code>cast_string_as_time</code> 中输入非法的 UTF-8 字节后导致崩溃的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9995" target="_blank">#9995</a></li> 
   <li>修复了 file dictionary 文件损坏之后 TiKV 无法启动的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftikv%2Ftikv%2Fpull%2F9992" target="_blank">#9992</a></li> 
  </ul> </li> 
 <li> <p>TiFlash</p> 
  <ul> 
   <li>修复存储引擎无法删除某些范围数据的问题</li> 
   <li>修复 <code>TIME</code> 类型转换为 <code>INT</code> 类型时产生错误结果的问题</li> 
   <li>修复 <code>receiver</code> 可能无法在 10 秒内找到对应任务的问题</li> 
   <li>修复 <code>cancelMPPQuery</code> 中可能存在无效迭代器的问题</li> 
   <li>修复 <code>bitwise</code> 算子和 TiDB 行为不一致的问题</li> 
   <li>修复当使用 <code>prefix key</code> 时出现范围重叠报错的问题</li> 
   <li>修复字符串转换为 <code>INT</code> 时产生错误结果的问题</li> 
   <li>修复连续快速写入可能导致 TiFlash 内存溢出的问题</li> 
   <li>修复列名重复会引发报错的问题</li> 
   <li>修复 MPP 执行计划无法被解析的问题</li> 
   <li>修复 Table GC 时会引发空指针的问题</li> 
   <li>修复向已被删除的表写数据时 TiFlash 进程崩溃的问题</li> 
   <li>修复当使用 BR 恢复数据时 TiFlash 进程可能崩溃的问题</li> 
  </ul> </li> 
 <li> <p>Tools</p> 
  <ul> 
   <li> <p>TiDB Lightning</p> 
    <ul> 
     <li>修复导入过程中进度日志中的表数量不准确的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1005" target="_blank">#1005</a></li> 
    </ul> </li> 
   <li> <p>Backup & Restore (BR)</p> 
    <ul> 
     <li>修复实际的备份速度超过 <code>--ratelimit</code> 限制的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1026" target="_blank">#1026</a></li> 
     <li>修复备份期间少数 TiKV 节点不可用导致的备份中断问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fbr%2Fpull%2F1019" target="_blank">#1019</a></li> 
    </ul> </li> 
   <li> <p>TiCDC</p> 
    <ul> 
     <li>修复 Unified Sorter 中的并发问题并过滤无用的错误消息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1678" target="_blank">#1678</a></li> 
     <li>修复同步到 MinIO 时，重复创建目录会导致同步中断的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1672" target="_blank">#1672</a></li> 
     <li>默认开启会话变量 <code>explicit_defaults_for_timestamp</code>，使得下游 MySQL 5.7 和上游 TiDB 的行为保持一致 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1659" target="_blank">#1659</a></li> 
     <li>修复错误地处理 <code>io.EOF</code> 可能导致同步中断的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1648" target="_blank">#1648</a></li> 
     <li>修正 TiCDC 面板中的 TiKV CDC endpoint CPU 统计信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1645" target="_blank">#1645</a></li> 
     <li>增加 <code>defaultBufferChanSize</code> 来避免某些情况下同步阻塞的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingcap%2Fticdc%2Fpull%2F1632" target="_blank">#1632</a></li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.pingcap.com%2Fzh%2Ftidb%2Fstable%2Frelease-5.0.1" target="_blank">https://docs.pingcap.com/zh/tidb/stable/release-5.0.1</a></p>
                                        </div>
                                      
</div>
            