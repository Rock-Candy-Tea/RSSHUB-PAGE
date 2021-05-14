
---
title: '在Javascript应用程序中执行语音识别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41f7c50f50394b6ca4c7e6853aeeacdf~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 04:57:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41f7c50f50394b6ca4c7e6853aeeacdf~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文：<a href="https://betterprogramming.pub/perform-speech-recognition-in-your-javascript-applications-91367b0d0" target="_blank" rel="nofollow noopener noreferrer">betterprogramming.pub/perform-spe…</a></p>
<p>作者：Jennifer Fu</p>
</blockquote>
<p>语音识别是计算机科学和计算语言学的一个跨学科子领域。它可以识别口语并将其翻译成文本，它也被称为自动语音识别（ASR），计算机语音识别或语音转文本（STT）。</p>
<p>机器学习（ML）是人工智能（AI）的一种应用，它使系统能够自动学习并从经验中进行改进，而无需进行明确的编程。机器学习在本世纪提供了大多数语音识别方面的突破。如今，语音识别技术无处不在，例如Apple Siri，Amazon Echo和Google Nest。</p>
<p>语音识别以及语音响应（也称为语音合成或文本到语音（TTS））由Web speech API提供支持。</p>
<p>在本文中，我们重点介绍JavaScript应用程序中的语音识别。另一篇文章介绍了<a href="https://medium.com/better-programming/perform-speech-synthesis-in-your-javascript-applications-ac3efa1eb6fa" target="_blank" rel="nofollow noopener noreferrer">语音合成</a>。</p>
<h2 data-id="heading-0">语音识别接口</h2>
<p><code>SpeechRecognition</code> 是识别服务的控制器接口，在Chrome中称为 <code>webkitSpeechRecognition</code>。<code>SpeechRecognition</code> 处理从识别服务发送的 <code>SpeechRecognitionEvent</code>。<code>SpeechRecognitionEvent.results</code> 返回一个<code>SpeechRecognitionResultList</code> 对象，该对象表示当前会话的所有语音识别结果。</p>
<p>可以使用以下几行代码来初始化 <code>SpeechRecognition</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建一个SpeechRecognition对象</span>
<span class="hljs-keyword">const</span> recognition = <span class="hljs-keyword">new</span> webkitSpeechRecognition();

<span class="hljs-comment">// 配置设置以使每次识别都返回连续结果</span>
recognition.continuous = <span class="hljs-literal">true</span>;

<span class="hljs-comment">// 配置应返回临时结果的设置</span>
recognition.interimResults = <span class="hljs-literal">true</span>;

<span class="hljs-comment">// 正确识别单词或短语时的事件处理程序</span>
recognition.onresult = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(event.results);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ognition.start()</code> 开始语音识别，而 <code>ognition.stop()</code> 停止语音识别，它也可以中止（ <code>recognition.abort</code>）。</p>
<p>当页面正在访问您的麦克风时，地址栏中将显示一个麦克风图标，以显示该麦克风已打开并且正在运行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41f7c50f50394b6ca4c7e6853aeeacdf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们用句子对页面说。“hello comma I'm talking period.” <code>onresult</code> 在我们说话时显示所有临时结果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bab2af4b79f3403e94a445639baf4a50~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是此示例的HTML代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Speech Recognition<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> button = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'button'</span>);
        button.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">if</span> (button.style[<span class="hljs-string">'animation-name'</span>] === <span class="hljs-string">'flash'</span>) &#123;
            recognition.stop();
            button.style[<span class="hljs-string">'animation-name'</span>] = <span class="hljs-string">'none'</span>;
            button.innerText = <span class="hljs-string">'Press to Start'</span>;
            content.innerText = <span class="hljs-string">''</span>;
          &#125; <span class="hljs-keyword">else</span> &#123;
            button.style[<span class="hljs-string">'animation-name'</span>] = <span class="hljs-string">'flash'</span>;
            button.innerText = <span class="hljs-string">'Press to Stop'</span>;
            recognition.start();
          &#125;
        &#125;);

        <span class="hljs-keyword">const</span> content = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'content'</span>);

        <span class="hljs-keyword">const</span> recognition = <span class="hljs-keyword">new</span> webkitSpeechRecognition();
        recognition.continuous = <span class="hljs-literal">true</span>;
        recognition.interimResults = <span class="hljs-literal">true</span>;
        recognition.onresult = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
          <span class="hljs-keyword">let</span> result = <span class="hljs-string">''</span>;
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = event.resultIndex; i < event.results.length; i++) &#123;
            result += event.results[i][<span class="hljs-number">0</span>].transcript;
          &#125;
          content.innerText = result;
        &#125;;
      &#125;;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      <span class="hljs-selector-tag">button</span> &#123;
        <span class="hljs-attribute">background</span>: yellow;
        <span class="hljs-attribute">animation-name</span>: none;
        <span class="hljs-attribute">animation-duration</span>: <span class="hljs-number">3s</span>;
        <span class="hljs-attribute">animation-iteration-count</span>: infinite;
      &#125;
      <span class="hljs-keyword">@keyframes</span> flash &#123;
        <span class="hljs-number">0%</span> &#123;
          <span class="hljs-attribute">background</span>: red;
        &#125;
        <span class="hljs-number">50%</span> &#123;
          <span class="hljs-attribute">background</span>: green;
        &#125;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"button"</span>></span>Press to Start<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第25行创建了 <code>SpeechRecognition</code> 对象，第26和27行配置了 <code>SpeechRecognition</code> 对象。</p>
