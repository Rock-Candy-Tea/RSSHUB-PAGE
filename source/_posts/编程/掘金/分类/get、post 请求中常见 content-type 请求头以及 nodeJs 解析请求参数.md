
---
title: 'get、post 请求中常见 content-type 请求头以及 nodeJs 解析请求参数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72c64cb1220643038a24c70eeb93b52e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 03:23:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72c64cb1220643038a24c70eeb93b52e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">form 标签的 enctype 属性的定义和用法</h2>
<p><code>enctype</code> 属性规定在发送到服务器之前应该如何对表单数据进行编码。
默认地，表单数据会编码为 <code>application/x-www-form-urlencoded</code>。就是说，在发送到服务器之前，所有字符都会进行编码（空格转换为 "+" 加号，特殊符号转换为 ASCII HEX 值）</p>





















<table><thead><tr><th>值</th><th>描述</th></tr></thead><tbody><tr><td>application/x-www-form-urlencoded</td><td>在发送前编码所有字符（默认）</td></tr><tr><td>multipart/form-data</td><td>不对字符编码，<br>在使用包含文件上传控件的表单时，必须使用该值</td></tr><tr><td>text/plain</td><td>空格转换为 "+" 加号，但不对特殊字符编码</td></tr></tbody></table>
<blockquote>
<p><code>HTTP/1.1</code> 协议规定的 HTTP 请求方法有 OPTIONS、GET、HEAD、POST、PUT、DELETE、TRACE、CONNECT 这几种。</p>
</blockquote>
<p>其中 POST 一般用来向服务端提交数据, GET 一般用来从指定的资源请求数据。<br>
本文主要讨论 POST 提交数据的几种方式及GET请求</p>
<h2 data-id="heading-1">HTTP 协议数据格式</h2>
<p>HTTP 协议是以 ASCII 码传输，建立在 TCP/IP 协议之上的应用层规范。
规范把 HTTP 请求分为三个部分：状态行、请求头、消息主体。结构类似如下：</p>
<pre><code class="copyable"><method> <request-URL> <version>
<headers>

