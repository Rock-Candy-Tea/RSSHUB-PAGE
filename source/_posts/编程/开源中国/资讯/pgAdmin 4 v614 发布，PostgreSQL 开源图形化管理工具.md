
---
title: 'pgAdmin 4 v6.14 发布，PostgreSQL 开源图形化管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6289'
author: 开源中国
comments: false
date: Sun, 25 Sep 2022 07:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6289'
---

<div>   
<div class="content">
                                                                    
                                                        <p>pgAdmin 是 PostgreSQL 领先的开源图形化管理工具。pgAdmin 4 旨在满足新手和有经验的 Postgres 用户的需求，提供强大的图形界面，简化了数据库对象的创建、维护和使用。</p> 
<p>这个版本的 pgAdmin 4 包括错误修复和新功能，主要更新内容如下：</p> 
<blockquote> 
 <p><strong>注意：pgAdmin 团队已将所有问题从 Redmine 移到 GitHub。新的问题不能再在 Redmine 上创建，任何现有的问题都应该在 GitHub 上更新（每个 Redmine 问题都包含一个指向 GitHub 新问题的链接）</strong></p> 
</blockquote> 
<h3>Bugs/Housekeeping:</h3> 
<ul> 
 <li>将 schema diff、search object 和 ERD 的其余组件移植到 React</li> 
 <li>删除 Alertify、Slickgrid、Backgrid 和 Backform</li> 
 <li>修复了用户打开 pgAdmin URL 时的重定向漏洞</li> 
 <li>修正了由于 bin 路径迁移导致 pgAdmin 启动失败的问题</li> 
 <li>修正了由于参数 <code>preexec_fn</code> 不再被支持而导致备份不工作的问题</li> 
 <li>确保转储服务器功能在 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsetup.py" target="_blank">setup.py</a> 中工作</li> 
 <li>确保导入/导出服务器的菜单选项是可见的</li> 
 <li>修正了在导入/导出数据前添加的列不可见的问题</li> 
 <li>修正了运行 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsetup.py" target="_blank">setup.py</a> 加载/转储服务器时的 ModuleNotFoundError 错误</li> 
 <li>修正了 JSON 编辑器的文本区不随对话框调整大小的问题</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpgadmin-4-v614-released-2515%2F" target="_blank">https://www.postgresql.org/about/news/pgadmin-4-v614-released-2515/</a></p>
                                        </div>
                                      
</div>
            