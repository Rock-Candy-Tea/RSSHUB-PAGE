
---
title: 'axios核心原理分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3213'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 01:50:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=3213'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">axios核心原理分析</h1>
<h2 data-id="heading-1">一、概述</h2>
<p>1、什么是axios？</p>
<p>axios是一个基于promise的HTTP库，可以用在浏览器和node.js中</p>
<p>2、axios有什么特性？</p>
<ul>
<li>从浏览器中创建XMLHTTPRequests</li>
<li>从node.js中创建http请求</li>
<li>支持Promise API</li>
<li>拦截请求和响应</li>
<li>转换请求和响应数据</li>
<li>自动转换JSON数据</li>
<li>客户端支持防御XRSF</li>
</ul>
<h2 data-id="heading-2">二、准备工作</h2>
<ol>
<li>首先新建一个mini-axios目录</li>
<li>在该根目录下新建一个server.js文件，内容如下：</li>
</ol>
<pre><code class="copyable">var express = require('express')
var app = express()
var path = require('path')

// 读取静态资源路径
app.use(express.static(path.join(__dirname, 'src')))

app.all('*', function (req, res, next) &#123;
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  res.header('Access-Control-Allow-Methods', '*');
  res.header('Content-Type', 'application/json;charset=utf-8');
  next()
&#125;)

app.get('/getTest', function (request, response) &#123;
  data = &#123;
    'fontEnd': '前端',
    'suuny': 'zbq'
  &#125;
  response.json(data);
&#125;)

var server = app.listen(5000, function () &#123;
  console.log('*********server start*********')
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>新建一个src/interceptors.js、src/myAxios.js文件</li>
<li>新建src/index.html文件，内容如下：</li>
</ol>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
<button class="btn">点我发送请求</button>
<script type="text/javascript" src="./interceptors.js"></script>
<script type="text/javascript" src="./myAxios.js"></script>
<script>
    document.querySelector('.btn').onclick = function() &#123;
    &#125;
</script>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>在当前目录下打开终端，执行npm init -y 初始化package.json文件</li>
<li>安装 express（npm i express）</li>
<li>执行npm start（启动server.js）</li>
</ol>
<p>在浏览器中输入：<a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A5000%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:5000/index.html" ref="nofollow noopener noreferrer">http://localhost:5000/index.html</a> 能正常访问</p>
<p>准备工作完成</p>
<h2 data-id="heading-3">三、实现一个简单的axios</h2>
<p><strong>实现axios与axios.method方法</strong></p>
<ol>
<li>新建一个Axios类，并实现核心方法request方法（也就是ajax封装）</li>
</ol>
<pre><code class="copyable">class Axios &#123;
  constructor () &#123;&#125;

  request (config) &#123;
    return new Promise(resolve => &#123;
      const &#123;url = '', method = 'get', data=&#123;&#125;&#125; = config
      const xhr = new XMLHttpRequest()
      xhr.open(method, url, true)
      xhr.onload = function () &#123;
        console.log('a:', xhr.responseText)
        resolve(xhr.responseText);
      &#125;
      xhr.send(data)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>导出一个axios方法，通过查看源码，它实际上导出的是axios的request方法</li>
</ol>
<pre><code class="copyable">function createInstance () &#123;
  var axios = new Axios()
  var req = axios.request.bind(axios)
  return req
&#125;
var axios = createInstance()
export default axios
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在Axios原型上添加get、post等方法，这些方法内部实际上调用的还是Axios上的request方法</li>
</ol>
<pre><code class="copyable">var methodsArr = ['get','delete', 'head', 'options', 'put', 'patch', 'post']
methodsArr.forEach(met => &#123;
  Axios.prototype[met] = function () &#123;
    if(['get','delete', 'head', 'options'].includes(met)) &#123;
      return this.request(&#123;
        method: met,
        url: arguments[0],
        ...arguments[1] || &#123;&#125;
      &#125;)
    &#125; else &#123;
      return this.request(&#123;
        method: met,
        url: arguments[0],
        data: arguments[1],
        ...arguments[2] || &#123;&#125;
      &#125;)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>由于此时只有Axios.prototype才有get、post这些方法，但是导出的request方法没有怎么办呢？源码中是通过util.extend方法，将Axios.prototype中的方法直接copy到request上</li>
</ol>
<pre><code class="copyable">var util = &#123;
  extend (a, b, context) &#123;
    for(let key in b)&#123;
      if (b.hasOwnProperty(key)) &#123;
        if (typeof b[key] === 'function') &#123;
          a[key] = b[key].bind(context) // 运行request中copy过来的方法，方法中的this指向的还是axios实例
        &#125; else &#123;
          a[key] = b[key]
        &#125;
      &#125;
    &#125;
  &#125;
&#125;

function createInstance () &#123;
  var axios = new Axios()
  var req = axios.request.bind(axios)
  // 新增
  util.extend(req, Axios.prototype, axios) // 将Axios原型上的方法搬运到request中
  return req
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，axios(实际上是request)，axios.method方法已经实现（不得不说这里用的实在巧妙了）</p>
<p><strong>实现请求与响应拦截器</strong></p>
<p>首先看一个拦截器的使用</p>
<pre><code class="copyable">// 添加请求拦截器
axios.interceptors.request.use(function (config) &#123;
    // 在发送请求之前做些什么
    return config;
  &#125;, function (error) &#123;
    // 对请求错误做些什么
    return Promise.reject(error);
  &#125;);

// 添加响应拦截器
axios.interceptors.response.use(function (response) &#123;
    // 对响应数据做点什么
    return response;
  &#125;, function (error) &#123;
    // 对响应错误做点什么
    return Promise.reject(error);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>什么是请求拦截器呢？拦截器其实就是在发送请求之前会先执行拦截器的代码，我们可以在拦截器中对请求的参数config做些处理。</p>
<p>响应拦截也是如此，在请求响应返回data数据后，会先直接响应拦截函数，我们可以处理放回的data数据</p>
<p>具体实现如下：</p>
<ol>
<li>首先新建一个拦截器Interceptors类</li>
</ol>
<pre><code class="copyable">class Interceptors &#123;
  constructor() &#123;
    this.handlers = []
  &#125;
  use (onResolved, onRejected) &#123;
    this.handlers.push(&#123;
      onResolved,
      onRejected
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>将axios新增interceptors对象属性，并为它新增request、response属性，属性值均是Interceptors的实例。新增sendAjax方法，将request内容剪切过去</li>
</ol>
<pre><code class="copyable">class Axios &#123;
  constructor() &#123;
    // 新增
    this.interceptors = &#123;
      request: new Interceptors(),
      response: new Interceptors()
    &#125;
  &#125;
  request (config) &#123;
  
  &#125;
  sendAjax (config) &#123;
    return new Promise(resolve => &#123;
      const &#123;url = '', method = 'get', data=&#123;&#125;&#125; = config
      const xhr = new XMLHttpRequest()
      xhr.open(method, url, true)
      xhr.onload = function () &#123;
        console.log('a:', xhr.responseText)
        resolve(xhr.responseText);
      &#125;
      xhr.send(data)
    &#125;)
  &#125;
  ....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>修改request方法，组装chain执行列表，实现如下：</li>
</ol>
<ul>
<li>新建一个chain，值为sendAjax函数，undefined</li>
<li>将请求拦截的onResolved, onRejected添加至chain最前边</li>
<li>将响应拦截的onResolved, onRejected添加至chain的最后</li>
</ul>
<p>新建promise，遍历chain列表，组装promise执行串，保证执行他们的执行顺序</p>
<pre><code class="copyable">request(config) &#123;
    var chain = [this.sendAjax.bind(this), undefined]

    // 请求拦截
    this.interceptors.request.handlers.forEach(interceptor => &#123;
      chain.unshift(interceptor.onResolved, interceptor.onRejected)
    &#125;)

    // 响应拦截
    this.interceptors.response.handlers.forEach(interceptor => &#123;
      chain.push(interceptor.onResolved, interceptor.onRejected)
    &#125;)

    var promise = Promise.resolve(config)
    while (chain.length > 0) &#123;
      promise = promise.then(chain.shift(), chain.shift())
    &#125;
    return promise   
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>由于只有Axiox构造函数才有interceptors拦截器的属性，因此需要将Axios构造函数属性搬运至request方法上</li>
</ol>
<pre><code class="copyable">function createInstance () &#123;
  var axios = new Axios()
  var req = axios.request.bind(axios)
  util.extend(req, Axios.prototype, axios) // 将Axios原型上的方法搬运到request中
  // 新增
  util.extend(req, axios)                  // 将axios实例上的属性搬运至request中
  return req
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">四、完整代码如下：</h2>
<pre><code class="copyable">class Interceptors &#123;
  constructor() &#123;
    this.handlers = []
  &#125;
  use (onResolved, onRejected) &#123;
    this.handlers.push(&#123;
      onResolved,
      onRejected
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class Axios &#123;
  constructor() &#123;
    this.interceptors = &#123;
      request: new Interceptors(),
      response: new Interceptors()
    &#125;
  &#125;
  request(config) &#123;
    var chain = [this.sendAjax.bind(this), undefined]

    // 请求拦截
    this.interceptors.request.handlers.forEach(interceptor => &#123;
      chain.unshift(interceptor.onResolved, interceptor.onRejected)
    &#125;)

    // 响应拦截
    this.interceptors.response.handlers.forEach(interceptor => &#123;
      chain.push(interceptor.onResolved, interceptor.onRejected)
    &#125;)

    var promise = Promise.resolve(config)
    while (chain.length > 0) &#123;
      promise = promise.then(chain.shift(), chain.shift())
    &#125;
    return promise   
  &#125;
  sendAjax (config) &#123;
    return new Promise(resolve => &#123;
      const &#123;url = '', method = 'get', data=&#123;&#125;&#125; = config
      const xhr = new XMLHttpRequest()
      xhr.open(method, url, true)
      xhr.onload = function () &#123;
        console.log('a:', xhr.responseText)
        resolve(xhr.responseText);
      &#125;
      xhr.send(data)
    &#125;)
  &#125;
&#125;
// 定义get,post...方法，挂在到Axios原型上
var methodsArr = ['get','delete', 'head', 'options', 'put', 'patch', 'post']
methodsArr.forEach(met => &#123;
  Axios.prototype[met] = function () &#123;
    if(['get','delete', 'head', 'options'].includes(met)) &#123;
      return this.request(&#123;
        method: met,
        url: arguments[0],
        ...arguments[1] || &#123;&#125;
      &#125;)
    &#125; else &#123;
      return this.request(&#123;
        method: met,
        url: arguments[0],
        data: arguments[1],
        ...arguments[2] || &#123;&#125;
      &#125;)
    &#125;
  &#125;
&#125;)

var util = &#123;
  extend (a, b, context) &#123;
    for(let key in b)&#123;
      if (b.hasOwnProperty(key)) &#123;
        if (typeof b[key] === 'function') &#123;
          a[key] = b[key].bind(context)
        &#125; else &#123;
          a[key] = b[key]
        &#125;
      &#125;
    &#125;
  &#125;
&#125;


function createInstance () &#123;
  let axios = new Axios();
  let req = axios.request.bind(axios)
  util.extend(req, Axios.property, axios)  // 将Axios原型上的方法搬运到request中
  util.extend(req, axios)                  // 将axios实例上的属性搬运至request中
  return req
&#125;

var axios = createInstance()
export default axios

<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试一下</p>
<pre><code class="copyable">// src/index.html
<script type="text/javascript" src="./myAxios.js"></script>
<script>
    document.querySelector('.btn').onclick = function() &#123;
        // 分别使用以下方法调用，查看myaxios的效果
        axios.post('/postAxios', &#123;
          name: 'zbqpost'
        &#125;).then(res => &#123;
          console.log('postAxios 成功响应', res);
        &#125;)
        axios.interceptors.request.use(function (config) &#123;
          config.method = 'get'
          console.log("被我请求拦截器拦截了，哈哈:",config);
          console.log('config', config)
          return config;
        &#125;, function (error) &#123;
          return Promise.reject(error)
        &#125;)

        axios.interceptors.response.use(function (response) &#123;
          console.log('response拦截了， 哈哈')
          response = &#123;message:"响应数据被我替换了，啊哈哈哈"&#125;
          return response;
        &#125;, function (error) &#123;
          console.log('response错了么:', error)
          return Promise.reject(error)
        &#125;)

        axios(&#123;
          method: 'get',
          url: '/getTest'
        &#125;).then(res => &#123;
          console.log('getAxios 成功响应', res);
        &#125;)

    &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">五、Axios的CSRF(XSRF)防御</h2>
<h2 data-id="heading-6">五、ajax、fetch、axios区别</h2>
<p><strong>ajax</strong></p>
<ul>
<li>存在嵌套地狱问题，不利于代码维护</li>
<li>针对mvc模式编程，不符合前端mvvm的浪潮</li>
<li>不符合关注分离的原则</li>
</ul>
<p><strong>fetch</strong></p>
<ul>
<li>fetch（号称是ajax的替代品）内部不是使用XMLHttpRequest对象，而是原生js，fetch的代码结构比ajax简单多了</li>
<li>更加底层，提供丰富的API(request、response)</li>
<li>fetch只对网络请求报错，会调用reject，对400，500等都当作成功的请求，因此需要封装去处理</li>
<li>默认不会带cookie，需要添加配置项 fetch(url, &#123;credentials: 'include'&#125;)</li>
<li>不支持abort，不支持超时控制，造成资源浪费</li>
<li>不能监测请求进度，而xhr可以</li>
<li>fetch不兼容IE，其他的一些低版本浏览器也不兼容</li>
</ul>
<p>*<strong>axios</strong>
axios 是一个基于Promise 用于浏览器和 nodejs 的 HTTP 客户端，它有如下特性：</p>
<ul>
<li>从浏览器中创建XMLHTTPRequests</li>
<li>从node.js中创建http请求</li>
<li>支持Promise API</li>
<li>拦截请求和响应</li>
<li>转换请求和响应数据</li>
<li>取消请求</li>
<li>自动转换JSON数据</li>
<li>客户端支持防御XRSF</li>
</ul>
<p>axios既提供了并发的封装，也没有fetch的各种问题，而且体积也较小，当之无愧现在最应该选用的请求的方式。</p>
<h2 data-id="heading-7">六、其他</h2>
<h3 data-id="heading-8">CSRF攻击</h3>
<p>CSRF（Cross-site request forgery）跨站请求伪造，也被称为“One Click Attack”或者Session Riding，通常缩写为CSRF或者XSRF，是一种对网站的恶意利用。</p>
<p>举个例子：</p>
<p>...
图片
...</p>
<p>解决办法：</p>
<ol>
<li>
<p>检查HTTP头上的检查 Referer 字段，一般请求的地址与Referer字段是位于同一个域名下的。当然这个方法也有局限性，因为攻击者也有可能直接去攻击浏览器，篡改其Referer字段</p>
</li>
<li>
<p>同步表单CSRF校验</p>
</li>
</ol>
<p>CSRF攻击之所以能成功，是因为服务器无法区分正常请求和攻击请求，因此针对这个问题，我们可以将CSRF token保存至表单的隐藏域中，当表单提交时，就可以一并提交了</p>
<ol start="3">
<li>双重Cookie防御</li>
</ol>
<p>就是将token保存只Cookie中，在提交(post、put, path, delete)等请求时，通过请求头或者请求体带上Cookie中已设置的token，服务器接收到请求后进行对比校验。</p>
<p>Axios就是通过双重Cookie，请看如下源码部分：</p>
<pre><code class="copyable">// lib/defaults.js
var defaults = &#123;
  adapter: getDefaultAdapter(),

  .....
  xsrfCookieName: 'XSRF-TOKEN',
  xsrfHeaderName: 'X-XSRF-TOKEN',
&#125;;


// lib/adapters/xhr.js
module.exports = function xhrAdapter(config) &#123;
 ....
    // 添加xsrf头部
    if (utils.isStandardBrowserEnv()) &#123;
      var xsrfValue = (config.withCredentials || isURLSameOrigin(fullPath)) && config.xsrfCookieName ?
        cookies.read(config.xsrfCookieName) :
        undefined;

      if (xsrfValue) &#123;
        requestHeaders[config.xsrfHeaderName] = xsrfValue;
      &#125;
    &#125;
...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">XSS攻击</h3>
<p>Cross-Site Scripting(跨站脚本攻击)简称XSS，是一种代码注入攻击。攻击者在目标网站注入恶意脚本，使之在用户的浏览器上运行。利用这些恶意脚本，攻击者可获取用户的敏感信息如cookie，SessionId等，进而危害数据安全。</p>
<p>XSS 的本质是：恶意代码未经过滤，与网站正常的代码混在一起；浏览器无法分辨哪些脚本是可信的，导致恶意脚本被执行。
而由于直接在用户的终端执行，恶意代码能够直接获取用户的信息，或者利用这些信息冒充用户向网站发起攻击者定义的请求。</p>
<p>解决办法：</p>
<ol>
<li>过滤用户输入的，检查用户输入的内容中是否有非法内容，如：<>（尖括号）、”（引号）、 ‘（单引号）、%（百分比符号）、;（分号）、()（括号）、&（& 符号）、+（加号）等。、严格控制输出。</li>
<li>表单提交，或url参数传递前，需要对参数进行过滤</li>
</ol>
<pre><code class="copyable">function safeStr(str)&#123;
return str.replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g, "&quot;").replace(/'/g, "&#039;");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">七、参考</h2>
<ul>
<li><a href="https://juejin.cn/post/6856706569263677447" target="_blank" title="https://juejin.cn/post/6856706569263677447">juejin.cn/post/685670…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F267095921" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/267095921" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/267095921</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F156862881" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/156862881" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/156862881</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F58062212" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/58062212" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/58062212</a></li>
</ul></div>  
</div>
            