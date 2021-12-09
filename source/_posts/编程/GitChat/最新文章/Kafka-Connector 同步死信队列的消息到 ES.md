
---
title: 'Kafka-Connector 同步死信队列的消息到 ES'
categories: 
 - 编程
 - GitChat
 - 最新文章
headimg: 'https://picsum.photos/400/300?random=2728'
author: GitChat
comments: false
date: Thu, 09 Dec 2021 14:08:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=2728'
---

<div>   
<p>基于上一篇 Chat 提到的消费端消息重试方案二使用 Kafka 自带的重试机制 + 死信队列，Kafka 消费端消费失败后经过三次重试仍然失败，这个时候会把消息存储到死信队列，架构师希望我们可以不在业务代码中消费死信队列，而是系统自...</p>  
</div>
            