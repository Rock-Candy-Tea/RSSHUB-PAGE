
---
title: 'Bytebase 1.0.4 发布，数据库 Schema 变更管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4b4eed9ecbe82b4182ec89aa68c59a11c17.png'
author: 开源中国
comments: false
date: Sat, 30 Apr 2022 07:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4b4eed9ecbe82b4182ec89aa68c59a11c17.png'
---

<div>   
<div class="content">
                                                                                            <p>Bytebase 1.0.4 已发布，Bytebase 是一款聚焦在 Database schema change and version control 的工具。它主打的是在应用研发过程中变更数据库数据结构 (schema) 的这个场景，主要面向的人群是研发工程师和 DBA。</p> 
<hr> 
<p><span style="background-color:#ffffff; color:#333333">新版本主要变化</span></p> 
<p><strong>支持通过</strong><strong style="color:#222222"><span><code><strong> --pg </strong></code></span></strong><strong>选项启动 Bytebase</strong></p> 
<p>用户可以使用外部 PostgreSQL 数据库来保存 Bytebase 本身的元数据。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4b4eed9ecbe82b4182ec89aa68c59a11c17.png" referrerpolicy="no-referrer"></p> 
<p><strong>新功能</strong></p> 
<ul style="list-style-type:disc; margin-left:16px; margin-right:16px"> 
 <li> <p style="margin-left:.5em; margin-right:0; text-align:left"><span><strong>bb<span> </span></strong><strong>命令行支持<span> </span></strong></span><code><span><strong>--dsn</strong></span></code><span><strong><span> </span>选项</strong></span></p> <p><span>命令行支持用数据源名称 (DSN) 连接数据库，比如<span> </span></span><code><span>--dsn mysql://user:passwd@host:port/dbname?opt1=val1&opt2=val2</span></code></p> </li> 
 <li> <p style="margin-left:.5em; margin-right:0; text-align:left"><span><strong>新增 bb 命令行的安装脚本</strong></span></p> <p><span>用户可以通过以下命令安装命令 </span><code><span>/bin/bash -c "$(curl -fsSL<span> </span></span></code><code><span>https://raw.githubusercontent.com/bytebase/bytebase/HEAD/scripts/install_bb.sh)"</span></code><span>。从原先需要手动在 GitHub Release 上下载、解压、移动到可执行文件目录的多个步骤简化为一条命令完成安装。</span></p> </li> 
 <li> <p style="margin-left:.5em; margin-right:0; text-align:left"><span><strong>新增 SQL 语句</strong><strong>工作表</strong><strong>管理页面</strong></span></p> <p><span>引入 SQL 语句工作表管理页面，用户可以通过表格的形式浏览所有项目中的工作表。</span></p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-54653c0f3cb3b484062612f40b8edb7157c.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:16px; margin-right:16px"> 
 <li> <p style="margin-left:.5em; margin-right:0; text-align:left"><span><strong>Admin 页面上显示项目清单</strong></span></p> <p><span>Workspace 当中角色为 Owner 和 DBA 的用户可以在设置 (Settings) 页面中浏览所有的项目。</span></p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f0fffdc18bca6ab537ae17c2afe05dd81b9.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:16px; margin-right:16px"> 
 <li> <p style="margin-left:.5em; margin-right:0; text-align:left"><span><strong>增添 /healthz 健康检查端</strong></span></p> </li> 
</ul> 
<p><span><strong>改进</strong></span></p> 
<ul style="list-style-type:disc; margin-left:16px; margin-right:16px"> 
 <li> <p><span>直接在页面上显示</span><code><span><span> </span>Visit Default Project<span> </span></span></code><span>按键。"Default Project" 是用于保持数据库与数据库实例同步的特殊项目。用户原本只能通过特地访问 Default Project 将数据库导入自己的项目中。</span></p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8c6e6933871ccd901a5f98d57d76ddb41a7.png" referrerpolicy="no-referrer"></p> 
<p><strong><span>安装及升级</span></strong></p> 
<ul> 
 <li><span>参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%23installation" target="_blank">https://github.com/bytebase/bytebase#installation</a>。如果是从之前版本升级，获取新版本后，重新启动升级即可。</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">来源：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FNeLDknpxYoxyqhTsP-j68A" target="_blank">Bytebase</a></p>
                                        </div>
                                      
</div>
            