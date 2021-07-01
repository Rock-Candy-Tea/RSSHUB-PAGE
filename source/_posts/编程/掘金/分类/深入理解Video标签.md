
---
title: '深入理解Video标签'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4813'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 01:05:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=4813'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Video相关属性</h2>
<h3 data-id="heading-1">1、自动播放</h3>
<p>目前主流浏览器加强了对自动播放策略（Autoplay）的限制：<strong>浏览器在没有交互操作之前不允许有声音的媒体文件自动播放。</strong> 而且各个浏览器关于自动播放策略有不同的实现。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;<span class="hljs-comment">/* 自动播放 */</span>&#125;
<video ref=&#123; videoRef &#125; controls autoPlay />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了解决自动播放失败，在这里介绍两种方法解决 Autoplay 限制的方案</p>
<ul>
<li>播放失败时绕过 Autoplay 限制</li>
<li>直接绕过 Autoplay 限制</li>
</ul>
<h4 data-id="heading-2">1.1 播放失败时绕过 Autoplay 限制</h4>
<p>在实际使用中，页面并不是完全被 Autoplay 限制，随着用户使用这个页面的次数增加，浏览器会将这个页面加入自己的 Autoplay 白名单列表中。</p>
<p>根据这个原理，可在检测到播放失败时，引导用户点击页面上的某个位置来恢复播放。(Google浏览器下测试均播放失败)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 可播放监听。当浏览器能够开始播放指定的音频/视频时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'canplay'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'视频可以播放了'</span>)
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// this.videoRef.paused 判断是否暂停，用来判断是视频是否在播放中，如果没有播放就</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.videoRef.paused) 
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'视频是否在暂停中'</span>, <span class="hljs-built_in">this</span>.videoRef.paused) 
        <span class="hljs-built_in">this</span>.isPlay = !<span class="hljs-built_in">this</span>.videoRef.paused
    &#125;, <span class="hljs-number">500</span>)
&#125;)

<span class="hljs-comment">// 通过promise来判断是否在播放</span>
<span class="hljs-keyword">const</span> videoPromise = <span class="hljs-built_in">this</span>.videoRef.play()
<span class="hljs-keyword">if</span>(!!videoPromise) &#123;
    videoPromise.then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.isPlay = <span class="hljs-literal">true</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'播放成功'</span>)
    &#125;).catch(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.isPlay = <span class="hljs-literal">false</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'播放失败'</span>)
    &#125;)
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 此时可以通过canplay 监听是否在播放</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">1.2 直接绕过 Autoplay 限制</h4>
<p>可以通过如下两种方案实现直接绕过 Autoplay 限制</p>
<ul>
<li>在video标签中关闭静音muted属性设置为true。媒体不包含声音时不会被 Autoplay 限制。(引导用户开启声音)</li>
<li>UI上引导用户触发播放</li>
</ul>
<p>注意：<strong>无论使用哪种方案，在自动播放策略的限制下，没有用户操作之前都不可能自动播放有声媒体。虽然浏览器会在本地维护一个白名单来决定对哪些网站解除自动播放限制，但该白名单无法通过 Javascript 探测到。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 移动端</span>
<span class="hljs-built_in">document</span>.body.addEventListener(<span class="hljs-string">'touchstart'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'触发播放'</span>)
    <span class="hljs-built_in">this</span>.videoRef.play();
&#125;)
<span class="hljs-comment">// PC端</span>
<span class="hljs-built_in">document</span>.body.addEventListener(<span class="hljs-string">'mousedown'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'触发播放'</span>)
    <span class="hljs-built_in">this</span>.videoRef.play();
&#125;)
<span class="hljs-comment">// 微信端IOS手机下触发自动播放，大部分IOS能正常自动播放（安卓机只能通过touchstart触发播放）</span>
<span class="hljs-built_in">document</span>.body.addEventListener(<span class="hljs-string">'WeixinJSBridgeReady'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'触发播放'</span>)
    <span class="hljs-built_in">this</span>.videoRef.play();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意： <strong>Safari 只允许通过用户交互来触发有声媒体的播放，而不是在用户交互后就打开 Autoplay 限制。</strong></p>
