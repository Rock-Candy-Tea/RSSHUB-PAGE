
---
title: 'webpack搭建vue项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://user-gold-cdn.xitu.io/2019/12/11/16ef2e08b877e7f5?imageView2/0/w/1280/h/960/ignore-error/1'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 06:42:01 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2019/12/11/16ef2e08b877e7f5?imageView2/0/w/1280/h/960/ignore-error/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、入门</h1>
<h2 data-id="heading-1">1.1 初始化项目</h2>
<p>新建一个目录，初始化npm</p>
<pre><code class="copyable">npm init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack是运行在node环境中的,我们需要安装以下两个npm包</p>
<pre><code class="hljs language-js copyable" lang="js">npm i -D webpack webpack-cli
<span class="hljs-comment">// npm i -D 为npm install --save-dev的缩写</span>
<span class="hljs-comment">// npm i -S 为npm install --save的缩写</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果下载不了，安装淘宝镜像：</p>
<pre><code class="copyable">npm install -g cnpm --registry=http://registry.npm.taobao.org
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果出现（cnpm : 无法加载文件 C:\Users\hp\AppData\Roaming\npm\cnpm.ps1，因为在此系统上禁止运行脚本。），以管理员身份运行power shell：</p>
<pre><code class="copyable">set-ExecutionPolicy RemoteSigned
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后根据提示输入 A 回车，就可以使用cnpm了，然后：</p>
<pre><code class="copyable">cnpm i -D webpack webpack-cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就可以下载成功了。</p>
<p>新建一个文件夹<code>src</code> ,然后新建一个文件<code>main.js</code>,写一点代码测试一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'测试一下...'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置package.json命令：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"webpack src/main.js"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行：</p>
<pre><code class="copyable">npm run build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时如果生成了一个dist文件夹，并且内部含有main.js说明已经打包成功了。</p>
<h2 data-id="heading-2">1.2 配置</h2>
<p>上面一个简单的例子只是webpack自己默认的配置，下面我们要实现更加丰富的自定义配置</p>
<ul>
<li>
<p>新建一个<code>build</code>文件夹,里面新建一个<code>webpack.config.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>

<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>:<span class="hljs-string">'development'</span>, <span class="hljs-comment">// 开发模式</span>
    <span class="hljs-attr">entry</span>: path.resolve(__dirname,<span class="hljs-string">'../src/main.js'</span>),    <span class="hljs-comment">// 入口文件</span>
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'output.js'</span>,      <span class="hljs-comment">// 打包后的文件名称</span>
        <span class="hljs-attr">path</span>: path.resolve(__dirname,<span class="hljs-string">'../dist'</span>)  <span class="hljs-comment">// 打包后的目录，不用新建，打包后自动生成</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>更改我们的打包命令</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"webpack --config build/webpack.config.js"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>执行 <code>npm run build</code> 会发现dist目录生成了了output.js文件其中<code>output.js</code>就是我们需要在浏览器中实际运行的文件。当然实际运用中不会仅仅如此,下面让我们通过实际案例带你快速入手webpack。</p>
