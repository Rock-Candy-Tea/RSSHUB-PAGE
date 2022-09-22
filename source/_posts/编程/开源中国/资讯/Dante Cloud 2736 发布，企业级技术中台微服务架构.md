
---
title: 'Dante Cloud 2.7.3.6 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6d378fb593cde0e92e8598c8be621bf3bf6.jpg'
author: 开源中国
comments: false
date: Thu, 22 Sep 2022 17:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6d378fb593cde0e92e8598c8be621bf3bf6.jpg'
---

<div>   
<div class="content">
                                                                                            <p><strong>Dante Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。首个全面拥抱 Spring Authorization Server 的版本，基于Spring Boot 2.7.3、Spring Cloud 2021.0.4、Spring Cloud Alibaba 2021.0.4.0、 Spring Authorization Server 0.3.1、Nacos 2.1.1 等最新版本开发的多租户系统，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位</strong></p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2.1 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<h2>[1]、特别说明</h2> 
<p><strong>Dante Cloud</strong> (但丁，原 <strong>Eurynome Cloud</strong>) 正式加入 <strong>Dromara</strong> 开源社区。<strong>Dante Cloud</strong> 将继续秉承“简洁、高效、包容、务实”的理念，不断地深耕细作、去粗取精，用心打造一款适应未来信息化建设需求的精致产品。同时，与 Dromara 开源社区以及社区中所有的优秀人才一起互相扶持、并肩前行，创造更多、更好、更精的产品以回馈社会，促进软件开源的发展。</p> 
<p>谢谢大家对 <strong>Eurynome Cloud</strong> 支持与厚爱，希望大家继续给与 <strong>Dante Cloud</strong> 以及 <strong>Dromara</strong> 开源社区关注与支持</p> 
<h2>[2]、为什么更名为 Dante Cloud</h2> 
<p>原项目名称 <strong>Eurynome Cloud</strong>，很多朋友都反映名字太长、读起来拗口、不容易记等问题。因此在加入 <strong>Dromara</strong> 开源社区之际，将名字进行了变更。</p> 
<p><strong>Dante</strong>，即但丁·阿利基耶里(公元1265年-公元1321年)，13世纪末意大利诗人，现代意大利语的奠基者，欧洲文艺复兴时代的开拓人物之一，以长诗《神曲》(原名《喜剧》)而闻名，后来一位作家叫薄伽丘将其命名为神圣的喜剧。</p> 
<p>他被认为是中古时期意大利文艺复兴中最伟大的诗人，也是西方最杰出的诗人之一，最伟大的作家之一。恩格斯评价说：“封建的中世纪的终结和现代资本主义纪元的开端，是以一位大人物为标志的，这位人物就是意大利人但丁，他是中世纪的最后一位诗人，同时又是新时代的最初一位诗人”</p> 
<p>更名为 Dante Cloud，寓意本项目会像恩格斯对但丁的评价一样，在行业变革的时期，可以成为一款承上启下，助力企业信息化建设变革的产品。</p> 
<h2>[3]、本次更新内容</h2> 
<ul> 
 <li>重要更新 
  <ul> 
   <li>[升级] Spring Boot Admin 版本升级至 2.7.5</li> 
   <li>[升级] 前端工程 Camunda Bpmn 在线编辑器核心组件大版本升级</li> 
   <li>[安全] 强制升级 xnio 版本至 3.8.8.Final，修复安全漏洞 (CVE-2022-0084)</li> 
  </ul> </li> 
 <li>其它更新 
  <ul> 
   <li>[新增] 新增 Spring Authorization Server 历史 Token 清理逻辑</li> 
   <li>[修复] 前端工程编译结果与 Nginx 一起打包为 Docker 后，在浏览器刷新页面出现 404 问题。</li> 
   <li>[优化] 优化 Token 过期检测逻辑，调整时钟偏移(Clock Skew)，与 Spring Security OAuth2 Jose 默认实现逻辑保持一致。fix: #I5RWGA（ISSUED by 狂练胸肌李大懒）</li> 
   <li>[优化] 优化前端封装 Axios 代码中阻止重复提交属性名称，将其修改为更容易理解的变量名称。</li> 
   <li>[优化] 优化自定义 Spring Authorization Server JPA 模块部分查询操作，启用基于 Jetcache 自定义的 JPA 多级缓存支持，提升数据查询效率</li> 
   <li>[优化] 优化部分代码日志输出级别，提升控制台日志输出内容的可聚焦性</li> 
  </ul> </li> 
 <li>依赖更新 
  <ul> 
   <li>log4j2 版本升级至 2.19.0</li> 
   <li>minio 版本升级 8.4.4</li> 
   <li>fastjson2 版本升级至 2.0.14</li> 
   <li>hutool 版本升级至 5.8.7</li> 
   <li>mybatis 版本升级至 3.5.11</li> 
   <li>tencentcloud-sdk-java-sms 版本升级至 3.1.597</li> 
  </ul> </li> 
