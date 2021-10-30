
---
title: 'TimescaleDB 2.5.0 发布，支持 PostgreSQL 14'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1626'
author: 开源中国
comments: false
date: Sat, 30 Oct 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1626'
---

<div>   
<div class="content">
                                                                                            <p>TimescaleDB 是基于 PostgreSQL 开发的一款时序数据库，以插件化的形式打包提供。此版本增加了对分布式超表（多节点 TimescaleDB）的支持，并添加了一些新特性和功能增强，让用户对数据的控制更加清晰和灵活。</p> 
<p>TimescaleDB 2.5.0 现已发布，这个版本值得注意的特性包括：</p> 
<ul> 
 <li>为分布式 Hypertables 添加连续聚合；</li> 
 <li>新增对 PostgreSQL 14 的支持；</li> 
 <li>实验性：在 <code>time_bucket_ng()</code> 中支持时区，包括 <code>origin</code> 参数；</li> 
</ul> 
<p><strong>错误修复</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3592" target="_blank">#3592</a> 允许在分布式 Hypertables 上改变列类型；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3618" target="_blank">#3618</a> 修复执行来自用户行为的 refresh_caggs 的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3625" target="_blank">#3625</a> 在创建 chunk 时添加共享的依赖关系；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3654" target="_blank">#3654</a> 修复 reorder_chunk 中的索引 attnum 映射</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3708" target="_blank">#3708</a> 修复 get_aggsplit 的崩溃问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3712" target="_blank">#3712</a> 修复 GRANT/REVOKE ALL IN SCHEMA 处理问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3727" target="_blank">#3727</a> 在 distributed_exec 中修复 DirectFunctionCall 崩溃问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3728" target="_blank">#3728</a> 修复带有 varchar 列的 SkipScan；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fissues%2F3733" target="_blank">#3733</a> 修复自定义类型的自定义统计的 ANALYZE 崩溃问题；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3747" target="_blank">#3747</a> 在 DecompressChunk 中总是重置 expr context；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Freleases%2Ftag%2F2.5.0" target="_blank">https://github.com/timescale/timescaledb/releases/tag/2.5.0</a></p>
                                        </div>
                                      
</div>
            