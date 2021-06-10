
---
title: 'AJAX'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcd8a8c99dd549dca65db80e9cd52a7a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 02:49:06 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcd8a8c99dd549dca65db80e9cd52a7a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">同步交互和异步交互</h1>
<p>所谓同步交互就是指当客户端向服务端和数据库发送数据之后，若要发送下一个请求需要等待服务端和数据库的响应结果。这就好比数据结构中的队列，一个执行完毕在执行下一个。也类似一些面向过程语言的代码执行顺序。</p>
<p>而异步交互就是指客户端向服务端发送数据之后，无需等待服务端和数据库的响应结果，就可以发送下一个请求。</p>
<p>如下图说明了同步交互和异步交互的区别：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcd8a8c99dd549dca65db80e9cd52a7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
异步交互与同步交互的劣势：</p>
<ul>
<li>破坏了浏览器的前进和后退机制</li>
<li>后面逻辑依靠前面逻辑时，可能会出现问题</li>
<li>Ajax 对搜索引擎支持较弱</li>
<li>容易引起 web 安全问题</li>
</ul>
<h1 data-id="heading-1">Ajax 是什么</h1>
<p>Ajax 全称 “Asynchronous JavaScript and XML” 被译为：异步 JavaScript 和 XML。</p>
<p>虽然 Ajax 中的 x 代表 XML，但是现在 JSON 的诸多优势 JSON 的使用比 XML 更加普遍。</p>
<p>JSON 和 XML 都用于在 Ajax 模型中封装数据</p>
<h2 data-id="heading-2">Ajax 涉及的技术</h2>
<p>Ajax 并不是一个新技术，而是多个技术的整合：</p>
<ul>
<li>HTML</li>
<li>CSS</li>
<li>JavaScript</li>
<li>DOM</li>
<li>XML</li>
<li>XMLHttpRequest 对象</li>
</ul>
<p><code>XMLHttpRequest</code> 是 Ajax 的核心。</p>
<p><code>XMLHttpRequest</code> 对象提供了在客户端和服务端传输数据的功能，<code>XMLHttpRequest</code> 对象提供了通过 URL 方式来获取数据，只更新网页的一部分数据。</p>
<h2 data-id="heading-3">实现 Ajax 的步骤</h2>
<ul>
<li>创建 Ajax 核心对象（XMLHttpRequest）</li>
<li>通过 Ajax 核心对象的 <code>open()</code> 方法建立与服务端的链接</li>
<li>构建请求的数据内容，通过核心对象的 <code>send()</code> 方法发送给服务端</li>
<li>通过核心对象提供的 <code>onreadystatechange</code> 事件，监听服务端的通信状态</li>
<li>接受处理服务端响应的结果</li>
<li>将结果更新到页面</li>
</ul>
<h2 data-id="heading-4">创建 XMLHttpRequest 对象</h2>
<p>由于创建 Ajax 对象的方式在浏览器之间存在不同的情况所以需要编写一个自定义 js 文件来实现浏览器兼容。
主要兼容的是 IE 浏览器。</p>
<p>在其他非 IE 的主流浏览器中创建 Ajax 对象的方法为：<code>new XMLHttpRequest()</code>，
而在 IE 中又分为两种情况：</p>
<p>IE7 版本：<code>new ActiveXObject("Msxml2.XMLHTTP")</code>
IE6 及以下版本：<code>new ActiveXObject("Microsoft.XMLHTTP")</code>
Tools.js 文件如下：</p>
<pre><code class="copyable">Object.defineProperty(window, "createXMLHttpRequest", &#123;
  value: function () &#123;
    var httpRequest;
    // 如果是非IE浏览器
    if (window.XMLHttpRequest) &#123;
      httpRequest = new XMLHttpRequest();
    &#125;
    // 如果是 IE 浏览器
    else if (window.ActiveXObject) &#123;
      try &#123;
        // IE 7+
        httpRequest = new ActiveXObject("Msxml2.XMLHTTP");
      &#125; catch (e) &#123;
        try &#123;
          // IE 6-
          httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
        &#125; catch (e) &#123;&#125;
      &#125;
    &#125;
    return httpRequest;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 HTML 页面中引入之前创建的 Tools.js 文件，然后调用 <code>createXMLHttpRequest</code> 方法进行创建即可。</p>
<p>如下代码：</p>
<pre><code class="copyable">var ajax = createXMLHttpRequest();
console.log(ajax);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回的结果为一个 <code>XMLHttpRequest</code> 对象。</p>
<h2 data-id="heading-5">实现 Ajax 异步交互</h2>
<p>接下来模拟发请求和获取响应数据的过程，还是依照上面的过程</p>
<blockquote>
<p>以下 XHR 均代表 XMLHttpRequest</p>
</blockquote>
<ul>
<li>创建 <code>XHR</code> 对象</li>
<li>调用 <code>XHR</code> 对象的 <code>open()</code> 方法</li>
<li>调用 <code>XHR</code> 对象的 <code>send()</code> 方法</li>
<li>调用 <code>onreadystatechange</code> 监听服务端通信状态</li>
<li>使用 <code>readyState</code> 属性判断服务端响应状态</li>
</ul>
<h3 data-id="heading-6"><code>open()</code> 方法</h3>
<p><code>open()</code> 方法语法结构：</p>
<p><code>open(method, url[, async, user, password])</code></p>
<p>参数说明：</p>
<ul>
<li>method：请求方法，get、post、put、delete 等</li>
<li>url：发送请求的 url</li>
<li>async：是否异步交互</li>
<li>user：用户名用于认证用途</li>
<li>password：用户密码</li>
</ul>
<h3 data-id="heading-7"><code>send()</code> 方法</h3>
<p>在调用 <code>send()</code> 方法时，用于发送数据，默认为异步发送，发送后立即返回；
若为同步发送等待响应后返回。<code>send</code> 方法不传入参数代表不发送数据，当请求方式为 <code>get</code>、<code>head</code> 时需要将主体设置为 <code>null</code>。</p>
<h3 data-id="heading-8"><code>readyState</code> 属性</h3>
<p><code>XHR</code> 对象的 <code>readyState</code> 属性返回值：</p>
<ul>
<li>0：XHR 被初始化，未调用 open 方法</li>
<li>1：XHR 调用 open</li>
<li>2：XHR 调用 send</li>
<li>3：下载中</li>
<li>4：下载完成</li>
</ul>
<p>当 <code>readyState</code> 属性放在 <code>open()</code> 之下和 <code>send()</code> 之下时，返回的结果都为 2,3,4；</p>
<p>当放在 <code>open()</code> 之上 <code>createXMLHttpRequest</code> 之下时，返回 1,2,3,4</p>
<h3 data-id="heading-9"><code>responseText</code> 属性</h3>
<p><code>XHR</code> 对象的 <code>responseText</code> 属性接受服务端对该请求的响应结果。</p>
<h3 data-id="heading-10"><code>status</code> 属性</h3>
<p><code>XHR</code> 的 <code>status</code> 属性返回当前服务端状态响应码，常见的状态响应码如下：</p>
<ul>
<li>200：请求成功</li>
<li>304：请求的资源伪未变化（没有改动）</li>
<li>404：服务器端地址未找到</li>
</ul>
<p>对于对于上面写法如果对 <code>open()</code> 方法写入的服务端地址不正确则返回一个 404 报错，如果请求正确则返回 200。</p>
<h3 data-id="heading-11">get 请求方式</h3>
<p>通过表单提交的数据，如果是 <code>get</code> 方式提交的数据会在地址栏上进行显示。</p>
<p>在 Ajax 提交方式中如果使用 <code>get</code> 或者 <code>head</code> 方式提交数据时，<code>send</code> 方法中只能写入 <code>null</code>。</p>
<p>若要提交数据需要在对服务器的请求网址中输入相应的参数。如下代码所示：</p>
<pre><code class="copyable"><body>
  <button id="btn">按钮</button>
  <script src="./myTools.js"></script>
  <script>
    var btn = document.getElementById("btn");
    btn.addEventListener("click", function () &#123;
      var xhr = createXMLHttpRequest();
      xhr.open(
        "get",
        "http://localhost:63343/ricardo/Ajax/%E4%BB%A3%E7%A0%81/%E6%B5%8B%E8%AF%95xhr.html?_ijt=22k61vqrrkstdjmlf6eo3ug8iu?user=hello#"
      );
      xhr.send(null);
    &#125;);
  </script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>get 请求方式会直接在地址栏中追加数据。</p>
<h3 data-id="heading-12">POST 请求方式</h3>
<p>在使用 POST 发送请求时，可以写在 <code>XHR</code> 中的 <code>send()</code> 方法中。
如下代码所示：</p>
<pre><code class="copyable"><body>
  <button id="btn">按钮</button>
  <script src="./myTools.js"></script>
  <script>
    var btn = document.getElementById("btn");
    btn.addEventListener("click", function () &#123;
      var xhr = createXMLHttpRequest();
      xhr.open(
        "post",
        "http://localhost:63343/ricardo/Ajax/%E4%BB%A3%E7%A0%81/%E6%B5%8B%E8%AF%95xhr.html?_ijt=3b3upkr00lb4gtto8n5tb2o21u"
      );
      xhr.send("user=zhang&pwd=1234");
    &#125;);
  </script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4012e5a08dd444de8731802400a355cc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在使用 <code>POST</code> 方式发送请求之前需要先使用 <code>XHR</code> 对象的 <code>setRequestHeader()</code> 方法设置请求头部信息。
如下代码所示：</p>
<pre><code class="copyable">var btn = document.getElementById("btn");
btn.addEventListener("click", function () &#123;
  var xhr = createXMLHttpRequest();
  xhr.open(
    "post",
    "http://localhost:63343/ricardo/Ajax/%E4%BB%A3%E7%A0%81/%E6%B5%8B%E8%AF%95xhr.html?_ijt=3b3upkr00lb4gtto8n5tb2o21u"
  );
  // 使用 POST 请求设置请求头部信息
  xhr.setRequestHeader("Content-Type", "application/x-www-for-urlencoded");
  xhr.send("user=zhang&pwd=1234");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当设置了头部信息之后，在浏览器的抓包工具中发现格式为：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6b024192b764b928b160d7c180e1ef1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">server.js-创建一个自己的服务</h2>
<pre><code class="copyable">var http = require('http')
var fs = require('fs')
var url = require('url')
var port = process.argv[2]

if(!port)&#123;
  console.log('请指定端口号好不啦？\nnode server.js 8888 这样不会吗？')
  process.exit(1)
&#125;

var server = http.createServer(function(request, response)&#123;
  var parsedUrl = url.parse(request.url, true)
  var pathWithQuery = request.url 
  var queryString = ''
  if(pathWithQuery.indexOf('?') >= 0)&#123; queryString = pathWithQuery.substring(pathWithQuery.indexOf('?')) &#125;
  var path = parsedUrl.pathname
  var query = parsedUrl.query
  var method = request.method

  /******** 从这里开始看，上面不要看 ************/

  console.log('有个傻子发请求过来啦！路径（带查询参数）为：' + pathWithQuery)

  if(path === '/')&#123;
    response.statusCode = 200
    response.setHeader('Content-Type', 'text/html;charset=utf-8')
    response.write(`二哈`)
    response.end()
  &#125; else if(path === '/x')&#123;
    response.statusCode = 200
    response.setHeader('Content-Type', 'text/css;charset=utf-8')
    response.write(`body&#123;color: red;&#125;`)
    response.end()
  &#125; else &#123;
    response.statusCode = 404
    response.setHeader('Content-Type', 'text/html;charset=utf-8')
    response.write(`你输入的路径不存在对应的内容`)
    response.end()
  &#125;

  /******** 代码结束，下面不要看 ************/
&#125;)

server.listen(port)
console.log('监听 ' + port + ' 成功\n请用在空中转体720度然后用电饭煲打开 http://localhost:' + port)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用node.server.js 8888启动</li>
<li>添加index.html和main.js两个路由</li>
</ul>
<h1 data-id="heading-14">总结</h1>
<ul>
<li>const request = new XMLHttpRequest</li>
<li>request.open("","")
<ul>
<li>request.onload()</li>
<li>request.onerror()</li>
</ul>
</li>
<li>request.onreadystatechange()</li>
<li>request.send()</li>
</ul>
<blockquote>
<p><a href="https://blog.csdn.net/weixin_45499478/article/details/109713381" target="_blank" rel="nofollow noopener noreferrer">参考资料</a></p>
</blockquote></div>  
</div>
            