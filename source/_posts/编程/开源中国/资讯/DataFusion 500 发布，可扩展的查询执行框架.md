
---
title: 'DataFusion 5.0.0 发布，可扩展的查询执行框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0826/065632_sDrb_4937141.png'
author: 开源中国
comments: false
date: Thu, 26 Aug 2021 07:15:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0826/065632_sDrb_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>DataFusion 是一个可扩展的查询执行框架，用 Rust 编写，使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farrow.apache.org%2F" target="_blank">Apache Arrow</a> 作为其内存格式。</p> 
<p>DataFusion 支持用于构建逻辑查询计划的 SQL 和 DataFrame API，以及能够使用线程对分区数据源（CSV 和 Parquet）并行执行的查询优化器和执行引擎。DataFusion 还通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Farrow-datafusion%2Fblob%2Fmaster%2Fballista%2FREADME.md" target="_blank">Ballista</a> crate 支持分布式查询执行 。</p> 
<p>近日，Apache Arrow 团队正式推出了 DataFusion 5.0.0 版本，该版本汇集了 31 个不同的贡献者共 211 个提交。</p> 
<p>该版本的更新亮点包括：</p> 
<h3>性能</h3> 
<p>这个版本在性能上有许多改进，下图显示了单个 TPC-H 查询与前一版本相比的相对性能。</p> 
<p>该版本还扩展了对更多 TPC-H 查询的支持：q7、q8、q9 和 q13 均在 DataFusion 5.0 中成功运行。</p> 
<p><img alt height="431" src="https://static.oschina.net/uploads/space/2021/0826/065632_sDrb_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>新功能</h3> 
<ul> 
 <li>对 SQL-99 Analytics 的初步支持；</li> 
 <li>改进了 JOIN 支持：cross join、semi-join、anti join，以及对空处理的修正；</li> 
 <li>改进的 EXPLAIN 支持；</li> 
 <li>支持 SELECT DISTINCT；</li> 
 <li>支持 Json 和 NDJson 格式的输入；</li> 
 <li>具有关系的查询列；</li> 
 <li>增加了更多与日期时间相关的函数： <code>now</code>, <code>date_trunc</code>, <code>to_timestamp_millis</code>, <code>to_timestamp_micros</code>, <code>to_timestamp_seconds</code></li> 
 <li>Streaming Dataframe.collect；</li> 
 <li>支持表列别名；</li> 
 <li>仅使用统计数字回答 count(*)、min() 和 max() 查询；</li> 
 <li>支持按列位置分组；</li> 
 <li>增加了常量折叠查询优化器；</li> 
 <li>哈希分区聚合；</li> 
 <li>增加了 <code>random</code> SQL 函数；</li> 
 <li>实现了对浮点和字典类型的计数区分；</li> 
 <li>在 Datafusion 中重新导出 arrow 和 parquet 板块；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Farrow-datafusion%2Fblob%2F5.0.0%2Fdatafusion%2FCHANGELOG.md" target="_blank">https://github.com/apache/arrow-datafusion/blob/5.0.0/datafusion/CHANGELOG.md</a></p>
                                        </div>
                                      
</div>
            