
---
title: 'Koa源码剖析笔记 - 主体流程、koa-compose洋葱模型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536a177099804422b6a889fba351e97c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 16:42:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536a177099804422b6a889fba351e97c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>笔者在工作中经常使用EggJS和Midway进行业务开发，而EggJS又是基于Koa封装的上层框架，对于Koa的底层细节实现知其然不知其所以然，带着这个疑问，开始学习/复习Koa的源码。</p>
<p>首先讲讲为什么要学习源码？</p>
<ul>
<li>解决问题：当遇到业务上的问题，清楚底层运作，可快速定位和解决</li>
<li>个人成长：设计思路可复用于未来的架构。</li>
</ul>
<p>开源且活跃的项目，往往更新频繁。当你阅读到本文时，源码可能已经不一致了，为了保证阅读体验和严谨，本文采用当前最新版。如遇到过程中跟源码不一致，请对比下版本。</p>
<ul>
<li>Node.js v14.17.5</li>
<li>Koa v2.13.1</li>
</ul>
<h2 data-id="heading-1">前置准备</h2>
<h3 data-id="heading-2"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fdist%2Flatest-v14.x%2Fdocs%2Fapi%2Fhttp.html" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/dist/latest-v14.x/docs/api/http.html" ref="nofollow noopener noreferrer">http模块</a></h3>
<p>http是Node.js的内置模块，由它为Koa提供Http Server请求响应的能力。Node.js创建一个Server非常简单。只需要</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);

<span class="hljs-comment">// 创建Http服务</span>
<span class="hljs-keyword">const</span> server = http.createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.end(<span class="hljs-string">'hello world'</span>);
&#125;);

<span class="hljs-comment">// 监听端口</span>
server.listen(<span class="hljs-number">8000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行</p>
<pre><code class="hljs language-shell copyable" lang="shell">node app.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开浏览器 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8000%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8000/" ref="nofollow noopener noreferrer">http://localhost:8000/</a>，即可看到</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536a177099804422b6a889fba351e97c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>http.createServer的回调函数中，有2个参数</p>
<ul>
<li>req 请求</li>
<li>res 响应</li>
</ul>
<p>通过res的end方法，可以向客户端输出hello world的纯文本。
一个简单的Server就创建完成了。</p>
<h3 data-id="heading-3">路由</h3>
<h4 data-id="heading-4">1、URL请求响应</h4>
<p>一个完整的Web服务，一般可接受多个请求。当浏览器请求不同路径时候，进行对应的业务处理。上面代码显然没有实现，于是对以上代码进行改造。</p>
<ul>
<li>当请求 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8000%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8000/" ref="nofollow noopener noreferrer">http://localhost:8000/</a> 时，响应 home page。</li>
<li>当请求其他任何路径，继续响应 hello world。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);

