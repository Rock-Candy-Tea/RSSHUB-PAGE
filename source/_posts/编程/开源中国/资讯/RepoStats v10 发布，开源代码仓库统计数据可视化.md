
---
title: 'RepoStats v1.0 发布，开源代码仓库统计数据可视化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fc53571df1456fa0ab21db5831ca129d05a.jpg'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 14:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fc53571df1456fa0ab21db5831ca129d05a.jpg'
---

<div>   
<div class="content">
                                                                                            <p>从2021年底开始构思，时至今日总算完成了第一个版本的发布！</p> 
<p>RepoStats <span>基于 Golang 开发，能够抓取开源代码仓库的 star、fork、commit、pull request、issue 等相关数据统计并可视化展示。</span></p> 
<p>RepoStats 致力于解决的痛点问题是：</p> 
<ol> 
 <li>开源代码仓库的数据抓取、存储、分析及统计</li> 
 <li>开源代码仓库的相关数据可视化展示</li> 
 <li>做到全平台打通，并支持分隔、组合展示</li> 
</ol> 
<p>主要工作原理如下图所示：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-fc53571df1456fa0ab21db5831ca129d05a.jpg" referrerpolicy="no-referrer"></p> 
<p><strong>主要功能包括：</strong></p> 
<ol> 
 <li>当前版本的 RepoStats 仅支持 Gitee 平台相关数据获取 (后续会持续新增其他平台，国产平台优先考虑)</li> 
 <li>管理后台：支持界面化的 Gitee Oauth 配置、Grafana Token 获取配置</li> 
 <li>管理后台：支持添加单个仓库、支持批量添加个人帐号及组织帐号下的公开仓库</li> 
 <li>管理后台：支持禁用、启用 Gitee 数据抓取(启动抓取除外)</li> 
 <li>管理后台：支持 Commit 列表显示及查询、Issue 列表显示及查询、Pull Request 列表显示及查询</li> 
 <li>Grafana 标签：每个面板均有附带仓库拥有者标签、仓库名称、平台名称等信息支持查询过滤</li> 
</ol> 
<p>界面截图：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1d0f56655abc5a92846614e9862620e55b4.jpg" referrerpolicy="no-referrer"></p> 
<p>代码已开源，敬请体验和吐槽。</p> 
<p>更多详情，请参考 RepoStats Gitee 页面：<a href="https://gitee.com/barat/repostats">https://gitee.com/barat/repostats</a></p>
                                        </div>
                                      
</div>
            