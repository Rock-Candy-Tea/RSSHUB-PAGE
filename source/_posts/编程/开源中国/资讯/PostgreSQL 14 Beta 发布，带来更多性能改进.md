
---
title: 'PostgreSQL 14 Beta 发布，带来更多性能改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7717'
author: 开源中国
comments: false
date: Sat, 22 May 2021 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7717'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PostgreSQL 14 首个 Beta 版本发布，PostgreSQL 的开发者持续改进这个流行的开源 SQL 数据库服务器，使其性能最大化。</p> 
<h3>Beta 版本时间表</h3> 
<p>这是 14 版的第一个测试版。PostgreSQL 项目将根据测试的需要发布多个测试版，在测试版之后还会有一个或多个候选版，直到 2021 年底的最终版本。</p> 
<h3>性能</h3> 
<p>PostgreSQL 14 Beta 延续了最近几个版本的趋势，为各种规模的工作负载提供性能优势。</p> 
<p>这个版本对有大量数据库连接的 PostgreSQL 系统的事务吞吐量有明显的改进，不管它们是处于活动状态还是空闲状态。</p> 
<p>PostgreSQL 14 在减少 B-tree 索引开销方面还具有其他优势，包括减少索引频繁更新的表的膨胀。 GiST 索引现在可以在其构建过程中对数据进行预排序，从而可以更快地创建索引并缩小索引。SP-GiST 索引现在支持覆盖索引，该索引使用户可以通过 INCLUDE 子句向索引添加其他不可搜索的列。</p> 
<p>在 PostgreSQL 14 中对查询的并行性有许多改进。除了对并行顺序扫描的整体性能的改进之外，PL/pgSQL 中的 RETURN QUERY 指令现在可以执行具有并行性的查询。REFRESH MATERIALIZED VIEW 现在也可以使用查询并行性。</p> 
<p>PostgreSQL 14 还引入了在使用外部数据封装器查询远程数据库时利用查询并行性的能力。PostgreSQL 外部数据封装器 postgres_fdw 在 PostgreSQL 14 中设置 async_capable 标志时增加了对这一功能的支持。postgres_fdw 还支持批量插入，并可以使用 IMPORT FOREIGN SCHEMA 导入表分区，现在可以在外部表中执行 TRUNCATE。</p> 
<p>这个版本对分区系统也有一些改进，包括在只有几个分区受到影响的表上更新或删除行时的性能提升。</p> 
<p>在上一版本中引入的增量排序，现在可以被 PostgreSQL 14 中的窗口函数所使用。这个新版本为扩展的统计数据增加了更多的功能，现在可以应用于表达式。</p> 
<p>PostgreSQL 一直支持对其 "超大数据" 列的压缩（即 TOAST 系统），但这个版本增加了可以选择使用 LZ4 压缩列的功能。</p> 
<h3>数据类型+SQL</h3> 
<p>在现有的范围类型支持的基础上，PostgreSQL 14 增加了新的多范围类型，让你指定一个非连续范围的有序列表，例如：</p> 
<pre><code>SELECT datemultirange( daterange('2021-07-01', '2021-07-31'), daterange('2021-09-01', '2021-09-30'), daterange('2021-11-01', '2021-11-30'), daterange('2022-01-01', '2022-01-31'), daterange('2022-03-01', '2022-04-07') ) 
</code></pre> 
<p>PostgreSQL 14 现在增加了一个通用的下标框架，用于检索嵌套对象中的信息。例如，你现在可以使用下标语法检索 JSONB 数据类型中的嵌套信息，例如。</p> 
<pre><code>SELECT ('&#123; "this": &#123; "now": &#123; "works": "in postgres 14!" &#125;&#125;&#125;':jsonb) ['this']['now']['works']。
</code></pre> 
<p>PostgreSQL 14 还增加了对存储过程中 OUT 参数的支持，并允许 GROUP BY 子句使用 DISTINCT 关键字来删除重复的 GROUPING SET 组合。</p> 
<p>对于递归的普通表表达式（WITH 查询），PostgreSQL 14 增加了 SEARCH 和 CYCLE 的语法便利，以分别帮助进行排序和循环检测。</p> 
<p>在 PostgreSQL 14 中还有一个新的 date_bin 函数，可以将时间戳与指定的间隔对齐，这种技术被称为 "binning"。</p> 
<h3>Administration</h3> 
<p>PostgreSQL 14 对 VACUUM 进行了大量改进，并针对索引进行了优化。Autovacuum 现在可以分析分区表，并可以将行数信息传播到父表。在 ANALYZE 中也有性能提升，可以用 maintain_io_concurrency 参数来控制。</p> 
<p>PostgreSQL 14 在可以监控的信息方面有很多改进，包括使用 pg_stat_progress_copy 视图跟踪 COPY 的进展。这个版本允许你从 pg_stat_wal 视图跟踪 WAL 活动，并从 pg_stat_replication_slots 视图检查复制槽的统计数据。</p> 
<p>在 PostgreSQL 14中，有几个新的参数可以帮助管理连接。这些参数包括 idle_session_timeout，它可以在指定时间后关闭空闲的连接，以及 client_connection_check_interval 参数，它可以让 PostgreSQL 在客户端断开连接时取消长期运行的查询。</p> 
<p>REINDEX 命令现在可以处理一个分区表的所有子索引，PostgreSQL 14 增加了 pg_amcheck 工具来帮助检查数据损坏。</p> 
<h3>复制和恢复</h3> 
<p>PostgreSQL 14 为逻辑复制增加了许多性能优势，包括将正在进行的事务流向订阅者而不是等待它们完成。ALTER SUBSCRIPTION 使用新的 ADD/DROP PUBLICATION 语法，使添加/删除变得更容易。</p> 
<p>在 PostgreSQL 14 中，对 PostgreSQL 在崩溃恢复时的启动方式进行了性能改进，你现在可以在一个处于待机模式的 PostgreSQL 实例上使用 pg_rewind。</p> 
<h3>安全性</h3> 
<p>PostgreSQL 14 增加了通过使用 pg_read_all_data 和 pg_write_all_data 预定义角色，分别给予用户在表/视图/序列上的通用 "只读" 和 "只写" 权限的能力。</p> 
<p>这个版本也默认在新的 PostgreSQL 实例上使用 SCRAM-SHA-256 进行密码管理。此外， pg_hba.conf 中的 clientcert 参数现在必须使用 verify-ca 或 verify-full 的值，而不是传统的值。</p> 
<p>PostgreSQL 14 可以在 pg_hba.conf 文件中使用证书的 "区分名称"（DN）来进行基于证书的认证，并使用 clientname=DN 参数。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpostgresql-14-beta-1-released-2213%2F" target="_blank">https://www.postgresql.org/about/news/postgresql-14-beta-1-released-2213/</a></p>
                                        </div>
                                      
</div>
            