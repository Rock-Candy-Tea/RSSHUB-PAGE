
---
title: 'Solon 1.6.33 发布，更现代感的应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6735'
author: 开源中国
comments: false
date: Sat, 19 Mar 2022 18:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6735'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">相对于 Spring Boot 和 Spring Cloud 的项目</h3> 
<ul> 
 <li>启动快 5 ～ 10 倍</li> 
 <li>qps 高 2～ 3 倍</li> 
 <li>运行时内存节省 1/3 ~ 1/2</li> 
 <li>打包可以缩小到 1/2 ~ 1/10（比如，90Mb 的变成了 9Mb）</li> 
</ul> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个更现代感的应用开发框架，轻量、开放生态型的。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放 + 生态的原则</strong></li> 
 <li>力求，<strong>更小、更少、更快、更自由的体验</strong></li> 
</ul> 
<p style="color:#24292e; text-align:start">目前有近<strong>130</strong>个生态插件，含盖了日常开发的各种需求。</p> 
<h3 style="text-align:start">本次主要更新</h3> 
<ul> 
 <li>增加 Session::sendAsync() 接口，便于支持跨线程发消息 
  <ul> 
   <li>插件 solon.boot.jetty 的 weboskcet 增加支持</li> 
   <li>插件 solon.boot.undertow 的 weboskcet 增加支持</li> 
   <li>插件 solon.boot.websocket 的 weboskcet 增加支持</li> 
   <li>插件 solon.boot.smarthttp 的 weboskcet 增加支持</li> 
   <li>插件 solon.boot.socketd.jdksocket 的 socket 增加支持</li> 
   <li>插件 solon.boot.socketd.netty 的 socket 增加支持</li> 
   <li>插件 solon.boot.socketd.smartsocket 的 socket 增加支持</li> 
  </ul> </li> 
 <li>增加 server.ssl.* 专属ssl配置属性 
  <ul> 
   <li>插件 solon.boot.jlhttp，增加 ssl 支持</li> 
   <li>插件 solon.boot.jetty，增加 ssl 支持</li> 
   <li>插件 solon.boot.undertow，增加 ssl 支持</li> 
  </ul> </li> 
 <li>插件 solon.schedule 添加 纯手工控制能力</li> 
 <li>插件 dubbo-solon-plugin 的注解添加属性模板支持</li> 
 <li>优化 Bean 的泛型基类在容器的注册</li> 
</ul> 
<h3 style="text-align:start">进一步了解 Solon</h3> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul> 
<h3 style="text-align:start"> </h3> 
<p> </p>
                                        </div>
                                      
</div>
            