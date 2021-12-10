
---
title: 'Flink Hudi 0.10.0 发布，多项重要更新，稳定性大幅提升'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1210/141313_j7Cu_5430600.png'
author: 开源中国
comments: false
date: Fri, 10 Dec 2021 06:21:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1210/141313_j7Cu_5430600.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#595959">随着云数仓技术的不断成熟，数据湖俨然已成为当下最热门的技术之一，而 Apache Hudi 是当下最具竞争力的数据湖格式之一：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:#595959">拥有最活跃的开源社区之一，周活跃 PR 一直维持在<span> </span><strong>50+</strong><span> </span>水平；</span></li> 
 <li><span style="color:#595959">拥有最活跃的国内用户群之一，目前的 Apache Hudi 钉钉群用户已超过<span> </span><strong>2200+</strong>，国内各大厂商都已经布局 Apache Hudi 生态。</span></li> 
</ul> 
<p><span style="color:#595959">Apache Hudi 的活跃度得益于其出色的 file format 设计和丰富的事物语义支持：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:#595959">类 LSM 的 file format 布局很好的适配了近实时更新场景，解决了超大数据集更新的痛点；</span></li> 
 <li><span style="color:#595959">Hudi 的事物层语义在目前的湖存储中是极其成熟和丰富的，基本所有的数据治理都可以自动化完成：<span>compaction、rollback、cleaning、clustering。</span></span></li> 
</ul> 
<h2>Flink On Hudi</h2> 
<p>Apache Hudi 的 table format 对流计算友好的特性使得 Flink On Hudi 成为 Apache Hudi 项目最值得探索和挖掘的方向之一，Flink 不仅为 Hudi 解锁了超大数据流的实时更新能力、更添加了流式消费和计算的能力，让端到端近实时 ETL 得以在低成本的文件存储上轻松实现。</p> 
<p>Flink On Hudi 项目在 2020 年 11 月立项，至今已迭代了三个版本，从第一个版本开始人气和活跃度就一直高涨。5 月份组建的 Apache Hudi 钉钉群截止目前半年的时间，已经有超过 2200+ 用户，并且活跃度一直排在 Flink 用户群的前列。</p> 
<p>Flink On Hudi 已成为部署 Apache Hudi 项目的首选方案，国内主要云厂商：阿里云、华为云、腾讯云，国外的 AWS 都已集成 Flink On Hudi；国内的大型互联网公司：头条、快手、B站 以及传统企业：顺丰、海康等均有 Flink On Hudi 的生产实践，具钉钉群的跟踪回访等不完全统计，至少超过 50+ 国内公司在生产上使用 Flink On Hudi，Uber 公司更将 Flink On Hudi 作为 2022 年的重点方向在推进 ！</p> 
<p>Flink On Hudi 的开发者生态也非常活跃，目前国内有阿里云、华为云、头条、B站的同学持续贡献，Uber 公司和 AWS 更专门投入人力来对接 Flink On Hudi。</p> 
<h2>版本 Highlights</h2> 
<p>0.10.0 版本经过社区用户的千锤百炼，贡献了多项重要的 fix，更有核心读写能力的大幅增强，解锁了多个新场景，Flink On Hudi 侧的更新重点梳理如下：</p> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>修复对象存储上极端 case 流读数据丢失的问题 [HUDI-2548]；</li> 
 <li>修复全量+增量同步偶发的数据重复 [HUDI-2686]；</li> 
 <li>修复 changelog 模式下无法正确处理 DELETE 消息 [HUDI-2798]；</li> 
 <li>修复在线压缩的内存泄漏问题 [HUDI-2715]。</li> 
</ul> 
<p><strong>新特性</strong></p> 
<ul> 
 <li>支持增量读取；</li> 
 <li>支持 batch 更新；</li> 
 <li>新增 Append 模式写入，同时支持小文件合并；</li> 
 <li>支持 metadata table。</li> 
</ul> 
<p><strong>功能增强</strong></p> 
<ul> 
 <li>写入性能大幅提升：优化写入内存、优化了小文件策略(更加均衡，无碎片文件)、优化了 write task 和 coordinator 的交互；</li> 
 <li>流读语义增强：新增参数 earliest，提升从最早消费性能、支持参数跳过压缩读取，解决读取重复问题；</li> 
 <li>在线压缩策略增强：新增 eager failover + rollback，压缩顺序改为从最早开始；</li> 
 <li>优化事件顺序语义：支持处理序，支持事件序自动推导。</li> 
</ul> 
<p>下面挑一些重点内容为大家详细介绍：</p> 
<p><strong>小文件优化</strong></p> 
<p>Flink On Hudi 写入流程大致分为以下几个组件：</p> 
<p><img alt height="189" src="https://static.oschina.net/uploads/space/2021/1210/141313_j7Cu_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><strong><span style="color:#595959">row data to hoodie：</span></strong><span style="color:#595959">负责将 table 的数据结构转成 HoodieRecord；</span></p> </li> 
 <li> <p><strong><span style="color:#595959">bucket assigner：</span></strong><span style="color:#595959">负责新的文件 bucket (file group) 分配；</span></p> </li> 
 <li> <p><strong><span style="color:#595959">write task：</span></strong><span style="color:#595959">负责将数据写入文件存储；</span></p> </li> 
 <li> <p><strong><span style="color:#595959">coordinator：</span></strong><span style="color:#595959">负责写 trasaction 的发起和 commit；</span></p> </li> 
 <li> <p><strong><span style="color:#595959">cleaner：</span></strong><span style="color:#595959">负责数据清理。</span></p> </li> 
