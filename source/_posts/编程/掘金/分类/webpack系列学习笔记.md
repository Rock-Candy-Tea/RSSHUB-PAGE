
---
title: 'webpack系列学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=721'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 21:49:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=721'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>本文整理了webpack前端资源构建工具以及静态模块打包器相关知识总结，如果对答案有不一样见解的同学欢迎评论区补充讨论，当然有问题，也欢迎在评论区指出。</p>
<p>参照引用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1e7411j7T5%3Ffrom%3Dsearch%26seid%3D6406688376558299765" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1e7411j7T5?from=search&seid=6406688376558299765" ref="nofollow noopener noreferrer">尚硅谷webpack教程视频</a>，以作记录</p>
<h2 data-id="heading-1">一、webpack简介</h2>
<h3 data-id="heading-2">1、webpack 是什么？</h3>
<p>（一）webpack 是一个前端资源构建工具。。</p>
<ul>
<li>像前端的某些资源文件（es6、less、sass、vue等），都需要各种小工具进行解析、转义后才能使用，然后就用到webpack这种包含这些小工具的一个大的构建工具，对这些文件做处理。</li>
</ul>
<p>（二）webpack是一个静态模块打包器。。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//index.js文件（模块）</span>
<span class="hljs-keyword">import</span> $ <span class="hljs-keyword">from</span> <span class="hljs-string">'jquery'</span>;（小模块）
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.less'</span>;（小模块）
​
$(<span class="hljs-string">'#title'</span>).click(<span class="hljs-function">()=></span>&#123;
    $(<span class="hljs-string">'body'</span>).css(<span class="hljs-string">'backgroundColor'</span>,<span class="hljs-string">'deepPink'</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="0">
<li>index.js先是将jquery和less这些文件（这些文件叫做<strong>模块</strong>）引进来，然后形成一个<strong>chunk（代码块）</strong></li>
<li>然后对chunk进行各项处理，如less编译成css，jquery编译成 js（浏览器能识别的语法），这些处理过程就叫做<strong>打包</strong></li>
<li>打包后输出出去的文件，叫<strong>bundle.js</strong></li>
</ol>
<h3 data-id="heading-3">2、webpack五个核心概念</h3>
<p>（一）Entry（入口）</p>
<p>指示webpack从哪个文件为入口开始打包</p>
<p>（二）Output（输出）</p>
<p>指示webpack打包后的资源输出到哪里去，以及如何命名</p>
<p>（三）Loader（转义）</p>
<p>让webpack能够去处理那些非js文件（webpack只能理解js、json）</p>
<p>（四）plugin（插件）</p>
<p>让webpack支持更多的功能，相当于扩展功能，像打包优化和压缩，重新定义环境中的变量等</p>
<p>（五）mode（模式）</p>
<ul>
<li>开发模式（development）：能让代码本地调试运行</li>
<li>生产模式（production）：能让代码生产上线运行</li>
</ul>
<h3 data-id="heading-4">3、初始化项目</h3>
<h5 data-id="heading-5">初始化配置</h5>
<p><code>npm init -y</code> 进行初始化</p>
<p>npm install webpack webpack-cli -D 安装webpack到本地</p>
<h5 data-id="heading-6">编译运行</h5>
<p>运行指令:</p>
<ul>
<li>开发环境: webpack ./src/index.js -o ./build/built.js --mode=development</li>
</ul>
<p>   webpack会以 ./src/index.js为入口文件开始打包，打包后输出到./build/built.js整体打包环境，是开发环境</p>
<ul>
<li>生产环境: webpack ./src/index.js -o ./build/built.js --mode=production</li>
</ul>
<p>   打包后的资源会被压缩，比开发环境小</p>
<h5 data-id="heading-7">结论</h5>
<ul>
<li>webpack能处理js/json资源，不能处理css/img等其他资源</li>
<li>生产环境和开发环境将ES6模块化编译成浏览器能识别的模块</li>
<li>生产环境比开发环境多一个压缩js代码。</li>
</ul>
<h3 data-id="heading-8">4、打包资源</h3>
<h5 data-id="heading-9">打包样式资源</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
  webpack.config.js  webpack的配置文件
    作用: 指示 webpack 干哪些活（当你运行 webpack 指令时，会加载里面的配置）
    所有构建工具都是基于nodejs平台运行的~模块化默认采用commonjs。
*/</span>
​
<span class="hljs-comment">// resolve用来拼接绝对路径的方法</span>
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
​
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ----------------webpack配置</span>
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, <span class="hljs-comment">//入口文件</span>
  <span class="hljs-attr">output</span>: &#123;  <span class="hljs-comment">// 输出</span>
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,  <span class="hljs-comment">// 输出文件名</span>
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)  <span class="hljs-comment">// 输出路径    __dirname nodejs的变量，代表当前文件的目录绝对路径</span>
  &#125;,
  <span class="hljs-comment">// loader的配置</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// 不同文件必须配置不同loader处理</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.css$/</span>,
        use: [
          <span class="hljs-string">'style-loader'</span>,
          <span class="hljs-string">'css-loader'</span>
        ]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,  <span class="hljs-comment">// 匹配哪些文件</span>
        use: [      <span class="hljs-comment">//使用哪些loader进行处理，use中loader的执行顺序：从后往前（先less->css->style）</span>
          <span class="hljs-string">'style-loader'</span>,   <span class="hljs-comment">//创建style标签，将js中的样式资源插入进去，添加到head中生效</span>
          <span class="hljs-string">'css-loader'</span>,  <span class="hljs-comment">//将css文件变成common模块加载js中，里面内容是样式字符串</span>
          <span class="hljs-string">'less-loader'</span>
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-comment">// plugins的配置</span>
  <span class="hljs-attr">plugins</span>: [],
  <span class="hljs-comment">// mode模式</span>
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>, <span class="hljs-comment">// 开发模式</span>
  <span class="hljs-comment">// mode: 'production'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">打包html资源</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
  loader: 1. 下载   2. 使用（配置loader）
  plugins: 1. 下载  2. 引入插件（构造函数）  3. 使用（调用函数）
*/</span>
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
​
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: []
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// html-webpack-plugin</span>
    <span class="hljs-comment">// 功能：默认会创建一个空的HTML，自动引入打包输出的所有资源（JS/CSS）</span>
    <span class="hljs-comment">// 需求：需要有结构的HTML文件</span>
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-comment">// 复制 './src/index.html' 文件，并自动引入打包输出的所有资源（JS/CSS）</span>
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
    &#125;)
  ],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">打包图片资源</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
​
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
        <span class="hljs-comment">// 要使用多个loader处理用use</span>
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'less-loader'</span>]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(jpg|png|gif)$/</span>,
        <span class="hljs-comment">// 使用一个loader ，必须下载 url-loader file-loader</span>
        loader: <span class="hljs-string">'url-loader'</span>,  <span class="hljs-comment">// 处理图片资源   问题：默认处理不了html中img图片</span>
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-comment">// 图片大小小于8kb，就会被base64处理</span>
          <span class="hljs-comment">// 优点: 减少请求数量（减轻服务器压力）</span>
          <span class="hljs-comment">// 缺点：图片体积会更大（文件请求速度更慢）</span>
          <span class="hljs-attr">limit</span>: <span class="hljs-number">8</span> * <span class="hljs-number">1024</span>,
            
          <span class="hljs-comment">// 问题：因为url-loader默认使用es6模块化解析，而html-loader引入图片是commonjs。</span>
          <span class="hljs-comment">// 解析时会出问题：[object Module]</span>
          <span class="hljs-comment">// 解决：关闭url-loader的es6模块化，使用commonjs解析</span>
          <span class="hljs-attr">esModule</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-comment">// 给图片进行重命名,[hash:10]取图片的hash的前10位,[ext]取文件原来扩展名</span>
          <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>
        &#125;
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.html$/</span>,
        <span class="hljs-comment">// 处理html文件的img图片（负责引入img，从而能被url-loader进行处理）</span>
        loader: <span class="hljs-string">'html-loader'</span>
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
    &#125;)
  ],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">打包其它资源</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
