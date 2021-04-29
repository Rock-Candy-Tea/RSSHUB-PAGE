
---
title: 'Vitess 10 发布，MySQL 数据库集群水平扩展系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=876'
author: 开源中国
comments: false
date: Thu, 29 Apr 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=876'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Vitess 10 发布了。Vitess 是一个分布式 MySQL 工具集，它可以自动分片存储 MySQL 数据表，将单个 SQL 查询改写为分布式发送到多个 MySQL Server 上，支持行缓存（比 MySQL 本身缓存效率高）与复制容错等。</p> 
<p>此版本主要新特性包括：</p> 
<p><strong>Major Themes</strong></p> 
<p>在这个版本中，Vitess 的维护者仍继续专注于兼容性。它仍然是 Vitess 成为 MySQL 生态系统一部分的最关键的组成部分。开发团队也已经开始着手进行基准测试和性能优化。这些改进让其对 Vitess 的哪些方面可以在性能上有所提高有了清晰的认识。</p> 
<p><strong>兼容性（MySQL、框架）</strong></p> 
<p>随着 V10.0 的发布，Vitess(unsharded) 通过了 Ruby on Rails 框架的所有自动化端到端测试。现在，即使你使用得不是 Rails，这些改进也可能使你受益。接下来，开发团队还计划继续增加对更多框架的测试。</p> 
<p><strong>Migration</strong></p> 
<ul> 
 <li>Freno-style throttling 已添加到 VReplication 工作流程中。source 和 target tablets 都可以根据 corresponding shards 的 replication lag 来 throttled。</li> 
 <li>通过新的安装和迁移命令，你可以从另一个 Vitess cluster 导入数据。</li> 
 <li>该版本还包括还包括 VReplication V2 用户指令的改进指标、错误修复和微调。</li> 
</ul> 
<p><strong>Schema Management</strong></p> 
<p>Online DDL 在第 9 版的基础上继续发展，一些新的和值得注意的内容有：</p> 
<ul> 
 <li>改进的 SQL 语法</li> 
 <li>通过<code>@@ddl_strategy='online'</code> VReplication 引入基于 VReplication 的迁移是 resharding、materialized views、MoveTables 等背后的基础机制。现在，它可以运行架构迁移</li> 
 <li>Revertible Online DDL：对已完成的迁移进行无损、online revert</li> 
 <li>Declarative schema 更改</li> 
</ul> 
<p><strong>性能优化</strong></p> 
<ul> 
 <li>为 query plans 添加了一个新的、性能更好的缓存实现。新的缓存使用 LFU 驱逐算法，使其对 pollution 有更强的适应性，所以它在 pathological cases 下表现得特别好（比如大量插入活动数据库），同时在正常操作中具有更快的响应时间和更好的命中率。</li> 
 <li>Vitess SQL Parser 的性能在解析速度和减少内存分配方面都得到了极大的提高。这将减少 vtgate 实例的 CPU 使用率，缩短查询时间，并减少 GC 流失。如果依赖 Vites 解析器的第三方应用程序升级到最新版本，它们也将获得这些好处-外部 API 基本上保持不变。</li> 
 <li>Vitess 在 SQL 语法树上执行的许多 AST 操作已经过重新设计，因此除非绝对必要，否则它们不会分配内存。这将导致 vtgate 进程的内存使用量明显减少，尤其是在 busy Vitess clusters 中。</li> 
 <li>大多数改进是在 vtgate 的 CPU 和内存使用方面。开发团队正在努力对延迟和吞吐量的影响进行基准测试，一旦有结果就会公布。</li> 
</ul> 
<p><strong>User Interface</strong></p> 
<p>Vitess 10.0 引入了一个实验性的 multi-cluster admin API 和 Web UI，称为 VTAdmin。部署 vtadmin-api 和 vtadmin-web 组件是完全自愿的。值得注意的是，VTAdmin 依赖于新的 VtctldServer API，所以你必须在你的 vtctlds 上运行新的 grpc-vtctld 服务才能使用它。</p> 
<p><strong>Benchmarking</strong></p> 
<p>为了确保 Vitess 为用户提供高性能，自 Vitess 9.0 以来，开发团队一直在改进基准测试和性能监控技术。项目<code>arewefastyet</code>是这些技术的核心，目前仍在开发中，其目标是自动测量和观察 Vitess 的性能。</p> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvitess.io%2Fblog%2F2021-04-27-announcing-vitess-10%2F" target="_blank">https://vitess.io/blog/2021-04-27-announcing-vitess-10/</a></p>
                                        </div>
                                      
</div>
            