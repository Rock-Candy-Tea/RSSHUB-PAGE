
---
title: 'webpack实现具有热更新功能的mock接口服务'
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 22:47:04 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. 前言</h1>
<p>在前端进行开发的时候，一定会遇到和中后台进行接口连调。很多时候，中后台和前端开发是并行的，前端进行静态界面功能开发，后端进行接口业务功能开发，这个时候，中后台是无法提供有用的接口的。这个时候，需要有一个 mock 服务来提供模拟的接口数据，供前端来进行调试，这快加快前端开发，并减少后续的与中后台的连调时间。</p>
<p>这里有个前提，接口的路径和返回结果的结构及返回字段需要由中后台提供。mock 服务只在前期开发模式下使用，如果中后台提供了开发环境的接口，那么可以不再依赖 mock 服务。</p>
<p>SPA 前端项目基本上是由 webpack 进行打包，使用 webpack-dev-server 进行开发调试。所以可以使用 webpack-dev-server 来拦截请求，通过解析接口请求路径，并返回相应的模拟的接口数据。</p>
<h1 data-id="heading-1">2. 方案一: devServer.before 解析请求路径并返回接口数据</h1>
<p>在 webpack 的 devServer 选项中，有个钩子方法 before，该方法会在服务器内部的所有其他中间件之前执行定制的功能。所以，在这个方法内，获取请求的路径，判断是否是接口请求，从而返回接口的 mock 数据。</p>
<p>devServer 的配置如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123;apiMocker&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../my-mock-server/index'</span>)

<span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">headers</span>: &#123;
      <span class="hljs-string">"Access-Control-Allow-Origin"</span>: <span class="hljs-string">"*"</span>,
    &#125;, 
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>, 
    <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-string">'9000'</span>,
    <span class="hljs-attr">before</span>: apiMocker
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>my-mock-server/index.js 文件内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">const</span> PREFIX = <span class="hljs-string">'/api/*'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">apiMocker</span>(<span class="hljs-params">app, server</span>) </span>&#123;
  app.get(PREFIX, handerAsyncRequest)
  app.post(PREFIX, handerAsyncRequest)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handerAsyncRequest</span>(<span class="hljs-params">req, res</span>) </span>&#123;
  <span class="hljs-keyword">const</span> reqPath = req.path.replace(<span class="hljs-regexp">/\/api/ig</span>, <span class="hljs-string">''</span>)
  <span class="hljs-keyword">const</span> filePath = path.resolve(__dirname, <span class="hljs-string">`./mocks<span class="hljs-subst">$&#123;reqPath&#125;</span>.js`</span>)
  <span class="hljs-keyword">if</span> (!fs.existsSync(filePath)) &#123;
    res.send(<span class="hljs-string">'文件不存在'</span>)
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">let</span> data = <span class="hljs-built_in">require</span>(filePath)
  res.send(data)
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  apiMocker
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码，devServer 的 before 方法中，通过解析请求路径是否包含 /api 前缀来判断是否为接口请求来读取本地的 mock 数据，数据存放在本地的 my-mock-server/mocks/* 下。</p>
<p>本地开发环境服务启动后，比如 <a href="http://127.0.0.1:9000/" target="_blank" rel="nofollow noopener noreferrer">http://127.0.0.1:9000</a> ，mock 服务器会监听同一个地址和端口。在接口调用中，可以通过设置 baseURL 为 <a href="http://127.0.0.1:9000/" target="_blank" rel="nofollow noopener noreferrer">http://127.0.0.1:9000</a> 来进行调用。</p>
<h1 data-id="heading-2">3. 方案二: 使用 express 提供 mock 服务器</h1>
<p>方案一中，如果 mock 数据在使用中基本不变话，可以考虑使用。但一般情况下，开发过程中会反复的修改 mock 数据来创建一定的业务场景，这个时候，方案一需要重启服务来使修改生效。所以为了提供 mock 数据的热更新功能，有了第二个方案，即使用 express 来提供服务。</p>
<p>启动 express 服务仍然使用了 devServer.before，在该钩子方法内启动 express 服务。webpack 配置如下：</p>
<pre><code class="hljs language-js copyable" lang="js">devServer: &#123;
    <span class="hljs-attr">headers</span>: &#123;
      <span class="hljs-string">"Access-Control-Allow-Origin"</span>: <span class="hljs-string">"*"</span>,
    &#125;,
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-string">'9000'</span>,
    <span class="hljs-function"><span class="hljs-title">before</span>(<span class="hljs-params">app, server</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (process.env.MOCK === <span class="hljs-string">'true'</span>) &#123;
        <span class="hljs-keyword">const</span> entry = path.resolve(__dirname, <span class="hljs-string">'../my-mock-server/index.js'</span>)

        <span class="hljs-comment">// child_process 模块来创建子进程</span>
        <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>).exec(<span class="hljs-string">`node-dev <span class="hljs-subst">$&#123;entry&#125;</span>`</span>)
      &#125;
    &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>my-mock-server/index.js 文件内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> cors = <span class="hljs-built_in">require</span>(<span class="hljs-string">'cors'</span>)
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)

<span class="hljs-keyword">var</span> app = express()
app.use(cors())

app.get(<span class="hljs-string">'/api/demo1'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
  <span class="hljs-keyword">const</span> reqPath = req.path.replace(<span class="hljs-regexp">/\/api/ig</span>, <span class="hljs-string">''</span>)
  <span class="hljs-keyword">const</span> filePath = path.resolve(__dirname, <span class="hljs-string">`./mocks<span class="hljs-subst">$&#123;reqPath&#125;</span>.js`</span>)
  <span class="hljs-keyword">if</span> (!fs.existsSync(filePath)) &#123;
    res.send(<span class="hljs-string">'文件不存在'</span>)
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">let</span> data = <span class="hljs-built_in">require</span>(filePath)
  res.send(data)
&#125;)

<span class="hljs-keyword">var</span> server = app.listen(<span class="hljs-number">9001</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> host = server.address().address
  <span class="hljs-keyword">var</span> port = server.address().port

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'应用实例，访问地址为 http://%s:%s'</span>, host, port)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动开发环境后，express 会监听在 9001 端口。业务代码中的接口请求的 baseURL 需要使用 <a href="http://127.0.0.1:9001/" target="_blank" rel="nofollow noopener noreferrer">http://127.0.0.1:9001</a> 。express 本身是不支持热更新的，这里使用了 node-dev 提供了热更新功能。</p>
<h1 data-id="heading-3">4. 总结</h1>
<p>接口的mock对前端在开发过程中功能的实现，和后续与中后台的开发连调提供很好的帮助。<a href="https://github.com/shjyy1983/juejin_article_samples/tree/master/webpack%E5%AE%9E%E7%8E%B0mock%E6%8E%A5%E5%8F%A3%E6%9C%8D%E5%8A%A1" target="_blank" rel="nofollow noopener noreferrer">Example Here</a>。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            