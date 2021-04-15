
---
title: 'Spring for Apache Kafka 2.7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3245'
author: 开源中国
comments: false
date: Thu, 15 Apr 2021 06:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3245'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring for Apache Kafka 2.7.0 已经发布，Spring for Apache Kafka 将 Spring 核心概念应用于基于 Kafka 的消息传递解决方案的开发，它提供了一个“模板”作为发送消息的高级抽象。它还通过 @KafkaListener 注解和“侦听器容器(listener container)”为消息驱动的 POJO 提供支持。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>使用 topic 时非阻塞延迟重试。当严格的排序并不重要时，可以将失败的交付发送到另一个 topic 中，以便以后消费。可以配置一系列这样的重试 topic，并增加延迟。</li> 
 <li>侦听器容器更改。onlyLogRecordMetadata 容器属性现在默认为 true，并且有了一个新的容器属性 stopImmediate。</li> 
 <li>@KafkaListener 更改。现在，用户可以验证 @KafkaHandler 方法的有效负载参数（类级侦听器），在 MessagingMessageConverter 和 BatchMessagingMessageConverter 上设置 rawRecordHeader 属性，这会将原始的 ConsumerRecord 添加到转换后的Message <？>中。</li> 
 <li>DeadLetterPublishing 恢复更改。现在，如果键和值的反序列化都失败了，原始值会被发布到DLT。此外，recoverer 在发布到目标解析器之前，会验证目标解析器选择的分区是否真的存在。</li> 
 <li>ReplyingKafkaTemplate 更改。现在有了检查回复的机制，并增加了对发送和接收 spring-messaging Message<?> 的支持。</li> 
 <li>Kafka 流更改。默认情况下，StreamsBuilderFactoryBean 现在被配置为不清理本地状态。</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F04%2F14%2Fspring-for-apache-kafka-2-7-0-available" target="_blank">更新公告</a>。</p> 
<p> </p> 
<ul> 
</ul>
                                        </div>
                                      
</div>
            