​
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.css$/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>]
      &#125;,
      <span class="hljs-comment">// 打包其他资源如：iconfont图标  (除了html/js/css资源以外的资源)</span>
      &#123;
        <span class="hljs-comment">// 排除css/js/html资源</span>
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/.(css|js|html|less)$/</span>,
        loader: <span class="hljs-string">'file-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>
        &#125;
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
    &#125;)
  ],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">devServer热更新</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
​
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;&#125;
  <span class="hljs-attr">plugins</span>: [],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
​
  <span class="hljs-comment">// 开发服务器 devServer：用来自动化（自动编译，自动打开浏览器，自动刷新浏览器~~）</span>
  <span class="hljs-comment">// 特点：只会在内存中编译打包，不会有任何输出</span>
  <span class="hljs-comment">// 启动devServer指令为：npx webpack-dev-server  （包需要下载）</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: resolve(__dirname, <span class="hljs-string">'build'</span>),   <span class="hljs-comment">// 项目构建后路径</span>
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,   <span class="hljs-comment">// 启动gzip压缩</span>
    <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,  <span class="hljs-comment">// 端口号</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>  <span class="hljs-comment">// 自动打开本地默认浏览器</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">开发环境配置</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
  开发环境配置：能让代码运行
    运行项目指令：
      webpack 会将打包结果输出出去
      npx webpack-dev-server 只会在内存中编译打包，没有输出
