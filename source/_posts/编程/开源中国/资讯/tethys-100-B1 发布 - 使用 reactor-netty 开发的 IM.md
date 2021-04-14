
---
title: 'tethys-1.0.0-B1 发布 - 使用 reactor-netty 开发的 IM'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/kk70/tethys/raw/main/docs/images/flow-20200330.png'
author: 开源中国
comments: false
date: Wed, 14 Apr 2021 11:30:00 GMT
thumbnail: 'https://gitee.com/kk70/tethys/raw/main/docs/images/flow-20200330.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">一个 IM 服务端项目，采用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fprojectreactor.io%2F" target="_blank">Spring Reactor</a> 作为基础技术研发，全站响应式技术应用(Reactor/R2DBC/Netty)。</p> 
<p style="text-align:left">内置完整的 IM 通讯协议，使用 WebSocket + HTTP 方式实现整个 IM 系统相关业务。</p> 
<p style="text-align:left"><strong>能够完全独立于业务系统之外运行，且能够方便快速的与现有系统整合，并提供了 HTTP、gRPC 服务接口能方便的与 Tethys 进行通讯，你可用于它快速搭建搭建私域 IM 服务，或用于替代公有云 IM 服务。</strong></p> 
<h2 style="text-align:left">特点</h2> 
<ul> 
 <li>响应式</li> 
 <li>免费的</li> 
 <li>高性能</li> 
</ul> 
<h2 style="text-align:left">交互流程图</h2> 
<p style="text-align:left"><img alt src="https://gitee.com/kk70/tethys/raw/main/docs/images/flow-20200330.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">更新功能</h2> 
<ul> 
 <li>新增 HTTP 发送消息接口</li> 
 <li>新增 gRPC 发送消息接口</li> 
 <li> <p>完善 Server to Server 对接 API</p> 
  <ul> 
   <li>完善同步用户 ID 接口</li> 
   <li>完善同步群组 ID 接口</li> 
   <li>完善群组用户绑定接口</li> 
   <li>完善访问令牌获取接口</li> 
  </ul> </li> 
 <li>优化消息存储表结构设计</li> 
 <li>删除消息包中无用的字段设计</li> 
 <li>规范化私聊、群聊消息包设计</li> 
 <li>修复大量 sonarlint 规范性代码错误</li> 
 <li>补充大量单元测试</li> 
</ul> 
<h2 style="text-align:left">文档更新</h2> 
<ul> 
 <li><a href="https://gitee.com/kk70/tethys/blob/main/docs/dev/index.md">新增开发手册</a></li> 
 <li><a href="https://gitee.com/kk70/tethys/blob/main/docs/design/message_id.md">完善分布式消息 ID 设计</a></li> 
 <li><a href="https://kk70.gitee.io/tethys/tethys-rest.html">完善 OpenAPI 接口文档</a></li> 
</ul> 
<h2 style="text-align:left">演示</h2> 
<h3 style="text-align:left">WebSocket 收发消息</h3> 
<p style="text-align:left"><img alt src="https://gitee.com/kk70/tethys/raw/main/docs/dev/images/328994a573dc.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">HTTP 消息发送</h3> 
<p style="text-align:left"><img alt src="https://gitee.com/kk70/tethys/raw/main/docs/dev/images/a21fa82f2da7.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">gRPC 发送消息</h3> 
<p style="text-align:left"><img alt src="https://gitee.com/kk70/tethys/raw/main/docs/dev/images/4c04babfe553.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">最后</h3> 
<p style="text-align:left">Tethys 目前还是处于一个在开发中的项目，目前发布的内容仅可用于测试。</p> 
<p style="text-align:left"><em>欢迎大家提 Issues，我会将好的建议都在 Tethys 中体现，让它功能更加的完善，适用更多的场景。</em></p> 
<p style="text-align:left">同时欢迎对 IM 有兴趣以及对响应式编程有兴趣的小伙伴加入我们，一起创造出一个通用稳定的 IM Server</p>
                                        </div>
                                      
</div>
            