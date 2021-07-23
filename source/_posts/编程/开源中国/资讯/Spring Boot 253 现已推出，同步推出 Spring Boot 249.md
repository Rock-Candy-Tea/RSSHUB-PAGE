
---
title: 'Spring Boot 2.5.3 现已推出，同步推出 Spring Boot 2.4.9'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a5537fccb0bddd9fae66eafbee72fc72514.png'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 07:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a5537fccb0bddd9fae66eafbee72fc72514.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:left">一、发布说明</h2> 
<p style="text-align:left">于美国时间7月22日发布Spring Boot 2.5.3版本，此版本包括58 个错误修复、文档改进和依赖项升级。</p> 
<p style="text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-a5537fccb0bddd9fae66eafbee72fc72514.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">二、更新内容</h2> 
<h3 style="text-align:left">2.1 新的功能</h3> 
<ul> 
 <li>将 Java 17 添加到 JavaVersion 枚举<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F26769" target="_blank">#26769</a></li> 
</ul> 
<h3>2.2 Bug修复</h3> 
<ul> 
 <li>尝试从未知数据源类型派生数据源时，DataSourceBuilder 抛出 UnsupportedDataSourcePropertyException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F27453" target="_blank">#27453</a></li> 
 <li>DatabaseInitializerDetector 和 DependsOnDatabaseInitializationDetector 实现可能会使用错误的 ClassLoader 进行实例化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27422" target="_blank">#27422</a></li> 
 <li>YamlPropertySourceLoader 可能不会使用正确的 ClassLoader 来检查 SnakeYAML 是否存在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27419" target="_blank">#27419</a></li> 
 <li>将 Gson 设置为首选映射器会破坏返回 JSON 字符串的控制器方法<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27361" target="_blank">#27361</a></li> 
 <li>Prometheus 的 Pushgateway 的依赖管理不完整<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27349" target="_blank">#27349</a></li> 
 <li>使用 spring.config.import=configtree:xxxx 时从 /actuator/configprops 端点抛出异常<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27346" target="_blank">#27346</a></li> 
 <li>图层配置 XSD 不可用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27321" target="_blank">#27321</a></li> 
 <li>当集群状态为失败时，Redis 健康指标报告 Redis 已启动<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27304" target="_blank">#27304</a></li> 
 <li>使用 Spring Batch 和 JDBC 时应用程序无法启动，并且启用了延迟初始化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27221" target="_blank">#27221</a></li> 
 <li>启用延迟初始化后，Spring Session JDBC 不起作用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27220" target="_blank">#27220</a></li> 
 <li>AbstractDataSourceInitializers 未被检测为数据库初始值设定项<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F27215" target="_blank">#27215</a></li> 
 <li>如果不存在，带有模式的可选文件搜索位置会引发异常<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27211" target="_blank">#27211</a></li> 
 <li>工作目录中名为“config”的文件导致 IllegalStateException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27210" target="_blank">#27210</a></li> 
 <li>使用 Devtools 的 Live Reload 不再连接<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27205" target="_blank">#27205</a></li> 
 <li>使用 Devtools 实时重新加载不再连接<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27204" target="_blank">#27204</a></li> 
 <li>DurationStyle.SIMPLE.print 不能与 ChronoUnit.MICROS 一起正常工作<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27154" target="_blank">#27154</a></li> 
 <li>从 2.5.1 开始，当一个 SpringLiquibase bean 被配置为依赖另一个时会创建一个循环引用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27131" target="_blank">#27131</a></li> 
 <li>配置属性元数据具有错误的 spring.netty.leak-detection 默认值<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27104" target="_blank">#27104</a></li> 
 <li>“无法确定数据库的类型，因为 ConnectionFactory 不支持选项”错误消息没有提供足够的详细信息<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F26977" target="_blank">#26977</a></li> 
 <li><code>@SpyBean</code>用于监视 Spring Data Repository 时不起作用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F7033" target="_blank">#7033</a></li> 
