
---
title: 'react+ts+webpack搭建electron项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9570'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 19:04:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=9570'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">项目初始化</h3>
<ol>
<li>项目目录结构</li>
</ol>
<pre><code class="copyable">├── 项目根目录
│ ├── app
│ │ ├── main      // 主进程模块
│ │ │    |—— electron.ts
│ │ │
│ │ ├── renderer  // 渲染进程模块
│ │ └── other // 需要之前打包好的一个项目使用webview引入(项目需要)
│ ├── package.json
│ └──
|___
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>修改package.json</li>
</ol>
<pre><code class="copyable">主要是注意里面的main字段，修改为以下（webpack打包的主线程代码所在位置）

"main": "./dist/electron.js"

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>
<p>安装依赖</p>
<ul>
<li>
<p>安装electron</p>
<pre><code class="copyable">yarn add electron@11.1.1 -D

安装遇到问题

可在根目录下增加.npmrc，增加以下内容

registry=https://registry.npm.taobao.org/
electron_mirror="https://npm.taobao.org/mirrors/electron/"


<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装react相关</p>
<pre><code class="copyable">yarn add react react-router react-router-dom react-dom
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装babel（使用babel-loader加ts的插件去编译ts）</p>
<pre><code class="copyable">yarn add @babel/polyfill 
yarn add @babel/core @babel/cli @babel/preset-env @babel/preset-react @babel/preset- typescript @babel/plugin-transform-runtime  @babel/plugin-transform-modules-commonjs -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>根目录创建babel.config.js</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-built_in">module</span>.exports = &#123;
        <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preset-env'</span>, <span class="hljs-string">'@babel/preset-react'</span>, <span class="hljs-string">'@babel/preset-typescript'</span>],
        <span class="hljs-attr">plugins</span>: [
          <span class="hljs-string">'@babel/plugin-transform-runtime'</span>,
              [
            <span class="hljs-string">'@babel/plugin-transform-modules-commonjs'</span>, 
            &#123;
              <span class="hljs-attr">allowTopLevelThis</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-attr">loose</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-attr">lazy</span>: <span class="hljs-literal">true</span>
            &#125;
      ],
      [
        <span class="hljs-string">'import'</span>, <span class="hljs-comment">// antd按需加载</span>
        &#123;
          <span class="hljs-attr">libraryName</span>: <span class="hljs-string">'antd'</span>,
          <span class="hljs-attr">libraryDirectory</span>: <span class="hljs-string">'es'</span>,
          <span class="hljs-attr">style</span>: <span class="hljs-string">'css'</span>
        &#125;
      ]
    ]
  &#125;


<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装webpack相关（这里使用的还是4版本，5版本尝试了下，一堆报错改的心累就放弃了）</p>
<pre><code class="copyable">yarn add webpack@4.44.1 webpack-cli@3.3.12 webpack-dev-server webpack-merge html-webpack-plugin@4.3.0 clean-webpack-plugin babel-loader -D

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>创建webpack配置</p>
<p>根目录下添加一个webpack文件夹，里面主要有以下文件</p>
<ul>
<li>webpack.base.js</li>
<li>webpack.main.dev.js</li>
<li>webpack.main.prod.js</li>
<li>webpack.render.dev.js</li>
<li>webpack.render.prod.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.base.js</span>

 <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
 <span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>)
 <span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>)

 <span class="hljs-keyword">const</span> isDev = process.env.NODE_ENV !== <span class="hljs-string">'production'</span>

 <span class="hljs-keyword">const</span> getCssLoaders = <span class="hljs-function"><span class="hljs-params">importLoaders</span> =></span> [
   isDev ? <span class="hljs-string">'style-loader'</span> : MiniCssExtractPlugin.loader,
   &#123;
     <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
     <span class="hljs-attr">options</span>: &#123;
       <span class="hljs-attr">modules</span>: <span class="hljs-literal">false</span>,
       <span class="hljs-attr">sourceMap</span>: isDev,
       importLoaders
     &#125;
   &#125;
 ]

 <span class="hljs-built_in">module</span>.exports = &#123;
   <span class="hljs-attr">resolve</span>: &#123;
     <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.js'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.tsx'</span>],
     <span class="hljs-attr">alias</span>: &#123;
       <span class="hljs-string">'@src'</span>: path.join(__dirname, <span class="hljs-string">'../'</span>, <span class="hljs-string">'app/renderer'</span>),
       <span class="hljs-string">'@viz'</span>: path.join(__dirname, <span class="hljs-string">'../'</span>, <span class="hljs-string">'app/viz/index1.html'</span>)
     &#125;
   &#125;,
   <span class="hljs-attr">module</span>: &#123;
     <span class="hljs-attr">rules</span>: [
       &#123;
         <span class="hljs-attr">oneOf</span>: [
           &#123;
             <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx|ts|tsx)$/</span>,
             exclude: <span class="hljs-regexp">/node_modules/</span>,
             use: &#123;
               <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
               <span class="hljs-attr">options</span>: &#123; <span class="hljs-attr">cacheDirectory</span>: <span class="hljs-literal">true</span> &#125;
             &#125;
           &#125;,
           &#123;
             <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
             use: getCssLoaders(<span class="hljs-number">0</span>)
           &#125;,
           &#123;
             <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
             use: [
               ...getCssLoaders(<span class="hljs-number">1</span>),
               &#123;
                 <span class="hljs-attr">loader</span>: <span class="hljs-string">'less-loader'</span>,
                 <span class="hljs-attr">options</span>: &#123;
                   <span class="hljs-attr">sourceMap</span>: isDev
                 &#125;
               &#125;
             ]
           &#125;,
           &#123;
             <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpg|png|jpeg|gif)$/</span>,
             use: [
               &#123;
                 <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                 <span class="hljs-attr">options</span>: &#123;
                   <span class="hljs-attr">name</span>: <span class="hljs-string">'[name]_[hash].[ext]'</span>,
                   <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'images/'</span>
                 &#125;
               &#125;
             ]
           &#125;
         ]
       &#125;
     ]
   &#125;,
   <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> CleanWebpackPlugin(&#123; <span class="hljs-attr">cleanOnceBeforeBuildPatterns</span>: [<span class="hljs-string">'**/*'</span>, <span class="hljs-string">'!electron.js'</span>] &#125;)]
 &#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.main.dev.js</span>
     <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
     <span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.base.js'</span>)
     <span class="hljs-keyword">const</span> webpackMerge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>)

     <span class="hljs-keyword">const</span> mainConfig = &#123;
       <span class="hljs-attr">entry</span>: path.resolve(__dirname, <span class="hljs-string">'../app/main/electron.ts'</span>),
       <span class="hljs-attr">target</span>: <span class="hljs-string">'electron-main'</span>,
       <span class="hljs-attr">output</span>: &#123;
         <span class="hljs-attr">filename</span>: <span class="hljs-string">'electron.js'</span>,
         <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../dist'</span>)
       &#125;,
       <span class="hljs-attr">devtool</span>: <span class="hljs-string">'inline-source-map'</span>,
       <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
     &#125;

     <span class="hljs-built_in">module</span>.exports = webpackMerge.merge(baseConfig, mainConfig)


