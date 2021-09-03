
---
title: 'WebRTC浅析与实战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17da667b8b4b48c892e57b66d6b5960c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 02:09:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17da667b8b4b48c892e57b66d6b5960c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>目前市场上音视频技术方案大致分为以下几类，WebRTC因其超低延时、集成音视频采集传输等优点，是在线教育、远程会议等领域首选技术。</p>



































<table><thead><tr><th><strong>方案</strong></th><th><strong>优势</strong></th><th><strong>劣势</strong></th><th><strong>应用场景</strong></th></tr></thead><tbody><tr><td>基于浏览器插件的flash播放RTMP</td><td>即将淘汰</td><td>即将淘汰</td><td>传统直播</td></tr><tr><td>跨平台的HLS/DASH 播放方案</td><td>- 跨端广泛支持：苹果浏览器原生支持 <br><br>- hls.js <br></td><td>- 延时高 <br><br>- 碎片化 <br></td><td>传统直播，如赛事直播、大型会议直播<br></td></tr><tr><td>基于HTML5  MSE 能力的flv播放技术</td><td>- 格式简单 <br><br>- 无需插件 <br></td><td>- 移动端MSE支持性差 <br><br>- 一定延时 <br></td><td>传统直播，同上</td></tr><tr><td>WebRTC实时通讯技术</td><td>- 毫秒级的低延时 <br><br>- 音视频采集上行传输 <br></td><td>- 相对复杂 <br><br>- 支持度低 <br><br>- 价格高 <br><br>- 容量有限 <br></td><td>在线教育、远程会议</td></tr></tbody></table>
<p>WebRTC是 Google 在 2010 年收购 VoIP 软件开发商 GlobalIPSolutions 的 GIPS 引擎后，基于 GIPS 引擎实现的浏览器音视频和数据通信技术，在 2012 年集成到 chrome 浏览器，到目前为止，大部分主流现代浏览器都已经支持。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17da667b8b4b48c892e57b66d6b5960c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2998a7284834bd69467aa41cb82bd42~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">WebRTC架构</h2>
<p>一个简单的音视频架构大致如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecc802ac994a4790b0d45655f93e66ce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>音视频采集模块：调用系统API，从系统麦克风和摄像头读取设备并采集音视频数据。音频是PCM数据，视频是YUV数据</p>
</li>
<li>
<p>音视频编码模块：根据不同类型数据使用不同编码方式，将原始PCM、YUV数据压缩编码</p>
</li>
<li>
<p>网络传输模块：将压缩编码后的数据封装成RTP包，通过网络传输至对端，同时对端接收RTP数据</p>
</li>
<li>
<p>音视频解码模块：将接收到的压缩编码数据还原成原始的PCM、YUV/RGB数据</p>
</li>
<li>
<p>音视频渲染模块：拿到原始数据后，音频数据输出到扬声器，视频数据输出到显示器</p>
</li>
</ul>
<p>如果我们按照上面的架构实现一个音视频通信系统，相当于至少需要开发7个小模块，想想就费时费力。此时WebRTC就可以闪亮登场了，它内部标准化的实现上述架构，并在此基础上进行拓展，对外只暴露了相关的API，其架构图如下（ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebrtc.github.io%2Fwebrtc-org%2Farchitecture%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webrtc.github.io/webrtc-org/architecture/" ref="nofollow noopener noreferrer">官网</a> 的有点旧，重新画的）：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a4431423052466ba166766e817b32ad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>WebRTC大体可以分为四层：接口层、Session层、引擎层、设备层：</p>
<ul>
<li>
<p>接口层：暴露给业务侧，业务侧可以使用原生的 C++ API 接口或者 Web API 开发音视频实时通信。核心是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection" ref="nofollow noopener noreferrer"><code>RTCPeerConnection</code></a></p>
</li>
<li>
<p>Session层：用于控制业务逻辑，比如媒体协商、收集 Candidate 等</p>
</li>
<li>
<p>引擎层：包括音频引擎、视频引擎和网络传输</p>
</li>
<li>
<p>设备层：主要和硬件交互，负责音频的采集和播放，视频的采集，物理网络等</p>
</li>
</ul>
<h2 data-id="heading-2">WebRTC音视频通信过程</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f9b95bdcc0d4aea8b3241275a430df4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个正常音视频通信架构如上图所示，通信双方分别是 caller（主叫） 与 callee（被叫），两边的内部逻辑相似，下面以caller端为例，了解内部流程：</p>
<ol>
<li>
<p>调用音视频检测模块，检测终端是否有可用的音视频设备</p>
</li>
<li>
<p>调用音视频采集模块，采集用户音视频数据</p>
</li>
<li>
<p>根据用户选择，是否开启录制（授权）</p>
</li>
<li>
<p>通过信令模块交换SDP</p>
</li>
<li>
<p>创建WebRTC的核心对象RTCPeerConnection，之后添加采集到的音视频数据</p>
</li>
<li>
<p>RTCPeerConnection向STUN(SessionTraversal Utilities forNAT)/TURN(Traversal Using Relays aroundNAT)服务器发送请求，返回caller的外网ip地址和端口号</p>
</li>
<li>
<p>通过信令服务器，caller和callee互相传递对方的外网ip地址和端口（媒体协商）</p>
</li>
<li>
<p>最终P2P链接建立完成，后面就会源源不断的发送音视频数据到对端</p>
</li>
</ol>
<p>下面就是该过程对应的泳道图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/563a8ebec4d7440ba167f46180b22bdc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">信令服务器</h2>
<p>信令是实现音视频通信的重要一环，比如创建房间、离开房间、交换双端offer/answer以及candidate信息等。但WebRTC规范文档中并未定义信令相关的内容，因为不同业务，逻辑不同，信令也会千差万别，所以需要各个业务自己实现一套信令服务。
下面以socket.io为例，实现一套信令服务：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
<span class="hljs-keyword">const</span> &#123; Server &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'socket.io'</span>);

<span class="hljs-keyword">const</span> USER_LIMITS = <span class="hljs-number">3</span>;

<span class="hljs-keyword">const</span> app = express();
<span class="hljs-keyword">const</span> httpServer = http.createServer(app);
<span class="hljs-keyword">const</span> io = <span class="hljs-keyword">new</span> Server(httpServer);

<span class="hljs-keyword">const</span> getRoomUsers = <span class="hljs-function"><span class="hljs-params">room</span> =></span> &#123;
  <span class="hljs-keyword">const</span> myRoom = io.sockets.adapter.rooms[room];
  <span class="hljs-keyword">return</span> myRoom || [];
&#125;;

<span class="hljs-keyword">const</span> getRoomUsersCount = <span class="hljs-function"><span class="hljs-params">room</span> =></span> &#123;
  <span class="hljs-keyword">return</span> getRoomUsers(room).length;
&#125;;

