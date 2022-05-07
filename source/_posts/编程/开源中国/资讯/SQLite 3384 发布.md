
---
title: 'SQLite 3.38.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2239'
author: 开源中国
comments: false
date: Sat, 07 May 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2239'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">SQLite 是一个 C 语言库，实现了一个小型、快速、独立、高可靠性、全功能的 SQL 数据库引擎。SQLite 是世界上使用最多的数据库引擎。SQLite 的源代码属于公共领域，每个人都可以免费使用，用于任何目的。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">SQLite 3.38.4 正式发布，更新内容如下：</p> 
<ul> 
 <li>修复 3.38.0 版本新增 Bloom filter 下拉优化的字节码问题，当下拉优化遇到 NULL key 时，字节码错误导致字节码引擎进入死循环。</li> 
 <li><span style="background-color:#ffffff; color:#444444">为 free() 修复 CLI 使用错误的分配器。</span></li> 
 <li><span style="background-color:#ffffff; color:#444444">将表达式的使用解析为对索引的引用时，在表达式的索引上保留 COLLATE operator</span><span style="background-color:#ffffff; color:#444444">。</span></li> 
</ul> 
<p><strong>Hashes</strong></p> 
<ul> 
 <li>SQLITE_SOURCE_ID: 2022-05-04 15:45:55 d402f49871152670a62f4f28cacb15d814f2c1644e9347ad7d258e562978e45e</li> 
 <li>SHA3-256 for sqlite3.c: e6a50effb021858c200e885664611ed3c5e949413ff2dca452ac7ee336b9de1d</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">https://sqlite.org/changes.html</a></p>
                                        </div>
                                      
</div>
            