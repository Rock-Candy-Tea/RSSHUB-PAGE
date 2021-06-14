
---
title: '面试官不要再问我axios了？我能手写简易版的axios'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88d9cff0af3742f6ba41a60ad6e78631~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 04:43:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88d9cff0af3742f6ba41a60ad6e78631~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557?utm_campaign=30day&utm_medium=Ccenter&utm_source=20210528" target="_blank">更文挑战</a></p>
<p>axios作为我们工作中的常用的ajax请求库，作为前端工程师的我们当然是想一探究竟，axios究竟是如何去架构整个框架，中间的拦截器、适配器、 取消请求这些都是我们经常使用的。</p>
<h1 data-id="heading-0">前言</h1>
<p>由于axios源码中有很多不是很重要的方法，而且很多方法为了考虑兼容性，并没有考虑到用es6 的语法去写。本篇主要是带你去梳理axios的主要流程，并用es6重写简易版axios</p>
<ul>
<li>拦截器</li>
<li>适配器</li>
<li>取消请求</li>
</ul>
<h1 data-id="heading-1">拦截器</h1>
<p>一个axios实例上有两个拦截器，一个是请求拦截器， 然后响应拦截器。我们下看下官网的用法：</p>
<p>添加拦截器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 添加请求拦截器</span>
axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">config</span>) </span>&#123;
    <span class="hljs-comment">// 在发送请求之前做些什么</span>
    <span class="hljs-keyword">return</span> config;
  &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-comment">// 对请求错误做些什么</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>移除拦截器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> myInterceptor = axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">/*...*/</span>&#125;);
