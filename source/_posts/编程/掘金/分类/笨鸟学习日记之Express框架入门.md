
---
title: '笨鸟学习日记之Express框架入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc2843183adc4d6696bb996f9f8d6564~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 19:02:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc2843183adc4d6696bb996f9f8d6564~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0"><strong>Express框架</strong></h1>
<ul>
<li>
<h2 data-id="heading-1">目录</h2>
</li>
<li>
<p><strong>Express框架简介及初体验</strong></p>
</li>
<li>
<p><strong>Express中间件</strong></p>
</li>
<li>
<p><strong>Express框架请求处理</strong></p>
</li>
<li>
<p><strong>epress-art-template模板引擎</strong></p>
</li>
</ul>
<h2 data-id="heading-2">官方文档</h2>
<hr>
<h2 data-id="heading-3"><strong>1.Express框架简介及初体验</strong></h2>
<h4 data-id="heading-4"><strong>1.1</strong> <strong>Express框架是什么</strong></h4>
<p>Express是一个基于<strong>Node平台</strong>的<strong>web应用开发框架</strong>，它提供了一系列的强大特性，帮助你<strong>创建各种Web应用</strong>。我们可以使用 <strong>npm install express</strong> 命令进行下载。</p>
<h4 data-id="heading-5"><strong>1.2</strong> <strong>Express框架特性</strong></h4>
<ol>
<li>
<p>提供了方便简洁的路由定义方式</p>
</li>
<li>
<p>对获取HTTP请求参数进行了简化处理</p>
</li>
<li>
<p>对模板引擎支持程度高，方便渲染动态HTML页面</p>
</li>
<li>
<p>提供了中间件机制有效控制HTTP请求</p>
</li>
<li>
<p>拥有大量第三方中间件对功能进行扩展</p>
</li>
</ol>
<h4 data-id="heading-6"><strong>1.3</strong> 原生Node.js与Express框架对比之路由</h4>
<p>原生Node.js：</p>
<pre><code class="hljs language-js copyable" lang="js">app.on(<span class="hljs-string">'request'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
     <span class="hljs-comment">// 获取客户端的请求路径</span>
 <span class="hljs-keyword">const</span> pathname = <span class="hljs-keyword">new</span> URL(req.url, <span class="hljs-string">"http://localhost:3000"</span>).pathname;
     <span class="hljs-comment">// 对请求路径进行判断 不同的路径地址响应不同的内容</span>
     <span class="hljs-keyword">if</span> (pathname == <span class="hljs-string">'/'</span> || pathname == <span class="hljs-string">'index'</span>) &#123;
        res.end(<span class="hljs-string">'欢迎来到首页'</span>);
     &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (pathname == <span class="hljs-string">'/list'</span>) &#123;
        res.end(<span class="hljs-string">'欢迎来到列表页页'</span>);
     &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (pathname == <span class="hljs-string">'/about'</span>) &#123;
        res.end(<span class="hljs-string">'欢迎来到关于我们页面'</span>)
     &#125; <span class="hljs-keyword">else</span> &#123;
        res.end(<span class="hljs-string">'抱歉, 您访问的页面出游了'</span>);
     &#125;
 &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>Express框架：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 当客户端以get方式访问/时</span>
 app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
     <span class="hljs-comment">// 对客户端做出响应</span>
     res.send(<span class="hljs-string">'Hello Express'</span>);
 &#125;);

 <span class="hljs-comment">// 当客户端以post方式访问/add路由时</span>
 app.post(<span class="hljs-string">'/add'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    res.send(<span class="hljs-string">'使用post方式请求了/add路由'</span>);
 &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7"><strong>1.4</strong> 原生Node.js与Express框架对比之获取请求参数</h4>
<p>原生Node.js：</p>
<pre><code class="hljs language-js copyable" lang="js">app.on(<span class="hljs-string">'request'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-comment">// 获取GET参数</span>
  <span class="hljs-keyword">const</span> query = <span class="hljs-keyword">new</span> URL(req.url, <span class="hljs-string">"http://localhost:3000"</span>).searchParams;
    <span class="hljs-comment">// 获取POST参数</span>
    <span class="hljs-keyword">let</span> postData = <span class="hljs-string">''</span>;
    req.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">chunk</span>) =></span> &#123;
        postData += chunk;
    &#125;);
    req.on(<span class="hljs-string">'end'</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(querystring.parse(postData)
    &#125;)); 
 &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>Express框架：</p>
<pre><code class="hljs language-js copyable" lang="js"> app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-comment">// 获取GET参数</span>
    <span class="hljs-built_in">console</span>.log(req.query);
 &#125;);

 app.post(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-comment">// 获取POST参数</span>
    <span class="hljs-built_in">console</span>.log(req.body);
 &#125;) 

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8"><strong>1.5</strong> <strong>Express初体验</strong></h4>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 引入Express框架</span>
 <span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
 <span class="hljs-comment">// 使用框架创建web服务器</span>
 <span class="hljs-keyword">const</span> app = express();
 <span class="hljs-comment">// 当客户端以get方式访问/路由时</span>
 app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-comment">// 对客户端做出响应 send方法会根据内容的类型自动设置请求头</span>
    res.send(<span class="hljs-string">'Hello Express'</span>); <span class="hljs-comment">// <h2>Hello Express</h2> &#123;say: 'hello'&#125;</span>
 &#125;);
 <span class="hljs-comment">// 程序监听3000端口</span>
 app.listen(<span class="hljs-number">3000</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">2.中间件</h2>
<h4 data-id="heading-10">2.1什么是中间件</h4>
<p>中间件就是一堆方法，可以接收客户端发来的请求、可以对请求做出响应，也可以将请求继续交给下一个中间件继续处理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc2843183adc4d6696bb996f9f8d6564~tplv-k3u1fbpfcp-watermark.image" alt="image-20210330092305487.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>中间件主要由两部分构成，中间件方法以及请求处理函数。</p>
<p>中间件方法由Express提供，负责拦截请求，请求处理函数由开发人员提供，负责处理请求。</p>
<pre><code class="hljs language-js copyable" lang="js"> app.get(<span class="hljs-string">'请求路径'</span>, <span class="hljs-string">'处理函数'</span>)   <span class="hljs-comment">// 接收并处理get请求</span>
 app.post(<span class="hljs-string">'请求路径'</span>, <span class="hljs-string">'处理函数'</span>)  <span class="hljs-comment">// 接收并处理post请求</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以针对同一个请求设置多个中间件，对同一个请求进行多次处理。</p>
<p>默认情况下，请求从上到下依次匹配中间件，一旦匹配成功，终止匹配。</p>
<p>可以调用next方法将请求的控制权交给下一个中间件，直到遇到结束请求的中间件。</p>
<pre><code class="hljs language-js copyable" lang="js">app.get(<span class="hljs-string">'/request'</span>, <span class="hljs-function">(<span class="hljs-params">req, res, next</span>) =></span> &#123;
     req.name = <span class="hljs-string">"张三"</span>;
     next();
 &#125;);
 app.get(<span class="hljs-string">'/request'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
     res.send(req.name);
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11"><strong>2.2</strong> <strong>app.use</strong>中间件用法</h4>
<p>app.use 匹配所有的请求方式，可以直接传入请求处理函数，代表接收所有的请求。</p>
<pre><code class="hljs language-js copyable" lang="js"> app.use(<span class="hljs-function">(<span class="hljs-params">req, res, next</span>) =></span> &#123;
     <span class="hljs-built_in">console</span>.log(req.url);
     next();
 &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>app.use 第一个参数也可以传入请求地址，代表不论什么请求方式，只要是这个请求地址就接收这个请求。</p>
<pre><code class="hljs language-js copyable" lang="js"> app.use(<span class="hljs-string">'/admin'</span>, <span class="hljs-function">(<span class="hljs-params">req, res, next</span>) =></span> &#123;
     <span class="hljs-built_in">console</span>.log(req.url);
     next();
 &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12"><strong>2.3</strong> <strong>中间件应用</strong></h4>
<p>1.路由保护，客户端在访问需要登录的页面时，可以先使用中间件判断用户登录状态，用户如果未登录，则拦截请求，直接响应，禁止用户进入需要登录的页面。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1.路由保护</span>
app.use(<span class="hljs-function">(<span class="hljs-params">req, res, next</span>) =></span> &#123;
     <span class="hljs-keyword">let</span> isLogined = <span class="hljs-literal">true</span>;
     <span class="hljs-keyword">if</span> (isLogined) &#123;
        next();
    &#125; <span class="hljs-keyword">else</span> &#123;
         res.send(<span class="hljs-string">'用户未登录，请登录'</span>)
     &#125;
 &#125;)
 app.get(<span class="hljs-string">'/index'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
     res.send(<span class="hljs-string">'用户已登录，欢迎来到主页面'</span>);
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.网站维护公告，在所有路由的最上面定义接收所有请求的中间件，直接为客户端做出响应，网站正在维护中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 2.网站公告</span>
app.use(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    res.send(<span class="hljs-string">'网站正在维护中...'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.自定义404页面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 3.404错误页面(放在所有路由最后)</span>
app.use(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    res.status(<span class="hljs-number">404</span>).send(<span class="hljs-string">'错误，页面为找到'</span>)<span class="hljs-comment">//允许链式编程</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13"><strong>2.4</strong> <strong>错误处理中间件</strong></h4>
<p>在程序执行的过程中，不可避免的会出现一些无法预料的错误，比如文件读取失败，数据库连接失败。</p>
<p>错误处理中间件是一个集中处理错误的地方。</p>
<pre><code class="hljs language-js copyable" lang="js"> app.use(<span class="hljs-function">(<span class="hljs-params">err, req, res, next</span>) =></span> &#123;
     res.status(<span class="hljs-number">500</span>).send(<span class="hljs-string">'服务器发生未知错误'</span>);
 &#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当程序出现错误时，调用next()方法，并且将错误信息通过参数的形式传递给next()方法，即可触发错误处理中间件。</p>
<pre><code class="hljs language-js copyable" lang="js">app.get(<span class="hljs-string">"/"</span>, <span class="hljs-function">(<span class="hljs-params">req, res, next</span>) =></span> &#123;
     fs.readFile(<span class="hljs-string">"/file-does-not-exist"</span>, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
         <span class="hljs-keyword">if</span> (err) &#123;
            next(err);
         &#125;
     &#125;);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14"><strong>2.5</strong> <strong>捕获错误</strong></h4>
<p>在node.js中，异步API的错误信息都是通过回调函数获取的，支持Promise对象的异步API发生错误可以通过catch方法捕获。</p>
<p>异步函数执行如果发生错误要如何捕获错误呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> promisify = <span class="hljs-built_in">require</span>(<span class="hljs-string">'util'</span>).promisify
<span class="hljs-keyword">const</span> readFile = promisify(fs.readFile);
app.get(<span class="hljs-string">'/'</span>, <span class="hljs-keyword">async</span> (req, res, next) => &#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'01.js'</span>, <span class="hljs-string">'utf8'</span>)
        res.send(result);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        next(error);
    &#125;
&#125;)
<span class="hljs-comment">// 错误处理中间件</span>
app.use(<span class="hljs-function">(<span class="hljs-params">err, req, res, next</span>) =></span> &#123;
    res.status(<span class="hljs-number">500</span>).send(err.message);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">3.Express框架请求处理</h2>
<h4 data-id="heading-16">3.1<strong>构建模块化路由</strong></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//app.js</span>
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>) 
 <span class="hljs-comment">// 创建路由对象</span>
 <span class="hljs-keyword">const</span> home = express.Router();
 <span class="hljs-comment">// 将路由和请求路径进行匹配</span>
 app.use(<span class="hljs-string">'/home'</span>, home);
  <span class="hljs-comment">// 在home路由下继续创建路由</span>
 home.get(<span class="hljs-string">'/index'</span>, <span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">//  /home/index</span>
         res.send(<span class="hljs-string">'欢迎来到博客展示页面'</span>);
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将上述代码进行模块抽取分离</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// home.js</span>
 <span class="hljs-keyword">const</span> home = express.Router(); 
 home.get(<span class="hljs-string">'/index'</span>, <span class="hljs-function">() =></span> &#123;
     res.send(<span class="hljs-string">'欢迎来到博客展示页面'</span>);
 &#125;);
 <span class="hljs-built_in">module</span>.exports = home;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// admin.js</span>
 <span class="hljs-keyword">const</span> admin = express.Router();
 admin.get(<span class="hljs-string">'/index'</span>, <span class="hljs-function">() =></span> &#123;
     res.send(<span class="hljs-string">'欢迎来到博客管理页面'</span>);
 &#125;);
 <span class="hljs-built_in">module</span>.exports = admin;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// app.js</span>
 <span class="hljs-keyword">const</span> home = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./route/home.js'</span>);
 <span class="hljs-keyword">const</span> admin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./route/admin.js'</span>);
 app.use(<span class="hljs-string">'/home'</span>, home);
 app.use(<span class="hljs-string">'/admin'</span>, admin);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时想要访问home.js下请求处理的结果需要加上/home路径 admin.js同理</p>
<h4 data-id="heading-17">3.2GET参数的获取</h4>
<p>Express框架中使用<strong>req.query</strong>即可获取GET参数，框架内部会将GET参数转换为对象并返回。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 接收地址栏中问号后面的参数</span>
 <span class="hljs-comment">// 例如: http://localhost:3000/?name=zhangsan&age=30</span>
 app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(req.query); <span class="hljs-comment">// &#123;"name": "zhangsan", "age": "30"&#125;</span>
 &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">3.3POST参数获取</h4>
<p>Express框架中使用req.body即可获取POST参数，但是要主要的是默认为underdefine，必须进行中间件的配置 不需要导入第三方模块 现在已经内嵌在Express框架内</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用中间件 查看官方文档</span>
app.use(express.json())
<span class="hljs-comment">// extended :true 方法内部用第三方模块qs处理请求 参数的格式</span>
app.use(express.urlencoded(&#123; <span class="hljs-attr">extended</span>: <span class="hljs-literal">true</span> &#125;))
<span class="hljs-comment">// 获取post参数</span>
app.post(<span class="hljs-string">'/index'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(req.body);
    res.send(req.body);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">3.4Express路由参数</h4>
<p>Express框架中使用req.params即可获取对应路由参数的对象类型</p>
<pre><code class="hljs language-js copyable" lang="js">app.get(<span class="hljs-string">'/find/:id'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123; 
     <span class="hljs-built_in">console</span>.log(req.params); <span class="hljs-comment">// &#123;id: 123&#125; </span>
 &#125;);
localhost:<span class="hljs-number">3000</span>/find/<span class="hljs-number">123</span> <span class="hljs-comment">//地址栏中输入的值</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">3.5静态资源的处理</h4>
<p>Express框架中内置的express.static(param)方法 param参数为静态资源存放的目录 需要进行path.join拼接，可以方便地托管静态文件，例如img、CSS、JavaScript 文件等。</p>
<pre><code class="hljs language-js copyable" lang="js"> app.use(express.static(path.join(__dirname,<span class="hljs-string">'public'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，public 目录下面的文件就可以访问了。</p>
<ul>
<li><a href="http://localhost:3000/images/kitten.jpg" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/images/kitten.jpg</a></li>
<li><a href="http://localhost:3000/css/style.css" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/css/style.css</a></li>
<li><a href="http://localhost:3000/js/app.js" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/js/app.js</a></li>
<li><a href="http://localhost:3000/images/bg.png" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/images/bg.png</a></li>
<li><a href="http://localhost:3000/hello.html" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/hello.html</a></li>
</ul>
<h2 data-id="heading-21">4.express-art-template模板引擎</h2>
<h4 data-id="heading-22">4.1模板引擎配置</h4>
<ul>
<li>为了使art-template模板引擎能够更好的和Express框架配合，模板引擎官方在原art-template模板引擎的基础上封装了express-art-template。</li>
<li>使用npm install art-template express-art-template命令进行安装。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 告诉express框架 用什么模板后缀什么模板引擎</span>
app.engine(<span class="hljs-string">'art'</span>, <span class="hljs-built_in">require</span>(<span class="hljs-string">'express-art-template'</span>));
<span class="hljs-comment">// 告诉express框架 模板文件的存放位置</span>
app.set(<span class="hljs-string">'views'</span>, path.join(__dirname, <span class="hljs-string">'views'</span>));
<span class="hljs-comment">// 告诉express框架 模板文件的默认后缀</span>
app.set(<span class="hljs-string">'view engine'</span>, <span class="hljs-string">'art'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置完成后即可使用res.render()方法</p>
<pre><code class="hljs language-js copyable" lang="js">app.get(<span class="hljs-string">'/index'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    res.render(<span class="hljs-string">'list'</span>, &#123;
        <span class="hljs-attr">msg</span>: <span class="hljs-number">123</span>
    &#125;);<span class="hljs-comment">//不需要加文件后缀 </span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">4.2app.locals对象</h4>
<p>将变量设置到app.locals对象下面，这个数据在所有的模板中都可以获取到。</p>
<pre><code class="hljs language-js copyable" lang="js"> app.locals.users = [&#123;
     <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>,
     <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>
 &#125;,&#123;
     <span class="hljs-attr">name</span>: <span class="hljs-string">'李四'</span>,
     <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>
&#125;]
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            