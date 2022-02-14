
---
title: 'Eurynome Cloud 2.7.0 预览版发布，庖丁解牛，技经肯綮'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1488'
author: 开源中国
comments: false
date: Mon, 14 Feb 2022 10:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1488'
---

<div>   
<div class="content">
                                                                                            <p><strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。基于Spring Boot 2.6.3、Spring Cloud 2021.0.0、Spring Cloud Alibaba 2021.1、Nacos 2.0.4 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位</strong></p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<h2>本次更新内容:</h2> 
<ul> 
 <li><strong>重要变更</strong> 
  <ul> 
   <li>将现有 Eurynome Cloud 微服务架构，进行了深度的“庖丁解牛”。将完整的微服务架构，根据各个组件的职责以及用途，拆解细化为多个各自独立组件模块，在最大程度上降低代码间的耦合。并将组件模块单独提取为一个独立的工程项目。</li> 
   <li>已有 Eurynome Cloud 微服务架构，根据新的模块化代码结构，进行了重构。</li> 
  </ul> </li> 
 <li><strong>升级目的</strong> 
  <ul> 
   <li>2021年11月8日 Spring 官方已经强烈建议使用 Spring Authorization Server 替换已经过时的 Spring Security OAuth2.0。距离 Spring Security OAuth2.0 结束生命周期还有小半年的时间，所以准备用 Spring Authorization Server 对已有的 Eurynome Cloud 微服务架构进行升级</li> 
   <li>Eurynome Cloud 微服务架构，一直遵循“高内聚、低耦合”的原则，在开发和维护的过程中不断优化已有代码，尽一切可能降低代码的耦合性。但是，毕竟所有的代码都堆积在同一个工程中，代码间的过度依赖和互相耦合还是较为严重。这为 Spring Authorization Server 替换 Spring Security OAuth2.0 带来了较大的阻力和难度。</li> 
   <li>为了进一步降低代码与代码间、模块与模块间的耦合度，进行了本次版本更新，并衍生了 Herodotus Engine 工程。</li> 
   <li>同时，本次版本迭代，也是为了后期升级使用 Spring Boot 3.X 和 JDK 17，做先期主备。</li> 
  </ul> </li> 
 <li>新模式特点 
  <ol> 
   <li>严格遵照“单一职责”原则，进行各个模块的划分和代码拆解。</li> 
   <li>严格遵循 Spring Boot 编码规则和命名规则。</li> 
   <li>大多数模块均支持 @EnableXXX注解 和 starter，不仅提升了模块使用的便捷性，同时在开发使用过程中，让 Spring Bean 的注入顺序更加可控和便于理解。</li> 
   <li>借鉴 Spring Boot 模块化设计思想，通过接口化编程、策略化 Bean 注入 以及丰富的自定义 @ConditionalXXX 注解，让模块的添加和使用更加灵活便捷。</li> 
   <li>各模块既可以综合在一起使用，也可以在其它 Spring Boot 工程中独立使用</li> 
  </ol> </li> 
 <li><strong>新模式优势</strong> 
  <ol> 
   <li>虽然模块看似很多，但是每个模块职责单一、代码清晰，更有利于聚焦和定位问题。</li> 
   <li>通过对微服务架构的“庖丁解牛”，初学者不再需要在代码的海洋里“遨游”，通过针对性地了解各个模块，以点带面快速掌握微服务架构整体结构。</li> 
   <li>模块间的依赖极大的降低，想要替换为 Spring Authorization Server，影响到的代码和范围将会很小。该工程也是使用 Spring Authorization Server 的前序工作</li> 
   <li>每个模块均是最小化依赖第三包，规避依赖包过度依赖，特别是 starter 过多依赖，导致不可预知、难以调试、不好修改等问题。</li> 
   <li>降低微服务系统代码量，独立组件可提前编译并上传至Maven仓库，降低工程代码编译耗时，改进 CICD 效率。</li> 
  </ol> </li> 
 <li><strong>尝鲜注意事项</strong> 
  <ol> 
   <li>建议新建目录、单独检出 Eurynome Cloud 2.7.0 分支代码，以防对现有代码产生影响。</li> 
   <li>独立出的各个模块，已经同步至 Maven 中央仓库，检出 Eurynome Cloud 2.7.0 分支代码既可以直接使用。当然，也可以先检出 Herodotus Engine 工程，编译后再进行 Eurynome Cloud 项目的使用。</li> 
   <li>想要研究、学习、了解已有的模块代码，可以访问 Herodotus Engine 代码库，地址：[https://gitee.com/herodotus/herodotus-engine](https://gitee.com/herodotus/herodotus-engine)</li> 
   <li>如果之前已经使用、部署过 Eurynome Cloud 微服务系统，那么尝鲜使用 2.7.0.Beta1 版，无须修改和变更数据库。但是需要更新 Nacos 配置，具体变化可自行详细对比工程中Nacos 配置文件。前端工程无须做任何修改，即可使用该版本后端系统。</li> 
   <li>Herodotus Engine 是独立的、可编译的、组件库式的工程，具体使用需要在其它 Spring Boot 工程中引入相关的组件模块。</li> 
  </ol> </li> 
</ul> 
<blockquote> 
 <p><strong>友情提示：</strong></p> 
 <p>本次代码发布，为尝鲜预览版，请结合自己的实际需求，谨慎选择使用！</p> 
</blockquote>
                                        </div>
                                      
</div>
            