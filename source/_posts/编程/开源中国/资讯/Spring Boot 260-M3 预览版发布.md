
---
title: 'Spring Boot 2.6.0-M3 预览版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-06943c299180d5fb179537b0c78382bba18.png'
author: 开源中国
comments: false
date: Sat, 25 Sep 2021 08:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-06943c299180d5fb179537b0c78382bba18.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">一、发布说明</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">9月24日官方发布了Spring Boot 2.6.0-M3预览版本，可以从如下地址获取：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo.spring.io%2Fui%2Fnative%2Fmilestone" target="_blank">https://repo.spring.io/ui/native/milestone</a>。</p> 
<p><img height="408" src="https://oscimg.oschina.net/oscnet/up-06943c299180d5fb179537b0c78382bba18.png" width="1594" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left">1.1 此版本亮点</h3> 
<ul> 
 <li>在<code>PathPattern</code>基于路径匹配策略现在默认用于Spring MVC应用。</li> 
 <li>不同客户端实现的 Elasticsearch 属性已得到整合和合理化。</li> 
 <li>清理规则现在是可插入的，并且可以基于支持<code>PropertySource</code>。</li> 
 <li><code>PollerMetadata</code>现在提供了Spring Integration属性。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">二、更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.1 新特性</h3> 
<ul> 
 <li>针对已配置多个互斥配置属性的情况，提供特定的异常和故障分析#28121</li> 
 <li>在“spring.boot.application.ready”下记录准备时间，而不是“spring.boot.application.running”下记录准备时间#28080</li> 
 <li>在 bootBuildImage 任务中公开 imageName 的默认值#28040</li> 
 <li>允许用户贡献一个 RedisStandaloneConfiguration bean #28028</li> 
 <li>添加 Spring Integration 默认轮询器自动配置#27992</li> 
 <li>自动配置 Kafka CommonErrorHandler #27927</li> 
 <li>添加启动时间指标#27878</li> 
 <li>自动配置 JVM 堆压力指标#27868</li> 
 <li>自动配置 Micrometer 的 Lettuce 延迟指标#27865</li> 
 <li>为应用自定义清理规则提供可插入的抽象#27840</li> 
 <li>删除具有旧 groupId 的 Oracle 驱动程序的依赖项管理#27827</li> 
 <li>在#27823 中包含@WebMvcTest WebMvcRegistrations</li> 
 <li>提供用于设置自动配置的磁盘空间指标使用的路径的配置属性#27660</li> 
 <li>在可重现的 Maven 构建中对 BOOT-INF/lib 的内容进行排序#27436</li> 
 <li>为 Elasticsearch 路径前缀提供配置属性#25010</li> 
 <li>切换默认 spring.mvc.pathmatch.matching-strategy #24805</li> 
 <li>为 MVC 执行器启用基于 PathPattern 的匹配#24645</li> 
 <li>整合常见的 Elasticsearch 配置属性#23106</li> 
 <li>记录对健康指标的失败调用#22632</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.2 Bug修复</h3> 
<ul> 
 <li>默认情况下，执行器端点不会清理 SPRING_APPLICATION_JSON #28082</li> 
 <li>当过滤器抛出 NestedServletException 以外的异常时，Web MVC 指标可能具有错误的状态#28070</li> 
 <li>在独立 Tomcat 中部署 War 会导致内存泄漏（元空间）#28034</li> 
 <li>当存档文件名包含 URL 中保留的字符时，嵌入式 Undertow 抛出 MalformedURLException #28033</li> 
 <li>并发镜像构建导致删除构建器镜像时出错#27994</li> 
 <li>运行大于 4GB 的 Zip64 jar 文件时出现 IndexOutOfBoundsException #27901</li> 
 <li>在 Windows 上未正确检测到 Azure 应用服务#27879</li> 
 <li>当路由数据源的目标路由键为空时，RoutingDataSourceHealthContributor 中出现 NullPointerException #27800</li> 
 <li>@MockBean结合@Repeat“字段不能有现有值”错误的结果#27799</li> 
</ul> 
<h3>2.3 文档</h3> 
<ul> 
 <li>Java 17 的文档支持#28099</li> 
 <li>文档描述使用 AspectJ weaving 时 devtools 重启不工作#28084</li> 
 <li>spring.data.elasticsearch.client.reactive.endpoints 的默认值没有记录 #28073</li> 
 <li>从文档中展开英文缩写 #28064</li> 
 <li>修复文档中的一些拼写错误#27968</li> 
 <li>澄清 Selenium 自动配置需要 HtmlUnit #27944</li> 
 <li>波兰语 javadoc 评论#27925</li> 
 <li>更新spring.redis.jedis.pool.enabled 的文档以注意在 Sentinel 模式下隐式启用池化#27891</li> 
 <li>spring-boot-starter-parent 配置Java编译使用-parameters的文档#27886</li> 
 <li>修复不一致的开发工具文档#27877</li> 
 <li>修复 javadoc 中的错字#27874</li> 
 <li>记录如何使用 WebTestClient 参数化 REST 文档的输出目录#27804</li> 
 <li>仅从参考文档的每种格式中链接到两种替代格式#27737</li> 
 <li>将参考文档中的弹簧靴功能拆分为更小的部分#27132</li> 
