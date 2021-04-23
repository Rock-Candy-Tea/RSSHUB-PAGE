
---
title: 'Node.js（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4371'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 16:22:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=4371'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">实现服务器步骤和核心代码</h3>
<ol>
<li>
<h4 data-id="heading-1">导入 <code>http</code> 模块</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>)  <span class="hljs-comment">// Node 自带核心内置模块</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-2">创建 <code>web</code>服务器实例</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 调用 http.createServer() 方法，即可快速创建一个 web 服务器实例</span>

<span class="hljs-keyword">const</span> server = http.createServer() 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-3">为服务器实例绑定 <code>request</code> 事件</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 为服务器实例绑定 request 事件，即可监听客户端发送过来的网络请求</span>

<span class="hljs-comment">// 使用服务器实例的 .on() 方法，为服务器绑定一个 request 事件</span>
server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  <span class="hljs-comment">// 只要有客户端来请求我们自己的服务器，就会被触发 request 事件，从而调用这个事件处理程序</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'访问服务器成功'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-4">启动服务器</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 调用服务器实例的 .listen() 方法，即可启动当前的 web 服务器实例</span>
<span class="hljs-comment">//设置 端口 3000 </span>
server.listen(<span class="hljs-number">3000</span>，=> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'running……'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-5">注意</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span>如果终端关闭就相当于 web服务关闭了
<span class="hljs-number">2.</span>ctrl+c 停止当前的进程
<span class="hljs-number">3.</span>前端请求的内容是中文乱码 需要 设置响应头res.setHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'text/html;      charset=utf-8'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h3 data-id="heading-6">创建基本的服务器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 导入 http 模块</span>
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>)

<span class="hljs-comment">// 2. 创建 web 服务器实例</span>
<span class="hljs-keyword">const</span> server = http.createServer()

<span class="hljs-comment">// 3. 为服务器实例绑定 request 事件，监听客户端的请求</span>
server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'访问服务器成功'</span>)
&#125;)

<span class="hljs-comment">// 4. 启动服务器</span>
server.listen(<span class="hljs-number">8080</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;  
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'running……'</span>)
&#125;)

<span class="hljs-comment">// 为了防止中文乱码问题，需要设置响应头，</span>
  res.setHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'text/html; charset=utf-8'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">req请求对象 （ request ）</h2>
<p>服务器 后台接收到前端的请求，就会调用  <code>server.on</code>为服务器绑定 request事件处理程序，监听前端发送的请求。如果想在事件处理程序中，访问与客户端相关的数据与属性，可以使用如下方式：</p>
<pre><code class="hljs language-js copyable" lang="js">server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
  <span class="hljs-comment">// req 是请求对象，它包含了与客户端相关的数据和属性</span>
  <span class="hljs-comment">// req.url 获取客户端请求的 url 地址</span>
  <span class="hljs-comment">// req.method 获取客户端请求的类型</span>

  <span class="hljs-keyword">const</span> str = <span class="hljs-string">`<span class="hljs-subst">$&#123;req.url&#125;</span> -- <span class="hljs-subst">$&#123;req.method&#125;</span>`</span>

  <span class="hljs-built_in">console</span>.log(str)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">res响应对象（response）</h2>
<blockquote>
<p>服务器 后台返回给前端的内容</p>
</blockquote>
<p>在服务器的 request 事件处理程序中，如果想访问与服务器相关的数据和属性，可以使用如下方式</p>
<p>res响应对象给前端 所携带的内容有如下</p>
<ul>
<li>响应对象，服务器给浏览器返回的响应内容，可以通过该对象设置</li>
<li>res.setHeader()  设置响应头，响应内容格式和编码</li>
<li>res.statusCode  设置状态码</li>
<li>res.end()    把响应报文（响应行、响应头、响应体）发送给浏览器</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
  <span class="hljs-comment">// res 是响应对象，它包含了与服务器相关的数据和属性</span>
  <span class="hljs-comment">// 例如：将字符串发送到客户端</span>

  <span class="hljs-keyword">const</span> str = <span class="hljs-string">`<span class="hljs-subst">$&#123;req.url&#125;</span> -- <span class="hljs-subst">$&#123;req.method&#125;</span>`</span>
  
  <span class="hljs-comment">// res.end() 方法的作用</span>
  <span class="hljs-comment">// 向客户端发送指定的内容，并结束这次请求的处理过程</span>
  res.end(str)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">解决中文乱码问题</h2>