*/</span>
​
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
​
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// loader的配置</span>
      &#123;
        <span class="hljs-comment">// 处理less资源</span>
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'less-loader'</span>]
      &#125;,
      &#123;
        <span class="hljs-comment">// 处理css资源</span>
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.css$/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>]
      &#125;,
      &#123;
        <span class="hljs-comment">// 处理图片资源</span>
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(jpg|png|gif)$/</span>,
        loader: <span class="hljs-string">'url-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">limit</span>: <span class="hljs-number">8</span> * <span class="hljs-number">1024</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>,
          <span class="hljs-comment">// 关闭es6模块化</span>
          <span class="hljs-attr">esModule</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'imgs'</span>
        &#125;
      &#125;,
      &#123;
        <span class="hljs-comment">// 处理html中img资源</span>
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.html$/</span>,
        loader: <span class="hljs-string">'html-loader'</span>
      &#125;,
      &#123;
        <span class="hljs-comment">// 处理其他资源</span>
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/.(html|js|css|less|jpg|png|gif)/</span>,
        loader: <span class="hljs-string">'file-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>,
          <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'media'</span>
        &#125;
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// plugins的配置</span>
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
    &#125;)
  ],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: resolve(__dirname, <span class="hljs-string">'build'</span>),
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">5、webpack 生产环境的基本配置</h3>
<h5 data-id="heading-16">处理css</h5>
<ul>
<li>提取 css 成单独文件</li>
</ul>
<p>mini-css-extract-plugin ，将a.css和b.css提取合并到单独文件main.js中</p>
<ul>
<li>css 兼容性处理 （有些样式在浏览器中无法解析）</li>
</ul>
<p>postcss-loader 和 postcss-preset-env 插件</p>
<ul>
<li>压缩 css</li>
</ul>
<p>optimize-css-assets-webpack-plugin</p>
<h5 data-id="heading-17">处理js</h5>
<ul>
<li>
<p>js 语法检查</p>
<ul>
<li><strong>eslint-loader</strong> <strong>eslint</strong> eslint-config-airbnb-base（语法风格） eslint-plugin-import</li>
<li>只检查自己写的源代码，第三方库不检查，需要设置exclude：/node_modules/ ，</li>
<li>自动修复检查出来的格式问题，需要设置options：&#123; fix:true&#125;</li>
</ul>
</li>
<li>
<p>js 兼容性处理</p>
</li>
</ul>
<p><strong>babel-loader</strong> @babel/core @babel/preset-env @babel/polyfill core-js</p>
<ul>
<li>js 和html代码压缩</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">plugins: [
    <span class="hljs-keyword">new</span> HtmlwebpackPlugin(&#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'./ src /index.html'</span>,
        <span class="hljs-attr">minify</span>: &#123;  <span class="hljs-comment">//设置minify，压缩htm1代码</span>
            <span class="hljs-attr">collapsewhitespace</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//移除空格</span>
            <span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span><span class="hljs-comment">//移除注释</span>
        &#125;
    &#125;)
],
<span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>  <span class="hljs-comment">//webpack的production模式，自带uglify.js，可以实现js代码压缩</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">生产环境配置</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-keyword">const</span> OptimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
​
<span class="hljs-comment">// 定义nodejs环境变量：决定使用browserslist的哪个环境</span>
process.env.NODE_ENV = <span class="hljs-string">'production'</span>;
​
<span class="hljs-comment">// 复用loader</span>
<span class="hljs-keyword">const</span> commonCssLoader = [
  MiniCssExtractPlugin.loader,
  <span class="hljs-string">'css-loader'</span>,
  &#123;
    <span class="hljs-comment">// 还需要在package.json中定义browserslist</span>
    <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
    <span class="hljs-attr">options</span>: &#123;
      <span class="hljs-attr">ident</span>: <span class="hljs-string">'postcss'</span>,
      <span class="hljs-attr">plugins</span>: <span class="hljs-function">() =></span> [<span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-preset-env'</span>)()]
    &#125;
  &#125;
];
​
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.css$/</span>,
        use: [...commonCssLoader]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
        use: [...commonCssLoader, <span class="hljs-string">'less-loader'</span>]
      &#125;,
      <span class="hljs-comment">/*
        正常来讲，一个文件只能被一个loader处理。
        当一个文件要被多个loader处理，那么一定要指定loader执行的先后顺序：
          先执行eslint 在执行babel
      */</span>
      &#123;
        <span class="hljs-comment">// 在package.json中eslintConfig --> airbnb</span>
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.js$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        <span class="hljs-comment">// 优先执行</span>
        enforce: <span class="hljs-string">'pre'</span>,
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'eslint-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">fix</span>: <span class="hljs-literal">true</span>
        &#125;
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.js$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        loader: <span class="hljs-string">'babel-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">presets</span>: [
            [
              <span class="hljs-string">'@babel/preset-env'</span>,
              &#123;
                <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>,
                <span class="hljs-attr">corejs</span>: &#123;<span class="hljs-attr">version</span>: <span class="hljs-number">3</span>&#125;,
                <span class="hljs-attr">targets</span>: &#123;
                  <span class="hljs-attr">chrome</span>: <span class="hljs-string">'60'</span>,
                  <span class="hljs-attr">firefox</span>: <span class="hljs-string">'50'</span>
                &#125;
              &#125;
            ]
          ]
        &#125;
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(jpg|png|gif)/</span>,
        loader: <span class="hljs-string">'url-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">limit</span>: <span class="hljs-number">8</span> * <span class="hljs-number">1024</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>,
          <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'imgs'</span>,
          <span class="hljs-attr">esModule</span>: <span class="hljs-literal">false</span>
        &#125;
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.html$/</span>,
        loader: <span class="hljs-string">'html-loader'</span>
      &#125;,
      &#123;
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/.(js|css|less|html|jpg|png|gif)/</span>,
        loader: <span class="hljs-string">'file-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'media'</span>
        &#125;
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/built.css'</span>
    &#125;),
    <span class="hljs-keyword">new</span> OptimizeCssAssetsWebpackPlugin(),
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>,
      <span class="hljs-attr">minify</span>: &#123;
        <span class="hljs-attr">collapseWhitespace</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;)
  ],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">6、webpack 性能优化</h3>
