
---
title: 'Electron _ Chromium 屏幕录制 - 那些我踩过的坑'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0afe5cf007ed41a89badc9ff629adb36~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 19:35:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0afe5cf007ed41a89badc9ff629adb36~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>Web 屏幕录制也许对我们来说并不陌生，最常见的场景，例如：各种视频会议、远程桌面软件，远程会议软件的出现大大方便了人们的交流与沟通，在 WFH 期间对众多企业的线上运转起到关键的作用。除了屏幕的实时分享，录屏的应用还存在另一种应用场景，即“记录实时操作并保留现场，方便后续追溯与回放”，即是我们业务的主要场景。对于我们的业务，强依赖该功能的稳定性。以下是我们业务对该功能的一些硬性指标：</p>
<h1 data-id="heading-1">指标要求</h1>
<ol>
<li>支持任意时长的录制，支持超过 6 小时时长的录制。</li>
<li>支持同时录音。在录屏同时录制到屏幕中正在播放的内容的声音。</li>
<li>支持跨平台，兼容 Windows、Mac、Linux 三个平台。</li>
<li>支持在 App 从 A 窗口拖拽到 B 窗口时持续录制。</li>
<li>支持在最小化，最大化，全屏时保持录屏，且录制范围仅在 App 内部，不可录制到 App 外。</li>
<li>支持长时间，不间断，不关闭 App 的情况下可以不断录制。</li>
<li>支持在无需完整下载录屏的情况下，在 Web 端随意拖拽时间线。</li>
<li>支持 App 多标签页切换情况下，对多标签页的同时录制。</li>
<li>支持 App 多开窗口在同一个系统窗口内，同时录制 App 窗口。</li>
<li>支持直播实时流的录制。</li>
<li>录屏文件不能存储在本地，录制结束后必须自动上传并加密存储。</li>
</ol>
<h1 data-id="heading-2">技术方案探索</h1>
<p>目前 Chromium 端上视频直接录制，一般来说有两种技术方案，即：rrweb 方案、以及 WebRTC API 方案。如果考虑 Electron 场景，又会额外多出一种 ffmpeg 的方案。</p>
<h2 data-id="heading-3">rrweb</h2>
<p><strong>优势</strong></p>
<ol>
<li>支持在录屏的同时直接录制到当前 Tab 内的声音。</li>
<li>跨平台兼容。</li>
<li>支持窗口的拖拽、最小化、最大化、全屏等情况的持续录制。</li>
<li>录屏尺寸小。</li>
<li>支持在无需完整下载录屏的情况下，在 Web 端随意拖拽时间线。</li>
<li>性能较好。</li>
</ol>
<p><strong>劣势</strong></p>
<ol>
<li>无法录制直播实时流。考虑其实现原理，录屏场景有限。</li>
<li>不支持在关闭 App 标签页的情况录制，如果 Renderer 进程关闭，则会直接终止录制并丢失录屏。</li>
<li>某些场景会对页面 DOM 有影响。</li>
</ol>
<h2 data-id="heading-4">ffmpeg</h2>
<p><strong>优势</strong></p>
<ol>
<li>同等体积，录屏文件的输出质量好。</li>
<li>性能好。</li>
<li>支持录制直播实时流。</li>
</ol>
<p><strong>劣势</strong></p>
<ol>
<li>跨平台兼容处理复杂。</li>
<li>录制区域非动态，虽支持选区，但若 App 移动则无能为力的录制到屏幕外内容。</li>
<li>不支持 App 多标签页切换情况下，对多标签页进行暂停或继续。</li>
<li>支持在 App 从 A 窗口拖拽到 B 窗口时持续对 App 录制。</li>
<li>录屏文件中间时间会存储在本地，若 App 关闭后会导致录屏文件的暴露。</li>
<li>不支持 App 多开窗口情况下的，且在同时录制。</li>
</ol>
<h2 data-id="heading-5">webRTC</h2>
<p><strong>优势</strong></p>
<ol>
<li>支持全部指标 1-11。</li>
</ol>
<p><strong>劣势</strong></p>
<ol>
<li>性能较差，录制时 CPU 占用率相对较高。</li>
<li>原生录制的视频文件，没有视频时长。</li>
<li>原生录制的视频文件，不支持时间线拖拽。</li>
<li>原生不支持超长时长的录制，若录屏文件大于磁盘空间的 1/10 会报错。</li>
<li>原生录制会有较大的内存占用。</li>
<li>视频删除依赖 V8 与 Blob 实现的垃圾回收机制，非常容易内存泄露。</li>
</ol>
<p>考虑到 rrweb 较好的性能，最初我们第一版实际上是基于 rrweb 实现的，但 rrweb 的原生硬伤最终导致我们放弃该方案，比如如果用户关闭窗口会直接导致录屏丢失是不可接受的，其次 rrweb 不支持直播实时流是我们最终放弃他的根本原因。此外考虑到 ffmpeg 的种种限制，以及我们自身的指标要求，最终我们选择了 webRTC API 直接录制的方案实现了录屏功能，并在后续踩了一些列的坑，一下是一些分享。</p>
<h1 data-id="heading-6">媒体流的获取</h1>
<p>在 WebRTC 标准中，一切持续不断产生媒体的起点，都被抽象成媒体流，例如我们需要录制屏幕与声音，其实现的关键就是找到需要录制屏幕的源和录制音频的源，整体的流程如下图所示：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0afe5cf007ed41a89badc9ff629adb36~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">视频流获取</h1>
<p>想获取视频流，首先需要获取所需要捕获视频流的 MediaSourceId。Electron 提供了一个获取各个“窗口”和“屏幕”视频 MediaSourceId 的通用 API</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">import</span> &#123; desktopCapturer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'electron'</span>;



<span class="hljs-comment">// 获取全部窗口或屏幕的mediaSourceId</span>

