
---
title: 'Audio 标签属性含义及其用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36d45acc1b884c109182043007e13dda~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 22:45:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36d45acc1b884c109182043007e13dda~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTML%2FElement%2Faudio" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/audio" ref="nofollow noopener noreferrer">audio</a> 用于在文档中嵌入音频元素。</p>
<p>  <code>audio</code>元素是<code>HTML5</code>新增的行内标签，<code>IE8</code>及以下浏览器不支持<code>audio</code>标签。</p>
<p>  若浏览器不支持<code>video</code>元素或者无法播放音频，则会显示替代文本（开始和结束标签之间的内容）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><audio src=<span class="hljs-string">"music.mp3"</span> >当前浏览器不支持audio标签</audio>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">标签属性</h2>
<ul>
<li><code>autoplay</code>：音频会尽快自动播放，不会等待整个音频下载完成</li>
<li><code>controls</code>：浏览器提供包括声音、播放进度、播放暂停的控制面板（不同浏览器不一致），用户可以控制音频播放</li>
<li><code>loop</code>：循环播放音频</li>
<li><code>muted</code>：是否静音，默认值为<code>false</code>，表示有声音</li>
<li><code>preload</code>：预加载，包括<code>auto</code>、<code>metadata</code>和<code>none</code>三个参数值，<code>auto</code>表示加载音频，<code>metadata</code>表示不加载音频，但是需要获取音频元数据（如音频长度），<code>none</code>表示不加载音频。若指定为空字符串，则等效于<code>auto</code>。注意<code>autoplay</code>属性优先级高于<code>preload</code>，若<code>autoplay</code>被指定，则会忽略此属性，浏览器将加载音频以供播放</li>
<li><code>src</code>：嵌入的音频<code>URL</code></li>
</ul>
<h2 data-id="heading-1">设置多个音频资源</h2>
<p>  不同浏览器支持的音频播放格式有所不同，一般为了兼容效果，会放置多种音频格式，浏览器会自上而下选择符合的音频格式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><audio controls>
    <source src="music.ogg" type="audio/ogg">
    <source src="music.mp3" type="audio/mpeg">
    <source src="music.wav" type="audio/Wav">
    当前浏览器不支持audio标签