<p>当一个单词或短语被正确识别时，第28-34行设置一个事件处理程序。</p>
<p>第19行开始语音识别，第12行停止语音识别。</p>
<p>在第12行，单击该按钮后，它可能仍会打印出一些消息。这是因为 <code>Recognition.stop()</code> 尝试返回到目前为止捕获的<code>SpeechRecognitionResult</code>。如果您希望它完全停止，请改用 <code>ognition.abort()</code>。</p>
<p>您会看到动画按钮的代码（第38-51行）比语音识别代码长。这是该示例的视频剪辑：<a href="https://youtu.be/5V3bb5YOnj0" target="_blank" rel="nofollow noopener noreferrer">youtu.be/5V3bb5YOnj0</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3920e3c9b7fb426995bde4ec4340cdc7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以下是浏览器兼容性表：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43441faf15d542308185224e6fc8e489~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>网络语音识别依赖于浏览器自己的语音识别引擎。在Chrome中，此引擎在云中执行识别。因此，它仅可在线运行。</p>
<h2 data-id="heading-1">语音识别库</h2>
<p>有一些开源语音识别库，以下是基于npm趋势的这些库的列表：</p>
<h3 data-id="heading-2">1. Annyang</h3>
<p><a href="https://github.com/TalAter/annyang" target="_blank" rel="nofollow noopener noreferrer">Annyang</a>是一个JavaScript语音识别库，用于通过语音命令控制网站。它建立在SpeechRecognition Web API之上。在下一节中，我们将举例说明annyang的工作原理。</p>
<h3 data-id="heading-3">2. artyom.js</h3>
<p><a href="https://github.com/sdkcarlos/artyom.js" target="_blank" rel="nofollow noopener noreferrer">artyom.js</a>是一个JavaScript语音识别和语音合成库。它建立在Web语音API的基础上，除语音命令外，它还提供语音响应。</p>
<h3 data-id="heading-4">3. Mumble</h3>
<p><a href="https://github.com/jrunestone/mumble" target="_blank" rel="nofollow noopener noreferrer">Mumble</a>是一个JavaScript语音识别库，用于通过语音命令控制网站。它建立在SpeechRecognition Web API之上，这类似于annyang的工作方式。</p>
<h3 data-id="heading-5">4. julius.js</h3>
<p><a href="https://github.com/julius-speech/julius" target="_blank" rel="nofollow noopener noreferrer">Julius</a>是面向语音相关研究人员和开发人员的高性能，占用空间小的大词汇量连续语音识别（LVCSR）解码器软件。它可以在从微型计算机到云服务器的各种计算机和设备上执行实时解码。Julis是使用C语言构建的，而julius.js是Julius自以为是JavaScript的移植版。</p>
<h3 data-id="heading-6">5.voice-commands.js</h3>
<p><a href="https://github.com/jimmybyrum/voice-commands.js" target="_blank" rel="nofollow noopener noreferrer">voice-commands.js</a>是一个JavaScript语音识别库，用于通过语音命令控制网站。它建立在SpeechRecognition Web API之上，这类似于annyang的工作方式。</p>
<h2 data-id="heading-7">Annyang</h2>
<p>Annyang初始化一个 <code>SpeechRecognition</code> 对象，该对象定义如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> SpeechRecognition = root.SpeechRecognition ||                                     
                        root.webkitSpeechRecognition ||                          
                        root.mozSpeechRecognition ||                          
                        root.msSpeechRecognition ||                          
                        root.oSpeechRecognition;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有一些API可以启动或停止annyang：</p>
