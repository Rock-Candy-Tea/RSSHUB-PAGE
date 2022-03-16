
---
title: 'pgAdmin 4 v6.7 发布，PostgreSQL 开源图形化管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8877'
author: 开源中国
comments: false
date: Wed, 16 Mar 2022 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8877'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">pgAdmin 是 PostgreSQL 领先的开源图形化管理工具。pgAdmin 4 旨在满足新手和有经验的 Postgres 用户的需求，提供强大的图形界面，简化了数据库对象的创建、维护和使用。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">此版本包含了自 pgAdmin4 6.6 发布以来的一些错误修复和新功能：</span></p> 
<div> 
 <blockquote> 
  <p style="color:#212529; text-align:left"><strong>Note</strong></p> 
  <p style="color:#212529; text-align:left"><strong>Security Release</strong></p> 
  <p><span style="color:#212529">请注意，此版本包含一个安全更新，以解决在服务器模式下运行 pgAdmin 时用户可以将文件上传到其存储目录之外的目录的问题。</span></p> 
  <p><span style="color:#212529">在服务器模式下运行 pgAdmin 的用户，包括基于标准容器的发行版，应尽快升级到此版本。</span></p> 
  <p><span style="color:#212529">此问题不会影响在桌面模式下运行的用户。</span></p> 
 </blockquote> 
</div> 
<p style="text-align:left"><span style="color:#000000"><strong>错误修复</strong></span></p> 
<blockquote> 
 <div>
  <span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7220" target="_blank">Issue #7220</a> - 修复了当表的外键值不同时不会生成差异 SQL 的模式差异问题。</span></span></span>
 </div> 
 <div>
  <span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7228" target="_blank">Issue #7228</a> - 修复了模式差异问题，其中字符串分隔符“_$PGADMIN$_”对于相同的用户映射可见。</span></span></span>
 </div> 
 <div>
  <span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7230" target="_blank">Issue #7230</a> - 修复了 pgAdmin 4 需要约 75 秒才能在初始屏幕上显示“Starting pgAdmin”文本的问题。</span></span></span>
 </div> 
 <div>
  <span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredmine.postgresql.org%2Fissues%2F7233" target="_blank">Issue #7233</a> - 确保上传路径是存储目录的子目录。</span></span></span>
 </div> 
</blockquote> 
<p> 更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.pgadmin.org%2Fdocs%2Fpgadmin4%2Flatest%2Frelease_notes_6_7.html" target="_blank">https://www.pgadmin.org/docs/pgadmin4/latest/release_notes_6_7.html</a></p>
                                        </div>
                                      
</div>
            