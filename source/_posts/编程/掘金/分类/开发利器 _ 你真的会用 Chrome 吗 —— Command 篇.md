
---
title: '开发利器 _ 你真的会用 Chrome 吗 —— Command 篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/374f5352bd6b48c7bd9304e069fce359~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 07:57:19 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/374f5352bd6b48c7bd9304e069fce359~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第9天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h1 data-id="heading-0">前言</h1>
<p>九边大大在《向上生长》中曾提及：“一个人掌握了复杂工具，才真正具备了能力。人的能力只有和工具叠加起来，才能形成效果叠加”，我深以为然。工具带来的效率提升不言而喻，我们有幸出生在这个各类工具都已经发展得相对成熟的年代，在前人种的大树下乘凉。那么，对 Chrome 这个大树，你的认识有多少？DevTools 的每个面板都认识了吗？Chrome 内置的 Command 用过几个？Chrome 可能远比你想象中强大！</p>
<blockquote>
<p>感谢创造工具的前辈们。</p>
</blockquote>
<h1 data-id="heading-1">Command</h1>
<p>这里首先想介绍的是 <strong>Command</strong>。打开 DevTools 后，<code>Ctrl + Shift + P</code> 打开 Command 面板，第一次打开 Command 的同学，你可能会有发现新大陆的感觉。这里集成了很多快速操作的方法。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/374f5352bd6b48c7bd9304e069fce359~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">面板中有的，它有</h2>
<p><strong>首先是很多面板中能找到的功能，也会同时提供 Command 的调用方式</strong>。比起在面板中苦苦寻觅，使用 Command 直接搜索关键词会更方便呐~ 习惯用命令的同学你一定会喜欢的。</p>
<p>以<strong>切换主题色</strong>为例，你可以在可视面板中找到 Settings - Performance - Appearance - theme 进行设置：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6706ff5b05634e60869fbb58bfafeb46~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你也可以使用 Command： <code>Ctrl + shift + P</code>，输入 theme，是的，然后咱就看到它了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b88b2f471f854acda336118f3b28f3cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51d5c969cd0a4a319f73ab3e23b4a960~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>哎，黑色主题还怪好看的有没有。</p>
</blockquote>
<p>再比如切换显示面板、清除 console 历史、设置颜色格式等，command 都提供了相应的指令。习惯用键盘的同学，完全可以用 command 进行这些操作。</p>
<h2 data-id="heading-3">面板中没有的，它也有</h2>
<p>如果你觉得上面那些面板里也能找到的东西不算啥，Command 里边还有很多被隐藏起来的功能呢！</p>
<h3 data-id="heading-4">截图</h3>
<p><strong>chrome 内置的截图功能</strong>你玩过了嘛？仍然是那个熟悉的 <code>Ctrl + Shift + P</code>，输入 <code>capture</code>，我们可以看到 chrome 内置了几种截图方式：自选区域截取、整页截取（比滚动切图更高效！）、可视区截取、节点截取。骄傲地告诉妈妈，咱再也不用借助第三方的截图工具啦~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/951dd404c6154f30882af64f8eba49eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>悄咪咪告诉你：无头浏览器中实现截图功能，用的就是这个喔。</p>
</blockquote>
<h3 data-id="heading-5">切换布局</h3>
<p>还是 <code>Ctrl + Shift + P</code>，输入 <code>layout</code>，左右布局、上下布局任君选择~</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f77e3816415643b59aa7127ef576fa14~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b16b2def540f4ec8b22530767450f10a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>还有更多功能待挖掘喔</p>
</blockquote>
<h2 data-id="heading-6">Command 命令类型</h2>
<p>Command 集成了非常丰富的方法，按标签可以分为：
<code>Panel</code>、<code>Drawer</code>、<code>Appearance</code>、<code>Console</code>、<code>Debugger</code>、<code>Elements</code>、<code>Global</code>、<code>Grid</code>、<code>Help</code>、<code>Mobile</code>、<code>Navigation</code>、<code>Network</code>、<code>Performance</code>、<code>Rendering</code>、<code>Resources</code>、<code>Screenshot</code>、<code>Sensors</code>、<code>Settings</code>、<code>Sources</code>。
需要查找功能的时候也可以借助这些关键字快速找到想要的功能。Command 的介绍就先到这里啦，更多的功能可以在实践中慢慢发现吧！下一篇咱们聊聊 console，console 又会给我们带来什么样的惊喜呢？可以期待一下~</p></div>  
</div>
            