
---
title: 'SQLite 3.37.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4586'
author: 开源中国
comments: false
date: Tue, 11 Jan 2022 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4586'
---

<div>   
<div class="content">
                                                                                            <p>SQLite 3.37.2 现已发布。<span style="background-color:#ffffff; color:#333333">SQLite 是一个 C 实现的 SQL 数据库引擎，它的特点是小型、快速、自包含、高可靠性和功能齐全。SQLite 嵌入在所有手机和大多数计算机中，也捆绑在为数众多的其它应用中，是</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Findex.html" target="_blank">世界上使用量最大</a><span style="background-color:#ffffff; color:#333333">的数据库引擎。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>主要变化：</strong></p> 
<ul> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html%23version_3_35_0" target="_blank">版本 3.35.0</a> (2021-03-12) 中引入<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fforum%2Fforumpost%2Fb03d86f9516cb3a2" target="_blank">的一个 bug</a>， 如果在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fpragma.html%23pragma_temp_store" target="_blank">PRAGMA temp_store=MEMORY</a> 模式下回滚 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Flang_savepoint.html" target="_blank">SAVEPOINT</a> 并进行其他更改，然后外部事务提交，则<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fhowtocorrupt.html%23svptbug" target="_blank">可能导致数据库损坏</a>。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fsrc%2Finfo%2F73c2b50211d3ae26" target="_blank">Check-in 73c2b50211d3ae26</a></li> 
 <li>修复了 ON DELETE CASCADE 和 ON UPDATE CASCADE 的一个长期存在的问题，在该问题中，用于实现级联更改的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fopcode.html" target="_blank">字节码</a>缓存在本地 DDL 更改后没有被重置。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fsrc%2Finfo%2F5232c9777fe4fb13" target="_blank">Check-in 5232c9777fe4fb13</a></li> 
 <li>其他的一些小修复，应该不会影响生产构建。</li> 
</ul> 
<p><span style="color:#000000"><strong>Hashes:</strong></span></p> 
<ul> 
 <li>SQLITE_SOURCE_ID: 2022-01-06 13:25:41 872ba256cbf61d9290b571c0e6d82a20c224ca3ad82971edc46b29818d5d17a0</li> 
 <li>SHA3-256 for sqlite3.c: 1bb01c382295cba85ec4685cedc52a7477cdae71cc37f1ad0f48719a17af1e1e</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">详情可查看变更说明</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            