
---
title: 'pgAdmin 4 v5.1 发布，PostgreSQL 的开源图形化管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8153'
author: 开源中国
comments: false
date: Thu, 25 Mar 2021 23:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8153'
---

<div>   
<div class="content">
                                                                                            <p>pgAdmin 是 PostgreSQL 领先的开源图形化管理工具。pgAdmin 开发团队很高兴地宣布 pgAdmin 4 5.1 版本正式发布。这个版本的 pgAdmin 4 包括众多的错误修复，并加入了一些新功能。</p> 
<p>本次版本更新中值得注意的变化包括：</p> 
<h3>特性:</h3> 
<ul> 
 <li> <p>在运行时使用键盘快捷键的缩放选项</p> <p>该功能包括缩放比例（放大、缩小、实际大小）选项以及进入/退出全屏模式。pgAdmin 已经在菜单中添加了选项，以及可以使用键盘快捷键，用户可以更方便的执行所需的操作；</p> </li> 
 <li> <p>当检查一个组角色时，显示组角色成员的登录角色；</p> </li> 
 <li> <p>在导入服务器中添加了“--replace”选项，用新导入的服务器替换服务器列表；</p> </li> 
 <li> <p>使容器分发版成为支持 x86_64 和 Arm64 的多架构构建；</p> </li> 
 <li> <p>将'Kerberos'作为 Python wheel 中的一个可选功能，以避免系统默认安装 MIT Kerberos。</p> </li> 
</ul> 
<h3>Bugs 修复</h3> 
<ul> 
 <li>修正了一个在目录中挂起符号链接会导致选择文件对话框崩溃的问题；</li> 
 <li>使 "保存数据更改"图标更加直观；</li> 
 <li>确保编辑单元格数据时自动选择单元格内容；</li> 
 <li>确保 SQLformatter 不应该添加额外的选项卡，并正确格式化 SQL；</li> 
 <li>确保如果"Use spaces?"设置为"false"时，SQL 格式化器不应该使用制表符大小；</li> 
 <li>修正了数据库编码设置为 SQL_ASCII 且列名为 ASCII 字符时的编码问题；</li> 
 <li>确保如果用户拥有 'pg_signal_backend' 角色，用户应该能够从 Dashboard 中终止会话；</li> 
 <li>确保 PGADMIN_DEFAULT_EMAIL 在初始化容器部署时看起来很正常；</li> 
 <li>修正了一个当打开任何 SQL 文件时，用户无法在查询工具中更改连接的问题；</li> 
 <li>修正了一个在视图数据中复制/粘贴行时，会粘贴错误的布尔类型值的问题；</li> 
 <li>确保大多数屏幕阅读器都能访问切换按钮。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.pgadmin.org%2Fdocs%2Fpgadmin4%2F5.1%2Frelease_notes_5_1.html" target="_blank">https://www.pgadmin.org/docs/pgadmin4/5.1/release_notes_5_1.html</a></p>
                                        </div>
                                      
</div>
            