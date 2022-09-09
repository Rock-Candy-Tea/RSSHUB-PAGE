
---
title: '码上掘金不仅可以写 PPT，还可以录视频'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d4a04f23800496c9292ce336f859316~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 08:05:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d4a04f23800496c9292ce336f859316~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<h2 data-id="heading-0">前言</h2>
<p>做短视频作为新时代的产物，到现在才发展了几年的时间，创作者们看到了短视频的红利，有不少人已经通过视频录制和知识付费的方式实现了流量的变现，当然这只是一少部分人，还有成千上万的热涌向这个风口，他们在干什么？他们正在学习视频录制、视频剪辑的路上。</p>
<p>短视频的入门门槛虽然很低，但想要获得流量还是有一定门槛的，我今年的 flag 之一就是学习视频制作剪辑，前段时间剪了一个视频总共 1 分 20 秒，就花了我一整天的时间，那么我在想，作为前端工程师能不能开发一款产品，让短视频创作更低，后来我看到了一款贴合程序员的产品 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.sli.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.sli.dev/" ref="nofollow noopener noreferrer">Slidev</a>，可以让我们使用 markdown 写 PPT，并且可以录制视频。</p>
<h2 data-id="heading-1">前端实现视频录制</h2>
<p>好了，正文开始，本文基于我之前写的一篇文章<a href="https://juejin.cn/post/7129385772561465358" target="_blank" title="https://juejin.cn/post/7129385772561465358">《Markdown 写 PPT 是如何实现的？》</a>，我们要在此之上实现视频录制的功能。</p>
<p>使用 WebRTC 的 API 可以实现了一个录音、录像、录屏工具</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMediaDevices%2FgetUserMedia" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaDevices/getUserMedia" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">MediaDevices.getUserMedia()</a> 可用于获取麦克风以及摄像头的流</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMediaDevices%2FgetDisplayMedia" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaDevices/getDisplayMedia" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">MediaDevices.getDisplayMedia()</a> 提示用户去选择和授权捕获展示的内容或部分内容，返回 MediaStream</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMediaRecorder%2FMediaRecorder" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MediaRecorder/MediaRecorder" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">MediaRecorder()</a> 构造函数会创建一个对指定的 <code>MediaStream</code> 进行录制，还提供了开始、结束、暂停、恢复等多个与 Record 相关的接口。</li>
</ul>
<p>我们先使用 React 写一个录制的组件</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; useState, useRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">ReactDom</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;

<span class="hljs-keyword">const</span> <span class="hljs-title function_">App</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> [videoUrl, setVideoUrl] = useState<<span class="hljs-built_in">string</span>>(<span class="hljs-string">''</span>);

  <span class="hljs-comment">// 结束</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">stopRecord</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) => &#123;
  &#125;

  <span class="hljs-comment">// 开始</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">startRecord</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) => &#123;
  &#125;

  <span class="hljs-keyword">const</span> <span class="hljs-title function_">pauseRecord</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) => &#123;
  &#125;

  <span class="hljs-keyword">const</span> <span class="hljs-title function_">resumeRecord</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) => &#123;

  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>React 录屏<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"video"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;videoUrl&#125;</span> <span class="hljs-attr">controls</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;startRecord&#125;</span>></span>开始<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;pauseRecord&#125;</span>></span>暂停<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;resumeRecord&#125;</span>></span>恢复<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;stopRecord&#125;</span>></span>停止<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-title class_">ReactDom</span>.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'app'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面有一个 <code>video</code> 标签，以及 开始、停止、暂停、恢复、几个按钮用于控制屏幕的录制。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> mediaStream = useRef<<span class="hljs-title class_">MediaStream</span>>();
