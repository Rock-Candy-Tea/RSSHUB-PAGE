
---
title: 'Chrome DevTools 入门和技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e090f35e4afe43c7830cc6de31144eea~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 18:59:55 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e090f35e4afe43c7830cc6de31144eea~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作为开发人员，平时用的最多的就是 Chrome Devtools 了， 本篇文章将介绍它的常用基础功能和使用技巧。基础部分面对入门开发者，有一定基础可以直接看使用技巧部分。</p>
<h2 data-id="heading-0">基础功能</h2>
<p>首先让我们看下打开 Chrome DevTools 的几种方式</p>
<ul>
<li>右键网页，点击检查</li>
<li>Command+Option+C (Mac) or Control+Shift+C (Windows, Linux, Chrome OS)</li>
<li>F12 快捷键</li>
</ul>
<p>打开后，可以看到 Chrome DevTools 界面</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e090f35e4afe43c7830cc6de31144eea~tplv-k3u1fbpfcp-watermark.image" alt="chrome_panel.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>界面顶部有提供看许多面板，其中常用面板作用如下</p>
<ul>
<li>Elements: 查看 HTML 元素和 CSS 样式，支持实时修改</li>
<li>Console: 记录日志信息，且可以作为与 JavaScript 进行交互的命令行 Shell</li>
<li>Sources: 调试 JavaScript</li>
<li>Network: 查看网络请求信息</li>
<li>Performance: 分析页面性能</li>
<li>Memory: 记录JS CPU执行时间细节、显示JS对象和相关的DOM节点的内存消耗、记录内存的分配细节</li>
<li>Application: 录网站加载的所有资源信息，包括存储数据（Local Storage、Session Storage、IndexedDB、Web SQL、Cookies）、缓存数据、字体、图片、脚本、样式表等</li>
</ul>
<p>接下来我们将重点介绍 Elements, Console, Sources, Network 这四个面板。Performance 和 Memory 面板在需要性能调试的时候在使用。 Application 相对简单，可以直接查看相关信息。</p>
<h3 data-id="heading-1">Elements</h3>
<h4 data-id="heading-2">查看 DOM</h4>
<p>查看 DOM 主要有下面两种方式：</p>
<ol>
<li>右键要查看的 DOM 元素，点击<code>检查</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/592bfce09a6941538496b9cd8c8e825f~tplv-k3u1fbpfcp-watermark.image" alt="dom_1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>点击开发者工具面板左上角的检查按钮（快捷键为 Control+Shift+C），在选择对应的 DOM</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6e9b8ef89d84cdda28182d0ca438aba~tplv-k3u1fbpfcp-watermark.image" alt="dom_2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在选中 DOM 后，我们可以使用键盘的上下左右浏览 DOM 树。左键收起 DOM 节点，右键为打开 DOM 节点。上下键为移动选中点</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb5142b81a74f779af3878f59593183~tplv-k3u1fbpfcp-watermark.image" alt="dom_3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">编辑 DOM</h4>
<p>DOM 的编辑操作可以通过双击对应的 DOM，或者右键点击 DOM。我们可以实时修改 DOM 的标签、属性、内容，甚至还可以打断点监听 DOM 的变化。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e92dcb16f4a4dc0aa8a2afe06e81a68~tplv-k3u1fbpfcp-watermark.image" alt="dom_4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">查看 CSS</h4>
<p>CSS 的查看是在 Elements 面板右侧的 Styles 面板。Styles 面板会展示当前选中的 DOM 节点的样式。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ba7d036a7d84279b437e8bc50205111~tplv-k3u1fbpfcp-watermark.image" alt="css_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">编辑 CSS</h4>
<p>CSS 的编辑可以直接在 Styles 面板中进行，在对应的元素选择器下编辑 CSS</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7994fea7dcc4c0b9d2626872f08a68d~tplv-k3u1fbpfcp-watermark.image" alt="css_1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">Console</h3>
<p>Console 控制台有两个主要用途: 查看日志消息和运行 JavaScript。</p>
<p>在 JavaScript 中输出的日志都可以在控制台中看到</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Loading!'</span>)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello, Console!'</span>)
&#125;, <span class="hljs-number">2000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e9446099b5d4520ba65262dac720df4~tplv-k3u1fbpfcp-watermark.image" alt="console_1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时你可以在 Console 控制台中运行 JavaScript。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f872e2df7534c1abd140d0918630b8d~tplv-k3u1fbpfcp-watermark.image" alt="console_2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">Sources</h3>
<p>Sources 面板主要用来调试 JavaScript，通常用它来调试 Bug。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f43788f64a7478cb63e741748baeffe~tplv-k3u1fbpfcp-watermark.image" alt="sources_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>面板左边部分为文件导航区，在这里可以看到当前页面加载的所有文件；
中间是代码编辑区域，右边是 JavaScript 调试区域，提供断点的步进、步出、继续等能力。</p>
<p>当需要调试 Bug 时，通常会在代码编辑区域对应的行打上断点，然后在逐步进行排查。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd41ac5f904460d8d37eaa61e1e9e88~tplv-k3u1fbpfcp-watermark.image" alt="sources_2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">Network</h3>
<p>Network 面板用来检查网络活动，它可以看到当前网页的所有请求。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33a0de5911814829a6987779d55347fc~tplv-k3u1fbpfcp-watermark.image" alt="network_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>网络请求列表中，可以看到每条请求的名称，返回状态，请求类型，请求发起者，瀑布流信息。</p>
<p>面板中工具栏还提供了筛选、禁用缓存、限制网速等能力。</p>
<h2 data-id="heading-9">使用技巧</h2>
<h3 data-id="heading-10">快速打开所有 DOM</h3>
<p>Alt + Click 可以快速打开当前 DOM 的所有层级。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5e598cdbf454a42bdc4d00554756d5a~tplv-k3u1fbpfcp-watermark.image" alt="chrome_devtools_1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">直观的查看 DOM 层级</h3>
<p>当 DOM 层级很多的时候，可以通过这个方式来查看 DOM 层级</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21e4d508e41748c6944252195622a913~tplv-k3u1fbpfcp-watermark.image" alt="chrome_devtools_5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">DOM 类名切换</h3>
<p>Styles 面板提供了类名快速编辑的能力，相比于直接修改 DOM class属性来说，它提供了更好的调试体验</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d10a6c345234199b0cbfd2bbef0f9f3~tplv-k3u1fbpfcp-watermark.image" alt="chrome_devtools_2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">调试伪类</h3>
<p>Styles 面板提供了伪类的调试能力</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27ddc8e15c2043819e0fe2a67b2874c3~tplv-k3u1fbpfcp-watermark.image" alt="chrome_devtools_3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">改变CSS值的快捷键</h3>
<p>可以通过快捷键来调整 CSS 样式的数值</p>
<ul>
<li><code>Alt+Up</code> + 0.1</li>
<li><code>Up</code> + 1</li>
<li><code>Shift+Up</code> + 10</li>
<li><code>Ctrl+Up</code> + 100</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/216da0727beb4217b13890e0a4b09c7e~tplv-k3u1fbpfcp-watermark.image" alt="chrome_devtools_4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">控制台</h3>
<ul>
<li><code>$()</code>是document.querySelector()的别名</li>
<li><code>$0</code> 返回最近一次选择的元素或 JavaScript 对象</li>
<li><code>console.table(data)</code> 以表格形式打印数据</li>
<li><code>console.time()</code> 和 <code>console.timeEnd()</code> 跟踪代码执行点之间经过的时间。</li>
<li><code>getEventListeners(document)</code> 获取对象的所有事件</li>
</ul>
<h3 data-id="heading-16">Copy</h3>
<p>当你想到控制台复制数据时可以使用</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c13758ae058845619358fa7f4664688b~tplv-k3u1fbpfcp-watermark.image" alt="chrome_devtools_7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">keys/values</h3>
<p>这个是 Devtools 提供的快速查看一个对象的 keys,values 的 API。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7efdcddcf4804ae790eb22aded2334f0~tplv-k3u1fbpfcp-watermark.image" alt="chrome_devtools_8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比直接用<code>Object.keys</code>, <code>Object.values</code> 方便些</p>
<h3 data-id="heading-18">调试安卓设备</h3>
<p>usb 连接设备后，打开 chrome://inspect/#devices</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/575e19bd8ec545d4befd506cf1dfabe9~tplv-k3u1fbpfcp-watermark.image" alt="chrome_devtools_6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了使用 usb 连接设备，你也可以使用 adb 远程连接设备后，在打开 chrome://inspect/#devices， 同样的你也可以看到上面的界面</p>
<h2 data-id="heading-19">参考资料</h2>
<ul>
<li><a href="https://developer.chrome.com/docs/devtools/overview/" target="_blank" rel="nofollow noopener noreferrer">Chrome DevTools 官方文档</a></li>
</ul></div>  
</div>
            