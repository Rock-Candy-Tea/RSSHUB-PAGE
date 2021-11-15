
---
title: 'Eurynome Cloud v2.5.6.50 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=882'
author: 开源中国
comments: false
date: Mon, 15 Nov 2021 15:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=882'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Eurynome Cloud v2.5.6.50 已经发布。</p> 
<p><strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。基于Spring Boot 2.5.6、Spring Cloud 2020.0.4、Spring Cloud Alibaba 2021.1、Nacos 2.0.3 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位</strong></p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<p><strong>本次更新内容</strong></p> 
<ul> 
 <li>重大更新 
  <ol> 
   <li>重构平台Engine代码，提取并新建 Cache、 Web、 Message 等代码模块。代码逻辑更内聚、模块职责更清晰。规避由于代码包以及模块间过度依赖，而导致模块使用过程中必须通过排除依赖或排除注入才能正常使用模块的问题。从根本上根除，由于过度依赖导致 spring-integration、spring-actuator 等组件在不受控的状态下启动或检查额外依赖组件问题。</li> 
   <li>增加 Sentinel 配置持久化机制。默认使用 Nacos 进行配置持久化存储与更新。</li> 
   <li>原 Management 服务名称变更为 Monitor，独立出 Management 服务作为平台各项配置统一管理服务。</li> 
   <li>Spring Boot Admin 升级至 2.5.4 版本</li> 
  </ol> </li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.6.50">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.6.50</a></p>
                                        </div>
                                      
</div>
            