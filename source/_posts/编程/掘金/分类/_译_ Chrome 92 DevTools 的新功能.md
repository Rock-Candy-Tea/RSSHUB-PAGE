
---
title: '_译_ Chrome 92 DevTools 的新功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4017ddbca9394d9186cdde493ea913b8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 23:35:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4017ddbca9394d9186cdde493ea913b8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.chrome.com%2Fblog%2Fnew-in-devtools-92%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.chrome.com/blog/new-in-devtools-92/" ref="nofollow noopener noreferrer">What's New In DevTools (Chrome 92)</a></li>
<li>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjec.fyi%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jec.fyi/" ref="nofollow noopener noreferrer">Jecelyn Yeen</a></li>
<li>译文出自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%2Fblob%2Fmaster%2Farticle%2F2021%2Fnew-in-devtools-92.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner/blob/master/article/2021/new-in-devtools-92.md" ref="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FUsualminds" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Usualminds" ref="nofollow noopener noreferrer">Usualminds</a></li>
<li>校对者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKimYangOfCat" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KimYangOfCat" ref="nofollow noopener noreferrer">KimYangOfCat</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FChorer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Chorer" ref="nofollow noopener noreferrer">Chorer</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffinalwhy" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/finalwhy" ref="nofollow noopener noreferrer">finalwhy</a></li>
</ul>
</blockquote>
<h2 data-id="heading-0">CSS 网格编辑器</h2>
<p><code>CSS Grid</code> 编辑器是一个社区呼声很高的特性。现在你可以通过它来预览和创建 <code>CSS Grid</code> 布局了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4017ddbca9394d9186cdde493ea913b8~tplv-k3u1fbpfcp-watermark.image" alt="CSS Grid 编辑器" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当页面上的 HTML 元素应用了 <code>display: grid</code> 或者 <code>display: inline-grid</code> 样式时，你可以在样式面板中看到一个图标在它的旁边。单击它就可以切换到 CSS grid 编辑器。在编辑器里，你可以通过屏幕上的图标预览页面的可能发生的变化。（比如：<code>justify-content: space-around</code>），只需要点击一下就可以创建网格对应的外观布局。</p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1203241" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1203241" ref="nofollow noopener noreferrer">1203241</a></p>
</blockquote>
<h2 data-id="heading-1">控制台支持 <code>const</code> 常量重复声明</h2>
<p>除了支持现有的 <a href="https://juejin.cn/blog/new-in-devtools-80/#redeclarations" target="_blank" title="/blog/new-in-devtools-80/#redeclarations"><code>let</code> 和 <code>class</code> 重复声明</a>外，控制台现在也支持了 <code>const</code> 常量的重复声明。无法重复声明常量对 web 开发者来说是一个令人头疼的问题，因为他们经常需要通过控制台来调试 JavaScript 代码。</p>
<p>这样允许开发人员将代码直接复制到 DevTools 控制台，进而查看其工作原理或进行相关调试，对代码进行小范围修改，并且是在不刷新页面的情况下，对该过程进行重复。以前，如果代码中重复声明了 <code>const</code> 绑定的常量，DevTools 是会抛出语法错误的。</p>
<p>可以参考下面的例子。在<strong>不同的 REPL 脚本</strong>中支持 <code>const</code> 常量的重复声明（参考变量 <code>a</code>）。需要注意的是，以下场景是不予支持的：</p>
<ul>
<li>页面脚本中的 <code>const</code> 重复声明，在 REPL 脚本中是不允许的</li>
<li>同一个 REPL 脚本中的 <code>const</code> 变量，也是不允许重复声明的（参考变量 <code>b</code>）</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56fc96ea6b4e4b699c8f2b9dfed69ce8~tplv-k3u1fbpfcp-watermark.image" alt="const 变量重复声明" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1076427" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1076427" ref="nofollow noopener noreferrer">1076427</a></p>
</blockquote>
<h2 data-id="heading-2">源代码查看器</h2>
<p>你可以在屏幕上查看页面元素的排列顺序，这可以更好地进行可访问性检查。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bb0998ee049498da09b4f5543395141~tplv-k3u1fbpfcp-watermark.image" alt="源代码查看器" loading="lazy" referrerpolicy="no-referrer"></p>
<p>HTML 文档中内容的顺序对于搜索引擎优化和提升可访问性至关重要。新的 CSS 特性允许开发人员创建页面内容，这些新创建的内容，在屏幕上的顺序和原来 HTML 文档中的顺序大不相同。这会导致很大的可访问性问题，因为使用屏幕阅读器的用户可能获得和正常用户不同的内容，这是最可能使人感到困惑的用户体验。</p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1094406" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1094406" ref="nofollow noopener noreferrer">1094406</a></p>
</blockquote>
<h2 data-id="heading-3">新的查看 iframe 的快捷方式</h2>
<p>通过右键单击元素面板中的 iframe 元素，并选择 <strong>Show iframe details</strong> 来查看 iframe 的详细信息。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7c37e137c1e437daa18bc9a4855538f~tplv-k3u1fbpfcp-watermark.image" alt="Show frame details" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可以在应用面板（Application）中查看 iframe 详细信息视图，在该面板中可以检查文档详细信息、安全性和隔离状态、权限策略等以调试可能存在的问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a8d8f77c4254fa5b70fa43ec2ccadf8~tplv-k3u1fbpfcp-watermark.image" alt="Frame details view" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1192084" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1192084" ref="nofollow noopener noreferrer">1192084</a></p>
</blockquote>
<h2 data-id="heading-4">增强的 CORS 调试支持</h2>
<p>跨域资源共享（CORS）错误会展示在“问题”选项卡中。造成 CORS 错误的原因有很大。你可以单击展开每个问题来了解可能的原因和解决方法。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f20bdf1b52b3400a8c674f36c9594f51~tplv-k3u1fbpfcp-watermark.image" alt="CORS issues in the Issues tab" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1141824" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1141824" ref="nofollow noopener noreferrer">1141824</a></p>
</blockquote>
<h2 data-id="heading-5">Network 面板更新</h2>
<h3 data-id="heading-6">重命名 XHR 标签为 Fetch/XHR</h3>
<p>XHR 标签现在被重命名为 <strong>Fetch/XHR</strong>。这个变更更明确地说明了该过滤器同时包含了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fxhr.spec.whatwg.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://xhr.spec.whatwg.org/" ref="nofollow noopener noreferrer"><code>XMLHttpRequest</code></a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ffetch.spec.whatwg.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://fetch.spec.whatwg.org/" ref="nofollow noopener noreferrer">Fetch API</a> 两种类型的网络请求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a564fb5ef9874c44bf59fc6b6efa4048~tplv-k3u1fbpfcp-watermark.image" alt="Fetch/XHR label" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1201398" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1201398" ref="nofollow noopener noreferrer">1201398</a></p>
</blockquote>
<h3 data-id="heading-7">Network 面板中过滤新增 Wasm 过滤类型</h3>
<p>现在你可以单击新的 <strong>Wasm</strong> 按钮来过滤 Wasm 类型的网络请求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/612cd6fdc3394021abe8bca1fbe7af38~tplv-k3u1fbpfcp-watermark.image" alt="Filter by Wasm" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1103638" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1103638" ref="nofollow noopener noreferrer">1103638</a></p>
</blockquote>
<h3 data-id="heading-8">Network 状态面板新增提示用户代理端设备选项</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fweb.dev%2Fuser-agent-client-hints" target="_blank" rel="nofollow noopener noreferrer" title="https://web.dev/user-agent-client-hints" ref="nofollow noopener noreferrer">用户代理端提示</a>（User-Agent Client Hints）现在迁移到 <strong>Network conditions</strong> 标签下的 <strong>User agent</strong> 字段中。</p>
<p>用户代理端提示（User-Agent Client Hints）是 Client Hints API 的一个新扩展，它允许开发人员以保护隐私和符合人体工程学的方式访问用户的浏览器信息。。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71611341fe2047e682fce0a674c8e8b0~tplv-k3u1fbpfcp-watermark.image" alt="Network 状态面板新增提示用户代理端设备选项" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1174299" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1174299" ref="nofollow noopener noreferrer">1174299</a></p>
</blockquote>
<h2 data-id="heading-9">在 Issues 标签页中反馈兼容模式问题</h2>
<p>DevTools 现在可以反馈<a href="https://link.juejin.cn/?target=https%3A%2F%2Fquirks.spec.whatwg.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://quirks.spec.whatwg.org/" ref="nofollow noopener noreferrer">兼容模式</a> 和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdom.spec.whatwg.org%2F%23concept-document-limited-quirks" target="_blank" rel="nofollow noopener noreferrer" title="https://dom.spec.whatwg.org/#concept-document-limited-quirks" ref="nofollow noopener noreferrer">受限兼容模式</a>问题。</p>
<p>兼容模式和受限兼容模式是网络标准制定之前就遗留下来的浏览器模式。这些模式模拟的是标准时代之前的布局行为，通常它们会产生意料之外的视觉效果。</p>
<p>当调试布局问题时，开发人员可能会误认为它们是由用户编写的 CSS 或 HTML bug 导致的问题，而真正的问题是页面所在的 Compat 模式。DevTools 提供了修复该问题的建议。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38df68b600c8493ab3a40dca8a5e7370~tplv-k3u1fbpfcp-watermark.image" alt="Report Quirks mode issues in the Issues tab" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F622660" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/622660" ref="nofollow noopener noreferrer">622660</a></p>
</blockquote>
<h2 data-id="heading-10">Performance 面板中新增计算交集</h2>
<p>DevTools 现在可以在火焰图中展示<strong>计算交集</strong>。这个变化可以帮助你识别<a href="https://link.juejin.cn/?target=https%3A%2F%2Fweb.dev%2Fintersectionobserver-v2%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://web.dev/intersectionobserver-v2/" ref="nofollow noopener noreferrer">交集观察</a>事件，并调试其的性能开销。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e01a06a00bb048d5a913112c3e0c289d~tplv-k3u1fbpfcp-watermark.image" alt="Compute Intersections in the Performance panel" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1199137" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1199137" ref="nofollow noopener noreferrer">1199137</a></p>
</blockquote>
<h2 data-id="heading-11">Lighthouse 面板 7.5 版本</h2>
<p>Lighthouse 面板现在运行的是 7.5 版本了。由于 CSS images 的新特性 <code>aspect-ratio</code>，"缺少明确的宽带和高度（missing explicit width and height）" 的警告现在已经被移除，此前，Lighthouse 会对没有明确宽高的图像显示警告。</p>
<p>查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FGoogleChrome%2Flighthouse%2Freleases%2Ftag%2Fv7.5.0" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/GoogleChrome/lighthouse/releases/tag/v7.5.0" ref="nofollow noopener noreferrer">发布说明</a>以获取完整的变更列表。</p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F772558" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/772558" ref="nofollow noopener noreferrer">772558</a></p>
</blockquote>
<h2 data-id="heading-12">调用栈弃用 "Restart frame" 上下文菜单</h2>
<p><strong>Restart frame</strong> 选项已弃用。这个功能需要进一步完善才可以正常工作，目前它已经崩溃，并且经常如此。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60af8fa1dabf4daa8f47a4bccea3c532~tplv-k3u1fbpfcp-watermark.image" alt="弃用 restart frame 上下文菜单" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1203606" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1203606" ref="nofollow noopener noreferrer">1203606</a></p>
</blockquote>
<h2 data-id="heading-13">[实验阶段] 协议监控器</h2>
<p>如果要启用该实验性质功能，请开启 <strong>Settings</strong> > <strong>Experiments</strong> 下的 <strong>Protocol Monitor</strong> 选项。</p>
<p>Chrome DevTools 使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fchromedevtools.github.io%2Fdevtools-protocol%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://chromedevtools.github.io/devtools-protocol/" ref="nofollow noopener noreferrer">Chrome DevTools 协议 (CDP)</a> 来检测、调试和配置 Chrome 浏览器。<strong>协议监控器</strong> 为你提供了一种查看所有 CDP 请求和 DevTools 响应的方法。</p>
<p>新增了两个功能，方便 CDP 测试：</p>
<p>一个是新的 <strong>Save</strong> 按钮允许你下载历史记录消息的 JSON 文件；一个是新的字段，允许你直接发送一个原始的 CDP 命令。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/533d140b3aa44def82eecf645c77d860~tplv-k3u1fbpfcp-watermark.image" alt="协议监控" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issues: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1204004" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1204004" ref="nofollow noopener noreferrer">1204004</a>, <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1204466" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1204466" ref="nofollow noopener noreferrer">1204466</a></p>
</blockquote>
<h2 data-id="heading-14">[实验阶段] Puppeteer Recorder</h2>
<p>如果要启用该实验性质功能，请开启 <strong>Settings</strong> > <strong>Experiments</strong> 下的 <strong>Recorder</strong> 选项。</p>
<p><a href="https://juejin.cn/blog/new-in-devtools-89/#record" target="_blank" title="/blog/new-in-devtools-89/#record">Puppeteer recorder</a> 现在可以根据你和浏览器的交互生成一个操作步骤列表，而之前的 DevTools 则是直接生成一个 Puppeteer 脚本。添加了另一个新的 <strong>Export</strong> 按钮，允许你以 Puppeteer 脚本的形式导出这些步骤。</p>
<p>记录完这些操作步骤后，你可以使用新的 <strong>Replay</strong> 按钮来重放这些步骤。可以按照这个<a href="https://juejin.cn/blog/new-in-devtools-89/#record" target="_blank" title="/blog/new-in-devtools-89/#record">说明</a>来学习如何开始记录浏览器操作步骤。</p>
<p>请注意，这是一个早期的实验功能。我们计划随着时间的推移改善和扩展 Recorder 的功能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82b88df5851f4c6a97ea819370ab6d6f~tplv-k3u1fbpfcp-watermark.image" alt="Puppeteer Recorder" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Chromium issue: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrbug.com%2F1199787" target="_blank" rel="nofollow noopener noreferrer" title="https://crbug.com/1199787" ref="nofollow noopener noreferrer">1199787</a></p>
</blockquote>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" title="https://juejin.im">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23android" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#android" ref="nofollow noopener noreferrer">Android</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23ios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#ios" ref="nofollow noopener noreferrer">iOS</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2589%258D%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" ref="nofollow noopener noreferrer">前端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2590%258E%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" ref="nofollow noopener noreferrer">后端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%258C%25BA%25E5%259D%2597%25E9%2593%25BE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" ref="nofollow noopener noreferrer">区块链</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25A7%25E5%2593%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" ref="nofollow noopener noreferrer">产品</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E8%25AE%25BE%25E8%25AE%25A1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" ref="nofollow noopener noreferrer">设计</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" ref="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="https://link.juejin.cn/?target=http%3A%2F%2Fweibo.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="http://weibo.com/juejinfanyi" ref="nofollow noopener noreferrer">官方微博</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/juejinfanyi" ref="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            