<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.main.prod.js</span>

        <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
        <span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.base.js'</span>)
        <span class="hljs-keyword">const</span> webpackMerge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>)
        <span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)

        <span class="hljs-keyword">const</span> prodConfig = &#123;
          <span class="hljs-attr">entry</span>: path.resolve(__dirname, <span class="hljs-string">'../app/main/electron.ts'</span>),
          <span class="hljs-attr">target</span>: <span class="hljs-string">'electron-main'</span>,
          <span class="hljs-attr">output</span>: &#123;
            <span class="hljs-attr">filename</span>: <span class="hljs-string">'electron.js'</span>,
            <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../dist'</span>)
          &#125;,
          <span class="hljs-attr">devtool</span>: <span class="hljs-string">'inline-source-map'</span>,
          <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
          <span class="hljs-attr">plugins</span>: [
            <span class="hljs-keyword">new</span> webpack.DefinePlugin(&#123;
              <span class="hljs-attr">__dirname</span>: <span class="hljs-string">'__dirname'</span>
            &#125;)
          ]
        &#125;

        <span class="hljs-built_in">module</span>.exports = webpackMerge.merge(baseConfig, prodConfig)


<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.render.dev.js</span>

<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> webpackMerge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>)
<span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.base.js'</span>)
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)

<span class="hljs-keyword">const</span> devConfig = &#123;
 <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
 <span class="hljs-attr">entry</span>: &#123;
   <span class="hljs-attr">index</span>: path.resolve(__dirname, <span class="hljs-string">'../app/renderer/app.tsx'</span>)
 &#125;,
 <span class="hljs-attr">output</span>: &#123;
   <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[hash].js'</span>,
   <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../dist'</span>)
 &#125;,
 <span class="hljs-attr">target</span>: <span class="hljs-string">'electron-renderer'</span>,
 <span class="hljs-attr">devtool</span>: <span class="hljs-string">'inline-source-map'</span>,
 <span class="hljs-attr">devServer</span>: &#123;
   <span class="hljs-attr">contentBase</span>: path.join(__dirname, <span class="hljs-string">'../dist'</span>),
   <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
   <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>,
   <span class="hljs-attr">port</span>: <span class="hljs-number">7001</span>,
   <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>
 &#125;,
 <span class="hljs-attr">plugins</span>: [
   <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
     <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'../app/renderer/index.html'</span>),
     <span class="hljs-attr">filename</span>: path.resolve(__dirname, <span class="hljs-string">'../dist/index.html'</span>),
     <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'index'</span>]
   &#125;)
 ]
&#125;

<span class="hljs-built_in">module</span>.exports = webpackMerge.merge(baseConfig, devConfig)


