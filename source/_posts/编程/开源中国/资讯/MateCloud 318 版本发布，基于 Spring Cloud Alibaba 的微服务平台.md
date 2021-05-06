
---
title: 'MateCloud 3.1.8 版本发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0108/094441_zv5H_2744687.jpg'
author: 开源中国
comments: false
date: Thu, 06 May 2021 15:57:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0108/094441_zv5H_2744687.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">功能升级</h2> 
<ul> 
 <li>消息队列升级，解决@StreamListener已过期问题</li> 
 <li>mate-starter-kafka模块升级</li> 
 <li>mate-starter-rocketmq模块升级</li> 
</ul> 
<h2 style="text-align:start">依赖升级</h2> 
<ul> 
 <li>升级至Dubbo 2.7.10</li> 
 <li>升级至Elasticsearch 7.12.1</li> 
</ul> 
<p>MateCloud 是一款基于Spring Cloud Alibaba的微服务架构。目前已经整合 Spring Cloud Gateway、Spring Security Oauth2、Feign、Dubbo、JetCache、RocketMQ 等服务套件，旨在为用户者提供技术框架的基础能力的封装，减少开发工作，可以专心于业务。</p> 
<p><img alt height="1381" src="https://static.oschina.net/uploads/space/2021/0108/094441_zv5H_2744687.jpg" width="2000" referrerpolicy="no-referrer"></p> 
<p><strong>功能特点</strong></p> 
<ul> 
 <li>采用最新的 Spring Cloud Hoxton SR8, Spring Boot 2.3.7.RELEASE, Spring Cloud Alibaba 2.2.3.RELEASE 版本进行系统设计</li> 
 <li>支持 nacos 作为注册中心，实现多配置、分群组、分命名空间、多业务模块的注册和发现功能</li> 
 <li>统一 Oauth2 认证协议，采用jwt的方式，实现统一认证，并支持自定义 grant_type 实现手机号码登录，第三方登录正在开发中</li> 
 <li>利用 Spring Boot Admin 来监控各个独立 Service 的运行状态；利用 Hystrix Dashboard 来实时查看接口的运行状态和调用频率等</li> 
 <li>集成了 feign 和 dubbo 两种模式支持内部调用，并且可以实现无缝切换，适合新老程序员，快速熟悉项目</li> 
 <li>采用 Sentinel 实现业务熔断处理，避免服务之间出现雪崩</li> 
 <li>通过注解的方式，实现用户登录信息的快速注入</li> 
 <li>通过接入 knife4j，实现在线API文档的查看与调试</li> 
 <li>基于 Mybatis-plus-generator 自动生成代码，提升开发效率，生成模式不断优化中，暂不支持前端代码生成</li> 
 <li>集成消息中间件 RocketMQ，对业务进行异步处理</li> 
 <li>采用前后端分离的框架设计，前端采用 vue-element-admin</li> 
 <li>自定义 traceId 的方式，实现简单的链路追踪功能</li> 
 <li>集成 Mybatis Plus，实现 saas 多租户功能</li> 
</ul>
                                        </div>
                                      
</div>
            