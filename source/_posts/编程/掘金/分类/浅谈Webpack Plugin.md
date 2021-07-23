
---
title: '浅谈Webpack Plugin'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b409422c169f4ae399a22d92dd7c8e87~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 01:52:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b409422c169f4ae399a22d92dd7c8e87~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>你想深入学习webpack吗？你想自己开发一个webpack plugin吗？我就问问，不想就算了吧！</p>
<h1 data-id="heading-0">了解一下什么是Plugin?</h1>
<p>官方文档定义：<strong>插件</strong>是 webpack 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Ftapable" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/tapable" ref="nofollow noopener noreferrer">支柱</a> 功能。webpack 自身也是构建于你在 webpack 配置中用到的<strong>相同的插件系统</strong>之上！</p>
<p>插件目的在于解决 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconcepts%2Floaders" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/concepts/loaders" ref="nofollow noopener noreferrer">loader</a> 无法实现的<strong>其他事</strong>。</p>
<p>Webpack Plugin其实就是一个类！！！</p>
<h1 data-id="heading-1">创建一个 Plugin</h1>
<h2 data-id="heading-2">先学会一个简易版的plugin</h2>
<pre><code class="copyable">// myPlugin.js
class MyPlugin &#123;
constructor() &#123;
    console.log('Plugin 被创建了');
  &#125;
  apply(compiler) &#123;&#125;
&#125;

module.exports = MyPlugin;

