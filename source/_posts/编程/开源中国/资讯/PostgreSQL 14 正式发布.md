
---
title: 'PostgreSQL 14 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4532'
author: 开源中国
comments: false
date: Fri, 01 Oct 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4532'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PostgreSQL 14 现已发布。该版本继续在复杂数据类型上添加创新，包括更方便的 JSON 访问和对非连续数据范围的支持，并且增加了 PostgreSQL 在提高高性能和分布式数据工作负载方面的趋势，在连接并发性、高写入工作负载、查询并行性和逻辑复制方面取得了进步。</p> 
<h4>JSON 访问和 multirange 数据类型</h4> 
<p>PostgreSQL 14 现在允许使用下标访问 JSON 数据，例如 SELECT ('&#123; "postgres": &#123; "release": 14 &#125;&#125;'::jsonb)['postgres']['release']。这使 PostgreSQL 与从 JSON 数据检索信息时普遍认可的语法保持一致。并且新增的下标框架一般可以扩展到其他嵌套数据结构，本次发布的 hstore 数据类型也同样适用。</p> 
<p>Range 类型现在通过引入"multirange" 数据类型支持非连续范围。一个 multirange 数据是不重叠范围的有序列表，它使开发人员可以编写更简单的查询来处理复杂的范围序列。 PostgreSQL 原生的范围类型（​​日期、时间、数字）支持多范围，其他数据类型可以扩展以使用多范围支持。</p> 
<h4>重型工作负载的性能改进</h4> 
<p>PostgreSQL 14 通过减少频繁更新索引的表上的索引膨胀来继续改进 B 树索引管理，使用许多连接的工作负载显着提升吞吐量，引入了将查询管道传输到数据库的功能，这可以显着提高高延迟连接或具有许多小写（插入/更新/删除）操作的工作负载的性能。</p> 
<h4>分布式工作负载增强</h4> 
<p>使用逻辑复制时，PostgreSQL 14 现在可以将正在进行的事务流式传输给订阅者。而用于处理跨 PostgreSQL 和其他数据库的联合工作负载的外部数据包装器，现在可以利用 PostgreSQL 14 中的查询并行性。此外，postgres_fdw 现在可以在外部表上批量插入数据并使用 IMPORT FOREIGN SCHEMA 指令导入表分区。</p> 
<h4>管理和可监测性</h4> 
<p>PostgreSQL 14 添加了一个 "紧急模式"，并且现在可以配置 TOAST 系统的压缩，同时为 TOAST 列添加了 LZ4 压缩，而保留对 pglz 压缩的支持。此外，该版本添加了几个新特性来帮助监控和观察，包括跟踪 COPY 命令的进度、预写日志 (WAL) 活动和复制槽统计信息的能力。启用 compute_query_id 可让进行跟踪查询。</p> 
<h4>SQL 性能、一致性和便利性</h4> 
<p>此版本包括对 PostgreSQL 查询并行性支持的多项改进，包括更好的并行顺序扫描性能、PL/pgSQL 在使用 RETURN QUERY 命令时执行并行查询的能力，以及启用 REFRESH MATERIALIZED VIEW 来执行并行查询。此外，使用嵌套循环连接的查询可能会通过添加的额外缓存获得性能优势。同时，扩展统计现在可以用于表达式，存储过程允许在代码块中进行事务控制，并可以使用 OUT 参数返回数据。</p> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpostgresql-14-released-2318%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            