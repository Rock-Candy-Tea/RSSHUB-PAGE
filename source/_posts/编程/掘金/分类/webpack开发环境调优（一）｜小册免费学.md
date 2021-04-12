
---
title: 'webpack开发环境调优（一）｜小册免费学'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b027a470944b59b1b2744835aa1a60~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 20:28:43 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b027a470944b59b1b2744835aa1a60~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Webpack 作为打包工具的重要使命之一就是提升效率。下面我们记录一些对日常开发有一定帮助的 Webpack 插件以及调试方法，本系列文章将包含以下内容：</p>
<ul>
<li>Webpack 周边插件介绍</li>
<li>模块热替换及其原理（下一篇）</li>
</ul>
<h2 data-id="heading-0">1. Webpack 开发效率插件</h2>
<p>这里我们记录几个使用较广的插件，可以从不同的方面对 Webpack 的能力进行增强。</p>
<h3 data-id="heading-1">1.1 webpack-dashboard</h3>
<p>Webpack 每一次构建结束后都会在控制台输出一些打包相关的信息，但是这些信息是以列表的形式展示的，有时会显得不够直观。webpack-dashboard 就是用来更好地展示这些信息的。</p>
<p>安装命令：<code>yarn add webpack-dashboard --save-dev</code></p>
<p>我们需要把 webpack-dashboard 作为插件添加到 Webpack 配置中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> DashboardPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-dashboard/plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].js'</span>,
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> DashboardPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了使 webpack-dashboard 生效还要更改一下 webpack 的启动方式，就是用 webpack-dashboard 模块命令替代原来的 webpack 或者 webpack-dev-server 命令，并将原有的启动命令作为参数传给它。</p>
<p>假设原本的启动命令如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// package.json</span>
&#123;
  ...
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行<code>yarn dev</code>启动后效果如图：</p>
<p><img alt="原始开发服务启动.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b027a470944b59b1b2744835aa1a60~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>加上 webpack-dashboard 后则变成：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// package.json</span>
&#123;
  ...
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dashboard -- webpack-dev-server"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行<code>yarn dev</code>启动后效果如图：</p>
<p><img alt="webpack-dashboard.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c27549eb42594bc4bc4c077bec0a958b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>webpack-dashboard 的控制台分为几个面板来展示不同方面的信息。比如左上角的 Log 面板就是 Webpack 本身的日志；下面的 Modules 面板则是此次参与打包的模块，从中我们可以看出哪些模块资源占用比较多；而从右下方的 Problems 面板中可以看到构建过程中的警告和错误等。</p>
<h3 data-id="heading-2">1.2 webpack-merge</h3>
<p>对于需要配置多种打包环境的项目来说，webpack-merge 是一个非常实用的工具。假设我们的项目有3种不同的配置，分别对应本地环境、测试环境和生产环境。每一个环境对应的配置都不同，但也有一些公共的部分，那么我们就可以将这些公共的部分提取出来。假设我们创建一个 webpack.common.js 来存放所有这些配置，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.common.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/app.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].js'</span>
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpg|gif)$/</span>,
        use: <span class="hljs-string">'file-loader'</span>
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// 用于生成 index.html</span>
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'Webpack Tutorials'</span>,
      <span class="hljs-attr">meta</span>: &#123;
        <span class="hljs-attr">viewport</span>: <span class="hljs-string">'width=device-width'</span>
      &#125;,
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./template/index.html'</span>
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每一个环境又有一个相对应的配置文件，如对于生产环境的 webpack.prod.js。假如不借助任何工具，我们自己从 webpack.common.js 引入公共配置，则大概如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.prod.js</span>
<span class="hljs-keyword">const</span> commonConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common.js'</span>);
<span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">Object</span>.assign(commonConfig, &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样看起来很简单，但问题是，假如我们想修改一下 CSS 的打包规则，例如用 mini-css-extract-plugin 将样式单独打包出来应该怎么办呢？这时就需要添加一些代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.prod.js</span>
<span class="hljs-keyword">const</span> commonConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common.js'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">Object</span>.assign(commonConfig, &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpg|gif)$/</span>,
        use: <span class="hljs-string">'file-loader'</span>
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [ MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span> ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin()
  ]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>mini-css-extract-plugin 与 extract-text-webpack-plugin 相比：</p>
