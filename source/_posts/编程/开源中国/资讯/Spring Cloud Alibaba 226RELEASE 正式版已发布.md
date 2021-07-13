
---
title: 'Spring Cloud Alibaba 2.2.6.RELEASE 正式版已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-34acb4a3be24ca241ec6b226606e7efd76e.png'
author: 开源中国
comments: false
date: Tue, 13 Jul 2021 07:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-34acb4a3be24ca241ec6b226606e7efd76e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2><img height="224" src="https://oscimg.oschina.net/oscnet/up-34acb4a3be24ca241ec6b226606e7efd76e.png" width="978" referrerpolicy="no-referrer"></h2> 
<h2>一、什么是Spring Cloud Alibaba</h2> 
<p style="text-align:start">Spring Cloud Alibaba 致力于提供微服务开发的一站式解决方案。此项目包含开发分布式应用微服务的必需组件，方便开发者通过 Spring Cloud 编程模型轻松使用这些组件来开发分布式应用服务。</p> 
<p style="text-align:start">依托 Spring Cloud Alibaba，您只需要添加一些注解和少量配置，就可以将 Spring Cloud 应用接入阿里微服务解决方案，通过阿里中间件来迅速搭建分布式应用系统。</p> 
<p style="text-align:start">参考文档 请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fwiki" target="_blank">WIKI</a> 。</p> 
<p style="text-align:start">为 Spring Cloud Alibaba 贡献代码请参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fwiki%2F%25E5%25A6%2582%25E4%25BD%2595%25E8%25B4%25A1%25E7%258C%25AE%25E4%25BB%25A3%25E7%25A0%2581" target="_blank">如何贡献</a> 。</p> 
<h2 style="text-align:start">二、主要功能</h2> 
<ul> 
 <li><strong>服务限流降级</strong>：默认支持 WebServlet、WebFlux, OpenFeign、RestTemplate、Spring Cloud Gateway, Zuul, Dubbo 和 RocketMQ 限流降级功能的接入，可以在运行时通过控制台实时修改限流降级规则，还支持查看限流降级 Metrics 监控。</li> 
 <li><strong>服务注册与发现</strong>：适配 Spring Cloud 服务注册与发现标准，默认集成了 Ribbon 的支持。</li> 
 <li><strong>分布式配置管理</strong>：支持分布式系统中的外部化配置，配置更改时自动刷新。</li> 
 <li><strong>消息驱动能力</strong>：基于 Spring Cloud Stream 为微服务应用构建消息驱动能力。</li> 
 <li><strong>分布式事务</strong>：使用 @GlobalTransactional 注解， 高效并且对业务零侵入地解决分布式事务问题。</li> 
 <li><strong>阿里云对象存储</strong>：阿里云提供的海量、安全、低成本、高可靠的云存储服务。支持在任何应用、任何时间、任何地点存储和访问任意类型的数据。</li> 
 <li><strong>分布式任务调度</strong>：提供秒级、精准、高可靠、高可用的定时（基于 Cron 表达式）任务调度服务。同时提供分布式的任务执行模型，如网格任务。网格任务支持海量子任务均匀分配到所有 Worker（schedulerx-client）上执行。</li> 
 <li><strong>阿里云短信服务</strong>：覆盖全球的短信服务，友好、高效、智能的互联化通讯能力，帮助企业迅速搭建客户触达通道。</li> 
</ul> 
<h2>三、组件</h2> 
<p style="text-align:start"><strong>Sentinel</strong>：把流量作为切入点，从流量控制、熔断降级、系统负载保护等多个维度保护服务的稳定性。</p> 
<p style="text-align:start"><strong>Nacos</strong>：一个更易于构建云原生应用的动态服务发现、配置管理和服务管理平台。</p> 
<p style="text-align:start"><strong>RocketMQ</strong>：一款开源的分布式消息系统，基于高可用分布式集群技术，提供低延时的、高可靠的消息发布与订阅服务。</p> 
<p style="text-align:start"><strong>Dubbo</strong>：Apache Dubbo™ 是一款高性能 Java RPC 框架。</p> 
<p style="text-align:start"><strong>Seata</strong>：阿里巴巴开源产品，一个易于使用的高性能微服务分布式事务解决方案。</p> 
<p style="text-align:start"><strong>Alibaba Cloud OSS</strong>: 阿里云对象存储服务（Object Storage Service，简称 OSS），是阿里云提供的海量、安全、低成本、高可靠的云存储服务。您可以在任何应用、任何时间、任何地点存储和访问任意类型的数据。</p> 
<p style="text-align:start"><strong>Alibaba Cloud SchedulerX</strong>: 阿里中间件团队开发的一款分布式任务调度产品，提供秒级、精准、高可靠、高可用的定时（基于 Cron 表达式）任务调度服务。</p> 
<p style="text-align:start"><strong>Alibaba Cloud SMS</strong>: 覆盖全球的短信服务，友好、高效、智能的互联化通讯能力，帮助企业迅速搭建客户触达通道。</p> 
<h2 style="text-align:start">四、2.2.6.RELEASE版本更新内容</h2> 
<h3>4.1 增强功能</h3> 
<ul> 
 <li> <p>【Nacos发现】</p> 
  <ul> 
   <li>支持注册快速失败的配置项<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2104" target="_blank">#2104</a></li> 
  </ul> </li> 
 <li> <p>[Dubbo]</p> 
  <ul> 
   <li>使用修订版来重构 dubbo 集成<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2101" target="_blank">#2101 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2121" target="_blank">#2121</a></li> 
  </ul> </li> 
