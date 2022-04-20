
---
title: 'Eurynome Cloud 2.7.0.Beta5 发布，全面个性化定制'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1ec1bfc02e539d4114a8b7cc75e44ddf5c3.png'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 09:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1ec1bfc02e539d4114a8b7cc75e44ddf5c3.png'
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
 <li>主要更新 
  <ul> 
   <li>[新增] 新增自定义 Spring Authorization Server 授权码模式登录认证页面和授权确认页面</li> 
   <li>[新增] 自定义 Spring Authorization Server 授权码模式登录使用 AES 进行数据加密传输。</li> 
   <li>[新增] 自定义 Spring Authorization Server 授权码模式登录增加验证码支持，支持多种验证码类型，暂不支持行为验证码。</li> 
   <li>[新增] 新增基于 Spring Authorization Server 的单体版应用，做为系统的有益补充，无须搭建复杂基础设施，即可快速搭建运行。</li> 
   <li>[优化] 优化平台错误体系，融合 Spring Authorization Server Form Login 以及验证码相关错误。</li> 
   <li>[优化] 优化调整 Spring Security 相关的依赖，增加自定义 Jackson Module 序列化，解决扩展的 WebAuthenticationDetails 无法反序列化问题。</li> 
  </ul> </li> 
 <li>界面预览</li> 
</ul> 
<p><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-1ec1bfc02e539d4114a8b7cc75e44ddf5c3.png" width="300" referrerpolicy="no-referrer"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-170038957cc4a4e61064afdf11978741989.png" width="300" referrerpolicy="no-referrer"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-94e6176612cb0984a34a29307bc5944c6c0.png" width="300" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>其它更新 
  <ul> 
   <li>Spring Boot Admin 版本升级至 2.6.6</li> 
   <li>Camunda 版本升级至 7.17.0</li> 
   <li>Antisamy 版本升级至 1.6.7</li> 
   <li>logstash-logback-encoder 版本升级至 7.1.1</li> 
   <li>Skywalking 版本升级至 8.10.0</li> 
   <li>Minio 版本升级 8.3.8</li> 
   <li>JetCache 版本升级至 2.6.4</li> 
   <li>Okhttps 版本升级至 3.5.0</li> 
   <li>Wxjava 版本升级至 4.3.0</li> 
   <li>bce-java-sdk 版本升级至 0.10.204</li> 
   <li>qiniu-java-sdk 版本升级至 7.10.0</li> 
   <li>alipay-sdk-java 版本升级至 4.22.86.ALL</li> 
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
            