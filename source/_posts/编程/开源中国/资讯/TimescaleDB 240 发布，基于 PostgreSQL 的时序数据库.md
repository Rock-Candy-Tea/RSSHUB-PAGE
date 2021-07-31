
---
title: 'TimescaleDB 2.4.0 发布，基于 PostgreSQL 的时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9049'
author: 开源中国
comments: false
date: Sat, 31 Jul 2021 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9049'
---

<div>   
<div class="content">
                                                                                            <p>TimescaleDB 2.4.0 现已发布，此版本添加了自 <a href="https://www.oschina.net/news/149323/timescaledb-2-3-1-released">2.3.1</a> 版本以来的新实验性功能。TimescaleDB 是基于 PostgreSQL 开发的一款时序数据库，以插件化的形式打包提供。 </p> 
<p>此版本中的实验性功能是：</p> 
<ul> 
 <li>用于在分布式 hypertable 设置中跨数据节点进行块操作的 API。这包括添加数据节点并将块移动到新数据节点以进行集群重新平衡的能力。</li> 
 <li><code>time_bucket_ng</code>函数是<code>time_bucket</code>的较新版本。支持年、月、日、小时、分钟和秒。</li> 
</ul> 
<p>此版本还包括几个错误修复；以及 TimescaleDB 2.4 不再支持 Postgres 11，需要 Postgres 12 及以上版本。</p> 
<p>具体更新内容如下：</p> 
<p><strong>Experimental Features</strong></p> 
<ul> 
 <li>#3293 添加 timescaledb_experimental 模式</li> 
 <li>#3302 将 block_new_chunks 和 allow_new_chunks API 添加到实验模式。添加基于块的 refresh_continuous_aggregate。</li> 
 <li>#3211 引入实验性的 time_bucket_ng 函数</li> 
 <li>#3366 允许在连续聚合中使用实验性 time_bucket_ng 函数</li> 
 <li>#3408 在 time_bucket_ng 中支持秒、分钟和小时</li> 
 <li>#3446 实现对 chunk copy/move 的清理。</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>#3401 修复没有 fdw_private 的 RelOptInfo 的段错误</li> 
 <li>#3411 验证压缩路径的压缩块有效性</li> 
 <li>#3416 修复连续聚合视图的目标列表名称</li> 
 <li>#3434 从 relcache 无效回调中删除扩展检查</li> 
 <li>#3440 修复 remote_tx_heal_data_node 以仅使用当前数据库</li> 
</ul> 
<p>详情查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank">https://github.com/timescale/timescaledb/blob/master/CHANGELOG.md</a></p>
                                        </div>
                                      
</div>
            