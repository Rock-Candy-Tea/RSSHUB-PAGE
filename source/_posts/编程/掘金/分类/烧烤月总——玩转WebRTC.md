
---
title: '烧烤月总——玩转WebRTC'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/770a32bd6c7d43bcb6fee10353b4c26b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 18:47:51 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/770a32bd6c7d43bcb6fee10353b4c26b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>有个需求：实现两个人的实时视频通话。</p>
<p>在WebRTC还没有诞生之前，你可能会首先想到直播手段：采流 -> 推流 -> 拉流。但是，如果把这个过程放在web浏览器去实现，估计很多人提交辞职报告。因此WebRTC的诞生就是想让让这种需求的实现变得简单。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/770a32bd6c7d43bcb6fee10353b4c26b~tplv-k3u1fbpfcp-watermark.image" alt="在线客服处理流程图 (2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>WebRTC是什么？底层原理是什么？怎么用？让烧烤哥给你娓娓道来！</p>
<h2 data-id="heading-0">什么是WebRTC？</h2>
<p>WebRTC全称Web Real-time Communication，网页即使通讯技术。它是由Google发起的一个的实时通讯解决方案。之所以称为一个方案，而不是协议，是因为它涵盖了音视频采集、通讯的建立、信息传输、音视频显示等整套的实现方案。该方案的发起让加快速地实现一个音视频通讯应用成为可能。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e90ae022e2fb4c96a6e43b290556b412~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你是web开发者，通过浏览器提供的WebRTC API可以轻松的实现音视频的采集和播放，实现端对端的通讯通道的建立，并可通过建立的通道实现音视频的数据的共享。</p>
<p>虽然WebRTC看起来是浏览器的玩意，但是由于谷歌的开源精神，它可以通过编译C++的代码实现全平台互通。所以，如果你想通过web远程控制windows电脑，可以让你的C++的小朋友接一波WebRTC，WebRTC还支持实时采集桌面哦！</p>
<h2 data-id="heading-1">WebRTC是如何实现端对端的音视频共享的？</h2>
<p>传统的资源共享更多的是通过一个中转服务器进行交换的。把对方想要的资源提前上传到固定的公网服务器中，然后再通过地址进行访问。这种形式好的好处是可靠性非常强，因为资源服务器是固定的，不会受传输方和使用方的网络影响，非常灵活可靠！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4866c8375a80426ba53581a548d1260e~tplv-k3u1fbpfcp-watermark.image" alt="demo.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是，实时性很差。需要等到对方把文件上传完成之后才可以下载文件。当然，这个流程也可以达到实时的，可以在服务器搭建一个文件流中转，让到达服务器的文件流立即传输给拉取方。如此麻烦，为什么不省略掉这个服务器呢？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34085cfa2e37410496341d228195ecd5~tplv-k3u1fbpfcp-watermark.image" alt="demo (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">P2P连接</h3>
<p>P2P全称peer to perr，学术名称为对等网络，它是一种网络技术和网络拓扑结构。建立起P2P连接的设备可以不经过第三方服务的转发，就可以达到1对1的信息传输交换。</p>
<p>那么如何创建一个P2P的连接呢？这里我们先看看现实的互联网世界是这样进行通讯的！</p>
<h4 data-id="heading-3">现实的网络世界</h4>
<p>现实世界中的网络是这样的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/325644b5737f4c028a5ac6dcf0e00c7d~tplv-k3u1fbpfcp-watermark.image" alt="demo (2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为目前互联网大部分部署的网际协议（IP协议）版本是IPV4，然而IPV4使用的是32位2进制的地址，能够产生43亿个IP地址，如果每一个用户终端都以独立的IP地址接入互联网，那么这43亿的地址将不够分。</p>
<p>所以目前的网络结构基本是多设备终端通过一层或多层的NAT代理接入到互联网中，也就是局域网。</p>
<h4 data-id="heading-4">NAT是什么？</h4>
<p>NAT：网络地址转换，它是一种解决专用网络内设备连接公网的技术。</p>
<p>那么NAT的工作原理是什么呢？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2839dfcbb0be49c796bb563c5206356c~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>当设备A想发送一个请求到服务器172.20.98.44:7777 => 8.8.8.8:23456，首先请求会先到达NAT，由NAT修改报文的源地址和源端口以及相应的校验码，然后才会发送给服务器，此时就形成流一个映射关系：</li>
</ul>
<pre><code class="copyable">172.20.98.44:7777 => 6.6.6.6:12345 => 8.8.8.8:23456
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当服务器处理完成请求后响应数据返回到NAT时，NAT根据映射关系，修改目的地址和目的端口以及相应的校验码，然后再发送给设备A：</li>
</ul>
<pre><code class="copyable">8.8.8.8:23456 => 6.6.6.6:12345 => 172.20.98.44:7777
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是NAT使得内网设备能够正常访问公网服务器到原理特性。</p>
<p>处于内网中的设备可以借助NAT实现公网服务器的访问，但是在P2P连接中可能两个设备都处于不同的内网中，这两个设备如何进行P2P连接呢？</p>
<h4 data-id="heading-5">NAT穿透技术</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a3592c0861640648fdf52b9a0fe686f~tplv-k3u1fbpfcp-watermark.image" alt="demo (4).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>要使得处于两个内网中的两个设备能够建立P2P连接的技术方案被统称为NAT穿透技术。一般来说，P2P可以建立UDP连接也可以建立TCP连接，所以这个机制又被称作<b>UDP打洞</b>或<b>TCP打洞</b>。因为webRTC使用的传输层协议是UDP协议，所以我这里主要讲解<b>UDP打洞</b>原理。</p>
<ul>
<li>第一步，添加一个信使服务器。信使服务器的作用是发现、记录内网设备在NAT中映射的端口以及其NAT的公网IP。这种服务器也被称为STUN服务器。根据NAT的特性，当设备A向STUN服务器发送请求时，会形成映射关系：<b>172.20.98.44:7777 => 6.6.6.6:12345 => 3.3.3.3:34567</b>，这时STUN服务器将6.6.6.6:12345响应给设备A。同样的，设备B也进行响应的请求以获取对应的映射关系。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a6b96f129414b2cbf4e8b30b1a21efc~tplv-k3u1fbpfcp-watermark.image" alt="demo (9).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>交换映射关系。设备A和设备B需要将自己在NAT的映射关系交换，为下一步建立连接做准备。这里需要另外协议进行交换。</li>
<li>交换完成之后，设备A向设备B的NAT-B地址<b>8.8.8.8:23456</b>发送请求包，因为这个请求不是设备B主动发起的，为了安全考虑，NAT-B接收到这个请求包之后不会转发给设备B，而是抛弃掉，但是NAT-A根据特性记录这个映射关系，后面从地址<b>8.8.8.8:23456</b>发来的包都会转发给设备A。同样的，设备B也向<b>6.6.6.6:12345</b>发起同样的请求，让NAT-B知道后面从<b>6.6.6.6:12345</b>发来的请求都转发给设备B。</li>
<li>完成上面的动作之后，设备A和设备B就可以建立P2P连接愉快的发送消息了。当然这个连接需要心跳包维持，防止被close掉。</li>
</ul>
<p>上面就是一个完整的UDP打动过程，完成打洞之后设备就可以跨过NAT实现P2P连接了。</p>
<h3 data-id="heading-6">WebRTC是基于UDP实现的端对端连接</h3>
<p>基于前面认知，WebRTC实现端对端的音视频传输也需要处理UDP打洞这个过程。在我们调用WebRTC创建端对端的连接时并不会去实现这个UDP打洞的过程（如果要，那就和提出WebRTC的初衷相背离了，<b>实现方便快捷地建立音视频即时通讯是WebRTC所追求的</b>）。更多的，我们需要按照流程调用API去完成WebRTC的创建。</p>
<h2 data-id="heading-7">从创建WebRTC连接中学习WebRTC的API使用</h2>
<p>一起看一下创建连接的整个过程：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cb372db929540878425bc8026e102b0~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件 (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>信令服务器：一种用于信息交换的服务，它在WebRTC过程中的作用是作为端交换建立连接所需要的信息。这个信令服务器实现不在WebRTC的方案范围，因为这个实现更贴近业务本身，而且有更多的实现方式搭配不同的业务场景。</p>
</blockquote>
<blockquote>
<p>虽然WebRTC的兼容性很不错（除了那个不可一世的IE），但是每个浏览器在提供顶层API的时候还是存在差异的，所以我们需要一个垫片解决这个差异：<a href="https://github.com/webrtcHacks/adapter" target="_blank" rel="nofollow noopener noreferrer">webrtcHacks/adapter</a></p>
</blockquote>
<p>分解一下：</p>
<ol>
<li>创建RTC实例。WebRTC提供了用于实例化连接的API RTCPeerConnection。下示代码，其中<strong>configuration</strong>可选，<strong>configuration</strong>用于配置STUN/TURN服务器信息的。这里STUN/TURN服务器也是需要自己搭建，有需求的看<a href="https://developer.aliyun.com/article/243478" target="_blank" rel="nofollow noopener noreferrer">部署stun和turn服务器</a>。</li>
</ol>
<pre><code class="copyable">let connection = new RTCPeerConnection([configuration]);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果不配制configuration，那意味着这个连接只能在内网进行。</p>
</blockquote>
<ol start="2">
<li>访问摄像头麦克风设备。通过下示代码可以不依赖任何插件的情况下打开摄像头麦克风（此时浏览器会请求授权）并获取媒体流。其中<strong>constraints</strong>指请求的媒体类型和相对应的参数；<strong>mediaStream</strong>指的是媒体流，可以将<strong>mediaStream</strong>赋值给video元素的srcObject属性实现实时媒体流播放。更多关于mediaDevices信息可以看<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaDevices" target="_blank" rel="nofollow noopener noreferrer">这里</a></li>
</ol>
<pre><code class="copyable">navigator.mediaDevices.getUserMedia(constraints)
    .then(function(mediaStream) &#123; ... &#125;)
    .catch(function(error) &#123; ... &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>getUserMedia在本地环境localhost以及可信域名（https）情况下才能够正常获取媒体流，否则会报错。</p>
</blockquote>
<ol start="3">
<li>将媒体流加入到RTCPeerConnection实例中。</li>
</ol>
<pre><code class="copyable">connection.addTrack(mediaStream.getVideoTracks()[0], stream);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>交换SDP。WebRTC使用的是Offer-Answer应答模式交换Offer。首先由发起方通过createOffer创建Offer SDP，通过信令服务传递给接收方；接收方通过createAnswer创建Answer SDP，通过信令服务器传递给发起方。双方需要通过setLocalDescription、setRemoteDescription将自己生成和对等方传来的SDP设置到连接中。</li>
</ol>
<blockquote>
<p><b>SDP(Session Description Protocol)</b> 是一种会话描述协议，基于文本，其本身并不属于传输协议，需要依赖其它的传输协议（比如 SIP 和 HTTP）来交换必要的媒体信息，用于两个会话实体之间的媒体协商。SDP里面包含了建立会话需要的媒体信息、网络信息、安全特性、传输策略。</p>
</blockquote>
<blockquote>
<p>注意：如果传输的是音视频流，在生成Offer SDP之前需要通过addTrack将媒体流添加到信道中，原因是生成SDP时需要采集流信息。如果不添加，则不会生存SDP。</p>
</blockquote>
<pre><code class="copyable">//添加流媒体信息
connection.addTrack(stream.getVideoTracks()[0], stream);

//发起方创建Offer SDP
connection
    .createOffer()
    .then((sessionDescription) => &#123;
        console.log("发送offer");
        if (connection) &#123;
            console.log("设置本地description");
            connection.setLocalDescription(sessionDescription);
        &#125;

        sendMessage(sessionDescription, targetId);
    &#125;)
    .catch(() => &#123;
        console.log("offer create error");
    &#125;);
    
//接收方设置远端描述
connection.setRemoteDescription(             
   new RTCSessionDescription(sessionDescription)         
);

//接收方生成Answer SDP
connection
    .createAnswer()
    .then((sessionDescription) => &#123;
        console.log("发送answer");

        if (connection) &#123;
            console.log("设置本地description");
            connection.setLocalDescription(sessionDescription);
        &#125;
        sendMessage(sessionDescription, targetId);
    &#125;)
    .catch(() => &#123;
        console.log("创建answer失败");
    &#125;);

//发起方设置远端描述
connection.setRemoteDescription(             
   new RTCSessionDescription(sessionDescription)         
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、交换候选人信息candidate。连接双方通过监听RTCPeerConnection的icecandidate事件得到本身的候选人信息，然后通过信令服务传输给对等方。候选人信息candidate交换是建立webRTC连接的重要步骤。得到对等方的candidate之后，需要实例化RTCIceCandidate对象，然后通过RTCPeerConnection的addIceCandidate方法添加到Rtc实例中。</p>
<blockquote>
<p>候选人信息candidate包含了当前设备所对应的NAT映射信息，包括：ip、端口、协议</p>
</blockquote>
<blockquote>
<p>icecandidate事件触发的时机是在setLocalDescription执行之后。</p>
</blockquote>
<pre><code class="copyable">//监听icecandidate的触发
connection.addEventListener("icecandidate", (event) => &#123;
    if (event.candidate) &#123;
        console.log("发送candidate", event.candidate.candidate);
        sendMessage(
            &#123;
                type: "candidate",
                label: event.candidate.sdpMLineIndex,
                id: event.candidate.sdpMid,
                candidate: event.candidate.candidate,
            &#125;,
            targetId
        );
    &#125; else &#123;
        console.log("End of candidates.");
    &#125;
&#125;);

//添加候选人信息
const candidate = new RTCIceCandidate(&#123;
    sdpMLineIndex: message.label,
    candidate: message.candidate,
&#125;);
connection.addIceCandidate(candidate).catch((error) => &#123;
    console.log(error);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上大概是完成整个WebRTC建立连接所需要的API，除此之外，还有很多关于连接的实践监听、关于创建连接过程中音视频编码的协商、以建立data channel的方式创建WebRTC连接等等API，有兴趣的可以查阅<a href="https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API" target="_blank" rel="nofollow noopener noreferrer">WebRTC API</a>。</p>
<h2 data-id="heading-8">实战</h2>
<p>了解玩WebRTC的一些主要API，让我们一起实战完成一个例子——开篇所说的实现两个人的实时通讯，这里我们来实现多人的同时视频通讯。这里主要是基于内网实现的例子，通过内网ip访问服务。</p>
<p>这里的实现主要分两部分，遵循前后端分离的思想，一部分是信令服务的实现，一部分是前端交互页面的实现。</p>
<h3 data-id="heading-9">第一步，创建信令服务：express + socke.io</h3>
<p>前面说过，信令服务最主要的作用是创建连接时的信息中继。这里为了简单实现功能，使用的是node的express框架以及可支持双向通讯的socket.io;</p>
<h4 data-id="heading-10">创建Https服务</h4>
<p>因为我们的网页如果需要多人在线视频通话，那我们的网站时需要分享出去的。前面说过，只有localhost或者可行地址才能访问浏览器媒体设备。所以这里为了避免跨协议所带来的问题，需要创建一个https服务。</p>
<pre><code class="copyable">const app = require("express")();
const fs = require("fs");
//读取证书
const key = fs.readFileSync(
    "/Users/XXX/Documents/study/https/172.20.210.160.key",
    "utf8"
);
const cert = fs.readFileSync(
    "/Users/XXX/Documents/study/https/172.20.210.160.crt",
    "utf8"
);

const http = require("https").Server(
    &#123;
        key,
        cert,
    &#125;,
    app
);

//监听3005端口
http.listen(3005, function () &#123;
    console.log("listening on *:3005");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其实创建https还可以通过配置nginx的形式，这里我比较不想搞nginx，所以就代码实现了。</p>
</blockquote>
<h4 data-id="heading-11">跨域设置</h4>
<p>因为页面和信令服务是两个不同的服务，会存在跨域的问题，入口文件需要加入以下代码：</p>
<pre><code class="copyable">const allowCors = function (req, res, next) &#123;
    res.header("Access-Control-Allow-Origin", req.headers.origin);
    res.header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS");
    res.header("Access-Control-Allow-Headers", "Content-Type");
    res.header("Access-Control-Allow-Credentials", "true");
    next();
&#125;;
app.use(allowCors);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">socket.io信息中继机制的实现。</h4>
<p>实现很简单，代码完成一个机制，不得不赞叹开源世界的伟大。</p>
<pre><code class="copyable">const socketIo = require("socket.io");

function createSocketIo(httpInstance) &#123;
    //初始化实例，支持跨域
    const io = socketIo(httpInstance, &#123;
        cors: &#123;
            origin: "*",
            allowedHeaders: ["Content-Type"],
            methods: ["GET,PUT,POST,DELETE,OPTIONS"],
        &#125;,
    &#125;);
    //监听每一个连接
    io.on("connection", function (socket) &#123;
        //监听连接上的单个端，同时像其他端发送新人加入消息
        socket.on("connect", () => &#123;
            console.log("连上了");
            socket.joinRoom("demo", () => &#123;
                socket.broadcast.to("demo").emit("new", socket.id);
            &#125;);
        &#125;);
        //消息中转
        socket.on("message", (message) => &#123;
            if (message.target) &#123;
                socket.to(message.target).emit("message", &#123;
                    originId: socket.id,
                    data: message.data,
                &#125;);
            &#125;
            else &#123;
                socket.broadcast.to('demo').emit("message", &#123;
                    originId: socket.id,
                    data: message.data,
                &#125;);
            &#125;
        &#125;);
    &#125;);
&#125;

module.exports = createSocketIo;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">第二步，前端交互界面的实现</h3>
<p>前端交互界面主要的作用是通过信令服务与加入房间的端建立WebRTC连接。</p>
<p>这里用户交互界面使用<a href="https://zh-hans.reactjs.org/docs/create-a-new-react-app.html" target="_blank" rel="nofollow noopener noreferrer">creat-react-app</a>快速创建项目。</p>
<p>其中用户交互界面两部分，一部分是WebRTC的创建连接的逻辑，另一部分是socket.io的交互逻辑。</p>
<h4 data-id="heading-14">封装WebRTC连接，支持多对等方连接</h4>
<pre><code class="copyable">//无敌垫片
import "webrtc-adapter";

class ConnectWebrtc &#123;
    protected connection: RTCPeerConnection | null;
    constructor() &#123;
        this.connection = null;
    &#125;

    //创建RTCPeerConnection实例，同时监听icecandidate，track事件
    create(
        onAddStream: EventListenerOrEventListenerObject,
        onReomveStream: EventListenerOrEventListenerObject,
        onCandidate: (candidate: RTCIceCandidate) => void
    ) &#123;
        this.connection = new RTCPeerConnection(undefined);

        this.connection.addEventListener("icecandidate", (event) => &#123;
            if (event.candidate) &#123;
                onCandidate(event.candidate);
            &#125; else &#123;
                console.log("End of candidates.");
            &#125;
        &#125;);
        this.connection.addEventListener("track", onAddStream);
        this.connection.addEventListener("removeTrack", onReomveStream);
    &#125;

    //创建offer sdp
    createOffer(
        onSessionDescription: (
            sessionDescription: RTCSessionDescriptionInit
        ) => void
    ) &#123;
        if (this.connection) &#123;
            this.connection
                .createOffer()
                .then((sessionDescription) => &#123;
                    if (this.connection) &#123;
                        this.connection.setLocalDescription(sessionDescription);
                        onSessionDescription(sessionDescription);
                    &#125;
                &#125;)
                .catch(() => &#123;
                    console.log("offer create error");
                &#125;);
        &#125;
    &#125;
    
    //创建answer sdp
    createAnswer(
        onSessionDescription: (
            sessionDescription: RTCSessionDescriptionInit
        ) => void
    ) &#123;
        if (this.connection) &#123;
            this.connection
                .createAnswer()
                .then((sessionDescription) => &#123;
                    if (this.connection) &#123;
                        this.connection.setLocalDescription(sessionDescription);
                    &#125;

                    onSessionDescription(sessionDescription);
                &#125;)
                .catch(() => &#123;
                    console.log("创建answer失败");
                &#125;);
        &#125;
    &#125;

    //设置远端描述
    setRemoteDescription(
        sessionDescription: RTCSessionDescriptionInit | undefined
    ) &#123;
        this.connection?.setRemoteDescription(
            new RTCSessionDescription(sessionDescription)
        );
    &#125;

    //设置候选人
    setCandidate(message: any) &#123;
        if (this.connection) &#123;
            const candidate = new RTCIceCandidate(&#123;
                sdpMLineIndex: message.label,
                candidate: message.candidate,
            &#125;);
            this.connection.addIceCandidate(candidate).catch((error) => &#123;
                console.log(error);
            &#125;);
        &#125;
    &#125;

    //讲媒体流添加到连接中
    addTrack(stream: MediaStream) &#123;
        if (this.connection) &#123;
            this.connection.addTrack(stream.getVideoTracks()[0], stream);
            this.connection.addTrack(stream.getAudioTracks()[0], stream);
        &#125;
    &#125;

    //从连接中删除媒体流
    removeTrack() &#123;
        if (this.connection) &#123;
            this.connection.removeTrack(this.connection.getSenders()[0]);
        &#125;
    &#125;
&#125;

export default ConnectWebrtc;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过封装创建连接到关键步骤，可以实现创建多个WebRTC的连接。</p>
<h4 data-id="heading-15">页面交互组件与socket.io连接</h4>
<pre><code class="copyable">import &#123; useEffect, useRef, useState &#125; from "react";
import &#123; io, Socket &#125; from 'socket.io-client';
import &#123; server &#125; from "./config";
import ConnectWebrtc from "./webrtc";

//媒体设备采集配置
const mediaStreamConstraints = &#123;
    video: &#123;
        width: 400,
        height: 400
    &#125;,
    audio: true
&#125;;

const Room = () => &#123;
    //本地流
    const localStream = useRef<MediaStream>();
    //播放本地流的video标签
    const localVideoRef = useRef<HTMLVideoElement>(null);
    //保存多个连接实例对象
    const connectList = useRef<&#123; [target: string]: any &#125;>(&#123;&#125;);
    //连接用户的列表
    const [userlist, setUserList] = useState<string[]>([]);
    //socket.io实例
    let socket = useRef<Socket>();

    //发送消息到指定对等方
    const sendMessage = (data: any, targetId?: string | null) => &#123;
        socket.current?.emit('message', &#123;
            target: targetId,
            data
        &#125;)
    &#125;
    
    //将对等方传来的媒体流添加到指定video标签中
    const handeStreamAdd = (originId: string) => (event: any) => &#123;
        let video = document.getElementById(originId) as HTMLVideoElement;

        if (video) &#123;
            video.srcObject = event.streams[0];
        &#125;
    &#125;

    //获取与指定对等方WebRTC连接实例，如果不存在，则创建
    const getConnection = (originId: string) => &#123;
        let connection = connectList.current?.[originId];
        if (!connection) &#123;
            connection = new ConnectWebrtc();
            connection.create(handeStreamAdd(originId), () => &#123; &#125;, (candidate: RTCIceCandidate) => &#123;
                sendMessage(
                    &#123;
                        type: "candidate",
                        label: candidate.sdpMLineIndex,
                        id: candidate.sdpMid,
                        candidate: candidate.candidate,
                    &#125;,
                    originId
                );
            &#125;);
            
            //优先将媒体流添加到连接中
            connection.addTrack(localStream.current);
            connectList.current[originId] = connection;
        &#125;
        return connection;
    &#125;

    //创建与信令服务的socket.io连接
    const handleConnectIo = () => &#123;
        socket.current = io(server);
        socket.current.on('connect', () => &#123;
            console.log('连上了');
        &#125;);

        //监听消息
        socket.current.on('message', function (message) &#123;
            //添加对等方
            if (!userlist.includes(message.originId)) &#123;
                userlist.push(message.originId);
                setUserList([...userlist])
            &#125;
     
            let connection = getConnection(message.originId);
            
            //当作为接收方时，设置远端描述，并创建answer sdp
            if (message.data.type === 'offer') &#123;
                connection.setRemoteDescription(message.data);
                connection.createAnswer((sdp) => &#123;
                   sendMessage(sdp, originId); 
                &#125;);
            &#125; 
            //当作为发起方时，收到answer sdp则设置为远端描述
            else if (message.data.type === 'answer') &#123;
                connection.setRemoteDescription(message.data);
            &#125; 
            //当收到候选人信息时，将候选人信息加入到连接中
            else if (message.data.type === 'candidate') &#123;
                connection.setCandidate(message.data);
            &#125;
        &#125;);

        //当收到新用户加入房间时，主动发起WebRTC连接
        socket.current.on('new', (newId) => &#123;
            const connection = getConnection(newId);
            connection.createOffer((sdp) => &#123;
                   sendMessage(sdp, originId); 
            &#125;);

            if (!userlist.includes(newId)) &#123;
                userlist.push(newId);
                setUserList([...userlist])
            &#125;
        &#125;)
    &#125;
    
    //打开本地媒体设备并设置到video标签中进行播放
    const handleGetLocalStream = (callback: () => void) => &#123;
        navigator.mediaDevices.getUserMedia(mediaStreamConstraints)
            .then((mediaStream) => &#123;
                localStream.current = mediaStream;

                if (localVideoRef.current) &#123;
                    localVideoRef.current.srcObject = mediaStream;
                &#125;
                callback();
            &#125;).catch((error) => &#123;
                console.log(error)
            &#125;);
    &#125;

    //组件挂载是优先打开媒体设备然后再建立socket.io连接
    useEffect(() => &#123;
        handleGetLocalStream(() => &#123;
            handleConnectIo();
        &#125;);
    &#125;, []);

    return (
        <div>
            <div style=&#123;&#123; marginTop: 20 &#125;&#125;>
                <p>我的画面</p>
                <video ref=&#123;localVideoRef&#125; autoPlay playsInline ></video>
            </div>
            <div style=&#123;&#123; marginTop: 20 &#125;&#125;>
                <p>其他人的画面</p>
                &#123;
                    userlist.map(user => &#123;
                        return <video id=&#123;user&#125; key=&#123;user&#125; autoPlay playsInline></video>
                    &#125;)
                &#125;
            </div>
        </div>
    )
&#125;

export default Room;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的这段组件代码清晰的展示了信令服务在整个WebRTC连接过程中的重要作用，可以说是主导整个流程的进行。整个过程还有很多细节还没有实现，但这不是我这里所要追求的。更重要的展示多方WebRTC实时通讯连接建立的大致实现过程。</p>
<p>实现的效果与头部的样子差不多，这里就不展示了。</p>
<h2 data-id="heading-16">延伸</h2>
<p>用一张图表示上面实战中用户之间的关系：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a45226a0d93143aba584a58e10ea76ec~tplv-k3u1fbpfcp-watermark.image" alt="demo (10).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>错综复杂的关系，如果再加几百几万个连进来，那岂不是爆炸了。</p>
<p>所以，P2P连接是一种去中心化的连接方式，它适用于小量的连接，对于大量的连接需要的，最后还是的得回归中心化思想，由中心服务去实现去中心的能力（如CDN）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d47ef10165e545f7b584a9387b4c18fc~tplv-k3u1fbpfcp-watermark.image" alt="demo (12).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>乍一看，这不会又回到了传统的音视频直播的路子了。那我为什么要选择WebRTC呢？</p>
<p><b>从技术选型等角度上说，WebRTC对比其他的音视频协议具有更好的兼容性和可扩展性（因为它是开源的）；再者，WebRTC连接的延时更低，这对于现要求实时性互动性越来越高的直播行业是一个非常不错的方案。</b></p>
<table class="relative-table wrapped confluenceTable"><thead><tr><th class="confluenceTh">协议</th><th class="confluenceTh">延时</th><th class="confluenceTh">数据分段</th><th class="confluenceTh">HTML5直播</th><th class="confluenceTh">应用场景</th><th class="confluenceTh" colspan="1">前端相关插件</th></tr></thead><tbody><tr><td class="confluenceTd">HLS</td><td class="confluenceTd">10~30s</td><td class="confluenceTd">切片</td><td class="confluenceTd">支持</td><td class="confluenceTd">H5直播，游戏直播</td><td class="confluenceTd" colspan="1"><a href="https://github.com/video-dev/hls.js/" target="_blank" rel="nofollow noopener noreferrer">hls.js</a></td></tr><tr><td class="confluenceTd">RTMP</td><td class="confluenceTd">2s~5s</td><td class="confluenceTd">连续流</td><td class="confluenceTd">不支持</td><td class="confluenceTd">互动直播</td><td class="confluenceTd" colspan="1"><br></td></tr><tr><td class="confluenceTd">HTTP-FLV</td><td class="confluenceTd">2s~5s，优于rtmp</td><td class="confluenceTd">连续流</td><td class="confluenceTd">支持</td><td class="confluenceTd">互动直播</td><td class="confluenceTd" colspan="1"><a href="https://github.com/Bilibili/flv.js/" target="_blank" rel="nofollow noopener noreferrer">flv.js</a></td></tr><tr><td class="confluenceTd">flv</td><td class="confluenceTd">一般做到500ms以下</td><td class="confluenceTd">连续流</td><td class="confluenceTd">不支持</td><td class="confluenceTd">互动直播</td><td class="confluenceTd" colspan="1"><br></td></tr><tr><td class="confluenceTd" colspan="1">webRTC</td><td class="confluenceTd" colspan="1">1s内</td><td class="confluenceTd" colspan="1">连续流</td><td class="confluenceTd" colspan="1">支持（兼容性）</td><td class="confluenceTd" colspan="1">互动娱乐</td><td class="confluenceTd" colspan="1">原生</td></tr></tbody></table>
<p>目前已经有一些对实时互动要求高的行业在使用WebRTC方案了。可以说是前景很光明。</p>
<h2 data-id="heading-17">总结</h2>
<p>本文从原理到实战角度简单剖析了WebRTC，WebRTC是一个很复杂的方案，肯定不是我这一篇文章能够讲得通的。如果有不对地方，欢迎指正。</p>
<h2 data-id="heading-18">最后</h2>
<p>觉得烧烤哥写的不错的，点赞关注吧；如有不足的地方，请不吝指正。</p>
<blockquote>
<p>关注「前端烧烤摊」 掘金 & 微信公众号, 第一时间获取烧烤哥前的总结与发现。</p>
</blockquote></div>  
</div>
            