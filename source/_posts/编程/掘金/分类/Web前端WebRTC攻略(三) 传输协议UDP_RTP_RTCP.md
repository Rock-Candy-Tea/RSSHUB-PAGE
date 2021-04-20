
---
title: 'Web前端WebRTC攻略(三) 传输协议UDP_RTP_RTCP'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee3311dbedb74cc0be9e32deaa6909b6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Apr 2021 04:51:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee3311dbedb74cc0be9e32deaa6909b6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>导语 | 音视频时代，WebRTC在形形色色的产品和业务场景下均有落地。在熟悉如何在浏览器获取设备的音视频数据和WebRTC是如何将获取的音视频数据进行网络传输的同时，我们更要夯实一下网络传输协议相关的基础知识，这能帮助我们更深入地学习WebRTC。推荐和前端音视频专题中的文章一起食用。</p>
<h2 data-id="heading-0">1. 传输层协议：TCP vs. UDP</h2>
<p>我们都知道HTTP协议，运行于TCP协议之上，是万维网的运转的基础。作为一名前端开发，我们似乎理所应当熟悉HTTP、TCP协议，以致于HTTP状态码、报文结构、TCP三次握手、四次挥手等等都已经成为了标配的基础面试题。但对于其他协议，我们似乎多多少少感到陌生。</p>
<p>下图是一个TCP/IP通讯协议的4层结构图，在基于网际层的运输层，它提供了节点间的数据传送服务，其中最为人所熟知的<strong>TCP协议（Transmission Control Protocol）</strong> 和 <strong>UDP协议（User Datagram Protocol）</strong>。</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee3311dbedb74cc0be9e32deaa6909b6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>两个协议本身涉及到内容非常多，但在实际选择使用中，我们不妨直接通过对比TCP和UDP，来去学习和理解它们。</p>
<h3 data-id="heading-1">1.1. TCP和UDP对比</h3>
<p>总体上有以下三点不同：</p>
<ul>
<li>
<p>TCP是面向连接的，UDP是无连接的。</p>
</li>
<li>
<p>TCP是面向字节流的，实际上是TCP把数据看成一连串无结构的字节流；UDP是面向报文的。</p>
</li>
<li>
<p>TCP提供可靠的传输，也就是说TCP连接传输的数据不会丢失，没有重复，并且按顺序到达，UDP提供不可靠传输。</p>
</li>
</ul>
<h4 data-id="heading-2">1.1.1. UDP无连接，TCP面向连接</h4>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4d577e2fa1549d0b3c471391f101cc2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>UDP在传输数据之前不需要建立连接，传输双方可以随时发送数据，因此UDP是无连接的。而TCP协议在传输数据之前三次握手建立连接，在结束后需要四次挥手释放连接，具体细节在此不做赘述。</p>
<h4 data-id="heading-3">1.1.2. UDP面向报文，TCP面向字节流</h4>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1f807f7cc7c4954a7b700dcef231ec2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对于UDP，发送接收方应用层只给UDP传输层发送或接收报文，而UDP除了传输外的处理只是对应用层报文添加或摘除UDP首部，保留了应用层报文，因此说UDP是面向报文。</p>
<p>对于TCP而言，TCP只将应用层交下来的数据当做一连串的无结构字节流，仅将他们存入缓存并根据策略构建TCP报文进行发送，而接受方TCP只提取数据载荷部分存入缓存，并同时将缓存字节流交给应用层。TCP不保证双方应用层的发送和接收数据具有对应大小关系。因此说它是面向字节流的，而它也是TCP实现流量控制和拥塞控制的基础。</p>
<h4 data-id="heading-4">1.1.3. UDP是不可靠连接，TCP是可靠连接</h4>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71ea13d470da4ac9893b4abd89d419db~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>UDP在传输数据时，发送产生了丢包，发送方不做任何处理。接收方校验首部发现误码，同样也不做任何处理。因此说UDP向上提供的是无连接不可靠服务。</p>
<p>而TCP在传输数据时，如果发生了丢包或者接收方检查了误码（此时会接收方会丢弃），接收方不会回确认报文，则触发接收方超时重发。由此可见，TCP通过其策略确保其传输过程无论发生什么情况，则接收方就能正确收到该数据包，因此说TCP是向上提供面向连接的可靠服务。</p>
<h3 data-id="heading-5">1.2. 为什么选择UDP</h3>
<p>既然TCP有这么多优点特性，那么为什么在实时音视频传输中使用UDP呢？</p>
<p>原因在于实时音视频对于延迟特别敏感，而基于TCP协议的做不到足够低。试想一下在丢包的情况下，TCP协议的超时重传机制中RTT是以2的指数的增长。如果7次重传任然失败，理论计算会达到2分钟！在延迟高的情况下，想做到正常的实时通讯显然是不可能的，此时TCP的可靠性反而成了累赘。</p>
<p>但实际情况是，通常实时音频视频数据在传输的少量数据包丢失，对接收者影响并不大。而UDP不属于连接型协议，我们认为它基本是管发不管收，因而具有资源消耗小，处理速度快的优点。</p>
<p><strong>因此UDP在实时性和效率性都很高，在实时音视频传输中通常会选用UDP协议作为传输层协议。</strong></p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/212394aceb314feba67512461d9e13fd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>WebRTC也是如此，在信令控制方面采用了可靠的TCP，<strong>但是音视频数据传输上，使用了UDP作为传输层协议</strong>（如上图右上）。</p>
<h2 data-id="heading-6">2. 应用层协议：RTP and RTCP</h2>
<p>实时音视频通讯只靠UDP够不够呢？答案显然是不够的！还需要基于UDP的应用层协议，来专门为音视频通讯做更多保障处理。</p>
<h3 data-id="heading-7">2.1. RTP协议</h3>
<p>音视频中一个视频帧数据量需要多个包来传送，并在接收端组成对应帧，正确还原出视频信号。因此要做到至少两点：</p>
<ol>
<li>
<p>检测出错顺序，并保持采样和播放之间的同步关系。</p>
</li>
<li>
<p>需要在接收端检测出分组的丢失。</p>
</li>
</ol>
<p>而UDP并没有这个能力，所以音视频传输中，并不直接使用UDP，而是需要RTP作为实时音视频中的应用层协议。</p>
<p><strong>RTP全名Real-timeTransportProtocol(实时传输协议)</strong>，主用于实时传输数据。那么RTP协议提供哪些能力？</p>
<p>包括以下四点：</p>
<ol>
<li>
<p>实时数据的端到端传输。</p>
</li>
<li>
<p>序号（用于丢包和重排序检）</p>
</li>
<li>
<p>时间戳（时间同步校对和分发监控）</p>
</li>
<li>
<p>载荷的定义类型（用于说明数据的编码格式）</p>
</li>
</ol>
<p>但不包括：</p>
<ol>
<li>
<p>及时发送</p>
</li>
<li>
<p>质量保证</p>
</li>
<li>
<p>送达（可能丢）</p>
</li>
<li>
<p>时序（到达顺序）</p>
</li>
</ol>
<p>接下来让我们简单看下<strong>RTP协议规范****[1]</strong></p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/062991c1c8bc460a9c8c141b36bc5df9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>RTP报文由两部分组成：报头和有效载荷。</p>
<p>以下为RTP协议头的解释，前12字节是固定的，CSRC可以有多个或者0个。</p>
<ul>
<li>
<p><strong>V</strong>：RTP协议的版本号，占2位，当前协议版本号为2。</p>
</li>
<li>
<p><strong>P</strong>：填充标志，占1位，如果P=1，则在该报文的尾部填充一个或多个额外的八位组，它们不是有效载荷的一部分。</p>
</li>
<li>
<p><strong>X</strong>：扩展标志，占1位，如果X=1，则在RTP报头后跟有一个扩展报头。</p>
</li>
<li>
<p><strong>CC</strong>：CSRC计数器，占4位，指示CSRC标识符个数。</p>
</li>
<li>
<p><strong>M</strong>：标志，占1位，不同的有效载荷有不同的含义，<strong>对于视频，标记一帧的结束；对于音频，标记会话的开始</strong>。</p>
</li>
<li>
<p><strong>PT（payload type）</strong>：<strong>有效荷载类型，占7位，用于记录RTP报文中有效载荷的类型/Codec</strong>，在流媒体中大部分是用来区分音频流和视频流，便于接收（receiver）找出相应的 decoder 解码出來。</p>
</li>
<li>
<p><strong>序列号（sequence number）</strong>：占16位，<strong>用于标识发送者所发送的RTP报文的序列号，每发送一个报文，序列号增1</strong>。 这个字段当下层的承载协议用UDP的时候，网络状况不好的时候可以用来检查丢包。当出现网络抖动的情况可以用来对数据进行重新排序。序列号的初始值是随机的，同时音频包和视频包的sequence是分别计数的。</p>
</li>
<li>
<p><strong>时戳（timestamp）</strong>：占32位，必须使用90kHZ时钟频率（程序中的90000）。<strong>时戳反映了该RTP报文的第一个八位组的采样时刻。接受者使用时戳来计算延迟和延迟抖动，并进行同步控制。可以根据RTP包的时间戳来获得数据包的时序。</strong></p>
</li>
<li>
<p><strong>同步源（SSRC）标识符</strong>：占32位，用于标识同步信源。同步信源是指产生媒体流的信源，他通过RTP报头中的一个32为数字SSRC标识符来标识，而不依赖网络地址，接收者将根据SSRC标识符来区分不同的信源，进行RTP报文的分组。</p>
</li>
<li>
<p><strong>贡献源（CSRC）标识符</strong>：每个CSRC标识符占32位，可以有0~15个CSRC。每个CSRC标识了包含在RTP报文有效载荷中的所有提供信源。</p>
</li>
</ul>
<h3 data-id="heading-8">2.2. RTCP协议</h3>
<p>前面提到RTP协议整体上还是比较简单粗暴的，其本身并没有提供按时发送机制或其它服务质量（QoS）保证。因此RTP还需要有一套配套协议为其服务质量提供保证，则就是<strong>RTCP协议（全名Real-timeControlProtocol）。</strong></p>
<blockquote>
<p>RTP标准定义了两个子协议，RTP和RTCP。</p>
</blockquote>
<p>举个例子，在传输音视频时的丢包，乱序，抖动，这些WebRTC在底层都有对应的处理策略。但是如何将这些传输时 <strong>“网络质量信息”</strong> 实时告诉对方，就是RTCP它的作用。相对于RTP来说，RTCP所占的带宽非常小，通常只有5%。</p>
<p>接下来让我们简单看下RTCP协议规范：首先RTCP报文有多种类型：</p>
<ol>
<li>
<p><strong>发送报告SR (Sender Report)</strong>: 当前活动发送者发送、接收统计。PT=200</p>
</li>
<li>
<p><strong>接受者报告RR (Reciver Report)</strong>：接收报告，非活动发送者接收统计。PT=201</p>
</li>
<li>
<p>源描述报告SDES(Source Description)：源描述项，包括CNAME PT=202</p>
</li>
<li>
<p>BYB报告：参与者结束对话 PT=203</p>
</li>
<li>
<p>APP报告：应用自定义 PT=204</p>
</li>
<li>
<p>jitter报告IJ PT=195</p>
</li>
<li>
<p>传输反馈RTPFB PT=205</p>
</li>
<li>
<p>Playload反馈PSFB PT=206 . . . . . 这里我们可以关注两个比较重要的的报文：<strong>SR</strong> 和 <strong>RR</strong>，通过他们让收发两端知道网络质量情况。</p>
</li>
</ol>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a89a55265f34ff687ff7e20d53a7fd6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>以上为SR的协议规范：</p>
<ul>
<li>
<p>Header 部分用于标识该报文的类型，比如是 SR（200） 还是 RR（201）。</p>
</li>
<li>
<p>Sender info 部分用于指明作为发送方，到底发了多少包。</p>
</li>
<li>
<p>Report block 部分指明发送方作为接收方时，它从各个 SSRC 接收包的情况。</p>
</li>
</ul>
<p>通过报告以上信息，各端知道网络传输反馈数据后，就可以根据其做传输策略的调整了。当然协议本身的内容并不只有上面的简单一小段，实际还涉及各项反馈数据的计算方法，这里篇幅有限不展开细讲。</p>
<h3 data-id="heading-9">2.3. RTP会话流程小结</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1eb79d28d4945d3b5a1190633c197fb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当了解为什么选择UDP协议、以及RTP/RTCP协议做了些什么事情之后，让我们简单总结在传输协议层面上的整个流程：</p>
<p>当应用建立一个RTP会话时，应用程序将确定一对目的传输地址。目的传输地址由一个网络地址和一对端口组成，有两个端口：一个给RTP包，一个给RTCP包。RTP数据发向偶数的UDP端口，而对应的控制信号RTCP数据发向相邻的奇数UDP端口（偶数的UDP端口＋1），这样就构成一个UDP端口对。大致流程如下：</p>
<ol>
<li>
<p>RTP协议从上层接收流媒体信息码流，封装成RTP数据包；</p>
</li>
<li>
<p>RTCP从上层接收控制信息，封装成RTCP控制包。</p>
</li>
<li>
<p>RTP将RTP 数据包发往UDP端口对中偶数端口；RTCP将RTCP控制包发往UDP端口对中的接收端口。</p>
</li>
</ol>
<h3 data-id="heading-10">2.4. 快速上手Wireshark抓包RTP及RTCP</h3>
<p>纸上得来终觉浅,绝知此事要躬行。接下来让我们通过实际播放WebRTC流媒体，并通过抓包来还原RTP包和RTCP报文的真面目。</p>
<p>Wireshark是一个强大的网络数据包分析软件，可以详细的展示网络数据包的交换过程，是监控网络请求定位网络问题的利器。这个强大的抓包工具，涉及非常多功能，由于这里不是Wireshark教程，更详细的功能课自行搜索挖掘，这里只会讲个大致流程：</p>
<ol>
<li>
<p>下载并安装Wireshark（非常简单）。</p>
</li>
<li>
<p>浏览器打开腾讯课堂，挑选一个免费且正在直播的课程，一般情况下采用WebRTC播放。(另起tab打开WebRTC调试工具 这里会展示页面WebRTC播放实时流媒体数据的网络情况。)</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/091296653bb9445790fb6e1e63203cda~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>打开Wireshark，需要选择要捕获机器上网卡的网络包。当你的机器上有多块网卡的时候，你需要选择一个网卡接口，这里我选择了我的Wifi，并点击左上角蓝色按钮开始抓包。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebaa4ea28def4d84ba6fe818789cf0b4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>一旦你启动抓包，这里会瞬间展示抓到的各种协议的大量数据包（下图展示wireshark每个区域的功能），其中在①过滤栏中输入UDP进行过滤，然后就会在②数据包列表中只展示出udp的数据包，并会解析出部分协议的数据包，并在Protocol列清楚的看到它们的协议。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa1cb38ecb724699912807aac086d453~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>由于WireShark不会直接识别RTP的UDP数据包，需要右键UDP包解析为（decode as）RTP包。</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b534db698b240689af3f1a30b418a33~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>此时wireshark能够识别RTP协议数据包，在分层协议可以看到清晰的结构，从上往下依次是：IP = > UDP => RTP 我们点开RTP协议那一层，展开可以看到，和上面RTP报文协议的一致：标明了版本号、填充标记...等等内容。</p>
</li>
</ol>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14d36d6a76b14112b640715245f81e6b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其中我们应该着重关注的部分内容：<br>
<strong>Playload type（PT值）</strong>：代表负载的类型，其中这里122对照WebRTC的SDP可以确认是H264视频负载类型数据。</p>
<p><strong>时间戳</strong>：记录的是采样时刻为6120，还要根据采样率进行换算。</p>
<p><strong>SSRC</strong>: 同步源（SSRC）标识符为0x0202c729。以上这些都是RTP头部，最后playload才是承载的媒体数据。</p>
<p>RTP的特点不仅仅支持承载在UDP上，有利于低延迟音视频数据的传输，它允许通过其它协议接收端和发送端协商音视频数据的封装和编解码格式，playload type字段比较灵活支持的音视频数据类型非常多的，具体可以参考：RTP payload formats</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/709a623b6a5f4a95bb2ae190bb4e5f6a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>让我们再具体看看RTP包的音视频帧：</p>
<p>其中下面seq=21到seq=24的多个数据包，每个单独为一个音频帧，所以时间戳不同。而红色框seq=96到seq=102的多个数据包组成，组成PT=122的一个视频帧，所以这几个报的时间戳也是相同的。这是因为一个视频帧包含数据量较大，需要分开多个包发送。而音频帧较小，则单独一个包发送，从它们的包length大小就能看出视频包比音频包要大的多。另外seq=102的数据包，mark字段为true表示为一个视频帧的最后一个数据包，通过结合seq可以知道音视频数据的接收是否有乱序或者是丢包。</p>
<ol start="15">
<li>通过上方‘工具栏’=>‘电话’=>‘RTP‘打开信息面板，可以看到当前有一条音频RTP流，和一条视频RTP流。左边分析出表示了流的源地址端口和目的地址和端口。右边为RTP相关内容，展示了RTP流的SSRC、载荷类型、丢包情况等等。</li>
</ol>
<pre><code class="copyable">![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c1384e475a74a6391e2d15c4a812943~tplv-k3u1fbpfcp-watermark.image)  
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="16">
<li>最后再简单看RTCP，在过滤栏中输入rtcp进行过滤，可以看到Sender Report 和 Receive Report。他们的PT（packcet type）分别为200和201，报告的SSRC为0x02029dfc，以及详细的发送包和接收的情况。详细的内容解析可以结合RTCP规范协议去进一步学习了解。</li>
</ol>
<pre><code class="copyable">![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c5e8a76818e48c19ebe9c4b04816c53~tplv-k3u1fbpfcp-watermark.image)  
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">3. 总结</h2>
<p>不少人觉得一名开发者在学习使用WebRTC时，能够快速上手实践和业务落地就足够了，再去了解这些传输协议有必要吗？但常常即便你已经清楚如何使用它，不代表你能发挥出它本身最大优势。我认为运用一项技术所达到的上限，往往取决于你对它的底层理解有多深入。</p>
<p>这里简单介绍为什么实时音视频选择UDP作为传输层协议，以及简单介绍WebRTC所涉及协议中比较重要的两个协议RTP/RTCP，像WebRTC技术涉及与融合多方面种技术（音视频处理，传输、安全加密等等）每个模块涉及的协议都能单独写一篇文章，篇幅所限以及本人掌握的内容比较有限，此文无法对更多内容进行展开。如果你想学习实践WebRTC，此文只能让你在其传输协议层面上有初步的认识。由于协议往往涉及底层，平时运用往往关注不到，因此还介绍了如何快速上手抓包来帮助理解，如果想深入学习还需另寻资料深入学习。</p>
<h2 data-id="heading-12">4. 参考资料</h2>
<p>[1]RTP协议:<a href="https://tools.ietf.org/html/rfc35f50#" target="_blank" rel="nofollow noopener noreferrer">tools.ietf.org/html/rfc35f…</a></p>
<p><img alt="扫码关注我们吧~" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aad6fee52bd448cc8119baebba5bce1c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            