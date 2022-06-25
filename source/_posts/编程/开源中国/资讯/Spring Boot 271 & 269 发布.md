
---
title: 'Spring Boot 2.7.1 & 2.6.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8537'
author: 开源中国
comments: false
date: Sat, 25 Jun 2022 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8537'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Spring Boot 为两个分支发布了更新，分别是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F06%2F23%2Fspring-boot-2-7-1-available-now" target="_blank"><span> </span>2.7.1<span> </span></a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F06%2F23%2Fspring-boot-2-6-9-available-now" target="_blank"><span> </span>2.6.9</a>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新内容包括修复错误、优化文档以及升级依赖。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.7.1" target="_blank"><strong>v2.7.1</strong></a></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复使用 HTTP/2 时忽略 Tomcat server.max-http-header-size 属性的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31329" target="_blank">#31329</a></li> 
 <li>修复 OAuth2 Resource Server Auto-Configuration 只能配置单个 JWS 算法的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31321" target="_blank">#31321</a></li> 
 <li>修复 spring-boot-starter-parent 中的 Maven shade 插件配置不附加 META-INF/spring/*.imports 文件的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31316" target="_blank">#31316</a></li> 
 <li>修复 spring-boot-dependencies 管理不再存在的 spring-ldap-ldif-batch 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31254" target="_blank">#31254</a></li> 
 <li>MimeMappings 不再包含 application/wasm <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31188" target="_blank">#31188</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.6.9" target="_blank"><strong>v2.6.9</strong></a></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复格式错误的 json 导致 BasicJsonParser 抛出 NullPointerException 异常 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31301" target="_blank">#31301</a></li> 
 <li>修复 spring.data.cassandra.config 文件中的值不能覆盖 CassandraProperties 中定义的部分默认值 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31238" target="_blank">#31238</a></li> 
 <li>需要很长时间才能响应的健康指标难以诊断 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31231" target="_blank">#31231</a></li> 
 <li>layers.xsd 与包含和排除模块依赖项的文档和实现不同步<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31127" target="_blank">#31127</a></li> 
 <li><code>@RestControllerAdvice</code> <code>@ExceptionHandler</code>与<code>@RestControllerEndpoint</code>行为不一致<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31495" target="_blank">#31495</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            