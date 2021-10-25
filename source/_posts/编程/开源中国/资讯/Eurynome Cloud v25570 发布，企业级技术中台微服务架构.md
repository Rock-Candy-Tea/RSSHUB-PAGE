
---
title: 'Eurynome Cloud v2.5.5.70 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=902'
author: 开源中国
comments: false
date: Sun, 24 Oct 2021 23:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=902'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Eurynome Cloud v2.5.5.70 已经发布，<strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。基于Spring Boot 2.5.5、Spring Cloud 2020.0.4、Spring Cloud Alibaba 2021.1、Nacos 2.0.3 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<h2><strong>v2.5.5.70 更新内容</strong></h2> 
<ul> 
 <li> <h3>重大更新</h3> 
  <ol> 
   <li>在现有架构基础之上，集成 Redisson 客户端。与 Spring Data Redis 同时使用，支持 Redisson 与 Lettuce 或 Jedis 共存。</li> 
   <li>重构核心包 eurynome-cloud-data 内主要 Configuration 代码。让各个 Configuration 职责更清晰、代码更内聚，更加便于理解、使用及扩展。</li> 
   <li>增加 WebSocket 核心代码模块，全面使用STOMP上层协议，支持 WebSocket 集群 Session共享、信息广播及点对点发送、在线统计，可方便拓展断开重连、心跳机制。</li> 
  </ol> </li> 
 <li> <h3>其它更新</h3> 
  <ol> 
   <li>前端工程升级大量依赖包版本，重新编译生成组件库</li> 
   <li>SpringDoc 升级至 1.5.12</li> 
   <li>Hutool 升级至 5.7.15</li> 
   <li>JustAuth 升级至 1.16.5</li> 
  </ol> </li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.5.70">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.5.70</a></p>
                                        </div>
                                      
</div>
            