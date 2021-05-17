
---
title: 'MDH 前端周刊第 2 期：babel、deno、0kb JavaScript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6bfecbbfafa4ccfa6cb448cd015aa76~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 19:11:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6bfecbbfafa4ccfa6cb448cd015aa76~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是 「MDH：前端周刊」 第 0002 期，发表于：2021/05/17。本期刊开源（GitHub: sorrycc/weekly），欢迎 issue 区投稿，推荐或自荐项目。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6bfecbbfafa4ccfa6cb448cd015aa76~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>封面图：2021.5.15，富阳树石村，摄影师：猪罐头。</p>
<h2 data-id="heading-0">⬆️ 头条</h2>
<h3 data-id="heading-1">1. Babel 被数百万人使用，那我们为什么没钱了呢?</h3>
<p><a href="https://babeljs.io/blog/2021/05/10/funding-update" target="_blank" rel="nofollow noopener noreferrer">babeljs.io/blog/2021/0…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab9e0ffb0aa64c6eaa8f6b3e85424bbc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在我看来 Babel 遇到的问题，</p>
<ul>
<li><strong>开发者感知力弱</strong>，Babel 不是上层应用，开发者其实较少能感知到，特别是像 umi、next.js 等框架的封装，开发者的日程使用完全不需要感知 Babel 的存在</li>
<li><strong>强有力的竞争者</strong>，swc、esbuild 的出现，越来越多的框架倾向于选择非 JavaScript 的编译工具来实现提速，Babel 不再是此方向的唯一选择</li>
</ul>
<p>但就蚂蚁而言，目前 Babel 在前端基建中的作用还是不可动摇的，应用包括，</p>
<ul>
<li>TypeScript 支持</li>
<li>高级语言特性</li>
<li>浏览器兼容</li>
<li>基于 babel-plugin-import 的按需编译</li>
<li>组件研发</li>
<li>自动 css modules 识别</li>
<li>约束、lint、代码校验</li>
<li>基于代码解析的自动化工具</li>
<li>…</li>
</ul>
<h3 data-id="heading-2">2. Deno 发布 v1.11</h3>
<p><a href="https://github.com/denoland/deno/releases/tag/v1.10.1" target="_blank" rel="nofollow noopener noreferrer">github.com/denoland/de…</a></p>
<p>包括，</p>
<ul>
<li>Web Storage API 支持，服务端的 localStorage 和 sessionStorage，前者限 5M</li>
<li>重写 deno test，并行 runner、权限、优化输出等</li>
<li>支持远端 import map</li>
</ul>
<h3 data-id="heading-3">3. 0kb 的 JavaScript 是未来吗？</h3>
<p><a href="https://dev.to/this-is-learning/is-0kb-of-javascript-in-your-future-48og" target="_blank" rel="nofollow noopener noreferrer">dev.to/this-is-lea…</a></p>
<p>大家讨论 0kb 时候讨论的是什么？</p>
<ul>
<li>渐进增强，Remix 和 SvelteKit 都可以 ssr 页面，然后不依赖 JavaScript 就拥有完整的表单能力</li>
<li>React Server Components</li>
<li>Islands Architecture</li>
<li>Partial Hydration</li>
</ul>
<h2 data-id="heading-4">📝 文章</h2>
<h3 data-id="heading-5">1. 不要解决问题，去消灭问题</h3>
<p><a href="https://kentcdodds.com/blog/don-t-solve-problems-eliminate-them" target="_blank" rel="nofollow noopener noreferrer">kentcdodds.com/blog/don-t-…</a></p>
<p>全篇看下来更像是 Remix 的软文，但思路没错。我们遇到问题时通常最直接的反应是如何解决他，但换个思路会不会就没有这个问题了？比如 webpack 构建慢社区想了无数的方法，换个思路用非 JavaScript 语言实现，是否就能消灭这个问题呢？</p>
<h3 data-id="heading-6">2. Hello, Modules!</h3>
<p><a href="https://blog.sindresorhus.com/hello-modules-d1010b4e777b" target="_blank" rel="nofollow noopener noreferrer">blog.sindresorhus.com/hello-modul…</a><br>
<a href="https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c" target="_blank" rel="nofollow noopener noreferrer">gist.github.com/sindresorhu…</a> （迁移步骤）</p>
<p>Node 10 已废弃，我们可以安心使用 esm 了。</p>
<p>esm 相比 cjs 有哪些优点？</p>
<ul>
<li>浏览器兼容</li>
<li>top-level await</li>
<li>re-export 语法</li>
<li>一行代码同时 import default export 和 named exports</li>
</ul>
<p>附迁移步骤。</p>
<h3 data-id="heading-7">3. 根据 visibility 懒加载 JS</h3>
<p><a href="https://codepen.io/jonneal/full/ZELvMvw" target="_blank" rel="nofollow noopener noreferrer">codepen.io/jonneal/ful…</a></p>
<p>基于 Intersection Observer，是 Islands Architecture 的一种应用，文中给了代码和 DEMO，但触发事件可以不仅是元素的可见，还可以是 media query、container query、event、闲置状态等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecd8c6a115ac45488471baaf0ab329c9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">4. 我给自己设立了每月 $20 的开源捐赠预算</h3>
<p><a href="https://lutaonan.com/blog/my-oss-donation-budget/" target="_blank" rel="nofollow noopener noreferrer">lutaonan.com/blog/my-oss…</a></p>
<p>👍🏻</p>
<h3 data-id="heading-9">5. WebAssembly 入门</h3>
<p><a href="https://lencx.github.io/book/wasm/rust_wasm_frontend.html" target="_blank" rel="nofollow noopener noreferrer">lencx.github.io/book/wasm/r…</a></p>
<p>使用 vite 快速开始一个 wasm 项目，vite + (rust -> wasm) + (vue/react)。</p>
<p>自荐人：lencx</p>
<h3 data-id="heading-10">6. Complete Intro to React, v6</h3>
<p><a href="https://btholt.github.io/complete-intro-to-react-v6/" target="_blank" rel="nofollow noopener noreferrer">btholt.github.io/complete-in…</a></p>
<h3 data-id="heading-11">7. 使用React 时应避免的10大错误</h3>
<p><a href="https://javascript.plainenglish.io/top-10-mistakes-to-avoid-when-using-react-1796711ad2a0" target="_blank" rel="nofollow noopener noreferrer">javascript.plainenglish.io/top-10-mist…</a></p>
<p>十大错误：</p>
<ol>
<li>组件拆分不够细</li>
<li>直接修改 state 对象</li>
<li>props 里把 number 当 string 传</li>
<li>组件列表不带 key</li>
<li>不清楚 setState 是异步的</li>
<li>过度使用 Redux</li>
<li>写巨石组件而不拆</li>
<li>目录结构不符合社区规范</li>
<li>写惯了 HTML 啥属性都用 String 传</li>
<li>组件名没有用大驼峰</li>
</ol>
<h2 data-id="heading-12">🪓 代码</h2>
<h3 data-id="heading-13">1. nuxt/vite</h3>
<p><a href="https://github.com/nuxt/vite" target="_blank" rel="nofollow noopener noreferrer">github.com/nuxt/vite</a></p>
<p>Nuxt 2 ❤️ Vite。</p>
<h3 data-id="heading-14">2. 专注于 React 的代码编辑器是什么样子?</h3>
<p><a href="https://codesandbox.io/s/ide-concept-ke6vz" target="_blank" rel="nofollow noopener noreferrer">codesandbox.io/s/ide-conce…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/882cb65c8ab74466a9a78938567b3795~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">3. sinclairzx81/hammer</h3>
<p><a href="https://github.com/sinclairzx81/hammer" target="_blank" rel="nofollow noopener noreferrer">github.com/sinclairzx8…</a></p>
<p>浏览器和 Node 应用的构建工具。基于 esbuild，看使用方式，类似 parcel？</p>
<h3 data-id="heading-16">4. dai-shi/excalidraw-animate</h3>
<p><a href="https://github.com/dai-shi/excalidraw-animate" target="_blank" rel="nofollow noopener noreferrer">github.com/dai-shi/exc…</a></p>
<p>转换 Excalidraw 图纸为动画。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bfa256263804a048f00576edc35c890~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">5. microsoft/folio</h3>
<p><a href="https://github.com/microsoft/folio" target="_blank" rel="nofollow noopener noreferrer">github.com/microsoft/f…</a></p>
<p>微软出的测试框架，Jest 有竞品了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">test(<span class="hljs-string">'insert an entry'</span>, <span class="hljs-keyword">async</span> (&#123; table &#125;) => &#123;
  <span class="hljs-keyword">await</span> table.insert(&#123; <span class="hljs-attr">username</span>: <span class="hljs-string">'folio'</span>, <span class="hljs-attr">password</span>: <span class="hljs-string">'testing'</span> &#125;);
  <span class="hljs-keyword">const</span> entry = <span class="hljs-keyword">await</span> table.query(&#123; <span class="hljs-attr">username</span>: <span class="hljs-string">'folio'</span> &#125;);
  expect(entry.password).toBe(<span class="hljs-string">'testing'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">6. hellodword/wechat-feeds</h3>
<p><a href="https://github.com/hellodword/wechat-feeds" target="_blank" rel="nofollow noopener noreferrer">github.com/hellodword/…</a></p>
<p>给微信公众号生成 RSS 订阅源，可以使用 rsshub 的，<code>https://rsshub.app/wechat/feeds/%%bizId%%</code>，有内容抓取。</p>
<h3 data-id="heading-19">7. chanify/chanify</h3>
<p><a href="https://github.com/chanify/chanify" target="_blank" rel="nofollow noopener noreferrer">github.com/chanify/cha…</a></p>
<p>Chanify 是一个简单的消息推送工具。每一个人都可以利用提供的 API 来发送消息推送到自己的 iOS 设备上。</p>
<h3 data-id="heading-20">8. princefishthrower/react-use-please-stay</h3>
<p><a href="https://github.com/princefishthrower/react-use-please-stay" target="_blank" rel="nofollow noopener noreferrer">github.com/princefisht…</a></p>
<p>页面的焦点丢失时，实现标题或 favicon 动画的 React Hook。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6de10f4a17644ef95f6dc3ae50ae9d3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">9. bytedance/guide</h3>
<p><a href="https://github.com/bytedance/guide" target="_blank" rel="nofollow noopener noreferrer">github.com/bytedance/g…</a></p>
<p>基于 React 的新功能引导组件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c04ba1de4aa4b10aed90861ba7ff145~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-22">🕒 订阅</h2>
<p>本周刊每周一发布，同步更新在语雀 <strong>「mdh/weekly」</strong> 和微信公众号。</p>
<p>微信搜索 <strong>「云谦」</strong> 即可订阅。</p>
<p>（完）</p></div>  
</div>
            