
---
title: 'Eurynome Cloud 2.7.0.50 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8369'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 08:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8369'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。首个全面拥抱 Spring Authorization Server 的版本，基于Spring Boot 2.7.0、Spring Cloud 2021.0.3、Spring Cloud Alibaba 2021.0.1.0、 Spring Authorization Server 0.3.0、Nacos 2.1.0 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位</strong></p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<h2>[1]、发布背景</h2> 
<p>2021年11月8日 Spring 官方已经强烈建议使用 Spring Authorization Server 替换已经过时的 Spring Security OAuth2.0。</p> 
<p>在 Spring Security OAuth2 彻底停止维护、Spring Boot 2.7.0 正式发布之时，又恰逢 Eurynome Cloud 开源一周年之际，推出基于 Spring Authorization Server 0.3.0、Spring Boot 2.7.0、Spring Cloud 2021.0.3、Spring Cloud Alibaba 2021.0.1.0 和 Nacos 2.1.0 的全新正式版本，细节满满，欢迎品鉴。</p> 
<h2>[2]、重要说明</h2> 
<p>Eurynome Cloud 自 v2.7.0.20 版本，开始全面使用 JDK 17。自该版本以后，系统代码将不再兼容 JDK 8，敬请悉知！</p> 
<p>升级使用 JDK 17 的主要原因：</p> 
<ol> 
 <li>Spring Authorization Server 0.3.0 版本，已经开始使用 JDK 11 进行代码编译。该版本在 JDK 8 下已无法编译成功，想要使用必须要升级 JDK 版本。</li> 
 <li>2022 年 11 月，Spring Boot 3 将会发布，最低版本要求 JDK 17。因此，直接将 JDK 版本升级至 17，同时为升级至 Spring Boot 3 提前做铺垫准备。</li> 
</ol> 
<h2>[3]、本次更新内容</h2> 
<ul> 
 <li>重要更新 
  <ul> 
   <li>Spring Boot Admin 版本升级至 2.7.0</li> 
  </ul> </li> 
 <li>主要更新 
  <ul> 
   <li>[新增] 新增读取全部角色和读取全部 Scope 接口，删除已有基于权限类别读取权限接口</li> 
   <li>[新增] 自定义 Validation 注解 EnumeratedValue，支持对指定枚举的 name 或 ordinal 值进行校验，提升接口的健壮性。</li> 
   <li>[新增] Spring Data JPA 分页查询数据排序支持。通过接口动态传递额外参数，实现分页数据的排序。</li> 
   <li>[修正] 修复幂等和防刷拦截器读取配置不正确问题。优先读取注解配置参数，如注解为设置参数值，则默认使用统一配置参数。</li> 
   <li>[优化] 优化 Security 工具类，使用 Spring Security 最新的获取 PasswordEncoder 工厂类重构密码创建方法和密码校验方法。</li> 
   <li>[优化] 优化幂等和防刷注解和配置的默认参数值，设置更合理的参数，解决幂等和防刷过于敏感问题。</li> 
  </ul> </li> 
 <li>依赖更新 
  <ul> 
   <li>docker-maven-plugin 版本升级至 0.40.1</li> 
   <li>maven-embedder 版本升级至 3.8.6</li> 
   <li>maven-compat 版本升级至 3.8.6</li> 
   <li>redisson 版本升级至 3.17.4</li> 
   <li>minio 版本升级至 8.4.2</li> 
   <li>hutool 版本升级至 5.8.3</li> 
   <li>weixin-java-sdk 版本升级至 4.3.5.B</li> 
   <li>tencentcloud-sdk-java 版本升级至 3.1.530</li> 
   <li>qiniu-java-sdk 版本升级至 7.11.0</li> 
  </ul> </li> 
