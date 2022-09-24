
---
title: 'Spring Boot 2.7.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9120'
author: 开源中国
comments: false
date: Sat, 24 Sep 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9120'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Boot 2.7.4 现已发布，具体更新内容如下：</p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的功能</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>将 NINETEEN 添加到 JavaVersion 枚举 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32260" target="_blank">#32260</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>H2 控制台自动配置中的数据源日志记录导致 Hikari 的线程具有错误的线程上下文类加载器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32406" target="_blank">#32406</a></li> 
 <li>Hazelcast 自动配置可以识别 hazelcast.xml 和 hazelcast.yaml 文件，但不能识别 hazelcast.yml <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32247" target="_blank">#32247</a></li> 
 <li>PeriodStyle.ISO8601 检测不支持小写输入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32244" target="_blank">#32244</a></li> 
 <li>DurationStyle.ISO8601 检测不支持小写输入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32231" target="_blank">#32231</a></li> 
 <li>SnakeYaml 1.31 中未正确处理 YAML 时间戳 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32229" target="_blank">#32229</a></li> 
 <li>Hazelcast shutdown logs 不是开箱即用的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F32184" target="_blank">#32184</a></li> 
 <li>Netty 'spring.netty leak detection' 默认属性值始终应用于资源泄漏检测器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32145" target="_blank">#32145</a></li> 
 <li>在启用 SELinux 的 Fedora 上使用 podman 构建镜像时出现错误“/var/run/docker.sock:connect:permission denied” <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32000" target="_blank">#32000</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>文档</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>对 JDK 19 的文档支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32402" target="_blank">#32402</a></li> 
 <li>阐明从中读取外部应用程序属性的 config 子目录的文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32291" target="_blank">#32291</a></li> 
 <li>阐明有关禁用 Web 客户端 request metrics 的文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32198" target="_blank">#32198 </a></li> 
 <li>constructor 绑定缺少 Kotlin 示例 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32177" target="_blank">#32177</a></li> 
 <li>从自动配置文档中删除过期链接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32174" target="_blank">#32174</a></li> 
 <li>改进有关在<code>@Bean</code>方法上使用的 <code>@ConditionalOnClass</code>javadoc <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32167" target="_blank">#32167</a></li> 
 <li>用于跨模块查找 GraphQL 模式的 Document classpath* location <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F31772" target="_blank">#31772</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>依赖升级</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>升级到字节好友 1.12.17 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32454" target="_blank"># 32454</a></li> 
 <li>升级到 Couchbase <span style="background-color:#ffffff; color:#24292f">Client</span> 3.3.4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32315" target="_blank">#32315</a></li> 
 <li>升级到 <span style="background-color:#ffffff; color:#24292f">Dependency Management Plugin</span> 1.0.14.RELEASE <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32459" target="_blank">#32459</a></li> 
 <li>升级到 Dropwizard <span style="background-color:#ffffff; color:#24292f">Metrics</span> 4.2.12 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32316" target="_blank"># 32316</a></li> 
 <li>升级到 Ehcache3 3.10.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32317" target="_blank">#32317</a></li> 
 <li>升级到 Elasticsearch 7.17.6 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32318" target="_blank">#32318</a></li> 
 <li>升级到 <span style="background-color:#ffffff; color:#24292f">Embedded Mongo</span> 3.4.9 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32319" target="_blank">#32319</a></li> 
 <li>升级到 Groovy <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32443" target="_blank">3.0.13 #32443</a></li> 
 <li>升级到 Hibernate 5.6.11.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32320" target="_blank">#32320</a></li> 
 <li>升级到 Hibernate Validator 6.2.5.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32321" target="_blank">#32321</a></li> 
 <li>升级到 Infinispan 13.0.11.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32322" target="_blank"># 32322</a></li> 
 <li>升级到 Jackson Bom 2.13.4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32323" target="_blank">#32323</a></li> 
 <li>升级到 Janino 3.1.8 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32324" target="_blank">#32324</a></li> 
 <li>升级到 Jetty 9.4.49.v20220914 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32444" target="_blank">#32444</a></li> 
 <li>升级到 Johnzon 1.2.19 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32325" target="_blank">#32325</a></li> 
 <li>升级到 Kafka 3.1.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32326" target="_blank">#32326</a></li> 
 <li>升级到 MariaDB 3.0.8 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32445" target="_blank">#32445</a></li> 
 <li>升级到 <span style="background-color:#ffffff; color:#24292f">Micrometer</span> 1.9.4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32272" target="_blank">#32272</a></li> 
 <li>升级到 Netty 4.1.82.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32327" target="_blank">#32327</a></li> 
 <li>升级到 Postgresql 42.3.7 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32243" target="_blank">#32243</a></li> 
 <li>升级到 R2DBC Bom Borca-SR2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32328" target="_blank">#32328</a></li> 
 <li>升级到 Reactor 2020.0.23 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32273" target="_blank">#32273</a></li> 
 <li>升级到 RSocket 1.1.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32380" target="_blank">#32380</a></li> 
 <li>升级到 Spring AMQP 2.4.7 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32276" target="_blank">#32276</a></li> 
 <li>升级到 Spring Batch 4.3.7 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32278" target="_blank">#32278</a></li> 
 <li>升级到 Spring Data 2021.2.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32275" target="_blank">#32275</a></li> 
 <li>升级到 Spring Framework 5.3.23 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32274" target="_blank">#32274</a></li> 
 <li>升级到 Spring GraphQL 1.0.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32426" target="_blank">#32426</a></li> 
 <li>升级到 Spring HATEOAS 1.5.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32378" target="_blank">#32378</a></li> 
 <li>升级到 Spring Integration 5.5.15 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32453" target="_blank">#32453</a></li> 
 <li>升级到 Spring Kafka <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32277" target="_blank">2.8.9 #32277</a></li> 
 <li>升级到 UnboundID LDAPSDK 6.0.6 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F32329" target="_blank"># 32329</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.7.4" target="_blank">https://github.com/spring-projects/spring-boot/releases/tag/v2.7.4</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            