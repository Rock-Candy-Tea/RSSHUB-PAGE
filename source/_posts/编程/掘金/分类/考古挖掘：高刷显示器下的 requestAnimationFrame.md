
---
title: '考古挖掘：高刷显示器下的 requestAnimationFrame'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbee8811d75b4da38c59bec27646c3bb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 01:33:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbee8811d75b4da38c59bec27646c3bb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">起因</h2>
<p>今天有一位同学，在群里问了这一个问题：<code>requestAnimationFrame</code> 的执行机制如何</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbee8811d75b4da38c59bec27646c3bb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个问题当然不陌生。<code>requestAnimationFrame</code> 在浏览器每一帧开始绘制之前会执行。借助 <code>requestAnimationFrame</code> 高效的执行效率，我们可以使用<code>requestAnimationFrame</code> 进行动画操作、FPS 的计算、甚至可以通过算每一帧所需要的真实时间，来增加帧数。
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/636e3fb0e4d146989352eb8ac2180fa5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Window/requestAnimationFrame" target="_blank" rel="nofollow noopener noreferrer">MDN</a>中，还有这样一句话：<strong>在多数遵循W3C建议的浏览器中，回调函数执行次数通常与浏览器屏幕刷新次数相匹配</strong>。于是yck同学此时问了一句：我屏幕刷新率特别快怎么办？</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0172b21ec91a4c71a3c376e53f6f9fcc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这句话令人深思。在如今高刷显示器盛行的年代，我依然在使用60hz的MacBook。虽然MDN写着匹配，但这个也不一定对。带着这个疑问，我开始了探索之旅。</p>
<p>作为一个半数码党，对于现在数码产品显示器的刷新率种类还是懂一点的。有120hz，144hz等等。我抱着试试看的心态，去搜了144hz下 <code>requestAnimationFrame</code> 的状况</p>
<h2 data-id="heading-1">现状</h2>
<p>果然不出所料。我通过搜索，找到了一篇问答帖：这位网友讲，它使用了<code>165hz</code>的显示器，但通过<code>requestAnimationFrame</code> 计算出来的<code>FPS</code>依然只有<code>30-60fps</code>。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/838ddbe4a7cb4d5a9081d728a9456fd3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那就证明了，的确在一部分用户下，刷新率和 <code>requestAnimationFrame</code> 存在不同步问题。可是在回答区，有一部分用户也反馈，他们屏幕刷新率和 <code>requestAnimationFrame</code> 是同步的。<strong>这样也印证了大概率是一个Bug。</strong></p>
<h2 data-id="heading-2">真的是 Bug</h2>
<p>于是我去<code>Chromium Bugs</code>网站内去查找，找到了这样的一个<a href="https://bugs.chromium.org/p/chromium/issues/detail?id=535392" target="_blank" rel="nofollow noopener noreferrer">Issue</a>。内容也在写，使用了<code>144hz</code>刷新率的显示器，但FPS上限依然只有60。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b517a4d03c244f6abbbe947e2e3a02a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>于是我抛弃掉一部分争论，直接找修复的代码和备注。继续向下翻，找到了<code>chromium</code>官方人员关于只有<code>60fps</code>的解释：</p>
<blockquote>
<p>On Linux Nvidia we use GLX_SGI_video_sync to time vsyncs. Unfortunatelyit's difficult to calculate an accurate refresh rate with it because itsvideo sync counter is wrong. Before, we hardcoded 60 FPS. Now insteadwe use xrandr to get the refresh rate of the primary monitor.</p>
</blockquote>
<p>其大意是，由于在<code>Linux</code>下的<code>Nvdia</code>驱动，在使用<code>GLX_SGI_video_sync</code>进行计算<code>vsyncs</code>(垂直同步)的时间时，由于计数器错误，于是官方直接将<code>60FPS</code><strong>进行硬编码</strong>。现在，他们换成了使用<code>xrandr</code>进行获取刷新率计算。</p>
<blockquote>
<p>xrandr 是一款Linux官方的 RandR (Resize and Rotate)。它可以设置屏幕显示的大小、方向、镜像等。<a href="https://wiki.archlinux.org/index.php/Xrandr_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)" target="_blank" rel="nofollow noopener noreferrer">wiki.archlinux.org/index.php/X…</a></p>
</blockquote>
<p>既然是<code>Bug</code>，那我们就看下<code>Chromium</code>到底是怎么修复的</p>
<h2 data-id="heading-3">修复逻辑</h2>
<p>找到回答中具体的<code>commit</code>记录，然后链接到<code>Chromium Gerrit</code>平台。来到了这个<a href="https://chromium-review.googlesource.com/c/chromium/src/+/1812241" target="_blank" rel="nofollow noopener noreferrer">CR详情</a></p>
<p>来到 <a href="https://chromium-review.googlesource.com/c/chromium/src/+/1812241/4/ui/gl/gl_surface_glx.cc" target="_blank" rel="nofollow noopener noreferrer">gl_surface_glx.cc</a>这个文件。<code>glx</code>是<code>Chromium</code>中硬件加速相关的代码</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9b8c38c9a064507b35ea542ca92e9f8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到，其中的一个float变量叫 <code>refresh_rate</code>，这个就是最后计算刷新率的值。然后使用 <code>(1 / refresh_rate)</code>，计算出刷新一次所控制的秒。如果是<code>60hz</code>，则 <code>1000ms / 60次 = 16.66ms</code> 1次。</p>
<p>这里我们继续跟 <code>refresh_rate</code> 的计算方法 => <code>GetRefreshRateFromXRRModeInfo</code>。找到 <a href="https://chromium-review.googlesource.com/c/chromium/src/+/1812241/4/ui/base/x/x11_display_util.cc" target="_blank" rel="nofollow noopener noreferrer">x11_display_util.cc</a> 文件可以看到逻辑</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e9bcb18cdf84d719177491b040d2e64~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里可以看到，其计算逻辑是 <code>Pixel Clock / (Horizontal Total * Vertical Total)</code>。那么这三个数值代表什么意思呢？</p>
<ul>
<li><code>Pixel Clock</code> 时钟频率，是显示器每秒钟绘制的像素数。</li>
<li><code>Horizontal Total</code> 每一帧绘制的水平像素数量</li>
<li><code>Vertical Total</code> 每一帧绘制的垂直像素数量</li>
</ul>
<p>即<code>时钟每秒处理的像素数量 / (水平像素数量) * (行像素数量)</code>。</p>
<h2 data-id="heading-4">关于多显示器</h2>
<p>从<code>Chromium Gerrit</code>平台提交的代码注释中可以看到，多显示器支持其实是存在问题的。这里可以参考另外一个<a href="https://bugs.chromium.org/p/chromium/issues/detail?id=726842" target="_blank" rel="nofollow noopener noreferrer">Bug</a>。这位同学使用了<code>144hz + 60hz</code>的显示器，但输出依然是<code>60fps</code></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed1a442887ef4d78988eea9827f0a088~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>目前官方人员只提出了解决方案，但没有看到任何<code>commit</code>有产出。所以这还是个<code>Bug</code></p>
<h2 data-id="heading-5">其他参考</h2>
<ul>
<li><a href="https://www.cnblogs.com/biglucky/p/4142505.html" target="_blank" rel="nofollow noopener noreferrer">www.cnblogs.com/biglucky/p/…</a></li>
<li><a href="https://superuser.com/questions/661084/what-is-the-pixel-clock-setting-on-my-monitor-actually-doing" target="_blank" rel="nofollow noopener noreferrer">superuser.com/questions/6…</a></li>
<li><a href="https://www.html5gamedevs.com/topic/17550-framerate-issues-at-144hz/" target="_blank" rel="nofollow noopener noreferrer">www.html5gamedevs.com/topic/17550…</a></li>
<li><a href="https://chromium-review.googlesource.com/c/chromium/src/+/1812241" target="_blank" rel="nofollow noopener noreferrer">chromium-review.googlesource.com/c/chromium/…</a></li>
<li><a href="https://bugs.chromium.org/p/chromium/issues/detail?id=535392" target="_blank" rel="nofollow noopener noreferrer">bugs.chromium.org/p/chromium/…</a></li>
<li><a href="https://news.ycombinator.com/item?id=21577661" target="_blank" rel="nofollow noopener noreferrer">news.ycombinator.com/item?id=215…</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            