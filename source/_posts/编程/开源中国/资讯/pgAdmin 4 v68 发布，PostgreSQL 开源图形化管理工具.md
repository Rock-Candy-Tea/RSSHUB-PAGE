
---
title: 'pgAdmin 4 v6.8 发布，PostgreSQL 开源图形化管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1726'
author: 开源中国
comments: false
date: Sat, 09 Apr 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1726'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0"><span style="color:#333333">pgAdmin 是 PostgreSQL 领先的开源图形化管理工具。pgAdmin 4 旨在满足新手和有经验的 Postgres 用户的需求，提供强大的图形界面，简化了数据库对象的创建、维护和使用。</span></p> 
<p style="margin-left:0"><span style="color:#333333">此版本包含了自 pgAdmin4 6.7 发布以来的一些错误修复和新功能：</span></p> 
<h4>New features</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7215" target="_blank">Issue #7215</a> - 在服务器活动会话视图中增加了<span style="color:#212529">事务</span>开始时间。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7249" target="_blank">Issue #7249</a> - <span style="color:#212529">添加了对 ERD 中唯一键的支持。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7257" target="_blank">Issue #7257</a> - <span style="color:#212529">支持在 OpenShift 下运行容器的备用 UID。</span></li> 
</ul> 
<h4>Housekeeping</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7132" target="_blank">Issue #7132</a> - <span style="color:#212529">React 中集合节点、Dashboard 和 SQL 面板的端口属性面板。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7149" target="_blank">Issue #7149</a> - <span style="color:#212529">React 的 </span>Port preferences 对话框</li> 
</ul> 
<h4>Bug fixes</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F4256" target="_blank">Issue #4256</a> - <span style="color:#212529">修复了数据库未显示用于撤销语句的 SQL 的问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F5836" target="_blank">Issue #5836</a> - <span style="color:#212529">添加新的 LDAP 身份验证配置参数，指示 LDAP 架构/服务器的区分大小写。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F6960" target="_blank">Issue #6960</a> - <span style="color:#212529">确保在缺少密码钥匙的情况下，弹出主密码对话框。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7059" target="_blank">Issue #7059</a> - <span style="color:#212529">修复了当身份验证源为 oauth2 时注销时显示错误的问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7176" target="_blank">Issue #7176</a> - <span style="color:#212529">修复了 browser tree state  未正确保留的问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7197" target="_blank">Issue #7197</a> - <span style="color:#212529">修复了修改主键时外键关系不更新的问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7216" target="_blank">Issue #7216</a> - 确保某些字段的值在集合节点的统计标签中被美化。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7221" target="_blank">Issue #7221</a> - <span style="color:#212529">确保依赖于扩展的对象不会显示在 Schema Diff 中。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7238" target="_blank">Issue #7238</a> - <span style="color:#212529">修复了即使在 ERD 中删除了引用的表，也不会删除外键的问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7239" target="_blank">Issue #7239</a> - <span style="color:#212529">修复了新添加的表在刷新时在表节点下不可见的问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7261" target="_blank">Issue #7261</a> - 纠正文档中的错别字。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7263" target="_blank">Issue #7263</a> - <span style="color:#212529">修复了模式差异问题，即当参数具有带逗号的默认值时，函数的差异 DDL 显示不正确。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7264" target="_blank">Issue #7264</a> - <span style="color:#212529">确保应在新连接对话框中选择正确的用户。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7265" target="_blank">Issue #7265</a> - <span style="color:#212529">修复了选项“null”未出现在外部表的 DDL 语句中的模式差异问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7267" target="_blank">Issue #7267</a> - <span style="color:#212529">修复了当用户通过 preferences 更改语言时显示意外错误消息的问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7269" target="_blank">Issue #7269</a> - <span style="color:#212529">确保 pgAdmin4 应该与最新的 jinja2 版本一起使用。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7275" target="_blank">Issue #7275</a> - <span style="color:#212529">修复了通过 ERD 工具创建表时出现的“无法读取未定义的属性”错误。</span></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.pgadmin.org%2Fdocs%2Fpgadmin4%2Flatest%2Frelease_notes_6_8.html" target="_blank">https://www.pgadmin.org/docs/pgadmin4/latest/release_notes_6_8.html</a></p>
                                        </div>
                                      
</div>
            