
---
title: '使用webpack搭建react脚手架'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5159'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 18:40:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=5159'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>create-react-app是个优秀的脚手架工具，然而作为前端开发者，不能不会自己搭建脚手架工具。所以，开始了学习webpack之路。</p>
<h3 data-id="heading-1">首先，大体了解webpack的工作流程</h3>
<p>打包就是将文件打包为另一个文件的能力。webpack将打包过程视为输入、输出两部分，其中这个过程还包括入口、模块、chunk、chunk组合和许多其他部分。从入口开始，webpack会创建一个依赖关系图，这个关系图中包含着应用程序中所需的所有模块，然后打包为bundle。</p>
<p>了解了之后，我们开始正式构建脚手架工具。</p>
<ol>
<li>首先进行基础配置，设置入口和出口。</li>
</ol>
<p>配置文件为webpack.config.js
安装npm install webpack webpack-cli webpack-dev-server.
我这里使用的是webpack4的版本。小伙伴们，请根据需要调整。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'src/index.js'</span>, <span class="hljs-comment">// 入口</span>
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>), <span class="hljs-comment">// 输出目录</span>
        <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'/dist/'</span>, <span class="hljs-comment">// 加载资源的目录</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span> <span class="hljs-comment">// 输出文件名</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的目录结构为:</p>
<pre><code class="hljs language-js copyable" lang="js">--public
----index.html
----logo.jpeg
--src
-----index.js
-----App.jsx
-----App.css
--webpack.config.js
--.babelrc
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>配置webpack使其能打包css、jpeg和jsx文件。</li>
</ol>
<p>webpack默认是只能打包js文件的。我们需要用不同的loader来增强它的打包能力。
使用stley-loader(自动生成style标签)、css-loader来打包css文件。
使用url-loader、file-loader打包图片资源文件。
同时为了使用es6等语法，使用babel-loader打包js、jsx文件。
webpack配置如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  ...,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx)$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        loader: <span class="hljs-string">'babel-loader'</span>
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span>]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpeg|gif)$/i</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">limit</span>: <span class="hljs-number">8192</span>
            &#125;
          &#125;
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">resolve</span>: &#123;
      <span class="hljs-attr">extensions</span>:[<span class="hljs-string">'*'</span>, <span class="hljs-string">'.js'</span>, <span class="hljs-string">'.jsx'</span>] <span class="hljs-comment">// 设置按顺序解析文件名</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置resolve.extensions属性的含义是:</p>
