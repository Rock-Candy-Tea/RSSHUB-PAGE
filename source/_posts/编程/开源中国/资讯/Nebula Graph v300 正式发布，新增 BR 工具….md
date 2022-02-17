
---
title: 'Nebula Graph v3.0.0 正式发布，新增 BR 工具…'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3888'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 10:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3888'
---

<div>   
<div class="content">
                                                                                            <p style="color:#222222; text-align:start">Nebula Graph v3.0.0 新版发布，支持 BR、openCypher 多 MATCH 查询、KV 分离、topN 下推以及中文 Schema 等多种特性。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">Feature</h2> 
<ul style="margin-left:1.25em; margin-right:0"> 
 <li> <p>新增备份与恢复工具BR。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3469" target="_blank">#3469</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-agent%2Fpull%2F1" target="_blank">#1</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-br%2Fpull%2F22" target="_blank">#22</a></p> </li> 
 <li> <p>支持<span> </span>openCypher 多 MATCH 查询。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3519" target="_blank">#3519</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3318" target="_blank">#3318<span> </span></a></p> </li> 
 <li> <p>新增存算合并版。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3310" target="_blank">#3310</a></p> </li> 
 <li> <p>新增存储引擎的 kv 分离。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3281" target="_blank">#3281</a></p> </li> 
 <li> <p>新增<code>LOOKUP</code>支持 topN 下推。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3499" target="_blank">#3499</a></p> </li> 
 <li> <p>新增不带 Tag 的点。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3316" target="_blank">#3316</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3335" target="_blank">#3335</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3328" target="_blank">#3328</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3286" target="_blank">#3286</a></p> </li> 
 <li> <p>新增参数化查询。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3379" target="_blank">#3379</a></p> </li> 
 <li> <p>新增不指定 VID 的查询，通过<code>LIMIT</code>子句限制输出结果。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3320" target="_blank">#3320</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3329" target="_blank">#3329</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3262" target="_blank">#3262</a></p> </li> 
 <li> <p>新增<span> </span>duration<span> </span>数据类型和函数。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3338" target="_blank">#3338</a></p> </li> 
 <li> <p>支持中文 Schema，可使用大部分 1~4 字节的<span> </span>UTF-8 编码字符。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3380" target="_blank">#3380</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3440" target="_blank">#3440</a></p> </li> 
 <li> <p>新增查看指定用户权限。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3300" target="_blank">#3300</a></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">Enhancement</h2> 
<ul style="margin-left:1.25em; margin-right:0"> 
 <li> <p>重构集群管理。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3343" target="_blank">#3343</a></p> </li> 
 <li> <p>当日志磁盘空间不足时，支持改变日志级别。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3576" target="_blank">#3576</a></p> </li> 
 <li> <p>支持反引号中的任何字符串作为 Tag 名称。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3424" target="_blank">#3424</a></p> </li> 
 <li> <p>Storage 服务通过心跳将 partition 的磁盘路径信息发送到 Meta 服务。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3369" target="_blank">#3369</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3416" target="_blank">#3416</a></p> </li> 
 <li> <p>添加对无效密码尝试的限制。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3573" target="_blank">#3573</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3629" target="_blank">#3629</a></p> </li> 
 <li> <p>TOSS 支持<code>DELETE</code>操作的一致性。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3374" target="_blank">#3374</a></p> </li> 
 <li> <p>支持对接 logrotate。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3541" target="_blank">#3541</a></p> </li> 
 <li> <p>支持更多的统计。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3446" target="_blank">#3446</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3605" target="_blank">#3605</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3590" target="_blank">#3590</a></p> </li> 
 <li> <p>增强日期解析器。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3179" target="_blank">#3179</a></p> </li> 
 <li> <p>删除 meta 服务中的读锁以减少读写锁的副作用。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3256" target="_blank">#3256</a></p> </li> 
 <li> <p>重构存储索引，解决节点间耦合严重的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3196" target="_blank">#3196</a></p> </li> 
 <li> <p>支持指定<code>round()</code>函数的浮点精度。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3178" target="_blank">#3178</a></p> </li> 
 <li> <p>ES 客户端支持 https。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3150" target="_blank">#3150</a></p> </li> 
 <li> <p>将版本信息移到心跳之外。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3378" target="_blank">#3378</a></p> </li> 
 <li> <p>支持空的列表、集合、映射。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3302" target="_blank">#3302</a></p> </li> 
 <li> <p>支持创建地理索引时指定 S2 区域覆盖参数。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3396" target="_blank">#3396</a></p> </li> 
 <li> <p><code>SHOW HOSTS</code>中新增版本信息的显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3702" target="_blank">#3702</a></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">Bug fix</h2> 
