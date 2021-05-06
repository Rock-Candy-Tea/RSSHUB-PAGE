
---
title: '图解 Kafka'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/5bcd443589adcfedc93702827e37cbaa.jpg'
author: Dockone
comments: false
date: 2021-05-06 04:01:50
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/5bcd443589adcfedc93702827e37cbaa.jpg'
---

<div>   
<br>Kafka 是主流的消息流系统，其中的概念还是比较多的，下面通过图示的方式来梳理一下 Kafka 的核心概念，以便在我们的头脑中有一个清晰的认识。<br>
<h4>基础</h4>Kafka 是一套流处理系统，可以让后端服务轻松的相互沟通，是微服务架构中常用的组件。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/5bcd443589adcfedc93702827e37cbaa.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/5bcd443589adcfedc93702827e37cbaa.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>生产者消费者</h4>生产者服务 Producer 向 Kafka 发送消息，消费者服务 Consumer 监听 Kafka 接收消息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/52532eb2efd699729b7d4782f59ea321.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/52532eb2efd699729b7d4782f59ea321.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
一个服务可以同时为生产者和消费者。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/5d2e56b842e10928842b3b25e9e8e661.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/5d2e56b842e10928842b3b25e9e8e661.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Topics 主题</h4>Topic 是生产者发送消息的目标地址，是消费者的监听目标。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/2b9e6e644b31a4dff56ccf0216987638.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/2b9e6e644b31a4dff56ccf0216987638.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
一个服务可以监听、发送多个 Topics。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/529536bbfb9cabce483a1b4a10f7dbf5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/529536bbfb9cabce483a1b4a10f7dbf5.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Kafka 中有一个【consumer-group（消费者组）】的概念。<br>
<br>这是一组服务，扮演一个消费者。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/96b5f09bb916c41ee3ec3f8cce9403a5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/96b5f09bb916c41ee3ec3f8cce9403a5.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如果是消费者组接收消息，Kafka 会把一条消息路由到组中的某一个服务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/d9599e6bf9da22d77cb2bf3d3707563a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/d9599e6bf9da22d77cb2bf3d3707563a.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这样有助于消息的负载均衡，也方便扩展消费者。<br>
<br>Topic 扮演一个消息的队列。<br>
<br>首先，一条消息发送了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/90516789ee52d823027fb80484a69438.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/90516789ee52d823027fb80484a69438.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
然后，这条消息被记录和存储在这个队列中，不允许被修改。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/deacc3f8ec7366a54c354bfb2d7942a5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/deacc3f8ec7366a54c354bfb2d7942a5.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
接下来，消息会被发送给此 Topic 的消费者。<br>
<br>但是，这条消息并不会被删除，会继续保留在队列中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/8886c80d1156c8aa74e9448d6f79a640.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/8886c80d1156c8aa74e9448d6f79a640.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
继续发送消息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/7183cafbdd5a23738fc8b178a1191dbb.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/7183cafbdd5a23738fc8b178a1191dbb.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
像之前一样，这条消息会发送给消费者、不允许被改动、一直呆在队列中。<br>
<br>（消息在队列中能呆多久，可以修改 Kafka 的配置）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/9d79358874bcf288e520077e33694bc9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/9d79358874bcf288e520077e33694bc9.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/dcaee8f5d94cfad5b77aa66fc3bcb33c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/dcaee8f5d94cfad5b77aa66fc3bcb33c.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Partitions 分区</h4>上面 Topic 的描述中，把 Topic 看做了一个队列，实际上，一个 Topic 是由多个队列组成的，被称为【Partition（分区）】。<br>
<br>这样可以便于 Topic 的扩展。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/f007cdabf3f22cc9b60bb89240b2602a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/f007cdabf3f22cc9b60bb89240b2602a.jpg" class="img-polaroid" title="14.jpg" alt="14.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
生产者发送消息的时候，这条消息会被路由到此 Topic 中的某一个 Partition。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/2a17a00282104461723465117bd0b4cd.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/2a17a00282104461723465117bd0b4cd.jpg" class="img-polaroid" title="15.jpg" alt="15.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
消费者监听的是所有分区。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/23d515356bb188426ccb2d02cd4cb5ae.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/23d515356bb188426ccb2d02cd4cb5ae.jpg" class="img-polaroid" title="16.jpg" alt="16.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
生产者发送消息时，默认是面向 Topic 的，由 Topic 决定放在哪个 Partition，默认使用轮询策略。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/e245b0b6e4293829a4bcfa921da3e552.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/e245b0b6e4293829a4bcfa921da3e552.jpg" class="img-polaroid" title="17.jpg" alt="17.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
也可以配置 Topic，让同类型的消息都在同一个 Partition。<br>
<br>例如，处理用户消息，可以让某一个用户所有消息都在一个 Partition。<br>
<br>例如，用户1发送了3条消息：A、B、C，默认情况下，这3条消息是在不同的 Partition 中（如 P1、P2、P3）。<br>
<br>在配置之后，可以确保用户1的所有消息都发到同一个分区中（如 P1）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/82069b9fc0618fb3dc66b361dc6e5d05.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/82069b9fc0618fb3dc66b361dc6e5d05.jpg" class="img-polaroid" title="18.jpg" alt="18.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这个功能有什么用呢？<br>
<br>这是为了提供消息的【有序性】。<br>
<br>消息在不同的 Partition 是不能保证有序的，只有一个 Partition 内的消息是有序的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/a25b929c040010cec2bfb978af7987c6.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/a25b929c040010cec2bfb978af7987c6.jpg" class="img-polaroid" title="19.jpg" alt="19.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/703f1625a6404d0ba0aeb034910a713e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/703f1625a6404d0ba0aeb034910a713e.jpg" class="img-polaroid" title="20.jpg" alt="20.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>架构</h4>Kafka 是集群架构的，ZooKeeper是重要组件。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/d35db488f188d6db0ec5290ca9afd13b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/d35db488f188d6db0ec5290ca9afd13b.jpg" class="img-polaroid" title="21.jpg" alt="21.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
ZooKeeper 管理者所有的 Topic 和 Partition。<br>
<br>Topic 和 Partition 存储在 Node 物理节点中，ZooKeeper负责维护这些 Node。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/68ae0266f46ab81f18e2a4c9bb71b6f0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/68ae0266f46ab81f18e2a4c9bb71b6f0.jpg" class="img-polaroid" title="22.jpg" alt="22.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
例如，有2个 Topic，各自有2个 Partition。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/48933cbad41fbbc62929dc64f18fe3eb.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/48933cbad41fbbc62929dc64f18fe3eb.jpg" class="img-polaroid" title="23.jpg" alt="23.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这是逻辑上的形式，但在 Kafka 集群中的实际存储可能是这样的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/282b17ee23e46256b16cf1959d3047e4.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/282b17ee23e46256b16cf1959d3047e4.jpg" class="img-polaroid" title="24.jpg" alt="24.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Topic A 的 Partition #1 有3份，分布在各个 Node 上。<br>
<br>这样可以增加 Kafka 的可靠性和系统弹性。<br>
<br>3个 Partition #1 中，ZooKeeper 会指定一个 Leader，负责接收生产者发来的消息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/1abd67008eaabc11848f3558003c75e1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/1abd67008eaabc11848f3558003c75e1.jpg" class="img-polaroid" title="25.jpg" alt="25.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
其他2个 Partition #1 会作为 Follower，Leader 接收到的消息会复制给 Follower。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/e32c27a39568eb02ac85c5f0000e5e0c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/e32c27a39568eb02ac85c5f0000e5e0c.jpg" class="img-polaroid" title="26.jpg" alt="26.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这样，每个 Partition 都含有了全量消息数据。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/e728cfb84d848fb123ae951899187c3c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/e728cfb84d848fb123ae951899187c3c.jpg" class="img-polaroid" title="27.jpg" alt="27.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
即使某个 Node 节点出现了故障，也不用担心消息的损坏。<br>
<br>Topic A 和 Topic B 的所有 Partition 分布可能就是这样的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210430/83a9a199fce72fc92e9d7001dc2f9603.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210430/83a9a199fce72fc92e9d7001dc2f9603.jpg" class="img-polaroid" title="28.jpg" alt="28.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
感谢阅读，希望对你有所帮助 :)<br>
<br>译文链接：<a href="https://mp.weixin.qq.com/s/5wJ5Qwek_SDujb7L9xzvHg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/5wJ5Qwek_SDujb7L9xzvHg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            