// webpack.config.js
// 引入
const MyPlugin = require('myPlugin.js');
module.exports = &#123;
plugins: [
  new MyPlugin(&#123;title: 'MyPlugin'&#125;),
  ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先来看一下 <strong>Webpack</strong> ****<strong>官方</strong>给的案例：</p>
<pre><code class="copyable">const pluginName = 'ConsoleLogOnBuildWebpackPlugin';

class ConsoleLogOnBuildWebpackPlugin &#123;
    apply(compiler) &#123;
        // 代表开始读取 records 之前执行
        compiler.hooks.run.tap(pluginName, compilation => &#123;
            console.log("webpack 构建过程开始！");
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">简单说明</h3>
<ul>
<li>Plugin 其实就是一个类。</li>
<li>类需要一个 apply 方法，执行具体的插件方法。</li>
</ul>

<ul>
<li>插件方法做了一件事情就是在 run 这个 Hook 上注册了一个同步的打印日志的方法。</li>
<li>apply 方法的入参注入了一个 compiler 实例，compiler 实例是 Webpack 的支柱引擎，代表了 CLI 和 Node API 传递的所有配置项。</li>
</ul>

<ul>
<li>Hook 回调方法注入了 compilation 实例，compilation 能够访问当前构建时的模块和相应的依赖。</li>
</ul>
<p>就这？就这？就这？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b409422c169f4ae399a22d92dd7c8e87~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-4">接下来讲解下基础知识点</h1>
<h2 data-id="heading-5">什么是Hook？</h2>
<p>Webpack 在编译的过程中会触发一系列流程，而在这样一连串的流程中，Webpack 把一些关键的流程节点暴露出来供开发者使用，这就是 Hook，可以类比 React / Vue的生命周期钩子。</p>
<p>Plugin 就是在这些 Hook 上暴露出方法供开发者做一些额外操作，因此在写 Plugin 的时候，也需要先了解我们应该在哪个 Hook 上做操作。</p>
<p>Webpack 共提供了以下十种 Hooks，代码中所有具体的 Hook 都是以下这 10 种中的一种。</p>
<pre><code class="copyable">// 源码取自：lib/index.js
"use strict";

exports.__esModule = true;

// 同步执行的钩子，不能处理异步任务
exports.SyncHook = require("./SyncHook");

// 同步执行的钩子，返回非空时，阻止向下执行
exports.SyncBailHook = require("./SyncBailHook");

// 同步执行的钩子，支持将返回值透传到下一个钩子中
exports.SyncWaterfallHook = require("./SyncWaterfallHook");

// 同步执行的钩子，支持将返回值透传到下一个钩子中，返回非空时，重复执行
exports.SyncLoopHook = require("./SyncLoopHook");

// 异步并行的钩子
exports.AsyncParallelHook = require("./AsyncParallelHook");

// 异步并行的钩子，返回非空时，阻止向下执行，直接执行回调
exports.AsyncParallelBailHook = require("./AsyncParallelBailHook");

// 异步串行的钩子
exports.AsyncSeriesHook = require("./AsyncSeriesHook");

// 异步串行的钩子，返回非空时，阻止向下执行，直接执行回调
exports.AsyncSeriesBailHook = require("./AsyncSeriesBailHook");

// 支持异步串行 && 并行的钩子，返回非空时，重复执行
exports.AsyncSeriesLoopHook = require("./AsyncSeriesLoopHook");

// 异步串行的钩子，下一步依赖上一步返回的值
exports.AsyncSeriesWaterfallHook = require("./AsyncSeriesWaterfallHook");

// 以下 2 个是 hook 工具类，分别用于 hooks 映射以及 hooks 重定向
exports.HookMap = require("./HookMap");
exports.MultiHook = require("./MultiHook");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Hook 的类型可以通过官方 API 查询，地址传送门：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.webpackjs.com%2Fapi%2Fcompiler-hooks%2F%3FfileGuid%3D3tGHdrykRgwCyTP8" target="_blank" rel="nofollow noopener noreferrer" title="https://www.webpackjs.com/api/compiler-hooks/?fileGuid=3tGHdrykRgwCyTP8" ref="nofollow noopener noreferrer">www.webpackjs.com/api/compile…</a></p>
<h2 data-id="heading-6">核心工具库Tapable</h2>
<p>Tapable是什么？webpack就是一个事件流，这个事件流是一个个插件组成的，而保证这些插件有序的运行就是Tapable的作用，它是采用发布订阅的架构模式。tapable中有很多钩子方法，用来搜集注册的plugin。简单来说Tapable就是webpack用来创建钩子的库。</p>
<p>Tapable 是 Webpack 核心工具库，它提供了所有 Hook 的抽象类定义，Webpack 许多对象都是继承自 Tapable 类。比如： tap，tapAsync和tapPrimise。</p>
<pre><code class="copyable">// 第二节 “创建一个 Plugin” 中说的 10 种 Hooks 都是继承了这两个类
// 源码取自：tapable.d.ts
declare class Hook<T, R, AdditionalOptions = UnsetAdditionalOptions> &#123;
  tap(options: string | Tap & IfSet<AdditionalOptions>, fn: (...args: AsArray<T>) => R): void;
&#125;

declare class AsyncHook<T, R, AdditionalOptions = UnsetAdditionalOptions> extends Hook<T, R, AdditionalOptions> &#123;
  tapAsync(
    options: string | Tap & IfSet<AdditionalOptions>,
    fn: (...args: Append<AsArray<T>, InnerCallback<Error, R>>) => void
  ): void;
  tapPromise(
    options: string | Tap & IfSet<AdditionalOptions>,
    fn: (...args: AsArray<T>) => Promise<R>
  ): void;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">什么是compiler?</h2>
<p>compiler包含了webpack环境所有的配置信息。 这个对象在启动webpack时被一次性建立，并配置好所有可操作的设置，包括options，loader和plugin。当在webpack环境中应用一个插件时，插件将收集到此compiler对象的引用。可以使用它来访问webpack的主环境。</p>
<h2 data-id="heading-8">什么是compilation?</h2>
<p>compilation对象包含了当前模块资源、编译生成资源、变化的文件等。当运行webpack开发环境中间件时，没检测到一个文件变化，就会创建资源。</p>
<p>compilation对象也提供了很多关键时机的回调，以供插件做自定义处理时选择使用。</p>
<h2 data-id="heading-9">compiler和compilation的区别？</h2>
<pre><code class="copyable">Compiler 对象包含了 Webpack 环境所有的的配置信息，包含 options，loaders，plugins 这些信息，这个对象在 Webpack 启动时候被实例化，它是全局唯一的，可以简单地把它理解为 Webpack 实例；

Compilation 对象包含了当前的模块资源、编译生成资源、变化的文件等。当 Webpack 以开发模式运行时，每当检测到一个文件变化，一次新的 Compilation 将被创建。Compilation 对象也提供了很多事件回调供插件做扩展。通过 Compilation 也能读取到 Compiler 对象。
                                              —— 摘自「深入浅出 Webpack」
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>生成时间不同，周期长度不同。compiler在webpack开始到关闭整个生命周期存在，而compilation只是代表了一次新的编译过程。</li>
<li>compiler和compilation暴露出的钩子不同。</li>
</ol>
<p><em><strong>compiler常用的钩子</strong></em></p>



































<table><thead><tr><th>Hook</th><th>type</th><th>调用</th></tr></thead><tbody><tr><td>run</td><td>AsyncSeriesHook</td><td>开始读取 records 之前</td></tr><tr><td>compile</td><td>SyncHook</td><td>一个新的编译(compilation)创建之后</td></tr><tr><td>emit</td><td>AsyncSeriesHook</td><td>生成资源到 output 目录之前</td></tr><tr><td>done</td><td>SyncHook</td><td>编译(compilation)完成</td></tr><tr><td>initialize</td><td>SyncHook</td><td>当编译器对象被初始化时调用(html-webpack-plugin中有用到)</td></tr></tbody></table>
<p><em><strong>compilation常用的钩子</strong></em></p>

























<table><thead><tr><th>Hook</th><th>type</th><th>调用</th></tr></thead><tbody><tr><td>buildModule</td><td>SyncHook</td><td>在模块构建开始之前触发。</td></tr><tr><td>finishModules</td><td>SyncHook</td><td>所有模块都完成构建。</td></tr><tr><td>optimize</td><td>SyncHook</td><td>优化阶段开始时触发。</td></tr></tbody></table>
<p>其他的就不做过多介绍了，附上官网的链接<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fapi%2Fcompiler-hooks%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/api/compiler-hooks/" ref="nofollow noopener noreferrer">webpack.docschina.org/api/compile…</a></p>
<hr>
<h1 data-id="heading-10">完成一个完整的Webpack Plugin</h1>
<p>Webpack 插件的名称都是叫xxx-webpack-plugin，Plugin demo就这样开始了。</p>
<h2 data-id="heading-11">Copyright-webpack-plugin</h2>
<p>这是一个简单的demo，通过plugin生成一个markdown文件，文件中输出'written by zhulm'</p>
<pre><code class="copyable">// plugin class
class CopyrightWebpackPlugin &#123;
  constructor () &#123;&#125;
  apply(compiler) &#123;
    // console.log('compiler: ', compiler);
    compiler.hooks.emit.tapAsync('CopyrightWebpackPlugin', 
      (compilation,cb) => &#123;
        // console.log('compilation: ', compilation);
        compilation.assets['copyright.md'] = &#123;
          source: function() &#123;
            return 'written by zhulm';
          &#125;,
          size: function() &#123;
            return 15;
          &#125;,
        &#125;
        cb()
      &#125;
    )
  &#125;
&#125;
module.exports = CopyrightWebpackPlugin;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码讲解：</p>
<ol>
<li>主要是运用单compiler的钩子的emit方法，使用这个方法创建一个copyright.md文件，写入文字。</li>
<li>tapAsync方法来调用钩子，需要转入两个参数，第一个参数是本身插件的名称，第二个参数是一个函数。</li>
</ol>

<ol start="3">
<li>source是源码文件，而size是生成文件的大小，返回 15 表示生成的文件大小是 15 byte。</li>
<li>assets: &#123; [pathname: string]: Source &#125; — 普通对象，其中 key 是 asset 的路径名，value 是 asset 的数据</li>
</ol>
<p>详情见我的github地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdakoujia%2Fwebpack-plugin-demos.git" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dakoujia/webpack-plugin-demos.git" ref="nofollow noopener noreferrer">github.com/dakoujia/we…</a></p>
<h2 data-id="heading-12">OutputCurrentBuildInfoPlugin</h2>
<p>这个插件是获取输出信息的一个插件，获取git的提交信息及时间</p>
<pre><code class="copyable">new OutputCurrentBuildInfoPlugin(&#123;
      outputName: 'build-log.json',
      dateFormatType: 'YYYY-MM-DD HH:mm:ss',
      buildType: 'local'
    &#125;),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成的build-log.json</p>
<pre><code class="copyable">// local
&#123;"build_time":"2021-07-04 20:28:20","build_type":"local","git":&#123;"currentBranch":"","build_user":&#123;"name":"zhulm","email":"liangming.zhu@foxmail.com"&#125;&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// git
&#123;"build_time":"2021-07-04 21:26:59","build_type":"git","git":&#123;"last_commit":&#123;"hash":"f94253ba4af5727f1b9bd48f9b0b225723d597a4","date":"2021-07-04T21:19:44+08:00","message":"docs(read me): README.md","refs":"HEAD -> main, origin/main, origin/HEAD","body":"提交人:朱良明\n","author_name":"zhulm","author_email":"liangming.zhu@foxmail.com"&#125;,"currentBranch":"main","build_user":&#123;"name":"zhulm","email":"liangming.zhu@foxmail.com"&#125;&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>详情见我的github地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdakoujia%2Fwebpack-plugin-demos.git" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dakoujia/webpack-plugin-demos.git" ref="nofollow noopener noreferrer">github.com/dakoujia/we…</a></p>
<h1 data-id="heading-13">遇到的问题</h1>
<h2 data-id="heading-14">1.构建的时候报错</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcac3ba4e7614badbef544fa459b8d59~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>webpack版本问题导致的，webpack5.0以上的版本会有这个问题，将版本降到4.16.5可以解决；</p>
<h1 data-id="heading-15">参考文献</h1>
<p>揭秘webpack plugin： <a href="https://juejin.cn/post/6844904048483631111" target="_blank" title="https://juejin.cn/post/6844904048483631111">juejin.cn/post/684490…</a></p>
<p>官网的plugin： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fplugins%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/plugins/" ref="nofollow noopener noreferrer">webpack.docschina.org/plugins/</a></p></div>  
</div>
            