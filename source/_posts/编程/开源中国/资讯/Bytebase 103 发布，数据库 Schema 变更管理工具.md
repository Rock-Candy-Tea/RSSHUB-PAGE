
---
title: 'Bytebase 1.0.3 发布，数据库 Schema 变更管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0420/071037_oe5T_2720166.gif'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 07:11:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0420/071037_oe5T_2720166.gif'
---

<div>   
<div class="content">
                                                                                            <p>Bytebase 1.0.3 已发布，Bytebase 是一款聚焦在 Database schema change and version control 的工具。它主打的是在应用研发过程中变更数据库数据结构 (schema) 的这个场景，主要面向的人群是研发工程师和 DBA。</p> 
<hr> 
<p>新版本主要变化</p> 
<p><span><strong><strong>发布 MySQL Database Review Guide</strong></strong></span></p> 
<p><span>Database Review Guide 罗列了 Schema 变更审核中的各种规则，从 Table, Column, Index 的命名规则，到需要指定 WHERE 语句。目前提供了预制的 MySQL 开发环境和生产环境的规则模版，DBA 可以基于模版再手动配置，生成图片，作为公司内部规则的参考。同时开发团队还在:</span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span>补充更多的规则，也欢迎 DBA 们直接到 https://github.com/bytebase/bytebase/issues 提建议</span></p> </li> 
 <li> <p><span>把这些规则集成到 Bytebase 产品中去，自动检测 SQL 语句是否符合规则</span></p> </li> 
</ul> 
<p><span>目前只支持 MySQL，之后会添加对于 PostgreSQL 的支持</span></p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0420/071037_oe5T_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><span><strong><span>新功能</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li style="text-align:left"> <p><span>在运行时开关 Debug 模式</span></p> </li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2022/0420/071050_ZtOT_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>只有 OWNER 和 DBA 可以开关 Debug 模式</p> 
<p>当 Debug 模式开启时，Bytebase 会在 web 控制台展示内部的报错信息，同时也会输出更详细的日志。之前，用户可以在 Bytebase 启动时传入 '--debug' 来开启。现在我们则可以在运行时动态设置。Debug 模式是一个全局设置，会影响所有的用户，所以只有 OWNER 和 DBA 可以设置。通常只有在需要诊断问题时才会临时开启。</p> 
<p><span><strong><span>改进</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li style="text-align:left"> <p><span>【SQL编辑器】在 EXPLAIN SELECT 的基础上，支持 EXPLAIN 其他类型的语句，例如 EXPLAIN INSERT</span></p> </li> 
</ul> 
<p><span><strong><span>社区</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span>发布版本中，预编译了多种可执行文件格式：Bytebase 主应用和 CLI 的可执行文件将会发布在 GitHub 发布页面。目前已经支持 Linux 和 Darwin，以及 x86_64 和 arm64</span></p> </li> 
</ul> 
<p><span><strong><span>安装及升级</span></strong></span></p> 
<p><span>参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%23installation" target="_blank">https://github.com/bytebase/bytebase#installation</a>。如果是从之前版本升级，获取新版本后，重新启动升级即可。</span></p> 
<p>来源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F13fe4GOGprFtO2cKsAru7Q" target="_blank">Bytebase</a></p>
                                        </div>
                                      
</div>
            