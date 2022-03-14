
---
title: 'SQLite 3.38.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7225'
author: 开源中国
comments: false
date: Mon, 14 Mar 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7225'
---

<div>   
<div class="content">
                                                                                            <p>SQLite 是一个 C 语言库，实现了一个小型、快速、独立、高可靠性、全功能的 SQL 数据库引擎。SQLite 是世界上使用最多的数据库引擎。SQLite 的源代码属于公共领域，每个人都可以免费使用，用于任何目的。</p> 
<p>SQLite 3.38.1 正式发布，更新内容如下：</p> 
<ul> 
 <li>修复了新的 Bloom 过滤器优化的问题，该问题可能会导致一些模糊的查询得到不正确的答案</li> 
 <li>修复日期和时间函数的 localtime 修饰符，以便它保留小数秒</li> 
 <li>修正 sqlite_offset SQL 函数，使其即使在极端情况下也能正确工作</li> 
 <li>修复了虚拟表的行值 IN 运算符约束，这样即使虚拟表的实现依赖于字节码来过滤不满足约束的行，它们也能正确工作</li> 
 <li>对 assert() 语句、测试用例和文档进行了小的修复</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsqlite.org%2Fchanges.html" target="_blank">https://sqlite.org/changes.html</a></p>
                                        </div>
                                      
</div>
            