<pre><code class="copyable">当使用import * from 'src/App'时，会先按照无后缀名匹配，然后App.js，如果找不到就按照App.jsx匹配文件。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>babel的配置如下:</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"presets"</span>: [<span class="hljs-string">"@babel/env"</span>, <span class="hljs-string">"@babel/preset-react"</span>],
  <span class="hljs-string">"plugins"</span>: [
    <span class="hljs-string">"@babel/plugin-proposal-optional-chaining"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>自动生成html文件</li>
</ol>
<p>每次打包之后都会生成bundle.js文件，如果改变打包路径的话，就需要手动改HTML文件中的script标签的src属性，为了方便，使用html-webpack-plugin自动生成HTML文件。
npm  install html-webpack-plugin --save-dev</p>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    ...
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">title</span>: <span class="hljs-string">'webpack for react'</span>, <span class="hljs-comment">// 设置title变量，可以在index.html中读取</span>
            <span class="hljs-attr">template</span>: <span class="hljs-string">'public/index.html'</span> <span class="hljs-comment">// 模板文件</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>html-webpack-plugin还有很多有用的配置，比如设置变量等。在这里设置了title变量，在HTML文件中可以使用<%= htmlWebpackPlugin.options.title %>读取这个变量的值。</p>
<ol start="4">
<li>使用clean-webpack-plugin清理打包文件。</li>
</ol>
<p>如果不清理打包文件，那么每次打包构建后的文件夹dist目录中会有很多多余的文件。
不再介绍如何安装插件。</p>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-comment">//...</span>
        <span class="hljs-keyword">new</span> CleanWebpackPlugin()
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>设置webpack-dev-server启动本地服务</li>
</ol>
<p>开发过程中，大部分时间都是在本地调试，webpack-dev-server提供了本地启动服务的方式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//...</span>
<span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: path.join(__dirname, <span class="hljs-string">'dist'</span>), <span class="hljs-comment">// 设置代理目录</span>
    <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,
    <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'http://localhost:3000/dist/'</span>, <span class="hljs-comment">// 设置打包文件url，可以直接写/dist/</span>
    <span class="hljs-attr">hotOnly</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 热更新</span>
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 压缩</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 自动打开浏览器</span>
    <span class="hljs-attr">writeToDisk</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// webpack-dev-server默认是将文件存在内存里，这里设置为存在磁盘中</span>
    <span class="hljs-attr">proxy</span>: &#123; <span class="hljs-comment">// 设置代理</span>
      <span class="hljs-attr">api</span>: <span class="hljs-string">'http://localhost:3000'</span>
      <span class="hljs-comment">/* 'api': &#123;
        target: 'http://localhost:3000',
        pathRewrite: &#123;
          '^/api': ''
        &#125;
      &#125; */</span>
    &#125;
    <span class="hljs-comment">// host: '127.0.0.1' // 修改dev server的host</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>设置每次webpack-dev-server重新打包时保留index.html文件</li>
</ol>
<p>这是启动本地服务后，每次webpack-dev-server重新打包，并不会再次生成index.html文件，而clean-webpack-plugin会将原来的html删除掉，所以为clean-webpack-plugin增加配置，使得每次打包后clean时并不删除index.html文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
 <span class="hljs-comment">// ...</span>
 <span class="hljs-attr">plugins</span>: [
   <span class="hljs-keyword">new</span> CleanWebpackPlugin(&#123;
      <span class="hljs-comment">/* 使得每次webpack-dev-server打包之后，index.html文件仍然保留 */</span>
      <span class="hljs-attr">cleanStaleWebpackAssets</span>: <span class="hljs-literal">false</span>
   &#125;)
 ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>将css文件提取出来</li>
</ol>
<p>css-loader会将css打包到js中，然后再由style-loader生成style标签。现在我使用mini-css-extract-plugin将css提取出来到单独的文件中。
总共有两步:</p>
<ol>
<li>替换loader</li>
<li>增加plugin</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
 <span class="hljs-comment">// ...</span>
 <span class="hljs-attr">module</span>: &#123;
     <span class="hljs-attr">rules</span>: &#123;
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        <span class="hljs-comment">// 将style-loader替换为MiniCssExtractPlugin.loader</span>
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span>]
      &#125;
      <span class="hljs-comment">// ...</span>
     &#125;
 &#125;,
 <span class="hljs-attr">plugins</span>: [
   <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-comment">// Options similar to the same options in webpackOptions.output</span>
      <span class="hljs-comment">// both options are optional</span>
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/[name].css'</span>,
      <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'css/[id].css'</span>
    &#125;)
 ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>配置热更新</li>
</ol>
<p>模块热替换(HMR - hot module replacement)功能会在应用程序运行过程中，替换、添加或删除模块，而无需重新加载整个页面。
但是，<strong>模块热更新绝不能用在生产环境中</strong>。
所以，要先判断是否为生产环境，如果是，则启用；否则，不启用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 设置运行环境</span>
<span class="hljs-keyword">const</span> mode = process.env.NODE_ENV
<span class="hljs-keyword">const</span> plugins = []
<span class="hljs-keyword">if</span> (mode !== <span class="hljs-string">'production'</span>) &#123;
  <span class="hljs-comment">// 设置热更新插件只在开发模式下启用,HMR决不能用在生产环境中</span>
  <span class="hljs-keyword">const</span> hotModuleReplacementPlugin = <span class="hljs-keyword">new</span> webpack.HotModuleReplacementPlugin()
  plugins.push(hotModuleReplacementPlugin)
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        ..plugins,
        <span class="hljs-comment">// ...</span>
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li>启用sourceMap</li>
</ol>
<p>一般来讲，生产环境和开发环境的考虑的因素不同，所以对于sourceMap的需求也不同。我这里配置的开发环境的sourceMap主要考虑的准确性，生产环境没有配置sourceMap。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//...</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">devtool</span>: mode === <span class="hljs-string">'development'</span> ? <span class="hljs-string">'eval-source-map'</span> : <span class="hljs-string">'none'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="10">
<li>处理热更新辅助文件</li>
</ol>
<p>每次热更新都会生成后缀名为.hot-update.js和.hot-update.json的辅助文件。热更新的次数多了之后，这些辅助文件也相应的多了。我们进行配置，只保留最新的辅助文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// ...</span>
        <span class="hljs-comment">/* 避免HotModuleReplacementPlugin每次都生成不同的描述文件json和补丁文件js */</span>
    <span class="hljs-attr">hotUpdateChunkFilename</span>: <span class="hljs-string">'hot/hot-update.js'</span>,
    <span class="hljs-attr">hotUpdateMainFilename</span>: <span class="hljs-string">'hot/hot-update.json'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，简易的脚手架搭建完毕，当然还有很多缺失，比如对字体的处理、相同模块的提取等等，但是骨架已经出来，大家可以根据这个进行简单学习。
<a href="https://github.com/hahei89/webpack-explore-demo" target="_blank" rel="nofollow noopener noreferrer">git地址 </a></p>
<p>欢迎大家批评指正。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            