</ul> 
<h3>4.2 BUG修复</h3> 
<ul> 
 <li> <p>【Nacos发现】</p> 
  <ul> 
   <li>如果 dns 不起作用，则修复 nacos 在 k8s 中不起作用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fnacos%2Fissues%2F5291" target="_blank">alibaba/nacos#5291</a></li> 
   <li>修复实例不在默认组下时无法获取实例的问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2113" target="_blank">#2113</a></li> 
   <li>修复 NacosWatch 影响 zipkin 追踪<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fissues%2F2140" target="_blank">#2140</a></li> 
  </ul> </li> 
 <li> <p>[Dubbo]</p> 
  <ul> 
   <li>修复组聚合在 SCA <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F1992" target="_blank">#1992 中不工作的问题</a></li> 
   <li>修复 SCA dubbo TagRouter 元数据错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fissues%2F2031" target="_blank">#2031 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2037" target="_blank">#2037</a></li> 
   <li>修复在服务更改期间发生的“注册表中没有可用的提供程序” <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fissues%2F2007" target="_blank">#2007</a></li> 
   <li>修复 dubbo cloud 无法正确注册到 consule <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fissues%2F2157" target="_blank">#2157</a></li> 
  </ul> </li> 
 <li> <p>[Sentinel]</p> 
  <ul> 
   <li>使用 NacosDataSource 修复 ak/sk 在哨兵上不起作用的问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2135" target="_blank">#2135</a></li> 
   <li>修复无法生成 SentinelFeignClient <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fissues%2F2137" target="_blank">#2137 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fissues%2F2122" target="_blank">#2122 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fissues%2F2107" target="_blank">#2107</a></li> 
   <li>修复使用 resttemplate 时丢失的异常<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fissues%2F2044" target="_blank">#2044 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fissues%2F1346" target="_blank">#1346</a></li> 
  </ul> </li> 
 <li> <p>[文档]</p> 
  <ul> 
   <li>文档改进<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2090" target="_blank">#2090 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2050" target="_blank">#2050</a></li> 
   <li>添加重量路线<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2159" target="_blank">#2159</a></li> 
  </ul> </li> 
 <li> <p>[例子]</p> 
  <ul> 
   <li>示例代码重新格式化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2015" target="_blank">#2015</a></li> 
  </ul> </li> 
</ul> 
<h3>4.3 参考文档</h3> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring-cloud-alibaba-group.github.io%2Fgithub-pages%2Fhoxton%2Fen-us%2Findex.html" target="_blank">英文版</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring-cloud-alibaba-group.github.io%2Fgithub-pages%2Fhoxton%2Fzh-cn%2Findex.html" target="_blank">中文版(中文)</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Faliyun-spring-boot" target="_blank">阿里云商用组件</a></p> </li> 
</ul> 
<p style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">2.2.6.RELEASE 兼容 Spring Cloud Hoxton.SR9，加油！🍺</span></span></p> 
<p style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">Spring Cloud Alibaba 现已上线<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstart.spring.io%2F" target="_blank">Spring Initializr</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstart.aliyun.com%2F" target="_blank">Aliyun Java Initializr</a>！</span></span></p> 
<h3 style="text-align:start">4.4 依赖升级</h3> 
<ul> 
 <li>[Nacos] 升级到 Nacos 客户端 1.4.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fpull%2F2097" target="_blank">#2097</a></li> 
</ul> 
<h2>五、应用案例</h2> 
<p><a href="https://gitee.com/matevip/matecloud">MateCloud</a> 是基于Spring Cloud Alibaba的微服务低代码开发平台。</p>
                                        </div>
                                      
</div>
            