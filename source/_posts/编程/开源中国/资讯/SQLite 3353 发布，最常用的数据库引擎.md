
---
title: 'SQLite 3.35.3 发布，最常用的数据库引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4893'
author: 开源中国
comments: false
date: Sun, 28 Mar 2021 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4893'
---

<div>   
<div class="content">
                                                                                            <p>SQLite 3.35.3 发布了，SQLite 是一个 C 实现的 SQL 数据库引擎，它的特点是小型、快速、自包含、高可靠性和功能齐全。SQLite 嵌入在所有手机和大多数计算机中，也捆绑在为数众多的其它应用中，是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Findex.html" target="_blank">世界上使用量最大</a>的数据库引擎。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>增强字节码引擎的 OP_OpenDup 操作码，以便即使复制的 cursor 本身来自 OP_OpenDup，它也可以工作。已修复  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2Fsrc%2Finfo%2Fbb8a9fd4a9b7fce5" target="_blank">ticket bb8a9fd4a9b7fce5</a>。由于最近进行了 MATERIALIZED hint enhancement，因此才发现此问题。</li> 
 <li>当实现相关的 common table expressions 时，需针对每个用例分别执行此操作，这是正确性所必需的。这解决了 MATERIALIZED hint enhancement 所引入的问题。</li> 
 <li>修复了 UNIX VFS 的文件名规范化的问题。</li> 
 <li>修复 CLI 中的“box”输出模式，以便它与返回一列或多列零列的语句一起使用（例如 PRAGMA incremental_vacuum）。</li> 
 <li>改进了 common table expressions 有问题所产生的错误信息。</li> 
 <li>修复一些错误的 assert() 语句。</li> 
 <li>对 SELECT 语句语法图进行修复，使 FROM 子句语法正确显示。</li> 
 <li>修复 EBCDIC 字符分类器，以便其将换行符理解为空格。</li> 
 <li>改进了（不受支持的）wholenumber 虚拟表扩展实现中的 xBestIndex 方法，以便说服 query planner 更好地完成工作，从而避免尝试实现具有无限行的表。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">https://sqlite.org/changes.html</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            