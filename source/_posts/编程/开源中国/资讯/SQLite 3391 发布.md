
---
title: 'SQLite 3.39.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4388'
author: 开源中国
comments: false
date: Sat, 16 Jul 2022 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4388'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SQLite 是一个 C 语言库，实现了一个小型、快速、独立、高可靠性、全功能的 SQL 数据库引擎。SQLite 是世界上使用最多的数据库引擎。SQLite 的源代码属于公共领域，每个人都可以免费使用，用于任何目的。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">SQLite 3.39.1 正式发布，更新内容如下：</p> 
<ul> 
 <li>修复使用包含复合 SELECT 的视图的查询的不正确结果，其中只有一个分支包含 RIGHT JOIN 并且视图不是包含该视图的查询的第一个 FROM 子句术语。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fforum%2Fforumpost%2F174afeae5734d42d" target="_blank">174afeae5734d42d</a>。</li> 
 <li>修复一些无害的编译器警告。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_altertable.html%23altertabrename" target="_blank">修复了 ALTER TABLE RENAME</a> 的一个长期存在的问题，该问题只有在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Flimit.html" target="_blank">sqlite3_limit</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fc_limit_attached.html%23sqlitelimitsqllength" target="_blank">SQLITE_LIMIT_SQL_LENGTH</a> ) 设置为非常小的值时才会出现。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Ffts3.html" target="_blank">修复了 FTS3</a> 中一个长期存在的问题，该问题只能在使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcompile.html%23enable_fts3_parenthesis" target="_blank">SQLITE_ENABLE_FTS3_PARENTHESIS</a> 编译时才会出现。</li> 
 <li>修复了构建问题，使其在同时提供<span style="color:#000000"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcompile.html%23debug" target="_blank">SQLITE_DEBUG</a> 和<span style="color:#000000"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcompile.html%23omit_windowfunc" target="_blank">SQLITE_OMIT_WINDOWFUNC</a><span style="color:#000000"><span> </span></span>两个编译时选项时能够正常工作。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_expr.html%23regexp" target="_blank">修复 REGEXP</a> 扩展的初始前缀优化，即使前缀包含需要 3 字节 UTF8 编码的字符，它也能正常工作。</li> 
 <li>增强 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fstmt.html" target="_blank">sqlite_stmt</a> 虚拟表，使其缓冲所有输出。</li> 
</ul> 
<p><strong>Hashes</strong></p> 
<ul> 
 <li>SQLITE_SOURCE_ID: 2022-07-13 19:41:41 7c16541a0efb3985578181171c9f2bb3fdc4bad6a2ec85c6e31ab96f3eff201f</li> 
 <li>SHA3-256 for sqlite3.c: 6d13fcf1c31133da541d1eb8a83552d746f39b81a0657bd4077fed0221749511</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">https://sqlite.org/changes.html</a></p>
                                        </div>
                                      
</div>
            