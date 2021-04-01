
---
title: 'Ajax跨域'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=983'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 19:54:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=983'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、Ajax</h1>
<p>XHR：使用XHR对象首先要调用open()方法，这个方法接收3个参数，请求类型（"get","post"等）、请求URL，以及表示请求是否异步的布尔值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
xhr.open(<span class="hljs-string">"get"</span>,<span class="hljs-string">"example.php"</span>,<span class="hljs-literal">false</span>);
<span class="hljs-comment">//这行代码就是可以向example.php发送一个同步的Get请求，并未发送请求，只是为发送请求做好准备。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">xhr.send(<span class="hljs-literal">null</span>);
<span class="hljs-comment">//send() 方法接收一个参数，是作为请求体发送的数据，如果不需要发送请求体，则必须传null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>send()后，请求就会发送到服务器，等待服务器响应。收到响应后XHR对象的一下属性会被填充上数据。</li>
<li>xhr.readyState == 4(0：未初始化，1：已打开，2：已发送，3：接受中，4：完成)</li>
<li>readyState从一个值变成另外一个值，都会触发readystatechange事件。</li>
</ol>
<p>xhr.onreadtstatechange=function()&#123;&#125;</p>
<p>表单序列化可以使用serialize()函数来创建相应的字符串。</p>
<h1 data-id="heading-1">二、跨域</h1>
<blockquote>
<p>当一个请求url的协议、域名、端口三者之间任意一个与当前页面url不同即为跨域</p>
</blockquote>
<p>非同源限制</p>
<ul>
<li>无法读取非同源网页的 Cookie、LocalStorage 和 IndexedDB</li>
<li>无法接触非同源网页的 DOM</li>
<li>无法向非同源地址发送 AJAX 请求</li>
</ul>
<h3 data-id="heading-2">1. 设置document.domain解决无法读取非同源网页的 Cookie问题</h3>
<ul>
<li>因为浏览器是通过document.domain属性来检查两个页面是否同源，因此只要通过设置相同的document.domain，两个页面就可以共享Cookie（此方案仅限主域相同，子域不同的跨域应用场景。）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.domain = <span class="hljs-string">'test.com'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.跨文档通信 API：window.postMessage()</h3>
<p>调用postMessage方法实现父窗口<a href="http://test1.xn--comhttp-oo3lknk23drf5f//test2.com%E5%8F%91%E6%B6%88%E6%81%AF%EF%BC%88%E5%AD%90%E7%AA%97%E5%8F%A3%E5%90%8C%E6%A0%B7%E5%8F%AF%E4%BB%A5%E9%80%9A%E8%BF%87%E8%AF%A5%E6%96%B9%E6%B3%95%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF%E7%BB%99%E7%88%B6%E7%AA%97%E5%8F%A3%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">test1.com向子窗口http://test2.com发…</a></p>
<ul>
<li>页面和其打开的新窗口的数据传递</li>
<li>多窗口之间消息传递</li>
<li>页面与嵌套的iframe消息传递</li>
<li>上面三个场景的跨域数据传递</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父窗口打开一个子窗口</span>
<span class="hljs-keyword">var</span> openWindow = <span class="hljs-built_in">window</span>.open(<span class="hljs-string">'http://test2.com'</span>, <span class="hljs-string">'title'</span>);
 
<span class="hljs-comment">// 父窗口向子窗口发消息(第一个参数代表发送的内容，第二个参数代表接收消息窗口的url)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用message事件，监听对方发送的消息</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 监听 message 消息</span>
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(e.source); <span class="hljs-comment">// e.source 发送消息的窗口</span>
  <span class="hljs-built_in">console</span>.log(e.origin); <span class="hljs-comment">// e.origin 消息发向的网址</span>
  <span class="hljs-built_in">console</span>.log(e.data);   <span class="hljs-comment">// e.data   发送的消息</span>
&#125;,<span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.JSONP</h3>
<p>JSONP 是服务器与客户端跨源通信的常用方法。最大特点就是简单适用，兼容性好（兼容低版本IE），缺点是只支持get请求，不支持post请求。</p>
<p>核心思想：网页通过添加一个<script>元素，向服务器请求 JSON 数据，服务器收到请求后，将数据放在一个指定名字的回调函数的参数位置传回来。
①原生实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><script src=<span class="hljs-string">"http://test.com/data.php?callback=dosomething"</span>></script>
<span class="hljs-comment">// 向服务器test.com发出请求，该请求的查询字符串有一个callback参数，用来指定回调函数的名字</span>
 
<span class="hljs-comment">// 处理服务器返回回调函数的数据</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dosomething</span>(<span class="hljs-params">res</span>)</span>&#123;
        <span class="hljs-comment">// 处理获得的数据</span>
        <span class="hljs-built_in">console</span>.log(res.data)
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4.CORS跨源资源共享（CORS，Cross-Origin Resource Sharing）</h3>
<p>CORS 是跨域资源分享（Cross-Origin Resource Sharing）的缩写。它是 W3C 标准，属于跨源 AJAX 请求的根本解决方法。</p>
<h5 data-id="heading-6">1、普通跨域请求：只需服务器端设置Access-Control-Allow-Origin</h5>
<h5 data-id="heading-7">2、带cookie跨域请求：前后端都需要进行设置</h5>
<p>【前端设置】根据xhr.withCredentials字段判断是否带有cookie</p>
<ul>
<li>原生ajax</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest(); <span class="hljs-comment">// IE8/9需用window.XDomainRequest兼容</span>
<span class="hljs-comment">// 前端设置是否带cookie</span>
xhr.withCredentials = <span class="hljs-literal">true</span>;
 
