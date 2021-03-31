
---
title: '【Tethys】通用的私域 IM Server 大量更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/kk70/tethys/raw/main/docs/images/tethys-tech-stack.png'
author: 开源中国
comments: false
date: Wed, 31 Mar 2021 10:01:00 GMT
thumbnail: 'https://gitee.com/kk70/tethys/raw/main/docs/images/tethys-tech-stack.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:left">Tethys</h1> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.reactivemanifesto.org%2Fzh-CN" target="_blank">We Are Reactive</a></p> 
<p style="text-align:left">一个 IM 服务端项目，采用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fprojectreactor.io%2F" target="_blank">Spring Reactor</a> 作为基础技术研发，全站响应式技术应用(Reactor/R2DBC/Netty)。</p> 
<p style="text-align:left">内置完整的 IM 通讯协议，使用 WebSocket + HTTP 方式实现整个 IM 系统相关业务。</p> 
<p style="text-align:left"><strong>能够完全独立于业务系统之外运行，且能够方便快速的与现有系统整合，你可用于它快速搭建搭建私域 IM 服务，或用于替代公有云 IM 服务。</strong></p> 
<h2 style="text-align:left">特点</h2> 
<ul> 
 <li>响应式</li> 
 <li>免费的</li> 
 <li>高性能</li> 
</ul> 
<h2 style="text-align:left">技术栈</h2> 
<p style="text-align:left"><img alt src="https://gitee.com/kk70/tethys/raw/main/docs/images/tethys-tech-stack.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">交互流程图</h2> 
<p style="text-align:left"><img alt src="https://gitee.com/kk70/tethys/raw/main/docs/images/flow-20200330.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">更新功能</h2> 
<ul> 
 <li>实现消息存储</li> 
 <li>消息拉取离线消息获取</li> 
 <li>消息已读状态设置</li> 
 <li>重构认证逻辑 - 并完全去除阻塞 API 的使用</li> 
 <li>S2S 新增用户同步</li> 
 <li>S2S 新增访问令牌获取</li> 
 <li>S2S 新增群组同步</li> 
 <li>S2S 新增群组成员同步</li> 
 <li>大量文档内容更新</li> 
</ul> 
<h2>REST 文档</h2> 
<p><a href="https://kk70.gitee.io/tethys/tethys-rest.html" target="_blank">在线连接</a></p> 
<h2><img alt height="784" src="https://oscimg.oschina.net/oscnet/up-a58e0b86fd2d96434dffe1e21494008b77f.png" width="844" referrerpolicy="no-referrer"></h2> 
<p>Tethys REST 接口分两大部分，<strong>Support 系统支撑</strong>是用于<strong>业务服务端</strong>调用的采用的是 HTTP Basic 认证。业务系统将用户、群组以及群组成员的关系同步到 Tethys 中。客户端直接与 Tethys 建立 WS 链接并进行 IM 通讯，详细请查看 README。</p> 
<h2>最后</h2> 
<p><em>Tethys 目前还是处于一个在开发中的项目，目前发布的内容仅可用于测试。</em></p> 
<p>欢迎大家提 Issues，我会将好的建议都在 Tethys 中体现，让它功能更加的完善，适用更多的场景。</p> 
<p>同时欢迎对 IM 有兴趣以及对响应式编程有兴趣的小伙伴加入我们，一起创造出一个通用稳定的 IM Server。</p>
                                        </div>
                                      
</div>
            