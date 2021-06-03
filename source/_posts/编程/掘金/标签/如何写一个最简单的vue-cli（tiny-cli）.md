
---
title: '如何写一个最简单的vue-cli（tiny-cli）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6083'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 17:33:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=6083'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><a href="https://github.com/pzl1026/tiny-cli" target="_blank" rel="nofollow noopener noreferrer">demo源码</a>
看着代码更容易理解，代码有注释。</p>
<h1 data-id="heading-0"><strong>仓库说明</strong></h1>
<h2 data-id="heading-1"><strong>base分支</strong></h2>
<p>基础的webpack配置，然后webpack运行项目，这边直接将webpack命令通过package.json的scripts去执行了。</p>
<pre><code class="hljs language-js copyable" lang="js">npm i
npm run watch
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2"><strong>base-vue分支</strong></h2>
<p>vue项目的webpack的一般配置</p>
<pre><code class="hljs language-js copyable" lang="js">npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3"><strong>base-cli分支</strong></h2>
<p>基本的cli所拥有的功能，生成项目，开发环境，生产环境是如何运行的。</p>
<pre><code class="hljs language-js copyable" lang="js">tiny-cli -i app <span class="hljs-comment">//创建一个app项目</span>
cd app
npm i
tiny-cli -d <span class="hljs-comment">//开发环境启动</span>
tiny-cli -b <span class="hljs-comment">//生产编译</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4"><strong>template分支</strong></h2>
<p>用于创建初始项目时需要clone的项目模板</p>
<h1 data-id="heading-5"><strong>需要的哪些模块？</strong></h1>
<p>做成cli，除了webpack和babel等一些基础的编译配置，还需要</p>
<p><a href="https://www.npmjs.com/package/commander" target="_blank" rel="nofollow noopener noreferrer">commander</a>，用于创建终端命令，上面的-d，-b等命令就是通过这个来创建的；</p>
<p><a href="https://www.npmjs.com/package/download-git-repo" target="_blank" rel="nofollow noopener noreferrer">download-git-repo</a>，创建项目的时候需要该模块从git上clone基本的项目目录；</p>
<p><a href="https://www.npmjs.com/package/chalk" target="_blank" rel="nofollow noopener noreferrer">chalk</a>、<a href="https://www.npmjs.com/package/ora" target="_blank" rel="nofollow noopener noreferrer">ora</a>，这两个库是用于编译时美化输出的，为了更好看。</p>
<h1 data-id="heading-6"><strong>以vue框架为例，基本webpack配置？</strong></h1>
<p>详情见源码的<a href="https://github.com/pzl1026/tiny-cli/tree/base-vue" target="_blank" rel="nofollow noopener noreferrer">base-vue分支</a>
常用配置</p>
<ul>
<li>entry：编译入口，当前项目的主要的js文件，比如当前的 src/index.js；</li>
<li>output: 输出配置；</li>
<li>module: 一般常用rules，用于编译不同文件的代码，如es，vue文件等，需要使用的vue-loader,babel-loader等；</li>
<li>plugins：编译时对某些运行钩子要做的事情；</li>
<li>resolve：加快对文件的引用，以及别名的命名等。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> CWD = process.cwd();
<span class="hljs-keyword">const</span> VueLoaderPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-loader/lib/plugin'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> ExtractTextPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'extract-text-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].[hash].js'</span>
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// babel编译</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js|jsx$/</span>,
        loader: <span class="hljs-string">'babel-loader'</span>,
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>,
      &#125;,
      <span class="hljs-comment">// vue编译loader，需要与下面的plugin的VueLoaderPlugin联合使用，不然会报错</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>,
        loader: <span class="hljs-string">'vue-loader'</span>
      &#125;,
      <span class="hljs-comment">// less编译</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'style-loader'</span>
          &#125;,
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
          &#125;,
        ]
      &#125;,
      <span class="hljs-comment">// 对css样式进行编译，包括vue文件里面的style</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: ExtractTextPlugin.extract(&#123;
          <span class="hljs-attr">fallback</span>: <span class="hljs-string">'style-loader'</span>,
          <span class="hljs-attr">use</span>: [<span class="hljs-string">'css-loader'</span>],
        &#125;),
      &#125;,
      <span class="hljs-comment">// 加载静态文件, webpack4版本不需要file-loader单独配置，不然图片出不来（巨坑）</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpg|gif)$/i</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">fallback</span>: <span class="hljs-built_in">require</span>.resolve(<span class="hljs-string">'file-loader'</span>),
              <span class="hljs-attr">limit</span>: <span class="hljs-number">8192</span>,
              <span class="hljs-attr">esModule</span>: <span class="hljs-literal">false</span>,
            &#125;,
          &#125;,
        ],
      &#125;,
    ],
  &#125;,
  <span class="hljs-attr">plugins</span>:  [
    <span class="hljs-comment">// 清空之前的输出目录</span>
    <span class="hljs-keyword">new</span> CleanWebpackPlugin(),
    <span class="hljs-comment">//  以什么html为模板</span>
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">hash</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">'tiny-demo'</span>,
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>,
    &#125;),
    <span class="hljs-keyword">new</span> ExtractTextPlugin(<span class="hljs-string">'style.css'</span>),
    <span class="hljs-comment">// 与vue-loader配合使用，编译vue文件</span>
    <span class="hljs-keyword">new</span> VueLoaderPlugin(),
    <span class="hljs-comment">// 启用热替换</span>
    <span class="hljs-keyword">new</span> webpack.NamedModulesPlugin(),
    <span class="hljs-keyword">new</span> webpack.HotModuleReplacementPlugin(),
  ],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'inline-source-map'</span>,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: <span class="hljs-string">'./dist'</span>,
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-comment">// 别名</span>
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'vue$'</span>: <span class="hljs-string">'vue/dist/vue.esm.js'</span>, <span class="hljs-comment">//这里如果不加这个，import vue时会报错</span>
      <span class="hljs-string">'@'</span>: path.join(CWD, <span class="hljs-string">'./src'</span>) <span class="hljs-comment">//src别名目录</span>
    &#125;,
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'*'</span>, <span class="hljs-string">'.js'</span>, <span class="hljs-string">'.vue'</span>, <span class="hljs-string">'.json'</span>]
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">如何将tiny-cli命令挂载到本地全局访问？</h1>
<p>其实很简单，package.json有个bin配置，将需要运行的nodejs文件配置好即可，如：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-string">"bin"</span>: &#123;
    <span class="hljs-string">"tiny-cli"</span>: <span class="hljs-string">"bin/index.js"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里写好之后，通过npm link就可以将tiny-cli挂载到全局访问，这里其实最终版运行的是bin目录下的index.js文件，最终执行的命令是node bin/index,所有的命令执行将通过bin下面的program文件去判断，当前执行的命令是什么，根据命令的不同通过判断，去做不同的操作，这里只做了三个命令操作，一个创建项目（-i），一个开发环境启动（-d）,一个生产编译（-b）。如果要去除这个tiny-cli全局命令，只需要npm unlink即可。</p>
<h1 data-id="heading-8"><strong>如何执行命令？</strong></h1>
<p>主要代码：bin/program.js</p>
<p>运用模块：<a href="https://www.npmjs.com/package/commander" target="_blank" rel="nofollow noopener noreferrer">commander</a></p>
<p>需要使用commander模块，主要代码在bin/program.js，这里可配置各种不同命令，运行时通过program的对象属性判断，比如，program.dev就是用于判断是否是开发环境</p>
<h1 data-id="heading-9"><strong>如何生成一个基本的template目录？</strong></h1>
<p>主要代码：repo.js</p>
<p>运用模块：<a href="https://www.npmjs.com/package/download-git-repo" target="_blank" rel="nofollow noopener noreferrer">download-git-repo</a></p>
<p>该文件主要处理项目创建时的模板clone,创建时使用了chalk和ora模块，美化了创建时的输出。</p>
<h1 data-id="heading-10">最后</h1>
<p>等一切测试成功之后，就可以直接运行npm publish 发布到自己的npm账号的packages了。自己对着代码，直接运行看看吧，代码较简单，没有附加功能，有问题直接评论区哦！！谢谢各位观看！！</p></div>  
</div>
            