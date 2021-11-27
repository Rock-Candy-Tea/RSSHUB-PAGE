
---
title: 'Apache Camel 3.11.4'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6295'
author: 开源中国
comments: false
date: Sat, 27 Nov 2021 00:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6295'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Camel 3.11.4 现已发布。Apache Camel 是一个开源的面向消息的中间件框架，它有一个基于规则的路由和调解引擎，提供了一个基于 Java 对象的企业集成模式的实现，使用应用编程接口来配置路由和调解规则。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在面向服务的架构项目中，Camel 经常与 Apache ServiceMix、Apache ActiveMQ 和 Apache CXF 一起使用。</p> 
<p><strong><span style="background-color:#ffffff; color:#182026">主要更新内容</span></strong></p> 
<ul> 
 <li>Bug 修复 
  <ul> 
   <li>camel-core - XPathBuilder 在使用 @XPath 注释时从不清除池并增加池导致内存泄漏</li> 
   <li>工作完成后，UnitOfWorkHelper 不会清除 UoW</li> 
   <li>Camel-AWS2-SQS：消息属性最多可以有 10 个</li> 
   <li>rest-dsl - clientRequestValidation 失败，然后操作产生的不仅仅是 xml 或 json</li> 
   <li>camel-karaf - 添加 camel-cxf 时出错</li> 
   <li>camel-debezium-mongodb-starter 不会从 application.properties 中提取值</li> 
   <li>抛出 JMX MBean InstanceAlreadyExistsException</li> 
   <li>HttpRestHeaderFilterStrategy 不过滤 queryParameter 标头</li> 
   <li>在 quarkus 开发模式下，camel-jslt 无法从类路径加载文件</li> 
   <li>忽略属性 Exchange.markRollbackOnlyLast</li> 
   <li>启用缓存时不正确的简单表达式行为</li> 
   <li>Datasonnet header 不能用于设置 bodyMediaType</li> 
   <li>authUsername 和 authPassword 参数未传递到底层端点</li> 
  </ul> </li> 
 <li>改进 
  <ul> 
   <li>camel-MLLP：值为 'false' 的选项 'logPhi' 不适用于异常记录</li> 
   <li>camel-aws - 处理完成时取消 "扩展可见性窗口" 会导致中断异常</li> 
   <li>camel-restdsl 插件没有实现参数 clientRequestValidation</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202111.mbox%2F%253CCADL1oAouxZrM9N0frO8r%3DAKdPDZiMZmAT00kr%2Bthk35723%3DU4g%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            