</audio>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">元素属性</h2>
<h3 data-id="heading-3">只读</h3>
<ul>
<li><code>duration</code>：双进度浮点数，音频的播放时长，以秒为单位。若音频不可用或者音频未加载，则返回<code>NaN</code></li>
<li><code>paused</code>：若音频被暂停或者未开始播放，则返回<code>true</code></li>
<li><code>ended</code>：音频是否播放完毕，播放完毕则返回<code>true</code></li>
<li><code>error</code>：发生错误情况下的<code>MediaError</code>对象</li>
<li><code>currentSrc</code>：返回正在播放或加载的音频的<code>URL</code>地址，对应于浏览器在<code>source</code>元素中选择的文件</li>
<li><code>seeking</code>：用户是否在音频中移动或者跳跃到新的播放点</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><audio preload=<span class="hljs-string">"auto"</span> src=<span class="hljs-string">"music.mp3"</span> onseeking=<span class="hljs-string">"fn()"</span> controls />
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> audio = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'audio'</span>)
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(audio.seeking)
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">可读写</h3>
<ul>
<li><code>autoplay</code>：设置音频自动播放，或者查询音频是否设置<code>autoplay</code></li>
<li><code>loop</code>：设置或者查询音频是否循环播放</li>
<li><code>currentTime</code>：返回音频当前的播放时间点，双精度浮点数，单位为秒。音频未播放，可用于设置音频开始播放的时间点。音频播放过程中，可用于设置音频播放时间点</li>
<li><code>controls</code>：显示或隐藏音频控制面板，或者查询控制面板是否可见</li>
<li><code>volume</code>：返回音量值，介于<code>0-1</code>之间的双进度浮点数，或者设置音量值</li>
<li><code>muted</code>：设置或者查询是否静音</li>
<li><code>playbackRate</code>：设置或者查询音频的播放速度，<code>1</code>表示正常速度，大于<code>1</code>表示快进，<code>0-1</code>之间表示慢进，<code>0 </code>表示暂停（控制面板仍然是播放，仅仅是速度为<code>0</code>）</li>
</ul>
<h3 data-id="heading-5">特殊属性</h3>
<h4 data-id="heading-6">played</h4>
<p>  表示用户已经播放的音频范围，返回 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FTimeRanges" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/TimeRanges" ref="nofollow noopener noreferrer">TimeRanges</a> 对象，其中<code>TimeRanges</code>对象包括一个<code>length</code>属性和<code>start()</code>、<code>end()</code>两个方法。</p>
<ul>
<li><code>length</code>：获取音频范围的数量，未开始播放为<code>0</code>，开始播放后至少为<code>1</code></li>
<li><code>start(index)</code>：获取某个音频范围的开始位置</li>
<li><code>end(index)</code>：获取某个音频范围的结束位置</li>
</ul>
<p>  若用户在音频中移动或者跳跃播放点，则会获得多个音频范围。</p>
<p>  如下为一段音频，用户跳跃了播放点两次，因此<code>played.length</code>为<code>3</code>，其中三段音频范围分别为开始播放、第一个跳跃点、第二个跳跃点的播放范围。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36d45acc1b884c109182043007e13dda~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  上述部分代码如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><audio src=<span class="hljs-string">"music.mp3"</span> controls></audio>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span>></span>console.log<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> btn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btn'</span>)
    <span class="hljs-keyword">var</span> audio = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'audio'</span>)

    btn.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> length = audio.played.length
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`length: <span class="hljs-subst">$&#123;length&#125;</span>`</span>)

        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
            <span class="hljs-keyword">var</span> start = audio.played.start(i)
            <span class="hljs-keyword">var</span> end = audio.played.end(i)

            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`index: <span class="hljs-subst">$&#123;i&#125;</span>, start: <span class="hljs-subst">$&#123;start&#125;</span>, end: <span class="hljs-subst">$&#123;end&#125;</span>, durations: <span class="hljs-subst">$&#123;end - start&#125;</span>s`</span>)
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">buffered</h4>
<p>  表示浏览器已经缓存的音频范围，返回<code>TimeRanges</code>对象，若音频已完全加载则<code>buffered.length</code>为<code>1</code>，<code>buffered.start(0)</code>为<code>0</code>，<code>buffered.end(0)</code>为音频时长，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fbuffered" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/buffered" ref="nofollow noopener noreferrer">详细参考</a>。</p>
<h4 data-id="heading-8">seekable</h4>
<p>  表示用户可跳转或移动的音频范围，返回<code>TimeRanges</code>对象，若音频已完全加载则<code>seekable.length</code>为<code>1</code>，<code>seekable.start(0)</code>为<code>0</code>，<code>seekable.end(0)</code>为音频时长。音频未加载或者加载错误，则<code>seakable.length</code>为<code>0</code>，对应的<code>start(0)</code>和<code>end(0)</code>也就不存在，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fseekable" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/seekable" ref="nofollow noopener noreferrer">详细参考</a>。</p>
<h4 data-id="heading-9">networkState</h4>
<p>  获取音频的网络范围，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2FnetworkState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/networkState" ref="nofollow noopener noreferrer">详细参考</a>。</p>
<ul>
<li><code>0</code>：<code>NETWORK_EMPTY</code>，音频尚未初始化</li>
<li><code>1</code>：<code>NETWORK_IDLE</code>，浏览器已选择好采用什么编码格式来播放媒体，但尚未建立网络连接</li>
<li><code>2</code>：<code>NETWORK_LOADING</code>，浏览器正在加载</li>
<li><code>3</code>：<code>NETWORK_NO_SOURCE</code>，未找到音频资源</li>
</ul>
<h4 data-id="heading-10">error</h4>
<p>  通常正常加载音频，则返回<code>null</code>，若加载过程中发生错误，浏览器将会返回<code>MediaError</code>对象。<code>MediaError</code>对象包括<code>code</code>和<code>message</code>属性，<code>message</code>为错误描述信息，<code>code</code>为如下错误码。</p>
<ul>
<li><code>1</code>：<code>MEDIA_ERR_ABORTED</code>，音频加载加载过程中由于用户操作而被终止</li>
<li><code>2</code>：<code>MEDIA_ERR_NETWORK</code>，确认音频资源可用，但是加载时出现网路错误，音频加载被终止</li>
<li><code>3</code>：<code>MEDIA_ERR_DECODE</code>，确认音频资源可用，但是解码发生错误</li>
<li><code>4</code>：<code>MEDIA_ERR_SRC_NOT_SUPPORTED</code>，音频格式不被支持或者资源不可用</li>
</ul>
<h2 data-id="heading-11">方法</h2>
<h3 data-id="heading-12">play</h3>
<p>  播放音频，返回<code>Promise</code>，播放成功时为<code>resolved</code>，因为任何原因播放失败为<code>rejected</code>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fplay" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/play" ref="nofollow noopener noreferrer">详细参考</a>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> audio = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'audio'</span>)
audio.play()
    .then(<span class="hljs-function">() =></span> &#123; &#125;)
    .catch(<span class="hljs-function">() =></span> &#123; &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">pause</h3>
<p>  暂停音频，无返回值，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fpause" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/pause" ref="nofollow noopener noreferrer">详细参考</a>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> audio = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'audio'</span>)
audio.pause()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">load</h3>
<p>  重新加载<code>src</code>指定的资源，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fload" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/load" ref="nofollow noopener noreferrer">详细参考</a>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> audio = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'audio'</span>)
audio.src = <span class="hljs-string">'music.mp3'</span>
audio.load()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">事件</h2>
<h3 data-id="heading-16">常用事件</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Floadstart_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/loadstart_event" ref="nofollow noopener noreferrer">loadstart</a>：开始载入音频时触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fdurationchange_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/durationchange_event" ref="nofollow noopener noreferrer">durationchange</a>：<code>duration</code>属性更新时触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Floadedmetadata_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadedmetadata_event" ref="nofollow noopener noreferrer">loadedmetadata</a>：音频元数据加载完成时触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Floadeddata_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/loadeddata_event" ref="nofollow noopener noreferrer">loadeddata</a>：音频的第一帧加载完成时触发，此时整个音频还未加载完</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fprogress_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/progress_event" ref="nofollow noopener noreferrer">progress</a>：音频正在加载时触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fcanplay_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/canplay_event" ref="nofollow noopener noreferrer">canplay</a>：浏览器能够开始播放音频时触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fcanplaythrough_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/canplaythrough_event" ref="nofollow noopener noreferrer">canplaythrough</a>：浏览器预计在不停下来进行缓冲的情况下，能够持续播放指定的音频时会触发</li>
</ul>
<h3 data-id="heading-17">其他事件</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fabort_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/abort_event" ref="nofollow noopener noreferrer">abort</a>：音频终止时触发，非错误导致</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Femptied_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/emptied_event" ref="nofollow noopener noreferrer">emptied</a>：音频加载后又被清空，如加载后又调用 load 重新加载</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fended_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ended_event" ref="nofollow noopener noreferrer">ended</a>：播放结束，若设置<code>loop</code>属性，音频播放结束后不会触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Ferror_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/error_event" ref="nofollow noopener noreferrer">error</a>：发生错误</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fplay_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/play_event" ref="nofollow noopener noreferrer">play</a>：播放事件，第一次播放、暂停后播放会触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fplaying_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/playing_event" ref="nofollow noopener noreferrer">playing</a>：播放事件，第一次播放、暂停后播放、播放结束后循环播放会触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fpause_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/pause_event" ref="nofollow noopener noreferrer">pause</a>：暂停事件</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fratechange_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ratechange_event" ref="nofollow noopener noreferrer">ratechange</a>：播放速率改变</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fratechange_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ratechange_event" ref="nofollow noopener noreferrer">seeking</a>：播放点改变开始</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fratechange_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ratechange_event" ref="nofollow noopener noreferrer">seeked</a>：播放点改变结束</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fstalled_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/stalled_event" ref="nofollow noopener noreferrer">stalled</a>：浏览器尝试获取音频，但是音频不可用时触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fsuspend_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/suspend_event" ref="nofollow noopener noreferrer">suspend</a>：音频加载暂停时触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Ftimeupdate_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/timeupdate_event" ref="nofollow noopener noreferrer">timeupdate</a>：音频 <code>currentTime </code>改变时触发</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fvolumechange_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/volumechange_event" ref="nofollow noopener noreferrer">volumechange</a>：音量改变时触发，包括静音</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%2Fwaiting_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/waiting_event" ref="nofollow noopener noreferrer">waiting</a>：开始播放前缓冲下一帧时触发</li>
</ul></div>  
</div>
            