</ul> 
<p>其中的 bucket assigner 负责了文件 file group 的分配，也是小文件分配策略的核心组件。0.10.0 版本的每个 bucket assign task 持有一个 bucket assigner，每个 bucket assigner 独立管理自己的一组 file group 分组：</p> 
<p><img alt height="176" src="https://static.oschina.net/uploads/space/2021/1210/141401_7Pw6_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<p>在写入 INSERT 数据的时候，bucket assigner 会扫描文件视图，查看当前管理的 file group 中哪些属于小文件范畴，如果 file group 被判定为小文件，则会继续追加写入。比如上图中 task-1 会继续往 FG-1、FG-2 中追加 80MB 和 60MB 的数据。</p> 
<p>为了避免过度的写放大，当可写入的 buffer 过小时会忽略，比如上图中 FG-3、FG-4、FG-5 虽然是小文件，但是不会往文件中追加写。task-2 会新开一个 file group 写入。</p> 
<p><strong>全局文件视图</strong></p> 
<p>0.10.0 版本将原本 write task 端的文件视图统一挪到 JobManager，JobManager 启动之后会使用 Javaline 本地启动一个 web server，提供全局文件视图的访问代理。Write task 通过发送 http 请求和 web server 交互，拿到当前写入的 file group 视图。</p> 
<p>Web server 避免了重复的文件系统视图加载，极大的节省了内存开销。</p> 
<p><img alt height="254" src="https://static.oschina.net/uploads/space/2021/1210/141708_yOrV_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<p><strong>流读能力增强</strong></p> 
<p>0.10.0 版本新增了从最早消费数据的参数，通过指定 read.start-commit 为 earliest 即可流读全量 + 增量数据，值得一提的是，当从 earliest 开始消费时，第一次的 file split 抓取会走直接扫描文件视图的方式，在开启 metadata table 功能后，文件的扫描效率会大幅度提升；之后的增量读取部分会扫描增量的 metadata，以便快速轻量地获取增量的文件讯息。</p> 
<p><img alt height="274" src="https://static.oschina.net/uploads/space/2021/1210/141523_Fv35_5430600.png" width="400" referrerpolicy="no-referrer"></p> 
<p><strong>新增处理顺序</strong></p> 
<p><span style="color:#595959">Apache Hudi 的消息合并大体分为两块：增量数据内部合并、历史数据和增量数据合并。消息之间合并通过 <span><code>write.precombine.field</code></span></span><span style="color:#595959"> 字段来判断版本新旧，如下图中标注蓝色方块的消息为合并后被选中的消息。</span></p> 
<p><img alt height="278" src="https://static.oschina.net/uploads/space/2021/1210/141900_eIWq_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#595959">0.10.0 版本可以不指定 </span><span style="background-color:#ffffff; color:#595959"><code>write.precombine.field</code> </span><span style="background-color:#ffffff; color:#595959">字段，此时使用处理顺序：即后来的消息比较新，对应上图紫色部分被选中的消息。</span></p> 
<p><strong>Metadata Table</strong></p> 
<p>Metadata table 是 0.7.0 Hudi 引入的功能，目的是在查询端减少 DFS 的访问，类似于文件 listings 和 partitions 信息直接通过 metadata table 查询获取。Metadata 在 0.10.0 版本得到大幅加强，Flink 端也支持了 该功能。</p> 
<p>新版的 metadata table 为同步更新模型，当完成一次成功的数据写入之后，coordinator 会先同步抽取文件列表、partiiton 列表等信息写入 metadata table 然后再写 event log 到 timeline (即 metadata 文件)。</p> 
<p>Metadata table 的基本文件格式为 avro log，avro log 中的文件编码区别于正常的 MOR data log 文件，是由高效的 HFile data block 构成，这样做的好处是自持更高效率的 kv 查找。同时 metadata table 的 avro log 支持直接压缩成 HFile 文件，进一步优化查询效率。</p> 
<p><img alt height="335" src="https://static.oschina.net/uploads/space/2021/1210/142000_B3Eo_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<h2>总结和展望</h2> 
<p><span style="color:#595959">在短短的半年时间，Flink On Hudi 至今已积攒了数量庞大的用户群体。积极的用户反馈和丰富的用户场景不断打磨 Flink On Hudi 的易用性和成熟度，使得 Flink On Hudi 项目以非常高效的形式快速迭代。通过和头部公司如头条、B 站等共建的形式，Flink On Hudi 形成了非常良性的开发者用户群。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#595959">Flink On Hudi 是 Apache Hudi 社区接下来两个大版本主要的发力方向，在未来规划中，主要有三点：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span style="color:#595959">完善端到端 streaming ETL 场景 支持原生的 change log、支持维表查询、支持更轻量的去重场景；</span></p> </li> 
 <li> <p><span style="color:#595959">Streaming 查询优化 record-level 索引，二级索引，独立的文件索引；</span></p> </li> 
 <li> <p><span style="color:#595959">Batch 查询优化 z-ordering、data skipping。</span></p> </li> 
</ul> 
<h2><strong><span style="color:#595959">致谢</span></strong></h2> 
<p><span style="color:#595959">最后感谢 Flink Hudi 活跃的社区用户以及开发者，正是有你们一路相伴，Flink On Hudi 才能高效率地演化和迭代；也因为有你们，Flink On Hudi 在实时数据湖方向的探索和实践逐渐成为行业先驱，且越来越成熟 ~</span></p>
                                        </div>
                                      
</div>
            