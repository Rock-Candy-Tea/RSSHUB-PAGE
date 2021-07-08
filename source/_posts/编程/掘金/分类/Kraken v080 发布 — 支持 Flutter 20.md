
---
title: 'Kraken v0.8.0 发布 — 支持 Flutter 2.0'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cf41cb15ae04c4bb98d56faf0a89472~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 23:53:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cf41cb15ae04c4bb98d56faf0a89472~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenkraken.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://openkraken.com/" ref="nofollow noopener noreferrer">openkraken.com/</a></p>
<p>Github: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/openkraken/kraken" ref="nofollow noopener noreferrer">github.com/openkraken/…</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cf41cb15ae04c4bb98d56faf0a89472~tplv-k3u1fbpfcp-watermark.image" alt="66084423.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>自 2021年4月21日开源以来，北海（Kraken）就迎来了社区极大的关注。作为一款兼容 W3C 标准的渲染引擎，打造出高性能，轻量，可扩展的产品一直是 Kraken 团队奋斗的目标。经过近 2 个多月的迭代，在修复了“亿点点”的 bug 后，Kraken 终于迎来了 0.8.0 版本。</p>
<h2 data-id="heading-0">更新内容</h2>
<p><strong>支持 Flutter 最新 stable 版本</strong></p>
<p>0.8 版本支持最新的 Flutter stable 版本 — v2.2.2，并且完美支持 Dart Null Safety。</p>
<p><strong>性能提升</strong></p>
<p>在这个版本中，我们优化了 Bridge 的运行性能，通过之前的调查研究我们发现 JavaScript Bindings 中每一次属性访问的调用，都会对已知的属性集合做一次额外的拷贝，因此我们优化这块的实现来减少不必要的拷贝。</p>
<p>通过这个的优化策略，Kraken 0.8 版本相比 0.7 版本提升了 10% 的首屏性能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/316c5d058f8846b19f627052f8ddaae0~tplv-k3u1fbpfcp-watermark.image" alt="0.7.0vs0.8.0.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Flexbox layout 性能增强</strong></p>
<p>Flexbox 布局的性能也得到了增强，我们新增了判断样式是否变更的策略来减少一些不必要的 layout 操作，进一步压缩了提升了 flexbox 所消耗的时间，即使页面中存在多层 flexbox 嵌套的情况，也能快速生成页面。</p>
<p><strong>新的 HTML 标签和新的 CSS 属性单位</strong></p>
<p>在标签和 CSS 能力方面，我们在 0.8.0 版本添加 h1-h6，strong 等常用 HTML 语义话标签的支持，并且新增了 vmin & vmax CSS 单位，同时还支持文本样式的继承。</p>
<p>在布局能力上，我们新增了 margin 双边距合并的，虽然这个功能在 W3C 小组看来是个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwiki.csswg.org%2Fideas%2Fmistakes" target="_blank" rel="nofollow noopener noreferrer" title="https://wiki.csswg.org/ideas/mistakes" ref="nofollow noopener noreferrer">design mistake</a>，但是我们依然打算去支持它，提供兼容 W3C 标准的渲染能力始终是 Kraken 的主要目标。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f58c637131744b4a13f9f6ef818f158~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210702221853035" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>大量问题修复</strong></p>
<p>开源之后，社区同学反馈了很多 Kraken 使用上的问题，其中包括集成应用黑/白屏，vue/react 页面无法运行，事件冒泡不符合 W3C 标准行为，以及一些其他的报错问题。</p>
<p>在 v0.8.0 版本，上诉的问题中都已经被解决，在这里还要再次感谢社区用户的支持。如果没有你们的帮助，我们做不到这些。</p>
<h2 data-id="heading-1">社区使用情况</h2>
<p>在 Kraken 开源之后，有多家公司都向 Kraken 团队表示，他们将尝试接入 Kraken 到他们的 App 中去，目前已知的公司包括：</p>
<ol>
<li>优酷</li>
<li>高德地图</li>
<li>QQ 音乐</li>
<li>陆金所</li>
<li>涂鸦科技</li>
</ol>
<p>如果你的产品也在尝试使用 Kraken，欢迎在评论区进行回复。</p>
<h2 data-id="heading-2">What's Next</h2>
<p>目前 Kraken 团队的首要目标是提供极致的启动性能，我们将在下个版本（0.9）推出更快的技术方案来提升应用的启动性能：</p>
<ul>
<li>支持 Quickjs，提供 Bytecode 加载支持。</li>
<li>支持 HTML 文本格式，支持 SSR 渲染方案。</li>
</ul>
<p>欢迎持续关注 Kraken 的进展，如果你有任何和 Kraken 有关的问题，欢迎在 Kraken 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/openkraken/kraken" ref="nofollow noopener noreferrer">Github Repo</a> 上发起讨论。</p></div>  
</div>
            