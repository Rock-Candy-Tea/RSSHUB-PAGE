
---
title: '使用 PeerJS 轻松实现 P2P 通信'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://cdn-images-1.medium.com/max/5760/1*-Rh8z0kzvXKz_BbONP60Yw.jpeg'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 21:23:51 GMT
thumbnail: 'https://cdn-images-1.medium.com/max/5760/1*-Rh8z0kzvXKz_BbONP60Yw.jpeg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.bitsrc.io%2Fsimplified-peer-to-peer-communication-with-peerjs-e37244267723" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.bitsrc.io/simplified-peer-to-peer-communication-with-peerjs-e37244267723" ref="nofollow noopener noreferrer">Simplified Peer to Peer Communication with PeerJS</a></li>
<li>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2F%40dulanka" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/@dulanka" ref="nofollow noopener noreferrer">Dulanka Karunasena</a></li>
<li>译文出自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%2Fblob%2Fmaster%2Farticle%2F2021%2Fsimplified-peer-to-peer-communication-with-peerjs.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner/blob/master/article/2021/simplified-peer-to-peer-communication-with-peerjs.md" ref="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FTong-H" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Tong-H" ref="nofollow noopener noreferrer">tong-h</a></li>
<li>校对者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjaredliw" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jaredliw" ref="nofollow noopener noreferrer">jaredliw</a>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCarlosChenN" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/CarlosChenN" ref="nofollow noopener noreferrer">CarlosChenN</a></li>
</ul>
</blockquote>
<h1 data-id="heading-0">使用 PeerJS 轻松实现 P2P 通信</h1>
<p><img src="https://cdn-images-1.medium.com/max/5760/1*-Rh8z0kzvXKz_BbONP60Yw.jpeg" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现 P2P 通信是一项具有挑战性的任务，但如果你知道如何使用正确的工具，那么这项任务就变得简单多了。</p>
<p>所以，我将在这篇文章探讨 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpeerjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://peerjs.com/" ref="nofollow noopener noreferrer">PeerJS</a>，这是一个封装了 WebRTC 的 JavaScript 库，可以在 web 应用中更加轻松的实现 P2P 通信。</p>
<h2 data-id="heading-1">PeerJS 是如何简化 WebRTC 的？</h2>
<p>当在 web 应用中涉及到实时 P2P 通信时，WebRTC 是许多开发者的使用标准。但它也自带了一些复杂性：</p>
<ul>
<li>如果你使用纯 WebRTC，首先你要定义一个 STUN（Session Traversal Utilities for NAT）服务为通讯中涉及到的每一个节点生成 ICE（Interactive Connectivity Establishment）协议候选者。</li>
<li>然后你需要将这些 ICE 协议候选者的详情存储在你的服务中。</li>
<li>最后，你需要使用 WebSockets 来处理实时更新。</li>
</ul>
<p>即使你之前没有接触过 WebRTC，我相信你也已经感受到了实现它的复杂性。但别担心，PeerJS 来解救你了。</p>
<blockquote>
<p>有了 PeerJS，我们不用担心 STUN，ICE 协议候选者，或者服务器的创建，而且我们甚至可以避免使用 WebSockets。</p>
</blockquote>
<p>PeerJS 提供一个完整的、可配置的点对点连接的 API， 以及一个称之为 PeerServer 的服务，使得我们能够轻松的在 PeerJS 的客户端之间建立连接。</p>
<p>那么就来看看我们如何使用 PeerJS 来创建一个简单的聊天应用。</p>
<h2 data-id="heading-2">使用 PeerJS 和 React 搭建你的第一个聊天室</h2>
<h3 data-id="heading-3">步骤 1 —— 安装 PeerJS</h3>
<p>首先，我们需要将 PeerJS 作为一个 node module 安装在你的项目中，并将 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fpeer" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/peer" ref="nofollow noopener noreferrer">peer</a> 作为全局依赖。</p>
<pre><code class="hljs language-bash copyable" lang="bash">// 安装 PeerJS
npm i peerjs

