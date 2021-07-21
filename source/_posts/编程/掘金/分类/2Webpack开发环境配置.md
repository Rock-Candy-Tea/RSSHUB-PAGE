
---
title: '2.Webpack开发环境配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=76'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 22:47:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=76'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 前言</h2>
<blockquote>
<p>回顾：<br>
<a href="https://link.juejin.cn/?target=%27.%2F..%2F1.webpack%25E5%2588%259D%25E8%25AF%2586.md" target="_blank" title="'./../1.webpack%E5%88%9D%E8%AF%86.md" ref="nofollow noopener noreferrer">webpack初识</a>简单介绍了webpack的五大概念，也一起写了两个例子。我们知道，webpack自身只能处理js, json文件，其他类型的文件需要配合loader 或 plugin；我们还知道，loader 和 plugin 需要先用<code>npm install</code>下载下来 (当然还有其他的下载方式) 。<br>
如果不记得了，可以回去复习一下~</p>
</blockquote>
<p>本文将会从文件出发，根据文件的类型去讲如何打包，需要使用哪些loader或plugin。</p>
<p>从篇幅考虑，只会列出必要的代码，完整的代码在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFE-Huang%2FStudyNotes%2Ftree%2Fmaster%2F6.%2520%25E5%25B7%25A5%25E5%2585%25B7%2FWebpack%2F%25E4%25BB%25A3%25E7%25A0%2581%2F2.webpack%25E5%25BC%2580%25E5%258F%2591%25E7%258E%25AF%25E5%25A2%2583%25E9%2585%258D%25E7%25BD%25AE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FE-Huang/StudyNotes/tree/master/6.%20%E5%B7%A5%E5%85%B7/Webpack/%E4%BB%A3%E7%A0%81/2.webpack%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE" ref="nofollow noopener noreferrer">这里</a></p>
<h2 data-id="heading-1">2. 资源打包</h2>
<h3 data-id="heading-2">2.1. 打包样式资源</h3>
<p>我们通常使用css, less, sass来编写样式，打包不同类型的样式资源也需要使用不同的loader。</p>
<h4 data-id="heading-3">用到的loader</h4>
<ul>
<li><strong>.css文件：</strong> <code>style-loader, css-loader</code>；
<ul>
<li><code>css-loader</code>：将css文件转换成commonjs模块加载到js中，css代码被转换成了样式字符串。（转换后得到的commonjs模块可以理解为：用js给元素动态添加样式的那种代码）；</li>
<li><code>style-loader</code>：创建<code>style标签</code>，将<code>css-loader</code>生成的样式资源插入进去，添加到head中，使样式生效。</li>
</ul>
</li>
<li><strong>.less文件：</strong> <code>style-loader, css-loader, less-loader</code>；
<ul>
<li><code>less-loader</code>：将less文件编译成css文件；</li>
<li>注：要想<code>less-loader</code>生效，还需要下载<code>less</code> (<code>npm install less -D</code>)。</li>
</ul>
</li>
<li><strong>.scss/.sass文件：</strong> <code>style-loader, css-loader, sass-loader</code>；
<ul>
<li><code>sass-loader</code>：将sass或scss文件编译成css文件；</li>
<li>注：要想<code>sass-loader</code>生效，还需要下载<code>node-sass</code> (<code>npm install node-sass -D</code>)。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-4">webpack配置</h4>
<p>配置loader时，不同的文件需要分开写rule。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>

