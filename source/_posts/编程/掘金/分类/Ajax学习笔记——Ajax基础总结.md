
---
title: 'Ajax学习笔记——Ajax基础总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d69905d255c43f09b671b0f46309a58~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 01:48:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d69905d255c43f09b671b0f46309a58~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. AJAX 简介</h3>
<p>AJAX 全称为 Asynchronous JavaScript And XML，就是异步的 JS 和 XML。通过 AJAX 可以在浏览器中向服务器发送异步请求，最大的优势：==无刷新获取数据==。AJAX 不是新的编程语言，而是一种将现有的标准组合在一起使用的新方式。</p>
<h3 data-id="heading-1">2. AJAX特点</h3>
<h5 data-id="heading-2">2.1AJAX 的优点</h5>
<ol>
<li>可以无需刷新页面而与服务器端进行通信。</li>
<li>允许你根据用户事件来更新部分页面内容。</li>
</ol>
<h5 data-id="heading-3">2.2 AJAX 的缺点</h5>
<ol>
<li>没有浏览历史，不能回退</li>
<li>存在跨域问题(同源)</li>
<li>SEO 不友</li>
</ol>
<h3 data-id="heading-4">3.使用</h3>
<h5 data-id="heading-5">3.1 XMLHttpRequest</h5>
<p>有关Ajax的所有操作都是通过<code>XMLHttpRequest</code>来操作的。</p>
<h5 data-id="heading-6">3.2 服务端的准备</h5>
<p>在使用Ajax之前，因为需要对服务端发送请求，因此这里使用<code>express</code>框架，创建<code>server.js</code>文件搭建一个服务器。由于Ajax默认是服从同源策略，因此在服务器中设置<code>Access-Control-Allow-Origin</code>响应头在解决跨域问题（CORS跨域）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// server.js</span>
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-comment">// 创建应用对象</span>
<span class="hljs-keyword">const</span> app = express()
<span class="hljs-comment">// 创建路由规则</span>
app.get(<span class="hljs-string">'/index'</span>, <span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
  <span class="hljs-comment">// 设置允许跨域的响应头</span>
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>)
  <span class="hljs-comment">// 设置响应体</span>
  response.send(<span class="hljs-string">'hello ajax'</span>)
&#125;)
app.post(<span class="hljs-string">'/index'</span>, <span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>)
  response.send(<span class="hljs-string">'post ajax'</span>)
&#125;)

