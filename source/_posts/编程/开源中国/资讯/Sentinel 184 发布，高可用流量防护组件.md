
---
title: 'Sentinel 1.8.4 发布，高可用流量防护组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cef6c9df1d170337edabb4c9cde75daeedf.png'
author: 开源中国
comments: false
date: Wed, 13 Apr 2022 14:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cef6c9df1d170337edabb4c9cde75daeedf.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel" target="_blank">Sentinel</a><span style="background-color:#ffffff; color:#333333"> 是阿里巴巴开源的，面向分布式服务架构的高可用流量防护组件，主要以流量为切入点，从流量控制、流量整形、依赖隔离、熔断降级、系统自适应过载保护、热点防控等多个维度来帮助开发者保障微服务的稳定性。Sentinel 承接了阿里巴巴近 10 年的双十一大促流量的核心场景，例如秒杀、冷启动、消息削峰填谷、集群流量控制、实时熔断下游不可用服务等，是保障微服务高可用的利器，原生支持 Java/Go/Rust/C++ 等多种语言，并且提供 Istio/Envoy/MOSN 全局流控支持来为 Service Mesh 提供高可用防护的能力。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1677" src="https://oscimg.oschina.net/oscnet/up-cef6c9df1d170337edabb4c9cde75daeedf.png" width="3000" referrerpolicy="no-referrer"></p> 
<p>近期 Sentinel 1.8.4 版本正式发布，带来多项特性改进与问题修复，其中主要变更有：</p> 
<ul> 
 <li>完善 transport 模块的扩展性，支持拦截器扩展以支持用户自定义鉴权等行为</li> 
 <li>网关流控中完善参数解析的扩展性，支持用户自定义解析参数的逻辑（如定制化解析 IP 的逻辑）</li> 
 <li>修复控制台在进行集群流控分配时的一些异常情况，并完善熔断规则配置提示</li> 
 <li>将控制台依赖的 Spring Boot 版本升级至 2.5.12（安全版本）</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292e">详情请参考</span><span style="background-color:#ffffff; color:#24292e"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Freleases%2Ftag%2F1.8.4" target="_blank">Release Notes</a><span style="background-color:#ffffff; color:#24292e">。感谢为该版本付出的所有贡献者：</span>@brotherlu-xcq, @code-ferry, @DollarB, @howiekang, @icodening, @Reagan1947, @Roger3581321, @sczyh30, @tain198127, @zhaoxinhu, @zhuyou1234</p>
                                        </div>
                                      
</div>
            