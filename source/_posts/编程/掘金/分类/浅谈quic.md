
---
title: '浅谈quic'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e41fd25a3c2242bfaf58b918326e4645~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 04:40:07 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e41fd25a3c2242bfaf58b918326e4645~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">简介与现状</h1>
<p>quic全称quickudpinternet connection，它的发音与英语单词“quick”相同。它的出现从根本上理解是为了更快的将数据进行交付，降低数据流往返的网络耗时（RTT）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e41fd25a3c2242bfaf58b918326e4645~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>udp是面向无连接的传输层协议，quic底层依赖udp实现端对端之间的连接，这样的好处是在网络传输层无需对数据包进行确认，但存在的问题就是为了确保数据传输的可靠性，应用层协议需要自己完成包传输情况的确认。</p>
<h3 data-id="heading-1">udp与tcp</h3>
<p>由于quic是基于udp的，所以需要看看udp与tcp的区别，从而了解到quic需要进行的实现。下面简述udp与tcp之间的几点区别，想了解更详细的看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F24860273" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/24860273" ref="nofollow noopener noreferrer">这个</a> 。</p>
<ul>
<li>
<p>tcp是面向连接的，udp是面向无连接的；</p>
</li>
<li>
<p>tcp是面向字节流的，udp是面向数据报的；</p>
</li>
<li>
<p>tcp传输的字节流是严格顺序性的，udp却是无序的</p>
</li>
<li>
<p>tcp会保证传输数据的可靠性，所谓可靠性是无差错、不丢失、不重复、顺序性</p>
</li>
</ul>
<h3 data-id="heading-2">RTT现状</h3>
<p>现在在用的https协议通常来说需要经历tcp连接、tsl/ssl连接、http数据交换这几个过程，时间消耗会有1.5RTT + 1.5RTT + 1RTT = 4RTT，4RTT在端和端之间的距离特别远的情况下，耗时是特别严重的。这还只是一个连接产生到数据交换的耗时，我们的网页渲染出来通常会有多个连接的，js、css、html这些数据通常都会产生连接，就算http2的情况下也必不可免，因为http2也只是复用每一种类型的第一个tcp和ssl连接，每一种类型大概可以降低1.5RTT。
可以说降低RTT的奋斗史是互联网通信的发展史上重大一笔了。</p>
<h1 data-id="heading-3">tcp问题</h1>
<p>在端之间的连接上http2发展方向算是复用连接，的确是降低了RTT，很大程度上改善了性能，这在我们的实践中已经体验过了。但是这并不能解决tcp协议现有的一些缺陷：队头阻塞、协议僵化以及协议本身有的弱点面向连接。</p>
<h3 data-id="heading-4"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F330300133" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/330300133" ref="nofollow noopener noreferrer"><strong>队头阻塞</strong></a></h3>
<p>可能由于多种原因产生，为了保证数据的可靠性，端之间建立连接之后，数据传输到对端是有顺序的，当某一个数据包过大，后面的数据都需要等待这一条传输成功应用层才能组装成完整的数据，也可能某一个数据包在传输的过程中丢失或者网络中断这个丢失的数据包需要重新传输才能继续后面步骤。如果http2在出现丢包率很高的网络状态下，它的性能表现可能还不如http1.x。</p>
<h3 data-id="heading-5"><strong>协议僵化</strong></h3>
<p>tcp协议的实现依赖于操作系统、中间设备各方的因素，恰巧这些因素经过这么多年的发展都出现了不同的弊端。
这些中间设备包括了防火墙、网关、路由器、交换机等等，它们各自的作用虽然都不同，在整个网络过程中起着不小的作用。通常依赖一些很少升级的软件，这些软件使用了大量的TCP特性，设置之后便很少进行更新，甚至有些形成了约定性的规则。tcp协议更新之后，但是这些设备仍然不更新，那么就会出现对于不理解的数据从而丢弃掉。
TCP协议都是通过操作系统内核来实现的，应用程序只能使用不能修改。在我们平常使用体验中也能知道操作系统的更新要过很久才会有一次，有些时候即使有新的操作系统出现，设备上也可能并不会去更新操作系统，比如windows xp应该还有不少的用户。</p>
<h1 data-id="heading-6">quic出现</h1>
<p>tcp的那些缺陷也促使了新的协议产生，毕竟tcp这条路也从1975年走到了现在，udp也是传输层的重要协议。提起udp我们通常会想起它的不靠谱，但是它很快，既有缺点也有优点，下面这个图就表示出了在建立连接传输数据中tcp和quic为基础的应用耗时。quic建立连接通常需要1RTT，更短的只需要0RTT。在目前tcp协议发展来看，个人感觉它出现的最主要原因应该是为了解决队头阻塞的问题。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baef2fe6253343bfb90447057441c95e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">建立连接</h2>
<p>从上面两张图可以看到quic集合了tcp和ssl/tsl各种功能，但是它连接耗时却是那么短，还是挺强的。quic的连接基于Diffie-Hellman的加密算法，</p>
<ol>
<li>
<p>首次连接时，客户端发送 Inchoate Client Hello 给服务端，用于请求连接；</p>
</li>
<li>
<p>服务端生成 g、p、a，根据 g、p 和 a 算出 A，然后将 g、p、A 放到 Server Config 中再发送 Rejection 消息给客户端；</p>
</li>
<li>
<p>客户端接收到 g、p、A 后，自己再生成 b，根据 g、p、b 算出 B，根据 A、p、b 算出初始密钥 K。B 和 K 算好后，客户端会用 K 加密 HTTP 数据，连同 B 一起发送给服务端；</p>
</li>
<li>
<p>服务端接收到 B 后，根据 a、p、B 生成与客户端同样的密钥，再用这密钥解密收到的 HTTP 数据。为了进一步的安全（前向安全性），服务端会更新自己的随机数 a 和公钥，再生成新的密钥 S，然后把公钥通过 Server Hello 发送给客户端。连同 Server Hello 消息，还有 HTTP 返回数据；</p>
</li>
<li>
<p>客户端收到 Server Hello 后，生成与服务端一致的新密钥 S，后面的传输都使用 S 加密。</p>
</li>
</ol>
<p>QUIC从请求连接到正式接发 HTTP 数据一共花了 1RTT，这 1 个 RTT 主要是为了获取 Server Config，后面的连接如果客户端缓存了 Server Config，那么就可以直接发送 HTTP 数据，实现 0 RTT 建立连接。</p>
<h2 data-id="heading-8">流量控制</h2>
<p>流量控制控制的是端之间的流量，需要考虑接收方的数据承受能力。流量控制通常是控制发送方的速度，如果发送方速度过快导致接收方处理不过来会造成数据溢出从而丢包。tcp的流量控制是通过控制接收方窗口大小来接收数据，从而通知发送方接收方的情况调整发送窗口。tcp的流量控制收到已确认字节数影响，如果某一个数据包丢失，后面再接收到更大的序号包，在没有重传这个数据包的情况下不会再接收移动窗口。
Quic的流量控制分两个级别： <strong>stream级别</strong> 和 <strong>connection级别</strong> ，stream级别可以理解成http连接，connect级别可以类比到tcp层的连接，同一条connect级别连接可以承载多个stream级别的连接。quic同样也有接收窗口和发送窗口，接收窗口的移动只取决于接收到的最大偏移字节数。
Stream 级别中，接收窗口= 最大接收窗口 - 已接收数据，而对 Connection 来说：接收窗口 = Stream1 接收窗口 + Stream2 接收窗口 + ... + StreamN 接收窗口 。
quic实现流量控制的基本原理主要有两点：1、通过 window_update 帧告诉对端自己可以接收的字节数，这样发送方就不会发送超过这个数量的数据；2、通过 block帧告诉对端由于流量控制被阻塞了，无法发送数据。</p>
<h2 data-id="heading-9">拥塞控制</h2>
<p>拥塞控制是用于控制网络之间数据流量的，也就是考虑网络资源的承受能力，避免过多数据涌入网络，导致网络过载。quic的拥塞控制默认使用了tcp的cubic拥塞算法，但是它在一些方面做了改进。下面介绍几个改进点，其他改进想要了解可以翻阅资料。
<strong>支持热插拔</strong> ：quic协议在应用层实现了拥塞控制，不再像tcp依赖于操作系统和硬件层，可以根据不同的网络环境，支持动态的选择拥塞控制算法，单个应用程序的不同连接也能支持配置不同的拥塞控制，应用程序不需要停机和升级就能实现拥塞控制的变更，我们在服务端只需要修改一下配置，reload 一下，完全不需要停止服务就能实现拥塞控制的切换。
<strong>单调递增的 Packet Number</strong> ：tcp为了保证包顺序性，在出现丢包重传的情况下，计算RTO的时候容易产生歧义。quic协议采用递增的 <strong>packet number</strong> ，在出现丢包的情况下，不会要求重传的报继续用之前的序号，而是大于之前的packet number。当然quic用了 <strong>stream offset</strong> 来保证数据的顺序性和可靠性。一个 Stream 可以经过多个 Packet 传输，Packet Number 严格递增，没有依赖。但是 Packet 里的 Payload 如果是 Stream 的话，就需要依靠 Stream 的 Offset 来保证应用数据的顺序。
<strong>更多的</strong> <strong>ack</strong> <strong>块</strong> ：TCP的 Sack 选项能够告诉发送方已经接收到的连续 Segment 的范围，但是 Tcp Sack Option 最大只能提供 3 个 Block，QuicAck Frame 可以同时提供 256 个 Ack Block，在丢包率比较高的网络下，更多的 Sack Block 可以提升网络的恢复速度，减少重传量。</p>
<h2 data-id="heading-10">多路复用</h2>
<p>quic和http2一样支持多路复用，但是它有一个很大的改进： <strong>没有队头阻塞的多路复用</strong> 。正如前面介绍的quic的连接有connect和stream两个层级的连接，一个connect中的多个stream连接是相互独立的，stream传输的基本单元是packet，某一条stream上packet过大或者丢失只会影响到这一条stream，其他的stream连接仍然可以正常传输。</p>
<h2 data-id="heading-11">连接迁移</h2>
<p>QUIC连接是两个QUIC端点之间的单次会话（conversation）过程，每个连接过程都有一组连接标识符，或称连接ID(64位)，该ID用以识别该连接。每个端点各自选择连接ID。每个端点选择对方使用的连接ID。连接ID的基本功能是确保底层协议（UDP、IP及其底层协议）的寻址变更不会使QUIC连接传输数据到错误的端点。
这个特性说明了出现从流量切换到wifi这种操作，只要 ID 不变，这条连接依然维持着，上层业务逻辑感知不到变化，不会中断，也就不需要重连。</p>
<h1 data-id="heading-12">总结</h1>
<p>quic相对于tcp来说，进行了很多的改进，也丢掉了它各种原因带来的包袱，借鉴tcp、ssl/tsl、http2的各种经验，基于ucp实现高效可靠的通信协议。不过对于它也存在很多非议，比如：目前网络环境对于udp不太友好，某一些udp端口可能永远都不通；quic不依赖于操作系统在应用层就实现了，但是会造成操作系统内核态和用户态的切换以及其他的性能开销，导致对于cpu性能消耗有点高等等，具体可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwgrape.github.io%2F2018%2F12%2F09%2FQUIC%25E5%2592%258CHTTP-3-%25E5%25A4%25AA%25E5%25A4%25A7%25E8%2580%258C%25E4%25B8%258D%25E8%2583%25BD%25E5%25A4%25B1%25E8%25B4%25A5%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://wgrape.github.io/2018/12/09/QUIC%E5%92%8CHTTP-3-%E5%A4%AA%E5%A4%A7%E8%80%8C%E4%B8%8D%E8%83%BD%E5%A4%B1%E8%B4%A5/" ref="nofollow noopener noreferrer">QUIC和HTTP/3：大而不倒?!(译文)</a> 了解到。</p>
<p><strong>参考文献</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.kancloud.cn%2Fkancloud%2Fhttp3-explained%2F1395002" target="_blank" rel="nofollow noopener noreferrer" title="https://www.kancloud.cn/kancloud/http3-explained/1395002" ref="nofollow noopener noreferrer">http3详解</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.infoq.cn%2Farticle%2Fquic-google-protocol-web-platform-from-tcp-to-udp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.infoq.cn/article/quic-google-protocol-web-platform-from-tcp-to-udp" ref="nofollow noopener noreferrer">从 TCP 到 UDP 的 Web 平台</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_41648631%2Farticle%2Fdetails%2F104357260" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_41648631/article/details/104357260" ref="nofollow noopener noreferrer">quic详解</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F143464334" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/143464334" ref="nofollow noopener noreferrer">http3原理实战</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F302412059" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/302412059" ref="nofollow noopener noreferrer">如何看待 HTTP/3</a></p></div>  
</div>
            