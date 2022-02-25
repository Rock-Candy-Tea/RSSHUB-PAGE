
---
title: 'TimescaleDB 2.6.0 发布，基于 PostgreSQL 的时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5165'
author: 开源中国
comments: false
date: Fri, 25 Feb 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5165'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">TimescaleDB 是基于 PostgreSQL 开发的一款时序数据库，以插件化的形式打包提供。此版本增加了对分布式超表（多节点 TimescaleDB）的支持，并添加了一些新特性和功能增强，让用户对数据的控制更加清晰和灵活。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">TimescaleDB 2.6.0 现已发布，<span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>自 2.5.2 版本以来增加的主要新功能包括：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>带压缩的 Continuous aggregates</li> 
 <li>time_bucket_ng 对连续聚合的 N 个月和时区的支持</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>2.6 版本中的实验性功能包括：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>time_bucket_ng 函数，time_bucket 的更新版本。此函数支持年、月、日、小时、分钟、秒和时区。</li> 
 <li>time_bucket_ng 对连续聚合的 N 个月和时区的支持。</li> 
 <li>用于在分布式 hypertable setup 中跨数据节点进行分块操作的 API。这包括添加数据节点并将块移动到新数据节点以进行集群重新平衡的能力。</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>Features</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3768" target="_blank">#3768</a> 允许 ALTER TABLE ADD COLUMN with DEFAULT 在 compressed hypertable 上</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3769" target="_blank">#3769</a> 允许 compressed hypertable 上的 ALTER TABLE DROP COLUMN</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3873" target="_blank">#3873</a> 对连续聚合启用压缩</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3943" target="_blank">#3943</a> 优化 first/last</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3945" target="_blank">#3945</a> 在多节点上添加对 ALTER SCHEMA 的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3949" target="_blank">#3949</a> 在多节点上添加对 DROP SCHEMA 的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3977" target="_blank">#3977</a> CAGG 中的时区支持</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>Bug 修复</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3808" target="_blank">#3808</a> 正确处理 max_retries 选项</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3863" target="_blank">#3863</a> 修复远程事务修复逻辑</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3869" target="_blank">#3869</a> 修复分布式 hypertable 上的 ALTER SET/DROP NULL 约束</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3944" target="_blank">#3944</a> 修复 add_compression_policy 中的 segfault</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3961" target="_blank">#3961</a> 修复分布式 hypertable 上 EXPLAIN VERBOSE 中的崩溃</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F4015" target="_blank">#4015</a> 消除 interpolate 中的浮点取整不稳定性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F4019" target="_blank">#4019</a> 更新处于过渡状态的 ts_extension_oid</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F4073" target="_blank">#4073</a> 修复分区方案中的缓冲区溢出问题</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>改进</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>具有大量块的 hypertable 的查询规划性能得到改进。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Freleases%2Ftag%2F2.6.0" target="_blank">https://github.com/timescale/timescaledb/releases/tag/2.6.0</a></p>
                                        </div>
                                      
</div>
            