
---
title: '12 JS-Web-API-Ajax'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: '跨域的图片地址/'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 19:53:05 GMT
thumbnail: '跨域的图片地址/'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ajax 的核心API - XMLHttpRequest</h2>
<h3 data-id="heading-1">面试题</h3>
<pre><code class="copyable">- 手写一个简易的ajax
- 跨域常用的实现方式
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>手写一个简易的ajax</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span>(<span class="hljs-params">url</span>)</span>&#123;
    <span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
        <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
        xhr.open(<span class="hljs-string">'GET'</span>,url,<span class="hljs-literal">true</span>)
        xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">if</span>(xhr.readyState === <span class="hljs-number">4</span>)&#123;
                <span class="hljs-keyword">if</span>(xhr.status === <span class="hljs-number">200</span>)&#123;
                    resolve(
                        <span class="hljs-built_in">JSON</span>.parse(xhr.responseText)
                    )
                &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(xhr.status === <span class="hljs-number">404</span>)&#123;
                    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'404 not found'</span>))
                &#125;
            &#125;
        &#125;
        xhr.send(<span class="hljs-literal">null</span>)
    &#125;)
    <span class="hljs-keyword">return</span> p;
&#125;

<span class="hljs-keyword">const</span> url = <span class="hljs-string">'/data/test.json'</span>
ajax(url)
.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res))
.catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>跨域常用的实现方式
<ul>
<li>JSONP</li>
<li>CORS(纯服务端设置)</li>
</ul>
</li>
</ul>
<p>知识点</p>
<ul>
<li>XMLHttpRequest</li>
<li>状态码</li>
<li>跨域：同源策略，跨域解决方案</li>
</ul>
<h3 data-id="heading-2">XMLHttpRequest</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//get请求</span>
<span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
xhr.open(<span class="hljs-string">"GET"</span>,<span class="hljs-string">"/api"</span>,<span class="hljs-literal">true</span>) <span class="hljs-comment">//true是支持异步，false是同步</span>
xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">//这里的函数异步执行，可参考之前JS基础中的异步模块</span>
    <span class="hljs-keyword">if</span>(xhr.readyState === <span class="hljs-number">4</span>)&#123;
        <span class="hljs-keyword">if</span>(xhr.status === <span class="hljs-number">200</span>)&#123;
            <span class="hljs-built_in">console</span>.log(
                <span class="hljs-built_in">JSON</span>.parse(xhr.responseText)
            )
            alert(xhr.responseText)
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(xhr.status === <span class="hljs-number">404</span>)&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'404 not found'</span>)
        &#125;
    &#125;
