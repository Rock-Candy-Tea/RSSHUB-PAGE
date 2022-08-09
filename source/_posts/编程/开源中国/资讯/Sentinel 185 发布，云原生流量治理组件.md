
---
title: 'Sentinel 1.8.5 发布，云原生流量治理组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cef6c9df1d170337edabb4c9cde75daeedf.png'
author: 开源中国
comments: false
date: Tue, 09 Aug 2022 15:40:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cef6c9df1d170337edabb4c9cde75daeedf.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel" target="_blank">Sentinel</a><span style="background-color:#ffffff; color:#333333"> 是阿里巴巴开源的，面向分布式服务架构的流量治理组件，主要以流量为切入点，从流量控制、流量整形、依赖隔离、熔断降级、系统自适应过载保护、热点防控等多个维度来帮助开发者保障微服务的稳定性。Sentinel 承接了阿里巴巴近 10 年的双十一大促流量的核心场景，例如秒杀、冷启动、消息削峰填谷、集群流量控制、实时熔断下游不可用服务等，是保障微服务高可用的利器，原生支持 Java/Go/Rust/C++ 等多种语言，并且提供 Istio/Envoy/MOSN 全局流控支持来为 Service Mesh 提供高可用防护的能力。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt="sentinel-eco" height="1398" src="https://oscimg.oschina.net/oscnet/up-cef6c9df1d170337edabb4c9cde75daeedf.png" width="2500" referrerpolicy="no-referrer"></span></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">本周 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Freleases%2Ftag%2F1.8.5" target="_blank">Sentinel 1.8.5</a><span> </span>正式发布，带来了多项特性和改进。主要新特性及改进如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新增 Apache Dubbo 3.x 适配模块，正式支持 Dubbo 3</li> 
 <li>完善 Sentinel 控制台以支持 JDK 17</li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">详情请参考<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Freleases%2Ftag%2F1.8.5" target="_blank">Release Notes</a>。感谢为该版本付出的所有贡献者：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAlbumenJ" target="_blank">@AlbumenJ</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbenyamin2014" target="_blank">@benyamin2014</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficodening" target="_blank">@icodening</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgzl" target="_blank">@jgzl</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsczyh30" target="_blank">@sczyh30</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuohl" target="_blank">@zuohl</a></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">同时，社区也在投入 Sentinel 2.0 的演进中。Sentinel 2.0 品牌升级将为流量治理，领域涵盖流量路由/调度、流量染色、流控降级等；同时社区正在将流量治理相关标准抽出到<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensergo.io%2Fzh-cn%2F" target="_blank">OpenSergo 标准</a>中，Sentinel 作为流量治理标准实现。有关 Sentinel 流控降级与容错 spec 的最新进展，请参考<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensergo%2Fopensergo-specification%2Fblob%2Fmain%2Fspecification%2Fzh-Hans%2Ffault-tolerance.md" target="_blank">opensergo-specification</a>，也欢迎社区一起来完善标准与实现。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://user-images.githubusercontent.com/9434884/183335605-4215c142-3f30-4cfb-a1f1-a235a44d024b.png" width="3000" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            