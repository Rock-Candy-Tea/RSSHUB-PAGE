
---
title: 'Apache Camel 3.13.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7092'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7092'
---

<div>   
<div class="content">
                                                                                            <p>Apache Camel 是一个开源的面向消息的中间件框架，它有一个基于规则的路由和调解引擎，提供了一个基于 Java 对象的企业集成模式的实现，使用应用编程接口来配置路由和调解规则。</p> 
<p>在面向服务的架构项目中，Camel 经常与 Apache ServiceMix、Apache ActiveMQ 和 Apache CXF 一起使用。</p> 
<p>Apache Camel 3.13.0 更新内容如下：</p> 
<h3>错误修复：</h3> 
<ul> 
 <li>CAMEL-17198：Camel Salesforce Maven 插件生成 "PicklistEnumConverter" 导入，但该类并不存在；</li> 
 <li>CAMEL-17167：Camel-AWS2-SQS: 消息属性最多可以有 10 个</li> 
 <li>CAMEL-17153：UnitOfWork 的 afterprocess 不能正常工作</li> 
 <li>camel-karaf - 添加 camel-cxf 时出错</li> 
 <li>CAMEL-17135：camel-debezium-mongodb-starter 不能从 application.properties 中获取值。</li> 
 <li>CAMEL-17124：HttpRestHeaderFilterStrategy 不能过滤 queryParameter headers</li> 
 <li>CAMEL-17114：camel-jslt 在 quarkus 开发模式下无法从 classpath 加载文件</li> 
 <li>CAMEL-17109：camel-azure 依赖性 bom 导致冲突的依赖被下载</li> 
 <li>CAMEL-17095：camel-resilience4j —— 同时使用 timeout 和 bulkhead 不起作用</li> 
 <li>CAMEL-17075：DatasonnetBuilder（和 SimpleBuilder）在 evaluate() 中进行初始化，这在负载下会导致问题</li> 
 <li>CAMEL-17074：camel-spring-main —— 来自 Spring XML 的 Camel 有自己的预配置，camel-main 不应该覆盖它</li> 
 <li>CAMEL-17068：FileLockClusterView 在 CIFS 中不工作</li> 
 <li>……</li> 
</ul> 
<h3>依赖项升级</h3> 
<ul> 
 <li>CAMEL-17164：camel-ssh - 升级到 SSHD 2.7.0 CAMEL-17123：升级至 Spring Boot 2.5.6</li> 
 <li>CAMEL-17098：升级至 CXF 3.4.5</li> 
 <li>CAMEL-17089：camel-grpc - 升级到 1.41.0</li> 
 <li>CAMEL-17082：camel-kubernetes - 升级到5.9.x</li> 
 <li>CAMEL-17071：camel-openapi-java - 升级到 apicurio 1.1.x</li> 
 <li>CAMEL-17053：升级至 Jandex 2.4.1</li> 
 <li>CAMEL-17047：camel-karaf - 将 aries 代理版本升级到 1.1.11 以支持 JDK11+</li> 
 <li>CAMEL-17044：camel-debezium - 升级到 1.7 版本</li> 
 <li>CAMEL-17000：升级到 junit 5.8.x</li> 
</ul> 
<h3>新功能</h3> 
<ul> 
 <li>CAMEL-17150：camel-yaml-dsl - 应该能够加载 camel-k yaml 文件</li> 
 <li>CAMEL-17149：camel-main - 绑定 Bean 应允许在构造器参数中引用其他 Bean</li> 
 <li>CAMEL-17096：camel-kafka - 添加异步提交支持</li> 
 <li>CAMEL-17072：camel-core - 允许在待机模式下启用追踪功能</li> 
 <li>CAMEL-17061：camel-openapi-java - 在 Spring Boot 上运行时支持 springdoc</li> 
 <li>CAMEL-17041：允许为实体类型类名配置别名</li> 
 <li>CAMEL-16975：组件应该能够提供自定义的健康检查</li> 
 <li>CAMEL-16612：camel-kamelet - 使用 jbang 运行</li> 
 <li>CAMEL-15714：camel-karaf - 增加 camel-aws2-s3 功能</li> 
 <li>……</li> 
</ul> 
<h3>SUB-TASK</h3> 
<ul> 
 <li>CAMEL-16952：改进关于使用 camel-spring-boot 测试的文档</li> 
</ul> 
<h3>测试</h3> 
<ul> 
 <li>CAMEL-17163：camel-ftp - 升级到 SSHD 2.7.x</li> 
 <li>CAMEL-17155：camel-openapi-java - 并行运行测试以加快测试速度</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Freleases%2Frelease-3.13.0%2F" target="_blank">https://camel.apache.org/releases/release-3.13.0/</a></p>
                                        </div>
                                      
</div>
            