</li>
</ul>
<h2 data-id="heading-3">1.3 配置HTML模板</h2>
<p>js文件打包好了，但是我们不可能每次在<code>html</code>文件中手动引入打包好的js。</p>
<p>这里可能有的朋友会认为我们打包js文件名称不是一直是固定的嘛(output.js)？这样每次就不用改动引入文件名称了呀？实际上我们日常开发中往往会这样配置:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// 省略其他配置</span>
    <span class="hljs-attr">output</span>: &#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[hash:8].js'</span>,      <span class="hljs-comment">// 打包后的文件名称</span>
      <span class="hljs-attr">path</span>: path.resolve(__dirname,<span class="hljs-string">'../dist'</span>)  <span class="hljs-comment">// 打包后的目录</span>
    &#125;
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候生成的<code>dist</code>目录文件如下</p>
<p><img src="https://user-gold-cdn.xitu.io/2019/12/11/16ef2e08b877e7f5?imageView2/0/w/1280/h/960/ignore-error/1" alt="p3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了缓存（浏览器缓存策略），你会发现打包好的js文件的名称每次都不一样。</p>
<h3 data-id="heading-4">1.3.1 html-webpack-plugin</h3>
<p>webpack打包出来的js文件我们需要引入到html中，但是每次我们都手动修改js文件名显得很麻烦，因此我们需要一个插件来帮我们完成这件事情。</p>
<pre><code class="copyable">npm i -D html-webpack-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建一个<code>build</code>同级的文件夹<code>public</code>,里面新建一个index.html。</p>
<p>同时，<code>webpack.config.js</code>里面做如下添加：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>, <span class="hljs-comment">// 开发模式</span>
    <span class="hljs-attr">entry</span>: path.resolve(__dirname, <span class="hljs-string">'../src/main.js'</span>), <span class="hljs-comment">// 入口文件</span>
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[hash:8].js'</span>, <span class="hljs-comment">// 打包后的文件名称(为了缓存，每次打包好的文件名字不一样)</span>
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../dist'</span>) <span class="hljs-comment">// 打包后的目录</span>
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>:path.resolve(__dirname,<span class="hljs-string">'../public/index.html'</span>) <span class="hljs-comment">// 在public下的index.html引入打包好的js</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再使用命令打包，在dist文件中会出现index.html，可以发现打包生成的js文件已经被自动引入html文件中</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"main.de1ae303.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span><span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.3.2 多入口文件如何开发</h3>
<p>生成多个html-webpack-plugin实例来解决这个问题</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>:<span class="hljs-string">'development'</span>, <span class="hljs-comment">// 开发模式</span>
    <span class="hljs-attr">entry</span>: &#123;
      <span class="hljs-attr">main</span>:path.resolve(__dirname,<span class="hljs-string">'../src/main.js'</span>),
      <span class="hljs-attr">header</span>:path.resolve(__dirname,<span class="hljs-string">'../src/header.js'</span>)
  &#125;, 
    <span class="hljs-attr">output</span>: &#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[hash:8].js'</span>,      <span class="hljs-comment">// 打包后的文件名称</span>
      <span class="hljs-attr">path</span>: path.resolve(__dirname,<span class="hljs-string">'../dist'</span>)  <span class="hljs-comment">// 打包后的目录</span>
    &#125;,
    <span class="hljs-attr">plugins</span>:[
      <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
        <span class="hljs-attr">template</span>:path.resolve(__dirname,<span class="hljs-string">'../public/index.html'</span>),
        <span class="hljs-attr">filename</span>:<span class="hljs-string">'index.html'</span>,
        <span class="hljs-attr">chunks</span>:[<span class="hljs-string">'main'</span>] <span class="hljs-comment">// 与入口文件对应的模块名</span>
      &#125;),
      <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
        <span class="hljs-attr">template</span>:path.resolve(__dirname,<span class="hljs-string">'../public/header.html'</span>),
        <span class="hljs-attr">filename</span>:<span class="hljs-string">'header.html'</span>,
        <span class="hljs-attr">chunks</span>:[<span class="hljs-string">'header'</span>] <span class="hljs-comment">// 与入口文件对应的模块名</span>
      &#125;),
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包后，文件目录如下：</p>
<p><img src="https://user-gold-cdn.xitu.io/2019/12/11/16ef2e1ff51375aa?imageView2/0/w/1280/h/960/ignore-error/1" alt="p5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">1.3.3 clean-webpack-plugin</h3>
<p>每次执行<code>npm run build</code> 会发现dist文件夹里会残留上次打包的文件，这里我们推荐一个plugin来帮我们在打包输出前清空文件夹<code>clean-webpack-plugin</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123;CleanWebpackPlugin&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// ...省略其他配置</span>
    <span class="hljs-attr">plugins</span>:[
        <span class="hljs-comment">// ...省略其他插件</span>
        <span class="hljs-keyword">new</span> CleanWebpackPlugin()
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">1.4 引用 CSS</h2>
<h3 data-id="heading-8">1.4.1 loader</h3>
<p>我们的入口文件是<code>main.js</code>，所以我们需要在入口中引入我们的css文件。</p>
<p><img src="https://user-gold-cdn.xitu.io/2019/12/11/16ef2e43d850e765?imageView2/0/w/1280/h/960/ignore-error/1" alt="p6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，我们也需要一些loader来解析我们的css文件</p>
<pre><code class="copyable">npm i -D style-loader css-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们使用less来构建样式，则需要多安装两个</p>
<pre><code class="copyable">npm i -D less less-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置文件如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// ...省略其他配置</span>
    <span class="hljs-attr">module</span>:&#123;
      <span class="hljs-attr">rules</span>:[
        &#123;
          <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.css$/</span>,
          use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>] <span class="hljs-comment">// 从右向左解析原则</span>
        &#125;,
        &#123;
          <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,
          use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>,<span class="hljs-string">'less-loader'</span>] <span class="hljs-comment">// 从右向左解析原则</span>
        &#125;
      ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器打开<code>html</code>如下，这时候我们发现css通过style标签的方式添加到了html文件中，但是如果样式文件很多，全部添加到html中，难免显得混乱。这时候我们想用把css拆分出来用外链的形式引入css文件怎么做呢？这时候我们就需要借助插件来帮助我们</p>
<p><img src="https://user-gold-cdn.xitu.io/2019/12/11/16ef2e4dc3ba12b4?imageView2/0/w/1280/h/960/ignore-error/1" alt="p7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">1.4.2 拆分 CSS</h3>
<p>webpack 4.0以前，我们通过<code>extract-text-webpack-plugin</code>插件，把css样式从js文件中提取到单独的css文件中。webpack4.0以后，官方推荐使用<code>mini-css-extract-plugin</code>插件来打包css文件</p>
<pre><code class="copyable">npm i -D mini-css-extract-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置文件如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mini-css-extract-plugin"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">//...省略其他配置</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: [
           MiniCssExtractPlugin.loader,
          <span class="hljs-string">'css-loader'</span>,
          <span class="hljs-string">'less-loader'</span>
        ],
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">"[name].[hash].css"</span>,
        <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">"[id].css"</span>,
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">1.4.3 拆分多个 CSS</h3>
<p>这里需要说的细一点,上面我们所用到的<code>mini-css-extract-plugin</code>会将所有的css样式合并为一个css文件。如果你想拆分为一一对应的多个css文件,我们需要使用到<code>extract-text-webpack-plugin</code>，而目前<code>mini-css-extract-plugin</code>还不支持此功能。我们需要安装@next版本的<code>extract-text-webpack-plugin</code></p>
<pre><code class="copyable">npm i -D extract-text-webpack-plugin@next
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> ExtractTextWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'extract-text-webpack-plugin'</span>)
<span class="hljs-keyword">let</span> indexLess = <span class="hljs-keyword">new</span> ExtractTextWebpackPlugin(<span class="hljs-string">'index.less'</span>);
<span class="hljs-keyword">let</span> indexCss = <span class="hljs-keyword">new</span> ExtractTextWebpackPlugin(<span class="hljs-string">'index.css'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>:&#123;
      <span class="hljs-attr">rules</span>:[
        &#123;
          <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.css$/</span>,
          use: indexCss.extract(&#123;
            <span class="hljs-attr">use</span>: [<span class="hljs-string">'css-loader'</span>]
          &#125;)
        &#125;,
        &#123;
          <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,
          use: indexLess.extract(&#123;
            <span class="hljs-attr">use</span>: [<span class="hljs-string">'css-loader'</span>,<span class="hljs-string">'less-loader'</span>]
          &#125;)
        &#125;
      ]
    &#125;,
    <span class="hljs-attr">plugins</span>:[
      indexLess,
      indexCss
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">1.4.4 css添加浏览器前缀</h3>
<pre><code class="copyable">npm i -D postcss-loader autoprefixer
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>:&#123;
        <span class="hljs-attr">rules</span>:[
            &#123;
                <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,
                use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>,<span class="hljs-string">'postcss-loader'</span>,<span class="hljs-string">'less-loader'</span>] <span class="hljs-comment">// 从右向左解析原则</span>
           &#125;
        ]
    &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们还需要引入<code>autoprefixer</code>使其生效，直接在<code>webpack.config.js</code>里配置</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: indexLess.extract(&#123;
            <span class="hljs-attr">use</span>: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, &#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">plugins</span>: [<span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>)]
                &#125;
            &#125;, <span class="hljs-string">'less-loader'</span>]
        &#125;) <span class="hljs-comment">// 从右向左解析原则</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">1.5 打包 图片、字体、媒体</h2>
<p>webpack加载css背景图片、img元素指向的网络图片、使用es6的import引入的图片时，需要使用url-loader或者file-loader。 url-loader和file-loader可以加载任何文件。</p>
<p><code>file-loader</code>就是将文件在进行一些处理后（主要是处理文件名和路径、解析文件url），并将文件移动到输出的目录中</p>
<p><code>url-loader</code> 一般与<code>file-loader</code>搭配使用，功能与 file-loader 类似，url-loader可以将图片转为base64字符串，能更快的加载图片，一旦图片过大， 就需要使用file-loader的加载本地图片，故url-loader可以设置图片超过多少字节时，使用file-loader加载图片。</p>
<p>webpack.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略其它配置 ...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// ...</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpe?g|png|gif)$/i</span>, <span class="hljs-comment">//图片文件</span>
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>,
              <span class="hljs-attr">fallback</span>: &#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">name</span>: <span class="hljs-string">'img/[name].[hash:8].[ext]'</span>
                &#125;
              &#125;
            &#125;
          &#125;
        ]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/</span>, <span class="hljs-comment">//媒体文件</span>
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>,
              <span class="hljs-attr">fallback</span>: &#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                  <span class="hljs-attr">name</span>: <span class="hljs-string">'media/[name].[hash:8].[ext]'</span>
                &#125;
              &#125;
            &#125;
          &#125;
        ]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(woff2?|eot|ttf|otf)(\?.*)?$/i</span>, <span class="hljs-comment">// 字体</span>
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>,
              <span class="hljs-attr">fallback</span>: &#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                  <span class="hljs-attr">name</span>: <span class="hljs-string">'fonts/[name].[hash:8].[ext]'</span>
                &#125;
              &#125;
            &#125;
          &#125;
        ]
      &#125;,
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">1.6 babel转义js文件</h2>
<p>为了使我们的js代码兼容更多的环境我们需要安装依赖</p>
<pre><code class="copyable">npm i -D babel-loader @babel/preset-env @babel/core
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意 <code>babel-loader</code>与<code>babel-core</code>的版本对应关系</p>
<blockquote>
<ol>
<li><code>babel-loader</code> 8.x 对应<code>babel-core</code> 7.x</li>
<li><code>babel-loader</code> 7.x 对应<code>babel-core</code> 6.x</li>
</ol>
</blockquote>
<p>配置如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// 省略其它配置 ...</span>
    <span class="hljs-attr">module</span>:&#123;
        <span class="hljs-attr">rules</span>:[
          &#123;
            <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.js$/</span>,
            use:&#123;
              <span class="hljs-attr">loader</span>:<span class="hljs-string">'babel-loader'</span>,
              <span class="hljs-attr">options</span>:&#123;
                <span class="hljs-attr">presets</span>:[<span class="hljs-string">'@babel/preset-env'</span>]
              &#125;
            &#125;,
            <span class="hljs-attr">exclude</span>:<span class="hljs-regexp">/node_modules/</span>
          &#125;,
       ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的<code>babel-loader</code>只会将 ES6/7/8语法转换为ES5语法，但是对新api并不会转换 例如(promise、Generator、Set、Maps、Proxy等).。此时我们需要借助babel-polyfill来帮助我们转换。</p>
<pre><code class="copyable">npm i @babel/polyfill
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: [<span class="hljs-string">"@babel/polyfill"</span>,path.resolve(__dirname,<span class="hljs-string">'../src/main.js'</span>)],    <span class="hljs-comment">// 入口文件</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">二、搭建 Vue 开发环境</h1>
<p>上面的小例子已经帮助而我们实现了打包css、图片、js、html等文件。 但是我们还需要以下几种配置：</p>
<h2 data-id="heading-15">2.1 解析 .vue 文件</h2>
<pre><code class="copyable">npm i -D vue-loader vue-template-compiler vue-style-loader
npm i -S vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>vue-loader</code> 用于解析<code>.vue</code>文件
<code>vue-template-compiler</code> 用于编译模板</p>
<p>配置如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> vueLoaderPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-loader/lib/plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>:&#123;
        <span class="hljs-attr">rules</span>:[&#123;
            <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.vue$/</span>,
            use:[<span class="hljs-string">'vue-loader'</span>]
        &#125;,]
     &#125;,
    <span class="hljs-attr">resolve</span>:&#123;
        <span class="hljs-comment">// 别名，方便引入文件</span>
        <span class="hljs-attr">alias</span>:&#123;
          <span class="hljs-string">'vue$'</span>:<span class="hljs-string">'vue/dist/vue.runtime.esm.js'</span>,
          <span class="hljs-string">' @'</span>:path.resolve(__dirname,<span class="hljs-string">'../src'</span>)
        &#125;,
        <span class="hljs-comment">// 以下文件不需要写后缀名就可以导入</span>
        <span class="hljs-attr">extensions</span>:[<span class="hljs-string">'*'</span>,<span class="hljs-string">'.js'</span>,<span class="hljs-string">'.json'</span>,<span class="hljs-string">'.vue'</span>]
   &#125;,
   <span class="hljs-attr">plugins</span>:[
        <span class="hljs-keyword">new</span> vueLoaderPlugin()
   ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，在loader中也要加入 <code>vue-style-loader</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    test: /\.css$/,
    use: indexCss.extract(&#123;
        use: ['vue-style-loader','style-loader', 'css-loader', &#123;
            loader: 'postcss-loader',
            options: &#123;
                plugins: [require('autoprefixer')]
            &#125;
        &#125;]
    &#125;) <span class="hljs-comment">// 从右向左解析原则</span>
&#125;,
&#123;
    test: /\.less$/,
    use: indexLess.extract(&#123;
        use: ['vue-style-loader','style-loader', 'css-loader', &#123;
            loader: 'postcss-loader',
            options: &#123;
                plugins: [require('autoprefixer')]
            &#125;
        &#125;, 'less-loader']
    &#125;) <span class="hljs-comment">// 从右向左解析原则</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">2.2 webpack-dev-server 热更新</h2>
<pre><code class="copyable">npm i -D webpack-dev-server
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack.config.js 配置如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...省略其他配置</span>
  <span class="hljs-attr">devServer</span>:&#123;
    <span class="hljs-attr">port</span>:<span class="hljs-number">3000</span>,
    <span class="hljs-attr">hot</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-attr">contentBase</span>:<span class="hljs-string">'../dist'</span>
  &#125;,
  <span class="hljs-attr">plugins</span>:[
    <span class="hljs-keyword">new</span> Webpack.HotModuleReplacementPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
<span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"webpack --config build/webpack.config.js"</span>,
    <span class="hljs-attr">"dev"</span>: <span class="hljs-string">"webpack-dev-server --config build/webpack.config.js --open"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行<code>npm run dev</code> 即可运行项目</p>
<p>完整配置如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>) <span class="hljs-comment">// index.html自动引入打包好的js文件</span>
<span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>) <span class="hljs-comment">// 清除上次打包生成的文件</span>
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mini-css-extract-plugin"</span>) <span class="hljs-comment">// 拆分css</span>
<span class="hljs-keyword">const</span> vueLoaderPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-loader/lib/plugin'</span>) <span class="hljs-comment">// 解析.vue文件</span>
<span class="hljs-keyword">const</span> Webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-keyword">const</span> devMode = process.argv.indexOf(<span class="hljs-string">'--mode=production'</span>) === -<span class="hljs-number">1</span>; <span class="hljs-comment">// 是否生产环境</span>

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>, <span class="hljs-comment">// 开发模式</span>
    <span class="hljs-attr">entry</span>: [<span class="hljs-string">"@babel/polyfill"</span>, path.resolve(__dirname, <span class="hljs-string">'../src/main.js'</span>)], <span class="hljs-comment">// 入口文件(使用@babel/polyfill编译)</span>
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[hash:8].js'</span>, <span class="hljs-comment">// 打包后的文件名称(为了缓存，每次打包好的文件名字不一样)</span>
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../dist'</span>) <span class="hljs-comment">// 打包后的目录</span>
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'../public/index.html'</span>) <span class="hljs-comment">// 在public下的index.html引入打包好的js</span>
        &#125;),
        <span class="hljs-keyword">new</span> CleanWebpackPlugin(), <span class="hljs-comment">// 清除上次打包生成的js文件</span>
        <span class="hljs-comment">// 压缩css</span>
        <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
            <span class="hljs-attr">filename</span>: devMode ? <span class="hljs-string">'[name].css'</span> : <span class="hljs-string">'[name].[hash].css'</span>,
            <span class="hljs-attr">chunkFilename</span>: devMode ? <span class="hljs-string">'[id].css'</span> : <span class="hljs-string">'[id].[hash].css'</span>
        &#125;),
        <span class="hljs-keyword">new</span> vueLoaderPlugin(),
        <span class="hljs-keyword">new</span> Webpack.HotModuleReplacementPlugin() <span class="hljs-comment">// 热更新</span>
    ],
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [&#123;
                    <span class="hljs-attr">loader</span>: devMode ? <span class="hljs-string">'vue-style-loader'</span> : MiniCssExtractPlugin.loader,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">publicPath</span>: <span class="hljs-string">"../dist/css/"</span>,
                        <span class="hljs-attr">hmr</span>: devMode
                    &#125;
                &#125;, <span class="hljs-string">'css-loader'</span>, &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">plugins</span>: [<span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>)]
                    &#125;
                &#125;],
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
                use: [&#123;
                    <span class="hljs-attr">loader</span>: devMode ? <span class="hljs-string">'vue-style-loader'</span> : MiniCssExtractPlugin.loader,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">publicPath</span>: <span class="hljs-string">"../dist/css/"</span>,
                        <span class="hljs-attr">hmr</span>: devMode
                    &#125;
                &#125;, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'less-loader'</span>, &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">plugins</span>: [<span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>)]
                    &#125;
                &#125;]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpe?g|png|gif)$/i</span>, <span class="hljs-comment">//图片文件</span>
                use: [
                    &#123;
                        <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
                        <span class="hljs-attr">options</span>: &#123;
                            <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>,
                            <span class="hljs-attr">fallback</span>: &#123;
                                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                                <span class="hljs-attr">options</span>: &#123;
                                    <span class="hljs-attr">name</span>: <span class="hljs-string">'img/[name].[hash:8].[ext]'</span>
                                &#125;
                            &#125;
                        &#125;
                    &#125;
                ]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/</span>, <span class="hljs-comment">//媒体文件</span>
                use: [
                    &#123;
                        <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
                        <span class="hljs-attr">options</span>: &#123;
                            <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>,
                            <span class="hljs-attr">fallback</span>: &#123;
                                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                                <span class="hljs-attr">options</span>: &#123;
                                    <span class="hljs-attr">name</span>: <span class="hljs-string">'media/[name].[hash:8].[ext]'</span>
                                &#125;
                            &#125;
                        &#125;
                    &#125;
                ]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(woff2?|eot|ttf|otf)(\?.*)?$/i</span>, <span class="hljs-comment">// 字体</span>
                use: [
                    &#123;
                        <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
                        <span class="hljs-attr">options</span>: &#123;
                            <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>,
                            <span class="hljs-attr">fallback</span>: &#123;
                                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                                <span class="hljs-attr">options</span>: &#123;
                                    <span class="hljs-attr">name</span>: <span class="hljs-string">'fonts/[name].[hash:8].[ext]'</span>
                                &#125;
                            &#125;
                        &#125;
                    &#125;
                ]
            &#125;,
            <span class="hljs-comment">// 使用 babel编译 js</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                use: &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preset-env'</span>]
                    &#125;
                &#125;,
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;,
            <span class="hljs-comment">// 解析 .vue 文件</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>,
                use: [<span class="hljs-string">'vue-loader'</span>]
            &#125;
        ]
    &#125;,
    <span class="hljs-attr">resolve</span>: &#123;
        <span class="hljs-comment">// 别名</span>
        <span class="hljs-attr">alias</span>: &#123;
            <span class="hljs-string">'vue$'</span>: <span class="hljs-string">'vue/dist/vue.runtime.esm.js'</span>,
            <span class="hljs-string">'@'</span>: path.resolve(__dirname, <span class="hljs-string">'../src'</span>)
        &#125;,
        <span class="hljs-comment">// 以下文件不需要写后缀名就可以导入</span>
        <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'*'</span>, <span class="hljs-string">'.js'</span>, <span class="hljs-string">'.json'</span>, <span class="hljs-string">'.vue'</span>]
    &#125;,
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,
        <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">contentBase</span>: <span class="hljs-string">'../dist'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">2.3 配置打包命令</h2>
<p>前面我们配置好了打包和运行命令：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"webpack --config build/webpack.config.js"</span>,
    <span class="hljs-attr">"dev"</span>: <span class="hljs-string">"webpack-dev-server --config build/webpack.config.js --open"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来让我们测试一下，首先在src新建一个main.js：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App"</span>;

<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建一个 App.vue</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="container">
    <h1>&#123;&#123;initData&#125;&#125;</h1>
  </div>
</template>

<script>
export default &#123;
  name: 'App',
  data() &#123;
    return &#123;
      initData: 'Vue 开发环境运行成功！'
    &#125;;
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>public中的index.html添加一个id为app的盒子</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 <code>npm run dev</code>，如果浏览器出现<strong>Vue开发环境运行成功！</strong>，那么恭喜你，已经成功迈出了第一步。</p>
<h2 data-id="heading-18">2.4 开发环境与生产环境</h2>
<p>实际应用到项目中，我们需要区分开发环境与生产环境，我们在原来webpack.config.js的基础上再新增两个文件</p>
<ul>
<li>
<p><code>webpack.dev.js</code>   开发环境配置文件，开发环境主要实现的是热更新,不要压缩代码，完整的sourceMap</p>
</li>
<li>
<p><code>webpack.prod.js</code>  生产环境配置文件，生产环境主要实现的是压缩代码、提取css文件、合理的sourceMap、分割代码。需要安装以下模块:</p>
</li>
</ul>
<pre><code class="copyable">cnpm i -D  webpack-merge copy-webpack-plugin optimize-css-assets-webpack-plugin uglifyjs-webpack-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ul>
<li><code>webpack-merge</code> 合并配置</li>
<li><code>copy-webpack-plugin</code> 拷贝静态资源</li>
<li><code>optimize-css-assets-webpack-plugin</code> 压缩css</li>
<li><code>uglifyjs-webpack-plugin</code> 压缩js</li>
<li><code>webpack mode</code>设置<code>production</code>的时候会自动压缩js代码。原则上不需要引入<code>uglifyjs-webpack-plugin</code>进行重复工作。但是<code>optimize-css-assets-webpack-plugin</code>压缩css的同时会破坏原有的js压缩，所以这里我们引入<code>uglifyjs</code>进行压缩</li>
</ul>
</blockquote>
<p>webpack.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>)
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-keyword">const</span> vueLoaderPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-loader/lib/plugin'</span>)
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mini-css-extract-plugin"</span>)
<span class="hljs-keyword">const</span> devMode = process.argv.indexOf(<span class="hljs-string">'--mode=production'</span>) === -<span class="hljs-number">1</span>;
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">main</span>: path.resolve(__dirname, <span class="hljs-string">'../src/main.js'</span>)
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../dist'</span>),
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].[hash:8].js'</span>,
        <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'js/[name].[hash:8].js'</span>
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                use: &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preset-env'</span>]
                    &#125;
                &#125;,
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>,
                use: [&#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'vue-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">compilerOptions</span>: &#123;
                            <span class="hljs-attr">preserveWhitespace</span>: <span class="hljs-literal">false</span>
                        &#125;
                    &#125;
                &#125;]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [&#123;
                    <span class="hljs-attr">loader</span>: devMode ? <span class="hljs-string">'vue-style-loader'</span> : MiniCssExtractPlugin.loader,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">publicPath</span>: <span class="hljs-string">"../dist/css/"</span>,
                        <span class="hljs-attr">hmr</span>: devMode
                    &#125;
                &#125;, <span class="hljs-string">'css-loader'</span>, &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">plugins</span>: [<span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>)]
                    &#125;
                &#125;]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
                use: [&#123;
                    <span class="hljs-attr">loader</span>: devMode ? <span class="hljs-string">'vue-style-loader'</span> : MiniCssExtractPlugin.loader,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">publicPath</span>: <span class="hljs-string">"../dist/css/"</span>,
                        <span class="hljs-attr">hmr</span>: devMode
                    &#125;
                &#125;, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'less-loader'</span>, &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">plugins</span>: [<span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>)]
                    &#125;
                &#125;]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jep?g|png|gif)$/</span>,
                use: &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>,
                        <span class="hljs-attr">fallback</span>: &#123;
                            <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                            <span class="hljs-attr">options</span>: &#123;
                                <span class="hljs-attr">name</span>: <span class="hljs-string">'img/[name].[hash:8].[ext]'</span>
                            &#125;
                        &#125;
                    &#125;
                &#125;
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/</span>,
                use: &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>,
                        <span class="hljs-attr">fallback</span>: &#123;
                            <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                            <span class="hljs-attr">options</span>: &#123;
                                <span class="hljs-attr">name</span>: <span class="hljs-string">'media/[name].[hash:8].[ext]'</span>
                            &#125;
                        &#125;
                    &#125;
                &#125;
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(woff2?|eot|ttf|otf)(\?.*)?$/i</span>,
                use: &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>,
                        <span class="hljs-attr">fallback</span>: &#123;
                            <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
                            <span class="hljs-attr">options</span>: &#123;
                                <span class="hljs-attr">name</span>: <span class="hljs-string">'media/[name].[hash:8].[ext]'</span>
                            &#125;
                        &#125;
                    &#125;
                &#125;
            &#125;
        ]
    &#125;,
    <span class="hljs-attr">resolve</span>: &#123;
        <span class="hljs-attr">alias</span>: &#123;
            <span class="hljs-string">'vue$'</span>: <span class="hljs-string">'vue/dist/vue.runtime.esm.js'</span>,
            <span class="hljs-string">' @'</span>: path.resolve(__dirname, <span class="hljs-string">'../src'</span>)
        &#125;,
        <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'*'</span>, <span class="hljs-string">'.js'</span>, <span class="hljs-string">'.json'</span>, <span class="hljs-string">'.vue'</span>]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> CleanWebpackPlugin(),
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'../public/index.html'</span>)
        &#125;),
        <span class="hljs-keyword">new</span> vueLoaderPlugin(),
        <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
            <span class="hljs-attr">filename</span>: devMode ? <span class="hljs-string">'[name].css'</span> : <span class="hljs-string">'[name].[hash].css'</span>,
            <span class="hljs-attr">chunkFilename</span>: devMode ? <span class="hljs-string">'[id].css'</span> : <span class="hljs-string">'[id].[hash].css'</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>webpack.dev.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-keyword">const</span> webpackConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.config.js'</span>)
<span class="hljs-keyword">const</span> WebpackMerge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>) <span class="hljs-comment">// 合并webpack.config.js配置</span>
<span class="hljs-built_in">module</span>.exports = WebpackMerge(webpackConfig, &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
    <span class="hljs-attr">devtool</span>: <span class="hljs-string">'cheap-module-eval-source-map'</span>,
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,
        <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">contentBase</span>: <span class="hljs-string">'../dist'</span>
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> Webpack.HotModuleReplacementPlugin()
    ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>webpack.prod.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> webpackConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.config.js'</span>)
<span class="hljs-keyword">const</span> WebpackMerge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>) <span class="hljs-comment">// 合并配置</span>
<span class="hljs-keyword">const</span> CopyWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'copy-webpack-plugin'</span>) <span class="hljs-comment">// 拷贝静态资源</span>
<span class="hljs-keyword">const</span> OptimizeCssAssetsPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>) <span class="hljs-comment">// 压缩 css</span>
<span class="hljs-keyword">const</span> UglifyJsPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'uglifyjs-webpack-plugin'</span>) <span class="hljs-comment">// 压缩 js</span>
<span class="hljs-built_in">module</span>.exports = WebpackMerge(webpackConfig, &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">devtool</span>: <span class="hljs-string">'cheap-module-source-map'</span>,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> CopyWebpackPlugin([&#123;
            <span class="hljs-attr">from</span>: path.resolve(__dirname, <span class="hljs-string">'../public'</span>),
            <span class="hljs-attr">to</span>: path.resolve(__dirname, <span class="hljs-string">'../dist'</span>)
        &#125;]),
    ],
    <span class="hljs-attr">optimization</span>: &#123;
        <span class="hljs-attr">minimizer</span>: [
            <span class="hljs-keyword">new</span> UglifyJsPlugin(&#123;<span class="hljs-comment">//压缩js</span>
                <span class="hljs-attr">cache</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">parallel</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">sourceMap</span>: <span class="hljs-literal">true</span>
            &#125;),
            <span class="hljs-keyword">new</span> OptimizeCssAssetsPlugin(&#123;&#125;)
        ],
        <span class="hljs-attr">splitChunks</span>: &#123;
            <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
            <span class="hljs-attr">cacheGroups</span>: &#123;
                <span class="hljs-attr">libs</span>: &#123;
                    <span class="hljs-attr">name</span>: <span class="hljs-string">"chunk-libs"</span>,
                    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>,
                    priority: <span class="hljs-number">10</span>,
                    <span class="hljs-attr">chunks</span>: <span class="hljs-string">"initial"</span> <span class="hljs-comment">// 只打包初始时依赖的第三方</span>
                &#125;
            &#125;
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">2.5 优化 webpack 配置</h2>
<p>优化配置对我们来说非常有实际意义，这实际关系到你打包出来文件的大小，打包的速度等。 具体优化可以分为以下几点：</p>
<h3 data-id="heading-20">2.5.1 优化打包速度</h3>
<h4 data-id="heading-21">2.5.1.1 合理的配置mode参数与devtool参数</h4>
<ul>
<li><code>mode</code>可设置<code>development， production</code>两个参数。 如果没有设置，<code>webpack4</code> 会将 <code>mode</code> 的默认值设置为 <code>production</code></li>
<li><code>production</code>模式下会进行<code>tree shaking</code>(去除无用代码)和<code>uglifyjs</code>(代码压缩混淆)</li>
</ul>
<h4 data-id="heading-22">2.5.1.2 缩小文件的搜索范围(配置include exclude alias noParse extensions)</h4>
<ul>
<li><code>alias</code>: 当我们代码中出现 <code>import 'vue'</code>时， webpack会采用向上递归搜索的方式去<code>node_modules</code> 目录下找。为了减少搜索范围我们可以直接告诉webpack去哪个路径下查找。也就是别名(<code>alias</code>)的配置。</li>
<li><code>include exclude</code>： 同样配置<code>include exclude</code>也可以减少<code>webpack loader</code>的搜索转换时间。</li>
<li><code>noParse </code>： 当我们代码中使用到<code>import jq from 'jquery'</code>时，<code>webpack</code>会去解析jq这个库是否有依赖其他的包。但是我们对类似<code>jquery</code>这类依赖库，一般会认为不会引用其他的包(特殊除外,自行判断)。增加<code>noParse</code>属性,告诉<code>webpack</code>不必解析，以此增加打包速度。</li>
<li><code>extensions </code>：<code>webpack</code>会根据<code>extensions</code>定义的后缀查找文件(频率较高的文件类型优先写在前面)</li>
</ul>
<p><img src="https://user-gold-cdn.xitu.io/2019/12/13/16efe4728f877d46?imageView2/0/w/1280/h/960/ignore-error/1" alt="carbon-2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-23">2.5.1.3 使用HappyPack开启多进程Loader转换</h4>
<p>在webpack构建过程中，实际上耗费时间大多数用在loader解析转换以及代码的压缩中。日常开发中我们需要使用Loader对js，css，图片，字体等文件做转换操作，并且转换的文件数据量也是非常大。由于js单线程的特性使得这些转换操作不能并发处理文件，而是需要一个个文件进行处理。HappyPack的基本原理是将这部分任务分解到多个子进程中去并行处理，子进程处理完成后把结果发送到主进程中，从而减少总的构建时间</p>
<pre><code class="copyable">cnpm i -D happypack
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HappyPack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'happypack'</span>)
<span class="hljs-keyword">const</span> os = <span class="hljs-built_in">require</span>(<span class="hljs-string">'os'</span>)
<span class="hljs-keyword">const</span> happyThreadPool = HappyPack.ThreadPool(&#123;<span class="hljs-attr">size</span>: os.cpus().length&#125;)
model.exports = &#123;
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                <span class="hljs-comment">// 把js文件交给id为happyBabel的HappyPack的实例执行</span>
                use: [&#123;<span class="hljs-attr">loader</span>:<span class="hljs-string">'happypack/loader?id=happyBabel'</span>&#125;],
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;
        ],
        <span class="hljs-attr">plugin</span>: [
            <span class="hljs-keyword">new</span> HappyPack(&#123;
            <span class="hljs-attr">id</span>: <span class="hljs-string">'happyBabel'</span>, <span class="hljs-comment">// 与loader对应的id标识</span>
            <span class="hljs-comment">// 用法和 loader 的配置一样，注意这里是loaders</span>
            <span class="hljs-attr">loaders</span>: [
                &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">presets</span>: [[<span class="hljs-string">'@babel/preset-env'</span>]],
                        <span class="hljs-attr">cacheDirectory</span>: <span class="hljs-literal">true</span>
                    &#125;
                &#125;
            ],
            <span class="hljs-attr">threadPool</span>: happyThreadPool <span class="hljs-comment">// 共享进程池</span>
        &#125;)
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">2.5.1.4 webpack-parallel-uglify-plugin</h4>
<p><code>webpack-parallel-uglify-plugin</code>： <strong>增强代码压缩</strong></p>
<p>上面对于loader转换已经做优化，那么下面还有另一个难点就是优化代码的压缩时间。</p>
<pre><code class="copyable">cnpm i -D webpack-parallel-uglify-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ParallelUglifyPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-parallel-uglify-plugin"</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">optimization</span>: &#123;
        <span class="hljs-attr">minimizer</span>: [
            <span class="hljs-keyword">new</span> ParallelUglifyPlugin(&#123;
                <span class="hljs-attr">cacheDir</span>: <span class="hljs-string">'.cache/'</span>,
                <span class="hljs-attr">uglifyJS</span>: &#123;
                    <span class="hljs-attr">output</span>: &#123;
                        <span class="hljs-attr">comments</span>: <span class="hljs-literal">false</span>,
                        <span class="hljs-attr">beautify</span>: <span class="hljs-literal">false</span>
                    &#125;,
                    <span class="hljs-attr">compress</span>: &#123;
                        <span class="hljs-attr">drop_console</span>: <span class="hljs-literal">true</span>,
                        <span class="hljs-attr">collapse_vars</span>: <span class="hljs-literal">true</span>,
                        <span class="hljs-attr">reduce_vars</span>: <span class="hljs-literal">true</span>
                    &#125;
                &#125;
            &#125;)
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">2.5.1.5 抽离第三方模块</h4>
<p>抽离第三方模块：<strong>提高打包速度</strong></p>
<p>对于开发项目中不经常会变更的静态依赖文件。类似于我们的<code>elementUi、vue</code>全家桶等等。因为很少会变更，所以我们不希望这些依赖要被集成到每一次的构建逻辑中去。 这样做的好处是每次更改我本地代码的文件的时候，<code>webpack</code>只需要打包我项目本身的文件代码，而不会再去编译第三方库。以后只要我们不升级第三方包的时候，那么<code>webpack</code>就不会对这些库去打包，这样可以快速的<strong>提高打包的速度</strong>。</p>
<p>这里我们使用<code>webpack</code>内置的<code>DllPlugin DllReferencePlugin</code>进行抽离。在与<code>webpack</code>配置文件同级目录下新建<code>webpack.dll.config.js</code> 代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.dll.config.js</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// 你想要打包的模块的数组</span>
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">vendor</span>: [<span class="hljs-string">'vue'</span>]
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dll/js'</span>), <span class="hljs-comment">// 打包后文件输出的位置</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].dll.js'</span>,
        <span class="hljs-attr">library</span>: <span class="hljs-string">'[name]_library'</span>
        <span class="hljs-comment">// 这里需要和webpack.DllPlugin中的`name: '[name]_library',`保持一致。</span>
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> webpack.DllPlugin(&#123;
            <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'[name]-manifest.json'</span>),
            <span class="hljs-attr">name</span>: <span class="hljs-string">'[name]_library'</span>,
            <span class="hljs-attr">context</span>: __dirname
        &#125;)
    ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>package.json</code>中配置如下命令</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"dll"</span>: <span class="hljs-string">"webpack --config build/webpack.dll.config.js"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来在我们的<code>webpack.config.js</code>中增加以下代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> AddAssetHtmlPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'add-asset-html-webpack-plugin'</span>) <span class="hljs-comment">// npm i 安装</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> webpack.DllReferencePlugin(&#123;
            <span class="hljs-attr">context</span>: __dirname,
            <span class="hljs-attr">manifest</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'./vendor-manifest.json'</span>)
        &#125;),
        <span class="hljs-keyword">new</span> AddAssetHtmlPlugin(
            [
                &#123;
                    <span class="hljs-attr">filepath</span>: path.resolve(__dirname, <span class="hljs-string">"dll/js/*.dll.js"</span>), <span class="hljs-comment">//将生成的dll文件加入到index.html中</span>
                &#125;,
            ]
        )
    ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行</p>
<pre><code class="copyable">npm run dll
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会发现生成了我们需要的集合第三地方 代码的<code>vendor.dll.js</code> 。这样如果我们没有更新第三方依赖包，就不必<code>npm run dll</code>。直接执行<code>npm run dev npm run build</code>的时候会发现我们的打包速度明显有所提升。因为我们已经通过<code>dllPlugin</code>将第三方依赖包抽离出来了。</p>
<h4 data-id="heading-26">2.5.1.6 cache-loader</h4>
<p><code>-loader</code>：<strong>配置缓存</strong></p>
<blockquote>
<p>我们每次执行构建都会把所有的文件都重复编译一遍，这样的重复工作是否可以被缓存下来呢，答案是可以的，目前大部分 <code>loader</code> 都提供了<code>cache</code> 配置项。比如在 <code>babel-loader</code> 中，可以通过设置<code>cacheDirectory</code> 来开启缓存，<code>babel-loader?cacheDirectory=true</code> 就会将每次的编译结果写进硬盘文件（默认是在项目根目录下的<code>node_modules/.cache/babel-loader</code>目录内，当然你也可以自定义）</p>
</blockquote>
<p>但如果 <code>loader</code> 不支持缓存呢？我们也有方法,我们可以通过<code>cache-loader</code> ，它所做的事情很简单，就是 <code>babel-loader</code> 开启 <code>cache </code>后做的事情，将 <code>loader</code> 的编译结果写入硬盘缓存。再次构建会先比较一下，如果文件较之前的没有发生变化则会直接使用缓存。使用方法如官方 demo 所示，在一些性能开销较大的 loader 之前添加此 loader即可</p>
<pre><code class="copyable">npm i -D cache-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">modeule.exports = &#123;
<span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.ext$/</span>,
                use: [<span class="hljs-string">'cache-loader'</span>, ...loaders],
                <span class="hljs-attr">include</span>: path.resolve(__dirname,<span class="hljs-string">'src'</span>)
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">2.5.2 优化打包文件体积</h3>
<p>打包的速度我们是进行了优化，但是打包后的文件体积却是十分大，造成了页面加载缓慢，浪费流量等，接下来让我们从文件体积上继续优化</p>
<h4 data-id="heading-28">2.5.2.1 引入webpack-bundle-analyzer 分析打包后的文件</h4>
<p><code>webpack-bundle-analyzer</code>将打包后的内容束展示为方便交互的直观树状图，让我们知道我们所构建包中真正引入的内容</p>
<pre><code class="copyable">npm i -D webpack-bundle-analyzer
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://user-gold-cdn.xitu.io/2019/12/16/16f0d6291cc2f70c?imageView2/0/w/1280/h/960/ignore-error/1" alt="carbon-6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">const
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来在<code>package.json</code>里配置启动命令</p>
<pre><code class="copyable">"analyz": "NODE_ENV=production npm_config_report=true npm run build" 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>windows请安装<code>npm i -D cross-env</code></p>
<pre><code class="copyable">"analyz": "cross-env NODE_ENV=production npm_config_report=true npm run build" 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来<code>npm run analyz</code>浏览器会自动打开文件依赖图的网页</p>
<h4 data-id="heading-29">2.5.2.2 externals</h4>
<blockquote>
<p>按照官方文档的解释，如果我们想引用一个库，但是又不想让<code>webpack</code>打包，并且又不影响我们在程序中以<code>CMD、AMD</code>或者<code>window/global</code>全局等方式进行使用，那就可以通过配置<code>Externals</code>。这个功能主要是用在创建一个库的时候用的，但是也可以在我们项目开发中充分使用 <code>Externals</code>的方式，我们将这些不需要打包的静态资源从构建逻辑中剔除出去，而使用 <code>CDN</code> 的方式，去引用它们。</p>
</blockquote>
<p>有时我们希望我们通过<code>script</code>引入的库，如用CDN的方式引入的<code>jquery</code>，我们在使用时，依旧用<code>require</code>的方式来使用，但是却不希望<code>webpack</code>将它又编译进文件中。这里官网案例已经足够清晰明了，大家有兴趣可以点击了解</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fconfiguration%2Fexternals%2F%23root" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/configuration/externals/#root" ref="nofollow noopener noreferrer">webpack</a> 官网案例如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>
  <span class="hljs-attr">src</span>=<span class="hljs-string">"https://code.jquery.com/jquery-3.1.0.js"</span>
  <span class="hljs-attr">integrity</span>=<span class="hljs-string">"sha256-slogkvB1K3VOkzAI8QITxV3VzpOnkeNVsKvtkYLMjfk="</span>
  <span class="hljs-attr">crossorigin</span>=<span class="hljs-string">"anonymous"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">//...</span>
  <span class="hljs-attr">externals</span>: &#123;
    <span class="hljs-attr">jquery</span>: <span class="hljs-string">'jQuery'</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> $ <span class="hljs-keyword">from</span> <span class="hljs-string">'jquery'</span>;
$(<span class="hljs-string">'.my-element'</span>).animate(<span class="hljs-comment">/* ... */</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">2.5.2.3 Tree-shaking</h4>
<blockquote>
<p>这里单独提一下<code>tree-shaking</code>,是因为这里有个坑。<code>tree-shaking</code>的主要作用是用来清除代码中无用的部分。目前在<code>webpack4</code> 我们设置<code>mode</code>为<code>production</code>的时候已经自动开启了<code>tree-shaking</code>。但是要想使其生效，生成的代码必须是ES6模块。不能使用其它类型的模块如<code>CommonJS</code>之流。如果使用<code>Babel</code>的话，这里有一个小问题，因为<code>Babel</code>的预案（preset）默认会将任何模块类型都转译成<code>CommonJS</code>类型，这样会导致<code>tree-shaking</code>失效。修正这个问题也很简单，在<code>.babelrc</code>文件或在<code>webpack.config.js</code>文件中设置<code>modules： false</code>就好了</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// .babelrc</span>
&#123;
  <span class="hljs-string">"presets"</span>: [
    [<span class="hljs-string">"@babel/preset-env"</span>,
      &#123;
        <span class="hljs-string">"modules"</span>: <span class="hljs-literal">false</span>
      &#125;
    ]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>

<span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
        &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
            use: &#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preset-env'</span>, &#123; <span class="hljs-attr">modules</span>: <span class="hljs-literal">false</span> &#125;]
                &#125;
            &#125;，
            <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/(node_modules)/</span>
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            