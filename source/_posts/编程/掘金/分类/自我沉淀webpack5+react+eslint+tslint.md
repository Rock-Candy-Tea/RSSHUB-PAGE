
---
title: '自我沉淀webpack5+react+eslint+tslint'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df448193a9fa4834a5b0664c2fb300fe~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 01:49:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df448193a9fa4834a5b0664c2fb300fe~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>自己学了一段时间webpack准备将自己的知识沉淀一下，千里之行始于足下，如果不沉淀一下的话总是觉得知识点有些浮躁，无法彻底沉淀下来。</p>
<h1 data-id="heading-0">初始化webpack配置。</h1>
<h5 data-id="heading-1">第一步 初始化webpack</h5>
<pre><code class="copyable">先创建一个文件，名字自定义，例：webpackdemo
1、执行npm init 一路回车最后输入yes 就可以初始化webpack.json   如图
2、执行npm init -y 也可以初始化webpack.json。
1与2 二选其一即可。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df448193a9fa4834a5b0664c2fb300fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-2">第二步 创建文件</h5>
<pre><code class="copyable">    在根目录创建文件夹src/index.js和index.html
    文件目录如下：
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d1235c35d0f4970a1663bfd813c594d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">第三步创建我们自己的webpack配置文件</h5>
<pre><code class="copyable">  在跟路径下面创建webpack.config.js 
  如图：
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a16f38438214c8b9a77bf4afc4ceb53~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">一、webpack自我总结大致分为几类配置</h2>
<h4 data-id="heading-5">1、mode （环境）</h4>
<h6 data-id="heading-6">mode分为两种模式</h6>
<pre><code class="copyable">mode:"production",   生产环境

mode:"development",   开发环境
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2、entry （入口）</h4>
<pre><code class="copyable">entry:'./src/index.js',  // 入口根据自己的实际情况而定
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-8">多入口格式</h6>
<pre><code class="copyable">特点：如果有一个入口最终就只有一个bundle文件。
     如果有两个入口就会产生两个bundle文件。
entry:&#123;
    mian:'./src/main.js',
    test:'./src/test.js',
&#125;
output（出口） 如果配置了多入口模式需要配置chunkFilename: '[id].js' 
来产生多个bundle(打包过后的)文件。
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-9">react入口文件内容</h6>
<pre><code class="copyable">import React from 'react';
import &#123; render &#125; from 'react-dom';
import &#123; ConfigProvider &#125; from 'antd';
import zhCN from 'antd/lib/locale/zh_CN';
import App from './containers/App';

render(
  <ConfigProvider locale=&#123;zhCN&#125;><App /></ConfigProvider>,
  document.getElementById('app'),  // app为html文件中的id
);

if (module.hot) &#123;
  module.hot.accept();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-10">html文件内容</h6>
