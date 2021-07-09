
---
title: 'HTTP之options预检请求'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bc19d234ff4429a82dbebe4d9c88bec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 02:32:05 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bc19d234ff4429a82dbebe4d9c88bec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前置知识点</h1>
<h2 data-id="heading-1">HTTP请求方法</h2>
<h2 data-id="heading-2">简单请求</h2>
<h1 data-id="heading-3">预检请求</h1>
<ul>
<li>只有跨域的情况下，才会发生预请求</li>
<li>与前述简单请求不同，“需预检的请求”要求必须首先使用OPTIONS方法发起一个预检请求到服务器，以获知服务器是否允许该实际请求。“预检请求”的使用，可以避免跨域请求对服务器的用户数据产生未预期的影响。</li>
</ul>
<h2 data-id="heading-4">withCredentials为true不会产生预请求</h2>
<h2 data-id="heading-5">哪些情况下会产生预请求？</h2>
<h3 data-id="heading-6">1.  请求头Content-Type为application/json会产生预请求</h3>
<p>前端代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
            xhr.open(<span class="hljs-string">'POST'</span>,<span class="hljs-string">'http://127.0.0.1:8080/Public//testPost'</span>)
            xhr.setRequestHeader(<span class="hljs-string">'Content-Type'</span>,<span class="hljs-string">'application/json'</span>)
            xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(res)
            &#125;
            xhr.send()
        &#125;

        run()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后端代码：</p>
<pre><code class="hljs language-js copyable" lang="js"> public <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testPost</span>(<span class="hljs-params"></span>)</span>&#123;
        header(<span class="hljs-string">"Access-Control-Allow-Headers: Content-Type"</span>);
        header(<span class="hljs-string">"Access-Control-Allow-Origin: *"</span>);
        echoJsonResult(<span class="hljs-number">1</span>,<span class="hljs-string">''</span>,$_POST);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当后端没有配置Access-Control-Allow-Headers包含Content-Type，报错如下：</p>
<pre><code class="hljs language-js copyable" lang="js">Request header field content-type is not allowed by Access-Control-Allow-Headers <span class="hljs-keyword">in</span> preflight response.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当后端没有配置Access-Control-Allow-Origin，报错如下</p>
<pre><code class="hljs language-js copyable" lang="js">Response to preflight request doesn<span class="hljs-string">'t pass access control check: No '</span>Access-Control-Allow-Origin<span class="hljs-string">' header is present on the requested resource.
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器发出的两次请求：</p>
<ul>
<li>OPTIONS请求</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bc19d234ff4429a82dbebe4d9c88bec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeed8b5a8a894974afb6d1fcd1fd99a5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043d3e0c99424f0b92eac10d9ca8ec8e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>POST请求</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a273e62045234cec9b1d440a81550d3d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54e30ec3aed54911acea8cf9eb59271f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b168156a2084efcbf0b2607aa408a61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">2. 设置了用户自定义请求头会产生预检请求</h3>
<p>前端代码：</p>
<pre><code class="hljs language-js copyable" lang="js">        <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
            xhr.open(<span class="hljs-string">'POST'</span>,<span class="hljs-string">'http://127.0.0.1:8080/Public//testPost'</span>)
            xhr.setRequestHeader(<span class="hljs-string">'abc'</span>,<span class="hljs-string">'123'</span>)
            xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(res)
        &#125;
         xhr.send()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后端代码：</p>
<pre><code class="hljs language-js copyable" lang="js">     public <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testPost</span>(<span class="hljs-params"></span>)</span>&#123;
        header(<span class="hljs-string">"Access-Control-Allow-Origin: *"</span>);
        header(<span class="hljs-string">'Access-Control-Allow-Headers: abc'</span>);
        echoJsonResult(<span class="hljs-number">1</span>,<span class="hljs-string">''</span>,$_POST);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OPTIONS请求的request请求头</p>
