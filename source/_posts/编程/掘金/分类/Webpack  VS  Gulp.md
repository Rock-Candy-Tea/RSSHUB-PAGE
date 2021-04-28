
---
title: 'Webpack  VS  Gulp'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bea4140f3244888b9e066283d85aab0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 19:51:10 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bea4140f3244888b9e066283d85aab0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>前端项目日益复杂，构建工具已经成为开发过程中不可或缺的一个部分。构建工具，说白了就是帮助我们通过配置或者编写约定好的代码，来自动完成上面的这些功能的一个工具。对于需要反复重复的任务，例如压缩、编译、单元测试、linting等，自动化工具可以减轻我们的劳动，解放我们的双手， 简化我们的工作。</p>
<p>时下流行的前端构建工具有 gulp 和 webpack，本文将对 gulp 和 webpack这两者做一个全面的比较。</p>
<h2 data-id="heading-1">gulp</h2>
<h4 data-id="heading-2">简介</h4>
<p>gulp是一个基于流的自动化构建工具。 除了可以管理和执行任务，还支持监听文件、读写文件。
官网描述如下：</p>
<blockquote>
<p>用自动化构建工具增强你的工作流程！gulp 将开发流程中让人痛苦或耗时的任务自动化，从而减少你所浪费的时间、创造更大价值</p>
</blockquote>
<h4 data-id="heading-3">安装</h4>
<h5 data-id="heading-4">1. 安装nodejs</h5>
<p>gulp是基于nodejs，理所当然需要安装nodejs，打开<a href="https://nodejs.org/en/" target="_blank" rel="nofollow noopener noreferrer">nodejs官网</a>， 官网首页会根据系统信息选择对应版本（.msi文件），点击Download按钮，然后一路next即可安装成功。安装之后可以通过node -v查看安装的nodejs版本，出现版本号，说明刚刚已正确安装nodejs。</p>
<h5 data-id="heading-5">2. 安装gulp</h5>
<p>使用命令行执行gulp的安装</p>
<blockquote>
<p>npm install --global gulp-cli</p>
</blockquote>
<p>通过gulp -v 查看安装的gulp版本，出现版本号，说明已正确安装。</p>
<h4 data-id="heading-6">实践</h4>
<h4 data-id="heading-7">配置gulpfile.js文件，</h4>
<p>gulpfile.js是gulp项目的配置文件（或者首字母大写 Gulpfile.js，就像 Makefile 一样命名）的文件，在运行 gulp 命令时会被自动加载。在这个文件中，你经常会看到类似 src()、dest()、series() 或 parallel() 函数之类的 gulp API，除此之外，纯 JavaScript 代码或 Node 模块也会被使用。任何导出（export）的函数都将注册到 gulp 的任务（task）系统中。（更多配置请<a href="https://www.gulpjs.com.cn/docs/getting-started/javascript-and-gulpfiles/" target="_blank" rel="nofollow noopener noreferrer">查看官网</a>）</p>
<p><strong>简单的gulpfile.js配置(配置文件1)</strong></p>
<pre><code class="copyable">// 导入gulp
const gulp = require('gulp');

