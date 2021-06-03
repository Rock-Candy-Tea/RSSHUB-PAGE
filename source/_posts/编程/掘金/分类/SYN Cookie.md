
---
title: 'SYN Cookie'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7355671ff3cf483a95c21bd90e23fd92~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 23:48:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7355671ff3cf483a95c21bd90e23fd92~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>SYN 泛洪攻击 SYN 攻击其实就是 Server 收到 Client 的 SYN，Server 向 Client 发送 SYN-ACK 之后未收到 Client 的 ACK 确认报文， 这样服务器就需要维护海量的半开连接 ，等待客户端的 ACK, 最终导致服务器资源耗尽 (sync queue 满) 而丢弃新的连接。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7355671ff3cf483a95c21bd90e23fd92~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0"><a href="https://juejin.cn/post/6969099827581812766#SYN%E6%B3%9B%E6%B4%AA%E6%94%BB%E5%87%BB" title="SYN泛洪攻击"></a>SYN 泛洪攻击</h2>
<p>SYN 攻击其实就是 Server 收到 Client 的 SYN，Server 向 Client 发送 SYN-ACK 之后未收到 Client 的 ACK 确认报文， 这样服务器就需要维护海量的半开连接 ，等待客户端的 ACK, 最终导致服务器资源耗尽 (sync queue 满) 而丢弃新的连接。 Server 会不断重发 SYN-ACK，Linux 服务器默认直到 63 秒才断开连接！</p>
<h2 data-id="heading-1"><a href="https://juejin.cn/post/6969099827581812766#SYN-Cookie" title="SYN Cookie"></a>SYN Cookie</h2>
<p>其中一种防护方式是 SYN Cookie， SYN Cookies 的应用允许服务器当 SYN 队列被填满时避免丢弃连接。相反，服务器会表现得像 SYN 队列扩大了一样。服务器会返回适当的 SYN+ACK 响应，但会丢弃 SYN 队列条目。如果服务器接收到客户端随后的 ACK 响应，服务器能够使用编码在 TCP 序号内的信息重构 SYN 队列条目。</p>
<h2 data-id="heading-2"><a href="https://juejin.cn/post/6969099827581812766#Linux%E5%86%85%E6%A0%B8%E5%AE%9E%E7%8E%B0" title="Linux内核实现"></a>Linux 内核实现</h2>
<p>服务器会构造一个 sequence number，根据 TCP 规范，由端点发送的第一个序号可以是由该端点决定的任何值。SYN Cookies 是根据以下规则构造的初始序号：</p>
<ul>
<li>令 t 为一个缓慢递增的时间戳（通常为 <code>time() >> 6</code>，提供 64 秒的分辨率）；</li>
<li>令 m 为服务器会在 SYN 队列条目中存储的最大分段大小（maximum segment size，简称为 MSS）；</li>
<li>令 s 为一个加密散列函数对服务器和客户端各自的 IP 地址和端口号以及 t 进行运算的结果。返回得到的数值 s 必须是一个 24 位值，取低 24 位</li>
</ul>
<p>为了达到最佳的传输效能，TCP 协议在建立连接的时候通常要协商双方的 MSS 值，这个值 TCP 协议在实现的时候往往用 MTU 值代替（需要减去 IP 数据包包头的大小 20Bytes 和 TCP 数据段的包头 20Bytes）所以一般 MSS 值 1460</p>
<p>则初始序列号<code>n</code>为：</p>
<ul>
<li>高 <strong>5</strong> 位为<code>t mod 32</code>（mod 是一种同余运算）</li>
<li>接下来 <strong>3</strong> 位为<code>m</code>的编码值</li>
<li>低 <strong>24</strong> 位为<code>s</code></li>
</ul>
<p>下面是具体过程，主要是低 24 位 s 得计算过程，服务器收到一个 SYN 包，计算一个消息摘要 mac。</p>
<p>mac = MAC(A, k);</p>
<p>MAC 是密码学中的一个消息认证码函数，也就是满足某种安全性质的带密钥的 hash 函数，它能够提供 cookie 计算中需要的安全性。在 Linux 实现中，MAC 函数为 SHA1</p>
<pre><code class="copyable">A = SOURCE_IP || SOURCE_PORT || DST_IP || DST_PORT || t || MSSIND
<span class="copy-code-btn">复制代码</span></code></pre>
<p>k 为服务器独有的密钥，实际上是一组随机数。t 为系统启动时间，每 60 秒加 1。MSSIND 为 MSS 对应的索引。</p>
<p>其实就是根据源 IP、源端口、目的 IP、目的端口、系统启动时间，MSS 索引通过哈希函数计算出的一个值</p>
<p>SYN Cookie 在 Linux 内核中的实现</p>
<p>如果 SYN Cookie 功能有编译进内核 (CONFIG_SYN_COOKIE)，且选项 tcp_syncookies 不为 0，那么可使用 SYN Cookie。同时设置 SYN Flood 标志 (listen_opt->synflood_warned)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af3581cc215441c3bcec8283625488ed~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8231abd7d88d4efe8032893f6187c046~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>SHA1 安全哈希算法 (Secure HASH Algorithm) 主要适用于数字签名。</p>
<p>对于长度小于 2^64 位的消息，SHA1 会产生一个 160 位的消息摘要。当接收到消息的时候，这个消息摘要可以用来<br>
验证数据的完整性。在传输的过程中，数据可能会发生变化，那么这时候就会产生不同的消息摘要。<br>
SHA1 有如下特性：</p>
<ul>
<li>
<p>不可以从消息摘要中复原信息。</p>
</li>
<li>
<p>两个不同的消息不会产生同样的消息摘要。</p>
</li>
</ul>
<p>当客户端收到此<code>SYN+ACK</code> 报文后，根据<code>TCP</code>标准，它会回复<code>ACK</code>报文，且报文中<code>ack = n + 1</code>，那么在服务器收到它时，将<code>ack - 1</code>就可以拿回当初发送的<code>SYN+ACK</code>报文中的序号了！服务器巧妙地通过这种方式间接保存了一部分<code>SYN</code>报文的信息。 看到这里在回顾一个这个序列号的组成</p>
<ul>
<li>高 <strong>5</strong> 位为<code>t mod 32</code>（mod 是一种同余运算）</li>
<li>接下来 <strong>3</strong> 位为<code>m</code>的编码值</li>
<li>低 <strong>24</strong> 位为<code>s</code></li>
</ul>
<p>接下来，服务器需要对<code>ack - 1</code>这个序号进行检查：</p>
<ul>
<li>将高 <strong>5</strong> 位表示的<code>t</code>与当前之间比较，看其到达地时间是否能接受。</li>
<li>根据<code>t</code>和连接元组重新计算<code>s</code>，看是否和低 <strong>24</strong> 一致，若不一致，说明这个报文是被伪造的。</li>
<li>解码序号中隐藏的<code>mss</code>信息</li>
</ul>
<p>如果成功匹配， 服务器就会为新的连接创建和初始化一个传输控制块，然后把完成三次握手的 req 和新 sock 关联起来，下面看看验证这段逻辑的代码</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4326980204b44bcb2e37c74e8169e5d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>SYN Cookie</code>技术可以让服务器在收到客户端的<code>SYN</code>报文时，不分配资源保存客户端信息，而是将这些信息保存在<code>SYN+ACK</code>的初始序号和时间戳中。对正常的连接，这些信息会随着<code>ACK</code>报文被带回来。</p>
<h2 data-id="heading-3"><a href="https://juejin.cn/post/6969099827581812766#SYN-Cookie%E6%80%BB%E7%BB%93" title="SYN Cookie总结"></a>SYN Cookie 总结</h2>
<p>由于 cookie 的计算只涉及到包头部分信息，在建立连接的过程。中不在服务器端保存任何信息，所以失去了协议的许多功能，比如超时重传。此外，由于计算 cookie 有一定的运算量，增加了连接建立的延迟时间，因此，SYN Cookie 技术不能作为高性能服务器的防御手段。一些 SYN 攻击的防火墙也是基于 SYN Cookie，只是把这个功能移动到内核之外的代理服务器上。</p>
<p>参考资料：</p>
<p><a href="https://lwn.net/Articles/277146/" target="_blank" rel="nofollow noopener noreferrer">lwn.net/Articles/27…</a></p>
<p><a href="https://zh.wikipedia.org/wiki/SYN_cookie" target="_blank" rel="nofollow noopener noreferrer">zh.wikipedia.org/wiki/SYN_co…</a></p></div>  
</div>
            