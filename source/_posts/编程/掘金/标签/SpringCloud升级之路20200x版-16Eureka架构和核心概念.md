
---
title: 'SpringCloud升级之路2020.0.x版-16.Eureka架构和核心概念'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc03c574c4894a56807acfba039ac4be~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 17:13:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc03c574c4894a56807acfba039ac4be~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第20天</p>
<blockquote>
<p>本系列代码地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FHashZhang%2Fspring-cloud-scaffold%2Ftree%2Fmaster%2Fspring-cloud-iiford" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/HashZhang/spring-cloud-scaffold/tree/master/spring-cloud-iiford" ref="nofollow noopener noreferrer">github.com/HashZhang/s…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc03c574c4894a56807acfba039ac4be~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Eureka 目前 1.x 版本还在更新</strong>，但是应该<strong>不会更新新的功能</strong>了，只是对现有功能进行维护，升级并兼容所需的依赖。 <strong>Eureka 2.x 已经胎死腹中了</strong>。但是，这也不代表 Eureka 就是不能用了。如果你需要一个简便易于部署的注册中心，Eureka 还是一个很好的选择。云服务环境中，基本上所有实例地址和微服务名称都在不断变化，也并不太需要 Eureka 所缺少的持久化特性。当你的集群属于中小规模的时候（节点小于 1000 个）， <strong>Eureka 依然是一个不错的选择</strong>。当你的集群很大的时候，Eureka 的同步机制可能就限制了他的表现。</p>
<p>Eureka 的设计比较小巧，<strong>没有复杂的同步机制</strong>(例如 Nacos 基于 Raft，Zookeeper 基于 Zab)，<strong>也没有复杂的持久化机制</strong>，集群关系只是简单的将收到的客户端请求转发到集群内的其他 Eureka 实例。Eureka 本身也只有注册中心的功能，不像其他种类的注册中心那样，将注册中心和配置中心合在一起，例如 Consul 和 nacos。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a60dab4bb08646caaad3c554a3a897a7~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们<strong>忽略所有的 AWS 相关</strong>的术语以及配置还有相关逻辑处理。</p>
<p>Eureka 中的术语：</p>
<ol>
<li><strong>Eureka 实例</strong>：每个注册到 Eureka 上面的实例就是 <strong>Eureka 实例</strong>。</li>
<li><strong>Eureka 实例状态</strong>：包括 UP（可以处理请求），DOWN（健康检查失败，不能正常处理请求），STARTING（启动中，不能处理请求），OUT_OF_SERVICE（人为下线，暂时不处理请求），UNKNOWN（未知状态）。</li>
<li><strong>Eureka 服务器</strong>：作为注册中心运行，主要提供<strong>实例管理功能</strong>（处理实例注册（register）请求、处理实例注销（cancel）请求、处理实例心跳（renew）请求、内部处理实例过期（evict））、<strong>实例查询功能</strong>（各种查询实例信息的接口，例如通过 AppName 获取实例列表，通过实例 id 获取实例信息等等）</li>
<li><strong>Eureka 服务器集群</strong>：Eureka 服务器的集群，每个 Eureka 服务器都配置了区域以及可用区，Eureka 服务器收到的客户端请求会转发到同一区域内的其他 Eureka 服务器，可以配置优先发到同一可用区的 Eureka 服务器。非同一区域内 Eureka 服务器，通过定时拉取的方式进行同步。</li>
<li><strong>Eureka 客户端</strong>：请求 Eureka 服务器的客户端。封装发送实例注册（register）请求、实例注销（cancel）请求和实例心跳（renew）请求。</li>
<li><strong>VIP（或者是 Virtual Hostname）</strong>: Eureka 中可以通过两种方式获取实例，一个是通过服务名称，另一种是通过 VIP。每个实例都有服务名称，以及 VIP。Eureka 服务器中的索引方式是以服务名称为 key 的索引，我们也可以通过遍历所有实例信息的方式通过 VIP 字符串匹配获取相关的实例。在 Spring Cloud 体系中，一个实例的 VIP、SVIP（其实就是 Secure VIP，即 https 的地址）以及服务名称都是 <code>spring.application.name</code> 指定的服务名称。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2500f5f0ede841daacc0c9b15ebd602b~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3bc10268a0a40909555fc414e321a62~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，Service A 通过 Eureka Client <strong>发送注册请求</strong>（Register）到同一可用区的 Eureka Server 1。之后通过<strong>发送心跳请求</strong>（Renew）到这个 Eureka Server 1. Eureka Server 1 收到这些请求的时候，会处理这些请求并将这些请求转发到其他的集群内的 Eureka Server 2 和 Eureka Server 3. <strong>Eureka Server 2 和 Eureka Server 3 不会再转发收到的 Eureka Server 1 转发过来的请求</strong>。然后，Service B 还有 Service C 通过 Eureka 获取到了 Service A 的位置，最后调用了 Service A。</p>
<p>对于本地没有查询到的微服务，Eureka Server 还会从远程 Region 的 Eureka Server 去获取，例如这里对于 Service D，本地没有查到，Eureka Server 会返回远程 Region 的 Service D 的实例。由于本地有 Service A，所以肯定不会返回远程 Region 的 Service A 的实例。并且，本地是定时拉取的远程 Region 的 Service 列表，并不是每次查询的时候现查询的。</p>
<p>一般的，微服务之间的互相调用，并不经过 Eureka，也不会涉及到 Eureka 客户端了，而是通过负载均衡器调用，这个我们后面就会提到。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4a8f30396004a9d816f434fbce70d80~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们这一节详细分析了 Eureka 的架构，以及其中的核心概念。下一节，我们将开始介绍我们微服务的注册中心 Eureka 的实例配置。</p>
<blockquote>
<p><strong>微信搜索“我的编程喵”关注公众号，每日一刷，轻松提升技术，斩获各种offer</strong>：</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/950933961f2547b38acddc9026f98b69~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            