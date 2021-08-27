
---
title: 'chrome extension 扩展开发入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/507cfd0290134211aa0a5dab6329fb0c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 01:21:22 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/507cfd0290134211aa0a5dab6329fb0c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">chrome extension 是什么</h2>
<p>扩展程序是自定义浏览体验的小型软件程序。它们让用户可以通过多种方式定制 Chrome 的功能和行为，例如能够提供以下内容：</p>
<ul>
<li>生产力工具</li>
<li>网页内容丰富</li>
<li>信息聚合</li>
<li>乐趣和游戏等</li>
</ul>
<h2 data-id="heading-1">chrome extension 能做什么</h2>
<p>增强浏览器功能，轻松实现属于自己的“定制版”浏览器，等等。</p>
<p>Chrome插件提供了很多实用API供我们使用，包括但不限于：</p>
<ul>
<li>书签控制；</li>
<li>下载控制；</li>
<li>窗口控制；</li>
<li>标签控制；</li>
<li>网络请求控制，各类事件监听；</li>
<li>自定义原生菜单；</li>
<li>完善的通信机制；</li>
<li>等等；</li>
</ul>
<h2 data-id="heading-2">chrome extension 的开发与调试</h2>
<h3 data-id="heading-3">调试</h3>
<p>从右上角菜单->更多工具->扩展程序可以进入 插件管理页面，也可以直接在地址栏输入 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">chrome://extensions</a> 访问。
勾选<code>开发者模式</code>即可以文件夹的形式直接加载插件，否则只能安装<code>.crx</code>格式的文件。Chrome要求插件必须从它的Chrome应用商店安装，其它任何网站下载的都无法直接安装，所以，其实我们可以把<code>crx</code>文件解压，然后通过开发者模式直接加载。</p>
<p>开发中，代码有任何改动都必须重新加载插件，只需要在插件管理页按下<code>Ctrl+R</code>即可，以防万一最好还把页面刷新一下。</p>
<h3 data-id="heading-4">开发</h3>
<p>扩展程序主要结构</p>
<ul>
<li>Manifest （清单文件）</li>
<li>Background Script （后台脚本）</li>
<li>UI Elements （页面元素）</li>
<li>Content Script （内容脚本）</li>
<li>Options Page（配置页面）</li>
</ul>
<h2 data-id="heading-5">chrome extension 结构</h2>
<p>扩展的结构</p>
<h3 data-id="heading-6">background scripts</h3>
<p>background scripts是扩展的事件处理程序; 它包含对扩展浏览器事件的监听，触发后执行指示的逻辑。有效的后台脚本仅在需要时加载，并在空闲时卸载。</p>
<h3 data-id="heading-7">用户界面</h3>
<ol>
<li>popup</li>
<li>可以包含带有 JavaScript 逻辑的普通 HTML 页面。</li>
<li>还可以调用<code>tabs.create</code>或<code>window.open()</code>显示扩展中存在的其他 HTML 文件。</li>
</ol>
<p>使用页面操作和弹出窗口的扩展程序可以使用declarative content API 在后台脚本中设置弹出窗口何时可供用户使用的规则。当条件满足时，后台脚本与弹出窗口通信，使其图标可被用户点击。</p>
<h3 data-id="heading-8">content scripts</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/507cfd0290134211aa0a5dab6329fb0c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">通信</h3>
<p>读取或写入网页的扩展程序使用content scripts。内容脚本包含在已加载到浏览器的页面上下文中执行的 JavaScript。content scripts读取和修改浏览器访问的网页的 DOM。
还可以通过使用storage API交换消息和存储值来进行父子通信。</p>
<h3 data-id="heading-10">通信</h3>
<ol>
<li><code>popup</code>和<code>background</code>之间的通信</li>
</ol>
<p><code>background => popup</code> 是通过<code>getBackgroundPage</code>,
<code>popup => background</code>是通过<code>getViews</code>。</p>
<ol start="2">
<li><code>background</code>和<code>content</code>之间的通信</li>
</ol>
<ul>
<li>长连接： <code>chrome.tabs.connect</code> 和 <code>chrome.runtime.connect</code></li>
<li>短连接： <code>chrome.tabs.sendMessage</code></li>
</ul>
<ol start="3">
<li>
<p><code>popup</code>和<code>content</code>之间的通信</p>
<p>chrome.runtime.sendMessage,
chrome.runtime.onMessage</p>
</li>
</ol>
<h2 data-id="heading-11">chrome extension 常用api</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FGoogleChrome%2Fchrome-extensions-samples" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/GoogleChrome/chrome-extensions-samples" ref="nofollow noopener noreferrer">官方示例</a></p></div>  
</div>
            