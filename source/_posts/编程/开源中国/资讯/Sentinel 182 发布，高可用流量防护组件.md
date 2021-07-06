
---
title: 'Sentinel 1.8.2 发布，高可用流量防护组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ae81d5d3bbafa8a9a4f1f7871c8459cab3b.png'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 10:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ae81d5d3bbafa8a9a4f1f7871c8459cab3b.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel" target="_blank">Sentinel</a><span style="background-color:#ffffff; color:#333333"> 是阿里巴巴开源的，面向分布式服务架构的高可用流量防护组件，主要以流量为切入点，从流量控制、流量整形、依赖隔离、熔断降级、系统自适应保护等多个维度来帮助开发者保障微服务的稳定性。Sentinel 承接了阿里巴巴近 10 年的双十一大促流量的核心场景，例如秒杀、冷启动、消息削峰填谷、集群流量控制、实时熔断下游不可用服务等，是保障微服务高可用的利器，原生支持 Java/Go/C++ 等多种语言，并且提供 Istio/Envoy/MOSN 全局流控支持来为 Service Mesh 提供高可用防护的能力。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt src="https://oscimg.oschina.net/oscnet/up-ae81d5d3bbafa8a9a4f1f7871c8459cab3b.png" referrerpolicy="no-referrer"></span></p> 
<p>本周 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Freleases%2Ftag%2F1.8.2" target="_blank">Sentinel 1.8.2</a> 正式发布，带来了多项特性和改进。主要变更如下：</p> 
<ul> 
 <li>完善 TimeUtil 在不同流量大小情况下的性能，低峰期可降低 CPU 占用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F1746" target="_blank">#1746</a>)</li> 
 <li><code>@SentinelResource</code> 注解的 blockHandler/fallback/defaultFallback 现在支持 private-level 函数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F2163" target="_blank">#2163</a>)</li> 
 <li>新增 <code>sentinel-transport-spring-mvc</code> 模块，支持直接将 Spring Web 作为 command center (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F1957" target="_blank">#1957</a>)</li> 
 <li>Redis 动态数据源支持 Redis Cluster 模式 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F1751" target="_blank">#1751</a>)</li> 
 <li>部分通用配置项支持通过系统环境变量进行配置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F2154" target="_blank">#2154</a>)</li> 
 <li>Dashboard 完善权限管理模块的扩展性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fpull%2F2059" target="_blank">#2059</a>)</li> 
</ul> 
<p style="text-align:start">详情请参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Freleases%2Ftag%2F1.8.2" target="_blank">Release Notes</a>。感谢为该版本付出的所有贡献者：@Amitbhave, @Anilople, @brotherlu-xcq, @cdfive, @drgnchan, @goodjava, @gvma, @huakai-zhang, @jasonjoo2010, @jiajiangnan, @JJFly-JOJO, @JerryChin, @liqiangz, @quaff, @Roger3581321, @ShubhamPalriwala, @Slideee, @SparkLee, @sczyh30, @shenbaoyong, @ss-superman, @VegetaPn, @wutingjia, @wuwen5, @zhangyunan1994</p> 
<p style="text-align:start"><span style="background-color:#ffffff; color:#24292e">Sentinel 正在朝着 2.0 云原生、自适应、标准化的方向演进。我们非常欢迎感兴趣的开发者参与贡献，若您有意愿参与贡献，欢迎联系我们加入 Sentinel 贡献小组一起成长。我们会定期给活跃贡献者寄送小礼品，核心贡献者会提名为 committer，一起主导社区的演进。Now let's start hacking!</span></p>
                                        </div>
                                      
</div>
            