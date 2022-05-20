
---
title: 'Apache Dubbo 3.0.8 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4087'
author: 开源中国
comments: false
date: Fri, 20 May 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4087'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#000000">Apache Dubbo 3.0.8 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</span></p> 
<p><span style="background-color:#ffffff; color:#000000">具体更新内容包括：</span></p> 
<p style="text-align:start"><strong>Bugfixes & Enhancements</strong></p> 
<ul> 
 <li>Triple Protocol 
  <ul> 
   <li>修复可能的内存泄漏<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9919" target="_blank">#9919</a></li> 
   <li>多协议情况下使用单独的 ThreadPool <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F10018" target="_blank">#10018</a></li> 
   <li>存根编译器增强</li> 
   <li>关机流程优化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9938" target="_blank">#9938</a></li> 
  </ul> </li> 
 <li>Service Discovery 
  <ul> 
   <li>修复 <span style="background-color:#ffffff; color:#24292f">interface-app mapping </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9992" target="_blank">#9992</a></li> 
   <li>修复 warmup 在消费者端不起作用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10022" target="_blank">#10022</a> , <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9990" target="_blank">#9990</a></li> 
   <li>修复 OfflineApp 在版本为 0 时无法更新注册表的问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9986" target="_blank"> #9986</a></li> 
   <li>当前地址模型不可用时，在 APPLICATION_FIRST 模式下回退到另一个地址模型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9964" target="_blank">#9964</a></li> 
   <li>重构元数据交换过程以支持某些注册表模式，例如 k8s 和 dns <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9904" target="_blank">#9904</a></li> 
   <li>为实例级参数过滤器扩展添加“exclude”过滤策略 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10015" target="_blank">#10015</a></li> 
  </ul> </li> 
 <li>Others 
  <ul> 
   <li>与 Cache 一起使用时，区分 ReferenceConfig 实例的 singleton 和 prototype status ​​​​​​​<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F10012" target="_blank">#10012</a></li> 
   <li>修复从 2.6 或更低版本升级到 3.x 时的 SPI 扩展兼容性问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9977" target="_blank">#9977</a></li> 
   <li>修改全局迁移 key 为 'dubbo.application.migration.step' <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10006" target="_blank">#10006</a></li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-3.0.8" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-3.0.8</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            