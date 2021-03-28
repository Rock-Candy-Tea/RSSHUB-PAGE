
---
title: 'Vite 2.0 初探'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d614ff751ac4341aa0782e4d45c9bd2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 20:56:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d614ff751ac4341aa0782e4d45c9bd2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文/灵傒</p>
</blockquote>
<p><a href="https://link.zhihu.com/?target=https%3A//cn.vitejs.dev/" target="_blank" rel="nofollow noopener noreferrer">Vite</a> 作者尤雨溪原话：</p>
<blockquote>
<p>Vite（法语意思是 “快”，发音为 /vit/，类似 veet）是一种全新的前端构建工具。你可以把它理解为一个开箱即用的开发服务器 + 打包工具的组合，但是更轻更快。Vite 利用浏览器原生的 ES 模块支持和用编译到原生的语言开发的工具（如 esbuild）来提供一个快速且现代的开发体验。</p>
</blockquote>
<h2 data-id="heading-0">发展原因</h2>
<p>在浏览器支持 ES 模块之前，开发者没有以模块化的方式开发 JavaScript 的原生机制。所以，我们一般基于 webpack、Rollup等构建工具，在本地开发的时候，提前把模块打包成浏览器可读取的 js bundle。</p>
<p>但是随着业务的发展，构建的应用也越来越大，模块可能动不动就上百个甚至上千个，就会遇到性能瓶颈，通常需要很长时间才能启动，启动了之后，即使用了HMR热更新，文件的修改也需要几秒钟才能在浏览器里看到效果。</p>
<p>但是现在，浏览器原生就支持了<a href="https://link.zhihu.com/?target=https%3A//developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules" target="_blank" rel="nofollow noopener noreferrer">ES模块化</a>，可以直接在html里写如下代码：</p>
<div id="user-content-root"></div> 
<p><a href="https://link.zhihu.com/?target=https%3A//caniuse.com/%3Fsearch%3Dmodules" target="_blank" rel="nofollow noopener noreferrer">支持原生引入ES模块的浏览器</a>：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d614ff751ac4341aa0782e4d45c9bd2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>所以，可以借助浏览器的自助加载模块功能，来替代构建工具。</p>
<h2 data-id="heading-1">问题和解法</h2>
<p>假设让你从零开始，利用浏览器可引入ES模块的特性，来开发一个开发服务器，会遇到什么问题呢？</p>
<h3 data-id="heading-2">引入路径问题</h3>
<p>首先不可能去改变大家写代码的形式，平时我们引入一个模块，通常用的是称为 bare import 的写法，即 <code>import lodash from 'lodash'</code>，webpack 等工具会去 node_modules 下查找对应模块，帮我们去处理js之间的依赖关系。尝试一下在浏览器直接去<code>import lodash from 'lodash'</code>，它会告诉你，只会识别相对路径或者绝对路径：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/508b9f40186b48058fa14fef1fcd607e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们来通过demo，来看看 Vite 是如何处理这一问题的：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc90a8b6947f44af87b9bdcbd9000f9a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们看vite处理后的代码，将 import React from 'react' 处理成 import __vite__cjsImport_react from "/node_modules/.vite/react.js?v=6c9747e8" 绝对路径：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a4e6383688d41a9a0d1c1087f89cb14~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>看看源码里是如何做到的：</p>
<ol>
<li>首先是启动了一个server</li>
</ol>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f0a6125ca6408a996409da0c156835~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>修改引入方式</li>
</ol>
<ul>
<li>通过 <strong><a href="https://link.zhihu.com/?target=https%3A//github.com/guybedford/es-module-lexer" target="_blank" rel="nofollow noopener noreferrer">es-module-lexer</a></strong> 解析代码生成 ast 语法树，拿到 import 的内容，并转换路径</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4995330da2f1465c935390661e6a497d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">大量零散模块</h3>
<h3 data-id="heading-4">依赖预构建prebuild</h3>
<p>Vite 2.0 在为用户启动开发服务器之前，默认会先用 <code>esbuild</code> 把检测到的依赖预先构建了一遍。</p>
<p>为什么要做这个事情，举个栗子：</p>
<p>当你用 <code>import debounce from 'lodash-es/debounce'</code> ，理想中的场景就是浏览器只加载这个函数的文件。但由于<code>debounce</code> 内部又依赖了 3 个模块：<code>isObject</code> 、<code>now</code>、<code>toNubmer</code>，而这3个模块又有其他的依赖，实际上最后这个函数会引入了14个模块，意味着将带来14次请求:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a233451ea73e498eb6d3aa17a24545b1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这是笔者将 <code>lodash-es</code> 加入到 vite.config.js里的 <code>optimizeDeps.exclude</code>，这样子就不会将 <code>lodash-es</code> 预先构建，此时，看一下在浏览器打开的效果：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57b8789ed665420e936433b0a077fc4f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>和lodash-es相关的一共发了14次请求，所以，为了解决这个问题，Vite 利用 <a href="https://link.zhihu.com/?target=https%3A//github.com/evanw/esbuild" target="_blank" rel="nofollow noopener noreferrer">Esbuild</a> 的超快构建速度，让你在没有感知的情况下在启动的时候预先帮你把 <code>debounce</code> 所用到的所有内部模块全部打包成一个传统的 <code>js bundle</code>。</p>
<p><a href="https://link.zhihu.com/?target=https%3A//esbuild.github.io/" target="_blank" rel="nofollow noopener noreferrer">Esbuild</a> 使用 Go 编写，并且比 JavaScript 编写的构建器预构建依赖快 10-100 倍：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f761abc9028349598526fdebca06b4cc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那我们看看 Vite 源码里这里是如何实现的：</p>
<p>首先，在 server 启动之前， 劫持了 <code>http.listen</code>，重写函数，执行依赖预构建 <code>runOptimize</code>：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21b9b5c8cde84697bb398e6f2789e2de~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其中，runOptimize 所做的事情大致如下：</p>
<ol>
<li>扫描依赖，形成依赖路径map，类似如下结构</li>
</ol>
<p>&#123; "lodash-es_debounce": "node_modules/lodash-es/_debounce" &#125;</p>
<ol>
<li>
<p>使用 Esbuild 把它们提前打包成单文件的 bundle，写入到缓存文件里</p>
</li>
</ol>
<blockquote>
<p>对 runOptimize 感兴趣的可以看这篇文章：<a href="https://link.zhihu.com/?target=https%3A//juejin.cn/post/6938003239610613773" target="_blank" rel="nofollow noopener noreferrer">Vite 2.0 预构建源码解析</a></p>
</blockquote>
<p>前面我们通过 vite.config.js 关闭了对lodash-es的预构建，现在开启，看看最后生成的文件，可以发现，lodash-es_debounce.js 一个文件已经聚合了其内部所依赖的所有模块：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f485fb338f9d499bb90caeb678d0e767~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>此外，在预构建这个步骤中，还会对 CommonJS 模块进行分析，方便后面需要统一处理成浏览器可以执行的 ES Module。</p>
<h3 data-id="heading-5">利用HTTP 2的特性</h3>
<p>可能总会有一些场景你不想让依赖预构建，想让浏览器直接加载它，那应该怎么优化多个并发请求呢？</p>
<p>HTTP 1.x 中，如果想并发多个请求，必须使用多个 TCP 链接，且浏览器为了控制资源，还会对单个域名有 6-8 个的 TCP 链接请求限制； HTTP 2 则可以使用多路复用，代替原来的序列和阻塞机制。所有请求都是通过一个 TCP 连接并发完成。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6888cfb466644dc599c97ace40eed604~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>所以vite也支持了http2，如果 <code>server.https</code> 配置为true，将启用 TLS + HTTP/2，源码：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3ddc755a5b74cc99980fb07043accd7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">真正的按需加载</h3>
<p>此外，和webpack不同的一点是，vite做到了真正的按需加载，只有屏幕上用到的代码才会真正加载进来：</p>
<p>webpack</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0094de214bba4c8bb191224100424671~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>基于 ESM 的构建模式：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/914ff2425d5c4d6cba51ead14d3d86eb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>灰色部分是暂时没有用到的路由，甚至完全不会参与构建过程，随着项目里的路由越来越多，构建速度也不会变慢。</p>
<h2 data-id="heading-7">其他</h2>
<h3 data-id="heading-8">react的热更新</h3>
<p>react的热更新是在 webpack 下是需要和 react-hot-loader 一起来实现的，这个工具虽然很赞，但是 bug 非常多，你甚至需要熟读<a href="https://link.zhihu.com/?target=https%3A//github.com/gaearon/react-hot-loader/blob/master/docs/Troubleshooting.md" target="_blank" rel="nofollow noopener noreferrer">问题清单</a>才能很好的用它。</p>
<p>其实 react 官方实现了 react-refresh 来代替 react-hot-loader，react-refresh 优点在于热更新是不会丢失组件的state的，有人基于 react-refresh 实现了webpack插件 <a href="https://link.zhihu.com/?target=https%3A//github.com/pmmmwh/react-refresh-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer">react-refresh-webpack-plugin</a>，Vite 也集成了 react-refresh。</p>
<h2 data-id="heading-9">结合业务，适用的场景</h2>
<p>如果要在业务中使用vite，可能面临的问题</p>
<ol>
<li>
<p>所使用的第三方包，是否有导出标准的 esm 模块</p>
</li>
<li>
<p>内部开发的包，尽量导出一份 esm 模块</p>
</li>
<li>
<p>外部的包，建议不要用没有 esm 模块的包（都这个年代了，没有 esm 模块导出的包质量有待商榷），或者自行通过工具去转换成 esm 模块</p>
</li>
<li>
<p>Vite 默认只支持原生支持 ESM 的现代浏览器，但可以通过官方的 <a href="https://link.zhihu.com/?target=https%3A//github.com/vitejs/vite/tree/main/packages/plugin-legacy" target="_blank" rel="nofollow noopener noreferrer">@vitejs/plugin-legacy</a> 来支持旧浏览器。legacy 插件会自动额外生成一个针对旧浏览器的包，并且在 html 中插入根据浏览器 ESM 支持来选择性加载对应包的代码（类似 vue-cli 的 modern mode）。</p>
</li>
<li>
<p>本地代理调试问题</p>
</li>
<li>
<p>配套生态完善，例如 babel-plugin-import 可以用 vite-plugin-imp 来代替，但是更多的需要等待 Vite 的生态丰富</p>
</li>
</ol>
<p>适用的场景：</p>
<ol>
<li>
<p>组件库的开发</p>
</li>
<li>
<p>内部应用的开发，对浏览器的兼容性要求不严苛</p>
</li>
<li>
<p>其他应用，可以利用 Vite 来本地开发，线上构建使用老的方式，可能有人担心这样到线上了会不会和本地不一致，导致一些奇怪的问题，但是实际上vite的生产环境构建也是用比较成熟的 rollup，并不是用 esbuild</p>
</li>
</ol>
<p>总之，如果你面临过以下痛点，可以尝试一下Vite:</p>
<ul>
<li>
<p>项目的启动耗时很长</p>
</li>
<li>
<p>改动后二次编译时间长</p>
</li>
<li>
<p>开发React应用，缺少稳定的 HMR 能力 （当然，也可以选择用webpack插件<a href="https://link.zhihu.com/?target=https%3A//github.com/pmmmwh/react-refresh-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer">react-refresh-webpack-plugin</a>)</p>
</li>
</ul>
<h3 data-id="heading-10">示例</h3>
<p>最后，笔者将之前在工作过程中开发过的一个模块，使用 Vite 进行改造，对比了一下启动时间：</p>
<p>旧的脚手架，启动时间，<strong>6586ms</strong>:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9add7df2132945678be1d0808a91ebff~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>使用Vite, 首次启动，<strong>1861ms</strong>，二次启动只需<strong>260ms</strong>:</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40829df3413e4662a96bac5832aa3262~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03e041f7cb9f4983a470285e9e918f51~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">参考文章</h2>
<blockquote>
<p><a href="https://link.zhihu.com/?target=https%3A//juejin.cn/post/6932367804108800007%3Futm_source%3Dgold_browser_extension" target="_blank" rel="nofollow noopener noreferrer">浅谈 Vite 2.0 原理，依赖预编译，插件机制是如何兼容 Rollup 的？</a><br>
<a href="https://link.zhihu.com/?target=https%3A//juejin.cn/post/6896809012512161799" target="_blank" rel="nofollow noopener noreferrer">bundleless热更新原理探索</a><br>
<a href="https://link.zhihu.com/?target=https%3A//js.plainenglish.io/what-is-react-fast-refresh-f3d1e8401333" target="_blank" rel="nofollow noopener noreferrer">What is React Fast Refresh?</a></p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            