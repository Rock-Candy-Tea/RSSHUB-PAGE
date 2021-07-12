
---
title: '2021年必须要掌握的webpack5最佳配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4537'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 21:05:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=4537'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>2021年啦，对webpack构建还是<code>cli</code>一揽子计划（啥也不懂），结合官网，决定系统性的学习一下<code>webpack</code>，了解一下<code>webpack</code>之美（生活所迫）</p>
<h1 data-id="heading-1">1、<code>webpack</code>是什么</h1>
<p>本质上，<code>webpack</code> 是一个用于现代 <code>JavaScript</code> 应用程序的 静态模块打包工具。当 <code>webpack</code> 处理应用程序时，它会在内部构建一个 依赖图(<code>dependency graph</code>)，此依赖图对应映射到项目所需的每个模块，并生成一个或多个 <code>bundle</code>。</p>
<p><code>module</code> -> <code>chunk</code> -> <code>bundle</code></p>
<h1 data-id="heading-2">2、初始化项目</h1>
<p>新建项目名，任意位置，任意名称（建议英文），新建文件夹 <code>mulei</code></p>
<p>初始化项目</p>
<pre><code class="hljs language-js copyable" lang="js">npm init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装 <code>webpack</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i webpack webpack-cli -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前安装版本</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^5.43.0"</span>,
<span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^4.7.2"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>入口文件默认是 <code>./src/index.js</code>，也可以在 <code>webpack.config.js</code> 配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从 v4.0.0 开始，webpack 可以不用再引入一个配置文件来打包项目
直接运行 <code>webpack</code> 即可走默认输出 <code>dist/main.js</code></p>
<ul>
<li>运行当前目录下的 <code>webpack</code> 需要使用 <code>npm</code> 内置的包处理器 <code>npx</code> ，<code>npx webpack</code> 会直接找项目的/node_modules/.bin/里面的命令执行</li>
<li><code>npx webpack</code> 不指定模式 <code>mode</code> 的情况下，默认走的是 <code>production</code> ，开发环境需要执行<code>npx webpack --mode development</code></li>
</ul>
<h1 data-id="heading-3">3、拆分配置和 <code>merge</code></h1>
<p><code>development</code>(开发环境) 和 <code>production</code>(生产环境) 这两个环境下的构建目标存在着巨大差异。在开发环境中，我们需要：强大的 <code>source map</code> 和一个有着 <code>live reloading</code>(实时重新加载) 或 <code>hot module replacement</code>(热模块替换) 能力的 <code>localhost server</code>。而生产环境目标则转移至其他方面，关注点在于压缩 <code>bundle</code>、更轻量的 <code>source map</code>、资源优化等，通过这些优化方式改善加载时间。由于要遵循逻辑分离，我们通常建议为每个环境编写彼此独立的 <code>webpack</code> 配置。</p>
<p>防止不同环境下配置有重复的配置，需要抽离出来公共的配置，然后使用 <code>webpack-merge</code> 工具，将公共配置和环境特有配置进行合并。</p>
<p>在根目录下新建 <code>build</code> 文件夹，里面新建公共配置 <code>webpack.common.js</code>、开发环境配置<code>webpack.dev.js</code>、生产环境配置 <code>webpack.prod.js</code>。</p>
<p>安装  <code>webpack-merge</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i webpack-merge -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置<code>webpack.dev.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-merge"</span>)
<span class="hljs-keyword">const</span> webpackCommon = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common.js'</span>)

