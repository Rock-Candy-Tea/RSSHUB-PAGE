
---
title: 'Eurynome Cloud 2.7.1.3 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6d378fb593cde0e92e8598c8be621bf3bf6.jpg'
author: 开源中国
comments: false
date: Mon, 18 Jul 2022 22:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6d378fb593cde0e92e8598c8be621bf3bf6.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。首个全面拥抱 Spring Authorization Server 的版本，基于Spring Boot 2.7.1、Spring Cloud 2021.0.3、Spring Cloud Alibaba 2021.0.1.0、 Spring Authorization Server 0.3.1、Nacos 2.1.0 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位</strong></p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<h2>[1]、更新内容</h2> 
<ul> 
 <li><strong>主要更新</strong> 
  <ul> 
   <li>[新增] 增加菜单管理功能，支持后端数据动态转换为前端菜单，根据用户角色动态切换菜单</li> 
   <li>[新增] 增加基于 Spring Authorization Server 的 Token 信息扩展，客户端在获取 Token 时就可以同时获取用户的相关信息，方便客户端区分用户身份信息，减少重复请求。使用前后端数据加密，进一步保护敏感信息。</li> 
   <li>[升级] 前端工程 Vite 版本升级至 3.0.1</li> 
  </ul> </li> 
 <li><strong>其它更新</strong> 
  <ul> 
   <li>[优化] 优化系统用户登录合规性记录代码，去除重复性逻辑及部分硬代码</li> 
   <li>[优化] 优化 ServiceContext 代码逻辑，增加统一的 HTTP 地址 Protocol 头处理机制，实现代码中 HTTP 或 HTTPS 协议头的统一配置和修改</li> 
   <li>[修复] 修复 Swagger 认证功能不生效无法在 Swagger 中进行测试问题，以及多环境下 Swagger 是否开启控制失效问题。</li> 
   <li>[修复] 修复单体版 Swagger 多是否开启控制失效问题， 以及 Swagger 界面中自动生成的接口地址错误问题。</li> 
   <li>[升级] 升级 Antisamy XSS 拦截分析配置文件版本</li> 
  </ul> </li> 
 <li><strong>依赖更新</strong> 
  <ul> 
   <li>antisamy 版本升级至 1.7.0</li> 
   <li>minio 版本升级至 8.4.3</li> 
   <li>jetcache 版本升级 2.6.6</li> 
   <li>dysmsapi20170525 版本升级至 2.0.16</li> 
   <li>tencentcloud-sdk-java 版本升级 3.1.552</li> 
   <li>alipay-sdk-java 版本升级至 4.31.64.ALL</li> 
  </ul> </li> 
</ul> 
<h2>[2]、界面预览</h2> 
<p><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-6d378fb593cde0e92e8598c8be621bf3bf6.jpg" width="300" referrerpolicy="no-referrer"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-245d9f17705154a27d07365ea0f3100d732.jpg" width="300" referrerpolicy="no-referrer"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-72baf59cbb8e24fbebbf34c1dee4192df29.jpg" width="300" referrerpolicy="no-referrer"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-26c4b96fec0d3f1fe89b90481655060178d.jpg" width="300" referrerpolicy="no-referrer"></p> 
<h2>[3]、重要说明</h2> 
<p>由于 Spring Authorization Server 0.3.0 版本，使用 Java 11 进行代码编译。导致使用该版本在 Java 8 下代码已无法编译成功，所以必须要升级 JDK 版本。同时，考虑到 2022 年 11 月，Spring Boot 3 将会发布，最低版本要求 Java 17。因此，直接将 Java 版本升级至 17。Eurynome Cloud 2.7.0.20 ~ 2.7.0.50 均是采用 Java 17 编译运行，同时不兼容 Java 8。</p> 
<p>不管是 Spring Authorization Server 还是本项目 Eurynome Cloud，各路网友均不主张在现阶段直接将 Java 升级 17，而是希望继续兼容 Java 8，在 Spring Boot 3 发布以后再统一升级为默认使用 Java 17</p> 
<p>因此 Spring Authorization Server 0.3.1 版本，代码降级兼容了 Java 8。Eurynome Cloud 也同步进行了代码的降级兼容处理，以兼容 Java 8。<strong>经过验证，目前 Erurynom Cloud 在 Java 8、11、17 环境下均可以正常稳定运行</strong></p> 
<blockquote> 
 <p>Spring Authorization Server 发布两个版本，Eurynome Cloud 使用的 Java 版本就跟着变，升到 Java 17 又跟着降回 Java 8，折腾一圈浪费功夫。看似折腾实则不然，经此一役，Eurynome Cloud 已经完全支持 Java 8 Java 11 和 Java 17，未来升级使用 Spring Boot 3 也不是问题。验证了那句话“用心认真走过的每条路都不会白走”</p> 
</blockquote> 
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
 <li>本项目以后将主要维护 `Spring Authorization Server` 版本，原有基于 `Spring Security OAuth2` 的版本已经移至 spring-security-oauth2 分支，可以从该分支或发行版页面获取历史版本继续使用。后期会根据 ISSUE 以及使用用户反馈情况，再行决定是否继续维护 `Spring Security OAuth2` 版本。</li> 
 <li>基于 Vue3、Vite2、Vuetify3、Pinia 等新版前端已发布，原有基于 Vue2、Vuetify2、Typescript 开发的前端代码已移至 vue2+vuetify2+typescript 分支 <p> </p> </li> 
</ol>
                                        </div>
                                      
</div>
            