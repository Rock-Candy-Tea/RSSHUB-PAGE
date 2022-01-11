
---
title: 'Chrome 98 Beta 发布：颜色渐变矢量字体、实验性的区域捕获等新特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0111/073900_Wr5t_5430600.png'
author: 开源中国
comments: false
date: Tue, 11 Jan 2022 08:05:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0111/073900_Wr5t_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px"><span style="color:rgba(0,0,0,0.87)">2022 年 1 月 10 日起，Chrome 98 转为 Beta 版，此版本带来一些有趣的功能，比如</span>颜色渐变的矢量字体  COLRv1 ，以及 Origin 版本试验性的视频区域捕获功能。</p> 
<h2 style="margin-left:0px">COLRv1 颜色渐变矢量字体</h2> 
<p style="margin-left:0px">这个版本中，Chrome 支持 COLRv1 颜色渐变矢量字体作为额外的新字体格式。COLRv1 是彩色字体，包含具有多种颜色的字形，可用于表情符号或国旗或多色字母等场景。</p> 
<p>COLRv1 是 COLRv0 字体格式的演变，旨在使彩色字体在网络上广泛传播。COLRv1 字体以非常小的字体大小带来了富有表现力的视觉功能，例如渐变、变换和组合。COLRv1 字体也支持 OpenType 变体。</p> 
<p>在性能方面，内部形状重用和紧凑的字体格式定义，加上有效的压缩，导致 COLRv1 的字体大小非常小。该图显示了 Noto Color Emoji 的示例，它作为位图字体大约 9MB，但作为 COLRv1 矢量字体只有 1.85MB（经过 WOFF2 压缩后）。</p> 
<p><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0111/073900_Wr5t_5430600.png" width="350" referrerpolicy="no-referrer"></p> 
<p><span style="color:#7f8c8d"><em>位图字体（右），Crisp COLRv1 矢量字体（左）</em></span></p> 
<h2>Origin 试用（Origin Trials）</h2> 
<p><span style="color:rgba(0, 0, 0, 0.87)">此版本的 Chrome 引入了 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.chrome.com%2Forigintrials%2F%23%2Ftrials%2Factive" target="_blank">Origin 试用功能</a>，开发者可以尝试新功能，并向 Web 社区提供有关新功能的可用性、实用性和有效性的反馈。</p> 
<p><strong>新的起源试用：区域捕获功能（Region Capture）</strong></p> 
<p>Region Capture 是一个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5712447794053120" target="_blank">用于裁剪自捕获视频轨道</a>的 API，目前应用程序可以使用 getDisplayMedia() 获取它们在其中运行的选项卡的捕获，无论是否使用 preferCurrentTab 。使用 Region Capture 可以裁剪<span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.87)">生成的视频轨道，以便从中删除一些内容。</span></p> 
<p><span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.87)">这个功能最典型的场景就是共享屏幕，或者视频会议的时候，只展示屏幕的某一部分。</span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">其他功能</h2> 
<ul> 
 <li><strong>为 contains-intrinsic-size 添加自动关键字</strong></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F6740477866934272" target="_blank"><code>contain-intrinsic-size</code></a>的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F6740477866934272" target="_blank">自动关键字</a><span style="color:rgba(0, 0, 0, 0.87)">让网站可以使用元素的最后记忆大小，</span> 如果没有这个功能，Web 开发人员必须猜测元素的渲染大小。</p> 
<ul> 
 <li><strong>AudioContext.outputLatency 属性</strong></li> 
</ul> 
<p>新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5682265146261504" target="_blank"><code>AudioContext.outputLatency</code>属性</a>是以秒为单位的音频输出延迟估计值。从技术上讲，这是用户代理请求主机系统缓冲的时间与音频输出设备处理缓冲区中的第一个样本的时间之间的时间间隔。（<span style="color:rgba(0, 0, 0, 0.87)">Firefox 中已实现</span>）。</p> 
<ul> 
 <li><strong>CSS Color Adjust: 'only' 颜色方案的关键字</strong></li> 
</ul> 
<p><code>only</code>关键字，已重新加入到 <code>color-scheme</code>规范，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5157621012103168" target="_blank">目前支持Chrome浏览器</a>。它允许为单个特定元素选择退出配色方案。例如允许覆盖强制变暗。比如:</p> 
<p><span style="background-color:#fafafa; color:#006600">div &#123; color-scheme: light &#125;</span>  会强制 div 元素脱离颜色方案黑暗。<br> <span style="background-color:#fafafa; color:#006600">div &#123; color-scheme: only light &#125;</span> 使 color-scheme 元素保持光亮，并使其不被用户代理（user agent）强制变暗。</p> 
<h2>弃用和删除</h2> 
<ul> 
 <li><strong>删除 WebRTC 的 SDES 密钥交换</strong></li> 
</ul> 
<p>自 2013 年以来，WebRTC 的 SDES 密钥交换机制已被宣布为不得在相关 IETF 标准中使用。它在 Chrome 中的使用量在过去一年中显着下降。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeatures%2F5695324321480704" target="_blank">SDES 被删除，</a>因为它是一个安全问题。它将会话密钥暴露给 Javascript，这意味着有权访问协商交换，或能够破坏 Javascript 的实体可以解密通过连接发送的媒体。</p> 
<p>关于新特性更完整的介绍，可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.chromium.org%2F2022%2F01%2Fchrome-98-beta-color-gradient-vector.html" target="_blank">官方博客</a>中查看。</p>
                                        </div>
                                      
</div>
            