
---
title: 'Bytebase 1.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d4b022e2e9b7da7de610fe8fed7d9797e8f.png'
author: 开源中国
comments: false
date: Sat, 06 Aug 2022 07:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d4b022e2e9b7da7de610fe8fed7d9797e8f.png'
---

<div>   
<div class="content">
                                                                                            <p>Bytebase 是一个基于网络、零配置、无依赖的数据库 Schema 变更和版本控制管理工具，适用于开发人员和 DBA。</p> 
<p>Bytebase 1.3 发布，更新内容如下：</p> 
<h3><strong>新功能</strong></h3> 
<ul> 
 <li>支持对 PostgreSQL 进行 SQL 审核，当前支持 13 条 SQL 审核规则。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bytebase.com%2Fdocs%2Fsql-review%2Freview-rules%2Foverview" target="_blank">https://www.bytebase.com/docs/sql-review/review-rules/overview</a></li> 
</ul> 
<p><img alt height="359" src="https://oscimg.oschina.net/oscnet/up-d4b022e2e9b7da7de610fe8fed7d9797e8f.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>支持使用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2FGitHub.com" target="_blank">GitHub.com</a> 作为 VCS 的集成后端进行数据库 Schema 变更管理，并允许用户使用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2FGitHub.com" target="_blank">GitHub.com</a> 账户直接登录 Bytebase。</li> 
</ul> 
<p><img alt height="393" src="https://oscimg.oschina.net/oscnet/up-79cb39c8dffb550f9a960697b80fe2fb96c.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>一键将数据库还原到最近一次变更操作之前。‍</li> 
</ul> 
<p><img alt height="612" src="https://oscimg.oschina.net/oscnet/up-1ba4e269ef482b1571ba5a206c1d4af3e20.png" width="700" referrerpolicy="no-referrer"></p> 
<h3><strong>改进</strong></h3> 
<ul> 
 <li>增强了数据库备份功能，支持设置周期性备份的具体时间，以及备份保留的周期。</li> 
</ul> 
<p><img alt height="552" src="https://oscimg.oschina.net/oscnet/up-c5738f4b5e60a4c5570fd87a429b1f04046.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>Gh-ost 改进：显示同步任务的进度；修复可能数据丢失，长时间锁表的问题。</li> 
 <li>当 VCS 有新的提交时，Bytebase 创建的对应的 issue 会根据邮箱尝试匹配以显示对应的创建者。</li> 
 <li>允许在多租户模式下修改 SQL 语句。</li> 
 <li>支持一次选择多个数据库进行转移到指定项目。</li> 
 <li>支持通过导入 SQL Script 文件进行数据库变更。</li> 
 <li>支持了数据库层级的 Schema 同步。</li> 
 <li>优化了数据库 Schema 同步性能。</li> 
</ul> 
<h3><strong>Bug 修复</strong></h3> 
<ul> 
 <li>[GitOps 工作流] 当把最新 schema 回写到仓库时，适当地处理 Token 过期的问题。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%2Freleases%2Ftag%2F1.3.0" target="_blank">https://github.com/bytebase/bytebase/releases/tag/1.3.0</a></p>
                                        </div>
                                      
</div>
            