<h3 data-id="heading-4">2、播放时间属性控制</h3>
<p>首先我们来看一段代码，在Google端能够正常播放，但是在移动端和Safari中还是重头开始播放。使用了canplay 和loadedmetadata，oncanplay事件来判断视频状态再设置currentTime，但移动端还是无效。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> videoPromise = <span class="hljs-built_in">this</span>.videoRef.play()
<span class="hljs-built_in">this</span>.videoRef.currentTime =  <span class="hljs-number">10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方案：</p>
<ul>
<li>设置视频的Timeupdate事件监听设置播放时间</li>
<li>使用定时器设置播放时间</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.videoRef.play();   
<span class="hljs-comment">// 通过时间更新播放时间</span>
<span class="hljs-keyword">let</span> timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 这里还是有一定的缺陷，如果用户触发了视频播放，但是加载比较长就会有问题</span>
    <span class="hljs-built_in">this</span>.videoRef.currentTime = 需要设置的时间;
    <span class="hljs-built_in">clearTimeout</span>(timer);
&#125;,<span class="hljs-number">200</span>);

<span class="hljs-comment">// timeupdate：目前的播放位置已更改时，播放时间更新</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'timeupdate'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'timeupdate'</span>)
    <span class="hljs-keyword">let</span> timeDisplay = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">this</span>.videoRef.currentTime);
    <span class="hljs-keyword">if</span>(timeDisplay > <span class="hljs-number">0</span>)&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.firstOpen)&#123;
            <span class="hljs-built_in">this</span>.videoRef.currentTime = <span class="hljs-number">10</span>;
            <span class="hljs-built_in">this</span>.firstOpen = <span class="hljs-literal">false</span>;
        &#125;
    &#125;
&#125;)

<span class="hljs-comment">// seeking：查找开始。当用户开始移动/跳跃到音频/视频中新的位置时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'seeking'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-comment">// 在这里处理视频播放是否播到放指定的时间</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开始移动进度条'</span>, <span class="hljs-built_in">this</span>.videoRef.currentTime)
&#125;)

<span class="hljs-comment">// seeked：查找结束。当用户已经移动/跳跃到视频中新的位置时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'seeked'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span>  &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'进度条已经移动到了新的位置'</span>, <span class="hljs-built_in">this</span>.videoRef.currentTime)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">其他属性介绍：</h3>
<p>this.videoRef.error; //null:正常</p>
<p>this.videoRef.error.code; //1.用户终止 2.网络错误 3.解码错误 4.URL无效</p>
<p>this.videoRef.networkState; //0.此元素未初始化 1.正常但没有使用网络 2.正在下载数据 3.没有找到资源</p>
<p>this.videoRef.buffered; //返回已缓冲区域，TimeRanges</p>
<p>this.videoRef.paused; //是否暂停</p>
<p>this.videoRef.defaultPlaybackRate = value;//默认的回放速度，可以设置</p>
<p>this.videoRef.playbackRate = value;//当前播放速度，设置后马上改变</p>
<p>this.videoRef.played; //返回已经播放的区域，TimeRanges，</p>
<p>this.videoRef.seekable; //返回可以seek的区域 TimeRanges</p>
<p>this.videoRef.ended; //是否结束</p>
<h2 data-id="heading-6">Video相关事件</h2>
<p>了解Video 标签相关事件触发时机，才能处理好业务相关逻辑。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loadstart 视频查找。当浏览器开始寻找指定的音频/视频时触发，也就是当加载过程开始时</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'loadstart'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'提示视频的元数据已加载'</span>)
    <span class="hljs-comment">// console.log(e)</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.videoRef.duration)            <span class="hljs-comment">// NaN</span>
&#125;)

<span class="hljs-comment">// durationchange 时长变化。当指定的音频/视频的时长数据发生变化时触发，加载后，时长由 NaN 变为音频/视频的实际时长</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'durationchange'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'提示视频的时长已改变'</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.videoRef.duration)           <span class="hljs-comment">// 视频的实际时长（单位：秒）</span>
&#125;)

<span class="hljs-comment">// loadedmetadata ：元数据加载。当指定的音频/视频的元数据已加载时触发，元数据包括：时长、尺寸（仅视频）以及文本轨道</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'loadedmetadata'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'提示视频的元数据已加载'</span>)
    <span class="hljs-comment">// console.log(e)</span>
&#125;)

<span class="hljs-comment">// loadeddata：视频下载监听。当当前帧的数据已加载，但没有足够的数据来播放指定音频/视频的下一帧时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'loadeddata'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'提示当前帧的数据是可用的'</span>)
&#125;)

