
---
title: 'Apache Dubbo 3.0.6 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2267'
author: 开源中国
comments: false
date: Sun, 06 Mar 2022 07:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2267'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">Apache Dubbo 3.0.6 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</span></p> 
<p>3.0.6 继续专注于 Dubbo3 的稳定性提升，变化主要与服务发现、三重协议、社区用户反馈的 bug 有关。查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fmilestone%2F48" target="_blank">milestone 3.0.6</a>了解更多详细信息。</p> 
<p><strong style="color:#24292f">Bug 修复</strong></p> 
<ul> 
 <li>修复带有嵌入式 RPC 调用的异步提供程序无法成功写回结果的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9704" target="_blank">#9704</a></li> 
 <li>修复 QoS endpoint /ready 和 /startup 不能正常工作的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9634" target="_blank">#9634</a></li> 
 <li>修复 Spring bean 无法注册到 SPI 实例的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F8792" target="_blank">#8792</a></li> 
 <li>修复注册到 ResponseFuture 的回调的执行顺序不确定的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9461" target="_blank">#9461</a></li> 
 <li>修复多个 metadata reporter 支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9322" target="_blank">#9322</a></li> 
</ul> 
<p><strong style="color:#24292f">功能增强</strong></p> 
<ul> 
 <li>服务发现模型 
  <ul> 
   <li>重构的 meta impl</li> 
   <li>cache 支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9684" target="_blank">#9684</a></li> 
   <li>并发<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9684" target="_blank">＃9684</a></li> 
  </ul> </li> 
 <li>三重协议</li> 
 <li>JDK 17 支持</li> 
 <li>支持 send.reconnect 可配置<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9195" target="_blank">#9195</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-3.0.6" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-3.0.6</a> </p>
                                        </div>
                                      
</div>
            