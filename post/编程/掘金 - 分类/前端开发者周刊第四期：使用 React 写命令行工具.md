
---
title: 前端开发者周刊第四期：使用 React 写命令行工具
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 17:49:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b245ff4b74ea4d2583e3eaa050e3db4f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前端爱好者周刊 (Github: shfshanyue/weekly)，每周记录关于前端的开源工具、优秀文章、重大库版本发布记录等等，周刊中优秀文章会在公众号<strong>全栈成长之路</strong>逐一推送。每周一发布，订阅平台如下，欢迎订阅。</p>
<ul>
<li>订阅网站: <a href="https://weekly.shanyue.tech/" target="_blank" rel="nofollow noopener noreferrer">weekly.shanyue.tech</a></li>
<li>订阅 Github: <a href="https://github.com/shfshanyue/weekly" target="_blank" rel="nofollow noopener noreferrer">shfshanyue/weekly</a></li>
</ul>
<h2 data-id="heading-0">封面</h2>
<p><img alt="三星堆遗址新出土黄金面具" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b245ff4b74ea4d2583e3eaa050e3db4f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>考古工作者在三星堆遗址新发现 6 座三星堆文化祭祀坑，目前已出土金面具残片、巨青铜面具、青铜神树、象牙等重要文物 500 余件，图示为出土半边黄金面具。</p>
<h2 data-id="heading-1">一句话</h2>
<ul>
<li><code>copy($var)</code> 在浏览器控制台可以直接复制变量数据</li>
<li>chrome 以前每隔六周一个版本迭代，今后将会加快迭代节奏，每隔四周发布一个新版本</li>
<li><code>npm audit fix</code> 会自动修复有风险的 package</li>
<li>我国科学家在一块形成于大约 9900 万年前的琥珀中发现昆虫新物种，科学家们称之为大角蝽</li>
<li>2021 年全国竞走锦标赛暨东京奥运会选拔赛女子 20 公里竞走比赛中，内蒙古队选手杨家玉以 1 小时 23 分 49 秒的成绩获得冠军并打破世界纪录</li>
</ul>
<h2 data-id="heading-2">开发利器</h2>
<h3 data-id="heading-3"><strong>一、 <a href="https://explainshell.com/" target="_blank" rel="nofollow noopener noreferrer">Explain Shell: 图示任一命令行每个参数的释义</a></strong></h3>
<p><img alt="explainshell" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0d88c6dd0284c91ad50663fcea5b0bc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可称之为学习及书写 shell 的最佳辅助神器，输入任一 linux 命令，都会一一指出每个参数的释义，PIPE 嵌套且复杂的命令也可解析。</p>
<h3 data-id="heading-4"><strong>二、 <a href="https://www.softr.io/tools/svg-wave-generator" target="_blank" rel="nofollow noopener noreferrer">SVG Wave Generator</a></strong></h3>
<p><img alt="SVG 波浪形随机生成器" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14175cbd3f034246b6ce505b32563d5b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>随机生成一个波浪 SVG，可调整锯齿、波折程度等，并可保存为 SVG/PNG/JPG</p>
<h3 data-id="heading-5"><strong>三、 <a href="https://emilkowalski.github.io/css-effects-snippets/" target="_blank" rel="nofollow noopener noreferrer">cssffects: 多种超实用 CSS 动画</a></strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0847afe62a904e18ae31459d71dd0efc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>收集多种 CSS 动画，大部分是各种 hover 效果、loading 动画等，纯 CSS 实现。收藏以备独立设计网站时的不时之需。</p>
<ul>
<li><a href="https://github.com/emilkowalski/css-effects-snippets" target="_blank" rel="nofollow noopener noreferrer">repo: emilkowalski/css-effects-snippets</a></li>
</ul>
<h3 data-id="heading-6"><strong>四、 <a href="https://www.chromestatus.com/features/schedule" target="_blank" rel="nofollow noopener noreferrer">Chrome Platform Status: Chrome 发布版本新特性大览</a></strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24df2ec089e74cb297cefc9e3eba99aa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>列举每一个 Chrome 的新特性大全，目前的稳定版本及下一个版本的发布日期等。</p>
<h2 data-id="heading-7">文章推荐</h2>
<h3 data-id="heading-8"><strong>一、 <a href="https://blog.bitsrc.io/why-you-should-use-picture-tag-instead-of-img-tag-b9841e86bf8b" target="_blank" rel="nofollow noopener noreferrer">为什么你应该使用 Picture 来代替 Img 标签</a></strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a88fd59e41864357a99c8b0b430c7d05~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>picture 标签拥有更好的分辨率切换与媒体查询，当小屏幕使用更小的图片益于性能优化，高分屏使用 2x 图片益于美术设计。</p>
<p>并且可支持书写多种图片格式，对最新的图片格式 avif/webp 提供回退方案，因此可采用最佳图片格式。此处与构建工具一同使用为最佳实践。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">picture</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">source</span> <span class="hljs-attr">srcset</span>=<span class="hljs-string">"test.avif"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"image/avif"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">source</span> <span class="hljs-attr">srcset</span>=<span class="hljs-string">"test.webp"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"image/webp"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"test.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"test image"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">picture</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://juejin.cn/post/6923840549170446343" target="_blank">跳转译文</a></li>
</ul>
<h3 data-id="heading-9"><strong>二、 <a href="https://segmentfault.com/a/1190000039418800" target="_blank" rel="nofollow noopener noreferrer">webpack 核心模块 tapable 用法解析</a></strong></h3>
<p>Plugin 是 webpack 的核心功能之一，而它依赖于 tabpable 这个库，它为 Plugin 的实现提供了事件处理和流程控制多种多样的钩子。</p>
<p>它的核心原理是高级版的发布订阅模式，使用 <code>tap</code> 注册事件，使用 <code>call</code> 触发事件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123;
  SyncHook,
  SyncBailHook,
  SyncWaterfallHook,
  SyncLoopHook,
  AsyncParallelHook,
  AsyncParallelBailHook,
  AsyncSeriesHook,
  AsyncSeriesBailHook,
  AsyncSeriesWaterfallHook
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tapable"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10"><strong>三、 <a href="https://tech.meituan.com/2021/03/18/flutterweb-in-meituanwaimai.html" target="_blank" rel="nofollow noopener noreferrer">Flutter Web 在美团外卖的实践</a></strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54cf5a1f011b461880726481914b1e1f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Flutter 对 Web 的支持已经进入了 Stable 阶段，美团落地了 Flutter Web 并总结了相关经验。但是在 Web 端使用 Flutter 现阶段仍有许多不足，比如脆弱的 Web 生态及构建</p>
<ul>
<li>Flutter 无法对文件进行 Hash 化，因此很难利用 Long Term Cache</li>
<li>Flutter 对打包文件很难进行拆包</li>
<li>Flutter 对资源上传 CDN 比较困难</li>
<li>Flutter Web 自身实现了一套页面滚动机制，页面滚动性能较差。</li>
</ul>
<p>来这篇文章看看美团是怎么解决这些问题的吧，下图是美团的技术架构</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef4f8080565f48c694fd638f6e5e5eb4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11"><strong>四、 <a href="https://segmentfault.com/a/1190000039650874" target="_blank" rel="nofollow noopener noreferrer">v8 Heapsnapshot 文件解析</a></strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcbb1f17168e4cff85ad6af4ac48c849~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>结合 v8 源码看 heapsnashot 文件的数据结构，了解它非常有利于我们调试 Node 中的内存问题</p>
<h2 data-id="heading-12">代码片段</h2>
<h3 data-id="heading-13"><strong>一、 如何给数组去重？</strong></h3>
<p><code>array-union</code> 虽是一个只有一行代码的库，但每个月有一亿次下载量，代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arrayUnion = <span class="hljs-function">(<span class="hljs-params">...arguments_</span>) =></span> [...new <span class="hljs-built_in">Set</span>(arguments_.flat())];