<span class="hljs-comment">// progress：浏览器下载监听。当浏览器正在下载指定的音频/视频时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'progress'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'提示视频正在下载中'</span>)
&#125;)

<span class="hljs-comment">// canplay：可播放监听。当浏览器能够开始播放指定的音频/视频时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'canplay'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'视频可以播放了'</span>)
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// this.videoRef.paused 判断是否暂停</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'视频是否在暂停中'</span>, <span class="hljs-built_in">this</span>.videoRef.paused) 
        <span class="hljs-built_in">this</span>.isPlay = !<span class="hljs-built_in">this</span>.videoRef.paused
    &#125;, <span class="hljs-number">1000</span>)
&#125;)

<span class="hljs-comment">// canplaythrough：可流畅播放。当浏览器预计能够在不停下来进行缓冲的情况下持续播放指定的音频/视频时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'canplaythrough'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'提示视频能够不停顿地一直播放'</span>)
    <span class="hljs-built_in">console</span>.log(e)
&#125;)

<span class="hljs-comment">// play: 播放监听</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'play'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'提示该视频正在播放中'</span>)
&#125;)

<span class="hljs-comment">// pause：暂停监听</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'pause'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'暂停播放'</span>)
&#125;)

<span class="hljs-comment">// seeking：查找开始。当用户开始移动/跳跃到音频/视频中新的位置时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'seeking'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-comment">// 在这里处理到底有没有更新到最新的位置</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开始移动进度条'</span>, <span class="hljs-built_in">this</span>.videoRef.currentTime)
&#125;)

<span class="hljs-comment">// seeked：查找结束。当用户已经移动/跳跃到视频中新的位置时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'seeked'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span>  &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'进度条已经移动到了新的位置'</span>, <span class="hljs-built_in">this</span>.videoRef.currentTime)
&#125;)

<span class="hljs-comment">// waiting：视频加载等待。当视频由于需要缓冲下一帧而停止，等待时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'waiting'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'视频加载等待'</span>)
    <span class="hljs-built_in">console</span>.log(e)
&#125;)

<span class="hljs-comment">// playing：当视频在已因缓冲而暂停或停止后已就绪时触发</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'playing'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'playing'</span>)
    <span class="hljs-built_in">console</span>.log(e)
&#125;)

<span class="hljs-comment">// timeupdate：目前的播放位置已更改时，播放时间更新</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'timeupdate'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-comment">// console.log('timeupdate')</span>
    <span class="hljs-comment">// let timeDisplay = Math.floor(this.videoRef.currentTime);</span>
    <span class="hljs-comment">// if(timeDisplay > 0)&#123;</span>
    <span class="hljs-comment">//     if(this.firstOpen)&#123;</span>
    <span class="hljs-comment">//         this.videoRef.currentTime = 10;</span>
    <span class="hljs-comment">//         this.firstOpen = false;</span>
    <span class="hljs-comment">//     &#125;</span>
    <span class="hljs-comment">// &#125;</span>
&#125;)

<span class="hljs-comment">// ended：播放结束</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'ended'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'视频播放完了'</span>)
    <span class="hljs-built_in">console</span>.log(e)
&#125;)

<span class="hljs-comment">// error：播放错误</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'error'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'视频出错了'</span>)
    <span class="hljs-built_in">console</span>.log(e)
&#125;)

<span class="hljs-comment">// volumechange：当音量更改时</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'volumechange'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'volumechange'</span>)
    <span class="hljs-built_in">console</span>.log(e)
&#125;)

<span class="hljs-comment">// stalled：当浏览器尝试获取媒体数据，但数据不可用时</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'stalled'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'stalled'</span>)
    <span class="hljs-built_in">console</span>.log(e)
&#125;)

<span class="hljs-comment">// ratechange：当视频的播放速度已更改时</span>
<span class="hljs-built_in">this</span>.videoRef.addEventListener(<span class="hljs-string">'ratechange'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ratechange'</span>)
    <span class="hljs-built_in">console</span>.log(e)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于微信H5视频兼容介绍：
<a href="https://juejin.cn/post/6961683577658408996" target="_blank">移动端兼容</a></p>
<h2 data-id="heading-7">最后</h2>
<p>移动端Web对于Video自动播放的兼容性是在太差，尤其安卓。各种问题，各种兼容，各种心累。</p>
<p>本文到此结束。希望对你有帮助。</p>
<p>小编第一次写文章文笔有限、才疏学浅，文中如有不正之处，万望告知。</p></div>  
</div>
            