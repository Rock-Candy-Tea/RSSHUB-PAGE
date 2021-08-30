
---
title: '如何使用fetch()'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9306'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 01:13:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=9306'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<p>fetch()是 XMLHttpRequest 的升级版，用于在 JavaScript 脚本里面发出 HTTP 请求</p>
<p>本文介绍一下它的用法</p>
<p> </p>
<h3 data-id="heading-0">基础请求方式</h3>
<p><code>fetch()</code>接受一个 URL 字符串作为参数，默认向这个参数地址发出 GET 请求，返回一个 Promise 对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 从服务器获取 JSON 数据</span>
fetch(<span class="hljs-string">'https://api.xxx'</span>)
  .then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> response.json())
  .then(<span class="hljs-function"><span class="hljs-params">json</span> =></span> <span class="hljs-built_in">console</span>.log(json))
  .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Request Failed'</span>, err))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>fetch()</code>接收到的<code>response</code>是一个 Stream 对象，<code>response.json()</code>是一个异步操作，取出所有内容，并将其转为 JSON 对象</p>
<p>Promise 可以使用 await 语法改写，使得语义更清晰</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getJSON</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> url = <span class="hljs-string">'https://api.xxx'</span>;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">let</span> response = <span class="hljs-keyword">await</span> fetch(url);
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> response.json();
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Request Failed'</span>, error);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面示例中，<code>await</code>语句必须放在<code>try...catch</code>里面，这样才能捕捉异步操作中可能发生的错误</p>
<p>后面都采用<code>await</code>的写法，不使用<code>.then()</code>的写法</p>
<h3 data-id="heading-1">响应成功或失败</h3>
<p><code>Response.status</code>属性返回一个数字，表示 HTTP 回应的状态码（例如200，表示成功请求）</p>
<p><code>fetch()</code>发出请求以后，有一个很重要的注意点：只有网络错误，或者无法连接时，<code>fetch()</code>才会报错，其他情况都不会报错，而是认为请求成功</p>
<p>这就是说，即使服务器返回的状态码是 4xx 或 5xx，<code>fetch()</code>也不会报错（即 Promise 不会变为 <code>rejected</code>状态）</p>
<p>只有通过<code>Response.status</code>属性，得到 HTTP 回应的真实状态码，才能判断请求是否成功</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fetchText</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> response = <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">'https://api.xxx'</span>);
  <span class="hljs-keyword">if</span> (response.status == <span class="hljs-number">200</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> response.text();
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(response.statusText);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面示例中，<code>response.status</code>属性只有等于 2xx （200~299），才能认定请求成功。这里不用考虑网址跳转（状态码为 3xx），因为<code>fetch()</code>会将跳转的状态码自动转为 200</p>
<p>另一种方法是判断<code>response.ok</code>是否为<code>true</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (response.ok) &#123;
  <span class="hljs-comment">// 请求成功</span>
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 请求失败</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">其他请求参数</h3>
<p><code>fetch()</code>的第一个参数是 URL，还可以接受第二个参数，作为配置对象，定制发出的 HTTP 请求。</p>
<pre><code class="hljs language-js copyable" lang="js">fetch(url, optionObj)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>optionObj</code> 是一个配置项对象，包括所有对请求的设置</p>
<p>可选参数示例:</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-comment">//请求的 body 信息 //如：Blob、BufferSource、FormData、URLSearchParams 或者 USVString 对象</span>
    <span class="hljs-attr">body</span>: <span class="hljs-built_in">JSON</span>.stringify(data), <span class="hljs-comment">//这里必须匹配 'Content-Type' //注意 GET 或 HEAD 方法的请求不能包含 body 信息。 </span>
   
    <span class="hljs-comment">//请求的 cache 模式。//如：default, no-cache, reload, force-cache, only-if-cached</span>
    <span class="hljs-attr">cache</span>: <span class="hljs-string">'no-cache'</span>,  
    
    <span class="hljs-comment">//请求的 credentials。//包括：omit、same-origin，include</span>
    <span class="hljs-attr">credentials</span>: <span class="hljs-string">'same-origin'</span>,  
      
    <span class="hljs-comment">//请求的头信息</span>
    <span class="hljs-attr">headers</span>: &#123;
      <span class="hljs-string">'user-agent'</span>: <span class="hljs-string">'Mozilla/4.0 MDN Example'</span>,
      <span class="hljs-string">'content-type'</span>: <span class="hljs-string">'application/json'</span>
    &#125;,
      
    <span class="hljs-comment">//请求使用的方法  //如：GET, POST, PUT, DELETE等</span>
    <span class="hljs-attr">method</span>: <span class="hljs-string">'POST'</span>, 
    
    <span class="hljs-comment">//请求的模式 //如 cors、 no-cors 或者 same-origin。</span>
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'cors'</span>, 
      
    <span class="hljs-comment">//重定向模式 //如 follow|自动重定向, error|如果产生重定向将自动终止并且抛出一个错误, manual|手动处理重定向</span>
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'follow'</span>, 
    
    <span class="hljs-comment">//USVString  //如 no-referrer、client或一个 URL。默认是 client</span>
    <span class="hljs-attr">referrer</span>: <span class="hljs-string">'no-referrer'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的是，有些标头不能通过headers属性设置，比如Content-Length、Cookie、Host等等。它们是由浏览器自动生成，无法修改</p></div>  
</div>
            