</ul> 
<h2>[4]、Dante Cloud 2.7.X 主要变化</h2> 
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
   <li>基于 <code>Spring Authorization Server</code> 和 JPA 构建支持 Database 和 Schema 模式的多租户架构。</li> 
  </ul> </li> 
 <li> <p>代码结构的大规模调整和优化：</p> 
  <ul> 
   <li>对原有代码进行了深度的“庖丁解牛”，严格遵照“单一职责”原则，根据各个组件的职责以及用途，将整个工程拆解细化为多个各自独立组件模块，在最大程度上降低代码间的耦合，也更容易聚焦和定位问题。</li> 
   <li>将通用化组件提取为独立工程，独立编译、按需选用，极大的降低系统主工程代码量。相关组件也已上传至 Maven 中央仓库，降低系统主工程工程代码编译耗时，改进和提升 CICD 效率，</li> 
   <li>原有主工程代码结构也进行了深化调整，代码分包更加合理，代码逻辑也更加清晰。</li> 
  </ul> </li> 
</ul> 
<h2>[5]、界面预览</h2> 
<p><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-6d378fb593cde0e92e8598c8be621bf3bf6.jpg" width="300" referrerpolicy="no-referrer"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-245d9f17705154a27d07365ea0f3100d732.jpg" width="300" referrerpolicy="no-referrer"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-72baf59cbb8e24fbebbf34c1dee4192df29.jpg" width="300" referrerpolicy="no-referrer"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-26c4b96fec0d3f1fe89b90481655060178d.jpg" width="300" referrerpolicy="no-referrer"></p> 
<h2>[6]、额外说明</h2> 
<ol> 
 <li>本项目以后将主要维护 `Spring Authorization Server` 版本，原有基于 `Spring Security OAuth2` 的版本已经移至 spring-security-oauth2 分支，可以从该分支或发行版页面获取历史版本继续使用。后期会根据 ISSUE 以及使用用户反馈情况，再行决定是否继续维护 `Spring Security OAuth2` 版本。</li> 
 <li>基于 Vue3、Vite3、Quasar2、Pinia 等新版前端已发布，原有基于 Vue2、Vuetify2、Typescript 开发的前端代码已移至 vue2+vuetify2+typescript 分支</li> 
 <li>自 2.7.2.3 版本起，Dante Cloud 所有核心代码全部开源。新开放内容包括： 
  <ul> 
   <li><strong>接口权限鉴权：</strong>全面整合 `@PreAuthorize` 注解权限与 `URL` 权限，通过后端动态配置，无须在代码中配置 `Spring Security` 权限注解以及权限方法，即可实现接口鉴权以及权限的动态修改。采用分布式鉴权方案，规避 Gateway 统一鉴权的压力以及重复鉴权问题</li> 
   <li><strong>动态权限数据分发：</strong>采用分布式服务独立鉴权方案，`Spring Security` `@PreAuthorize` 的权限注解、权限方法以及 `URL` 权限，通过后端动态配置后，实时动态分发至对应服务。</li> 
   <li><strong>User 数据策略访问：</strong>`OAuth2` `UserDetails` 核心数据支持直连数据库获取和 `Feign` 远程调用两种模式。`OAuth2` 直连数据库模式性能更优，`Feign` 访问远程调用可扩展性更强。可通过配置动态修改采用策略方式。</li> 
   <li><strong>手机短信验证码注册认证：</strong>采用自定义 `OAuth2` 授权模式，使用统一 `Token` 接口，实现手机验证码登录认证，与平台为统一体系，统一返回`OAuth2` Token，支持服务接口鉴权</li> 
   <li><strong>第三方系统社交注册认证：</strong>集成 `JustAuth`，采用自定义 `OAuth2` 授权模式，使用统一 `Token` 接口，实现基于 `JustAuth` 实现第三方系统社交登录认证，与平台为统一体系，统一返回 `OAuth2` Token，支持服务接口鉴权。所有 `JustAuth` 支持的第三方系统均支持。</li> 
   <li><strong>微信小程序注册认证：</strong>采用自定义 `OAuth2` 授权模式，使用统一 `Token` 接口，实现支持微信小程序登录认证，与平台为统一体系，统一返回 `OAuth2` Token，支持服务接口鉴权。</li> 
   <li><strong>其它方式注册认证：</strong>采用策略模式对外部系登录认证和用户注册进行接入支持，采用 `OAuth2` 默认认证接口。目前未集成的外部系统，可参考标准，适当增减参数，即可支持接入。</li> 
   <li><strong>多通道 SMS 集成：</strong>集成阿里，百度，中国移动，华为，京东，极光，网易，七牛，腾讯，又拍，云片等平台短信发送通道。可通过配置动态选择具体使用通道。支持多模版定义以及模版参数顺序控制</li> 
   <li><strong>微信小程序订阅消息：</strong>支持微信小程序订阅消息发送。提供订阅消息模版工厂，可根据自身业务需求，编写少量代码既可以拓展支持新订阅消息模版。 <p> </p> </li> 
  </ul> </li> 
</ol> 
<h2>Dromara 开源社区</h2> 
<h3>一、社区愿景</h3> 
<p><strong>让每一位开源爱好者，体会到开源的快乐。</strong></p> 
<h3>二、社区官网</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdromara.org" target="_blank">https://dromara.org</a> 是 Dromara 开源社区官方网站。</p> 
<h3>三、成员项目</h3> 
<p><img align="left" alt height="346" src="https://oscimg.oschina.net/oscnet/up-fcb9a3a7245ab9ca6e84698d1f280d39681.jpg" width="800" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            