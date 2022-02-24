
---
title: 'Eurynome Cloud 2.6.3.30 发布 Spring Cloud 升级 2021.0.1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2ac394be433d321963eafb43ec6903d90b6.png'
author: 开源中国
comments: false
date: Thu, 24 Feb 2022 12:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2ac394be433d321963eafb43ec6903d90b6.png'
---

<div>   
<div class="content">
                                                                                            <p><strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。基于Spring Boot 2.6.3、Spring Cloud 2021.0.1、Spring Cloud Alibaba 2021.1、Nacos 2.0.4 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位</strong></p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<h2>[1]、本次更新内容</h2> 
<ul> 
 <li>主要更新 
  <ul> 
   <li>Spring Cloud 版本升级至 2021.0.1</li> 
  </ul> </li> 
 <li>其它更新 
  <ul> 
   <li>Hutool 版本升级至 5.17.21</li> 
   <li>WxJava 版本升级至 4.2.6.B</li> 
   <li>alipay-sdk-java 版本升级至 4.22.37.ALL</li> 
  </ul> </li> 
</ul> 
<h2>[2]、额外说明</h2> 
<p>近期发布版本的频次降低，更新的内容也比较少。主要原因一方面是恰逢新春佳节，另一方面也是最主要的原因也是为后期的更新迭代做积极的准备和开发工作。</p> 
<p>主要是因为后期的更新迭代对现有系统影响比较大：</p> 
<p>1. Spring 官宣 spring-security-oauth 即将不再维护。虽然 spring-security-oauth2-autoconfigure 等组件包依旧可用，现目前 Spring 依赖的 spring-security-oauth2-autoconfigure 版本比较低，高版本所有的代码均已标记为过期。</p> 
<p><img alt height="624" src="https://oscimg.oschina.net/oscnet/up-2ac394be433d321963eafb43ec6903d90b6.png" width="846" referrerpolicy="no-referrer"></p> 
<p>所以近期一直在进行使用 Spring Authorization Server 替换现有 spring-security-oauth 的开发工作。包括 Herodotus Engine 工程的提取，以及 Eurynome Cloud v2.7.0.Beta2 的开发，均是为了降低已有系统代码间耦合，为 Spring Authorization Server 使用和升级铺路。</p> 
<p>2. Spring Boot 3 下一代框架将基于 Java 17。Kafka 3.0也已经宣布弃用 Java 8 的支持。Hibernate宣布他们目前积极维护的分支都支持 Java17。Java生态正在潜移默化进入一个新的时代，所以开始着手准备支持 Java 17 势在必行。</p> 
<p>虽然说 Java 一直都是向下兼容的，但是微服务架构依赖的第三方开源包非常多，势必会存在一些依赖组件包在 Java 17 下使用不畅的情况，所以需要及时更新或替换。不断的升级更新，跟随业界的发展趋势，用新的技术来改善开发和使用。同时，规避处于长期不更新导致后期即使很小的更新都会牵一发而动全身的尴尬境地。</p> 
<blockquote> 
 <p><strong>还请持续关注和支持 Eurynome Cloud。</strong></p> 
</blockquote>
                                        </div>
                                      
</div>
            