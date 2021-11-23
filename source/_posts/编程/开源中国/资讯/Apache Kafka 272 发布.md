
---
title: 'Apache Kafka 2.7.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4586'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 06:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4586'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Apache Kafka 2.7.2 现已发布。Apache Kafka 是一个分布式流平台，具有四个核心 API。借助这些 API，Kafka 可以用于以下两大类应用：建立实时流数据管道，可靠地进行数据传输，在系统或应用程序之间获取数据；构建实时流媒体应用程序，以改变系统或应用程序之间的数据或对数据流做出反应。</span></p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li> 改进 
  <ul> 
   <li>ConnectSchema.validateValue() 提供的错误信息应包括模式名称</li> 
   <li>升级 jetty-server 以修复 CVE-2021-34429</li> 
  </ul> </li> 
 <li>Bug 修复 
  <ul> 
   <li>尽管有 KAFKA-5051，SASL_SSL 仍然执行反向 DNS 查找</li> 
   <li>如果任务在启动期间失败，则失败任务计数 JMX 指标不会更新</li> 
   <li>Kafka 客户端在 Kerberos 重新登录期间抛出 AuthenticationException</li> 
   <li>FileStreamSourceTask 缓冲区可以无限增长</li> 
   <li>当 worker 失去领导权时，分布式 <span style="color:#000000">herder<span> </span></span><span style="background-color:#ffffff; color:#182026">tick </span>线程快速循环</li> 
   <li>当拥有密钥的追随者成为领导者时，永远不会分发新的会话密钥</li> 
   <li>StateDirectory 关闭时错误日志不正确</li> 
   <li>单个 Kerberos 登录失败会导致 Java 9 以后的所有连接失败</li> 
   <li>如果提议状态与实际状态相同，则 ISR 仍处于飞行状态</li> 
   <li>CVE-2021-28168: 将 <span style="color:#000000">jersey<span> </span></span>升级到 2.34 或 3.02</li> 
   <li>Connect 的验证 REST 端点使用不正确的超时</li> 
   <li>节点处于连接状态的 NetworkClient.close(node) 使 NetworkClient 无法使用</li> 
   <li>恢复 GlobalKTable 时的无限循环</li> 
   <li>在加入组之前并不总是调用 onJoinPrepare</li> 
   <li>当获取偏移量小于领导者起始偏移量时，无法正确处理 OffsetOutOfRange 以用于发散时期</li> 
   <li>使 transactionalIds 过期时消息太大错误</li> 
   <li>如果存在分歧时期，领导者不应更新追随者获取偏移量</li> 
   <li>消费者在断开连接后不应重置组状态</li> 
   <li>TopologyTestDriver 在使用 EOS-beta 配置时崩溃</li> 
   <li>请求/响应中长标记字符串的序列化抛出 BufferOverflowException</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202111.mbox%2F%253CCA%2BOCqnbp-qsFEvvA8s7T7oLGvWhwkCDjV4%2B-spuK%3DSStHjZAEg%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            