axios.interceptors.request.eject(myInterceptor);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实源码中就是，所有拦截器的执行 所以说肯定有一个forEach方法。</p>
<p>思路理清楚了，现在我们就开始去写吧。代码我就直接发出来，然后我在下面注解。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">InterceptorManager</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 存放所有拦截器的栈</span>
    <span class="hljs-built_in">this</span>.handlers = []
  &#125;

  <span class="hljs-function"><span class="hljs-title">use</span>(<span class="hljs-params">fulfilled, rejected</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.handlers.push(&#123;
      fulfilled,
      rejected,
    &#125;)
    <span class="hljs-comment">//返回id 便于取消</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.handlers.length - <span class="hljs-number">1</span>
  &#125;
  <span class="hljs-comment">// 取消一个拦截器</span>
  <span class="hljs-function"><span class="hljs-title">eject</span>(<span class="hljs-params">id</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.handlers[id]) &#123;
      <span class="hljs-built_in">this</span>.handlers[id] = <span class="hljs-literal">null</span>
    &#125;
  &#125;

  <span class="hljs-comment">// 执行栈中所有的hanlder</span>
  <span class="hljs-function"><span class="hljs-title">forEach</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.handlers.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
      <span class="hljs-comment">// 这里为了过滤已经被取消的拦截器，因为已经取消的拦截器被置null</span>
      <span class="hljs-keyword">if</span> (item) &#123;
        fn(item)
      &#125;
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拦截器这个类我们已经初步实现了，现在我们去实现axios 这个类，还是先看下官方文档，先看用法，再去分析。</p>
<p><strong>axios(config)</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 发送 POST 请求</span>
axios(&#123;
  <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
  <span class="hljs-attr">url</span>: <span class="hljs-string">'/user/12345'</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">firstName</span>: <span class="hljs-string">'Fred'</span>,
    <span class="hljs-attr">lastName</span>: <span class="hljs-string">'Flintstone'</span>
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-2">axios(url[, config])</h6>
<pre><code class="copyable">// 发送 GET 请求（默认的方法） 
axios('/user/12345');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Axios 这个类最核心的方法其实还是 request 这个方法。我们先看下实现吧</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Axios</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">config</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.defaults = config
    <span class="hljs-built_in">this</span>.interceptors = &#123;
      <span class="hljs-attr">request</span>: <span class="hljs-keyword">new</span> InterceptorManager(),
      <span class="hljs-attr">response</span>: <span class="hljs-keyword">new</span> InterceptorManager(),
    &#125;
  &#125;
  <span class="hljs-comment">// 发送一个请求</span>
  <span class="hljs-function"><span class="hljs-title">request</span>(<span class="hljs-params">config</span>)</span> &#123;
    <span class="hljs-comment">// 这里呢其实就是去处理了 axios(url[,config])</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> config == <span class="hljs-string">'string'</span>) &#123;
      config = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>] || &#123;&#125;
      config.url = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>]
    &#125; <span class="hljs-keyword">else</span> &#123;
      config = config || &#123;&#125;
    &#125;

    <span class="hljs-comment">// 默认get请求，并且都转成小写</span>
    <span class="hljs-keyword">if</span> (config.method) &#123;
      config.method = config.method.toLowerCase()
    &#125; <span class="hljs-keyword">else</span> &#123;
      config.method = <span class="hljs-string">'get'</span>
    &#125;

    <span class="hljs-comment">// dispatchRequest 就是发送ajax请求</span>
    <span class="hljs-keyword">const</span> chain = [dispatchRequest, <span class="hljs-literal">undefined</span>]
    <span class="hljs-comment">//  发生请求之前加入拦截的 fulfille 和reject 函数</span>
    <span class="hljs-built_in">this</span>.interceptors.request.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
      chain.unshift(item.fulfilled, item.rejected)
    &#125;)
    <span class="hljs-comment">// 在请求之后增加 fulfilled 和reject 函数</span>
    <span class="hljs-built_in">this</span>.interceptors.response.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
      chain.push(item.fulfilled, item.rejected)
    &#125;)

    <span class="hljs-comment">// 利用promise的链式调用，将参数一层一层传下去</span>
    <span class="hljs-keyword">let</span> promise = <span class="hljs-built_in">Promise</span>.resolve(config)

    <span class="hljs-comment">//然后我去遍历 chain</span>
    <span class="hljs-keyword">while</span> (chain.length) &#123;
      <span class="hljs-comment">// 这里不断出栈 直到结束为止</span>
      promise = promise.then(chain.shift(), chain.shift())
    &#125;
    <span class="hljs-keyword">return</span> promise
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里其实就是体现了axios设计的巧妙， 维护一个栈结构 + promise 的链式调用 实现了 拦截器的功能， 可能有的小伙伴到这里还是不是很能理解，我还是给大家画一个草图去模拟下这个过程。</p>
<p>假设我有1个请求拦截器handler和1个响应拦截器handler</p>
<p>一开始我们栈中的数据就两个</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88d9cff0af3742f6ba41a60ad6e78631~tplv-k3u1fbpfcp-watermark.image" alt="image-20210612233821686.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个没什么问题，由于有拦截器的存在，如果存在的话，那么我们就要往这个栈中加数据，请求拦截器顾名思义要在请求之前所以是unshift。加完请求拦截器我们的栈变成了这样</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36ff1bce15014111a722bd3e0c7bc160~tplv-k3u1fbpfcp-watermark.image" alt="image-20210612234321645.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没什么问题，然后请求结束后，我们又想对请求之后的数据做处理，所以响应拦截的数据自然是push了。这时候栈结构变成了这样：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88389df0d4e544a19ad73753802c3c31~tplv-k3u1fbpfcp-watermark.image" alt="image-20210612234601128.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后遍历整个栈结构，每次出栈都是一对出栈， 因为promise 的then 就是 一个成功，一个失败嘛。 遍历结束后，返回经过所有处理的promise，然后你就可以拿到最终的值了。</p>
<h1 data-id="heading-3">adapter</h1>
<p>Adapter: 英文解释是适配器的意思。 这里我就不实现了，我带大家看一下源码。 adapter 做了一件事非常简单，就是根据不同的环境 使用不同的请求。如果用户自定义了adapter，就用config.adapter。 否则就是默认是default.adpter.</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">var</span> adapter = config.adapter || defaults.adapter;

 <span class="hljs-keyword">return</span> adapter(config).then() ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>继续往下看deafults.adapter做了什么事情：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDefaultAdapter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> adapter;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> XMLHttpRequest !== <span class="hljs-string">'undefined'</span>) &#123;
    <span class="hljs-comment">// For browsers use XHR adapter</span>
    adapter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./adapters/xhr'</span>);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> process !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">Object</span>.prototype.toString.call(process) === <span class="hljs-string">'[object process]'</span>) &#123;
    <span class="hljs-comment">// For node use HTTP adapter</span>
    adapter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./adapters/http'</span>);
  &#125;
  <span class="hljs-keyword">return</span> adapter;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实就是做个选择：如果是浏览器环境：就是用xhr 否则就是node 环境。 判断process是否存在。从写代码的角度来说，axios源码的这里的设计可扩展性非常好。 有点像设计模式中的<strong>适配器模式</strong>， 因为浏览器端和node 端 发送请求其实并不一样， 但是我们不重要，我们不去管他的内部实现，用promise包一层做到对外统一。所以 我们用axios 自定义adapter 器的时候, 一定是返回一个promise。ok请求的方法我在下面模拟写出。</p>
