
---
title: 'SQLite 3.39.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2848'
author: 开源中国
comments: false
date: Wed, 07 Sep 2022 07:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2848'
---

<div>   
<div class="content">
                                                                                            <p>SQLite 是一个 C 语言库，实现了一个小型、快速、独立、高可靠性、全功能的 SQL 数据库引擎。SQLite 是世界上使用最多的数据库引擎。SQLite 的源代码属于公共领域，每个人都可以免费使用，用于任何目的。</p> 
<p>SQLite 3.39.3 已正式发布，更新内容如下：</p> 
<ol> 
 <li value="1">支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_select.html%23rjoin" target="_blank">RIGHT and FULL OUTER JOIN</a></li> 
 <li>添加新的二进制比较运算符<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_expr.html%23isdf" target="_blank">IS NOT DISTINCT FROM</a><span> 和 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_expr.html%23isdf" target="_blank">IS DISTINCT FROM</a>，两者分别等同于 IS 和 IS NOT, 兼容 PostgreSQL 和 SQL 标准</li> 
 <li>从<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fvtab_distinct.html" target="_blank">sqlite3_vtab_distinct()</a><span> 接口添加了新的返回代码</span> (value "3")，表示一个同时包含 DISTINCT 和 ORDER BY 子句的查询</li> 
 <li>新增<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fdb_name.html" target="_blank">sqlite3_db_name()</a><span> 接口</span></li> 
 <li>unix os 接口解析了数据库文件名中的所有符号链接，以便在文件打开之前为数据库创建一个规范的名称。如果 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fc_open_autoproxy.html" target="_blank">SQLITE_OPEN_NOFOLLOW</a><span> </span>flag 与<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fopen.html" target="_blank">sqlite3_open_v2()</a> 或类似的接口一起使用，如果路径中的任何元素是一个符号链接，打开将失败。</li> 
 <li>任何聚合查询都允许使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_select.html" target="_blank">SELECT 语句</a>的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_select.html%23resultset" target="_blank">HAVING 子句</a>，即使是没有 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_select.html%23resultset" target="_blank">GROUP BY 子句</a>的查询</li> 
 <li>许多<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcpu.html%23microopt" target="_blank">细小优化</a>共同将 CPU 周期减少了约 2.3%</li> 
</ol> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Freleaselog%2F3_39_3.html" target="_blank">详情点此查看</a>。</p>
                                        </div>
                                      
</div>
            