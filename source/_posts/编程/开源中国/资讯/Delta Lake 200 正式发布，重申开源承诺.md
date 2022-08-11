
---
title: 'Delta Lake 2.0.0 正式发布，重申开源承诺'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-410afbe8155554a5fcc3e14ee9a51090e5d.png'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 18:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-410afbe8155554a5fcc3e14ee9a51090e5d.png'
---

<div>   
<div class="content">
                                                                                            <p>Delta Lake 2.0.0 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdelta.io%2Fblog%2F2022-08-02-delta-2-0-the-foundation-of-your-data-lake-is-open%2F" target="_blank">发布</a>，该版本发布正值 Delta Lake 的 3 岁生日之际。“我们很高兴地宣布在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspark.apache.org%2Freleases%2Fspark-release-3-2-0.html" target="_blank">Apache Spark 3.2 上发布 Delta Lake 2.0 (</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.org%2Fproject%2Fdelta-spark%2F" target="_blank">pypi</a><span style="background-color:#ffffff; color:#002638">,</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmvnrepository.com%2Fartifact%2Fio.delta%2Fdelta-core_2.13%2F2.0.0" target="_blank"><span> </span>maven</a><span style="background-color:#ffffff; color:#002638">,</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Freleases%2Ftag%2Fv2.0.0" target="_blank"><span> </span>release notes</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspark.apache.org%2Freleases%2Fspark-release-3-2-0.html" target="_blank">)</a>......Delta Lake 2.0 的意义不仅仅是一个数字，它重申了我们对 Delta Lake 开源的集体承诺”。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="507" src="https://oscimg.oschina.net/oscnet/up-410afbe8155554a5fcc3e14ee9a51090e5d.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Delta Lake 是一个存储层，为 Apache Spark 和大数据 workloads 提供 ACID 事务能力，其通过写和快照隔离之间的乐观并发控制（optimistic concurrency control），在写入数据期间提供一致性的读取，从而为构建在 HDFS 和云存储上的数据湖（data lakes）带来可靠性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="247" src="https://oscimg.oschina.net/oscnet/up-e0e39618238310f14441b89b58dc282af88.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本的一些主要功能包括：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li> <p><span><strong>支持 Delta 表上的 Change Data Feed。</strong>Change Data Feed 表示不同版本的表之间的行级更改。启用后，将记录有关表上每个写入操作的行级别更改的附加信息。有关更多详细信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.delta.io%2F2.0.0%2Fdelta-change-data-feed.html" target="_blank">文档</a>。</span></p> </li> 
</ul> 
<p><span><img alt height="223" src="https://oscimg.oschina.net/oscnet/up-0597fad95ecfbb3a4bfeed870d8b34984a3.png" width="500" referrerpolicy="no-referrer"></span></p> 
<ul> 
 <li> <p><span><strong>支持数据的 Z-Order 聚类，减少读取的数据量。</strong>Z-Ordering 是一种将相关信息放在同一组文件中的技术。这种数据聚类允许列统计信息（在 Delta 1.2 中发布）更有效地跳过查询中基于过滤器的数据。有关更多详细信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.delta.io%2F2.0.0%2Foptimizations-oss.html%23z-ordering-multi-dimensional-clustering" target="_blank">文档</a>。</span></p> </li> 
</ul> 
<p><img alt height="318" src="https://oscimg.oschina.net/oscnet/up-ca5f2522da563f0552f2753d7e92cf26f62.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p><span><strong>支持对 Delta 表的幂等写入，</strong>以启用 Delta 表写入作业的容错重试，而无需多次将数据写入表。有关更多详细信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.delta.io%2F2.0.0%2Fdelta-streaming.html%23idempotent-table-writes-in-foreachbatch" target="_blank">文档</a>。</span></p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:start"><span>app_id</span> <span style="color:#3f7f5f">=</span> <span style="color:#3f7f5f">...</span> <span style="color:#3f7f5f"># A unique string that is used as an application ID.</span>

<strong style="color:#7f0055">def</strong> <span style="color:#0000ff">writeToDeltaLakeTableIdempotent</span><span>(</span><span>batch_df</span><span>,</span> <span>batch_id</span><span>):</span>
  <span>batch_df</span><span style="color:#3f7f5f">.</span><span>write</span><span style="color:#3f7f5f">.</span><span>format</span><span>(</span><span style="color:#3f7f5f">...</span><span>)</span><span style="color:#3f7f5f">.</span><span>option</span><span>(</span><span style="color:#2a00ff">"txnVersion"</span><span>,</span> <span>batch_id</span><span>)</span><span style="color:#3f7f5f">.</span><span>option</span><span>(</span><span style="color:#2a00ff">"txnAppId"</span><span>,</span> <span>app_id</span><span>)</span><span style="color:#3f7f5f">.</span><span>save</span><span>(</span><span style="color:#3f7f5f">...</span><span>)</span> <span style="color:#3f7f5f"># location 1</span>
  <span>batch_df</span><span style="color:#3f7f5f">.</span><span>write</span><span style="color:#3f7f5f">.</span><span>format</span><span>(</span><span style="color:#3f7f5f">...</span><span>)</span><span style="color:#3f7f5f">.</span><span>option</span><span>(</span><span style="color:#2a00ff">"txnVersion"</span><span>,</span> <span>batch_id</span><span>)</span><span style="color:#3f7f5f">.</span><span>option</span><span>(</span><span style="color:#2a00ff">"txnAppId"</span><span>,</span> <span>app_id</span><span>)</span><span style="color:#3f7f5f">.</span><span>save</span><span>(</span><span style="color:#3f7f5f">...</span><span>)</span> <span style="color:#3f7f5f"># location 2</span></pre> 
<ul> 
 <li> <p><span><strong>支持将 Delta 表中的列作为元数据变更操作来删除。</strong>此命令从元数据中删除列，而不是从底层文件中删除列数据。有关更多详细信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.delta.io%2F2.0.0%2Fdelta-batch.html%23drop-columns" target="_blank">文档</a>。</span></p> </li> 
</ul> 
<p><span><img alt height="182" src="https://oscimg.oschina.net/oscnet/up-e48573db6d8b94681f3f0fdeb533ecc032f.png" width="500" referrerpolicy="no-referrer"></span></p> 
<ul> 
 <li> <p><span><strong>支持动态分区覆盖。</strong>仅覆盖在运行时写入数据的分区。值得注意的是，</span>动态分区覆盖与分区表的<code>replaceWhere</code>选项冲突。<span>有关详细信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.delta.io%2F2.0.0%2Fdelta-batch.html%23dynamic-partition-overwrites" target="_blank">文档</a>。</span></p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:start"><strong style="color:#7f0055">SET</strong><span style="color:#bbbbbb"> </span><span>spark</span><span>.</span><strong style="color:#7f0055">sql</strong><span>.</span><span>sources</span><span>.</span><span>partitionOverwriteMode</span><span style="color:#3f7f5f">=</span><strong style="color:#7f0055">dynamic</strong><span>;</span>
<strong style="color:#7f0055">INSERT</strong><span style="color:#bbbbbb"> </span><span>OVERWRITE</span><span style="color:#bbbbbb"> </span><strong style="color:#7f0055">TABLE</strong><span style="color:#bbbbbb"> </span><strong style="color:#7f0055">default</strong><span>.</span><span>people10m</span><span style="color:#bbbbbb"> </span><strong style="color:#7f0055">SELECT</strong><span style="color:#bbbbbb"> </span><span style="color:#3f7f5f">*</span><span style="color:#bbbbbb"> </span><strong style="color:#7f0055">FROM</strong><span style="color:#bbbbbb"> </span><span>morePeople</span><span>;</span></pre> 
<ul> 
 <li> <p><span><strong>对 multi-part checkpoints 的实验性支持，</strong>将 Delta Lake checkpoint 拆分为多个部分，以加快 checkpoint 的写入和读取速度。有关更多详细信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.delta.io%2F2.0.0%2Foptimizations-oss.html%23multi-part-checkpointing" target="_blank">文档</a>。</span></p> </li> 
 <li> <p><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.delta.io%2F2.0.0%2Fapi%2Fpython%2Findex.html%23delta.tables.DeltaTable.optimize" target="_blank">Python</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.delta.io%2F2.0.0%2Fapi%2Fscala%2Fio%2Fdelta%2Ftables%2FDeltaTable.html%23optimize%28%29%3Aio.delta.tables.DeltaOptimizeBuilder" target="_blank">Scala</a> API 支持 OPTIMIZE 文件压缩和 Z-order by。</span></p> </li> 
</ul> 
<ul> 
 <li> <p><span><strong>其他显着变化</strong></span></p> 
  <ul> 
   <li>通过添加对嵌套列生成列跳过的支持，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Fcommit%2F258071dd" target="_blank">改进生成列数据跳过</a></li> 
   <li>通过阻止 Delta Lake 中不受支持的数据类型来<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Fcommit%2F57207c8a" target="_blank">改进表架构验证。</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Fcommit%2F392f8bbb" target="_blank">支持</a>创建具有空模式的 Delta Lake 表。</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Fcommit%2Fa6c161dc" target="_blank">更改</a> DROP CONSTRAINT 在约束不存在时引发错误的行为。在此版本之前，该命令用于静默返回。</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Fcommit%2Fdde57a3b" target="_blank">当分区值中包含 space 时，修复</a>符号链接清单生成问题。</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Fcommit%2F5a829a25" target="_blank">修复</a>了收集不正确的提交统计信息的问题。</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Fcommit%2F91f065" target="_blank">支持</a> S3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.delta.io%2F2.0.0%2Fdelta-storage.html%23multi-cluster-setup" target="_blank">多集群写入</a>支持的 LogStore 中的 SimpleAWSCredentialsProvider 或 TemporaryAWSCredentialsProvider。</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Fcommit%2F86ae53" target="_blank">修复</a>了生成的列中的一个问题，即使列是空的，也不允许在插入的 DataFrame 中写入空列。</li> 
  </ul> </li> 
</ul> 
<h4>Benchmark Framework Update</h4> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>独立于此版本，开发团队改进了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Ftree%2Fmaster%2Fbenchmarks" target="_blank">编写大型 scala 性能基准测试的框架（在</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Freleases%2Ftag%2Fv1.2.0" target="_blank">1.2.0</a> 版本中添加了初始版本），添加<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdelta-io%2Fdelta%2Fcommit%2F9e7f3e9d070345c5f53b2d14313f0f1aee615169" target="_blank">了对使用 Google Dataproc 在 Google Compute Platform 上运行基准测试的支持</a>（除了现有的对 AWS 上 EMR 的支持之外）。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h4><strong><span><span><span><span><span style="color:#002638"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>社区扩展和增长的更新</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<p><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-47a44480a7c4dd734994f5366209bf7b97c.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="282" src="https://oscimg.oschina.net/oscnet/up-09b70eb254ee4ad4298046a3debbb53c976.png" width="500" referrerpolicy="no-referrer"></p> 
<p>公告称，<span><span><span style="color:#002638"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Delta Lake 将更加依赖于通过提供 ACID 事务以及在现有云数据存储之上统一流和批处理事务来为数据湖带来可靠性和改进的性能。通过使用最流行的计算引擎和技术构建连接器，Delta Lake 的吸引力将继续增加 —— 推动社区的更多增长，并在全球最具创新性和最大的企业中快速采用该技术。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><span><span><span style="color:#002638"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="282" src="https://static.oschina.net/uploads/space/2022/0811/180324_k0wX_4252687.png" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p>更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdelta.io%2Fblog%2F2022-08-02-delta-2-0-the-foundation-of-your-data-lake-is-open%2F" target="_blank">查看官方公告</a>。</p>
                                        </div>
                                      
</div>
            