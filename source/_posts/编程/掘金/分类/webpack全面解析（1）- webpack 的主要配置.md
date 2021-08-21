
---
title: 'webpack全面解析（1）- webpack 的主要配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/138724085dd44e2592bbde1ec57ef956~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 00:40:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/138724085dd44e2592bbde1ec57ef956~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/138724085dd44e2592bbde1ec57ef956~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>webpack</strong> 是一个用于现代 JavaScript 应用程序的 <em>静态模块打包工具</em>。当 webpack 处理应用程序时，它会在内部构建一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconcepts%2Fdependency-graph%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/concepts/dependency-graph/" ref="nofollow noopener noreferrer">依赖图(dependency graph)</a>，此依赖图对应映射到项目所需的每个模块，并生成一个或多个 <em>bundle</em>。</p>
</blockquote>
<p><strong>webpack</strong>作为现代前端打包最重要的工具之一，在前端开发应用中是必不可少的。虽然说工程化的项目中，比如 <code>react</code> 的 <code>cra</code>、 <code>VUE</code> 的 <code>cli</code> 以及其他的一些脚手架，都会将相关的配置给我们配置好，但是在大型的应用项目中，如果想要对自己的工程项目进行充分优化，那么对 <code>webpack</code> 的学习就是必不可少的了。</p>
<p>正如 lucasHC 的观点： <code>webpack</code> 工程师 是大于 前端开发工程师的。</p>
<p>同时，前端项目的工程化实现，也离不开 <code>webpack</code> 的参与。</p>
<p>本文将会结合 <code>webpack</code> 的官方文档，从如下几个角度依次带大家学习 <code>webpack</code>。</p>
<ol>
<li>webpack 的主要配置</li>
<li>学习 create-react-app 的 webpack 配置</li>
<li>webpack的主要API (loader & plugin)</li>
<li>如果去实现一个 loader</li>
<li>如果去实现一个 plugin</li>
<li>webpack 的源码解析</li>
<li>如何实现一个最小的 webpack 打包工具</li>
</ol>
<p>-- 值得说明的是，本项目使用的<code>webpack</code>版本为 <code>webpack ^5.x.x</code>。</p>
<h2 data-id="heading-0">WebPack 的主要配置</h2>
<p>这一部分的内容，其实在 webpack 的官方中文文档中阐述的比较清楚，下面我们就一起看一个普通项目的 webpack 配置。</p>
<h3 data-id="heading-1">1.  chunk | module | bundle?</h3>
<p>在说配置之前，需要先讲清楚这几个概念。</p>
<p>先来说说<code>chunk</code></p>
<p><code>chunk</code>: 此 <code>webpack</code> 特定术语在内部用于管理捆绑过程。输出束（<code>bundle</code>）由块组成，其中有几种类型（例如 <code>entry</code> 和 <code>child</code> ）。通常，<em>块</em> 直接与 <em>输出束</em> (<code>bundle</code>）相对应，但是，有些配置不会产生一对一的关系。</p>
<p>以上是官方给出的解释，我自认为写得太抽象了，有些人说，每有一个<code>entry</code>，就对应一个<code>chunk</code>，其实这种说法也不完全准确。</p>
<p>准确的说，<code>chunk</code>是<code>webpack</code>执行的中间文件。</p>
<p>而对应到<code>module</code>和<code>bundle</code>，可以说是 <code>webpack</code>的<strong>输入</strong>和<strong>输出</strong>。</p>
<p>比如：</p>
<p>我们写了一些<code>es6 module</code>的模块、一些<code>css</code>文件，以及一些静态资源  --<code>module</code></p>
<p>通过打包工具，从某个<code>entry</code>进行打包，在<code>webpack</code>内部就形成了一   个<code>chunk</code></p>
<p>最后我们通过例如 <code>MiniCssExtractPlugin</code>等插件，生成了一些 <code>xx.bundle.js</code>、<code>xx.bundle.css</code>文件。</p>
<h3 data-id="heading-2">2.  输入(entry) | 输出(output) | loader | 插件(plugins)</h3>
<h4 data-id="heading-3">2.1 entry</h4>
<p>entry 是一个 webpack 配置的入口文件，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">pageOne</span>: <span class="hljs-string">'./src/pageOne/index.js'</span>,
    <span class="hljs-attr">pageTwo</span>: <span class="hljs-string">'./src/pageTwo/index.js'</span>,
    <span class="hljs-attr">pageThree</span>: <span class="hljs-string">'./src/pageThree/index.js'</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里值得说明的有几点：</p>
<ul>
<li>
<p>当我们有多个应用入口，但是使用了相同的一些第三方库，比如 <code>echarts</code>、<code>react</code> 等，我们有两种方法去对<strong>共享的代码</strong>进行单独打包。</p>
<p>a. 使用 <code>optimization.splitChunks</code> 为页面间共享的应用程序代码创建 <code>bundle</code>。</p>
<p>b. 在<code>entry</code> 中使用 <code>dependOn</code> 来实现。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> entry: &#123;
    <span class="hljs-attr">shared</span>: [<span class="hljs-string">'echarts'</span>,<span class="hljs-string">'react'</span>,<span class="hljs-string">'react-dom'</span>],
    <span class="hljs-attr">catalog</span>: &#123;
        <span class="hljs-attr">import</span>: <span class="hljs-string">'./src/react/catalog.js'</span>,
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'./catalog.js'</span>,
        <span class="hljs-attr">dependOn</span>: <span class="hljs-string">'shared'</span>,
    &#125;,
    <span class="hljs-attr">personal</span>: &#123;
        <span class="hljs-attr">import</span>: <span class="hljs-string">'./src/react/personal.js'</span>,
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'./personal.js'</span>,
        <span class="hljs-attr">dependOn</span>: <span class="hljs-string">'shared'</span>,
    &#125;,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>必要的时候，我们亦可以在<code>entry</code>中指明输出文件的名称。</p>
</li>
<li>
<p>常见的代码分割有三种方式：</p>
<ul>
<li>在 <code>webpack</code> 配置的入口点 <code>entry</code> 中去进行分割；</li>
<li>使用 <code>SplitChunkPlugin</code> 进行分割；</li>
<li>在工程中使用 <code>import().then()</code>， 或者 <code>react</code> 的 <code>lazy</code>， <code>VUE</code> 的 <code>dynamicImport</code> 进行分割。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-4">2.2 output</h4>
<p>output</p>
<p>默认情况下，我们导出的是支持浏览器解析的版本。</p>
<p>output的 chunkFormat 、chunkLoading 等参数，是和 target 深度绑定的。（<em>详细内容可以参考 webpack/lib/defaults.js中的设置。</em>）</p>
<p>当然，这里也可以通过 chunkFormat 、chunkLoading 等设置，导出 node 等相关的版本。</p>
<p>关于 output 的配置还有很多，一般情况下我们在使用框架开发时，不太能用得到，这里只给出来一些比较简单的。</p>
<p>这里值得说明的有几点：</p>
<ul>
<li>
<p>hash | contenthash | chunkhash 这几者的区别</p>
<ul>
<li><strong>hash</strong>： 针对每一次单独打包时进行生成，所以不同的打包环境，生成的不同，不利于缓存。同时，对于多入口的文件，每一次打包的 hash 值是相同的。</li>
<li><strong>contenthash</strong>： 根据文件内容生成不同的 hash 值，改变文件内容时， hash 值会发生变化。</li>
<li><strong>chunkhash</strong>： 顾名思义，不同的 <code>chunk</code> ， 生成的 hash 值不同。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-5">2.3 loader</h4>
<p>loader 的配置在 module 选项中，这里关于 module 的其他选项我们暂不介绍，直接说说loader，即 module.rules</p>
<p>一个典型的 rule 的配置包括了 test 和 use 的配置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">module</span>:&#123;
        <span class="hljs-attr">rules</span>:[&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js/i</span>,
            use:[
                &#123;<span class="hljs-attr">loader</span> :<span class="hljs-string">"babel-loader"</span>&#125;
            ]
        &#125;]
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>loader 在使用时，我需要注意的是：</p>
<ul>
<li>必要时请声明 include 和 exclude，这样会减少 loader 的编译内容，从而提高打包的性能；</li>
<li>老生长谈的是，loader 是自右向左进行加载的，如对less文件的解析，可能的配置如下：<code>use: ["style-loader", "css-loader", "less-loader"],</code></li>
</ul>
<h4 data-id="heading-6">2.4 plugins</h4>
<p>整个的webpack是基于插件化实现的，如果我们尝试读过源码，可以发现，很多配置内的参数，在内部是通过一个个插件，在打包的不同阶段进行处理的。</p>
<p>关于插件的解释，我们在后面会详细给出。</p>
<h3 data-id="heading-7">3. resolve | library | optimization</h3>
<h4 data-id="heading-8">3.1 resolve</h4>
<p>resolve 作为解析模块，更多的是在我们进行工程项目开发时，可能会遇到的一些问题的处理。</p>
<p>如 alias 的使用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">resolve: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-attr">Utilities</span>: path.resolve(__dirname, <span class="hljs-string">'src/utilities/'</span>),
      <span class="hljs-attr">Templates</span>: path.resolve(__dirname, <span class="hljs-string">'src/templates/'</span>),
    &#125;,
  &#125;,
<span class="hljs-comment">// 在代码里，我们可以直接使用</span>
<span class="hljs-comment">// import Utilities/index.js 取代：</span>
<span class="hljs-comment">// import ../../src/utiluties/index.js</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如 extensions 的使用：</p>
<p>可以指定默认扩展名称的加载类型；</p>
<p>如 modules 的使用：
告诉 webpack 解析模块时应该搜索的目录，一般为 node_modules</p>
<p>值得说明的是：webpack 5 不再自动 polyfill Node.js 的核心模块，这意味着如果你在浏览器或类似的环境中运行的代码中使用它们，你必须从 NPM 中安装兼容的模块，并自己包含它们。</p>
<h4 data-id="heading-9">3.2 library</h4>
<p>library的配置应用于，当你想要打包一个库的时候。可以选择在 output 中去使用它。</p>
<p>这里指的说明的是<code>umd</code>规范。</p>
<p>当我们用这种规范去打包一个库的时候，可以通过多种方式去引用它。</p>
<p>比如：</p>
<ul>
<li>
<p><strong>CommonJS module require</strong>:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> webpackNumbers = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-numbers'</span>);
<span class="hljs-comment">// ...</span>
webpackNumbers.wordToNum(<span class="hljs-string">'Two'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>AMD module require</strong>:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span>([<span class="hljs-string">'webpackNumbers'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">webpackNumbers</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  webpackNumbers.wordToNum(<span class="hljs-string">'Two'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>script tag</strong>:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  ...
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://example.org/webpack-numbers.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// Global variable</span>
    webpackNumbers.wordToNum(<span class="hljs-string">'Five'</span>);
    <span class="hljs-comment">// Property in the window object</span>
    <span class="hljs-built_in">window</span>.webpackNumbers.wordToNum(<span class="hljs-string">'Five'</span>);
    <span class="hljs-comment">// ...</span>
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-10">3.3 optimization</h4>
<p>从名称上我们也能看得出来，这一部分的配置主要用于优化的工作。</p>
<p>我们最常用的几个地方如下：</p>
<h5 data-id="heading-11">minimize / minimizer</h5>
<p>这里主要是用于设置一些对代码压缩的工具和插件。</p>
<h5 data-id="heading-12">splitChunk 和 runtimeChunk</h5>
<p>这两个都是对一些代码做<code>chunk</code>上的拆分，笔者在学习的时候也常常搞混，这里我们举个例子，来详细地说明一下。</p>
<p>我们创建一个项目，在 ./src下增加一个react的文件夹，并建立如下几个文件：</p>
<pre><code class="hljs language-react copyable" lang="react">// ./src/react/app.js
import React, &#123; Component &#125; from 'react';
export default class app extends Component &#123;
    render() &#123;
        return (
            <div>
                this is a React app
            </div>
        )
    &#125;
&#125;

// ./src/react/index.js

import ReactDOM from 'react-dom';
import App from './app';
import React from 'react';
ReactDOM.render(<App />, document.getElementById('root'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们使用如下的配置进行打包，因为我的测试程序的<code>webpack.config.js</code>是自行编辑的，所以声明了执行目录：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>:<span class="hljs-string">"production"</span>,
    <span class="hljs-attr">context</span>: path.resolve(process.cwd()),
    <span class="hljs-attr">entry</span>: &#123; <span class="hljs-attr">app</span>: <span class="hljs-string">'./src/react/home.js'</span> &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">clean</span>:<span class="hljs-literal">true</span>,
        <span class="hljs-attr">path</span>:path.resolve(process.cwd(),<span class="hljs-string">'./dist04'</span>),
        <span class="hljs-attr">filename</span>:<span class="hljs-string">'[name].[chunkhash].js'</span>
    &#125;,
    <span class="hljs-attr">module</span>:&#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx)$/</span>,
            use: &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preset-env'</span>, <span class="hljs-string">'@babel/preset-react'</span>]
                    &#125;
                &#125;,

            <span class="hljs-attr">include</span>: path.resolve(process.cwd(), <span class="hljs-string">'./src/react'</span>),
            <span class="hljs-attr">exclude</span>: path.resolve(process.cwd(), <span class="hljs-string">'./node_modules/'</span>)
        &#125;]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们生成的文件如下：</p>
<p><code>app.bdeb74ac3557b6d6c47a.js</code>   <em>( 129KB )</em></p>
<p>很显然，这个129KB 的文件里，包含了 react 的相关的源码，那么我们先加一个 <code>runtimecHUNK</code> 的配置：</p>
<p><code>optimization:&#123; runtimeChunk:'single'&#125; </code></p>
<p>我们发现，打包完成了的内容中，多了一个：</p>
<p><code>runtime.ecfe325a56eb578bdcaf.js</code>  <em>(1KB)</em></p>
<p>这里其实是把 <code>app</code> 中的运行时函数给切分了出来。这里由于文件太单一，看不出来，我们再在 src/react下增加一个文件：</p>
<pre><code class="hljs language-react copyable" lang="react">// ./src/react/home.js

import ReactDOM from 'react-dom';
import App from './app';
import React from 'react';
ReactDOM.render(<App />, document.getElementById('root'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再在配置中增加：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">entry: &#123;
    <span class="hljs-attr">home</span>:<span class="hljs-string">'./src/react/index.js'</span>,
        <span class="hljs-attr">app</span>: <span class="hljs-string">'./src/react/home.js'</span>
&#125;,
<span class="hljs-attr">optimization</span>:&#123;
    <span class="hljs-attr">splitChunks</span> :&#123;
        <span class="hljs-attr">chunks</span>:<span class="hljs-string">'all'</span>
    &#125;,
    <span class="hljs-attr">runtimeChunk</span>:<span class="hljs-string">'multiple'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再看看打包后的结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/699be5e2cb8f4dd780a13fc4ada630a9~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们发现，<code>react</code>、<code>react-dom</code>等相关的第三方库，被打到了单独的文件中。</p>
<p>我们来总结一下：</p>
<ul>
<li>
<p><code>runtimeChunk</code>会根据配置内容是<code>multiple</code>还是<code>single</code>，对<code>runtime</code>相关的文件，打包单独的或共享的<code>chunk</code>；</p>
</li>
<li>
<p><code>splitChunks</code>中，会对多入口上共用的文件，打成单独的包。当然，在单一入口下，也会生成相应的内容。</p>
<p>当然，<code>splitChunks</code>作为一个老版本的独立插件，还是有很多强大的功能，如<code>cacheGroups</code>中的各种配置，对缓存的处理，都是值得我们去学习的。</p>
</li>
</ul>
<h3 data-id="heading-13">4. watch | devServer | middleware</h3>
<p>最后，我们来说说自动编译。</p>
<p>我们知道，在每次编译代码时，手动运行 <code>npm run build</code> 会显得很麻烦。</p>
<p>webpack 提供几种可选方式，帮助你在代码发生变化后自动编译代码：</p>
<ol>
<li>webpack's <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fwatch%2F%23watch" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/watch/#watch" ref="nofollow noopener noreferrer">Watch Mode</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack-dev-server" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/webpack-dev-server" ref="nofollow noopener noreferrer">webpack-dev-server</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack-dev-middleware" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/webpack-dev-middleware" ref="nofollow noopener noreferrer">webpack-dev-middleware</a></li>
</ol>
<p>多数场景中，你可能需要使用 <code>webpack-dev-server</code>，但是不妨探讨一下以上的所有选项。</p>
<h4 data-id="heading-14">4.1 watch 模式</h4>
<p>我们可以通过在配置中增加<code>&#123; watch: true &#125;</code>， 或者直接在脚本的运行中添加 <code>webpack -- watch</code>的方法启动 watch 模式。</p>
<p>值得注意的是，在这种模式下如果我们想要提高 watch 的效率，最好的办法是添加一些配置，让 watch 的内容缩减到最小：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">watchOptions</span>: &#123;
        <span class="hljs-attr">ignored</span>: [<span class="hljs-string">'**/node_modules'</span>, <span class="hljs-string">"**/files/**/*.js"</span>]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">4.2 webpack-dev-server</h4>
<p>第二种方式是使用 <code>webpack-dev-server</code>，也是目前 <code>React</code> 的脚手架中，使用的方法。</p>
<p>使用 webpack-dev-server 至少要满足两个条件：</p>
<ul>
<li>第一：添加一个 <code>html-webpack-plugin</code></li>
<li>第二：在<code>webpack</code>的命令中增加：<code>serve --open</code></li>
</ul>
<p>同时，你可以修改相关的配置，增加 <code>devServer: &#123; contentBase: './dist' , port:'8080'&#125;</code>等配置，但这不是必须的。</p>
<p>值得说明的是，我们也可以使用 <code>node.js</code>的方式进行执行：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> compiler = webpack(config);
<span class="hljs-keyword">const</span> devServer = <span class="hljs-keyword">new</span> WebpackDevServer(compiler, serverConfig);
devServer.listen(port, <span class="hljs-function">() =></span> &#123;
    
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式在 <code>react</code> 的 <code>cra</code> 中有详细的时候，后面我们可以进行讨论。</p>
<h4 data-id="heading-16">4.3 webpack-dev-middleware</h4>
<p>关于 <code>webpack-dev-middleware</code>也很简单，我们只需要启动一个<code>node-server</code>，即可以实现，这里不作详细讨论。</p>
<h3 data-id="heading-17">总结</h3>
<p>到了这里，关于 <code>webpack</code> 常用的一些配置就说完了。</p>
<p>当然还有很多更复杂的内容我们没有讲解，比如一些关于微前端、优化、缓存、lib库的内容，其实都是很重要的。</p>
<p>在后续的文章中，我们还会针对某一块的内容，做更详细的探讨。</p></div>  
</div>
            