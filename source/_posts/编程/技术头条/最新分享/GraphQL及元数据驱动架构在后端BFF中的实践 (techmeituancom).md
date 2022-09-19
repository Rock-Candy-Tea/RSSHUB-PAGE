
---
title: 'GraphQL及元数据驱动架构在后端BFF中的实践 (tech.meituan.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=3282'
author: 技术头条
comments: false
date: 2022-09-19 06:52:04
thumbnail: 'https://picsum.photos/400/300?random=3282'
---

<div>   
GraphQL是Facebook提出的一种数据查询语言，核心特性是数据聚合和按需索取，目前被广泛应用于前后端之间，解决客户端灵活使用数据问题。本文介绍的是GraphQL的另一种实践，我们将GraphQL下沉至后端BFF层之下，结合元数据技术，实现数据和加工逻辑的按需查询和执行。这样不仅解决了后端BFF层灵活使用数据的问题，这些字段加工逻辑还可以直接复用，大幅度提升了研发的效率。本文介绍的实践方案已经在美团部分业务场景中落地，并取得不错效果，希望这些经验能够对大家有帮助。
    
</div>
            