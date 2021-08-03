
---
title: 'Spring Cloud 2021.0.0-M1（代号 Jubilee）发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bdaf77cb346f46aef9976ee7dd236b1fcaf.png'
author: 开源中国
comments: false
date: Tue, 03 Aug 2021 08:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bdaf77cb346f46aef9976ee7dd236b1fcaf.png'
---

<div>   
<div class="content">
                                                                                            <h2>一、发布说明</h2> 
<p>Spring Cloud 2021.0.0-M1 现已发布。该版本可以在 Spring Milestone 存储库中找到，并与 Spring Boot 2.6.0-M1 兼容。GITHUB项目可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Forgs%2Fspring-cloud%2Fprojects%2F63" onclick="s_objectID='apps_scodevmw : 此处 : 76'" target="_blank">此处</a>找到。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bdaf77cb346f46aef9976ee7dd236b1fcaf.png" referrerpolicy="no-referrer"></p> 
<h2>二、更新内容</h2> 
<h3 style="text-align:start">2.1 Spring Cloud Gateway</h3> 
<ul> 
 <li>StripPrefixFilter 现在默认为 1 而不是 0</li> 
 <li>添加新的 CacheRequestBodyFilter</li> 
 <li>使用 Redis 跨网关实例共享路由</li> 
</ul> 
<h3>2.2 Spring Cloud Sleuth</h3> 
<ul> 
 <li>添加 JDBC 支持</li> 
 <li>支持 Spring Vault</li> 
 <li>自动标签表生成文档</li> 
 <li>支持 Spring Cloud Deployer</li> 
 <li>支持 Spring Cloud Skipper</li> 
 <li>支持 R2DBC</li> 
 <li>支持 Reactor Kafka</li> 
 <li>支持 Spring Batch</li> 
 <li>RSocket 检测 #1677</li> 
 <li>支持 Spring Cloud 任务 </li> 
 <li>Spring Cloud 配置检测 </li> 
 <li>添加了对 Spring Cloud Circuit Breaker Reactive 的支持</li> 
 <li>添加了对 Kotlin 协程的支持 </li> 
</ul> 
<h3>2.3 Spring Cloud Openfeign</h3> 
<ul> 
 <li>将 Feign 提升到 11.6</li> 
</ul> 
<h3>2.4 Spring Cloud Kubernetes</h3> 
<ul> 
 <li>更新 kubernetes-client 至 5.5.0</li> 
</ul> 
<h3>2.5 Spring Cloud Task</h3> 
<ul> 
 <li>升级 Spring Cloud Stream 至 3.2</li> 
 <li>通过删除 TaskJobLauncherCommandLineRunner 以支持 TaskJobLauncherApplicationRunner，为 Spring Boot 2.6 做好准备</li> 
</ul> 
<h3>2.6 Spring Cloud Config</h3> 
<ul> 
 <li>与 AWS Secrets Manager 集成</li> 
 <li>GCP 秘密管理器集成</li> 
 <li>支持 AWS Systems Manager Parameter Store</li> 
</ul> 
<h3 style="text-align:start">2.7 Spring Cloud Contract</h3> 
<ul> 
 <li>支持 JDK16</li> 
</ul> 
<p>更多说明请参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F07%2F30%2Fspring-cloud-2021-0-0-m1-aka-jubilee-is-available" target="_blank">https://spring.io/blog/2021/07/30/spring-cloud-2021-0-0-m1-aka-jubilee-is-available</a></p> 
<h2 style="text-align:left"><span style="color:#24292e"><span style="background-color:#ffffff">三、 应用案例</span></span></h2> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#4a4a4a"><a href="https://gitee.com/matevip/matecloud">MateCloud</a>是一款基于Spring Cloud Alibaba的微服务架构。目前已经整合Spring Boot 2.5.3、 Spring Cloud 2020.3、Spring Cloud Alibaba 2021.1、Nacos2.0.3、Sentinel 1.8.2、Spring Security Oauth2、Feign、Dubbo、JetCache、RocketMQ等服务套件，集成了大量的工具类组件的微服务快速开发平台。</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#4a4a4a">项目地址：</span><a href="https://gitee.com/matevip/matecloud">https://gitee.com/matevip/matecloud</a></p>
                                        </div>
                                      
</div>
            