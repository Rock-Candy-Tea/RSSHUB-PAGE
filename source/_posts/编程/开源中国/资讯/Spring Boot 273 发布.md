
---
title: 'Spring Boot 2.7.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7106'
author: 开源中国
comments: false
date: Fri, 19 Aug 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7106'
---

<div>   
<div class="content">
                                                                                            <p>Spring Boot 2.7.3 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F08%2F18%2Fspring-boot-2-7-3-available-now" target="_blank">发布</a>，此版本包括 48 个错误修复、文档改进和依赖项升级。具体更新内容如下：</p> 
<p><strong>Bugfix</strong></p> 
<ul> 
 <li>使用 JarMode Layertools 且源不是存档时出现误导性错误消息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32097" target="_blank">#32097</a></li> 
 <li>在 GC 压力下，可以为嵌套 jar 中的类抛出 ClassNotFoundException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32085" target="_blank">#32085</a></li> 
 <li>Flyway 自动配置在 Flyway 9 中失败 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32034" target="_blank">#32034</a></li> 
 <li>BasicJsonParser 不能防止深度嵌套的映射 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32031" target="_blank">#32031</a></li> 
 <li>OptionalLiveReloadServer 在配置为使用临时端口时记录错误的端口号 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31984" target="_blank">#31984</a></li> 
 <li>Servlet WebServerStartStopLifecycle 在停止时未将运行设置为 false <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31967" target="_blank">#31967</a></li> 
 <li>在关闭应用程序上下文期间执行的基于 JUL 的日志记录丢失 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31963" target="_blank">#31963</a></li> 
 <li>添加到胖 jar 中的 spring-boot-jarmode-layertools.jar 的哈希与等效的已发布工件的哈希不匹配 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31949" target="_blank">#31949</a></li> 
 <li>management.endpoint.health.probes.add-additional-paths 在配置属性已经创建了 liveness 和/或 readiness 组时无效<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31926" target="_blank"> #31926</a></li> 
 <li>尝试为 C3P0 设置 jdbcUrl 时抛出 UnsupportedDataSourcePropertyException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31921" target="_blank">#31921</a></li> 
 <li>由太短的 quiet period 难以诊断导致的开发工具重启失败 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31906" target="_blank">#31906</a></li> 
 <li>每次调用时都会重新创建由 CompositeHealthContributor 管理的 HealthContributor bean <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31879" target="_blank">#31879</a></li> 
 <li>REST Assured 的依赖管理不完整 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31877" target="_blank">#31877</a></li> 
 <li>Jar Handler 从未清除 PROTOCOL_HANDLER 系统属性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31875" target="_blank">#31875</a></li> 
 <li>BasicJsonParser 在处理 malformed map JSON时可能会出现超时或堆栈溢出的情况 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31873" target="_blank">#31873</a></li> 
 <li>BasicJsonParser 可能会因 堆栈溢出异常而失败<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31871" target="_blank">#31871</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>文档</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>查看 Git 贡献文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32099" target="_blank">#32099</a></li> 
 <li>Maven 插件分类器的文档有一个未解决的外部引用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32043" target="_blank">#32043</a></li> 
 <li>更新 Static Content 参考文档以反映默认情况下不再启用 DefaultServlet <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32026" target="_blank">#32026</a></li> 
 <li>示例日志输出已过时且不一致 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31987" target="_blank">#31987</a></li> 
 <li>必须启用 Undertow 的 record-request-start-time 服务器选项以便 %D 在访问日志中发挥作用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31976" target="_blank"> #31976</a></li> 
 <li>更新有关使用 H2C 以考虑在执行 TLS 终止的代理后运行的文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31974" target="_blank">#31974</a></li> 
 <li>Common Application Properties 附录中的某些属性没有描述 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31971" target="_blank">#31971</a></li> 
 <li>修复文档中的链接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31951" target="_blank">#31951</a></li> 
 <li>外部配置文档使用不正确的占位符语法 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31943" target="_blank">#31943</a></li> 
 <li>server.reactive.session.cookie 属性未在应用程序属性附录中列出 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31914" target="_blank">#31914</a></li> 
 <li>删除对 ConfigFileApplicationListener 的文档和元数据引用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31901" target="_blank">#31901</a></li> 
 <li>'spring.beaninfo.ignore' 的元数据具有不正确的 SourceType <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31899" target="_blank">#31899</a></li> 
 <li>删除对 nitrite-spring-boot-starter 的引用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31893" target="_blank">#31893</a></li> 
 <li>删除对 Azure Application Insights 的引用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31890" target="_blank">#31890</a></li> 
 <li>修复代码和文档中的拼写错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31865" target="_blank">#31865</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>依赖升级</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>升级到 <span style="background-color:#ffffff; color:#24292f">Byte Buddy</span> 1.12.13 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32013" target="_blank">#32013</a></li> 
 <li>升级到 Couchbase <span style="background-color:#ffffff; color:#24292f">Client</span> 3.3.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32014" target="_blank">#32014</a></li> 
 <li>升级到 <span style="background-color:#ffffff; color:#24292f">Dependency Management Plugin</span> 1.0.13.RELEASE <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32056" target="_blank">#32056</a></li> 
 <li>升级到 Dropwizard <span style="background-color:#ffffff; color:#24292f">Metrics</span> 4.2.11 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32015" target="_blank">#32015</a></li> 
 <li>升级到 <span style="background-color:#ffffff; color:#24292f">Embedded</span> Mongo 3.4.8 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32016" target="_blank">#32016</a></li> 
 <li>升级到 GraphQL Java 18.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31945" target="_blank">#31945</a></li> 
 <li>升级到 Groovy 3.0.12 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32017" target="_blank">#32017</a></li> 
 <li>升级到 Gson 2.9.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32018" target="_blank">#32018</a></li> 
 <li>升级到 Hazelcast 5.1.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32019" target="_blank">#32019</a></li> 
 <li>升级到 Hibernate Validator 6.2.4.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32020" target="_blank">#32020</a></li> 
 <li>升级到 MariaDB 3.0.7 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32021" target="_blank">#32021</a></li> 
 <li>升级到 Maven<span style="background-color:#ffffff; color:#24292f"><span> </span>Javadoc Plugin<span> </span></span>3.4.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32089" target="_blank">#32089</a></li> 
 <li>升级到 <span style="background-color:#ffffff; color:#24292f">Micrometer</span> 1.9.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32022" target="_blank">#32022</a></li> 
 <li>升级到 MySQL 8.0.30 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32023" target="_blank">#32023</a></li> 
 <li>升级到 Reactor 2020.0.22 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32038" target="_blank">#32038</a></li> 
 <li>升级到 Spring Security 5.7.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32040" target="_blank">#32040</a></li> 
 <li>升级到 Undertow 2.2.19.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32090" target="_blank">#32090</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.7.3" target="_blank">https://github.com/spring-projects/spring-boot/releases/tag/v2.7.3</a></p>
                                        </div>
                                      
</div>
            