<ul>
<li>异步加载</li>
<li>没有重复的编译（性能）</li>
<li>更容易使用</li>
<li>特定于CSS</li>
</ul>
</blockquote>
<p>是不是一下子感觉有些冗余了呢？这是因为通过 Object.assign 方法会把同名属性的值覆盖掉，所以必须替换掉整个 module 的配置。</p>
<p>下面我们看一下如何用 webpack-merge 来解决这个问题。安装：<code>yarn add webpack-merge -D</code></p>
<p>更改 webpack.prod.js 如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.prod.js</span>
<span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>);
<span class="hljs-keyword">const</span> commonConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common.js'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = merge(commonConfig, &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [ MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span> ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [ <span class="hljs-keyword">new</span> MiniCssExtractPlugin() ]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 merge 方法后的效果相当于：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/app.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].js'</span>
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpg|gif)$/</span>,
        use: <span class="hljs-string">'file-loader'</span>
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [ MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span> ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// 用于生成 index.html</span>
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'Webpack Tutorials'</span>,
      <span class="hljs-attr">meta</span>: &#123;
        <span class="hljs-attr">viewport</span>: <span class="hljs-string">'width=device-width'</span>
      &#125;,
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./template/index.html'</span>
    &#125;),
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin()
  ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>merge 方法会对值类型进行覆盖，对数组进行合并拓展。</p>
<h3 data-id="heading-3">1.3 speed-measure-webpack-plugin</h3>
<p>觉得 Webpack 构建很慢但又不清楚如何下手优化吗？那么可以试试 speed-measure-webpack-plugin 这个插件（简称 SMP）。SMP 可以分析出 Webpack 整个打包过程中在各个 loader 和 plugins 上耗费的时间，这将会有助于找出构建过程中的性能瓶颈。</p>
<p>安装：<code>yarn add speed-measure-webpack-plugin -D</code></p>
<p>SMP 的使用很简单，只要用它的 wrap 方法包裹在 Webpack 的配置对象外面即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-keyword">const</span> SpeedMeasurePlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'speed-measure-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> smp = <span class="hljs-keyword">new</span> SpeedMeasurePlugin();
<span class="hljs-built_in">module</span>.exports = smp.wrap(&#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/main.js'</span>,
  ......
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 Webpack 构建命令，将会输出 SMP 的时间测量结果，如下图：</p>
<p><img alt="smp.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0491be0a7ce4f14bb513b7bdababe2e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上面的分析结果就可以找出哪些构建步骤耗时较长，以便于优化和反复测试。</p>
<h3 data-id="heading-4">1.4 size-plugin</h3>
<p>一般而言，随着项目的开发产出的资源会越来越大，最终生成的资源会逐渐变得臃肿。size-plugin 这个插件可以帮助监控资源体积的变化，尽早地发现问题。</p>
<p>安装：<code>yarn add size-plugin -D</code></p>
<p>size-plugin 的配置同样很简单：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> SizePlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'size-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  ......,
  <span class="hljs-attr">plugins</span>: [
  <span class="hljs-keyword">new</span> SizePlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在每次执行 Webpack 打包命令后，size-plugin 都会输出本次构建的资源体积（gzip过后），以及与上次构建相比体积变化了多少，如图：</p>
<p><img alt="size-plugin.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1eea34411f7431298ff595f79efafbe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>该插件目前还不够完善，理想情况下它应该可以把这些结果以文件的形式输出来，这样就变与我们在持续集成平台上对结果进行对比。不过它还在快速完善中，也许未来会添加类似的功能。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            