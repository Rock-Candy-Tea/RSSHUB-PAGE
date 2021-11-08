
---
title: 'Nebula Graph v2.6 Release Note，新增 TOSS、ZONE 等多样特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9469'
author: 开源中国
comments: false
date: Mon, 08 Nov 2021 11:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9469'
---

<div>   
<div class="content">
                                                                                            <p>本版本新增 TOSS、ZONE、Geo Spatial、传输加密、返回 JSON 格式等功能，并优化了部分下推的计算、YIELD 语句格式、内存水位检测等功能。</p> 
<h3>特性</h3> 
<ul> 
 <li>新增 TOSS 功能，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2525" target="_blank">https://github.com/vesoft-inc/nebula/pull/2525</a></li> 
 <li>新增 ZONE 功能，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fissues%2F2604" target="_blank">https://github.com/vesoft-inc/nebula/issues/2604</a></li> 
 <li>支持 Geo Spatial 功能，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2954" target="_blank">https://github.com/vesoft-inc/nebula/pull/2954</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2979" target="_blank">https://github.com/vesoft-inc/nebula/pull/2979</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3043" target="_blank">https://github.com/vesoft-inc/nebula/pull/3043</a></li> 
 <li>支持传输加密，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2584" target="_blank">https://github.com/vesoft-inc/nebula/pull/2584</a></li> 
 <li>支持服务端返回 JSON 格式的查询结果，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2824" target="_blank">https://github.com/vesoft-inc/nebula/pull/2824</a></li> 
 <li>支持 SPACE 的 meta 克隆，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2763" target="_blank">https://github.com/vesoft-inc/nebula/pull/2763</a></li> 
 <li>支持 LOOKUP 中使用 IN 表达式，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2906" target="_blank">https://github.com/vesoft-inc/nebula/pull/2906</a></li> 
 <li>集成 Breakpad，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2536" target="_blank">https://github.com/vesoft-inc/nebula/pull/2536</a></li> 
 <li>支持将 metad 的本地文件夹复制到远程，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2532" target="_blank">https://github.com/vesoft-inc/nebula/pull/2532</a></li> 
 <li>支持 <code>DELETE TAG</code>，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2520" target="_blank">https://github.com/vesoft-inc/nebula/pull/2520</a></li> 
 <li>支持 concat 函数，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2540" target="_blank">https://github.com/vesoft-inc/nebula/pull/2540</a></li> 
 <li>支持<code>SHOW META LEADER</code>，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2542" target="_blank">https://github.com/vesoft-inc/nebula/pull/2542</a></li> 
</ul> 
<h3>优化</h3> 
<ul> 
 <li>优化 indexscan 的 LIMIT 下推的计算，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2905" target="_blank">https://github.com/vesoft-inc/nebula/pull/2905</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2823" target="_blank">https://github.com/vesoft-inc/nebula/pull/2823</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2796" target="_blank">https://github.com/vesoft-inc/nebula/pull/2796</a></li> 
 <li>优化 GO 语句每步采样和 LIMIT 下推的计算，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2904" target="_blank">https://github.com/vesoft-inc/nebula/pull/2904</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2853" target="_blank">https://github.com/vesoft-inc/nebula/pull/2853</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2831" target="_blank">https://github.com/vesoft-inc/nebula/pull/2831</a></li> 
 <li>优化 YIELD 语句的格式，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2555" target="_blank">https://github.com/vesoft-inc/nebula/pull/2555</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2572" target="_blank">https://github.com/vesoft-inc/nebula/pull/2572</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2779" target="_blank">https://github.com/vesoft-inc/nebula/pull/2779</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2779" target="_blank">https://github.com/vesoft-inc/nebula/pull/2895</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2944" target="_blank">https://github.com/vesoft-inc/nebula/pull/2944</a></li> 
 <li>启用 prefix bloom filter 以提升性能，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2860" target="_blank">https://github.com/vesoft-inc/nebula/pull/2860</a></li> 
 <li>支持服务端验证客户端版本，使用可配套的客户端版本才允许连接（客户端版本从 v2.6.0 开始），pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2965" target="_blank">https://github.com/vesoft-inc/nebula/pull/2965</a></li> 
 <li>优化拉动整个分片时的流量控制，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2557" target="_blank">https://github.com/vesoft-inc/nebula/pull/2557</a></li> 
 <li><code>SHOW JOBS</code> 只显示本 SPACE 的 JOB，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2872" target="_blank">https://github.com/vesoft-inc/nebula/pull/2872</a></li> 
 <li>为除 GUEST 之外的所有角色授予作业权限，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2928" target="_blank">https://github.com/vesoft-inc/nebula/pull/2928</a></li> 
 <li>优化内存水位检测，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2885" target="_blank">https://github.com/vesoft-inc/nebula/pull/2885</a></li> 
 <li>支持 storage 的慢查询终止，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2534" target="_blank">https://github.com/vesoft-inc/nebula/pull/2534</a></li> 
