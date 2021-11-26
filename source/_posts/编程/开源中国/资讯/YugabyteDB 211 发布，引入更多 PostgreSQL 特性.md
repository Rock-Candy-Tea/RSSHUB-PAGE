
---
title: 'YugabyteDB 2.11 发布，引入更多 PostgreSQL 特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7393'
author: 开源中国
comments: false
date: Fri, 26 Nov 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7393'
---

<div>   
<div class="content">
                                                                    
                                                        <p>YugabyteDB 2.11 为数据库带来了广泛使用的 PostgreSQL 特性，包括外部数据包装器（FDW）、GIN 索引、排序（Collation）支持、追随者读取、改进的空间放大和并发事务的 read-committed 隔离级别。</p> 
<p>外部数据包装器允许 PostgreSQL 数据库将远程数据库中的表视为本地可用的表。这使开发人员能够毫不费力地编写查询，访问外部数据源中的数据，就好像它们是来自 PostgreSQL 数据库中的表一样。对 FDW 的支持允许开发人员编写一个访问外部云原生数据库中数据的 JOIN 查询。</p> 
<p>Read Committed 事务隔离：PostgreSQL 使用一种叫做多版本并发控制的技术来隔离并发事务并确保数据一致性。SQL-92 标准定义了四个级别的事务隔离；可序列化、可重复读取、read committed和 read uncommitted。</p> 
<p>YugabyteDB 此前已经支持两个最严格的隔离级别，可序列化和快照（类似于可重复读取）。YugabyteDB 2.11 增加了对 read committed 事务隔离的支持，这也是 PostgreSQL 的默认隔离级别。</p> 
<p><strong>YugabyteDB 2.11 中其他值得注意的内容：</strong></p> 
<ul> 
 <li>GIN 索引：这些加速了表内多列的文本搜索</li> 
 <li>排序：这提供了对数据的排序顺序和字符分类行为的精细控制</li> 
 <li>支持分析：这允许你收集关于数据库表的内容的统计数据，从而实现查询的高效执行计划。</li> 
 <li>支持 Dapper 和 Mybatis ORMs：这些简化了 .Net 和 Java 应用程序的开发</li> 
 <li>支持 pg_stat_monitor：这是一个流行的 PostgreSQL 的查询性能监控工具</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.yugabyte.com%2Fannouncing-yugabytedb-2-11%2F" target="_blank">https://blog.yugabyte.com/announcing-yugabytedb-2-11/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            