
---
title: '【SSD系列】五分钟，100余行代码，纯web技术一起实现摄像头和麦克风视频录制，并带历史记录功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0186363530cb415b926106e2e54f9823~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 16:18:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0186363530cb415b926106e2e54f9823~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>关于关于<a href="https://juejin.cn/column/6991252706941730852" target="_blank" title="https://juejin.cn/column/6991252706941730852">【SSD系列】</a>：<br>
<strong>前端一些有意思的内容，旨在3-10分钟里， 500-1500字，有所获，又不为所累。</strong></p>
<p>如题，今天我们用<strong>纯web技术，实现摄像头+麦克风 视频的录制功能</strong>，代码约100余行，
主要涉及的知识点：</p>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDevices" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices" ref="nofollow noopener noreferrer">MediaDevices</a><br>
提供对连接的媒体输入设备（如照相机和麦克风）的访问，以及屏幕共享等。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaRecorder" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder" ref="nofollow noopener noreferrer">MediaRecorder</a><br>
录制音频或者视频。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FGlossary%2FIndexedDB" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Glossary/IndexedDB" ref="nofollow noopener noreferrer">IndexedDB</a><br>
储存较大数据结构的事务性数据库。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FURL" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/URL" ref="nofollow noopener noreferrer">URL</a><br>
用来把视频的Blob数据生成地址，提供给<code>video</code>标签使用。</li>
</ol>
<h2 data-id="heading-1">效果演示</h2>
<h3 data-id="heading-2">真机效果</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0186363530cb415b926106e2e54f9823~tplv-k3u1fbpfcp-watermark.image" alt="品目录制，gif.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">PC端 + 模拟移动 + 虚拟摄像头(VCam)</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9dca622ad0e4d7b9c433d9e5acdf724~tplv-k3u1fbpfcp-watermark.image" alt="录制.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">源码地址</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiangwenhu%2FjuejinBlogsCodes%2Ftree%2Fmaster%2FrecordAV" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiangwenhu/juejinBlogsCodes/tree/master/recordAV" ref="nofollow noopener noreferrer">本文源码-recordAV</a></p>
<p>注意：</p>
<ol>
<li>权限问题，需要显式的授权</li>
<li>如果手机端预览，需要启用https，demo已经附带证书</li>
</ol>
<h2 data-id="heading-5">思路</h2>
<ol>
<li>利用MediaDevices唤起摄像头和麦克风</li>
<li>把第一步获取的流，同时用于<code>video</code>和 <code>MediaRecorder</code><br>
因为录制的同时需要看到我们摄像头的内容</li>
<li>录制结束后，把录制视频存入indexedDB</li>
<li>按照keys列出已录制的视频，点击后，获取Blob文件，生成url，提供给video标签播放。</li>
</ol>
<h2 data-id="heading-6">实现</h2>
<h3 data-id="heading-7">唤起摄像头和麦克风并获得其流</h3>
<p>这里需要用的就是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDevices" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices" ref="nofollow noopener noreferrer">MediaDevices</a>，对应的API就是<code>navigator.mediaDevices.getUserMedia</code></p>
<p>核心代码如下:</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-keyword">const</span> stream = <span class="hljs-keyword">await</span> navigator.mediaDevices.getUserMedia(&#123;
    <span class="hljs-attr">video</span>: &#123; <span class="hljs-attr">facingMode</span>: <span class="hljs-string">"environment"</span> &#125;,  <span class="hljs-comment">// 唤起内面的摄像头，</span>
    <span class="hljs-attr">audio</span>: <span class="hljs-literal">true</span>  <span class="hljs-comment">// 需要音频，例如麦克风</span>
