
---
title: 'Spring Boot 2.5.4 已发布，MateCloud 同步完成升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-488316810d888e54ae93b90ac6946d92b3f.png'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 03:15:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-488316810d888e54ae93b90ac6946d92b3f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>一、发布说明</h2> 
<p><span style="background-color:#ffffff; color:#333333">于美国时间8月19日发布Spring Boot 2.5.4版本，此版本35 个错误修复、文档改进和依赖项升级。已经可以从中央仓库中更新。</span></p> 
<p><img height="306" src="https://oscimg.oschina.net/oscnet/up-488316810d888e54ae93b90ac6946d92b3f.png" width="1332" referrerpolicy="no-referrer"></p> 
<h2>二、更新内容</h2> 
<h3>2.1 错误修复</h3> 
<ul> 
 <li>spring-boot-configuration-metadata 将依赖约束泄漏到消费构建中<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27730" target="_blank">#27730</a></li> 
 <li>潜在 NPE<code>TomcatMetricsBinder.findContext() </code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27616" target="_blank">#27616 </a></li> 
 <li>当 Spring Data 存储库是 MeterBinder 的依赖项时的循环 bean 定义<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27591" target="_blank">#27591</a></li> 
 <li>spring-boot:build-image 在上传过程中抛出异常时挂起 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27535" target="_blank">#27535</a></li> 
 <li>当 WebClient 在没有支持的 HTTP 客户端的类路径上时，WebTestClientContextCustomizerFactory 会导致 IllegalStateException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27527" target="_blank">#27527</a></li> 
 <li>在单独的管理上下文中运行时，sp​​ring.security.dispatcher-types 不适用于 Spring Security 的过滤器<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27505" target="_blank">#27505</a></li> 
 <li>方案中包含未经过清理的非字母字符的URI <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27488" target="_blank">#27488</a></li> 
</ul> 
<h2>2.2 文档</h2> 
<ul> 
 <li>在 Gradle 插件的文档中提及 productionRuntimeClasspath <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27620" target="_blank">#27620</a></li> 
 <li>修复 javadoc 中的错字<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27618" target="_blank">#27618</a></li> 
</ul> 
<h2>2.3 <span style="color:#24292e"><span style="background-color:#ffffff">依赖升级</span></span></h2> 
<ul> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 ActiveMQ 5.16.3 #27742</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 AppEngine SDK 1.9.91 #27743</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Cassandra Driver 4.11.3 #27674</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Couchbase Client 3.1.7 #27675</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Ehcache3 3.9.5 #27676</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Glassfish JAXB 2.3.5 #27677</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Hazelcast 4.1.5 #27744</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Hazelcast Hibernate5 2.2.1 #27678</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Janino 3.1.6 #27679</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Logback 1.2.5 #27680</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 MariaDB 2.7.4 #27681</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Maven Enforcer Plugin 3.0.0 #27682</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Micrometer 1.7.3 #27601</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 MIMEPull 1.9.15 #27683</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Netty 4.1.67.Final #27745</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Nimbus JOSE JWT 9.10.1 #27701</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 OAuth2 OIDC SDK 9.9.1 #27700</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Reactor 2020.0.10 #27600</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 SendGrid 4.7.4 #27684</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Spring Data 2021.0.4 #27633</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Spring Integration 5.5.3 #27604</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Spring Kafka 2.7.6 #27602</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Spring Security 5.5.2 #27603</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Spring Session 2021.0.2 #27605</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Tomcat 9.0.52 #27685</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Undertow 2.2.10.Final #27686</span></span></li> 
</ul> 
<p>更多请参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.5.4" target="_blank">https://github.com/spring-projects/spring-boot/releases/tag/v2.5.4</a></p> 
<h2 style="text-align:left">三、同步更新</h2> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">MateCloud 基于Spring Cloud Alibaba推出的微服务快速开发平台，集成Nacos 2.0.3、Sentinel 1.8.2、Jetcache等诸多中间件。前端采用Vue 3.2.2、Pinia 2.0.0-rc.4、Vite </span><span style="background-color:#ffffff; color:#40485b">2.5.0-beta.2</span><span style="background-color:#ffffff; color:#333333">、 Ant-Design-Vue </span><span style="background-color:#ffffff; color:#40485b">2.2.6</span><span style="background-color:#ffffff; color:#333333">、TypeScript 的大型中后台解决方案。目前dev分支已升级</span></p> 
<p style="text-align:left"><a href="https://gitee.com/matevip/matecloud">https://gitee.com/matevip/matecloud</a></p>
                                        </div>
                                      
</div>
            