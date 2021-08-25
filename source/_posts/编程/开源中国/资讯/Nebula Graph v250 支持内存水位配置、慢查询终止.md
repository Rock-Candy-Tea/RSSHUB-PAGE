
---
title: 'Nebula Graph v2.5.0 支持内存水位配置、慢查询终止'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7483'
author: 开源中国
comments: false
date: Wed, 25 Aug 2021 17:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7483'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Nebula Graph 年中版本 v2.5.0 在稳定性方面新增内存水位配置，支持慢查询终止、SUBGRAPH 返回不带属性图结构、全文索引重建等等新功能。</p> 
<h2 style="text-align:start">Feature</h2> 
<ul> 
 <li>支持 session 管理，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F280" target="_blank">#280</a></li> 
 <li>支持慢查询终止，已知问题：所有 query 的查询与终止都会有延迟，这与实现方案有关，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1152" target="_blank">#1152</a></li> 
 <li>LOOKUP 语句增强表达式解析索引的能力，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1188" target="_blank">#1188</a></li> 
 <li>支持配置机器内存水位，一定程度上缓解 OOM 问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1067" target="_blank">#1067</a></li> 
 <li>FIND PATH 支持边过滤，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1091" target="_blank">#1091</a></li> 
 <li>SUBGRAPH 支持只返回图结构，不包含属性，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1134" target="_blank">#1134</a></li> 
 <li>TIMESTAMP 函数支持无参数执行，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-common%2Fpull%2F515" target="_blank">#515</a></li> 
 <li>支持查询各个服务的版本，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F944" target="_blank">#944</a></li> 
 <li>支持 INDEX 和 TTL 同时使用，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F382" target="_blank">#382</a></li> 
 <li>支持在指定属性创建全文索引。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F460" target="_blank">#460</a></li> 
 <li>创建 space 及 schema 支持 comment，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F895" target="_blank">#895</a></li> 
 <li>支持全文索引重建，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1123" target="_blank">#1123 <span style="background-color:var(--primary-low); color:var(--primary-medium)">1</span></a></li> 
</ul> 
<h2 style="text-align:start">Bug Fix</h2> 
<ul> 
 <li>权限导致的多语句执行问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1165" target="_blank">#1165</a></li> 
 <li>修复 UNWIND 导致没有结果的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1018" target="_blank">#1018</a></li> 
 <li>修复聚合函数在某些场景下导致的 crash 问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1015" target="_blank">#1015</a></li> 
 <li>修复 OR 表达式在索引匹配中的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1005" target="_blank">#1005 <span style="background-color:var(--primary-low); color:var(--primary-medium)">2</span></a></li> 
 <li>修复函数的大小写敏感问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fissues%2F927" target="_blank">#927</a></li> 
 <li>修复查询索引创建信息时没有检查 tag/edge 类型的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F933" target="_blank">#933</a></li> 
 <li>修复 SUBSTRING 函数的 bug，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-common%2Fpull%2F491" target="_blank">#491</a></li> 
 <li>修复 meta 不能正确返回 leader change，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F423" target="_blank">#423</a></li> 
 <li>修复 LIMIT、ORDER、GROUP 语句使用变量的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F1314" target="_blank">#1314</a></li> 
 <li>修复 db_dump 工具打印 int 类型 VID 的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F533" target="_blank">#533</a></li> 
 <li>修复 BALANCE 任务恢复后仍显示 FAILE 的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F528" target="_blank">#528</a></li> 
</ul> 
<h2 style="text-align:start">Enhancement</h2> 
<ul> 
 <li>listener 接口优化，支持获取全量数据，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F465" target="_blank">#465</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F484" target="_blank">#484</a></li> 
 <li>meta 的 leader 表重新组织，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F439" target="_blank">#439</a></li> 
 <li>增加 DiskManager 用于检查磁盘剩余容量，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F461" target="_blank">#461</a></li> 
 <li>优化 raft 的 heartbeat 实现，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F438" target="_blank">#438</a></li> 
 <li>storage 支持并发执行 GO/FETCH/LOOKUP，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F503" target="_blank">#503</a></li> 
 <li>加强了 exists 函数对 map 的支持，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F973" target="_blank">#973</a></li> 
 <li>加强聚合函数的使用方式，比如 COUNT(v) + AVG(v)，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F968" target="_blank">#968</a></li> 
</ul> 
<h2 style="text-align:start">Change</h2> 
<ul> 
 <li>SUBGRAPH 语法变化</li> 
</ul> 
<pre style="text-align:start"><code># 增加<strong>WITH</strong> PROP关键字用于输出属性
<strong>GET</strong> SUBGRAPH <strong>WITH</strong> PROP <strong>FROM</strong> <vids>

# 原有语法将只输出图结构
<strong>GET</strong> SUBGRAPH <strong>FROM</strong> <vids>
</code></pre> 
<ul> 
 <li><code>ORDER BY</code> 用法变更</li> 
</ul> 
<pre style="text-align:start"><code># Before:
LOOKUP <strong>ON</strong> player \
    <strong>YIELD</strong> player.age <strong>As</strong> playerage \
    | <strong>GROUP</strong> <strong>BY</strong> $-.playerage \
     <strong>YIELD</strong> $-.playerage <strong>as</strong> age, count(*) <strong>AS</strong> number \
     | <strong>ORDER</strong> <strong>BY</strong> number DESC, age DESC;


# <strong>From</strong> v2.<span style="color:var(--hljs-number)">5.0</span>
LOOKUP <strong>ON</strong> player \
    <strong>YIELD</strong> player.age <strong>As</strong> playerage \
    | <strong>GROUP</strong> <strong>BY</strong> $-.playerage \
    <strong>YIELD</strong> $-.playerage <strong>as</strong> age, count(*) <strong>AS</strong> number \
    | <strong>ORDER</strong> <strong>BY</strong> $-.number DESC, $-.age DESC;
</code></pre> 
<p style="text-align:start">本次 v2.5.0 支持从 v1.x 和 v2.x 直接升级，具体升级步骤参考文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.nebula-graph.com.cn%2F2.5.0%2F4.deployment-and-installation%2F3.upgrade-nebula-graph%2Fupgrade-nebula-graph-to-250%2F" target="_blank">升级历史版本至v2.5.0 - Nebula Graph Database 手册 </a> 、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.nebula-graph.com.cn%2F2.5.0%2F4.deployment-and-installation%2F3.upgrade-nebula-graph%2Fupgrade-nebula-from-200-to-250%2F" target="_blank">升级v2.0.x至v2.5.0 - Nebula Graph Database 手册</a></p>
                                        </div>
                                      
</div>
            