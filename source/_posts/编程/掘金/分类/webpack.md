
---
title: 'webpack'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9859'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 02:06:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=9859'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">入口/出口</h1>
<p>npx 打包，使用 npm init -y 进行初始化(也可以使用 yarn)。要使用 webpack，那么必然需要安装 webpack、webpack-cli:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span>
    <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
    <span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-comment">// 入口文件路径</span>
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'./path/to/my/entry/file.js'</span>,
      <span class="hljs-comment">// 出口</span>
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// 打包后引入文件的前缀</span>
        <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'http://cdn.xxx.com'</span>
        <span class="hljs-comment">// 打包文件输出的路径</span>
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
        <span class="hljs-comment">// 打包后文件名字</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'main.js'</span>,
      &#125;
    &#125;;
    
<span class="hljs-number">2.</span>
     <span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-comment">// 入口文件路径</span>
      <span class="hljs-attr">entry</span>: &#123;
          <span class="hljs-comment">// 打包后的文件名字</span>
          <span class="hljs-attr">text</span>: <span class="hljs-string">'./path/to/my/entry/file.js'</span>
      &#125;,
      <span class="hljs-comment">// 出口</span>
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// 打包文件输出的路径</span>
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
      &#125;,
    &#125;;

<span class="hljs-number">3.</span>
     <span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-comment">// 入口文件路径</span>
      <span class="hljs-attr">entry</span>: &#123;
          <span class="hljs-comment">// 打包后的文件名字(多个文件)</span>
          <span class="hljs-attr">main</span>: <span class="hljs-string">'./path/to/my/entry/file.js'</span>
          <span class="hljs-attr">text</span>: <span class="hljs-string">'./path/to/my/entry/file.js'</span>
      &#125;,
      <span class="hljs-comment">// 出口</span>
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// 打包文件输出的路径</span>
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
        filename：<span class="hljs-string">'[name].js'</span>
      &#125;,
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">loader：</h1>
<p>处理不同类型的文件打包js文件以外的模块：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 图片：</span>
<span class="hljs-comment">// file-loader：打包图片，单独文件</span>
<span class="hljs-comment">// url-loader：打包图片，单独文件，base64格式，可配置：</span>
<span class="hljs-comment">// base64格式：不生成图片文件，图片过大，打包文件大，页面加载时间长，未加载完图片为空白</span>

<span class="hljs-comment">// 样式</span>
<span class="hljs-comment">// style-loader：生成html中的style标签样式</span>
<span class="hljs-comment">// css-loader: 处理样式引用关系</span>