arrayUnion([<span class="hljs-string">'🐱'</span>, <span class="hljs-string">'🦄'</span>], [<span class="hljs-string">'🐻'</span>, <span class="hljs-string">'🦄'</span>], [<span class="hljs-string">'🐶'</span>, <span class="hljs-string">'🌈'</span>, <span class="hljs-string">'🌈'</span>]);
<span class="hljs-comment">//=> ['🐱', '🦄', '🐻', '🐶', '🌈']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14"><strong>二、 Array.prototype.flat: 数组扁平化</strong></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> l = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>]]

l.flat()
<span class="hljs-comment">//=> [1, 2, 3, 4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">开源与库</h2>
<h3 data-id="heading-16"><strong>一、 <a href="https://github.com/formium/tsdx" target="_blank" rel="nofollow noopener noreferrer">tsdx: 零配置可快速开发 npm package 支持 typescript 的命令行工具</a></strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c41ac89a93440c3b495287bacf42a55~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>零配置的可快速开发 Package 的命令行工具，开箱即用 Prettier、ESLint、Jest、Rollup、Publish 等繁琐配置化整为零，并可自动打包为 CJS、ESM、UMD 等多个格式而无需多余配置。</p>
<p>如果你开发 React 组件，还可选内置 Storybook 等，为开发新的 Package 造成了极大的便利。</p>
<ul>
<li><a href="https://tsdx.io/" target="_blank" rel="nofollow noopener noreferrer">repo: https://tsdx.io/</a></li>
<li><a href="https://npmjs.com/package/tsdx" target="_blank" rel="nofollow noopener noreferrer">npm: tsdx</a></li>
</ul>
<h3 data-id="heading-17"><strong>二、 <a href="https://animejs.com/" target="_blank" rel="nofollow noopener noreferrer">anime: 轻量高性能 javascript 动画引擎</a></strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a851633d32e46e0afafd8991a08b93d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可快速地通过编程制作动画，包括而不限于 SVG、CSS、Keyframes 等。在前几期前端开发者周刊中，也曾介绍过另外一个动画引擎: <code>GSAP</code>。</p>
<ul>
<li><a href="https://github.com/juliangarnier/anime" target="_blank" rel="nofollow noopener noreferrer">repo: juliangarnier/anime</a></li>
<li><a href="https://npmjs.com/package/animejs" target="_blank" rel="nofollow noopener noreferrer">npm: animejs</a></li>
</ul>
<h3 data-id="heading-18"><strong>三、 <a href="https://github.com/vadimdemedes/ink" target="_blank" rel="nofollow noopener noreferrer">ink: 使用 React 编写命令行工具</a></strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/414339c73c2640b48e03fe922a630723~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React, &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>
<span class="hljs-keyword">import</span> &#123; render, Text &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"ink"</span>