<ul style="margin-left:1.25em; margin-right:0"> 
 <li> <p>修复 nGQL 中未指定值时使用默认值的情况下，存在内存没有释放的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3666" target="_blank">#3666</a></p> </li> 
 <li> <p>修复无法使用<code>coalesce()</code>函数的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3653" target="_blank">#3653</a></p> </li> 
 <li> <p>修复批量插入时，由于 Tag 已创建索引而导致查找结果错误的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3627" target="_blank">#3627</a></p> </li> 
 <li> <p>修复表达式超过深度时的崩溃问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3606" target="_blank">#3606</a></p> </li> 
 <li> <p>禁用 nGQL 的<code>YIELD</code>子句和<code>WHERE</code>子句中的聚合函数。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3597" target="_blank">#3597</a></p> </li> 
 <li> <p>修复在<code>UNWIND</code>、<code>WHERE</code>子句中使用聚合函数时的崩溃问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3397" target="_blank">#3397</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3355" target="_blank">#3355</a></p> </li> 
 <li> <p>修复使用旧 Schema 版本值重建标签索引的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3332" target="_blank">#3332</a></p> </li> 
 <li> <p>修复使用<code>GO...REVERSELY</code>查询结果会包含过期边的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3536" target="_blank">#3536</a></p> </li> 
 <li> <p>修复 CentOS 6 中估计内存信息的错误。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3534" target="_blank">#3534</a></p> </li> 
 <li> <p>修复当<code>LOOKUP</code>语句包含一个过滤器，该过滤器由一个逻辑 AND 表达式和一个只有一个元素的 IN 表达式组成时的崩溃问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3525" target="_blank">#3525</a></p> </li> 
 <li> <p>修复 metad 在高负载下挂起的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3482" target="_blank">#3482</a></p> </li> 
 <li> <p>修复<code>UNWIND</code>子图的崩溃问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3506" target="_blank">#3506</a></p> </li> 
 <li> <p>修复重建索引时<code>DROP SPACE</code>的崩溃问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3406" target="_blank">#3406</a></p> </li> 
 <li> <p>修复 cgroup v2 下读取内存统计的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3419" target="_blank">#3419</a></p> </li> 
 <li> <p>修复<code>DROP TAG INDEX</code>会删除同名边索引，删除边索引时也会删除同名 TAG 索引的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3413" target="_blank">#3413</a></p> </li> 
 <li> <p>修复克隆空间后无法显示边的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3351" target="_blank">#3351</a></p> </li> 
 <li> <p>修复索引存在检查的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3315" target="_blank">#3315</a></p> </li> 
 <li> <p>修复执行<code>ALTER</code>语句后获取类型属性时可能导致存储获取空指针的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3325" target="_blank">#3325</a></p> </li> 
 <li> <p>优化 raft 从而确保系统更稳定。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3172" target="_blank">#3172</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3435" target="_blank">#3435</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3358" target="_blank">#3358</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3322" target="_blank">#3322</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3031" target="_blank">#3031</a></p> </li> 
 <li> <p>内存比率大于 1.0 时取消内存检查。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3289" target="_blank">#3289</a></p> </li> 
 <li> <p>修复使用 Ninja 编译时的错误。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3195" target="_blank">#3195</a></p> </li> 
 <li> <p>修复同时创建同名 Tag 和 Edge type 可能都成功的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3735" target="_blank">#3735</a></p> </li> 
 <li> <p>修复当不同的图空间中存在相同的 Tag 或 Edge type 的内部 ID 时，创建全文索引失败的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3747" target="_blank">#3747</a></p> </li> 
 <li> <p>修复<code>YIELD</code>子句和<span> </span><code>GO</code><span> </span>语句中变量不一致的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3430" target="_blank">#3430</a></p> </li> 
 <li> <p>修复当 Schema 版本大于 256 时的崩溃问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3893" target="_blank">#3893</a></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">Incompatibility</h2> 
