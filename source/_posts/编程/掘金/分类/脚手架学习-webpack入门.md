
---
title: '脚手架学习-webpack入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7fb90b066c7424a90239f6e0c960a6b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 07:13:52 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7fb90b066c7424a90239f6e0c960a6b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557?share_token=f6aeb154-c823-4ed1-91b3-8548eb91ca10" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">一、Node项目如何支持ES Module</h1>
<h2 data-id="heading-1">1.安装webpack及配置</h2>
<pre><code class="hljs language-js copyable" lang="js">npm i -D webpack webpack-cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置webpack.config.js文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./bin/core.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">'/dist'</span>),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'core.js'</span>
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>__dirname是指当前文件</li>
<li>dist目录，会在打包的过程中创建目录，</li>
<li>filename是文件的名称，</li>
<li>mode是指当前的模式，是生产模式还是打包模式</li>
</ol>
<p>创建解析文件core.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello webpack'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并在index.js文件中引用，注意，我们引用的是打包后的文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">require</span>(<span class="hljs-string">'../dist/core'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们执行zl1-test命令，</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7fb90b066c7424a90239f6e0c960a6b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>得到以上输出，我们就成功了</p>
<h2 data-id="heading-2">2.支持node内置库</h2>
<pre><code class="hljs language-js copyable" lang="js">npm i -S path-exists
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在utils.js文件中使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> pathExists <span class="hljs-keyword">from</span> <span class="hljs-string">'path-exists'</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">exists</span>(<span class="hljs-params">p</span>) </span>&#123;
  <span class="hljs-keyword">return</span> pathExists.sync(p)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>core.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>
<span class="hljs-keyword">import</span> &#123; exists &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils'</span>

<span class="hljs-built_in">console</span>.log(path.resolve(<span class="hljs-string">'.'</span>))
<span class="hljs-built_in">console</span>.log(exists(path.resolve(<span class="hljs-string">'.'</span>)))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行npm run build时会报以下错误</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac7ecbf51cbf4aa4bdf5c132d83b52e4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改webpakc.config的配置</p>
<pre><code class="hljs language-js copyable" lang="js">target: <span class="hljs-string">'node'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置为node,编译为类node环境，再次执行命令</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6ca9bbac4cf43a6a1e4892e0892d5d6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编译成功</p>
<h1 data-id="heading-3">二、配置babel-loader支持低版本node</h1>
<h2 data-id="heading-4">1.babel-loader支持低版本node</h2>
<pre><code class="hljs language-js copyable" lang="js"> npm i -D babel-loader @babel/core @babel/preset-env
 npm i -D @babel/plugin-transform-runtime
 npm i -D @babel/runtime-corejs3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上边是需要安装的依赖</p>
<p>core.js</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">reslove</span> =></span> <span class="hljs-built_in">setTimeout</span>(reslove, <span class="hljs-number">10000</span>));
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ok'</span>);
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置webpack.config文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preset-env'</span>],
            <span class="hljs-attr">plugins</span>: [
              [
                <span class="hljs-string">'@babel/plugin-transform-runtime'</span>,
                &#123;
                  <span class="hljs-attr">corejs</span>: <span class="hljs-number">3</span>,
                  <span class="hljs-attr">regenerator</span>: <span class="hljs-literal">true</span>,
                  <span class="hljs-attr">useESModules</span>: <span class="hljs-literal">true</span>,
                  <span class="hljs-attr">helpers</span>: <span class="hljs-literal">true</span>
                &#125;
              ]
            ]
          &#125;
        &#125;
      &#125;
    ]
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置plugins时，请一定要安装好@babel/plugin-transform-runtime，还有使用corejs：3，也记得安装@babel/runtime-corejs3</p>
<p>现在我们可以编译了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9e2498f5f8f4bf5b9ecdeff18a2461b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>请记得分号，尤其要注意，不然你可能报以下错误</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61dc081a7cb14158baf4dc4e18f89634~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">2. node原生支持ESmodule</h2>
<p>将.js的文件修改为.mjs， index文件导入core的方式改为import</p>
<p>运行方式为</p>
<pre><code class="hljs language-js copyable" lang="js">node --experimental-modules bin/index.mjs
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66152154447b4cb09a7cbe2bfeca12a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行成功！！！</p>
<p>node14以上的版本可以直接使用node bin/index.mjs</p></div>  
</div>
            