</ul> 
<h2>[4]、Eurynome Cloud 2.7.X 主要变化</h2> 
<ul> 
 <li> <p>基于 <code>Spring Authorization Server</code> 深度定制:</p> 
  <ul> 
   <li>基于 <code>Spring Data JPA</code>，重新构建 <code>Spring Authorization Server</code> 基础数据存储代码，替代原有 JDBC 数据访问方式，破除 <code>Spring Authorization Server</code> 原有数据存储局限，扩展为更符合实际应用的方式和设计。</li> 
   <li>基于 <code>Spring Authorization Server</code>，在 OAuth 2.1 规范基础之上，增加自定义“密码”认证模式，以兼容现有基于 OAuth 2 规范的、前后端分离的应用。</li> 
   <li>基于 <code>Spring Authorization Server</code>，在 OAuth 2.1 规范基础之上，增加自定义Social Credentials 认证模式，支持手机短信验证码、微信小程序、第三方应用登录。</li> 
   <li>遵照 <code>Spring Security 5</code> 以及 <code>Spring Authorization Server</code> 的代码规范，进行 OAuth2 认证服务器核心代码的开发，遵照其使用 Jackson 反序列化的方式， 增加大量自定义 Jackson Module。</li> 
   <li>支持 <code>Spring Authorization Server</code> 的标准的Token加密校验方式外，还了增加支持自定义证书的 Token 加密方式，可通过配置动态修改</li> 
   <li>支持 OAuth2 OIDC 认证模式，补充前端 OIDC 认证相关配置操作，以及对应的 /userinfo 接口调用支持 和 客户端注册支持</li> 
   <li>支持 OAuth2 Authorization Code PKCE 认证模式</li> 
   <li>扩展 <code>Spring Authorization Server</code> 默认的 <code>Client Credentials</code> 模式，实现 Refresh Token 的创建。</li> 
   <li>扩展 <code>Spring Authorization Server</code> 默认的 <code>Client Credentials</code> 模式，实现真正的使用 Scope 权限对接口进行验证。 增加客户端 Scope 的权限配置功能，并与已有的用户权限体系解耦</li> 
   <li>自定义 <code>Spring Authorization Server</code> 授权码模式登录认证页面和授权确认页面，授权码模式登录采用数据加密传输。支持多种验证码类型，暂不支持行为验证码。</li> 
  </ul> </li> 
 <li> <p>代码结构的大规模调整和优化：</p> 
  <ul> 
   <li>对原有代码进行了深度的“庖丁解牛”，严格遵照“单一职责”原则，根据各个组件的职责以及用途，将整个工程拆解细化为多个各自独立组件模块，在最大程度上降低代码间的耦合，也更容易聚焦和定位问题。</li> 
   <li>将通用化组件提取为独立工程，独立编译、按需选用，极大的降低系统主工程代码量。相关组件也已上传至 Maven 中央仓库，降低系统主工程工程代码编译耗时，改进和提升 CICD 效率，</li> 
   <li>原有主工程代码结构也进行了深化调整，代码分包更加合理，代码逻辑也更加清晰。</li> 
  </ul> </li> 
</ul> 
<h2>[5]、额外说明</h2> 
<ol> 
 <li>本项目以后将主要维护  Spring Authorization Server  版本，原有基于 Spring Security OAuth2  的版本已经移至 spring-security-oauth2 分支，可以从该分支或发行版页面获取历史版本继续使用。后期会根据 ISSUE 以及使用用户反馈情况，再行决定是否继续维护  Spring Security OAuth2 版本。</li> 
 <li>最新版本代码，暂时继续沿用原有基于 Vue2、Vuetify2、Typescript开发的前端系统。基于 Vue3、Vite2、Quasar、Pinia、Typescript 的新版前端正在加进开发中，预计本月底发布。</li> 
 <li>原有基于 Vue2、Vuetify2、Typescript 开发的前端，由于使用了过渡性 Typescript IOC 组件，以及依赖组件版本限制等问题，初次接触该项目在编译过程中会出现一些问题，请移步至本项目在线文档，详见“常见问题”章节。</li> 
</ol> 
<p> </p>
                                        </div>
                                      
</div>
            