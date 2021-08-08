
---
title: 'Eurynome Cloud v2.5.4.20 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9808'
author: 开源中国
comments: false
date: Sat, 07 Aug 2021 21:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9808'
---

<div>   
<div class="content">
                                                                                            <p>Eurynome Cloud v2.5.4.20 已经发布，企业级技术中台微服务架构。</p> 
<p>此版本更新内容包括：</p> 
<p>v2.5.4.20</p> 
<ol> 
 <li>本地权限缓存更换为JetCache，为服务多实例的权限扫描和存储提供更好的支持</li> 
 <li>将数据访问策略从Conditional类，升级为Conditional注解，使用更加便捷</li> 
 <li>调整包依赖关系，新建assistant、constant包，删除message包。 逐步将平台中各类非独有常量移入constant包方便管理和修改</li> 
 <li>采用Spring Boot Event和Spring Cloud Bus Event 机制重构接口收集逻辑。支持单体架构、UPMS、分布式多实例等不同场景接口扫描的特殊需求</li> 
 <li>优化Docker Compose配置，使用Debezium Kafka 替换已有kafka，以支持Debezium应用</li> 
 <li>删除无用代码</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.20">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.20</a></p> 
<hr> 
<p> </p> 
<p>Eurynome Cloud是一款企业级微服务架构和服务能力开发平台。基于Spring Boot 2.5.3、Spring Cloud 2020.0.3、Spring Cloud Alibaba 2021.1、Nacos 2.0.3 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能，代码简洁，架构清晰，非常适合学习和企业作为基础框架使用。</p> 
<p> </p>
                                        </div>
                                      
</div>
            