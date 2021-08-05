
---
title: '多图详解，一次性搞懂Webpack Loader'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f15fb8403b4a8ca5347d8d1c898453~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 17:38:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f15fb8403b4a8ca5347d8d1c898453~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/" ref="nofollow noopener noreferrer">Webpack</a> 是一个模块化打包工具，它被广泛地应用在前端领域的大多数项目中。利用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/" ref="nofollow noopener noreferrer">Webpack</a> 我们不仅可以打包 JS 文件，还可以打包图片、CSS、字体等其他类型的资源文件。而支持打包非 JS 文件的特性是基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Floaders%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/loaders/" ref="nofollow noopener noreferrer">Loader</a> 机制来实现的。因此要学好 Webpack，我们就需要掌握 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Floaders%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/loaders/" ref="nofollow noopener noreferrer">Loader</a> 机制。本文阿宝哥将带大家一起深入学习 Webpack 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Floaders%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/loaders/" ref="nofollow noopener noreferrer">Loader</a> 机制，阅读完本文你将了解以下内容：</p>
<ul>
<li>Loader 的本质是什么？</li>
<li>Normal Loader 和 Pitching Loader 是什么？</li>
<li>Pitching Loader 的作用是什么？</li>
<li>Loader 是如何被加载的？</li>
<li>Loader 是如何被运行的？</li>
<li>多个 Loader 的执行顺序是什么？</li>
<li>Pitching Loader 的熔断机制是如何实现的？</li>
<li>Normal Loader 函数是如何被运行的？</li>
<li>Loader 对象上 <code>raw</code> 属性有什么作用？</li>
<li>Loader 函数体中的 <code>this.callback</code> 和 <code>this.async</code> 方法是哪里来的？</li>
<li>Loader 最终的返回结果是如何被处理的？</li>
</ul>
<h3 data-id="heading-0">一、Loader 的本质是什么？</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f15fb8403b4a8ca5347d8d1c898453~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由上图可知，Loader 本质上是导出函数的 JavaScript 模块。所导出的函数，可用于实现内容转换，该函数支持以下 3 个参数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string|Buffer&#125;</span> </span>content 源文件的内容
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;object&#125;</span> </span>[map] 可以被 https://github.com/mozilla/source-map 使用的 SourceMap 数据
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> </span>[meta] meta 数据，可以是任何内容
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">webpackLoader</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-comment">// 你的webpack loader代码</span>
&#125;
<span class="hljs-built_in">module</span>.exports = webpackLoader;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>了解完导出函数的签名之后，我们就可以定义一个简单的 <code>simpleLoader</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">simpleLoader</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是 SimpleLoader"</span>);
  <span class="hljs-keyword">return</span> content;
&#125;
<span class="hljs-built_in">module</span>.exports = simpleLoader;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上的 <code>simpleLoader</code> 并不会对输入的内容进行任何处理，只是在该 Loader 执行时输出相应的信息。Webpack 允许用户为某些资源文件配置多个不同的 Loader，比如在处理 <code>.css</code> 文件的时候，我们用到了 <code>style-loader</code> 和 <code>css-loader</code>，具体配置方式如下所示：</p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
     <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>,
     <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/i</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>],
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webpack 这样设计的好处，是可以保证每个 Loader 的职责单一。同时，也方便后期 Loader 的组合和扩展。比如，你想让 Webpack 能够处理 Scss 文件，你只需先安装 <code>sass-loader</code>，然后在配置 Scss 文件的处理规则时，设置 rule 对象的 <code>use</code> 属性为 <code>['style-loader', 'css-loader', 'sass-loader']</code> 即可。</p>
<h3 data-id="heading-1">二、Normal Loader 和 Pitching Loader 是什么？</h3>
<h4 data-id="heading-2">2.1 Normal Loader</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dc36aa6ac1948ec8fde5753500f3f95~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Loader 本质上是导出函数的 JavaScript 模块，而该模块导出的函数（若是 ES6 模块，则是默认导出的函数）就被称为 Normal Loader。<strong>需要注意的是，这里我们介绍的 Normal Loader 与 Webpack Loader 分类中定义的 Loader 是不一样的</strong>。在 Webpack 中，loader 可以被分为 4 类：pre 前置、post 后置、normal 普通和 inline 行内。其中 pre 和 post loader，可以通过 <code>rule</code> 对象的 <code>enforce</code> 属性来指定：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.txt$/i</span>,
        use: [<span class="hljs-string">"a-loader"</span>],
        <span class="hljs-attr">enforce</span>: <span class="hljs-string">"post"</span>, <span class="hljs-comment">// post loader</span>
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.txt$/i</span>,
        use: [<span class="hljs-string">"b-loader"</span>], <span class="hljs-comment">// normal loader</span>
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.txt$/i</span>,
        use: [<span class="hljs-string">"c-loader"</span>],
        <span class="hljs-attr">enforce</span>: <span class="hljs-string">"pre"</span>, <span class="hljs-comment">// pre loader</span>
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>了解完 Normal Loader 的概念之后，我们来动手写一下 Normal Loader。首先我们先来创建一个新的目录：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> mkdir webpack-loader-demo</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后进入该目录，使用 <code>npm init -y</code> 命令执行初始化操作。该命令成功执行后，会在当前目录生成一个 <code>package.json</code> 文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"webpack-loader-demo"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>
  &#125;,
  <span class="hljs-string">"keywords"</span>: [],
  <span class="hljs-string">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"license"</span>: <span class="hljs-string">"ISC"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：本地所使用的开发环境：Node v12.16.2；Npm 6.14.4；</p>
</blockquote>
<p>接着我们使用以下命令，安装一下 <code>webpack</code> 和 <code>webpack-cli</code> 依赖包：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> npm i webpack webpack-cli -D</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完项目依赖后，我们根据以下目录结构来添加对应的目录和文件：</p>
<pre><code class="hljs language-shell copyable" lang="shell">├── dist # 打包输出目录
│   └── index.html
├── loaders # loaders文件夹
│   ├── a-loader.js
│   ├── b-loader.js
│   └── c-loader.js
├── node_modules
├── package-lock.json
├── package.json
├── src # 源码目录
│   ├── data.txt # 数据文件
│   └── index.js # 入口文件
└── webpack.config.js # webpack配置文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>dist/index.html</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"zh-cn"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Webpack Loader 示例<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>Webpack Loader 示例<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"message"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./bundle.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>src/index.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Data <span class="hljs-keyword">from</span> <span class="hljs-string">"./data.txt"</span>

