
---
title: 'webpack 配置知其然知其所以然（持续更新...)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9512'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 01:06:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=9512'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">webpack核心模块</h1>
<ul>
<li>mode 环境配置，production、development、none三个值，默认production</li>
<li>entry 打包入口文件</li>
<li>output 打包出口文件</li>
<li>loader 文件解析</li>
<li>plugins 插件配置</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>                   <span class="hljs-comment">// 环境配置，production、development、none三个值，默认production</span>
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,             <span class="hljs-comment">// 打包入口文件</span>
  <span class="hljs-attr">output</span>: &#123;                            <span class="hljs-comment">// 打包出口文件</span>
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name]_[hash].js'</span>,
    <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">'./dist'</span>)
  &#125;,
  <span class="hljs-attr">module</span>: &#123;                            <span class="hljs-comment">// 文件loader配置</span>
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        loader: <span class="hljs-string">'babel-loader'</span>
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: []                         <span class="hljs-comment">// 插件配置                    </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">loader example</h1>
<h2 data-id="heading-2">js | jsx</h2>
<blockquote>
<p>npm install babel-loader @babel/core @babel/preset-env @babel/preset-react --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx)$/</span>,
        options: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">"babel-loader"</span>,
          <span class="hljs-attr">presets</span>: [
            <span class="hljs-string">"@babel/preset-env"</span>, <span class="hljs-comment">// es6+ => es5</span>
            <span class="hljs-string">"@babel/preset-react"</span>, <span class="hljs-comment">// jsx</span>
          ],
        &#125;,
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">css | less</h2>
<blockquote>
<p>npm install style-loader css-loader less-loadr less --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>], <span class="hljs-comment">// loader 从右往左执行</span>
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>, <span class="hljs-string">"less-loader"</span>], <span class="hljs-comment">// loader 从右往左执行</span>
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">watch</h1>
<blockquote>
<p>原理：轮询判断文件最后编辑时间是否变化，某个文件发生了变化，并不会立即告诉监听者，而生先缓存起来，等 aggregateTimeout 设置时间到了再执行</p>
</blockquote>
<p>两种设置方式：</p>
<p>1、npm scripts 带 --watch 参数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"watch"</span> : <span class="hljs-string">"webpack --watch"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、webpack 配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">watch</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// watch设置true才有效</span>
  <span class="hljs-attr">watchOptions</span>: &#123;
    <span class="hljs-comment">// 默认为空，不监听文件</span>
    <span class="hljs-attr">ignored</span>: <span class="hljs-regexp">/node_modules/</span>,
    <span class="hljs-comment">// 监听到变化后会等300ms再执行</span>
    aggregateTimeout: <span class="hljs-number">300</span>,
    <span class="hljs-comment">// 轮询监听文件，默认每秒轮询次数1000</span>
    <span class="hljs-attr">poll</span>: <span class="hljs-number">1000</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">热更新 HMR</h1>
<blockquote>
<p>热更新：使用 webpack-dev-server, WDS 不刷新浏览器，不输出文件，而是放在内存中；使用 webpack.HotModuleRepleacementPlugin 插件刷新浏览器</p>
</blockquote>
<ol>
<li>webpack 配置</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> webpack.HotModuleRepleacementPlugin()],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>npm scripts 配置</li>
</ol>
<p><strong>webpack 4+</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// package.json</span>
&#123;
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server --open --mode=development"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack 5+</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// package.json</span>
&#123;
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack server --open --mode=development"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">热更新原理</h2>
<p><strong>热更新有两个阶段：</strong></p>
<ol>
<li>启动阶段</li>
<li>文件改变更新阶段</li>
</ol>
<ul>
<li>Webpack Compile :将 js 编译成对应Bundle文件</li>
<li>HMR Server: 将热更新的文件输出给 HMR Runtime</li>
<li>Bundle Server： 提供文件在浏览器访问的服务</li>
<li>HMR Runtime： 会被注入到浏览器，更新文件的变化</li>
</ul>
<h1 data-id="heading-7">文件指纹</h1>
<blockquote>
<p>hash、 chunkhash、 contenthash</p>
</blockquote>
<ol>
<li>
<p>hash：和整个项目构建相关，项目相关文件发生变化就会改变</p>
</li>
<li>
<p>chunkhash: 和 webpack 入口 entr 入口文件有关，不同的 entry 会生成不同的 chunkhash 值</p>
</li>
<li>
<p>contenthash: 根据文件内容有关，只有文件改变才会改变</p>
</li>
</ol>
<h2 data-id="heading-8">js 文件指纹设置</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">"[name]_[chunkhash:8].js"</span>,
    <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">"./dist"</span>),
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">css 文件指纹设置</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mini-css-extract-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">"css-loader"</span>],
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">"css-loader"</span>, <span class="hljs-string">"less-loader"</span>],
      &#125;,
    ],
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">`[name]_[contenthash:8].css`</span>,
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">图片、文件指纹设置</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpeg|jpg|gif)$/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">"file-loader"</span>,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"[name]_[hash:8].[ext]"</span>,
          &#125;,
        &#125;,
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>设置 file-loade 的 name，使用 [hash]</p>
</blockquote>
<p><strong>文件相关占位符含义</strong></p>

































