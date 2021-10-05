
---
title: 'Apache Camel 3.12.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3059'
author: 开源中国
comments: false
date: Tue, 05 Oct 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3059'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Camel 是一个开源的面向消息的中间件框架，它有一个基于规则的路由和调解引擎，提供了一个基于 Java 对象的企业集成模式的实现，使用应用编程接口来配置路由和调解规则。</p> 
<p>在面向服务的架构项目中，Camel 经常与 Apache ServiceMix、Apache ActiveMQ 和 Apache CXF 一起使用。</p> 
<p>Apache Camel 3.12.0 更新内容如下：</p> 
<h3><strong>Bug 修复：</strong></h3> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-17008" target="_blank">CAMEL-17008</a></strong> okStatusCodeRange 不允许使用单一状态代码</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-17007" target="_blank">CAMEL-17007</a></strong> camel-aws2-lambda: GetAlias 不工作</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-17004" target="_blank">CAMEL-17004</a></strong> camel-servlet: 在将主体读入流式缓存时不应该关闭 HttpServletInputStream</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16990" target="_blank">CAMEL-16990</a></strong> camel-core: 流缓存检查引起的异常可能导致转换器问题</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16957" target="_blank">CAMEL-16957</a></strong> 在 CamelHttpPath 为空的情况下，NettyHttpHelper 将斜线追加到 URI 上</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16932" target="_blank">CAMEL-16932</a></strong> AS2 客户端端点的配置属性（AS2Configuration）被忽略了</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16927" target="_blank">CAMEL-16927</a></strong> camel-spring - 当涉及多个 camel 代理时，使用 Spring XML 和多个 Camel context 可能导致死锁</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16924" target="_blank">CAMEL-16924</a></strong> 升级到 Camel 3.11.0 后，使用聚合器时，无法写入 HttpServletResponse</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16923" target="_blank">CAMEL-16923</a></strong> 指定 OpenAPI 许可证和联系信息导致 NullPointerException</li> 
 <li>……</li> 
</ul> 
<h3>依赖升级：</h3> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-17002" target="_blank">CAMEL-17002</a></strong> 升级到 vertx 4.1.4</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16999" target="_blank">CAMEL-16999</a></strong> camel-spring-boot 更新至2.5.5</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16910" target="_blank">CAMEL-16910</a></strong> 更新 Commons Compress 至 1.21</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16890" target="_blank">CAMEL-16890</a></strong> 升级 kotlin 至 1.5.30</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16880" target="_blank">CAMEL-16880</a></strong> 升级 thrift 至 0.14.1</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16872" target="_blank">CAMEL-16872</a></strong> 升级 xchange 到 5.0.11</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-15650" target="_blank">CAMEL-15650</a></strong> 升级 apache spark 至 3.x</li> 
 <li>……</li> 
</ul> 
<h3><strong>新功能：</strong></h3> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16983" target="_blank">CAMEL-16983</a></strong> camel-spring-main - 当从传统的 Spring XML 文件迁移时，添加选项以允许多个 camelContext</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16833" target="_blank">CAMEL-16833</a></strong> camel-core - LambdaEndpointRouteBuilder</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16819" target="_blank">CAMEL-16819</a></strong> camel-core - 在错误处理程序中增加对可配置的 ExceptionPolicyStrategy 的支持</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16770" target="_blank">CAMEL-16770</a></strong> 增加对缓存 JDBC Idempotent Repository 的支持</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16768" target="_blank">CAMEL-16768</a></strong> camel-core - 允许使用 BiFunction 作为 AggregationStrategy</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16738" target="_blank">CAMEL-16738</a></strong> camel-websocket - 支持 websocket 子协议</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16589" target="_blank">CAMEL-16589</a></strong> [camel-azure-servicebus] 创建 Azure ServiceBus 组件</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FCAMEL-16379" target="_blank">CAMEL-16379</a></strong> 对 JDK 16 的支持</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Freleases%2Frelease-3.12.0%2F" target="_blank">https://camel.apache.org/releases/release-3.12.0/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            