<span class="hljs-keyword">const</span> Counter = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [counter, setCounter] = useState(<span class="hljs-number">0</span>)

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      setCounter(<span class="hljs-function">(<span class="hljs-params">previousCounter</span>) =></span> previousCounter + <span class="hljs-number">1</span>)
    &#125;, <span class="hljs-number">100</span>)

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">clearInterval</span>(timer)
    &#125;
  &#125;, [])

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">color</span>=<span class="hljs-string">"green"</span>></span>&#123;counter&#125; tests passed<span class="hljs-tag"></<span class="hljs-name">Text</span>></span></span>
&#125;

render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Counter</span> /></span></span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://github.com/vadimdemedes/ink" target="_blank" rel="nofollow noopener noreferrer">repo: vadimdemedes/ink</a></li>
<li><a href="https://npmjs.com/package/ink" target="_blank" rel="nofollow noopener noreferrer">npm: ink</a></li>
</ul>
<h3 data-id="heading-19"><strong>四、 <a href="https://json-ld.org/" target="_blank" rel="nofollow noopener noreferrer">jsonld: JS 实现的 JSON-LD 处理器</a></strong></h3>
<p>JSON-LD 是带有 Link Data 的 JSON 数据格式，常见的 mongo 就是以 jsonld 组织数据。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"@context"</span>: <span class="hljs-string">"https://json-ld.org/contexts/person.jsonld"</span>,
  <span class="hljs-string">"@id"</span>: <span class="hljs-string">"http://dbpedia.org/resource/John_Lennon"</span>,
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"John Lennon"</span>,
  <span class="hljs-string">"born"</span>: <span class="hljs-string">"1940-10-09"</span>,
  <span class="hljs-string">"spouse"</span>: <span class="hljs-string">"http://dbpedia.org/resource/Cynthia_Lennon"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">版本发布</h2>
<h3 data-id="heading-21"><strong>一、 <a href="https://v8.dev/blog/v8-release-90" target="_blank" rel="nofollow noopener noreferrer">v8 9.0 Release</a></strong></h3>
<p>v8 9.0 在三月十七号发布</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            