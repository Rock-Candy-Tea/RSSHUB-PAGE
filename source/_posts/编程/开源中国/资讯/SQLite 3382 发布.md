
---
title: 'SQLite 3.38.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3347'
author: 开源中国
comments: false
date: Mon, 28 Mar 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3347'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SQLite 是一个 C 语言库，实现了一个小型、快速、独立、高可靠性、全功能的 SQL 数据库引擎。SQLite 是世界上使用最多的数据库引擎。SQLite 的源代码属于公共领域，每个人都可以免费使用，用于任何目的。</p> 
<p>SQLite 3.38.2 正式发布，更新内容如下：</p> 
<ul> 
 <li>修复了另一个用户所发现的新 Bloom 过滤器优化问题</li> 
 <li>不允许在 assert() 中使用 #ifdef</li> 
 <li>强化 unix 和 Windows VFSes 的 xShmLock 方法，使其在 SHM 文件未打开时不会被调用</li> 
 <li>在 btree 模块的 sqlite3BtreeInsert() 函数中加强对损坏的数据库的保护</li> 
 <li>修复 zipfile 扩展，使其知道零长度的 BLOB 返回一个 NULL 指针</li> 
 <li>运行 sqlite3_declare_vtab() 时禁用触发器编码</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">https://sqlite.org/changes.html</a></p>
                                        </div>
                                      
</div>
            