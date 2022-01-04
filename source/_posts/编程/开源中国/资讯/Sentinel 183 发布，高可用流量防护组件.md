
---
title: 'Sentinel 1.8.3 发布，高可用流量防护组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-33c992f88e6af6e3214c47ed30fbe74dd2b.png'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 11:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-33c992f88e6af6e3214c47ed30fbe74dd2b.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel" target="_blank">Sentinel</a><span style="background-color:#ffffff; color:#333333"> 是阿里巴巴开源的，面向分布式服务架构的高可用流量防护组件，主要以流量为切入点，从流量控制、流量整形、依赖隔离、熔断降级、系统自适应过载保护、热点防控等多个维度来帮助开发者保障微服务的稳定性。Sentinel 承接了阿里巴巴近 10 年的双十一大促流量的核心场景，例如秒杀、冷启动、消息削峰填谷、集群流量控制、实时熔断下游不可用服务等，是保障微服务高可用的利器，原生支持 Java/Go/Rust/C++ 等多种语言，并且提供 Istio/Envoy/MOSN 全局流控支持来为 Service Mesh 提供高可用防护的能力。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-33c992f88e6af6e3214c47ed30fbe74dd2b.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Freleases%2Ftag%2F1.8.3" target="_blank">Sentinel 1.8.3</a> 版本正式发布，带来了多项特性和改进。主要变更如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Ftree%2Fmaster%2Fsentinel-cluster%2Fsentinel-cluster-server-envoy-rls" target="_blank">集群流控 token server 支持 Envoy RLS v3 API</a>，以支持较新版本 Envoy (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F2336" target="_blank">#2336</a>)</li> 
 <li>新增 JMX metric exporter 模块 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F2275" target="_blank">#2275</a>)</li> 
 <li>Consul 动态数据源支持 ACL token (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F2307" target="_blank">#2307</a>)</li> 
 <li>完善系统规则 inbound QPS 策略判断的条件，采用 pass QPS 而不是 complete QPS (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F2455" target="_blank">#2455</a>)</li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">详情请参考<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Freleases%2Ftag%2F1.8.3" target="_blank">Release Notes</a>。感谢为该版本付出的所有贡献者：@brotherlu-xcq, @chenzhiguo, @sczyh30, @shaohsiung, @su787910081, @winjaychan, @wucheng1997, @xiaojun207, @xianwdong</p>
                                        </div>
                                      
</div>
            