
---
title: 'Eurynome Cloud v2.5.6.60 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5709'
author: 开源中国
comments: false
date: Fri, 19 Nov 2021 17:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5709'
---

<div>   
<div class="content">
                                                                                            <p>Eurynome Cloud v2.5.6.60 已经发布，企业级技术中台微服务架构。</p> 
<p>此版本更新内容包括：</p> 
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
 <li> <p>重大更新</p> 
  <ol> 
   <li>Spring Cloud Alibaba Sentinel 升级至 1.8.2</li> 
   <li>扩展 Spring Cloud Alibaba Sentinel，实现应用数据持久化存储到 Influxdb 时序数据库中，支持将 Sentinel 配置信息以配置文件的形式持久化存储至 Nacos中。时序数据存储基于Influxdb1 版本实现，默认使用原有方式存储数据，可通过配置参数动态开启或关闭 Influxdb 和 Nacos 存储机制。</li> 
   <li>更换使用扩展的 Sentinel 进行接口管理。扩展的 Sentinel Dashboard 已封装为 Docker 镜像，并上传至 Docker Hub， 可以通过docker命令 <code>docker pull herodotus/sentinel-dashboard:1.8.2(latest)</code> 直接使用。Sentinel、Influxdb、Nacos 等相关内容均支持动态参数配置。</li> 
   <li>新增 Telegraf、InfluxDB、Chronograf、Kapacitor支持，新增 Influxdb 集成模块，补充时序数据存储管理能力和数据展现能力。提供默认配置文件及docker-compose脚本。</li> 
  </ol> </li> 
 <li> <p>其它更新</p> 
  <ol> 
   <li>修正 Docker build 参数错误，解决打包过程中无法定位jar文件问题。</li> 
   <li>前端 Vuetify 版本升级至 2.6.0</li> 
   <li>前端工程升级大量依赖包版本，重新编译生成组件库</li> 
  </ol> </li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.6.60">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.6.60</a></p>
                                        </div>
                                      
</div>
            