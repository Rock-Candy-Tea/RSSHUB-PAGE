
---
title: 'ClickHouse 可视化工具 CH Visualize Release 1.10.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5675'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 00:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5675'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><span><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>DBM 1.10.0 版本发布！</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FEdurtIO%2Fdbm%2Fissues%2F54" target="_blank">重构</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.10.0-20220127%2F%23refactor" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <p style="margin-left:-0.8rem; margin-right:-0.6rem"><span><span><span style="background-color:var(--md-admonition-bg-color)"><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:rgba(68, 138, 255, 0.1)"><strong><span>核</span></strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <p><span><span><span style="background-color:var(--md-admonition-bg-color)"><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>我们正在放弃 VUE 并使用 Angular 和 Typescript 进行重构</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
</div> 
<ul style="list-style-type:disc"> 
 <li>重构查询模块</li> 
 <li>重构数据源模块</li> 
 <li>重构磁盘模块</li> 
 <li>重构数据库模块</li> 
 <li>重构表模块</li> 
 <li>重构列模块</li> 
 <li>重构监控模块</li> 
 <li>重构工具模块</li> 
 <li>重构设置模块</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>增强<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.10.0-20220127%2F%23enhancement" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>将查询历史拆分为新页面</li> 
 <li>拆分应用程序设置到新页面</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>优化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.10.0-20220127%2F%23optimize" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>优化表操作逻辑</li> 
 <li>优化列操作逻辑</li> 
 <li>优化多窗口编辑器</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>漏洞<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.10.0-20220127%2F%23bug" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>修复编辑器无法格式化 SQL 的问题</li> 
 <li>修复快速查询表名显示问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FEdurtIO%2Fdbm%2Fissues%2F84" target="_blank">issues-84</a></li> 
 <li>修复了右键菜单无法跟随所选文本的问题</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>删除（暂时）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.10.0-20220127%2F%23remove-temporarily" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <p style="margin-left:-0.8rem; margin-right:-0.6rem"><span><span><span style="background-color:var(--md-admonition-bg-color)"><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:rgba(68, 138, 255, 0.1)"><strong><span>为什么？</span></strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <p><span><span><span style="background-color:var(--md-admonition-bg-color)"><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>由于以下功能存在一些问题，我们将暂时重写并重新上线</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
</div> 
<ul style="list-style-type:disc"> 
 <li>数据迁移功能</li> 
 <li>添加列，修改列</li> 
 <li>列详细信息</li> 
</ul>
                                        </div>
                                      
</div>
            