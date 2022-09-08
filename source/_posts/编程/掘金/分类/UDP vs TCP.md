
---
title: 'UDP vs TCP'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3fb2c100407470f8638f747283777d1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 06:17:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3fb2c100407470f8638f747283777d1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、UDP</h2>
<p>UDP（User Datagram Protocol），用户数据包协议，是一个简单的<strong>面向数据报的通信协议</strong>，即对应用层交下来的报文，不合并，不拆分，只是在其上面加上首部后就交给了下面的网络层</p>
<p>也就是说无论应用层交给<code>UDP</code>多长的报文，它统统发送，一次发送一个报文</p>
<p>而对接收方，接到后直接去除首部，交给上面的应用层就完成任务</p>
<p><code>UDP</code>报头包括4个字段，每个字段占用2个字节（即16个二进制位），标题短，开销小</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3fb2c100407470f8638f747283777d1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>特点如下：</p>
<ul>
<li>UDP 不提供复杂的控制机制，利用 IP 提供面向无连接的通信服务</li>
<li>传输途中出现丢包，UDP 也不负责重发</li>
<li>当包的到达顺序出现乱序时，UDP没有纠正的功能。</li>
<li>并且它是将应用程序发来的数据在收到的那一刻，立即按照原样发送到网络上的一种机制。即使是出现网络拥堵的情况，UDP 也无法进行流量控制等避免网络拥塞行为</li>
</ul>
<h2 data-id="heading-1">二、TCP</h2>
<p>TCP（Transmission Control Protocol），传输控制协议，是一种可靠、<strong>面向字节流的通信协议</strong>，把上面应用层交下来的数据看成无结构的字节流来发送</p>
<p>可以想象成流水形式的，发送方TCP会将数据放入“蓄水池”（缓存区），等到可以发送的时候就发送，不能发送就等着，TCP会根据当前网络的拥塞状态来确定每个报文段的大小</p>
<p><code>TCP</code>报文首部有20个字节，额外开销大</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/071014755ef348998576fbddbd43f255~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>特点如下：</p>
<ul>
<li>TCP充分地实现了数据传输时各种控制功能，可以进行丢包时的重发控制，还可以对次序乱掉的分包进行顺序控制。而这些在 UDP 中都没有。</li>
<li>此外，TCP 作为一种面向有连接的协议，只有在确认通信对端存在时才会发送数据，从而可以控制通信流量的浪费。</li>
<li>根据 TCP 的这些机制，在 IP 这种无连接的网络上也能够实现高可靠性的通信（ 主要通过检验和、序列号、确认应答、重发控制、连接管理以及窗口控制等机制实现）</li>
</ul>
<h2 data-id="heading-2">三、区别</h2>
<p><code>UDP</code>与<code>TCP</code>两者的都位于传输层，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fecf742bc8f40c7b51011f6a5008ccb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>两者区别如下表所示：</p>


















































<table><thead><tr><th></th><th>TCP</th><th>UDP</th></tr></thead><tbody><tr><td>可靠性</td><td>可靠</td><td>不可靠</td></tr><tr><td>连接性</td><td>面向连接</td><td>无连接</td></tr><tr><td>报文</td><td>面向字节流</td><td>面向报文</td></tr><tr><td>效率</td><td>传输效率低</td><td>传输效率高</td></tr><tr><td>双共性</td><td>全双工</td><td>一对一、一对多、多对一、多对多</td></tr><tr><td>流量控制</td><td>滑动窗口</td><td>无</td></tr><tr><td>拥塞控制</td><td>慢开始、拥塞避免、快重传、快恢复</td><td>无</td></tr><tr><td>传输效率</td><td>慢</td><td>快</td></tr></tbody></table>
<ul>
<li>TCP 是面向连接的协议，建立连接3次握手、断开连接四次挥手，UDP是面向无连接，数据传输前后不连接连接，发送端只负责将数据发送到网络，接收端从消息队列读取</li>
<li>TCP 提供可靠的服务，传输过程采用流量控制、编号与确认、计时器等手段确保数据无差错，不丢失。UDP 则尽可能传递数据，但不保证传递交付给对方</li>
<li>TCP 面向字节流，将应用层报文看成一串无结构的字节流，分解为多个TCP报文段传输后，在目的站重新装配。UDP协议面向报文，不拆分应用层报文，只保留报文边界，一次发送一个报文，接收方去除报文首部后，原封不动将报文交给上层应用</li>
<li>TCP 只能点对点全双工通信。UDP 支持一对一、一对多、多对一和多对多的交互通信</li>
</ul>
<p>两者应用场景如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8172873735ce4ecdad207002b685dbc2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，TCP 应用场景适用于对效率要求低，对准确性要求高或者要求有链接的场景，而UDP 适用场景为对效率要求高，对准确性要求低的场景</p>
<h2 data-id="heading-3"></h2></div>  
</div>
            