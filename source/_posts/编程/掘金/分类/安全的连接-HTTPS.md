
---
title: '安全的连接-HTTPS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7208'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 02:02:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=7208'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">起源：为什么我们需要 HTTPS</h2>
<h3 data-id="heading-1">HTTP: 双刃剑</h3>
<ul>
<li><strong>简单灵活（优点）</strong></li>
</ul>
<p>想想我们平时开发时看到的 Request ，是不是觉得很简单：Header + Body，然后再分一次 Request 和 Response，甚至还是明文传输，这就是 HTTP 协议的全部了，甚至 Header 字段也没有规定死，随时可以提供给开发者自行扩展并解释。（我们请求时常带在 Header 里的 token 字段就是灵活扩展的最好例子）当然这种可靠性也体现在 HTTP 协议其实不关心下层协议是什么，在任何条件下只要你保证上层 HTTP 协议的语义稳定，理论上通过任何下层协议传输都是没问题的。</p>
<ul>
<li><strong>广泛应用 （优点）</strong></li>
</ul>
<p>随着互联网的发展，各种软硬件设施的成熟，网络速度加快，HTTP 变得无处不在，当我们打开抖音时，我们在使用 HTTP ，当我们刷 B 站时，我们在使用 HTTP，当我们开始一局荣耀时，HTTP 也在背后运作着，HTTP 可以说是无处不在。
 </p>
<ul>
<li><strong>无状态 （优点/缺点）</strong></li>
</ul>
<p>首先我们应当知道什么叫做有状态的协议：在大多数的网络协议中，比如邮件通常使用的 SMTP 协议，其都需要经过经过一系列的握手(HELO → AUTH ）才能一步一步的往下进行 SEND 和 QUIT ，其本质意义上就是一个状态机，通信的双方都需要明确的知道当前连接的状态，且之前命令传输的数据也要清楚，这些都会对后续的请求有影响。这种协议便是有状态的协议，而我们的 HTTP （严格意义上讲 HTTP 1.x），它的每个请求都是完全独立的，每个请求包含了处理这个请求所需的完整的数据，发送请求不涉及到状态变更。即使在HTTP/1.1上，同一个连接允许传输多个HTTP请求的情况下，如果第一个请求出错了，后面的请求一般也能够继续处理。这样的无状态，让服务器根本不需要关注额外的状态信息，也就是变相的说，其减轻了服务器的压力，而且得益于此，让任何其他的机器处理 HTTP 请求实际上都是没有区别的，我们可以简单地通过负载均衡和堆机器实现高并发。然而这样做其实也会带来额外的负担，比如我们的后台管理页面，如果没有用户的状态维护，我们根本无法将用户的操作串联起来。所以才有了 cookie 和 token Header 的j解决方案。</p>
<ul>
<li><strong>明文传输和不安全（优点/缺点）</strong></li>
</ul>
<p>与 TCP 和 UDP 这一类的二进制传输协议不同，HTTP 协议的报文也就是 HEADER 部分全部都是简单可阅读的文本格式，其给我们带来了开发的便利的同时，也增加了不安全性，因为无状态的缘故，HTTP 协议也无法进行身份认证和完整性校验，任何人都有可能在请求的中间进行劫持、篡改你的请求，保存你的用户信息，用做他用。</p>
<p>通过梳理 HTTP 协议的优缺点，我们可以很快发现 HTTP 协议的安全实际上存在着极大地问题，任何人都有可能在任何网络环境下截取到你的请求（想一想我们用过的 charles 抓包），并进行篡改，这在很多对安全性要求高的线上场景：电商、银行是完全不能接受的，于是 HTTPS 应运而生。</p>
<h2 data-id="heading-2">安全：HTTPS</h2>
<h3 data-id="heading-3">什么是安全</h3>
<p>我们需要知道，只有当一个传输协议拥有如下的几个特征时，他才是安全的：</p>
<p>机密性：用户之间的通讯必须能保证无法被中间人获取到具体细节，这里我们可以回想一下老套抗战剧里常有的谍战情节，间谍截取了电报，但是没有密码本，只能眼睁睁的看着信息正常传递，这种信息就是具有机密性的。</p>
<p>完整性：用户之间的通讯必须能验证消息是否被完整没有被篡改，这个我们可以用一些无良媒体的报道来举例，因为读者无法验证消息的完整性，所以只能看到媒体公布的部分消息，于是被引导产生了完全错误的认知和看法，这种报道就是不具备完整性的。</p>
<p>身份认证：用户之间通讯时必须明确通讯的对象是否是真的对方还是有人顶替，这个地方我们还是可以用老套抗战剧来讲一讲，把剧情推进到密码本被间谍拿到手上，破解了电报传讯甚至伪造了假消息发出，这造成的后果大家可想而知。</p>
<p>不可否定：用户之间的通讯必须保证每一次交流都是不可否定的，不应出现发出了数据接受方却否认接收到信息的情况。</p>
<h3 data-id="heading-4">HTTPS 和 HTTP 有什么区别？</h3>
<p>HTTP 和 HTTP 其实在顶层协议上没有任何区别，其继承了 HTTP 的所有优势，并得益于 SSL/TLS 的出现，改善了其安全性，仅仅改动协议名为：HTTPS (HTTP + SSL/TLS)，并将默认端口号改为了 443。其简易的协议分层示意图如下：</p>
<p>可以看到，HTTPS 不再直接通过 TCP/IP 调用 Socket API 进行报文的传输，而是通过专门的安全接口进行传输。</p>
<h3 data-id="heading-5">什么是 SSL/TLS</h3>
<p>SSL 是安全套接层，经过多年的发展后被改名为 TLS（传输层安全，Transport Layer Security），其由几个不同的子协议组成：</p>
<ul>
<li><strong>记录协议</strong>：发送所有的子协议</li>
<li><strong>握手协议</strong>：浏览器和服务端交换密码套件、tls版本号、随机数等后续加密需要的信息</li>
<li><strong>警告协议</strong>：当用户的协议版本或者证书有问题时发出警告</li>
<li><strong>变更密码规范协议</strong>: 告知对方接下来的请求将由之前交换的信息进行加密后发送</li>
<li><strong>扩展协议</strong>: 通过该协议扩展 TLS </li>
</ul>
<h3 data-id="heading-6">SSL/TLS 如何保证了安全性？</h3>
<h4 data-id="heading-7">TLS1.2 如何建立连接</h4>
<p>其中的关键节点为：</p>
<ul>
<li><strong>ClientHello</strong>: 通知服务端即将开始连接，传递客户端生成的随机数 CR ，TLS 版本号和其支持的密码套件（密钥交换算法 + 签名算法 + 对称加密算法 + 摘要算法）还有扩展列表，让服务端进行选择。</li>
</ul>
<pre><code class="copyable">Handshake Protocol: Client Hello
    Version: TLS 1.2 (0x0303)
    Random: 1cbf803321fd2623408dfe…
    Cipher Suites (17 suites)
        Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)
        Cipher Suite: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>ServerHello</strong>: 服务端检测 TLS 版本号，如果支持则选择合适的密码套件, 生成一个 服务端的 Server Random 并根据选择密码套件决定是否需要传输额外的 Server Params (通过 Server Key Exchange)，以及其使用的证书，方便服务端进行校验和下面的加密通信（注意：这里会交换服务端的公钥到客户端）。</li>