<entity-body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>协议规定 POST 提交的数据必须放在消息主体（entity-body）中，但协议并没有规定数据必须使用什么编码方式。实际上，开发者完全可以自己决定消息主体的格式，只要最后发送的 HTTP 请求满足上面的格式就可以。</p>
<p>但是，数据发送出去，还要服务端解析成功才有意义。一般服务端语言如 php、python 等，以及它们的 framework，都内置了自动解析常见数据格式的功能。
服务端通常是根据请求头（headers）中的 Content-Type 字段来获知请求中的消息主体是用何种方式编码，再对主体进行解析。</p>
<p>所以说到 POST 提交数据方案，包含了 Content-Type 和消息主体编码方式两部分。</p>
<h2 data-id="heading-2">演示代码准备</h2>
<p>这里我们基于 <code>node Express</code> 库搭建一个简单的服务器，用来解析页面发起的各种类型请求</p>
<p>环境要求：安装 <code>nodeJs</code>, 安装 web 服务启动工具 <code>npm install -g serve</code></p>
<p>目录结构</p>
<pre><code class="copyable">|____form-get
| |____index.html // get 请求 demo
|____index.html // web 服务入口文件
|____.gitignore
|____package-lock.json
|____package.json
|____form-data
| |____index.html // content-type => form-data 请求 demo
|____application-json
| |____index.html // content-type => application-json 请求 demo
|____form-urlencode
| |____index.html // content-type => application/x-www-form-urlencoded 请求 demo
| |____serve.js // node 服务
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>serve.js</code> 创建服务 监听本地 <code>3111</code> 端口</p>
<pre><code class="copyable">const express = require('express')
const app = express()
const port = 3111
app.listen(port, () => &#123;
  console.log(`Started at port $&#123;port&#125;`)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>切换到当前目录</p>
<p>启动 web 服务 <code>serve</code>, 默认会启用 <code>5000</code> 端口，浏览器访问 <code>localhost:5000</code></p>
<p>安装 npm 包依赖 <code>npm i</code></p>
<p>启动 node 服务 <code>node serve.js</code></p>
<h2 data-id="heading-3">application/x-www-form-urlencoded</h2>
<p>这应该是最常见的 POST 提交数据的方式了。浏览器的原生 <code><form></code> 表单，如果不设置 enctype 属性，那么最终就会以 <code>application/x-www-form-urlencoded</code> 方式提交数据</p>
<p><code>form-urlencode/index.html</code></p>
<pre><code class="copyable">  <!-- 注意必须是 post 请求 -->
  <form action="http://localhost:3111/form-urlencode" method="post" enctype="application/x-www-form-urlencoded">
    <p>First name: <input type="text" name="fname" /></p>
    <p>Last name: <input type="text" name="lname" /></p>
    <input type="submit" value="Submit" />
  </form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器访问 <code>localhost:5000/form-urlencode/index.html</code>并填写表单，点击<code>Submit</code>按钮</p>
<p><img alt="图示" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72c64cb1220643038a24c70eeb93b52e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>serve.js</code> 处理<code>/form-urlencode</code>请求的代码【示例给到的回包均为 JSON 格式】</p>
<pre><code class="copyable">const bodyParser = require('body-parser')

// 用来解析 form-urlencode body
const urlencodedParser = bodyParser.urlencoded(&#123; extended: false &#125;)

app.post('/form-urlencode', urlencodedParser, function (req, res) &#123;
  console.log('get application/x-www-form-urlencoded Params: ', req.body)
  res.json(&#123; result: 'success', data: req.body &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时Form提交的请求数据，抓包时看到的请求的 <code>Content-Type</code> 请求头值是<code>application/x-www-form-urlencoded</code></p>
<p>提交的数据按照 <code>key1=val1&key2=val2</code> 的方式进行编码，key 和 val 都进行了 URL 转码, 点击下图 <code>Form data</code> 旁边的 <code>view source</code> 即可看到效果 <code>fname=Jack&lname=Chan</code></p>
<p>表单提交的响应结果</p>
<p><img alt="图示" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec0ae250ad34fceb45eeaa8a97b83e3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果用 Ajax 代替 Form 提交数据，也是使用这种方式。
<code>Content-Type</code> 默认值都是<code>application/x-www-form-urlencoded;charset=utf-8</code></p>
<h2 data-id="heading-4">multipart/form-data</h2>
<p>这又是一个常见的 POST 数据提交的方式。我们使用表单上传文件时，必须让 </p> 表单的enctype 等于 <code>multipart/form-data</code>。<p></p>
<p><code>form-data/index.html</code></p>
<pre><code class="copyable">  <!-- js中通过 new FormData() 发送数据 表单中通过以下demo -->
  <form action="http://localhost:3111/form-data" method="post" enctype="multipart/form-data">
    <p>name: <input type="text" name="name" /></p>
    <p>age : <input type="number" name="age" /></p>
    <input type="submit" value="Submit" />
  </form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器访问 <code>localhost:5000/form-data/index.html</code>并填写表单，点击<code>Submit</code>按钮</p>
<p><img alt="图示" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/295854de70d24d428dc2801464bd096c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>serve.js</code> 处理<code>/form-data</code>请求的代码【示例给到的回包均为 JSON 格式】</p>
<pre><code class="copyable">const multipart = require('connect-multiparty')

// 用来解析 form-data body
const multipartMiddleware = multipart()

app.post('/form-data', multipartMiddleware, function (req, res) &#123;
  console.log('get application/form-data Params: ', req.body)
  res.json(&#123; result: 'success', data: req.body &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表单提交的响应结果</p>
<p><img alt="图示" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae3e69b77675494c9932f5026287512a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>此时Form提交的请求数据，抓包时看到的请求的 <code>Content-Type</code> 请求头值是<code>multipart/form-data</code></p>
<p>而且可以看到上图请求的<code>form data</code>：</p>
<pre><code class="copyable">------WebKitFormBoundaryTPENO2DooTSePmIO
Content-Disposition: form-data; name="name"

Jack
------WebKitFormBoundaryTPENO2DooTSePmIO
Content-Disposition: form-data; name="age"

30
------WebKitFormBoundaryTPENO2DooTSePmIO--
<span class="copy-code-btn">复制代码</span></code></pre>
<p>格式说明：</p>
<p>首先生成了一个 <code>boundary</code> 用于分割不同的字段，为了避免与正文内容重复，<code>boundary</code> 很长很复杂。</p>
<p>然后 <code>Content-Type</code> 里指明了数据是以 <code>multipart/form-data</code> 来编码，本次请求的 <code>boundary</code> 是什么内容。消息主体里按照字段个数又分为多个结构类似的部分，每部分都是以 <code>--boundary</code> 开始，紧接着是内容描述信息</p>
<p>然后是回车，最后是字段具体内容（文本或二进制）。如果传输的是文件，还要包含文件名和文件类型信息。消息主体最后以 <code>--boundary--</code> 标示结束。</p>
<p>关于 <code>multipart/form-data</code> 的详细定义，请前往 <a href="https://www.ietf.org/rfc/rfc1867.txt" target="_blank" rel="nofollow noopener noreferrer">rfc1867</a> 查看</p>
<blockquote>
<p><strong>上面提到的这两种 POST 数据的方式，都是浏览器原生支持的，而且现阶段标准中原生  表单也只支持这两种方式（通过  元素的 enctype 属性指定，默认为 application/x-www-form-urlencoded。 enctype 还支持 text/plain，不过用得非常少）</strong></p>
</blockquote>
<h2 data-id="heading-5">application/json</h2>
<p><code>application/json</code> 这个 <code>Content-Type</code> 现在越来越多的人把它作为请求头，用来告诉服务端消息主体是序列化后的 JSON 字符串。</p>
<p>由于 JSON 规范的流行，除了低版本 IE 之外的各大浏览器都原生支持<code>JSON.stringify</code>，服务端语言也都有处理 JSON 的函数，使用 JSON 不会遇上什么麻烦。</p>
<p><code>form-data/application-json.html</code></p>
<pre><code class="copyable">  <!-- html -->
  <p>First name: <input type="text" name="fname" /></p>
  <p>Last name: <input type="text" name="lname" /></p>
  <button onclick="submit()">Submit</button>
  <br>
  <p>
    返回结果：
    <p style="color:red" id="result"></p>
  </p>
  
  <!-- script -->
  <script>
    submit = function () &#123;
      var fname = document.getElementsByName('fname')[0].value  //用户输入的 fname
      var lname = document.getElementsByName('lname')[0].value  //用户输入的 lname
      var xhr = new XMLHttpRequest()
      // 使用HTTP POST请求与服务器交互数据
      xhr.open("POST", "http://localhost:3111/application-json", true)
      // 设置发送数据的请求格式 application/json
      xhr.setRequestHeader('content-type', 'application/json')
      xhr.onreadystatechange = function () &#123;
        if (xhr.readyState == 4) &#123;
          document.getElementById('result').innerHTML=JSON.stringify(JSON.parse(xhr.responseText))
          console.log()
        &#125;
      &#125;
      var sendData = &#123; fname, lname &#125;
      //将用户输入值序列化成字符串
      xhr.send(JSON.stringify(sendData))
    &#125;
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器访问 <code>localhost:5000/application-json/index.html</code>并填写表单，点击<code>Submit</code>按钮，得到的回包内容在如图红色箭头处渲染出来</p>
<p><img alt="图示" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f203cedc308244269741e5bc185d2769~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>serve.js</code> 处理<code>/application-json</code>请求的代码【示例给到的回包均为 JSON 格式】</p>
<pre><code class="copyable">const bodyParser = require('body-parser')

// 用来解析 application-json body
const jsonParser = bodyParser.json(&#123;extended: false&#125;)

/** application-json 数据类型接口演示 */
app.post('/application-json', jsonParser, function (req, res) &#123;
  console.log('get application-json Params: ', req.body)
  res.json(&#123; result: '您发送的数据是：', data: req.body &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时接口提交的请求数据，抓包时看到的请求的 <code>Content-Type</code> 请求头值是<code>application/json</code>，并且我们把回包内容以红色文本形式渲染在页面上</p>
<p>表单提交的响应结果</p>
<p><img alt="图示" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b752d702dec400199a98c1e9c0906f6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>application-json</code> 类型可以方便的提交复杂的结构化数据，很适合 <code>RESTful</code> 的接口。各大抓包工具如 Chrome 自带的开发者工具、Fiddler、Charles，都会以树形结构展示 JSON 数据，非常友好。</p>
<h2 data-id="heading-6">GET 接口</h2>
<p>最后附上 get 接口，这样基本上覆盖日常开发的90%以上的接口类型了</p>
<p>请求发起方式我们采用表单形式</p>
<blockquote>
<p>Get 方法是不含“body”的，它的请求参数都会被编码到url后面，所以在 Get 方法中加 Content-type 是无用的</p>
</blockquote>
<p><code>form-get/index.html</code></p>
<pre><code class="copyable">  <form action="http://localhost:3111/get" method="get">
    <p>name: <input type="text" name="name" /></p>
    <p>age : <input type="number" name="age" /></p>
    <input type="submit" value="Submit - get" />
  </form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>填写表单，提交</p>
<p><img alt="图示" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/483daad2e94748b9b7e0231c92a98a38~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>serve.js</code> 接口响应也很简单，直接取<code>req.query</code>即可，无需任何中间件</p>
<pre><code class="copyable">app.get('/get', function (req, res) &#123;
  console.log('get Params: ', req.query)
  res.json(&#123; result: '您发送的数据是：', data: req.query &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表单提交的响应结果</p>
<p><img alt="图示" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5f8a20d079d49c2abab331bd659288e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到，get 参数通过 url 传递，直接拼接在 query 参数中，请求头中也没有<code>Content-type</code></p>
<h2 data-id="heading-7">福利 GET - POST 的 区别</h2>
<pre><code class="copyable">get 参数通过 url 传递，post 放在 request body 中。 
get 请求在 url 中传递的参数是有长度限制的，而 post 没有。 
get 比 post 更不安全，因为参数直接暴露在 url 中，所以不能用来传递敏感信息。 
get 请求只能进行 url 编码，而 post 支持多种编码方式。
get 请求会浏览器主动 cache，而 post 支持多种编码方式。 
get 请求参数会被完整保留在浏览历史记录里，而 post 中的参数不会被保留。 

GET 和 POST 本质上就是 TCP 链接，并无差别。但是由于 HTTP 的规定和浏览器/服务器 的限制，导致他们在应用过程中体现出一些不同。 

GET 产生一个 TCP 数据包；POST 产生两个 TCP 数据包。
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>看到这里，是不是觉得日常业务接口类型也就这些，无非就是在做一些数据库的CRUD操作，so，前后端一起搞起来吧~~</p>
<hr>
<p><em>参考：<a href="https://www.cnblogs.com/mmzuo-798/p/11634055.html" target="_blank" rel="nofollow noopener noreferrer">post请求头中常见content-type</a></em></p>
<p>demo源码：<a href="https://github.com/melunar/proj02/tree/master/nodejs/server/content-type" target="_blank" rel="nofollow noopener noreferrer">github.com/melunar</a></p>
<hr>
<p><strong>更多关于我</strong></p>
<ul>
<li>💻<a href="http://blog.lalapkp.cn/" target="_blank" rel="nofollow noopener noreferrer">博客</a></li>
<li>🐱<a href="https://github.com/melunar" target="_blank" rel="nofollow noopener noreferrer">Github</a></li>
<li>🔨<a href="https://juejin.cn/user/2612095355979405" target="_blank">掘金</a></li>
<li>👱<a href="http://www.lalapkp.cn/about" target="_blank" rel="nofollow noopener noreferrer">关于我</a></li>
<li>🐒<a href="https://blog.csdn.net/Haoyong110?spm=1000.2115.3001.5343&type=1" target="_blank" rel="nofollow noopener noreferrer">CSDN</a></li>
</ul>
<p><strong>微信公众号</strong><br>
<a href="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7981f683c1fe4ac784d0fcea660510fe~tplv-k3u1fbpfcp-zoom-1.image" target="_blank" rel="nofollow noopener noreferrer">代表moon</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            