<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.render.prod.js</span>

  <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
  <span class="hljs-keyword">const</span> webpackMerge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>)
  <span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.base.js'</span>)
  <span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)

  <span class="hljs-keyword">const</span> prodConfig = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">entry</span>: &#123;
      <span class="hljs-attr">index</span>: path.resolve(__dirname, <span class="hljs-string">'../app/renderer/app.tsx'</span>)
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[hash].js'</span>,
      <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../dist'</span>)
    &#125;,
    <span class="hljs-attr">target</span>: <span class="hljs-string">'electron-renderer'</span>,
    <span class="hljs-attr">devtool</span>: <span class="hljs-string">'inline-source-map'</span>,
    <span class="hljs-attr">plugins</span>: [
      <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
        <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'../app/renderer/index.html'</span>),
        <span class="hljs-attr">filename</span>: path.resolve(__dirname, <span class="hljs-string">'../dist/index.html'</span>),
        <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'index'</span>]
      &#125;)
    ]
  &#125;

  <span class="hljs-built_in">module</span>.exports = webpackMerge.merge(baseConfig, prodConfig)


<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>编写一些代码</p>
<ul>
<li>
<p>在main文件夹下的electron.ts加入如下代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>
<span class="hljs-keyword">import</span> &#123; app, BrowserWindow &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'electron'</span>
<span class="hljs-keyword">import</span> isDev <span class="hljs-keyword">from</span> <span class="hljs-string">'electron-is-dev'</span>

<span class="hljs-keyword">let</span> mainWindow = <span class="hljs-literal">null</span>


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createWindow</span>(<span class="hljs-params"></span>) </span>&#123;
  mainWindow = <span class="hljs-keyword">new</span> BrowserWindow(&#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">1200</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">800</span>,
    <span class="hljs-attr">webPreferences</span>: &#123;
      <span class="hljs-attr">nodeIntegration</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">enableRemoteModule</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">contextIsolation</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">webviewTag</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;)

  <span class="hljs-keyword">if</span> (isDev) &#123;
    mainWindow.loadURL(<span class="hljs-string">`http://127.0.0.1:7001`</span>)
    mainWindow.webContents.openDevTools()
  &#125; <span class="hljs-keyword">else</span> &#123;
    mainWindow.loadURL(<span class="hljs-string">`file://<span class="hljs-subst">$&#123;path.join(__dirname, <span class="hljs-string">'../dist/index.html'</span>)&#125;</span>`</span>)
  &#125;

  mainWindow.on(<span class="hljs-string">'close'</span>, <span class="hljs-function">() =></span> &#123;
    mainWindow = <span class="hljs-literal">null</span>
  &#125;)
&#125;


app.whenReady().then(<span class="hljs-function">() =></span> &#123;
  createWindow()
  app.on(<span class="hljs-string">'activate'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (BrowserWindow.getAllWindows().length === <span class="hljs-number">0</span>) createWindow()
  &#125;)
&#125;)


<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在renderer文件夹下添加index.html</p>
<pre><code class="hljs language-html copyable" lang="html">   <span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
       <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
       <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span> /></span>
       <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
       <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
       <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在renderer文件夹下添加app.tsx</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> &#123; HashRouter <span class="hljs-keyword">as</span> Router, Route, Switch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>基础模板<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            
          <span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Router</span>></span></span>
    );
  &#125;

  ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));


<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>配置package.json文件的脚本</p>
<pre><code class="copyable">
    scripts": &#123;
     "start": "concurrently \"yarn start:render\" \"wait-on http://127.0.0.1:7001 && yarn start:main \"", // 开发环境一个指令整体启动项目，需要安装concurrently和wait-on
     "start:main": "webpack --config ./webpack/webpack.main.dev.js && electron ./dist/electron.js", // 启动主进程
     "start:render": "webpack-dev-server --config ./webpack/webpack.render.dev.js", // 启动渲染进程
     "build": "yarn build:main && yarn build:render", // 打包同上
     "build:main": "webpack --config ./webpack/webpack.main.prod.js",
     "build:render": "webpack --config ./webpack/webpack.render.prod.js",
     "ele:pack": "electron-builder"  // 打包后使用electron-builder（需要安装）构建exe文件
     &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>一些其他的额外配置</p>
<ul>
<li>elsint</li>
<li>husky</li>
<li>css采用css in js</li>
<li>路由使用react-router-config来管理</li>
</ul>
</li>
<li>
<p>更多配置见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FYangJ0605%2Freact_ts_electron_template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/YangJ0605/react_ts_electron_template" ref="nofollow noopener noreferrer">git仓库</a></p>
</li>
<li>
<p>主要参考<a href="https://juejin.cn/book/6950646725295996940" target="_blank" title="https://juejin.cn/book/6950646725295996940">掘金小册 Electron + React 从 0 到 1 实现简历平台实战</a></p>
</li>
</ul>
</li>
</ol></div>  
</div>
            