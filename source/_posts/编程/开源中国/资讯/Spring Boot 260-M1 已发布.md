
---
title: 'Spring Boot 2.6.0-M1 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5a9b365ab99a7fa3713464cd5867a906cb0.png'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 10:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5a9b365ab99a7fa3713464cd5867a906cb0.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:left">一、发布说明</h2> 
<p><span style="background-color:#ffffff; color:#333333">于美国时间7月22日发布了Spring Boot 2.6.0-M1版本，</span>此版本包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.6.0-M1" onclick="s_objectID='apps_scodevmw : 120 bug fixes, documentation improvements, and dependency upgrades : 73'" target="_blank">120 个错误修复、文档改进和依赖项升级</a>。值得关注的新功能包括：</p> 
<ul> 
 <li>Spring Data Envers 的自动配置</li> 
 <li>更多指标支持（包括任务执行和调度导出以及对 Dynatrace v2 API 的支持）</li> 
 <li>自动配置的 Spring Web 服务服务器测试</li> 
 <li>改进了 Maven 插件启动目标的配置</li> 
</ul> 
<p><img height="852" src="https://oscimg.oschina.net/oscnet/up-5a9b365ab99a7fa3713464cd5867a906cb0.png" width="1572" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">二、版本发行说明</h2> 
<p>2.6.0-M1从2.5.0版本升级而来，这次Spring Boot 频繁更新，节奏很快。</p> 
<h3 style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">2.1 嵌入式 Mongo</span></span></h3> 
<div style="text-align:start">
 使用 mongo，现在必须要设置
 <code>spring.mongodb.embedded.version</code>属性。有助于确保嵌入式使用的 MongoDB 版本与生产中使用的 MongoDB 版本匹配一致。