&#125;
xhr.send(<span class="hljs-literal">null</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//post请求
const xhr = new XMLHttpRequest()
xhr.open("POST","/login",true)//true是支持异步，false是同步
xhr.onreadystatechange = function()&#123;
    //这里的函数异步执行，可参考之前JS基础中的异步模块
    if(xhr.readyState === 4)&#123;
        if(xhr.status === 200)&#123;
            alert(xhr.responseText)
        &#125;
    &#125;
&#125;
const postData = &#123;
    userName:'zc',
    password:'xxd'
&#125;
xhr.send(JSON.stringify(postData))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">xhr.readyState</h3>
<ul>
<li>0 - (未初始化） 还没有调用send()方法</li>
<li>1 - (载入) 已调用send()方法，正在发送请求</li>
<li>2 - （载入完成） send()方法执行完成，已经接收到全部响应内容</li>
<li>3 - （交互） 正在解析响应内容</li>
<li>4 - （完成） 响应内容解析完成，可以在客户端调用</li>
</ul>
<p>我们也是在状态4的时候才会获取responseText</p>
<h3 data-id="heading-4">xhr.status</h3>
<ul>
<li>2xx - 表示成功处理请求，如200</li>
<li>3xx - 需要重定向，浏览器直接跳转，如301 302 304</li>
<li>4xx - 客户端请求错误，如404  403</li>
<li>5xx - 服务器端错误</li>
</ul>
<h3 data-id="heading-5">ajax常用插件工具</h3>
<ul>
<li>jQuery</li>
<li>fetch</li>
<li>axios</li>
</ul>
<h2 data-id="heading-6">什么是浏览器的同源策略</h2>
<ul>
<li>什么是跨域（同源策略）</li>
<li>JSONP</li>
<li>CORS(服务端支持)</li>
</ul>
<h3 data-id="heading-7">同源策略</h3>
<ul>
<li>ajax请求时，浏览器要求当前网页和server必须同源（安全）</li>
<li>同源：协议、域名、端口，三者必须一致</li>
<li>前端：<a href="http://a.com:8080/" target="_blank" rel="nofollow noopener noreferrer">a.com:8080</a>; server:<a href="https://b.com/api/xxx" target="_blank" rel="nofollow noopener noreferrer">b.com/api/xxx</a></li>
</ul>
<p>只是浏览器的要求， 服务器是可以跨域的，比如爬虫</p>
<h3 data-id="heading-8">加载图片css js 可无视同源策略</h3>
<ul>
<li><code><img src=跨域的图片地址/></code></li>
<li><code><link href=跨域的css地址/></code></li>
<li><code><script src=跨域的js地址/></script></code></li>
<li><code><img/></code>可用于统计打点，可使用第三方统计服务</li>
<li><code><link/> <script></code>可使用CDN,CDN一般都是外域</li>
<li><code><script></code>可实现JSONP</li>
</ul>
<h3 data-id="heading-9">跨域</h3>
<ul>
<li>所有的跨域，都必须经过server允许和配合</li>
<li>未经server端允许就实现跨域，说明浏览器有漏洞，危险信号</li>
</ul>
<h2 data-id="heading-10">实现跨域的常见方式 - jsonp 和 CORS</h2>
<ul>
<li>访问<code>https://baidu.com/</code>服务端一定返回一个html文件吗？
<ul>
<li>服务器可以任意动态拼接数据返回，只要符合html格式要求</li>
<li>同理于<code><script src='https://baidu.com/getData.js</code>></li>
</ul>
</li>
<li><code><scrip></code>可绕过跨域限制</li>
<li>服务器可以任意动态拼接数据返回</li>
<li>所以，<code><script></code>就可以获得跨域的数据，只要服务端愿意返回</li>
</ul>
<h3 data-id="heading-11">什么是jsonp</h3>
<ul>
<li>
<p>首先，因为ajax无法跨域，然后开发者就有所思考</p>
</li>
<li>
<p>其次，开发者发现， <code><script></code>标签的src属性是可以跨域的,把跨域服务器写成 调用本地的函数 ，回调数据回来不就好了？</p>
</li>
<li>
<p>json刚好被js支持（object）</p>
</li>
<li>
<p>调用跨域服务器上动态生成的js格式文件（不管是什么类型的地址，最终生成的返回值都是一段js代码）</p>
</li>
<li>
<p>这种获取远程数据的方式看起来非常像ajax，但其实并不一样</p>
</li>
<li>
<p>便于客户端使用数据，逐渐形成了一种非正式传输协议，人们把它称作JSONP。</p>
</li>
<li>
<p>传递一个callback参数给跨域服务端，然后跨域服务端返回数据时会将这个callback参数作为函数名来包裹住json数据即可。</p>
</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">//jsonp示例
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-built_in">window</span>.callback = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
    <span class="hljs-comment">//这是我们跨域得到的信息</span>
    <span class="hljs-built_in">console</span>.log(data)
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">'https://baidu.com/getData.js'</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-comment"><!-- 将返回callback(&#123;x:100,y:200&#125;) --></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>jQuery实现jsonp</p>
<pre><code class="hljs language-js copyable" lang="js">$.ajax(&#123;
    <span class="hljs-attr">url</span>:<span class="hljs-string">'http://localhost:8882/api.json'</span>,
    <span class="hljs-attr">dataType</span>:<span class="hljs-string">'jsonp'</span>,
    <span class="hljs-attr">jsonpCallback</span>:<span class="hljs-string">'callback'</span>,
    <span class="hljs-attr">success</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(data)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">jsonp与AJAX的区别是什么？</h3>
<ul>
<li>ajax和jsonp本质上是不同的东西。</li>
<li>ajax的核心是通过XmlHttpRequest获取非本页内容</li>
<li>jsonp的核心则是动态添加
</li></ul>
<h3 data-id="heading-13">CORS - 服务器设置http header</h3>
<p>通过服务端调置可解决跨域</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f890948856804e168aa5d197e73bd330~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            