<span class="hljs-comment">// 创建Http服务</span>
<span class="hljs-keyword">const</span> server = http.createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  <span class="hljs-comment">// req.url上可以获取当前请求的URL</span>
  <span class="hljs-comment">// 根据url将处理映射到不同的处理代码上</span>
  <span class="hljs-keyword">if</span> (req.url === <span class="hljs-string">'/'</span>) &#123;
    res.end(<span class="hljs-string">'home page'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    res.end(<span class="hljs-string">'hello world'</span>);
  &#125;
&#125;);

<span class="hljs-comment">// 监听端口</span>
server.listen(<span class="hljs-number">8000</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2、代码拆分</h4>
<p>当我们的业务逐渐增多，这个文件就会越来越复杂，不能将代码无脑的堆在回调中，我们可以简单封装一下将模块解耦出去。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
<span class="hljs-keyword">const</span> router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./router.js'</span>);

<span class="hljs-comment">// 创建Http服务</span>
<span class="hljs-keyword">const</span> server = http.createServer(router);

<span class="hljs-comment">// 监听端口</span>
server.listen(<span class="hljs-number">8000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建新文件 router.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// router.js</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  <span class="hljs-comment">// 根据url将处理映射到不同到处理代码上</span>
  <span class="hljs-keyword">if</span> (req.url === <span class="hljs-string">'/'</span>) &#123;
    res.end(<span class="hljs-string">'home page'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    res.end(<span class="hljs-string">'hello world'</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">3、路由匹配</h4>
<p>使用过koa开发项目的同学，应该比较清楚，我们是不需要如上这么麻烦来自己进行路径的判断和执行函数的绑定的。</p>
<p>这得益于koa-router使用一个第三方模块<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpillarjs%2Fpath-to-regexp" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pillarjs/path-to-regexp" ref="nofollow noopener noreferrer">path-to-regexp</a></p>
<p>该模块实现了将路径转换为正则表达式，再基于正则对Url进行匹配，找到处理函数。</p>
<p>以下我们基于path-to-regexp将router.js进行简单改造。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// router.js</span>
<span class="hljs-keyword">const</span> &#123; pathToRegexp &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path-to-regexp'</span>);

<span class="hljs-comment">// 定义路径和回调函数</span>
<span class="hljs-keyword">const</span> routes = &#123;
  <span class="hljs-string">'/'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
    res.end(<span class="hljs-string">'home page'</span>);
  &#125;,
  <span class="hljs-string">'(.*)'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
    res.end(<span class="hljs-string">'hello world'</span>);
  &#125;,
&#125;;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  <span class="hljs-comment">// 逐一匹配路由</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> path <span class="hljs-keyword">in</span> routes) &#123;
    <span class="hljs-keyword">if</span> (req.url.match(pathToRegexp(path))) &#123;
      routes[path](req, res);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">4、最终</h4>
<p>处理函数部分基本是固定的，业务只需要定义路由即可。
于是我们再做了以下封装。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
<span class="hljs-keyword">const</span> router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./router.js'</span>);
<span class="hljs-keyword">const</span> routes = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./routes.js'</span>);

<span class="hljs-comment">// 创建Http服务</span>
<span class="hljs-keyword">const</span> server = http.createServer(router(routes));

<span class="hljs-comment">// 监听端口</span>
server.listen(<span class="hljs-number">8000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// router.js</span>
<span class="hljs-keyword">const</span> &#123; pathToRegexp &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path-to-regexp'</span>);

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRoutes</span>(<span class="hljs-params">routes</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
    <span class="hljs-comment">// 逐一匹配路由</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> path <span class="hljs-keyword">in</span> routes) &#123;
      <span class="hljs-keyword">if</span> (req.url.match(pathToRegexp(path))) &#123;
        routes[path](req, res);
      &#125;
    &#125;
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// routes.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-string">'/'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
    res.end(<span class="hljs-string">'home page'</span>);
  &#125;,
  <span class="hljs-string">'(.*)'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
    res.end(<span class="hljs-string">'hello world'</span>);
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的封装，基本实现了一个简单通过配置，绑定路由和处理函数。</p>
<p>Koa也有这部分关于路由的处理，它将封装到了koa-router中，后续章节会继续详细讲解。</p>
<h3 data-id="heading-8"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fdist%2Flatest-v14.x%2Fdocs%2Fapi%2Fevents.html%23events_class_eventemitter" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/dist/latest-v14.x/docs/api/events.html#events_class_eventemitter" ref="nofollow noopener noreferrer">events模块</a></h3>
<p>events也是Node.js的内置模块，通常用于为Node.js类扩展发布订阅能力。</p>
<p>它提供EventEmitter类，通过继承EventEmitter，则具备了on和emit 2个函数，用于事件绑定和触发</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> EventEmitter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'events'</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyEmitter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">EventEmitter</span> </span>&#123;&#125;

<span class="hljs-keyword">const</span> myEmitter = <span class="hljs-keyword">new</span> MyEmitter();
myEmitter.on(<span class="hljs-string">'event'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'an event occurred!'</span>);
&#125;);
myEmitter.emit(<span class="hljs-string">'event'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fcreate" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/create" ref="nofollow noopener noreferrer">Object.create</a></h3>
<p>Object.create()方法创建一个新对象，使用现有的对象来提供新创建的对象的__proto__。</p>
<h3 data-id="heading-10">小结</h3>
<p>我们通过对http封装，了解了如何扩展路由的概念；并且了解了EventEmitter和Object.create的基本概念。接下来我们继续带着以上的知识，探索Koa是这么实现的。</p>
<h2 data-id="heading-11">Koa文件目录分析</h2>
<p>首先下载koa源码</p>
<pre><code class="hljs language-shell copyable" lang="shell">git clone https://github.com/koajs/koa
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开仓库时，先查看package.json，以下截取核心一段。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"koa"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"2.13.1"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Koa web app framework"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"lib/application.js"</span>,
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出仓库导出 main 中配置 lib/application.js。</p>
<p>去掉一些跟核心源码无关的文件，继续分析项目文件夹，可以看到lib就是主要源码区域。我们可以将重心聚焦在lib文件夹的4个文件。</p>
<pre><code class="copyable">- lib
  - application.js
  - context.js
  - request.js
  - response.js
- package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>application.js作为入口导出给用户使用。</p>
<h2 data-id="heading-12">Koa主体流程 - application.js</h2>
<p>以下这段是Koa官网上提供的一段最简单使用Koa的demo。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();

app.use(<span class="hljs-keyword">async</span> ctx => &#123;
  ctx.body = <span class="hljs-string">'Hello World'</span>;
&#125;);

app.listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是前面讲到的原生http的入口代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>)

<span class="hljs-comment">// 创建Http服务</span>
<span class="hljs-keyword">const</span> server = http.createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  req.end(<span class="hljs-string">'hello world'</span>)
&#125;)

<span class="hljs-comment">// 监听端口</span>
server.listen(<span class="hljs-number">8000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比下两者，可以得出</p>
<ul>
<li>koa通过导出new Koa()创建实例，而http通过createServer创建</li>
<li>koa通过use绑定监听函数(且可多次绑定)，而http直接定义在createServer回调函数中(仅一次)</li>
<li>koa回调函数只有一个ctx参数，而http有req和res两个参数</li>
<li>监听端口代码基本一致</li>
</ul>
<p>简单猜测</p>
<ul>
<li>application中导出一个类</li>
<li>Koa类中实现了对createServer调用</li>
<li>使用use中定义的函数，接受响应时，底层会在createServer中调用</li>
<li>ctx对象对req和res进行封装以实现它的功能。</li>
</ul>
<p>带着以上假设，继续研究代码。</p>
<h3 data-id="heading-13">1、new Koa()</h3>
<p>application.js <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkoajs%2Fkoa%2Fblob%2Fmaster%2Flib%2Fapplication.js%23L27" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/koajs/koa/blob/master/lib/application.js#L27" ref="nofollow noopener noreferrer">27行-214行</a>，导出Application对象，该对象继承EventEmiter。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Emitter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'events'</span>)

<span class="hljs-built_in">module</span>.exports = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Emitter</span> </span>&#123;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">2、createServer</h3>
<p>不同于http，当koa调用listen后，会在方法内createServer。然后继续listen。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkoajs%2Fkoa%2Fblob%2Fmaster%2Flib%2Fapplication.js%23L76" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/koajs/koa/blob/master/lib/application.js#L76" ref="nofollow noopener noreferrer">点击查看源码</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Emitter</span> </span>&#123;
  ...
  listen (...args) &#123;
    debug(<span class="hljs-string">'listen'</span>)
    <span class="hljs-keyword">const</span> server = http.createServer(<span class="hljs-built_in">this</span>.callback())
    <span class="hljs-keyword">return</span> server.listen(...args)
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">3、callback和handleRequest</h3>
<p>从上面代码，我可以看出Koa对象实现了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkoajs%2Fkoa%2Fblob%2Fmaster%2Flib%2Fapplication.js%23L139" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/koajs/koa/blob/master/lib/application.js#L139" ref="nofollow noopener noreferrer">this.callback()</a>，将回调放置进createServer中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Emitter</span> </span>&#123;
   ...
   <span class="hljs-function"><span class="hljs-title">callback</span>(<span class="hljs-params"></span>)</span> &#123;
    ...
    <span class="hljs-keyword">const</span> handleRequest = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> ctx = <span class="hljs-built_in">this</span>.createContext(req, res)
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.handleRequest(ctx, fn)
    &#125;

    <span class="hljs-keyword">return</span> handleRequest
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>callback函数中，实现了handleRequest方法，该方法将req和res进行封装，组装成ctx对象，交给handleRequest回调函数执行。</p>
<p>handleRequest函数，才是最终createServer回调函数的真实执行。</p>
<h3 data-id="heading-16">4、ctx封装</h3>
<p>从上面代码可以看出，每次收到新的请求都会创建新的ctx。ctx的生命周期也是伴随一次请求到响应的过程。</p>
<p>那么createContext到底做了什么？<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkoajs%2Fkoa%2Fblob%2Fmaster%2Flib%2Fapplication.js%23L168" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/koajs/koa/blob/master/lib/application.js#L168" ref="nofollow noopener noreferrer">详见源码</a></p>
<p>以下省去较多其他与此无关的代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// application.js</span>
...
<span class="hljs-keyword">const</span> response = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./response'</span>)
<span class="hljs-keyword">const</span> context = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./context'</span>)
<span class="hljs-keyword">const</span> request = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./request'</span>)

<span class="hljs-built_in">module</span>.exports = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Emitter</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">options</span>) &#123;
      ...
    <span class="hljs-built_in">this</span>.context = <span class="hljs-built_in">Object</span>.create(context)
    <span class="hljs-built_in">this</span>.request = <span class="hljs-built_in">Object</span>.create(request)
    <span class="hljs-built_in">this</span>.response = <span class="hljs-built_in">Object</span>.create(response)
    ...
  &#125;,
  createContext (req, res) &#123;
    <span class="hljs-keyword">const</span> context = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">this</span>.context)
    <span class="hljs-keyword">const</span> request = context.request = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">this</span>.request)
    <span class="hljs-keyword">const</span> response = context.response = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">this</span>.response)
    context.app = request.app = response.app = <span class="hljs-built_in">this</span>
    context.req = request.req = response.req = req
    context.res = request.res = response.res = res
    request.ctx = response.ctx = context
    request.response = response
    response.request = request
    context.originalUrl = request.originalUrl = req.url
    context.state = &#123;&#125;
    <span class="hljs-keyword">return</span> context
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>首先Application在new构造时，就创建了this.context、this.request、this.response“模板”</li>
<li>每次请求响应会重新复制以上“模板”，创建新的context、request、response实例</li>
<li>并将 koa对象, 原生req, 原生res实例挂载在context,request,reponse上（方便在后续中间件中获取和调用）</li>
<li>将请求的url也挂载在context.originUrl和request.originalUrl上</li>
<li>最后返回context</li>
</ol>
<p>而Koa的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkoajs%2Fkoa%2Fblob%2Fmaster%2Flib%2Fcontext.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/koajs/koa/blob/master/lib/context.js" ref="nofollow noopener noreferrer">context</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkoajs%2Fkoa%2Fblob%2Fmaster%2Flib%2Frequest.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/koajs/koa/blob/master/lib/request.js" ref="nofollow noopener noreferrer">request</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkoajs%2Fkoa%2Fblob%2Fmaster%2Flib%2Fresponse.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/koajs/koa/blob/master/lib/response.js" ref="nofollow noopener noreferrer">response</a> 基于原生http req/res定义了一些更方便开发者使用的setter和getter属性。</p>
<h3 data-id="heading-17">小结</h3>
<p>根据上面的源码分析，我们大体了解了</p>
<ul>
<li>Koa定义了一个Application类</li>
<li>该类定义了listen和callback方法，对handleRequest的封装，处理了请求的响应。</li>
<li>每次接受响应，会创建新的context
<ul>
<li>通过对req和res的封装定义了Koa的Request和Response对象（内置了更多方便的setter和getter）</li>
<li>将request和response挂载在context</li>
</ul>
</li>
</ul>
<h2 data-id="heading-18">中间件机制</h2>
<p>上面我们知道Koa整体工作流程，但有一点忽略了，就是我们的路由处理到底是怎么工作的？这里不得不提Koa核心的中间件机制。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();

<span class="hljs-comment">// 此处use可多次调用</span>
app.use(<span class="hljs-keyword">async</span> ctx => &#123;
  ctx.body = <span class="hljs-string">'Hello World'</span>;
&#125;);

app.listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">中间件注册</h3>
<p>Application实例中维护了一个 middleware 的数组，并提供了一个use方法，这个方法可以注册中间件函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Emitter</span> </span>&#123;
    <span class="hljs-title">constructor</span> (<span class="hljs-params">options</span>) &#123;
        ...
        <span class="hljs-built_in">this</span>.middleware = []
        ...
    &#125;
    use (fn) &#123;
      <span class="hljs-comment">// 限制传入的必须是函数，否则报错</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'middleware must be a function!'</span>)
      debug(<span class="hljs-string">'use %s'</span>, fn._name || fn.name || <span class="hljs-string">'-'</span>)

      <span class="hljs-comment">// 将函数push进middleware数组</span>
      <span class="hljs-built_in">this</span>.middleware.push(fn)

      <span class="hljs-comment">// 返回自己，方便链式调用</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每一次use都会将函数push进middleware数组中。因此中间件处理函数，都是依次的注册在middlware数组中。</p>
<h3 data-id="heading-20">洋葱模型</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99b8eaba2d0641e9b5fe66e496ec47d9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a16c60e08e4f4ad6901d43ad506d75ab~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个经典的模型，也是面试经常问到的题目。
从前面代码我们知道，通过use会注册中间件，中间件本身是有顺序的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);

<span class="hljs-comment">// 应用程序</span>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();

<span class="hljs-comment">// 中间件1</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
    <span class="hljs-keyword">await</span> next();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
&#125;);

<span class="hljs-comment">// 中间件2</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
    <span class="hljs-keyword">await</span> next();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>);
&#125;);

app.listen(<span class="hljs-number">8000</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Server is starting`</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终输出的结果是</p>
<pre><code class="hljs language-shell copyable" lang="shell">1
3
4
2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当接受到请求后，上面的执行过程，如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);

<span class="hljs-comment">// 应用程序</span>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();

<span class="hljs-comment">// 中间件1</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>); <span class="hljs-comment">// 第1步</span>
    <span class="hljs-keyword">await</span> next(); <span class="hljs-comment">// 第2步</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>); <span class="hljs-comment">// 第6步</span>
&#125;);

<span class="hljs-comment">// 中间件2</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>); <span class="hljs-comment">// 第3步</span>
    <span class="hljs-keyword">await</span> next(); <span class="hljs-comment">// 第4步</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>); <span class="hljs-comment">// 第5步</span>
&#125;);

app.listen(<span class="hljs-number">8000</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Server is starting`</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">中间件执行</h3>
<p>接下来我们根据源码理解下，为啥是如此执行的结果。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> compose = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-compose'</span>)
...

<span class="hljs-built_in">module</span>.exports = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Emitter</span> </span>&#123;
  ...
  callback () &#123;
    <span class="hljs-keyword">const</span> fn = compose(<span class="hljs-built_in">this</span>.middleware)

    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.listenerCount(<span class="hljs-string">'error'</span>)) <span class="hljs-built_in">this</span>.on(<span class="hljs-string">'error'</span>, <span class="hljs-built_in">this</span>.onerror)

    <span class="hljs-keyword">const</span> handleRequest = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> ctx = <span class="hljs-built_in">this</span>.createContext(req, res)
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.handleRequest(ctx, fn)
    &#125;

    <span class="hljs-keyword">return</span> handleRequest
  &#125;
  
  handleRequest (ctx, fnMiddleware) &#123;
    ...
    <span class="hljs-keyword">const</span> onerror = <span class="hljs-function"><span class="hljs-params">err</span> =></span> ctx.onerror(err)
    <span class="hljs-keyword">const</span> handleResponse = <span class="hljs-function">() =></span> respond(ctx)
    ...
    <span class="hljs-keyword">return</span> fnMiddleware(ctx).then(handleResponse).catch(onerror)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>callback方法中，通过koa-compose，将中间件数组转化为一个fn执行函数。</p>
<p>然后在handleRequest中通过
fnMiddleware(ctx).then(handleResponse).catch(onerror)执行。</p>
<h3 data-id="heading-22"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkoajs%2Fcompose" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/koajs/compose" ref="nofollow noopener noreferrer">koa-compose</a></h3>
<p>首先根据上面代码调用，可以看出</p>
<blockquote>
<p>const fn = compose(this.middleware)</p>
</blockquote>
<p>这部分代码也是Koa的精华和最难懂的部分</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-built_in">module</span>.exports = compose

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span> (<span class="hljs-params">middleware</span>) </span>&#123;
  <span class="hljs-comment">// 校验必须是数组</span>
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(middleware)) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Middleware stack must be an array!'</span>)
  <span class="hljs-comment">// 校验每一个元素，必须是函数</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> fn <span class="hljs-keyword">of</span> middleware) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Middleware must be composed of functions!'</span>)
  &#125;

  <span class="hljs-comment">// 返回首个函数</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context, next</span>) </span>&#123;
    <span class="hljs-keyword">let</span> index = -<span class="hljs-number">1</span>
    <span class="hljs-keyword">return</span> dispatch(<span class="hljs-number">0</span>) <span class="hljs-comment">// 执行第一个中间件，第一个执行完递归执行下一个</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span> (<span class="hljs-params">i</span>) </span>&#123;
      <span class="hljs-comment">// 防止中间件中，多次调用next()</span>
      <span class="hljs-keyword">if</span> (i <= index) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'next() called multiple times'</span>))
      index = i
      <span class="hljs-keyword">let</span> fn = middleware[i]
      <span class="hljs-keyword">if</span> (i === middleware.length) fn = next
      <span class="hljs-keyword">if</span> (!fn) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(fn(context, dispatch.bind(<span class="hljs-literal">null</span>, i + <span class="hljs-number">1</span>)));
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err)
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码有点多，我们先去掉一些异常判断类型代码，抽丝剥茧分析下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span> (<span class="hljs-params">middleware</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context, next</span>) </span>&#123;
    <span class="hljs-keyword">let</span> index = -<span class="hljs-number">1</span>
    <span class="hljs-keyword">return</span> dispatch(<span class="hljs-number">0</span>) 
  
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span> (<span class="hljs-params">i</span>) </span>&#123;
      index = i
      <span class="hljs-keyword">let</span> fn = middleware[i]
      <span class="hljs-keyword">if</span> (i === middleware.length) fn = next
      <span class="hljs-keyword">if</span> (!fn) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
      
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(fn(context, dispatch.bind(<span class="hljs-literal">null</span>, i + <span class="hljs-number">1</span>)));
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">第一次执行</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = compose

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span> (<span class="hljs-params">middleware</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context, next</span>) </span>&#123;
    <span class="hljs-keyword">let</span> index = -<span class="hljs-number">1</span>
    <span class="hljs-keyword">return</span> dispatch(<span class="hljs-number">0</span>) <span class="hljs-comment">// 执行第一个中间件，第一个执行完递归执行下一个    </span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看下第一次执行了什么</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 以下是伪码。i = 0，将以下 i 都 置为0</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span> (<span class="hljs-params"><span class="hljs-number">0</span></span>) </span>&#123;
  index = <span class="hljs-number">0</span>
  <span class="hljs-comment">// 取到当前中间件</span>
  <span class="hljs-keyword">let</span> fn = middleware[<span class="hljs-number">0</span>]
  
  <span class="hljs-comment">// 是否到最后一位</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-number">0</span> === middleware.length) fn = next
  <span class="hljs-comment">// 如果没有下一个，则Promise.resolve()</span>
  <span class="hljs-keyword">if</span> (!fn) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
  
  <span class="hljs-comment">// 如果有下一个，则执行下一个。并返回Promise对象</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(fn(context, dispatch.bind(<span class="hljs-literal">null</span>,  <span class="hljs-number">1</span>)));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">第二次执行 & 更多执行</h4>
<p>执行当前中间件，并将下一个中间件调用函数next, 作为参数传入执行。
当代码内调用了，next() 或 await next()，就会执行下一个中间件。
从而一直执行下去</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(fn(context, dispatch.bind(<span class="hljs-literal">null</span>,  i + <span class="hljs-number">1</span>)));
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">最后一次执行后</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span> (<span class="hljs-params">i</span>) </span>&#123;
  ...
  <span class="hljs-keyword">if</span> (i === middleware.length) fn = next
  <span class="hljs-keyword">if</span> (!fn) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">为什么要用Promise.resolve</h4>
<p>前面通过递归，我们理解了从 0 ->最后一条 的执行流程</p>
<p>但是有一点比较费解的是，为什么调用不能直接</p>
<blockquote>
<p>fn(context, dispatch.bind(null, i + 1))</p>
</blockquote>
<p>而需要全程包一层Promise处理</p>
<blockquote>
<p>Promise.resolve(fn(context, dispatch.bind(null, i + 1)))</p>
</blockquote>
<p>因为我们在Koa中全面支持了async/await写法，调用next时，</p>
<p>可能直接next() 也可能 await next()调用，它会等待next()执行的结果完成，通过Promise.resolve将所有中间件调用都Promise化。</p>
<h3 data-id="heading-27">小结</h3>
<p>最后我们将前面讲的总结以下，假设我们有3个中间件，通过dispatch + Promise.resolve()封装后，代码调用铺平就变成了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 中间件中有3个函数</span>
<span class="hljs-keyword">const</span> [fn1, fn2, fn3] = <span class="hljs-built_in">this</span>.middleware;
<span class="hljs-keyword">const</span> fnMiddleware = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context</span>) </span>&#123;
  <span class="hljs-comment">// 第一层Promise</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(
    fn1(context, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 第二层Promise</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(
        fn2(context, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-comment">// 第三层Promise</span>
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(
            fn3(context, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params"></span>) </span>&#123;
              <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve();
            &#125;),
          );
        &#125;),
      );
    &#125;),
  );
&#125;;

<span class="hljs-comment">// 最后调用</span>
fnMiddleware(ctx).then(handleResponse).catch(onerror);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkoajs%2Fkoa%2Fblob%2Fmaster%2Flib%2Fapplication.js%23L220" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/koajs/koa/blob/master/lib/application.js#L220" ref="nofollow noopener noreferrer">respond</a></h2>
<p>回顾最开始的响应，发现Koa通过ctx.body直接设置，而http需要通过req.end设置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();

app.use(<span class="hljs-keyword">async</span> ctx => &#123;
  ctx.body = <span class="hljs-string">'Hello World'</span>; <span class="hljs-comment">// 为什么ctx上设置body就可以生效</span>
&#125;);

app.listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原生http的写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);

<span class="hljs-comment">// 创建Http服务</span>
<span class="hljs-keyword">const</span> server = http.createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  req.end(<span class="hljs-string">'hello world'</span>); <span class="hljs-comment">// 原生通过res.end</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>中间件函数处理完成后，会再执行handleResponse，中间如果出现错误会被onerror捕获。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">fnMiddleware(ctx).then(handleResponse).catch(onerror);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>handleResponse中会根据body类型，调用不同的处理。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">respond</span> (<span class="hljs-params">ctx</span>) </span>&#123;
  <span class="hljs-keyword">let</span> body = ctx.body;
  ...
  <span class="hljs-comment">// 如果是Buffer类型</span>
  <span class="hljs-keyword">if</span> (Buffer.isBuffer(body)) <span class="hljs-keyword">return</span> res.end(body);
  <span class="hljs-comment">// 如果是字符串类型</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> body === <span class="hljs-string">'string'</span>) <span class="hljs-keyword">return</span> res.end(body);
  <span class="hljs-comment">// 如果是流类型</span>
  <span class="hljs-keyword">if</span> (body <span class="hljs-keyword">instanceof</span> Stream) <span class="hljs-keyword">return</span> body.pipe(res);
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">最后</h2>
<p>这是Koa剖析笔记的第一篇，后续会针对koa-router以及更多的中间件进行剖析，接下来还有分析EggJS乃至Midway源码，欢迎关注。</p></div>  
</div>
            