<span class="hljs-keyword">const</span> msgElement = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#message"</span>);
msgElement.innerText = Data;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>src/data.txt</strong></p>
<pre><code class="copyable">大家好，我是阿宝哥
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>loaders/a-loader.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">aLoader</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始执行aLoader Normal Loader"</span>);
  content += <span class="hljs-string">"aLoader]"</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`module.exports = '<span class="hljs-subst">$&#123;content&#125;</span>'`</span>;
&#125;

<span class="hljs-built_in">module</span>.exports = aLoader;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>aLoader</code> 函数中，我们会对 <code>content</code> 内容进行修改，然后返回 <code>module.exports = '$&#123;content&#125;'</code> 字符串。那么为什么要把 <code>content</code> 赋值给 <code>module.exports</code> 属性呢？这里我们先不解释具体的原因，后面我们再来分析这个问题。</p>
<p><strong>loaders/b-loader.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bLoader</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始执行bLoader Normal Loader"</span>);
  <span class="hljs-keyword">return</span> content + <span class="hljs-string">"bLoader->"</span>;
&#125;

<span class="hljs-built_in">module</span>.exports = bLoader;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>loaders/c-loader.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cLoader</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始执行cLoader Normal Loader"</span>);
  <span class="hljs-keyword">return</span> content + <span class="hljs-string">"[cLoader->"</span>;
&#125;

<span class="hljs-built_in">module</span>.exports = cLoader;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <strong>loaders</strong> 目录下，我们定义了以上 3 个 <strong>Normal Loader</strong>。这些 Loader 的实现都比较简单，只是在 Loader 执行时往 <code>content</code> 参数上添加当前 Loader 的相关信息。为了让 Webpack 能够识别 <strong>loaders</strong> 目录下的自定义 Loader，我们还需要在 Webpack 的配置文件中，设置 <code>resolveLoader</code> 属性，具体的配置方式如下所示：</p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">"./src/index.js"</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">"bundle.js"</span>,
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">"dist"</span>),
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.txt$/i</span>,
        use: [<span class="hljs-string">"a-loader"</span>, <span class="hljs-string">"b-loader"</span>, <span class="hljs-string">"c-loader"</span>],
      &#125;,
    ],
  &#125;,
  <span class="hljs-attr">resolveLoader</span>: &#123;
    <span class="hljs-attr">modules</span>: [
      path.resolve(__dirname, <span class="hljs-string">"node_modules"</span>),
      path.resolve(__dirname, <span class="hljs-string">"loaders"</span>),
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当目录更新完成后，在 <strong>webpack-loader-demo</strong> 项目的根目录下运行 <code>npx webpack</code> 命令就可以开始打包了。以下内容是阿宝哥运行 <code>npx webpack</code> 命令之后，控制台的输出结果：</p>
<pre><code class="hljs language-shell copyable" lang="shell">开始执行cLoader Normal Loader
开始执行bLoader Normal Loader
开始执行aLoader Normal Loader
asset bundle.js 4.55 KiB [emitted] (name: main)
runtime modules 937 bytes 4 modules
cacheable modules 187 bytes
  ./src/index.js 114 bytes [built] [code generated]
  ./src/data.txt 73 bytes [built] [code generated]
webpack 5.45.1 compiled successfully in 99 ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过观察以上的输出结果，我们可以知道 Normal Loader 的执行顺序是从右到左。此外，当打包完成后，我们在浏览器中打开 <strong>dist/index.html</strong> 文件，在页面上你将看到以下信息：</p>
<pre><code class="copyable">Webpack Loader 示例
大家好，我是阿宝哥[cLoader->bLoader->aLoader]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由页面上的输出信息 <strong>”大家好，我是阿宝哥[cLoader->bLoader->aLoader]“</strong> 可知，Loader 在执行的过程中是以管道的形式，对数据进行处理，具体处理过程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14e63a3942864f97b01537fce79ec8fa~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在你已经知道什么是 Normal Loader 及 Normal Loader 的执行顺序，接下来我们来介绍另一种 Loader —— <strong>Pitching Loader</strong>。</p>
<h4 data-id="heading-3">2.2 Pitching Loader</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f65ecbc34c044009959fdd4881f39f5~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在开发 Loader 时，我们可以在导出的函数上添加一个 <code>pitch</code> 属性，它的值也是一个函数。该函数被称为 <strong>Pitching Loader</strong>，它支持 3 个参数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@remainingRequest </span>剩余请求
 * <span class="hljs-doctag">@precedingRequest </span>前置请求
 * <span class="hljs-doctag">@data </span>数据对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">remainingRequest, precedingRequest, data</span>) </span>&#123;
 <span class="hljs-comment">// some code</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>data</code> 参数，可以用于数据传递。即在 <code>pitch</code> 函数中往 <code>data</code> 对象上添加数据，之后在 <code>normal</code> 函数中通过 <code>this.data</code> 的方式读取已添加的数据。 而 <code>remainingRequest</code> 和 <code>precedingRequest</code> 参数到底是什么？这里我们先来更新一下 <code>a-loader.js</code> 文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">aLoader</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-comment">// 省略部分代码</span>
&#125;

aLoader.pitch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">remainingRequest, precedingRequest, data</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始执行aLoader Pitching Loader"</span>);
  <span class="hljs-built_in">console</span>.log(remainingRequest, precedingRequest, data)
&#125;;

<span class="hljs-built_in">module</span>.exports = aLoader;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，我们为 aLoader 函数增加了一个 <code>pitch</code> 属性并设置它的值为一个函数对象。在函数体中，我们输出了该函数所接收的参数。接着，我们以同样的方式更新 <code>b-loader.js</code> 和 <code>c-loader.js</code> 文件：</p>
<p><strong>b-loader.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bLoader</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-comment">// 省略部分代码</span>
&#125;

