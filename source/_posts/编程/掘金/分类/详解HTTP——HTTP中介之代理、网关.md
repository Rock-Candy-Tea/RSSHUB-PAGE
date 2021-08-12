
---
title: '详解HTTP——HTTP中介之代理、网关'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53b373cb51064ef6b5bcc53a68d0ce65~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 00:16:16 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53b373cb51064ef6b5bcc53a68d0ce65~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">HTTP中介之代理</h2>
<h3 data-id="heading-1">HTTP 代理存在两种形式</h3>
<p>第一种是 <a href="https://link.juejin.cn/?target=http%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc7230" target="_blank" rel="nofollow noopener noreferrer" title="http://tools.ietf.org/html/rfc7230" ref="nofollow noopener noreferrer">RFC 7230 - HTTP/1.1: Message Syntax and Routing</a>（即修订后的 RFC 2616，HTTP/1.1 协议的第一部分）描述的普通代理。<strong>这种代理扮演的是「中间人」角色</strong>，对于连接到它的客户端来说，它是服务端；对于要连接的服务端来说，它是客户端。<strong>它就负责在两端之间来回传送 HTTP 报文。</strong></p>
<p>第二种是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Fdraft-luotonen-web-proxy-tunneling-01" target="_blank" rel="nofollow noopener noreferrer" title="https://tools.ietf.org/html/draft-luotonen-web-proxy-tunneling-01" ref="nofollow noopener noreferrer">Tunneling TCP based protocols through Web proxy servers</a>（通过 Web 代理服务器用隧道方式传输基于 TCP 的协议）描述的隧道代理。<strong>它通过 HTTP 协议正文部分（Body）完成通讯，以 HTTP 的方式实现任意基于 TCP 的应用层协议代理。这种代理使用 HTTP 的 CONNECT 方法建立连接，</strong> 但 CONNECT 最开始并不是 RFC 2616 - HTTP/1.1 的一部分，直到 2014 年发布的 HTTP/1.1 修订版中，才增加了对 CONNECT 及隧道代理的描述，详见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc7231%23section-4.3.6" target="_blank" rel="nofollow noopener noreferrer" title="https://tools.ietf.org/html/rfc7231#section-4.3.6" ref="nofollow noopener noreferrer">RFC 7231 - HTTP/1.1: Semantics and Content</a>。实际上这种代理早就被广泛实现。</p>
<h3 data-id="heading-2">普通代理</h3>
<p>第一种 Web 代理原理特别简单：</p>
<blockquote>
<p>HTTP 客户端向代理发送请求报文，代理服务器需要正确地处理请求和连接（例如正确处理 Connection: keep-alive），同时向服务器发送请求，并将收到的响应转发给客户端。</p>
</blockquote>
<h3 data-id="heading-3">隧道代理</h3>
<p>第二种 Web 代理的原理也很简单：</p>
<blockquote>
<p>HTTP 客户端通过 CONNECT 方法请求隧道代理创建一条到达任意目的服务器和端口的 TCP 连接，并对客户端和服务器之间的后继数据进行盲转发。</p>
</blockquote>
<p>以上引用 Jerry Qu的文章<a href="https://link.juejin.cn/?target=https%3A%2F%2Fimququ.com%2Fpost%2Fweb-proxy.html" target="_blank" rel="nofollow noopener noreferrer" title="https://imququ.com/post/web-proxy.html" ref="nofollow noopener noreferrer">imququ.com/post/web-pr…</a></p>
<h3 data-id="heading-4">HTTP 代理的作用</h3>
<ol>
<li>抓包</li>
<li>FQ**</li>
</ol>
<p>虽然用的最多是vpn，但是vpn和代理不一样，对于构建VPN来说，隧道技术用来在IP公网中仿真条点到点的通路，实现两个节点间（VPN网关之间，或VPN网关与VPN远程用户之间）的安全通信，使数据包在公共网络上的专用隧道内传输。
封装是构建隧道的基本手段。从隧道的两端来看，封装就是用来创建、维持和撤销一个隧道，来实现信息的隐蔽和抽象。而如果流经隧道的数据不加密，那么整个隧道就暴露在公共网络中，虚拟专用网络的安全性和私有性就得不到体现。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53b373cb51064ef6b5bcc53a68d0ce65~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3.匿名访问</p>
<p>经常听新闻，说”某某某“在网络上发布帖子，被跨省追缉了。 假如他使用匿名的代理服务器，就不容易暴露自己的身份了。</p>
<p>http代理服务器的匿名性是指： HTTP代理服务器通过删除HTTP报文中的身份特性（比如客户端的IP地址， 或cookie,或URI的会话ID）， 从而对远端服务器隐藏原始用户的IP地址以及其他细节。 同时HTTP代理服务器上也不会记录原始用户访问记录的log(否则也会被查到)。</p>
<p>4.儿童过滤器
很多教育机构， 会利用过滤器代理来阻止学生访问成人内容。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd4dad16689d4e80a9c104f16e09460f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">HTTP代理优点</h3>
<p>1、<strong>突破自身IP访问限制，访问国外站点</strong>。如：教育网、169网等网络用户可以通过代理访问国外网站。 </p>
<p>2、<strong>访问一些单位或团体内部资源</strong>，如某大学FTP(前提是该代理地址在该资源的允许访问范围之内)，使用教育网内地址段免费。代理服务器，就可以用于对教育网开放的各类FTP下载上传，以及各类资料查询共享等服务。 </p>
<p>3、<strong>突破中国电信的IP封锁</strong>：中国电信用户有很多网站是被限制访问的，这种限制是人为的，不同Serve对地址的封锁是不同的，所以不能访问时可以换一个国外的代理服务器试试。 </p>
<p>4、<strong>提高访问速度</strong>：通常代理服务器都设置一个较大的硬盘缓冲区，当有外界的信息通过时，同时也将其保存到缓冲区中，当其他用户再访问相同的信息时，则直接由缓冲区中取出信息，传给用户，以提高访问速度。 </p>
<p>5、<strong>隐藏真实IP</strong>：上网者也可以通过这种方法隐藏自己的IP，免受攻击。</p>
<h2 data-id="heading-6">HTTP中介之网关</h2>
<ul>
<li>网关可以作为某种翻译使用，它抽象出了一种能够到达资源的方法，网关是资源和应用程序之间的粘合剂</li>
<li>网关扮演的是“协议转换器”的角色</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1146fa6892649b4850eb77436ad7643~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>网关可以向数据库发送查询数据，发邮件，生成动态内容，像一个门一样，进入一个请求，出来一个响应</p>
<h3 data-id="heading-7">WEB网关</h3>
<ul>
<li>Web网关在一侧使用HTTP协议，在另一侧使用另一种协议</li>
</ul>
<p>客户端协议 / 服务器端协议</p>
<ol>
<li>(HTTP/)服务器端网关：通过HTTP协议与客户端对话，通过其他协议与服务器通信</li>
<li>(/HTTP)客户端网关：通过其他协议与客户端对话，通过HTTP协议与服务器通信</li>
</ol>
<h3 data-id="heading-8">常见的网关类型</h3>
<ul>
<li>(HTTP/*) 服务器端Web网关</li>
</ul>
<p>请求流入原始服务器时，服务器端Web网关会将客户端HTTP请求转换为其他协议与服务器进行连接，完成获取资源以后，会将对象放在一条http响应中发送给客户端</p>
<ul>
<li>(HTTP/HTTPS) 服务器端安全网关</li>
</ul>
<p>一个组织可以通过网关对所有的输入Web请求加密，以提供额外的隐私和安全性保护。客户端可以用普通的HTTP浏览Web内容，但网关会自动加密对话。</p>
<ul>
<li>(HTTPS/HTTP) 客户端安全加速器网关</li>
</ul>
<p>将HTTPS/HTTP 网关作为安全加速器使用的情况越来越多了，这些 HTTPS/HTTP 网关位于Web服务器之前，通常作为不可见的拦截网关或反向代理使用。它们接收安全的 HTTPS 流量，对安全流量进行解密，并向 Web服务器发送普通的HTTP请求。这些网关中通常都包含专用的解密硬件，以比原始服务器有效的多的方式来解密安全流量，以减轻原始服务器的负荷。这些网关在网关和原始服务器之间发送的是未加密的流量。所以，要谨慎使用，确保网关和原始服务器之间的网络是安全的。</p>
<ul>
<li>资源网关</li>
</ul>
<p>最常见的网关，应用程序服务器，会将目标服务器与网关结合在一个服务器中实现。应用程序服务器是服务器端网关，与客户端通过HTTP进行通信，并与服务器端的应用程序相连。客户端是通过HTTP连接到应用程序服务器的。但应用程序服务器并没有回送文件，而是将请求通过一个网关应用编程接口(Application Programming Interface，API)发送给运行在服务器上的应用程序。</p></div>  
</div>
            