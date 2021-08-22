
---
title: 'webpack5——plugin'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4885'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 04:27:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=4885'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote>
<p>插件是 webpack 的 支柱 功能。webpack 自身也是构建于你在 webpack 配置中用到的相同的插件系统之上！</p>
<p>插件目的在于解决 loader 无法实现的其他事。</p>
<blockquote>
<p>Tip</p>
<p>如果在插件中使用了 webpack-sources 的 package，请使用 require('webpack').sources 替代 require('webpack-sources')，以避免持久缓存的版本冲突。</p>
</blockquote>
<h2 data-id="heading-0">剖析</h2>
<p>webpack 插件是一个具有 apply 方法的 JavaScript 对象。apply 方法会被 webpack compiler 调用，并且在 整个 编译生命周期都可以访问 compiler 对象。</p>
<p>ConsoleLogOnBuildWebpackPlugin.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> pluginName = <span class="hljs-string">'ConsoleLogOnBuildWebpackPlugin'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConsoleLogOnBuildWebpackPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    compiler.hooks.run.tap(pluginName, <span class="hljs-function">(<span class="hljs-params">compilation</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'webpack 构建过程开始！'</span>);
    &#125;);
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = ConsoleLogOnBuildWebpackPlugin;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>compiler hook 的 tap 方法的第一个参数，应该是驼峰式命名的插件名称。建议为此使用一个常量，以便它可以在所有 hook 中重复使用。</p>
<h2 data-id="heading-1">用法</h2>
<p>由于插件可以携带参数/选项，你必须在 webpack 配置中，向 plugins 属性传入一个 new 实例。</p>
<p>取决于你的 webpack 用法，对应有多种使用插件的方式。</p>
<h3 data-id="heading-2">配置方式</h3>
<p>webpack.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>); <span class="hljs-comment">// 通过 npm 安装</span>
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>); <span class="hljs-comment">// 访问内置的插件</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./path/to/my/entry/file.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'my-first-webpack.bundle.js'</span>,
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx)$/</span>,
        use: <span class="hljs-string">'babel-loader'</span>,
      &#125;,
    ],
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> webpack.ProgressPlugin(),
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123; <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span> &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ProgressPlugin 用于自定义编译过程中的进度报告，HtmlWebpackPlugin 将生成一个 HTML 文件，并在其中使用 script 引入一个名为 my-first-webpack.bundle.js 的 JS 文件。</p>
<h3 data-id="heading-3">Node API 方式</h3>
<p>在使用 Node API 时，还可以通过配置中的 plugins 属性传入插件。</p>
<p>some-node-script.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>); <span class="hljs-comment">// 访问 webpack 运行时(runtime)</span>
<span class="hljs-keyword">const</span> configuration = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.config.js'</span>);

<span class="hljs-keyword">let</span> compiler = webpack(configuration);

<span class="hljs-keyword">new</span> webpack.ProgressPlugin().apply(compiler);

compiler.run(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, stats</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Tip</p>
<p>你知道吗：以上看到的示例和 webpack 运行时(runtime)本身 极其类似。webpack 源码 中隐藏有大量使用示例，你可以将其应用在自己的配置和脚本中。</p>
</blockquote>
<blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote></div>  
</div>
            