</ul> 
<h3>Bugfix</h3> 
<ul> 
 <li>修复了 <code>LOOKUP</code> 中 <code>YIELD</code> 子句出现聚合函数时 nebula 连接会被中断的缺陷，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3245" target="_blank">https://github.com/vesoft-inc/nebula/pull/3245</a></li> 
 <li>修复 <code>raftpart::reset</code> 时清理部分 RocksDB 数据的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2522" target="_blank">https://github.com/vesoft-inc/nebula/pull/2522</a></li> 
 <li>修复了插入不匹配的日期时间类型的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2527" target="_blank">https://github.com/vesoft-inc/nebula/pull/2527</a></li> 
 <li>修复了设置毫秒失败但微秒有效的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2781" target="_blank">https://github.com/vesoft-inc/nebula/pull/2781</a></li> 
 <li>修复了批量插入过多数据时 meta 服务崩溃（百万行）的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2813" target="_blank">https://github.com/vesoft-inc/nebula/pull/2813</a></li> 
 <li>修复了当 SPACE 中不存在边 schema 时获取边信息导致崩溃的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2571" target="_blank">https://github.com/vesoft-inc/nebula/pull/2571</a></li> 
 <li>修复了属性数据类型为 fixed_string 时 GO WHERE 子句表达式解析错误，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2762" target="_blank">https://github.com/vesoft-inc/nebula/pull/2762</a></li> 
 <li>修复了 <code>FIND ALL PATH</code> 查询不到的错误，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2773" target="_blank">https://github.com/vesoft-inc/nebula/pull/2773</a></li> 
 <li>修复了没有配置角色的用户却有查找 SPACE 的角色权限问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2778" target="_blank">https://github.com/vesoft-inc/nebula/pull/2778</a></li> 
 <li>修复了 CASE 表达式错误，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2819" target="_blank">https://github.com/vesoft-inc/nebula/pull/2819</a></li> 
 <li>修复了使用 time 函数时死循环问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2820" target="_blank">https://github.com/vesoft-inc/nebula/pull/2820</a></li> 
 <li>修复了当节点被 shutdown 后，JOB 仍显示为运行中的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2843" target="_blank">https://github.com/vesoft-inc/nebula/pull/2843</a></li> 
 <li>修复了在多个副本的情况下，INSERT 语句可能导致副本之间属性值不一致的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2862" target="_blank">https://github.com/vesoft-inc/nebula/pull/2862</a></li> 
 <li>修复了 USE 后提交作业时 SPACE 不对的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3010" target="_blank">https://github.com/vesoft-inc/nebula/pull/3010</a></li> 
 <li>修复了当列不为空时获取 thrift 结构属性出错的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3012" target="_blank">https://github.com/vesoft-inc/nebula/pull/3012</a></li> 
 <li>修复了即使 meta 未 ready，graphd 也能运行的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3069" target="_blank">https://github.com/vesoft-inc/nebula/pull/3069</a></li> 
 <li>修复了使用 <code>FIND PATH WITH PROP</code> 时，悬挂边会返回空顶点的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3008" target="_blank">https://github.com/vesoft-inc/nebula/pull/3008</a></li> 
 <li>修复了 <code>YIELD DISTINCT</code> map 类型时的崩溃问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3051" target="_blank">https://github.com/vesoft-inc/nebula/pull/3051</a></li> 
 <li>修复了错误的 ip 或者 host 时服务仍然可以启动的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3057" target="_blank">https://github.com/vesoft-inc/nebula/pull/3057</a></li> 
 <li>修复了在一个语句中更改相同属性的错误，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3036" target="_blank">https://github.com/vesoft-inc/nebula/pull/3036</a></li> 
 <li>修复了在边上多步过滤无效的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3144" target="_blank">https://github.com/vesoft-inc/nebula/pull/3144</a></li> 
</ul>
                                        </div>
                                      
</div>
            