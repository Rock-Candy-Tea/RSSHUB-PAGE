
---
title: 'Apache Camel 3.11.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5786'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 08:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5786'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Camel 3.11.0 现已发布。这是一个基于已知<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Fcomponents%2Flatest%2Feips%2Fenterprise-integration-patterns.html" target="_blank">企业集成模式</a>的开源<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Fmanual%2Flatest%2Ffaq%2Fwhat-is-camel.html" target="_blank">集成框架</a>，支持 50 多种<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Fcomponents%2Flatest%2Fdataformats%2F" target="_blank">数据格式</a>，允许开发者集成产生和消费数据的系统。本次更新是一个 LTS 版本，包含 101 个新特性、改进和错误修复。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>bug 修复 
  <ul> 
   <li>接收者列表不会等待接收者处理交换，并在处理路由时忽略聚合策略</li> 
   <li>修复了与 Netty TCP + Resilience4J circuit breaker 的冲突</li> 
   <li>修复了 camel-mongodb streamFilter 组件选项不被认可的问题</li> 
   <li>camel-rabbitmq 连接在 '声明' 过程出错时泄漏</li> 
   <li>camel-spring-boot 在运行时更改 Camel Log 的 LoggingLevel</li> 
   <li>如果使用 KafkaConfiguration，则不会设置 topic</li> 
   <li>LazyStartProducer 在多线程情况中可能导致 NullPointerException</li> 
   <li>当使用 Mockito mock 作为 camel-bean 组件的 bean 时，出现 AmbiguousMethodCallException</li> 
  </ul> </li> 
 <li>依赖项升级 
  <ul> 
   <li>camel-grpc 升级到 1.38</li> 
   <li>CXF 升级到 3.4.4</li> 
   <li>camel-yaml-dsl 升级到 snakeyaml 2.3</li> 
   <li>camel-spring-boot  升级到 Spring Boot 2.5.0</li> 
   <li>Camel-DJL 升级到 Deep Java Library 0.11.0</li> 
   <li>camel-opentelemetry 升级到 1.0.x</li> 
  </ul> </li> 
 <li>改进 
  <ul> 
   <li>camel-ftp：excludeExt/includeExt 没有得到正确的文件扩展名</li> 
   <li>Camel-avro-rpc 允许使用 SPI 更改 http 服务器实现</li> 
   <li>在向列表解压过程中收集 CSV 头信息时保留 CSV 头信息</li> 
   <li>按类型调用 bean 方法会导致创建新 bean 而不是使用注册表中的现有 bean</li> 
   <li>openapi 生成器现在允许指定端点</li> 
   <li>camel-mock 增加收到信息时的记录选项</li> 
   <li>将依赖 OSGi 的代码移至 camel-karaf</li> 
  </ul> </li> 
 <li>新特性 
  <ul> 
   <li>openapi 生成器：生成 YAML DSL</li> 
   <li>增加华为云 IAM 组件</li> 
   <li>增加华为云 FunctionGraph 组件</li> 
   <li>从 github 加载资源加载器</li> 
   <li>camel-core：为源时间戳添加通用 header</li> 
   <li>camel-smpp：将 JSMPP 的 pduProcessorDegree 和 queueCapacity 导出到 SmppConfiguration</li> 
   <li>camel-kamelet：使用 Kamelets 引导 Camel 的主类</li> 
   <li>为 Solr 创建一个 test-infra 模块</li> 
  </ul> </li> 
</ul> 
<p>更多详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Freleases%2Frelease-3.11.0%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            