<h5 data-id="heading-20">开发环境性能优化</h5>
<ul>
<li>
<p>优化打包构建速度</p>
<p>当修改css文件，连同js文件一起都重新打包了一次</p>
<ul>
<li>
<p>HMR：hot module replacement 模块热替换，当一个模块变化，只会打包这一个模块</p>
</li>
<li>
<pre><code class="hljs language-js copyable" lang="js">样式文件：可以使用HMR功能：因为style-loader内部实现了~
js文件：默认不能使用HMR功能 --> 需要修改js代码，添加支持HMR功能的代码
    注意：HMR功能对js的处理，只能处理非入口js文件的其他文件。
html文件: 默认不能使用HMR功能.同时会导致问题：html文件不能热更新了~ （不用做HMR功能，html文件是主文件，包含所有的引用）
    解决：修改entry入口，将html文件引入  entry: [<span class="hljs-string">'./src/js/index.js'</span>, <span class="hljs-string">'./src/index.html'</span>],
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="hljs language-js copyable" lang="js">mode: <span class="hljs-string">'development'</span>,
<span class="hljs-attr">devServer</span>: &#123;
  <span class="hljs-attr">contentBase</span>: resolve(__dirname, <span class="hljs-string">'build'</span>),
  <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,
  <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span><span class="hljs-comment">// 开启HMR功能--当修改了webpack配置，新配置要想生效，必须重新webpack服务---解决了样式文件</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.hot) &#123;<span class="hljs-comment">// 一旦 module.hot 为true，说明开启了HMR功能。 --> 让HMR功能代码生效</span>
  <span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">'./print.js'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// ----解决了js文件</span>
    <span class="hljs-comment">// 方法会监听 print.js 文件的变化，一旦发生变化，其他模块不会重新打包构建。</span>
    <span class="hljs-comment">// 会执行后面的回调函数</span>
    print();
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>优化代码调试</p>
<ul>
<li>
<p>source-map-----能定位到代码错误的地方</p>
</li>
<li>
<pre><code class="hljs language-js copyable" lang="js">devServer: &#123;
  <span class="hljs-attr">contentBase</span>: resolve(__dirname, <span class="hljs-string">'build'</span>),
  <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,
  <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>
