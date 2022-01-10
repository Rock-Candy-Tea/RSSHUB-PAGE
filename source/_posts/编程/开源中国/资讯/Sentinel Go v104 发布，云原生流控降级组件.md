
---
title: 'Sentinel Go v1.0.4 发布，云原生流控降级组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0e0fd5ed3e12ddf31bf4b454fe35d69dfcf.png'
author: 开源中国
comments: false
date: Mon, 10 Jan 2022 11:10:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0e0fd5ed3e12ddf31bf4b454fe35d69dfcf.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel" target="_blank">Sentinel</a><span style="color:#24292e"> 是阿里巴巴开源的，面向分布式、云原生服务架构的高可用防护组件，主要以流量为切入点，从限流、流量整形、并发控制、熔断降级、系统自适应过载保护等多个维度来帮助开发者保障微服务的稳定性。Sentinel 承接了阿里巴巴近 10 年的双十一大促流量的核心场景，例如秒杀、冷启动、消息削峰填谷、集群流量控制、实时熔断下游不可用服务、业务防抖动等，是保障微服务高可用的利器，原生支持 Java/Go/C++/Rust 等多种语言，并且提供 Istio/Envoy 全局流控支持来为 Service Mesh 提供高可用防护的能力。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fsentinel-golang" target="_blank">Sentinel Go</a> 是 Sentinel 原生的 Go 版本实现，已正式 GA，对齐高可用防护和容错的核心能力（流控、并发控制、熔断降级、系统自适应过载保护、热点流量识别与管控），并推出 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsentinel-group%2Fsentinel-go-datasource-k8s-crd" target="_blank">Kubernetes CRD data-source</a> 等云原生相关的整合。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#24292e"><img alt height="391" src="https://oscimg.oschina.net/oscnet/up-0e0fd5ed3e12ddf31bf4b454fe35d69dfcf.png" width="700" referrerpolicy="no-referrer"></span></p> 
<p>近期 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fsentinel-golang%2Freleases%2Ftag%2Fv1.0.4" target="_blank">Sentienl Go v1.0.4 版本</a><span style="color:#24292e">正式发布，带来了 Prometheus metric exporter、熔断恢复策略强化、Apollo 数据源等多项特性与改进。同时，我们也对<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsentinel-group%2Fsentinel-go-datasource-k8s-crd" target="_blank">Sentinel Go Kubernetes CRD data-source</a><span style="color:#24292e"><span> </span>进行了升级更新，从而可以支持最新的 Kubernetes 1.22 及以上版本。</span></p> 
<p>详细信息可以参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fsentinel-golang%2Freleases%2Ftag%2Fv1.0.4" target="_blank">Release Notes</a>。<span style="background-color:#ffffff; color:#24292e">感谢为该版本付出的所有贡献者：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fansiz" target="_blank">@ansiz</a><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCasper-Mars" target="_blank">@Casper-Mars</a><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fecafkoob" target="_blank">@ecafkoob</a><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flouyuting" target="_blank">@louyuting</a><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fluckyxiaoqiang" target="_blank">@luckyxiaoqiang</a><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsanxun0325" target="_blank">@sanxun0325</a></p>
                                        </div>
                                      
</div>
            