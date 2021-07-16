
---
title: '前端通讯协议大比拼：WebSockets和HTTP'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2d30bf3a5444fd6a9dc93e7102ea99f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 19:34:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2d30bf3a5444fd6a9dc93e7102ea99f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p>在实时应用程序中，毋庸置疑，需要在信息可用时立即从服务器获取信息。而且，从根本上说，经典的 HTTP <code>请求/响应</code>模式无法胜任这项工作。因为服务器将保持沉默，无论是否有新数据，除非或直到消费者请求更新。</p>
<p>随着开发人员试图使<code>请求/响应</code>模型适应更动态的实时Web的需求，这种限制导致了各种黑客和变通方法的出现（其中一些变得正式并被广泛采用）。</p>
<p>所有这些技术和方法，从 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FComet_%2528web%25E6%258A%2580%25E6%259C%25AF%2529" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/Comet_%28web%E6%8A%80%E6%9C%AF%29" ref="nofollow noopener noreferrer">Comet</a> 到 HTTP 长轮询，都有一个共同点：本质上，它们开始创造真正实时（事件驱动）数据交换/通信的错觉，所以当服务器有一些新数据时，它发送一个响应。</p>
<p>尽管 HTTP 不是事件驱动的协议，因此也不是真正的实时，但这些方法实际上在特定用例中非常有效，例如 Gmail 聊天。然而，在低延迟应用程序或大规模应用程序中会出现问题，主要是因为与 HTTP 相关的处理需求。</p>
<p>也就是说，对于 HTTP，必须不断请求更新（并获得响应），这是非常耗费资源的：客户端建立连接->请求更新->从服务器获得响应，然后关闭连接。想象一下，这个过程被成千上万的并发用户无休止地重复，这对服务器来说是非常繁重的压力。</p>
<p>正是这些问题最终促使开发人员 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frakutentechnologyconference2017.sched.com%2Fspeaker%2Fmichael_carter.1x8q89tm" target="_blank" rel="nofollow noopener noreferrer" title="https://rakutentechnologyconference2017.sched.com/speaker/michael_carter.1x8q89tm" ref="nofollow noopener noreferrer">Michael Carter</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FIan_Hickson" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Ian_Hickson" ref="nofollow noopener noreferrer">Ian Hickson</a> 开发 WebSockets ，本质上是一个构建在设备 TCP/IP 堆栈之上的薄传输层。其目的是为 Web 应用程序提供本质上是 TCP 通信层的东西，它尽可能接近原生，禁止一些抽象，以消除某些基于安全的复杂性和其他问题。</p>
<p>本文将着眼于一些用于绕过实时应用程序中 HTTP <code>请求/响应</code> 模式的限制的技术，每个技术的一些相关问题，以及 WebSockets 如何帮助克服这些问题。</p>
<h3 data-id="heading-0">HTTP</h3>
<p>HTTP 本质上是<code>客户端-服务器</code>计算模型中的<code>请求/响应</code>协议，是万维网的主要通信方式。最初的版本由 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E8%2592%2582%25E5%25A7%2586%25C2%25B7%25E4%25BC%25AF%25E7%25BA%25B3%25E6%2596%25AF-%25E6%259D%258E" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E8%92%82%E5%A7%86%C2%B7%E4%BC%AF%E7%BA%B3%E6%96%AF-%E6%9D%8E" ref="nofollow noopener noreferrer">Tim Berners-Lee</a> 在 1989 年作为应用程序协议提出，非常有限，并迅速修改以支持更广泛的浏览器和服务器功能。</p>
<p>尽管 HTTP/1.0 不被视为正式规范或互联网标准，但这些修改最终在 1996 年被 HTTP 工作组记录为 HTTP/1.0（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc1945" target="_blank" rel="nofollow noopener noreferrer" title="https://datatracker.ietf.org/doc/html/rfc1945" ref="nofollow noopener noreferrer">RFC 1945</a>）。</p>
<h4 data-id="heading-1">HTTP/1.1</h4>
<p>HTTP/1.1 是 Web 浏览器和服务器中最广泛支持的版本，它的到来是向前迈出的一大步，因为它实现了一些非常重要的优化和增强，从持久和管道连接到新的<strong>请求/响应头字段</strong>。其中最主要的是两个标头，它们是许多改进的基础，这些改进有助于实现更动态的实时WEB：</p>
<p><code>Keep-Alive 标头</code>：用于设置主机之间的持久通信。意味着连接可以被重复用于多个请求，这显着减少了请求延迟，这样客户端就不需要在发送第一个请求后重新协商 TCP握手（3次握手）连接。另一个积极的副作用是，由于 TCP 的慢启动机制，连接会随着时间的推移而变得更快。在 HTTP/1.1 之前，必须为每个请求/响应对打开一个新连接。</p>
<p><code>Upgrade 头</code>：用于将连接升级到增强协议模式（如 WebSockets）。</p>
<h5 data-id="heading-2">HTTP 轮询</h5>
<p>HTTP 轮询代表了经典<strong>请求/响应</strong>机制的进步，尽管轮询有多种版本，但只有长轮询在任何情况下都适用于实时 WEB 程序。</p>
<p>例如，HTTP 短轮询使用基于 AJAX 的计时器来确保客户端设备以固定时间间隔发送服务器请求。但是，服务器仍会立即响应每个请求，在关闭连接之前，要么提供新数据，要么在没有新数据的情况下发送“<strong>空</strong>”响应。因此，当客户端需要在新数据可用时立即响应时，这在实时应用程序中真的没有多大用处。</p>
<p>正是这种限制导致了 HTTP 长轮询的发展，它本质上是一种旨在模拟服务器推送功能的技术。</p>
<p>本质上长轮询是一种技术，其中服务器选择将客户端的连接保持尽可能长的时间（通常为 20 秒），仅在任一数据之后传递响应变为可用或达到超时阈值。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2d30bf3a5444fd6a9dc93e7102ea99f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>长轮询的主要优点是，理论上，只要新信息可用，就会立即将其发送给客户端。然而，不足之处是处理 HTTP 请求带来的额外开销。</p>
<h5 data-id="heading-3">HTTP 流媒体</h5>
<p>HTTP 流是一种推送式数据传输技术，它允许 Web 服务器通过无限期保持打开的单个 HTTP 连接向客户端连续发送数据。本质上，客户端发出一个 HTTP 请求，服务器推出一个不确定长度的响应。</p>
<p>然而，虽然 HTTP 流传输性能良好、易于使用并且可以替代 WebSockets，但它存在有局限性。从实时角度来看，主要问题是中介可以中断连接（无论是通过超时还是仅仅因为它以“循环方式”服务多个请求），因此并不总是能够保证实时性。</p>
<h4 data-id="heading-4">HTTP/2.0</h4>
<p>HTTP/2.0 由 Google 于 2009 年最初宣布的实验性协议 SPDY 演变而来。到 2015 年，HTTP 工作组发布了 HTTP/2.0 作为建议标准，并以 SPDY 规范为起点。</p>
<p>它本质上是一个旨在提高 Web 通信速度的性能更新，主要有以下两个实用功能：</p>
<ul>
<li>
<p><strong>多路复用</strong>：不是以明文格式传输数据，而是将数据编码为二进制并封装在帧内，这些帧可以沿着称为流的双向通道进行多路复用，全部通过单个 TCP 连接。这就允许同时发生许多并行的<strong>请求/响应</strong></p>
</li>
<li>
<p><strong>服务器推送</strong>：服务器推送是一种性能特性，它允许服务器在客户端请求响应之前向符合 HTTP/2 的客户端发送响应。当服务器知道客户端需要“推送”响应来完全处理原始请求时，此功能很有用。</p>
</li>
</ul>
<p>尽管有这些进步，如今由于移动设备的大量使用，互联网流量的爆炸式增长使得 HTTP/2.0 难以提供流畅、透明的网页浏览体验，特别是在实时应用程序及其用户需求日益增长的情况下。</p>
<h5 data-id="heading-5">优点</h5>
<ul>
<li>
<p>通过安装 SSL 证书，所有浏览器都支持基于 HTTPS 的 HTTP/2 协议。</p>
</li>
<li>
<p>HTTP/2 允许客户端通过单个 TCP 连接并发发送所有请求，理论上，客户端可以更快地加载资源。</p>
</li>
<li>
<p>TCP 是一种可靠、稳定的连接协议。</p>
</li>
</ul>
<h5 data-id="heading-6">缺点</h5>
<ul>
<li>
<p>并发请求会增加服务器的负载。HTTP/2 服务器可以大批量接收请求，这可能会导致请求超时。服务器负载峰值的问题可以通过使用负载均衡器或代理服务器来解决，限制转发请求。</p>
</li>
<li>
<p>服务器对 HTTP/2 优先级的支持还不成熟。软件支持仍在不断发展，某些 CDN 或负载均衡器可能无法正确支持优先级。</p>
</li>
<li>
<p>HTTP/2 推送功能可能很难正确实现。</p>
</li>
<li>
<p>HTTP/2 解决了 HTTP 首尾阻塞问题，但 TCP 级别的阻塞仍然会导致问题。</p>
</li>
</ul>
<h4 data-id="heading-7">HTTP/3.0</h4>
<p>HTTP/3.0 是 HTTP 的新迭代，自 2018 年以来一直在开发中，尽管它仍然是标准草案，但一些浏览器已经支持它了，如 Chrome。</p>
<p>HTTP/3 的目标是通过解决 HTTP/2 与传输相关的问题，在所有形式的设备上提供快速、可靠和安全的 Web 连接。为此，它使用称为 QUIC 的不同传输层网络协议，该协议运行在用户数据报协议 (UDP) 上，而不像其他早期版本那样使用 TCP。</p>
<p>不过 HTTP/3 已经开始出现一些潜在的问题，例如：</p>
<ul>
<li>
<p><strong>传输层的影响</strong>：过渡到 HTTP/3 不仅涉及应用层的变化，还涉及底层传输层的变化。因此，与其前身相比，采用 HTTP/3 更具挑战性。</p>
</li>
<li>
<p><strong>可靠性和数据完整性问题</strong>：UDP 一般适用于可以接受丢包的应用，那是因为 UDP 不保证数据包会按顺序到达。事实上，它并不能保证数据包一定会到达，因此，如果数据完整性对应用实例很重要并且使用的是 HTTP/3，则将必须构建相应的机制来确保消息排序和完整的到达。</p>
</li>
</ul>
<h5 data-id="heading-8">优点</h5>
<ul>
<li>
<p>引入运行在 UDP 上的新（不同）传输协议 QUIC 意味着理论上和目前实验上的延迟减少。</p>
</li>
<li>
<p>由于 UDP 不在协议栈中执行错误检查和纠正，因此它适用于不需要这些或在应用程序中执行这些的应用场景。UDP 通常用于时间敏感的应用程序，例如实时系统，它不能等待数据包重新传输，因此可以容忍一些丢弃的数据包。</p>
</li>
</ul>
<h5 data-id="heading-9">缺点</h5>
<ul>
<li>
<p><strong>传输层的影响</strong>：过渡到 HTTP/3 不仅涉及应用层的变化，还涉及底层传输层的变化。因此，与其前身相比，采用 HTTP/3 更具挑战性。</p>
</li>
<li>
<p><strong>可靠性问题</strong>：UDP 应用程序往往缺乏可靠性，必须承认会有一定程度的数据包丢失、重新排序、错误或重复。由最终用户应用程序提供任何必要的握手，例如已收到消息的实时确认。</p>
</li>
<li>
<p>HTTP/3 还没有完全标准化。</p>
</li>
</ul>
<h3 data-id="heading-10">WebSockets</h3>
<p>关于WebSockets 的详细介绍，可以参阅《<a href="https://juejin.cn/post/6984805538819227684" target="_blank" title="https://juejin.cn/post/6984805538819227684">深入学习WebSockets概念和实践</a>》。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fed6dc6ba7bf4a3095e7b62491841867~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>WebSockets 允许服务器和客户端随时推送消息，而与之前的请求没有任何关系。使用 WebSockets 的一个显着优势是，几乎每个浏览器都支持 WebSockets。</p>
<p>WebSocket 解决了一些 HTTP 问题：</p>
<ul>
<li>
<p><strong>双向协议</strong>：客户端/服务器可以向对方发送消息（在 HTTP 中，请求总是由客户端发起，响应由服务器处理）</p>
</li>
<li>
<p><strong>全双工通信</strong>：客户端和服务器可以同时独立地相互通信。</p>
</li>
<li>
<p><strong>单个 TCP 连接</strong>： 一开始升级 HTTP 连接后，客户端和服务器在 WebSocket 连接的整个生命周期都通过相同的 TCP 连接（持久连接）进行通信，很好的节省服务器资源和带宽。</p>
</li>
</ul>
<h4 data-id="heading-11">优点</h4>
<ul>
<li>
<p>WebSocket 是一种事件驱动的协议，这意味着可以将其用于真正的实时通信。与 HTTP 不同（必须不断地请求更新），而使用 websockets，更新在可用时就会立即发送。</p>
</li>
<li>
<p>WebSockets 保持单个持久连接打开，同时消除基于 HTTP <strong>请求/响应</strong>的方法出现的延迟问题。</p>
</li>
<li>
<p>WebSockets 通常不使用 XMLHttpRequest，因此，每次需要从服务器获取更多信息时，都不会发送标头。这反过来又减少了发送到服务器的数据负载。</p>
</li>
</ul>
<h4 data-id="heading-12">缺点</h4>
<ul>
<li>
<p>当连接终止时，WebSockets 不会自动恢复，这是应用开发中需要自己实现的机制，也是存在许多客户端开源库的原因之一。</p>
</li>
<li>
<p>早于 2011 年的浏览器无法支持 WebSocket 连接，这个现在可以忽略不计。</p>
</li>
</ul>
<h3 data-id="heading-13">总结</h3>
<p>通常，在实时、持续通信的上下文中，WebSockets 将是更好的选择。</p>
<p>基于 HTTP 的技术往往在服务器上占用更多资源，而 WebSockets 在服务器上的占用空间非常小。同时，像长轮询这样的方法也需要在服务器和设备之间进行多次跳转，并且这些网关通常对允许连接保持打开状态的时间有不同的限制。</p>
<p>如果项目中有长连接、不断更新、实时数据交互的需求，应该首选 WebSockets 来构建。</p></div>  
</div>
            