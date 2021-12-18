
---
title: 'pgAdmin 4 v6.3 发布，PostgreSQL 开源图形化管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5387'
author: 开源中国
comments: false
date: Sat, 18 Dec 2021 08:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5387'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">pgAdmin 是 PostgreSQL 领先的开源图形化管理工具。pgAdmin 4 旨在满足新手和有经验的 Postgres 用户的需求，提供强大的图形界面，简化了数据库对象的创建、维护和使用。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">这个版本的 pgAdmin 4 包括 31 个错误修复和新功能，本次更新中值得关注的变化包括：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">功能</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>增加了对两步认证（2FA）的支持以提高安全性 
  <ul style="margin-left:0; margin-right:0"> 
   <li>2FA 是登录网站或应用程序时使用的一个额外的安全层。使用 2FA，你必须用你的用户名和密码登录，并提供另一种只有你知道或可以访问的认证形式</li> 
  </ul> </li> 
 <li>增加了对禁用数据库服务器自动发现的支持 
  <ul style="margin-left:0; margin-right:0"> 
   <li>该功能允许你禁用数据库服务器的自动发现功能。在 config_local.py 或 config_distro.py 中设置<span> </span><code>AUTO_DISCOVER_SERVERS = False</code></li> 
  </ul> </li> 
 <li>在 macOS 上的 PostgreSQL 库和实用程序中包括 GSSAPI 支持</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Bugs/Housekeeping：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>升级 Flask 到第 2 版，用 Flask-Babel 替换 Flask-BabelEx</li> 
 <li>确保重命名服务器组时应保持排序顺序</li> 
 <li>确保在创建扩展时应允许用户设置其模式</li> 
 <li>修正了一个问题，即用户不能调试有时间戳参数的函数</li> 
 <li>修正了 Aggregate 的反向工程 SQL 错误的问题</li> 
 <li>更正了 PG14 中带有 Atomic 关键字的函数/程序的 SQL 定义</li> 
 <li>修正了 SQLite 数据库定义错误的问题，因为 USER_ID FK 引用的表 user_old 是不可用的</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpgadmin-4-v63-released-2373%2F" target="_blank">https://www.postgresql.org/about/news/pgadmin-4-v63-released-2373/</a></p>
                                        </div>
                                      
</div>
            