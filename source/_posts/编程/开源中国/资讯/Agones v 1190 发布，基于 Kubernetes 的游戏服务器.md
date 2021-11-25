
---
title: 'Agones v 1.19.0 发布，基于 Kubernetes 的游戏服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9872'
author: 开源中国
comments: false
date: Thu, 25 Nov 2021 06:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9872'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Agones 是谷歌和游戏厂商育碧联合开发的游戏服务器，y用于在 Kubernetes 上托管、运行和扩展专用游戏服务器。1.19.0 版本</span><span style="color:#24292f">带来了对 Kubernetes 1.21 的支持、将 Terraform 升级到 1.0，且稳定了<span> </span></span><code>SDKWatchSendOnExecute</code><span> </span>功能。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>重大变化：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>升级到 Kubernetes 1.21<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2311" target="_blank">#2311</a></li> 
 <li>将 NodeExternalDNS 移至 Beta<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2240" target="_blank">#2240</a></li> 
 <li>将客户端升级到 v0.21.5<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2333" target="_blank">＃2333</a></li> 
 <li>将 terraform 升级到 Kubernetes 1.21<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2326" target="_blank">＃2326</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>功能改进：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>允许将证书作为值而不是 Helm 图表中的文件传递<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2364" target="_blank">#2364</a></li> 
 <li>将 SDK sidecar 移动到容器列表中的第一个位置<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2355" target="_blank">#2355</a></li> 
 <li>添加 Unity SDK 的 Unity 包<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2338" target="_blank">#2338</a></li> 
 <li>Prometheus 指标：使用 ServiceMonitor 而不是已弃用的注释机制<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2262" target="_blank">#2262</a><span> </span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2290" target="_blank">#2290</a> </li> 
 <li>如果健康检查主体为空，Sidecar REST 端点应返回 400<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2256" target="_blank">#2256</a></li> 
 <li>将 SDKWatchSendOnExecute 升级至稳定版<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2238" target="_blank">#2238</a></li> 
 <li>将 Terraform 升级到 1.0<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2142" target="_blank">#2142</a></li> 
 <li>NodeExternalDNS 转入测试版<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2369" target="_blank">#2369</a> </li> 
 <li>公开自定义证书的 Helm 图表值<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2367" target="_blank">#2367</a></li> 
 <li>将 agones sidecar 容器移动到容器列表的开头<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2357" target="_blank">#2357</a> </li> 
 <li>SDKWatchSendOnExecute 已稳定<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2353" target="_blank">#2353</a> </li> 
 <li>将 alpine 版本更新到 3.14<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2345" target="_blank">#2345</a> </li> 
 <li>支持 Unity Package Manager<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2343" target="_blank">#2343</a> </li> 
 <li><span style="color:#2e3033">为简单的游戏服务器上添加一个标志，这样它就可以在标记自己之前有小段延迟<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2340" target="_blank">#2340</a></li> 
 <li>添加为 SDK 服务帐户指定注释的功能<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2317" target="_blank">#2317</a></li> 
 <li>在 Node.js SDK 中向 WatchGameServer 添加错误回调<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2315" target="_blank">#2315</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Freleases%2Ftag%2Fv1.19.0" target="_blank">https://github.com/googleforgames/agones/releases/tag/v1.19.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            