// 安装 Peer
npm i -g peer
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意</strong>：PeerJS 用于在本地启动 PeerServer，但你也可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpeerjs.com%2Fpeerserver.html" target="_blank" rel="nofollow noopener noreferrer" title="https://peerjs.com/peerserver.html" ref="nofollow noopener noreferrer">PeerServer Cloud</a> 实例。</p>
</blockquote>
<h3 data-id="heading-4">步骤 2 —— 实现聊天室</h3>
<p>现在，让我们移至 React 应用，先初始化聊天组件的 state。</p>
<p>我们将在 state 内处理我们自己的 ID，目标节点 ID，聊天信息，以及一个 Peer 对象的实例。</p>
<pre><code class="hljs language-js copyable" lang="js">state = &#123;
  <span class="hljs-attr">myId</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">friendId</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">peer</span>: &#123;&#125;,
  <span class="hljs-attr">message</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">messages</span>: []
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要通过定义主机名，端口号以及路径来创建一个 Peer 实例用于管理我们的 P2P 连接。在整个通信过程中我们都将使用该实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> peer = <span class="hljs-keyword">new</span> Peer(<span class="hljs-string">''</span>, &#123;
  <span class="hljs-attr">host</span>: <span class="hljs-string">'localhost'</span>,
  <span class="hljs-attr">port</span>: <span class="hljs-string">'3001'</span>,
  <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>**提示：**你可以使用你自己的 ID 作为第一个参数，或者不传参，让 PeerServer 生成一个随机 ID。如果你使用 <code>const peer = new Peer();</code>，你将连接到 PeerServer Cloud。</p>
</blockquote>
<p>Peer 实例有几个方法去处理 peer 之间的通信。<code>peer.on</code> 是用于监听节点的事件，当接收远程节点的通话时该方法很有用。</p>
<p><code>open</code> 事件将会在成功连接 PeerServer 后发出，我们将通过该事件去更新 myId 和 peer 实例的 state。</p>
<pre><code class="hljs language-js copyable" lang="js">peer.on(<span class="hljs-string">'open'</span>, <span class="hljs-function">(<span class="hljs-params">id</span>) =></span> &#123;

<span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">myId</span>: id,
    <span class="hljs-attr">peer</span>: peer
   &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们需要通过 <code>connection</code> 事件来监听远程节点连接，并通过其回调函数获取远程节点发送的消息。</p>
<pre><code class="hljs language-js copyable" lang="js">peer.on(<span class="hljs-string">'connection'</span>, <span class="hljs-function">(<span class="hljs-params">conn</span>) =></span> &#123;
  conn.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;

      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">messages</span>: [...this.state.messages, data]
      &#125;);

   &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们已经实现了消息接收的功能。那么在最后一步，让我们创建一个方法用于消息发送。</p>
<p><code>peer.connect</code> 方法使我们可以通过指定远程节点 id 来连接该节点。然后它将返回一个 <code>DataConnection</code> 对象用于向节点发送消息。</p>
<pre><code class="hljs language-js copyable" lang="js">send = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> conn = <span class="hljs-built_in">this</span>.state.peer.connect(<span class="hljs-built_in">this</span>.state.friendId);

  conn.on(<span class="hljs-string">'open'</span>, <span class="hljs-function">() =></span> &#123;

    <span class="hljs-keyword">const</span> msgObj = &#123;
      <span class="hljs-attr">sender</span>: <span class="hljs-built_in">this</span>.state.myId,
      <span class="hljs-attr">message</span>: <span class="hljs-built_in">this</span>.state.message
    &#125;;

   conn.send(msgObj);

    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">messages</span>: [...this.state.messages, msgObj],
      <span class="hljs-attr">message</span>: <span class="hljs-string">''</span>
    &#125;);

  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">步骤 3 —— 实现视频聊天</h3>
<p>现在，让我们修改聊天室用于发送视频消息。该功能的的实现与之前我们讨论过的步骤非常相似。我们可以通过 <code>peer.on</code> 方法监听 <code>call</code> 事件从而获知来自远程节点的来电。该监听事件提供一个携带 <code>MediaConnection</code> 对象的回调函数，而接受者的视频流和音频流将提供给 <code>MediaConnection</code> 对象的 <code>answer</code> 方法。</p>
<pre><code class="hljs language-js copyable" lang="js">peer.on(<span class="hljs-string">'call'</span>, <span class="hljs-function">(<span class="hljs-params">call</span>) =></span> &#123;

<span class="hljs-keyword">var</span> getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;

getUserMedia(&#123; <span class="hljs-attr">video</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">audio</span>: <span class="hljs-literal">true</span> &#125;, <span class="hljs-function">(<span class="hljs-params">stream</span>) =></span> &#123;

  <span class="hljs-built_in">this</span>.myVideo.srcObject = stream;
  <span class="hljs-built_in">this</span>.myVideo.play();
  
  call.answer(stream);

  call.on(<span class="hljs-string">'stream'</span>, <span class="hljs-function">(<span class="hljs-params">remoteStream</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.friendVideo.srcObject = remoteStream;
    <span class="hljs-built_in">this</span>.friendVideo.play();
  &#125;);

&#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Error!'</span>) &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，让我们从我们的端口向远程节点发送一个视频通话。这个方法与来电响应类似。我们需要调用最初的 <code>peer</code> 实例上的 <code>call</code> 方法并且将提供节点 ID 和视频流作为其参数。</p>
<p><code>call</code> 方法将由此返回一个 <code>MediaConnection</code> 对象，我们可以通过该对象使用节点的视频流。</p>
<pre><code class="hljs language-js copyable" lang="js">videoCall = <span class="hljs-function">() =></span> &#123;

<span class="hljs-keyword">var</span> getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;

getUserMedia(&#123; <span class="hljs-attr">video</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">audio</span>: <span class="hljs-literal">true</span> &#125;, <span class="hljs-function">(<span class="hljs-params">stream</span>) =></span> &#123;

  <span class="hljs-built_in">this</span>.myVideo.srcObject = stream;
  <span class="hljs-built_in">this</span>.myVideo.play();

  <span class="hljs-keyword">const</span> call = <span class="hljs-built_in">this</span>.state.peer.call(<span class="hljs-built_in">this</span>.state.friendId, stream);

  call.on(<span class="hljs-string">'stream'</span>, <span class="hljs-function">(<span class="hljs-params">remoteStream</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.friendVideo.srcObject = remoteStream;
    <span class="hljs-built_in">this</span>.friendVideo.play();
  &#125;);
&#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Error!'</span>) &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">步骤 4 —— 最后的事项</h3>
<p>终于到时候添加一些 JSX 来渲染我们的聊天室了。让我们添加两个输入框用于输入节点 ID 以及聊天信息。我们将使用 <code>ref</code> 属性来操作 <code>video</code> 元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"wrapper"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"col"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>My ID: &#123;this.state.myId&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">label</span>></span>Friend ID:<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span>
     <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
     <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state.friendId&#125;</span>
     <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;e</span> =></span> &#123; this.setState(&#123; friendId: e.target.value &#125;);&#125;&#125; />

<span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">br</span> /></span>

    <span class="hljs-tag"><<span class="hljs-name">label</span>></span>Message:<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span>
     <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
     <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state.message&#125;</span>
     <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;e</span> =></span> &#123; this.setState(&#123; message: e.target.value &#125;); &#125;&#125; />

    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.send&#125;</span>></span>Send<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.videoCall&#125;</span>></span>Video Call<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    &#123;
      this.state.messages.map((message, i) => &#123;
        return (
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;i&#125;</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;message.sender&#125;:<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;message.message&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        )
      &#125;);
    &#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"col"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref</span> =></span> this.myVideo = ref&#125; />
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref</span> =></span> this.friendVideo = ref&#125; />
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就这样！现在，一个快速视频聊天已经全部设置好了。最后的成果看起来像这样，你可以在我的 GitHub <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FDulanka-K%2Fvideo-chat" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Dulanka-K/video-chat" ref="nofollow noopener noreferrer">仓库</a>找到完整的代码。</p>
<p><img src="https://cdn-images-1.medium.com/max/3840/1*G48OkV0QlFvETj2zqDuqIw.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://cdn-images-1.medium.com/max/2000/1*0epo9iaN7-wx39_FkRTBCw.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>注意</strong>：在不是 HTTPS 连接的情况下，一些浏览器（尤其是手机浏览器）可能不允许使用相机和麦克风。你可以参考这篇<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.bitsrc.io%2Fusing-https-for-local-development-for-react-angular-and-node-fdfaf69693cd" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.bitsrc.io/using-https-for-local-development-for-react-angular-and-node-fdfaf69693cd" ref="nofollow noopener noreferrer">文章</a>，通过几个步骤设置一个本地 HTTPS 连接。</p>
</blockquote>
<h2 data-id="heading-7">结语</h2>
<p>WebRTC 是支持 P2P 通信的浏览器标准。但是因为牵涉到 STUN 服务器，ICE 协议候选者，SDPs，以及 WebSockets，所以实现 WebRTC 会有一点复杂。</p>
<p>PeerJS 通过封装 WebRTC 简化了整个流程，为我们提供了更简单的事件和方法。</p>
<p>所以，我邀请你尝试使用 PeerJS，并在评论区中让我知道你的观点。</p>
<p>感谢阅读！！！</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" title="https://juejin.im">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23android" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#android" ref="nofollow noopener noreferrer">Android</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23ios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#ios" ref="nofollow noopener noreferrer">iOS</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2589%258D%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" ref="nofollow noopener noreferrer">前端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2590%258E%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" ref="nofollow noopener noreferrer">后端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%258C%25BA%25E5%259D%2597%25E9%2593%25BE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" ref="nofollow noopener noreferrer">区块链</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25A7%25E5%2593%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" ref="nofollow noopener noreferrer">产品</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E8%25AE%25BE%25E8%25AE%25A1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" ref="nofollow noopener noreferrer">设计</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" ref="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="https://link.juejin.cn/?target=http%3A%2F%2Fweibo.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="http://weibo.com/juejinfanyi" ref="nofollow noopener noreferrer">官方微博</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/juejinfanyi" ref="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            