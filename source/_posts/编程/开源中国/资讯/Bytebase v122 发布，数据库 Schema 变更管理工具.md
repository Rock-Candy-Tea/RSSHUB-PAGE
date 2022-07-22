
---
title: 'Bytebase v1.2.2 发布，数据库 Schema 变更管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3107'
author: 开源中国
comments: false
date: Fri, 22 Jul 2022 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3107'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Bytebase 是一个基于网络、零配置、无依赖的数据库 Schema 变更和版本控制管理工具，适用于开发人员和 DBA。</p> 
<p style="margin-left:0px">Bytebase 1.2.2 发布，更新内容如下：</p> 
<h2>功能</h2> 
<ul> 
 <li>👻添加了对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgithub%2Fgh-ost" target="_blank">gh-ost 的</a> 支持，大型​​表的在线模式迁移（测试版）。</li> 
 <li>更新了帮助提示的显示方式，使用侧抽屉而不是弹出提示。</li> 
 <li>为表/列/索引/外键/唯一键名称添加了长度限制。</li> 
 <li>添加了一个新规则，以禁止表上的外键。</li> 
 <li>删除表时，添加了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bytebase.com%2Fdocs%2Fsql-review%2Freview-rules%2Ftable-drop-naming" target="_blank">新</a>的命名约定规则。</li> 
</ul> 
<h2><strong>增强功能</strong></h2> 
<ul> 
 <li><span style="color:#24292f">issue </span>创建者过滤器现在支持“All”和“Bytebase”。</li> 
 <li><span style="color:#24292f">issue </span>列表现在显示 <span style="color:#24292f">issue</span> ID。</li> 
 <li>[VCS 工作流程] 弹出窗口，提示如何更新问题的 SQL 语句。</li> 
 <li>[SQL Advise API] 启用数据库连接。</li> 
</ul> 
<h2><strong>修复</strong></h2> 
<ul> 
 <li>修复了如果数据库名称包含大写字母，则无法正确执行数据库的时间点恢复。</li> 
 <li>[VCS 工作流] webhook 推送事件多次包含同一个文件时，创建重复数据删除问题。</li> 
 <li>[VCS 工作流] 读取 VCS 文件内容时，处理 OAuth 令牌过期问题 。</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%2Freleases%2Ftag%2F1.2.2" target="_blank">https://github.com/bytebase/bytebase/releases/tag/1.2.2</a></p>
                                        </div>
                                      
</div>
            