<span class="hljs-built_in">module</span>.exports = merge(webpackCommon, &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那怎么才能运行 <code>webpack.dev.js</code>呢？为了方便，需要在 <code>package.js</code> 的 <code>scripts</code>中配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack --config build/webpack.dev.js"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack --config build/webpack.prod.js"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">4、html自动构建</h1>
<h2 data-id="heading-5"><code>html-webpack-plugin</code></h2>
<p>在根目录新建文件夹 <code>public</code>，里面新建 <code>index.html</code> 文件，那我们怎么把 <code>index.html</code> 打包到 <code>dist</code> 文件夹内，并引入输出的 <code>main.js</code> 呢？通过使用 <code>html-webpack-plugin</code> 插件生成一个 <code>HTML5</code> 文件， 在 <code>body</code> 中使用 <code>script</code> 标签引入你所有 <code>webpack</code> 生成的 <code>bundle</code>。</p>
<p>安装 <code>html-webpack-plugin</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i html-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于无论开发环境还是生产环境都需要构建 <code>html</code>，所以把 <code>html-webpack-plugin</code> 配置在公共配置 <code>webpack.common.js</code> 内</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin()
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>html-webpack-plugin</code>插件在没有任何配置下，默认在 <code>dist</code> 文件夹内生成 <code>index.html</code></p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Webpack App</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script defer src="main.js?e68f6906a7f78bef340d"></script>
</head>

<body>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是生成的默认的 <code>index.html</code> 和我们自己创建的 <code>index.html</code> 还是有区别的，此时需要配置参数 <code>template</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">"./public/index.html"</span>,
            <span class="hljs-attr">hash</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 为CSS文件和JS文件引入时，添加唯一的hash，破环缓存非常有用</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6"><code>copy-webpack-plugin</code></h2>
<p>将已存在的单个文件或整个目录复制到构建目录，比如网站图标</p>
<p>安装 <code>copy-webpack-plugin</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i copy-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.common.js</span>
<span class="hljs-keyword">const</span> CopyPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"copy-webpack-plugin"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> CopyPlugin(&#123;
            <span class="hljs-attr">patterns</span>: [
                &#123;
                    <span class="hljs-attr">from</span>: <span class="hljs-string">"public/favicon.ico"</span>,
                    <span class="hljs-attr">to</span>: <span class="hljs-string">"favicon.ico"</span>
                &#125;
            ]
        &#125;),
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">5、编译JS文件</h1>
<p>使用 Babel 加载 ES2015+ 代码并将其转换为 ES5</p>
<p>需要安装以下插件</p>
<pre><code class="hljs language-js copyable" lang="js">npm install babel-loader @babel/core @babel/preset-env -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>babel</code> 配置既可以在配置文件中 <code>webpack.common.js</code> 配置，也可以在 <code>.babelrc</code> 中配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.common.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                use: &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader?cacheDirectory'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-string">"presets"</span>: [<span class="hljs-string">"@babel/preset-env"</span>]
                    &#125;
                &#125;,
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;,
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// .babelrc</span>
&#123;
    <span class="hljs-string">"presets"</span>: [<span class="hljs-string">"@babel/preset-env"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中有2个提升构建速度的知识点：</p>
<ul>
<li><code>include</code> 包含、<code>exclude</code> 排除文件，减少编译文件</li>
<li><code>cacheDirectory</code> 用来缓存 loader 的执行结果。之后的 webpack 构建，将会尝试读取缓存，默认的缓存目录 <code>node_modules/.cache/babel-loader</code></li>
</ul>
<h1 data-id="heading-8">6、<code>CSS</code> 预处理语言和 <code>CSS</code></h1>
<h2 data-id="heading-9">编译</h2>
<p><code>webpack</code>是不能直接编译样式文件的，需要使用<code>loader</code></p>
<p>预处理语言以 <code>less</code> 为例，主要分为4步：</p>
<ul>
<li><code>less-loader</code>： <code>webpack</code> 将 <code>Less</code> 编译为 <code>CSS</code> 的 <code>loader</code></li>
</ul>
<p>安装 <code>less</code> 和 <code>less-loader</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i less less-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>postcss-loader</code>：使用 <code>PostCSS</code> 处理 <code>CSS</code> 的 <code>loader</code>，<code>postcss-preset-env</code> 自动添加兼容浏览器样式前缀，需要设置兼容浏览器版本</li>
</ul>
<p><code>postcss-loader</code> 的属性 <code>postcssOptions</code> 允许设置插件，也可以在 <code>postcss.config.js</code>中配置</p>
<p>安装 <code>postcss-loader</code> 和 <code>postcss-preset-env</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i postcss-loader postcss-preset-env -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>css-loader</code>：对 <code>@import</code> 和 <code>url()</code> 进行处理</li>
</ul>
<p>安装 <code>css-loader</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i css-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>style-loader</code>：把 <code>CSS</code> 插入到 <code>DOM</code> 中，通过 <code>style</code> 标签的方式添加到了<code>html</code> 文件的 <code>head</code> 标签中</li>
</ul>
<p>安装 <code>style-loader</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i style-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了方便大家可以一并安装：</p>
<pre><code class="hljs language-js copyable" lang="js">npm i less less-loader postcss-loader postcss-preset-env css-loader style-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>执行顺序从右到左，从下到上</strong></p>
</blockquote>
<p>详细配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.dev.js</span>
<span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-merge"</span>)
<span class="hljs-keyword">const</span> webpackCommon = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common.js'</span>)

<span class="hljs-built_in">module</span>.exports = merge(webpackCommon, &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [
                    <span class="hljs-string">"style-loader"</span>,
                    <span class="hljs-string">"css-loader"</span>,
                    <span class="hljs-string">"postcss-loader"</span>
                    <span class="hljs-comment">// &#123;</span>
                    <span class="hljs-comment">//     loader: "postcss-loader",</span>
                    <span class="hljs-comment">//     options: &#123;</span>
                    <span class="hljs-comment">//         postcssOptions: &#123;</span>
                    <span class="hljs-comment">//             plugins: [</span>
                    <span class="hljs-comment">//                 [</span>
                    <span class="hljs-comment">//                     "postcss-preset-env",</span>
                    <span class="hljs-comment">//                     &#123;</span>
                    <span class="hljs-comment">//                         browsers: ["last 1 version", "> 1%", "IE 10"]</span>
                    <span class="hljs-comment">//                     &#125;</span>
                    <span class="hljs-comment">//                 ]</span>
                    <span class="hljs-comment">//             ]</span>
                    <span class="hljs-comment">//         &#125;</span>
                    <span class="hljs-comment">//     &#125;</span>
                    <span class="hljs-comment">// &#125;</span>
                ]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
                use: [
                    <span class="hljs-string">"style-loader"</span>,
                    <span class="hljs-string">"css-loader"</span>,
                    <span class="hljs-string">"postcss-loader"</span>,
                    <span class="hljs-comment">// &#123;</span>
                    <span class="hljs-comment">//     loader: "postcss-loader",</span>
                    <span class="hljs-comment">//     options: &#123;</span>
                    <span class="hljs-comment">//         postcssOptions: &#123;</span>
                    <span class="hljs-comment">//             plugins: [</span>
                    <span class="hljs-comment">//                 [</span>
                    <span class="hljs-comment">//                     "postcss-preset-env",</span>
                    <span class="hljs-comment">//                     &#123;</span>
                    <span class="hljs-comment">//                         browsers: ["last 1 version", "> 1%", "IE 10"]</span>
                    <span class="hljs-comment">//                     &#125;</span>
                    <span class="hljs-comment">//                 ]</span>
                    <span class="hljs-comment">//             ]</span>
                    <span class="hljs-comment">//         &#125;</span>
                    <span class="hljs-comment">//     &#125;</span>
                    <span class="hljs-comment">// &#125;,</span>
                    <span class="hljs-string">"less-loader"</span>
                ]
            &#125;
        ]
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// postcss.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        [
            <span class="hljs-string">"postcss-preset-env"</span>,
            &#123;
                <span class="hljs-attr">browsers</span>: [<span class="hljs-string">"last 1 version"</span>, <span class="hljs-string">"> 1%"</span>, <span class="hljs-string">"IE 10"</span>]
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了保证不同工具公用一套浏览器兼容版本，建议在根目录新建 <code>.browserslistrc</code> 文件</p>
<pre><code class="hljs language-js copyable" lang="js">last <span class="hljs-number">1</span> version
> <span class="hljs-number">1</span>%
IE <span class="hljs-number">10</span> # sorry
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">抽取 <code>CSS</code></h2>
<p>随着项目越来越复杂，更多的css插入到head中，开发环境还可以忍受，生产环境就太杂乱无章了，所以生产环境借用 <code>mini-css-extract-plugin</code> 插件将 CSS 提取到单独的文件中
安装 <code>mini-css-extract-plugin</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i mini-css-extract-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.prod.js</span>
<span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-merge"</span>)
<span class="hljs-keyword">const</span> webpackCommon = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common.js'</span>)
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mini-css-extract-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = merge(webpackCommon, &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"production"</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [
                    MiniCssExtractPlugin.loader,
                    <span class="hljs-string">"css-loader"</span>,
                    <span class="hljs-string">"postcss-loader"</span>
                ]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
                use: [
                    MiniCssExtractPlugin.loader,
                    <span class="hljs-string">"css-loader"</span>,
                    <span class="hljs-string">"postcss-loader"</span>,
                    <span class="hljs-string">"less-loader"</span>
                ]
            &#125;,
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
            <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/style.[contenthash:8].css'</span>
        &#125;)
    ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11"><code>CSS</code> 压缩</h2>
<p>现在可以把样式单独抽离了，但是代码并没有压缩，使用插件 <code>css-minimizer-webpack-plugin</code> 启动 <code>CSS</code> 压缩
安装 <code>css-minimizer-webpack-plugin</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i css-minimizer-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过配置 <code>optimization.minimizer</code>来添加插件 <code>css-minimizer-webpack-plugin</code>，但它会覆盖默认的压缩工具，所以需要在 <code>webpack@5</code> 中，可以使用 <code>...</code> 语法来扩展现有的 minimizer（即 <code>terser-webpack-plugin</code>）</p>
<p>具体配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.prod.js</span>
<span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-merge"</span>)
<span class="hljs-keyword">const</span> webpackCommon = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common.js'</span>)
<span class="hljs-keyword">const</span> CssMinimizerPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"css-minimizer-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = merge(webpackCommon, &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"production"</span>,
    <span class="hljs-attr">optimization</span>: &#123;
        <span class="hljs-attr">minimizer</span>: [
            <span class="hljs-comment">// 在 webpack@5 中，你可以使用 `...` 语法来扩展现有的 minimizer（即 `terser-webpack-plugin`），将下一行取消注释</span>
            <span class="hljs-string">`...`</span>,
            <span class="hljs-keyword">new</span> CssMinimizerPlugin(),
        ],
    &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">7、资源模块</h1>
<p>资源模块(<code>asset module</code>)是一种模块类型，它允许使用资源文件（字体，图标等）而无需配置额外 <code>loader</code>。</p>
<p>包括四种类型：</p>
<ul>
<li><code>asset/resource</code> 发送一个单独的文件并导出 <code>URL</code>。之前通过使用 <code>file-loader</code> 实现。</li>
<li><code>asset/inline</code> 导出一个资源的 <code>data URI</code>。之前通过使用 <code>url-loader</code> 实现。</li>
<li><code>asset/source</code> 导出资源的源代码。之前通过使用 <code>raw-loader</code> 实现。</li>
<li><code>asset</code> 在导出一个 <code>data URI</code> 和发送一个单独的文件之间自动选择。之前通过使用 <code>url-loader</code>，并且配置资源体积限制实现。</li>
</ul>
<p>它们替换了 <code>url-loader</code> 和 <code>file-loader</code> 处理字体图片的能力。</p>
<p>我设置的资源类型为 <code>asset</code>，默认以 <code>images/[hash][ext][query]</code> 格式输出在dist文件夹内，那它在哪里配置呢？两种方式如下：</p>
<ul>
<li>设置 <code>output.assetModuleFilename</code> 来修改默认输出位置</li>
<li>设置 <code>Rule.generator.filename</code>，给不同的类型文件设置不同的输出位置，仅适用于 <code>asset</code> 和 <code>asset/resource</code> 模块类型。</li>
</ul>
<p><code>webpack</code> 将按照默认条件，自动地在 <code>resource</code> 和 <code>inline</code> 之间进行选择：小于 <code>8kb</code> 的文件，将会视为 <code>inline</code> 模块类型，否则会被视为 <code>resource</code> 模块类型。</p>
<p>可以通过在 <code>webpack</code> 配置的 <code>module rule</code> 层级中，设置 <code>Rule.parser.dataUrlCondition.maxSize</code> 选项来修改此条件</p>
<p>具体配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.common.js</span>
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">"[name].[contenthash:8].js"</span>,
        <span class="hljs-attr">clean</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// assetModuleFilename: 'images/[hash][ext][query]'</span>
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                use: &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader?cacheDirectory'</span>,
                &#125;,
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpg|gif|jpeg|webp|svg|eot|ttf|woff|woff2)$/</span>,
                type: <span class="hljs-string">'asset'</span>,
                <span class="hljs-attr">generator</span>: &#123;
                    <span class="hljs-comment">// 与 output.assetModuleFilename 相同，并且仅适用于 asset 和 asset/resource 模块类型</span>
                    <span class="hljs-comment">// filename: "images/[hash][ext][query]"</span>
                &#125;,
                <span class="hljs-attr">parser</span>: &#123;
                    <span class="hljs-attr">dataUrlCondition</span>: &#123;
                        <span class="hljs-attr">maxSize</span>: <span class="hljs-number">8</span> * <span class="hljs-number">1024</span> <span class="hljs-comment">// 默认是8kb</span>
                    &#125;
                &#125;,
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">"./public/index.html"</span>,
            <span class="hljs-attr">hash</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 为CSS文件和JS文件引入时，添加唯一的hash，破环缓存非常有用</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">8、出口配置</h1>
<h2 data-id="heading-14"><code>output.filename</code></h2>
<p><code>output.filename</code> 决定每个输出bundle的名称，一般以 <code>bundle.[contenthash:8].js</code> 命名；多入口的情况，一般以 <code>[name].[contenthash:8].js</code></p>
<p>添加 <code>contenthash</code>，当内容有修改的情况，它是随时变化的，这样浏览器在访问资源的时候，就不会走缓存。</p>
<h2 data-id="heading-15"><code>output.clean</code></h2>
<p>设置为 <code>true</code>，打包前清空输出目录</p>
<p>排除某些文件使用 <code>keep</code> 属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">clean</span>: &#123;
            <span class="hljs-attr">keep</span>: <span class="hljs-regexp">/assets/</span>
        &#125;,
    &#125;,
&#125;;

<span class="hljs-comment">// or</span>

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">clean</span>: &#123;
            keep (asset) &#123;
                <span class="hljs-comment">// 如果文件较多，可以设置一个白名单</span>
                <span class="hljs-keyword">return</span> asset.includes(<span class="hljs-string">'assets'</span>);
            &#125;,
        &#125;,
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">9、开发服务器</h1>
<h2 data-id="heading-17"><code>webpack-dev-server</code></h2>
<p><code>webpack-dev-server</code> 可用于快速开发应用程序。</p>
<p>安装 <code>webpack-dev-server</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i webpack-dev-server -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更改 <code>package.json</code> 文件的 <code>scripts</code>，将 <code>dev</code> 改为 <code>webpack serve --config build/webpack.dev.js</code>，运行 <code>npm run dev</code>，访问 <code>http://localhost:8080/</code> 可以看到自己的页面</p>
<p>以下属性比较常用：</p>
<ul>
<li><code>port</code> 设置端口号</li>
<li><code>proxy</code> 启用代理</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">proxy</span>: &#123;
            <span class="hljs-string">'/api'</span>: <span class="hljs-string">'http://localhost:3000'</span>,
        &#125;,
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对 <code>/api/users</code> 的请求会将请求代理到 <code>http://localhost:3000/api/users</code></p>
<p>如果接口没有 <code>/api</code>，则需要重写路径</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">proxy</span>: &#123;
            <span class="hljs-string">'/api'</span>: &#123;
                <span class="hljs-attr">target</span>: <span class="hljs-string">'http://localhost:3000'</span>,
                <span class="hljs-attr">pathRewrite</span>: &#123; <span class="hljs-string">'^/api'</span>: <span class="hljs-string">''</span> &#125;,
            &#125;,
        &#125;,
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>hot</code> 启用 <code>webpack</code> 的 <code>Hot Module Replacement</code> 功能</li>
</ul>
<p>要完全启用 <code>HMR</code> ，需要 <code>webpack.HotModuleReplacementPlugin</code>。如果使用 <code>--hot</code> 选项启动 <code>webpack</code> 或 <code>webpack-dev-server</code>，该插件将自动添加</p>
<h2 data-id="heading-18"><code>HRM</code></h2>
<p>模块热替换，允许在运行时更新所有类型的模块，而无需完全刷新。
具体设置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.dev.js</span>
<span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-merge"</span>)
<span class="hljs-keyword">const</span> webpackCommon = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common.js'</span>)
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>)

<span class="hljs-built_in">module</span>.exports = merge(webpackCommon, &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [
                    <span class="hljs-string">"style-loader"</span>,
                    <span class="hljs-string">"css-loader"</span>,
                    <span class="hljs-string">"postcss-loader"</span>
                ]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
                use: [
                    <span class="hljs-string">"style-loader"</span>,
                    <span class="hljs-string">"css-loader"</span>,
                    <span class="hljs-string">"postcss-loader"</span>,
                    <span class="hljs-string">"less-loader"</span>
                ]
            &#125;
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> webpack.HotModuleReplacementPlugin()
    ],
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">proxy</span>: &#123;
            <span class="hljs-string">'/api'</span>: <span class="hljs-string">'http://localhost:3000'</span>,
        &#125;,
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>此时热更新并不能生效，需要设置 <code>target</code> 为 <code>web</code>，因为当存在 <code>.browserslistrc</code> 文件时会根据配置推荐出运行环境</p>
</blockquote>
<p>之后修改样式文件不会重新刷新页面，修改js文件，页面又重新刷新了</p>
<p>需要在 <code>index.js</code> 配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(<span class="hljs-built_in">module</span> && <span class="hljs-built_in">module</span>.hot) &#123;
    <span class="hljs-built_in">module</span>.hot.accept() <span class="hljs-comment">// 接受自更新</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">10、devtool配置</h1>
<p>当代码中出现错误时，却找不到出现错误的具体文件和具体行，这时就需要选择一种 <code>source map</code> 格式来增强调试过程。</p>
<p>开发环境，需要知道具体的报错文件和具体行，并需要源代码快速的找到报错具体位置，所以配置 <code>eval-cheap-module-source-map</code></p>
<p>生产环境，需要知道具体的报错文件和具体行，但并不需要暴露源代码，所以配置 <code>nosources-source-map</code></p>
<h1 data-id="heading-20">参考</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/" ref="nofollow noopener noreferrer">webpack官网</a></li>
<li><a href="https://juejin.cn/user/3368559358523944" target="_blank" title="https://juejin.cn/user/3368559358523944">刘小夕</a></li>
</ul>
<h1 data-id="heading-21">结语</h1>
<p>到此，<code>webpack</code>一些基础的配置已经完成，第一次研究 <code>webpack</code>，很多内容理解的可能不够深刻，欢迎大家批评指正。</p>
<p>码字不易，点赞、评论、收藏三连哟！</p></div>  
</div>
            