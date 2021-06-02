
---
title: 'HeidiSQL 11.3 发布，数据库客户端软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8b3e90243cea10b7ffdeb135794cc602889.png'
author: 开源中国
comments: false
date: Wed, 02 Jun 2021 07:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8b3e90243cea10b7ffdeb135794cc602889.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>HeidiSQL 11.3 现已发布。HeidiSQL 是一个功能非常强大的数据库客户端软件，采用 Delphi 开发，支持 Windows 操作系统。支持 MySQL、MariaDB、Percona Server 和微软的 SQL Server。</p> 
<p>此版本具体更新内容如下：</p> 
<p><strong>Still need 32bit support?</strong></p> 
<ul> 
 <li>计划在未来的版本中放弃 32 位版本，以保持安装包的小规模，并减少部署工作。</li> 
</ul> 
<p><strong>3rd party updates ​​​​​</strong></p> 
<ul> 
 <li>更新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSynEdit%2FSynEdit" target="_blank">SynEdit component code</a></li> 
 <li>更新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJAM-Software%2FVirtual-TreeView" target="_blank">VirtualTrees component code</a></li> 
 <li>在安装程序中包含 Microsoft Visual C++ 2015-2019 Redistributable，某些 3rd 方库需要（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F1296" target="_blank">问题 #1296</a>）</li> 
 <li>将 plink.exe 更新到 v0.75</li> 
</ul> 
<p><strong>新的东西：</strong></p> 
<ul> 
 <li>将每个会话的 DDL 和/或 DML 查询记录到自定义文件路径（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F397" target="_blank">问题 #397</a>）</li> 
 <li>Grid text editor： 
  <ul> 
   <li>64 种代码语言的语法高亮，包括 JSON 和 XML（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F136" target="_blank">问题 #136</a>）</li> 
   <li>带有行号和已编辑行标记的 gutter</li> 
   <li>现在使用带有正则表达式支持的搜索/替换对话框</li> 
  </ul> </li> 
 <li>为 MySQL 和 MariaDB 启用查询超时设置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F1306" target="_blank">问题＃1306</a>）</li> 
 <li>在 MySQL、MSSQL 和 PostgreSQL 上显示检查约束（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F1298" target="_blank">问题 #1298</a>）</li> 
 <li>新菜单 Query > "Editor commands"，显示 SQL 编辑器可用的快速操作</li> 
 <li>在“Query”主菜单中创建“Editor commands”菜单，并用所有可用的编辑器命令填入其中</li> 
 <li>添加新的首选项以小写显示十六进制内容</li> 
</ul> 
<p><img alt height="366" src="https://oscimg.oschina.net/oscnet/up-8b3e90243cea10b7ffdeb135794cc602889.png" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>错误修正和增强功能：</strong></p> 
<ul> 
 <li>Query tab 在最小化后调整大小（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F1113" target="_blank">问题 #1113</a>）</li> 
 <li>外键添加问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F1320" target="_blank">问题 #1320</a>）</li> 
 <li>无法从数据编辑器中更新/插入 postgres jsonb 列（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F1321" target="_blank">问题 #1321</a>）</li> 
 <li>MariaDB 10.5：REPLICATION CLIENT 权限重命名为 BINLOG MONITOR（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F1302" target="_blank">问题 #1302</a>）</li> 
 <li>Percona 上的引用列默认值表达式（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F1282" target="_blank">问题 #1282</a>）</li> 
 <li>无法删除 MSSQL 中的行（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHeidiSQL%2FHeidiSQL%2Fissues%2F1294" target="_blank">问题 #1294</a>）</li> 
 <li>始终以 UTF8 模式读取 portable settings 文件和导入的设置文件，而不是自动检测潜在的错误编码。修复了从大于检查的 16 (?) KB 的 portable file 加载的损坏字符</li> 
 <li>......</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.heidisql.com%2Fforum.php%3Ft%3D37945%23p37952" target="_blank">https://www.heidisql.com/forum.php?t=37945#p37952</a></p>
                                        </div>
                                      
</div>
            