
---
title: 'Agones v 1.23.0 发布，谷歌和育碧联合开发的游戏服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3187'
author: 开源中国
comments: false
date: Fri, 13 May 2022 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3187'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Agones 是谷歌和游戏厂商育碧联合开发的游戏服务器，用于在 Kubernetes 上托管、运行和扩展专用游戏服务器。</p> 
<p>目前，Agones V1.23.0 发布了，此版本引入了对在使用 ARM 架构的 linux 机器上运行游戏服务器的初步支持。同时带来了对 Kubernetes 1.22 的支持。</p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本还有许多重要的错误修复，包括：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复了将健康的 pod 标记为不健康的健康控制器竞争条件。</li> 
 <li>在缩放之前检查 fleet 和游戏服务器集的 DeletionTimestamp。</li> 
 <li>GameServer 卡在关闭状态，阻止滚动更新完成。</li> 
 <li>修复 GameServer 总是回到 Ready 的问题。</li> 
 <li>使用 DeletionTimestamp 对更新的 GameServer 进行排队。</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>重大变化：</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>将 terraform 升级到 Kubernetes 1.22 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2551" target="_blank">#2551</a></li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>增强功能：</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>升级到 Kubernetes 1.22 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2494" target="_blank">#2494</a></li> 
 <li>更新 App Engine 中使用的 golang 版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2382" target="_blank">#2382</a></li> 
 <li>分配器控制器 arm64  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2565" target="_blank">#2565</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLudea" target="_blank">Ludea</a> )</li> 
 <li>sdk arm64 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2521" target="_blank">#2521</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Freleases%2Ftag%2Fv1.23.0" target="_blank">https://github.com/googleforgames/agones/releases/tag/v1.23.0</a></p>
                                        </div>
                                      
</div>
            