<h1 data-id="heading-4">cancleToken</h1>
<p>我首先问大家一个问题，取消请求原生浏览器是怎么做到的？ 有一个abort 方法。可以取消请求。 那么axios源码肯定也是运用了这一点去取消请求。 现在浏览器其实也支持fetch请求， fetch可以取消请求？ 很多同学说是不可以的，其实不是？fetch 结合 abortController  可以实现取消fetch请求。我们看下例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> controller = <span class="hljs-keyword">new</span> AbortController();
<span class="hljs-keyword">const</span> &#123; signal &#125; = controller;

fetch(<span class="hljs-string">"http://localhost:8000"</span>, &#123; signal &#125;).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Request 1 is complete!`</span>);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`Fetch 1 error: <span class="hljs-subst">$&#123;e.message&#125;</span>`</span>);
&#125;);
<span class="hljs-comment">// Wait 2 seconds to abort both requests</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> controller.abort(), <span class="hljs-number">2000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这是个实验性功能，可恶的ie。 所以我们这次还是用原生的浏览器xhr基于promise简单的封装一下。代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatchRequest</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
    xhr.open(config.method, config.url)
    xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status <= <span class="hljs-number">300</span> && xhr.readyState === <span class="hljs-number">4</span>) &#123;
        resolve(xhr.responseText)
      &#125; <span class="hljs-keyword">else</span> &#123;
        reject(<span class="hljs-string">'失败了'</span>)
      &#125;
    &#125;

    <span class="hljs-keyword">if</span> (config.cancelToken) &#123;
      <span class="hljs-comment">// Handle cancellation</span>
      config.cancelToken.promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onCanceled</span>(<span class="hljs-params">cancel</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (!xhr) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
        xhr.abort()
        reject(cancel)
        <span class="hljs-comment">// Clean up request</span>
        xhr = <span class="hljs-literal">null</span>
      &#125;)
    &#125;
    xhr.send()
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Axios 源码里面做了很多处理， 这里我只做了get处理，我主要的目的就是为了axios是如何取消请求的。  先看下官方用法:</p>
<p>主要是两种用法：</p>
<p>使用 <em>cancel token</em> 取消请求</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CancelToken = axios.CancelToken;
<span class="hljs-keyword">const</span> source = CancelToken.source();

axios.get(<span class="hljs-string">'/user/12345'</span>, &#123;
  <span class="hljs-attr">cancelToken</span>: source.token
&#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">thrown</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (axios.isCancel(thrown)) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Request canceled'</span>, thrown.message);
  &#125; <span class="hljs-keyword">else</span> &#123;
     <span class="hljs-comment">// 处理错误</span>
  &#125;
&#125;);

axios.post(<span class="hljs-string">'/user/12345'</span>, &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'new name'</span>
&#125;, &#123;
  <span class="hljs-attr">cancelToken</span>: source.token
&#125;)

<span class="hljs-comment">// 取消请求（message 参数是可选的）</span>
source.cancel(<span class="hljs-string">'Operation canceled by the user.'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还可以通过传递一个 executor 函数到 <code>CancelToken</code> 的构造函数来创建 cancel token：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CancelToken = axios.CancelToken;
<span class="hljs-keyword">let</span> cancel;

axios.get(<span class="hljs-string">'/user/12345'</span>, &#123;
  <span class="hljs-attr">cancelToken</span>: <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">executor</span>(<span class="hljs-params">c</span>) </span>&#123;
    <span class="hljs-comment">// executor 函数接收一个 cancel 函数作为参数</span>
    cancel = c;
  &#125;)
&#125;);

<span class="hljs-comment">// cancel the request</span>
cancel();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看了官方用法 和结合axios源码： 我给出以下实现:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">cancelToken</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">exactor</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> executor !== <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'executor must be a function.'</span>)
        &#125;
        <span class="hljs-comment">// 这里其实将promise的控制权 交给 cancel 函数</span>
        <span class="hljs-comment">// 同时做了防止多次重复cancel 之前 Redux 还有React 源码中也有类似的案列</span>
        <span class="hljs-keyword">const</span> resolvePromise;
        <span class="hljs-built_in">this</span>.promise =  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
            resolvePromise = resolve;
        &#125;)
        <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>;
        
        <span class="hljs-keyword">const</span> cancel  = <span class="hljs-function">(<span class="hljs-params">message</span>) =></span> &#123;
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.reason) &#123;
                <span class="hljs-keyword">return</span>;
            &#125;
            <span class="hljs-built_in">this</span>.reason = <span class="hljs-string">'cancel'</span> + message;
            resolvePromise(<span class="hljs-built_in">this</span>.reason);
        &#125;
        exactor(cancel)
    &#125;

    <span class="hljs-function"><span class="hljs-title">throwIfRequested</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.reason) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-built_in">this</span>.reason
        &#125;
    &#125;
    
    <span class="hljs-comment">// source 其实本质上是一个语法糖 里面做了封装</span>
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">source</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> cancel;
        <span class="hljs-keyword">const</span> token = <span class="hljs-keyword">new</span> cancelToken(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">executor</span>(<span class="hljs-params">c</span>) </span>&#123;
            cancel = c;
        &#125;);
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">token</span>: token,
            <span class="hljs-attr">cancel</span>: cancel
        &#125;;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>截止到这里大体axios 大体功能已经给出。</p>
<p>接下来我就测试下我的手写axios 有没有什么问题？</p>
<pre><code class="hljs language-js copyable" lang="js"> <script type=<span class="hljs-string">"module"</span> >
    <span class="hljs-keyword">import</span> Axios <span class="hljs-keyword">from</span> <span class="hljs-string">'./axios.js'</span>;
    <span class="hljs-keyword">const</span> config = &#123; <span class="hljs-attr">url</span>:<span class="hljs-string">'http://101.132.113.6:3030/api/mock'</span> &#125;
    <span class="hljs-keyword">const</span> axios =  <span class="hljs-keyword">new</span> Axios();
    axios.request(config).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(res,<span class="hljs-string">'0000'</span>)
    &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(err)
    &#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开浏览器看一下结果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acc52c260cdd4a01a90e0ce46e15684d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210613170742511.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>成功了ok, 然后我来测试一下拦截器的功能： 代码更新成下面这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Axios <span class="hljs-keyword">from</span> <span class="hljs-string">'./axios.js'</span>;
<span class="hljs-keyword">const</span> config = &#123; <span class="hljs-attr">url</span>:<span class="hljs-string">'http://101.132.113.6:3030/api/mock'</span> &#125;
<span class="hljs-keyword">const</span> axios =  <span class="hljs-keyword">new</span> Axios();
<span class="hljs-comment">// 在axios 实例上挂载属性</span>
<span class="hljs-keyword">const</span> err = <span class="hljs-function">() =></span> &#123;&#125;
axios.interceptors.request.use(<span class="hljs-function">(<span class="hljs-params">config</span>)=></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是请求拦截器1'</span>)
    config.id = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">return</span>  config
&#125;,err )
axios.interceptors.request.use(<span class="hljs-function">(<span class="hljs-params">config</span>)=></span> &#123;
    config.id = <span class="hljs-number">2</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是请求拦截器2'</span>)
    <span class="hljs-keyword">return</span> config
&#125;,err)
axios.interceptors.response.use(<span class="hljs-function">(<span class="hljs-params">data</span>)=></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是响应拦截器1'</span>,data )
    data += <span class="hljs-number">1</span>;
    <span class="hljs-keyword">return</span> data;
&#125;,err)
axios.interceptors.response.use(<span class="hljs-function">(<span class="hljs-params">data</span>)=></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是响应拦截器2'</span>,data )
    <span class="hljs-keyword">return</span>  data
&#125;,err)
axios.request(config).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-comment">// console.log(res,'0000')</span>
    <span class="hljs-comment">// return res;</span>
&#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ajax 请求的结果 我是resolve(1) ，所以我们看下输出路径：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f191090e082e4ea4a7ccbf651bbf1fed~tplv-k3u1fbpfcp-watermark.image" alt="image-20210613195735319.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没什么问题， 响应后的数据我加了1。</p>
<p>接下来我来是取消请求的两种方式</p>
<pre><code class="copyable">// 第一种方式
let  cancelFun = undefined;
const cancelInstance = new cancelToken((c)=>&#123;
    cancelFun = c;
&#125;);
config.cancelToken = cancelInstance;
// 50 ms 就取消请求
setTimeout(()=>&#123;
    cancelFun('取消成功')
&#125;,50)

第二种方式：
const &#123; token, cancel &#125;  = cancelToken.source();
config.cancelToken = token;
setTimeout(()=>&#123;
    cancel()
&#125;,50)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a230094a93034282872abda359d7b6c2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210613201656905.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结果都是OK的,至此axios简单源码终于搞定了。</p>
<h1 data-id="heading-5">反思</h1>
<p>本篇文章只是把axios源码的大体流程走了一遍， axios源码内部还是做了很多兼容比如： 配置优先级：他有一个mergeConfig 方法， 还有数据转换器。不过这些不影响我们对axios源码的整体梳理， 源码中其实有一个createInstance，至于为什么有？ 我觉得就是为了可扩展性更好， 将来有啥新功能，直接在原有axios的实例的原型链上去增加，代码可维护性强， axios.all spread 都是实例new出来再去挂的，不过都很简单，没啥的。有兴趣大家自行阅读。</p>
<h1 data-id="heading-6">总结</h1>
<p>本篇文章所有代码都在我的<a href="https://github.com/wzf1997/MyPolyfill" target="_blank" rel="nofollow noopener noreferrer">github</a>这个项目上，欢迎star, 如果文章看了对你有帮助，欢迎点赞+关注！后面会持续更新源码系列。如果文章有任何错误，请随时感谢大家！</p>
<h1 data-id="heading-7">往期回顾</h1>
<ul>
<li><a href="https://juejin.cn/post/6965366315833884680" target="_blank">带你从头到尾系统地撸一遍Redux源码</a></li>
<li><a href="https://juejin.cn/post/6967738672279994382" target="_blank">React17源码解读—— 事件系统</a></li>
</ul></div>  
</div>
            