
---
title: 'ajax 基础巩固'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a04360d5ffc7485fa3d3fe10824a4774~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 23:39:49 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a04360d5ffc7485fa3d3fe10824a4774~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>这是我参与新手入门的第二篇文章，记录一下ajax的基础使用方法，方便以后温故知新。</p>
<ul>
<li>ajax 基础</li>
<li>Promise + ajax 备忘</li>
</ul>
<h2 data-id="heading-1">一、ajax 基础</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fajax%2Fajax-tutorial.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/ajax/ajax-tutorial.html" ref="nofollow noopener noreferrer">文档链接 菜鸟</a>
/
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FGuide%2FAJAX" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/Guide/AJAX" ref="nofollow noopener noreferrer">文档链接 MDN</a></p>
<h3 data-id="heading-2">AJAX 简介</h3>
<blockquote>
<p>AJAX是异步的JavaScript和XML（Asynchronous JavaScript And XML）。简单点说，就是使用 XMLHttpRequest 对象与服务器通信。 它可以使用JSON，XML，HTML和text文本等格式发送和接收数据。AJAX最吸引人的就是它的“异步”特性，也就是说它可以在不重新刷新页面的情况下与服务器通信，交换数据，或更新页面。</p>
</blockquote>
<h3 data-id="heading-3">Step 1 - 怎样发送http请求</h3>
<p>流程大致可以分为三个步骤：</p>
<ol>
<li>发送一个http请求。</li>
<li>收到响应后，告诉XMLHttp请求对象是哪个js函数来处理响应，当请求状态改变时就调用该函数。</li>
<li>发送一个实际的请求，通过调用HTTP请求对象的 open() 和 send() 方法。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">  (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-comment">// 创建 XMLHttpRequest对象 用于在后台与服务器交换数据 （1.发送一个http请求）</span>
      <span class="hljs-keyword">var</span> httpRequest;

      <span class="hljs-comment">// 为了应对所有的现代浏览器，包括 IE5 和 IE6，请检查浏览器是否支持 XMLHttpRequest 对象</span>
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">window</span>.XMLHttpRequest)&#123;
        <span class="hljs-comment">//  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码</span>
        httpRequest = <span class="hljs-keyword">new</span> XMLHttpRequest();
      &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-comment">// IE6, IE5 浏览器执行代码</span>
        httpRequest = <span class="hljs-keyword">new</span> ActiveXObject(<span class="hljs-string">"Microsoft.XMLHTTP"</span>);
      &#125;
      
      <span class="hljs-comment">// 当您使用 async=false 时，请不要编写 onreadystatechange 函数，将 open() 方法中的第三个参数改为 false 即可。</span>
      <span class="hljs-comment">// 当使用 async=true 时，请规定在响应处于 onreadystatechange 事件中的就绪状态时执行的函数</span>
      <span class="hljs-comment">// 2.发送一个请求后，你会收到响应。在这一阶段，你要告诉XMLHttp请求对象是由哪一个JavaScript函数处理响应，在设置了对象的 onreadystatechange 属性后给他命名，当请求状态改变时调用函数。</span>
      httpRequest.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">if</span>(httpRequest.readyState === <span class="hljs-number">4</span>)&#123;
          <span class="hljs-keyword">if</span>(httpRequest.status === <span class="hljs-number">200</span>)&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"请求成功"</span>,httpRequest.responseText);
          &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"发生错误"</span>,httpRequest.status);
          &#125;
        &#125;
      &#125;
      
      <span class="hljs-comment">// 3.接下来，声明当你接到响应后要做什么，你要发送一个实际的请求，通过调用HTTP请求对象的 open() 和 send() 方法，像下面这样:</span>

      <span class="hljs-comment">// 规定请求的类型、URL 以及是否异步处理请求。</span>
      <span class="hljs-comment">// GET 演示</span>
      <span class="hljs-comment">// httpRequest.open("GET","/try/ajax/demo_get2.php?fname=Henry&lname=Ford",true);</span>
      <span class="hljs-comment">// httpRequest.send(); </span>

      <span class="hljs-comment">// POST 演示</span>
      httpRequest.open(<span class="hljs-string">"POST"</span>,<span class="hljs-string">"/try/ajax/demo_post2.php"</span>,<span class="hljs-literal">true</span>);
      httpRequest.setRequestHeader(<span class="hljs-string">"Content-type"</span>,<span class="hljs-string">"application/x-www-form-urlencoded"</span>); <span class="hljs-comment">// 如果你使用 POST 数据，那就需要设置请求的MIME类型。</span>
      httpRequest.send(<span class="hljs-string">"fname=Henry&lname=Ford"</span>);
      
    &#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Step 2 - 处理服务器响应</h3>
