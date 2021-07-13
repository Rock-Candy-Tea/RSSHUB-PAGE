
---
title: '我是这样搭建React+TS的通用webpack脚手架的（阶段一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f21ff24f71784d789032170102ab0ab2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 03:16:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f21ff24f71784d789032170102ab0ab2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>目前公司前端体系还不太完善的原因，一般写项目用的都是使用 create-react-app 搭建的一套通用的脚手架。这个脚手架虽然非常的通用、基础，但是在搭配了 tailwindcss、postcss 后，每次的编译和打包消耗的时间实在是太久了，非常影响工作效率。那么，为了<strong>不加班</strong>，手动来搭建一套通用的 <code>webpack</code> 脚手架，就成为了当前的一个没有标。</p>
<h1 data-id="heading-1">正文</h1>
<h2 data-id="heading-2">项目基本配置</h2>
<h3 data-id="heading-3">项目初始化</h3>
<pre><code class="copyable">mkdir webpack-demo-1
cd ./webpack-demo-1
yarn init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先需要创建项目的入口文件和 <code>webpack</code> 的配置文件，此时项目目录如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f21ff24f71784d789032170102ab0ab2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，需要安装 webpack 依赖</p>
<pre><code class="copyable">yarn add --dev  webpack webpack-cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里用到的 <code>webpack</code> 相关版本如下：</p>
<pre><code class="copyable">"webpack": "^5.44.0",
"webpack-cli": "^4.7.2"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">写入内容</h3>
<p>在 <code>index.js</code> 中随便写点东西进去：</p>
<pre><code class="copyable">class Hello &#123;
  constructor() &#123;
      console.log('hello webpack!')
  &#125;
&#125;

const test = new Hello()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们运行 <code>webpack</code> 来体验一下具体是什么效果</p>
<pre><code class="copyable">npx webpack
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，在运行完以后，在根目录下会增加一个 dist 目录，该目录下会新增一个 main.js 文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2849e13fbdc1423bb6345f449009be3e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中的内容：</p>
<pre><code class="copyable">new class&#123;constructor()&#123;console.log('hello webpack!')&#125;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那这样肯定是不 OK 的呀，需要使用 babel 把 ES6 转换成 ES5 的代码。下面就来安装一些 babel 的一些相关依赖。</p>
<h3 data-id="heading-5">配置 babel</h3>
<p>安装依赖：</p>
<pre><code class="copyable">yarn add --dev babel-loader @babel/core @babel/preset-env @babel/plugin-transform-runtime  @babel/plugin-proposal-decorators  @babel/plugin-proposal-class-properties @babel/plugin-proposal-private-methods

yarn add @babel/runtime @babel/runtime-corejs3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.config.js</code> 文件：</p>
<pre><code class="copyable">const path = require('path');

