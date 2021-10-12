
---
title: 'Agones v 1.18.0 发布，基于 Kubernetes 的游戏服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5867'
author: 开源中国
comments: false
date: Tue, 12 Oct 2021 05:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5867'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Agones 是谷歌和游戏厂商育碧联合开发的游戏服务器。它是一个用于在 Kubernetes 上托管、运行和扩展专用游戏服务器的库。</p> 
<p>Agones 1.18.0 版本修复了 Agones 1.11.0 中引入的分配器服务中的 gRPC 兼容性问题。</p> 
<p>如果您有一个不能与分配器服务器一起工作的 gRPC 客户端，现在可以禁用 REST 服务器或将其设置为不同的端口，以获得更好的客户端兼容性。</p> 
<p><span style="background-color:rgba(175, 184, 193, 0.2); color:#24292f">RollingUpdateOnRead</span> 功能已升级至稳定，新的 alpha 特性 <span style="background-color:rgba(175, 184, 193, 0.2); color:#24292f">SDKGracefulTermination</span> 使 Agones 在 Preemptible VMs 上工作得更好。</p> 
<p>一些与分配器服务相关的 helm 参数被重命名，以使它们更加一致。如果您设置了这些值的其中一个，您将需要修改 helm 脚本，以使用新的参数。</p> 
<p><strong>突破性更新：</strong></p> 
<ul> 
 <li>允许为分配器服务配置 gRPC 和 REST 的端口<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2272" target="_blank">#2272</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Froberthbailey" target="_blank">roberthbailey</a> )</li> 
</ul> 
<p><strong>实现的增强功能：</strong></p> 
<ul> 
 <li>如果 mTLS 上的 TLS 被禁用，则跳过分配器 pod 中的卷挂载<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2276" target="_blank">#2276</a></li> 
 <li>允许分配器服务使用 go http/2 服务器<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2263" target="_blank">#2263</a></li> 
 <li>将 RollingUpdateOnReady 移至稳定<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2239" target="_blank">#2239</a></li> 
 <li>解释命名空间参数如何用于分配<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F2090" target="_blank">#2090</a></li> 
 <li>建议：在游戏服务器命名空间中提供 allocator-client.default 机密<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F1686" target="_blank">#1686</a></li> 
 <li>游戏服务器分配高级过滤：玩家数量、状态、重新分配<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fissues%2F1239" target="_blank">#1239</a></li> 
 <li>不需要时，跳过分配器 pod 中的机密和卷挂载<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2277" target="_blank">#2277</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Froberthbailey" target="_blank">roberthbailey</a> )</li> 
 <li>将 RollingUpdateOnReady 移动到稳定位置<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2271" target="_blank">#2271</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJeffwan" target="_blank">Jeffwan</a> )</li> 
 <li>文档：高密度集成模式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2270" target="_blank">#2270</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmarkmandel" target="_blank">markmandel</a> )</li> 
 <li>文档：集成模式 - 复用 GameServers <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2251" target="_blank">#2251</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmarkmandel" target="_blank">markmandel</a> )</li> 
 <li>支持优雅终止<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fpull%2F2205" target="_blank">#2205</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbennetty" target="_blank">Bennetty</a> )</li> 
</ul> 
<p>更多详细更新内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogleforgames%2Fagones%2Fblob%2Frelease-1.18.0-rc%2FCHANGELOG.md" target="_blank">更新日志</a>。</p>
                                        </div>
                                      
</div>
            