</ul>
<pre><code class="copyable">Handshake Protocol: Server Hello
    Version: TLS 1.2 (0x0303)
    Random: 0e6320f21bae50842e96…
    Cipher Suite: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">Handshake Protocol: Server Key Exchange
    EC Diffie-Hellman Server Params
        Curve Type: named_curve (0x03)
        Named Curve: x25519 (0x001d)
        Pubkey: 3b39deaf00217894e...
        Signature Algorithm: rsa_pkcs1_sha512 (0x0601)
        Signature: 37141adac38ea4...
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>ClientKeyExchange</strong>: 当接收到服务端的证书后，客户端会向上一层一层的查找，直到查找到系统或浏览器内置的根证书（Charles 之所以能抓取 HTTPS 请求也因为其提供了一个根证书让你内置到系统或浏览器中），确认了其是安全的之后才会开始连接并交换一个通过密钥交换算法加密的 Client Params （在不同的对称加密算法下其不同）。因为此时双方都共享 Client Params / Server Params / ClientRandom , 于是其直接根据 Client Params 和 Server Params  算出 Pre-Master（非 RSA）。这之后双方都会以 Server Random、Client Random、Pre-Master 为基础，计算出真正的主密钥和会话密钥。</li>
</ul>
<pre><code class="copyable">Handshake Protocol: Client Key Exchange
    EC Diffie-Hellman Client Params
        Pubkey: 8c674d0e08dc27b5eaa…// 如果这里是 RSA 算法，其直接交换 Pre-Master
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><strong>ClientChangeCipherSpec</strong>: 当主密钥、会话密钥就位之后，客户端会通知服务端之后的消息将全部用协定的加密算法加上会话密钥来加密，并把之前所有的传递的消息通过摘要算法计算后带在请求里发给服务端，让服务端验证是否是之前的客户端在发送消息，并且加密是否正确（完整性、机密性、身份认证）。</p>
</li>
<li>
<p><strong>ServerChangeCipher</strong>：当接收到消息，服务端验证完消息后，服务端也会把之前的消息像客户端一样进行计算并传递，双方验证通过之后，握手完毕开始通信。</p>
</li>
</ul>
<p>看起来 TLS1.2 通过三次随机数的混合再加密已经很好地解决了安全性的问题，那么问题来了，他好用吗？答案当然是否定的：一次 TLS1.2 的握手需要两次消息（2-RTT）的往返，都快要赶上 TCP/IP 了，其会带来额外的连接时长，当网络环境变差的时候这种情况会更甚。</p>
<h3 data-id="heading-8">更好的 TLS</h3>
<p>为了解决 TLS 中某些算法的安全问题，在新版本的 TLS 中，不安全的加密套件被移除，并为了更好的兼容性，升级到新版本的 TLS 使用了扩展协议来存放升级的信息，且为了减少握手流程，其把密码套件和密码套件对应的 params 在第一次 Hello 就全部带给了服务端，服务端接收到的时候选择好密码套件的同时就已经获取了ClientParams，完全移除了 Client 的 KeyExchange 步骤，每次握手只会有一次消息往返 （1-RTT）。具体流程可以参考下图：</p>
<h2 data-id="heading-9">结语</h2>
<p>回到如今，现在 HTTPS 的 TLS1.3 都已经是 2018 年的事情了，伴随着网络的发展，用户需求的增加，大家对网络的要求也越来越高，虽然TLS1.3 已经做得相当好了，但是他始终还是基于 HTTP 1.x，继承了 HTTP 1.x 优势的同时，也继承了 HTTP 1.x 的一些劣势，比如报文信息过大，比如队头阻塞，于是有了 HTTP/2 。而 HTTP/2 还是没有解决 TCP 的队头阻塞，于是又有了 QUIC。协议只会无尽的更新迭代，但是选用与否，还是需要大家：具体需求具体分析。新协议虽好，切莫贪杯。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            