desktopCapturer.getSources(&#123;
  <span class="hljs-attr">types</span>: [<span class="hljs-string">'screen'</span>, <span class="hljs-string">'window'</span>], <span class="hljs-comment">// 设定需要捕获的是"屏幕"，还是"窗口"</span>
  <span class="hljs-attr">thumbnailSize</span>: &#123;
    <span class="hljs-attr">height</span>: <span class="hljs-number">300</span>, <span class="hljs-comment">// 窗口或屏幕的截图快照高度</span>
    <span class="hljs-attr">width</span>: <span class="hljs-number">300</span> <span class="hljs-comment">// 窗口或屏幕的截图快照宽度</span>
  &#125;,
  <span class="hljs-attr">fetchWindowIcons</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 如果视频源是窗口且有图标，则设置该值可以捕获到的窗口图标</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">sources</span> =></span> &#123;

  sources.forEach(<span class="hljs-function"><span class="hljs-params">source</span> =></span> &#123;

    <span class="hljs-comment">// 如果视频源是窗口且有图标，且fetchWindowIcons设为true，则为捕获到的窗口图标</span>

    <span class="hljs-built_in">console</span>.log(source.appIcon);

    <span class="hljs-comment">// 显示器Id</span>

    <span class="hljs-built_in">console</span>.log(source.display_id);

    <span class="hljs-comment">// 视频源的mediaSourceId，可通过该mediaSourceId获取视频源</span>

    <span class="hljs-built_in">console</span>.log(source.id);

    <span class="hljs-comment">// 窗口名，通常来说与任务管理器看到的进程名一致</span>

    <span class="hljs-built_in">console</span>.log(source.name);

    <span class="hljs-comment">// 窗口或屏幕在调用本API瞬间抓捕到的截图快照</span>

    <span class="hljs-built_in">console</span>.log(source.thumbnail);

  &#125;);

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你只想获取当前窗口的 MediaSourceID</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">import</span> &#123; remote &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'electron'</span>;



<span class="hljs-comment">// 获取当前窗口mediaSourceId的做法</span>

<span class="hljs-keyword">const</span> mediaSourceId = remote.getCurrentWindow().getMediaSourceId();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在获取到 mediaSourceId 后，继续获取视频流，方法如下：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">import</span> &#123; remote &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'electron'</span>;



<span class="hljs-comment">// 视频流获取</span>

<span class="hljs-keyword">const</span> videoSource: MediaStream = <span class="hljs-keyword">await</span> navigator.mediaDevices.getUserMedia(&#123;

  <span class="hljs-attr">audio</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 强行表示不录制音频，音频额外获取</span>

  <span class="hljs-attr">video</span>: &#123;

    <span class="hljs-attr">mandatory</span>: &#123;

      <span class="hljs-attr">chromeMediaSource</span>: <span class="hljs-string">'desktop'</span>,

      <span class="hljs-attr">chromeMediaSourceId</span>: remote.getCurrentWindow().getMediaSourceId()

    &#125;

  &#125;

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中如果获取的视频源是整个桌面窗口，且操作系统如果是 macOS，还要授权“屏幕录制权限”<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/616d3f9362a04e55b539e87048d5583f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
以上步骤执行后，我们便可以轻松获得视频源。</p>
<h1 data-id="heading-8">音频源获取</h1>
<p>不同于视频源的轻松获取，音频源的获取着实有些复杂，针对 macOS 和 Windows 系统，需要分别处理两种获取方式。首先，在 Windows 获取屏幕音频非常简单且容易，且不需要任何授权，因此这里如果大家需要录制音频，一定要做好权限提示、</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// Windows音频流获取</span>

<span class="hljs-keyword">const</span> audioSource: MediaStream = <span class="hljs-keyword">await</span> navigator.mediaDevices.getUserMedia(&#123;

  <span class="hljs-attr">audio</span>: &#123;

    <span class="hljs-attr">mandatory</span>: &#123;

      <span class="hljs-comment">// 无需指定mediaSourceId就可以录音了，录得是系统音频</span>

      <span class="hljs-attr">chromeMediaSource</span>: <span class="hljs-string">'desktop'</span>,

    &#125;,

  &#125;,

  <span class="hljs-comment">// 如果想要录制音频，必须同样把视频的选项带上，否则会失败</span>

  <span class="hljs-attr">video</span>: &#123;

    <span class="hljs-attr">mandatory</span>: &#123;

      <span class="hljs-attr">chromeMediaSource</span>: <span class="hljs-string">'desktop'</span>,

    &#125;,

  &#125;,

&#125;);



<span class="hljs-comment">// 接着手工移除点不用的视频源，即可完成音频流的获取</span>

(audioSource.getVideoTracks() || []).forEach(<span class="hljs-function"><span class="hljs-params">track</span> =></span> audioSource.removeTrack(track));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，再看 macOS 音频流的获取，这里就有一些难度了，由于 macOS 的音频权限设定(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Flatest%2Fapi%2Fdesktop-capturer%2F%23desktopcapturergetsourcesoptions" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electronjs.org/docs/latest/api/desktop-capturer/#desktopcapturergetsourcesoptions" ref="nofollow noopener noreferrer">参考</a>)，任何人都没办法直接录制系统音频，除非安装第三方驱动 Kext，比如 soundFlower 或者 blackHole，由于 blackHole 同时支持 arm64 M1 处理器和 x64 Intel 处理器(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FExistentialAudio%2FBlackHole" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ExistentialAudio/BlackHole" ref="nofollow noopener noreferrer">参考</a>)，因此我们最终选择 blackHole 的方式获取系统音频。那么在引导用户安装 BlackHole 前，我们需要先检查当前的安装状况，如果用户没有安装过，则提示其安装，如果安装过则继续，这里的方式如下：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">import</span> &#123; remote &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'electron'</span>;



<span class="hljs-keyword">const</span> isWin = process.platform === <span class="hljs-string">'win32'</span>;

<span class="hljs-keyword">const</span> isMac = process.platform === <span class="hljs-string">'darwin'</span>;



declare type AudioRecordPermission =

  | <span class="hljs-string">'ALLOWED'</span>

  | <span class="hljs-string">'RECORD_PERMISSION_NOT_GRANTED'</span>

  | <span class="hljs-string">'NOT_INSTALL_BLACKHOLE'</span>

  | <span class="hljs-string">'OS_NOT_SUPPORTED'</span>;



<span class="hljs-comment">// 检查用户电脑是否有安装SoundFlower或者BlackHole</span>

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getIfAlreadyInstallSoundFlowerOrBlackHole</span>(<span class="hljs-params"></span>): <span class="hljs-title">Promise</span><<span class="hljs-title">boolean</span>> </span>&#123;

  <span class="hljs-keyword">const</span> devices = <span class="hljs-keyword">await</span> navigator.mediaDevices.enumerateDevices();

  <span class="hljs-keyword">return</span> devices.some(

    <span class="hljs-function"><span class="hljs-params">device</span> =></span> device.label.includes(<span class="hljs-string">'Soundflower (2ch)'</span>) || device.label.includes(<span class="hljs-string">'BlackHole 2ch (Virtual)'</span>)

  );

&#125;



<span class="hljs-comment">// 获取是否有麦克风权限（blackhole的实现方式是将屏幕音频模拟为麦克风）</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getMacAudioRecordPermission</span>(<span class="hljs-params"></span>): '<span class="hljs-title">not</span>-<span class="hljs-title">determined</span>' | '<span class="hljs-title">granted</span>' | '<span class="hljs-title">denied</span>' | '<span class="hljs-title">restricted</span>' | '<span class="hljs-title">unknown</span>' </span>&#123;

  <span class="hljs-keyword">return</span> remote.systemPreferences.getMediaAccessStatus(<span class="hljs-string">'microphone'</span>);

&#125;



<span class="hljs-comment">// 请求麦克风权限（blackhole的实现方式是将屏幕音频模拟为麦克风）</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requestMacAudioRecordPermission</span>(<span class="hljs-params"></span>): <span class="hljs-title">Promise</span><<span class="hljs-title">boolean</span>> </span>&#123;

  <span class="hljs-keyword">return</span> remote.systemPreferences.askForMediaAccess(<span class="hljs-string">'microphone'</span>);

&#125;



<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getAudioRecordPermission</span>(<span class="hljs-params"></span>): <span class="hljs-title">Promise</span><<span class="hljs-title">AudioRecordPermission</span>> </span>&#123;

  <span class="hljs-keyword">if</span> (isWin) &#123;

    <span class="hljs-comment">// Windows直接支持</span>

    <span class="hljs-keyword">return</span> <span class="hljs-string">'ALLOWED'</span>;

  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isMac) &#123;

    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">await</span> getIfAlreadyInstallSoundFlowerOrBlackHole()) &#123;

      <span class="hljs-keyword">if</span> (getMacAudioRecordPermission() !== <span class="hljs-string">'granted'</span>) &#123;

        <span class="hljs-keyword">if</span> (!(<span class="hljs-keyword">await</span> requestMacAudioRecordPermission())) &#123;

          <span class="hljs-keyword">return</span> <span class="hljs-string">'RECORD_PERMISSION_NOT_GRANTED'</span>;

        &#125;

      &#125;

      <span class="hljs-keyword">return</span> <span class="hljs-string">'ALLOWED'</span>;

    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-string">'NOT_INSTALL_BLACKHOLE'</span>;

  &#125; <span class="hljs-keyword">else</span> &#123;

    <span class="hljs-comment">// Linux暂时还不支持录制音频</span>

    <span class="hljs-keyword">return</span> <span class="hljs-string">'OS_NOT_SUPPORTED'</span>;

  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，Electron 应用必须在 info.plist 中声明自己需要用到音频录制权限，才可以录制音频，以 Electron-builder 打包流程为例：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// 添加electron-builder配置</span>

<span class="hljs-keyword">const</span> createMac = <span class="hljs-function">() =></span> (&#123;

  ...commonConfig,

  <span class="hljs-comment">// 声明afterPack钩子函数，用于处理音频授权时的i18n</span>

  <span class="hljs-attr">afterPack</span>: <span class="hljs-string">'scripts/macAfterPack.js'</span>,

  <span class="hljs-attr">mac</span>: &#123;

    ...commonMacConfig,

    <span class="hljs-comment">// 必须指定entitlements.mac.plist用于签名时的权限声明</span>

    <span class="hljs-attr">entitlements</span>: <span class="hljs-string">'scripts/entitlements.mac.plist'</span>,

    <span class="hljs-comment">// 必须限制运行时为"hardened"，以使应用通过natorize公证</span>

    <span class="hljs-attr">hardenedRuntime</span>: <span class="hljs-literal">true</span>,

    <span class="hljs-attr">extendInfo</span>: &#123;

      <span class="hljs-comment">// 为info.plist添加多语言支持</span>

      <span class="hljs-attr">LSHasLocalizedDisplayName</span>: <span class="hljs-literal">true</span>,

    &#125;

  &#125;

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了获取音频录制权限，需要自定义 entitlements.mac.plist，并声明以下四个变量：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><?xml version=<span class="hljs-string">"1.0"</span> encoding=<span class="hljs-string">"UTF-8"</span>?>

<!DOCTYPE plist PUBLIC <span class="hljs-string">"-//Apple//DTD PLIST 1.0//EN"</span> <span class="hljs-string">"http://www.apple.com/DTDs/PropertyList-1.0.dtd"</span>>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">plist</span> <span class="hljs-attr">version</span>=<span class="hljs-string">"1.0"</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">dict</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">key</span>></span>com.apple.security.cs.allow-jit<span class="hljs-tag"></<span class="hljs-name">key</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">true</span>/></span>

    <span class="hljs-tag"><<span class="hljs-name">key</span>></span>com.apple.security.cs.allow-unsigned-executable-memory<span class="hljs-tag"></<span class="hljs-name">key</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">true</span>/></span>

    <span class="hljs-tag"><<span class="hljs-name">key</span>></span>com.apple.security.cs.allow-dyld-environment-variables<span class="hljs-tag"></<span class="hljs-name">key</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">true</span>/></span>

    <span class="hljs-tag"><<span class="hljs-name">key</span>></span>com.apple.security.device.audio-input<span class="hljs-tag"></<span class="hljs-name">key</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">true</span>/></span>

  <span class="hljs-tag"></<span class="hljs-name">dict</span>></span>

<span class="hljs-tag"></<span class="hljs-name">plist</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了使音频录制前的“麦克风授权”提示支持多语言，我们这里手动添加以下自定义文字到每个语言的.lproj/InfoPlist.strings 文件内：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// macAfterPack.js</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);



<span class="hljs-comment">// 用于存储到xxx.lproj/InfoPlist.strings的的i18n文字</span>
<span class="hljs-keyword">const</span> i18nNSStrings = &#123;
  <span class="hljs-attr">en</span>: &#123;
    <span class="hljs-attr">NSMicrophoneUsageDescription</span>: <span class="hljs-string">'Please allow this program to access your system audio'</span>,
  &#125;,
  <span class="hljs-attr">ja</span>: &#123;
    <span class="hljs-attr">NSMicrophoneUsageDescription</span>: <span class="hljs-string">'このプログラムがシステムオーディオにアクセスして録音することを許可してください'</span>,
  &#125;,
  <span class="hljs-attr">th</span>: &#123;
    <span class="hljs-attr">NSMicrophoneUsageDescription</span>: <span class="hljs-string">'โปรดอนุญาตให้โปรแกรมนี้เข้าถึงและบันทึกเสียงระบบของคุณ'</span>,
  &#125;,
  <span class="hljs-attr">ko</span>: &#123;
    <span class="hljs-attr">NSMicrophoneUsageDescription</span>: <span class="hljs-string">'이 프로그램이 시스템 오디오에 액세스하고 녹음 할 수 있도록 허용하십시오'</span>,
  &#125;,
  <span class="hljs-attr">zh_CN</span>: &#123;
    <span class="hljs-attr">NSMicrophoneUsageDescription</span>: <span class="hljs-string">'请允许本程序访问录制您的系统音频'</span>,
  &#125;,
&#125;;



<span class="hljs-built_in">exports</span>.default = <span class="hljs-keyword">async</span> context => &#123;

  <span class="hljs-keyword">const</span> &#123; electronPlatformName, appOutDir &#125; = context;

  <span class="hljs-keyword">if</span> (electronPlatformName !== <span class="hljs-string">'darwin'</span>) &#123;

    <span class="hljs-keyword">return</span>;

  &#125;

  <span class="hljs-keyword">const</span> productFilename = context.packager.appInfo.productFilename;

  <span class="hljs-keyword">const</span> resourcesPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;appOutDir&#125;</span>/<span class="hljs-subst">$&#123;productFilename&#125;</span>.app/Contents/Resources/`</span>;



  <span class="hljs-built_in">console</span>.log(

    <span class="hljs-string">`[After Pack] start create i18n NSString bundle, productFilename: <span class="hljs-subst">$&#123;productFilename&#125;</span>, resourcesPath: <span class="hljs-subst">$&#123;resourcesPath&#125;</span>`</span>

  );



  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(

    <span class="hljs-built_in">Object</span>.keys(i18nNSStrings).map(<span class="hljs-function"><span class="hljs-params">langKey</span> =></span> &#123;

      <span class="hljs-keyword">const</span> infoPlistStrPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;langKey&#125;</span>.lproj/InfoPlist.strings`</span>;

      <span class="hljs-keyword">let</span> infos = <span class="hljs-string">''</span>;

      <span class="hljs-keyword">const</span> langItem = i18nNSStrings[langKey];

      <span class="hljs-built_in">Object</span>.keys(langItem).forEach(<span class="hljs-function"><span class="hljs-params">infoKey</span> =></span> &#123;

        infos += <span class="hljs-string">`"<span class="hljs-subst">$&#123;infoKey&#125;</span>" = "<span class="hljs-subst">$&#123;langItem[infoKey]&#125;</span>";\n`</span>;

      &#125;);

      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;

        <span class="hljs-keyword">const</span> filePath = <span class="hljs-string">`<span class="hljs-subst">$&#123;resourcesPath&#125;</span><span class="hljs-subst">$&#123;infoPlistStrPath&#125;</span>`</span>;

        fs.writeFile(filePath, infos, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;

          resolve();

          <span class="hljs-keyword">if</span> (err) &#123;

            <span class="hljs-keyword">throw</span> err;

          &#125;

          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`[After Pack] <span class="hljs-subst">$&#123;filePath&#125;</span> create success`</span>);

        &#125;);

      &#125;);

    &#125;)

  );

&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上，可以完成最基本的 macOS 音频录制能力权限。
接着，以 Blackhole 安装过程为例如下图：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d30854f55deb408db54454ad36979813~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b2f8fe14519416e9eeaa45eb43c17e9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee9feb4bf7614a73960e87803a4e0cd0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ac0315011fd495d916e6b6525984ede~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
当安装后，需要在「启动台」中搜索系统自带软件「音频 MIDI 设置」并打开。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d13ca4e3141447c99be0cd38d322d5c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
点击左下角「+」号，选择「创建多输出设备」。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1826c915d53b4e9582ab2d1d5c675ab4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
在右侧菜单中的「使用」里勾选「BlackHole」（必选）和「扬声器」/「耳机」（二选一或多选）「主设备」选择「扬声器」/「耳机」。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f17fcf72c85497db717edd06ad3deac~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a469d4ffadbc4ddfb01ff89544567d81~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
在菜单栏的「音量」设置中选择刚才创建好的「多输出设备」为声音输出设备。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53d85a02ffc64b0989cceed2e93b9982~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
是的，macOS 的音频录制步骤非常繁琐，但是这只能说是目前的最优解法了。在完成以上“基本权限配置”与“Blackhole 扩展配置”后，我们便可以在代码中顺利获取音频流了：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">if</span> (process.platform === <span class="hljs-string">'darwin'</span>) &#123;

      <span class="hljs-keyword">const</span> permission = <span class="hljs-keyword">await</span> getAudioRecordPermission();



      <span class="hljs-keyword">switch</span> (permission) &#123;

        <span class="hljs-keyword">case</span> <span class="hljs-string">'ALLOWED'</span>:

          <span class="hljs-keyword">const</span> devices = <span class="hljs-keyword">await</span> navigator.mediaDevices.enumerateDevices();

          <span class="hljs-keyword">const</span> outputdevices = devices.filter(

            <span class="hljs-function"><span class="hljs-params">_device</span> =></span> _device.kind === <span class="hljs-string">'audiooutput'</span> && _device.deviceId !== <span class="hljs-string">'default'</span>

          );

          <span class="hljs-keyword">const</span> soundFlowerDevices = outputdevices.filter(<span class="hljs-function"><span class="hljs-params">_device</span> =></span> _device.label === <span class="hljs-string">'Soundflower (2ch)'</span>);

          <span class="hljs-keyword">const</span> blackHoleDevices = outputdevices.filter(<span class="hljs-function"><span class="hljs-params">_device</span> =></span> _device.label === <span class="hljs-string">'BlackHole 2ch (Virtual)'</span>);



          <span class="hljs-comment">// 如果用户安装soundFlower或者blackhole，则按优先级获取deviceId</span>

          <span class="hljs-keyword">const</span> deviceId = soundFlowerDevices.length ?

            soundFlowerDevices[<span class="hljs-number">0</span>].deviceId :

            blackHoleDevices.length ?

              blackHoleDevices[<span class="hljs-number">0</span>].deviceId :

              <span class="hljs-literal">null</span>;

          <span class="hljs-keyword">if</span> (deviceId) &#123;

            <span class="hljs-comment">// 当获取到可使用的deviceId时，抓取音频流</span>

            <span class="hljs-keyword">const</span> audioSource = <span class="hljs-keyword">await</span> navigator.mediaDevices.getUserMedia(&#123;

              <span class="hljs-attr">audio</span>: &#123;

                <span class="hljs-attr">deviceId</span>: &#123;

                  <span class="hljs-attr">exact</span>: deviceId, <span class="hljs-comment">// 根据获取到的deviceId，获取音频流</span>

                &#125;,

                <span class="hljs-attr">sampleRate</span>: <span class="hljs-number">44100</span>,

                <span class="hljs-comment">// 这里的三个参数都关闭可以获得最原始的音频</span>

                <span class="hljs-comment">// 否则Chromium默认会对音频做一些处理</span>

                <span class="hljs-attr">echoCancellation</span>: <span class="hljs-literal">false</span>,

                <span class="hljs-attr">noiseSuppression</span>: <span class="hljs-literal">false</span>,

                <span class="hljs-attr">autoGainControl</span>: <span class="hljs-literal">false</span>,

              &#125;,

              <span class="hljs-attr">video</span>: <span class="hljs-literal">false</span>,

            &#125;);

          &#125;

          <span class="hljs-keyword">break</span>;

        <span class="hljs-keyword">case</span> <span class="hljs-string">'NOT_INSTALL_BLACKHOLE'</span>:

          <span class="hljs-comment">// 这里做一些提示，告知用户没有安装插件</span>

          <span class="hljs-keyword">break</span>;

        <span class="hljs-keyword">case</span> <span class="hljs-string">'RECORD_PERMISSION_NOT_GRANTED'</span>:

          <span class="hljs-comment">// 这里做一些提示，告知用户没有授权</span>

          <span class="hljs-keyword">break</span>;

        <span class="hljs-keyword">default</span>:

          <span class="hljs-keyword">break</span>;

      &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上，虽然有些许繁琐，但是！至少！我们可以同时录制 Windows 和 macOS 的音频啦~如果正确配置好，执行上述代码后，会弹出如图所示的原生授权弹窗：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8763c3abac2b472f81dad3a9b4aa268d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
如果用户不小心点了不允许，后续也可以在“系统偏好设置-安全与隐私-麦克风”这里打开录制授权。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/caebbaf51572409793a039f32bdcec38~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">合并音视频流</h1>
<p>在以上步骤执行后，我们便可以合并两个流，提取各自的轨道，完成一个新的 MediaStream 的创建。</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// 合并音频流与视频流</span>

<span class="hljs-keyword">const</span> combinedSource = <span class="hljs-keyword">new</span> MediaStream([...this._audioSource.getAudioTracks(), ...this._videoSource.getVideoTracks()]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">媒体流的录制</h1>
<h2 data-id="heading-11">编码格式</h2>
<p>我们已经有了录制源，但没有创建录制 = 没有开始录，Chromium 提供了一个叫做 MediaRecorder 的类，用于我们传入媒体流并录制视频，因此如何创建 MediaRecorder 并发起录制，是录屏的核心。MediaRecorder 本身支持仅支持录制 webm 格式，但支持多种编码格式，例如：vp8、vp9、h264 等，MediaRecorder 贴心的提供了一个 API，方便我们测试编码格式兼容性</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">let</span> types: string[] = [

  <span class="hljs-string">"video/webm"</span>,

  <span class="hljs-string">"audio/webm"</span>,

  <span class="hljs-string">"video/webm;codecs=vp9"</span>,

  <span class="hljs-string">"video/webm;codecs=vp8"</span>,

  <span class="hljs-string">"video/webm;codecs=daala"</span>,

  <span class="hljs-string">"video/webm;codecs=h264"</span>,

  <span class="hljs-string">"audio/webm;codecs=opus"</span>,

  <span class="hljs-string">"video/mpeg"</span>

];



<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> types) &#123;

  <span class="hljs-comment">// 可以自行测试需要的编码的MIME Type是否支持</span>

  <span class="hljs-built_in">console</span>.log( <span class="hljs-string">"Is "</span> + types[i] + <span class="hljs-string">" supported? "</span> + (MediaRecorder.isTypeSupported(types[i]) ? <span class="hljs-string">"Yes"</span> : <span class="hljs-string">"No :("</span>));

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经测试，以上编码格式录制时的 CPU 占用并没有什么本质区别，因此建议直接选 VP9 录。</p>
<h2 data-id="heading-12">创建录制</h2>
<p>确定好编码，并合并好音视频流，我们可以真正开始录制了：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">const</span> recorder = <span class="hljs-keyword">new</span> MediaRecorder(combinedSource, &#123;

   <span class="hljs-attr">mimeType</span>: <span class="hljs-string">'video/webm;codecs=vp9'</span>,

   <span class="hljs-comment">// 支持手动设置码率，这里设了1.5Mbps的码率，以限制码率较大的情况</span>

   <span class="hljs-comment">// 由于本身还是动态码率，这个值并不准确</span>

   <span class="hljs-attr">videoBitsPerSecond</span>: <span class="hljs-number">1.5e6</span>,

&#125;);



<span class="hljs-keyword">const</span> timeslice = <span class="hljs-number">5000</span>;

<span class="hljs-keyword">const</span> fileBits: Blob[] = [];



<span class="hljs-comment">// 当数据可用时，会回调该函数，有以下四种情况：</span>

<span class="hljs-comment">// 1. 手动停止MediaRecorder时</span>

<span class="hljs-comment">// 2. 设置了timeslice，每到一次timeslice时间间隔时</span>

<span class="hljs-comment">// 3. 媒体流内所有轨道均变成非活跃状态时</span>

<span class="hljs-comment">// 4. 调用recorder.requestData()转移缓冲区数据时</span>

recorder.ondataavailable = <span class="hljs-function">(<span class="hljs-params">event: BlobEvent</span>) =></span> &#123;

    fileBits.push(event.data <span class="hljs-keyword">as</span> Blob);

&#125;



recorder.onstop = <span class="hljs-function">() =></span> &#123;

    <span class="hljs-comment">// 录屏停止并获取录屏文件</span>

    <span class="hljs-comment">// 触发时机一定在ondataavailable之后</span>

    <span class="hljs-keyword">const</span> videoFile = <span class="hljs-keyword">new</span> Blob(fileBits, &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'video/webm;codecs=vp9'</span> &#125;);

&#125;



<span class="hljs-keyword">if</span> (timeslice === <span class="hljs-number">0</span>) &#123;

  <span class="hljs-comment">// 开始录制，并一直存储数据到缓冲区，直到停止</span>

  recorder.start();

&#125; <span class="hljs-keyword">else</span> &#123;

  <span class="hljs-comment">// 开始录制，并且每timeslice毫秒，触发一次ondataavailable，输出并清空缓冲区（非常重要）</span>

  recorder.start(timeslice);

&#125;





<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;

 <span class="hljs-comment">// 30秒后停止</span>

 recorder.stop();

&#125;, <span class="hljs-number">30000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">暂停/恢复录制</h2>
<pre><code class="copyable">// 暂停录制

recorder.pause();



// 恢复录制

recorder.resume();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成以上 API 的调用，我们“录屏功能 MVP”版本就算跑通了。</p>
<h1 data-id="heading-14">录制产物的处理</h1>
<p>正如前面技术方案探索内容中提到的，直接使用浏览器实现的这套方法，会有一些坑，尽管如此，本文的核心其实就是这部分，也就是解决录屏带来的那些坑。</p>
<h2 data-id="heading-15">锁屏触发视频流停止问题</h2>
<p>实验发现，通过 navigator.getUserMedia 获取的视频流，在锁屏情况（是的 macOS、Windows 全部操作系统都会）会中断，我们可以通过一下代码测试该现象：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">import</span> &#123; remote &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'electron'</span>;



<span class="hljs-comment">// 视频流获取</span>

<span class="hljs-keyword">const</span> videoSource: MediaStream = <span class="hljs-keyword">await</span> navigator.mediaDevices.getUserMedia(&#123;

  <span class="hljs-attr">audio</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 强行表示不录制音频，音频额外获取</span>

  <span class="hljs-attr">video</span>: &#123;

    <span class="hljs-attr">mandatory</span>: &#123;

      <span class="hljs-attr">chromeMediaSource</span>: <span class="hljs-string">'desktop'</span>,

      <span class="hljs-attr">chromeMediaSourceId</span>: remote.getCurrentWindow().getMediaSourceId()

    &#125;

  &#125;

&#125;);



recorder.ondataavailable = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'数据可用'</span>);

recorder.onstop = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'录屏停止'</span>);



<span class="hljs-keyword">const</span> recorder = <span class="hljs-keyword">new</span> MediaRecorder(videoSource, &#123;

   <span class="hljs-attr">mimeType</span>: <span class="hljs-string">'video/webm;codecs=vp9'</span>,

   <span class="hljs-comment">// 支持手动设置码率，这里设了1.5Mbps的码率，以限制码率较大的情况</span>

   <span class="hljs-comment">// 由于本身还是动态码率，这个值并不准确</span>

   <span class="hljs-attr">videoBitsPerSecond</span>: <span class="hljs-number">1.5e6</span>,

&#125;);



<span class="hljs-comment">// 开始录制，等10秒，手动触发锁屏</span>

recorder.start();



<span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;

   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'轨道活跃:'</span>, videoSource.active);

&#125;, <span class="hljs-number">1000</span>);



<span class="hljs-number">10</span>秒后控制台输出:



轨道活跃: <span class="hljs-literal">true</span>

轨道活跃: <span class="hljs-literal">true</span>

轨道活跃: <span class="hljs-literal">true</span>

轨道活跃: <span class="hljs-literal">true</span>

轨道活跃: <span class="hljs-literal">true</span>

轨道活跃: <span class="hljs-literal">true</span>

轨道活跃: <span class="hljs-literal">true</span>

轨道活跃: <span class="hljs-literal">true</span>

轨道活跃: <span class="hljs-literal">true</span>

数据可用

录屏停止

轨道活跃: <span class="hljs-literal">false</span>

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上实验说明锁屏会触发视频流状态由“活跃”转为“不活跃”，该问题最大的坑点在于<strong>解锁后“状态并不会自动恢复为活跃”</strong>，必须开发者手动重新调用 navigator.mediaDevices getUserMedia 获取视频流。那么如何知道用户是否锁屏呢？这里我探索出来一种方法：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// 启动MediaRecorder的时候，如果抛错，此时重新获取视频流</span>

 <span class="hljs-keyword">try</span> &#123;

  <span class="hljs-built_in">this</span>.recorder.start(<span class="hljs-number">5000</span>);

&#125; <span class="hljs-keyword">catch</span> (e) &#123;

  <span class="hljs-built_in">this</span>._combinedSource = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.getSystemVideoMediaStream()

  <span class="hljs-built_in">this</span>.recorder = <span class="hljs-keyword">new</span> MediaRecorder(<span class="hljs-built_in">this</span>._combinedSource, &#123;

    <span class="hljs-attr">mimeType</span>: VIDEO_RECORD_FORMAT,

    <span class="hljs-attr">videoBitsPerSecond</span>: <span class="hljs-number">1.5e6</span>,

  &#125;);

  <span class="hljs-built_in">this</span>.recorder.start(<span class="hljs-number">5000</span>);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个坑点在于，以上仅针对纯视频流场景录屏，如果同时录制音频流+视频流，那么“<strong>由于音频流锁屏时的状态始终保持活跃</strong>”，而“<strong>仅视频流锁屏时会触发状态变为不活跃</strong>”，由于并非全部轨道都变为不活跃，<strong>这里“MediaRecorder 并不会触发 ondataavailable 和 onstop，录屏将会仍然继续进行，但录出来的视频是黑屏”</strong>，成为这个问题的一大槽点与大坑。
那么如何解决音视频流锁屏时并不触发 ondataavailable 和 onstop 的问题呢？这里有一种我探索的方法：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// 如果视频流不活跃，停止音频流</span>

<span class="hljs-comment">// 如果音频流不活跃，停止视频流（虽然不会发生，只是兜底）</span>

<span class="hljs-keyword">const</span> startStreamActivityChecker = <span class="hljs-function">() =></span>

  <span class="hljs-built_in">window</span>.setInterval(<span class="hljs-function">() =></span> &#123;

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._videoSource?.active === <span class="hljs-literal">false</span>) &#123;

      <span class="hljs-built_in">this</span>._audioSource?.getTracks().forEach(<span class="hljs-function"><span class="hljs-params">track</span> =></span> track.stop());

    &#125;

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._audioSource?.active === <span class="hljs-literal">false</span>) &#123;

      <span class="hljs-built_in">this</span>._videoSource?.getTracks().forEach(<span class="hljs-function"><span class="hljs-params">track</span> =></span> track.stop());

    &#125;

  &#125;, <span class="hljs-number">1000</span>);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">缺少视频时长与时间线不可拖拽问题</h2>
<blockquote>
<ul>
<li>Issue1: MediaRecorder output should have Cues element -<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fchromium%2Fissues%2Fdetail%3Fid%3D561606" target="_blank" rel="nofollow noopener noreferrer" title="https://bugs.chromium.org/p/chromium/issues/detail?id=561606" ref="nofollow noopener noreferrer">bugs.chromium.org/p/chromium/…</a></li>
</ul>
</blockquote>
<blockquote>
<ul>
<li>Issue2: Videos created with MediaRecorder API are not seekable / scrubbable -<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fchromium%2Fissues%2Fdetail%3Fid%3D569840" target="_blank" rel="nofollow noopener noreferrer" title="https://bugs.chromium.org/p/chromium/issues/detail?id=569840" ref="nofollow noopener noreferrer">bugs.chromium.org/p/chromium/…</a></li>
</ul>
</blockquote>
<blockquote>
<ul>
<li>Issue3: No duration or seeking cue for opus audio produced with mediarecoder -<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fchromium%2Fissues%2Fdetail%3Fid%3D599134" target="_blank" rel="nofollow noopener noreferrer" title="https://bugs.chromium.org/p/chromium/issues/detail?id=599134" ref="nofollow noopener noreferrer">bugs.chromium.org/p/chromium/…</a></li>
</ul>
</blockquote>
<blockquote>
<ul>
<li>Issue4: MediaRecorder: consider producing seekable WebM files -<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fchromium%2Fissues%2Fdetail%3Fid%3D642012" target="_blank" rel="nofollow noopener noreferrer" title="https://bugs.chromium.org/p/chromium/issues/detail?id=642012" ref="nofollow noopener noreferrer">bugs.chromium.org/p/chromium/…</a></li>
</ul>
</blockquote>
<p>私以为这两个问题，算是 MediaRecorder api 设计的最大失误了。由于 webm 文件的视频时长和拖拽信息是写在文件头部的，因此在 WebM 录制未完成前，头部的"Duration"永远是不断增加的一个未知值。但由于 MediaRecorder 支持分片定时输出小 Blob 文件，导致第一个 Blob 的头部是不可能包含 Duration 字段的，同样搜索头信息"SeekHead", "Seek", "SeekID", "SeekPosition", "Cues", "CueTime", "CueTrack", "CueClusterPosition", "CueTrackPositions", "CuePoint" 同样缺失。但 Blob 在设计之初又是不可变的文件类型，导致最终录制出的文件没有 Duration 视频时长字段，这个问题已经被 Chromium 官方标识为“wont fix”，并推荐开发者自行找社区解决。</p>
<h2 data-id="heading-17">使用 ffmpeg 修复</h2>
<p>社区内的一种方案是使用 ffmpeg 对文件进行“拷贝”并输出，例如输入下面的命令：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript">ffmpeg -i without_meta.webm  -vcodec copy -acodec copy with_meta.webm
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ffmpeg 会自动计算 Duration 与搜索头信息，这种方案最大的问题在于，如果对客户端集成 ffmpeg，需要直接操作文件且编写跨平台方案，将文件暴露于本地。如果做在服务端，又会增加文件的整体处理流程与时间，虽然不是不可以，但是这不是我们追求的极致方案。</p>
<h3 data-id="heading-18">使用 npm 库 fix-webm-duration 修复</h3>
<p>这是社区内的另一种方案，即解析 webm 文件的头部信息，并在前端手工记录视频时长，在解析好之后手动将记录好的 Duration 写入 webm 头部，但该方案同样不能解决搜索头丢失导致的可拖拽信息，且依赖手工记录的 duration，修复内容比较有限。</p>
<h3 data-id="heading-19">基于 ts-ebml，利用 fix-webm-metainfo 修复</h3>
<p>这是本问题的最终解，即完全解析 webm ebml 和 segment 头，根据实际 simple block 的大小计算 Duration 与搜索头。我们利用 ebml 解析 webm，以 MediaRecorder 直出的 webm 文件为例解析，结构如下：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript">m  <span class="hljs-number">0</span>  EBML

u  <span class="hljs-number">1</span>    EBMLVersion <span class="hljs-number">1</span>

u  <span class="hljs-number">1</span>    EBMLReadVersion <span class="hljs-number">1</span>

u  <span class="hljs-number">1</span>    EBMLMaxIDLength <span class="hljs-number">4</span>

u  <span class="hljs-number">1</span>    EBMLMaxSizeLength <span class="hljs-number">8</span>

s  <span class="hljs-number">1</span>    DocType webm

u  <span class="hljs-number">1</span>    DocTypeVersion <span class="hljs-number">4</span>

u  <span class="hljs-number">1</span>    DocTypeReadVersion <span class="hljs-number">2</span>

m  <span class="hljs-number">0</span>  Segment

m  <span class="hljs-number">1</span>    Info                                segmentContentStartPos, all CueClusterPositions provided <span class="hljs-keyword">in</span> info.cues will be relative to here and will need adjusted

u  <span class="hljs-number">2</span>      TimecodeScale <span class="hljs-number">1000000</span>

<span class="hljs-number">8</span>  <span class="hljs-number">2</span>      MuxingApp Chrome

<span class="hljs-number">8</span>  <span class="hljs-number">2</span>      WritingApp Chrome

m  <span class="hljs-number">1</span>    Tracks                              tracksStartPos

m  <span class="hljs-number">2</span>      TrackEntry

u  <span class="hljs-number">3</span>        TrackNumber <span class="hljs-number">1</span>

u  <span class="hljs-number">3</span>        TrackUID <span class="hljs-number">31790271978391090</span>

u  <span class="hljs-number">3</span>        TrackType <span class="hljs-number">2</span>

s  <span class="hljs-number">3</span>        CodecID A_OPUS

b  <span class="hljs-number">3</span>        CodecPrivate <Buffer <span class="hljs-number">19</span>>

m  <span class="hljs-number">3</span>        Audio

f  <span class="hljs-number">4</span>          SamplingFrequency <span class="hljs-number">48000</span>

u  <span class="hljs-number">4</span>          Channels <span class="hljs-number">1</span>

m  <span class="hljs-number">2</span>      TrackEntry

u  <span class="hljs-number">3</span>        TrackNumber <span class="hljs-number">2</span>

u  <span class="hljs-number">3</span>        TrackUID <span class="hljs-number">24051277436254136</span>

u  <span class="hljs-number">3</span>        TrackType <span class="hljs-number">1</span>

s  <span class="hljs-number">3</span>        CodecID V_VP9

m  <span class="hljs-number">3</span>        Video

u  <span class="hljs-number">4</span>          PixelWidth <span class="hljs-number">1200</span>

u  <span class="hljs-number">4</span>          PixelHeight <span class="hljs-number">900</span>

m  <span class="hljs-number">1</span>    Cluster                             clusterStartPos

u  <span class="hljs-number">2</span>      Timecode <span class="hljs-number">0</span>

b  <span class="hljs-number">2</span>      SimpleBlock track:<span class="hljs-number">2</span> timecode:<span class="hljs-number">0</span>  keyframe:<span class="hljs-literal">true</span> invisible:<span class="hljs-literal">false</span> discardable:<span class="hljs-literal">false</span> lacing:<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而根据 webm 官网描述（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.webmproject.org%2Fdocs%2Fcontainer%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.webmproject.org/docs/container/" ref="nofollow noopener noreferrer">链接</a>），一个正常的 webm 的头信息，应该解析如下：</p>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">m 0 EBML

u 1   EBMLVersion 1

u 1   EBMLReadVersion 1

u 1   EBMLMaxIDLength 4

u 1   EBMLMaxSizeLength 8

s 1   DocType webm

u 1   DocTypeVersion 4

u 1   DocTypeReadVersion 2

m 0 Segment

// 这部分缺失

m 1   SeekHead                            -> This is SeekPosition 0, so all SeekPositions can be calculated as (bytePos - segmentContentStartPos), which is 44 in this case

m 2     Seek

b 3       SeekID                          -> Buffer([0x15, 0x49, 0xA9, 0x66])  Info

u 3       SeekPosition                    -> infoStartPos =

m 2     Seek

b 3       SeekID                          -> Buffer([0x16, 0x54, 0xAE, 0x6B])  Tracks

u 3       SeekPosition &#123; tracksStartPos &#125;

m 2     Seek

b 3       SeekID                          -> Buffer([0x1C, 0x53, 0xBB, 0x6B])  Cues

u 3       SeekPosition &#123; cuesStartPos &#125;

m 1   Info

// 这部分缺失

f 2     Duration 32480                    -> overwrite, or insert if it doesn't exist

u 2     TimecodeScale 1000000

8 2     MuxingApp Chrome

8 2     WritingApp Chrome

m 1   Tracks

m 2     TrackEntry

u 3       TrackNumber 1

u 3       TrackUID 31790271978391090

u 3       TrackType 2

s 3       CodecID A_OPUS

b 3       CodecPrivate <Buffer 19>

m 3       Audio

f 4         SamplingFrequency 48000

u 4         Channels 1

m 2     TrackEntry

u 3       TrackNumber 2

u 3       TrackUID 24051277436254136

u 3       TrackType 1

s 3       CodecID V_VP9

m 3       Video

u 4         PixelWidth 1200

u 4         PixelHeight 900

// 这部分缺失

m  1   Cues                                -> cuesStartPos

m  2     CuePoint

u  3       CueTime 0

m  3       CueTrackPositions

u  4         CueTrack 1

u  4         CueClusterPosition 3911

m  2     CuePoint

u  3       CueTime 600

m  3       CueTrackPositions

u  4         CueTrack 1

u  4         CueClusterPosition 3911

m  1   Cluster

u  2     Timecode 0

b  2     SimpleBlock track:2 timecode:0 keyframe:true invisible:false discardable:false lacing:1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，我们只要修复好缺失的 Duration、SeakHead、Cues，就可以解决我们的问题，整体流程如下：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/189a16c4c1814f68923aa5c8bdfc8e1c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">ts-ebml 是一个社区开源的库，该库在 ebml 的 Decoder、Reader 实现的 ArrayBuffer 到可读 EBML 的相互转换能力的基础上，添加了 Webm 修复功能，但不支持大于 2GB 的视频文件，根本原因在于直接对 Blob 转换为 ArrayBuffer 是有问题的，ArrayBuffer 的最大长度仅为 2046 * 1024 * 1024， 为此早期我发布了一个叫做 fix-webm-metainfo 的 npm 包，利用 Buffer 的 slice 方法，使用 Buffer[]代替 Buffer 解决了该问题。</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">import</span> &#123; tools, Reader &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'ts-ebml'</span>;

<span class="hljs-keyword">import</span> LargeFileDecorder <span class="hljs-keyword">from</span> <span class="hljs-string">'./decoder'</span>;



<span class="hljs-comment">// fix-webm-metainfo 早期的实现过程</span>

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fixWebmMetaInfo</span>(<span class="hljs-params">blob: Blob</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">Blob</span>> </span>&#123;

  <span class="hljs-comment">// 解决ts-ebml不支持大于2GB视频文件的问题</span>

  <span class="hljs-keyword">const</span> decoder = <span class="hljs-keyword">new</span> LargeFileDecorder();

  <span class="hljs-keyword">const</span> reader = <span class="hljs-keyword">new</span> Reader();

  reader.logging = <span class="hljs-literal">false</span>;



  <span class="hljs-keyword">const</span> bufSlices: <span class="hljs-built_in">ArrayBuffer</span>[] = [];

  <span class="hljs-comment">// 由于Uint8Array或者ArrayBuffer支持的最大长度为2046 * 1024 * 1024</span>

  <span class="hljs-keyword">const</span> sliceLength = <span class="hljs-number">1</span> * <span class="hljs-number">1024</span> * <span class="hljs-number">1024</span> * <span class="hljs-number">1024</span>;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < blob.size; i = i + sliceLength) &#123;

    <span class="hljs-comment">// 切割Blob，并读取ArrayBuffer</span>

    <span class="hljs-keyword">const</span> bufSlice = <span class="hljs-keyword">await</span> blob.slice(i, <span class="hljs-built_in">Math</span>.min(i + sliceLength, blob.size)).arrayBuffer();

    bufSlices.push(bufSlice);

  &#125;



  <span class="hljs-comment">// 解析ArrayBuffer到可阅读与修改的EBML Element类型，并使用reader读取以计算Duration和Cues</span>

  decoder.decode(bufSlices).forEach(<span class="hljs-function"><span class="hljs-params">elm</span> =></span> reader.read(elm));



  <span class="hljs-comment">// 当全部读取结束后，结束reader</span>

  reader.stop();



  <span class="hljs-comment">// 利用reader生成好的cues与duration，重建meta头，并转换回arrayBuffer</span>

  <span class="hljs-keyword">const</span> refinedMetadataBuf = tools.makeMetadataSeekable(reader.metadatas, reader.duration, reader.cues);



  <span class="hljs-keyword">const</span> firstPartSlice = bufSlices.shift() <span class="hljs-keyword">as</span> <span class="hljs-built_in">ArrayBuffer</span>;

  <span class="hljs-keyword">const</span> firstPartSliceWithoutMetadata = firstPartSlice.slice(reader.metadataSize);



  <span class="hljs-comment">// 重建回Blob</span>

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Blob([refinedMetadataBuf, firstPartSliceWithoutMetadata, ...bufSlices], &#123; <span class="hljs-attr">type</span>: blob.type &#125;);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">进程卡死与缓存未复用问题</h1>
<p>随着视频长度的增加，fix-webm-metainfo 尽管解决了大尺寸长视频的修复问题，但面对大文件在短时间的全量读取与计算，存在短时间卡死渲染进程的问题。</p>
<h2 data-id="heading-21">Web Worker 处理</h2>
<p>Web Worker 天生适合该场景的处理，利用 Web Worker，我们可以在不额外创建进程的同时，额外创建一个 Worker 线程，专门进行大视频文件的处理与解析，同时不会卡死主线程，此外由于 Web Worker 支持以引用的方式（Transferable Object）传递 ArrayBuffer，因此也成了本问题最佳解决方法。首先在 Electron 的 BrowserWindow 中开启 nodeIntegrationInWorker：</p>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">webPreferences: &#123;
   ...
   nodeIntegration: true,
   nodeIntegrationInWorker: true,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着编写 Worker 进程：</p>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">import &#123; tools, Reader &#125; from 'ts-ebml';

import LargeFileDecorder from './decoder';



// index.worker.ts

export interface IWorkerPostData &#123;

  type: 'transfer' | 'close';

  data?: ArrayBuffer;

&#125;



export interface IWorkerEchoData &#123;

  buffer: ArrayBuffer;

  size: number;

  duration: number;

&#125;



const bufSlices: ArrayBuffer[] = [];



async function fixWebm(): Promise<void> &#123;

  const decoder = new LargeFileDecorder();

  const reader = new Reader();

  reader.logging = false;



  decoder.decode(bufSlices).forEach(elm => reader.read(elm));

  reader.stop();



  const refinedMetadataBuf = tools.makeMetadataSeekable(reader.metadatas, reader.duration, reader.cues);

  // 将计算后的结果传回父线程

  self.postMessage(&#123;

    buffer: refinedMetadataBuf,

    size: reader.metadataSize,

    duration: reader.duration

  &#125; as IWorkerEchoData, [refinedMetadataBuf]);

&#125;



self.addEventListener('message', (e: MessageEvent<IWorkerPostData>) => &#123;

  switch (e.data.type) &#123;

    case 'transfer':

      // 保存传递过来的ArrayBuffer

      bufSlices.push(e.data.data);

      break;

    case 'close':

      // 修复WebM，之后关闭Worker进程

      fixWebm().catch(self.postMessage).finally(() => self.close());

      break;

    default:

      break;

  &#125;

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父进程：</p>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">import FixWebmWorker from './worker/index.worker';

import type &#123; IWorkerPostData, IWorkerEchoData &#125; from './worker/index.worker';



async function fixWebmMetaInfo(blob: Blob): Promise<Blob> &#123;

  // 创建Worker进程

  const fixWebmWorker: Worker = new FixWebmWorker();



  return new Promise(async (resolve, reject) => &#123;

    fixWebmWorker.addEventListener('message', (event: MessageEvent<IWorkerEchoData>) => &#123;

      if (Object.getPrototypeOf(event.data)?.name === 'Error') &#123;

        return reject(event.data);

      &#125;



      let refinedMetadataBlob = new Blob([event.data.buffer], &#123; type: blob.type &#125;);

      // 手动关闭Worker进程

      fixWebmWorker.terminate();



      let body: Blob;

      let firstPartBlobSlice = blobSlices.shift();

      body = firstPartBlobSlice.slice(event.data.size);

      firstPartBlobSlice = null;



      // 注：除了利用Web Worker，与早期方案相比，并对meta ArrayBuffer生成Blob

      // 不再用ArrayBuffer重建，而是复用之前的Blob

      // 这一步做了之后会大量减少一次文件写入，并可解决引用不释放导致的内存泄露问题

      // 是本文最关键的决定性一步

      let blobFinal = new Blob([refinedMetadataBlob, body, ...blobSlices], &#123; type: blob.type &#125;);



      refinedMetadataBlob = null;

      body = null;

      blobSlices = [];



      resolve(blobFinal);

      blobFinal = null;

    &#125;);



    fixWebmWorker.addEventListener('error', (event: ErrorEvent) => &#123;

      blobSlices = [];

      reject(event);

    &#125;);



    let blobSlices: Blob[] = [];

    let slice: Blob;



    const sliceLength = 1 * 1024 * 1024 * 1024;

    try &#123;

      for (let i = 0; i < blob.size; i = i + sliceLength) &#123;

        slice = blob.slice(i, Math.min(i + sliceLength, blob.size));

        // 切片读取ArrayBuffer

        const bufSlice = await slice.arrayBuffer();

        // 发送给Worker进程，并利用 Transferable Objects 提高性能

        fixWebmWorker.postMessage(&#123;

          type: 'transfer',

          data: bufSlice

        &#125; as IWorkerPostData, [bufSlice]);

        blobSlices.push(slice);

        slice = null;

      &#125;

      // 结束处理

      fixWebmWorker.postMessage(&#123;

        type: 'close',

      &#125;);

    &#125; catch (e) &#123;

      blobSlices = [];

      slice = null;

      reject(new Error(`[fix webm] read buffer failed: $&#123;e?.message || e&#125;`));

    &#125;

  &#125;);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过对早期 fix-webm-metainfo 的修复过程中 blob_storage 暂存目录的分页文件进行观察，我们察觉到了明显的内存不释放以及文件重复生成的问题，再取出 fix-webm 逻辑后，该问题不再复现，这就说明目前的 fix-webm-metainfo 存在文件缓存未复用和文件引用未删除的问题（这个问题后面讨论）。</p>
<h2 data-id="heading-22">文件缓存复用</h2>
<p>那么在 ArrayBuffer 与 Blob 的转换中，是否有一种无损，且可复用文件缓存的方式呢？这就是为什么 fix-webm-metainfo 在后面的迭代中，采用了复用 Blob 的方式建立修复后的 Blob，而不是直接使用 ArrayBuffer 建立 Blob 的原因。观察下面的两种方式生成的 Blob 有什么区别：</p>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">// 首先创建一个Blob

const a = new Blob([new ArrayBuffer(10000000)]);



// 读出它的buffer

const buffer = await a.arrayBuffer();



// 方式1，实际会占用多少内存？

const b = new Blob([buffer]);

const c = new Blob([buffer]);

const d = new Blob([buffer]);

const e = new Blob([buffer]);

const f = new Blob([buffer]);

const g = new Blob([buffer]);

const h = new Blob([buffer]);



// 方式2，那这种呢？

const i = new Blob([a]);

const j = new Blob([a]);

const k = new Blob([a]);

const l = new Blob([a]);

const m = new Blob([a]);

const n = new Blob([a]);

const o = new Blob([a]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>猜猜答案是什么？是的，Blob 存在复用本地文件缓存的机制，方式 1 会在内存或磁盘生成 7 份一模一样的文件，而方式 2 不会额外生成一个文件，i 到 o 的文件均复用了 a 的 blob，在内存或磁盘中只存在一份。那么，修复 webm 的那种方式本质上修改了文件头部的字节，那这种方式也会复用同一个本地文件缓存么？答案是肯定的，被修复前的 webm 和被修复后的 webm 由于差异仅在头部，而整体的大部分区域均采用相同的 Blob slice 出来的子 blob 建立，因此空间依然是复用的。</p>
<h1 data-id="heading-23">主进程内存泄露问题</h1>
<p>根据 Electron 官方提供的 process.getProcessMemoryInfo() api，我们分别对主进程和渲染进程实现了内存监控，通过监控发现使用录屏的用户的主进程内存占用经常可以达到 2GB，而不使用录屏功能的用户，主进程内存占用仅 80MB，这说明百分百存在内存泄露。
在谈及主进程内存泄漏问题之前，不得不提及 Blob 文件类型的实现方式。根据 Chromium Blob 实现官方说明（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.google.com%2Fpresentation%2Fd%2F1MOm-8kacXAon1L2tF6VthesNjXgx0fp5AP17L7XDPSM%2Fedit%23slide%3Did.g91839e9b6_4_5" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.google.com/presentation/d/1MOm-8kacXAon1L2tF6VthesNjXgx0fp5AP17L7XDPSM/edit#slide=id.g91839e9b6_4_5" ref="nofollow noopener noreferrer">PPT</a>）如下图，我们在 Renderer 进程通过任何一种方式创建的 Blob，本质上最终都会有一个跨进程传输到 Browser 进程的过程（即主进程），也就是说尽管 MediaRecorder 是基于渲染进程的录制，但在将缓冲区文件输出为 Blob 的过程（即 ondataavailable 触发瞬间），会存在跨进程传输。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5a42ccd45e54ed599e0707345184f03~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
以上说明了在“渲染进程”录制，而“主进程”内存占用不断增大的根本原因，那么再具体点，Blob 到底是怎么传输的？
换句话说，我们仅知道创建 Blob 时，二进制数据会跨进程传输到主进程是不够的。
如果文件足够大，主进程内存不足会怎样？
Chromium 又是如何管理并存储 Blob 内包含的二进制文件呢？</p>
<h2 data-id="heading-24">Blob 的传输方式</h2>
<p>这里我们通过阅读 Chromium 的 Blob Controller（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsource.chromium.org%2Fchromium%2Fchromium%2Fsrc%2F%2B%2Fmaster%3Astorage%2Fbrowser%2Fblob%2Fblob_memory_controller.cc%3Fq%3DCalculateBlobStorageLimitsImpl%26ss%3Dchromium" target="_blank" rel="nofollow noopener noreferrer" title="https://source.chromium.org/chromium/chromium/src/+/master:storage/browser/blob/blob_memory_controller.cc?q=CalculateBlobStorageLimitsImpl&ss=chromium" ref="nofollow noopener noreferrer">Code</a>）并添加 LOG(INFO)观察</p>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">// 作用：判断传输策略

// storage/browser/blob/blob_memory_controller.cc

BlobMemoryController::Strategy BlobMemoryController::DetermineStrategy(

    size_t preemptive_transported_bytes,

    uint64_t total_transportation_bytes) const &#123;

  // Blob文件大小为0，不需要传输

  if (total_transportation_bytes == 0)

    return Strategy::NONE_NEEDED;

  // 当Blob文件大小大于可用内存数，且大于可用磁盘空间时，传输直接失败

  if (!CanReserveQuota(total_transportation_bytes))

    return Strategy::TOO_LARGE;



  // 普通调用可忽略

  if (preemptive_transported_bytes == total_transportation_bytes &&

      pending_memory_quota_tasks_.empty() &&

      preemptive_transported_bytes <= GetAvailableMemoryForBlobs()) &#123;

    return Strategy::NONE_NEEDED;

  &#125;



  // Chromium编译时开启文件分页（默认开启），且配置了override_file_transport_min_size时

  if (UNLIKELY(limits_.override_file_transport_min_size > 0) &&

      file_paging_enabled_ &&

      total_transportation_bytes >= limits_.override_file_transport_min_size) &#123;

    return Strategy::FILE;

  &#125;



  // Blob小于0.25MB时，直接走ipc传输

  if (total_transportation_bytes <= limits_.max_ipc_memory_size)

    return Strategy::IPC;



  // Chromium编译时开启文件分页（默认开启）

  // Blob文件大小小于可用磁盘空间

  // Blob文件大小大于可用内存空间

  if (file_paging_enabled_ &&

      total_transportation_bytes <= GetAvailableFileSpaceForBlobs() &&

      total_transportation_bytes > limits_.memory_limit_before_paging()) &#123;

    return Strategy::FILE;

  &#125;



  // 默认传输策略，即内存共享方式，通过渲染进程传递给主进程

  return Strategy::SHARED_MEMORY;

&#125;



bool BlobMemoryController::CanReserveQuota(uint64_t size) const &#123;

  // 同时检查内“可用内存空间”与“可用磁盘空间”

  return size <= GetAvailableMemoryForBlobs() ||

         size <= GetAvailableFileSpaceForBlobs();

&#125;



// 如果当前内存使用量小于2GB（按x64电脑算，max_blob_in_memory_space = 2 * 1024 * 1024 * 1024）

// 计算剩余内存量

size_t BlobMemoryController::GetAvailableMemoryForBlobs() const &#123;

  if (limits_.max_blob_in_memory_space < memory_usage())

    return 0;

  return limits_.max_blob_in_memory_space - memory_usage();

&#125;



// 计算剩余磁盘量

uint64_t BlobMemoryController::GetAvailableFileSpaceForBlobs() const &#123;

  if (!file_paging_enabled_)

    return 0;

  uint64_t total_disk_used = disk_used_;

  if (in_flight_memory_used_ < pending_memory_quota_total_size_) &#123;

    total_disk_used +=

        pending_memory_quota_total_size_ - in_flight_memory_used_;

  &#125;

  if (limits_.effective_max_disk_space < total_disk_used)

    return 0;

  // 实际最大磁盘空间 - 已用磁盘空间

  return limits_.effective_max_disk_space - total_disk_used;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可发现：Blob 的传输与储存基本分为三种，即：“文件”，“共享内存”，以及“IPC”，</p>
<ol>
<li>当文件小于 0.25MB 时优先走“IPC”方式传输</li>
<li>当“可用内存空间”大于文件体积时优先走“共享内存”方式传输</li>
<li>当“可用内存空间”不足但“可用磁盘空间”充足时，优先走“文件”方式传输</li>
<li>当“可用内存空间”与“可用磁盘空间”均不充足时，Blob 不会传输，且最终反馈到渲染进程，会报“File not readble”之类的报错。</li>
</ol>
<h2 data-id="heading-25">最大存储限制</h2>
<p>这里引发一个问题“可用内存空间”与“可用磁盘空间”是如何界定的？如果计算？
想到这里，又引发我的思考，如果可用内存空间非常大，会造成什么问题？带着这些疑问，我们继续研究 Chromium 的实现：</p>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">BlobStorageLimits CalculateBlobStorageLimitsImpl(

    const FilePath& storage_dir,

    bool disk_enabled,

    base::Optional<int64_t> optional_memory_size_for_testing) &#123;

  int64_t disk_size = 0ull;

  int64_t memory_size = optional_memory_size_for_testing

                            ? optional_memory_size_for_testing.value()

                            : base::SysInfo::AmountOfPhysicalMemory();

  if (disk_enabled && CreateBlobDirectory(storage_dir) == base::File::FILE_OK)

    disk_size = base::SysInfo::AmountOfTotalDiskSpace(storage_dir);



  BlobStorageLimits limits;



  if (memory_size > 0) &#123;

#if !defined(OS_CHROMEOS) && !defined(OS_ANDROID) && !defined(OS_ANDROID) && defined(ARCH_CPU_64_BITS)

    // 不是ChromeOS，不是安卓，且架构是64位，则“最大可用内存大小”为2GB

    constexpr size_t kTwoGigabytes = 2ull * 1024 * 1024 * 1024;

    limits.max_blob_in_memory_space = kTwoGigabytes;

#elif defined(OS_ANDROID)

    // 安卓，“最大可用内存”为物理内存的1/100

    limits.max_blob_in_memory_space = static_cast<size_t>(memory_size / 100ll);

#else

    // 其他架构或，“最大可用内存”为物理内存的1/5

    limits.max_blob_in_memory_space = static_cast<size_t>(memory_size / 5ll);

#endif

  &#125;



  // 实现了一下“最大可用内存”的最小值不小于两倍的“最小分页大小”

  if (limits.max_blob_in_memory_space < limits.min_page_file_size)

    limits.max_blob_in_memory_space = limits.min_page_file_size;



  if (disk_size >= 0) &#123;

#if defined(OS_CHROMEOS)

    // ChromeOS，“最大可用磁盘大小”为物理磁盘大小的1/2

    limits.desired_max_disk_space = static_cast<uint64_t>(disk_size / 2ll);

#elif defined(OS_ANDROID)

     // Android，“最大可用磁盘大小”为物理磁盘大小3/50

    limits.desired_max_disk_space = static_cast<uint64_t>(3ll * disk_size / 50);

#else

     // 其他平台或架构，“最大可用磁盘大小”为物理磁盘大小1/10

    limits.desired_max_disk_space = static_cast<uint64_t>(disk_size / 10);

#endif

  &#125;

  if (disk_enabled) &#123;

    UMA_HISTOGRAM_COUNTS_1M("Storage.Blob.MaxDiskSpace2",

                            limits.desired_max_disk_space / kMegabyte);

  &#125;

  limits.effective_max_disk_space = limits.desired_max_disk_space;



  CHECK(limits.IsValid());



  return limits;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结一下两个指标，与 OS、Arch、Memory Size、Disk Size 都有可能有关系：</p>
<blockquote>
<p><strong>最大可用内存大小</strong></p>
</blockquote>
<ul>
<li>
<blockquote>
<p>架构是 x64 且平台不是 Chrome OS 或 Android:<code>2GB</code></p>
</blockquote>
</li>
</ul>
<ul>
<li>
<blockquote>
<p>平台是 Android:<code>所在设备物理内存大小/ 100</code></p>
</blockquote>
</li>
<li>
<blockquote>
<p>其他平台或架构（例如 macOS arm64，chromeOS）:<code>所在设备物理内存大小 / 5</code></p>
</blockquote>
</li>
</ul>
<blockquote>
<p><strong>最大可用磁盘大小</strong></p>
</blockquote>
<ul>
<li>
<blockquote>
<p>平台是 Chrome OS:<code>所在设备，软件所在分区的逻辑磁盘的大小 / 2</code></p>
</blockquote>
</li>
</ul>
<ul>
<li>
<blockquote>
<p>平台是安卓:<code>所在设备，软件所在分区的逻辑磁盘的大小 * 3/50</code></p>
</blockquote>
</li>
<li>
<blockquote>
<p>其他平台或架构:<code>所在设备，软件所在分区的逻辑磁盘的大小 / 10</code></p>
</blockquote>
</li>
</ul>
<p>以上结论说明了什么？我们从中发现了两个问题：</p>
<ol>
<li>问题 1：X64 架构的最大可用内存是 2GB，这实际上非常大了，用户的录屏存储并非频繁访问的内容，用户的电脑可能只有 8GB，如果这 2GB 平白被占据实际上是很大一个浪费。</li>
<li>问题 2：X64 与非 X64 架构的最大可用内存并不一致。</li>
<li>问题 3：最大可用磁盘大小仅为物理硬盘大小的 1/10, 以 128GB 的 SSD 硬盘为例，即使将全部 128GB 均分配给 C 盘，那么最大可用磁盘大小仅为 12.8GB，不考虑其他任何 Blob 的磁盘占用，即使用户 C 盘有 100GB 的剩余空间，依然逃不了录屏文件体积被限制到 12.8GB 的尴尬。</li>
</ol>
<p>事实真相大白，主进程并非“内存泄露”而是“设计如此”。</p>
<h2 data-id="heading-26">修改 Chromium</h2>
<p>那么我们如果将最大内存空间改小，将最大可用磁盘空间改大，是不是即可解决主进程内存占用问题，又解决了录屏文件体积限制两个问题呢？
答案是肯定的，修改起来也很简单：</p>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">  // 如果物理内存数大于0
  if (memory_size > 0) &#123;

#if !defined(OS_CHROMEOS) && !defined(OS_ANDROID)

    // 去除64位判断逻辑，保持32位 Windows，Arm64 Mac一致的2000MB -> 200MB最大内存录制空间逻辑修改

    constexpr size_t kTwoHundrendMegabytes = 2ull * 100 * 1024 * 1024;

    limits.max_blob_in_memory_space = kTwoHundrendMegabytes;

#elif defined(OS_ANDROID)

    limits.max_blob_in_memory_space = static_cast<size_t>(memory_size / 100ll);

#else

    limits.max_blob_in_memory_space = static_cast<size_t>(memory_size / 5ll);

#endif

  &#125;


  if (limits.max_blob_in_memory_space < limits.min_page_file_size)

    limits.max_blob_in_memory_space = limits.min_page_file_size;


  if (disk_size >= 0) &#123;

#if defined(OS_CHROMEOS)

    limits.desired_max_disk_space = static_cast<uint64_t>(disk_size / 2ll);

#elif defined(OS_ANDROID)

    limits.desired_max_disk_space = static_cast<uint64_t>(3ll * disk_size / 50);

#else

    // 去除录屏Blob_Storage的大小限制, 最大空间由完整磁盘空间的1/10 变为 1

    limits.desired_max_disk_space = static_cast<uint64_t>(disk_size);

#endif

  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你有类似的需要，可以直接复用该修改，且无任何副作用。</p>
<h1 data-id="heading-27">缓冲区内存释放问题</h1>
<p>有了上述对 Blob 文件格式的理解，我们基本可以理清录屏功能的整个传输链路。缓冲区内存释放问题的解法，相信大家也能想到了，在录制过程中，未对 MediaRecorder stop 前，由于 MediaRecorder 录制的全部数据均存储于 Renderer 进程中，便会造成内存的异常占用，随着录屏时间的增长，这部分的占用会尤为庞大，解决方法也很简单，设定一个 timeslice 或定时 requestData()即可</p>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">const recorder = new MediaRecorder(combinedSource, &#123;

   mimeType: 'video/webm;codecs=vp9',

   videoBitsPerSecond: 1.5e6,

&#125;);


const timeslice = 5000;

const fileBits: Blob[] = [];


recorder.ondataavailable = (event: BlobEvent) => &#123;

    fileBits.push(event.data as Blob);

&#125;



recorder.onstop = () => &#123;

    const videoFile = new Blob(fileBits, &#123; type: 'video/webm;codecs=vp9' &#125;);

&#125;



// 解法一，开始录制时，设定timeSlice，确保每timeslice毫秒，自动触发一次ondataavailable，输出并清空缓冲区（非常重要）

recorder.start(timeslice);



// 解法二，录制过程中手动requestData清空缓冲区

recorder.start();

setInterval(() => recorder.requestData(), timeslice);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-28">渲染进程内存泄露问题</h1>
<p>在编写过程中，由于一些疏忽，我们可能会写出具有内存泄露的代码，那么如何解决该问题？结论是，时刻遵循以下原则：</p>
<ol>
<li>
<pre><code class="copyable">  一切对Blob的引用都及时清除
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">  尽量用let 指向Blob并手动释放，防止引用不释放的情况发生
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<pre><code class="hljs language-Javacript copyable" lang="Javacript">// 例1

const a = new Map();



a.set('key', &#123;

    blob: new Blob([1]) // Blob1

&#125;);



// 手动释放

a.get('key').blob = null;



// 例2

let a = new Blob([]);



doSomething(a);



// 手动释放

a = null;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">Blob-Internals 观察引用</h2>
<p>若想随时 Debug，可以通过观察 Blob 的引用计数的方式，直接访问 chrome://blob-internals/<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/995d95ac2673436fbc3d7acd30a8facc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
以上图为例，每一个 Blob 均有一个独一无二的 UUID，通过观察某 UUID 的 Blob 的引用计数，我们可以相对较轻松的 Debug Blob 的泄露情况。</p>
<h2 data-id="heading-30">Profiler 抓取堆快照</h2>
<p>也可以利用 Profiler 抓取内存堆栈情况。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdc64676b843449c8bd634d45dc3a106~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-31">blob_storage 目录观察</h2>
<p>如果你有对 Chromium 修改的能力，可以通过将“最大可用内存”改为较小值（比如 10MB，以此迫使 Blob 直接走文件传输方式存储到硬盘），直接观测 blob_storage 目录内分页文件的产生。Blob 文件在本地磁盘是以分页的形式存储，它的大小是一个动态值，最小为 5MB，最大为 100MB。每次关闭应用时该目录都会被清空，因此需要确保应用开启并持续观测，这种方式是目前最为直观易用的方式，一般来说如果用户持续不关闭应用，而你的代码又存在内存泄露，那么基本可以观察到该目录会产生大量的分页文件而不被释放。</p>
<h1 data-id="heading-32">后续的性能优化</h1>
<p>当前的处理，尽管已经完美解决了一切修复问题，但存在最后一个问题，就是修复时会占用大量内存，后续我会持续维护 fix-webm-metainfo 库，通过不传输完整 ArrayBuffer 的方式，解决这个问题。</p>
<p>欢迎关注「 字节前端 ByteFE 」</p>
<p>简历投递联系邮箱「<a href="https://link.juejin.cn/?target=mailto%3Atech%40bytedance.com" target="_blank" title="mailto:tech@bytedance.com" ref="nofollow noopener noreferrer">tech@bytedance.com</a>」</p></div>  
</div>
            