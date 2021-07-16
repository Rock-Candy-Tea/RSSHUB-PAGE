
---
title: '有趣的 SVG、Favicon'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e0a7245b46480e9b273572791cf7d8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 06:35:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e0a7245b46480e9b273572791cf7d8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p><code>favicons</code>是在浏览器选项卡中看到的小图标，当浏览浏览器的书签和标签时，它们可以帮助用户清晰的知道是哪个网站。它们是互联网历史的一部分，能够实现一些很酷的效果。</p>
<p>一个非常新的技巧是能够将 <code>SVG</code> 用作 <code>favicon</code>，现在大部份浏览器都支持这一特征。</p>
<p>以下是如何向网站添加收藏夹图标的代码：</p>
<pre><code class="copyable"><link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="alternate icon" href="/favicon.ico">
<link rel="mask-icon" href="/safari.svg" color="#1454ec">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果浏览器不支持 SVG 图标，它将忽略第一个链接元素声明并继续第二个，这确保了所有支持网站图标的浏览器都可以正常显示。</p>
<p>细心的你可能发现第二行中 <code>rel</code> 声明的备用属性值，这是向浏览器声明，使用<code>.ico</code>文件格式的 <code>favicon</code> 是专门用作替代表示的。</p>
<p>最后一行代码，用于加载另一个 SVG 图标，名为<code> safari.svg</code>。这是为了支持 Safari 的固有的标签功能，这个功能在其他浏览器支持 <code>SVG favicon</code> 之前就存在了。当然也可以在这里添加额外的文件，以针对不同的应用程序和服务增强网站。</p>
<p>以下是有关 <code>SVG favicons</code> 浏览器支持情况，截图数据来自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F%3Fsearch%3Dlink-icon-svg" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/?search=link-icon-svg" ref="nofollow noopener noreferrer">Caniuse</a> ：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e0a7245b46480e9b273572791cf7d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">为什么要用SVG</h3>
<p><code> .ico</code> 文件格式很早就存在，可以支持最大 <code>256×256</code> 像素的图像，为什么要用svg？</p>
<h4 data-id="heading-1">容易制作</h4>
<p>制作<code> .ico</code> 文件很痛苦，现在一般通过在线网站来转换。该文件是 Microsoft 使用的专有格式，这意味着需要专门的工具来制作它们。 SVG 是一个开放标准，这意味着可以使用它们而无需任何进一步的工具或平台锁定。</p>
<h4 data-id="heading-2">面向未来</h4>
<p>视网膜？ 5K、 6k，当为网站图标使用对分辨率无感的 SVG 文件时，在确保网站图标在未来的设备上看起来也很清晰，无关显示器分辨率大小。</p>
<h4 data-id="heading-3">性能</h4>
<p>SVG 通常是非常小的文件，特别是与它们的光栅图像对应的文件相比甚至更小。通过仅使用 <code>16×16</code> 像素 <code>favicon</code> 作为不支持 SVG 的浏览器的兼容方案，提供了一个组合设置，使其具有高度的兼容性。</p>
<h3 data-id="heading-4">使用技巧</h3>
<p>SVG 的另一个很酷的地方是可以直接在其中嵌入 CSS，这意味着可以做一些有趣的效果，比如用 JavaScript 动态调整它们，前提是 SVG 被声明为内联而不是使用 <code>img</code> 标签嵌入。</p>
<pre><code class="copyable"><svg  version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <style>
    path &#123; fill: #272019; &#125;
  </style>
  <!-- etc. -->
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于 SVG 图标是使用 link 元素嵌入的，因此无法真正使用 JavaScript 对其进行修改。但是，可以使用 <code>emoji</code> 和 <code>media</code> 之类的技术。</p>
<h4 data-id="heading-5">Emoji</h4>
<p>Emoji表情符号作为网站图标，在SVG的文本元素中使用表情符号来制作一个带有透明背景的小图标，以此作为网站的图标。如有兴趣，可以点击这里<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.devpoint.cn%2Flaboratory%2Ffavicon%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.devpoint.cn/laboratory/favicon/index.html" ref="nofollow noopener noreferrer">查看DEMO</a> 。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3b96dff89a2471da61287db1324a9fb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">暗黑模式支持</h4>
<p>使用 <code>preferred -color-scheme</code> 媒体查询来支持暗黑模式。对于支持的浏览器，很简单就可以实现此效果。</p>
<pre><code class="copyable"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"   viewBox="0 0 16 16">
    <style>
        path &#123;
            fill: #1454ec;
        &#125;
        @media (prefers-color-scheme: dark) &#123;
            path &#123;
                fill: #ffffff;
            &#125;
        &#125;
    </style>
    <path d="m8 0 1.669.864 1.858.282.842 1.68 1.337 1.32L13.4 6l.306 1.854-1.337 1.32-.842 1.68-1.858.282L8 12l-1.669-.864-1.858-.282-.842-1.68-1.337-1.32L2.6 6l-.306-1.854 1.337-1.32.842-1.68L6.331.864 8 0z"/>
    <path d="M4 11.794V16l4-1 4 1v-4.206l-2.018.306L8 13.126 6.018 12.1 4 11.794z"/>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正常效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a9f6d2baf4d4b38951eb0c422454651~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>暗黑模式效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37f3a4f17aee4c288b78afb195224179~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">总结</h3>
<p>favicons 在大小上的不足，在用户体验上弥补。这些图标在网站上作为用户的导航工具，往往会留下浏览器标签。</p>
<p>通常情况下，favicon 是一个快速的视觉标识符，它将用户与数字呈现联系起来。建议使用中以确保它是最好的，更准确地代表品牌。</p></div>  
</div>
            