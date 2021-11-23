
---
title: 'Spring Boot 2.5.7 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b42e12328d8f262e5619d05bae30d32e400.png'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 15:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b42e12328d8f262e5619d05bae30d32e400.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:left">一、发布说明</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">11月18日官方发布了Spring Boot 2.5.7版本，此版本包括35个错误修复、文档改进和依赖项升级。</p> 
<p><img height="814" src="https://oscimg.oschina.net/oscnet/up-b42e12328d8f262e5619d05bae30d32e400.png" width="1548" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">二、更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.1 bug修复</h3> 
<ul> 
 <li>JSTL 的依赖管理已过时#28659</li> 
 <li>JUnit 注释可能会阻止缓存测试上下文#28565</li> 
 <li>使用 FilteredClassLoader 避免重复的 AOP 代理类定义#28531</li> 
 <li>使用添加的配置文件@ActiveProfiles具有不同的优先级#28530</li> 
 <li>Logback 应该默认为 JVM 的默认字符集而不是 ASCII #28486</li> 
 <li>当父上下文具有方法验证配置时，它不会在其子上下文中自动配置#28479</li> 
 <li>除非明确接受 application/openmetrics-text，否则 Prometheus 执行器端点应生成文本/纯文本响应#28446</li> 
</ul> 
<h3>2.2 文档</h3> 
<ul> 
 <li>修复“配置两个数据源”示例#28712</li> 
 <li>GraphQL Spring Boot 启动程序的更新 URL #28683</li> 
 <li>修复@deprecated并@see在org.springframework.boot.loader.archive.Archive的Javadoc ＃28680</li> 
 <li>参考文档中的配置示例有错误的 yaml 格式#28671</li> 
 <li>修复参考文档中的 yaml 示例格式#28670</li> 
 <li>修复“Ant-style path matching”中的错字#28549</li> 
 <li>更改属性“logging.logback.rollingpolicy.max-history”的描述以匹配 Logback 文档#28466</li> 
 <li>改进有关使用嵌入式 ActiveMQ 代理的文档#28434</li> 
 <li>不要在 javadoc 或错误消息中使用Markdown语法#28424</li> 
</ul> 
<h3>2.3 依赖升级</h3> 
<ul> 
 <li>升级至 AppEngine SDK 1.9.92 #28556</li> 
 <li>升级至 Gson 2.8.9 #28557</li> 
 <li>升级至 Hazelcast 4.1.6 #28558</li> 
 <li>升级至 Johnzon 1.2.15 #28559</li> 
 <li>升级至 Kafka 2.7.2 #28694</li> 
 <li>升级至 Logback 1.2.7 #28695</li> 
 <li>升级至 Micrometer 1.7.6 #28511</li> 
 <li>升级至 Neo4j Java Driver 4.2.8 #28717</li> 
 <li>升级至 Netty 4.1.70.Final #28560</li> 
 <li>升级至 Netty tcNative 2.0.46.Final #28718</li> 
 <li>升级至 Reactor 2020.0.13 #28509</li> 
 <li>升级至 Spring AMQP 2.3.12 #28600</li> 
 <li>升级至 Spring Batch 4.3.4 #28250</li> 
 <li>升级至 Spring Data 2021.0.7 #28512</li> 
 <li>升级至 Spring Framework 5.3.13 #28510</li> 
 <li>升级至 Spring HATEOAS 1.3.6 #28609</li> 
 <li>升级至 Spring Integration 5.5.6 #28513</li> 
 <li>升级至 Spring Kafka 2.7.9 #28539</li> 
 <li>升级至 Tomcat 9.0.55 #28696</li> 
</ul>
                                        </div>
                                      
</div>
            