
---
title: 'Spring Boot 2.6.11 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8791'
author: 开源中国
comments: false
date: Sat, 20 Aug 2022 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8791'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0">Spring Boot 2.6.11 已发布，更新内容主要是修复错误、改进文档以及升级依赖。</p> 
<p style="margin-left:0"><strong>Bugfix</strong></p> 
<ul> 
 <li>修复 BasicJsonParser 无法保护深度嵌套 map 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32029" target="_blank">#32029</a></li> 
 <li>当使用 JarMode Layertools，并且源码不是一个归档文件时，会出现误导性的错误信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31997" target="_blank">#31997</a></li> 
 <li>当 OptionalLiveReloadServer 被配置为使用瞬时端口 (ephemeral port) 时，它记录了错误的端口号 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31983" target="_blank">#31983</a></li> 
 <li><span style="color:#24292f">Servlet WebServerStartStopLifecycle 在停止时未将 running 设置为 false</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31966" target="_blank">#31966</a></li> 
 <li><span style="color:#24292f">尝试为 C3P0 设置 jdbcUrl 时，抛出 UnsupportedDataSourcePropertyException 异常</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31920" target="_blank">#31920</a></li> 
 <li>Jar Handler 永远不会清除 PROTOCOL_HANDLER 系统属性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31870" target="_blank">#31870</a></li> 
 <li>修复 <span style="color:#24292f">BasicJsonParser 解析可能会因 stackoverflow 异常而失败的问题</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31868" target="_blank">#31868</a></li> 
 <li>修复 <span style="color:#24292f">REST Assured 依赖管理不完整的问题</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31864" target="_blank">#31864</a></li> 
 <li>修复在关闭应用程序上下文期间执行的基于 JUL 的日志记录会丢失的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F9457" target="_blank">#9457</a></li> 
</ul> 
<p><strong>改进文档</strong></p> 
<ul> 
 <li>优化<span style="color:#24292f">外部配置文档使用不正确占位符语法的问题</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31941" target="_blank">#31941</a></li> 
 <li><span style="color:#24292f">改进 Common Application Properties 附录中某些属性没有描述的问题</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31916" target="_blank">#31916</a></li> 
 <li><span style="color:#24292f">删除对 ConfigFileApplicationListener 的文档和元数据引用</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31895" target="_blank">#31895</a></li> 
 <li>删除对 nitrite-spring-boot-starter 的引用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31892" target="_blank">#31892</a></li> 
 <li>删除对 Azure Application Insights 的引用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31889" target="_blank">#31889</a></li> 
 <li>修复文档中的链接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31887" target="_blank">#31887</a></li> 
 <li>修复代码和文档中的拼写错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31734" target="_blank">#31734</a></li> 
 <li>修复示例日志输出已过时且不一致的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28208" target="_blank">#28208</a></li> 
</ul> 
<p><strong>升级依赖</strong></p> 
<ul> 
 <li>Upgrade to Dependency Management Plugin 1.0.13.RELEASE <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32055" target="_blank">#32055</a></li> 
 <li>Upgrade to Dropwizard Metrics 4.2.11 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32007" target="_blank">#32007</a></li> 
 <li>Upgrade to Groovy 3.0.12 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32008" target="_blank">#32008</a></li> 
 <li>Upgrade to Hibernate Validator 6.2.4.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32009" target="_blank">#32009</a></li> 
 <li>Upgrade to Micrometer 1.8.9 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32010" target="_blank">#32010</a></li> 
 <li>Upgrade to MySQL 8.0.30 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32011" target="_blank">#32011</a></li> 
 <li>Upgrade to Netty tcNative 2.0.54.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32012" target="_blank">#32012</a></li> 
 <li>Upgrade to Reactor 2020.0.22 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32037" target="_blank">#32037</a></li> 
 <li>Upgrade to Spring Security 5.6.7 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32039" target="_blank">#32039</a></li> 
 <li>Upgrade to Undertow 2.2.19.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32087" target="_blank">#32087</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.6.11" target="_blank">Release Note</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F08%2F17%2Fspring-boot-2-6-11-available-now" target="_blank">发布公告</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            