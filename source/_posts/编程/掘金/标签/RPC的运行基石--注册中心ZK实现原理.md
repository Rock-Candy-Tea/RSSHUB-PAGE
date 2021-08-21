
---
title: 'RPC的运行基石--注册中心ZK实现原理'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34b66597e3a5494d8c9672ad0a91cb71~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 19:25:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34b66597e3a5494d8c9672ad0a91cb71~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第16天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>RPC的目的，是将远程调用变得像本地调用一样简单方便，主要由客户端、服务端、注册中心三部分组成。</p>
<p>那么，服务端发布的接口怎么向客户端暴露？客户端怎么获取到服务端的地址并创建连接执行调用逻辑呢？</p>
<p>本篇将带大家 通过分析一个由Zookeeper引发的全链路服务雪崩的真实案例，来说明注册中心的生产场景诉求和选型原则。</p>
<h2 data-id="heading-0">0.1 注册中心</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34b66597e3a5494d8c9672ad0a91cb71~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图所示</p>
<p><em>Provider</em> 主要向注册中心进行服务注册，以及上报服务节点心跳。</p>
<p><em>Consumer</em> 需要向注册中心订阅感兴趣的服务，将对应服务的节点信息缓存到本地，同时接受注册中心下发的服务变动通知。</p>
<p><em>注册中心</em> 的职权也很明确了，就是维护服务信息以及服务实例节点信息，同时监测服务节点心跳，确认节点状态，在节点状态不健康时，从实例列表中剔除；同时在节点列表变动时，负责通知订阅者，以实现服务的及时更新和数据一致性</p>
<h2 data-id="heading-1">0.2 Zookeeper 注册中心实现方案</h2>
<p>ZK曾经真的非常火，当然现在也不差。很多年之前，同事曾经笑称，只要架构里用上ZK，就可以叫分布式。</p>
<p>ZK是经常被提及的注册中心选型。那么ZK怎么实现注册中心呢？</p>
<p><strong>节点创建的能力</strong></p>
<p>持久化节点。在节点创建后，就一直存在，直到有删除操作来主动清除这个节点。</p>
<p>临时节点。将自身的生命周期和客户端状态绑定。如果客户端会话失效，那么这个节点就会自动被清除掉。注意，这里提到的是会话失效，而非连接断开。</p>
<p><strong>监听通知的能力</strong></p>
<p>也就是Watch机制。一个zk的节点可以被监控，包括这个目录中存储的数据的修改，子节点目录的变化，一旦变化可以通知设置监控的客户端。<br>
这个功能是zookeeper对于应用最重要的特性，通过这个特性可以实现的功能包括配置的集中管理，集群管理，分布式锁等等。</p>
<p><em>ZK的上述两个关键能力，让其成为注册中心成为可能</em>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10bf9bfa04a64dca985d2fadb8d4ecde~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Zookeeper注册中心</p>
<p>如上图所示，ZK创建了Service的持久化节点，在Service下创建了Provider和Consumer两个子节点，也是持久化的；在Provider和Consumer下挂着很多临时节点，每一个临时节点，代表一个应用实例。这样方便根据实例状态进行动态增减。然后用wtach机制来监听服务端心跳，通知客户端服务节点的变动，从而实现注册中心的整个能力。</p></div>  
</div>
            