<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'dist'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
          <span class="hljs-string">'style-loader'</span>,
          <span class="hljs-string">'css-loader'</span>
        ]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: [
          <span class="hljs-string">'style-loader'</span>,
          <span class="hljs-string">'css-loader'</span>,
          <span class="hljs-string">'less-loader'</span>
        ]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.s[ac]ss$/</span>,
        use: [
          <span class="hljs-string">'style-loader'</span>,
          <span class="hljs-string">'css-loader'</span>,
          <span class="hljs-string">'sass-loader'</span>,
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.2. 打包html资源</h3>
<p>打包html资源需要使用一个plugin: <code>html-webpack-plugin</code>。</p>
<h4 data-id="heading-6">用到的plugin</h4>
<p><code>html-webpack-plugin</code>：</p>
<ul>
<li>不传参的情况：
<ul>
<li>new HTMLWebpackPlugin()：会在配置的output文件夹创建一个空的html, 自动引入打包输出的所有资源，包括js, css...；</li>
<li>设置参数template：复制设置的'./src/index.html'文件到配置的output文件夹，并自动引入打包输出的所有资源。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-7">webpack配置</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HTMLWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>),
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: []
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">/**
     * html-webpack-plugin
     *    1) 不传参的情况 - new HTMLWebpackPlugin()：会在配置的output文件夹创建一个空的html, 自动引入打包输出的所有资源，包括js, css...
     *    2) 参数template：复制设置的'./src/index.html'文件到配置的output文件夹，并自动引入打包输出的所有资源
     */</span>
    <span class="hljs-keyword">new</span> HTMLWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
    &#125;),
  ],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2.3. 打包图片资源</h3>
<h4 data-id="heading-9">用到的loader</h4>
<ul>
<li><code>url-loader</code>：用来处理css中的图片资源，但<strong>不能处理html中的img标签</strong>：
<ul>
<li><code>url-loader</code>基于<code>file-loader</code>运行，所以需下载<code>url-loader 和 file-loader</code>；</li>
<li>可以通过<code>options</code>给loader增加配置项（本文仅介绍案例中用到的）：
<ul>
<li>limit: 图片大小限制，超过的就会被处理成base64；</li>
<li>esModule：url-loader默认使用es6解析。设置为false：关闭它的es6模块化，使用commonjs解析;</li>
<li>name: 给图片进行重命名。[hash:10] - 取图片的hash的前10位；[ext] - 取文件原来的拓展名。</li>
</ul>
</li>
</ul>
</li>
<li><code>html-loader</code>：处理html文件的img图片（负责引入img，从而能被url-loader进行处理）：
<ul>
<li>也可以通过<code>options</code>给loader增加配置项：
<ul>
<li>esModule：设置为false：关闭它的es6模块化，使用commonjs解析；</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-10">webpack配置</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: [
          <span class="hljs-string">'style-loader'</span>,
          <span class="hljs-string">'css-loader'</span>,
          <span class="hljs-string">'less-loader'</span>
        ]
      &#125;,
      &#123;
        <span class="hljs-comment">/**
         * url-loader:
         *    1）处理css中的图片资源，注意：不能处理html中的img标签
         *    2）url-loader基于file-loader运行，所以需下载url-loader和file-loader
         *    3）options：loader的其他配置
         *        limit: 图片大小小于8Kb，就会被处理成base64；
         *        esModule：url-loader默认使用es6解析。设置为false：关闭它的es6模块化，使用commonjs解析;
         *        name: 给图片进行重命名。[hash:10] - 取图片的hash的前10位；[ext] - 取文件原来的拓展名。
         */</span>
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpg|png|gif|jpeg)$/</span>,
        loader: <span class="hljs-string">'url-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">limit</span>: <span class="hljs-number">8</span> * <span class="hljs-number">1024</span>,
          <span class="hljs-attr">esModule</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>
        &#125;
      &#125;,
      &#123;
        <span class="hljs-comment">/**
         * html-loader: 处理html文件的img图片（负责引入img，从而能被url-loader进行处理）
         */</span>
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.html$/</span>,
        loader: <span class="hljs-string">'html-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">esModule</span>: <span class="hljs-literal">false</span>
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
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">2.4. 打包其他资源</h3>
<p>比如，项目中经常会用到的字体图标文件~</p>
<h4 data-id="heading-12">使用的loader：<code>file-loader</code></h4>
<h4 data-id="heading-13">webpack配置</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/indes.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        <span class="hljs-comment">// 写法一：</span>
        <span class="hljs-comment">// use: ['style-loader', 'css-loader']</span>
        <span class="hljs-comment">// 写法二：</span>
        use: [
          &#123; <span class="hljs-attr">loader</span>: <span class="hljs-string">'style-loader'</span> &#125;,
          &#123; <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span> &#125;
        ]
      &#125;,
      &#123;
        <span class="hljs-comment">// exclude：命中除了exclude值之外的文件</span>
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/\.(css|js|html|png|gif|jpg)$/</span>,
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
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">3. 开发环境配置 - devServer</h2>
<h3 data-id="heading-15">3.1. devServer简单介绍</h3>
<p><strong>devServer</strong>：开发服务器，用来自动化（自动编译，自动打开浏览器，自动刷新浏览器）</p>
<p><strong>特点</strong>：只会在内存中编译打包，不会有任何输出（不会在项目中新建一个文件夹）</p>
<p><strong>如何启动</strong>：</p>
<ul>
<li><code>npx webpack serve(webpack-cli: 4.x)</code>;</li>
<li><code>npx webpack-dev-server(webpack-cli 3.x)</code>;</li>
</ul>
<h3 data-id="heading-16">3.2. webpack配置</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/indes.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: []
  &#125;,
  <span class="hljs-attr">plugins</span>: [],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: resolve(__dirname, <span class="hljs-string">'build'</span>), <span class="hljs-comment">// 项目构建后的路径</span>
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否使用gzip压缩</span>
    <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>, <span class="hljs-comment">// 设置端口号</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 是否自动打开浏览器</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">4. 思考和总结</h2>