xhr.open(<span class="hljs-string">'post'</span>, <span class="hljs-string">'http://www.domain2.com:8080/login'</span>, <span class="hljs-literal">true</span>);
xhr.setRequestHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'application/x-www-form-urlencoded'</span>);
xhr.send(<span class="hljs-string">'user=admin'</span>);
 
xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (xhr.readyState == <span class="hljs-number">4</span> && xhr.status == <span class="hljs-number">200</span>) &#123;
        alert(xhr.responseText);
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>jQuery ajax</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">$.ajax(&#123;
   <span class="hljs-attr">url</span>: <span class="hljs-string">'http://www.test.com:8080/login'</span>,
   <span class="hljs-attr">type</span>: <span class="hljs-string">'get'</span>,
   <span class="hljs-attr">data</span>: &#123;&#125;,
   <span class="hljs-attr">xhrFields</span>: &#123;
       <span class="hljs-attr">withCredentials</span>: <span class="hljs-literal">true</span>    <span class="hljs-comment">// 前端设置是否带cookie</span>
   &#125;,
   <span class="hljs-attr">crossDomain</span>: <span class="hljs-literal">true</span>,   <span class="hljs-comment">// 会让请求头中包含跨域的额外信息，但不会含cookie</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>axios</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">axios.defaults.withCredentials = <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>服务端设置</li>
</ul>
<p>服务器端对于CORS的支持，主要是通过设置Access-Control-Allow-Origin来进行的。如果浏览器检测到相应的设置，就可以允许Ajax进行跨域的访问。
1、 Java后台</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">/*
 * 导入包：import javax.servlet.http.HttpServletResponse;
 * 接口参数中定义：HttpServletResponse response
 */</span>
 
<span class="hljs-comment">// 允许跨域访问的域名：若有端口需写全（协议+域名+端口），若没有端口末尾不用加'/'</span>
response.setHeader(<span class="hljs-string">"Access-Control-Allow-Origin"</span>, <span class="hljs-string">"http://www.domain1.com"</span>); 
 
<span class="hljs-comment">// 允许前端带认证cookie：启用此项后，上面的域名不能为'*'，必须指定具体的域名，否则浏览器会提示</span>
response.setHeader(<span class="hljs-string">"Access-Control-Allow-Credentials"</span>, <span class="hljs-string">"true"</span>); 
 
<span class="hljs-comment">// 提示OPTIONS预检时，后端需要设置的两个常用自定义头</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、 Nodejs后台</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
<span class="hljs-keyword">var</span> server = http.createServer();
<span class="hljs-keyword">var</span> qs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'querystring'</span>);
 
server.on(<span class="hljs-string">'request'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res</span>) </span>&#123;
    <span class="hljs-keyword">var</span> postData = <span class="hljs-string">''</span>;
 
    <span class="hljs-comment">// 数据块接收中</span>
    req.addListener(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">chunk</span>) </span>&#123;
        postData += chunk;
    &#125;);
 
    <span class="hljs-comment">// 数据接收完毕</span>
    req.addListener(<span class="hljs-string">'end'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        postData = qs.parse(postData);
 
        <span class="hljs-comment">// 跨域后台设置</span>
        res.writeHead(<span class="hljs-number">200</span>, &#123;
            <span class="hljs-string">'Access-Control-Allow-Credentials'</span>: <span class="hljs-string">'true'</span>,     <span class="hljs-comment">// 后端允许发送Cookie</span>
            <span class="hljs-string">'Access-Control-Allow-Origin'</span>: <span class="hljs-string">'http://www.domain1.com'</span>,    <span class="hljs-comment">// 允许访问的域（协议+域名+端口）</span>
            <span class="hljs-comment">/* 
             * 此处设置的cookie还是domain2的而非domain1，因为后端也不能跨域写cookie(nginx反向代理可以实现)，
             * 但只要domain2中写入一次cookie认证，后面的跨域接口都能从domain2中获取cookie，从而实现所有的接口都能跨域访问
             */</span>
            <span class="hljs-string">'Set-Cookie'</span>: <span class="hljs-string">'l=a123456;Path=/;Domain=www.domain2.com;HttpOnly'</span>  <span class="hljs-comment">// HttpOnly的作用是让js无法读取cookie</span>
        &#125;);
 
        res.write(<span class="hljs-built_in">JSON</span>.stringify(postData));
        res.end();
    &#125;);
&#125;);
server.listen(<span class="hljs-string">'8080'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考链接：
<a href="https://blog.csdn.net/qq_38128179/article/details/84956552" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/qq_38128179…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            