<p style="color:#222222; text-align:start">Nebula Graph v3 不支持 v2.x 的大部分生态工具，请升级生态工具。</p> 
<ul style="margin-left:1.25em; margin-right:0"> 
 <li> <p>在配置文件中添加的 Storage 主机无法直接读写，配置文件的作用仅仅是将 Storage 主机注册至 Meta 服务中。必须使用<code>ADD HOSTS</code>命令后，才能正常读写 Storage 主机。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3343" target="_blank">#3343</a></p> </li> 
 <li> <p>禁用 ZONE 和 GROUP。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3776" target="_blank">#3776</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3825" target="_blank">#3825</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3330" target="_blank">#3330</a></p> </li> 
 <li> <p>禁用<code>BALANCE DATA</code>。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3756" target="_blank">#3756</a></p> </li> 
 <li> <p>将默认会话超时时间从<code>0</code>修改为<code>28800</code>秒，范围从<code>1</code>到<code>604800</code>秒。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3357" target="_blank">#3357</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3807" target="_blank">#3807</a></p> </li> 
 <li> <p>添加<code>SHOW LOCAL SESSIONS</code>和<code>SHOW LOCAL QUERIES</code>命令，并弃用<code>SHOW ALL QUERIES</code>。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3488" target="_blank">#3488</a></p> </li> 
 <li> <p>从点至少有一个 Tag 修改为可以没有 Tag。<code>DELETE VERTEX</code>修改为默认只删除点，不再删除该点关联的出边和入边，此时将默认存在悬挂边。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3316" target="_blank">#3316</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3335" target="_blank">#3335</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3328" target="_blank">#3328</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3286" target="_blank">#3286</a></p> </li> 
 <li> <p>禁用<code>YIELD</code>子句返回自定义变量。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3271" target="_blank">#3271<span> </span><span style="background-color:var(--primary-low); color:var(--primary-medium)">1</span></a></p> </li> 
 <li> <p><code>FETCH</code>、<code>GO</code>、<code>LOOKUP</code>、<code>FIND PATH</code>、<code>GET SUBGRAPH</code>语句中必须添加<code>YIELD</code>子句。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F2957" target="_blank">#2957<span> </span><span style="background-color:var(--primary-low); color:var(--primary-medium)">1</span></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3056" target="_blank">#3056</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3139" target="_blank">#3139</a></p> </li> 
 <li> <p>新增非保留关键字<code>s2_max_level</code>、<code>s2_max_cells</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3396" target="_blank">#3396</a></p> </li> 
 <li> <p>MATCH 语句中获取点属性时，必须指定 Tag，例如从<code>return v.name</code>变为<code>return v.player.name</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F3255" target="_blank">#3255</a></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">历史版本</h2> 
<p style="color:#222222; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnebula-graph.com.cn%2Ftags%2Frelease-note%2F" target="_blank">历史版本</a></p> 
<p style="color:#222222; text-align:start">可前往 GitHub 体验该版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Freleases%2Ftag%2Fv3.0.0" target="_blank">https://github.com/vesoft-inc/nebula/releases/tag/v3.0.</a></p>
                                        </div>
                                      
</div>
            