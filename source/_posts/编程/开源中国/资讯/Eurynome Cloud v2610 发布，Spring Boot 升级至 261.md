
---
title: 'Eurynome Cloud v2.6.1.0 发布，Spring Boot 升级至 2.6.1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f7857fd6c741ea19c72f485740fc738cb7d.jpg'
author: 开源中国
comments: false
date: Sat, 04 Dec 2021 18:14:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f7857fd6c741ea19c72f485740fc738cb7d.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>Eurynome Cloud </strong>是一款企业级微服务架构和服务能力开发平台。基于Spring Boot 2.5.7、Spring Cloud 2020.0.4、Spring Cloud Alibaba 2021.1、Nacos 2.0.3 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位 </strong> </p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<h2><strong>[1]、本次更新内容</strong></h2> 
<ul> 
 <li>重大更新</li> 
</ul> 
<ol> 
 <li>  Spring Boot 版本升级至 2.6.1</li> 
 <li>  Spring Cloud 版本升级至 2021.0.0</li> 
 <li>  新增 Sentinel 自动降级处理机制。</li> 
</ol> 
<ul> 
 <li>其它更新</li> 
</ul> 
<ol> 
 <li>  解决 JetCache 2.6.0 在 Spring Boot 2.6.X 环境下，Bean 循环依赖问题。</li> 
 <li>  解决 Spring Cloud Alibaba Sentinel 2021.1 在 Spring Boot 2.6.X 环境下，Bean 循环依赖问题。</li> 
 <li>  解决 Spring Boot 2.6.X 环境下，由于代码方法变更，导致接口自动化扫描抛空错误问题。</li> 
 <li>  解决 Sentinel 与 Feign 冲突问题。</li> 
 <li>  解决 Spring Cloud OAuth2 由于无用代码的注入，导致的 Bean 循环依赖问题。</li> 
 <li>  前端 Vuetify 版本升级至 2.6.1，升级相关依赖包版本，重新编译组件库</li> 
</ol> 
<h2>[2]、总体架构</h2> 
<div>
 <img alt height="500" src="https://oscimg.oschina.net/oscnet/up-f7857fd6c741ea19c72f485740fc738cb7d.jpg" width="720" referrerpolicy="no-referrer">
</div> 
<p> </p> 
<h2>[3]、特色功能演示</h2> 
<h3>（1） 方法级动态权限</h3> 
<div>
 <img alt height="352" src="https://oscimg.oschina.net/oscnet/up-ba8f726011731bd2f0f92cfbc2548021d2b.gif" width="720" referrerpolicy="no-referrer">
</div> 
<p> </p> 
<h3>（2） 服务调用链监控</h3> 
<div>
 <img alt height="500" src="https://oscimg.oschina.net/oscnet/up-a3b13863626646deb9c055fe900602ce0d7.gif" width="720" referrerpolicy="no-referrer">
</div> 
<p> </p> 
<h2>[4]、技术栈和版本说明</h2> 
<h3>（1）Spring全家桶及核心技术版本</h3> 
<table border="1" cellpadding="1" cellspacing="1" style="width:500px"> 
 <tbody> 
  <tr> 
   <td>组件</td> 
   <td>版本</td> 
  </tr> 
  <tr> 
   <td>Spring Boot</td> 
   <td>2.6.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud </td> 
   <td>2021.0.0</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Alibaba</td> 
   <td>2021.1</td> 
  </tr> 
  <tr> 
   <td>Spring Boot Admin</td> 
   <td>2.5.4</td> 
  </tr> 
  <tr> 
   <td>Nacos</td> 
   <td>2.0.3</td> 
  </tr> 
  <tr> 
   <td>Sentinel</td> 
   <td>1.8.2</td> 
  </tr> 
  <tr> 
   <td>Seata</td> 
   <td>1,.3.0</td> 
  </tr> 
 </tbody> 
</table> 
<h3>（2）所涉及的相关的技术</h3> 
<ul> 
 <li>- 持久层框架： Spring Data Jpa & Mybatis Plus</li> 
 <li>- API网关：Spring Cloud Gateway</li> 
 <li>- 服务注册&发现和配置中心: Alibaba Nacos</li> 
 <li>- 服务消费：Spring Cloud OpenFeign & RestTemplate & OkHttps</li> 
 <li>- 负载均衡：Spring Cloud Loadbalancer</li> 
 <li>- 服务熔断&降级&限流：Alibaba Sentinel</li> 
 <li>- 服务监控：Spring Boot Admin</li> 
 <li>- 消息队列：使用Spring Cloud消息总线Spring Cloud Bus 默认Kafka 适配RabbitMQ</li> 
 <li>- 链路跟踪：Skywalking</li> 
 <li>- 分布式事务：Seata</li> 
 <li>- 数据缓存：JetCache + Redis + Caffeine, 自定义多级缓存</li> 
 <li>- 数据库： Postgresql，MySQL，Oracle ...</li> 
 <li>- JSON序列化：Jackson & FastJson</li> 
 <li>- 文件服务：阿里云OSS/Minio</li> 
 <li>- 数据调试：p6spy</li> 
 <li>- 日志中心：ELK</li> 
 <li>- 日志收集：Logstash Logback Encoder</li> 
</ul> 
<h2>[5]、工程结构</h2> 
<pre><code class="language-bash">eurynome-cloud
├── configurations -- 配置文件脚本和统一Docker build上下文目录
├── dependencies -- 工程Maven顶级依赖，统一控制版本和依赖
├── integrates -- 外部工具组件集成代码包
├    ├── eurynome-integration-oss -- 对象存储模块
├    └── eurynome-integration-influxdb -- 时序数据储模块
├── packages -- 基础通用依赖包
├    ├── eurynome-cloud-assistant -- Spring相关公共辅助工具、注解相关工具代码组件
├    ├── eurynome-cloud-cache -- Cache和Redis工具模块组件
├    ├── eurynome-cloud-data -- 数据持久化等数据处理相关代码组件
├    ├── eurynome-cloud-kernel -- 微服务接入平台必备组件
├    ├── eurynome-cloud-message -- 消息处理相关代码组件
├    ├── eurynome-cloud-oauth -- OAuth2通用代码
├    ├── eurynome-cloud-oauth-starter -- 自定义OAuth2 Starter，Athena单体版核心Starter
├    ├── eurynome-cloud-rest -- Rest相关代码组件
├    ├── eurynome-cloud-sercurity -- Security通用代码
├    ├── eurynome-cloud-starter -- 微服务核心Starter
├    ├── eurynome-cloud-web -- Web 应用基础组件
├    └── eurynome-cloud-websocket -- WebSocket核心代码包
├── platform -- 平台核心服务
├    ├── eurynome-cloud-gateway -- 服务网关
├    ├── eurynome-cloud-monitor -- Spring Boot Admin 监控服务
├    └── eurynome-cloud-uaa -- 统一认证模块
├── services -- 平台业务服务
├    ├── eurynome-cloud-upms-api -- 通用用户权限api 
├    ├── eurynome-cloud-upms-logic -- 通用用户权限service
├    ├── eurynome-cloud-upms-rest -- 通用用户权限rest 接口
├    ├── eurynome-cloud-upms-ability -- 通用用户权限服务
├    ├── eurynome-cloud-upms-rest -- 工作流基础代码包
└──  └── eurynome-cloud-bpmn-ability -- 工作流服务 </code></pre>
                                        </div>
                                      
</div>
            