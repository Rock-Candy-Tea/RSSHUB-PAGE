
---
title: 'pgAdmin 4 v5.3 发布，PostgreSQL 的开源图形化管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2118'
author: 开源中国
comments: false
date: Sat, 22 May 2021 09:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2118'
---

<div>   
<div class="content">
                                                                    
                                                        <p>pgAdmin 是 PostgreSQL 领先的开源图形化管理工具。pgAdmin 开发团队很高兴地宣布 pgAdmin 4 5.3 版本正式发布，这个版本包含了自 pgAdmin4 5.2 发布以来的一些错误修复和新功能。</p> 
<p>本次版本更新中值得注意的变化包括：</p> 
<p><strong>New features</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F5954" target="_blank">Issue #5954</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F5954" target="_blank">-</a> 增加了在数据输出窗口中按内容大小自动设置列宽的支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6158" target="_blank">Issue #6158</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6158" target="_blank">-</a> 新增了通过 Kerberos 认证连接 PostgreSQL 服务器的支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6397" target="_blank">Issue #6397</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6397" target="_blank">-</a> 在创建表和分区表时添加了“IF NOT EXISTS”子句，这在使用 ERD 工具时很方便。</li> 
</ul> 
<p><strong>Bug 修复</strong> </p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F4436" target="_blank">Issue #4436</a> - 修复了在属性对话框的 codemirror 中拖放对象不正确的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F5477" target="_blank">Issue #5477</a> - 增加了对 cache bust webpack chunk 文件的支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F5555" target="_blank">Issue #5555</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F5555" target="_blank">-</a> 修复了重复执行查询时数据显示顺序错误的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F5776" target="_blank">Issue #5776</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F5776" target="_blank">-</a> 确保在使用 SSPI 登录名连接到服务器时，它不应提示输入密码。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6329" target="_blank">Issue #6329</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6329" target="_blank">-</a>  修复了子分区表显示错误 SQL 的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6341" target="_blank">Issue #6341</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6341" target="_blank">-</a> 修复了 CSV 下载引用数字列的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6355" target="_blank">Issue #6355</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6355" target="_blank">-</a> 确保 pgAdmin 不允许打开拖动到其中的外部文件。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6377" target="_blank">Issue #6377</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6377" target="_blank">-</a> 修复了 schema diff 不能为列创建 DROP DEFAULT 语句的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6385" target="_blank">Issue #6385</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6385" target="_blank">-</a> 确保 Backup 和 Restore 应在共享服务器上正常工作。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6392" target="_blank">Issue #6392</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6392" target="_blank">-</a> 修复了 filter“Include/Exclude By Selection”不适用于空值的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6399" target="_blank">Issue #6399</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6399" target="_blank">-</a> 确保用户不应添加重复的面板。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6407" target="_blank">Issue #6407</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6407" target="_blank">-</a> 为 Advanced Server 增加了对创建嵌套表和可变数组类型的支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6408" target="_blank">Issue #6408</a> - 修复了从根目录外运行 setup.py 时出现的 ModuleNotFoundError。</li> 
 <li>......</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.pgadmin.org%2Fdocs%2Fpgadmin4%2Flatest%2Frelease_notes_5_3.html" target="_blank">https://www.pgadmin.org/docs/pgadmin4/latest/release_notes_5_3.html</a></p>
                                        </div>
                                      
</div>
            