bLoader.pitch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">remainingRequest, precedingRequest, data</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始执行bLoader Pitching Loader"</span>);
  <span class="hljs-built_in">console</span>.log(remainingRequest, precedingRequest, data);
&#125;;

<span class="hljs-built_in">module</span>.exports = bLoader;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>c-loader.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cLoader</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-comment">// 省略部分代码</span>
&#125;

cLoader.pitch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">remainingRequest, precedingRequest, data</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始执行cLoader Pitching Loader"</span>);
  <span class="hljs-built_in">console</span>.log(remainingRequest, precedingRequest, data);
&#125;;

<span class="hljs-built_in">module</span>.exports = cLoader;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当所有文件都更新完成后，我们在 <strong>webpack-loader-demo</strong> 项目的根目录再次执行 <code>npx webpack</code> 命令后，就会输出相应的信息。这里我们以 <code>b-loader.js</code> 的 <code>pitch</code> 函数的输出结果为例，来分析一下 <code>remainingRequest</code> 和 <code>precedingRequest</code> 参数的输出结果：</p>
<pre><code class="copyable">/Users/fer/webpack-loader-demo/loaders/c-loader.js!/Users/fer/webpack-loader-demo/src/data.txt #剩余请求
/Users/fer/webpack-loader-demo/loaders/a-loader.js #前置请求
&#123;&#125; #空的数据对象
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了以上的输出信息之外，我们还可以很清楚的看到 <strong>Pitching Loader</strong> 和 <strong>Normal Loader</strong> 的执行顺序：</p>
<pre><code class="hljs language-shell copyable" lang="shell">开始执行aLoader Pitching Loader
...
开始执行bLoader Pitching Loader
...
开始执行cLoader Pitching Loader
...
开始执行cLoader Normal Loader
开始执行bLoader Normal Loader
开始执行aLoader Normal Loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显对于我们的示例来说，<strong>Pitching Loader</strong> 的执行顺序是 <strong>从左到右</strong>，而 <strong>Normal Loader</strong> 的执行顺序是 <strong>从右到左</strong>。具体的执行过程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb407a1daffa4d8cae2cd0fa00f819c3~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>提示：Webpack 内部会使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">loader-runner</a> 这个库来运行已配置的 loaders。</p>
</blockquote>
<p>看到这里有的小伙伴可能会有疑问，<strong>Pitching Loader</strong> 除了可以提前运行之外，还有什么作用呢？其实当某个 <strong>Pitching Loader</strong> 返回非 <code>undefined</code> 值时，就会实现熔断效果。这里我们更新一下 <code>bLoader.pitch</code> 方法，让它返回 <code>"bLoader Pitching Loader->"</code> 字符串：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">bLoader.pitch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">remainingRequest, precedingRequest, data</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始执行bLoader Pitching Loader"</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-string">"bLoader Pitching Loader->"</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当更新完 <code>bLoader.pitch</code> 方法，我们再次执行 <code>npx webpack</code> 命令之后，控制台会输出以下内容：</p>
<pre><code class="hljs language-shell copyable" lang="shell">开始执行aLoader Pitching Loader
开始执行bLoader Pitching Loader
开始执行aLoader Normal Loader
asset bundle.js 4.53 KiB [compared for emit] (name: main)
runtime modules 937 bytes 4 modules
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上输出结果可知，当 <code>bLoader.pitch</code> 方法返回非 <code>undefined</code> 值时，跳过了剩下的 loader。具体执行流程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1686bed630924ec7868acf4dcaae3db3~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>提示：Webpack 内部会使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">loader-runner</a> 这个库来运行已配置的 loaders。</p>
</blockquote>
<p>之后，我们在浏览器中再次打开 <strong>dist/index.html</strong> 文件。此时，在页面上你将看到以下信息：</p>
<pre><code class="hljs language-html copyable" lang="html">Webpack Loader 示例
bLoader Pitching Loader->aLoader]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>介绍完 Normal Loader 和 Pitching Loader 的相关知识，接下来我们来分析一下 Loader 是如何被运行的。</p>
<h3 data-id="heading-4">三、Loader 是如何被运行的？</h3>
<p>要搞清楚 Loader 是如何被运行的，我们可以借助断点调试工具来找出 Loader 的运行入口。这里我们以大家熟悉的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://code.visualstudio.com/" ref="nofollow noopener noreferrer">Visual Studio Code</a> 为例，来介绍如何配置断点调试环境：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae53a2653c7e43799c9802a100886a37~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当你按照上述步骤操作之后，在当前项目（webpack-loader-demo）下，会自动创建 <strong>.vscode</strong> 目录并在该目录下自动生成一个 <strong>launch.json</strong> 文件。接着，我们复制以下内容直接替换 <strong>launch.json</strong> 中的原始内容。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.2.0"</span>,
    <span class="hljs-attr">"configurations"</span>: [&#123;
       <span class="hljs-attr">"type"</span>: <span class="hljs-string">"node"</span>,
       <span class="hljs-attr">"request"</span>: <span class="hljs-string">"launch"</span>,
       <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Webpack Debug"</span>,
       <span class="hljs-attr">"cwd"</span>: <span class="hljs-string">"$&#123;workspaceFolder&#125;"</span>,
       <span class="hljs-attr">"runtimeExecutable"</span>: <span class="hljs-string">"npm"</span>,
       <span class="hljs-attr">"runtimeArgs"</span>: [<span class="hljs-string">"run"</span>, <span class="hljs-string">"debug"</span>],
       <span class="hljs-attr">"port"</span>: <span class="hljs-number">5858</span>
    &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用以上配置信息，我们创建了一个 <strong>Webpack Debug</strong> 的调试任务。当运行该任务的时候，会在当前工作目录下执行 <code>npm run debug</code> 命令。因此，接下来我们需要在 <strong>package.json</strong> 文件中增加 <strong>debug</strong> 命令，具体内容如下所示：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
&#123;  
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"debug"</span>: <span class="hljs-string">"node --inspect=5858 ./node_modules/.bin/webpack"</span>
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>做好上述的准备之后，我们就可以在 <strong>a-loader</strong> 的 <code>pitch</code> 函数中添加一个断点。对应的调用堆栈如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ac317f33710488ba06c52b1a4cd47cc~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过观察以上的调用堆栈信息，我们可以看到调用 <code>runLoaders</code> 方法，该方法是来自于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">loader-runner</a> 模块。所以要搞清楚 Loader 是如何被运行的，我们就需要分析 <code>runLoaders</code> 方法。下面我们来开始分析项目中使用的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">loader-runner</a> 模块，它的版本是 <strong>4.2.0</strong>。其中 <code>runLoaders</code> 方法被定义在 <code>lib/LoaderRunner.js</code> 文件中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/LoaderRunner.js</span>
<span class="hljs-built_in">exports</span>.runLoaders = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runLoaders</span>(<span class="hljs-params">options, callback</span>) </span>&#123;
  <span class="hljs-comment">// read options</span>
<span class="hljs-keyword">var</span> resource = options.resource || <span class="hljs-string">""</span>;
<span class="hljs-keyword">var</span> loaders = options.loaders || [];
<span class="hljs-keyword">var</span> loaderContext = options.context || &#123;&#125;; <span class="hljs-comment">// Loader上下文对象</span>
<span class="hljs-keyword">var</span> processResource = options.processResource || 
        (<span class="hljs-function">(<span class="hljs-params">readResource, context, resource, callback</span>) =></span> &#123;
context.addDependency(resource);
readResource(resource, callback);
&#125;).bind(<span class="hljs-literal">null</span>, options.readResource || readFile);

<span class="hljs-comment">// prepare loader objects</span>
loaders = loaders.map(createLoaderObject);
        loaderContext.context = contextDirectory;
loaderContext.loaderIndex = <span class="hljs-number">0</span>;
loaderContext.loaders = loaders;
  
        <span class="hljs-comment">// 省略大部分代码</span>
<span class="hljs-keyword">var</span> processOptions = &#123;
  <span class="hljs-attr">resourceBuffer</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">processResource</span>: processResource
&#125;;
       <span class="hljs-comment">// 迭代PitchingLoaders</span>
iteratePitchingLoaders(processOptions, loaderContext, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, result</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上代码可知，在 <code>runLoaders</code> 函数中，会先从 <code>options</code> 配置对象上获取 <code>loaders</code> 信息，然后调用 <code>createLoaderObject</code> 函数创建 Loader 对象，调用该方法后会返回包含 <code>normal</code>、<code>pitch</code>、<code>raw</code> 和 <code>data</code> 等属性的对象。目前该对象的大多数属性值都为 <code>null</code>，在后续的处理流程中，就会填充相应的属性值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/LoaderRunner.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createLoaderObject</span>(<span class="hljs-params">loader</span>) </span>&#123;
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">path</span>: <span class="hljs-literal">null</span>,
          <span class="hljs-attr">query</span>: <span class="hljs-literal">null</span>, 
          <span class="hljs-attr">fragment</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">options</span>: <span class="hljs-literal">null</span>, 
          <span class="hljs-attr">ident</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">normal</span>: <span class="hljs-literal">null</span>, 
          <span class="hljs-attr">pitch</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">raw</span>: <span class="hljs-literal">null</span>, 
          <span class="hljs-attr">data</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">pitchExecuted</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">normalExecuted</span>: <span class="hljs-literal">false</span>
&#125;;
<span class="hljs-comment">// 省略部分代码</span>
obj.request = loader;
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">Object</span>.preventExtensions) &#123;
  <span class="hljs-built_in">Object</span>.preventExtensions(obj);
&#125;
<span class="hljs-keyword">return</span> obj;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在创建完 Loader 对象及初始化 loaderContext 对象之后，就会调用 <code>iteratePitchingLoaders</code> 函数开始迭代 Pitching Loader。为了让大家对后续的处理流程有一个大致的了解，在看具体代码前，我们再来回顾一下前面运行 <strong>txt loaders</strong> 的调用堆栈：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b13f00876c14ecaae5ac94789d6919f~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>与之对应 <code>runLoaders</code> 函数的 <code>options</code> 对象结构如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28b559a87e934bbbbfd2e7cfb7366d96~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>基于上述的调用堆栈和相关的源码，阿宝哥也画了一张相应的流程图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4b3ae00bbea49869d7cad8e54c47acd~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看完上面的流程图和调用堆栈图，接下来我们来分析一下流程图中相关函数的核心代码。这里我们先来分析 <code>iteratePitchingLoaders</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/LoaderRunner.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">iteratePitchingLoaders</span>(<span class="hljs-params">options, loaderContext, callback</span>) </span>&#123;
<span class="hljs-comment">// abort after last loader</span>
<span class="hljs-keyword">if</span>(loaderContext.loaderIndex >= loaderContext.loaders.length)
        <span class="hljs-comment">// 在processResource函数内，会调用iterateNormalLoaders函数</span>
        <span class="hljs-comment">// 开始执行normal loader</span>
<span class="hljs-keyword">return</span> processResource(options, loaderContext, callback);

        <span class="hljs-comment">// 首次执行时，loaderContext.loaderIndex的值为0</span>
<span class="hljs-keyword">var</span> currentLoaderObject =  
         loaderContext.loaders[loaderContext.loaderIndex];

<span class="hljs-comment">// 如果当前loader对象的pitch函数已经被执行过了，则执行下一个loader的pitch函数</span>
<span class="hljs-keyword">if</span>(currentLoaderObject.pitchExecuted) &#123;
   loaderContext.loaderIndex++;
   <span class="hljs-keyword">return</span> iteratePitchingLoaders(options, loaderContext, callback);
&#125;

<span class="hljs-comment">// 加载loader模块</span>
loadLoader(currentLoaderObject, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
           <span class="hljs-keyword">if</span>(err) &#123;
       loaderContext.cacheable(<span class="hljs-literal">false</span>);
       <span class="hljs-keyword">return</span> callback(err);
    &#125;
           <span class="hljs-comment">// 获取当前loader对象上的pitch函数</span>
   <span class="hljs-keyword">var</span> fn = currentLoaderObject.pitch;
           <span class="hljs-comment">// 标识loader对象已经被iteratePitchingLoaders函数处理过</span>
   currentLoaderObject.pitchExecuted = <span class="hljs-literal">true</span>;
   <span class="hljs-keyword">if</span>(!fn) <span class="hljs-keyword">return</span> iteratePitchingLoaders(options, loaderContext, 
             callback);

           <span class="hljs-comment">// 开始执行pitch函数</span>
   runSyncOrAsync(fn,loaderContext, ...);
   <span class="hljs-comment">// 省略部分代码</span>
       &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>iteratePitchingLoaders</code> 函数内部，会从最左边的 loader 对象开始处理，然后调用 <code>loadLoader</code> 函数开始加载 loader 模块。在 <code>loadLoader</code> 函数内部，会根据 <code>loader</code> 的类型，使用不同的加载方式。对于我们当前的项目来说，会通过 <code>require(loader.path)</code> 的方式来加载 loader 模块。具体的代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/loadLoader.js</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadLoader</span>(<span class="hljs-params">loader, callback</span>) </span>&#123;
<span class="hljs-keyword">if</span>(loader.type === <span class="hljs-string">"module"</span>) &#123;
  <span class="hljs-keyword">try</span> &#123;
           <span class="hljs-keyword">if</span>(url === <span class="hljs-literal">undefined</span>) url = <span class="hljs-built_in">require</span>(<span class="hljs-string">"url"</span>);
   <span class="hljs-keyword">var</span> loaderUrl = url.pathToFileURL(loader.path);
   <span class="hljs-keyword">var</span> modulePromise = <span class="hljs-built_in">eval</span>(<span class="hljs-string">"import("</span> + 
             <span class="hljs-built_in">JSON</span>.stringify(loaderUrl.toString()) + <span class="hljs-string">")"</span>);
   modulePromise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span></span>) </span>&#123;
     handleResult(loader, <span class="hljs-built_in">module</span>, callback);
   &#125;, callback);
   <span class="hljs-keyword">return</span>;
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
    callback(e);
 &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">var</span> <span class="hljs-built_in">module</span> = <span class="hljs-built_in">require</span>(loader.path);
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
    <span class="hljs-comment">// 省略相关代码</span>
  &#125;
        <span class="hljs-comment">// 处理已加载的模块</span>
 <span class="hljs-keyword">return</span> handleResult(loader, <span class="hljs-built_in">module</span>, callback);
   &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不管使用哪种加载方式，在成功加载 <code>loader</code> 模块之后，都会调用 <code>handleResult</code> 函数来处理已加载的模块。该函数的作用是，获取模块中的导出函数及该函数上 <code>pitch</code> 和 <code>raw</code> 属性的值并赋值给对应 <code>loader</code> 对象的相应属性：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/loadLoader.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleResult</span>(<span class="hljs-params">loader, <span class="hljs-built_in">module</span>, callback</span>) </span>&#123;
<span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">module</span> !== <span class="hljs-string">"function"</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">module</span> !== <span class="hljs-string">"object"</span>) &#123;
  <span class="hljs-keyword">return</span> callback(<span class="hljs-keyword">new</span> LoaderLoadingError(
    <span class="hljs-string">"Module '"</span> + loader.path + <span class="hljs-string">"' is not a loader (export function or es6 module)"</span>
  ));
&#125;
loader.normal = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">module</span> === <span class="hljs-string">"function"</span> ? <span class="hljs-built_in">module</span> : <span class="hljs-built_in">module</span>.default;
loader.pitch = <span class="hljs-built_in">module</span>.pitch;
loader.raw = <span class="hljs-built_in">module</span>.raw;
<span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> loader.normal !== <span class="hljs-string">"function"</span> && <span class="hljs-keyword">typeof</span> loader.pitch !== <span class="hljs-string">"function"</span>) &#123;
<span class="hljs-keyword">return</span> callback(<span class="hljs-keyword">new</span> LoaderLoadingError(
<span class="hljs-string">"Module '"</span> + loader.path + <span class="hljs-string">"' is not a loader (must have normal or pitch function)"</span>
));
&#125;
callback();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在处理完已加载的 <code>loader</code> 模块之后，就会继续调用传入的 <code>callback</code> 回调函数。在该回调函数内，会先在当前的 <code>loader</code> 对象上获取 <code>pitch</code> 函数，然后调用 <code>runSyncOrAsync</code> 函数来执行 <code>pitch</code> 函数。对于我们的项目来说，就会开始执行 <code>aLoader.pitch</code> 函数。</p>
<p>看到这里的小伙伴，应该已经知道 loader 模块是如何被加载的及 loader 模块中定义的 pitch 函数是如何被运行的。由于篇幅有限，阿宝哥就不再详细展开介绍 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">loader-runner</a> 模块中其他函数。接下来，我们将通过几个问题来继续分析 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">loader-runner</a> 模块所提供的功能。</p>
<h3 data-id="heading-5">四、Pitching Loader 的熔断机制是如何实现的？</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/LoaderRunner.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">iteratePitchingLoaders</span>(<span class="hljs-params">options, loaderContext, callback</span>) </span>&#123;
<span class="hljs-comment">// 省略部分代码</span>
loadLoader(currentLoaderObject, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
<span class="hljs-keyword">var</span> fn = currentLoaderObject.pitch;
        <span class="hljs-comment">// 标识当前loader已经被处理过</span>
currentLoaderObject.pitchExecuted = <span class="hljs-literal">true</span>;
        <span class="hljs-comment">// 若当前loader对象上未定义pitch函数，则处理下一个loader对象</span>
<span class="hljs-keyword">if</span>(!fn) <span class="hljs-keyword">return</span> iteratePitchingLoaders(options, loaderContext, 
            callback);

        <span class="hljs-comment">// 执行loader模块中定义的pitch函数</span>
runSyncOrAsync(
  fn, loaderContext, [loaderContext.remainingRequest, 
          loaderContext.previousRequest, currentLoaderObject.data = &#123;&#125;],
   <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
     <span class="hljs-keyword">if</span>(err) <span class="hljs-keyword">return</span> callback(err);
      <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>);
      <span class="hljs-keyword">var</span> hasArg = args.some(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
<span class="hljs-keyword">return</span> value !== <span class="hljs-literal">undefined</span>;
      &#125;);
      <span class="hljs-keyword">if</span>(hasArg) &#123;
loaderContext.loaderIndex--;
iterateNormalLoaders(options, loaderContext, args, callback);
       &#125; <span class="hljs-keyword">else</span> &#123;
iteratePitchingLoaders(options, loaderContext, callback);
       &#125;
    &#125;
  );
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，<code>runSyncOrAsync</code> 函数的回调函数内部，会根据当前 <code>loader</code> 对象 <code>pitch</code> 函数的返回值是否为 <code>undefined</code> 来执行不同的处理逻辑。如果 <code>pitch</code> 函数返回了非 <code>undefined</code> 的值，则会出现熔断。即跳过后续的执行流程，开始执行上一个 <code>loader</code> 对象上的 <strong>normal loader</strong> 函数。具体的实现方式也很简单，就是 <code>loaderIndex</code> 的值减 1，然后调用 <code>iterateNormalLoaders</code> 函数来实现。而如果 <code>pitch</code> 函数返回 <code>undefined</code>，则继续调用 <code>iteratePitchingLoaders</code> 函数来处理下一个未处理 <code>loader</code> 对象。</p>
<h3 data-id="heading-6">五、Normal Loader 函数是如何被运行的？</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/LoaderRunner.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">iterateNormalLoaders</span>(<span class="hljs-params">options, loaderContext, args, callback</span>) </span>&#123;
<span class="hljs-keyword">if</span>(loaderContext.loaderIndex < <span class="hljs-number">0</span>)
<span class="hljs-keyword">return</span> callback(<span class="hljs-literal">null</span>, args);

<span class="hljs-keyword">var</span> currentLoaderObject = loaderContext.loaders[loaderContext.loaderIndex];

<span class="hljs-comment">// normal loader的执行顺序是从右到左</span>
<span class="hljs-keyword">if</span>(currentLoaderObject.normalExecuted) &#123;
loaderContext.loaderIndex--;
<span class="hljs-keyword">return</span> iterateNormalLoaders(options, loaderContext, args, callback);
&#125;

        <span class="hljs-comment">// 获取当前loader对象上的normal函数</span>
<span class="hljs-keyword">var</span> fn = currentLoaderObject.normal;
        <span class="hljs-comment">// 标识loader对象已经被iterateNormalLoaders函数处理过</span>
currentLoaderObject.normalExecuted = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">if</span>(!fn) &#123; <span class="hljs-comment">// 当前loader对象未定义normal函数，则继续处理前一个loader对象</span>
   <span class="hljs-keyword">return</span> iterateNormalLoaders(options, loaderContext, args, callback);
&#125;

convertArgs(args, currentLoaderObject.raw);

runSyncOrAsync(fn, loaderContext, args, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(err) <span class="hljs-keyword">return</span> callback(err);

  <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>);
  iterateNormalLoaders(options, loaderContext, args, callback);
&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上代码可知，在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">loader-runner</a> 模块内部会通过调用 <code>iterateNormalLoaders</code> 函数，来执行已加载 <code>loader</code> 对象上的 <strong>normal loader</strong> 函数。与 <code>iteratePitchingLoaders</code> 函数一样，在 <code>iterateNormalLoaders</code> 函数内部也是通过调用 <code>runSyncOrAsync</code> 函数来执行 <code>fn</code> 函数。不过在调用 <strong>normal loader</strong> 函数前，会先调用 <code>convertArgs</code> 函数对参数进行处理。</p>
<p><code>convertArgs</code> 函数会根据 <code>raw</code> 属性来对 args[0]（文件的内容）进行处理，该函数的具体实现如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/LoaderRunner.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convertArgs</span>(<span class="hljs-params">args, raw</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(!raw && Buffer.isBuffer(args[<span class="hljs-number">0</span>]))
      args[<span class="hljs-number">0</span>] = utf8BufferToString(args[<span class="hljs-number">0</span>]);
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(raw && <span class="hljs-keyword">typeof</span> args[<span class="hljs-number">0</span>] === <span class="hljs-string">"string"</span>)
      args[<span class="hljs-number">0</span>] = Buffer.from(args[<span class="hljs-number">0</span>], <span class="hljs-string">"utf-8"</span>);
&#125;

<span class="hljs-comment">// 把buffer对象转换为utf-8格式的字符串</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">utf8BufferToString</span>(<span class="hljs-params">buf</span>) </span>&#123;
  <span class="hljs-keyword">var</span> str = buf.toString(<span class="hljs-string">"utf-8"</span>);
  <span class="hljs-keyword">if</span>(str.charCodeAt(<span class="hljs-number">0</span>) === <span class="hljs-number">0xFEFF</span>) &#123;
     <span class="hljs-keyword">return</span> str.substr(<span class="hljs-number">1</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
     <span class="hljs-keyword">return</span> str;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信看完 <code>convertArgs</code> 函数的相关代码之后，你对 <code>raw</code> 属性的作用有了更深刻的了解。</p>
<h3 data-id="heading-7">六、Loader 函数体中的 this.callback 和 this.async 方法是哪里来的？</h3>
<p>Loader 可以分为同步 Loader 和异步 Loader，对于同步 Loader 来说，我们可以通过 <code>return</code> 语句或 <code>this.callback</code> 的方式来同步地返回转换后的结果。只是相比 <code>return</code> 语句，<code>this.callback</code> 方法则更灵活，因为它允许传递多个参数。</p>
<p><strong>sync-loader.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
  <span class="hljs-keyword">return</span> source + <span class="hljs-string">"-simple"</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>sync-loader-with-multiple-results.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source, map, meta</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.callback(<span class="hljs-literal">null</span>, source + <span class="hljs-string">"-simple"</span>, map, meta);
  <span class="hljs-keyword">return</span>; <span class="hljs-comment">// 当调用 callback() 函数时，总是返回 undefined</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是 <code>this.callback</code> 方法支持 4 个参数，每个参数的具体作用如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.callback(
  err: <span class="hljs-built_in">Error</span> | <span class="hljs-literal">null</span>,    <span class="hljs-comment">// 错误信息</span>
  <span class="hljs-attr">content</span>: string | Buffer,    <span class="hljs-comment">// content信息</span>
  sourceMap?: SourceMap,    <span class="hljs-comment">// sourceMap</span>
  meta?: any    <span class="hljs-comment">// 会被 webpack 忽略，可以是任何东西</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而对于异步 loader，我们需要调用 <code>this.async</code> 方法来获取 <code>callback</code> 函数：</p>
<p><strong>async-loader.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
   <span class="hljs-keyword">var</span> callback = <span class="hljs-built_in">this</span>.async();
   <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
     callback(<span class="hljs-literal">null</span>, source + <span class="hljs-string">"-async-simple"</span>);
   &#125;, <span class="hljs-number">50</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么以上示例中，<code>this.callback</code> 和 <code>this.async</code> 方法是哪里来的呢？带着这个问题，我们来从 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">loader-runner</a> 模块的源码中，一探究竟。</p>
<p><strong>this.async</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/LoaderRunner.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runSyncOrAsync</span>(<span class="hljs-params">fn, context, args, callback</span>) </span>&#123;
<span class="hljs-keyword">var</span> isSync = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 默认是同步类型</span>
<span class="hljs-keyword">var</span> isDone = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 是否已完成</span>
<span class="hljs-keyword">var</span> isError = <span class="hljs-literal">false</span>; <span class="hljs-comment">// internal error</span>
<span class="hljs-keyword">var</span> reportedError = <span class="hljs-literal">false</span>;
  
context.async = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span>(isDone) &#123;
    <span class="hljs-keyword">if</span>(reportedError) <span class="hljs-keyword">return</span>; <span class="hljs-comment">// ignore</span>
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"async(): The callback was already called."</span>);
  &#125;
  isSync = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">return</span> innerCallback;
&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在前面我们已经介绍过 <code>runSyncOrAsync</code> 函数的作用，该函数用于执行 Loader 模块中设置的 <strong>Normal Loader</strong> 或 <strong>Pitching Loader</strong> 函数。在 <code>runSyncOrAsync</code> 函数内部，最终会通过 <code>fn.apply(context, args)</code> 的方式调用 Loader 函数。即会通过 <code>apply</code> 方法设置 Loader 函数的执行上下文。</p>
<p>此外，由以上代码可知，当调用 <code>this.async</code> 方法之后，会先设置 <code>isSync</code> 的值为 <code>false</code>，然后返回 <code>innerCallback</code> 函数。其实该函数与 <code>this.callback</code> 都是指向同一个函数。</p>
<p><strong>this.callback</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/LoaderRunner.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runSyncOrAsync</span>(<span class="hljs-params">fn, context, args, callback</span>) </span>&#123;
        <span class="hljs-comment">// 省略部分代码</span>
<span class="hljs-keyword">var</span> innerCallback = context.callback = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span>(isDone) &#123;
    <span class="hljs-keyword">if</span>(reportedError) <span class="hljs-keyword">return</span>; <span class="hljs-comment">// ignore</span>
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"callback(): The callback was already called."</span>);
  &#125;
  isDone = <span class="hljs-literal">true</span>;
  isSync = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">try</span> &#123;
    callback.apply(<span class="hljs-literal">null</span>, <span class="hljs-built_in">arguments</span>);
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
    isError = <span class="hljs-literal">true</span>;
    <span class="hljs-keyword">throw</span> e;
  &#125;
   &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在 Loader 函数中，是通过 <code>return</code> 语句来返回处理结果的话，那么 <code>isSync</code> 值仍为 <code>true</code>，将会执行以下相应的处理逻辑：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loader-runner/lib/LoaderRunner.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runSyncOrAsync</span>(<span class="hljs-params">fn, context, args, callback</span>) </span>&#123;
        <span class="hljs-comment">// 省略部分代码</span>
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-keyword">var</span> result = (<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">LOADER_EXECUTION</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> fn.apply(context, args);
&#125;());
<span class="hljs-keyword">if</span>(isSync) &#123; <span class="hljs-comment">// 使用return语句返回处理结果</span>
  isDone = <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">if</span>(result === <span class="hljs-literal">undefined</span>)
    <span class="hljs-keyword">return</span> callback();
  <span class="hljs-keyword">if</span>(result && <span class="hljs-keyword">typeof</span> result === <span class="hljs-string">"object"</span> 
            && <span class="hljs-keyword">typeof</span> result.then === <span class="hljs-string">"function"</span>) &#123;
       <span class="hljs-keyword">return</span> result.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">r</span>) </span>&#123;
 callback(<span class="hljs-literal">null</span>, r);
       &#125;, callback);
   &#125;
   <span class="hljs-keyword">return</span> callback(<span class="hljs-literal">null</span>, result);
  &#125;
&#125; <span class="hljs-keyword">catch</span>(e) &#123;
         <span class="hljs-comment">// 省略异常处理代码</span>
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过观察以上代码，我们可以知道在 Loader 函数中，可以使用 <code>return</code> 语句直接返回 <code>Promise</code> 对象，比如这种方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(source + <span class="hljs-string">"-promise-simple"</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们已经知道 Loader 是如何返回数据，那么 Loader 最终返回的结果是如何被处理的的呢？下面我们来简单介绍一下。</p>
<h3 data-id="heading-8">七、Loader 最终的返回结果是如何被处理的？</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack/lib/NormalModule.js（Webpack 版本：5.45.1）</span>
<span class="hljs-function"><span class="hljs-title">build</span>(<span class="hljs-params">options, compilation, resolver, fs, callback</span>)</span> &#123;
               <span class="hljs-comment">// 省略部分代码</span>
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.doBuild(options, compilation, resolver, fs, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
<span class="hljs-comment">// if we have an error mark module as failed and exit</span>
<span class="hljs-keyword">if</span> (err) &#123;
<span class="hljs-built_in">this</span>.markModuleAsErrored(err);
<span class="hljs-built_in">this</span>._initBuildHash(compilation);
<span class="hljs-keyword">return</span> callback();
&#125;

                        <span class="hljs-comment">// 省略部分代码</span>
<span class="hljs-keyword">let</span> result;
<span class="hljs-keyword">try</span> &#123;
result = <span class="hljs-built_in">this</span>.parser.parse(<span class="hljs-built_in">this</span>._ast || <span class="hljs-built_in">this</span>._source.source(), &#123;
<span class="hljs-attr">current</span>: <span class="hljs-built_in">this</span>,
<span class="hljs-attr">module</span>: <span class="hljs-built_in">this</span>,
<span class="hljs-attr">compilation</span>: compilation,
<span class="hljs-attr">options</span>: options
&#125;);
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
handleParseError(e);
<span class="hljs-keyword">return</span>;
&#125;
handleParseResult(result);
&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上代码可知，在 <code>this.doBuild</code> 方法的回调函数中，会使用 <code>JavascriptParser</code> 解析器对返回的内容进行解析操作，而底层是通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Facornjs%2Facorn" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/acornjs/acorn" ref="nofollow noopener noreferrer">acorn</a> 这个第三方库来实现 JavaScript 代码的解析。而解析后的结果，会继续调用 <code>handleParseResult</code> 函数进行进一步处理。这里阿宝哥就不展开介绍了，感兴趣的小伙伴可以自行阅读一下相关源码。</p>
<h3 data-id="heading-9">八、为什么要把 content 赋值给 module.exports 属性呢？</h3>
<p>最后我们来回答前面留下的问题 —— 在 <strong>a-loader.js</strong> 模块中，为什么要把 <code>content</code> 赋值给 <code>module.exports</code> 属性呢？要回答这个问题，我们将从 Webpack 生成的 <strong>bundle.js</strong> 文件（已删除注释信息）中找到该问题的答案：</p>
<p><strong><code>__webpack_modules__</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> __webpack_modules__ = (&#123;
  <span class="hljs-string">"./src/data.txt"</span>:  (<span class="hljs-function">(<span class="hljs-params"><span class="hljs-built_in">module</span></span>)=></span>&#123;
    <span class="hljs-built_in">eval</span>(<span class="hljs-string">"module.exports = '大家好，我是阿宝哥[cLoader->bLoader->aLoader]'\n\n//# 
      sourceURL=webpack://webpack-loader-demo/./src/data.txt?"</span>);
   &#125;),
 <span class="hljs-string">"./src/index.js"</span>:(<span class="hljs-function">(<span class="hljs-params">__unused_webpack_module, __webpack_exports__, __webpack_require__</span>) =></span> &#123;
    <span class="hljs-built_in">eval</span>(<span class="hljs-string">"__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var 
     _data_txt__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./data.txt */ \"./src/data.txt\");...
    );
  &#125;)
&#125;);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>__webpack_require__</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// The module cache</span>
<span class="hljs-keyword">var</span> __webpack_module_cache__ = &#123;&#125;;
<span class="hljs-comment">// The require function</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span>(<span class="hljs-params">moduleId</span>) </span>&#123;
  <span class="hljs-comment">// Check if module is in cache</span>
  <span class="hljs-keyword">var</span> cachedModule = __webpack_module_cache__[moduleId];
  <span class="hljs-keyword">if</span> (cachedModule !== <span class="hljs-literal">undefined</span>) &#123;
     <span class="hljs-keyword">return</span> cachedModule.exports;
  &#125;
 <span class="hljs-comment">// Create a new module (and put it into the cache)</span>
 <span class="hljs-keyword">var</span> <span class="hljs-built_in">module</span> = __webpack_module_cache__[moduleId] = &#123;
   <span class="hljs-attr">exports</span>: &#123;&#125;
 &#125;;
 <span class="hljs-comment">// Execute the module function</span>
 __webpack_modules__[moduleId](<span class="hljs-built_in">module</span>, <span class="hljs-built_in">module</span>.exports, __webpack_require__);
 <span class="hljs-comment">// Return the exports of the module</span>
 <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>.exports;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在生成的 <strong>bundle.js</strong> 文件中，<code>./src/index.js</code> 对应的函数内部，会通过调用 <code>__webpack_require__</code> 函数来导入 <code>./src/data.txt</code> 路径中的内容。而在 <code>__webpack_require__</code> 函数内部会优先从缓存对象中获取 <code>moduleId</code> 对应的模块，若该模块已存在，就会返回该模块对象上 <code>exports</code> 属性的值。如果缓存对象中不存在 <code>moduleId</code> 对应的模块，则会创建一个包含 <code>exports</code> 属性的 <code>module</code> 对象，然后会根据 <code>moduleId</code> 从 <code>__webpack_modules__</code> 对象中，获取对应的函数并使用相应的参数进行调用，最终返回 <code>module.exports</code> 的值。所以在 <strong>a-loader.js</strong> 文件中，把 <code>content</code> 赋值给 <code>module.exports</code> 属性的目的是为了导出相应的内容。</p>
<h3 data-id="heading-10">九、总结</h3>
<p>本文介绍了 Webpack Loader 的本质、Normal Loader 和 Pitching Loader 的定义和使用及 Loader 是如何被运行的等相关内容，希望阅读完本文之后，你对 Webpack Loader 机制能有更深刻的理解。文中阿宝哥只介绍了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">loader-runner</a> 模块，其实 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-utils" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-utils" ref="nofollow noopener noreferrer">loader-utils</a>（Loader 工具库）和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Fschema-utils" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/schema-utils" ref="nofollow noopener noreferrer">schema-utils</a>（Loader Options 验证库）这两个模块也与 Loader 息息相关。在编写 Loader 的时候，你可能就会使用到它们。如果你对如何编写一个 Loader 感兴趣的话，可以阅读 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fcontribute%2Fwriting-a-loader%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/contribute/writing-a-loader/" ref="nofollow noopener noreferrer">writing-a-loader</a> 这个文档或掘金上 <a href="https://juejin.cn/post/6844903555673882632" target="_blank" title="https://juejin.cn/post/6844903555673882632">手把手教你撸一个 Webpack Loader</a> 这篇文章。</p>
<h3 data-id="heading-11">十、参考资源</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/" ref="nofollow noopener noreferrer">Webpack 官网</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">Github — loader-runner</a></li>
</ul></div>  
</div>
            