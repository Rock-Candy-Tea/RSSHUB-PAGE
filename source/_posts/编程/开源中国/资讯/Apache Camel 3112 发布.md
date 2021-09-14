
---
title: 'Apache Camel 3.11.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=386'
author: 开源中国
comments: false
date: Tue, 14 Sep 2021 06:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=386'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p><span style="background-color:#ffffff; color:#333333">Apache Camel 3.11.2 现已发布。这是一个基于已知</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Fcomponents%2Flatest%2Feips%2Fenterprise-integration-patterns.html" target="_blank">企业集成模式</a><span style="background-color:#ffffff; color:#333333">的开源</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Fmanual%2Flatest%2Ffaq%2Fwhat-is-camel.html" target="_blank">集成框架</a><span style="background-color:#ffffff; color:#333333">，支持 50 多种</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Fcomponents%2Flatest%2Fdataformats%2F" target="_blank">数据格式</a><span style="background-color:#ffffff; color:#333333">，允许开发者集成产生和消费数据的系统。本次更新是一个 LTS 版本，包含 22 改进和错误修复。</span></p> 
 <p><strong>主要更新内容</strong></p> 
 <ul> 
  <li>Bug 
   <ul> 
    <li>指定 OpenAPI 许可证和联系信息导致 NullPointerException</li> 
    <li>StringHelper.removeLeadingAndEndingQuotes() 可能导致 IndexOutOfBoundsException</li> 
    <li>KafkaSpanDecorator 有时会设置错误的 message_bus.destination 标签值</li> 
    <li>Dump route s不显示带有 endpointdsl 的 uri</li> 
    <li>Datasonnet 表达式在多播中调用的路由中首次运行会失败</li> 
    <li>确定 Spring ApplicationContext 是否为自我管理的 ApplicationContext 的更通用方法</li> 
    <li>即使没有指定 allowableValues，Camel Swagger API 响应字符串类型的消息头也会生成一个空枚举</li> 
    <li>camel-core - WireTap 在复制时应保留OUT消息</li> 
    <li>GrpcStreamingExchangeForwarder 中潜在的 NPE</li> 
    <li>使用面包屑可能导致 MailBinding 中的 ClassCastException</li> 
    <li>带有文件和选项 sendEmptyMessageWhenIdle 的 PollEnrich 不断发送空信息</li> 
    <li>Xtokenize 一旦检测到不匹配的命名空间，就不会再追踪到一个级别</li> 
    <li>breakOnFirstError 导致 camel-kafka 的线程和内存泄漏</li> 
    <li>camel-xslt：通过 URI 设置 resultHandlerFactory 被破坏了</li> 
    <li>camel-main - 引导后无法引用属性</li> 
    <li>camel-kubernetes - 在停止子组件消费者时，NULL 观察器会导致 NPE</li> 
    <li>camel-kafka - 文件描述符泄漏</li> 
    <li>REST DSL 中的 apiHost 选项被忽略了</li> 
   </ul> </li> 
  <li>依赖项升级 
   <ul> 
    <li>升级到 spring boot 2.5.4</li> 
    <li>将 Commons Compress 更新至 1.21</li> 
    <li>将 xchange 升级到 5.0.11</li> 
    <li>camel-karaf - 将 azure-blob-changefeed 包添加到 camel-azure-blob-storage 功能</li> 
   </ul> </li> 
  <li>改进 
   <ul> 
    <li>当 dumpRoutesAsXML 时，路线模板参数不被替换</li> 
   </ul> </li> 
 </ul> 
 <p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamel.apache.org%2Freleases%2Frelease-3.11.2%2F" target="_blank">更新公告</a>。</p> 
</div>
                                        </div>
                                      
</div>
            