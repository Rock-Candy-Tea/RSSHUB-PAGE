
---
title: 'SQLite 3.38.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8366'
author: 开源中国
comments: false
date: Thu, 24 Feb 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8366'
---

<div>   
<div class="content">
                                                                                            <p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left">SQLite 3.38.0 现已发布。<span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">SQLite 是一个 C 实现的 SQL 数据库引擎，它的特点是小型、快速、自包含、高可靠性和功能齐全。SQLite 嵌入在所有手机和大多数计算机中，也捆绑在为数众多的其它应用中，是</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Findex.html" target="_blank">世界上使用量最大</a><span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">的数据库引擎。</span></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left"><strong>主要变化：</strong></p> 
<ul> 
 <li>添加<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fjson1.html%23jptr" target="_blank">了 -> 和 ->> 运算符</a>以便于处理 JSON。新的运算符与 MySQL 和 PostgreSQL 兼容。</li> 
 <li>JSON 函数现在是内置的。不再需要使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcompile.html%23enable_json1" target="_blank">-DSQLITE_ENABLE_JSON1</a> 编译时选项来启用 JSON 支持。默认情况下启用 JSON。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcompile.html%23omit_json" target="_blank">使用新的 -DSQLITE_OMIT_JSON</a> 编译时选项禁用 JSON 接口。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_datefunc.html" target="_blank">日期和时间功能</a>的增强： 
  <ul> 
   <li>添加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_datefunc.html%23uepch" target="_blank">unixepoch() 函数</a>。</li> 
   <li>添加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_datefunc.html%23automod" target="_blank">auto 修饰符</a>和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_datefunc.html%23jdmod" target="_blank">julianday 修饰符</a>。</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_corefunc.html%23printf" target="_blank">将 printf() SQL 函数</a>重命名为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_corefunc.html%23format" target="_blank">format()</a> 以获得更好的兼容性。保留原始 printf() 名称作为别名以实现向后兼容性。</li> 
 <li>添加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Ferrcode.html" target="_blank">sqlite3_error_offset()</a> 接口，有时可以帮助将 SQL error 定位到输入 SQL 文本中的特定字符，以便应用程序可以提供更好的错误消息。</li> 
 <li>增强了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fvtab.html" target="_blank">virtual tables </a>的接口如下： 
  <ul> 
   <li>添加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fvtab_distinct.html" target="_blank">sqlite3_vtab_distinct()</a> 接口。</li> 
   <li>添加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fvtab_rhs_value.html" target="_blank">sqlite3_vtab_rhs_value()</a> 接口。</li> 
   <li>添加了新的 operator 类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fc_index_constraint_eq.html" target="_blank">SQLITE_INDEX_CONSTRAINT_LIMIT</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fc_index_constraint_eq.html" target="_blank">SQLITE_INDEX_CONSTRAINT_OFFSET</a>。</li> 
   <li>添加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Fvtab_in.html" target="_blank">sqlite3_vtab_in()</a> 接口（及相关接口）以使 virtual table 能够一次处理所有 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_expr.html%23in_op" target="_blank">IN operator</a> 约束，而不是单独处理 IN operator 右侧的每个值。</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcli.html" target="_blank">CLI</a> enhancement： 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcli.html%23clmnr" target="_blank">Columnar output modes</a> 得到增强，可以正确处理嵌入在文本中的制表符和换行符。</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcli.html%23clmnr" target="_blank">在 Columnar output modes</a> 中添加了“--wrap N”、“--wordwrap on”和“--quote”等选项。</li> 
   <li>添加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcli.html%23qbox" target="_blank">.mode qbox</a> 别名。</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcli.html%23csv" target="_blank">.import 命令</a>自动消除列名的歧义。</li> 
   <li>使用新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fc3ref%2Ferrcode.html" target="_blank">sqlite3_error_offset()</a> 接口提供更好的错误消息。</li> 
  </ul> </li> 
 <li>Query planner enhancements： 
  <ul> 
   <li>使用 Bloom filter 来加速大型分析查询。</li> 
   <li>使用 balanced merge tree 来评估具有 ORDER BY 子句的 UNION 或 UNION ALL 复合 SELECT 语句。</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_altertable.html" target="_blank">ALTER TABLE</a> 语句更改为静默忽略 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fschematab.html" target="_blank">sqlite_schema 表中在</a>时不解析的条目。改变了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_altertable.html" target="_blank">ALTER TABLE</a> 语句，当 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fpragma.html%23pragma_writable_schema" target="_blank">PRAGMA writable_schema=ON</a> 时，静默忽略<span data-darkreader-inline-color style="--darkreader-inline-color:#e8e6e3; color:#000000"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fschematab.html" target="_blank">sqlite_schema table </a>中没有解析的条目。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">https://sqlite.org/changes.html</a></p>
                                        </div>
                                      
</div>
            