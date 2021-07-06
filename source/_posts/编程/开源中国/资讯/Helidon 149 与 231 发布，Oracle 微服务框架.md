
---
title: 'Helidon 1.4.9 与 2.3.1 发布，Oracle 微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4411'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 09:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4411'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Helidon <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Freleases%2Ftag%2F1.4.9" target="_blank">1.4.9</a> 与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Freleases%2Ftag%2F2.3.1" target="_blank">2.3.1</a> 现已发布，Helidon 是 Oracle 开源的一个用于编写微服务的 Java 框架，这些微服务运行在由 Netty 提供支持的快速 Web 内核上。该项目的特性包括轻量、快速、支持 Microprofile、函数式编程模型与可观察性、弹性。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>1.4.9 
  <ul> 
   <li>WebServer：绑定多个端口时尊重绑定地址（主机）</li> 
   <li>WebServer：在 1.x 3102 中匹配路由时忽略路径参数</li> 
   <li>WebServer： 对作为 400 和 404 响应的一部分返回的路径进行编码</li> 
   <li>升级 netty 3079</li> 
   <li>升级 Jakarta 依赖项以匹配 2.x 3062 中的内容</li> 
   <li>更新到适用于 1.x 3081 的 SmallRye OpenAPI 1.2.3</li> 
   <li>恢复 jaeger-client 的 libthrift 强制升级</li> 
  </ul> </li> 
 <li>2.3.1 
  <ul> 
   <li>添加了 MP Config 2.0 向后兼容的功能，包括添加配置文件以及支持 OptionalInt、OptionalLong 和 OptionalDouble 类型</li> 
   <li>WebServer：支持密码中的冒号</li> 
   <li>WebServer：添加了清除 cookie 和使 cookie 无效的便捷方法</li> 
   <li>WebServer：修复 SSE 事件发送</li> 
   <li>WebClient：现在会缓存主机 IPv6 匹配</li> 
   <li>Tracing：通过 Helidon 的指标系统 3000 发布内部 Jaeger 跟踪指标</li> 
   <li>Test：在 Helidon Junit 5 测试中添加对 YAML 配置的支持</li> 
   <li>Security：增加 Helidon 加密模块</li> 
   <li>Security：向安全提供者添加可选支持</li> 
  </ul> </li> 
</ul> 
<p>更多详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Ftags" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            