</ul> 
<h3>2.4 依赖升级</h3> 
<ul> 
 <li>升级至 ActiveMQ 5.16.3 #27997</li> 
 <li>升级至 AppEngine SDK 1.9.91 #27998</li> 
 <li>升级至 AssertJ 3.21.0 #28090</li> 
 <li>升级至 Byte Buddy 1.11.18 #28110</li> 
 <li>升级至 Cassandra Driver 4.13.0 #28000</li> 
 <li>升级至 Commons Pool2 2.11.1 #28001</li> 
 <li>升级至 Couchbase Client 3.2.1 #28002</li> 
 <li>升级至 Ehcache3 3.9.6 #28003</li> 
 <li>升级至 Elasticsearch 7.14.1 #28004</li> 
 <li>升级至 Flyway 7.15.0 #28049</li> 
 <li>升级至 Glassfish EL 3.0.4 #28005</li> 
 <li>升级至 Groovy 3.0.9 #28006</li> 
 <li>升级至 Gson 2.8.8 #28007</li> 
 <li>升级至 Hibernate 5.5.7.Final #28008</li> 
 <li>升级至 HtmlUnit 2.53.0 #28092</li> 
 <li>升级至 InfluxDB Java 2.22 #28050</li> 
 <li>升级至 Jackson Bom 2.12.5 #28009</li> 
 <li>升级至 Jedis 3.7.0 #28010</li> 
 <li>升级至 Jersey 2.35 #28051</li> 
 <li>升级至 Jetty EL 9.0.52 #28011</li> 
 <li>升级至 Jolokia 1.7.1 #28093</li> 
 <li>升级至 jOOQ 3.14.15 #28094</li> 
 <li>升级至 JUnit Jupiter 5.8.1 #28052</li> 
 <li>升级至 Kafka 2.8.1 #28095</li> 
 <li>升级至 Kotlin 1.5.31 #28096</li> 
 <li>升级至 Kotlin Coroutines 1.5.2 #28014</li> 
 <li>升级至 Lettuce 6.1.5.RELEASE #28043</li> 
 <li>升级至 Logback 1.2.6 #28015</li> 
 <li>升级至 Maven Javadoc Plugin 3.3.1 #28016</li> 
 <li>升级至 Maven War Plugin 3.3.2 #28017</li> 
 <li>升级至 Micrometer 1.8.0-M3 #27931</li> 
 <li>升级至 Mockito 3.12.4 #28053</li> 
 <li>升级至 MongoDB 4.3.2 #28018</li> 
 <li>升级至 Neo4j Java Driver 4.3.4 #28019</li> 
 <li>升级至 Netty 4.1.68.Final #28020</li> 
 <li>升级至 Netty tcNative 2.0.43.Final #28021</li> 
 <li>升级至 Oracle Database 21.3.0.0 #28054</li> 
 <li>升级至 Prometheus Client 0.12.0 #28055</li> 
 <li>升级至 Rabbit AMQP Client 5.13.1 #28022</li> 
 <li>升级至 Rabbit Stream Client 0.4.0 #28056</li> 
 <li>升级至 Reactor 2020.0.11 #27929</li> 
 <li>升级至 Selenium HtmlUnit 2.53.0 #28097</li> 
 <li>升级至 SendGrid 4.7.5 #28111</li> 
 <li>升级至 Spring AMQP 2.4.0-M3 #27933</li> 
 <li>升级至 Spring Data 2021.1.0-M3 #27932</li> 
 <li>升级至 Spring Framework 5.3.10 #27930</li> 
 <li>升级至 Spring HATEOAS 1.4.0-M3 #27971</li> 
 <li>升级至 Spring Integration 5.5.4 #27950</li> 
 <li>升级至 Spring Kafka 2.8.0-M3 #27934</li> 
 <li>升级至 Spring Security 5.6.0-M3 #27935</li> 
 <li>升级至 SQLite JDBC 3.36.0.3 #28098</li> 
 <li>升级至 Thymeleaf Layout Dialect 3.0.0 #28057</li> 
 <li>升级至 Tomcat 9.0.53 #27964</li> 
 <li>升级至 WebJars Locator Core 0.48 #28058</li> 
</ul> 
<p>更多详细信息，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fwiki%2FSpring-Boot-2.6.0-M3-Release-Notes" onclick="s_objectID='apps_scodevmw : release notes wiki page : 74'" target="_blank">发行说明 wiki 页面</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.6.0-M3" onclick="s_objectID='apps_scodevmw : changelog : 75'" target="_blank">变更日志</a>。</p> 
<h2>三、下一版本发布预告</h2> 
<p>Spring Boot 2.6.0-RC1 将于 10 月 21 日发布，GA 将于 11 月 18 日发布。</p>
                                        </div>
                                      
</div>
            