&#125;,
<span class="hljs-attr">devtool</span>: <span class="hljs-string">'eval-source-map'</span> <span class="hljs-comment">//只需要加这行代码</span>
<span class="hljs-comment">//eval-cheap-module-souce-map</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">  source-map: 一种 提供源代码到构建后代码映射 技术 （如果构建后代码出错了，通过映射可以追踪源代码错误）
  
    [inline-|hidden-|eval-][nosources-][cheap-[module-]]source-map
​
    source-map：外部
      错误代码准确信息 和 源代码的错误位置
    inline-source-map：内联----会导致文件过大，不推荐
      只生成一个内联source-map
      错误代码准确信息 和 源代码的错误位置
    hidden-source-map：外部
      错误代码错误原因，但是没有错误位置
      不能追踪源代码错误，只能提示到构建后代码的错误位置
    eval-source-map：内联
      每一个文件都生成对应的source-map，都在eval
      错误代码准确信息 和 源代码的错误位置
    nosources-source-map：外部
      错误代码准确信息, 但是没有任何源代码信息
    cheap-source-map：外部
      错误代码准确信息 和 源代码的错误位置 
      只能精确的行
    cheap-module-source-map：外部
      错误代码准确信息 和 源代码的错误位置 
      module会将loader的source map加入
​
    内联 和 外部的区别：1. 外部生成了文件，内联没有 2. 内联构建速度更快
​
✔✔✔✔开发环境：速度快，调试更友好
      速度快(eval>inline>cheap>...)
        eval-cheap-souce-map
        eval-source-map
      调试更友好  
        souce-map
        cheap-module-souce-map
        cheap-souce-map
​
      推荐的两种--> eval-source-map 调试更友好  / eval-cheap-module-souce-map  性能可以做到最好
​
✔✔✔✔生产环境：源代码要不要隐藏? 调试要不要更友好
      内联会让代码体积变大，所以在生产环境不用内联
      nosources-source-map 全部隐藏
      hidden-source-map 只隐藏源代码，会提示构建后代码错误信息
​
      推荐的两种--> source-map / cheap-module-souce-map
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h5 data-id="heading-21">生产环境性能优化</h5>
<ul>
<li>
<p>优化打包构建速度</p>
<ul>
<li>
<p>oneOf</p>
</li>
<li>
<p>babel缓存</p>
</li>
<li>
<p>多进程打包</p>
<pre><code class="copyable">开启多进程打包。 
进程启动大概为600ms，进程通信也有开销。
只有工作消耗时间比较长，才需要多进程打包
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>externals</p>
<p>禁止一些模块打包进来</p>
<pre><code class="copyable">mode: 'production',
externals: &#123;
  // 拒绝jQuery被打包进来
  jquery: 'jQuery'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>dll</p>
