
---
title: 'CrateDB 4.5.1 发布，分布式 SQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3316'
author: 开源中国
comments: false
date: Tue, 04 May 2021 23:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3316'
---

<div>   
<div class="content">
                                                                                            <p>CrateDB 4.5.1 现已发布。Crate 是一个开源的大规模的可伸缩的数据存储系统，无需任何系统管理需求。提供强大的搜索功能。用于存储各种表格数据、非结构化数据和二进制对象。并可通过 SQL 进行检索。易于安装和使用，支持高可用性和实时大规模并行访问和处理。Crate 特别适合用于 Docker 环境中。</p> 
<p><strong>注意</strong></p> 
<p>如果要升级群集，则必须先运行 CrateDB 4.0.2 或更高版本，然后才能升级到 4.5.1。官方建议在升级到 4.5.1 之前先升级到最新的 4.4 版本。支持从 4.4.0+ 到 4.5.1的滚动升级。升级之前，建议先<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrate.io%2Fdocs%2Fcrate%2Freference%2Fen%2Flatest%2Fadmin%2Fsnapshots.html" target="_blank">备份数据</a>。</p> 
<p><strong>Fixes</strong></p> 
<ul> 
 <li> <p>修复了以下问题：如果在 sub-query 的选择列表中使用了表函数，但在 parent relation 的输出中没有使用，则可能导致对虚拟表的查询返回不正确的结果。举例：</p> <pre>SELECT name FROM (SELECT name, unnest(tags) FROM metrics) m;</pre> </li> 
 <li> <p>将捆绑的 JDK 更新为 16.0.1 + 9</p> </li> 
 <li> <p>修复了以下问题：如果在一个有多个类型重载的函数中作为参数使用，会导致有长度限制的 varchar 类型的列被错误地转换为另一种类型。</p> </li> 
 <li> <p>修复了一个问题，该问题导致 ALTER TABLE ADD COLUMN 语句从同一表中的现有列中删除约束，如 analyzers 或 NOT NULL。</p> </li> 
 <li> <p>允许以常规用户身份执行<code>CREATE TABLE .. AS</code><code>DDL</code><code>DQL</code> ，并具有对 target schema 的 DDL 权限以及对 source relations 的 DQL 权限。</p> </li> 
 <li> <p>改变了发送给 PostgreSQL 客户端的 RowDescription 信息，以避免 JDBC 客户端在每次访问结果集的 MetaData 信息时触发对 pg_catalog 模式表的查询。</p> </li> 
 <li> <p>修复了<code>crate-node</code>辅助程序，以在 Linux 上使用捆绑的 Java 运行时。</p> </li> 
</ul> 
<p>发布说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrate.io%2Fdocs%2Fcrate%2Freference%2Fen%2F4.5%2Fappendices%2Frelease-notes%2F4.5.1.html" target="_blank">https://crate.io/docs/crate/reference/en/4.5/appendices/release-notes/4.5.1.html</a></p>
                                        </div>
                                      
</div>
            