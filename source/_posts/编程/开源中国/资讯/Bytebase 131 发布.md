
---
title: 'Bytebase 1.3.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a4d2f8bc098c37ea485be40b50abf2c2dd2.png'
author: 开源中国
comments: false
date: Sat, 20 Aug 2022 07:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a4d2f8bc098c37ea485be40b50abf2c2dd2.png'
---

<div>   
<div class="content">
                                                                                            <p>Bytebase 是一个基于网络、零配置、无依赖的数据库 Schema 变更和版本控制管理工具，适用于开发人员和 DBA。</p> 
<p>Bytebase 1.3.1 发布，更新内容如下：</p> 
<h3><strong>新功能</strong></h3> 
<ul> 
 <li>SQL Review 在 GitHub Action Marketplace发布。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmarketplace%2Factions%2Fsql-review" target="_blank">https://github.com/marketplace/actions/sql-review</a></li> 
</ul> 
<p><img alt height="374" src="https://oscimg.oschina.net/oscnet/up-a4d2f8bc098c37ea485be40b50abf2c2dd2.png" width="700" referrerpolicy="no-referrer"></p> 
<h3><strong>改进</strong></h3> 
<ul> 
 <li>MySQL 数据库备份恢复速度提升 20 倍。</li> 
 <li>支持设置项目所有者（Project owner）作为工单审核人。</li> 
</ul> 
<p><img alt height="337" src="https://oscimg.oschina.net/oscnet/up-b630869825fc8d80a391c72d36f58eee922.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>变更 Schema 页面支持通过搜索的方式快速定位数据库。</li> 
</ul> 
<p><img alt height="526" src="https://oscimg.oschina.net/oscnet/up-47a9bf12df7474505a44b9907b39efa1369.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>支持在多租户模式的项目中变更单个数据库的 schema。</li> 
</ul> 
<p><img alt height="353" src="https://oscimg.oschina.net/oscnet/up-cc57591739e58a9274cf41a5c411198d0be.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>更新 SQL Editor「打开连接」按钮的使用方式。</li> 
</ul> 
<p><img alt height="318" src="https://oscimg.oschina.net/oscnet/up-6e61d2a2f11c8e8ba2f0c0ceccd83cb1c38.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>提升了 SQL Editor 数据库实例树的显示速度。</li> 
 <li>评论区可点击按钮回复「LGTM」。</li> 
</ul> 
<p><img alt height="419" src="https://oscimg.oschina.net/oscnet/up-ac9bf30a60687bde180ece9dc0024dc8f9f.png" width="700" referrerpolicy="no-referrer"></p> 
<h3><strong>Bug 修复</strong></h3> 
<ul> 
 <li>禁止从 VCS 发起基线（Baseline）请求。基线请求只应该从 Bytebase console 发起，用来同步数据库 schema，来解决 schema 偏差。</li> 
 <li>修复了在 VCS 项目下的数据库创建 schema 基线的回写问题。</li> 
</ul> 
<h3><strong>社区</strong></h3> 
<ul> 
 <li>创建了配置 SQL Review GitHub Action 的样例。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FBytebase%2Fsql-review-action-example" target="_blank">https://github.com/Bytebase/sql-review-action-example</a></li> 
</ul> 
<p><img alt height="270" src="https://oscimg.oschina.net/oscnet/up-8bcaa9211c5df63d9e01aa0b4925aad1317.png" width="700" referrerpolicy="no-referrer"></p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%2Freleases%2Ftag%2F1.3.1" target="_blank">https://github.com/bytebase/bytebase/releases/tag/1.3.1</a></p>
                                        </div>
                                      
</div>
            