
---
title: 'Spring Native 0.11.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7210'
author: 开源中国
comments: false
date: Sat, 05 Mar 2022 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7210'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Spring Native 0.11.3<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F03%2F01%2Fspring-native-0-11-3-available-now" target="_blank">已发布</a>。更新内容包括修复 bug、改进文档、升级依赖以及引入新特性。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#252525">Spring Native（前身为 Spring GraalVM Native，Spring 社区试验性项目）通过使用 GraalVM 原生镜像编译器将 Spring 应用程序编译为独立的系统原生可执行文件（无需安装 JVM），提供了一种在轻量级容器中原生部署 Spring 应用程序的新方法，支持 Java 和 Kotlin，并提供有趣的特性，包括几乎即时启动（通常<100ms），即时峰值性能和较低的内存消耗，但所需的构建时间和运行时优化次数少于 JVM。目标是在此新平台上几乎不做修改就能支持 Spring Boot 应用程序。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>新特性</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>优化 Spring Data 仓库触发器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1504" target="_blank">#1504</a></li> 
 <li>添加对 ManagedList 和 ManagedSet 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1483" target="_blank">#1483</a></li> 
 <li>支持"<code>@SpringBootTest</code>"中的"args"参数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1447" target="_blank">#1447</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>优化兼容性</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新 FunctionHints 以及 s-c-function 所需的额外提示 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1497" target="_blank">#1497</a></li> 
 <li>添加 HdrHistogram 所缺失的提示 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1484" target="_blank">#1484</a></li> 
 <li>spring-aot-test: 引入多扩展或多嵌套的测试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1474" target="_blank">#1474</a></li> 
 <li>JPA : antlr error with <code>@ElementCollection</code> <code>@OrderBy</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1473" target="_blank">#1473</a></li> 
 <li><span style="color:#24292f">在涉及反射时优化对 kotlinx.serialization 的支持</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1410" target="_blank">#1410</a></li> 
 <li>ErrorAttributes 序列化异常 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1084" target="_blank">#1084</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Bug Fixes</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持使用自定义 text banner <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1501" target="_blank">#1501</a></li> 
 <li>修复无法查找 DefaultPersistenceUnitManager 的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1500" target="_blank">#1500</a></li> 
 <li>修复 Spring Data Elasticsearch 的回归错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1492" target="_blank">#1492</a></li> 
 <li>使用 records 优化显式<code>@ConfigurationPropertie</code> 处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1491" target="_blank">#1491</a></li> 
 <li>支持<code>@SpringBootConfiguration</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1490" target="_blank">#1490</a></li> 
 <li>修复 SimpleMongoRepository 中无法找到合适构造函数的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1487" target="_blank">#1487</a></li> 
 <li>内部 bean 定义的 beanClass 可能未被解析，并以 Object 而非目标类型生成 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1481" target="_blank">#1481</a></li> 
 <li>修复与 Flyway 和 Liquibase 的循环依赖关系 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1480" target="_blank">#1480</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>改进文档</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Document Spring Boot substitutions <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1475" target="_blank">#1475</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>升级依赖</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将 GraalVM 升级至 22.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1448" target="_blank">#1448</a></li> 
 <li>将 native build tools 升级至 0.9.10 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1495" target="_blank">#1495</a></li> 
 <li>将 Spring Boot 升级至 2.6.4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1489" target="_blank">#1489</a></li> 
 <li>将 Spring Cloud 升级至 2021.0.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1512" target="_blank">#1512</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Freleases%2Ftag%2F0.11.3" target="_blank">详情查看 release notes</a>。</p>
                                        </div>
                                      
</div>
            