
---
title: 'ShowMeBug字节级回放在线笔面试过程实现思路'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6f5de298b6741e2a4c59394c392b2f6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 00:35:30 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6f5de298b6741e2a4c59394c392b2f6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p>为一个数字化驱动的可记录、可分析、可复盘的技术评估与在线 Coding 面试平台，<a href="https://link.juejin.cn/?target=http%3A%2F%2Fshowmebug.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://showmebug.com/" ref="nofollow noopener noreferrer">ShowMeBug</a> 的字节级回放在线笔面试过程特别为面试官和 HR 们所看重。</p>
<p>那么 ShowMeBug 是怎么做到让面试官和 HR 像看电影一样，回看候选人的在线笔面试过程呢？今天小编就和大家一起来看看，Web 端实现回放功能的方案都有哪些。</p>
<h2 data-id="heading-0">方案一：MediaRecorder 录屏</h2>
<p>MediaRecorder 是最新的 Web 标准（仍处于工作草案状态），目的是方便用户进行媒体录制，不过也正因为该标准非常新，故浏览器兼容性不是很好，对于 ShowMeBug 这种需要适配诸多设备类型的场景而言，不是很合适。</p>
<h2 data-id="heading-1">方案二：Canvas 截图</h2>
<p>这一方案主要是利用了 canvas.captureStream() 这个接口，将 canvas 中获取到的截图以流的方式传给上面提到的 MediaRecorder 接口，从而生成视频。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> allChunks=[];
<span class="hljs-keyword">let</span> canvas=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvasId"</span>);
<span class="hljs-keyword">let</span> stream=canvas.captureStream(<span class="hljs-number">60</span>); <span class="hljs-comment">// 60 帧每秒</span>
<span class="hljs-keyword">let</span> recorder=newMediaRecorder(stream, &#123;
  <span class="hljs-attr">mimeType</span>: <span class="hljs-string">'video/webm;codecs=vp9'</span>,
&#125;);
<span class="hljs-comment">// canvas 录制回调</span>
recorder.ondataavailable=<span class="hljs-function">(<span class="hljs-params">e</span>)=></span>&#123;
   allChunks.push(e.data);
&#125;
recorder.start(<span class="hljs-number">10</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一方案的问题主要是要生成流畅的视频需要消耗非常大的带宽，且只适用于 canvas 录屏，虽然有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fniklasvh%2Fhtml2canvas" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/niklasvh/html2canvas" ref="nofollow noopener noreferrer">html2canvas</a> 这种库，但也没到可应用于生产环境的程度。</p>
<h2 data-id="heading-2">方案三：基于用户操作记录还原</h2>
<p>那我们是否可以收集用户的操作序列，然后按照操作的先后顺序，将操作应用到需要录屏的页面DOM上呢？这样不就能还原用户的所有操作过程了吗？</p>
<p>要做到这一点，我们需要：</p>
<ol>
<li>在前端用 MutationObserver API 监听 DOM 变更，比如节点增减、属性变化、文本内容变动等；</li>
<li>监听用户鼠标的 mouseover 事件，并将其变动时的坐标和时间记录下来；</li>
<li>将上述两步的记录按照时间先后顺序放入队列并上传到服务器；</li>
<li>后端将事件队列应用到初始页面上，生成图片再拼接成视频；</li>
<li>最后将视频链接发送给用户即可。</li>
</ol>
<p>这个方案网络开销小，且兼容性好，非常适合录屏回放的场景。知名录屏回放工具 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frrweb-io%2Frrweb" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rrweb-io/rrweb" ref="nofollow noopener noreferrer">rrweb</a> 就是这么实现的。</p>
<blockquote>
<p>rrweb 是 'record and replay the web'（录制并回放互联网） 的简写，旨在利用现代浏览器所提供的强大 API 录制并回放任意 web 界面中的用户操作。</p>
<p>rrweb 主要由 3 部分组成：</p>
<p>rrweb-snapshot，包含 snapshot 和 rebuild 两个功能。snapshot 用于将 DOM 及其状态转化为可序列化的数据结构并添加唯一标识；rebuild 则是将 snapshot 记录的数据结构重建为对应的 DOM。</p>
<p>rrweb，包含 record 和 replay 两个功能。record 用于记录 DOM 中的所有变更（mutation）；replay 则是将记录的变更按照对应的时间一一重放。</p>
<p>rrweb-player，为 rrweb 提供一套 UI 控件，提供基于 GUI 的暂停、快进、拖拽至任意时间点播放等功能。</p>
</blockquote>
<p>可以看出，rrweb 就是第三个方案的实现，不过 ShowMeBug 并没有使用 rrweb，而是投入了大量精力，基于第三个方案自研了字节级回放技术。让笔面试过程都有存档，方便面试官和 HR 回溯笔面试过程每一秒。</p>
<p>因为用心，所以专业，如果您有在线笔面试需求，欢迎试用 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fshowmebug.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://showmebug.com/" ref="nofollow noopener noreferrer">ShowMeBug</a>  哦～</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6f5de298b6741e2a4c59394c392b2f6~tplv-k3u1fbpfcp-watermark.image" alt="footer.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            