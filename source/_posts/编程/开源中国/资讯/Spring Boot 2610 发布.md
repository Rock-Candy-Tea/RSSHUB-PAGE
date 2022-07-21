
---
title: 'Spring Boot 2.6.10 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7865'
author: 开源中国
comments: false
date: Thu, 21 Jul 2022 10:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7865'
---

<div>   
<div class="content">
                                                                                            <p>Spring Boot 2.6.10 已发布，更新内容主要是修复错误、改进文档以及升级依赖。</p> 
<p><strong>Bugfix</strong></p> 
<ul> 
 <li>修复<span style="background-color:#ffffff; color:#24292f">在自定义类加载器加载的 jar 包中使用</span>'ImportAutoConfigurationImportSelector'<span style="background-color:#ffffff; color:#24292f">会引发 ClassNotFoundException 的问题</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31798" target="_blank">#31798</a></li> 
 <li>修复由于 UnsupportedOperationException 异常，包含属性的路由函数会导致 /actuator/ 映射返回 500 响应码的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31784" target="_blank">#31784</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">使用 Log4j 2.18 或更高版本时没有禁用 Log4j2 的 shutdown hook</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31719" target="_blank">#31719</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">使用具有多个上下文并启用 JMX 的 Actuator 时出现 InstanceAlreadyExistsException 异常</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31718" target="_blank">#31718</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">spring.data.mongodb.grid-fs-database 的弃用提示位于错误的部分</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31689" target="_blank">#31689</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果返回时间较长，ApplicationPid 不会记录警告</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31572" target="_blank">#31572</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在故障分析描述中，难以识别属性值中的行尾空格 (</span>Trailing whitespace<span style="background-color:#ffffff; color:#24292f">)</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31571" target="_blank">#31571</a></li> 
 <li>修复 Derby 依赖管理不完整的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31570" target="_blank">#31570</a></li> 
 <li>HTTP Server 和数据存储库的指标描述记录为空<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F31516" target="_blank">#31516</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">使用最新的 Paketo base 构建器和配置的其他构建包，构建镜像失败</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31233" target="_blank">#31233</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">将 docker 镜像发布到私有注册表会在没有身份验证的情况下失败</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28844" target="_blank">#28844</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在非反应式应用程序中，找不到父上下文中的健康指标</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27308" target="_blank">#27308</a></li> 
</ul> 
<p><strong>改进文档</strong></p> 
<ul> 
 <li>说明如何确定 docker 镜像的发布注册表<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31820" target="_blank">#31820</a></li> 
</ul> 
<p><strong>升级依赖</strong></p> 
<ul> 
 <li>Upgrade to AppEngine SDK 1.9.98<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31788" target="_blank">#31788</a></li> 
 <li>Upgrade to Dependency Management Plugin 1.0.12.RELEASE<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31555" target="_blank">#31555</a></li> 
 <li>Upgrade to Hibernate 5.6.10.Final<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31724" target="_blank">#31724</a></li> 
 <li>Upgrade to HttpCore5 5.1.4<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31725" target="_blank">#31725</a></li> 
 <li>Upgrade to Jetty Reactive HTTPClient 1.1.12<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31726" target="_blank">#31726</a></li> 
 <li>Upgrade to JsonAssert 1.5.1<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31727" target="_blank">#31727</a></li> 
 <li>Upgrade to Lettuce 6.1.9.RELEASE<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31728" target="_blank">#31728</a></li> 
 <li>Upgrade to MariaDB 2.7.6<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31729" target="_blank">#31729</a></li> 
 <li>Upgrade to Micrometer 1.8.8<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31612" target="_blank">#31612</a></li> 
 <li>Upgrade to Neo4j Java Driver 4.4.9<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31730" target="_blank">#31730</a></li> 
 <li>Upgrade to Netty 4.1.79.Final<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31731" target="_blank">#31731</a></li> 
 <li>Upgrade to Reactor 2020.0.21<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31607" target="_blank">#31607</a></li> 
 <li>Upgrade to Spring Data 2021.1.6<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31611" target="_blank">#31611</a></li> 
 <li>Upgrade to Spring Framework 5.3.22<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31610" target="_blank">#31610</a></li> 
 <li>Upgrade to Spring Integration 5.5.14<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31799" target="_blank">#31799</a></li> 
 <li>Upgrade to Spring Kafka 2.8.8<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31785" target="_blank">#31785</a></li> 
 <li>Upgrade to Tomcat 9.0.65<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31829" target="_blank">#31829</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.6.10" target="_blank">Release Note</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F07%2F21%2Fspring-boot-2-6-10-available-now" target="_blank">发布公告</a></p>
                                        </div>
                                      
</div>
            