<span class="hljs-comment">// css-loader模块化： </span>
<span class="hljs-comment">// import style from './index.css'</span>
<span class="hljs-comment">// index.css 中的样式保存在style这个变量中</span>
<span class="hljs-comment">// 添加类名：div.calssNmae = style.item</span>
<span class="hljs-comment">// 配置：</span>
<span class="hljs-comment">// &#123;</span>
<span class="hljs-comment">//     loader: 'css-loader',</span>
<span class="hljs-comment">//     opstions: &#123;</span>
<span class="hljs-comment">//      module: true</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-comment">// postcss-loader: 处理css3样式，添加前缀兼容代码</span>
<span class="hljs-comment">// scss-loader：处理scss样式</span>
 <span class="hljs-attr">module</span>: &#123;
     <span class="hljs-comment">// developemt: 测试环境</span>
     <span class="hljs-comment">// production：生产</span>
     <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
     <span class="hljs-comment">// 启用sourceMap,设置为fasle时关闭,</span>
     <span class="hljs-comment">// 常用开发环境：eval-cheap-module-source-map， </span>
     <span class="hljs-comment">// 生产环境（有需要的话）：cheap-module-source-map</span>
     <span class="hljs-attr">devtool</span>: <span class="hljs-string">'eval-cheap-module-source-map'</span>
     <span class="hljs-attr">rules</span>: [
       &#123;
           <span class="hljs-comment">// 打包图片：当文件后缀为jpg|pan|gif时，使用flie-loader插件打包</span>
           <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(jpg|pan|gif)$/</span>,
           <span class="hljs-comment">// use: 'file-loader'</span>
           use: &#123;
               <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>, 
               <span class="hljs-attr">options</span>: &#123;
                   <span class="hljs-comment">// 打包生成的文件，为原来的文件名/格式</span>
                   <span class="hljs-attr">name</span>: <span class="hljs-string">'[name].[ext]'</span> <span class="hljs-comment">// 添加哈希值：[name]_[hash].[ext]</span>
                   <span class="hljs-comment">// 输出文件路径 图片打包到images文件下</span>
                   <span class="hljs-attr">outputPath</span>:<span class="hljs-string">'/images/'</span>
                   <span class="hljs-comment">// 设置图片大小（字节）2048 = 2K，</span>
                   <span class="hljs-comment">// 超过这个大小，生成图片文件，否则base64格式</span>
                   <span class="hljs-attr">limit</span>:<span class="hljs-number">2048</span>
               &#125;
           &#125;
       &#125;,
       &#123;
           <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.css$/</span>
           use:[
               <span class="hljs-string">'style-loader'</span>,
               <span class="hljs-string">'css-loader'</span>,
               <span class="hljs-string">'postcss-loader'</span>, <span class="hljs-comment">// 需要配置</span>
               <span class="hljs-string">'scss-loader'</span>
           ]
       &#125;,
       &#123;
           <span class="hljs-comment">// 处理字体文件</span>
           <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.(eot|svg|ttf|woff)/</span>,
           use: <span class="hljs-string">'flie-loader'</span>
       &#125;
     ]
 &#125;
 <span class="hljs-comment">// 配置postcss-loader</span>
 <span class="hljs-comment">// npm install atuoprefixer -D</span>
 <span class="hljs-comment">// package.json 中添加 </span>
     <span class="hljs-string">"browserslist"</span>:[
         <span class="hljs-string">"> 1%"</span> <span class="hljs-comment">// 大于1%的浏览器</span>
         <span class="hljs-string">"last 2versions"</span> <span class="hljs-comment">// 兼容浏览器的上两个版本</span>
     ]
 <span class="hljs-built_in">module</span>.export = &#123;
     <span class="hljs-attr">plugins</span>: &#123;
         <span class="hljs-built_in">require</span>(<span class="hljs-string">'autoPrefixer)
     &#125;
 &#125;
 

</span><span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">插件</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// npm install --save-dev html-webpack-plugin 自动生成html文件</span>
<span class="hljs-comment">// npm install --save-dev clear-webpack-plugin 删除打包文件</span>
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> &#123; ClearWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clrae-webpack-plugin'</span>);

plugins: [
    <span class="hljs-comment">// 自动生成HTML文件</span>
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123; 
      <span class="hljs-comment">// 引入html模板文件</span>
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span> 
    &#125;),
    <span class="hljs-comment">// 删除打包文件，HtmlWebpackPlugin重新生成文件</span>
    <span class="hljs-keyword">new</span> ClearWebpackPlugin()
],
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">webpackDevserve</h1>
<p>自动打包，热加载，请求转发,代理（只能在测试环境上使用）,模块热替换</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// webpackDevServe：不需要重新打包</span>
     <span class="hljs-comment">// 1. 自动打包</span>
         <span class="hljs-comment">// 配置命令：webpack内置命令启动项目</span>
        <span class="hljs-string">"script"</span>:&#123;
            <span class="hljs-string">"watch"</span>: <span class="hljs-string">"webpack --watck"</span>
        &#125;
        <span class="hljs-built_in">module</span>.exports = &#123;
          <span class="hljs-attr">plugins</span>:&#123;
            <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123; 
              <span class="hljs-comment">// 引入html模板文件</span>
              <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span> ,
              <span class="hljs-attr">cache</span>: <span class="hljs-literal">false</span>
            &#125;),
          &#125;
        &#125;;
     <span class="hljs-comment">//  2. 自动打包，热加载，请求转发</span>
         <span class="hljs-comment">// 配置启动命令</span>
         <span class="hljs-string">"script"</span>:&#123;
             <span class="hljs-comment">// 自动打包</span>
            <span class="hljs-string">"start"</span>: <span class="hljs-string">"webpack serve"</span>
        &#125;
         <span class="hljs-built_in">module</span>.exports = &#123;
          <span class="hljs-attr">debServe</span>: &#123;
             <span class="hljs-comment">// 自动打包</span>
             <span class="hljs-comment">// contentBase: './dist',</span>
             <span class="hljs-comment">// 热加载</span>
             <span class="hljs-string">"static"</span>：<span class="hljs-string">"./dist"</span>,
             <span class="hljs-comment">// 模块热替换，启动HMR：css不需要配置，，js需要配置</span>
             <span class="hljs-string">"hot"</span>: <span class="hljs-literal">true</span>
              <span class="hljs-comment">// 请求转发</span>
              <span class="hljs-attr">proxy</span>: &#123;
                  <span class="hljs-comment">// 请求路径开头为api/xxx时,在前面加上域名</span>
                  <span class="hljs-string">'/api/xxx'</span>: &#123;
                      target：<span class="hljs-string">"http://xxx.xxx"</span>,
                      <span class="hljs-comment">// 所以以api开头的都替换成''</span>
                      <span class="hljs-attr">pathRewrite</span>: &#123;
                          <span class="hljs-string">'^api'</span>: <span class="hljs-string">''</span>
                      &#125;
                      <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>
                  &#125;
              &#125;
          &#125;,
          <span class="hljs-attr">plugins</span>:&#123;
            <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123; 
              <span class="hljs-comment">// 引入html模板文件</span>
              <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span> ,
              <span class="hljs-attr">cache</span>: <span class="hljs-literal">false</span>
            &#125;),
          &#125;
        &#125;;
        
         <span class="hljs-comment">// js热加载</span>
         <span class="hljs-comment">// 入口文件，中执行</span>
         <span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.hot) &#123;
            <span class="hljs-built_in">module</span>.hot.accepy(<span class="hljs-string">"./number.js"</span>, <span class="hljs-function">() =></span> &#123;
                <span class="hljs-comment">// 获取dom元素</span>
                <span class="hljs-keyword">const</span> numberDiv = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'number'</span>)
               <span class="hljs-comment">// remove掉dom元素</span>
                <span class="hljs-built_in">document</span>.dody.removeChild(numberDiv)
                <span class="hljs-comment">// 重新执行number方法,重新生成dom元素</span>
                number()
           &#125;)
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>babel处理ES6语法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ES6语法转换为ES5语法</span>
<span class="hljs-comment">// npm install --save-dev babel-loader @babel/core</span>
<span class="hljs-comment">// npm install @babel/preset-env --save-dev</span>
<span class="hljs-comment">// 兼容低版本浏览器：polyfill: npm install --save @babel/polyfill</span>
<span class="hljs-comment">// 在使用了ES6语法的js文件引入：import '@babel/polyfill'</span>
<span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: &#123;
        <span class="hljs-comment">// 文件以js结尾的</span>
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\/js$/</span>,
        <span class="hljs-comment">// 排除node_module文件下的js文件,依赖</span>
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">"babel-loader"</span>,
            <span class="hljs-comment">// opstions: ['@babel/preset--env']</span>
             <span class="hljs-attr">opstions</span>: &#123;
                [<span class="hljs-string">'@babel/preset--env'</span>],
                &#123;
                    <span class="hljs-comment">// 配置@babel/polyfill,只引入需要文件中需要转换的ES6语法</span>
                    <span class="hljs-attr">useBuiltins</span>: <span class="hljs-string">'usage'</span>
                &#125;
            &#125;
        &#125;
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            