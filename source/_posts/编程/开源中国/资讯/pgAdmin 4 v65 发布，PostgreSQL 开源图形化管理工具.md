
---
title: 'pgAdmin 4 v6.5 发布，PostgreSQL 开源图形化管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6826'
author: 开源中国
comments: false
date: Mon, 14 Feb 2022 07:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6826'
---

<div>   
<div class="content">
                                                                                            <p>pgAdmin 是 PostgreSQL 领先的开源图形化管理工具。pgAdmin 4 旨在满足新手和有经验的 Postgres 用户的需求，提供强大的图形界面，简化了数据库对象的创建、维护和使用。</p> 
<p>这个版本包含了自 pgAdmin4 6.4 发布以来的一些错误修复和新功能：</p> 
<h3>新功能：</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7139" target="_blank">Issue #7139</a> - 增加了在外部网络浏览器中打开 SQL 帮助、对话框帮助和在线帮助的支持。</li> 
</ul> 
<h3>Housekeeping</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7016" target="_blank">Issue #7016</a> - 移植依赖关系、统计面板到 React</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7017" target="_blank">Issue #7017</a> - 移植导入/导出对话框到 React</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7163" target="_blank">Issue #7163</a> - 将菜单 “Disconnect Server” 重命名为 “Disconnect from server”</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6916" target="_blank">Issue #6916</a> - 在运行时增加了禁用 GPU 硬件加速的标志</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7035" target="_blank">Issue #7035</a> - 修复了在初始连接数据库服务器时，连接保持打开的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7085" target="_blank">Issue #7085</a> - 确保在创建多个分区级别时分区表应该正确可见</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7086" target="_blank">Issue #7086</a> - 更正 "Add named restore point" 的文档</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7100" target="_blank">Issue #7100</a> - 修正当滚动序列时，浏览器树会消失的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7109" target="_blank">Issue #7109</a> - 在文件选择对话框中，所有目录的大小为空白</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7110" target="_blank">Issue #7110</a> - 确保光标应集中在实用程序对话框的第一个选项上</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7118" target="_blank">Issue #7118</a> - 确保 JSON 文件应从存储管理器中正确下载</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7126" target="_blank">Issue #7126</a> - 修复了 F2 功能键删除浏览器面板内容的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7127" target="_blank">Issue #7127</a> - 在服务器对话框中添加了对 Hostname 的验证</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7135" target="_blank">Issue #7135</a> - 强制执行安装程序运行的最低 Windows 版本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7136" target="_blank">Issue #7136</a> - 修复了查询工具显示不正确标签的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7142" target="_blank">Issue #7142</a> - 修复了数据库创建/修改后显示警告信息的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7146" target="_blank">Issue #7146</a> - 修复了 Schema Diff 工具中的事件触发器比较问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7150" target="_blank">Issue #7150</a> - 修复了在 Desktop 模式下上传 CSV 时出现的错误问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7151" target="_blank">Issue #7151</a> - 修复了还原对话框中的数值错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7154" target="_blank">Issue #7154</a> - 确保在打开查询工具和重启 pgAdmin 时，布局不应该被重置</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.pgadmin.org%2Fdocs%2Fpgadmin4%2F6.5%2Frelease_notes_6_5.html" target="_blank">https://www.pgadmin.org/docs/pgadmin4/6.5/release_notes_6_5.html</a></p>
                                        </div>
                                      
</div>
            