<span class="hljs-comment">// 监听端口，启动服务</span>
app.listen(<span class="hljs-number">8282</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'服务器启动，8000端口监听中...'</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在测试过程中，要保证服务端处于开启状态，开启命令：<code>node server.js</code></p>
<h5 data-id="heading-7">3.3 ajax发送get请求</h5>
<p>准备一个<code>html</code>文档，点击按钮向接口<code>http://127.0.0.1:8282/index</code>发送请求，请求的数据显示在<code>div</code>中</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>ajax get请求<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.result</span>&#123;
      <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid black;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">250px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span>></span>发送请求<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">br</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">br</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"result"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> button = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'button'</span>)[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> divObj = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">'result'</span>)[<span class="hljs-number">0</span>]
    button.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-comment">// 创建对象</span>
      <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
      <span class="hljs-comment">// 设置请求方法和url</span>
      xhr.open(<span class="hljs-string">'GET'</span>, <span class="hljs-string">'http://127.0.0.1:8282/index'</span>)
      <span class="hljs-comment">// 发送请求</span>
      xhr.send()
      <span class="hljs-comment">// 处理服务端返回的结果</span>
      xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">/* 
          readyState属性值：
            0 - 对象未初始化
            1 - open方法执行
            2 - send方法执行
            3 - 服务端返回部分结果
            4 - 服务端返回全部结果
        */</span>
        <span class="hljs-keyword">if</span>(xhr.readyState === <span class="hljs-number">4</span>) &#123;
          <span class="hljs-comment">// 判断响应状态码  2xx成功</span>
          <span class="hljs-keyword">if</span>(xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
            <span class="hljs-comment">// 响应行</span>
            <span class="hljs-comment">// console.log(xhr.status)</span>
            <span class="hljs-comment">// console.log(xhr.statusText) // 状态描述</span>
            <span class="hljs-comment">// // 响应头</span>
            <span class="hljs-comment">// console.log(xhr.getAllResponseHeaders())</span>
            <span class="hljs-comment">// // 响应体</span>
            <span class="hljs-comment">// console.log(xhr.response)</span>
            divObj.innerHTML = xhr.response
          &#125;
        &#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d69905d255c43f09b671b0f46309a58~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
若需要在发送get请求时携带参数，则url应写为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">xhr.open(<span class="hljs-string">'GET'</span>, <span class="hljs-string">'http://127.0.0.1:8282/index?a=100&b=200&c=300'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">3.4 发送post请求</h5>
<p>将原来代码中<code>xhr.open()</code>第一个参数右<code>GET</code>改为<code>POST</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">xhr.open(<span class="hljs-string">'POST'</span>,<span class="hljs-string">'http://127.0.0.1:8282/index'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77849963f85b4b1ba6b64a9ba3d5436d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
使用post方法发送请求体时，要将请求体内容放在<code>send</code>方法中，格式不固定，只要服务端能够处理即可：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 形式一</span>
xhr.send(<span class="hljs-string">'a=100&b=200&c=300'</span>)
<span class="hljs-comment">// 形式二</span>
xhr.send(<span class="hljs-string">'a:100&b:200&c:300'</span>)
<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">3.5 设置请求头信息</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Content-Type  请求体类型</span>
<span class="hljs-comment">// application/x-www-form-urlencoded 查询字符串类型</span>
xhr.setRequestHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'application/x-www-form-urlencoded'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自定义请求头</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">xhr.setRequestHeader(<span class="hljs-string">'Name'</span>, <span class="hljs-string">'Alice'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时服务端需要设置<code>Access-Control-Allow-Headers</code>字段，表示可以接收处理的请求头，否则会报错：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">app.post(<span class="hljs-string">'/index'</span>, <span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>)
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Headers'</span>, <span class="hljs-string">'*'</span>)
  response.send(<span class="hljs-string">'post ajax'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般可以在请求头中存放服务端要校验的信息。</p>
<h5 data-id="heading-10">3.6 服务端响应 json数据时</h5>
<p>服务端若需要将json对象的数据返回给客户端，需要将其转为JSON字符串再发送，<code>server.js</code>添加代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// all()表示可以匹配所有请求的方法</span>
app.all(<span class="hljs-string">'/json-data'</span>, <span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>)
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Headers'</span>, <span class="hljs-string">'*'</span>)
  <span class="hljs-comment">// 响应json数据，需要将json对象转为字符串格式</span>
  <span class="hljs-keyword">const</span> data = &#123;
    <span class="hljs-string">'name'</span>: <span class="hljs-string">'Alice'</span>,
    <span class="hljs-string">'age'</span>: <span class="hljs-number">34</span>
  &#125;
  response.send(<span class="hljs-built_in">JSON</span>.stringify(data))
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>客户端处理结果时，需要将json字符串转为json对象：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">button.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
  xhr.open(<span class="hljs-string">'GET'</span>, <span class="hljs-string">'http://127.0.0.1:8282/json-data'</span>)
  xhr.send()
  xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span>(xhr.readyState === <span class="hljs-number">4</span>) &#123;
      <span class="hljs-keyword">if</span>(xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
        <span class="hljs-comment">// 将服务端返回的json数据转为json对象</span>
        <span class="hljs-keyword">let</span> data = <span class="hljs-built_in">JSON</span>.parse(xhr.response)
        <span class="hljs-built_in">console</span>.log(data)
      &#125;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9b67d2d68e341a59f2e8c3af180512b~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
或者可以直接在<code>xhr</code>对象上设置响应体类型为<code>json</code>，就不用执行转换步骤：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">button.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
  xhr.responseType = <span class="hljs-string">'json'</span>
  xhr.open(<span class="hljs-string">'GET'</span>, <span class="hljs-string">'http://127.0.0.1:8282/json-data'</span>)
  xhr.send()
  xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span>(xhr.readyState === <span class="hljs-number">4</span>) &#123;
      <span class="hljs-keyword">if</span>(xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
        <span class="hljs-keyword">let</span> data = xhr.response
        <span class="hljs-built_in">console</span>.log(data)
      &#125;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b14bef4bd7407b9277ad95e7b838ab~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-11">3.7 解决IE缓存问题</h5>
<p>在IE浏览器中，发送Ajax请求回来的数据会被缓存，导致在某些时效性比较强的场景下会得到错误的数据。因此需要在<code>url</code>中携带一个表示时间戳的参数，使得IE浏览器认为每次都在发送不同的请求：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> xhr.open(<span class="hljs-string">'get'</span>, <span class="hljs-string">'http://127.0.0.1:8282/json-data?t='</span>+<span class="hljs-built_in">Date</span>.now())
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">3.8 请求超时和网络异常处理</h5>
<p>可以在<code>xhr</code>对象上设置超时时间，若在这个时间之内没有获取到响应结果，则会自动取消。例如，在服务端设置3秒后返回结果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 延迟响应</span>
app.get(<span class="hljs-string">'/delay'</span>, <span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
  response.setHeader(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>)
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    response.send(<span class="hljs-string">'延迟响应'</span>)
  &#125;, <span class="hljs-number">3000</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>客户端设置超时时间为2s</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> button = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'button'</span>)[<span class="hljs-number">0</span>]
  <span class="hljs-keyword">let</span> divObj = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'div'</span>)[<span class="hljs-number">0</span>]
  button.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
    <span class="hljs-comment">// 设置超时2s取消请求</span>
    xhr.timeout = <span class="hljs-number">2000</span>
    <span class="hljs-comment">// 超时回调</span>
    xhr.ontimeout = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      alert(<span class="hljs-string">'网络较慢，请稍后重试！'</span>)
    &#125;
    xhr.open(<span class="hljs-string">'GET'</span>, <span class="hljs-string">'http://127.0.0.1:8282/delay'</span>)
    xhr.send()
    xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span>(xhr.readyState === <span class="hljs-number">4</span>) &#123;
        <span class="hljs-keyword">if</span>(xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
          divObj.innerHTML = xhr.response
        &#125;
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a35ff54e5ba4f4fa5b33e3932fd746f~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
也可以设置网络异常时的回调：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">xhr.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  alert(<span class="hljs-string">'网络异常！'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器中，将网络状态设为<code>offline</code>，模拟没有网络的情况
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76231e27930e4f0da757931c8368f21d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-13">3.9 取消请求</h6>
<p><code>xhr</code>对象上的<code>abort()</code>可以用于取消请求：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">xhr.abort()
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">3.10 重复发送请求问题</h5>
<p>当我们多次点击按钮发送请求时，会对服务器造成一定压力，且多次请求的操作并不是必要的，解决这个重复请求问题，需要当再次发送请求时，把上一次没完成的请求取消掉。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span>></span>发送请求<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> button = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'button'</span>)[<span class="hljs-number">0</span>]
    <span class="hljs-comment">// 是否正在处理ajax请求的标识</span>
    <span class="hljs-keyword">let</span> isSending = <span class="hljs-literal">false</span>  
    <span class="hljs-keyword">let</span> xhr
    button.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 如果上一次请求还在，取消，重新发起请求</span>
      <span class="hljs-keyword">if</span>(isSending) &#123;
        xhr.abort()
      &#125;
      xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
      isSending = <span class="hljs-literal">true</span>
      xhr.open(<span class="hljs-string">'GET'</span>, <span class="hljs-string">'http://127.0.0.1:8282/delay'</span>)
      xhr.send()
      xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span>(xhr.readyState === <span class="hljs-number">4</span>) &#123;
          <span class="hljs-comment">// 请求处理完，无论状态码是什么，都是为false</span>
          isSending = <span class="hljs-literal">false</span>
        &#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            