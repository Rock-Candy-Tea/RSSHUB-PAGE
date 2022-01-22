
---
title: 'Bytebase 0.12.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1899'
author: 开源中国
comments: false
date: Sat, 22 Jan 2022 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1899'
---

<div>   
<div class="content">
                                                                                            <p>Bytebase 是一个基于网络、零配置、无依赖的数据库 Schema 变更和版本控制管理工具，适用于开发人员和 DBA。</p> 
<p>Bytebase 0.12.0 发布，更新内容如下：</p> 
<h2><strong>新功能</strong></h2> 
<h3><strong>多租户数据库管理</strong></h3> 
<p>我有很多数据库使用一样的表结构和需要统一化的管理。比如：我有一个高可用服务依赖于把用户数据存储在多区域的数据库中。或者我有个提供多租户独立数据库的SaaS服务。这个多租户数据库管理功能可以帮您更统一和方便的对多个同构数据库进行管理和表结构变更。</p> 
<ul> 
 <li>智能同构多租户数据库管理。</li> 
 <li>创建和管理数据库标签。标签可用户数据库搜索和租户识别。</li> 
 <li>灵活的多租户数据库部署。例如：按区域分阶段部署。</li> 
 <li>对所有租户的数据库表结构进行统一变更。当新的租户加入时，会自动使用已有租户的表结构。</li> 
</ul> 
<h3><strong>SQL 编辑器</strong></h3> 
<ul> 
 <li>多标签页管理</li> 
 <li>在 SQL Editor 表格展示区提交变更 DDL 操作</li> 
 <li>在 SQL Editor 输入非 Select 语句时提示可提交 DML 变更</li> 
 <li>基于项目的权限控制，用户只可以访问项目下托管的数据库</li> 
 <li>保存查询语句：支持保存 SQL 语句，搜索高亮显示并删除</li> 
 <li>查询历史记录：所有执行的查询语句都将被记录为历史记录</li> 
</ul> 
<h3><strong>通过 GitLab 进行登录</strong></h3> 
<p>用户可以使用他们已有的 GitLab 账号登录。</p> 
<ul> 
 <li><strong>支持数据变更（DML）工作流</strong></li> 
</ul> 
<p>除结构变更（DDL）工作流外，我们现也支持数据变更（DML）工作流。</p> 
<p><strong>改进</strong></p> 
<ul> 
 <li>当在启动 bytebase 时传入 --debug，会把详细错误信息展示在 UI 上。</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>修复了当 Git 分支包含 slash 时 (比如 feature/foo)，把 schema 回写到 VCS 会失败的问题</li> 
 <li>修复了 MySQL 8.0 窗口功能句法错误</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%2Freleases%2Ftag%2F0.12.0" target="_blank">https://github.com/bytebase/bytebase/releases/tag/0.12.0</a></p>
                                        </div>
                                      
</div>
            