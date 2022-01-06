
---
title: 'Apache Dubbo 3.0.5 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9967'
author: 开源中国
comments: false
date: Thu, 06 Jan 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9967'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Apache Dubbo 3.0.5 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</span></p> 
<p>此版本专注于 Dubbo3 的稳定性改进，突出了 resilience、performance、triple、service discovery 和其他一些重要的错误修复。有关更多详细信息，可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fmilestone%2F47" target="_blank">milestone 3.0.5</a>。</p> 
<p><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul> 
 <li>修复部分注册表扩展的问题，包括 Nacos 和 Zookeeper。</li> 
 <li>修复 Dubbo3 初始化和关闭过程中报的 bug</li> 
 <li>修复 Async RPC 相关的 bug，包括线程切换和回调混乱的上下文恢复。</li> 
 <li>修复服务发现（应用级）问题</li> 
</ul> 
<p><span style="color:#24292f"><strong>功能增强</strong></span></p> 
<ul> 
 <li>Resilience 提升 
  <ul> 
   <li>空地址通知保护</li> 
   <li>不健康节点/地址的自动黑名单。</li> 
  </ul> </li> 
 <li><span style="color:#24292f">Triple protocol </span>的增强</li> 
 <li>性能调优，减少内存分配</li> 
</ul> 
<p><span style="color:#24292f"><strong>漏洞</strong></span></p> 
<ul> 
 <li>升级 Log4j 到 2.17.0，见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9380" target="_blank">＃9380</a> 的详细信息</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-3.0.5" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-3.0.5</a></p>
                                        </div>
                                      
</div>
            