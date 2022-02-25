
---
title: 'Spring Boot 2.5.10 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9756'
author: 开源中国
comments: false
date: Fri, 25 Feb 2022 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9756'
---

<div>   
<div class="content">
                                                                                            <p>Spring Boot 2.5.10 已经发布，该版本包括 52 个错误修复、文档改进和依赖性升级。</p> 
<h3>错误修复</h3> 
<ul> 
 <li>默认的 JmxAutoConfiguration 改变了多属性 <code>@ManagedResource</code> 对象名称的 JConsole 层次结构</li> 
 <li>当配置文件的名称包含一个逗号时，活动配置文件的日志信息是不明确的</li> 
 <li>失败的应用程序上下文没有从 SpringApplicationShutdownHook 中取消注册</li> 
 <li>Gradle 插件触发了某些任务的急切配置</li> 
 <li>ots 的 MimeMapping 在其 mime 类型中有一个尾随空格（trailing space）</li> 
 <li>Liquibase 的依赖管理不包括其 liquibase-cdi 模块</li> 
 <li>读取日志更新事件时忽略无效的流类型</li> 
 <li>bootJar、bootRun 和 bootWar 不会获取在应用 Boot 插件后对主源集的运行时 classpath 所做的更改</li> 
 <li>当存在循环引用时， <code>@SpyBean</code> 导致 BeanCurrentlyInCreationException</li> 
 <li>用 Gradle 构建的胖 jar 将 META-INF 移至 BOOT-INF/classes 之下，而 Maven 则将其留在 jar 的根部</li> 
</ul> 
<h3>文档</h3> 
<ul> 
 <li>bootRun 示例应使用 mainClass，而不是 Gradle 7.1 中废弃的 main</li> 
 <li>"Customizing the Banner" 应更明显地说明可以使用任何环境属性</li> 
 <li>更新 javadoc 以反映从 WebSecurityConfigurerAdapter 到 SecurityFilterChain 的变化</li> 
 <li>添加 WebMvc.fn 的文档</li> 
 <li>在 Gradle 插件文档中，将实例中的 classifier（已废弃）改为 archiveClassifier</li> 
 <li>升级参考文档中 gradle-git-properties 的版本</li> 
 <li>将 Boxfuse 改名为 CloudCaptain</li> 
 <li>提供一些关于识别和解决 Devtools 类加载问题的指导</li> 
 <li>警告使用 <code>@ConditionalOnExpression</code> 时早期 bean 初始化的危险</li> 
 <li>记录下 <code>@DefaultValue</code> 注解中的占位符未解析</li> 
 <li>……</li> 
</ul> 
<h3>依赖项升级</h3> 
<ul> 
 <li>ActiveMQ 升级到 5.16.4</li> 
 <li>AppEngine SDK 升级到 1.9.95</li> 
 <li>Dropwizard Metrics 升级到 4.1.30</li> 
 <li>Glassfish JAXB 升级到 2.3.6</li> 
 <li>Hibernate Validator 升级到 6.2.2.Final</li> 
 <li>Jetty 升级到 9.4.45.v20220203</li> 
 <li>Jetty Reactive HTTPClient 升级到 1.1.11</li> 
 <li>Johnzon 升级到 1.2.16</li> 
 <li>Json-smart 升级到 2.4.8</li> 
 <li>Micrometer 升级到 1.7.9</li> 
 <li>Neo4j Java Driver 升级到 4.2.9</li> 
 <li>Netty 升级到 4.1.74.Final</li> 
 <li>Netty tcNative 升级到 2.0.50.Final</li> 
 <li>Postgresql 升级到 42.2.25</li> 
 <li>Reactor 升级到 2020.0.16</li> 
 <li>SLF4J 升级到 1.7.36</li> 
 <li>Spring Batch 升级到 4.3.5</li> 
 <li>Spring Data 升级到 2021.0.9</li> 
 <li>Spring Framework 升级到 5.3.16</li> 
 <li>Spring Integration 升级到 5.5.9</li> 
 <li>Spring Kafka 升级到 2.7.11</li> 
 <li>Spring LDAP 升级到 2.3.6</li> 
 <li>Spring Security 升级到 5.5.5</li> 
 <li>Spring Session 升级到 2021.0.5</li> 
 <li>Thymeleaf 升级到 3.0.15.RELEASE</li> 
 <li>Tomcat 升级到 9.0.58</li> 
 <li>Undertow 升级到 2.2.16.Final</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.5.10" target="_blank">https://github.com/spring-projects/spring-boot/releases/tag/v2.5.10</a></p>
                                        </div>
                                      
</div>
            