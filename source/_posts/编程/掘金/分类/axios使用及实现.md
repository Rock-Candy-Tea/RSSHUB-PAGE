
---
title: 'axios使用及实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd5b6ec5e7ba437791ad427b21b051cf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 26 Mar 2021 19:57:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd5b6ec5e7ba437791ad427b21b051cf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>axios其实是一个对象，有主要的6部分组成，分别为：config,data,headers,request,status,statusText</p>
</blockquote>
<p><img alt="截屏2021-03-26 06.57.08.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd5b6ec5e7ba437791ad427b21b051cf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">1.get</h3>
<h4 data-id="heading-1">1.1.使用</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
<span class="hljs-keyword">const</span> baseUrl = <span class="hljs-string">'http://localhost:8080'</span>;
<span class="hljs-keyword">const</span> user = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'zhangsan'</span>,
    <span class="hljs-attr">password</span>: <span class="hljs-string">'123456'</span>
&#125;
axios(&#123;
    <span class="hljs-attr">url</span>:baseUrl+ <span class="hljs-string">'/get'</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
    <span class="hljs-attr">params</span>: user
&#125;).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(response);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(error);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">1.2.支持get的实现</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios
├── Axios.js
└── index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">1.2.1.<code>axios/index.js</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Axios <span class="hljs-keyword">from</span> <span class="hljs-string">'./Axios'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createInstance</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> context=<span class="hljs-keyword">new</span> Axios();
    <span class="hljs-comment">//让request方法里的this永远指向context也就是new Axios</span>
    <span class="hljs-keyword">let</span> instance=Axios.prototype.request.bind(context);
    <span class="hljs-comment">//把Axios的类的实例和类的原型上的方法都拷贝到了instance上，也就是request方法上</span>
    instance=<span class="hljs-built_in">Object</span>.assign(instance,Axios.prototype,context);
    <span class="hljs-keyword">return</span> instance;
&#125;
<span class="hljs-keyword">const</span> axios=createInstance();
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">1.2.2.<code>axios/Axios.js</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;
<span class="hljs-keyword">import</span> parseHeaders <span class="hljs-keyword">from</span> <span class="hljs-string">'parse-headers'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Axios</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">request</span>(<span class="hljs-params">config = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.dispatchRequest(config);
    &#125;

    <span class="hljs-function"><span class="hljs-title">dispatchRequest</span>(<span class="hljs-params">config</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> &#123; url, method, params &#125; = config;
            <span class="hljs-keyword">if</span> (params) &#123;<span class="hljs-comment">//&#123;name:'zhangsan',password:'123456'&#125;=>name='zhangsan'&password='123456'</span>
                params = qs.stringify(params);
                url = url + (url.indexOf(<span class="hljs-string">'?'</span>) > -<span class="hljs-number">1</span> ? <span class="hljs-string">'&'</span> : <span class="hljs-string">'?'</span>) + params;
            &#125;
            <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
            <span class="hljs-comment">//第三个参数异步</span>
            xhr.open(method, url, <span class="hljs-literal">true</span>);
            <span class="hljs-comment">//设置返回值为json</span>
            xhr.responseType = <span class="hljs-string">'json'</span>;
            xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">if</span> (xhr.readyState === <span class="hljs-number">4</span>) &#123;
                    <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
                        <span class="hljs-keyword">const</span> response = &#123;
                            <span class="hljs-attr">data</span>: xhr.response,
                            <span class="hljs-attr">headers</span>: parseHeaders(xhr.getAllResponseHeaders()),
                            <span class="hljs-attr">status</span>: xhr.status,
                            <span class="hljs-attr">statusText</span>: xhr.statusText,
                            config,
                            <span class="hljs-attr">request</span>: xhr
                        &#125;
                        resolve(response);
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        reject(<span class="hljs-string">'请求失败'</span>);
                    &#125;
                &#125;
            &#125;
            xhr.send();
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.post</h3>
<h4 data-id="heading-6">2.1.使用</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
<span class="hljs-keyword">const</span> baseUrl = <span class="hljs-string">'http://localhost:8080'</span>;
<span class="hljs-keyword">const</span> user = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'zhangsan'</span>,
    <span class="hljs-attr">password</span>: <span class="hljs-string">'123456'</span>
&#125;
axios(&#123;
    <span class="hljs-attr">url</span>:baseUrl+ <span class="hljs-string">'/post'</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">headers</span>:&#123;<span class="hljs-comment">//请求头</span>
        <span class="hljs-string">'Content-Type'</span>:<span class="hljs-string">'application/json'</span>
    &#125;,
    <span class="hljs-attr">data</span>:user,<span class="hljs-comment">//请求体</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(response);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(error);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2.2.实现</h4>
<h5 data-id="heading-8">2.2.1.修改<code>Axios.js</code></h5>
<blockquote>
<p>主要是对请求头和请求体做处理</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;
<span class="hljs-keyword">import</span> parseHeaders <span class="hljs-keyword">from</span> <span class="hljs-string">'parse-headers'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Axios</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">request</span>(<span class="hljs-params">config = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.dispatchRequest(config);
    &#125;

    <span class="hljs-function"><span class="hljs-title">dispatchRequest</span>(<span class="hljs-params">config</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
+           <span class="hljs-keyword">let</span> &#123; url, method = <span class="hljs-string">'get'</span>, params, data, headers &#125; = config;
            <span class="hljs-keyword">if</span> (params) &#123;<span class="hljs-comment">//&#123;name:'zhangsan',password:'123456'&#125;=>name='zhangsan'&password='123456'</span>
                params = qs.stringify(params);
                url = url + (url.indexOf(<span class="hljs-string">'?'</span>) > -<span class="hljs-number">1</span> ? <span class="hljs-string">'&'</span> : <span class="hljs-string">'?'</span>) + params;
            &#125;
            <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
            <span class="hljs-comment">//第三个参数异步</span>
            xhr.open(method, url, <span class="hljs-literal">true</span>);
            <span class="hljs-comment">//设置返回值为json</span>
            xhr.responseType = <span class="hljs-string">'json'</span>;
            xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">if</span> (xhr.readyState === <span class="hljs-number">4</span>) &#123;
                    <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
                        <span class="hljs-keyword">const</span> response = &#123;
                            <span class="hljs-attr">data</span>: xhr.response,
                            <span class="hljs-attr">headers</span>: parseHeaders(xhr.getAllResponseHeaders()),
                            <span class="hljs-attr">status</span>: xhr.status,
                            <span class="hljs-attr">statusText</span>: xhr.statusText,
                            config,
                            <span class="hljs-attr">request</span>: xhr
                        &#125;
                        resolve(response);
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        reject(<span class="hljs-string">'请求失败'</span>);
                    &#125;
                &#125;
            &#125;

            <span class="hljs-comment">//请求头的处理</span>
+           <span class="hljs-keyword">if</span> (headers) &#123;
+               <span class="hljs-built_in">Object</span>.keys(headers).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
+                   xhr.setRequestHeader(key, headers[key]);
+               &#125;)
+           &#125;

            <span class="hljs-comment">//请求体的处理</span>
+           <span class="hljs-keyword">let</span> body = <span class="hljs-literal">null</span>;
+           <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'object'</span> && data !== <span class="hljs-literal">null</span>) &#123;
+               body = <span class="hljs-built_in">JSON</span>.stringify(data);<span class="hljs-comment">//转化为字符串</span>
+           &#125;
+           xhr.send(body);
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.错误处理</h3>
<ul>
<li>请求超时</li>
<li>网络异常</li>
<li>状态码错误</li>
</ul>
<h4 data-id="heading-10">3.1.实例</h4>
<h5 data-id="heading-11">3.1.1.请求超时</h5>
<blockquote>
<p>这个的这个<code>/post_timeout?timeout=3000</code>接口会在<code>3s</code>后返回结果,接口调用设置的请求时间为<code>1s</code>，因此会报:<code>Error: timeout of 1000ms exceeded</code>异常</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios(&#123;
    <span class="hljs-attr">url</span>: baseUrl + <span class="hljs-string">'/post_timeout?timeout=3000'</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json'</span>
    &#125;,
    <span class="hljs-attr">data</span>: user,
+   timeout: <span class="hljs-number">1000</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(response);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(error);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">3.1.2.网络异常</h5>
<blockquote>
<p>设置<code>3s</code>后发请求，但是在这个期间断网了，报：<code>net::ERR_INTERNET_DISCONNECTED</code></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">+ <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    axios(&#123;
        <span class="hljs-attr">url</span>: baseUrl + <span class="hljs-string">'/post'</span>,
        <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
        <span class="hljs-attr">headers</span>: &#123;
            <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json'</span>
        &#125;,
        <span class="hljs-attr">data</span>: user
    &#125;).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(response);
    &#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(error);
    &#125;)
+ &#125;, <span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">3.1.3.状态码错误</h5>
<blockquote>
<p>这个的这个接口<code>/post_status?code=300</code>,返回的状态码是<code>300</code>,报：<code>Error: Request failed with status code 300</code></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios(&#123;
    <span class="hljs-attr">url</span>: baseUrl + <span class="hljs-string">'/post_status?code=300'</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json'</span>
    &#125;,
    <span class="hljs-attr">data</span>: user,
    <span class="hljs-attr">timeout</span>:<span class="hljs-number">1000</span>,
&#125;).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(response);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(error);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">3.2.实现</h4>
<h5 data-id="heading-15">3.2.1.<code>Axios.js修改</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;
<span class="hljs-keyword">import</span> parseHeaders <span class="hljs-keyword">from</span> <span class="hljs-string">'parse-headers'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Axios</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">request</span>(<span class="hljs-params">config = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.dispatchRequest(config);
    &#125;

    <span class="hljs-function"><span class="hljs-title">dispatchRequest</span>(<span class="hljs-params">config</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
+       <span class="hljs-keyword">let</span> &#123; url, method = <span class="hljs-string">'get'</span>, params, data, headers,timeout &#125; = config;
            <span class="hljs-keyword">if</span> (params) &#123;<span class="hljs-comment">//&#123;name:'zhangsan',password:'123456'&#125;=>name='zhangsan'&password='123456'</span>
                params = qs.stringify(params);
                url = url + (url.indexOf(<span class="hljs-string">'?'</span>) > -<span class="hljs-number">1</span> ? <span class="hljs-string">'&'</span> : <span class="hljs-string">'?'</span>) + params;
            &#125;
            <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
            <span class="hljs-comment">//第三个参数异步</span>
            xhr.open(method, url, <span class="hljs-literal">true</span>);
            <span class="hljs-comment">//设置返回值为json</span>
            xhr.responseType = <span class="hljs-string">'json'</span>;
            xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
+                <span class="hljs-keyword">if</span> (xhr.readyState === <span class="hljs-number">4</span> && xhr.status !==<span class="hljs-number">0</span>) &#123;
                   <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status <<span class="hljs-number">300</span>) &#123;
                        <span class="hljs-keyword">const</span> response = &#123;
                            <span class="hljs-attr">data</span>: xhr.response,
                            <span class="hljs-attr">headers</span>: parseHeaders(xhr.getAllResponseHeaders()),
                            <span class="hljs-attr">status</span>: xhr.status,
                            <span class="hljs-attr">statusText</span>: xhr.statusText,
                            config,
                            <span class="hljs-attr">request</span>: xhr
                        &#125;
                        resolve(response);
                    &#125; <span class="hljs-keyword">else</span> &#123;
 +                      reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: Request failed with status code <span class="hljs-subst">$&#123;xhr.status&#125;</span>`</span>))
                    &#125;
                &#125;
            &#125;

            <span class="hljs-comment">//请求头的处理</span>
            <span class="hljs-keyword">if</span> (headers) &#123;
                <span class="hljs-built_in">Object</span>.keys(headers).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
                    xhr.setRequestHeader(key, headers[key]);
                &#125;)
            &#125;

            <span class="hljs-comment">//请求体的处理</span>
            <span class="hljs-keyword">let</span> body = <span class="hljs-literal">null</span>;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'object'</span> && data !== <span class="hljs-literal">null</span>) &#123;
                body = <span class="hljs-built_in">JSON</span>.stringify(data);<span class="hljs-comment">//转化为字符串</span>
            &#125;

            <span class="hljs-comment">//超时异常</span>
+           <span class="hljs-keyword">if</span>(timeout)&#123;
+               xhr.timeout=timeout;<span class="hljs-comment">//设置超时时间</span>
+               xhr.ontimeout=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-comment">//超时监听</span>
+                   reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: timeout of <span class="hljs-subst">$&#123;timeout&#125;</span>ms exceeded`</span>));
+               &#125;
+           &#125;

            <span class="hljs-comment">//网络异常</span>
+           xhr.onerror=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
+               reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`net::ERR_INTERNET_DISCONNECTED`</span>));
+           &#125;

            xhr.send(body);
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">4.拦截器</h3>
<ul>
<li>axios请求拦截器是插入后执行，响应拦截器是先插入先执行</li>
<li>interceptors.request.use:使用请求拦截器
<ul>
<li><code>use(onFulfilled?: (value: AxiosRequestConfig) => AxiosRequestConfig | Promise<AxiosRequestConfig>, onRejected?: (error: any) => any): number</code></li>
<li>use回调有两个可选参数：<code>onFulfilled</code>和<code>onRejected</code></li>
<li>onFulfilled执行返回值可能是<code>AxiosRequestConfig</code>|<code>Promise<AxiosRequestConfig></code>,use执行返回值是当前位置，便于eject取消</li>
</ul>
</li>
<li>interceptors.response.use:使用响应拦截器
<ul>
<li><code>use(onFulfilled?: (value: AxiosResponse<any>) => AxiosResponse<any> | Promise<AxiosResponse<any>>, onRejected?: (error: any) => any): number</code></li>
<li>use回调有两个可选参数：<code>onFulfilled</code>和<code>onRejected</code></li>
<li>onFulfilled执行返回值可能是<code>AxiosResponse<any></code>|<code>Promise<AxiosResponse<any>>,</code>,use执行返回值是当前位置，便于eject取消</li>
</ul>
</li>
<li>interceptors.request.eject:取消请求使用的某个拦截器</li>
<li>interceptors.response.eject:取消响应使用的某个拦截器</li>
</ul>
<h4 data-id="heading-17">4.1.使用</h4>
<blockquote>
<p>axios请求拦截器是插入后执行，响应拦截器是先插入先执行</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
<span class="hljs-keyword">const</span> baseUrl = <span class="hljs-string">'http://localhost:8080'</span>;
<span class="hljs-keyword">const</span> user = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'zhangsan'</span>,
    <span class="hljs-attr">password</span>: <span class="hljs-string">'123456'</span>
&#125;

<span class="hljs-comment">//请求拦截</span>
+axios.interceptors.request.use(<span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
+   config.headers.name += <span class="hljs-string">'1'</span>;
+   <span class="hljs-keyword">return</span> config;
+&#125;)
+<span class="hljs-keyword">const</span> request_interceptor = axios.interceptors.request.use(<span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
+   config.headers.name += <span class="hljs-string">'2'</span>;
+   <span class="hljs-keyword">return</span> config;
+&#125;)
+axios.interceptors.request.use(<span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
+   config.headers.name += <span class="hljs-string">'3'</span>;
+   <span class="hljs-keyword">return</span> config;
+&#125;)
+axios.interceptors.request.eject(request_interceptor);<span class="hljs-comment">//取消某个请求拦截器</span>


<span class="hljs-comment">//响应拦截</span>
+axios.interceptors.response.use(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
+   response.data.name += <span class="hljs-string">'1'</span>;
+   <span class="hljs-keyword">return</span> response;
+&#125;)
+<span class="hljs-keyword">const</span> response_intereptor = axios.interceptors.response.use(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
+   response.data.name += <span class="hljs-string">'2'</span>;
+   <span class="hljs-keyword">return</span> response;
+&#125;)
+axios.interceptors.response.use(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
+   response.data.name += <span class="hljs-string">'3'</span>;
+   <span class="hljs-keyword">return</span> response;
+&#125;)
+axios.interceptors.response.eject(response_intereptor);<span class="hljs-comment">//取消某个设置的影响拦截器</span>

axios(&#123;
    <span class="hljs-attr">url</span>: baseUrl + <span class="hljs-string">'/post'</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json'</span>,
+       <span class="hljs-string">'name'</span>:<span class="hljs-string">'lisi'</span>
    &#125;,
    <span class="hljs-attr">data</span>: user,
    <span class="hljs-attr">timeout</span>: <span class="hljs-number">1000</span>,
&#125;).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(response.data);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(error);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">4.1.1.请求分析</h5>
<blockquote>
<p>从请求头我们能观察到，name=lisi31,过程是这样的，我们设置了三次请求拦截，由于请求拦截是先插入的后执行，所以应该是<code>name321</code>,但是由于我们<code>eject(取消)</code>了第二次的请求拦截，所以最终请求发的是<code>name31</code></p>
</blockquote>
<p><img alt="9DD0F4C5803EC97E32BCC771E9A7FBAD.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3b757aa2f7d4453b07611c7d28b8d98~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-19">4.1.2.响应分析</h5>
<blockquote>
<p>从响应数据我们很容观测到，name最终返回了zhangsan13,同样我们也设置了三次响应拦截，响应拦截是先插入的先执行，本应该是<code>zhangsan123</code>的，但是因为我们同样<code>eject(取消)</code>了第二次响应拦截，所以最终结果成了<code>zhangsan13</code></p>
</blockquote>
<p><img alt="QQ20210326-082934@2x.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcac196f5a2a477e9c47f8b15fda5d8a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-20">4.2.实现</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios
├── Axios.js
├── AxiosInterceptorManager.js
└── index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">4.2.1.<code>AxiosInterceptorManager.js</code>拦截器管理者</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AxiosInterceptorManager</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.interceptors=[];
    &#125;
    <span class="hljs-comment">//注册拦截器</span>
    <span class="hljs-function"><span class="hljs-title">use</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.interceptors.push(&#123;
            onFulfilled,
            onRejected
        &#125;)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.interceptors.length-<span class="hljs-number">1</span>;<span class="hljs-comment">//返回当前注册的位置</span>
    &#125;
    <span class="hljs-comment">//取消拦截器</span>
    <span class="hljs-function"><span class="hljs-title">eject</span>(<span class="hljs-params">interceptorIndex</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.interceptors[interceptorIndex])&#123;
            <span class="hljs-built_in">this</span>.interceptors[interceptorIndex]=<span class="hljs-literal">null</span>;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> AxiosInterceptorManager;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">4.2.2.<code>Axios.js修改</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;
<span class="hljs-keyword">import</span> parseHeaders <span class="hljs-keyword">from</span> <span class="hljs-string">'parse-headers'</span>;
+ <span class="hljs-keyword">import</span> AxiosInterceptorManager <span class="hljs-keyword">from</span> <span class="hljs-string">'./AxiosInterceptorManager'</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Axios</span> </span>&#123;

+   <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
+       <span class="hljs-built_in">this</span>.interceptors = &#123;
+           request: <span class="hljs-keyword">new</span> AxiosInterceptorManager(),<span class="hljs-comment">//请求拦截器的管理者</span>
+           response: <span class="hljs-keyword">new</span> AxiosInterceptorManager()<span class="hljs-comment">//响应拦截器的管理者</span>
+       &#125;;
+   &#125;

    <span class="hljs-function"><span class="hljs-title">request</span>(<span class="hljs-params">config = &#123;&#125;</span>)</span> &#123;
 +      <span class="hljs-keyword">const</span> chain = [&#123;<span class="hljs-comment">//设置真正发请求的，然后将请求拦截出入前面，响应拦截插入后面，实现现走请求拦截，再发请求，最后响应拦截</span>
 +          onFulfilled: <span class="hljs-built_in">this</span>.dispatchRequest,
 +          onRejected: <span class="hljs-literal">undefined</span>
 +      &#125;];
        <span class="hljs-comment">//将请求拦截器一个一个插入最前面，实现先放的后执行</span>
 +      <span class="hljs-built_in">this</span>.interceptors.request.interceptors.forEach(<span class="hljs-function"><span class="hljs-params">interceptor</span> =></span> &#123;
 +          interceptor && chain.unshift(interceptor);
 +      &#125;)
        <span class="hljs-comment">//将响应拦截一个个查处末尾，实现先放先执行</span>
 +      <span class="hljs-built_in">this</span>.interceptors.response.interceptors.forEach(<span class="hljs-function"><span class="hljs-params">interceptor</span> =></span> &#123;
 +          interceptor && chain.push(interceptor);
 +      &#125;)
 +      <span class="hljs-keyword">let</span> promise = <span class="hljs-built_in">Promise</span>.resolve(config);
 +      <span class="hljs-keyword">while</span> (chain.length) &#123;
 +          <span class="hljs-keyword">const</span> &#123; onFulfilled, onRejected &#125; = chain.shift();<span class="hljs-comment">//取出每次的第一条数据</span>
            <span class="hljs-comment">//将config传入onFulfilled</span>
 +          promise = promise.then(onFulfilled, onRejected);
 +      &#125;
 +      <span class="hljs-keyword">return</span> promise;
 +  &#125;

    <span class="hljs-function"><span class="hljs-title">dispatchRequest</span>(<span class="hljs-params">config</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> &#123; url, method = <span class="hljs-string">'get'</span>, params, data, headers, timeout &#125; = config;
            <span class="hljs-keyword">if</span> (params) &#123;<span class="hljs-comment">//&#123;name:'zhangsan',password:'123456'&#125;=>name='zhangsan'&password='123456'</span>
                params = qs.stringify(params);
                url = url + (url.indexOf(<span class="hljs-string">'?'</span>) > -<span class="hljs-number">1</span> ? <span class="hljs-string">'&'</span> : <span class="hljs-string">'?'</span>) + params;
            &#125;
            <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
            <span class="hljs-comment">//第三个参数异步</span>
            xhr.open(method, url, <span class="hljs-literal">true</span>);
            <span class="hljs-comment">//设置返回值为json</span>
            xhr.responseType = <span class="hljs-string">'json'</span>;
            xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">if</span> (xhr.readyState === <span class="hljs-number">4</span> && xhr.status !==<span class="hljs-number">0</span>) &#123;
                    <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
                        <span class="hljs-keyword">const</span> response = &#123;
                            <span class="hljs-attr">data</span>: xhr.response,
                            <span class="hljs-attr">headers</span>: parseHeaders(xhr.getAllResponseHeaders()),
                            <span class="hljs-attr">status</span>: xhr.status,
                            <span class="hljs-attr">statusText</span>: xhr.statusText,
                            config,
                            <span class="hljs-attr">request</span>: xhr
                        &#125;
                        resolve(response);
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: Request failed with status code <span class="hljs-subst">$&#123;xhr.status&#125;</span>`</span>))
                    &#125;
                &#125;
            &#125;

            <span class="hljs-comment">//请求头的处理</span>
            <span class="hljs-keyword">if</span> (headers) &#123;
                <span class="hljs-built_in">Object</span>.keys(headers).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
                    xhr.setRequestHeader(key, headers[key]);
                &#125;)
            &#125;

            <span class="hljs-comment">//请求体的处理</span>
            <span class="hljs-keyword">let</span> body = <span class="hljs-literal">null</span>;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'object'</span> && data !== <span class="hljs-literal">null</span>) &#123;
                body = <span class="hljs-built_in">JSON</span>.stringify(data);<span class="hljs-comment">//转化为字符串</span>
            &#125;

            <span class="hljs-comment">//超时异常</span>
            <span class="hljs-keyword">if</span> (timeout) &#123;
                xhr.timeout = timeout;<span class="hljs-comment">//设置超时时间</span>
                xhr.ontimeout = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">//超时监听</span>
                    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: timeout of <span class="hljs-subst">$&#123;timeout&#125;</span>ms exceeded`</span>));
                &#125;
            &#125;

            <span class="hljs-comment">//网络异常</span>
            xhr.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`net::ERR_INTERNET_DISCONNECTED`</span>));
            &#125;

            xhr.send(body);
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">5.合并配置</h3>
<blockquote>
<p>此过程主要是将客户设置的headers和默认headers合并起来</p>
</blockquote>
<h4 data-id="heading-24">5.1.使用：</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios(&#123;
    <span class="hljs-attr">url</span>: baseUrl + <span class="hljs-string">'/post'</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-string">'name'</span>: <span class="hljs-string">'lisi'</span>,
    &#125;,
    <span class="hljs-attr">data</span>: user,
    <span class="hljs-attr">timeout</span>: <span class="hljs-number">1000</span>,
&#125;).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(response.data);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(error);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="QQ20210327-102916.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/198d337a3a904fa2a9908b946806882e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-25">5.2.实现</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;
<span class="hljs-keyword">import</span> parseHeaders <span class="hljs-keyword">from</span> <span class="hljs-string">'parse-headers'</span>;
<span class="hljs-keyword">import</span> AxiosInterceptorManager <span class="hljs-keyword">from</span> <span class="hljs-string">'./AxiosInterceptorManager'</span>;

<span class="hljs-comment">//默认配置</span>
+<span class="hljs-keyword">const</span> defaults = &#123;
+   method: <span class="hljs-string">'get'</span>,
+   timeout: <span class="hljs-number">0</span>,
+   headers: &#123;
+       common: &#123;
+           accept: <span class="hljs-string">'application/json'</span><span class="hljs-comment">//指定告诉服务器返回JSON格式的数据</span>
+       &#125;
+   &#125;
+&#125;
+<span class="hljs-keyword">const</span> getStyleMethods = [<span class="hljs-string">'get'</span>, <span class="hljs-string">'head'</span>, <span class="hljs-string">'delete'</span>, <span class="hljs-string">'options'</span>];<span class="hljs-comment">//get风格的请求</span>
+getStyleMethods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
+   defaults.headers[method] = &#123;&#125;
+&#125;)

+<span class="hljs-keyword">const</span> postStyleMethods = [<span class="hljs-string">'put'</span>, <span class="hljs-string">'post'</span>, <span class="hljs-string">'patch'</span>];<span class="hljs-comment">//post风格的请求，会有请求体，需要加默认请求体格式</span>
+postStyleMethods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
+   defaults.headers[method] = &#123;
+       <span class="hljs-string">'content-type'</span>:<span class="hljs-string">'application/json'</span><span class="hljs-comment">//请求体格式</span>
+   &#125;
+&#125;)

+<span class="hljs-keyword">const</span> allMethods = [...getStyleMethods, ...postStyleMethods];

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Axios</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
+       <span class="hljs-built_in">this</span>.defaults = defaults;
        <span class="hljs-built_in">this</span>.interceptors = &#123;
            <span class="hljs-attr">request</span>: <span class="hljs-keyword">new</span> AxiosInterceptorManager(),<span class="hljs-comment">//请求拦截器的管理者</span>
            <span class="hljs-attr">response</span>: <span class="hljs-keyword">new</span> AxiosInterceptorManager()<span class="hljs-comment">//响应拦截器的管理者</span>
        &#125;;
    &#125;

    <span class="hljs-function"><span class="hljs-title">request</span>(<span class="hljs-params">config = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-comment">//合并默认配置headers和用户自己配置headers</span>
+       config.headers = <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>.defaults.headers, config.headers);

        <span class="hljs-keyword">const</span> chain = [&#123;<span class="hljs-comment">//设置真正发请求的，然后将请求拦截出入前面，响应拦截插入后面，实现现走请求拦截，再发请求，最后响应拦截</span>
            <span class="hljs-attr">onFulfilled</span>: <span class="hljs-built_in">this</span>.dispatchRequest,
            <span class="hljs-attr">onRejected</span>: <span class="hljs-literal">undefined</span>
        &#125;];
        <span class="hljs-comment">//将请求拦截器一个一个插入最前面，实现先放的后执行</span>
        <span class="hljs-built_in">this</span>.interceptors.request.interceptors.forEach(<span class="hljs-function"><span class="hljs-params">interceptor</span> =></span> &#123;
            interceptor && chain.unshift(interceptor);
        &#125;)
        <span class="hljs-comment">//将响应拦截一个个查处末尾，实现先放先执行</span>
        <span class="hljs-built_in">this</span>.interceptors.response.interceptors.forEach(<span class="hljs-function"><span class="hljs-params">interceptor</span> =></span> &#123;
            interceptor && chain.push(interceptor);
        &#125;)
        <span class="hljs-keyword">let</span> promise = <span class="hljs-built_in">Promise</span>.resolve(config);
        <span class="hljs-keyword">while</span> (chain.length) &#123;
            <span class="hljs-keyword">const</span> &#123; onFulfilled, onRejected &#125; = chain.shift();<span class="hljs-comment">//取出每次的第一条数据</span>
            <span class="hljs-comment">//将config传入onFulfilled</span>
            promise = promise.then(onFulfilled, onRejected);
        &#125;
        <span class="hljs-keyword">return</span> promise;
    &#125;

    <span class="hljs-function"><span class="hljs-title">dispatchRequest</span>(<span class="hljs-params">config</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> &#123; url, method = <span class="hljs-string">'get'</span>, params, data, headers, timeout &#125; = config;
            <span class="hljs-keyword">if</span> (params) &#123;<span class="hljs-comment">//&#123;name:'zhangsan',password:'123456'&#125;=>name='zhangsan'&password='123456'</span>
                params = qs.stringify(params);
                url = url + (url.indexOf(<span class="hljs-string">'?'</span>) > -<span class="hljs-number">1</span> ? <span class="hljs-string">'&'</span> : <span class="hljs-string">'?'</span>) + params;
            &#125;
            <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
            <span class="hljs-comment">//第三个参数异步i,</span>
            xhr.open(method, url, <span class="hljs-literal">true</span>);
            <span class="hljs-comment">//设置返回值为json</span>
            xhr.responseType = <span class="hljs-string">'json'</span>;
            xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">if</span> (xhr.readyState === <span class="hljs-number">4</span>  && xhr.status !==<span class="hljs-number">0</span>) &#123;
                    <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
                        <span class="hljs-keyword">const</span> response = &#123;
                            <span class="hljs-attr">data</span>: xhr.response,
                            <span class="hljs-attr">headers</span>: parseHeaders(xhr.getAllResponseHeaders()),
                            <span class="hljs-attr">status</span>: xhr.status,
                            <span class="hljs-attr">statusText</span>: xhr.statusText,
                            config,
                            <span class="hljs-attr">request</span>: xhr
                        &#125;
                        resolve(response);
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: Request failed with status code <span class="hljs-subst">$&#123;xhr.status&#125;</span>`</span>))
                    &#125;
                &#125;
            &#125;

            <span class="hljs-comment">//请求头的处理</span>
            <span class="hljs-keyword">if</span> (headers) &#123;
                <span class="hljs-comment">/**
                 * headers:&#123;
                 *   common:&#123;accept: 'application/json'&#125;,
                 *   post:&#123;'content-type':'application/json'&#125;
                 * &#125;
                 */</span>
+               <span class="hljs-built_in">Object</span>.keys(headers).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
+                   <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'common'</span> || allMethods.includes(key)) &#123;
+                       <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'common'</span> || key === config.method) &#123;
+                           <span class="hljs-built_in">Object</span>.keys(headers[key]).forEach(<span class="hljs-function"><span class="hljs-params">key2</span> =></span> &#123;
+                               xhr.setRequestHeader(key2, headers[key][key2]);
+                           &#125;)
+                       &#125;
+                   &#125; <span class="hljs-keyword">else</span> &#123;
+                       xhr.setRequestHeader(key, headers[key]);
+                   &#125;
+               &#125;)
+           &#125;

            <span class="hljs-comment">//请求体的处理</span>
            <span class="hljs-keyword">let</span> body = <span class="hljs-literal">null</span>;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'object'</span> && data !== <span class="hljs-literal">null</span>) &#123;
                body = <span class="hljs-built_in">JSON</span>.stringify(data);<span class="hljs-comment">//转化为字符串</span>
            &#125;

            <span class="hljs-comment">//超时异常</span>
            <span class="hljs-keyword">if</span> (timeout) &#123;
                xhr.timeout = timeout;<span class="hljs-comment">//设置超时时间</span>
                xhr.ontimeout = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">//超时监听</span>
                    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: timeout of <span class="hljs-subst">$&#123;timeout&#125;</span>ms exceeded`</span>));
                &#125;
            &#125;

            <span class="hljs-comment">//网络异常</span>
            xhr.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`net::ERR_INTERNET_DISCONNECTED`</span>));
            &#125;

            xhr.send(body);
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">6.转换请求与响应</h3>
<h4 data-id="heading-27">6.1.<code>Axios.js修改</code></h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;
<span class="hljs-keyword">import</span> parseHeaders <span class="hljs-keyword">from</span> <span class="hljs-string">'parse-headers'</span>;
<span class="hljs-keyword">import</span> AxiosInterceptorManager <span class="hljs-keyword">from</span> <span class="hljs-string">'./AxiosInterceptorManager'</span>;

<span class="hljs-comment">//默认配置</span>
<span class="hljs-keyword">const</span> defaults = &#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
    <span class="hljs-attr">timeout</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-attr">common</span>: &#123;
            <span class="hljs-attr">accept</span>: <span class="hljs-string">'application/json'</span><span class="hljs-comment">//指定告诉服务器返回JSON格式的数据</span>
        &#125;
    &#125;,
+   transformRequest: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data, headers</span>) </span>&#123;
+       headers[<span class="hljs-string">'content-type'</span>] = <span class="hljs-string">'application/x-www-form-urlencoded'</span>;
+       <span class="hljs-keyword">return</span> qs.stringify(data);
+   &#125;,
+   transformResponse: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
+       <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'string'</span>);
+       data = <span class="hljs-built_in">JSON</span>.parse(data);
+       <span class="hljs-keyword">return</span> data;
+   &#125;
&#125;
<span class="hljs-keyword">const</span> getStyleMethods = [<span class="hljs-string">'get'</span>, <span class="hljs-string">'head'</span>, <span class="hljs-string">'delete'</span>, <span class="hljs-string">'options'</span>];<span class="hljs-comment">//get风格的请求</span>
getStyleMethods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
    defaults.headers[method] = &#123;&#125;
&#125;)

<span class="hljs-keyword">const</span> postStyleMethods = [<span class="hljs-string">'put'</span>, <span class="hljs-string">'post'</span>, <span class="hljs-string">'patch'</span>];<span class="hljs-comment">//post风格的请求，会有请求体，需要加默认请求体格式</span>
postStyleMethods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
    defaults.headers[method] = &#123;
        <span class="hljs-string">'content-type'</span>: <span class="hljs-string">'application/json'</span><span class="hljs-comment">//请求体格式</span>
    &#125;
&#125;)

<span class="hljs-keyword">const</span> allMethods = [...getStyleMethods, ...postStyleMethods];

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Axios</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.defaults = defaults;
        <span class="hljs-built_in">this</span>.interceptors = &#123;
            <span class="hljs-attr">request</span>: <span class="hljs-keyword">new</span> AxiosInterceptorManager(),<span class="hljs-comment">//请求拦截器的管理者</span>
            <span class="hljs-attr">response</span>: <span class="hljs-keyword">new</span> AxiosInterceptorManager()<span class="hljs-comment">//响应拦截器的管理者</span>
        &#125;;
    &#125;

    <span class="hljs-function"><span class="hljs-title">request</span>(<span class="hljs-params">config = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-comment">//合并默认配置headers和用户自己配置headers</span>
        config.headers = <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>.defaults.headers, config.headers);
        <span class="hljs-comment">//如果有请求转换，执行</span>
+       <span class="hljs-keyword">if</span> (config.transformRequest && config.data) &#123;
+           config.data = config.transformRequest(config.data, config.headers);
+       &#125;
        <span class="hljs-keyword">const</span> chain = [&#123;<span class="hljs-comment">//设置真正发请求的，然后将请求拦截出入前面，响应拦截插入后面，实现现走请求拦截，再发请求，最后响应拦截</span>
            <span class="hljs-attr">onFulfilled</span>: <span class="hljs-built_in">this</span>.dispatchRequest,
            <span class="hljs-attr">onRejected</span>: <span class="hljs-literal">undefined</span>
        &#125;];
        <span class="hljs-comment">//将请求拦截器一个一个插入最前面，实现先放的后执行</span>
        <span class="hljs-built_in">this</span>.interceptors.request.interceptors.forEach(<span class="hljs-function"><span class="hljs-params">interceptor</span> =></span> &#123;
            interceptor && chain.unshift(interceptor);
        &#125;)
        <span class="hljs-comment">//将响应拦截一个个查处末尾，实现先放先执行</span>
        <span class="hljs-built_in">this</span>.interceptors.response.interceptors.forEach(<span class="hljs-function"><span class="hljs-params">interceptor</span> =></span> &#123;
            interceptor && chain.push(interceptor);
        &#125;)
        <span class="hljs-keyword">let</span> promise = <span class="hljs-built_in">Promise</span>.resolve(config);
        <span class="hljs-keyword">while</span> (chain.length) &#123;
            <span class="hljs-keyword">const</span> &#123; onFulfilled, onRejected &#125; = chain.shift();<span class="hljs-comment">//取出每次的第一条数据</span>
            <span class="hljs-comment">//将config传入onFulfilled</span>
            promise = promise.then(onFulfilled, onRejected);
        &#125;
        <span class="hljs-keyword">return</span> promise;
    &#125;

    <span class="hljs-function"><span class="hljs-title">dispatchRequest</span>(<span class="hljs-params">config</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> &#123; url, method = <span class="hljs-string">'get'</span>, params, data, headers, timeout &#125; = config;
            <span class="hljs-keyword">if</span> (params) &#123;<span class="hljs-comment">//&#123;name:'zhangsan',password:'123456'&#125;=>name='zhangsan'&password='123456'</span>
                params = qs.stringify(params);
                url = url + (url.indexOf(<span class="hljs-string">'?'</span>) > -<span class="hljs-number">1</span> ? <span class="hljs-string">'&'</span> : <span class="hljs-string">'?'</span>) + params;
            &#125;
            <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
            <span class="hljs-comment">//第三个参数异步i,</span>
            xhr.open(method, url, <span class="hljs-literal">true</span>);
            <span class="hljs-comment">//设置返回值为json</span>
            xhr.responseType = <span class="hljs-string">'json'</span>;
            xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">if</span> (xhr.readyState === <span class="hljs-number">4</span> && xhr.status !==<span class="hljs-number">0</span>) &#123;
                    <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
                        <span class="hljs-keyword">let</span> response = &#123;
                            <span class="hljs-attr">data</span>: xhr.response,
                            <span class="hljs-attr">headers</span>: parseHeaders(xhr.getAllResponseHeaders()),
                            <span class="hljs-attr">status</span>: xhr.status,
                            <span class="hljs-attr">statusText</span>: xhr.statusText,
                            config,
                            <span class="hljs-attr">request</span>: xhr
                        &#125;
                        <span class="hljs-comment">//响应转换</span>
+                       <span class="hljs-keyword">if</span> (config.transformResponse) &#123;
+                           response = config.transformResponse(response);
+                       &#125;
                        resolve(response);
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: Request failed with status code <span class="hljs-subst">$&#123;xhr.status&#125;</span>`</span>))
                    &#125;
                &#125;
            &#125;

            <span class="hljs-comment">//请求头的处理</span>
            <span class="hljs-keyword">if</span> (headers) &#123;
                <span class="hljs-comment">/**
                 * headers:&#123;
                 *   common:&#123;accept: 'application/json'&#125;,
                 *   post:&#123;'content-type':'application/json'&#125;
                 * &#125;
                 */</span>
                <span class="hljs-built_in">Object</span>.keys(headers).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
                    <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'common'</span> || allMethods.includes(key)) &#123;
                        <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'common'</span> || key === config.method) &#123;
                            <span class="hljs-built_in">Object</span>.keys(headers[key]).forEach(<span class="hljs-function"><span class="hljs-params">key2</span> =></span> &#123;
                                xhr.setRequestHeader(key2, headers[key][key2]);
                            &#125;)
                        &#125;
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        xhr.setRequestHeader(key, headers[key]);
                    &#125;
                &#125;)
            &#125;

            <span class="hljs-comment">//请求体的处理</span>
            <span class="hljs-keyword">let</span> body = <span class="hljs-literal">null</span>;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'object'</span> && data !== <span class="hljs-literal">null</span>) &#123;
                body = <span class="hljs-built_in">JSON</span>.stringify(data);<span class="hljs-comment">//转化为字符串</span>
            &#125;

            <span class="hljs-comment">//超时异常</span>
            <span class="hljs-keyword">if</span> (timeout) &#123;
                xhr.timeout = timeout;<span class="hljs-comment">//设置超时时间</span>
                xhr.ontimeout = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">//超时监听</span>
                    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: timeout of <span class="hljs-subst">$&#123;timeout&#125;</span>ms exceeded`</span>));
                &#125;
            &#125;

            <span class="hljs-comment">//网络异常</span>
            xhr.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`net::ERR_INTERNET_DISCONNECTED`</span>));
            &#125;

            xhr.send(body);
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">7.取消任务</h3>
<ul>
<li>isCancel:判断是否是用户自己取得任务</li>
<li>CancelToken:是一个类，<code>source</code>方法返回一个对象，包含<code>token</code>和<code>cancel</code></li>
<li>cancel:取消任务</li>
</ul>
<h4 data-id="heading-29">7.1.实例</h4>
<p><img alt="QQ20210327-111900.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7183309f72674a9b975637febdd12dd4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
<span class="hljs-keyword">const</span> baseUrl = <span class="hljs-string">'http://localhost:8080'</span>;
<span class="hljs-keyword">const</span> user = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'zhangsan'</span>,
    <span class="hljs-attr">password</span>: <span class="hljs-string">'123456'</span>
&#125;

<span class="hljs-keyword">const</span> CancelToken = axios.CancelToken;
<span class="hljs-keyword">const</span> source = CancelToken.source();
<span class="hljs-keyword">const</span> isCancel = axios.isCancel;
axios(&#123;
    <span class="hljs-attr">url</span>: baseUrl + <span class="hljs-string">'/post'</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-string">'name'</span>: <span class="hljs-string">'lisi'</span>,
    &#125;,
    <span class="hljs-attr">data</span>: user,
    <span class="hljs-attr">timeout</span>: <span class="hljs-number">1000</span>,
    <span class="hljs-attr">cancelToken</span>: source.token
&#125;).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(response.data);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (isCancel(error)) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'用户自己'</span> + error)
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.log(error);
    &#125;
&#125;)

source.cancel(<span class="hljs-string">'取消请求'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">7.2.实现</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios
├── Axios.js
├── AxiosInterceptorManager.js
├── cancel.js
└── index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-31">7.2.1.<code>cancel.js</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cancel</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">reason</span>)</span> &#123;
        <span class="hljs-comment">//存放取消的原因</span>
        <span class="hljs-built_in">this</span>.reason = reason;
    &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CancelToken</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.resolve = <span class="hljs-literal">null</span>;
    &#125;
    <span class="hljs-function"><span class="hljs-title">source</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">token</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
                <span class="hljs-built_in">this</span>.resolve = resolve;
            &#125;),
            <span class="hljs-attr">cancel</span>: <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
                <span class="hljs-built_in">this</span>.resolve(<span class="hljs-keyword">new</span> Cancel(reason))
            &#125;
        &#125;
    &#125;
&#125;

<span class="hljs-comment">//判断error是不是Cancel的实例</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isCancel</span>(<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-keyword">return</span> error <span class="hljs-keyword">instanceof</span> Cancel;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-32">7.2.2.<code>index.js修改</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">import</span> Axios <span class="hljs-keyword">from</span> <span class="hljs-string">'./Axios'</span>;
+   <span class="hljs-keyword">import</span> &#123; CancelToken, isCancel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./cancel'</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createInstance</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">const</span> context = <span class="hljs-keyword">new</span> Axios();
        <span class="hljs-comment">//让request方法里的this永远指向context也就是new Axios</span>
        <span class="hljs-keyword">let</span> instance = Axios.prototype.request.bind(context);
        <span class="hljs-comment">//把Axios的类的实例和类的原型上的方法都拷贝到了instance上，也就是request方法上</span>
        instance = <span class="hljs-built_in">Object</span>.assign(instance, Axios.prototype, context);
        <span class="hljs-keyword">return</span> instance;
    &#125;
    <span class="hljs-keyword">const</span> axios = createInstance();
+   axios.CancelToken = <span class="hljs-keyword">new</span> CancelToken();
+   axios.isCancel = isCancel;
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-33">7.2.3.<code>Axios.js修改</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;
<span class="hljs-keyword">import</span> parseHeaders <span class="hljs-keyword">from</span> <span class="hljs-string">'parse-headers'</span>;
<span class="hljs-keyword">import</span> AxiosInterceptorManager <span class="hljs-keyword">from</span> <span class="hljs-string">'./AxiosInterceptorManager'</span>;

<span class="hljs-comment">//默认配置</span>
<span class="hljs-keyword">const</span> defaults = &#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
    <span class="hljs-attr">timeout</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-attr">common</span>: &#123;
            <span class="hljs-attr">accept</span>: <span class="hljs-string">'application/json'</span><span class="hljs-comment">//指定告诉服务器返回JSON格式的数据</span>
        &#125;
    &#125;,
    <span class="hljs-attr">transformRequest</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data, headers</span>) </span>&#123;
        headers[<span class="hljs-string">'content-type'</span>] = <span class="hljs-string">'application/x-www-form-urlencoded'</span>;
        <span class="hljs-keyword">return</span> qs.stringify(data);
    &#125;,
    <span class="hljs-attr">transformResponse</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'string'</span>);
        data = <span class="hljs-built_in">JSON</span>.parse(data);
        <span class="hljs-keyword">return</span> data;
    &#125;
&#125;
<span class="hljs-keyword">const</span> getStyleMethods = [<span class="hljs-string">'get'</span>, <span class="hljs-string">'head'</span>, <span class="hljs-string">'delete'</span>, <span class="hljs-string">'options'</span>];<span class="hljs-comment">//get风格的请求</span>
getStyleMethods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
    defaults.headers[method] = &#123;&#125;
&#125;)

<span class="hljs-keyword">const</span> postStyleMethods = [<span class="hljs-string">'put'</span>, <span class="hljs-string">'post'</span>, <span class="hljs-string">'patch'</span>];<span class="hljs-comment">//post风格的请求，会有请求体，需要加默认请求体格式</span>
postStyleMethods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
    defaults.headers[method] = &#123;
        <span class="hljs-string">'content-type'</span>: <span class="hljs-string">'application/json'</span><span class="hljs-comment">//请求体格式</span>
    &#125;
&#125;)

<span class="hljs-keyword">const</span> allMethods = [...getStyleMethods, ...postStyleMethods];

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Axios</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.defaults = defaults;
        <span class="hljs-built_in">this</span>.interceptors = &#123;
            <span class="hljs-attr">request</span>: <span class="hljs-keyword">new</span> AxiosInterceptorManager(),<span class="hljs-comment">//请求拦截器的管理者</span>
            <span class="hljs-attr">response</span>: <span class="hljs-keyword">new</span> AxiosInterceptorManager()<span class="hljs-comment">//响应拦截器的管理者</span>
        &#125;;
    &#125;

    <span class="hljs-function"><span class="hljs-title">request</span>(<span class="hljs-params">config = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-comment">//合并默认配置headers和用户自己配置headers</span>
        config.headers = <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>.defaults.headers, config.headers);
        <span class="hljs-comment">//如果有请求转换，执行</span>
        <span class="hljs-keyword">if</span> (config.transformRequest && config.data) &#123;
            config.data = config.transformRequest(config.data, config.headers);
        &#125;
        <span class="hljs-keyword">const</span> chain = [&#123;<span class="hljs-comment">//设置真正发请求的，然后将请求拦截出入前面，响应拦截插入后面，实现现走请求拦截，再发请求，最后响应拦截</span>
            <span class="hljs-attr">onFulfilled</span>: <span class="hljs-built_in">this</span>.dispatchRequest,
            <span class="hljs-attr">onRejected</span>: <span class="hljs-literal">undefined</span>
        &#125;];
        <span class="hljs-comment">//将请求拦截器一个一个插入最前面，实现先放的后执行</span>
        <span class="hljs-built_in">this</span>.interceptors.request.interceptors.forEach(<span class="hljs-function"><span class="hljs-params">interceptor</span> =></span> &#123;
            interceptor && chain.unshift(interceptor);
        &#125;)
        <span class="hljs-comment">//将响应拦截一个个查处末尾，实现先放先执行</span>
        <span class="hljs-built_in">this</span>.interceptors.response.interceptors.forEach(<span class="hljs-function"><span class="hljs-params">interceptor</span> =></span> &#123;
            interceptor && chain.push(interceptor);
        &#125;)
        <span class="hljs-keyword">let</span> promise = <span class="hljs-built_in">Promise</span>.resolve(config);
        <span class="hljs-keyword">while</span> (chain.length) &#123;
            <span class="hljs-keyword">const</span> &#123; onFulfilled, onRejected &#125; = chain.shift();<span class="hljs-comment">//取出每次的第一条数据</span>
            <span class="hljs-comment">//将config传入onFulfilled</span>
            promise = promise.then(onFulfilled, onRejected);
        &#125;
        <span class="hljs-keyword">return</span> promise;
    &#125;

    <span class="hljs-function"><span class="hljs-title">dispatchRequest</span>(<span class="hljs-params">config</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> &#123; url, method = <span class="hljs-string">'get'</span>, params, data, headers, timeout &#125; = config;
            <span class="hljs-keyword">if</span> (params) &#123;<span class="hljs-comment">//&#123;name:'zhangsan',password:'123456'&#125;=>name='zhangsan'&password='123456'</span>
                params = qs.stringify(params);
                url = url + (url.indexOf(<span class="hljs-string">'?'</span>) > -<span class="hljs-number">1</span> ? <span class="hljs-string">'&'</span> : <span class="hljs-string">'?'</span>) + params;
            &#125;
            <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
            <span class="hljs-comment">//第三个参数异步i,</span>
            xhr.open(method, url, <span class="hljs-literal">true</span>);
            <span class="hljs-comment">//设置返回值为json</span>
            xhr.responseType = <span class="hljs-string">'json'</span>;
            xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">if</span> (xhr.readyState === <span class="hljs-number">4</span> && xhr.status !== <span class="hljs-number">0</span>) &#123;
                    <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;
                        <span class="hljs-keyword">let</span> response = &#123;
                            <span class="hljs-attr">data</span>: xhr.response,
                            <span class="hljs-attr">headers</span>: parseHeaders(xhr.getAllResponseHeaders()),
                            <span class="hljs-attr">status</span>: xhr.status,
                            <span class="hljs-attr">statusText</span>: xhr.statusText,
                            config,
                            <span class="hljs-attr">request</span>: xhr
                        &#125;
                        <span class="hljs-keyword">debugger</span>
                        <span class="hljs-comment">//响应转换</span>
                        <span class="hljs-keyword">if</span> (config.transformResponse) &#123;
                            response = config.transformResponse(response);
                        &#125;
                        resolve(response);
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: Request failed with status code <span class="hljs-subst">$&#123;xhr.status&#125;</span>`</span>))
                    &#125;
                &#125;
            &#125;

            <span class="hljs-comment">//请求头的处理</span>
            <span class="hljs-keyword">if</span> (headers) &#123;
                <span class="hljs-comment">/**
                 * headers:&#123;
                 *   common:&#123;accept: 'application/json'&#125;,
                 *   post:&#123;'content-type':'application/json'&#125;
                 * &#125;
                 */</span>
                <span class="hljs-built_in">Object</span>.keys(headers).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
                    <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'common'</span> || allMethods.includes(key)) &#123;
                        <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'common'</span> || key === config.method) &#123;
                            <span class="hljs-built_in">Object</span>.keys(headers[key]).forEach(<span class="hljs-function"><span class="hljs-params">key2</span> =></span> &#123;
                                xhr.setRequestHeader(key2, headers[key][key2]);
                            &#125;)
                        &#125;
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        xhr.setRequestHeader(key, headers[key]);
                    &#125;
                &#125;)
            &#125;

            <span class="hljs-comment">//请求体的处理</span>
            <span class="hljs-keyword">let</span> body = <span class="hljs-literal">null</span>;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'object'</span> && data !== <span class="hljs-literal">null</span>) &#123;
                body = <span class="hljs-built_in">JSON</span>.stringify(data);<span class="hljs-comment">//转化为字符串</span>
            &#125;

            <span class="hljs-comment">//超时异常</span>
            <span class="hljs-keyword">if</span> (timeout) &#123;
                xhr.timeout = timeout;<span class="hljs-comment">//设置超时时间</span>
                xhr.ontimeout = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">//超时监听</span>
                    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Error: timeout of <span class="hljs-subst">$&#123;timeout&#125;</span>ms exceeded`</span>));
                &#125;
            &#125;

            <span class="hljs-comment">//网络异常</span>
            xhr.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`net::ERR_INTERNET_DISCONNECTED`</span>));
            &#125;

            <span class="hljs-comment">//处理用户自己取消的操作</span>
+           <span class="hljs-keyword">if</span> (config.cancelToken) &#123;
+               config.cancelToken.then(<span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
+                   xhr.abort();<span class="hljs-comment">//取消请求</span>
+                   reject(reason);
+               &#125;)
+           &#125;
            xhr.send(body);
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Axios;
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            