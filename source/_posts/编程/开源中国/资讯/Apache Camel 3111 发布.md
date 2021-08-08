
---
title: 'Apache Camel 3.11.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6735'
author: 开源中国
comments: false
date: Sun, 08 Aug 2021 06:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6735'
---

<div>   
<div class="content">
                                                                                            <p>Apache Camel 3.11.1 现已发布。这是一个基于已知<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Fcomponents%2Flatest%2Feips%2Fenterprise-integration-patterns.html" target="_blank">企业集成模式</a>的开源<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Fmanual%2Flatest%2Ffaq%2Fwhat-is-camel.html" target="_blank">集成框架</a>，支持 50 多种<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Fcomponents%2Flatest%2Fdataformats%2F" target="_blank">数据格式</a>，允许开发者集成产生和消费数据的系统。本次更新是一个 LTS 版本，包含 33 个新特性、改进和错误修复。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>camel-jpa：不丢失头文件</li> 
 <li>camel-core：OGNL "properties" 变量应使用 "allProperties"</li> 
 <li>camel-core：Kamelet 在 #class local bean 中增加对工厂方法的支持</li> 
 <li>在 platform-http-vertx 中改进对 Vert.x Buffer 有效载荷的处理</li> 
 <li>当并发的 FILE 组件消费者试图在 JdbcMessageIdRepository 中获得锁时，不发出异常</li> 
 <li>camel-bean：带有 Process bean 的 BeanProcessor 不能处理 Throwable</li> 
 <li>camel-core：路由转储没有打印正确的路由与 kamelet eip</li> 
 <li>使用 Avro 键的 OpenTracing 导致警告</li> 
 <li>无法从设置了 deliveryMode 的 sjms2 端点消费信息</li> 
 <li>camel-kafka：在同一个应用程序中使用两个 kafka 连接的问题</li> 
 <li>AWS2 S3 文档包含对过时的 AWS 1 API 的引用</li> 
 <li>使用 try-with-resources 和 MainConfigurationProperties 时出现 NullPointerException</li> 
 <li>camel-core：以随机顺序分割/聚合并行处理的聚合体</li> 
 <li>camel-cxf：消息计数为-1的问题</li> 
 <li>camel-file：最小长度文件的读锁失败</li> 
 <li>camel-core：循环处理器中的竞争条件</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202108.mbox%2F%253CCADL1oAoK1jKwyoTQDhb0WxS9diFL8HvevLMWpPZ4RRhPFBmTfg%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            