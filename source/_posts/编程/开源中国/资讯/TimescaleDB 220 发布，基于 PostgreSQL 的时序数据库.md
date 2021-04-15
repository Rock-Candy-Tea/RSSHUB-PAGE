
---
title: 'TimescaleDB 2.2.0 发布，基于 PostgreSQL 的时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5292'
author: 开源中国
comments: false
date: Thu, 15 Apr 2021 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5292'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TimescaleDB 2.1.1 现已发布，此版本包含了自 2.1.1 版本以来增加的一些新功能，官方将其标为中等程度的优先升级。TimescaleDB 是基于 PostgreSQL 开发的一款时序数据库，以插件化的形式打包提供。 </p> 
<p>该版本添加了 Skip Scan 优化，显著提高了 DISTINCT ON 的查询性能。目前，这个优化还不能应用于分布式超表的查询。同时还增加了一个功能，以创建一个分布式的还原点，允许从备份中执行多节点集群的一致还原。</p> 
<p>此外，其还进行了一些 bug 修复。包括解决了 size 和 stats functions 的问题、分布式插入中内存占用率高、分布式 ORDER BY queries 速度慢、涉及 INCLUDE 的索引和 single chunk 查询规划等问题。</p> 
<p><strong>PostgreSQL 11 弃用公告</strong></p> 
<p>官方表示，其计划只继续支持 PostgreSQL 11 直到 2021 年 6 月中旬。彼时，他们将公布具体的不支持 PostgreSQL 11 的 TimescaleDB 版本。</p> 
<p><strong>Major Features</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F2843" target="_blank">＃2843</a> 添加分布式还原点功能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3000" target="_blank">＃3000</a> SkipScan 加快 SELECT DISTINCT 的速度</li> 
</ul> 
<p><strong>Bugfixes</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F2989" target="_blank">＃2989</a> 重构和强化 size 和 stats functions</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3058" target="_blank">＃3058</a> 减少分布式插入的内存使用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3067" target="_blank">＃3067</a> 修复 multi-node order by queries 极慢的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3082" target="_blank">＃3082</a> 修复块索引列名称映射</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3083" target="_blank">＃3083</a> 在 ChunkAppend 中保留 Append pathkeys</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Freleases%2Ftag%2F2.2.0" target="_blank">https://github.com/timescale/timescaledb/releases/tag/2.2.0</a></p>
                                        </div>
                                      
</div>
            