<p>在发送请求时，你提供的JavaScript函数负责处理响应。这个函数应该做什么？</p>
<ul>
<li>首先，函数要检查请求的状态（httpRequest.readyState === 4）。</li>
<li>然后，检查HTTP响应码（httpRequest.status === 200）。</li>
</ul>
<p>在检查完请求状态和HTTP响应码后，就可以用服务器返回的数据做任何你想做的了。有两个方法去访问这些数据：</p>
<ul>
<li>httpRequest.responseText – 服务器以文本字符的形式返回</li>
<li>httpRequest.responseXML – 以 XMLDocument 对象方式返回，之后就可以使用JavaScript来处理</li>
</ul>
<p>注意上面这一步只在你发起异步请求时有效（即 open() 的第三个参数未特别指定或设为 true）。如果你你发起的是同步请求则不必使用函数，但是非常不推荐这样子做，它的用户体验很糟糕。</p>
<h4 data-id="heading-5">onreadystatechange 事件</h4>
<blockquote>
<p>当请求被发送到服务器时，我们需要执行一些基于响应的任务。每当 readyState 改变时，就会触发 onreadystatechange 事件。readyState 属性存有 XMLHttpRequest 的状态信息。</p>
</blockquote>
<p>下面是 XMLHttpRequest 对象的三个重要的属性：</p>
<ol>
<li>
<p>onreadystatechange</p>
<ul>
<li>存储函数（或函数名），每当 readyState 属性改变时，就会调用该函数。</li>
</ul>
</li>
<li>
<p>readyState - 存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。</p>
<ul>
<li>0： (未初始化) or (<strong>请求还未初始化</strong>)</li>
<li>1： (正在加载) or (<strong>已建立服务器链接</strong>)</li>
<li>2： (加载成功) or (<strong>请求已接受</strong>)</li>
<li>3： (交互) or (<strong>正在处理请求</strong>)</li>
<li>4： (完成) or (<strong>请求已完成并且响应已准备好</strong>)</li>
</ul>
</li>
<li>
<p>status</p>
<ul>
<li>200："OK"</li>
<li>404：未找到页面</li>
</ul>
</li>
</ol>
<p>在 onreadystatechange 事件中，规定当服务器响应已做好被处理的准备时所执行的任务。
当 readyState 等于 4 且状态为 200 时，表示响应已就绪。</p>
<h2 data-id="heading-6">二、 Promise + ajax 备忘</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fpromise" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/promise" ref="nofollow noopener noreferrer">参考链接</a>
/
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjs%2Fjs-promise.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/js/js-promise.html" ref="nofollow noopener noreferrer">文档链接</a></p>
<h3 data-id="heading-7">Promise 简介</h3>
<blockquote>
<p>所谓Promise，简单说就是一个容器，里面保存着某个未来才会结束的事件（通常是一个异步操作）的结果。从语法上说，Promise 是一个对象，从它可以获取异步操作的消息。</p>
</blockquote>
<p>Promise 构造函数只有一个参数，是一个函数，这个函数在构造之后会直接被异步运行，所以我们称之为起始函数。起始函数包含两个参数 resolve 和 reject。</p>
<p>当 Promise 被构造时，起始函数会被异步执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Run"</span>);
&#125;);
<span class="hljs-comment">// 直接输出 Run</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>resolve 和 reject 都是函数，其中调用 resolve 代表一切正常，reject 是出现异常时所调用的</p>
<p>Promise 类有 .then() .catch() 和 .finally() 三个方法，这三个方法的参数都是一个函数。</p>
<ul>
<li>.then() 可以将参数中的函数添加到当前 Promise 的正常执行序列。</li>
<li>.catch() 则是设定 Promise 的异常处理序列。</li>
<li>.finally() 是在 Promise 执行的最后一定会执行的序列。</li>
</ul>
<p>.then() 传入的函数会按顺序依次执行，有任何异常都会直接跳到 catch 序列。</p>
<p>resolve() 中可以放置一个参数用于向下一个 then 传递一个值，then 中的函数也可以返回一个值传递给 then。但是，如果 then 中返回的是一个 Promise 对象，那么下一个 then 将相当于对这个返回的 Promise 进行操作。</p>
<p>reject() 参数中一般会传递一个异常给之后的 catch 函数用于处理异常。</p>
<p>请注意以下两点：</p>
<ul>
<li>resolve 和 reject 的作用域只有起始函数，不包括 then 以及其他序列；</li>
<li>resolve 和 reject 并不能够使起始函数停止运行，别忘了 return。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a04360d5ffc7485fa3d3fe10824a4774~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210706160855.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">使用案例</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fpromise" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/promise" ref="nofollow noopener noreferrer">案例来源</a></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> getJSON = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">url</span>)</span>&#123;
    <span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve,reject</span>)</span>&#123;

      <span class="hljs-keyword">const</span> handler = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.readyState !==<span class="hljs-number">4</span>)&#123;
          <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === <span class="hljs-number">200</span>)&#123;
          resolve(<span class="hljs-built_in">this</span>.response)
        &#125;<span class="hljs-keyword">else</span>&#123;
          reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-built_in">this</span>.statusText))
        &#125;
      &#125;;

      <span class="hljs-keyword">const</span> xmlHttp = <span class="hljs-keyword">new</span> XMLHttpRequest();

      xmlHttp.open(<span class="hljs-string">"GET"</span>,url);
      xmlHttp.onreadystatechange = handler;
      xmlHttp.responseType = <span class="hljs-string">"json"</span>;
      xmlHttp.setRequestHeader(<span class="hljs-string">"Accept"</span>,<span class="hljs-string">"application/json"</span>);
      xmlHttp.send();

    &#125;);

    <span class="hljs-keyword">return</span> promise;
  &#125;;


  getJSON(<span class="hljs-string">"/test.json"</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">json</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"请求成功"</span>,json)
  &#125;,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"发生错误"</span>,error)
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">总结</h2>
<p>ajax基础本身不难，可能因为有各种好用的插件，所以一直记不住具体的参数和流程。</p>
<p>我一直觉得基础知识才是王道，一步步往上走的时候，台阶也要修的牢固，但是本身记性也不太好，学了不用，必定是会忘记的，所以记录和分享也是一种好习惯吧，希望自己能够温故而知新，学习新技术的时候，也不要忘记底层技术。</p>
<p>离抱枕又进了一步，加油，冲！</p></div>  
</div>
            