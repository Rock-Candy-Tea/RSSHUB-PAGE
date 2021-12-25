
---
title: 'Bytebase 0.10.0 发布，数据库 Schema 变更管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-723050fc18990b9c743828a5e14135a8623.png'
author: 开源中国
comments: false
date: Sat, 25 Dec 2021 07:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-723050fc18990b9c743828a5e14135a8623.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%2Freleases%2Ftag%2F0.10.0" target="_blank">Bytebase 0.10.0 已发布</a>，Bytebase 是一款聚焦在 Database schema change and version control 的工具。它主打的是在应用研发过程中变更数据库数据结构 (schema) 的这个场景，主要面向的人群是研发工程师和 DBA。</p> 
<h2 style="margin-left:8px; margin-right:8px; text-align:left"><span><strong>新功能</strong></span></h2> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span><strong><span>支持中文</span></strong></span></p> </li> 
</ul> 
<p><span>Bytebase 现在正式支持简体中文。用户可以通过仪表盘右上角的下拉菜单进行切换。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-723050fc18990b9c743828a5e14135a8623.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span><strong><span>指定任务最早允许的执行时间</span></strong></span></p> </li> 
</ul> 
<p><span>用户可以指定每项任务的最早开始时间，Bytebase 会确保任务只有在指定时间之后才会被执行。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-90d0c999b7a50a507068df3c3698e5928c1.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-80459b6b26e89d52a04bd9450ec4b44d79d.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:8px; margin-right:8px; text-align:left"><span><strong>改进</strong></span></h2> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0"><span><strong><span>记录用户对 SQL statement 的变更</span></strong></span></p> </li> 
</ul> 
<p><span>用户对 SQL statement 作出的每项变更都将被记录，并且通过站内信的形式推送给相关人员。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-248e0770105fe37b8d1cad37e2602049f9a.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0"><span><strong><span>叠加窗口查看检查的详细状态</span></strong></span></p> </li> 
</ul> 
<p><span>当审核人打开了同意执行工单的模态窗时，可以通过打开一个新的叠加的模态窗来查看检查的详细状态。</span></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1225/072200_FDex_2720166.gif" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:8px; margin-right:8px; text-align:left"><span><strong>Bug 修复</strong></span></h2> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span><strong><span>Postgres CREATE DATABASE不能在交易块内运行</span></strong></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span><strong><span>修复MySQL表结构里的自增初始值导致的 Schema Drift 问题</span></strong></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><strong><span>过期时自动刷新GitLab访问令牌</span></strong></span></p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px">更新说明</h2> 
<ul style="margin-left:8px; margin-right:8px"> 
 <li> <p><span>安装方式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%23installation" target="_blank">https://github.com/bytebase/bytebase#installation</a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            