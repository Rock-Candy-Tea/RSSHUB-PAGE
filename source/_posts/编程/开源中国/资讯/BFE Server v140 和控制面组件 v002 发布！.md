
---
title: 'BFE Server v1.4.0 和控制面组件 v.0.0.2 发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2490'
author: 开源中国
comments: false
date: Thu, 16 Dec 2021 05:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2490'
---

<div>   
<div class="content">
                                                                                            <p>12 月 10 日，BFE 开源项目的数据面转发引擎 BFE Server 和控制面各组件相继发布了新版本。</p> 
<p>作为 BFE 数据面核心转发引擎，BFE Server 本次发布了 v1.4.0。</p> 
<p>该版本主要包括如下变化：</p> 
<ul> 
 <li>修复了配合 Go 1.17 使用时出现的问题</li> 
 <li>在部分实现中，使用 RWMutex 代替 Mutex，获得了部分性能上的收益</li> 
 <li>对 mod_markdown 模块，升级了其中使用的 bluemonday</li> 
 <li>优化了 Makefile 和 pre-commit 工具</li> 
</ul> 
<p>BFE 控制面包括 APIServer、Conf Agent、Dashboard 三个程序，本次均发布了新版本 v0.0.2。</p> 
<p>控制面本次发布的版本主要包括如下变化：</p> 
<p>对于 API Server</p> 
<ul> 
 <li>提供了 BFE Open API 的完整中文文档</li> 
 <li>完善了认证和授权部分的逻辑和功能，可以更好地管理控制台用户，及管理程序访问调用中使用的 Token，并支持按租户的权限控制</li> 
 <li>修复了初始化时的数据库 DDL（Data Definition Language）由于 MySQL 的 NO_ZERO_DATE 限制导致失败的问题</li> 
</ul> 
<p>对于 Conf Agent</p> 
<ul> 
 <li>配合 API Server 的修改做了升级</li> 
</ul> 
<p>对于 Dashboard</p> 
<ul> 
 <li>修复了后端集群的部分超时参数默认值设置不合理的问题</li> 
 <li>配合 API Server，完善了用户和 Token 的管理功能</li> 
</ul> 
<p>您可以访问如下地址，获取最新版本的安装包：</p> 
<p>BFE Server: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbfenetworks%2Fbfe%2Freleases%2Ftag%2Fv1.4.0" target="_blank">https://github.com/bfenetworks/bfe/releases/tag/v1.4.0</a></em></p> 
<p>API Server: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbfenetworks%2Fapi-server%2Freleases%2Ftag%2Fv0.0.2" target="_blank">https://github.com/bfenetworks/api-server/releases/tag/v0.0.2</a></em></p> 
<p>Dashboard: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbfenetworks%2Fdashboard%2Freleases%2Ftag%2Fv0.0.2" target="_blank">https://github.com/bfenetworks/dashboard/releases/tag/v0.0.2</a></em></p> 
<p>Conf Agent: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbfenetworks%2Fconf-agent%2Freleases%2Ftag%2Fv0.0.2" target="_blank">https://github.com/bfenetworks/conf-agent/releases/tag/v0.0.2</a></em></p> 
<p>还有哪些新功能是您期待的？您在 BFE 使用中有什么疑问么？访问下面的链接，提交您的反馈：</p> 
<p><em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbfenetworks%2Fbfe%2Fissues" target="_blank">https://github.com/bfenetworks/bfe/issues</a></em></p>
                                        </div>
                                      
</div>
            