<pre><code class="copyable"><!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Hello World</title>
  </head>
  <body>
    <div id="app" style="height: 100%;"></div>  // id="app" 对应index.js文件中的document.getElementById('app')
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">3、output(出口）</h4>
<h6 data-id="heading-12">文件输出</h6>
<h6 data-id="heading-13">webpack地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Foutput%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/output/" ref="nofollow noopener noreferrer">webpack.docschina.org/configurati…</a></h6>
<pre><code class="copyable"> const &#123;resolve&#125;=require('path');    // node环境的方法，可以获取到当前项目的路径
 ...
 ouput:&#123;
     filename:'js/main.js',          // 最终会在打包的文件夹中产生js/main.js的文件
                                     // 如果怕产生冲突的话可以使用chunk文件格式 js/[hash:5].js。这样会产生hash前5位的文件名
     path:resolve(__dirname,'dist'), // 设置build之后产生的文件夹名称'dist'，意为在项目的根路径创建dist文件。
     clean:true,                     // 每一次build之后将原文件删除再重新创建一个文件。
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">4、module</h4>
<h6 data-id="heading-15">配置 解析文件 比如将es5+转换为es5、less转换为css等等...</h6>
<pre><code class="copyable">module:&#123;
    rules:[
    
        // webpack地址：https://webpack.docschina.org/loaders/babel-loader/
        // 需要安装  npm install @babel/core @babel/preset-env @babel/preset-react @babel/preset-typescript -D  
        // 如果npm网速过慢的话可以使用cnpm(淘宝镜像)或者yarn。
        &#123;
            test: /\.(js|jsx)$/,                // 匹配结尾是js/jsx的文件
            include: resolve(__dirname,'src'),  // 从src路径下面开始寻找，节省解析时间
            exclude: /node_modules/             // 不解析node_modules文件
            exclude: 'pre'                      // pre:优先执行 post:延后执行 不设置enforce则顺序执行
            use: [
                &#123;
                  loader:'babel-loader',
                  options:&#123;
                      presets:[
                          '@babel/preset-env',      // 将es5+转换成es5
                          '@babel/preset-react',    // 将react中的jsx语法转换成js语法
                          '@babel/preset-tyscript'  // 将react中ts
                      ],
                      cacheDirectory: true,  // 缓存：第二次编译时，会读取之前的缓存，节省编译时间
                  &#125;
                &#125;
            ]
        &#125;,
        
        
        // 如果匹配到css文件，则将css转换为style
        // 需要安装  npm install style-loader css-loader -D  
        &#123;
            test: /\.css$/,
            use:['style-loader','css-loader']
        &#125;,
        
        
        // 如果匹配到以less文件，则使用less-loader转换成css，再通过css-loader转换成style，再通过style-loader转换成行内样式。
        // 因为上方已经安装过了style-loader和css-loader所以这里只需安装less-loader  cnpm install less-loader -D 
        &#123;
            test: /\.less$/,
            use:['style-loader','css-laoder','less-laoder'],
        &#125;,
        
        
        // 如果匹配到以sass或者scss结尾的文件则使用sass-loader和sass去做转译.
        // 同样的上方安装过style-loader和css-loader 则现在只需安装 cnpm install sass sass-loader -D
        &#123;
            test: /\.s[ac]ss$/,
            use:['style-loader','css-loader','sass-loader']
        &#125;,
        
        
        // 解析各种图片，需要一个file-laoder插件。
        // cnpm install file-loader -D
        &#123;
            exclude: /.(html|less|css|sass|js|jsx|ts|tsx)$/,  // 排除哪些文件。
            test: /\.(jpg|jpe|png|gif)$/,
            loader: 'file-loader',
            opions: &#123;
              name: 'imgs/[name].[ext]', 
              outputPath: 'other'        // 输出到dist中的文件名 
            &#125;
        &#125;,
        
        
        &#123;
            test: /\.(ect|ttf|svg|woff)$/,
            use: &#123;
              loader: 'file-loader',
              options: &#123;
                name: 'icon/[name].[ext]'
              &#125;
            &#125;
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">5、resolve(解析模块规则别名)</h4>
<h6 data-id="heading-17">webpack地址： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fresolve%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/resolve/" ref="nofollow noopener noreferrer">webpack.docschina.org/configurati…</a></h6>
<pre><code class="copyable">resolve:&#123;
    alias:&#123;
        "@":reslove(__dirname,'src/'), // 使用@代表从src/下方开始查找。  省略了../../ 繁琐方式
   &#125;,
   extensions:[".js",".jsx",".ts",".tsx"],  // 省略文件路径的后缀名。 index.jsx=index  index相当于index.jsx.
   mainFiles:["index.js","index.jex",index.ts","index.tsx"],  // 省略文件名。demo/index.js=demo
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">6、plugins</h4>
<h6 data-id="heading-19">plugins主要是添加一些插件,比如压缩css文件、将css提取出来放在一个文件中。 webpack地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fplugins%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/plugins/" ref="nofollow noopener noreferrer">webpack.docschina.org/plugins/</a></h6>
<pre><code class="copyable">plugins:&#123;
  // 使用HtmlWebpackPlugin去自动生成html文件。 需要安装
  new HtmlWebpackPlugin(&#123;
      // 指定html文件。如果没有指定则会自动生成一个html文件
      template: './index.html',  // 例：在第二步的时候创建的index.html文件。
      title: 'My App',
  &#125;),
  

  
  // 显示百分比编译  样式如图1。
  // 需要引入const webpack = require('webpack')。
  // 不需要安装webpack。
  new webpack.ProgressPlugin(&#123;
      activeModules: false,
      entries: true,
      modules: true,
      modulesCount: 5000,
      profile: false,
      dependencies: true,
      dependenciesCount: 10000,
      percentBy: 'entries',
  &#125;),
  
  
  // 将所有的css文件提取出来到一个css文件。
  // 需要下载  mini-css-extract-plugin插件  cnpm install --save-dev mini-css-extract-plugin
  // 引入方式 const MiniCssExtractPlugin = require('mini-css-extract-plugin');
  // 引入了 mini-css-extract-plugin之后在生产环境中要将module中的style-loader更换成 MiniCssExtractPlugin.loader 才可以将css抽取出来并解析。
  // webpack 地址 https://webpack.docschina.org/plugins/mini-css-extract-plugin/
  new MiniCssExtractPlugin(&#123;
    filename: 'css/main.css'  // 设置dist文件中的css文件路径
  &#125;),
  
  
  //  压缩css文件CssMinimizerPlugin
  //  需要下载 cnpm install css-minimizer-webpack-plugin -D
  //  引用方式 const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
  new CssMinimizerPlugin(),  // 启动css压缩
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-20">(图1)</h6>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c7e7200c8344b60ba3e1f57f8332073~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-21">7、devtool 配置source-map</h4>
<h5 data-id="heading-22">webpack地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fdevtool%2F%23root" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/devtool/#root" ref="nofollow noopener noreferrer">webpack.docschina.org/configurati…</a></h5>
<h5 data-id="heading-23">一种提供源代码到构建后代码映射技术(如果构建后代码出错了，通过映射可以追踪源代码错误)         source-map指的是使用可以在调试过程中向开发者展示源码，如果不开启source-map开发者查看时就会展示编译过的代码不利于开发者开发。</h5>
<pre><code class="copyable"> /** 
   * 配置：[inline-|hidden-|eval-][nodources-][cheap-[module-]]source-map
   * source-map               外部    错误代码准确信息和源代码错误信息。
   * inline-source-map        内联    打包到文件中打包速度快。文件体积大。错误代码准确信息和源代码错误信息，只生成一个source-map
   * eval-source-map          内联    打包到文件中，每一个js文件都会生成source-map文件，错误代码准确信息和源代码错误信息会多一个hash值。
   * hidden-source-map        外部    打包到外部，但是打包速度慢，文件体积小。可以提示到错误代码的原因，但是没有错误位置，不能追踪到源代码的位置，只能提示到构建后代码的错误位置。
   * nocource-source-map      外部    错误代码的准确信息，但是没有任何源代码的信息。为了隐藏源代码
   * checp-module-source-map  外部    只精确到行
 */
  devtool:"inline-source-map",
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">8、devServer  制定启动服务的配置</h4>
<h6 data-id="heading-25">weback 地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fdev-server%2F%23root" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/dev-server/#root" ref="nofollow noopener noreferrer">webpack.docschina.org/configurati…</a></h6>
<pre><code class="copyable">devServer:&#123;
    hot:true,         // 是否开启HMR(热更新)模式，保存之后不需要重新打包就可以进行热更新。
    port:3000,        // 指定启动项目的端口号
    host:'127.0.0.1', // 指定启动项目的host地址
    compress:true,    // 是否开启gzip压缩
    open:true,        // 启动项目之后是否自动打开新的浏览器窗口
    proxy: &#123;          // 代理 解决开大环境的跨域问题
                      // 一旦服务器接收到/api的请求就会把请求转发到另外一个服务器(http://localhost:8000)   
                      // 浏览器和服务器之间存在跨域，但是服务器和服务器之间不存在跨域
      '/api': &#123;
        target: 'http://localhost:8000',
        pathRewrite: &#123; '^/api': '' &#125;,   // 发送请求时，请求路径重写将 /api/xxxx 转换为 /xxx 去掉api
        secure: false      //  默认情况下，将不接受在 HTTPS 上运行且证书无效的后端服务器。 如果需要，可以这样修改配置
      &#125;
    &#125;,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">9、optimization  默认压缩工具</h4>
<h6 data-id="heading-27">webpack地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Foptimization%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/optimization/" ref="nofollow noopener noreferrer">webpack.docschina.org/configurati…</a></h6>
<h6 data-id="heading-28">通过TerserPlugin覆盖默认压缩工具</h6>
<pre><code class="copyable">   cnpm install  terser-webpack-plugin -D
   使用方式 const TerserPlugin = require('terser-webpack-plugin'); // 压缩js打包文件 优化build速度、优化start速度

optimization: &#123;
    minimizer: [new TerserPlugin(&#123;   // 通过配置TerserPlugin插件
      test: /\.(js|jsx|ts|tsx)$/,    // 针对js、jsx、ts、tsx文件去压缩
      exclude: /node_modules/,       // 排出掉node_modules文件，使star速度更快
      extractComments: true,         // 针对src下方的文件去优化
      include: './src',
    &#125;)],
    usedExports: true,
    sideEffects: false
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">上面就是webpack的几项基本配置。有兴趣的同学可以看一下webpack官网，里面有中文版文档  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/" ref="nofollow noopener noreferrer">webpack.docschina.org/</a></h4>
<h2 data-id="heading-30">二、  根据环境区分不同的webpack配置</h2>
<h4 data-id="heading-31">上面讲到过环境分为。development(开发环境)和producion(生产环境)</h4>
<pre><code class="copyable">  开发环境和生产环境的侧重点是不同的
  1、开发环境注重start的速度和方便调试。
  2、生产模式则主要侧重于build之后文件的大小，以及build的速度。
  
  因为在提取css文件会消耗大量的时间，所以在开发模式下直接使用style-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-32">1、开发环境配置</h5>
<h5 data-id="heading-33">下面我就不详细写注释了直接上配置</h5>
<pre><code class="copyable">const webpack = require('webpack');
const &#123;resolve&#125;=require('path');
const HtmlWebpackPlugin=require('html-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');

module.exports=&#123;
  entry:'./src/index.js',
  output:&#123;
    filename:'js/main.js',
    path:resolve(__dirname,'dist'),
    clean:true,
  &#125;,
  
  resolve:&#123;
    alias: &#123;
      "@": resolve(__dirname, 'src/')
    &#125;,
    extensions: [".js", ".jsx", ".json", '.ts', '.tsx'],
    mainFiles: ["index.js", "index.jsx", "index.tsx", "index.ts"]
  &#125;,
  
  mode:'development',
  
  devtool:'inline-source-map',
  
  devServer:&#123;
    hot:true,
    port:3002,
    host:'127.0.0.1',
    compress:true,
    open:true,
    proxy: &#123;
      '/api': &#123;
        target: 'http://localhost:8000',
        pathRewrite: &#123; '^/api': '' &#125;,
        secure: false
      &#125;
    &#125;,
  &#125;,
  
  module:&#123;
    rules:[
      &#123;
        test:/\.(js|jsx)$/,
        include: resolve(__dirname,'src'),
        exclude: /node_modules/,
        enforce: 'pre',
        use:[&#123;
          loader:'babel-loader',
          options:&#123;
            presets: [
              '@babel/preset-env',
              '@babel/preset-react',
              '@babel/preset-typescript',
            ],
            cacheDirectory: true,
          &#125;
        &#125;]
      &#125;,
      &#123;
        test:/\.(ts|tsx)$/,
        loader:'ts-loader',
        exclude: /node_modules/
      &#125;,
      // 因为开发环境不需要压缩css文件，开启压缩css文件插件会导致start时间过长。
      &#123;
        test:/\.css$/,
        use:['style-loader','css-loader'],
      &#125;,
      &#123;
        test:/\.less$/,
        use:['style-loader','css-loader','less-loader'],
      &#125;,
      &#123;
        test:/\.s[ac]ss$/,
        use:['style-loader','css-loader','sass-loader']
      &#125;,
      &#123;
        exclude: /.(html|less|css|sass|js|jsx|ts|tsx)$/,
        test: /\.(jpg|jpe|png|gif)$/,
        loader: 'file-loader',
        options: &#123;
          name: 'imgs/[name].[ext]',
          outputPath: 'other'
        &#125;
      &#125;,
      &#123;
        test: /\.(ect|ttf|svg|woff)$/,
        use: &#123;
          loader: 'file-loader',
          options: &#123;
            name: 'icon/[name].[ext]'
          &#125;
        &#125;
      &#125;
    ]
  &#125;,
  
  plugins:[
    new HtmlWebpackPlugin(&#123;
      template: './index.html',
      title: 'My App',
      minify: &#123;
        removeAttributeQuotes: true,
        removeComments: true,
      &#125;
    &#125;),
    // 显示百分比编译
    new webpack.ProgressPlugin(&#123;
      activeModules: false,
      entries: true,
      modules: true,
      modulesCount: 5000,
      profile: false,
      dependencies: true,
      dependenciesCount: 10000,
      percentBy: 'entries',
    &#125;)
  ],
  
  optimization: &#123;
    minimizer: [new TerserPlugin(&#123;
      test: /\.(js|jsx|ts|tsx)$/,
      exclude: /node_modules/,
      extractComments: true,
      include: './src',
    &#125;)],
    usedExports: true,
    sideEffects: false
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-34">2、生产环境配置</h5>
<pre><code class="copyable">如果将mode设置为生产环境(production) webpack会自动开启tree shaking功能
并且我们要将css文件提取出来，
/**
 * tree shaking   去除无用代码
 * 前提：1、必须使用ES6代码
 *      2、开启production环境会自动开启tree shaking
 * 作用：减少代码体积
 * 
 * 在package.json中配置
 *  sideEffects:false  所有代码都没有副作用    (都可以进行tree  shaking)
 *   问题：可能会把css/@babel/polyfile (副作用)文件干掉
 *   解决："sideEffects":["*.css"]
 * */
const webpack = require('webpack');
const &#123;resolve&#125;=require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

const cssloader = [
  MiniCssExtractPlugin.loader,
  'css-loader',
  &#123;
    loader: 'postcss-loader',
    options: &#123;
      postcssOptions: &#123;
        plugins: [
          ['autoprefixer'],
          require('postcss-preset-env')()
        ]
      &#125;
    &#125;
  &#125;
];

module.exports =&#123;
  mode: 'production',
  entry:'./src/index.js',
  output:&#123;
    filename:'js/main.js',
    path:resolve(__dirname,'dist'),
    clean:true,
  &#125;,
  resolve:&#123;
    alias: &#123;
      "@": resolve(__dirname, 'src/')
    &#125;,
    extensions: [".js", ".jsx", ".json", '.ts', '.tsx'],
    mainFiles: ["index.js", "index.jsx", "index.tsx", "index.ts"]
  &#125;,
  
  module: &#123;
    rules: [
      &#123;
        test:/\.(js|jsx)$/,
        include: resolve(__dirname,'src'),
        exclude: /node_modules/,
        enforce: 'pre',
        use:[&#123;
          loader:'babel-loader',
          options:&#123;
            presets: [
              '@babel/preset-env',
              '@babel/preset-react',
            ],
            cacheDirectory: true,
          &#125;
        &#125;]
      &#125;,
      &#123;
        test: /\.css$/,
        use: [...cssloader]
      &#125;,
      &#123;
        test: /\.less$/,
        use: [...cssloader, 'less-loader'],
      &#125;,
      &#123;
        test: /.s[ac]ss$/,
        use: [...cssloader, 'sass-loader'],
      &#125;,
      &#123;
        exclude: /.(html|less|css|sass|js|jsx|ts|tsx)$/,
        test: /\.(jpg|jpe|png|gif)$/,
        loader: 'file-loader',
        options: &#123;
          name: 'imgs/[name].[ext]',
          outputPath: 'other'
        &#125;
      &#125;,
      &#123;
        test: /\.(ect|ttf|svg|woff)$/,
        use: &#123;
          loader: 'file-loader',
          options: &#123;
            name: 'icon/[name].[ext]'
          &#125;
        &#125;
      &#125;
    ]
  &#125;,
  
  plugins: [
    new MiniCssExtractPlugin(&#123;
      filename: 'css/main.css'
    &#125;),
    new CssMinimizerPlugin(),
    new webpack.ProgressPlugin(&#123;
      activeModules: false,
      entries: true,
      modules: true,
      modulesCount: 5000,
      profile: false,
      dependencies: true,
      dependenciesCount: 10000,
      percentBy: 'entries',
    &#125;)
  ],
  optimization: &#123;
    usedExports: true,
    minimize: true,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">仔细读文章的同学一定也会发现生产环境和开发环境中有些配置是冲突的 咱们可以提取一下，将公共的配置提取到一个common的文件中。</h4>
<h4 data-id="heading-36">webpack.common.js</h4>
<pre><code class="copyable">const webpack = require('webpack');
const &#123;resolve&#125;=require('path');
const HtmlWebpackPlugin=require('html-webpack-plugin');

module.exports=&#123;
  entry:'./src/index.js',
  
  output:&#123;
    filename:'js/main.js',
    path:resolve(__dirname,'dist'),
    clean:true,
  &#125;,
 
  resolve:&#123;
    alias: &#123;
      "@": resolve(__dirname, 'src/')
    &#125;,
    extensions: [".js", ".jsx", ".json", '.ts', '.tsx'],
    mainFiles: ["index.js", "index.jsx", "index.tsx", "index.ts"]
  &#125;,
  
  module:&#123;
    rules:[
      &#123;
        test:/\.(js|jsx)$/,
        include: resolve(__dirname,'src'),
        exclude: /node_modules/,
        enforce: 'pre',
        use:[&#123;
          loader:'babel-loader',
          options:&#123;
            presets: [
              '@babel/preset-env',
              '@babel/preset-react',
              '@babel/preset-typescript',
            ],
            cacheDirectory: true,
          &#125;
        &#125;]
      &#125;,
      &#123;
        test:/\.(ts|tsx)$/,
        loader:'ts-loader',
        exclude: /node_modules/
      &#125;,
      &#123;
        test:/\.css$/,
        use:['style-loader','css-loader'],
      &#125;,
      &#123;
        test:/\.less$/,
        use:['style-loader','css-loader','less-loader'],
      &#125;,
      &#123;
        test:/\.s[ac]ss$/,
        use:['style-loader','css-loader','sass-loader']
      &#125;,
      &#123;
        exclude: /.(html|less|css|sass|js|jsx|ts|tsx)$/,
        test: /\.(jpg|jpe|png|gif)$/,
        loader: 'file-loader',
        options: &#123;
          name: 'imgs/[name].[ext]',
          outputPath: 'other'
        &#125;
      &#125;,
      &#123;
        test: /\.(ect|ttf|svg|woff)$/,
        use: &#123;
          loader: 'file-loader',
          options: &#123;
            name: 'icon/[name].[ext]'
          &#125;
        &#125;
      &#125;
    ]
  &#125;,
  
  plugins:[
    new HtmlWebpackPlugin(&#123;
      template: './index.html',
      title: 'My App',
      minify: &#123;
        removeAttributeQuotes: true,
        removeComments: true,
      &#125;
    &#125;),
    new webpack.ProgressPlugin(&#123;
      activeModules: false,
      entries: true,
      modules: true,
      modulesCount: 5000,
      profile: false,
      dependencies: true,
      dependenciesCount: 10000,
      percentBy: 'entries',
    &#125;)
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-37">开发环境: 这时需要一个插件webpack-merge</h4>
<h5 data-id="heading-38">使用方法:</h5>
<pre><code class="copyable">const &#123;merge&#125;=require('webpack-merge');
const &#123;merge&#125;=require('webpack-merge');
const common=require("./webpack.common");
const TerserPlugin = require('terser-webpack-plugin'); // 压缩js打包文件 优化build速度、优化start速度
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">开发环境文件: webpack.dev.js</h4>
<pre><code class="copyable">const &#123;merge&#125;=require('webpack-merge');
const common=require("./webpack.common");
const TerserPlugin = require('terser-webpack-plugin'); // 压缩js打包文件 优化build速度、优化start速度
module.exports=merge(common,&#123;
  mode:'development',
  devtool:'inline-source-map',
  devServer:&#123;
    hot:true,
    port:3002,
    host:'127.0.0.1',
    compress:true,
    open:true,
    proxy: &#123;
      '/api': &#123;
        target: 'http://localhost:8000',
        pathRewrite: &#123; '^/api': '' &#125;,
        secure: false
      &#125;
    &#125;,
  &#125;,
  optimization: &#123;
    // minimize: false,
    minimizer: [new TerserPlugin(&#123;
      test: /\.(js|jsx|ts|tsx)$/,
      exclude: /node_modules/,
      extractComments: true,
      include: './src',
    &#125;)],
    usedExports: true,
    sideEffects: false
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-40">生产环境文件: webpack.prod.js</h4>
<pre><code class="copyable">/**
 * tree shaking   去除无用代码
 * 前提：1、必须使用ES6代码
 *      2、开启production环境会自动开启tree shaking
 * 作用：减少代码体积
 *
 * 在package.json中配置
 *  sideEffects:false  所有代码都没有副作用    (都可以进行tree  shaking)
 *   问题：可能会把css/@babel/polyfile (副作用)文件干掉
 *   解决："sideEffects":["*.css"]
 * */
const webpack = require('webpack');
const &#123;resolve&#125;=require('path');
//  将所有的css提取到同一个文件夹中
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
// 压缩css文件
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const &#123;merge&#125;=require('webpack-merge');
const common=require("./webpack.common");

const cssloader = [
  // 将css提出的方法替换style-loader
  MiniCssExtractPlugin.loader,
  'css-loader',
  &#123;
    loader: 'postcss-loader',
    options: &#123;
      postcssOptions: &#123;
        plugins: [
          ['autoprefixer'],
          require('postcss-preset-env')()
        ]
      &#125;
    &#125;
  &#125;
];
module.exports =merge(common,&#123;
  // 启动环境
  mode: 'production',
  // 转换方法
  module: &#123;
    rules: [
      &#123;
        /**
        * lazy loading懒加载
        */
        test:/\.(js|jsx)$/,
        include: resolve(__dirname,'src'),
        exclude: /node_modules/,
        /**
         *  pre:优先执行
         *  post:延后执行
         *  不设置enforce则顺序执行
         */
        enforce: 'pre',
        use:[&#123;
          loader:'babel-loader',
          options:&#123;
            presets: [
              '@babel/preset-env',
              '@babel/preset-react',
            ],
            // 缓存：第二次构建时，会读取之前的缓存
            cacheDirectory: true,
          &#125;
        &#125;]
      &#125;,
      &#123;
        test: /\.css$/,
        use: [...cssloader]
      &#125;,
      &#123;
        test: /\.less$/,
        use: [...cssloader, 'less-loader'],
      &#125;,
      &#123;
        test: /.s[ac]ss$/,
        use: [...cssloader, 'sass-loader'],
      &#125;,
      &#123;
        exclude: /.(html|less|css|sass|js|jsx|ts|tsx)$/,
        test: /\.(jpg|jpe|png|gif)$/,
        loader: 'file-loader',
        options: &#123;
          name: 'imgs/[name].[ext]',
          outputPath: 'other'
        &#125;
      &#125;,
      &#123;
        test: /\.(ect|ttf|svg|woff)$/,
        use: &#123;
          loader: 'file-loader',
          options: &#123;
            name: 'icon/[name].[ext]'
          &#125;
        &#125;
      &#125;
    ]
  &#125;,
  plugins: [
    new MiniCssExtractPlugin(&#123;
      filename: 'css/main.css'
    &#125;),
    new CssMinimizerPlugin(),
    // 显示百分比编译
    new webpack.ProgressPlugin(&#123;
      activeModules: false,
      entries: true,
      modules: true,
      modulesCount: 5000,
      profile: false,
      dependencies: true,
      dependenciesCount: 10000,
      percentBy: 'entries',
    &#125;)
  ],
  optimization: &#123;
    usedExports: true,
    minimize: true,
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-41">文件格式如下：</h5>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d786522ce08445e1a7c82fafd7709391~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-42">三、好啦。 配置已经完成，下面就可以运行项目啦:</h3>
<p>我们在webpack.json文件中配置一下启动的命令
在webpack5中的启动命令和4中有些不一样
<a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">webpack.docschina.org/guides/gett…</a></p>
<pre><code class="copyable">"scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "npx webpack server --config webpack.dev.js", // npx webpack server   执行start操作，开始运行项目    --config 指定使用哪一个文件启动
    "build": "npx webpack --config webpack.prod.js"  // npx webpack 开始打包执行build操作
  &#125;,
  "browserslist": &#123;
    // 配置兼容性 postcss会根据兼容性来在css文件中添加样式前缀  
    // 具体可以查阅browserslist文档https://github.com/browserslist/browserslist#queries
    "development": [
      "last 1 chrome version", // chrome最后一个大版本
      "last 1 firefox version",  // firefox 最后一个大版本
      "last 1 safari version"   // safari 最后一个大版本
    ],
    "production": [
      ">0.2%",  // 忽略市场上使用率小于0.2%的浏览器
      "not dead",  // 忽略已经死亡浏览器
    ]
  &#125;,
  "sideEffects": "*.css"  //  mode为production的时候css压缩会产生副作用，会将css文件压缩到js文件中，导致无法提取出来，所以需要使用sideEffect取消这个副作用。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-43">四、别忘了还有eslint和tslint校验以及css校验哦：</h4>
<pre><code class="copyable">安装 cnpm install eslint eslint-config-airbnb-typescript eslint-plugin-jsx-a11y eslint-plugin-import eslint-plugin-react eslint-plugin-react-hooks typescript -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-44">eslint配置文件  .eslint.rc</h5>
<h6 data-id="heading-45">文件路径如图：</h6>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5489cf05c544322bd62c8746aeac872~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-46">具体配置如下：</h6>
<pre><code class="copyable">module.exports = &#123;
  root: true,
  parser: "@typescript-eslint/parser",
  parserOptions: &#123;
    ecmaFeatures: &#123;
      jsx: true,
    &#125;,
    ecmaVersion: 11,
    sourceType: "module",
    project: "./tsconfig.json",
  &#125;,
  plugins: ["react", "react-hooks", "@typescript-eslint"],
  extends: [
    "airbnb-typescript",
    "plugin:@typescript-eslint/recommended",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
  ],
  rules: &#123;
    // 禁止使用 var
    "no-var": "error",
    // 优先使用 interface 而不是 type
    "@typescript-eslint/consistent-type-definitions": ["error", "interface"],
    "@typescript-eslint/no-explicit-any": "off",
    "@typescript-eslint/explicit-module-boundary-types": "off",
    "react-hooks/rules-of-hooks": "error",
    "react-hooks/exhaustive-deps": "warn",
    "react/prop-types": "off",
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-47">ts配置文件. tsconfig.json</h5>
<h6 data-id="heading-48">文件路径如图：</h6>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78e84ba81d2a443fa0fa8e134ab7d750~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-49">配置如下：</h6>
<pre><code class="copyable"> &#123;
  "compilerOptions": &#123;
    "outDir": "./dist/",
    "noImplicitAny": true,
    "module": "es6",
    "target": "es5",
    "jsx": "react",
    "allowJs": true,
    "moduleResolution": "node",
    "allowSyntheticDefaultImports": true
  &#125;,
  "rules": &#123;
    "indent": [true, "spaces", 2],
    "interface-name": false,
    "no-consecutive-blank-lines": false,
    "object-literal-sort-keys": false,
    "ordered-imports": false,
    "quotemark": [true, "single"],
    "semicolon": [true, "never"],
    "trailing-comma": [true, &#123; "multiline": "never", "singleline": "never" &#125;]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-50">增加 custom.d.ts  有时引用svg和png图片的时候ts会找不到声明文件则使用：</h6>
<pre><code class="copyable">    declare module "*.svg" &#123;
      const content: any;
      export default content;
    &#125;
    declare module "*.png" &#123;
      const content: any;
      export default content;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-51">style 配置文件</h5>
<h6 data-id="heading-52">需要安装 cnpm install  stylelint-config-standard -D</h6>
<h6 data-id="heading-53">文件路径如图</h6>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33d199cde99b4d7e831b0952f2783149~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-54">配置如下：</h6>
<pre><code class="copyable">    &#123;
      "extends": "stylelint-config-standard"
    &#125;
    
    
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-55">好了下面就要配置  .eslintignore eslint有时会校验一些我们不想让它校验的文件，我们可以加一下这个配置哦。</h3>
<h6 data-id="heading-56">文件路径如图</h6>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b87244ffa44a46ec866e075de12c62b8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-57">配置如下：</h6>
<pre><code class="copyable">    config/
    scripts/
    node_modules/
    \.eslintrc.js
    webpack.common.js
    webpack.dev.js
    webpack.prod.js
    
    
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-58">大功告成！！！！！！！！</h2>
<h2 data-id="heading-59">下面附上完整的配置哦</h2>
<h3 data-id="heading-60">文件目录</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18ae699706da473a947609c99f164faa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-61">.eslintignore</h3>
<pre><code class="copyable">config/
scripts/
node_modules/
\.eslintrc.js
webpack.common.js
webpack.dev.js
webpack.prod.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-62">.eslintrc.js</h3>
<pre><code class="copyable">module.exports = &#123;
  root: true,
  parser: "@typescript-eslint/parser",
  parserOptions: &#123;
    ecmaFeatures: &#123;
      jsx: true,
    &#125;,
    ecmaVersion: 11,
    sourceType: "module",
    project: "./tsconfig.json",
  &#125;,
  plugins: ["react", "react-hooks", "@typescript-eslint"],
  extends: [
    "airbnb-typescript",
    "plugin:@typescript-eslint/recommended",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
  ],
  rules: &#123;
    // 禁止使用 var
    "no-var": "error",
    // 优先使用 interface 而不是 type
    "@typescript-eslint/consistent-type-definitions": ["error", "interface"],
    "@typescript-eslint/no-explicit-any": "off",
    "@typescript-eslint/explicit-module-boundary-types": "off",
    "react-hooks/rules-of-hooks": "error",
    "react-hooks/exhaustive-deps": "warn",
    "react/prop-types": "off",
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-63">.stylelintrc.json</h3>
<pre><code class="copyable">&#123;
  "extends": "stylelint-config-standard"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-64">custom.d.ts</h3>
<pre><code class="copyable">declare module "*.svg" &#123;
  const content: any;
  export default content;
&#125;
declare module "*.png" &#123;
  const content: any;
  export default content;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-65">package.json</h3>
<pre><code class="copyable">&#123;
  "name": "demo",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "npx webpack server --config webpack.dev.js",
    "build": "npx webpack --config webpack.prod.js"
  &#125;,
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": &#123;
    "@babel/core": "^7.15.0",
    "@babel/preset-env": "^7.15.0",
    "@babel/preset-react": "^7.14.5",
    "@types/react": "^17.0.19",
    "@typescript-eslint/eslint-plugin": "^4.29.3",
    "@typescript-eslint/parser": "^4.29.3",
    "antd": "^4.16.13",
    "autoprefixer": "^10.3.2",
    "babel-loader": "^8.2.2",
    "css-loader": "^6.2.0",
    "css-minimizer-webpack-plugin": "^3.0.2",
    "eslint": "^7.32.0",
    "eslint-config-airbnb-typescript": "^14.0.0",
    "eslint-plugin-import": "^2.24.1",
    "eslint-plugin-jsx-a11y": "^6.4.1",
    "eslint-plugin-react": "^7.24.0",
    "eslint-plugin-react-hooks": "^4.2.0",
    "file-loader": "^6.2.0",
    "html-webpack-plugin": "^5.3.2",
    "less-loader": "^10.0.1",
    "mini-css-extract-plugin": "^2.2.0",
    "postcss-loader": "^6.1.1",
    "postcss-preset-env": "^6.7.0",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-router-dom": "^5.2.0",
    "sass": "^1.38.0",
    "sass-loader": "^12.1.0",
    "style-loader": "^3.2.1",
    "stylelint": "^13.13.1",
    "stylelint-config-standard": "^22.0.0",
    "terser-webpack-plugin": "^5.1.4",
    "thread-loader": "^3.0.4",
    "ts-loader": "^9.2.5",
    "typescript": "^4.3.5",
    "webpack": "^5.51.1",
    "webpack-cli": "^4.8.0",
    "webpack-dev-server": "^4.0.0",
    "webpack-merge": "^5.8.0"
  &#125;,
  "browserslist": &#123;
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ],
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ]
  &#125;,
  "eslintConfig": &#123;
    "extends": "airbnb-base"
  &#125;,
  "sideEffects": "*.css"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-66">tsconfig.json</h3>
<pre><code class="copyable">&#123;
  "compilerOptions": &#123;
    "outDir": "./dist/",
    "noImplicitAny": true,
    "module": "es6",
    "target": "es5",
    "jsx": "react",
    "allowJs": true,
    "moduleResolution": "node",
    "allowSyntheticDefaultImports": true
  &#125;,
  "rules": &#123;
    "indent": [true, "spaces", 2],
    "interface-name": false,
    "no-consecutive-blank-lines": false,
    "object-literal-sort-keys": false,
    "ordered-imports": false,
    "quotemark": [true, "single"],
    "semicolon": [true, "never"],
    "trailing-comma": [true, &#123; "multiline": "never", "singleline": "never" &#125;]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-67">webpack.common.js</h3>
<pre><code class="copyable">/**
 * HMR hot module replacement 热模块替换 / 模块热替换
 * 作用：一个模块发生变化，只会重新打包这一个模块(而不是打包所有模块)  可以极大的提升构建速度
 * 样式文件：可以使用HMR功能：因为style-loader内部实现了HMR功能   开发环境使用style-loader会使性能更好 打包速度更快
 * html文件：默认没有HMR功能，代表html不能热更新
 */
const webpack = require('webpack');
const &#123;resolve&#125;=require('path');
const HtmlWebpackPlugin=require('html-webpack-plugin');

module.exports=&#123;
  entry:'./src/index.js',
  /** 多入口:   特点:如果有一个入口最终只有一个bundle
  *                如果有两个入口就有两个bundle
  * entry: &#123;
  *   main: './src/index.js',
  *   test: './src/index.js',
  *  &#125;,
  */
  output:&#123;
    filename:'js/main.js',
    path:resolve(__dirname,'dist'),
    clean:true,
  &#125;,
  /**
   * 解析模块规则别名
   */
  resolve:&#123;
    /**
     * 使用 @ 代替路径 @ 代表从src/ 下面找路径
     */
    alias: &#123;
      "@": resolve(__dirname, 'src/')
    &#125;,
    /**配置省略文件路径的后缀名
     * index.jsx ===  index    index相当于index.jsx
     */
    extensions: [".js", ".jsx", ".json", '.ts', '.tsx'],
    /**配置省略文件路径的后缀名
     * demo/index.jsx ===  demo
     */
    mainFiles: ["index.js", "index.jsx", "index.tsx", "index.ts"]
  &#125;,
  module:&#123;
    rules:[
      &#123;
        /**
        * lazy loading懒加载
        */
        test:/\.(js|jsx)$/,
        include: resolve(__dirname,'src'),
        exclude: /node_modules/,
        /**
         *  pre:优先执行
         *  post:延后执行
         *  不设置enforce则顺序执行
         */
        enforce: 'pre',
        use:[&#123;
          loader:'babel-loader',
          options:&#123;
            presets: [
              '@babel/preset-env',
              '@babel/preset-react',
              '@babel/preset-typescript',
            ],
            // 缓存：第二次构建时，会读取之前的缓存
            cacheDirectory: true,
          &#125;
        &#125;]
      &#125;,
      &#123;
        test:/\.(ts|tsx)$/,
        loader:'ts-loader',
        exclude: /node_modules/
      &#125;,
      &#123;
        test:/\.css$/,
        use:['style-loader','css-loader'],
      &#125;,
      &#123;
        test:/\.less$/,
        use:['style-loader','css-loader','less-loader'],
      &#125;,
      &#123;
        test:/\.s[ac]ss$/,
        use:['style-loader','css-loader','sass-loader']
      &#125;,
      &#123;
        exclude: /.(html|less|css|sass|js|jsx|ts|tsx)$/,
        test: /\.(jpg|jpe|png|gif)$/,
        loader: 'file-loader',
        options: &#123;
          name: 'imgs/[name].[ext]',
          outputPath: 'other'
        &#125;
      &#125;,
      &#123;
        test: /\.(ect|ttf|svg|woff)$/,
        use: &#123;
          loader: 'file-loader',
          options: &#123;
            name: 'icon/[name].[ext]'
          &#125;
        &#125;
      &#125;
    ]
  &#125;,
  plugins:[
    new HtmlWebpackPlugin(&#123;
      template: './index.html',
      title: 'My App',
      minify: &#123;
        removeAttributeQuotes: true,
        removeComments: true,
      &#125;
    &#125;),
    // 显示百分比编译
    new webpack.ProgressPlugin(&#123;
      activeModules: false,
      entries: true,
      modules: true,
      modulesCount: 5000,
      profile: false,
      dependencies: true,
      dependenciesCount: 10000,
      percentBy: 'entries',
    &#125;)
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-68">webpack.dev.js</h3>
<pre><code class="copyable">const &#123;merge&#125;=require('webpack-merge');
const common=require("./webpack.common");
const TerserPlugin = require('terser-webpack-plugin'); // 压缩js打包文件 优化build速度、优化start速度
module.exports=merge(common,&#123;
  mode:'development',
  /**
   * contentBase:'./dist'  运行代码的目录
   * compress:true  启动gzip压缩
   * prot:3000  指定端口号
   * host:'127.0.0.1'  指定域名
   * open:true  自动打开浏览器
   * hot：true   开启HMR功能(热更新)
   * whatchContentBase: true 监视contentBase目录下的所有文件，一旦文件有变化就会reload
   * whatchOptions:&#123;   忽略监视的文件
   *                  ignored:/node_modules/
   *                &#125;
   * overlay:false  如果出现错误不要全屏提示～
   * clientLogLevel:'none'  不要显示启动服务器的日志信息
   * quiet:true   除了一些基本的启动信息外不要打印其他内容
   * 服务器代理
   * proxy:&#123;  解决开大环境的跨域问题
   *          一旦服务器接收到/api的请求就会把请求转发到另外一个服务器(3000)   浏览器和服务器之间存在跨域，但是服务器和服务器之间不存在跨域
   *         '/api': &#123;
   *                target:'http://localhost:3000'
   *          &#125;,
   *          发送请求时，请求路径重写将 /api/xxxx 转换为 /xxx 去掉api
   *          pathRewite:&#123;
   *               '^/api':''
   *          &#125;
   *      &#125;
   */
  devtool:'inline-source-map',
  devServer:&#123;
    hot:true,
    port:3002,
    host:'127.0.0.1',
    compress:true,
    open:true,
    // proxy: &#123;
    //   '/api': &#123;
    //     target: 'http://localhost:8000',
    //     pathRewrite: &#123; '^/api': '' &#125;,
    //     secure: false
    //   &#125;
    // &#125;,
  &#125;,
  optimization: &#123;
    // minimize: false,
    minimizer: [new TerserPlugin(&#123;
      test: /\.(js|jsx|ts|tsx)$/,
      exclude: /node_modules/,
      extractComments: true,
      include: './src',
    &#125;)],
    usedExports: true,
    sideEffects: false
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-69">webpack.prod.js</h3>
<pre><code class="copyable">/**
 * tree shaking   去除无用代码
 * 前提：1、必须使用ES6代码
 *      2、开启production环境会自动开启tree shaking
 * 作用：减少代码体积
 *
 * 在package.json中配置
 *  sideEffects:false  所有代码都没有副作用    (都可以进行tree  shaking)
 *   问题：可能会把css/@babel/polyfile (副作用)文件干掉
 *   解决："sideEffects":["*.css"]
 * */
const webpack = require('webpack');
const &#123;resolve&#125;=require('path');
//  将所有的css提取到同一个文件夹中
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
// 压缩css文件
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const &#123;merge&#125;=require('webpack-merge');
const common=require("./webpack.common");

const cssloader = [
  // 将css提出的方法替换style-loader
  MiniCssExtractPlugin.loader,
  'css-loader',
  &#123;
    loader: 'postcss-loader',
    options: &#123;
      postcssOptions: &#123;
        plugins: [
          ['autoprefixer'],
          require('postcss-preset-env')()
        ]
      &#125;
    &#125;
  &#125;
];
module.exports =merge(common,&#123;
  // 启动环境
  mode: 'production',
  // 转换方法
  module: &#123;
    rules: [
      &#123;
        /**
        * lazy loading懒加载
        */
        test:/\.(js|jsx)$/,
        include: resolve(__dirname,'src'),
        exclude: /node_modules/,
        /**
         *  pre:优先执行
         *  post:延后执行
         *  不设置enforce则顺序执行
         */
        enforce: 'pre',
        use:[&#123;
          loader:'babel-loader',
          options:&#123;
            presets: [
              '@babel/preset-env',
              '@babel/preset-react',
            ],
            // 缓存：第二次构建时，会读取之前的缓存
            cacheDirectory: true,
          &#125;
        &#125;]
      &#125;,
      &#123;
        test: /\.css$/,
        use: [...cssloader]
      &#125;,
      &#123;
        test: /\.less$/,
        use: [...cssloader, 'less-loader'],
      &#125;,
      &#123;
        test: /.s[ac]ss$/,
        use: [...cssloader, 'sass-loader'],
      &#125;,
      &#123;
        exclude: /.(html|less|css|sass|js|jsx|ts|tsx)$/,
        test: /\.(jpg|jpe|png|gif)$/,
        loader: 'file-loader',
        options: &#123;
          name: 'imgs/[name].[ext]',
          outputPath: 'other'
        &#125;
      &#125;,
      &#123;
        test: /\.(ect|ttf|svg|woff)$/,
        use: &#123;
          loader: 'file-loader',
          options: &#123;
            name: 'icon/[name].[ext]'
          &#125;
        &#125;
      &#125;
    ]
  &#125;,
  plugins: [
    new MiniCssExtractPlugin(&#123;
      filename: 'css/main.css'
    &#125;),
    new CssMinimizerPlugin(),
    // 显示百分比编译
    new webpack.ProgressPlugin(&#123;
      activeModules: false,
      entries: true,
      modules: true,
      modulesCount: 5000,
      profile: false,
      dependencies: true,
      dependenciesCount: 10000,
      percentBy: 'entries',
    &#125;)
  ],
  optimization: &#123;
    usedExports: true,
    minimize: true,
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-70">好累呀！！！！ 终于完成。如有不对请指出。谢谢～～～～</h2></div>  
</div>
            