
---
title: 'Spring Boot 2.6.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1187'
author: 开源中国
comments: false
date: Wed, 22 Dec 2021 09:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1187'
---

<div>   
<div class="content">
                                                                                            <p style="color:#595959; margin-left:0; margin-right:0">12 月 21 日官方发布了 Spring Boot 2.6.2 版本，此版本包括 55 个错误修复、文档改进和依赖项升级。</p> 
<pre><code><span style="color:#000080"><<span style="color:#000080">parent</span>></span>
  <span style="color:#000080"><<span style="color:#000080">groupId</span>></span>org.springframework.boot<span style="color:#000080"></<span style="color:#000080">groupId</span>></span>
  <span style="color:#000080"><<span style="color:#000080">artifactId</span>></span>spring-boot-starter-parent<span style="color:#000080"></<span style="color:#000080">artifactId</span>></span>
  <span style="color:#000080"><<span style="color:#000080">version</span>></span>2.6.2<span style="color:#000080"></<span style="color:#000080">version</span>></span>
  <span style="color:#000080"><<span style="color:#000080">relativePath</span>/></span>
<span style="color:#000080"></<span style="color:#000080">parent</span>></span>
</code></pre> 
<h2><span>BUG 修复</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>当 getter 或 setter 被覆盖以使用属性类型的子类时，配置属性绑定期间使用的 getter 和 setter 会有所不同</p> </li> 
 <li> <p><code>DatabaseInitializationDependencyConfigurer</code>触发了<code>factory beans</code>的饿加载</p> </li> 
 <li> <p>在 Spring Boot 2.6.0 中,<code>Quartz</code>无法在<code>mysql</code>/<code>mariadb</code>数据库下建表</p> </li> 
 <li> <p><code>Quartz</code>, <code>Session</code>, <code>Integration</code>和 <code>Batch</code>的数据库平台初始化无法被配置</p> </li> 
 <li> <p>依赖<code>thymeleaf-extras-springsecurity5</code>但没有包含<code>Spring Security</code>时，应用启动失败</p> </li> 
 <li> <p>使用 Spring Security 时，<code>ResponseStatusException</code>没有返回响应体</p> </li> 
 <li> <p><code>DatabaseInitializationMode</code>为<code>never</code>时，<code>DataSourceScriptDatabaseInitializer</code>依然尝试访问数据库</p> </li> 
 <li> <p>在 Spring Boot 2.6.1 中，设置<code>useCodeAsDefaultMessage</code>属性为<code>true</code>时导致<code>Hibernate validation messages</code>无法正常工作</p> </li> 
 <li> <p>没有设置镜像构建包的标签时，不会默认设置<code>latest</code></p> </li> 
 <li> <p>使用 maven 编译 war 文件时出现无效的类路径索引清单属性</p> </li> 
 <li> <p>发布到兼容 Servlet3.1 规范的容器时，<code>org.springframework.boot.web.servlet.filter.ErrorPageSecurityFilter</code>出现的抽象方法错误</p> </li> 
 <li> <p>为健康检查端点设置缓存<code>time-to-live</code>属性无效</p> </li> 
 <li> <p><code>server.servlet.session.cookie.same-site</code>无法被应用在 spring-session 创建的 Cookie</p> </li> 
</ul> 
<h2><span>文档改进</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>2.5.x 快照文档链接到主分支上的源代码</p> </li> 
 <li> <p>WebFlux 不支持将 DevTools 与远程应用程序一起使用的文档</p> </li> 
 <li> <p>发布在核心功能参考文档中创建您自己的自动配置部分</p> </li> 
 <li> <p>发布参考文档中的 CacheManager 自定义部分</p> </li> 
 <li> <p>发布 README.adoc</p> </li> 
 <li> <p>修复属性 spring.mvc.pathmatch.matching-strategy 的记录默认值</p> </li> 
 <li> <p>在参考文档的 YAML 示例中添加一致的引号</p> </li> 
</ul> 
<h2><span>依赖项升级</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>Upgrade to Logback 1.2.9</p> </li> 
 <li> <p>Upgrade to AppEngine SDK 1.9.93</p> </li> 
 <li> <p>Upgrade to Caffeine 2.9.3</p> </li> 
 <li> <p>Upgrade to Couchbase Client 3.2.4</p> </li> 
 <li> <p>Upgrade to DB2 JDBC 11.5.7.0</p> </li> 
 <li> <p>Upgrade to Dropwizard Metrics 4.2.7</p> </li> 
 <li> <p>Upgrade to Ehcache3 3.9.9</p> </li> 
 <li> <p>Upgrade to Flyway 8.0.5</p> </li> 
 <li> <p>Upgrade to Hazelcast 4.2.4</p> </li> 
 <li> <p>Upgrade to Hibernate 5.6.3.Final</p> </li> 
 <li> <p>Upgrade to HttpAsyncClient 4.1.5</p> </li> 
 <li> <p>Upgrade to HttpCore 4.4.15</p> </li> 
 <li> <p>Upgrade to Infinispan 12.1.10.Final</p> </li> 
 <li> <p>Upgrade to Jackson Bom 2.13.1</p> </li> 
 <li> <p>Upgrade to JDOM2 2.0.6.1</p> </li> 
 <li> <p>Upgrade to Jedis 3.7.1</p> </li> 
 <li> <p>Upgrade to JUnit Jupiter 5.8.2</p> </li> 
 <li> <p>Upgrade to Kotlin 1.6.10</p> </li> 
 <li> <p>Upgrade to Log4j2 2.17.0</p> </li> 
 <li> <p>Upgrade to Micrometer 1.8.1</p> </li> 
 <li> <p>Upgrade to MSSQL JDBC 9.4.1.jre8</p> </li> 
 <li> <p>Upgrade to Netty 4.1.72.Final</p> </li> 
 <li> <p>Upgrade to Reactor 2020.0.14</p> </li> 
 <li> <p>Upgrade to Spring AMQP 2.4.1</p> </li> 
 <li> <p>Upgrade to Spring Framework 5.3.14</p> </li> 
 <li> <p>Upgrade to Spring Integration 5.5.7</p> </li> 
 <li> <p>Upgrade to Spring Kafka 2.8.1</p> </li> 
 <li> <p>Upgrade to Spring LDAP 2.3.5</p> </li> 
 <li> <p>Upgrade to Spring Security 5.6.1</p> </li> 
 <li> <p>Upgrade to Spring Session 2021.1.1</p> </li> 
 <li> <p>Upgrade to Spring WS 3.1.2</p> </li> 
 <li> <p>Upgrade to Thymeleaf 3.0.14.RELEASE</p> </li> 
 <li> <p>Upgrade to Tomcat 9.0.56</p> </li> 
 <li> <p>Upgrade to Undertow 2.2.14.Final</p> </li> 
 <li> <p>Upgrade to XmlUnit2 2.8.4</p> </li> 
</ul>
                                        </div>
                                      
</div>
            