<span class="hljs-comment">// 连接事件</span>
io.sockets.on(<span class="hljs-string">'connection'</span>, <span class="hljs-function"><span class="hljs-params">socket</span> =></span> &#123;
  <span class="hljs-comment">// 转发消息</span>
  socket.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">room, data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`message, room: <span class="hljs-subst">$&#123;room&#125;</span>, data type: <span class="hljs-subst">$&#123;data.<span class="hljs-keyword">type</span>&#125;</span>`</span>);
    socket.to(room).emit(<span class="hljs-string">'message'</span>, room, data);
  &#125;);

  <span class="hljs-comment">// 加入房间</span>
  socket.on(<span class="hljs-string">'join'</span>, <span class="hljs-function"><span class="hljs-params">room</span> =></span> &#123;
    socket.join(room);
    <span class="hljs-keyword">const</span> userCount = getRoomUsersCount(room);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`user join, room number <span class="hljs-subst">$&#123;userCount&#125;</span>`</span>);

    <span class="hljs-comment">// 房间未满员</span>
    <span class="hljs-keyword">if</span> (userCount < USER_LIMITS) &#123;
      <span class="hljs-comment">// 广播用户加入房间</span>
      socket.emit(<span class="hljs-string">'joined'</span>, room, socket.id);

      <span class="hljs-keyword">if</span> (userCount > <span class="hljs-number">1</span>) &#123;
        <span class="hljs-comment">// 广播其他用户加入房间</span>
        socket.to(room).emit(<span class="hljs-string">'otherJoin'</span>, room, socket.id);
      &#125;
    &#125;
    <span class="hljs-comment">// 房间满员</span>
    <span class="hljs-keyword">else</span> &#123;
      socket.leave(room);
      socket.emit(<span class="hljs-string">'full'</span>, room, socket.id);
    &#125;
  &#125;);

  socket.on(<span class="hljs-string">'leave'</span>, <span class="hljs-function"><span class="hljs-params">room</span> =></span> &#123;
    socket.leave(room);

    <span class="hljs-keyword">const</span> userCount = getRoomUsersCount(room);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`user leave, room number <span class="hljs-subst">$&#123;userCount&#125;</span>`</span>);

    <span class="hljs-comment">// 广播有用户退出房间</span>
    socket.to(room).emit(<span class="hljs-string">'exit'</span>, room, socket.id);

    socket.emit(<span class="hljs-string">'leaved'</span>, room, socket.id);
  &#125;);
&#125;);

httpServer.listen(<span class="hljs-string">'80'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">常用API</h2>
<blockquote>
<p>💡WebRTC的api返回值基本上都是Promise。</p>
</blockquote>
<h3 data-id="heading-5">获取设备 <code>enumerateDevices</code></h3>
<blockquote>
<p><code>navigator.mediaDevices.enumerateDevices()</code></p>
</blockquote>
<p>该API的返回值是一个 <code>Promise<MediaDeviceInfo[]></code> 。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> MediaDeviceInfo &#123;
  <span class="hljs-attr">deviceId</span>: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 设备的唯一编号</span>
  kind: MediaDeviceKind; <span class="hljs-comment">// 设备的类型</span>
  label: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 设备的名字</span>
  groupId: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 设备组编号，如果两个设备在同一个硬件上，则值是一致的</span>
&#125;

<span class="hljs-built_in">enum</span> MediaDeviceKind &#123;
   AudioInput = <span class="hljs-string">'audioinput'</span>, <span class="hljs-comment">// 麦克风</span>
   AudioOutput = <span class="hljs-string">'audiooutput'</span>, <span class="hljs-comment">// 扬声器</span>
   VideoInput = <span class="hljs-string">'videoinput'</span>, <span class="hljs-comment">// 摄像头</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个🌰，在控制台输入下面的命令：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">navigator.mediaDevices.enumerateDevices().then(<span class="hljs-function"><span class="hljs-params">deviceInfos</span> =></span> <span class="hljs-built_in">console</span>.table(deviceInfos))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/669fcf5bc3434e16afd6d416234ab37a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">采集音视频 <code>getUserMedia</code></h3>
<blockquote>
<p><code>navigator.mediaDevices.getUserMedia(constrains?: MediaStreamConstrains):Promise<MediaStream></code></p>
</blockquote>
<p>通过 <code>enumerateDevices</code> 方法获取音视频设备后，就可以调用 <code>getUserMedia</code> 方法指定设备采集音视频数据了。 <code>constrains</code> 详情参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaTrackConstraints" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints" ref="nofollow noopener noreferrer">MediaTrackConstraints - Web APIs | MDN</a></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> MediaStreamConstrains &#123;
  video?: MediaTrackConstrains | <span class="hljs-built_in">boolean</span>;
  audio?: MediaTrackConstrains | <span class="hljs-built_in">boolean</span>;
&#125;

<span class="hljs-keyword">interface</span> MediaTrackConstrains &#123;
  <span class="hljs-comment">// 视频相关</span>
  width?: ConstrainULong; <span class="hljs-comment">// 宽度</span>
  height?: ConstrainULong; <span class="hljs-comment">// 高度</span>
  aspectRatio?: ConstrainDouble; <span class="hljs-comment">// 宽高比</span>
  frameRate?: ConstrainDouble; <span class="hljs-comment">// 帧率</span>
  facingMode?: ConstrainDOMString; <span class="hljs-comment">// 前置/后置摄像头</span>
  resizeMode?: ConstrainDOMString; <span class="hljs-comment">// 缩放或裁剪</span>

  <span class="hljs-comment">// 音频相关</span>
  sampleRate?: ConstrainULong; <span class="hljs-comment">// 采样率</span>
  sampleSize?: ConstrainULong; <span class="hljs-comment">// 采样大小</span>
  echoCancellation?: ConstrainBoolean; <span class="hljs-comment">// 是否开启回音消除</span>
  autoGainControl?: ConstrainBoolean; <span class="hljs-comment">// 是否开启自动增益控制</span>
  noiseSuppression?: ConstrainBoolean; <span class="hljs-comment">// 是否开启降噪</span>
  latency?: ConstrainDouble; <span class="hljs-comment">// 目标延迟</span>
  channelCount?: ConstrainULong; <span class="hljs-comment">// 声道数量</span>

  <span class="hljs-comment">// 设备相关</span>
  deviceId?: ConstrainDOMString; <span class="hljs-comment">// 设备编号</span>
  groupId?: ConstrainDOMString; <span class="hljs-comment">// 设备组编号</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个🌰：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"video"</span> <span class="hljs-attr">autoplay</span>></span><span class="hljs-tag"></<span class="hljs-name">video</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> setLocalMediaStream = <span class="hljs-function"><span class="hljs-params">mediaStream</span> =></span> &#123;
    <span class="hljs-keyword">const</span> video = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'video'</span>);
    video.srcObject = mediaStream;
  &#125;;
  navigator.mediaDevices
      .getUserMedia(&#123;
        <span class="hljs-attr">video</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">audio</span>: <span class="hljs-literal">false</span>,
      &#125;)
      .then(setLocalMediaStream)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">核心对象 <code>RTCPeerConnection</code></h3>
<blockquote>
<p><code>new RTCPeerConnection(config: RTCConfiguration)</code></p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection" ref="nofollow noopener noreferrer">RTCPeerConnection</a> 对象是WebRTC的核心，同时也是暴露给用户的统一接口，内部包含了网络处理模块、服务质量模块、音视频引擎模块等，可以把它理解为一个socket，能够快速稳定的实现端到端的数据传输。
创建 <code>RTCPeerConnection</code> 对象时，需要传入STUN/TURN服务器等相关信息。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> RTCConfiguration &#123;
    bundlePolicy?: RTCBundlePolicy;
    certificates?: RTCCertificate[];
    iceCandidatePoolSize?: <span class="hljs-built_in">number</span>;
    iceServers?: RTCIceServer[];
    iceTransportPolicy?: RTCIceTransportPolicy;
    rtcpMuxPolicy?: RTCRtcpMuxPolicy;
&#125;

<span class="hljs-keyword">type</span> RTCBundlePolicy = <span class="hljs-string">"balanced"</span> | <span class="hljs-string">"max-bundle"</span> | <span class="hljs-string">"max-compat"</span>;
<span class="hljs-keyword">type</span> RTCIceCredentialType = <span class="hljs-string">"password"</span>;
<span class="hljs-keyword">type</span> RTCIceTransportPolicy = <span class="hljs-string">"all"</span> | <span class="hljs-string">"relay"</span>;
<span class="hljs-keyword">type</span> RTCRtcpMuxPolicy = <span class="hljs-string">"require"</span>;

<span class="hljs-keyword">interface</span> RTCCertificate &#123;
    <span class="hljs-keyword">readonly</span> expires: <span class="hljs-built_in">number</span>;
    getFingerprints(): RTCDtlsFingerprint[];
&#125;

<span class="hljs-keyword">interface</span> RTCDtlsFingerprint &#123;
    algorithm?: <span class="hljs-built_in">string</span>;
    value?: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">interface</span> RTCIceServer &#123;
    credential?: <span class="hljs-built_in">string</span>;
    credentialType?: RTCIceCredentialType;
    urls: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">string</span>[];
    username?: <span class="hljs-built_in">string</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个🌰：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-attr">iceServers</span>: [
    &#123;
      <span class="hljs-attr">urls</span>: <span class="hljs-string">'[stun:xxx.exmaple.com](http://stun:xxx.exmaple.com/)'</span>
    &#125;
  ]
&#125;;

<span class="hljs-keyword">const</span> pc = <span class="hljs-keyword">new</span> RTCPeerConnection(config);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">属性</h4>

















































<table><thead><tr><th><strong>属性名</strong></th><th><strong>描述</strong></th></tr></thead><tbody><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FcanTrickleIceCandidates" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/canTrickleIceCandidates" ref="nofollow noopener noreferrer">canTrickleIceCandidates</a><br></td><td>如果远端支持UDP打洞或支持通过中继服务器连接，则该属性值为true。否则，为false。该属性的值依赖于远端设置且仅在本地的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FsetRemoteDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/setRemoteDescription" ref="nofollow noopener noreferrer">RTCPeerConnection.setRemoteDescription()</a> 方法被调用时有效，如果该方法没被调用，则其值为null.</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FconnectionState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/connectionState" ref="nofollow noopener noreferrer">connectionState</a></td><td>返回由枚举RTCPeerConnectionState指定的字符串值之一来指示对等连接的当前状态。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FcurrentLocalDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/currentLocalDescription" ref="nofollow noopener noreferrer">currentLocalDescription</a></td><td>返回一个描述连接本地端的RTCSessionDescription对象。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FcurrentRemoteDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/currentRemoteDescription" ref="nofollow noopener noreferrer">currentRemoteDescription</a></td><td>返回一个描述连接远程端的RTCSessionDescription对象。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FiceConnectionState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/iceConnectionState" ref="nofollow noopener noreferrer">iceConnectionState</a></td><td>返回与RTCPeerConnection关联的ICE代理的状态类型为RTCIceConnectionState的枚举。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FiceGatheringState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/iceGatheringState" ref="nofollow noopener noreferrer">iceGatheringState</a></td><td>返回一个RTCIceGatheringState类型的结构体，它描述了连接的ICE收集状态</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FlocalDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/localDescription" ref="nofollow noopener noreferrer">localDescription</a></td><td>返回一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCSessionDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCSessionDescription" ref="nofollow noopener noreferrer">RTCSessionDescription</a> ，它描述了这条连接的本地端的会话控制（用户会话所需的属性以及配置信息）。如果本地的会话控制还没有被设置，它的值就会是null。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FpeerIdentity" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/peerIdentity" ref="nofollow noopener noreferrer">peerIdentity</a></td><td>返回一个RTCIdentityAssertion,它由一组信息构成，包括一个域名（idp）以及一个名称（name），它们代表了这条连接的远端机器的身份识别信息。如果远端机器还没有被设置以及校验，这个属性会返回一个null值。一旦被设置，它不能被一般方法改变。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FremoteDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/remoteDescription" ref="nofollow noopener noreferrer">remoteDescription</a></td><td>返回一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCSessionDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCSessionDescription" ref="nofollow noopener noreferrer">RTCSessionDescription</a> ，它描述了和远程对端之间的会话(包括配置和媒体信息) ，如果还没有被设置过的话，它会是 null.</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FsignalingState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/signalingState" ref="nofollow noopener noreferrer">signalingState</a></td><td>返回一个RTC通信状态的结构体，这个结构体描述了本地连接的通信状态。这个 状态描述了一个定义连接配置的SDPoffer。它包含了下列信息，与 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMediaStream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaStream" ref="nofollow noopener noreferrer">MediaStream</a> 类型本地相关的对象的描述，媒体流编码方式或RTP和 RTCP协议的选项 ，以及被ICE服务器收集到的candidates(连接候选者)。当 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FsignalingState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/signalingState" ref="nofollow noopener noreferrer">RTCPeerConnection.signalingState</a> 的值改变时，对象上的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FReference%2FEvents%2Fsignalingstatechange" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/Reference/Events/signalingstatechange" ref="nofollow noopener noreferrer">signalingstatechange</a> 事件会被触发。</td></tr></tbody></table>
<h4 data-id="heading-9">方法</h4>

















































































<table><thead><tr><th>方法名</th><th>描述</th></tr></thead><tbody><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FcreateOffer" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/createOffer" ref="nofollow noopener noreferrer">createOffer</a></td><td>生成一个offer，它是一个带有特定的配置信息寻找远端匹配机器（peer）的请求。这个方法的前两个参数分别是方法调用成功以及失败的回调函数，可选的第三个参数是用户对视频流以及音频流的定制选项（一个对象）。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FcreateAnswer" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/createAnswer" ref="nofollow noopener noreferrer">createAnswer</a></td><td>在协调一条连接中的两端offer/answers时，根据从远端发来的offer生成一个answer。这个方法的前两个参数分别是方法调用成功以及失败时的回调函数，可选的第三个参数是生成的answer的可供选项。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FsetLocalDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/setLocalDescription" ref="nofollow noopener noreferrer">setLocalDescription</a></td><td>改变与连接相关的本地描述。这个描述定义了连接的属性，例如：连接的编码方式。连接会受到它的改变的影响，而且连接必须能同时支持新的以及旧的描述。这个方法可以接收三个参数，一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCSessionDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCSessionDescription" ref="nofollow noopener noreferrer">RTCSessionDescription</a> 对象包含设置信息，还有两个回调函数，它们分别是方法调用成功以及失败的回调函数。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FsetRemoteDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/setRemoteDescription" ref="nofollow noopener noreferrer">setRemoteDescription</a></td><td>改变与连接相关的远端描述。这个描述定义了连接的属性，例如：连接的编码方式。连接会受到它的改变的影响，而且连接必须能同时支持新的以及旧的描述。这个方法可以接收三个参数，一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCSessionDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCSessionDescription" ref="nofollow noopener noreferrer">RTCSessionDescription</a> 对象包含设置信息，还有两个回调函数，它们分别是方法调用成功以及失败的回调函数。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FaddIceCandidate" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/addIceCandidate" ref="nofollow noopener noreferrer">addIceCandidate</a></td><td>添加iceCandidate时调用的方法</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FgetConfiguration" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/getConfiguration" ref="nofollow noopener noreferrer">getConfiguration</a></td><td>获取配置信息时调用的方法</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FgetSenders" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/getSenders" ref="nofollow noopener noreferrer">getLocalStreams</a></td><td>返回连接的本地媒体流数组。这个数组可能是空数组</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FgetReceivers" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/getReceivers" ref="nofollow noopener noreferrer">getRemoteStreams</a></td><td>返回连接的远端媒体流数组。这个数组可能是空数组</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FgetStreamById" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/getStreamById" ref="nofollow noopener noreferrer">getStreamById</a></td><td>返回连接中与所给id匹配的媒体流 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMediaStream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaStream" ref="nofollow noopener noreferrer">MediaStream</a> ，如果没有匹配项，返回null</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FaddStream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/addStream" ref="nofollow noopener noreferrer">addStream</a></td><td>添加一个媒体流 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMediaStream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaStream" ref="nofollow noopener noreferrer">MediaStream</a> 作为本地音频或视频源。如果本地端与远端协调已经发生了，那么需要一个新的媒体流，这样远端才可以使用它</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FremoveStream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/removeStream" ref="nofollow noopener noreferrer">removeStream</a></td><td>将一个作为本地音频或视频源的媒体流 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMediaStream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaStream" ref="nofollow noopener noreferrer">MediaStream</a> 移除。如果本地端与远端协调已经发生了，那么需要一个新的媒体流，这样远端才可以停止使用它</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FaddTrack" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/addTrack" ref="nofollow noopener noreferrer">addTrack</a></td><td>将一个新的媒体轨道添加到一组轨道中，这些轨道将被传输给另一个对等点。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FremoveTrack" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/removeTrack" ref="nofollow noopener noreferrer">removeTrack</a></td><td>移除轨道中的某个轨道，停止发送到对等点。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2Fclose" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/close" ref="nofollow noopener noreferrer">close</a></td><td>关闭一个RTCPeerConnection实例所调用的方法</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FcreateDataChannel" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/createDataChannel" ref="nofollow noopener noreferrer">createDataChannel</a></td><td>在一条连接上建立一个新的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCDataChannel" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCDataChannel" ref="nofollow noopener noreferrer">RTCDataChannel</a> （用于数据发送）。这个方法把一个数据对象作为参数，数据对象中包含必要的配置信息</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FgetStats" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/getStats" ref="nofollow noopener noreferrer">getStats</a></td><td>生成一个新的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCStatsReport" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCStatsReport" ref="nofollow noopener noreferrer">RTCStatsReport</a> ，它包含连接相关的统计信息</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FsetIdentityProvider" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/setIdentityProvider" ref="nofollow noopener noreferrer">setIdentityProvider</a></td><td>根据所给的三个参数设置身份提供者（IdP)，这三个参数是它的名称，通信所使用的协议（可选），以及一个可选的用户名。只有当一个断言被需要时，这个IdP才会被使用。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FgetIdentityAssertion" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/getIdentityAssertion" ref="nofollow noopener noreferrer">getIdentityAssertion</a></td><td>初始化身份断言的收集，只有当 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FsignalingState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/signalingState" ref="nofollow noopener noreferrer">signalingState</a> 的值不为"closed"时，它才有效。它自动完成，在需求发生前调用它是最好的选择。</td></tr></tbody></table>
<h4 data-id="heading-10">事件</h4>









































<table><thead><tr><th><strong>事件名</strong></th><th><strong>描述</strong></th></tr></thead><tbody><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2Fonaddstream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/onaddstream" ref="nofollow noopener noreferrer">onaddstream</a></td><td>当 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMediaStream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaStream" ref="nofollow noopener noreferrer">MediaStream</a> 被远端机器添加到这条连接时，该事件会被触发。 当调用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FsetRemoteDescription" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/setRemoteDescription" ref="nofollow noopener noreferrer">RTCPeerConnection.setRemoteDescription()</a> 方法时，这个事件就会被立即触发，它不会等待SDP协商的结果。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2Fondatachannel" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/ondatachannel" ref="nofollow noopener noreferrer">ondatachannel</a></td><td>当一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCDataChannel" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCDataChannel" ref="nofollow noopener noreferrer">RTCDataChannel</a> 被添加到连接时，这个事件被触发。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2Fonicecandidate" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/onicecandidate" ref="nofollow noopener noreferrer">onicecandidate</a></td><td>当一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidate" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCIceCandidate" ref="nofollow noopener noreferrer">RTCICECandidate</a> 对象被添加时，这个事件被触发。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2Foniceconnectionstatechange" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/oniceconnectionstatechange" ref="nofollow noopener noreferrer">oniceconnectionstatechange</a></td><td>当 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FiceConnectionState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCPeerConnection/iceConnectionState" ref="nofollow noopener noreferrer">iceConnectionState</a> 改变时，这个事件被触发。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2Fonnegotiationneeded" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/onnegotiationneeded" ref="nofollow noopener noreferrer">onnegotiationneeded</a></td><td>浏览器发送该事件以告知在将来某一时刻需要协商。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2Fonremovestream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/onremovestream" ref="nofollow noopener noreferrer">onremovestream</a></td><td>当一条 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMediaStream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaStream" ref="nofollow noopener noreferrer">MediaStream</a> 从连接上移除时，该事件被触发。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2Fonsignalingstatechange" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/onsignalingstatechange" ref="nofollow noopener noreferrer">onsignalingstatechange</a></td><td>当 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2FsignalingState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/signalingState" ref="nofollow noopener noreferrer">signalingState</a> 的值发生改变时，该事件被触发。</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnection%2Ftrack_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/track_event" ref="nofollow noopener noreferrer">ontrack</a></td><td>当新轨道加入时，该事件被触发。</td></tr></tbody></table>
<p>下面以绑定本地音视频数据为例，说明api的使用方法。
目前 RTCPeerConnection 提供了两种方法用来绑定音视频数据：addTrack() 和 addSteam() ，其中 addStream 已经被官方标记为废弃，推荐使用 addTrack() 方法，这两个方法可以转换：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">peerConnection.addStream(mediaStream);
<span class="hljs-comment">// 等价于</span>
mediaStream.getTracks().forEach(<span class="hljs-function"><span class="hljs-params">track</span> =></span> &#123;
  peerConnection.addTrack(track, mediaStream);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面以 addTrack 为例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> localMediaStream = <span class="hljs-literal">null</span>;

<span class="hljs-keyword">const</span> setLocalMediaStream = <span class="hljs-function"><span class="hljs-params">mediaStream</span> =></span> &#123;
  localMediaStream = mediaStream;
&#125;;

navigator.mediaDevices
  .getUserMedia(&#123;
    <span class="hljs-attr">video</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">audio</span>: <span class="hljs-literal">false</span>,
  &#125;)
  .then(setLocalMediaStream);

<span class="hljs-keyword">const</span> bindTracks = <span class="hljs-function">() =></span> &#123;
  localMediaStream
    .getTracks()
    .forEach(<span class="hljs-function"><span class="hljs-params">track</span> =></span> &#123;
      peerConnection.addTrack(track, localMediaStream);
    &#125;)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">媒体协商</h2>
<p>媒体协商就是在双端通信之前，了解双方具备哪些能力。其协商过程中交换的内容就是SDP协议定义的。</p>
<h3 data-id="heading-12">会话描述协议SDP</h3>
<p>SDP（SessionDescription Protocol）是一个2006年发布的老协议，以 <code><type>=<value></code> 的格式描述会话内容，其中 <code><type></code> 表示描述的目标，由单个字符构成； <code><value></code> 是对 <code><type></code> 的描述和约束，包括音视频编解码器类型、传输协议等，详情可以查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc4566" target="_blank" rel="nofollow noopener noreferrer" title="https://datatracker.ietf.org/doc/html/rfc4566" ref="nofollow noopener noreferrer">RFC4566</a> 。WebRTC引入SDP来描述媒体信息，用于媒体协商，决定双端使用何种方式通信。
SDP协议的具体格式如下，分为两部分：会话描述和媒体描述。其中带星号（*）的表示可选。</p>
<pre><code class="hljs language-lisp copyable" lang="lisp">Session description
    v=  (<span class="hljs-name">protocol</span> version)
    o=  (<span class="hljs-name">originator</span> and session identifier)
    s=  (<span class="hljs-name">session</span> name)
    i=* (<span class="hljs-name">session</span> information)
    u=* (<span class="hljs-name">URI</span> of description)
    e=* (<span class="hljs-name">email</span> address)
    p=* (<span class="hljs-name">phone</span> number)
    c=* (<span class="hljs-name">connection</span> information -- not required if included in all media)
    b=* (<span class="hljs-name">zero</span> or more bandwidth information lines)
    [...One or more time descriptions (<span class="hljs-string">"t="</span> and <span class="hljs-string">"r="</span> lines)]
    z=* (<span class="hljs-name">time</span> zone adjustments)
    k=* (<span class="hljs-name">encryption</span> key)
    a=* (<span class="hljs-name">zero</span> or more session attribute lines)
    [...Zero or more media descriptions]

Time description
    <span class="hljs-literal">t</span>=  (<span class="hljs-name">time</span> the session is active)
    r=* (<span class="hljs-name">zero</span> or more repeat times)

Media description, if present
    m=  (<span class="hljs-name">media</span> name and transport address)
    i=* (<span class="hljs-name">media</span> title)
    c=* (<span class="hljs-name">connection</span> information -- optional if included at session level)
    b=* (<span class="hljs-name">zero</span> or more bandwidth information lines)
    k=* (<span class="hljs-name">encryption</span> key)
    a=* (<span class="hljs-name">zero</span> or more media attribute lines)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个🌰：</p>
<pre><code class="hljs language-apache copyable" lang="apache"><span class="hljs-attribute">v</span>=<span class="hljs-number">0</span>
<span class="hljs-attribute">o</span>=jdoe <span class="hljs-number">2890844526</span> <span class="hljs-number">2890842807</span> IN IP<span class="hljs-number">4</span> <span class="hljs-number">10.47.16.5</span>
<span class="hljs-attribute">s</span>=SDP Seminar
<span class="hljs-attribute">i</span>=A Seminar <span class="hljs-literal">on</span> the session description protocol
<span class="hljs-attribute">u</span>=[http://www.example.com/seminars/sdp.pdf](http://www.example.com/seminars/sdp.pdf)<span class="hljs-meta">
[e](mailto:e=j.doe@example.com)[=j.doe@example.com](mailto:e=j.doe@example.com) (Jane Doe)
c=IN IP4 224.2.17.12/127
t=2873397496 2873404696
a=recvonly
m=audio 49170 RTP/AVP 0
m=video 51372 RTP/AVP 99
a=rtpmap:99 h263-1998/90000
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">协商流程</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc00d6d0bfe4c0b8fe62379e4ccd291~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>caller生成本地描述信息</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> offer = <span class="hljs-keyword">await</span> peerConnection.createOffer()
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>caller设置本地描述信息</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">await</span> peerConnection.setLocalDescription(offer);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>caller发送本地描述信息至远端</li>
</ol>
<pre><code class="hljs language-scala copyable" lang="scala">const signalServer = <span class="hljs-keyword">new</span> <span class="hljs-type">WebSocket</span>(<span class="hljs-symbol">'ws</span>:<span class="hljs-comment">//[xxx.signal.com](http://xxx.signal.com/)');</span>

signalServer.send(&#123;
  <span class="hljs-class"><span class="hljs-keyword">type</span></span>: <span class="hljs-symbol">'offe</span>r',
  data: offer,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>callee设置远端描述信息</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">await</span> peerConnection.setRemoteDescription(offer);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>callee生成本地应答描述信息</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> answer = <span class="hljs-keyword">await</span> peerConnection.createAnswer();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>callee设置本地描述信息</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">await</span> peerConnection.setLocalDescription(answer);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>callee发送answer描述信息至远端</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> signalServer = <span class="hljs-keyword">new</span> WebSocket(<span class="hljs-string">'ws://[xxx.signal.com](http://xxx.signal.com/)'</span>);

signalServer.send(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'answer'</span>,
  <span class="hljs-attr">data</span>: answer,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>callee设置远端描述信息</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">peerConnection.setRemoteDescription(answer);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">交互式连接建立 ICE</h3>
<p>当各端调用 setLocalDescription 后，WebRTC就开始建立网络连接，主要包括收集candidate、交换candidate和按优先级尝试连接，该过程被称为ICE（Interactive Connectivity Establishment，交互式连接建立）。其中每个 candidate 都包含IP地址、端口、传输协议、类型等信息。
根据 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc5245" target="_blank" rel="nofollow noopener noreferrer" title="https://datatracker.ietf.org/doc/html/rfc5245" ref="nofollow noopener noreferrer">RFC5245</a> 协议，WebRTC将 candidate分为了四个类型：host、srflx、prflx、relay，它们的优先级依次降低。</p>
<ul>
<li>
<p>host：Host Candidate，根据主机的网卡数量决定，一般一个网卡对应一个ip地址，然后给每个ip随机分配一个端口生成</p>
</li>
<li>
<p>srflx：Server Reflexive Candidate，根据STUN服务器获得的ip和端口生成</p>
</li>
<li>
<p>prflx：Peer Reflexive Candidate，根据对端的ip和端口生成</p>
</li>
<li>
<p>relay：Relayed Candidate，根据TURN服务器获得的ip和端口生成</p>
</li>
</ul>
<h2 data-id="heading-15">网络地址转换NAT</h2>
<p>NAT在真实网络环境中随处可见，主要由两个用处：</p>
<ul>
<li>
<p>解决IPv4地址不够用的问题，可以让多台主机共用一个公网IP</p>
</li>
<li>
<p>安全问题，将主机隐藏在内网中，外网就比较难访问到真实主机</p>
</li>
</ul>
<h3 data-id="heading-16">NAT类型</h3>
<p>根据 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Frfc3489%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://datatracker.ietf.org/doc/rfc3489/" ref="nofollow noopener noreferrer">RFC3489</a> 协议，NAT总共分成4种类型：完全锥型（Full ConeNAT）、IP限制锥型（Address Restricted ConeNAT）、端口限制锥型（Port Restricted ConeNAT）、对称型（SymmetrictNAT），依次检测越来越严格。</p>
<blockquote>
<p>💡所谓“打洞”，其实就是在 NAT 建立一个内外网的映射表。包括内网IP和端口，以及映射的外网IP和端口。</p>
</blockquote>
<h4 data-id="heading-17">完全锥型</h4>
<p>NAT打洞成功后，所有知道该洞的主机都可以通过它与内网主机进行通信。映射表内容如下：</p>
<pre><code class="hljs language-html copyable" lang="html">&#123;
  内网ip，
  内网端口，
  映射的外网ip，
  映射的外网端口
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子：从同一私网地址端口192.168.0.8:4000发至公网的所有请求都映射成同一个公网地址端口1.2.3.4:62000 ，192.168.0.8可以收到任意外部主机发到1.2.3.4:62000的数据报。</p>
<h4 data-id="heading-18">IP限制锥型</h4>
<p>NAT打洞成功后，只有打洞成功的外网主机才能通过该洞与内网主机通信，其他外网主机即使知道洞口也不能内网主机通信。映射表内容如下：</p>
<pre><code class="hljs language-html copyable" lang="html">&#123;
  内网ip，
  内网端口，
  映射的外网ip，
  映射的外网端口，
  [被访问主机的ip，....]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子：从同一私网地址端口192.168.0.8:4000发至公网的所有请求都映射成同一个公网地址端口1.2.3.4:62000，只有当内部主机192.168.0.8先给服务器C 6.7.8.9发送一个数据报后，192.168.0.8才能收到6.7.8.9发送到1.2.3.4:62000的数据报。</p>
<h4 data-id="heading-19">端口限制锥型</h4>
<p>除了像IP限制锥型一样对IP进行检测以外，还需要检测端口。映射表内容如下：</p>
<pre><code class="hljs language-html copyable" lang="html">&#123;
  内网ip，
  内网端口，
  映射的外网ip，
  映射的外网端口，
  [
    &#123;被访问主机的ip，被访问主机的端口&#125;，
    ...
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子：从同一私网地址端口192.168.0.8:4000发至公网的所有请求都映射成同一个公网地址端口1.2.3.4:62000，只有当内部主机192.168.0.8先向外部主机地址端口6.7.8.9:8000发送一个数据报后，192.168.0.8才能收到6.7.8.9:8000发送到1.2.3.4:62000的数据报。</p>
<h4 data-id="heading-20">对称型</h4>
<p>内网主机每次访问不同的外网时，都需要打一个新洞，而不像前面三种NAT类型使用的是同一个“洞”，即只有收到过一个数据包的外部主机才能够向该内部主机发送数据包，映射表内容如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  内网ip，
  内网端口，
  <span class="hljs-comment">// 不仅访问地址变化，映射ip也要发生变化</span>
  映射的外网ip，
  <span class="hljs-comment">// 不仅访问端口变化，映射端口也要发生变化</span>
  映射的外网端口，
  被访问主机的ip，
  被访问主机的端口
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">NAT类型检测</h3>
<blockquote>
<p>💡下述算法在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc3489" target="_blank" rel="nofollow noopener noreferrer" title="https://tools.ietf.org/html/rfc3489" ref="nofollow noopener noreferrer">RFC 3489</a> 被提出，但在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc5389" target="_blank" rel="nofollow noopener noreferrer" title="https://tools.ietf.org/html/rfc5389" ref="nofollow noopener noreferrer">RFC 5389</a> 中被删除。因为随着发展，NAT类型比协议中描述的更多种多样，检测过程变得比较脆弱。更详细的原因可以到 RFC 5389 的Page 45中‘ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc5389%23section-19" target="_blank" rel="nofollow noopener noreferrer" title="https://datatracker.ietf.org/doc/html/rfc5389#section-19" ref="nofollow noopener noreferrer">19.Changes since RFC 3489</a> ’查看。</p>
</blockquote>
<p>下面（ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F6%2F63%2FSTUN_Algorithm3.svg" target="_blank" rel="nofollow noopener noreferrer" title="https://upload.wikimedia.org/wikipedia/commons/6/63/STUN_Algorithm3.svg" ref="nofollow noopener noreferrer">原图</a> ）就是内网主机进行NAT类型检测的算法流程，总共需要2台STUN服务器，每台STUN服务器又需要两块网卡，每块网卡都需要配置公网ip地址。
如果双端都进入红色部分，则表示无法通信，进入黄色或者绿色就有打洞通信的可能性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa47e60586d249c3bc89d9f9b4a4d538~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-22">检测是否具备通信能力（Test1）</h4>
<ul>
<li>
<p>客户端建立UDPsocket，然后用这个socket向服务器 Server#1 的（IP-1，Port-1）发送数据包，要求服务器从（IP-1，Port-1）返回客户端的IP和Port，客户端发送请求后立即开始接收数据包。</p>
<ul>
<li>
<p>如果超时收不到服务器的响应，则说明客户端无法进行UDP通信，表明：防火墙阻止UDP通信；</p>
</li>
<li>
<p>如果能收到回应，则比较服务器返回的客户端（ip:port）与本地的（ip:port）是否一致；</p>
</li>
</ul>
</li>
<li>
<p>如果完全相同则表明：客户端具有公网IP，然后进行防火墙检测；</p>
</li>
<li>
<p>如果不同，则表明：客户端在NAT后，要做进一步的NAT类型检测（继续）。</p>
</li>
</ul>
<h4 data-id="heading-23">检测是否具有防火墙（Test2）</h4>
<ul>
<li>
<p>客户端向服务器 Server#1 的（IP-1，PORT-1）发送请求，要求服务器从（IP-2，PORT-2）向客户端发送数据包：</p>
<ul>
<li>
<p>如果客户端能够收到数据包，则认为客户端处在一个开放的网络上，网络类型为公开的互联网IP</p>
</li>
<li>
<p>否则客户端被前置防火墙拦截，判断为对称型网络；</p>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-24">检测是否为完全锥型网络（Test2）</h4>
<ul>
<li>
<p>客户端向服务器的（IP-1，Port-1）发送数据包，并要求服务器从（IP-2，Port-2）向客户端发回一个响应数据包，客户端发送请求后立即开始接受数据包。</p>
<ul>
<li>
<p>如果能够接受到服务器从(IP-2,Port-2)返回的应答UDP包，则说明客户端是一个完全锥型网络。</p>
</li>
<li>
<p>否则进行下一步检测（继续）；</p>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-25">检测是否为对称型（Test1#2）</h4>
<ul>
<li>
<p>客户端向另一台STUN服务器 Server#2 的 （IP-3，Port-3）发送请求，要求服务器从（IP-3，Port-3）返回客户端的ip和端口。</p>
<ul>
<li>
<p>如果服务端返回的客户端ip与本地ip不一致，则表明是对称型网络；</p>
</li>
<li>
<p>否则，表明是限制型网络，进行下一步检测（继续）；</p>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-26">检测为IP限制锥型 or 端口限制锥型（Test3）</h4>
<ul>
<li>
<p>客户端向另一台STUN服务器 Server#2 的 （IP-3，Port-3）发送请求，要求服务器从（IP-3，Port-4）返回客户端的ip和端口。</p>
<ul>
<li>
<p>如果收到数据，则表明是：IP限制锥形网络；</p>
</li>
<li>
<p>否则表明是：端口限制锥形网络。</p>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-27">实战</h2>
<p>接下来开发一个本地1v1通信的简单demo以及附加的拍照功能.</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>WebRTC Demo<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      <span class="hljs-selector-tag">video</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"localVideo"</span> <span class="hljs-attr">autoplay</span>></span><span class="hljs-tag"></<span class="hljs-name">video</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"remoteVideo"</span> <span class="hljs-attr">autoplay</span>></span><span class="hljs-tag"></<span class="hljs-name">video</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"startBtn"</span>></span>打开摄像头<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"callBtn"</span>></span>建立远程连接<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"hangupBtn"</span>></span>断开远程连接<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"photoBtn"</span> <span class="hljs-attr">disabled</span>></span>拍照<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"photoContainer"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> startBtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"startBtn"</span>);
    <span class="hljs-keyword">const</span> callBtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"callBtn"</span>);
    <span class="hljs-keyword">const</span> hangupBtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"hangupBtn"</span>);
    <span class="hljs-keyword">const</span> photoBtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"photoBtn"</span>);
    <span class="hljs-keyword">const</span> photoContainer = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"photoContainer"</span>);
    <span class="hljs-keyword">const</span> photoCtx = photoContainer.getContext(<span class="hljs-string">"2d"</span>);

    startBtn.addEventListener(<span class="hljs-string">"click"</span>, startHandle);
    callBtn.addEventListener(<span class="hljs-string">"click"</span>, callHandle);
    hangupBtn.addEventListener(<span class="hljs-string">"click"</span>, hangupHandle);
    photoBtn.addEventListener(<span class="hljs-string">"click"</span>, photoHandle);

    <span class="hljs-comment">// 本地流</span>
    <span class="hljs-keyword">let</span> localStream;
    <span class="hljs-comment">// 远端流</span>
    <span class="hljs-keyword">let</span> remoteStream;

    <span class="hljs-comment">// 本地连接对象</span>
    <span class="hljs-keyword">let</span> localPeerConnection;
    <span class="hljs-comment">// 远端连接对象</span>
    <span class="hljs-keyword">let</span> remotePeerConnection;

    <span class="hljs-comment">// 本地视频</span>
    <span class="hljs-keyword">const</span> localVideo = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"localVideo"</span>);
    <span class="hljs-comment">// 远端视频</span>
    <span class="hljs-keyword">const</span> remoteVideo = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"remoteVideo"</span>);

    <span class="hljs-comment">// 设置约束</span>
    <span class="hljs-keyword">const</span> mediaStreamConstraints = &#123;
      <span class="hljs-attr">video</span>: <span class="hljs-literal">true</span>,
    &#125;;

    <span class="hljs-comment">// 仅交换视频</span>
    <span class="hljs-keyword">const</span> offerOptions = &#123;
      <span class="hljs-attr">offerToReceiveVideo</span>: <span class="hljs-number">1</span>,
    &#125;;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">startHandle</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开启本地摄像头"</span>);
      startBtn.disabled = <span class="hljs-literal">true</span>;
      navigator.mediaDevices
        .getUserMedia(mediaStreamConstraints)
        .then(setLocalMediaStream)
        .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.error(<span class="hljs-string">"getUserMedia"</span>, err);
        &#125;);
    &#125;

    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callHandle</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"建立远端连接"</span>);
      callBtn.disabled = <span class="hljs-literal">true</span>;
      hangupBtn.disabled = <span class="hljs-literal">false</span>;
      photoBtn.disabled = <span class="hljs-literal">false</span>;

      <span class="hljs-comment">// 本地直连，没有STUN服务器</span>
      <span class="hljs-keyword">const</span> rtcConfig = <span class="hljs-literal">null</span>;

      <span class="hljs-comment">// 1. 创建 RTCPeerConnection</span>
      createLocalPeerConnection(rtcConfig);
      createRemotePeerConnection(rtcConfig);

      <span class="hljs-comment">// 2.添加本地音视频流</span>
      addLocalStream();

      <span class="hljs-comment">/** 媒体协商 */</span>
      <span class="hljs-comment">// 2.创建SDP offer</span>
      <span class="hljs-keyword">const</span> offer = <span class="hljs-keyword">await</span> createOffer(offerOptions);
      <span class="hljs-comment">// 3.设置本地SDP offer</span>
      setLocalDescription(localPeerConnection, offer);
      <span class="hljs-comment">// 4.远端设置远端SDP offer</span>
      setRemoteDescription(remotePeerConnection, offer);
      <span class="hljs-comment">// 5.远端创建SDP answer</span>
      <span class="hljs-keyword">const</span> answer = <span class="hljs-keyword">await</span> createAnswer();
      <span class="hljs-comment">// 6.远端设置本地SDP answer</span>
      setLocalDescription(remotePeerConnection, answer);
      <span class="hljs-comment">// 7.本地设置SDP answer</span>
      setRemoteDescription(localPeerConnection, answer);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hangupHandle</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"断开远端连接"</span>);
      <span class="hljs-comment">// 关闭连接并设置为空</span>
      localPeerConnection.close();
      remotePeerConnection.close();
      localPeerConnection = <span class="hljs-literal">null</span>;
      remotePeerConnection = <span class="hljs-literal">null</span>;
      hangupBtn.disabled = <span class="hljs-literal">true</span>;
      callBtn.disabled = <span class="hljs-literal">false</span>;
      photoBtn.disabled = <span class="hljs-literal">true</span>;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">photoHandle</span>(<span class="hljs-params"></span>) </span>&#123;
      photoContainer.setAttribute(<span class="hljs-string">"width"</span>, localVideo.videoWidth);
      photoContainer.setAttribute(<span class="hljs-string">"height"</span>, localVideo.videoHeight);
      photoCtx.drawImage(localVideo, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createLocalPeerConnection</span>(<span class="hljs-params">rtcConfig</span>) </span>&#123;
      <span class="hljs-comment">// 创建本地 RTCPeerConnection 对象</span>
      localPeerConnection = <span class="hljs-keyword">new</span> RTCPeerConnection(rtcConfig);
      <span class="hljs-comment">// 监听本地返回的 Candidate</span>
      localPeerConnection.addEventListener(<span class="hljs-string">"icecandidate"</span>, handleICEConnection);
      <span class="hljs-comment">// 监听本地 ICE 状态变化</span>
      localPeerConnection.addEventListener(
        <span class="hljs-string">"iceconnectionstatechange"</span>,
        handleICEConnectionChange
      );
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRemotePeerConnection</span>(<span class="hljs-params">rtcConfig</span>) </span>&#123;
      <span class="hljs-comment">// 创建远端 RTCPeerConnection 对象</span>
      remotePeerConnection = <span class="hljs-keyword">new</span> RTCPeerConnection(rtcConfig);
      <span class="hljs-comment">// 监听远端返回的 Candidate</span>
      remotePeerConnection.addEventListener(
        <span class="hljs-string">"icecandidate"</span>,
        handleICEConnection
      );
      <span class="hljs-comment">// 监听远端 ICE 状态变化</span>
      remotePeerConnection.addEventListener(
        <span class="hljs-string">"iceconnectionstatechange"</span>,
        handleICEConnectionChange
      );
      <span class="hljs-comment">// 监听远端轨道添加</span>
      remotePeerConnection.addEventListener(<span class="hljs-string">"track"</span>, setRemoteMediaStream);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addLocalStream</span>(<span class="hljs-params"></span>) </span>&#123;
      localStream.getTracks().forEach(<span class="hljs-function">(<span class="hljs-params">track</span>) =></span> &#123;
        localPeerConnection.addTrack(track, localStream);
      &#125;);
    &#125;

    <span class="hljs-comment">// 设置本地媒体流</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setLocalMediaStream</span>(<span class="hljs-params">mediaStream</span>) </span>&#123;
      localVideo.srcObject = mediaStream;
      localStream = mediaStream;
      callBtn.disabled = <span class="hljs-literal">false</span>;
    &#125;

    <span class="hljs-comment">// 设置本地SDP</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setLocalDescription</span>(<span class="hljs-params">peerConnection, description</span>) </span>&#123;
      <span class="hljs-keyword">return</span> peerConnection.setLocalDescription(description);
    &#125;

    <span class="hljs-comment">// 生成SDP offer</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createOffer</span>(<span class="hljs-params">options</span>) </span>&#123;
      <span class="hljs-keyword">return</span> localPeerConnection.createOffer(options);
    &#125;

    <span class="hljs-comment">// 生成SDP answer</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAnswer</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> remotePeerConnection.createAnswer();
    &#125;

    <span class="hljs-comment">// 设置远端SDP</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setRemoteDescription</span>(<span class="hljs-params">peerConnection, description</span>) </span>&#123;
      <span class="hljs-keyword">return</span> peerConnection.setRemoteDescription(description);
    &#125;

    <span class="hljs-comment">// 端与端建立连接</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleICEConnection</span>(<span class="hljs-params">event</span>) </span>&#123;
      <span class="hljs-comment">// 获取到触发 icecandidate 事件的 RTCPeerConnection 对象</span>
      <span class="hljs-comment">// 获取到具体的Candidate</span>
      <span class="hljs-keyword">const</span> peerConnection = event.target;
      <span class="hljs-keyword">const</span> iceCandidate = event.candidate;

      <span class="hljs-keyword">if</span> (iceCandidate) &#123;
        <span class="hljs-comment">// 创建 RTCIceCandidate 对象</span>
        <span class="hljs-keyword">const</span> newIceCandidate = <span class="hljs-keyword">new</span> RTCIceCandidate(iceCandidate);
        <span class="hljs-comment">// 得到对端的 RTCPeerConnection</span>
        <span class="hljs-keyword">const</span> otherPeer = getOtherPeer(peerConnection);

        <span class="hljs-comment">// 将本地获得的 Candidate 添加到远端的 RTCPeerConnection 对象中</span>
        otherPeer.addIceCandidate(newIceCandidate);
      &#125;
    &#125;

    <span class="hljs-comment">// 显示远端媒体流</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setRemoteMediaStream</span>(<span class="hljs-params">event</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (remoteVideo.srcObject !== event.streams[<span class="hljs-number">0</span>]) &#123;
        remoteVideo.srcObject = event.streams[<span class="hljs-number">0</span>];
        remoteStream = event.streams[<span class="hljs-number">0</span>];
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始接收远端音视频流"</span>);
      &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleICEConnectionChange</span>(<span class="hljs-params">event</span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"ICE连接状态改变: "</span>, event);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getOtherPeer</span>(<span class="hljs-params">peerConnection</span>) </span>&#123;
      <span class="hljs-keyword">return</span> peerConnection === localPeerConnection
        ? remotePeerConnection
        : localPeerConnection;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed9bc23c09d447ddb4c2517f07915c0e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-28">参考文档</h2>
<p><a href="https://juejin.cn/post/7000205126719766565" target="_blank" title="https://juejin.cn/post/7000205126719766565">浅聊WebRTC视频通话</a><br>
<a href="https://juejin.cn/post/6896045087659130894#heading-1" target="_blank" title="https://juejin.cn/post/6896045087659130894#heading-1">从0到1打造一个 WebRTC 应用</a><br>
<a href="https://juejin.cn/post/6884851075887661070" target="_blank" title="https://juejin.cn/post/6884851075887661070">前端音视频WebRTC实时通讯的核心</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fu011330638%2Farticle%2Fdetails%2F81107312" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/u011330638/article/details/81107312" ref="nofollow noopener noreferrer">音视频开发基础概述 - PCM、YUV、H264、常用软件介绍</a><br>
《 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fe.jd.com%2F30731934.html" target="_blank" rel="nofollow noopener noreferrer" title="https://e.jd.com/30731934.html" ref="nofollow noopener noreferrer">WebRTC音视频实时互动技术——李超</a> 》
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebrtc.github.io%2Fwebrtc-org%2Farchitecture%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webrtc.github.io/webrtc-org/architecture/" ref="nofollow noopener noreferrer">官网 WebRTC 架构</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F1432c729df4d" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/1432c729df4d" ref="nofollow noopener noreferrer">STUN(RFC3489)的NAT类型检测方法</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnewteo%2Fteam-blog-repo%2Fissues%2F19" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/newteo/team-blog-repo/issues/19" ref="nofollow noopener noreferrer">webRTC连接过程详细剖析,及阶段总结 - github</a></p></div>  
</div>
            