<h3 data-id="heading-18">4.1. 打包不同类型的文件</h3>
<ul>
<li>.css文件：<code>style-loader</code>, <code>css-loader</code>;</li>
<li>.less文件：<code>style-loader</code>, <code>css-loader</code>, <code>less-node</code>;（还需安装<code>less</code>）</li>
<li>.scss/sass文件：<code>style-loader</code>, <code>css-loader</code>, <code>sass-loader</code>;（还需安装<code>node-sass</code>）</li>
<li>.html文件：<code>html-webpack-plugin</code>;</li>
<li>图片文件(.png/.jpg/.jepg/.gif等)：<code>url-loader</code>, <code>html-loader</code>;</li>
<li>其他文件：<code>file-loader</code>。</li>
</ul>
<h3 data-id="heading-19">4.2. 配置loader的不同写法</h3>
<p>注意到了吗，本文中配置loader用到了不同的写法。总的来说，一个loader如果有options配置，就单独分来写。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/indes.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'built.js'</span>,
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        <span class="hljs-comment">// 写法一：</span>
        <span class="hljs-comment">// use: ['style-loader', 'css-loader']</span>
        <span class="hljs-comment">// 写法二：</span>
        use: [
          &#123; <span class="hljs-attr">loader</span>: <span class="hljs-string">'style-loader'</span> &#125;,
          &#123; <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span> &#125;
        ]
      &#125;,
      &#123;
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/\.(css|js|html|png|gif|jpg)$/</span>,
        <span class="hljs-comment">// 写法三：</span>
        loader: <span class="hljs-string">'file-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>
        &#125;
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">4.3. 思考</h3>
<p>尝试一下将这些配置串起来写个demo吧？写完我们可以对对答案哦。我的作业放在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFE-Huang%2FStudyNotes%2Ftree%2Fmaster%2F6.%2520%25E5%25B7%25A5%25E5%2585%25B7%2FWebpack%2F%25E4%25BB%25A3%25E7%25A0%2581%2F2.webpack%25E5%25BC%2580%25E5%258F%2591%25E7%258E%25AF%25E5%25A2%2583%25E9%2585%258D%25E7%25BD%25AE%2F08.%25E5%25BC%2580%25E5%258F%2591%25E7%258E%25AF%25E5%25A2%2583%25E9%2585%258D%25E7%25BD%25AE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FE-Huang/StudyNotes/tree/master/6.%20%E5%B7%A5%E5%85%B7/Webpack/%E4%BB%A3%E7%A0%81/2.webpack%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE/08.%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE" ref="nofollow noopener noreferrer">这里</a>了~</p></div>  
</div>
            