</div> 
<div style="text-align:start"> 
 <h3 style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">2.2 移除 Nimbus DS 依赖管理</span></span></h3> 
 <p><span style="color:#24292e"><span style="background-color:#ffffff">删除了依赖com.nimbusds:oauth2-oidc-sdk和com.nimbusds:nimbus-jose-jwt。如果您正在使用 Spring Security，您需要手动引入。</span></span></p> 
 <h3><span style="color:#24292e"><span style="background-color:#ffffff">2.3 移除 </span></span><span style="background-color:rgba(27, 31, 35, 0.05); color:#24292e">hal-browser</span><span style="color:#24292e"><span style="background-color:#ffffff">依赖管理</span></span></h3> 
 <p><span style="color:#24292e"><span style="background-color:#ffffff">删除 </span></span><span style="background-color:rgba(27, 31, 35, 0.05); color:#24292e">org.webjars:hal-browser </span><span style="color:#24292e"><span style="background-color:#ffffff">依赖管理，如果你需要，则手动引入。</span></span></p> 
 <h3 style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">2.4 Maven 构建信息的默认时间</span></span></h3> 
 <div style="text-align:start">
  Maven 插件的构建信息可设置
  <code>project.build.outputTimestamp</code>属性值作为默认构建时间。如果未设置该属性，则使用之前的构建会话的开始时间。和以前一样，可以通过将时间
  <code>off</code>来设置完全禁用。
 </div> 
 <div style="text-align:start"> 
  <h3 style="text-align:start">2.5 Prometheus 版本属性</h3> 
  <p>控制 Prometheus 版本的属性已从 更改<code>prometheus-pushgateway.version</code>为<code>prometheus-client.version</code>。显示该属性管理 Prometheus 客户端中每个模块的版本，而不仅仅是 pushgateway。</p> 
  <h3 style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">2.6 Spring Boot 2.4 的弃用类删除</span></span></h3> 
  <p>在 Spring Boot 2.4 中弃用的类、方法和属性已在此版本中删除。请确保在升级之前您没有调用已弃用的方法。</p> 
  <h2 style="text-align:start"><span style="color:#24292e">三、 版本更新和需要注意事项</span></h2> 
  <h3><span style="color:#24292e"><span style="background-color:#ffffff">3.1 Spring Data Envers 的自动配置</span></span></h3> 
  <p>现在提供了 Spring Data Envers 的自动配置。要使用它，请添加依赖<code>org.springframework.data:spring-data-envers</code>并从<code>RevisionRepository</code>更新您的 JPA 存储库。</p> 
  <h3 style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">3.2 指标导出到 Dynatrace v2 API</span></span></h3> 
  <p>添加了对将指标导出到 Dynatrace v2 API 的支持。在主机上运行本地 OneAgent 时<code>io.micrometer:micrometer-registry-dynatrace</code>，只需要依赖即可。如果没有本地 OneAgent，则必须配置<code>management.metrics.export.dynatrace.uri</code>和<code>management.metrics.export.dynatrace.api-token</code>属性。可以使用<code>management.metrics.export.dynatrace.v2</code>属性配置特定于 v2 API 的其他设置。有关更多详细信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-boot%2Fdocs%2F2.6.0-SNAPSHOT%2Freference%2Fhtml%2F%2Factuator.html%23actuator.metrics.export.dynatrace" target="_blank">更新的参考文档</a>。</p> 
  <h3 style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">3.3 任务执行和调度指标</span></span></h3> 
  <p><span style="background-color:#ffffff; color:#24292e">Micrometer’s </span><code>DiskSpaceMetrics</code><span style="background-color:#ffffff; color:#24292e"> 是自动配置的。 </span><code>disk.free</code><span style="background-color:#ffffff; color:#24292e"> 和 </span><code>disk.total</code><span style="background-color:#ffffff; color:#24292e"> 提供了由当前的工作目录标识的分区指标。 要更改使用路径, 定义你自己的  </span><code>DiskSpaceMetrics</code><span style="background-color:#ffffff; color:#24292e"> 对象。</span></p> 
  <h3><span style="color:#24292e"><span style="background-color:#ffffff">3.4 Jetty 连接和 SSL 指标</span></span></h3> 
  <p><span style="background-color:#ffffff; color:#24292e">Micrometer的 </span><code>JettyConnectionMetrics</code><span style="background-color:#ffffff; color:#24292e"> 现在是自动配置的。 此外，当 </span><code>server.ssl.enabled</code><span style="background-color:#ffffff; color:#24292e"> 设置为 </span><code>true</code><span style="background-color:#ffffff; color:#24292e">, Micrometer的 </span><code>JettySslHandshakeMetrics</code><span style="background-color:#ffffff; color:#24292e"> 也同样会自动配置。</span></p> 
  <h3><span style="color:#24292e"><span style="background-color:#ffffff">3.5 Redis 连接池</span></span></h3> 
  <p>Redis（Jedis 和 Lettuce）现在将在<code>commons-pool2</code>类路径上自动启用连接池。如果需要，可设置<code>spring.redis.jedis.pool.enabled</code>或<code>spring.redis.lettuce.pool.enabled</code>为<code>false</code>禁用连接池。</p> 
  <h3 style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">3.6 改进了 Maven 插件启动目标的配置</span></span></h3> 
  <p>Maven 插件的<code>start</code>目标已经从命令行变得更加可配置。它的<code>wait</code>和<code>maxAttempts</code>属性可以分别使用<code>spring-boot.start.wait</code>和指定<code>spring-boot.start.maxAttempts</code>。</p> 
  <h3 style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">3.7 自动配置的 Spring Web 服务服务器测试</span></span></h3> 
  <p>引入<code>@WebServiceServerTest</code>可用于测试 Web 服务<code>@Endpoint</code>bean的新注释。注释创建一个包含<code>@Endpoint</code>bean的测试切片，并自动配置一个<code>MockWebServiceClient</code>可用于测试您的 Web 服务端点的bean。</p> 
  <h3><span style="color:#24292e"><span style="background-color:#ffffff">3.8 依赖升级</span></span></h3> 
  <p><span style="background-color:#ffffff; color:#24292e">Spring Boot 2.6迁移到几个Spring项目的新版本：</span></p> 
  <ul> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F07%2F19%2Fspring-security-5-6-0-m1-released" target="_blank">Spring Security 5.6.0-M1</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F07%2F16%2Fspring-data-2021-1-0-m1-released" target="_blank">Spring Data 2021.1.0-M1</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-hateoas%2Freleases%2Ftag%2F1.4.0-M1" target="_blank">Spring HATEOAS 1.4.0-M1</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-kafka%2Freleases%2Ftag%2Fv2.8.0-M1" target="_blank">Spring Kafka 2.8.0-M1</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-amqp%2Freleases%2Ftag%2Fv2.4.0-M1" target="_blank">Spring AMQP 2.4.0-M1</a></p> </li> 
  </ul> 
  <p>还更新了一些第三方依赖，典型的如下所示：</p> 
  <ul> 
   <li> <p>Micrometer 1.8.0-M1</p> </li> 
   <li> <p>QueryDSL 5.0.0.M1</p> </li> 
   <li> <p>SnakeYAML 1.29</p> </li> 
   <li> <p>Cassandra Driver 4.12.0</p> </li> 
   <li> <p>Kafka 2.8.0</p> </li> 
  </ul> 
  <p>更多说明请参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fwiki%2FSpring-Boot-2.6.0.M1-Release-Notes" target="_blank">https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.6.0.M1-Release-Notes</a></p> 
  <p>另：微服务项目<a href="https://gitee.com/matevip/matecloud">MateCloud</a>会在正式版本发布后引入。</p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            