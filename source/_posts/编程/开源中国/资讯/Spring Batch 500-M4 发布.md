
---
title: 'Spring Batch 5.0.0-M4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4173'
author: 开源中国
comments: false
date: Sat, 23 Jul 2022 07:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4173'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Spring Batch 5.0.0-M4<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F07%2F20%2Fspring-batch-5-0-0-m4-available-now" target="_blank"><span> </span>已发布</a>，新版本在支持 Java Records 方面进行了部分改进，以及其他功能增强、错误修复、依赖升级和文档更新。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Spring Batch 是一个轻量级且功能全面的批处理框架，使用 Spring 和 Java 编写离线和批处理应用程序，旨在为开发对企业系统日常运行至关重要的批处理应用程序提供支持。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>改进对 Java Records 的支持</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">v4.3 是最早支持 Java Records 的版本，不过这种支持能力有限，原因是 v4 系列基于 Java 8 开发。在 Java 8 中，Records 尚未进入预览阶段，最初的支持是基于反射技术来创建 Java Records 并使用数据进行填充，而无需访问<code>java.lang.Record</code>，该 API 最终在 Java 16 才确定。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">现在 v5 基于 Java 17 开发，开发者通过在框架的不同部分利用<code>java.lang.Record</code>API 来改进 Spring Batch 中的 Records 支持。例如，<code>FlatFileItemReaderBuilder</code>现在能够检测项目类型是 Records 还是常规类，并相应地配置相应的<code>FieldSetMapper</code>实现（<code>RecordFieldSetMapper</code>用于Records，<code>BeanWrapperFieldSetMapper</code>用于常规类）。同样的功能也已经在 FlatFileItemWriterBuilder 中实现，以便根据项目类型配置<code>RecordFieldExtractor</code><span style="color:#333333">或<span> </span></span><code>BeanWrapperFieldExtractor</code><span style="color:#333333">。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>修复错误</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本修复了一些重要错误，并会破坏兼容性。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>如果 classpath 中没有<code>spring-tx</code>，则无法读取 XML 数据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Fissues%2F4132" target="_blank">#4132</a></li> 
 <li>使用链式<code>StepBuilder</code>时会丢失事务属性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Fissues%2F3686" target="_blank">#3686</a></li> 
 <li>添加<code>StepExecutionListener</code><span style="color:#191e1e">后，</span>无法正确注册<code>ItemReadListener</code><span style="color:#191e1e"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Fissues%2F773" target="_blank">#773</a></li> 
 <li><code>无法继承final class com.sun.proxy.$Proxy202</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Fissues%2F793" target="_blank">#793</a></li> 
 <li><code>StepBuilderFactory</code>仅支持 Listener Annotations，不支持 Listener Interfaces <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Fissues%2F1098" target="_blank">#1098</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>升级依赖</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Upgrade to Spring Framework 6.0.0-M5</li> 
 <li>Upgrade to Spring Data 2022.0.0-M5</li> 
 <li>Upgrade to Spring Integration 6.0.0-M4</li> 
 <li>Upgrade to Spring AMQP 3.0.0-M3</li> 
 <li>Upgrade to Spring for Apache Kafka 3.0.0-M5</li> 
 <li>Upgrade to Micrometer 1.10.0-M3</li> 
 <li>Upgrade to Hibernate 6.1.1.Final</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Freleases%2Ftag%2F5.0.0-M4" target="_blank">Release Notes</a> |<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F07%2F20%2Fspring-batch-5-0-0-m4-available-now" target="_blank">发布公告</a></p>
                                        </div>
                                      
</div>
            