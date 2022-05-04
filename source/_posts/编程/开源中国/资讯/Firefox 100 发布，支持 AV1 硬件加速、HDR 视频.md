
---
title: 'Firefox 100 发布，支持 AV1 硬件加速、HDR 视频'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0504/070708_GedR_4937141.png'
author: 开源中国
comments: false
date: Wed, 04 May 2022 07:07:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0504/070708_GedR_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>经过 17 年的发展，Firefox 于今天正式发布第 100 个版本！Firefox 在最近的几个版本中仅仅带来了一些小幅改动，而在 Firefox 100 中，Mozilla 则是一次性带来了众多新特性，让我们来看看这个版本都有什么改动。</p> 
<p><img alt height="367" src="https://static.oschina.net/uploads/space/2022/0504/070708_GedR_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>新特性：</h3> 
<ul> 
 <li>现在在画中画模式下观看 YouTube、Prime Video 和 Netflix 视频时，支持显示字幕。只要打开页面内视频播放器上的字幕，它们就会出现在画中画中。</li> 
 <li>画中画现在还支持使用 WebVTT（Web Video Text Track）格式的网站的视频字幕。</li> 
 <li>在安装后第一次运行 Firefox 时，Firefox 会检测到其语言与操作系统语言不一致的情况，并为用户提供两种语言的选择。</li> 
 <li>Firefox 浏览器的拼写检查现在可以检查多种语言的拼写。要启用其他语言，在文本字段的上下文菜单中选择它们。</li> 
 <li>Mac 上的 Firefox 现在支持 HDR 视频，用户不需要手动修改任何偏好设置来打开 HDR 视频支持，只需确保电池偏好设置没有设置为 "使用电池时优化视频流"。</li> 
 <li>在 Windows 系统以及支持的 GPU 上（Intel Gen 11+、AMD RDNA 2 和 GeForce 30）启用硬件加速的 AV1 视频解码，可能还需要从微软商店安装 AV1 视频扩展。</li> 
 <li>在 Windows 上为英特尔 GPU 启用视频叠加，减少视频播放时的功耗。</li> 
 <li>改进了绘制和处理其他事件之间的公平性，这明显改善了 Twitch 上音量滑块的性能。</li> 
 <li>Linux 和 Windows 11 上的滚动条默认不会占用空间。</li> 
 <li>在英国，Firefox 现在支持信用卡自动填写。</li> 
 <li>Firefox 现在会忽略限制较少的引荐来源网址策略——包括 unsafe-url、no-referrer-when-downgrade 和 origin-when-cross-origin —— 用于跨站点子资源/iframe 请求，以防止引荐来源网址泄露隐私。</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>用户现在可以为网站选择首选的颜色方案。</li> 
 <li>从这个版本开始，Windows 版的 Firefox 安装程序使用 SHA-256 而不是 SHA-1。</li> 
 <li>在 macOS 11+ 中，现在每个窗口只对字体进行一次光栅化。这意味着打开新标签页的速度更快，在同一窗口中切换标签页的速度也更快。</li> 
 <li>深度嵌套的 <code>display: grid</code> 元素的性能得到了极大的改善。</li> 
 <li>增加了对多个 Java 线程的分析支持。</li> 
 <li>软重载一个网页将不再导致所有资源的重新验证。</li> 
 <li>Non-vsync 任务有了更多的运行时间，这改善了 Google docs 和 Twitch 的行为。</li> 
 <li>增加了 Geckoview API，以控制捕获配置文件的开始/停止时间。</li> 
 <li>各种安全问题的修复。</li> 
</ul> 
<h3>变化</h3> 
<ul> 
 <li>Firefox 浏览器有一个新的链接焦点指示器，它用一个实心的蓝色轮廓取代了旧的虚线轮廓。这一变化统一了各表单字段和链接的焦点指示器，使其更容易识别焦点链接。</li> 
 <li>新用户现在可以在将 Firefox 设置为默认浏览器时将 Firefox 设置为默认的 PDF 处理程序。</li> 
 <li>由于 Firefox 新的三位数版本，一些网站可能无法在 Firefox 100 版本中正常工作。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mozilla.org%2Fen-US%2Ffirefox%2F100.0%2Freleasenotes%2F" target="_blank">https://www.mozilla.org/en-US/firefox/100.0/releasenotes/</a></p>
                                        </div>
                                      
</div>
            