<table><thead><tr><th>占位符名称</th><th>含义</th></tr></thead><tbody><tr><td>[ext]</td><td>文件后缀名</td></tr><tr><td>[name]</td><td>文件名</td></tr><tr><td>[path]</td><td>文件相对路径</td></tr><tr><td>[folder]</td><td>文件所在的文件夹</td></tr><tr><td>[contenthash]</td><td>文件内容 hash， 默认 md5 生成</td></tr><tr><td>[hash]</td><td>文件内容 hash， 默认 md5 生成</td></tr></tbody></table>
<h1 data-id="heading-11">html、css、javascript 代码压缩</h1>
<h2 data-id="heading-12">html</h2>
<blockquote>
<p>npm install html-webpack-plugin --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">"./public/index.html"</span>,
      <span class="hljs-attr">filename</span>: <span class="hljs-string">"index.html"</span>,
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">css</h2>
<p><strong>webpack 4.+版本</strong></p>
<blockquote>
<p>npm install optimize-css-assets-webpack-plugin cssnano --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> OptimizeCssAssetsPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> cssnano = <span class="hljs-built_in">require</span>(<span class="hljs-string">'cssnano'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> OptimizeCssAssetsPlugin(&#123;
      <span class="hljs-attr">assetNameRegExp</span>: <span class="hljs-regexp">/\.css$/</span>,
      cssProcessor: cssnano,
    &#125;),
  ];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack 5.+版本</strong></p>
<blockquote>
<p>npm install css-minimizer-webpack-plugin --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CssMinimizerPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"css-minimizer-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">minimize</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">minimizer</span>: [
      <span class="hljs-keyword">new</span> CssMinimizerPlugin(&#123;
        <span class="hljs-attr">parallel</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 启用/禁用多进程并发执行</span>
      &#125;),
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">javascript</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> TerserPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"terser-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">minimize</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">minimizer</span>: [
      <span class="hljs-keyword">new</span> TerserPlugin(&#123;
        <span class="hljs-attr">parallel</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 启用/禁用多进程并发执行</span>
      &#125;),
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>mode: production 是开启 js 压缩</p>
</blockquote>
<h1 data-id="heading-15">清楚构建目录</h1>
<blockquote>
<p>npm install clean-webpack-plugin --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"clean-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> CleanWebpackPlugin()],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>webpack 5+ 使用 output.clean 设置</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">clean</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">css3 自动添加厂商前缀</h1>
<blockquote>
<p>npm install postcss-loader autoprefixer -save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
          <span class="hljs-string">"style-loader"</span>,
          <span class="hljs-string">"css-loader"</span>,
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">"postcss-loader"</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">postcssOptions</span>: &#123;
                <span class="hljs-attr">plugins</span>: [[<span class="hljs-string">"autoprefixer"</span>]],
              &#125;,
            &#125;,
          &#125;,
        ],
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">抽取公共资源</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">splitChunks</span>: &#123;
      <span class="hljs-attr">cacheGroups</span>: &#123;
        <span class="hljs-attr">vendors</span>: &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"vendors"</span>,
          <span class="hljs-attr">test</span>: <span class="hljs-regexp">/(react|teact-dom)/</span>,
          chunks: <span class="hljs-string">"all"</span>,
        &#125;,
      &#125;,
    &#125;,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-18">Tree Shaking 原理和分析</h1>
<p><strong>分析</strong>
代码中以下情况的代码会被 Tree Shaking</p>
<ol>
<li>代码不会被执行，不可到达</li>
<li>代码执行的结果不会被使用</li>
<li>代码只会影响死变量（只读不写）</li>
</ol>
<p><strong>原理</strong>
利用 es6 模块特点：</p>
<ol>
<li>只能作为顶层语句的出现</li>
<li>import 的模块名只能是字符串常量</li>
<li>import binding 是 immutable 的</li>
</ol>
<p>代码擦除：ugify 阶段删除无用代码</p>
<h1 data-id="heading-19">Scope Hoisting 原理和分析</h1>
<p><strong>分析</strong>
webpack 构建后对每个模块会包裹，增加构建后代码体积；构建后的代码存在大量闭包，运行时创建函数作用域，内存开销变得</p>
<p><strong>原理</strong>
构建时将模块引用按照引用顺序放在一个函数作用域里，然后适当的重命名防止变量名冲突</p>
<p>通过 Scope Hoisting 可以减少函数声明代码和内存开发</p>
<blockquote>
<p>webpack 4+版本默认已经集成，设置 mode: production, webpack 3 版本设置： new webpack.optimize.ModuleConcatenationPlugin()</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> webpack.optimize.ModuleConcatenationPlugin()],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">代码分割和动态 import</h1>
<blockquote>
<p>npm install @babel/plugin-syntax-dynamic-import --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// .babbelrc</span>
&#123;
  <span class="hljs-string">"presets"</span>: [],
  <span class="hljs-string">"plugins"</span>: [
    <span class="hljs-string">"@babel/plugin-syntax-dynamic-import"</span>
  ];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-21">构建速度和体积优化策略</h1>
<h2 data-id="heading-22">构建速度</h2>
<p><strong>分析 loader 和 plugin 耗时</strong></p>
<blockquote>
<p>npm install speed-measure-webpack-plugin --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> SpeedMeasurePlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"speed-measure-webpack-plugin"</span>);

<span class="hljs-keyword">const</span> smp = <span class="hljs-keyword">new</span> SpeedMeasurePlugin();

<span class="hljs-built_in">module</span>.exports = smp.wrap(&#123;
  <span class="hljs-comment">// webpackConfig</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>优化策略</strong></p>
<ol>
<li>多进程、多实例构建</li>
</ol>
<p><strong>推荐方案</strong></p>
<blockquote>
<p>npm install thread-loader --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">"thread-loader"</span>,
            <span class="hljs-attr">options</span>: [
              workders: <span class="hljs-literal">true</span>
            ],
          &#125;,
          <span class="hljs-string">'babel-loader'</span>
        ],
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>可选方案</strong></p>
<blockquote>
<p>npm install happypack --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Happypack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"happypack"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        use: [<span class="hljs-string">"happypack/loader"</span>],
      &#125;,
    ],
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> Happypack(&#123;
      <span class="hljs-attr">loaders</span>: [<span class="hljs-string">"babel-loader"</span>],
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>预编译</li>
</ol>
<blockquote>
<p>使用 Dllplugin 分离基础包</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: &#123;
      <span class="hljs-attr">library</span>: [
          <span class="hljs-string">'react'</span>,
          <span class="hljs-string">'react-dom'</span> <span class="hljs-comment">//分离的基础包</span>
      ]
  &#125;,
  <span class="hljs-attr">output</span>: &#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name]_[chunkhash:8].dll.js'</span>,
      <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">'./library'</span>),
      <span class="hljs-attr">library</span>: <span class="hljs-string">'[name]'</span>
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> <span class="hljs-keyword">new</span> webpackDllplugin(&#123;
       <span class="hljs-attr">name</span>: <span class="hljs-string">'[name]'</span>,
      <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">'manifest.json'</span>)
    &#125;)
  ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>DllReferencePlugin 引入 manifest.json</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> webpack.DllReferencePlugin(&#123;
      <span class="hljs-attr">manifest</span>: <span class="hljs-built_in">require</span>(<span class="hljs-comment">/* 预编译基础包路径 */</span>),
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">缓存</h2>
<ol>
<li>babel缓存 babel-loader?cacheDirectory=true</li>
<li>代码压缩缓存 zerser-webpack-plguin</li>
<li>模块缓存 hard-source-webpack-plugin</li>
</ol>
<blockquote>
<p>babel-loader</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        user: [&#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">cacheDirectory</span>: <span class="hljs-literal">true</span>
          &#125;
        &#125;]
      &#125;
    ]

  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>terser-webpack-plugin</p>
</blockquote>
<blockquote>
<p>hard-source-webpack-plugin</p>
</blockquote>
<h2 data-id="heading-24">缩小构建目标</h2>
<h2 data-id="heading-25">构建体积</h2>
<p><strong>包大小分析</strong></p>
<blockquote>
<p>npm install webpack-bundle-analyzer --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; BundleAnalyzerPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-bundle-analyzer"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> BundleAnalyzerPlugin()],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>优化策略</strong></p>
<ol>
<li>多进程并行压缩代码</li>
</ol>
<blockquote>
<p>npm install terser-webpack-plugin css-minimizer-webpack-plugin --save-dev</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">minimize</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">minimizer</span>: [
      <span class="hljs-keyword">new</span> CssMinimizerPlugin(&#123;
        <span class="hljs-attr">parallel</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 启用多进程并行压缩代码</span>
      &#125;),
      <span class="hljs-keyword">new</span> TerserPlugin(&#123;
        <span class="hljs-attr">parallel</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 启用/禁用多进程并行压缩代码</span>
      &#125;),
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            