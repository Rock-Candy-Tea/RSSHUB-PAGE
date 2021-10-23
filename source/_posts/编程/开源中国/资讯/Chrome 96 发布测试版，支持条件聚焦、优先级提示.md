
---
title: 'Chrome 96 发布测试版，支持条件聚焦、优先级提示'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9340'
author: 开源中国
comments: false
date: Sat, 23 Oct 2021 08:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9340'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px"><span style="color:rgba(0,0,0,0.87)">2021 年 10 月 21 日，Chrome 96 推出了测试版，此版本适用于 Android、Chrome OS、Linux、macOS 和 Windows 的最新 Chrome 测试版本。 </span></p> 
<h2 style="margin-left:0px"><span style="color:rgba(0,0,0,0.87)">主要更新</span><span style="color:rgba(0,0,0,0.87)">内容：</span></h2> 
<h3 style="margin-left:0px">三位数的版本号</h3> 
<p>Chrome 100 预计在明年发布，到时候用户代理字符串中报告的版本号会从两位数变成三位数。所以 Chrome 96 引入了一个 runtime flag 在用户代理字符串中返回 “100” ，方便开发者测试新字符串。</p> 
<p>新的标记是<code>chrome://flags/#force-major-version-to-100</code>。</p> 
<h3 style="margin-left:0px">起源试炼</h3> 
<ul> 
 <li> <h4 style="margin-left:0px">条件聚焦</h4> </li> 
</ul> 
<p style="margin-left:0px"><span style="color:rgba(0,0,0,0.87)">捕获其他窗口或选项卡的应用程序，没有办法控制是调用项还是捕获项获得焦点。（比如视频会议里面的演示功能。）</span></p> 
<p style="margin-left:0px"><span style="color:rgba(0,0,0,0.87)">Chrome 96 通过 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrack" target="_blank">MediaStreamTrack</a> 的一个子类：<span style="color:#006600"><code>FocusableMediaStreamTrack</code></span> 实现了这个功能，<span style="color:#2e3033">它支持一个新的<code>focus() </code>方法，看这个代码：</span></p> 
<pre style="text-align:start">stream = await navigator.mediaDevices.getDisplayMedia();
let [track] = stream.getVideoTracks();
</pre> 
<p>以前，<code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStream%2FgetVideoTracks" target="_blank">getVideoTracks()</a></code>会返回一个<code>MediaStreamTrack</code>对象数组，现在它返回<code>FocusableMediaStreamTrack</code>对象（<span style="color:rgba(0, 0, 0, 0.87)">Chrome 97 可能会改为</span><code>BrowserCaptureMediaStreamTrack</code><span style="color:rgba(0, 0, 0, 0.87)"><span> </span></span>）。</p> 
<p>为了确定哪个显示媒体获得焦点，这个代码的下一行将调用<code>track.focus()</code><code>"focus-captured-surface"</code>来聚焦新捕获的窗口或选项卡，或者用<code>"no-focus-change"</code>调用窗口来保持焦点。在 Chrome 96 或更高的版本上，可以逐步执行<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feladalon1983.github.io%2Fconditional-focus%2Fdemo%2F" target="_blank">演示代码</a>查看它的效果。</p> 
<ul> 
 <li> <h4 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span><span><span><span>优先级提示</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> </li> 
</ul> 
<p>引入了一个 developer-set ：<code>"importance"</code>属性来影响资源的计算优先级，它支持这三个值：<code>"auto"</code>、<code>"low"</code>、和<code>"high"</code></p> 
<p>优先级提示会指出各种资源对浏览器的相对重要性，允许对资源的加载顺序进行更多控制。很多因素都会影响浏览器中资源的优先级，包括资源的类型、可见性和预加载状态。</p> 
<p>其他功能更新，请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.chromium.org%2F2021%2F10%2Fchrome-96-beta-conditional-focus.html" target="_blank">点此查看</a>。</p>
                                        </div>
                                      
</div>
            