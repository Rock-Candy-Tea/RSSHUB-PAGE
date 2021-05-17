
---
title: '当我们谈论VITE时，我们在谈论什么'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3308d6520a514fb391b9947000f8aaa7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 06:58:08 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3308d6520a514fb391b9947000f8aaa7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在ES6之前，JavaScript没有一个标准的模块方案，社区比较流行的是AMD方案和node使用的CommonJS的方案。</p>
<p>为了能够在浏览器端使用npm上大量的CommonJS规范的包，需要我们去对模块进行兼容和处理，这就是前端打包需要解决的一个问题。</p>
<h2 data-id="heading-1">Webpack</h2>
<p>Webpack是现在主流的打包工具，不管是蚂蚁的umi还是vue的vue-cli，底层都是基于Webpack来进行二次封装的。</p>
<p>Webpack 官方将它定位为一个 <code>module bundler</code>，它通过定义的入口文件，进行依赖收集，构建出项目的依赖图，最后生成并输出一个或多个bundle。</p>
<p>下图是官方给出的Webapck对于模块的处理流程</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3308d6520a514fb391b9947000f8aaa7~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-28_10-18-58.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">一个能在浏览器中运行的模块系统</h3>
<p>我们希望浏览器能够顺利的运行第三方的包和业务代码，不管是commonjs、requirejs或者是es6的模块，所以需要提供一个新的模块系统，将这些第三方包和项目里的业务模块进行统一处理，以便在浏览器中能正确的运行。</p>
<p>webpack 用类似于node 的commonjs的模块方案，将最终打包的代码运行在浏览器中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">modules</span>) </span>&#123; <span class="hljs-comment">// webpackBootstrap</span>
    <span class="hljs-comment">// 已经加载的模板</span>
    <span class="hljs-keyword">var</span> installedModules = &#123;&#125;;
    
    <span class="hljs-comment">// 模块加载函数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span>(<span class="hljs-params">moduleId</span>) </span>&#123;
      <span class="hljs-comment">// ...</span>
    &#125;
    
    <span class="hljs-comment">// 入口文件</span>
    <span class="hljs-keyword">return</span> __webpack_require__(__webpack_require__.s = <span class="hljs-string">"./index.js"</span>);
  &#125;)
  (&#123;
    <span class="hljs-string">"./index.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;&#125;),
    <span class="hljs-string">"./utils/test.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;&#125;)
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面就是webpack打包出来的代码，其中index.js是项目的入口文件，所以的模块都通过 <code>__webpack_require__</code> 进行加载，并且会把加载完成的模块进行缓存。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> installedModules = &#123;&#125;;

<span class="hljs-comment">// The require function</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span>(<span class="hljs-params">moduleId</span>) </span>&#123;
  <span class="hljs-comment">// Check if module is in cache</span>
  <span class="hljs-keyword">if</span>(installedModules[moduleId]) &#123;
    <span class="hljs-keyword">return</span> installedModules[moduleId].exports;
  &#125;
  <span class="hljs-comment">// Create a new module (and put it into the cache)</span>
  <span class="hljs-keyword">var</span> <span class="hljs-built_in">module</span> = installedModules[moduleId] = &#123;
    <span class="hljs-attr">i</span>: moduleId, <span class="hljs-comment">// Module ID</span>
    <span class="hljs-attr">l</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// </span>
    <span class="hljs-attr">exports</span>: &#123;&#125;
  &#125;;

  <span class="hljs-comment">// Execute the module function</span>
  modules[moduleId].call(<span class="hljs-built_in">module</span>.exports, <span class="hljs-built_in">module</span>, <span class="hljs-built_in">module</span>.exports, __webpack_require__);

  <span class="hljs-comment">// Flag the module as loaded</span>
  <span class="hljs-built_in">module</span>.l = <span class="hljs-literal">true</span>;

  <span class="hljs-comment">// Return the exports of the module</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>.exports;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>__webpack_require_</code>的代码可以看出，webpack实现了一个类似CommonJS的模块方案。</p>
<h3 data-id="heading-3">插件系统</h3>
<p>对于webpack来说，如果仅仅解决不同方案模块的聚合和运行，是远远不够的。对于越来越复杂的前端项目，需要提供更加底层的能力给开发者，去实现不同业务场景的不同需求。</p>
<p>Webpack 基于 Tapable 实现了一个复杂的插件系统，在它的构建过程中，对外抛出了各个关键的节点的hook，开发者可以通过订阅这些勾子，对webpack中的资源进行加工和处理，从而完成定制化的需求</p>
<p>通过Plugin和Loader，能够不断扩展Webpack的功能。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4228ad7ffa6940f6a07d1b97c148c0a1~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-28_14-12-36.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">存在的问题</h3>
<p>当然，Webpack 也不是十全十美的，在学习和试用过程中，也会存在大大小小的问题</p>
<ul>
<li>概念和配置项太多，需要配合实际的项目场景不断的优化配置文件，umi、vue-cli等脚手架就是为了解决无法开箱即用的问题</li>
<li>随着项目的不断变大，devServer的启动时间会越来越长，并且hmr的速度也会受到影响</li>
<li>功能缺失，在webpack5之前，没有系统级别的文件缓存系统</li>
</ul>
<h2 data-id="heading-5">契机的出现</h2>
<h3 data-id="heading-6">契机一：http/2</h3>
<p>由于http/2的普及，使得很多基于http/1的优化工作都变成了反模式，其中最主要的一条就是合并代码减少网络请求。</p>
<p>因为在http/1的时代，浏览器只能并行的发起5个请求，这就造成如果文件太多，会存在请求阻塞的问题，所以在很多项目中，我们都会去对代码进行打包生成尽量少的vendor。但是在http/2里，所有的请求都会在一个tcp链接里面完成，并且资源都是并行加载的，这时候单个大文件的加载时间反而会比多个小文件的时间要多。所以在http/2的网络里，我们需要对项目资源进行合理的拆分，充分利用资源的并行请求来减少资源的加载时间。</p>
<h3 data-id="heading-7">契机二：ES Module</h3>
<p>在es6中，加入了JavaScript的模块。</p>
<p>只需要在script标签上加上 <code>type=module</code> 的属性，浏览器就会将内联代码或者外部引用的脚本视为ECMAScript模块。</p>
<p>相比于 Node 的 CommonJS 模块，ES Module 有很多的不同：</p>
<ul>
<li>ES module 抛出的是一个引用，而exports抛出的是一个值</li>
<li>require 可以进行动态引用，而ES module需要在作用域的顶层声明所有的依赖，这就导致Node是可以在运行时去加载模块的， 而ES module可以在编译阶段就完成所有的依赖分析，并为后面的优化做准备(比如tree shaking)</li>
<li>...</li>
</ul>
<p>下面的代码可以在浏览器中直接运行</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// test.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello world'</span>);
&#125;

<span class="hljs-comment">// index.html</span>
<script type=<span class="hljs-string">"module"</span>>
  <span class="hljs-keyword">import</span> hello <span class="hljs-keyword">from</span> <span class="hljs-string">'./test.js'</span>;

  hello(); <span class="hljs-comment">// hello world</span>
</scirpt>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在支持ES module的浏览器中，当解析到ES module模块的时候，浏览器就会自动发起一个请求去加载对应的模块资源，不再需要我们去处理模块的引入和加载。</p>
<p>对于ES module的支持，主流的现代浏览器已经有这不错的兼容性，随着使用者的升级，这个覆盖率会越来越高。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d78e4c4c8064d8fa791694a588c495e~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-28_15-28-10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">Vite</h2>
<p>通过上面的介绍，我们似乎可以利用 http/2 和 浏览器对 ES module 的支持，来直接加载代码，而不再需要进行代码的打包。</p>
<p>Vite 和 snowpack 就是基于这种想法而诞生的前端构建工具。</p>
<h3 data-id="heading-9">Vite是什么</h3>
<blockquote>
<p>Vite，一个基于浏览器原生 ES imports 的开发服务器。利用浏览器去解析 imports，在服务器端按需编译返回，完全跳过了打包这个概念，服务器随起随用。同时不仅有 Vue 文件支持，还搞定了热更新，而且热更新的速度不会随着模块增多而变慢。针对生产环境则可以把同一份代码用 rollup 打。虽然现在还比较粗糙，但这个方向我觉得是有潜力的，做得好可以彻底解决改一行代码等半天热更新的问题。</p>
</blockquote>
<p>-- 摘自尤雨溪微博</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/208fe2e818334026bd3f4f8f82546fe7~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-31_15-41-55.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">Bundleless</h3>
<p>Vite 直接使用ES Module，利用浏览器去解析文件中import的依赖，对于使用到的依赖通过请求去获得相应的资源文件， 从而不再需要像Webpack那样，从入口文件出发，收集所有的依赖然后整体打包，最后把打包的bundle文件交给浏览器解析运行</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/841741c7d82748308b1871c5ae5d3aec~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-28_16-17-56.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是各个构建工具在打包生成最终的代码所需要的时间，其中snowpack和vite都是Bundleless的方案，所以在最后生成代码的时候不需要任何的构建，直接把ES module的代码抛给浏览器即可。</p>
<h3 data-id="heading-11">极速的hmr</h3>
<p>Vite 不会因为模块数量的膨胀而造成热更新的速度变慢，因为 Vite 不像 Webpack 需要构建一份全量的依赖图，并且这份依赖图有可能在模块依赖特别复杂的时候会造成热更新的不准确</p>
<p>devServer使用304来进行协商缓存，对于已经加载过的模块，会增加Cache-Control: max-age=31536000 来做缓存，减少网络请求</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96eab6ad7ee74ef3b657bbf905655b93~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-28_17-52-11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是snowpack和webpack 热更新所需时间的对比</p>
<h3 data-id="heading-12">真正的按需编译</h3>
<p>Vite 通过浏览器的解析来进行依赖资源的加载，所以在文件没有被使用之前，所有的依赖文件都不用进行处理，真正做到了按需编译</p>
<p>Webpack 的spa模式很难进行按需编译，因为从入口文件开始，会做完所有的依赖分析和处理，就算是进行了按需加载的模块，也还是会被编译。 另一个可行的方案是mpa，但是就脱离了单页应用的开发模式了，并且项目在开发和发布的时候复杂度都会增加。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c44f7ba4319c4191b19383498639a753~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-28_10-19-52.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df00b11605a64b898ead3b4fbe95912c~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-28_10-20-07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面两张图片可以直观的看出Vite在编译上的优势，项目只需要在路由层面进行按需加载，就能够做到按需编译。</p>
<p><strong>这里需要注意的是，如果项目没有对路由进行按需加载的处理，最后还是会一次性编译加载所有的依赖</strong></p>
<h3 data-id="heading-13">极速的编译速度</h3>
<p>Vite 使用 Esbuild 来进行代码的编译，其中jsx和tsx都是通过Esbuild解析生成AST，再生成最终的es module的代码，commonjs到ES module也使用它来进行转换</p>
<p>Esbuild是使用Go语言进行开发的，并且发布的是进行编译过的更底层的机器码，在执行效率上远远高于JavaScript编写的打包器，预期会快10-100百倍</p>
<p>在 Vite 1.0 中，使用 rollup 的 @rollup/plugin-commonjs 来实现commonjs转换成ES6，在Vite 2.0 中，使用esbuild来处理模块转换，大大提高了效率</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0823ad6cd2504e608f0edec7c15a575b~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-28_21-04-03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是对10份<code>there.js</code>的包进行打包时，各个构建工具所需要的时间，可以看出esbuild的优势十分巨大</p>
<h3 data-id="heading-14">依赖预构建</h3>
<p>在 Vite 首次运行的时候，会从入口文件出发，对其中的第三方依赖进行分析和打包，并把这些chunk进行缓存，提高页面的加载速度</p>
<p>很多第三方的依赖都是commonjs和umd的模块，通过预构建，用 esbuild 将模块转换为ESM，这样这些第三方的包就能在浏览器中直接运行了</p>
<p>将多入口的模块，比如lodash，转换成单文件的模块，减少网络请求，提高页面的加载性能</p>
<h3 data-id="heading-15">开箱即用</h3>
<p>除了对于Vue的第一优先级的支持，Vite 还在内部内置了大量默认的处理，比如支持jsx和tsx，样式预处理库支持less、sass 和 CSS module</p>
<p>完整的脚手架工具链，可以快速生成Vue、React等项目的模板，提供了大量的配置项，作者说后期有可能会替换掉vue-cli</p>
<p>和vue、vue-cli 一样优秀又友好的文档，并且有对应的中文文档</p>
<h2 data-id="heading-16">简单的处理流程</h2>
<p>使用的核心依赖</p>
<ul>
<li>Connect & Connect middleware</li>
<li>Rollup & Rollup plugin</li>
<li>esbuild & esbuild plugin</li>
<li>acorn、es-module-lexer ...</li>
</ul>
<p>Vite 1.0 的版本中使用 koa 来作为devServer，并且通过koa的插件机制，使用不同的插件来处理各种格式的文件和各种拓展的功能</p>
<p>Vite 2.0 中使用Connect替代了koa，并通过中间件来进行流程控制，因为Vite使用Rollup来进行最终的代码build，所以直接拥抱了Rollup的开源社区， 在内部也继承了Rollup的插件扩展方案，通过Rollup插件来拓展Vite的功能</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a954900da794814b895429f720a8d74~tplv-k3u1fbpfcp-watermark.image" alt="vite流程图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">不足之处</h2>
<ul>
<li>Esbuild 现在还不够稳定，无法用于生产环境的打包，项目打包的时候需要使用Rollup，这就造成开发环境和生产环境的代码不一致，有可能一些bug会无法定位</li>
<li>浏览器的支持度还有待提升</li>
<li>ssr还在试验阶段</li>
</ul>
<h2 data-id="heading-18">惯性思维导致的一些问题</h2>
<p>在试用vite跑demo的时候，遇到了一些问题。</p>
<p>因为使用的技术栈是react + antd，所以就简单的搭了一个demo，来看一下实际的开发体验。在以往的开发中经验中，对于有antd的项目，做的第一件事可能就是引入 babel-plugin-import 实现模块的按需加载，在这个demo中也试用了相同的方案实现按需加载。</p>
<p>但是在项目本地运行以后，发现在没有缓存的第一性运行时，页面加载速度有时候会非常慢，通过network的瀑布图分析后，是因为每次页面进来的时候，都会加载试用到的antd模块。后来分析发现，是 babel-plugin-import 这个插件造成的。</p>
<p>babel-plugin-import的作用是做antd引入语法的转换，转换的效果如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
 
    ↓ ↓ ↓ ↓ ↓ ↓
 
<span class="hljs-keyword">var</span> _button = <span class="hljs-built_in">require</span>(<span class="hljs-string">'antd/lib/button'</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">'antd/lib/button/style/css'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插件将antd的bare import的语法转换成绝对路径的引入方式，这就导致Vite对于antd 的预编译失效，因为预编译只对bare import的模块有效，并且如果当前路由依赖的antd的模块比较多，就会造成页面的加载速度比较慢</p>
<p>最近遇到的另一个babel-plugin-import造成的问题是组件库打包的问题。因为组件依赖了antd，在打包成umd包的时候，需要通过externals将antd、react和react-dom 排除出去，但是在分析最后打包产物的时候，发现react和react-dom没有打包进来，但是antd用到的模块还是被打包进来了。后来经过排查发现，在打包的babel配置中，使用了babel-plugin-import，因为loader的编译是在build构建之前完成的，所有的antd的bare import全被编译成了绝对路径的引入方式，导致webpack build的时候externals替换规则失效，因为externals也只能对bare import的模块进行替换。</p>
<p>所以惯性思维会对我们造成一定程度的困扰，需要我们更透彻的理解其中的原理和构建过程，才能避免很多坑。</p>
<h2 data-id="heading-19">总结</h2>
<ul>
<li>基于 ES Module 的前端构建工具，充分利用浏览器自身的能力，本质上解决本地开发项目构建时间长等问题</li>
<li>相比于Webpack，更加轻量，封装的层级更高</li>
<li>完整的生态，活跃的社区，稳定的核心开发</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff59577026eb440598697416d633d7ed~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-03-28_14-57-41.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            