
---
title: 'Eurynome Cloud 2.7.0.Beta3 发布，首个全面拥抱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1237'
author: 开源中国
comments: false
date: Wed, 23 Mar 2022 00:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1237'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。首个全面拥抱 Spring Authorization Server 的版本，基于Spring Boot 2.6.4、Spring Cloud 2021.0.1、Spring Cloud Alibaba 2021.0.1.0、 Spring Authorization Server 0.2.2、Nacos 2.0.4 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位</strong></p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<h2>[1]、发布背景</h2> 
<p>2021年11月8日 Spring 官方已经强烈建议使用 Spring Authorization Server 替换已经过时的 Spring Security OAuth2.0。距离 2022年5月28日，Spring Security OAuth2.0 结束生命周期还有两个月的时间，所以用 Spring Authorization Server 对已有的 Eurynome Cloud 微服务架构进行升级，以应对依赖组件停止维护的问题。</p> 
<h2>[2]、本次更新内容</h2> 
<ul> 
 <li> <p>重大更新</p> 
  <ul> 
   <li> <p>全面拥抱 Spring Authorization Server。基于 Spring Authorization Server 重新改版，替换即将停止维护的 Spring Security OAuth2。再也不用担心 Spring Security OAuth2 停止维护了。</p> </li> 
   <li> <p>基于 Spring Data JPA，重新构建 Spring Authorization Server 基础数据存储代码。替代原有 JDBC 数据访问方式，破除 Spring Authorization Server 原有数据存储局限，扩展为更符合实际应用的方式。配合自定义多级缓存加持，认证过程更加顺滑。</p> </li> 
   <li> <p>基于 Spring Authorization Server，在 OAuth 2.1 规范基础之上，增加自定义“密码”认证模式，以兼容现有基于 OAuth 2 规范的、前后端分离的应用可以平滑使用。</p> </li> 
   <li> <p>完全遵照 Spring Security 5 以及 Spring Authorization Server 的代码规范，进行 OAuth2 认证服务器核心代码的开发。</p> </li> 
   <li> <p>除了支持 Spring Authorization Server 的标准的Token加密校验方式外，还了增加支持自定义证书的 JWK Token 加密方式，可通过配置动态修改。</p> </li> 
   <li> <p>重新梳理并调整优化已有配置参数，让工程配置参数更加清晰，层级更加合理。同时，拆分原有使用内部类定义的配置参数，进一步由配置参数导致的代码耦合。</p> </li> 
   <li> <p>同步优化 Nacos 配置内容，采用 Spring Authorization Server 标准 Token 校验方式，新服务增加无须再增加配置文件和进行 Client 配置。</p> </li> 
   <li> <p>重新梳理本微服务架构内的错误体系及相关代码，已有的 Exception 类放入更合理的保重，无须再经过修改通用基础包中代码，即可便捷的将新的 Exception 融入到系统的错误体系中。同时，仍旧支持自定义错误码以及人机交互友好的自定义错误提示。</p> </li> 
   <li> <p>对已有代码进行了深度的“庖丁解牛”。严格遵照“单一职责”原则，根据各个组件的职责以及用途，拆解细化为多个各自独立组件模块，在最大程度上降低代码间的耦合。降低工程代码编译耗时，改进 CICD 效率，提升代码可维护性。</p> </li> 
   <li> <p>除已有的组件模块外，对现有工程代码分包也进一步调整，分包和逻辑更加清晰。</p> </li> 
  </ul> </li> 
 <li> <p>其它更新</p> 
  <ul> 
   <li> <p>优化接口权限鉴权逻辑，解决通配符类型权限与全路径权限冲突或重复的问题，实现重复权限剔除并以最大化匹配方式进行权限匹配逻辑。</p> </li> 
   <li> <p>前端部分功能配合后端功能变化进行同步修改。基于 Spring Authorization Server 新的数据存储结构，重新定义应用管理、客户端管理功能，同步修改前后端代码，管理更加便捷</p> </li> 
   <li> <p>由于 Spring Authorization Server 机制和模式的变化，原有团队管理功能已不符合实际，相关功能已删除。</p> </li> 
   <li> <p>原有 Herodotus Engine 工程中的模块，根据实际代码变更。代码包以及代码进行了一定的优化和整合。</p> </li> 
   <li> <p>核心依赖 dependencies 采用参数方式，统一定义版本号方便其它依赖工程覆盖和修改版本号。</p> </li> 
   <li> <p>改进错误信息展示，同时支持 Mvc 和 Json 两种方式，通过浏览器操作的 Mvc 方式错误也可以通过界面展示了。</p> </li> 
  </ul> </li> 
 <li> <p>尝鲜注意事项</p> 
  <ol> 
   <li> <p>建议新建目录、单独检出 Eurynome Cloud 2.7.0 分支代码，以防对现有代码产生影响。</p> </li> 
   <li> <p>数据表结构以及 Nacos 存在较大变化，建议重新建库、重新导入 Nacos 配置。</p> </li> 
   <li> <p>系统支持 MySQL 数据库，但是尚未进行充分的验证和测试，为规避不必要的问题，建议直接使用 PostgreSQL 数据库。</p> </li> 
   <li> <p>Herodotus Engine 是独立的、可编译的、组件库式的工程，具体使用需要在其它 Spring Boot 工程中引入相关的组件模块。独立出的各个模块，已经同步至 Maven 中央仓库，检出 Eurynome Cloud 2.7.0 分支代码既可以直接使用。当然，也可以先检出 Herodotus Engine 工程，编译后再进行 Eurynome Cloud 项目的使用。</p> </li> 
   <li> <p>想要研究、学习、了解已有的模块代码，可以访问 Herodotus Engine 代码库，地址：[https://gitee.com/herodotus/herodotus-engine](https://gitee.com/herodotus/herodotus-engine)</p> </li> 
  </ol> </li> 
 <li><strong>友情提示：</strong> 
  <ul> 
   <li> <p>本次代码发布，为尝鲜预览版，请结合自己的实际需求，谨慎选择使用！</p> </li> 
   <li> <p><strong>Spring Authorization Server 也在不断的改进中，0.2.3 和 0.2.2 代码就有较大差异，因此暂时不要将该版本用于生产，随着 Spring Authorization Server 升级，代码还会进行较大的修改。</strong></p> <p> </p> </li> 
  </ul> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            