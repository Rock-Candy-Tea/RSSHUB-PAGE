
---
title: 'SQLite 3.39.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2853'
author: 开源中国
comments: false
date: Sun, 26 Jun 2022 23:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2853'
---

<div>   
<div class="content">
                                                                                            <p>SQLite 是一个 C 语言库，实现了一个小型、快速、独立、高可靠性、全功能的 SQL 数据库引擎。SQLite 是世界上使用最多的数据库引擎。SQLite 的源代码属于公共领域，每个人都可以免费使用，用于任何目的。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">SQLite 3.39.0 正式发布，更新内容如下：</p> 
<ul> 
 <li>添加了对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_select.html%23rjoin" target="_blank">RIGHT 和 FULL OUTER JOIN</a> 的支持。</li> 
 <li>添加新的二进制比较运算符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_expr.html%23isdf" target="_blank">IS NOT DISTINCT FROM</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_expr.html%23isdf" target="_blank">IS DISTINCT FROM</a> ，它们分别等效于 IS 和 IS NOT，以与 PostgreSQL 和 SQL 标准兼容。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fvtab_distinct.html" target="_blank">从 sqlite3_vtab_distinct()</a> 接口添加一个新的 return code（值为“3”），表示一个查询同时具有 DISTINCT 和 ORDER BY 子句。</li> 
 <li>添加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fdb_name.html" target="_blank">sqlite3_db_name()</a> 接口。</li> 
 <li>unix os 接口解析数据库文件名中的所有符号链接，以便在打开文件之前为数据库创建一个规范名称。</li> 
 <li>推迟 materializing views，直到实际需要 materialization，从而避免在 materialization 从未被使用时进行不必要的工作。</li> 
 <li>现在，任何聚合查询都允许使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_select.html" target="_blank">SELECT 语句</a>的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_select.html%23resultset" target="_blank">HAVING 子句</a>，即使是没有 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_select.html%23resultset" target="_blank">GROUP BY 子句</a>的查询。</li> 
 <li>一些<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcpu.html%23microopt" target="_blank">微小的优化</a>共同将 CPU 周期减少了约 2.3%。</li> 
</ul> 
<p><strong style="color:#333333">Hashes</strong></p> 
<ul> 
 <li>SQLITE_SOURCE_ID: 2022-06-25 14:57:57 14e166f40dbfa6e055543f8301525f2ca2e96a02a57269818b9e69e162e98918</li> 
 <li>SHA3-256 for sqlite3.c: d9c439cacad5e4992d0d25989cfd27a4c4f59a3183c97873bc03f0ad1aa78b7a</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">https://sqlite.org/changes.html</a></p>
                                        </div>
                                      
</div>
            