module.exports = &#123;
  entry: './src/index.js',
  output: &#123;
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.[contenthash:8].js',
  &#125;,
  module: &#123;
    rules: [
      &#123;
        test: /\.(jsx|js)$/,
        use: 'babel-loader',
        exclude: /node_modules/,
      &#125;,
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在根目录下创建 <code>.babelrc</code> 文件：</p>
<pre><code class="copyable">&#123;
  "presets": ["@babel/preset-env"],
  "plugins": [
    ["@babel/plugin-transform-runtime", &#123;"corejs": 3&#125;],
    ["@babel/plugin-proposal-decorators", &#123; "legacy": true &#125;],
    ["@babel/plugin-proposal-class-properties", &#123; "loose": true &#125;],
    ["@babel/plugin-proposal-private-methods", &#123; "loose": true &#125;]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让我们再执行一次 <code>npx webpack</code> 来看看输出结果。此时的项目目录：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ced88f1b97f416493613c72ef9888b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>来查看一下这个 dist 目录下的 <code>bundle.xxxx.js</code> 文件的内容：</p>
<pre><code class="copyable">(()=>&#123;"use strict";new function n()&#123;!function(n,o)&#123;if(!(n instanceof o))throw new TypeError("Cannot call a class as a function")&#125;(this,n),console.log("hello webpack!")&#125;&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样应该就没什么问题了。接下来来让项目运行在浏览器中吧！</p>
<h3 data-id="heading-6">运行在浏览器中</h3>
<p>这里直接使用 webpack 生态圈里一个非常知名的插件 <code>html-webpack-plugin</code>，这个插件可以让我们的构建产物使用我们指定的 <code>html</code> 文件作为模板来使用。</p>
<pre><code class="copyable">yarn add --dev html-webpack-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在根目录下，创建一个 public 文件夹，并放入一个 <code>index.html</code> 文件，并给他写入最基本的 html 的内容</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dee85c3a1e8b42678fae297a2784fa1d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <code>wbepack.config.js</code>文件中使用 <code>html-webpack-plugin</code> 插件</p>
<pre><code class="copyable">const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = &#123;
  // ...
  plugins: [
    new HtmlWebpackPlugin(&#123;
      template: path.resolve(__dirname, './public/index.html'),
      inject: 'body',
      scriptLoading: 'blocking',
    &#125;),
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，在运行 <code>npx webpack</code> 查看打包结果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8a65b9d4577477eb2d08e109a23f93d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开 <code>dist</code> 文件夹目录，直接用浏览器打开这个 <code>index.html</code> 文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cad8253ccf8644d48267ba22f79db307~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时可以看到我们输入的 "hello webpack!" 已经显示在控制台中了。</p>
<h2 data-id="heading-7">目前存在的问题</h2>
<p>以上就算是跑通了一个最基本的流程，但当前还面临几个最大的问题：</p>
<ol>
<li>需要<strong>热更新</strong>。不可能每次更新内容后都重新 build 一次，去使用打包后的文件来做调试；</li>
<li>在每次打包前需要清除上一次打包的内容。</li>
<li>环境拆分</li>
</ol>
<p>那么接下来，先来解决这两个问题吧！</p>
<h3 data-id="heading-8">热更新</h3>
<p>这里我们根据官网提示，使用 <code>webpack-dev-server</code></p>
<pre><code class="copyable">yarn add --dev webpack-dev-server
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后需要在 <code>webpack.config.js</code> 中添加上相关的配置内容：</p>
<pre><code class="copyable">module.exports = &#123;
  // ...
  devServer: &#123;
    port: '8080', // 开启的端口号，一般是 8080
    hot: true, // 是否启用 webpack 的 Hot Module Replacement 功能，也就是模块热替换
    stats: 'errors-only', // 终端仅打印 error
    compress: true, // 是否启用 gzip 压缩
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后我们需要在 <code>package.json</code> 中添加一个 ``scripts<code> 命令</code></p>
<pre><code class="copyable">&#123;
    // ...
    "scripts": &#123;
        "start": "webpack serve  --open"
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，就可以使用 <code>yarn start</code> 命令，在浏览器中打开 <code>http://localhost:8080/</code>页面，并可以使用热更新来进行调试，真是太方便了！</p>
<h3 data-id="heading-9">清除旧的打包产物</h3>
<p>这个问题很好解决，直接使用 <code>clean-webpack-plugin</code> 插件即可。但是，要注意的是，<strong>在 <code>webpack</code> 5.20 版本后，<code>webpack</code> 的 <code>output</code>已经支持在每次打包前清除构建产物</strong>，仅需在 webpack.config.js 中，在 output 字段中添加 <code>clean: true</code> 即可实现与 <code>clean-webpack-plugin</code> 相同的效果</p>
<pre><code class="copyable">// ...

module.exports = &#123;
  ...
  output: &#123;
      // ...
      clean: true
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">环境拆分</h3>
<p>一般来说，一个项目会分为 <code>开发</code>、<code>预发</code>和<code>生产</code>环境，这里的话主要还是分为<code>开发</code>和<code>生产环境</code></p>
<p>更新目录结构，在根目录下创建 <code>build</code> 文件夹，将原来根目录下的 <code>wbepack.config.js</code> 删除，在 <code>build</code> 目录下创建 <code>webpack.base.config.js</code>（公共部分）、<code>webpack.dev.config.js</code>（开发部分）、<code>webpack.prod.config.js</code>（生产部分） 三个文件。</p>
<p><code>webpack.base.config.js</code>：</p>
<pre><code class="copyable">const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const rootDir = process.cwd();

module.exports = &#123;
  entry: path.resolve(rootDir, 'src/index.js'),
  output: &#123;
    path: path.resolve(rootDir, 'dist'),
    filename: 'bundle.[contenthash:8].js',
  &#125;,
  module: &#123;
    rules: [
      &#123;
        test: /\.(jsx|js)$/,
        use: 'babel-loader',
        include: path.resolve(rootDir, 'src'),
        exclude: /node_modules/,
      &#125;,
    ]
  &#125;,
  plugins: [
    new HtmlWebpackPlugin(&#123;
      template: path.resolve(rootDir, 'public/index.html'),
      inject: 'body',
      scriptLoading: 'blocking',
    &#125;),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在配置生产和开发环境时，需要安装一个 <code>webpack-merge</code> 的插件，用于合并配置。</p>
<pre><code class="copyable">yarn add --dev webpack-merge
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>webpack.dev.config.js</code>：</p>
<pre><code class="copyable">const &#123; merge &#125; = require('webpack-merge');
const baseConfig = require('./webpack.base.config');

module.exports = merge(baseConfig, &#123;
  mode: 'development',
  devServer: &#123;
    port: '8080', // 默认是 8080
    hot: true,
    stats: 'errors-only', // 终端仅打印 error
    compress: true, // 是否启用 gzip 压缩
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>webpack.prod.config,js</code>：</p>
<pre><code class="copyable">const &#123; merge &#125; = require('webpack-merge');
const baseConfig = require('./webpack.base.config');

module.exports = merge(baseConfig, &#123;
  mode: 'production',
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，要注意，更新一下 <code>package.json</code> 文件中的 <code>scripts</code> 命令：</p>
<pre><code class="copyable">"scripts": &#123;
    "start": "webpack serve --config build/webpack.dev.config.js --open",
    "build": "npx webpack --config build/webpack.prod.config.js"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">继续完善功能</h2>
<h3 data-id="heading-12">支持 sass 和 css</h3>
<p>首先，在 src 目录下添加一个 <code>index.scss</code> 文件，并在 <code>index.js</code> 文件中引入，此时在执行 <code>yarn start</code> 后，会发现，<code>webpack</code> 是无法在没有安装对应 loader 的情况下，识别 scss 和 css 文件的内容。</p>
<p>接下来让我们来安装 loader。</p>
<pre><code class="copyable">yarn add --dev sass dart-sass sass-loader css-loader style-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：安装 <code>sass</code> 一般需要配合 <code>node-sass</code> 来使用，但根据官方文档，会发现其实他们更推荐使用的是 <code>dart-sass</code>，如果使用过 <code>creat-react-app</code> 来配置 <code>sass</code> 的同学会发现，<code>create-react-app</code> 是不支持 <code>dart-sass</code> 的。不过在这里我们自己手动配置，那使用 <code>dart-sass</code> 自然是没有问题的。</p>
<p>然后，修改 <code>webpack.base.config.js</code> 文件</p>
<pre><code class="copyable">module.exports = &#123;
  // ...
  module: &#123;
    rules: [
      // ...
      &#123;
        test: /\.(s[ac]ss|css)$/i,
        exclude: /node_modules/,
        use: ['style-loader', 'css-loader', 'sass-loader']
      &#125;,
    ]
  &#125;,
  // ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，再使用 <code>yarn start</code> 运行项目，就可以看到 css 在项目中已经可以展示啦！</p>
<h3 data-id="heading-13">添加 postcss</h3>
<p>接下来，我们来加入 <code>postcss</code></p>
<pre><code class="copyable">yarn add --dev autoprefixer postcss postcss-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更新 <code>webpack.base.config.js</code> 文件</p>
<pre><code class="copyable">const autoprefixer = require('autoprefixer');

module.exports = &#123;
  // ...
  module: &#123;
    rules: [
      // ...
      &#123;
        test: /\.(s[ac]ss|css)$/i,
        exclude: /node_modules/,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader',
          &#123;
            loader: "postcss-loader",
            options: &#123;
              postcssOption: &#123;
                plugins: [
                  ["autoprefixer"]
                ]
              &#125;
            &#125;
          &#125;
        ]
      &#125;,
    ]
  &#125;,
  // ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">打包后抽离 css 文件</h3>
<p>首先安装 <code>mini-css-extract-plugin</code> 插件</p>
<pre><code class="copyable">yarn add --dev mini-css-extract-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更新 <code>webpack.base.config.js</code></p>
<pre><code class="copyable">const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = &#123;
  // ...
  module: &#123;
    rules: [
      // ...
      &#123;
        test: /\.(s[ac]ss|css)$/i,
        exclude: /node_modules/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
          &#123;
            loader: "postcss-loader",
            options: &#123;
              postcssOptions: &#123;
                plugins: [
                  ["autoprefixer"]
                ]
              &#125;
            &#125;
          &#125;
        ]
      &#125;,
    ]
  &#125;,
  plugins: [
    // 省略...
    new MiniCssExtractPlugin(&#123;
      filename: 'css/[name].css',
    &#125;),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，再运行 <code>yarn build</code> 来查看一下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb0e56b6090443e3b052bb176c8d2a22~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，css 文件已经被抽离到指定的目录下了。</p>
<h3 data-id="heading-15">把静态资源复制到打包目录</h3>
<p>有时候可能会有一份静态的、需要手动下载下来的文件，需要手动加入到项目中。通常情况下，需要把这份资源放入到我们的 <code>public</code> 文件目录中，然后在 <code>index.html</code> 中用 <code>script</code> 导入。
但实际情况是，在 <code>public</code> 目录下添加后，还是无法找到这个文件。</p>
<pre><code class="copyable">// index.html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>

<script src="./js/test.js"></script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译结果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d228c892d5294b3889ba7cca591ca75f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么这时候就需要用到 <code>copy-webpack-plugin</code> 这个插件，在打包构建时，把指定的文件复制到打包的产物中。</p>
<pre><code class="copyable">yarn add --dev copy-webpack-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更新 <code>webpack.base.js</code></p>
<pre><code class="copyable">const CopyWebpackPlugin = require('copy-webpack-plugin');

const rootDir = process.cwd();

module.exports = &#123;
  // ...
  plugins: [
    
    new CopyWebpackPlugin(&#123;
      patterns: [
        &#123;
          from: '*.js',
          context: path.resolve(rootDir, "public/js"),
          to: path.resolve(rootDir, 'dist/js'),
        &#125;,
      ],
    &#125;)
    new MiniCssExtractPlugin(&#123;
      filename: 'css/[name].css',
    &#125;),
    new OptimizeCssPlugin(),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次运行 <code>yarn start</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/775f3a0f02f249f9a92a0ed82f8f21a4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在这个静态的 js 文件已经可以成功加载了</p>
<h3 data-id="heading-16">加载图片资源</h3>
<p>前端项目，自然免不了要引入图片等资源，此时，我们尝试在项目中引入资源。
在 index.js 中引入图片：</p>
<pre><code class="copyable">import './index.scss'
import imgTets from './assets/1.png'
class Hello &#123;
  constructor() &#123;
    console.log('hello webpack!')
  &#125;

  renderImg() &#123;
    const img = document.createElement('img')
    img.src = imgTets
    document.body.appendChild(img)
  &#125;
&#125;

const test = new Hello()
test.renderImg()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行项目，会看到一个熟悉的报错：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a04db24d5d0d44e8ac044825738bef86~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>正常来说，那就按提示走，缺少什么 <code>loader</code>，那就直接 <code>yarn add xxx-loader</code> 就完事了，那这里就安装 <code>raw-loader</code>、<code>url-loader</code>、<code>file-loader</code>，一把梭就行了。</p>
<p>但是，要注意的是，在 <code>webpack 5</code> 中，并不需要再安装这些依赖了，只需在 <code>webpack.base.config.js</code> 的配置中加上：</p>
<pre><code class="copyable">rules: [
    // ...
    &#123;
        test: /\.(png|jpg|gif|jpeg|webp|svg|eot|ttf|woff|woff2)$/,
        type: 'asset',
    &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新运行一遍 <code>yarn start</code>，此时再运行，就没有问题啦！</p>
<h2 data-id="heading-17">构建阶段的项目优化</h2>
<h3 data-id="heading-18">缓存</h3>
<p>webpack 5 已经为我们做了许多事情，其中就包括了缓存。配置：</p>
<pre><code class="copyable">// webpack.dev.config.js

module.exports = merge(baseConfig, &#123;
  mode: 'development',
  //...
  cache: &#123;
    type: 'memory'
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// webpack.prod.config.js

module.exports = merge(baseConfig, &#123;
  mode: 'production',
  // ...
  cache: &#123;
    type: 'filesystem',
    buildDependencies: &#123;
      config: [__filename]
    &#125;,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们来尝试运行两次 <code>yarn build</code>，来查看前后的时间差</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0525ae6870fa459496931594b93c6f06~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efc67b86c6a945dc92b2921850b0255c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到前后的差距，还是比较大的</p>
<h3 data-id="heading-19">代码拆分</h3>
<p>分割各个模块代码，提取相同部分代码，好处是减少重复代码的出现频率。从 webpack 4 开始，就开始使用 <code>splitChunks</code> 来代替 <code>CommonsChunksPlugin</code> 做代码的拆分操作。
配置：</p>
<pre><code class="copyable">// webpack.base.config.js

module.exports = &#123;
  //...
  optimization: &#123;
    splitChunks: &#123;
      chunks: 'all' // 代码分割类型：all全部模块，async异步模块，initial入口模块
    &#125;
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">多线程打包</h3>
<p>项目的打包速度在大型项目里是一个比较令人头疼的点，这里我们利用 <code>thread-loader</code> 来对项目进行多线程打包。</p>
<p>安装依赖：</p>
<pre><code class="copyable">yarn add --dev thread-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更新 <code>webpack.base.config.js</code></p>
<pre><code class="copyable">module.exports = &#123;
  entry: path.resolve(rootDir, 'src/index.js'),
  output: &#123;
    path: path.resolve(rootDir, 'dist'),
    filename: 'bundle.[contenthash:8].js',
    clean: true
  &#125;,
  module: &#123;
    rules: [
      &#123;
        test: /\.(jsx|js)$/,
        use: ['thread-loader', 'babel-loader'],
        include: path.resolve(rootDir, 'src'),
        exclude: /node_modules/,
      &#125;,
      &#123;
        test: /\.(s[ac]ss|css)$/i,
        exclude: /node_modules/,
        use: [
          MiniCssExtractPlugin.loader,
          'thread-loader',
          'css-loader',
          'sass-loader',
          &#123;
            loader: "postcss-loader",
            options: &#123;
              postcssOptions: &#123;
                plugins: [
                  ["autoprefixer"]
                ]
              &#125;
            &#125;
          &#125;
        ]
      &#125;,
      &#123;
        test: /\.(png|jpg|gif|jpeg|webp|svg|eot|ttf|woff|woff2)$/,
        type: 'asset',
      &#125;,
    ]
  &#125;,
  //...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">阶段一总结</h2>
<p>到这里为止，就是一个比较通用的、基于 <code>webpack 5</code> 的脚手架了。但是，要直接拿来开发，还是需要再做一些操作，因为，<strong>连 <code>react</code> 或者 <code>vue</code> 都还没有安装配置呢！</strong></p>
<p>在阶段二，我需要在这个脚手架的基础上，根据自己的需求，添加 <code>react</code>、<code>typescript</code>、<code>tailwindcss</code> 等功能，以满足日常开发的需要！</p></div>  
</div>
            