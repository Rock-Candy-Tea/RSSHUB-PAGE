
---
title: 'Eurynome Cloud 2.7.0.0 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9175'
author: 开源中国
comments: false
date: Mon, 23 May 2022 00:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9175'
---

<div>   
<div class="content">
                                                                                            <h2>企业级技术中台微服务架构与服务能力开发平台</h2> 
<p>Eurynome Cloud是一款企业级微服务架构和服务能力开发平台。基于Spring Boot 2.7.0、Spring Cloud 2021.0.2、Spring Cloud Alibaba 2021.0.1.0、Spring Authorization Server 0.2.3、Nacos 2.1.0 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能，代码简洁，架构清晰，非常适合学习和企业作为基础框架使用。</p> 
<h2>平台定位</h2> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<h2>[1]、发布背景</h2> 
<p>2021年11月8日 Spring 官方已经强烈建议使用 Spring Authorization Server 替换已经过时的 Spring Security OAuth2.0。距离 2022年5月28日，Spring Security OAuth2.0 结束生命周期还有几天的时间，所以用 Spring Authorization Server 对已有的 Eurynome Cloud 微服务架构进行升级，以应对依赖组件停止维护的问题。</p> 
<h2>[2]、升级说明</h2> 
<p>在 <code>Spring Security OAuth2</code> 彻底停止维护、Spring Boot 2.7.0 正式发布之时，又恰逢 <code>Eurynome Cloud</code> 开源一周年之际，推出基于Spring Authorization Server 0.2.3、Spring Boot 2.7.0、Spring Cloud 2021.0.2、Spring Cloud Alibaba 2021.0.1.0 和 Nacos 2.1.0 的全新正式版本。</p> 
<h2>[3]、新版特点</h2> 
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
<h2>[4]、细节品鉴</h2> 
<p>俗话说：不看“广告”，看“疗效”。本项目除了将微服务应用涉及的“标准动作”实现之外，也尽可能的“推陈出新”，增加大量细节内容，不仅更加“包容兼顾”，也更利于开发使用。加之本着不重复“造轮子”的原则，在能使用成熟组件代码的情况下，绝不重复实现相关代码，代码实现简洁、可读性高。本项目后端代码最为闪耀，细节满满，值得品鉴。</p> 
<ul> 
 <li>遵照 Spring Boot 标准化的方式，装配模块和相关代码。大量使用自定义 @ConditionOnXXX、@EnableXXX 注解，实现配置的动态、灵活的注入。</li> 
 <li>大量使用 Spring 和 Spring Boot 自身的事件驱动、InitializingBean等机制，实现相关代码逻辑，代码更加清晰、逻辑更加简洁、维护更加方便。</li> 
 <li>大量使用基于 Spring Boot 的策略模式和工厂模式，让同质的功能可以条件化、策略化的注入，便于根据使用者自身需求动态变更支持代码。</li> 
 <li>自定义多级缓存，与 <code>Spring Data JPA</code> 有机整合，有效解决 <code>Spring Cache</code> 等缓存对条件查询、分页查询支持不够便捷的问题。</li> 
 <li>基于数字信封原理，综合使用对称和非对称加密算法，实现前后端数据加密传输。支持国密算法 SM2 和 SM4 混合以及标准的 RSA 和 AES 混合。可通过配置文件配置进行切换，通过注解灵活个性化设置。</li> 
 <li>基于自定义 Session 实现秘钥动态生成、加密传输、一人一钥的安全机制，可通过配置动态开启和关闭。不是使用传统 Filter 方式进行加密处理，而是扩展 @RequestParam 等注解实现逻辑实现数据加解密。支持使用自定义注解灵活配置加密策略以及数据缓存策略。</li> 
 <li>遵照知名开源项目方式，设计 Maven Dependencies 依赖继承结构，结构清晰明了、依赖干净无冗余、修改维护便捷。各个模块以最小化模式进行包的依赖，简洁清爽，逻辑清晰，不会出现依赖循环问题。</li> 
 <li>个性化设计 Nacos 配置文件关系及逻辑，将高频修改配置参数统一提取，仅需在同一配置文件修改少量参数即可完成环境搭建和配置控制，降低修改参数的出错率。</li> 
 <li>将 Maven、Spring Boot、Nacos、Docker 等内容涉及的多环境配置有机融合和关联，可以方便地在各个环境中切换。</li> 
 <li>包含 Git 提交信息打包、源代码生成、容器打包等多种 Maven 构建插件及配置，相关信息也可在 <code>Spring Boot Admin</code> 展现。</li> 
 <li>集成较多同质组件或代码实现的可选择化使用，选择更丰富，使用更灵活</li> 
