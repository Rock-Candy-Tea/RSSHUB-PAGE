
---
title: 'Eurynome Cloud 2.7.0.Beta4 发布，全面升级优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=854'
author: 开源中国
comments: false
date: Wed, 06 Apr 2022 07:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=854'
---

<div>   
<div class="content">
                                                                                            <p><strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。首个全面拥抱 Spring Authorization Server 的版本，基于Spring Boot 2.6.6、Spring Cloud 2021.0.1、Spring Cloud Alibaba 2021.0.1.0、 Spring Authorization Server 0.2.3、Nacos 2.0.4 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
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
 <li> <p>主要更新</p> 
  <ul> 
   <li> <p>[升级] Spring Authorization Server 版本升级至 0.2.3 版本</p> </li> 
   <li> <p>[升级] Spring Boot 版本升级至 2.6.6</p> </li> 
   <li> <p>[新增] 基于 Spring Authorization Server 0.2.3 最新代码调用方式，重构自定义 OAuth2 密码模式</p> </li> 
   <li> <p>[新增] 对 OAuth2 OIDC 认证模式的支持，补充前端 OIDC 认证相关配置操作</p> </li> 
   <li> <p>[新增] OAuth2 OIDC 认证方式下，对应的 /userinfo 接口调用支持 和 客户端注册支持</p> </li> 
   <li> <p>[新增] OAuth2 Authorization Code PKCE 认证模式支持</p> </li> 
   <li> <p>[新增] OAuth2 Client Credentials 模式下，提供 Refresh Token。</p> </li> 
   <li> <p>[新增] OAuth2 Client Credentials 模式下，支持使用 Scope 权限对接口进行验证。</p> </li> 
   <li> <p>[新增] 在已有的 oauth2-sdk-authorization-server 模块下，增加客户端 Scope 的权限配置功能，并与已有的用户权限体系解耦</p> </li> 
   <li> <p>[新增] 自定义 Social Credentials 认证模式，支持手机短信验证码、微信小程序、第三方应用登录</p> </li> 
   <li> <p>[修复] 在 OAuth2 OIDC 认证方式下，/userinfo 接口调用始终为 401 问题。</p> </li> 
   <li> <p>[修复] 自定义 Spring Authorization Server JPA 存储模式参数丢失，遗漏 Scope 设置，导致 /userinfo 调用失败问题</p> </li> 
   <li> <p>[修复] No AuthenticationProvider found for UsernamePasswordAuthenticationToken 问题导致的用户名无法登录问题</p> </li> 
   <li> <p>[修复] 服务启动过程中，由于异步操作与事务操作冲突，导致的 JetCache 数据存储产生并发异常</p> </li> 
   <li> <p>[修复] 改进 @Async 注解调用代码，解决由 jdk 自动代理与 CGlib 代理两种代理方式的区别造成代码抛出异常</p> </li> 
   <li> <p>[修复] 改进 OAuth2 基础操作代码，解决 Spring Authorization Server 部分配置不能设置为空值的问题</p> </li> 
   <li> <p>[修复] Spring Cloud Bus 进行远程事件发布时，所有事件监听代码均会接收数据，无法根据服务 Destination 定向处理的问题。</p> </li> 
   <li> <p>[优化] 优化 SecurityGlobalExceptionHandler，支持 OIDC 场景下对错误内容的拦截，并将其融合进整体错误体系</p> </li> 
   <li> <p>[优化] EndpointProperties 配置，区分系统涉及的 url 以及 endpoint，以便支持更多用途</p> </li> 
   <li> <p>[优化] 重构并抽象出策略事件 Event，以规范化大量使用的混合本地时间和远程事件的各类操作。</p> </li> 
   <li> <p>[优化] 规范化所有 Enum 类，使用统一方式为前端提供常量</p> </li> 
   <li> <p>[优化] 优化 OAuth2 应用管理前后端交互相关代码及 OpenApi 文档说明</p> </li> 
  </ul> </li> 
 <li> <p>其它更新</p> 
  <ul> 
   <li> <p>Spring boot admin 版本升级至 2.6.4</p> </li> 
   <li> <p>Redisson 版本升级至 3.17.0</p> </li> 
   <li> <p>Antisamy 版本升级至 1.6.6</p> </li> 
   <li> <p>Fastjson 版本升级至 1.2.80</p> </li> 
   <li> <p>Okhttps 版本升级至 3.4.6</p> </li> 
   <li> <p>Bce-java-sdk 版本升级至 0.10.202</p> </li> 
   <li> <p>Alipay-sdk-java 版本升级至 4.22.75.ALL</p> </li> 
   <li> <p>Qiniu-java-sdk 版本升级至 7.9.5</p> </li> 
   <li> <p>Logback 版本升级至 1.2.11</p> </li> 
  </ul> </li> 
 <li> <p>尝鲜注意事项</p> 
  <ol> 
   <li> <p>建议新建目录、单独检出 Eurynome Cloud 2.7.0 分支代码，以防对现有代码产生影响。</p> </li> 
   <li> <p>数据表结构以及 Nacos 存在较大变化，建议重新建库、重新导入 Nacos 配置。</p> </li> 
   <li> <p>支持 MySQL 数据库，但是尚未进行充份的验证和测试，为规避不必要的问题，建议直接使用 PostgreSQL 数据库。</p> </li> 
   <li> <p>Herodotus Engine 是独立的、可编译的、组件库式的工程，具体使用需要在其它 Spring Boot 工程中引入相关的组件模块。独立出的各个模块，已经同步至 Maven 中央仓库，检出 Eurynome Cloud 2.7.0 分支代码既可以直接使用。当然，也可以先检出 Herodotus Engine 工程，编译后再进行 Eurynome Cloud 项目的使用。</p> </li> 
   <li> <p>想要研究、学习、了解已有的模块代码，可以访问 Herodotus Engine 代码库，地址：[https://gitee.com/herodotus/herodotus-engine](https://gitee.com/herodotus/herodotus-engine)</p> </li> 
  </ol> </li> 
 <li><strong>友情提示：</strong> 
  <ul> 
   <li> <p>本次代码发布，为尝鲜预览版，请结合自己的实际需求，谨慎选择使用！</p> </li> 
  </ul> </li> 
</ul>
                                        </div>
                                      
</div>
            