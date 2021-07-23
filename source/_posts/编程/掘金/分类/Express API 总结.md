
---
title: 'Express API 总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7701'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 01:49:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=7701'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近学习了 express，在这里小小地总结一下，分别从app 相关 API、request 相关 API、 response 相关 API、router 相关 API 进行阐述。</p>
<p>express 属于一种 node 框架，所以在使用之前就必须要下载好 node，然后还要下载 express 框架.</p>
<p>命令：
<code>npm install express --save</code></p>
<h2 data-id="heading-0">express() 创建应用</h2>
<p>express()是 express 模块导出的入口函数，用于创建一个 express 应用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);

<span class="hljs-keyword">var</span> app = express();

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">app 相关 API</h2>
<p>如上所示，app 是创建的一个 express 应用，它具有很多 api，下面分别陈述。</p>
<h4 data-id="heading-2">1. app.set(name,value)</h4>
<p>用于将设置项 name 的值设为 value。</p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.set(<span class="hljs-string">"age"</span>,<span class="hljs-number">18</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2. app.get(name)</h4>
<p>用于获取设置项 name 的值。</p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.get(<span class="hljs-string">"age"</span>)
<span class="hljs-comment">// => 18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">3. app.enable(name)</h4>
<p>用于将设置项 name 的值设为 true。</p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.enable(<span class="hljs-string">"isopen"</span>)
app.get(<span class="hljs-string">"isopen"</span>)
<span class="hljs-comment">// => true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">4. app.disable(name)</h4>
<p>用于将设置项 name 的值设为 false。</p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.disable(<span class="hljs-string">"isopen"</span>)
app.get(<span class="hljs-string">"isopen"</span>)
<span class="hljs-comment">// => false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">5. app.enabled(name)</h4>
<p>用于检查设置项 name 的值是否为 true。</p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.enabled(<span class="hljs-string">"isopen"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">6. app.disabled(name)</h4>
<p>用于检查设置项 name 的值是否为 false。</p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.disabled(<span class="hljs-string">"isopen"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">7.app.listen()</h4>
<p>在给定的主机和端口监听请求，可以同时处理 http 和 https 版本的服务。</p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.listen(<span class="hljs-number">3000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">8.app.use()</h4>
<p>用于使用 express 相关中间件，示例如下，其中挂载的路径不会在req里出现，对中间件 function 不可见，这就意味着在回调参数req里找不到path，这样设计的目的是让中间件不需要更改代码在任意前缀路径下执行。</p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.use(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res,next</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"req.method ->"</span>,req.method)
    next()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">request 相关 API</h2>
<p>下面陈列一些request常用的 API。</p>
<h4 data-id="heading-11">1.req.params</h4>
<p>这是一个数组对象，命名过的参数会以键值对的形式存放。如有一个路由 /user/:id，那么 "id" 属性会存放在 req.param.id 中，而这个对象默认为 &#123;&#125;。对应的还有一个 api 是 req.param(name)，则会返回对应 name 参数的值。</p>
<h4 data-id="heading-12">2.req.query</h4>
<p>这是一个解析过的请求参数对象，默认为&#123;&#125;，如有一个路由 /detail/id=123，那么 req.query.id 的值就为 123.</p>
<h4 data-id="heading-13">3.req.body</h4>
<p>这是解析过的请求体，该对象默认为 &#123;&#125;。</p>
<h4 data-id="heading-14">4.req.route</h4>
<p>这个对象里是当前匹配的 Route 里包含的属性，包括原始路径字符串、产生的正则、method、查询参数等。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.get(<span class="hljs-string">"/user/:id?"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res</span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(req.route)
&#125;)
<span class="hljs-comment">// 输出的结果是：</span>
&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id?'</span>,
  <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
  <span class="hljs-attr">callbacks</span>: [ [<span class="hljs-built_in">Function</span>] ],
  <span class="hljs-attr">keys</span>: [ &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'id'</span>, <span class="hljs-attr">optional</span>: <span class="hljs-literal">true</span> &#125; ],
  <span class="hljs-attr">regexp</span>: <span class="hljs-regexp">/^/u</span>ser(?:<span class="hljs-regexp">/([^/]+?))?/</span>?$/i,
  <span class="hljs-attr">params</span>: [ id: <span class="hljs-string">'12'</span> ] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">4.req.cookies</h4>
<p>使用 cookieParaser() 中间件后该对象默认为 &#123;&#125;，也包含用户代理传过来的 cookies。</p>
<h4 data-id="heading-16">5.req.get(field)</h4>
<p>获取请求头里的 field 的值，注意是大小写不敏感的，其中 referrer 和 referer 字段是可以互换的。例如 req.get("Content-Type")。</p>
<h4 data-id="heading-17">6.req.accepts(types)</h4>
<p>检查给定的 types 是不是可以接受类型，当可以接受时返回最匹配的，否则返回 undefined ，这个时候应该响应一个 406 "Not Acceptable"。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Accept:text/html</span>
req.accepts(<span class="hljs-string">"html"</span>)  <span class="hljs-comment">// "html"</span>
<span class="hljs-comment">// Accept:text/*,application/json</span>
req.accepts(<span class="hljs-string">"html"</span>)  <span class="hljs-comment">// "html"</span>
req.accepts(<span class="hljs-string">"text/html"</span>)  <span class="hljs-comment">// "text/html"</span>
req.accepts(<span class="hljs-string">"json,text"</span>)  <span class="hljs-comment">// "json"</span>
req.accepts(<span class="hljs-string">"image/png"</span>)  <span class="hljs-comment">// undefined</span>
req.accepts(<span class="hljs-string">"png"</span>)  <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">7.req.is(type)</h4>
<p>检查请求的文件头是不是包含 "Content-Type" 字段，它匹配给定的 type。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Content-Type：text/html</span>
req.is(<span class="hljs-string">"html"</span>)  <span class="hljs-comment">//true</span>
req.is(<span class="hljs-string">"text"</span>)  <span class="hljs-comment">//true</span>
req.is(<span class="hljs-string">"text/html"</span>)  <span class="hljs-comment">//true</span>
req.is(<span class="hljs-string">"json"</span>)  <span class="hljs-comment">//false</span>
req.is(<span class="hljs-string">"application/json"</span>)  <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他的api，类如 req.is 返回远程地址，req.path 返回请求的 URL 的路径名， req.host 返回从"Host"请求头里取的主机名，不包含端口号，req.protocol 返回表示请求协议的字符串，一般是 "http"，当用tls 请求的时候返回的是"https"。</p>
<h2 data-id="heading-19">response 相关 API</h2>
<p>下面陈列一些 response 相关 API。</p>
<h4 data-id="heading-20">1.res.status(code)</h4>
<p>用于设置响应的 HTTP 状态，是 node 的 response.statusCode的链式调用。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js">res.status(<span class="hljs-number">403</span>).end()
res.status(<span class="hljs-number">400</span>).send(Bad Request)
res.status(<span class="hljs-number">404</span>).sendFile(<span class="hljs-string">"/images/404.png"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">2.res.set(field,[value])</h4>
<p>设置响应头字段 field 值为 value，也可以一次传入一个对象设置多个值。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js">res.set(<span class="hljs-string">"Content-Type"</span>,<span class="hljs-string">"text/plain"</span>)
res.set(&#123;
    <span class="hljs-string">"Content-Type"</span>:<span class="hljs-string">"text/plain"</span>,
    <span class="hljs-string">"Content-Length"</span>:<span class="hljs-string">"123"</span>,
    <span class="hljs-string">"ETag"</span>:<span class="hljs-string">"12345"</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">3.res.get(field)</h4>
<p>返回一个大小写不敏感的响应头里的 field 的值。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js">res.get(<span class="hljs-string">"Content-Type"</span>)  <span class="hljs-comment">// "text/plain"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">4.res.cookie(name,value,[options])</h4>
<p>设置 cookie name 值为 value，接受字符串参数或者JSON对象。path属性默认为 "/"。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js">res.cookie(<span class="hljs-string">"name"</span>,<span class="hljs-string">"mary"</span>,&#123;<span class="hljs-attr">domain</span>:<span class="hljs-string">".baidu.com"</span>,<span class="hljs-attr">path</span>:<span class="hljs-string">"/index"</span>,<span class="hljs-attr">secure</span>:<span class="hljs-literal">true</span>&#125;)
res.cookie(<span class="hljs-string">"cart"</span>,&#123;<span class="hljs-attr">items</span>:[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">5.res.clearCookie(name,[options])</h4>
<p>把 name 的 cookie 清除，path 参数默认为"/"。如 res.clearCookie("name",&#123;path:"/index"&#125;)</p>
<h4 data-id="heading-25">6.res.redirect([status],url)</h4>
<p>使用可选的状态码跳转到 url，状态码 status 默认为 302 "Found"。express 支持几种跳转，第一种：使用一个完整的 URL 跳转到一个完全不同的网站，例 res.redirect("<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaidu.com" target="_blank" rel="nofollow noopener noreferrer" title="https://baidu.com" ref="nofollow noopener noreferrer">baidu.com</a> ")； 第二种是根据相对根域路径跳转，如当前在 "<a href="https://link.juejin.cn/?target=http%3A%2F%2Fexample.com" target="_blank" rel="nofollow noopener noreferrer" title="http://example.com" ref="nofollow noopener noreferrer">example.com</a> "， 则 res.redirect("/detail") 则是跳转到 "<a href="https://link.juejin.cn/?target=http%3A%2F%2Fexample.com%2Fdetail" target="_blank" rel="nofollow noopener noreferrer" title="http://example.com/detail" ref="nofollow noopener noreferrer">example.com/detail</a> "。第三种是路径名跳转，res.redirect("..")是跳转到上一级网页，如当前在 "<a href="https://link.juejin.cn/?target=http%3A%2F%2Fexample.com%2Fproducts%2Fdetail" target="_blank" rel="nofollow noopener noreferrer" title="http://example.com/products/detail" ref="nofollow noopener noreferrer">example.com/products/de…</a> "，那么则会跳转至 "<a href="https://link.juejin.cn/?target=http%3A%2F%2Fexample.com%2Fproducts" target="_blank" rel="nofollow noopener noreferrer" title="http://example.com/products" ref="nofollow noopener noreferrer">example.com/products</a> "，res.redirect("back") 则是跳转到 referer 的地址，当 Referer 丢失的时候默认为 /。</p>
<h4 data-id="heading-26">7.res.send([body|status],[body])</h4>
<p>发送一个响应，这个方法在输出响应的时候会自动完成大量有用的任务，比如定义前面没有定义的 Content-Length，加一些自动的 HEAD等。当参数为一个 Buffer 时 Content-Type 会被设置为 "application/octet-stream"，当参数为 String 时 Content-Type 默认设置为 "text/html"，当参数为 Array 或 Object 时 Express 会返回一个 JSON，当参数为 Number 时，express 会自动设置一个响应体，比如 200 会返回字符"OK"，404会返回 "Not Found" 等等。</p>
<h4 data-id="heading-27">8.res.json([status|body],[body])</h4>
<p>返回一个 JSON 响应。当 res.send() 的参数是一个对象或者数组的时候会调用这个方法，它在复杂的空值(null,undefined,etc)JSON转换的时候有用。比如 res.json(null)， res.json(&#123;user:"mary"&#125;)，res.json(500,&#123;error:"message"&#125;)</p>
<h4 data-id="heading-28">9.res.format(object)</h4>
<p>设置特定请求头的响应，这个方法使用 req.accepted，执行第一个匹配的回调，当没有匹配时服务器会返回一个 406 "Not Acceptable" 或者执行 default 回调。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js">res.format(&#123;
    <span class="hljs-string">"text/plain"</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        res.send(<span class="hljs-string">"hi"</span>)
    &#125;,
    <span class="hljs-string">"text/html"</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        res.send(<span class="hljs-string">"hey"</span>)
    &#125;,
    <span class="hljs-string">"application/json"</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        res.send(&#123;<span class="hljs-attr">message</span>:<span class="hljs-string">"boy"</span>&#125;)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码在请求头为 "application/json" 或 "*/json" 的时候则会返回 "&#123;message:'boy'&#125;"</p>
<p>其他的api，类如 res.locals 指的是在某一次请求范围下的响应体的本地变量，只对此次请求期间的 views 可见，和 app.locals 是一样的。res.render(view,[locals],callback)渲染 view，同时向 callback 传入渲染后的字符串。</p>
<h2 data-id="heading-29">router 相关 API</h2>
<p>一个 router 对象是一个单独的实例，可以认为是一个 "mini-application"，具有操作中间件和路由方法的能力，每一个express 程序有一个内建的app路由，路由自身表现为一个中间件，所以可以使用它作为app.use()方法的一个参数或者作为另一个路由的use()的参数。
创建路由：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> router = express.Router([options])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以在一个特别的根URL上挂在一个路由，这样就能把各个路由放在不同的文件中。示例：</p>
<pre><code class="hljs language-js copyable" lang="js">app.use(<span class="hljs-string">"/index"</span>,router)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">1.router.all(path,[callback,...]callback)</h4>
<p>会匹配所有的HTTP动作，对想映射全局的逻辑处理到特殊的路径前缀或者任意匹配是十分有用的，例如想要对从某个点开始的所有路由进行验证操作和自动加载用户信息，示例如下：</p>
<pre><code class="hljs language-js copyable" lang="js">router.all(<span class="hljs-string">"*"</span>,requireAuthentication,loadUser)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>仅仅作用于以api开头的路径：</p>
<pre><code class="hljs language-js copyable" lang="js">router.all(<span class="hljs-string">"/api/*"</span>,requireAuthentication)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">2.router.method(path,[callback,...]callback)</h4>
<p>指的是router.get()，router.put()，router.post()等等，使用方式和router.all() 一样，若对匹配的path有特殊的限制，也可以使用正则表达式。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js">router.get(<span class="hljs-string">"/"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res</span>)</span>&#123;
    res.send(<span class="hljs-string">"hello world"</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">3.router.param(name,callback)</h4>
<p>给路由参数添加回调触发器，name 指的是参数名，function 是回调方法，回调方法的参数依次是请求对象、响应对象、下个中间件、参数值和参数名，对于param的回调定义的路由来说，他们是局部的，不会被挂载的app或者路由继承，所以定义在router上的param回调只有是在router上的路由具有这个路由参数时才起作用。在定义param的路由上，param回调都是第一个被调用的，他们在一个请求-响应循环中都会被调用一次并且只有一次，即使多个路由都匹配。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js">router.param(<span class="hljs-string">"id"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res,next,id</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"called only once"</span>)
&#125;)
router.get(<span class="hljs-string">"/user/:id"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res,next</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"although this matches"</span>)
    next()
&#125;)
router.get(<span class="hljs-string">"/user/:id"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"and this matches too"</span>)
    res.end()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 GET /user/43,得到下面的结果：</p>
<pre><code class="hljs language-js copyable" lang="js">called only once
although <span class="hljs-built_in">this</span> matches
and <span class="hljs-built_in">this</span> matches too
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">4.router.route(path)</h4>
<p>返回一个单例模式的路由的实例，之后可以在其上施加各种HTTP动作的中间件。
示例：</p>
<pre><code class="hljs language-js copyable" lang="js">router.param(<span class="hljs-string">'user_id'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res, next, id</span>) </span>&#123;
    req.user = &#123;
        <span class="hljs-attr">id</span>:id,
        <span class="hljs-attr">name</span>:<span class="hljs-string">"TJ"</span>
    &#125;;
    next();
&#125;);
router.route(<span class="hljs-string">'/users/:user_id'</span>)
    .all(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res, next</span>) </span>&#123;
        next();
    &#125;)
    .get(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res, next</span>) </span>&#123;
        res.json(req.user);
    &#125;)
    .put(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res, next</span>) </span>&#123;
        req.user.name = req.params.name;
        res.json(req.user);
    &#125;)
    .post(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res, next</span>) </span>&#123;
        next(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'not implemented'</span>));
    &#125;)
    .delete(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res, next</span>) </span>&#123;
        next(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'not implemented'</span>));
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">5.router.use([path],[function,...]function)</h4>
<p>给可选的 path 参数指定的路径挂载给定的中间件方法，未指定 path 参数时默认为 /，类似于app.use()方法。</p>
<p>本文参考：</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fexpressjs.jser.us%2F3x_zh-cn%2Fapi.html" target="_blank" rel="nofollow noopener noreferrer" title="http://expressjs.jser.us/3x_zh-cn/api.html" ref="nofollow noopener noreferrer">express中文文档</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fw3cnote%2Fexpress-4-x-api.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/w3cnote/express-4-x-api.html" ref="nofollow noopener noreferrer">菜鸟教程</a></p></div>  
</div>
            