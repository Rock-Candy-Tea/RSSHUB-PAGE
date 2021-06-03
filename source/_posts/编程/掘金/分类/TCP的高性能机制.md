
---
title: 'TCP的高性能机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/623df20d5d18416c99ce393d9dedf9cb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 23:46:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/623df20d5d18416c99ce393d9dedf9cb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>之前介绍了 TCP 的报文格式（《TCP 协议基本特性》），TCP 的连接管理，学习了 TCP 如何建立连接，释放连接以及一些网络安装方面的问题，现在还剩下 TCP 的几个关键机制，主要是 TPC 的延迟应答和捎带应答、超......</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/623df20d5d18416c99ce393d9dedf9cb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>之前介绍了 TCP 的报文格式（<a href="https://zouchanglin.cn/2019/11/21/3947143266.html" target="_blank" rel="nofollow noopener noreferrer">《TCP 协议基本特性》</a>），TCP 的连接管理，学习了 TCP 如何建立连接，释放连接以及一些网络安装方面的问题，现在还剩下 TCP 的几个关键机制，主要是 TPC 的延迟应答和捎带应答、超时重传、快重传和快恢复、滑动窗口机制、拥塞避免算法；然后最后还记录了 TCP 的粘包问题和解决方案！</p>
<p>TCP 实现的可靠传输其实依赖于确认应答机制，也就是接收方每次接收完数据之后会回发一个 ack 确认号，代表自己下次期望收到的序号，意思是告诉发送者, 我已经收到了哪些数据; 下一次你从哪里开始发。 TCP 数据包中的序列号（Sequence Number）不是以报文段来进行编号的，而是将连接生存周期内传输的所有数据当作一个字节流，序列号就是整个字节 流中每个字节的编号。一个 TCP 数据包中包含多个字节流的数据（即数据段），而且每个 TCP 数据包中的数据大小不一定相同。在建立 TCP 连接的三次握手 过程中，通信双方各自已确定了初始的序号 x 和 y，TCP 每次传送的报文段中的序号字段值表示所要传送本报文中的第一个字节的序号。</p>
<h2 data-id="heading-0"><a href="https://juejin.cn/post/6969099827577782279#TCP%E7%9A%84%E7%A1%AE%E8%AE%A4%E5%BA%94%E7%AD%94" title="TCP的确认应答"></a>TCP 的确认应答</h2>
<p>TCP 提供的确认机制，可以在通信过程中可以不对每一个 TCP 数据包发出单独的确认包（Delayed ACK 机制），而是在传送数据时，顺便把确认信息传出， 这样可以大大提高网络的利用率和传输效率。同时，TCP 的确认机制，也可以一次确认多个数据报，例如，接收方收到了 201，301，401 的数据报，则只 需要对 401 的数据包进行确认即可，对 401 的数据包的确认也意味着 401 之前的所有数据包都已经确认，这就是延迟应答，这样也可以提高系统的效率。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ddd70993e21414e9528db8d06a5b4ed~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>再说说捎带应答，TCP 的确认应答和回执数据可以通过一个包发送。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9f959e8f13f4322ac9f2bccc857fd8d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1"><a href="https://juejin.cn/post/6969099827577782279#TCP%E7%9A%84%E8%B6%85%E6%97%B6%E9%87%8D%E4%BC%A0" title="TCP的超时重传"></a>TCP 的超时重传</h2>
<p>若发送方在规定时间内没有收到接收方的确认信息，就要将未被确认的数据包重新发送。接收方如果收到一个有差错的报文，则丢弃此报文，并不向发送方 发送确认信息。因此，TCP 报文的重传机制是由设置的超时定时器来决定的，在定时的时间内没有收到确认信息，则进行重传。这个定时的时间值的设定非常重要，太大会使包重传的延时比较大，太小则可能没有来得及收到对方的确认包发送方就再次重传，会使网络陷入无休止的重传过程中。接收方如果收到 了重复的报文，将会丢弃重复的报文，但是必须发回确认信息，否则对方会再次发送。</p>
<p>但是主机 A 未收到 B 发来的确认应答, 也可能是因为 ACK 丢失了；因此主机 B 会收到很多重复数据。那么 TCP 协议需要能够识别出那些包是重复的包,，并且把重复的丢弃掉。这时候我们可以利用前面提到的序列号, 就可以很容易做到去重的效果。</p>
<p>超时时间如何确定?</p>
<p>TCP 为了保证无论在任何环境下都能比较高性能的通信，因此会动态计算这个最大超时时间：Linux 中 (BSD Unix 和 Windows 也是如此)，超时以 500ms 为一个单位进行控制，每次判定超时重发的超时时间都是 500ms 的整数倍，如果重发一次之后，仍然得不到应答，等待 <code>2*500ms</code> 后再进行重传如果仍然得不到应答，等待 <code>4*500ms</code>进行重传。依次类推以指数形式递增，累计到一定的重传次数，TCP 认为网络或者对端主机出现异常，强制关闭连接</p>
<h2 data-id="heading-2"><a href="https://juejin.cn/post/6969099827577782279#TCP%E5%BF%AB%E9%80%9F%E9%87%8D%E4%BC%A0%EF%BC%88%E5%86%97%E4%BD%99ACK%EF%BC%89" title="TCP快速重传（冗余ACK）"></a>TCP 快速重传（冗余 ACK）</h2>
<p>有了超时重传机制为什么还出现了快速重传呢？其实这也是 TCP 为了效率的一种保障，每当比期望序号大的失序报文段到达时，发送一个冗余 ACK，指明下一个期待字节的序号。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cc15a95a2e345788e58f8ff28d1341f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>超时重传是底线，是功能性的，但是快重传是建立在超时重传上的，为了效率的提高</p>
<h2 data-id="heading-3"><a href="https://juejin.cn/post/6969099827577782279#TCP%E6%B5%81%E9%87%8F%E6%8E%A7%E5%88%B6" title="TCP流量控制"></a>TCP 流量控制</h2>
<p>接收端处理数据的速度是有限的。如果发送端发的太快，导致接收端的缓冲区被打满，这个时候如果发送端继续发送，就会造成丢包，继而引起丢包重传等等一系列连锁反应。因此 TCP 支持根据接收端的处理能力，来决定发送端的发送速度。这个机制就叫做流量控制 (Flow Control)；</p>
<p>在通信过程中，接收方根据自己接收缓存的大小，动态地调整发送方的发送窗口大小，即接收窗口 rwnd (接收方设置确认报文段的窗口字段来将 rwnd 通知给发送方)， 发送方的发送窗口取接收窗口 rwnd 和拥塞窗口 cwnd 的最小值。接收窗口也就是接收方的接收缓冲区，拥塞窗口简单来说就是网络堵塞了，那就是说明在这个网络中使用网络带宽的主机很多，或者占用了很多资源，导致发送缓慢，那么这就是一个网络拥塞的情况</p>
<p>TCP 首部中，专门有一个窗口大小的字段用来通知窗口大小。接收主机将自己可以接收的缓冲区大小放人这个字段中通知给发送端。这个字段的值越大，说明网络的吞吐量越高。不过，接收端的这个缓冲区一旦面临数据溢出时，窗口大小的值也会随之被设置为一个更小的值通知给发送端，从而控制数据发送量。也就是说，发送端主机会根据接收端主机的指示，对发送数据的量进行控制。这也就形成了一个完整的 TCP 流控制 (流量控制)。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fd0afa55e6f40c29ca976c67d97b546~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以看到，如果过了重发时间还没有收到窗口的更新通知，会发送一个探测报文去探测接收方的窗口。</p>
<p>滑动窗口虽然只能往右滑，但是可能变大，也可能变小，也可能是 0；收到第一个 ACK 后，滑动窗口向后移动，继续发送第五个段的数据，依次类推，操作系统内核为了维护这个滑动窗口，需要开辟发送缓冲区来记录当前还有哪些数据没有应答；只有确认应答过的数据，才能从缓冲区删掉；窗口越大，则网络的吞吐率就越高;</p>
<h2 data-id="heading-4"><a href="https://juejin.cn/post/6969099827577782279#TCP%E6%8B%A5%E5%A1%9E%E6%8E%A7%E5%88%B6" title="TCP拥塞控制"></a>TCP 拥塞控制</h2>
<p>因为网络上有很多的计算机，可能当前的网络状态就已经比较拥堵。在不清楚当前网络状态下，贸然发送大量的数据，是很有可能引起雪上加霜的。一般来说，计算机网络都处在一个共享的环境。因此也有可能会因为其他主机之间的通信使得网络拥堵。在网络出现拥堵时，如果突然发送一个较大量的数据，极有可能会导致整个网络的瘫痪看看 TCP 是如何解决这个问题的呢？</p>
<p>TCP 引入了慢启动机制：先发少量的数据，探探路，摸清当前的网络拥堵状态，再决定按照多大的速度传输数据；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/792275b8be3c4645a51636ef07892bae~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么慢启动和拥塞避免的算法如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/260c6c0d61854107a00bcf84f7fad3f5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>cwnd 指的是一个报文段（最大报文段长度 MSS），最开始发一个报文段然后呈指数式增长到 ssthresh 初始值，这就是慢启动，然后执行加法增大，也就是拥塞避免阶段，达到阈值的时候变会触发快重传，此时降到新的 ssthresh 值，即为拥塞时的一半，这就是快恢复策略！当 TCP 通信开始以后，网络吞吐量会逐渐上升，但是随着网络拥堵的发生吞吐量也会急速下降。于是会再次进人吞吐量慢慢上升的过程。因此所谓 TCP 的吞吐量的特点就好像是在逐步占领网络带宽的感觉。</p>
<h2 data-id="heading-5"><a href="https://juejin.cn/post/6969099827577782279#TCP%E7%B2%98%E5%8C%85%E9%97%AE%E9%A2%98" title="TCP粘包问题"></a>TCP 粘包问题</h2>
<p>首先要明确，粘包问题中的” 包” 是指的应用层的数据包。</p>
<p>在 TCP 的协议头中，没有如同 UDP 一样的” 报文长度” 这样的字段，但是有一个序号这样的字段。站在传输层的角度，TCP 是一个一个报文过来的，按照序号排好序放在缓冲区中。站在应用层的角度，看到的只是一串连续的字节数据，那么应用程序看到了这么一连串的字节数据，就不知道从哪个部分开始到哪个部分是一个完整的应用层数据包</p>
<p>那么如何避免粘包问题呢? 归根结底就是一句话，明确两个包之间的边界：</p>
<ul>
<li>对于定长的包，保证每次都按固定大小读取即可；例如对于一个结构体 struct，是固定大小的，那么就从缓冲区从头开始按 sizeof(struct) 依次读取即可；</li>
<li>对于变长的包，可以在包头的位置，约定一个包总长度的字段，从而就知道了包的结束位置；</li>
<li>对于变长的包，还可以在包和包之间使用明确的分隔符 (应用层协议，是程序猿自己来定的，只要保证分隔符不和正文冲突即可);</li>
</ul>
<p>对于 UDP 是否也存在” 粘包问题” 呢？对于 UDP，如果还没有上层交付数据，UDP 的报文长度仍然在。同时，UDP 是一个一个把数据交付给应用层，就有很明确的数据边界。站在应用层的角度，使用 UDP 的时候，要么收到完整的 UDP 报文，要么不收，不会出现” 半个” 的情况。</p></div>  
</div>
            