<span class="hljs-keyword">const</span> audioStream = useRef<<span class="hljs-title class_">MediaStream</span>>();
<span class="hljs-keyword">const</span> recorder = useRef<<span class="hljs-title class_">MediaRecorder</span>>();
<span class="hljs-keyword">const</span> mediaBlobs = useRef<<span class="hljs-title class_">Blob</span>[]>([]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们使用 <code>useRef</code> 来存放数据，mediaStream 存放视频流， <code>audioStream</code> 存放音频流，<code>recorder</code> 存放视频录制对象，<code>mediaBlobs</code> 将流转化为 <code>Blob</code> 对象。</p>
<p>下面代码是开始录制和结束录制的逻辑:</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 结束</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">stopRecord</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) => &#123;
  recorder.<span class="hljs-property">current</span>?.<span class="hljs-title function_">stop</span>()
  <span class="hljs-comment">// 不仅让 MediaRecorder 停止，还要让所有轨道停止</span>
  mediaStream.<span class="hljs-property">current</span>?.<span class="hljs-title function_">getTracks</span>().<span class="hljs-title function_">forEach</span>(<span class="hljs-function">(<span class="hljs-params">track</span>) =></span> track.<span class="hljs-title function_">stop</span>());
&#125;

<span class="hljs-comment">// 开始</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">startRecord</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-comment">// 录屏接口</span>
  mediaStream.<span class="hljs-property">current</span> = <span class="hljs-keyword">await</span> navigator.<span class="hljs-property">mediaDevices</span>.<span class="hljs-title function_">getDisplayMedia</span>(&#123; <span class="hljs-attr">video</span>: <span class="hljs-literal">true</span> &#125;);
  <span class="hljs-comment">// 主动停止录制</span>
  mediaStream.<span class="hljs-property">current</span>?.<span class="hljs-title function_">getTracks</span>()[<span class="hljs-number">0</span>].<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'ended'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-title function_">stopRecord</span>()
  &#125;)
  <span class="hljs-comment">// 录音接口</span>
  audioStream.<span class="hljs-property">current</span> = <span class="hljs-keyword">await</span> navigator.<span class="hljs-property">mediaDevices</span>.<span class="hljs-title function_">getUserMedia</span>(&#123; <span class="hljs-attr">audio</span>: <span class="hljs-literal">true</span> &#125;)
  <span class="hljs-comment">// 往视频流中加入音频流</span>
  audioStream.<span class="hljs-property">current</span>?.<span class="hljs-title function_">getAudioTracks</span>().<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">audioTrack</span> =></span> mediaStream.<span class="hljs-property">current</span>?.<span class="hljs-title function_">addTrack</span>(audioTrack));
  <span class="hljs-comment">// 录制视频流</span>
  recorder.<span class="hljs-property">current</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MediaRecorder</span>(mediaStream.<span class="hljs-property">current</span>);

  <span class="hljs-comment">// 将 stream 转成 blob 来存放</span>
  recorder.<span class="hljs-property">current</span>.<span class="hljs-property">ondataavailable</span> = <span class="hljs-function">(<span class="hljs-params">blobEvent</span>) =></span> &#123;
    mediaBlobs.<span class="hljs-property">current</span>.<span class="hljs-title function_">push</span>(blobEvent.<span class="hljs-property">data</span>);
  &#125;
  <span class="hljs-comment">// 停止时生成预览的 blob url</span>
  recorder.<span class="hljs-property">current</span>.<span class="hljs-property">onstop</span> = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> blob = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Blob</span>(mediaBlobs.<span class="hljs-property">current</span>, &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'video/mp4'</span> &#125;)
    <span class="hljs-comment">//来生成预览链接</span>
    <span class="hljs-keyword">const</span> mediaUrl = <span class="hljs-variable constant_">URL</span>.<span class="hljs-title function_">createObjectURL</span>(blob);
    <span class="hljs-title function_">setVideoUrl</span>(mediaUrl);
  &#125;

  recorder.<span class="hljs-property">current</span>?.<span class="hljs-title function_">start</span>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码先通过 <code>navigator.mediaDevices.getDisplayMedia</code> 获取用户选中的录屏流，接着通过 <code>navigator.mediaDevices.getUserMedia(&#123; audio: true &#125;)</code>获取音频流，然后通过 <code>mediaStream.current?.addTrack(audioTrack)</code> 将所有音频流加入到视频流中。再 通过 <code>MediaRecorder</code> 录制视频流，通过 <code>ondataavailable</code> 来存放当前流中的 <code>Blob</code> 数据。
最后一步，调用 <code>URL.createObjectURL</code> 来生成预览链接。</p>
<p>下面是暂停和恢复的代码，是 <code>MediaRecorder</code> 提供的方法</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> <span class="hljs-title function_">pauseRecord</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) => &#123;
  recorder.<span class="hljs-property">current</span>?.<span class="hljs-title function_">pause</span>();
&#125;

<span class="hljs-keyword">const</span> <span class="hljs-title function_">resumeRecord</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) => &#123;
  recorder.<span class="hljs-property">current</span>?.<span class="hljs-title function_">resume</span>()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就实现了一个在线录屏的 Demo，一起来“码上掘金”中看看效果吧。</p>
<p><span href="https://code.juejin.cn/pen/7140845249294762017" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140845249294762017" data-src="https://code.juejin.cn/pen/7140845249294762017" style="display: none" loading="lazy"></iframe></span></p>
<h2 data-id="heading-2">实现幻灯片演讲录制</h2>
<p>接下来我们将视频录制的功能集成到之前的幻灯片中，只需要将上面的 <code>App</code> 组件改成 <code>RecordView</code> 组件，并且通过 <code>position: fixed;</code> 属性将操作按钮定位到幻灯片之上。</p>
<p>录制完成后，通过创建一个 <code>a</code> 标签，就可以实现自动下载。</p>
<p>下面是自动下载的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">downloadBlob</span>(<span class="hljs-params">blob, filename</span>) &#123;
  <span class="hljs-keyword">let</span> element = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">"a"</span>);
  element.<span class="hljs-title function_">setAttribute</span>(<span class="hljs-string">"href"</span>, blob);
  element.<span class="hljs-title function_">setAttribute</span>(<span class="hljs-string">"download"</span>, filename);
  element.<span class="hljs-property">style</span>.<span class="hljs-property">display</span> = <span class="hljs-string">"none"</span>;
  <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">appendChild</span>(element);
  element.<span class="hljs-title function_">click</span>();
  <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">removeChild</span>(element);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样我们在“码上掘金”中看看效果吧。
<span href="https://code.juejin.cn/pen/7140939415622418468" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140939415622418468" data-src="https://code.juejin.cn/pen/7140939415622418468" style="display: none" loading="lazy"></iframe></span>
鼠标移动到左下角会显示操作按钮，我们还可以点击编辑按钮对幻灯片进行实时编辑，这么简单就实现了想要的效果，简直不可思议。</p>
<h2 data-id="heading-3">竖屏录制</h2>
<p>目前短视频都是竖屏的，我们那么能否录制竖屏版的视频呢？答案是可以的，但是在“码上掘金”中不能，因为“码上掘金”是一个代码编辑器，在移动端无法访问，因此我还将这个应用部署到了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvercel.com%2F" title="https://vercel.com/" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">vercel</a> 上，大家可以通过这个地址访问 :</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fppt.runjs.cool%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://ppt.runjs.cool/" ref="nofollow noopener noreferrer">ppt.runjs.cool/</a></p>
<p>打开 Chrome devtools 选择手机调试模式，选中一个合适的型号，便可以开始录制了，录制的时候选中当前网页就可以了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d4a04f23800496c9292ce336f859316~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="竖屏录制" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样保存下来的视频便是竖屏的。</p>
<p>最后，我将这个工程的源码上传到了GitHub：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmaqi1520%2Fvitejs-md-ppt" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/maqi1520/vitejs-md-ppt" ref="nofollow noopener noreferrer">github.com/maqi1520/vi…</a></p>
<p>目前还比较粗糙，经过精雕细琢后肯能会成为一个好产品，先占个坑吧！</p>
<h2 data-id="heading-4">小结</h2>
<p>本文用 WebRTC 的 API 简单地实现了一个录屏工具，并且可以结合 markdown 写 PPT 实现录制幻灯片的功能，我们一起来梳理下录屏的实现逻辑</p>
<ul>
<li>使用 <code>getUserMedia</code> 可获取麦克风以及摄像头的流；</li>
<li>使用 <code>getDisplayMedia</code> 可获取屏幕的视频、音频流；</li>
<li>使用 <code>MediaRecorder</code> 可监听 <code>stream</code>， 从而获取 <code>Blob</code> 数据；</li>
<li>最后使用 <code>URL.createObjectURL</code> 将 <code>Blob</code> 转为下载链接；</li>
</ul>
<p>以上就是本文全部内容，如果对你有帮助，可以随手点个赞，这对我真的很重要，希望这篇文章对大家有所帮助，也可以参考我往期的文章或者在评论区交流你的想法和心得，欢迎一起探索前端。</p></div>  
</div>
            