<p>当调用 <code>res.end()</code> 方法，向客户端发送中文内容的时候，会出现乱码问题，此时，需要手动设置内容的编码格式</p>
<pre><code class="hljs language-js copyable" lang="js">server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
  <span class="hljs-comment">// 发送包含中文的内容</span>
  <span class="hljs-keyword">const</span> str = <span class="hljs-string">`您请求的 url 地址是：<span class="hljs-subst">$&#123;req.url&#125;</span>，请求的 method 类型是：<span class="hljs-subst">$&#123;req.method&#125;</span>`</span>

  <span class="hljs-comment">// 为了防止中文乱码问题，需要设置响应头，</span>
  res.setHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'text/html; charset=utf-8'</span>)

  <span class="hljs-comment">// 把包含中文的内容返回给客户端</span>
  res.end(str)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">请求对象_GET方式_</h2>
<pre><code class="hljs language-js copyable" lang="js">server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;  
  <span class="hljs-comment">// 形参req 是 请求request的意思，所有和请求相关的信息，都在req对象中</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>形参 req</p>
<ul>
<li>请求对象，浏览器发送的请求报文中的数据已经被解析到该对象上</li>
<li>req.url   获取请求行中的路径</li>
<li>req.method  获取请求行中的方式</li>
<li>req.headers  获取请求头数据</li>
</ul>
</li>
<li>
<p>代码实例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);

<span class="hljs-keyword">const</span> server = http.createServer();

server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123; 
    <span class="hljs-built_in">console</span>.log(req.method); <span class="hljs-comment">// 获取前端使用的请求方式   GET</span>
    <span class="hljs-built_in">console</span>.log(req.url); <span class="hljs-comment">// 获取前端使用的请求地址(从域名和端口往后的部分)   /?a=10&b=20&c=30</span>
    <span class="hljs-built_in">console</span>.log(req.headers); <span class="hljs-comment">// 获取前端使用的请求头  </span>
    res.end(); 
&#125;);

