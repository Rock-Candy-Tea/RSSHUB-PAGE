
---
title: 'SQLite 3.37.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7071'
author: 开源中国
comments: false
date: Sat, 01 Jan 2022 07:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7071'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">SQLite 3.37.1 现已发布。<span style="background-color:#ffffff; color:#333333">SQLite 是一个 C 实现的 SQL 数据库引擎，它的特点是小型、快速、自包含、高可靠性和功能齐全。SQLite 嵌入在所有手机和大多数计算机中，也捆绑在为数众多的其它应用中，是</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Findex.html" target="_blank">世界上使用量最大</a><span style="background-color:#ffffff; color:#333333">的数据库引擎。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">主要变化：</p> 
<ul> 
 <li>修复了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html%23version_3_35_0" target="_blank">3.35.0 版</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_upsert.html" target="_blank">UPSERT</a> 增强引入的错误，该错误可能导致为某些晦涩但有效的 SQL 生成不正确的字节码，从而可能导致 NULL-pointer dereference。</li> 
 <li>修复读取损坏的数据库文件时 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Ffts5.html" target="_blank">FTS5</a> 中可能发生的 OOB 读取问题。</li> 
 <li>改进了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fcli.html" target="_blank">CLI 中</a>-- safe 选项的稳健性。</li> 
 <li>对 assert() 语句和测试用例的其他小修复</li> 
</ul> 
<p><strong>Hashes:</strong></p> 
<ul> 
 <li>SQLITE_SOURCE_ID: 2021-12-30 15:30:28 378629bf2ea546f73eee84063c5358439a12f7300e433f18c9e1bddd948dea62</li> 
 <li>SHA3-256 for sqlite3.c: 915afb3f29c2d217ea0c283326a9df7d505e6c73b40236f0b33ded91f812d174</li> 
</ul> 
<p style="color:#000000; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">详情可查看变更说明</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            