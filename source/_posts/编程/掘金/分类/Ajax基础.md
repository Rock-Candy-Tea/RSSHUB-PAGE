
---
title: 'Ajax基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6994359562069344286'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 01:28:03 GMT
thumbnail: 'https://juejin.cn/post/6994359562069344286'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<h2 data-id="heading-0">Ajax简介</h2>
</blockquote>
<p>什么是Ajax</p>
<ul>
<li>Ajax===><code>Asynchronous Javascript And XML</code></li>
<li>Ajax 是一个令人误导的名称。Ajax 应用程序可能使用 XML 来传输数据，但将数据作为纯文本或 JSON 文本传输也同样常见。</li>
<li>Ajax 允许通过与场景后面的 Web 服务器交换数据来异步更新网页。这意味着可以更新网页的部分，而不需要重新加载整个页面</li>
</ul>
<p>我们学习Ajax可以干什么</p>
<ul>
<li>可以在不刷新页面更新页面的时候拿到数据</li>
<li>在页面加载后从服务器请求数据</li>
<li>在页面加载后从服务器接收数据</li>
<li>在后台向服务器发送数据</li>
</ul>
<p>Ajax是如何工作的</p>
<p><img alt="image-20210809165344260" src="https://juejin.cn/post/6994359562069344286" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>网页中发送的一个事件(页面加载，按钮点击)</li>
<li>由JavaScript创建XMLHttpRequest对象</li>
<li>XMLHttpRequest对象向web服务器发送请求</li>
<li>服务器处理该请求</li>
<li>服务器将响应发送回网页</li>
<li>由JavaScript读取响应</li>
<li>由JavaScript执行正确的动作，比如更新页面等</li>
</ul>
<blockquote>
<h2 data-id="heading-1">XMLHttpRequest 对象</h2>
</blockquote>
<p>所有现代浏览器都支持 XMLHttpRequest 对象。</p>
<p>XMLHttpRequest 对象用于同幕后服务器交换数据。这意味着可以更新网页的部分，而不需要重新加载整个页面。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-comment"><!--<div>用于显示来自服务器的信息--></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span>
    <span class="hljs-comment"><!-- <button> 调用函数（当它被点击）--></span>
<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>XMLHttpRequest 对象<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"loadDoc()"</span>></span>修改内容<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    loadDoc()
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadDoc</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//实例化ajax请求</span>
        <span class="hljs-keyword">let</span> xhttp=<span class="hljs-keyword">new</span> XMLHttpRequest()
       xhttp.onreadystatechange=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-comment">//判断是否成功，成功的话就执行里面修改内容</span>
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.readyState==<span class="hljs-number">4</span>&&<span class="hljs-built_in">this</span>.statue==<span class="hljs-number">200</span>)&#123;
 <span class="hljs-comment">//修改内容             </span>
                <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'dome'</span>).innerHTML=<span class="hljs-built_in">this</span>.responseText
            &#125;
        &#125;
        <span class="hljs-comment">//xhttp.poen('请求方式','请求地址')</span>
        xhttp.open(<span class="hljs-string">'GET'</span>,<span class="hljs-string">'http://www.liulongbin.top:3006/api/addbooks'</span>)
        xhttp.send()
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h2 data-id="heading-2">XMLHttpRequest 对象方法</h2>
</blockquote>









































<table><thead><tr><th>方法</th><th>描述</th></tr></thead><tbody><tr><td>new XMLHttpRequest()</td><td>创建新的XMLHttpREquest对象</td></tr><tr><td>abort()</td><td>取消当前请求</td></tr><tr><td>getAllResponseHeaders()</td><td>返回头部信息</td></tr><tr><td>getResponseHeader()</td><td>返回特定的头部信息</td></tr><tr><td>open(method,url,async,user,psw)</td><td>规定请求：                 method:请求类型(默认GET)    url:请求的地址        async:true(异步)或false(同步) user:可选的用户名称               psw:可选的密码</td></tr><tr><td>send()</td><td>将请求发送到服务器，用于Get请求</td></tr><tr><td>send(string)</td><td>将请求发送到服务器，用于POST请求</td></tr><tr><td>setRequestHeader()</td><td>向要发送的报头添加标签/键值对</td></tr></tbody></table>
<blockquote>
<h2 data-id="heading-3">XMLHttpRequest 对象属性</h2>
</blockquote>

































<table><thead><tr><th><strong>属性</strong></th><th><strong>描述</strong></th></tr></thead><tbody><tr><td>onreadystatechange</td><td>定义当 readyState 属性发生变化时被调用的函数</td></tr><tr><td>readyState</td><td>保存 XMLHttpRequest 的状态。0：请求未初始化1：服务器连接已建立2：请求已收到3：正在处理请求4：请求已完成且响应已就绪</td></tr><tr><td>responseText</td><td>以字符串返回响应数据</td></tr><tr><td>responseXML</td><td>以 XML 数据返回响应数据</td></tr><tr><td>status</td><td>返回请求的状态号200: "OK"403: "Forbidden"404: "Not Found"</td></tr><tr><td>statusText</td><td>返回状态文本（比如 "OK" 或 "Not Found"）</td></tr></tbody></table>
<blockquote>
<h2 data-id="heading-4">GET请求</h2>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>XMLHttpRequest 对象<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"loadDoc()"</span>></span>请求数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadDoc</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> xhttp = <span class="hljs-keyword">new</span> XMLHttpRequest();
  xhttp.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.readyState == <span class="hljs-number">4</span> && <span class="hljs-built_in">this</span>.status == <span class="hljs-number">200</span>) &#123;
      <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"demo"</span>).innerHTML = <span class="hljs-built_in">this</span>.responseText;
    &#125;
  &#125;;
  xhttp.open(<span class="hljs-string">"GET"</span>, <span class="hljs-string">"/demo/demo_get.asp"</span>, <span class="hljs-literal">true</span>);
  xhttp.send();
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h2 data-id="heading-5">POST请求</h2>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>XMLHttpRequest 对象<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"loadDoc()"</span>></span>请求数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
 
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadDoc</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> xhttp = <span class="hljs-keyword">new</span> XMLHttpRequest();
  xhttp.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.readyState == <span class="hljs-number">4</span> && <span class="hljs-built_in">this</span>.status == <span class="hljs-number">200</span>) &#123;
      <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"demo"</span>).innerHTML = <span class="hljs-built_in">this</span>.responseText;
    &#125;
  &#125;;
  xhttp.open(<span class="hljs-string">"POST"</span>, <span class="hljs-string">"/demo/demo_post2.asp"</span>, <span class="hljs-literal">true</span>);
  xhttp.setRequestHeader(<span class="hljs-string">"Content-type"</span>, <span class="hljs-string">"application/x-www-form-urlencoded"</span>);
  xhttp.send(<span class="hljs-string">"fname=Bill&lname=Gates"</span>);
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            