</li>
</ul>
</li>
<li>
<p>优化代码运行的性能</p>
<ul>
<li>
<p>缓存(hash-chunkhash-contenthash)</p>
</li>
<li>
<p>tree shaking-----去除无用代码</p>
<pre><code class="copyable">前提：1. 必须使用ES6模块化  2. 开启production环境
作用: 减少代码体积
​
在package.json中配置 
      "sideEffects": false 所有代码都没有副作用（都可以进行tree shaking）
        问题：可能会把css / @babel/polyfill （副作用）文件干掉
      "sideEffects": ["*.css", "*.less"]  这样就会保留css、less文件
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>code split</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 单入口 --- 单页面</span>
<span class="hljs-comment">// entry: './src/js/index.js',</span>
<span class="hljs-attr">entry</span>: &#123; ---- 多页面
  <span class="hljs-comment">// 多入口：有一个入口，最终输出就有一个bundle</span>
  <span class="hljs-attr">index</span>: <span class="hljs-string">'./src/js/index.js'</span>,
  <span class="hljs-attr">test</span>: <span class="hljs-string">'./src/js/test.js'</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
  1. 可以将node_modules中代码单独打包一个chunk最终输出
  2. 自动分析多入口chunk中，有没有公共的文件。如果有会打包成单独一个chunk
*/</span>
<span class="hljs-attr">optimization</span>: &#123;
  <span class="hljs-attr">splitChunks</span>: &#123;
    <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>
  &#125;
&#125;,
<span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//index.js</span>
<span class="hljs-comment">/*
  通过js代码，让某个文件被单独打包成一个chunk
  import动态导入语法：能将某个文件单独打包（即test文件单独打包）
*/</span>
<span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: 'test' */</span><span class="hljs-string">'./test'</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">&#123; mul, count &#125;</span>) =></span> &#123;
    <span class="hljs-comment">// 文件加载成功~</span>
    <span class="hljs-comment">// eslint-disable-next-line</span>
    <span class="hljs-built_in">console</span>.log(mul(<span class="hljs-number">2</span>, <span class="hljs-number">5</span>));
  &#125;)
  .catch(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// eslint-disable-next-line</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'文件加载失败~'</span>);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>懒加载/预加载</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'index.js文件被加载了~'</span>);
​
<span class="hljs-comment">// import &#123; mul &#125; from './test';</span>
​
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 懒加载~：当文件需要使用时才加载~ ---- 但当使用某个模块，模块又非常大时，加载的就会慢</span>
  <span class="hljs-comment">// 预加载 prefetch：会在使用之前，提前加载js文件，使用时读取缓存 ---- 兼容性较差</span>
  <span class="hljs-comment">// 正常加载可以认为是并行加载（同一时间加载多个文件）  </span>
  <span class="hljs-comment">// 预加载 prefetch：等其他资源加载完毕，浏览器空闲了，再偷偷加载资源</span>
  <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: 'test', webpackPrefetch: true */</span><span class="hljs-string">'./test'</span>).then(<span class="hljs-function">(<span class="hljs-params">&#123; mul &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(mul(<span class="hljs-number">4</span>, <span class="hljs-number">5</span>));
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>PWA 渐进式网络开发应用程序(离线可访问)</p>
</li>
</ul>
<p>在离线情况下，会从serviceWorker中和CacheStorage中获取资源</p>
<pre><code class="hljs language-js copyable" lang="js">workbox --> workbox-webpack-plugin

<span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> WorkboxWebpackPlugin.GenerateSW(&#123;
        <span class="hljs-comment">/*
        1. 帮助serviceworker快速启动
        2. 删除旧的 serviceworker

        生成一个 serviceworker 配置文件~
      */</span>
        <span class="hljs-attr">clientsClaim</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">skipWaiting</span>: <span class="hljs-literal">true</span>
    &#125;)
],

<span class="hljs-comment">// 在index.js  注册serviceWorker</span>
<span class="hljs-comment">// 处理兼容性问题</span>
<span class="hljs-keyword">if</span> (<span class="hljs-string">'serviceWorker'</span> <span class="hljs-keyword">in</span> navigator) &#123;
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'load'</span>, <span class="hljs-function">() =></span> &#123;
    navigator.serviceWorker
      .register(<span class="hljs-string">'/service-worker.js'</span>)
      .then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'sw注册成功了~'</span>);
      &#125;)
      .catch(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'sw注册失败了~'</span>);
      &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h1 data-id="heading-22">总结</h1>
<p>觉得写得好的，对你有帮助的，可以分享给身边人，<strong>知识越分享越多，千万不要吝啬呀</strong></p>
<p>后续更新前端其它知识总结，请关注我，整理好，分享给你们，我们一起学前端</p></div>  
</div>
            