// 定义一个print任务 (自定义任务名称)
gulp.task("print",function()&#123;
    console.log("打印123");
&#125;)
// gulp.task(name[, deps], fn) 定义任务  name：任务名称 deps：依赖任务名称 fn：回调函数
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用插件的gulpfile.js配置(配置文件2)</strong></p>
<pre><code class="copyable">// 导入gulp
const gulp = require('gulp'),
    less = require('gulp-less');

// 定义一个testLess任务（自定义任务名称）
gulp.task('testLess', function () &#123;
    gulp.src('src/less/index.less') // 该任务针对的文件
        .pipe(less()) // 该任务调用的模块
        .pipe(gulp.dest('src/css')); // 将会在src/css下生成index.css
&#125;);

// gulp.task(name[, deps], fn) 定义任务  name：任务名称 deps：依赖任务名称 fn：回调函数
// gulp.src(globs[, options]) 执行任务处理的文件  globs：处理的文件路径(字符串或者字符串数组) 
// gulp.dest(path[, options]) 处理完后文件生成路径

gulp.task('default',gulp.series('testLess')); // 定义默认任务

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">运行gulp命令</h4>
<p>根据<strong>配置文件1</strong>在命令行中输入gulp print，得到运行结果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bea4140f3244888b9e066283d85aab0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据<strong>配置文件2</strong>在命令行中输入gulp default，得到运行结果，并在src/css目录下生产index.css文件</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96ea4bda05fb40cb9ac8571cb9170550~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">webpack</h2>
<h4 data-id="heading-10">简介</h4>
<p>webpack 是一个打包模块化 JavaScript 的工具，在 Webpack 里一切文件皆模块，通过 Loader 转换文件，通过 Plugin 注入钩子，最后输出由多个模块组合成的文件。Webpack 专注于构建模块化项目。
其官网的首页图很形象的画出了 Webpack 是什么，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad0618cde399487e9f5b7e406806daf5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">安装webpack</h4>
<p>webpack 跟 gulp 一样都是 node 包，所以在安装webpack之前依然需要安装nodejs，安装完毕后，webpack 的安装指令如下</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install --global webpack
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过webpack -v 查看安装的webpack版本，出现版本号，说明已正确安装。</p>
<h4 data-id="heading-12">实践</h4>
<h5 data-id="heading-13">配置webpack.config.js</h5>
<p>安装完 webpack 之后在项目根目录下新建一个 webpack.config.js，这是 webpack 的默认配置文件，同 gulp 的 gulpfile.js 的功能类似。</p>
<p>由于 webpack 遵循 CommonJS 模块规范，因此，你可以在配置中使用（更多配置请<a href="https://webpack.docschina.org/concepts/configuration/" target="_blank" rel="nofollow noopener noreferrer">查看官网</a>）：</p>
<ul>
<li>通过 require(...) 引入其他文件</li>
<li>通过 require(...) 使用 npm 下载的工具函数</li>
<li>使用 JavaScript 控制流表达式，例如 ?: 操作符</li>
<li>对 value 使用常量或变量赋值</li>
<li>编写并执行函数，生成部分配置</li>
</ul>
<h4 data-id="heading-14">基本配置</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>, <span class="hljs-comment">// 通过选择 development, production 或 none 之中的一个，来设置 mode 参数，你可以启用 webpack 内置在相应环境下的优化。其默认值为 production</span>
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./foo.js'</span>, <span class="hljs-comment">// 入口文件，告诉 webpack 你要编译哪个文件</span>
  <span class="hljs-attr">output</span>: &#123;    <span class="hljs-comment">// output 属性告诉 webpack 在哪里输出它所创建的 bundle，以及如何命名这些文件。主要输出文件的默认值是 ./dist/main.js，其他生成文件默认放置在 ./dist 文件夹中</span>
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'foo.bundle.js'</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">运行webpack命令</h4>
<p>在控制台运行 webpack 命令，生成 bundle.js，编译好的文件 bundle.js 输出到了 dist 目录</p>
<h2 data-id="heading-16">对比结论</h2>
<p>两者都是前端构建工具，gulp在早期比较流行，现在webpack相对来说比较主流，不过一些轻量化的任务还是会用gulp来处理，比如单独打包CSS文件等。</p>
<p>gulp是基于任务和流（Task、Stream）的。类似jQuery，找到一个（或一类）文件，对其做一系列链式操作，更新流上的数据， 整条链式操作构成了一个任务，多个任务就构成了整个web的构建流程。</p>
<p>webpack是基于入口的。webpack会自动地递归解析入口所需要加载的所有资源文件，然后用不同的Loader来处理不同的文件，用Plugin来扩展webpack功能。</p>
<p>所以总结一下：</p>
<ul>
<li>从构建思路来说</li>
</ul>
<p>gulp需要开发者将整个前端构建过程拆分成多个<code>Task</code>，并合理控制所有<code>Task</code>的调用关系。
webpack需要开发者找到入口，并需要清楚对于不同的资源应该使用什么Loader做何种解析和加工。</p>
<ul>
<li>对于知识背景来说</li>
</ul>
<p>gulp更像后端开发者的思路，需要对于整个流程了如指掌 webpack更倾向于前端开发者的思路。</p>
<p>下表是从各个角度对 gulp 和 webpack 做的对比：</p>























































<table><thead><tr><th></th><th>gulp</th><th>webpack</th></tr></thead><tbody><tr><td>分类</td><td>基于流的自动化构建工具。</td><td>模块化加载器兼打包工具。</td></tr><tr><td>目标</td><td>自动化和优化开发工作流，为通用 website 开发而生。</td><td>通用模块打包加载器，为移动端大型 SPA 应用而生。</td></tr><tr><td>上手难易程度</td><td>易于学习，易于使用，api总共只有5个方法。</td><td>有大量新的概念和api，不过好在有详尽的官方文档。</td></tr><tr><td>适用场景</td><td>基于流的作业方式适合多页面应用开发。</td><td>一切皆模块的特点适合单页面应用开发。</td></tr><tr><td>构建方式</td><td>对输入（gulp.src）的 js，ts，scss，less 等源文件依次执行打包（bundle）、编译（compile）、压缩、重命名等处理后输出（gulp.dest）到指定目录中去，为了构建而打包。</td><td>对入口文件（entry）递归解析生成依赖关系图，然后将所有依赖打包在一起，在打包之前会将所有依赖转译成可打包的 js 模块，为了打包而构建。</td></tr><tr><td>使用方式</td><td>常规 js 开发，编写一系列构建任务（task）。</td><td>编辑各种 JSON 配置项。</td></tr><tr><td>优点</td><td>适合多页面开发，易于学习，易于使用，接口优雅。</td><td>可以打包一切资源，适配各种模块系统</td></tr><tr><td>缺点</td><td>在单页面应用方面输出乏力，而且对流行的单页技术有些难以处理（比如 Vue 单文件组件，使用 gulp 处理就会很困难，而 webpack 一个 loader 就能轻松搞定）</td><td>不适合多页应用开发，灵活度高但同时配置很繁琐复杂。“打包一切” 这个优点对于 HTTP/1.1 尤其重要，因为所有资源打包在一起能明显减少浏览器访问页面时的资源请求数量，从而减少应用程序必须等待的时间。但这个优点可能会随着 HTTP/2 的流行而变得不那么突出，因为 HTTP/2 的多路复用可以有效解决客户端并行请求时的瓶颈问题。</td></tr><tr><td>结论</td><td>浏览器多页应用(MPA)首选方案</td><td>浏览器单页应用(SPA)首选方案</td></tr></tbody></table>
<h3 data-id="heading-17">参考文档</h3>
<p><a href="https://www.gulpjs.com.cn/docs/getting-started/quick-start/" target="_blank" rel="nofollow noopener noreferrer">gulp官方文档</a></p>
<p><a href="https://webpack.docschina.org/concepts/why-webpack/" target="_blank" rel="nofollow noopener noreferrer">webpack官方文档</a></p>
<p><a href="https://zhuanlan.zhihu.com/p/44438844" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/44438844</a></p>
<p><a href="https://www.sohu.com/a/298325544_355123" target="_blank" rel="nofollow noopener noreferrer">www.sohu.com/a/298325544…</a></p>
<h3 data-id="heading-18">参考文档</h3>
<p><a href="https://www.gulpjs.com.cn/docs/getting-started/quick-start/" target="_blank" rel="nofollow noopener noreferrer">gulp官方文档</a></p>
<p><a href="https://webpack.docschina.org/concepts/why-webpack/" target="_blank" rel="nofollow noopener noreferrer">webpack官方文档</a></p></div>  
</div>
            