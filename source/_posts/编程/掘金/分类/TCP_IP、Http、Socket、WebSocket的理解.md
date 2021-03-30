
---
title: 'TCP_IP、Http、Socket、WebSocket的理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/376549b16d9944b38f4d3ea7c207e18a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 29 Mar 2021 19:00:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/376549b16d9944b38f4d3ea7c207e18a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">OSI 模型</h1>
<ul>
<li><strong>应用层</strong>：各种应用层协议，Http、WebSocket、FTP、SMTP等</li>
<li>表示层：信息的语法语义以及他们的关联，如加密解密、转换翻译、压缩解压缩</li>
<li>会话层：不同机器上的用户之间建立及管理会话</li>
<li><strong>传输层</strong>：接受上一层的数据，在必要的时候把数据进行分割，并将这些数据提交给网络层，且保证这些数据段有效到达对端。TCP、UDP协议。</li>
<li><strong>网络层</strong>：控制子网的运行，如逻辑编址、分组传输、路由选择。IP
协议。</li>
<li>数据链路层：物理寻址，同时将原始比特流转变为逻辑传输线路。</li>
<li>物理层：机械、电子、定时接口通信信道上的原始比特流传输。</li>
</ul>
<h1 data-id="heading-1">基本介绍</h1>
<p><strong>TPC/IP协议栈，主要解决数据如何在网络中传输，而HTTP是应用层协议，主要解决如何包装数据。</strong></p>
<p>把<strong>IP想像两个站点</strong>，<strong>TCP和UDP是高速公路，HTTP 、FTP 就是货车</strong>，而 Socket 就是两个站点的检票口。<strong>货车(http)在一端站点(ip)先通过检票口(socket)，检票后行驶在高速公路(tcp)上，到达另一站点(ip)卸载货物(http)。</strong></p>
<p><a href="https://juejin.cn/post/6945276190965891108#http">HTTP</a>，<a href="https://juejin.cn/post/6945276190965891108#websocket">WebSocket</a>，<a href="https://juejin.cn/post/6945276190965891108#tcp/udp">TCP，UDP</a>，IP都是协议，而 TCP/IP 是不同协议的组合，通常称之为 <strong>协议栈</strong>，是为了完成对应功能而制定的统一规则。</p>
<p><a href="https://juejin.cn/post/6945276190965891108#socket">Socket（套接字）</a>实际上是对 TCP/IP协议栈 的封装，本身并不是协议，而是一个<strong>调用接口（API）</strong>。</p>
<span id="user-content-http">
<h2 data-id="heading-2">1. Http协议</h2>
<p>Http协议，超文本传输协议，web上一问一答的两台计算机之间遵循的通信规则。</p>
<ul>
<li>请求组成：请求行、请求头、请求空行、请求主体</li>
<li>响应组成：响应状态行、响应头、响应空行、响应正文</li>
</ul>
<p>Http是<strong>无状态</strong>的，客户端每次发送的请求都是一个新的请求，所以一般网站登录后的身份信息，放置到请求头 cookie 上。</p>
<p>Http是<strong>无连接</strong>的，HTTP是基于TCP协议的应用，请求时需建立TCP连接，HTTP协议本身无需连接，其只处理数据的封装。</p>
<ul>
<li>
<p>每次 http 请求时需建立TCP连接，请求结束后断开连接，完成一次请求/响应操作，所以为<code>短连接</code>。</p>
</li>
<li>
<p>而 <strong>HTTP/1.1</strong> 中的 <code>keep-alive</code> 所保持的<code>长连接</code>则是为了优化每次 HTTP 请求中 TCP连接三次握手的麻烦和资源开销，只建立一次TCP连接，多次的在这个通道上完成请求/响应操作。但这些请求是<strong>串行</strong>的，当某一个请求阻塞时就会导致同一条连接的后续请求被阻塞。</p>
</li>
<li>
<p><strong>Http/2</strong> ：多路复用技术出现；能够让多个请求和响应的传输完全混杂在一起进行；通过 <code>streamID</code> 来互相区别，更多了解 <a href="https://www.imyangyong.com/blog/2019/05/http/%E6%9C%8D%E5%8A%A1%E7%AB%AF%E6%8E%A8%E9%80%81%E6%96%B9%E6%A1%88/" target="_blank" rel="nofollow noopener noreferrer">服务端推动方案</a> 最后有介绍。</p>
</li>
</ul>
<blockquote>
<p>值得一提的是，服务器无法主动给客户端推送消息。</p>
</blockquote>
<span id="user-content-socket">
<h2 data-id="heading-3">2. Socket协议</h2>
<p>Socket是为了方便开发者<strong>直接使用</strong> **更底层协议（一般是TCP或UDP）**而存在的一个抽象层。</p>
<p>Socket实际上是对 TCP/IP协议栈 的封装，本身并不是协议，而是一个<strong>调用接口（API）</strong>。</p>
<p>Socket的出现只是使得程序员更方便地使用 TCP/IP协议栈 而已，是对 TCP/IP协议栈 的抽象，从而形成了我们知道的一些最基本的函数接口，比如create、listen、connect、accept、send、read和write。</p>
<p>主机A 的应用程序要能和 主机B 的应用程序通信，必须通过Socket建立连接，而建立Socket连接必须需要底层TCP/IP协议 来建立 TCP连接。建立 TCP连接 需要底层IP协议来寻找网络中的主机。我们知道网络层使用IP协议可以帮助我们根据IP地址来找到目标主机，但是一台主机上可能运行着多个应用程序，如何才能与指定的应用程序通信就要通过TCP或UDP的地址也就是端口号来指定。这样就可以通过一个Socket实例唯一代表一个主机上的一个应用程序的通信链路了。</p>
<span id="user-content-websocket">
<h2 data-id="heading-4">3. WebSocket协议</h2>
<p>基于Http协议的扩展，支持长连接，用于建立客户端和服务器的双向通道。</p>
<p>而传统的轮询方式（即采用http协议不断发送请求）的缺点：浪费流量（http请求头比较大）、浪费资源（没有更新也要请求）、消耗服务器CPU占用（没有信息也要接收请求）。</p>
<p><strong>实现过程：</strong></p>
<p>在Javascript中创建了WebSockets之后，会有一个 Http 的 Upgrade 请求发送到服务器，在取得服务器响应后，建立的连接会从 Http升级，从 Http协议转换为WebSocket协议。</p>
<p><strong>So:</strong></p>
<p>1、客户端发送 Http GET请求， upgrade
2、服务器响应给客户端 switching protocol。【Http => WebSocket】
3、可以进行 WebSocket 通信。</p>
<p>HTTP(协议)和WebSocket(协议)都位于OSI模型的应用层，因此依赖于第4层的TCP。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/376549b16d9944b38f4d3ea7c207e18a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<span id="user-content-tcp/udp">
<h2 data-id="heading-5">4. TCP协议和UDP协议</h2>
<p>TCP是面向连接的一种传输控制协议。TCP连接之后，客户端和服务器可以互相发送和接收消息，在客户端或者服务器没有主动断开之前，连接一直存在，故称为长连接。特点：连接有耗时，传输数据无大小限制，准确可靠，先发先至。</p>
<p>UDP是无连接的用户数据报协议，所谓的无连接就是在传输数据之前不需要交换信息，没有握手建立连接的过程，只需要直接将对应的数据发送到指定的地址和端口就行。故UDP的特点是不稳定，速度快，可广播，一般数据包限定64KB之内，先发未必先至。</p>
<span id="user-content-代理">
<h1 data-id="heading-6">代理(Proxy)</h1>
<h2 data-id="heading-7">http代理</h2>
<p>Bill 希望从 Jane 的Web服务器下载一个网页。Bill 不能直接连接到 Jane 的服务器，因为在他的网络上设置了防火墙。为了与该服务器通信，Bill 连接到其网络的 HTTP代理。他的网页浏览器与代理通信的方式与他直接连接 Jane的服务器的方式相同；也就是说，网页浏览器会发送一个标准的 HTTP请求头。HTTP代理连接到 Jane 的服务器，然后将 Jane 的服务器返回的任何数据传回 Bill。</p>
<p>现在一般的 web服务器 都作为代理服务器（例：nginx），同时解决了<a href="https://www.imyangyong.com/blog/2019/07/http/%E6%B5%8F%E8%A7%88%E5%99%A8%E8%B7%A8%E5%9F%9F/" target="_blank" rel="nofollow noopener noreferrer">浏览器的跨域</a>问题，这样前后端项目就可以不用部署到一台服务器，实现了前后端的分离。</p>
<h2 data-id="heading-8">Socks代理</h2>
<p>Bill 希望通过互联网与 Jane 沟通，但他们的网络之间存在一个<a href="https://zh.wikipedia.org/wiki/%E9%98%B2%E7%81%AB%E5%A2%99" target="_blank" rel="nofollow noopener noreferrer">防火墙</a>，Bill 不能直接与 Jane 沟通。所以，Bill 连接到他的网络上的 SOCKS代理，告知它他想要与 Jane 创建连接；SOCKS代理打开一个能穿过防火墙的连接，并促进 Bill 和 Jane 之间的通信。</p>
<p>Socks属于会话层一个代理协议，比Http更低的层次，所以如果Socks代理了网络请求，那么像 Http、webSocket 等应用层协议都会走Socks的代理路线。</p>
<p>Socks代理只是简单的传递数据包，而不必关心是何种协议，所以socks代理比其他应用层代理要快的多。</p>
<p>我们平时提到的ss(shadowsocks)/ssr(shadowsocks-R)，其实就是Socks5代理。</p>
<h2 data-id="heading-9">Socks代理与HTTP代理的对比</h2>
<p><em>SOCKS</em>工作在比<a href="https://zh.wikipedia.org/wiki/%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8" target="_blank" rel="nofollow noopener noreferrer">HTTP代理</a>更低的层次：SOCKS使用握手协议来通知代理软件其客户端试图进行的连接SOCKS，然后尽可能透明地进行操作，而常规代理可能会解释和重写报头（例如，使用另一种底层协议，例如<a href="https://zh.wikipedia.org/wiki/%E6%96%87%E4%BB%B6%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE" target="_blank" rel="nofollow noopener noreferrer">FTP</a>；然而，HTTP代理 只是将HTTP请求转发到所需的HTTP服务器）。虽然HTTP代理有不同的使用模式，<a href="https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE" target="_blank" rel="nofollow noopener noreferrer">CONNECT</a>方法允许转发TCP连接；然而，SOCKS代理还可以转发<a href="https://zh.wikipedia.org/wiki/%E7%94%A8%E6%88%B7%E6%95%B0%E6%8D%AE%E6%8A%A5%E5%8D%8F%E8%AE%AE" target="_blank" rel="nofollow noopener noreferrer">UDP</a>流量和<a href="https://zh.wikipedia.org/wiki/%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86" target="_blank" rel="nofollow noopener noreferrer">反向代理</a>，而HTTP代理不能。HTTP代理通常更了解HTTP协议，执行更高层次的过滤（虽然通常只用于GET和POST方法，而不用于CONNECT方法）。</p>
<h1 data-id="heading-10">容易混淆的关系</h1>
<ul>
<li>Http和WebSocket：两种不同的应用层协议，都是基于 TCP连接。</li>
<li>Socket和WebSocket：完全无关，前者套接字，后者协议。</li>
<li>Socket和Tcp：前者是为了可以直接调用后者的API，可以方便程序员直接使用**更底层协议（一般是TCP或UDP）**而存在的一个抽象层。</li>
<li>Socket和Socks：完全无关，前者是套接字，后者是代理协议。</li>
</ul>
<h1 data-id="heading-11">参考</h1>
<ol>
<li><a href="https://zh.wikipedia.org/wiki/SOCKS" target="_blank" rel="nofollow noopener noreferrer">SOCKS</a> by wikipedia</li>
<li><a href="https://zh.wikipedia.org/wiki/%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8" target="_blank" rel="nofollow noopener noreferrer">Http代理服务器</a> by wikipedia</li>
<li><a href="https://juejin.cn/post/6945276190965891108#https://www.jianshu.com/p/34b06c7008b5" target="_blank" rel="nofollow noopener noreferrer">网络协议——Http、Socket、WebSocket</a></li>
<li><a href="https://juejin.cn/post/6945276190965891108#https://www.jianshu.com/p/42260a2575f8" target="_blank" rel="nofollow noopener noreferrer">1小时教你理解HTTP，TCP，UDP，Socket，WebSocket</a></li>
<li><a href="https://blog.csdn.net/qq_36119192/article/details/83825685" target="_blank" rel="nofollow noopener noreferrer">Socket套接字、Socks协议和Socks代理</a></li>
<li><a href="https://deeponion.org/community/threads/vpnss-ssr.901/" target="_blank" rel="nofollow noopener noreferrer">Vpn与ss/ssr的区别</a></li>
<li><a href="https://juejin.cn/post/6945276190965891108#https://blog.csdn.net/qq_35181209/article/details/75212533" target="_blank" rel="nofollow noopener noreferrer">TCP/IP、Http、Socket的关系理解</a></li>
<li><a href="https://juejin.cn/post/6945276190965891108#https://www.jianshu.com/p/bae7ea3e9adb" target="_blank" rel="nofollow noopener noreferrer">WebSocket 的连接建立过程</a></li>
<li><a href="https://juejin.cn/post/6945276190965891108#https://www.jianshu.com/p/30744fbd1f01" target="_blank" rel="nofollow noopener noreferrer">怎么理解HTTP协议是无状态的无连接的的协议？</a></li>
</ol></span></span></span></span></span></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            