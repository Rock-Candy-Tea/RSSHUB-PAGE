
---
title: '_Flutter翻译_迈向Flutter Web的旅程第三部分：设计'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c8ca0c8c0eb4a248e5a5b8779228902~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 16:02:28 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c8ca0c8c0eb4a248e5a5b8779228902~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文地址：<a href="https://medium.com/flutter-clan/journey-towards-flutter-web-part-3-design-6c144d89c83e" target="_blank" rel="nofollow noopener noreferrer">medium.com/flutter-cla…</a></p>
<p>原文作者：<a href="https://medium.com/@hiashutosh" target="_blank" rel="nofollow noopener noreferrer">medium.com/@hiashutosh</a></p>
<p>发布时间：2021年5月27日 - 3分钟阅读</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c8ca0c8c0eb4a248e5a5b8779228902~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果您是直接来到这个页面，请确保在开始这个页面之前，您先通过走向<a href="https://medium.com/flutter-clan/journey-towards-flutter-web-part-2-routing-da09370f3c9d" target="_blank" rel="nofollow noopener noreferrer">Flutter Web的旅程：2</a>。</p>
<p>在这篇文章中，我们将讨论如何在保持单一代码库的情况下，使应用程序在移动和网络上都能响应。</p>
<p>这里有一些Flutter提供的用于构建响应式布局的小工具。</p>
<ul>
<li>自定义单子布局（CustomSingleChildLayout</li>
<li>自定义多子版图（CustomMultiChildLayout</li>
<li>合适的盒子</li>
<li>小数点阵图（FractionallySizedBox</li>
<li>布局生成器</li>
<li>媒体查询</li>
<li>媒体查询数据</li>
<li>方向构建器</li>
<li>纵横比</li>
</ul>
<p>这些部件将帮助你使应用程序在不同尺寸的设备上响应，但在每个设备上的相同的用户界面看起来并不直观，如果你想在不同尺寸的设备上显示不同的用户界面，该怎么办？</p>
<p>下面是<a href="https://gallery.flutter.dev/#/rally" target="_blank" rel="nofollow noopener noreferrer">Rally</a>项目的响应式用户界面的截图，该项目在移动和桌面视图上有不同的用户界面。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47817df854ae480badc35831249ce533~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>拉力赛的桌面界面</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac9e791f90044c8b8f4aed7fe410d926~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>拉力赛的手机版界面</p>
</blockquote>
<p>因此，在这种情况下，你需要使用一个断点，当设备宽度超过或低于该断点时，将改变UI，例如，如果我的断点是700px，那么当设备宽度≤700时显示移动UI，设备宽度>700且设备宽度<=1200时显示平板UI，设备宽度>1200时显示桌面UI。</p>
<p>如果你不想定义自己的断点，你可以使用<a href="https://pub.dev/packages/breakpoint" target="_blank" rel="nofollow noopener noreferrer">这个包</a>，它有很多断点。</p>
<p>下面是如何通过一个辅助类来实现上述条件的。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-comment">/// <span class="markdown">list of all devices</span></span>
<span class="hljs-keyword">enum</span> DeviceType &#123;
  desktop,
  tablet,
  handset,
&#125;

<span class="hljs-comment">/// <span class="markdown">breakpoints for desktop, tablet and handset</span></span>
<span class="hljs-keyword">final</span> desktop = <span class="hljs-number">1200</span>;
<span class="hljs-keyword">final</span> tablet = <span class="hljs-number">900</span>;
<span class="hljs-keyword">final</span> handset = <span class="hljs-number">600</span>;

DeviceType _displayTypeOf(BuildContext context) &#123;
  <span class="hljs-comment">/// <span class="markdown">Use shortestSide to detect device type regardless of orientation</span></span>
  <span class="hljs-built_in">double</span> deviceWidth = MediaQuery.of(context).size.shortestSide;

  <span class="hljs-keyword">if</span> (deviceWidth > desktop) &#123;
    <span class="hljs-keyword">return</span> DeviceType.desktop;
  &#125;
  <span class="hljs-keyword">if</span> (deviceWidth > tablet) &#123;
    <span class="hljs-keyword">return</span> DeviceType.tablet;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> DeviceType.handset;
  &#125;
&#125;

<span class="hljs-built_in">bool</span> isDeviceDesktop(BuildContext context) &#123;
  <span class="hljs-keyword">return</span> _displayTypeOf(context) == DeviceType.desktop;
&#125;

<span class="hljs-built_in">bool</span> isDeviceTab(BuildContext context) &#123;
  <span class="hljs-keyword">return</span> _displayTypeOf(context) == DeviceType.tablet;
&#125;

<span class="hljs-built_in">bool</span> isDeviceMobile(BuildContext context) &#123;
  <span class="hljs-keyword">return</span> _displayTypeOf(context) == DeviceType.handset;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让我们看看如何使用上面的辅助类。</p>
<pre><code class="hljs language-dart copyable" lang="dart">Container(
  child: isDeviceDesktop(context)
      ? _buildDesktopUI()
      : isDeviceTab()
          ? _buildTabletUI()
          : _buildMobileUI(),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请看这些例子项目以供参考。</p>
<ol>
<li><a href="https://github.com/annshsingh/AQI_Monitor" target="_blank" rel="nofollow noopener noreferrer">aqi_monitor</a></li>
<li><a href="https://gallery.flutter.dev/#/" target="_blank" rel="nofollow noopener noreferrer">flutter_gallery</a></li>
</ol>
<hr>
<p>如果你觉得这篇文章有用，请点击拍手图标👏，并与你的朋友分享，因为这将激励我写更多的文章。
如有任何关于Flutter的疑问，请随时在社交媒体平台上与我联系。</p>
<blockquote>
<p><a href="https://linktr.ee/hiahutoshsingh" target="_blank" rel="nofollow noopener noreferrer">linktr.ee/hiahutoshsi…</a></p>
</blockquote>
<hr>
<p>通过www.DeepL.com/Translator（免费版）翻译</p></div>  
</div>
            