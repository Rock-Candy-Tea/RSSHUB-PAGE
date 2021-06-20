
---
title: 'SQLite 3.36.0 发布，最常用的数据库引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7730'
author: 开源中国
comments: false
date: Sun, 20 Jun 2021 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7730'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SQLite 3.36.0 发布了，SQLite 是一个 C 实现的 SQL 数据库引擎，它的特点是小型、快速、自包含、高可靠性和功能齐全。SQLite 嵌入在所有手机和大多数计算机中，也捆绑在为数众多的其它应用中，是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Findex.html" target="_blank">世界上使用量最大</a>的数据库引擎。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Feqp.html" target="_blank">EXPLAIN QUERY PLAN</a> 输出的改进，使其更容易理解。</li> 
 <li>token 开始的字节顺序标记被跳过，就像它们是空白的一样。</li> 
 <li>在试图访问一个 VIEW 或子查询的 rowid 时，会产生一个错误。以前，一个 VIEW 的 rowid 是不确定的，而且经常是 NULL。-DSQLITE_ALLOW_ROWID_IN_VIEW 编译时选项可用于恢复需要它的应用程序的传统行为。</li> 
 <li>sqlite3_deserialize() 和 sqlite3_serialize() 接口现在被默认启用。不再需要 -DSQLITE_ENABLE_DESERIALIZE 编译时选项了。取而代之的是一个新的 -DSQLITE_OMIT_DESERIALIZE 编译时选项来省略这些接口。</li> 
 <li>"memdb"VFS 现在允许同一进程中的多个数据库连接共享同一个内存数据库，只要数据库名称以"/"开头。</li> 
 <li>取消了 EXISTS-to-IN 优化（SQLite 3.35.0 变更日志中的第 8b 项），因为发现它降低了查询速度，而不是加快了查询速度。</li> 
 <li>改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Foptoverview.html%23constprop" target="_blank">constant-propagation </a>优化，使其适用于非连接查询。</li> 
 <li>REGEXP 扩展现在包含在 CLI 构建中。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">https://sqlite.org/changes.html</a> </p>
                                        </div>
                                      
</div>
            