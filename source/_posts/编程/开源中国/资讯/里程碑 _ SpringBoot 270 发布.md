
---
title: '里程碑 _ SpringBoot 2.7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9137'
author: 开源中国
comments: false
date: Fri, 20 May 2022 09:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9137'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0"><span>⭐ 新特性</span></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p>为 GraphQL 添加 "application/graphql+json" MIME 类型</p> </li> 
 <li> <p>Spring Security SAML 可针对某一个配置注销策略</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"><span>🐞 Bug 修复</span></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0"><code>SpringApplication</code> 配置的默认属性比使用<code>@PropertySource</code> 3 配置的属性具有更高的优先级</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">WebClient 记录指标时失败导致请求失败#31089</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">Artemis 依赖管理不完整#31079</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">Statsd 组件缺少 buffered 和 step 属性的配置</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">WebFlux 端点的请求调试日志记录格式化为字符串方便阅读</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">@ConditionalOnProperty 元注解 @AliasFor 不起作用</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">JobExecutionExitCodeGenerator 事件处理线程不安全</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">Hibernate 服务加载日志 使用 Gradle 构建警告 ServiceConfigurationError</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">日志配置使用 LOGGING_LEVEL 环境变量时 启动失败</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">未使用 MethodValidationExcludeFilter byAnnotation(Class, SearchStrategy) 的 SearchStrategy 参数</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0"><code>spring.security.saml2.relyingparty.registration.asserting-party</code>属性在断言方中包含不需要的连字符</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">DevTools 设置不推荐 spring.mustache.cache 属性</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"><span>🔨 依赖更新</span></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p>ActiveMQ 5.16.5 #30927</p> </li> 
 <li> <p>Byte Buddy 1.12.10 #30928</p> </li> 
 <li> <p>Cassandra Driver 4.14.1 #30929</p> </li> 
 <li> <p>Couchbase Client 3.2.7 #30930</p> </li> 
 <li> <p>Couchbase Client 3.3.0 #31031</p> </li> 
 <li> <p>Elasticsearch 7.17.3 #30931</p> </li> 
 <li> <p>Flyway 8.5.11 #31080</p> </li> 
 <li> <p>GraphQL Java 18.1 #30859</p> </li> 
 <li> <p>Hibernate 5.6.9.Final #31081</p> </li> 
 <li> <p>Infinispan 13.0.10.Final #30933</p> </li> 
 <li> <p>Jackson Bom 2.13.3 #31046</p> </li> 
 <li> <p>Jaybird 4.0.6.java8 #30934</p> </li> 
 <li> <p>Johnzon 1.2.18 #30935</p> </li> 
 <li> <p>Kafka 3.1.1 #31047</p> </li> 
 <li> <p>Micrometer 1.9.0 #31013</p> </li> 
 <li> <p>Mockito 4.5.1 #30936</p> </li> 
 <li> <p>MSSQL JDBC 10.2.1.jre8 #31048</p> </li> 
 <li> <p>MySQL 8.0.29 #30937</p> </li> 
 <li> <p>Netty 4.1.77.Final #30938</p> </li> 
 <li> <p>Postgresql 42.3.5 #30939</p> </li> 
 <li> <p>Reactor Bom 2020.0.19 #30940</p> </li> 
 <li> <p>Selenium 4.1.4 #30941</p> </li> 
 <li> <p>Selenium HtmlUnit 3.61.0 #30855</p> </li> 
 <li> <p>SendGrid 4.9.2 #31116</p> </li> 
 <li> <p>Spring AMQP 2.4.5 #31022</p> </li> 
 <li> <p>Spring Batch 4.3.6 #31020</p> </li> 
 <li> <p>Spring Data 2021.2.0 #31015</p> </li> 
 <li> <p>Spring for GraphQL 1.0.0 #30858</p> </li> 
 <li> <p>Spring Framework 5.3.20 #31014</p> </li> 
 <li> <p>Spring HATEOAS 1.5.0 #31016</p> </li> 
 <li> <p>Spring Integration 5.5.12 #31062</p> </li> 
 <li> <p>Spring Kafka 2.8.6 #31018</p> </li> 
 <li> <p>Spring LDAP 2.4.0 #31017</p> </li> 
 <li> <p>Spring Security 5.7.1 #31100</p> </li> 
 <li> <p>Spring Session Bom 2021.2.0 #31021</p> </li> 
 <li> <p>Tomcat 9.0.63 #31082</p> </li> 
 <li> <p>UnboundID LDAPSDK 6.0.5 #30942</p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            