&#125;)
<span class="hljs-comment">// 把流传给video元素，即可看到摄像头内容</span>
videoEL.srcObject = stream;  
<span class="hljs-comment">// 初始化 MediaRecorder</span>
mediaRecorder = <span class="hljs-keyword">new</span> MediaRecorder(stream, &#123; <span class="hljs-attr">mimeType</span>: <span class="hljs-string">"video/webm"</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意事项：</p>
<ol>
<li>getUserMedia方法的facingMode参数<br>
<code>user</code>为前置的摄像头，<code>environment</code>为后置摄像头。</li>
<li>new MediaRecorder的参数<code>&#123; mimeType: "video/webm" &#125;</code><br>
如果未设置正确，可能就只有视频，没有麦克风声音了</li>
</ol>
<h3 data-id="heading-8">录制和保存</h3>
<p>录制必然有开始和停止两个操作，实现方式很多，我们就采用最简单的两个按钮形式, 并分别给注册上相关的事件处理程序。</p>
<p>代码如下：<br>
这里有一个小的知识点，<strong>任何有id属性的节点，你均可使用id属性对应的变量直接访问该元素。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btnRecord"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span>></span>录制<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btnStop"</span>  <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span> ></span>停止<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

btnRecord.addEventListener("click", () => &#123;
    startRecord(mediaRecorder);
    mediaRecorder.start();
&#125;);

btnStop.addEventListener("click", () => &#123;
    mediaRecorder.stop();
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是很简单。 注意上面停止按钮点击后，我们调用了<code>mediaRecorder.stop</code>方法，其之后会触发<code>recorder.onstop</code>事件，这个时候，我们唤起弹出框，让用户输入视频的名字，然后将内容保存到indexedDB即可。</p>
<p>indexedDB的存取有很多封装库，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FIndexedDB_API%23%25E5%258F%2582%25E8%25A7%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/IndexedDB_API#%E5%8F%82%E8%A7%81" ref="nofollow noopener noreferrer">indexedDB 参见</a>部分列出了不少于10个库，这里我们采用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fidb-keyval" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/idb-keyval" ref="nofollow noopener noreferrer">idb-keyval</a>库，其简单且小巧的（~600B）基于 Promise 的键值对存储，使用也是极其简单，get, set就行了。</p>
<p>具备上面的知识后，看代码：是不是很简单。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">startRecord</span>(<span class="hljs-params">recorder</span>) </span>&#123;
    <span class="hljs-keyword">var</span> chunks = [];
    <span class="hljs-comment">// 收集数据</span>
    recorder.ondataavailable = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
        chunks.push(e.data);
    &#125;
    <span class="hljs-comment">// 监听停止事件</span>
    recorder.onstop = <span class="hljs-keyword">async</span> () => &#123;
        <span class="hljs-keyword">var</span> clipName = prompt(<span class="hljs-string">'请输入视频的名字'</span>);
        <span class="hljs-keyword">var</span> blob = <span class="hljs-keyword">new</span> Blob(chunks, &#123; <span class="hljs-string">'type'</span>: <span class="hljs-string">'audio/mp4;'</span> &#125;);
        <span class="hljs-keyword">await</span> idbKeyval.set(clipName + <span class="hljs-string">".mp4"</span>, blob);
        listHistory();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">历史和观看</h3>
<p>历史嘛，那就是读取keys，严格意义上，<strong>应该使用indexedDB的游标来读取</strong>，本文为了简单，直接读取所有的keys，然后判断文件后缀来过滤。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">listHistory</span>(<span class="hljs-params"></span>) </span>&#123;
    list.innerHTML = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">const</span> keys = <span class="hljs-keyword">await</span> idbKeyval.keys();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"keys:"</span>, keys);

    keys.filter(<span class="hljs-function"><span class="hljs-params">k</span> =></span> k.endsWith(<span class="hljs-string">".mp4"</span>)).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
        <span class="hljs-keyword">const</span> divEl = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
        divEl.textContent = key;
        divEl.onclick = <span class="hljs-function">() =></span> playVideo(key);

        list.appendChild(divEl);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此为止，我们就差点击某个历史视频之后的播放逻辑了，也很简单：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">playVideo</span>(<span class="hljs-params">key</span>) </span>&#123;
        <span class="hljs-keyword">const</span> blob = <span class="hljs-keyword">await</span> idbKeyval.get(key);
        <span class="hljs-comment">// 生成地址</span>
        fplayer.src = URL.createObjectURL(blob);
        fplayer.style.display = <span class="hljs-string">"block"</span>;
        fplayer.play();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此文本，所有的核心代码都已经实现了。</p>
<h2 data-id="heading-10">小结</h2>
<p>是不是很简单，一切都看起来没那么难，这样，你才容易入坑啊。</p>
<h2 data-id="heading-11">写在最后</h2>
<p>不忘初衷，【SSD系列】，3-5分钟，500-1000字，有所得，而不为所累，如果你觉得不错，你的一赞一评就是我前行的最大动力。</p>
<p>技术交流群请到 <a href="https://juejin.cn/pin/6994350401550024741" title="https://juejin.cn/pin/6994350401550024741" target="_blank">这里来</a>。
或者添加我的微信 cloud-dirge，一起学习。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_43864427%2Farticle%2Fdetails%2F105782611" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_43864427/article/details/105782611" ref="nofollow noopener noreferrer">MediaDevices.getUserMedia()的部分坑和解决方案</a></p>
</blockquote></div>  
</div>
            