server.listen(<span class="hljs-number">3000</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'服务器启动了'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-11">请求对象-POST方式 -接参数</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);

<span class="hljs-keyword">const</span> server = http.createServer();

server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(req.method); <span class="hljs-comment">// POST</span>
    <span class="hljs-built_in">console</span>.log(req.url); 
    <span class="hljs-built_in">console</span>.log(req.headers);

    <span class="hljs-comment">// 接受参数</span>
    <span class="hljs-keyword">let</span> str = <span class="hljs-string">''</span>; <span class="hljs-comment">// 定义一个用于保存数据的空字符串</span>
    req.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">chunk</span>) =></span> &#123; <span class="hljs-comment">// 给req注册data事件，只要有数据提交过来，就会触发；用于接收提交过来的数据(数据过大, 会多次触发, 接收字节)</span>
        str += chunk; <span class="hljs-comment">// 拼接到变量上</span>
    &#125;);
    req.on(<span class="hljs-string">'end'</span>, <span class="hljs-function">() =></span> &#123; <span class="hljs-comment">// 给req注册end事件，当完全接收了提交过来的数据，就会触发</span>
        <span class="hljs-built_in">console</span>.log(str); <span class="hljs-comment">// a=10&b=20&c=30</span>
    &#125;);
    res.end(str);
&#125;);
<span class="hljs-comment">// 前端请求插件: 发送POST请求和参数 a=10&b=20&c=30</span>
server.listen(<span class="hljs-number">3000</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'服务器启动了'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">小结</h2>
<pre><code class="hljs language-js copyable" lang="js">req.url    <span class="hljs-comment">//获取请求行中的路径</span>
req.method  <span class="hljs-comment">//获取请求行中的方式</span>
req.headers  <span class="hljs-comment">//获取请求头数据 </span>
res.setHeader()  <span class="hljs-comment">//设置响应头，响应内容格式和编码</span>
res.statusCode  <span class="hljs-comment">//设置状态码</span>
res.end()     <span class="hljs-comment">//把响应报文（响应行、响应头、响应体）发送给浏览器</span>
res.setHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'text/html; charset=utf-8'</span>)  <span class="hljs-comment">// 为了防止中文乱码问题，需要设置响应头，</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">接口编写</h2>
<p>需求: 后端监测前端发送的请求方式, 以及请求的url, 以及请求的参数</p>
<p>功能:  GET  /api/list  后台把数据返回给前端</p>
<p>功能:  POST /api/add 前端把参数key=value&key=value字符串发到后台, 保存到数组里</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
<span class="hljs-keyword">const</span> querystring = <span class="hljs-built_in">require</span>(<span class="hljs-string">"querystring"</span>);
<span class="hljs-keyword">const</span> server = http.createServer();

<span class="hljs-keyword">let</span> arr = []; <span class="hljs-comment">// 不要写在下面的函数里, 不然每次请求都会初始化, 但是这个js重启代码会重新执行清空数组</span>

server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> &#123; method, url &#125; = req; <span class="hljs-comment">// 提取请求方式, 和请求地址</span>
    res.setHeader(<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"text/html; charset=utf-8;"</span>); <span class="hljs-comment">// 设置响应头, 返回的是中文</span>

    <span class="hljs-comment">// 1. GET方式 - 查询所有数据</span>
    <span class="hljs-keyword">if</span> (method == <span class="hljs-string">"GET"</span> && url == <span class="hljs-string">"/api/list"</span>) &#123;
        res.end(<span class="hljs-built_in">JSON</span>.stringify(&#123; <span class="hljs-comment">// 把数据响应回给前端</span>
            <span class="hljs-attr">status</span>: <span class="hljs-number">200</span>,
            <span class="hljs-attr">msg</span>: <span class="hljs-string">"获取成功"</span>,
            <span class="hljs-attr">data</span>: arr
        &#125;));
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (method == <span class="hljs-string">"POST"</span> && url == <span class="hljs-string">"/api/add"</span>) &#123; <span class="hljs-comment">// 接收前端发来的数据, 组织格式保存到数组里</span>
        <span class="hljs-comment">// POST方式 - 添加数据到arr数组里 (要求前台传递一个JSON字符串数据)</span>
        <span class="hljs-keyword">let</span> str = <span class="hljs-string">''</span>;
        req.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">chunk</span>) =></span> &#123;
            str += chunk;
        &#125;);
        req.on(<span class="hljs-string">'end'</span>, <span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 直接用queryString可以把key=value&key=value字符串转成对象格式</span>
            <span class="hljs-keyword">let</span> obj = querystring.parse(str.replace(<span class="hljs-string">"?"</span>, <span class="hljs-string">""</span>));
            arr.push(obj); <span class="hljs-comment">// 把发来的数据对象保存到全局 数组里</span>
            res.end(<span class="hljs-built_in">JSON</span>.stringify(&#123;
                <span class="hljs-attr">status</span>: <span class="hljs-number">201</span>,
                <span class="hljs-attr">msg</span>: <span class="hljs-string">"添加成功"</span>
            &#125;));
        &#125;);
    &#125; <span class="hljs-keyword">else</span> &#123;
        res.end(<span class="hljs-string">"请确认接口地址和对应的请求方式是否正确"</span>);
    &#125;
&#125;);

server.listen(<span class="hljs-number">3000</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'服务器启动了, http://127.0.0.1:3000'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">「点赞、收藏和评论」</h2>
<p>❤️关注+点赞+收藏+评论+转发❤️，鼓励笔者创作更好的文章，谢谢🙏大家。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            