<ul>
<li><code>annyang.start</code>：使用选项（自动重启，连续或暂停）开始监听，例如 <code>annyang.start(&#123;autoRestart：true，Continuous：false&#125;)</code>。</li>
<li><code>annyang.abort</code>：停止收听（停止SpeechRecognition引擎或关闭麦克风）。</li>
<li><code>annyang.pause</code>：停止收听（无需停止SpeechRecognition引擎或关闭麦克风）。</li>
<li><code>annyang.resume</code>：开始收听时不带任何选项。</li>
</ul>
<p>这是此示例的HTML代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Annyang<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"//cdnjs.cloudflare.com/ajax/libs/annyang/2.6.1/annyang.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> button = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'button'</span>);
        button.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">if</span> (button.style[<span class="hljs-string">'animation-name'</span>] === <span class="hljs-string">'flash'</span>) &#123;
            annyang.pause();
            button.style[<span class="hljs-string">'animation-name'</span>] = <span class="hljs-string">'none'</span>;
            button.innerText = <span class="hljs-string">'Press to Start'</span>;
            content.innerText = <span class="hljs-string">''</span>;
          &#125; <span class="hljs-keyword">else</span> &#123;
            button.style[<span class="hljs-string">'animation-name'</span>] = <span class="hljs-string">'flash'</span>;
            button.innerText = <span class="hljs-string">'Press to Stop'</span>;
            annyang.start();
          &#125;
        &#125;);

        <span class="hljs-keyword">const</span> content = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'content'</span>);

        <span class="hljs-keyword">const</span> commands = &#123;
          <span class="hljs-attr">hello</span>: <span class="hljs-function">() =></span> &#123;
            content.innerText = <span class="hljs-string">'You said hello.'</span>;
          &#125;,
          <span class="hljs-string">'hi *splats'</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
            content.innerText = <span class="hljs-string">`You greeted to <span class="hljs-subst">$&#123;name&#125;</span>.`</span>;
          &#125;,
          <span class="hljs-string">'Today is :day'</span>: <span class="hljs-function">(<span class="hljs-params">day</span>) =></span> &#123;
            content.innerText = <span class="hljs-string">`You said <span class="hljs-subst">$&#123;day&#125;</span>.`</span>;
          &#125;,
          <span class="hljs-string">'(red) (green) (blue)'</span>: <span class="hljs-function">() =></span> &#123;
            content.innerText = <span class="hljs-string">'You said a primary color name.'</span>;
          &#125;,
        &#125;;

        annyang.addCommands(commands);
      &#125;;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      <span class="hljs-selector-tag">button</span> &#123;
        <span class="hljs-attribute">background</span>: yellow;
        <span class="hljs-attribute">animation-name</span>: none;
        <span class="hljs-attribute">animation-duration</span>: <span class="hljs-number">3s</span>;
        <span class="hljs-attribute">animation-iteration-count</span>: infinite;
      &#125;
      <span class="hljs-keyword">@keyframes</span> flash &#123;
        <span class="hljs-number">0%</span> &#123;
          <span class="hljs-attribute">background</span>: red;
        &#125;
        <span class="hljs-number">50%</span> &#123;
          <span class="hljs-attribute">background</span>: green;
        &#125;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"button"</span>></span>Press to Start<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第7行添加了annyang源代码。</p>
<p>第20行启动annyang，第13行暂停annyang。</p>
<p>Annyang提供语音命令来控制网页（第26-42行）。</p>
<p>第27行是一个简单的命令。如果用户打招呼，页面将回复“您说‘你好’。”</p>
<p>第30行是带有 <code>splats</code> 的命令，该命令会贪婪地捕获命令末尾的多词文本。如果您说“<code>hi</code>,爱丽丝e”，它的回答是“您向爱丽丝致意。”如果您说“嗨，爱丽丝和约翰”，它的回答是“您向爱丽丝和约翰打招呼。”</p>
<p>第33行是一个带有命名变量的命令。一周的日期被捕获为 <code>day</code>，在响应中被呼出。</p>
<p>第36行是带有可选单词的命令。如果您说“黄色”，则将其忽略。如果您提到任何一种原色，则会以“您说的是原色名称”作为响应。</p>
<p>从第26行到第39行定义的所有命令都在第41行添加到annyang中。</p>
<p>... ...</p>
<h2 data-id="heading-8">结束</h2>
<p>我们已经了解了JavaScript应用程序中的语音识别，Chrome对Web语音API提供了最好的支持。我们所有的示例都是在Chrome浏览器上实现和测试的。</p>
<p>在探索Web语音API时，这里有一些提示：如果您不想在日常生活中倾听，请记住关闭语音识别应用程序。</p></div>  
</div>
            