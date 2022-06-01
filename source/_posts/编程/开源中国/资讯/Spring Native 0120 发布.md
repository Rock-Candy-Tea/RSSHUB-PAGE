
---
title: 'Spring Native 0.12.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9616'
author: 开源中国
comments: false
date: Wed, 01 Jun 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9616'
---

<div>   
<div class="content">
                                                                                            <p>Spring Native 0.12.0 现已发布。此版本包括 12 个 bug 修复、文档改进以及对 GraalVM 22.1、Spring Boot 2.7.0 和 Spring Cloud 2021.0.3 的依赖项升级。</p> 
<p><span style="color:#252525">Spring Native（前身为 Spring GraalVM Native，Spring 社区试验性项目）通过使用 GraalVM 原生镜像编译器将 Spring 应用程序编译为独立的系统原生可执行文件（无需安装 JVM），提供了一种在轻量级容器中原生部署 Spring 应用程序的新方法，支持 Java 和 Kotlin，并提供有趣的特性，包括几乎即时启动（通常 < 100ms），即时峰值性能和较低的内存消耗，但所需的构建时间和运行时优化次数少于 JVM。目标是在此新平台上几乎不做修改就能支持 Spring Boot 应用程序。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#252525">具体更新内容如下：</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>兼容性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复 GraalVM 22.1的 session-redis-webflux 和 session-without-security samples <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1588" target="_blank">#1588</a></li> 
 <li>更新 Batch schemas <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1573" target="_blank">#1573</a></li> 
</ul> 
<p><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>Devtools developmentOnly 依赖破坏了 Gradle 的 AOT generation <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1579" target="_blank">#1579</a></li> 
 <li>文件名或扩展名太长<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1567" target="_blank">#1567</a></li> 
</ul> 
<p><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>文档</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复损坏的链接和过时的插件名称<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1583" target="_blank">#1583</a></li> 
</ul> 
<p><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>依赖升级</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>将 GraalVM 更新到 22.1.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1621" target="_blank">#1621</a></li> 
 <li>升级到 Spring Boot 2.7.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1541" target="_blank">#1541</a></li> 
 <li>升级到 Spring Cloud 2021.0.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1606" target="_blank">#1606</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F05%2F31%2Fspring-native-0-12-0-available-now" target="_blank">https://spring.io/blog/2022/05/31/spring-native-0-12-0-available-now</a></p>
                                        </div>
                                      
</div>
            