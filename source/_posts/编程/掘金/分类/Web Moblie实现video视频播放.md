
---
title: 'Web Moblie实现video视频播放'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=646'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 19:00:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=646'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">设置meta标签</h2>
<pre><code class="copyable"><!--添加viewport标签-->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" />
<!--禁止将数字变为电话号码-->
<meta name="format-detection" content="telephone=no" />
<!--ios设备的safari的私有meta标签-->
<meta name="apple-mobile-web-app-capable" content="yes" />
<!--ios的私有标签-->
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">设置body、html的font-size</h2>
<ul>
<li>通过js设置</li>
</ul>
<pre><code class="copyable">(function(doc, win) &#123;
var docEl = doc.documentElement,
resizeEvt = 'orientationchange' in window ? 'orientationchange' : 'resize',
recalc = function() &#123;
var clientWidth = docEl.clientWidth;
if(!clientWidth) return;
docEl.style.fontSize = 20 * (clientWidth / 320) + 'px';
&#125;;
if(!doc.addEventListener) return;
win.addEventListener(resizeEvt, recalc, false);
doc.addEventListener('DOMContentLoaded', recalc, false)
&#125;)(document, window);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过scss、less等设置</li>
</ul>
<p>$num 为实际的px值</p>
<pre><code class="copyable">@function rem($num)&#123;
  @return unquote(($num/100) + 'rem');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置之后使用rem作为单位来适配手机屏幕</p>
<h2 data-id="heading-2">video.js的使用</h2>
<ol>
<li>引入js，css文件,也可以直接下载到本地再引入</li>
</ol>
<pre><code class="copyable"><link href="http://vjs.zencdn.net/4.12/video-js.css" rel="stylesheet">
<script src="http://vjs.zencdn.net/4.12/video.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用video标签</li>
</ol>
<pre><code class="copyable"><video id="example_video_1" class="video-js vjs-default-skin" controls
 preload="auto" width="640" height="264" poster="really-cool-video-poster.jpg"
 data-setup='&#123;&#125;'>
  <source src="really-cool-video.mp4" type='video/mp4'>
  <source src="really-cool-video.webm" type='video/webm'>
  <p class="vjs-no-js">
    To view this video please enable JavaScript, and consider upgrading to a web browser
    that <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
  </p>
</video>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以通过js改变值：</p>
<pre><code class="copyable">var myPlayer = videojs('example_video_1');
videojs("example_video_1").ready(function()&#123;
  var myPlayer = this;
  // EXAMPLE: Start playing the video.
  myPlayer.play();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">VideoJs API方法：</h2>
<ol>
<li>获取对象</li>
</ol>
<pre><code class="copyable">var videoObj = videojs(“videoId”);
ready:
myPlayer.ready(function()&#123;
    //在回调函数中，this代表当前播放器，
    //可以调用方法，也可以绑定事件。
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>播放:<code>myPlayer.play();</code></li>
<li>暂停:<code>myPlayer.pause();</code></li>
<li>获取播放进度:<code>var whereYouAt = myPlayer.currentTime();</code></li>
<li>设置播放进度:<code>myPlayer.currentTime(120);</code></li>
<li>视频持续时间，加载完成视频才可以知道视频时长，且在flash情况下无效:<code>var howLongIsThis = myPlayer.duration();</code></li>
<li>缓冲，就是返回下载了多少:<code>var whatHasBeenBuffered = myPlayer.buffered();</code></li>
<li>百分比的缓冲:<code>var howMuchIsDownloaded = myPlayer.bufferedPercent();</code></li>
<li>声音大小（0-1之间）:<code>var howLoudIsIt = myPlayer.volume();</code></li>
<li>设置声音大小:<code>myPlayer.volume(0.5);</code></li>
<li>取得视频的宽度:<code>var howWideIsIt = myPlayer.width();</code></li>
<li>设置宽度:<code>myPlayer.width(640);</code></li>
<li>获取高度:<code>var howTallIsIt = myPlayer.height();</code></li>
<li>设置高度:<code>myPlayer.height(480);</code></li>
<li>一步到位的设置大小:<code>myPlayer.size(640,480);</code></li>
<li>全屏:<code>myPlayer.enterFullScreen();</code></li>
<li>离开全屏:<code>myPlayer.enterFullScreen();</code></li>
<li>添加事件:</li>
</ol>
<pre><code class="copyable">durationchange
ended //播放结束
firstplay
fullscreenchange
loadedalldata
loadeddata
loadedmetadata
loadstart
pause //暂停
play //播放
progress
seeked
seeking
timeupdate
volumechange
waiting
resize inherited
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">var myFunc = function()&#123;
// Do something when the event is fired
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="18">
<li>事件绑定</li>
</ol>
<pre><code class="copyable">myPlayer.on("ended", function()&#123;
    console.log("end", this.currentTime());
&#125;);
myPlayer.on("pause", function()&#123;
    console.log("pause")
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="19">
<li>删除事件</li>
</ol>
<p><code>myPlayer.removeEvent(“eventName”, myFunc);</code></p>
<h2 data-id="heading-4">我遇到的坑：</h2>
<ul>
<li>video标签支持的视频的格式需要与规定的一致。<br>
参考：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.w3school.com.cn%2Fhtml5%2Fhtml_5_video.asp" target="_blank" rel="nofollow noopener noreferrer" title="http://www.w3school.com.cn/html5/html_5_video.asp" ref="nofollow noopener noreferrer">www.w3school.com.cn/html5/html_…</a><br>
Ogg = 带有 Theora 视频编码和 Vorbis 音频编码的 Ogg 文件<br>
MPEG4 = 带有 H.264 视频编码和 AAC 音频编码的 MPEG 4 文件<br>
WebM = 带有 VP8 视频编码和 Vorbis 音频编码的 WebM 文件</li>
<li>ios版本播放的问题<br>
因为我是用Hbuiler测试手机的，设置了内置服务器之后，一直用ios手机访问都不成功，视频无法播放，找了无数种方法，结果是错在了服务器支持的MIME类型里。也就是我换成xampp作为服务器去访问时成功的！！！</li>
</ul></div>  
</div>
            