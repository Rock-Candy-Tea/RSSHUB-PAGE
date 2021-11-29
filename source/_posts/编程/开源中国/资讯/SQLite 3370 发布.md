
---
title: 'SQLite 3.37.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5603'
author: 开源中国
comments: false
date: Mon, 29 Nov 2021 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5603'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SQLite 3.37.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Freleaselog%2F3_37_0.html" target="_blank">已发布</a>。<span style="background-color:#ffffff; color:#333333">SQLite 是一个 C 实现的 SQL 数据库引擎，它的特点是小型、快速、自包含、高可靠性和功能齐全。SQLite 嵌入在所有手机和大多数计算机中，也捆绑在为数众多的其它应用中，是</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Findex.html" target="_blank">世界上使用量最大</a><span style="background-color:#ffffff; color:#333333">的数据库引擎。</span></p> 
<p>主要变化：</p> 
<ol> 
 <li>新增的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fstricttables.html" target="_blank">STRICT 表</a>为喜爱这种类型的开发者提供了一种规范的数据类型管理方式。</li> 
 <li>当添加包含 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Flang_createtable.html%23ckconst" target="_blank">CHECK 约束</a>的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fgencol.html" target="_blank">列</a>或包含 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Flang_createtable.html%23notnullconst" target="_blank">NOT NULL 约束</a>的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fgencol.html" target="_blank">生成列时</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Flang_altertable.html%23altertabaddcol" target="_blank">ALTER TABLE ADD COLUMN</a> 现在会根据数据库中预先存在的行检查新约束，并且只有在没有违反约束时才会继续</li> 
 <li>添加<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fpragma.html%23pragma_table_list" target="_blank">PRAGMA table_list</a><span> </span>语句</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fcli.html" target="_blank">CLI</a><span> 功能增强</span>： 
  <ol style="list-style-type:lower-alpha"> 
   <li>添加<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fcli.html%23dotconn" target="_blank">.connection</a><span> </span>命令，<span style="color:#000000">允许 CLI 同时保持多个数据库连接打开</span></li> 
   <li>添加<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fcli.html%23safemode" target="_blank">--safe 命令行选项</a>，以禁用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fcli.html%23dotcmd" target="_blank">dot-commands</a> 和 SQL 语句，这些<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fcli.html%23dotcmd" target="_blank">命令</a>和 SQL 语句可能会导致超出命令行上指定的单个数据库文件的副作用</li> 
   <li><span style="color:#000000">读取跨越多行的 SQL 语句时的性能改进</span></li> 
  </ol> </li> 
 <li>添加<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fc3ref%2Fautovacuum_pages.html" target="_blank">sqlite3_autovacuum_pages()</a><span> 接口</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fc3ref%2Fdeserialize.html" target="_blank">sqlite3_deserialize()</a><span> </span>对 TEMP 数据库不起作用，也从来没有起过作用。此限制现在已经在文档中指出</li> 
 <li>如果删除子查询和视图的 ORDER BY 子句不会改变查询的语义，则查询计划器现在会省略这些子句</li> 
 <li>对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fseries.html" target="_blank">generate_series</a> 表值函数 (table-valued) 的扩展进行了修改，使第一个参数 ("START") 成为必需。这样做是为了演示如何编写带有必要参数的表值函数。使用 -DZERO_ARGUMENT_GENERATE_SERIES 编译时选项可以使用传统的行为</li> 
 <li>添加新的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fc3ref%2Fchanges.html" target="_blank">sqlite3_changes64()</a><span> </span>和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fc3ref%2Ftotal_changes.html" target="_blank">sqlite3_total_changes64()</a><span> </span>接口</li> 
 <li>为<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fc3ref%2Fopen.html" target="_blank">sqlite3_open_v2()</a> 添加<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fc3ref%2Fc_open_autoproxy.html" target="_blank">SQLITE_OPEN_EXRESCODE</a><span> </span>flag 选项</li> 
</ol> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">详情查看变更说明</a>。</p>
                                        </div>
                                      
</div>
            