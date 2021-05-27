
---
title: 'TimescaleDB 2.3.0 发布，最后一个支持 PostgreSQL 11 的版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8470'
author: 开源中国
comments: false
date: Wed, 26 May 2021 23:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8470'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TimescaleDB 是基于 PostgreSQL 开发的一款时序数据库，以插件化的形式打包提供。此版本增加了对分布式超表（多节点 TimescaleDB）的支持，并添加了一些新特性和功能增强，让用户对数据的控制更加清晰和灵活。</p> 
<p>TimescaleDB 2.3.0 现已发布。TimescaleDB 2.3 将是支持 PostgreSQL 11 的最后一个小版本。TimescaleDB 2.4 将需要 PostgreSQL 12 或 13。</p> 
<p>特性：</p> 
<ul> 
 <li>#3116 增加了分布式 hypertables 压缩策略</li> 
 <li>#3162 在执行分布式 INSERTs 时使用 COPY</li> 
 <li>#3199 在分布式 hypertables 上增加 GENERATED 列的支持</li> 
 <li>#3210 在分布式 hypertables 上添加触发器支持</li> 
 <li>#3230 支持插入到压缩块中</li> 
</ul> 
<p>错误修正：</p> 
<ul> 
 <li>#3213 向压缩的 hypertables 传播授权</li> 
 <li>#3229 更新块时使用正确的锁模式</li> 
 <li>#3243 在 decompress_chunk_plan_create 中修复断言故障</li> 
 <li>#3250 修复 hypertables 上的约束触发器</li> 
 <li>#3251 修复由于对 chunk_scan_internal 的错误调用导致的分段故障</li> 
 <li>#3252 修复带有过渡表的阻塞触发器</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Freleases%2Ftag%2F2.3.0" target="_blank">https://github.com/timescale/timescaledb/releases/tag/2.3.0</a></p>
                                        </div>
                                      
</div>
            