<pre><code class="hljs language-js copyable" lang="js">Access-Control-Request-Headers: abc
Access-Control-Request-Method: POST
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OPTIONS请求的response响应头</p>
<pre><code class="hljs language-js copyable" lang="js">Access-Control-Allow-Headers: abc
Access-Control-Allow-Origin: *
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当后端没有配置Access-Control-Allow-Headers为abc时 ，报错如下</p>
<pre><code class="hljs language-js copyable" lang="js">Request header field abc is not allowed by Access-Control-Allow-Headers <span class="hljs-keyword">in</span> preflight response.
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">CORS跨域</h1>
<h2 data-id="heading-9">当请求跨域，后端没有配置时，报错如下</h2>
<pre><code class="hljs language-js copyable" lang="js">Access to XMLHttpRequest at <span class="hljs-string">'http://127.0.0.1:8080/Public//testPost'</span> <span class="hljs-keyword">from</span> origin <span class="hljs-string">'http://10.200.137.43:8080'</span> has been blocked by CORS policy: No <span class="hljs-string">'Access-Control-Allow-Origin'</span> header is present on the requested resource.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>则后端配置代码：</p>
<pre><code class="hljs language-js copyable" lang="js">     public <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testPost</span>(<span class="hljs-params"></span>)</span>&#123;
        header(<span class="hljs-string">"Access-Control-Allow-Origin: *"</span>);
        echoJsonResult(<span class="hljs-number">1</span>,<span class="hljs-string">''</span>,$_POST);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">withCredentials为true时需要后端配置响应头Access-Control-Allow-Credentials为true （不会产生预请求）</h2>
<p>前端代码：</p>
<pre><code class="hljs language-js copyable" lang="js">         <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
            xhr.open(<span class="hljs-string">'POST'</span>,<span class="hljs-string">'http://127.0.0.1:8080/Public//testPost'</span>)
            xhr.withCredentials = <span class="hljs-literal">true</span>
            xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(res)
          &#125;
          xhr.send()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后端代码：</p>
<pre><code class="hljs language-js copyable" lang="js">    public <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testPost</span>(<span class="hljs-params"></span>)</span>&#123;
        header(<span class="hljs-string">"Access-Control-Allow-Origin: http://10.200.137.43:8080"</span>);
        header(<span class="hljs-string">"Access-Control-Allow-Credentials: true"</span>);
        echoJsonResult(<span class="hljs-number">1</span>,<span class="hljs-string">''</span>,$_POST);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器只发起一次POST请求：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/530b651ec9e04dddbb5b250901edacc2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5f9c06ea4724d5293afd698ddbb6967~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41ae6d262b7b44c297871d8336a82848~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当后端配置Access-Control-Allow-Origin为星号时，报错如下：</p>
<pre><code class="hljs language-js copyable" lang="js">The value <span class="hljs-keyword">of</span> the <span class="hljs-string">'Access-Control-Allow-Origin'</span> header <span class="hljs-keyword">in</span> the response must not be the wildcard <span class="hljs-string">'*'</span> when the request<span class="hljs-string">'s credentials mode is '</span>include<span class="hljs-string">'.
The credentials mode of requests initiated by the XMLHttpRequest is controlled by the withCredentials attribute.
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>当后端没有配置Access-Control-Allow-Credential时，报错如下</p>
<pre><code class="hljs language-js copyable" lang="js">The value <span class="hljs-keyword">of</span> the <span class="hljs-string">'Access-Control-Allow-Credentials'</span> header <span class="hljs-keyword">in</span> the response is <span class="hljs-string">''</span> which must be <span class="hljs-string">'true'</span> when the request<span class="hljs-string">'s credentials mode is '</span>include<span class="hljs-string">'. The credentials mode of requests initiated by the XMLHttpRequest is controlled by the withCredentials attribute.
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">参考链接</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTTP%2FCORS" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></li>
<li><a href="https://juejin.cn/post/6844904183905157127" target="_blank" title="https://juejin.cn/post/6844904183905157127">juejin.cn/post/684490…</a></li>
<li><a href="https://juejin.cn/post/6844904000815366157" target="_blank" title="https://juejin.cn/post/6844904000815366157">juejin.cn/post/684490…</a></li>
</ul></div>  
</div>
            