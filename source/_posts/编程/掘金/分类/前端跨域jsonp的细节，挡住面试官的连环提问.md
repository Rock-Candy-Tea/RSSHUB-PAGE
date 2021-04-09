
---
title: '前端跨域jsonp的细节，挡住面试官的连环提问'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fb3d06c2c12425ea28364ed8a5383ea~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 01:36:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fb3d06c2c12425ea28364ed8a5383ea~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.前言</h1>
<blockquote>
<p>在前端面试中，想必每一个人都会被问到跨域相关的问题，背过八股文的小伙伴肯定对跨域的解决对答如流，常见的跨域解决方案在网上有很多整理，但是如果问到实现的细节，你是否能够手写实现或者深入解读呢？其实很多情况下，面试官不仅仅会考察第一层的概念，还会追问第二层、第三层内容，所以对于实现原理的掌握是必要的，今天笔者就整理一下跨域的基本方式，重点介绍<code>jsonp</code>的实现~</p>
</blockquote>
<h1 data-id="heading-1">2.跨域方案</h1>
<p>常见的跨域解决方案有8种左右，在面试中能答出4-5种就可以了~</p>
<h3 data-id="heading-2">2.1 如果只是想要实现主域名下的不同子域名的跨域操作，我们可以使用设置document.domain 来解决</h3>
<p>将 <code>document.domain</code> 设置为主域名，来实现相同子域名的跨域操作，这个时候主域名下的 <code>cookie</code> 就能够被子域名所访问。同时如果文档中含有主域名相同，子域名不同的 <code>iframe</code> 的话，我们也可以对这个 <code>iframe</code> 进行操作。</p>
<h3 data-id="heading-3">2.2 使用 location.hash 的方法</h3>
<p>我们可以在主页面动态的修改 <code>iframe</code> 窗口的 <code>hash</code> 值，然后在 <code>iframe</code> 窗口里实现监听函数来实现这样一个单向的通信。因为在 <code>iframe</code> 是没有办法访问到不同源的父级窗口的，所以我们不能直接修改父级窗口的 <code>hash</code> 值来实现通信，我们可以在 <code>iframe</code> 中再加入一个 <code>iframe</code> ，这个 <code>iframe</code> 的内容是和父级页面同源的，所以我们可以 <code>window.parent.parent</code> 来修改最顶级页面的 <code>src</code>，以此来实现双向通信。</p>
<h3 data-id="heading-4">2.3 使用 window.name 的方法</h3>
<p>主要是基于同一个窗口中设置了 <code>window.name</code> 后不同源的页面也可以访问，所以不同源的子页面可以首先在 <code>window.name</code> 中写入数据，然后跳转到一个和父级同源的页面。这个时候父级页面就可以访问同源的子页面中 <code>window.name</code> 中的数据了，这种方式的好处是可以传输的数据量大。</p>
<h3 data-id="heading-5">2.4 使用 postMessage 来解决的方法</h3>
<p>这是一个 <code>h5</code> 中新增的一个 <code>api</code>。通过它我们可以实现多窗口间的信息传递，通过获取到指定窗口的引用，然后调用 <code>postMessage</code> 来发送信息，在窗口中我们通过对 <code>message</code> 信息的监听来接收信息，以此来实现不同源间的信息交换。如果是像解决 <code>ajax</code> 无法提交跨域请求的问题，我们可以使用 <code>jsonp</code>、<code>cors</code>、<code>websocket</code> 协议、服务器代理来解决问题。</p>
<h3 data-id="heading-6">2.5 使用 jsonp 来实现跨域请求</h3>
<p>它的主要原理是通过动态构建 <code>script</code> 标签来实现跨域请求，因为浏览器对 <code>script</code> 标签的引入没有跨域的访问限制 。通过在请求的 <code>url</code> 后指定一个回调函数，然后服务器在返回数据的时候，构建一个 <code>json</code> 数据的包装，这个包装就是回调函数，然后返回给前端，前端接收到数据后，因为请求的是脚本文件，所以会直接执行，这样我们先前定义好的回调函数就可以被调用，从而实现了跨域请求的处理。这种方式只能用于 <code>get</code> 请求。</p>
<h3 data-id="heading-7">2.6 使用 CORS 的方式</h3>
<p><code>CORS</code> 是一个 <code>W3C</code> 标准，全称是"跨域资源共享"。<code>CORS</code> 需要浏览器和服务器同时支持。目前，所有浏览器都支持该功能，因此我们只需要在服务器端配置就行。浏览器将 <code>CORS</code> 请求分成两类：简单请求和非简单请求。对于简单请求，浏览器直接发出 <code>CORS</code> 请求。具体来说，就是会在头信息之中，增加一个 <code>Origin</code> 字段。<code>Origin</code> 字段用来说明本次请求来自哪个源。服务器根据这个值，决定是否同意这次请求。对于如果 <code>Origin</code> 指定的源，不在许可范围内，服务器会返回一个正常的 HTTP 回应。浏览器发现，这个回应的头信息没有包含 <code>Access-Control-Allow-Origin</code> 字段，就知道出错了，从而抛出一个错误，<code>ajax</code> 不会收到响应信息。如果成功的话会包含一些以 <code>Access-Control-</code> 开头的字段。非简单请求，浏览器会先发出一次预检请求，来判断该域名是否在服务器的白名单中，如果收到肯定回复后才会发起请求。</p>
<h3 data-id="heading-8">2.7 使用 websocket 协议，这个协议没有同源限制</h3>
<h3 data-id="heading-9">2.6 使用服务器来代理跨域的访问请求</h3>
<p>就是有跨域的请求操作时发送请求给后端，让后端代为请求，然后最后将获取的结果发返回。</p>
<h1 data-id="heading-10">3.jsonp详解</h1>
<h2 data-id="heading-11">3.1 基本原理</h2>
<p><code>Jsonp(JSON with Padding) </code>是 <code>json</code> 的一种"使用模式"，可以让网页从别的域名（网站）那获取资料，即跨域读取数据。在上文中已经说明，<code>jsonp</code> 的基本原理，主要就是利用了 <code>script</code> 标签的 <code>src</code> 没有跨域限制来完成的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">123</span>;
<span class="hljs-built_in">this</span>.document.getElementById(<span class="hljs-string">'123'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">3.2 执行过程</h2>
<ul>
<li>前端定义一个解析函数(如: <code>jsonpCallback = function (res) &#123;&#125;</code>)</li>
<li>通过<code>params</code>的形式包装<code>script</code>标签的请求参数，并且声明执行函数(如<code>cb=jsonpCallback</code>)</li>
<li>后端获取到前端声明的执行函数(<code>jsonpCallback</code>)，并以带上参数且调用执行函数的方式传递给前端</li>
<li>前端在script标签返回资源的时候就会去执行<code>jsonpCallback</code>并通过回调函数的方式拿到数据了。</li>
</ul>
<h2 data-id="heading-13">3.3 优缺点</h2>
<p><strong>缺点</strong>：只能进行GET请求,而且需要后端配合进行函数逻辑书写。</p>
<p><strong>优点</strong>：兼容性好，在一些古老的浏览器中都可以运行。</p>
<h2 data-id="heading-14">3.4 案例分析</h2>
<p>先来看看我们要实现一个什么效果,在一个叫<code>index.html</code>的文件中有以下代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">'text/javascript'</span>></span><span class="javascript">
    <span class="hljs-built_in">window</span>.jsonpCallback = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(res)
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">'http://localhost:8080/api/jsonp?id=1&cb=jsonpCallback'</span> <span class="hljs-attr">type</span>=<span class="hljs-string">'text/javascript'</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我本地有一个文件<code>server.js</code>它会使用<code>node</code>提供一个服务，来模拟服务器,并且定义一个接口<code>/api/jsonp</code>来查询id对应的数据。</p>
<p>当我打开<code>index.html</code>的时候就会加载<code>script</code>标签，并执行了此次跨域请求。</p>
<h3 data-id="heading-15">前期准备</h3>
<ul>
<li>我在本地新建一个文件夹<code>node-cors</code></li>
<li>并在此目录下<code>npm init</code>，初始化<code>package.json</code></li>
<li>安装<code>koa</code>(<code>node</code>的一个轻量级框架)</li>
<li>新建文件夹<code>jsonp</code>，并新建<code>index.html</code>和<code>server.js</code>，一个写前端代码，一个写后端</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">mkdir node-cors && cd node-cors
npm init
cnpm i --save-dev koa
mkdir jsonp && cd jsonp
touch index.html
touch server.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">后端代码</h3>
<p>由于JSONP的实现需要前后端配合，先来写一下后端的实现
（看不懂没关系，下面的前端简单实现会做解释）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();
<span class="hljs-keyword">const</span> items = [&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">'title1'</span> &#125;, &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">'title2'</span> &#125;]

app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
  <span class="hljs-keyword">if</span> (ctx.path === <span class="hljs-string">'/api/jsonp'</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; cb, id &#125; = ctx.query;
    <span class="hljs-keyword">const</span> title = items.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.id == id)[<span class="hljs-string">'title'</span>]
    ctx.body = <span class="hljs-string">`<span class="hljs-subst">$&#123;cb&#125;</span>(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(&#123;title&#125;)&#125;</span>)`</span>;
    <span class="hljs-keyword">return</span>;
  &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'listen 8080...'</span>)
app.listen(<span class="hljs-number">8080</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写完之后，保存。并在jsonp这个文件夹下执行：</p>
<pre><code class="hljs language-js copyable" lang="js">node server.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来启动服务，可以看到编辑器的控制台中会打印出<code>"listen 8080..."</code></p>
<p>前端简单实现OK👌，后端已经实现了，现在让我们来看看前端最简单的一种实现方式，也就是写死一个script并发送请求：</p>
<p><code>index.html</code>中：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">'text/javascript'</span>></span><span class="javascript">
    <span class="hljs-built_in">window</span>.jsonpCallback = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(res)
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">'http://localhost:8080/api/jsonp?id=1&cb=jsonpCallback'</span> <span class="hljs-attr">type</span>=<span class="hljs-string">'text/javascript'</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个<code>script</code>的意思是：</p>
<ul>
<li>第一个，创建一个<code>jsonpCallback</code>函数。但是它还没有被调用</li>
<li>第二个，加载<code>src</code>中的资源，并等待请求的内容返回</li>
</ul>
<p>整个过程就是：</p>
<ol>
<li>
<p>当执行到第二个<code>script</code>的时候，由于请求了我们的<code>8080</code>端口，并且把<code>id</code>和<code>cb</code>这两个参数放到URL里。那么后台就可以拿到<code>UR</code>L里的这两个参数。</p>
</li>
<li>
<p>也就是在后端代码中的<code>const &#123; id, cb &#125; = ctx.query</code>这里获取到了。</p>
</li>
<li>
<p>那么后端在拿到这两个参数之后，可能就会根据id来进行一些查询，当然，我这里只是模拟的查询，用了一个简单的<code>find</code>来进行一个查找。查找到<code>id</code>为<code>1</code>的那项并且取<code>title</code>。</p>
</li>
<li>
<p>第二个参数<code>cb</code>，拿到的就是<code>"jsonpCallback"</code>了，这里也就是告诉后端，前端那里是会有一个叫做<code>jsonpCallback</code>的函数来接收后端想要返回的数据，而后端你只需要在返回体中写入<code>jsonpCallback()</code>就可以了。</p>
</li>
<li>
<p>前端在得到了后端返回的内容<code>jsonpCallback(&#123;"title":"title1"&#125;)</code>，发现里面是一段执行函数的语句，因此就会去执行第一个<code>script</code>中的<code>jsonpCallback</code>方法了，并且又是带了参数的，所以此时浏览器控制台会打印出<code>&#123; title: 'title1' &#125;</code></p>
</li>
</ol>
<p>以此来达到一个简单的跨域的效果。</p>
<p>其实你想想，如果我们把第二个<code>script</code>标签换成以下代码，是不是也能达到同样的效果呢？</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- <script src='http://localhost:8080/api/jsonp?id=1&cb=jsonpCallback' type='text/javascript'></script> --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
    jsonpCallback(&#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'title1'</span> &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">jQuery中的jsonp实现</h3>
<p>上面👆我们介绍了用<code>script</code>标签来实现，在<code>jQuery</code>的<code>$.ajax()</code>方法其实也提供了<code>jsonp</code>。</p>
<p>让我们一起来看看：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcss.com/jquery/3.5.0/jquery.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    $.ajax(&#123;
        <span class="hljs-attr">url</span>: <span class="hljs-string">"http://localhost:8080/api/jsonp"</span>,
        <span class="hljs-attr">dataType</span>: <span class="hljs-string">"jsonp"</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">"get"</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>
        &#125;,
        <span class="hljs-attr">jsonp</span>: <span class="hljs-string">"cb"</span>,
        <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(data);
        &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>success</code>回调中同样可以拿到数据。</p>
<h2 data-id="heading-18">3.5 完整jsonp封装实现</h2>
<h3 data-id="heading-19">简易版</h3>
<p>先看下我们要实现的功能</p>
<p>定义一个<code>JSONP</code>方法，它接收四个参数：</p>
<ul>
<li>url</li>
<li>params</li>
<li>callbackKey：与后台约定的回调函数是用哪个字段(如<code>cb</code>)</li>
<li>callback：拿到数据之后执行的回调函数</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">JSONP</span>(<span class="hljs-params">&#123;
        url,
        params = &#123;&#125;,
        callbackKey = <span class="hljs-string">'cb'</span>,
        callback
    &#125;</span>) </span>&#123;
        <span class="hljs-comment">// 定义本地的一个callback的名称</span>
        <span class="hljs-keyword">const</span> callbackName = <span class="hljs-string">'jsonpCallback'</span>;
        <span class="hljs-comment">// 把这个名称加入到参数中: 'cb=jsonpCallback'</span>
        params[callbackKey] = callbackName;
        <span class="hljs-comment">//  把这个callback加入到window对象中，这样就能执行这个回调了</span>
        <span class="hljs-built_in">window</span>[callbackName] = callback;

        <span class="hljs-comment">// 得到'id=1&cb=jsonpCallback'</span>
        <span class="hljs-keyword">const</span> paramString = <span class="hljs-built_in">Object</span>.keys(params).map(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>=<span class="hljs-subst">$&#123;params[key]&#125;</span>`</span>
        &#125;).join(<span class="hljs-string">'&'</span>)
        <span class="hljs-comment">// 创建 script 标签</span>
        <span class="hljs-keyword">const</span> script = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
        script.setAttribute(<span class="hljs-string">'src'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;url&#125;</span>?<span class="hljs-subst">$&#123;paramString&#125;</span>`</span>);
        <span class="hljs-built_in">document</span>.body.appendChild(script);
    &#125;
    JSONP(&#123;
        <span class="hljs-attr">url</span>: <span class="hljs-string">'http://localhost:8080/api/jsonp'</span>,
        <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span> &#125;,
        <span class="hljs-attr">callbackKey</span>: <span class="hljs-string">'cb'</span>,
        callback (res) &#123;
            <span class="hljs-built_in">console</span>.log(res)
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样写打开页面也可是可以看到效果的。</p>
<h3 data-id="heading-20">同时多个请求</h3>
<p>上面我们虽然实现了<code>JSONP</code>，但有一个问题，那就是如果我同时多次调用<code>JSONP</code>：</p>
<pre><code class="hljs language-js copyable" lang="js">JSONP(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">'http://localhost:8080/api/jsonp'</span>,
    <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span> &#125;,
    <span class="hljs-attr">callbackKey</span>: <span class="hljs-string">'cb'</span>,
    callback (res) &#123;
        <span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// No.1</span>
    &#125;
&#125;)
JSONP(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">'http://localhost:8080/api/jsonp'</span>,
    <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span> &#125;,
    <span class="hljs-attr">callbackKey</span>: <span class="hljs-string">'cb'</span>,
    callback (res) &#123;
        <span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// No.2</span>
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这里我调用了两次<code>JSONP</code>，只是传递的参数不同。但是并不会按我们预期的在<code>No.1</code>和<code>No.2</code>中分别打印，而是都会在No.2中打印出结果。这是因为后面一个<code>callback</code>把<code>JSONP</code>里封装的第一个<code>callback</code>给覆盖了，它们都是共用的同一个<code>callbackName</code>，也就是<code>jsonpCallback</code>。如下所示：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fb3d06c2c12425ea28364ed8a5383ea~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>两次结果都是从76行打印出来的。</p>
<p>所以我们得改造一下上面的<code>JSONP</code>方法：</p>
<p>让<code>callbackName</code>是一个唯一的，可以使用递增
不要把回调定义在<code>window</code>中这样会污染全局变量，可以把它扔到<code>JSON.xxx</code>中
OK👌，来看看改造之后的代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">JSONP</span>(<span class="hljs-params">&#123;
        url,
        params = &#123;&#125;,
        callbackKey = <span class="hljs-string">'cb'</span>,
        callback
    &#125;</span>) </span>&#123;
        <span class="hljs-comment">// 定义本地的唯一callbackId，若是没有的话则初始化为1</span>
        JSONP.callbackId = JSONP.callbackId || <span class="hljs-number">1</span>;
        <span class="hljs-keyword">let</span> callbackId = JSONP.callbackId;
        <span class="hljs-comment">// 把要执行的回调加入到JSON对象中，避免污染window</span>
        JSONP.callbacks = JSONP.callbacks || [];
        JSONP.callbacks[callbackId] = callback;
        <span class="hljs-comment">// 把这个名称加入到参数中: 'cb=JSONP.callbacks[1]'</span>
        params[callbackKey] = <span class="hljs-string">`JSONP.callbacks[<span class="hljs-subst">$&#123;callbackId&#125;</span>]`</span>;

        <span class="hljs-comment">// 得到'id=1&cb=JSONP.callbacks[1]'</span>
        <span class="hljs-keyword">const</span> paramString = <span class="hljs-built_in">Object</span>.keys(params).map(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>=<span class="hljs-subst">$&#123;params[key]&#125;</span>`</span>
        &#125;).join(<span class="hljs-string">'&'</span>)
        <span class="hljs-comment">// 创建 script 标签</span>
        <span class="hljs-keyword">const</span> script = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
        script.setAttribute(<span class="hljs-string">'src'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;url&#125;</span>?<span class="hljs-subst">$&#123;paramString&#125;</span>`</span>);
        <span class="hljs-built_in">document</span>.body.appendChild(script);
        <span class="hljs-comment">// id自增，保证唯一</span>
        JSONP.callbackId++;
    &#125;
    JSONP(&#123;
        <span class="hljs-attr">url</span>: <span class="hljs-string">'http://localhost:8080/api/jsonp'</span>,
        <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span> &#125;,
        <span class="hljs-attr">callbackKey</span>: <span class="hljs-string">'cb'</span>,
        callback (res) &#123;
            <span class="hljs-built_in">console</span>.log(res)
        &#125;
    &#125;)
    JSONP(&#123;
        <span class="hljs-attr">url</span>: <span class="hljs-string">'http://localhost:8080/api/jsonp'</span>,
        <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span> &#125;,
        <span class="hljs-attr">callbackKey</span>: <span class="hljs-string">'cb'</span>,
        callback (res) &#123;
            <span class="hljs-built_in">console</span>.log(res)
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到现在调用了两次回调，但是会分别执行<code>JSONP.callbacks[1]</code>和<code>JSONP.callbacks[2]</code>：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05806327d64c423ea3aba6296550b0fe~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">继续改进</h3>
<p>其实上面已经算比较完美了，但是还会有一个小问题，比如下面这种情况：</p>
<p>我改一下后端的代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();
<span class="hljs-keyword">const</span> items = [&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">'title1'</span> &#125;, &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">'title2'</span> &#125;]

app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
  <span class="hljs-keyword">if</span> (ctx.path === <span class="hljs-string">'/api/jsonp'</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; cb, id &#125; = ctx.query;
    <span class="hljs-keyword">const</span> title = items.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.id == id)[<span class="hljs-string">'title'</span>]
    ctx.body = <span class="hljs-string">`<span class="hljs-subst">$&#123;cb&#125;</span>(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(&#123;title&#125;)&#125;</span>)`</span>;
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-keyword">if</span> (ctx.path === <span class="hljs-string">'/api/jsonps'</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; cb, a, b &#125; = ctx.query;
    ctx.body = <span class="hljs-string">`<span class="hljs-subst">$&#123;cb&#125;</span>(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(&#123; a, b &#125;)&#125;</span>)`</span>;
    <span class="hljs-keyword">return</span>;
  &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'listen 8080...'</span>)
app.listen(<span class="hljs-number">8080</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>增加了一个<code>/api/jsonps</code>的接口。</p>
<p>然后前端代码增加了一个这样的请求：</p>
<pre><code class="hljs language-js copyable" lang="js">JSONP(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">'http://localhost:8080/api/jsonps'</span>,
    <span class="hljs-attr">params</span>: &#123;
        <span class="hljs-attr">a</span>: <span class="hljs-string">'2&b=3'</span>,
        <span class="hljs-attr">b</span>: <span class="hljs-string">'4'</span>
    &#125;,
    <span class="hljs-attr">callbackKey</span>: <span class="hljs-string">'cb'</span>,
    callback (res) &#123;
        <span class="hljs-built_in">console</span>.log(res)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，参数的<code>a</code>中也会有<code>b</code>这个字符串，这样就导致我们获取到的数据不对了：</p>
<p>后台并不知道<code>a</code>的参数是一个字符串，它只会按照<code>&</code>来截取参数。</p>
<p>所以为了解决这个问题，可以使用<code>URI</code>编码。</p>
<p>也就是使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">encodeURIComponent</span>(<span class="hljs-string">'2&b=3'</span>)

<span class="hljs-comment">// 结果为"2%26b%3D3"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只需要改一下<code>JSONP</code>方法中参数的生成：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 得到'id=1&cb=JSONP.callbacks[1]'</span>
<span class="hljs-keyword">const</span> paramString = <span class="hljs-built_in">Object</span>.keys(params).map(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>=<span class="hljs-subst">$&#123;<span class="hljs-built_in">encodeURIComponent</span>(params[key])&#125;</span>`</span>
&#125;).join(<span class="hljs-string">'&'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">最终实现</h3>
<p>来看一下完整版的JSONP方法：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">JSONP</span>(<span class="hljs-params">&#123;
        url,
        params = &#123;&#125;,
        callbackKey = <span class="hljs-string">'cb'</span>,
        callback
    &#125;</span>) </span>&#123;
        <span class="hljs-comment">// 定义本地的唯一callbackId，若是没有的话则初始化为1</span>
        JSONP.callbackId = JSONP.callbackId || <span class="hljs-number">1</span>;
        <span class="hljs-keyword">let</span> callbackId = JSONP.callbackId;
        <span class="hljs-comment">// 把要执行的回调加入到JSON对象中，避免污染window</span>
        JSONP.callbacks = JSONP.callbacks || [];
        JSONP.callbacks[callbackId] = callback;
        <span class="hljs-comment">// 把这个名称加入到参数中: 'cb=JSONP.callbacks[1]'</span>
        params[callbackKey] = <span class="hljs-string">`JSONP.callbacks[<span class="hljs-subst">$&#123;callbackId&#125;</span>]`</span>;
        <span class="hljs-comment">// 得到'id=1&cb=JSONP.callbacks[1]'</span>
        <span class="hljs-keyword">const</span> paramString = <span class="hljs-built_in">Object</span>.keys(params).map(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>=<span class="hljs-subst">$&#123;<span class="hljs-built_in">encodeURIComponent</span>(params[key])&#125;</span>`</span>
        &#125;).join(<span class="hljs-string">'&'</span>)
        <span class="hljs-comment">// 创建 script 标签</span>
        <span class="hljs-keyword">const</span> script = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
        script.setAttribute(<span class="hljs-string">'src'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;url&#125;</span>?<span class="hljs-subst">$&#123;paramString&#125;</span>`</span>);
        <span class="hljs-built_in">document</span>.body.appendChild(script);
        <span class="hljs-comment">// id自增，保证唯一</span>
        JSONP.callbackId++;

    &#125;
    JSONP(&#123;
        <span class="hljs-attr">url</span>: <span class="hljs-string">'http://localhost:8080/api/jsonps'</span>,
        <span class="hljs-attr">params</span>: &#123;
            <span class="hljs-attr">a</span>: <span class="hljs-string">'2&b=3'</span>,
            <span class="hljs-attr">b</span>: <span class="hljs-string">'4'</span>
        &#125;,
        <span class="hljs-attr">callbackKey</span>: <span class="hljs-string">'cb'</span>,
        callback (res) &#123;
            <span class="hljs-built_in">console</span>.log(res)
        &#125;
    &#125;)
    JSONP(&#123;
        <span class="hljs-attr">url</span>: <span class="hljs-string">'http://localhost:8080/api/jsonp'</span>,
        <span class="hljs-attr">params</span>: &#123;
            <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>
        &#125;,
        <span class="hljs-attr">callbackKey</span>: <span class="hljs-string">'cb'</span>,
        callback (res) &#123;
            <span class="hljs-built_in">console</span>.log(res)
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意⚠️：</p>
<p><code>encodeURI</code>和<code>encodeURIComponent</code>的区别：</p>
<p><code>encodeURI()</code>不会对本身属于URI的特殊字符进行编码，例如冒号、正斜杠、问号和井字号；
而<code>encodeURIComponent()</code>则会对它发现的任何非标准字符进行编码
例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> url = <span class="hljs-string">'https://lindaidai.wang'</span>

<span class="hljs-built_in">encodeURI</span>(url) <span class="hljs-comment">// "https://lindaidai.wang"</span>

<span class="hljs-built_in">encodeURIComponent</span>(url) <span class="hljs-comment">// "https%3A%2F%2Flindaidai.wang"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，可以使用<code>decodeURIComponent</code>来解码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">decodeURIComponent</span>(<span class="hljs-string">"https%3A%2F%2Flindaidai.wang"</span>)
<span class="hljs-comment">// 'https://lindaidai.wang'</span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            