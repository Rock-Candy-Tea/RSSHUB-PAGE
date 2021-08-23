
---
title: 'Fintech FE Weekly issues 1'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7240c950c40f4623b574873927121bf3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 09:31:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7240c950c40f4623b574873927121bf3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">关于本刊</h2>
<p>此周刊主要包含国内、国外每周的前端精选文章和业界趣闻，以及我们前端团队调研、学习的资料分享，每周一更新，权当作者每周的阅读笔记吧~</p>
<h2 data-id="heading-1">正文开始</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.vuejs.org%2Fposts%2Fvue-3.2.html" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.vuejs.org/posts/vue-3.2.html" ref="nofollow noopener noreferrer">Vue 3.2 Released!</a></p>
<p>Vue 3.2 发布了，厉害了~</p>
<ul>
<li>SFC 新特性</li>
<li>直接创建原生的 Web Components</li>
<li>服务端渲染</li>
<li>Effect Scope API</li>
<li>...等等</li>
</ul>
<p><a href="https://juejin.cn/post/6865101730166767623" target="_blank" title="https://juejin.cn/post/6865101730166767623">用「增量」思想提升代码检查和打包构建的效率</a></p>
<p>我们团队正好在做 CI 流水线的增量代码扫描，以及构建打包优化相关的工作，正好看到以下文章，可以参考参考。文章提到了一个库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpahen%2Fmadge" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pahen/madge" ref="nofollow noopener noreferrer">madge</a>，可以分析 CommonJS，AMD 或者 ES6 模块的依赖关系，收藏备用。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7240c950c40f4623b574873927121bf3~tplv-k3u1fbpfcp-watermark.image" alt="madge.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FciKbBI0EKsM_TqKiicAocQ" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/ciKbBI0EKsM_TqKiicAocQ" ref="nofollow noopener noreferrer">重构指北——《重构，改善既有代码设计》精读</a></p>
<p>一篇读书笔记，有关代码重构的，收藏备用。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdinerojs%2Fdinero.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dinerojs/dinero.js" ref="nofollow noopener noreferrer">Dinero.js 格式化金额的小工具</a></p>
<p>做金融相关的业务难免会遇到金额处理的问题，这是一个计算、格式化金额的库，如果不满足国内情况是不是可以二次开发下。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FStuk%2Fjszip" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Stuk/jszip" ref="nofollow noopener noreferrer">jszip</a></p>
<p>JS 直接创建、读取、编辑 <code>.zip</code> 文件</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbubkoo%2Fhtml-to-image" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/bubkoo/html-to-image" ref="nofollow noopener noreferrer">html-to-image</a></p>
<p>html2canvas 几乎都听过，这个是 HTML DOM 直接转图片的库，支持 PNG、SVG、JPG、Blob、Canvas 等格式。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgoogle%2Fzx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/google/zx" ref="nofollow noopener noreferrer">zx</a></p>
<p>Google 出品的库，Node.js 写 shell 脚本更加便利，要求<code>Node.js >= 14.8.0</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e938a560f90e4ac0a6acacedf83d756d~tplv-k3u1fbpfcp-watermark.image" alt="zx.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbvaughn%2Freact-error-boundary" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/bvaughn/react-error-boundary" ref="nofollow noopener noreferrer">react-error-boundary</a></p>
<p>React 核心团队成员写的一个 React error boundary 组件，可以试试。</p></div>  
</div>
            