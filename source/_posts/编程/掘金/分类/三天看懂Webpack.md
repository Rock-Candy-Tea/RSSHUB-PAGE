
---
title: '三天看懂Webpack'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/506ed36ba3ab4874a0fb0fea6da9b53b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 02:03:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/506ed36ba3ab4874a0fb0fea6da9b53b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">Webpack-01</h1>
<h3 data-id="heading-1">在网页中会引用哪些常见的静态资源？</h3>
<ul>
<li>JS</li>
<li>.js .jsx .ts（TypeScript）</li>
<li>CSS</li>
<li>.css .less .sass .scss</li>
<li>Images</li>
<li>.jpg .png .gif .bmp .svg</li>
<li>字体文件（Fonts）</li>
<li>.svg .ttf .eot .woff .woff2</li>
<li>模板文件</li>
<li>.ejs .jade .vue【这是在webpack中定义组件的方式，推荐这么用】</li>
</ul>
<h3 data-id="heading-2">网页中引入的静态资源多了以后有什么问题？</h3>
<ol>
<li>一个前端项目里面可能有多个 .js, 多个 .css , 多个静态图片， 多个其他前端资源。 当一个页面需要加载多个 .js 的话，也会拖累整个页面的加载速度，因为我们要发起很多的二次请求；</li>
<li>要处理错综复杂的依赖关系，例如一些 js 资源彼此之间存在依赖关系。</li>
</ol>
<h3 data-id="heading-3">什么是webpack?</h3>
<ul>
<li>Webpack 是一个前端资源加载/打包工具（项目构建工具）。它将根据模块的依赖关系进行静态分析，然后将这些模块按照指定的规则生成对应的静态资源。</li>
<li>webpack 提供了友好的模块化支持，以及资源的合并、打包、压缩、混淆、处理 js 兼容问题、性能优化等强大的功能，从而让程序员把工作的重心放到具体的功能实现上，提高了开发效率和项目的可维护性。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.webpackjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.webpackjs.com/" ref="nofollow noopener noreferrer">webpack官网</a></li>
</ul>
<h3 data-id="heading-4">为什么要使用webpack</h3>
<ol>
<li>一个前端项目里面可能有多个 .js, 多个 .css , 多个静态图片， 多个其他前端资源。 当一个页面需要加载多个 .js 的话，也会拖累整个页面的加载速度，因为我们要发起很多的二次请求；</li>
<li>要处理错综复杂的依赖关系，例如一些 js 资源彼此之间存在依赖关系。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/506ed36ba3ab4874a0fb0fea6da9b53b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">## webpack安装的两种方式</h3>
<ol>
<li>运行<code>npm i webpack -g</code>全局安装webpack，这样就能在全局使用webpack的命令</li>
<li>在项目根目录中运行<code>npm i webpack --save-dev</code>安装到项目依赖中</li>
<li>查看webpack 信息 npm info webpack webpack -v</li>
</ol>
<h3 data-id="heading-6">初步使用webpack打包构建列表隔行变色案例</h3>
<ol>
<li>运行<code>npm init</code>初始化项目，使用npm管理项目中的依赖包</li>
<li>创建项目基本的目录结构</li>
<li>使用<code>cnpm i jquery --save</code>安装jquery类库</li>
<li>创建<code>main.js</code>并书写各行变色的代码逻辑：</li>
</ol>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">    <span class="hljs-keyword">import</span> $ <span class="hljs-keyword">from</span> <span class="hljs-string">'jquery'</span>
    <span class="hljs-comment">// 设置偶数行背景色，索引从0开始，0是偶数</span>
    $(<span class="hljs-string">'#list li:even'</span>).css(<span class="hljs-string">'backgroundColor'</span>,<span class="hljs-string">'lightblue'</span>);
    <span class="hljs-comment">// 设置奇数行背景色</span>
    $(<span class="hljs-string">'#list li:odd'</span>).css(<span class="hljs-string">'backgroundColor'</span>,<span class="hljs-string">'pink'</span>);
    
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>
<p>直接在页面上引用<code>main.js</code>会报错，因为浏览器不认识<code>import</code>这种高级的JS语法，需要使用webpack进行处理，webpack默认会把这种高级的语法转换为低级的浏览器能识别的语法；</p>
</li>
<li>
<p>运行<code>webpack 入口文件路径 -o 输出文件路径</code>对<code>main.js</code>进行处理：
webpack ./src/js/main.js -o ./dist/bundle.js -o === --output</p>
</li>
</ol>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">不通过配置文件打包方式
webpack4 默认不需要再创建webpack.config.js来配置打包的入口和出口；

默认情况下， webpack
入口为./src/index.js文件
出口为./dist/main.js文件
确保入口文件/src/index.js位置正确，在项目根目录下运行命令：
webpack  默认打包  (最新版的可以不用引入配置文件)
    
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">## 使用webpack的配置文件简化打包时候的命令</h3>
<ol start="0">
<li>在项目根目录中创建<code>webpack.config.js</code></li>
<li>由于运行webpack命令的时候，webpack需要指定入口文件和输出文件的路径，所以，我们需要在<code>webpack.config.js</code>中配置这两个路径：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// 导入处理路径的模块</span>
    <span class="hljs-keyword">var</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
​
    <span class="hljs-comment">// 导出一个配置对象，将来webpack在启动的时候，会默认来查找webpack.config.js，并读取这个文件中导出的配置对象，来进行打包处理</span>
    <span class="hljs-built_in">module</span>.exports = &#123;
        <span class="hljs-attr">entry</span>: path.resolve(__dirname, <span class="hljs-string">'src/js/main.js'</span>), <span class="hljs-comment">// 项目入口文件</span>
        <span class="hljs-comment">// 多入口</span>
        <span class="hljs-comment">// entry:['./src/js/index.js','./src/js/one.js'],</span>
        <span class="hljs-comment">//entry: &#123;</span>
            <span class="hljs-comment">//ind: './src/js/index.js',</span>
            <span class="hljs-comment">//on: './src/js/one.js'</span>
        <span class="hljs-comment">//&#125;,</span>
        <span class="hljs-attr">output</span>: &#123; <span class="hljs-comment">// 配置输出选项</span>
            <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>), <span class="hljs-comment">// 配置输出的路径</span>
            <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span> <span class="hljs-comment">// 配置输出的文件名</span>
        &#125;,
        <span class="hljs-comment">// 多出口</span>
        <span class="hljs-comment">//output: &#123;</span>
         <span class="hljs-comment">//   filename: 'js/webpack02.[name].js',</span>
         <span class="hljs-comment">//   path: path.resolve(__dirname, 'dist')</span>
        <span class="hljs-comment">//&#125;,</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            