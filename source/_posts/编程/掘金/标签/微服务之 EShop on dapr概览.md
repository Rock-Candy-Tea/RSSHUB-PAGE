
---
title: '微服务之 EShop on dapr概览'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9b644f53f3442d79689fc1626a1912b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 06:38:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9b644f53f3442d79689fc1626a1912b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第26天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">1. Dapr简介</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9b644f53f3442d79689fc1626a1912b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Dapr，微软牵头开发的分布式运行时，致力于打造一款事件驱动，可移植可扩展可构建在云端，也可构建在本地的分布式运行时。</p>
<p>身具服务发现、基础设施服务代理网关、自身具有状态管理、消息订阅发布以及Actors，遥测等功能，实乃微服务架构之首选。</p>
<h1 data-id="heading-1">2. Eshop 示例</h1>
<p>微软的web应用基本都以Eshop为例来阐述自己真的可以完成搞定XXX的需求，因此这次也不例外，一个基于Dapr的微服务就摆在了我们的面前。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6197c0328c34e5f9780653fa6567b4f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Eshop的业务就是线上的一个小商店，具有订单、支付、分类、购物车等功能。</p>
<h1 data-id="heading-2">3.微服务架构</h1>
<p>这个示例支持多种部署方案，可以使用Docker，也可以使用Kubernetes。
就让我们来看看其架构如何？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bddaeb459b242e98349ce3b15b9278e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>微服务使用到了Dapr的Actors功能、状态管理功能、服务积木功能、发布/订阅功能、安全配置、事件绑定触发功能，这里例子还是比较齐活的。</p>
<p>这套业务采用经典的前后分离方式，由前端SPA， 后端Api组成。重点在后端的架构。</p>
<p>后端服务统一使用Dapr管理，SPA前端访问的是一个Api网关，网关由基础服务Envoy构成，其和SideCar模式的Dapr功能组成前置服务。</p>
<p>登录授权服务由Identity Service完成，注意其是独立的，并未加入到Dapr服务内。主要提供OAuth授权Token。</p>
<p>Api网关通过Dapr，可以直接访问主要的业务Api服务：（Basket、Catelog、Ordering、Payment），也可以访问Api聚合服务（BFF）；Api聚合服务（Web shopping aggregator）通过Dapr的访问接口访问聚合上游服务接口。</p>
<p>在上游Api服务中，其通讯协议均采用Http方式，而Dapr使用GRPC协议方式和其进行通讯，并通过Http方式和下游服务进行通讯。当然也可以配置为统一使用 GRPC协议方式。</p>
<h1 data-id="heading-3">4.项目地址</h1>
<p>项目存放在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdotnet-architecture%2FeShopOnDapr" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dotnet-architecture/eShopOnDapr" ref="nofollow noopener noreferrer">Github</a>，感兴趣的童鞋可以拉下来运行下，因为我工作机器内存配置的问题，我并没有把这个例子跑起来。</p>
<p>是的，微服务的本地调试环境是个大问题，要搭起来K8s一套，实在是让人头疼啊。</p>
<p>Dapr简化了什么工作呢？</p>
<p>Dapr 使开发人员可以使用任何语言或框架轻松编写微服务。它解决了分布式应用程序中的许多挑战，例如：</p>
<ul>
<li>分布式服务如何相互发现并同步通信？</li>
<li>他们如何实现异步消息传递？</li>
<li>他们如何在整个事务中维护上下文信息？</li>
<li>他们如何才能适应失败？</li>
<li>它们如何扩展以满足不断变化的需求？</li>
<li>他们是如何被监控和观察的？</li>
</ul>
<p>项目文件结构</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/373a95e8fde84eb6a00c5181c54c2b9a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>希望周末能运行起来它！</p>
<pre><code class="copyable">dapr init
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">🎏 5. 小结</h1>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            