</ul> 
<h3>2.3 <span style="color:#24292e"><span style="background-color:#ffffff">文档</span></span></h3> 
<ul> 
 <li>修复对 cloud.adoc 中配置属性的引用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F27357" target="_blank">#27357</a></li> 
 <li>记录自动配置的 Jetty 指标<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27301" target="_blank">#27301</a></li> 
 <li>文档说明 hatoas starter 是 spring MVC 特定的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27139" target="_blank">#27139</a></li> 
 <li>改进<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F27137" target="_blank">#27137 的</a>javadoc<code>@DefaultValue</code></li> 
 <li>修复包含问号的锚重写<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F27107" target="_blank">#27107</a></li> 
 <li>删除 spring.datasource.tomcat.max-active 的不必要单元<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F27103" target="_blank">#27103</a></li> 
 <li>修复部分标题中的错字<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F27102" target="_blank">#27102</a></li> 
</ul> 
<h3>2.4 <span style="color:#24292e"><span style="background-color:#ffffff"> 依赖升级</span></span></h3> 
<ul> 
 <li>升级至AppEngine SDK 1.9.90 #27384</li> 
 <li>升级至AspectJ 1.9.7 #27194</li> 
 <li>升级至Caffeine 2.9.2 #27195</li> 
 <li>升级至DB2 JDBC 11.5.6.0 #27196</li> 
 <li>升级至Dropwizard Metrics 4.1.25 #27385</li> 
 <li>升级至Infinispan 12.1.7.Final #27386</li> 
 <li>升级至Jackson Bom 2.12.4 #27198</li> 
 <li>升级至Jedis 3.6.3 #27448</li> 
 <li>升级至Jetty 9.4.43.v20210629 #27199</li> 
 <li>升级至Jetty Reactive HTTPClient 1.1.10 #27388</li> 
 <li>升级至Johnzon 1.2.14 #27200</li> 
 <li>升级至jOOQ 3.14.13 #27389</li> 
 <li>升级至Kotlin 1.5.21 #27316</li> 
 <li>升级至Kotlin Coroutines 1.5.1 #27317</li> 
 <li>升级至Lettuce 6.1.4.RELEASE #27341</li> 
 <li>升级至Logback 1.2.4 #27449</li> 
 <li>升级至Micrometer 1.7.2 #27342</li> 
 <li>升级至MySQL 8.0.26 #27450</li> 
 <li>升级至Netty 4.1.66.Final #27390</li> 
 <li>升级至Postgresql 42.2.23 #27202</li> 
 <li>升级至Reactor 2020.0.9 #27162</li> 
 <li>升级至SLF4J 1.7.32 #27451</li> 
 <li>升级至Spring AMQP 2.3.10 #27392</li> 
 <li>升级至Spring Data 2021.0.3 #27164</li> 
 <li>升级至Spring Framework 5.3.9 #27163</li> 
 <li>升级至Spring HATEOAS 1.3.3 #27184</li> 
 <li>升级至Spring Integration 5.5.2 #27166</li> 
 <li>升级至Spring Kafka 2.7.4 #27165</li> 
 <li>升级至Tomcat 9.0.50 #27203</li> 
 <li>升级至Undertow 2.2.9.Final #27452</li> 
</ul> 
<h2 style="text-align:left">三、同步更新</h2> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">MateCloud是一款基于Spring Cloud Alibaba的微服务架构。目前已经整合Spring Cloud Gateway、Spring Security Oauth2、Feign、Dubbo、JetCache、RocketMQ等服务套件，为您的开发保驾护航！</span>现已更新至Spring Boot 2.5.3版本。详见dev分支。</p> 
<p style="text-align:left"><a href="https://gitee.com/matevip/matecloud">https://gitee.com/matevip/matecloud</a></p>
                                        </div>
                                      
</div>
            