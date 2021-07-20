
---
title: 'VSCode摸鱼插件 — FreeWindow'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d1c14420edc4ca99fee4ca55fcf3fd7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 05:33:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d1c14420edc4ca99fee4ca55fcf3fd7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>在一些不是很忙的时候，想高效利用下时间，看看书丰富一下自己，但是大庭广众下 长时间看一本实体书，或者看手机的电子书，或者在电脑上看网页书，都不太合适，显得自己很闲的样子，那该如何看起来不是那么明显呢？——那就是写一个VSCode插件，掺和在代码中，沉浸式阅读，就显得自然多了~</p>
<p>于是就有了下面的插件。</p>
<h1 data-id="heading-1">FreeWindow</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d1c14420edc4ca99fee4ca55fcf3fd7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>插件的图标是一条鱼，中间有一个“摸”字 <del>，是摸鱼的意思</del>。</p>
<h3 data-id="heading-2">原理</h3>
<p>实现原理非常简单，没几行代码，就是内置一个浏览器页面在 VSCode 中，把你想要访问的地址填上，点击 Free 就可以访问了。</p>
<h3 data-id="heading-3">使用</h3>
<p>插件地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dlp-moyu-free-window.freewindow" target="_blank" rel="nofollow noopener noreferrer" title="https://marketplace.visualstudio.com/items?itemName=lp-moyu-free-window.freewindow" ref="nofollow noopener noreferrer">marketplace.visualstudio.com/items?itemN…</a></p>
<p>点击插件地址，会在自动打开VSCode进行安装。</p>
<p>安装完成后，按快捷键：<code>cmd + shift + p</code> 或者 <code>查看 -> 命令面板</code>，输入 <code>freewindow</code> 即可打开。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7f9e04b74f0446483532f1c90773b11~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后就会出现一只可爱的鱼：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ab72a9d55e941a2ba5fdbe1d0781628~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后就可以开启<del>摸鱼</del>高效时间利用之旅了</p>
<p>如微信读书，使用暗色模式，嵌入的十分不显眼：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c7dd3992a9741cfa93fcc18c86af191~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73c39c8354d5482ba38ee861882ea063~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb65f4d8b48147108c3ed66c380f0cec~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，你也可以用来看股票、动漫、新闻等等。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edaa09bd41464fa28b3b62d6ff836fb5~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>GitHub Repo: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flecepin%2Fvscode-free-window" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lecepin/vscode-free-window" ref="nofollow noopener noreferrer">github.com/lecepin/vsc…</a></p></div>  
</div>
            