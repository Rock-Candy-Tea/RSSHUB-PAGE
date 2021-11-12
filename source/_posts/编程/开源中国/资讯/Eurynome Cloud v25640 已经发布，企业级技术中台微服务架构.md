
---
title: 'Eurynome Cloud v2.5.6.40 已经发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7992'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 18:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7992'
---

<div>   
<div class="content">
                                                                                            <p>Eurynome Cloud v2.5.6.40 已经发布，企业级技术中台微服务架构</p> 
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
<ol> 
 <li>前端工程支持 docker-compose 打包，进行容器化部署。集成 Nginx，默认配置支持 gzip 压缩，提升页面首次加载效率。</li> 
 <li>修复 Vue 工程打包部署至 Nginx，favicon.ico 图标报404错误问题。</li> 
 <li>修复 Spring Boot Admin 在正式环境下，依赖的 spring-boot-starter-actuator 主动连接 Redis 问题。</li> 
 <li>优化 Management 服务 Docker 打包逻辑，修复 Spring Boot Admin 混入 Skywalking 监控逻辑问题。</li> 
 <li>优化工程 docker-compose 脚本，补充 BPMN 服务运行脚本。</li> 
 <li>优化 Logstash 日志收集内容格式，修复 Logback 会创建多个 Logback 上下文导致冲突的问题</li> 
 <li>补充 Nacos 2.0.3 数据库初始化脚本，删除低版本无用脚本。</li> 
 <li>插件 docker-maven-plugin 升级至 0.38.0</li> 
 <li>Vuetify 升级至 2.5.14。</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.6.40">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.6.40</a></p>
                                        </div>
                                      
</div>
            