</ul> 
<blockquote> 
 <p>更多细节，欢迎对本项目进行深入了解</p> 
</blockquote> 
<h2>[5]、额外说明</h2> 
<ol> 
 <li>本项目以后将主要维护 <code>Spring Authorization Server</code> 版本，原有基于 <code>Spring Security OAuth2</code> 的版本已经移至 spring-security-oauth2 分支，可以从该分支或发行版页面获取历史版本继续使用。后期会根据 ISSUE 以及使用用户反馈情况，再行决定是否继续维护 <code>Spring Security OAuth2</code> 版本。</li> 
 <li>最新版本代码，暂时继续沿用原有基于 Vue2、Vuetify2、Typescript开发的前端系统。基于 Vue3、Vite2、Vuetify3、Pinia 等新版前端正在加进开发中，由于 Vuetify3 版本发布跳票以及部分已有组件的缺失，导致新版前端开发延后。</li> 
 <li>原有基于 Vue2、Vuetify2、Typescript 开发的前端，由于使用了过渡性 Typescript IOC 组件，以及依赖组件版本限制等问题，初次接触该项目在编译过程中会出现一些问题，请移步至本项目在线文档，详见“常见问题”章节。</li> 
</ol> 
<h4>为什么前端框架选择 Vuetify</h4> 
<p>在本项目建设初期，选择 Vuetify 作为前端组件，主要原因就是其是 Material 样式的UI组件以及更新频率较高、维护的持续性较好。经过几年的使用，发现该套组件库封装度很高，组件的属性配置丰富、使用灵活、可定制性强、学习使用曲线低。</p> 
<p>特别是 Vuetify 对常见的样式使用和布局处理进行了深度封装，不需在样式和布局设计上投入大量精力，通过简单的属性配置就可以做出比较好看的界面。这一点对不擅长前端和美工设计、想快速实现前端的后端人员非常友好。</p> 
<p>在进行 Vue3 版本开发之前，也对 Element Plus、Naive UI 等组件库进行了对比，也基于评分较高的开源后台模版进行了尝试性开发。发现大多数组件库相比 Vuetify，组件配置属性都少了很多，没有Vuetify灵活，而且都需要自己编写大量的样式，甚至需要自己实现常规组件。因此，新版本前端最终仍旧选择使用 Vuetify。</p> 
<h2>[6]、更新内容</h2> 
<ul> 
 <li>主要更新 
  <ul> 
   <li>Spring Boot 版本升级至 2.7.0</li> 
  </ul> </li> 
 <li>其它更新 
  <ul> 
   <li>修正新版 Spring Boot 下 applicationContext 获取 Bean RequestMappingHandlerMapping 出错问题。</li> 
   <li>修正权限数据通过消息队列传递， Jackson 反序列化出错问题。</li> 
   <li>修正新版 Spring Boot 下，OkHttp 与已有 Spring Cloud 版本不兼容，导致服务无法启动问题。</li> 
   <li>将 RestTemplate 底层客户端组件，临时由 OkHttp 改为 HttpClient，以规避 Okhttp 与 Spring Cloud 不兼容问题</li> 
  </ul> </li> 
 <li>依赖更新 
  <ul> 
   <li>Maven Invoker 版本升级至 3.2.0</li> 
   <li>Minio 版本升级至 8.4.1</li> 
   <li>Hutool 版本升级至 5.8.1</li> 
   <li>Okhttps 版本升级至 3.5.2</li> 
   <li>WxJava 版本升级至 4.3.3.B</li> 
   <li>Alipay-sdk-java 版本升级至 4.23.21.ALL</li> 
  </ul> </li> 
</ul>
                                        </div>
                                      
</div>
            