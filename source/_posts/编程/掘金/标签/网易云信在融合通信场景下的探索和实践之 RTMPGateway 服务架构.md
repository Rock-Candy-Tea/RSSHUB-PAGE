
---
title: '网易云信在融合通信场景下的探索和实践之 RTMPGateway 服务架构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1af6f1ae97946e893bb64404e0bce08~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 00:16:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1af6f1ae97946e893bb64404e0bce08~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">0 导读</h2>
<p>随着各个行业的互联网化进程不断演进，融合通信在越来越多的场景中得到应用，例如金融场景的视频面签、医疗场景的远程会诊、企业协作场景的多人视频会议等。在这些场景中，通过微信小程序实现音视频互通，可以降低用户沟通成本，提升业务运营效率，同时帮助企业或组织进一步打通微信社群中的沟通障碍，以一种轻量化的敏捷运营模式轻松实现微信生态中的客户转化闭环。因此，小程序音视频必将受到越来越多企业和组织的青睐。</p>
<p>那么，一个能够支持微信小程序之间实现音视频通话，同时能够支持微信小程序跨平台互联互通的媒体服务器需要完成哪些事情？</p>
<h2 data-id="heading-1">1 RTMPGateway</h2>
<p>微信在6.5.21版本通过小程序开放了实时音视频能力，开发者们可以使用组件 < live-pusher > 实现基于 RTMP 的直播推流（录制），在新版本中加入了 RTC 模式，用于实时音视频通话上行，使用组件 < live-player > 实现基于 RTMP 的直播拉流（播放），RTC 模式则用于实时音视频通话下行。可以看出，微信小程序的音视频是基于 RTMP 协议的，同时，微信小程序的音视频只是提供了终端上的能力，并没有实现媒体服务器，那么如何实现微信小程序之间的音视频通话，同时实现和多平台之间互联互通？答案是肯定的，我们需要自己开发一个媒体服务器。</p>
<p>在网易云信融合通信场景下，</p>
<ul>
<li>微信小程序端使用 RTMP 协议，接入边缘媒体网关，即 RTMPGateway；</li>
<li>RTMPGateway 支持 RTMP 协议，完成微信小程序间的媒体转发；</li>
<li>同时，RTMPGateway 将 RTMP 协议转换成 RTP 协议，转发给云信边缘媒体服务器，完成与云信 SDK、标准 WebRTC 终端的互联互通。</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1af6f1ae97946e893bb64404e0bce08~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">2 关于 RTMP 连接</h2>
<p>上文提到 RTMP，这里我们再简单介绍一下，RTMP(Real Time Messaging Protocol，即实时消息传送协议)，是 Adobe 公司开发的一个基于 TCP 的应用层协议，被广泛应用于直播领域。</p>
<p>RTMP 协议是基于 TCP 的，而在 TCP 连接建立完成后，无论是发布还是播放一个 RTMP 协议的流媒体，都还需要经过以下几个步骤：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6d87aff0ece4f539ee3c629305df1c5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">RTMP 握手（Handshake）</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0305b737b0064358bad301b7d523d0c7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>握手开始于客户端发送 C0、C1 块；服务器收到 C0 或 C1 后发送 S0 和 S1。</li>
<li>客户端收齐 S0 和 S1 后，开始发送 C2；服务器收齐 C0 和 C1 后，开始发送 S2。</li>
<li>客户端和服务器分别收到 S2 和 C2 后，握手完成。</li>
</ul>
<p>这就是一个完整的握手过程。</p>
<p>在实际工程应用中，一般是客户端先将 C0、C1 块同时发出，服务器在收到 C1 之后同时将 S0、 S1、 S2 发给客户端。之后客户端向服务器端发送 C2 块，简单握手完成。</p>
<p>Flash 播放器连接服务器时，若服务器只支持简单握手，则无法播放 H.264 和 AAC 的流，可能是 Adobe 的限制，Adobe 将简单握手改为了有一系列加密算法的复杂握手（complex handshake）。</p>
<p>简单握手的包是随机的1536字节（S1/S2/C1/C2），复杂握手则是需要进行摘要和加密，此处不再赘述。</p>
<h3 data-id="heading-4">建立网络连接（NetConnection）</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1468a8949e44c59a31ed1d7bc4e0e92~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>客户端发送命令消息(connect)到服务器，请求与一个服务器建立连接。</li>
<li>服务器接收消息后，发送确认窗口大小协议，设置带宽协议，设置块大小协议消息到客户端。</li>
<li>客户端处理设置带宽协议消息后，发送确认窗口大小协议消息到服务器端。</li>
<li>服务端向客户端发送“流开始”（Stream Begin）。</li>
<li>服务器发送(_result)，通知客户端连接的状态。</li>
</ul>
<h3 data-id="heading-5">建立网络流（Create Stream）</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ab2183946ef47acb1aef8cbe2b88e03~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>客户端发送命令消息（CreateStream）命令到服务器端。</li>
<li>服务器端接收消息后，发送(_result)，通知客户端流的状态。</li>
</ul>
<p>可以看出，建立一个 RTMP 连接，需要完成复杂的协议交互，并且这些协议交互都是同步的。那么，如何实现一个异步的 RTMP 协议栈？</p>
<p>对于一个需要处理大量连接的 Server，无非两种策略：多线程或使用异步 Socket。</p>
<p>例如对于 RTMPDump 提供的基于同步 Socket 的 librtmp，只能使用多线程处理多个连接，但是多线程的并发数上限明显，同时需要处理复杂的锁和同步等。Winlin 则是在 SRS 中使用 st 协程在单线程中实现了异步的 RTMP 协议栈。</p>
<p>而在云信的 RTMPGatway 中，我们使用状态机的方式，同样在单线程实现了异步的 RTMP 协议栈。针对每一条 RTMP 连接，RTMPGatway 均会记录连接目前所处状态，以跟踪整个连接的建立。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9b89eb9a284412ab5deb9fff119f389~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">3 关于媒体协议封装</h2>
<p>为了实现微信小程序与云信 SDK、标准 WebRTC 终端的互联互通，RTMPGatway 需要实现 RTMP 协议和 RTP 协议的转换。</p>
<h3 data-id="heading-7">RTMP 封装 AAC</h3>
<p>微信小程序推拉流使用 RTMP 协议，音频使用 AAC 编码。</p>
<p>使用 RTMP 推送 AAC 直播流，首先需要发送“AAC sequence header”，其中包含重要的编码信息，没有它解码器将无法解码。AAC sequence header 存放的是 AudioSpecificConfig 结构，其结构描述非常复杂（详见“ISO-14496-3 Audio”），可以简化为下表：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b724af2a0823427badca68d8f675f5b9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在发送这个 header 需要在前面分别加上1个字节（8bits）的 AudioTags 数据，其中每 bit 表示的意义如下图：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/826106b92e7246ff8755946db0b2bae1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a06880b96d6439fafdfe189bf60d851~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其中 SoundData 的组成如下：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df583f80450e4f3286451533a37dda20~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当数据的第一个字节为0时，后面跟 AAC sequence header；当数据的第一个字节为1时，后面跟AAC 数据。</p>
<h3 data-id="heading-8">RTMP 封装 H.264</h3>
<p>微信小程序使用 RTMP 协议进行推拉流，使用 H.264 进行视频编码。</p>
<p>使用 RTMP 推送 H.264 直播流，首先需要发送"AVC sequence header"，同样包含重要的编码信息，没有它解码器将无法解码。AVC sequence header 就是 AVCDecoderConfigurationRecord 结构（详见“ISO-14496-15 AVC file format”），简化为下表：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afd625be967345da9c3d0ee22dd56897~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在发送这个 Header 需要在前面分别加上1个字节（8bits）的 VideoTags 数据，其中每 bit 表示的意义如下图：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83c780ff78034ab6832edac64e783d2e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>发送的为 avc 数据，所以 CodecID（后 4bit）的值为 7；videodata 的数据打包方式为 AVCVIDEOPACKET，具体的信息见下图：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b8b49590b8c42dabdb9fe64531bc01a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">RTP 协议</h3>
<p>RTP( Real-time Transport Protocol，即实时传输协议），为语音、图像、传真等多种需要实时传输的多媒体数据提供端到端的实时传输服务，服务质量则由 RTCP（Real-time Transport Control Protocol，即实时传输控制协议）来提供。</p>
<p>RTP 协议头信息包括 RTP 固定头以及 RTP 扩展头，如下图：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0df28d5bf024ae88f68f25e9c284b27~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>RTP 固定头</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb950b6fc2894407b80b6fd433791973~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>RTP 扩展头</p>
<p>若 RTP 固定头中的扩展比特位置 1，则一个长度可变的头扩展部分被加到 RTP 固定头之后，如果有 CSRC 列表，则在 CSRC 列表之后。头扩展包含 16 比特的长度域，指示扩展项中 32 比特字的个数，不包括 4 个字节扩展头(因此零是有效值)。</p>
<p>RTP 固定头之后只允许有一个头扩展。为允许多个互操作实现独立生成不同的头扩展，或某种特定实现有多种不同的头扩展，扩展项的前 16 比特用以识别标识符或参数。这 16 比特的格式由具体实现的上层协议定义。基本的 RTP 说明并不定义任何头扩展本身。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa0b9597154b43e19eec5925c333886e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>IETF 针对 RFC3550 在档次方面定义了一系列扩展协议，一些总结如下：</p>
<ul>
<li>RFC3550 - RTP: A Transport Protocol for Real-Time Applications (RTP)：定义最基本的RTP/RTCP报文格式和收发规则；</li>
<li>RFC3551 - RTP Profile for Audio and Video Conferences with Minimal Control ：定义音视频会议最基本的音视频数据负载格式、编码和传输，是其它档次的基础；</li>
<li>RFC3711 - The Secure Real-time Transport Protocol (SRTP)：定义了RTP在安全方面的增强，如加密、认证和重放保护；</li>
<li>RFC4585 - Extended RTP Profile for Real-time Transport Control Protocol (RTCP)-Based Feedback (RTP/AVPF) ：定义了RTP基于RTCP在及时反馈方面的增强，如定义NACK，PLI，SLI等RTCP报文；</li>
<li>RFC5124 - Extended Secure RTP Profile for Real-time Transport Control Protocol (RTCP)-Based Feedback (RTP/SAVPF)：综合RTP/SAVP和RTP/AVPF的安全性和及时反馈性的最全面的档次。</li>
</ul>
<p>RFC 3550 定义五种 RTCP 报文，类型在报文头部的PT域定义。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/516d121927d44693b0d280432f27aa02~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>SR 报文用于发送端报告本端的数据发送统计信息和数据接收统计信息，RR 报文用于报告本端的数据接收统计信息，SDES 报文用于报告本端的描述性信息，BYE 在本端离开会话时发送，而 APP 则是特定于应用的数据。IETF 根据实际需求对 RTCP 的报文类型进行扩展，定义了一系列协议，此处不再赘述。</p>
<h3 data-id="heading-10">RTP 封装 H.264</h3>
<p>针对 H.264 的封装，WebRTC 选择了使用 RFC3984 的 Non-Interleaved 封装方案。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa9a4a11f5a449ce8280fad36fd314aa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>Single NAL Unit Packet</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78da9a7f7e824266b33894323c0e9437~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Single NAL Unit Packet 是 RTP 最基本的打包方式，其中，</p>
<ul>
<li>forbidden_bit：禁止位，初始为0，当网络发现 NAL 单元有比特错误时可设置该比特为 1，以便接收方纠错或丢掉该单元。</li>
<li>nal_reference_bit：nal 重要性指示，标志该 NAL 单元的重要性，值越大，越重要，解码器在解码处理不过来的时候，可以丢掉重要性为 0 的 NALU。</li>
<li>Type：NAL 单元中的 RBSP 数据结构的类型，其中 0 未指，1-19 在 H.264 协议中有定义，20-23 为 264 协议指定的保留位，24-29 在 RFC3984 中进行了指定。</li>
</ul>
<p>Type 后面的数据为 RBSP 的数据，需要注意的是：编码器的每个 slice 或者每帧头一般会有由0x000001 或者 0x00000001 作为起始头，在 RTP 封装中需要去掉。此外在 H.264 裸码流数据后面可能还会带有 padding 的数据由 RTP 头的 padding 位决定。</p>
<p><strong>STAP-A</strong></p>
<p>STAP-A 的作用是可以把多个 nal 单元封装在一个 RTP 包里面进行传输，需要注意：-A 的格式都是不允许跨帧的，也就是 nal 单元的时间戳必须是相同的。常见的场景是 sps 和 pps 两个小包被合并封装。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/832ac9efbb234df984ff55d38926daee~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>RTP 头后面仅跟着 STAP-A 的头，由 F、NRI 和 Type 组合而成，占一个字节，这里的 Type 为 24。后面两个字节为第一个 nalu 单元的长度，后面跟第一个 nalu 数据同 Single NAL Unit 的封装一致，第一个数据结束后，跟着第二个 nalu 的长度，占 2 个字节，依次类推。</p>
<p><strong>FU-A</strong></p>
<p>FU-A 的作用是把一个原始大的 nalu 切成多个数据包进行传输，主要使用场景在 slice 比较大的情况下。FU-A 比较特殊，有 FU-A 起始包、FU-A 包（如果只切两个包可能没有）和 FU-A 结束包组成。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c95e50185a934e688d1b584d95d375ad~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>FU indicator 占一个字节，由 F、NRI 和 Type 组合而成，这里的 Type 为28。</li>
<li>FU header 占一个字节：</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb7ff241e9aa4070947a15dbeacf20f3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>S： 占1位如果是1表示当前这个包是 FU-A 的起始包</li>
<li>E： 占1位如果是1表示当前这个包是 FU-A 的结束包</li>
<li>R： 占1位，保留位，为0</li>
<li>Type： 实际包含 nalu 的类型</li>
</ul>
<h2 data-id="heading-11">4 关于协议转换</h2>
<h3 data-id="heading-12">帧完整性判断</h3>
<p>为了实现微信小程序与云信 SDK、标准  WebRTC终端的互联互通，在协议转换时，无论是 RTMP 到 RTP 还是 RTP 到 RTMP，对于视频都需要首先拿到 H.264 数据，最重要则是对帧完整性的判断。</p>
<p>在 RTMPGateway 收到 RTP 视频包后，则需要先组成完整的帧才能再转封装成 RTMP 协议，失败则进行I帧请求。而仅根据 RTP 头部中的M比特判断完整性是不准确的，在 RTMPGateway 中，帧的完整性判断还需要满足 ：</p>
<ul>
<li>本帧包个数 = 本帧末包序 - 本帧首包序 + 1</li>
<li>本帧首包序 = 上一帧末包序 + 1</li>
</ul>
<p>下面以例子说明：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17445bbe0b41485baf9601bce09a7bac~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>帧1帧2正常进入转封装。</li>
<li>帧3超时，进行I帧请求，上一帧末包序置19。</li>
<li>帧4判断完整，非I帧，上一帧末包序置22。</li>
<li>帧5判断完整，且为I帧，进入转封装。</li>
<li>帧6超时，且丢失M包，上一帧末包序置27。</li>
<li>帧7一定超时，上一帧末包序置31。</li>
<li>帧8判断完整，且为I帧，进入转封装。</li>
</ol>
<h3 data-id="heading-13">音频转码</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fa0f4c701e24820806de14855323a4c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对于音频，因为微信小程序使用 AAC 编码，云信边缘媒体服务器支持 Opus 编码，因此在完成协议解封装后，还需要完成音频的转码。在云信 RTMPGateway 中，我们采用了独立的音频转码线程组，减轻逻辑处理线程的压力的目的。每个转码任务将被分配到固定的音频转码线程，线程根据任务数量进行负载均衡。</p>
<h2 data-id="heading-14">关于小程序用户和云信云端用户管理</h2>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ced3869ae02437984ee3e30086b4183~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>RTMPGateway 与小程序端间的信令采用 WebSocket 传输协议，此时 RTMPGateway 是 WebSocket 的服务端，接收来自小程序端的连接请求；RTMPGateway 与媒体服务器之间的信令同样采用 WebSocket 传输协议，此时 RTMPGateway 作为 WebSocket 的客户端，向媒体服务器发起连接请求。</p>
<ul>
<li>微信小程序端登录后除了在 RTMPGateway 创建对应的 mini-user 对象，还需要模拟成一个对应的 mini-fakeClient 向媒体服务器登录加入会议；</li>
<li>同时，RTMPGateway 在创建房间时，会针对这个房间模拟出一个特殊的用户 room-fakeClient 加入房间；</li>
<li>在广播房间及流信息时，如新的 NRTC 用户加入，媒体服务器会向所有的用户（包括mini-fakeClient、room-fakeClient）。对于 RTMPGateway，则只需要处理 room-fakeClient 收到的媒体服务器主动下发的信令，达到信令去重目的；</li>
<li>当新的 NRTC 用户加入房间，room-fakeClient 将收到广播信令，RTMPGateway 同步管理该 NRTC 用户（nrtc-user）状态。例如当收到该用户的发布流的信令后，将由 room-fakeClient 向媒体服务器发起订阅音视频流的请求。</li>
</ul>
<h2 data-id="heading-15">6 写在最后的话</h2>
<p>一个完整的微信小程序网关服务架构，除了完成上述的 RTMP 协议栈、媒体协议转封装、房间业务管理等基础模块，我们还需要考虑：</p>
<ul>
<li>RTMP 协议是基于 TCP 协议的，而 TCP 协议自身的一些拥塞算法，在弱网环境下对网络的退避策略过于激进，因此需要我们去寻求解决方案。例如在 RTMPGateway 中，对于 RTMP 下行在服务器引入 BBR 算法，通过直接修改内核 TCP 协议机制代码，达到更高的带宽利用率，降低卡顿。</li>
<li>关于 RTP 解封装后的音视频时间戳计算，可以有多种方案。例如在收到 SR 之前使用系统时间代替 NTP 时间，收到 SR 之后进行系统时间和 NTP 时间的误差修正；也可以在收到 SR 之前，将收到的第一个 RTP 包时间设置为起始时间，并使用固定采样频率根据公式计算时间戳，收到 SR 之后则先计算真实采样频率，再根据公式计算时间戳。为了进一步解决音画同步问题，在 RTMPGateway 中，对于 RTP 解封装后的音视频数据，将分别进入对应的 buffer，通过控制两个buffer的读取速度，以达到音画同步以及控制时延的目的。</li>
</ul>
<p>由于篇幅关系，更多细节不再展开，以上便是本次分享的全部内容。随着应用场景越来越多元化，比如企业内部 APP 移动工作台，系统集成电话呼叫功能，智能硬件，诸如智能门禁，智能机器人等将会对全终端的互通能力提出更高的要求，网易云信在这条赛道的探索会将持续进行，尽力满足用户不同场景的需求，真正做到助力用户内生长。</p>
<p>欢迎持续关注我们，了解更多网易云信关于微信小程序网关服务的技术探索和实践。</p>
<h3 data-id="heading-16">作者介绍</h3>
<p>本森，网易云信资深音视频服务端开发工程师，负责云信流媒体服务器、小程序网关服务器、 WebRTC 网关服务器及直播源站的开发工作，是帅的。</p>
<p>更多技术干货，欢迎关注【网易智企技术+】微信公众号</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            