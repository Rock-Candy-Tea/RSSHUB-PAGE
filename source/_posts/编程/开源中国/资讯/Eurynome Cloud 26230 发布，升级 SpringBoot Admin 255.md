
---
title: 'Eurynome Cloud 2.6.2.30 发布，升级 SpringBoot Admin 2.5.5'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3152a26db51892c35a11ed4efdab72056ad.jpg'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 11:27:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3152a26db51892c35a11ed4efdab72056ad.jpg'
---

<div>   
<div class="content">
                                                                                            <p><strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。基于Spring Boot 2.6.1、Spring Cloud 2021.0.0、Spring Cloud Alibaba 2021.1、Nacos 2.0.3 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位</strong></p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<h2>[2]、本次更新内容</h2> 
<ol> 
 <li>重大更新 
  <ul> 
   <li>Spring Boot Admin 版本升级至 2.5.5</li> 
  </ul> </li> 
 <li>其它更新 
  <ul> 
   <li>Apache Log4j2 版本升级至 2.17.0，解决第三个安全漏洞 CVE-2021-45105</li> 
   <li>独立的eurynome-cloud-upms-api包，已经失去单独提取的意义，将其与eurynome-cloud-upms-logic包整合。</li> 
   <li>新增认证成功后，登录信息日志记录。<br>  </li> 
  </ul> </li> 
</ol> 
<h2>[2]、总体架构</h2> 
<p><img alt height="424" src="https://oscimg.oschina.net/oscnet/up-3152a26db51892c35a11ed4efdab72056ad.jpg" width="720" referrerpolicy="no-referrer"></p> 
<h2>[3]、特色功能演示</h2> 
<h3>（1）方法级可配置动态权限</h3> 
<p><img alt height="489" src="https://oscimg.oschina.net/oscnet/up-8126b2fbe6737d6200b541b7ccceee3aa28.gif" width="1000" referrerpolicy="no-referrer"></p> 
<h3>（2）<span style="background-color:#ffffff; color:#333333">组合式、可定制图形验证码</span></h3> 
<p><br> <img alt height="260" src="https://oscimg.oschina.net/oscnet/up-8b820919d8f729cc0aa731f7897f279a55c.png" width="343" referrerpolicy="no-referrer"><img alt height="262" src="https://oscimg.oschina.net/oscnet/up-f8df3441bec959e465e84e1fc182b1fb6a9.png" width="348" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">[4]、技术栈和版本说明</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">（1）Spring全家桶及核心技术版本</h3> 
<table border="1" cellpadding="1" cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-indent:0px; text-transform:none; white-space:normal; widows:2; width:500px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">组件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">版本</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Spring Boot</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2.6.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Spring Cloud </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2021.0.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Spring Cloud Alibaba</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2021.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Spring Boot Admin</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2.5.5</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Nacos</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2.0.3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Sentinel</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.8.2</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Seata</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1,.3.0</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="margin-left:0; margin-right:0; text-align:left">（2）所涉及的相关的技术</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>持久层框架： Spring Data Jpa & Mybatis Plus</li> 
 <li>API网关：Spring Cloud Gateway</li> 
 <li>服务注册&发现和配置中心: Alibaba Nacos</li> 
 <li>服务消费：Spring Cloud OpenFeign & RestTemplate & OkHttps</li> 
 <li>负载均衡：Spring Cloud Loadbalancer</li> 
 <li>服务熔断&降级&限流：Alibaba Sentinel</li> 
 <li>服务监控：Spring Boot Admin</li> 
 <li>消息队列：使用Spring Cloud消息总线Spring Cloud Bus 默认Kafka 适配RabbitMQ</li> 
 <li>链路跟踪：Skywalking</li> 
 <li>分布式事务：Seata</li> 
 <li>数据缓存：JetCache + Redis + Caffeine, 自定义多级缓存</li> 
 <li>数据库： Postgresql，MySQL，Oracle ...</li> 
 <li>JSON序列化：Jackson & FastJson</li> 
 <li>文件服务：阿里云OSS/Minio</li> 
 <li>数据调试：p6spy</li> 
 <li>日志中心：ELK</li> 
 <li>日志收集：Logstash Logback Encoder</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">[5]、工程结构</h2> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash">eurynome-cloud
├── configurations <span style="color:#6a737d">-- 配置文件脚本和统一Docker build上下文目录</span>
├── dependencies <span style="color:#6a737d">-- 工程Maven顶级依赖，统一控制版本和依赖</span>
├── integrates <span style="color:#6a737d">-- 外部工具组件集成代码包</span>
├    ├── eurynome-integration-oss <span style="color:#6a737d">-- 对象存储模块</span>
├    └── eurynome-integration-influxdb <span style="color:#6a737d">-- 时序数据储模块</span>
├── packages <span style="color:#6a737d">-- 基础通用依赖包</span>
├    ├── eurynome-cloud-assistant <span style="color:#6a737d">-- Spring相关公共辅助工具、注解相关工具代码组件</span>
├    ├── eurynome-cloud-cache <span style="color:#6a737d">-- Cache和Redis工具模块组件</span>
├    ├── eurynome-cloud-captcha <span style="color:#6a737d">-- 验证码模块组件</span>
├    ├── eurynome-cloud-data <span style="color:#6a737d">-- 数据持久化等数据处理相关代码组件</span>
├    ├── eurynome-cloud-kernel <span style="color:#6a737d">-- 微服务接入平台必备组件</span>
├    ├── eurynome-cloud-message <span style="color:#6a737d">-- 消息处理相关代码组件</span>
├    ├── eurynome-cloud-oauth <span style="color:#6a737d">-- OAuth2通用代码</span>
├    ├── eurynome-cloud-oauth-starter <span style="color:#6a737d">-- 自定义OAuth2 Starter，Athena单体版核心Starter</span>
├    ├── eurynome-cloud-rest <span style="color:#6a737d">-- Rest相关代码组件</span>
├    ├── eurynome-cloud-sercurity <span style="color:#6a737d">-- Security通用代码</span>
├    ├── eurynome-cloud-starter <span style="color:#6a737d">-- 微服务核心Starter</span>
├    ├── eurynome-cloud-web <span style="color:#6a737d">-- Web 应用基础组件</span>
├    └── eurynome-cloud-websocket <span style="color:#6a737d">-- WebSocket核心代码包</span>
├── platform <span style="color:#6a737d">-- 平台核心服务</span>
├    ├── eurynome-cloud-gateway <span style="color:#6a737d">-- 服务网关</span>
├    ├── eurynome-cloud-monitor <span style="color:#6a737d">-- Spring Boot Admin 监控服务</span>
├    └── eurynome-cloud-uaa <span style="color:#6a737d">-- 统一认证模块</span>
├── services <span style="color:#6a737d">-- 平台业务服务</span>
├    ├── eurynome-cloud-upms-logic <span style="color:#6a737d">-- 通用用户权限service</span>
├    ├── eurynome-cloud-upms-rest <span style="color:#6a737d">-- 通用用户权限rest 接口</span>
├    ├── eurynome-cloud-upms-ability <span style="color:#6a737d">-- 通用用户权限服务</span>
├    ├── eurynome-cloud-upms-rest <span style="color:#6a737d">-- 工作流基础代码包</span>
└──  └── eurynome-cloud-bpmn-ability <span style="color:#6a737d">-- 工作流服务 </span></code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            