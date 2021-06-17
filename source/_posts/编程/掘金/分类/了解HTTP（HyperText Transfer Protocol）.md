
---
title: '了解HTTP（HyperText Transfer Protocol）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eff1fac202194b2891b1c418aae4c21a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 02:30:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eff1fac202194b2891b1c418aae4c21a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0"><strong>一、诞生</strong></h1>
<p>89年3月，CERN（欧洲核子研究组织）蒂姆• 伯纳斯 - 李（Tim BernersLee） 博士提出了一种能让远隔两地的研究者们共享知识的设想。理念：借助多文档之间相互关联形成的超文本 （HyperText），连成可相互参阅的 WWW（World Wide Web，万维网）；
92年9月，第一个网站（ <a href="http://www.ibarakiken.gr.jp/www/" target="_blank" rel="nofollow noopener noreferrer">www.ibarakiken.gr.jp/www/</a> ）</p>
<h1 data-id="heading-1"><strong>二、传输过程</strong></h1>
<p>一个简单的HTTP报文（起始行、首部、主体）：
request</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eff1fac202194b2891b1c418aae4c21a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
response</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6997c7248e484d84aa0d39d19dca9097~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
传输过程：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df775cb760fa49579fded4e4b3f30bc4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d210031f61f411fa8760f19c45a03bf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">三、发展</h1>
<h2 data-id="heading-3">http0.9</h2>
<ol>
<li>
<p>只有一个命令GET</p>
</li>
<li>
<p>没有header等描述数据的信息</p>
</li>
<li>
<p>服务器发送完毕，就关闭TCP连接</p>
</li>
</ol>
<h2 data-id="heading-4">http1.0</h2>
<ol>
<li>
<p>增加了status,code和header</p>
</li>
<li>
<p>多字符集，多部分发送，权限，缓存</p>
</li>
<li>
<p>缓存：If-Modified-Since,Expires</p>
</li>
</ol>
<h2 data-id="heading-5">http1.1</h2>
<ol>
<li>
<p>持久连接keep-alive，复用TCP链接，时间由服务端控制，在一个TCP连接上可以传送多个HTTP请求和响应，减少了建立和关闭连接的消耗和延迟，在HTTP1.1中默认开启Connection： keep-alive，一定程度上弥补了HTTP1.0每次请求都要创建连接的缺点。</p>
</li>
<li>
<p>缓存：Entity tag，If-Unmodified-Since, If-Match, If-None-Match</p>
</li>
<li>
<p>断点续传： range</p>
</li>
<li>
<p>Host头处理，在HTTP1.0中认为每台服务器都绑定一个唯一的IP地址，因此，请求消息中的URL并没有传递主机名（hostname）。但随着虚拟主机技术的发展，在一台物理服务器上可以存在多个虚拟主机（Multi-homed Web Servers），并且它们共享一个IP地址。HTTP1.1的请求消息和响应消息都应支持Host头域，且请求消息中如果没有Host头域会报告一个错误（400 Bad Request）。</p>
</li>
</ol>
<h2 data-id="heading-6">http2</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/218bfc95ad7047c29e78e3e0b9721f1d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">1. 二进制分帧/多路复用</h4>
<p>所有数据以二进制传输，在 TCP 协议中，数据的传输单位是数据报。数据分成两大部分。头部(header) 和 实际数据部分(body)。在 HTTP 2.0 中，它把数据报的两大部分分成了 header frame 和 data frame。也就是头部帧和数据体帧。帧的传输最终在流（Stream）中进行，
同一个连接里面发送多个请求不再需要按照顺序来。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1285db77a9948548411df9b3202ac32~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
HTTP2中二进制协议的基本单元叫 frame（帧），不同frame 有不同作用，如：</p>
<ol>
<li>
<p><code>SETTING</code> 帧：建立连接时，向对方传达一些配置信息如是否开启 server push 功能、最大帧 size等等；</p>
</li>
<li>
<p><code>HEADERS</code> 帧：发送 http 的 request 或者response的头部；</p>
</li>
<li>
<p><code>CONTINUATION</code> 帧：headers 要跨越多个帧，用此来指示头部上一个 <code>HEADERS</code> ；本质就是 <code>HEADERS</code> 帧，但是为了轻松处理，就用明确的类型来区分这种情况；</p>
</li>
<li>
<p><code>DATA</code> 帧：发送body数据用；</p>
</li>
<li>
<p><code>PUSH_PROMISE</code> 帧：用来告知对端初始化哪些数据，服务于 <code>server push</code> 功能</p>
</li>
<li>
<p><code>WINDOW_UPDATE</code> 帧：用来做流量控制。</p>
</li>
</ol>
<p>流代表了一个完整的请求-响应数据交互过程。它具有如下几个特点：</p>
<ol>
<li>
<p>双向性：同一个流内，可同时发送和接受数据。</p>
</li>
<li>
<p>有序性：流中被传输的数据就是二进制帧 。帧在流上的被发送与被接收都是按照顺序进行的。</p>
</li>
<li>
<p>并行性：流中的 二进制帧 都是被并行传输的，无需按顺序等待。但却不会引起数据混乱，因为每个帧都有顺序标号。它们最终会被按照顺序标号来合并。</p>
</li>
<li>
<p>流的创建：流可以被客户端或服务器单方面建立, 使用或共享。</p>
</li>
<li>
<p>流的关闭：流也可以被任意一方关闭。</p>
</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccb1802ce0db4df1a53f0011756dc713~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">2. 服务端推送</h4>
<p>服务端可以在发送页面HTML时主动推送其它资源，而不用等到浏览器解析到相应位置，发起请求再响应。例如服务端可以主动把JS和CSS文件推送给客户端，而不需要客户端解析HTML时再发送这些请求。
服务端可以主动推送，客户端也有权利选择是否接收。如果服务端推送的资源已经被浏览器缓存过，浏览器可以通过发送RST_STREAM帧来拒收。主动推送也遵守同源策略，服务器不会随便推送第三方资源给客户端。</p>
<h4 data-id="heading-9">3. 头部压缩（HPACK）</h4>
<p>HTTP1.x的header很多时候都是重复多余的。选择合适的压缩算法可以减小包的大小和数量。通过静态 Huffman 代码对传输的标头字段进行编码，从而减小了各个传输的大小。客户端和服务器同时维护和更新一个包含之前见过的header的索引列表（换句话说，它可以建立一个共享的压缩上下文），此列表随后会用作参考，对之前传输的值进行有效编码。利用 Huffman 编码，可以在传输时对各个值进行压缩，而利用之前传输值的索引列表，我们可以通过传输索引值的方式对重复值进行编码，索引值可用于有效查询和重构完整的header键值对。</p>
<ul>
<li>
<p>消息发送端和消息接受端共同维护一份静态表和一份动态表（这两个合起来充当 <strong>字典</strong> 的角色），</p>
</li>
<li>
<p>每次请求时，发送方根据字典的内容以及一些特定指定，编码压缩消息头部，</p>
</li>
<li>
<p>接收方根据字典进行解码，并且根据指令来判断是否需要更新动态表</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/193bd73d5d574e6d987770cf009d6160~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">4. 其他</h4>
<p>http2.0并没有改变http1.x的语义，只是把原来http1.x的header和body部分用frame重新封装了一层而已，HTTP2向下兼容，需确认server是否支持2.0，这一过程一般在ssl握手阶段完成，http2叫ALPN(Application Layer Protocol Negotiation)，SPDY叫NPN (Next Protocol Negotiation)。</p>
<h4 data-id="heading-11">5. 与http1.*对比</h4>
<p><a href="https://http2.akamai.com/demo" target="_blank" rel="nofollow noopener noreferrer">http2加载速度对比http1.1</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4ffd0c9af6d43ce8abfc859af00220e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>HTTP2.0的多路复用和HTTP1.X中的长连接复用有什么区别？</strong>
HTTP/1.* 一次请求-响应，建立一个连接，用完关闭；每一个请求都要建立一个连接；HTTP/1.1，Pipeling解决方式为，若干个请求排队串行化单线程处理，后面的请求等待前面请求的返回才能获得执行机会，一旦有某请求超时等，后续请求只能被阻塞。（ <a href="https://www.chromium.org/developers/design-documents/network-stack/http-pipelining" target="_blank" rel="nofollow noopener noreferrer">Pipeling条件苛刻</a> ，只有幂等的请求（GET，HEAD）能使用pipelining，非幂等请求比如POST不能使用，且中间路由支持参差不齐，最终的结果可能反而使页面访问速度下降，所以浏览器一般都是直接建立多个TCP链接）。
HTTP/2多个请求可同时在一个连接上并行执行。某个请求任务耗时严重，不会影响到其它连接的正常执行，但丢包同样会阻塞后面的请求，HTTP2通过streamID来区分一个TCP链接中的不同请求。</p>
<h2 data-id="heading-12">HTTP3(QUIC（Quick UDP Internet Connection））</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b1df3e76f12480ebb67b4d857a77190~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>实现了类似 TCP 的流量控制、传输可靠性的功能。虽然 UDP 不提供可靠性的传输，但 QUIC 在 UDP 的基础之上增加了一层来保证数据可靠性传输。它提供了数据包重传、拥塞控制以及其他一些 TCP 中存在的特性。</p>
</li>
<li>
<p>集成了 TLS 加密功能。目前 QUIC 使用的是 TLS1.3，相较于早期版本 TLS1.3 有更多的优点，其中最重要的一点是减少了握手所花费的 RTT 个数。</p>
</li>
<li>
<p>实现了 HTTP/2 中的多路复用功能。和 TCP 不同，QUIC 实现了在同一物理连接上可以有多个独立的逻辑数据流。实现了数据流的单独传输，就解决了 TCP 中队头阻塞的问题。</p>
</li>
</ul>
<p>参考
<a href="https://juejin.im/post/5b88a4f56fb9a01a0b31a67e" target="_blank" rel="nofollow noopener noreferrer">juejin.im/post/5b88a4…</a>
<a href="https://segmentfault.com/a/1190000017011816" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p></div>  
</div>
            