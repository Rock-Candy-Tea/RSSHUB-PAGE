
---
title: '项目中使用axios过滤多次重复请求'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/635e940456b64e9d8065d96dab2eaf15~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 22:35:01 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/635e940456b64e9d8065d96dab2eaf15~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言：</h2>
<p>我们在web应用开发过程当中，经常会遇到一个时刻发起了多个请求的场景
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/635e940456b64e9d8065d96dab2eaf15~tplv-k3u1fbpfcp-watermark.image" alt="多个请求.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">这个情况下，我们通常的做法有两种：</h3>
<ul>
<li>可以在请求时show一个loading，阻止用户操作。</li>
<li>或者人为加个变量，做一个请求的节流</li>
</ul>
<p>我们的项目中，目前大部分情况也是采用以上两种方式做的。今天来介绍一个新的方式。</p>
<h2 data-id="heading-2">二、CancelToken类</h2>
<p>我们之前实例化一个Promise，这个对象是否成功与否，是无法在函数外部决定的，这里边使用要用到一个小窍门，可以让一个promise 和resolve分离。任何时机都可以触发resolve:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-comment">// 一个promise</span>
  <span class="hljs-keyword">let</span> resolvePromise
  <span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolvePromise = resolve
  &#125;)
  <span class="hljs-comment">// 这样在外部执行</span>
  resolvePromise()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok，有了这个前提，我们需要借助axios.CancelToken这个类。
这个类相当于在每次请求的时候开启另一个promise和当前的请求形成一个promise.race(请求p1，取消请求p2)，在promise中的resolve方法赋值给了一个外部的变量去接收。我们可以根据需求，人为决定是否取消前次请求。其实这就类似，原来我们写fetch封装接口超时的Promise.race类似。</p>
<ol>
<li>cancelToken中也提供了相应的static方法source用来生成一个cancelToken和一个cancel方法其实就是这个promise的一个resolve。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">    CancelToken.source = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">source</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> cancel;
    <span class="hljs-comment">// </span>
    <span class="hljs-keyword">var</span> token = <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">executor</span>(<span class="hljs-params">c</span>) </span>&#123;
        cancel = c;
    &#125;);
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">token</span>: token,
        <span class="hljs-attr">cancel</span>: cancel,
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>根据我们常用的的缓存方式，我们可以声明一个map来存储每次请求的url，同时存储对应的cancel方法。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// 声明一个全局map</span>
    <span class="hljs-keyword">const</span> pendingHttp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
    <span class="hljs-comment">// axios中内置的CancelToken类</span>
    <span class="hljs-keyword">const</span> CancelToken = axios.CancelToken
       
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addApi</span> (<span class="hljs-params">config</span>) </span>&#123;
      config.cancelToken = <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function">(<span class="hljs-params">cancel</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> url = config.url
        <span class="hljs-built_in">console</span>.log(pendingHttp)
        <span class="hljs-keyword">if</span> (!pendingHttp.has(url)) &#123;
          pendingHttp.set(url, cancel)
        &#125;
      &#125;)
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cancelApi</span> (<span class="hljs-params">config</span>) </span>&#123;
      <span class="hljs-keyword">const</span> url = config.url
      <span class="hljs-keyword">if</span> (pendingHttp.has(url)) &#123; <span class="hljs-comment">// 如果在 pending 中存在当前请求标识，需要取消当前请求，并且移除</span>
        <span class="hljs-keyword">const</span> cancel = pendingHttp.get(url)
        cancel(url + <span class="hljs-string">'取消了'</span>)
        pendingHttp.delete(url) <span class="hljs-comment">// 清空当前url的缓存</span>
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>要特殊注意，要想取消掉一个请求，需要在config上添加cancelToken这个属性赋值为CancelToken的实例。否则cancel不掉。</li>
</ul>
<ol start="3">
<li>就像操作定时器一样，要先尝试取消上一次，然后再开启下一次</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">    httpService.interceptors.request.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;

      cancelApi(config)
      addApi(config)
      
      <span class="hljs-comment">// 本地调试的时候,是跨域的情况，加请求头会有限制(此处是项目代码无关紧要)</span>
      <span class="hljs-keyword">const</span> &#123; headers = &#123;&#125; &#125; = config; <span class="hljs-keyword">const</span> &#123; globalObj = &#123;&#125; &#125; = <span class="hljs-built_in">window</span>
      <span class="hljs-built_in">Object</span>.assign(headers, globalObj, &#123; <span class="hljs-keyword">from</span> &#125;)
      
      <span class="hljs-keyword">return</span> config
    &#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(error)
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>然后还有一种可能性，第一次请求已经返回了，又发起了相同的一次请求，所以在response里边也要cancelApi一下。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">    httpService.interceptors.response.use(
      <span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        cancelApi(response.config)
        sentryCatchApi(response)
      &#125;,
      <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
        <span class="hljs-comment">// 请求超时</span>
        <span class="hljs-keyword">if</span> (error.message.includes(<span class="hljs-string">'timeout'</span>)) &#123; <span class="hljs-comment">// 判断请求异常信息中是否含有超时timeout字符串</span>
          Toast.error(&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'网页请求超时，请刷新重试~'</span> &#125;)
        &#125;
        sentryCatchApi(error)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
      &#125;
    )
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>我们需要注意一点，cancel其实就是resolve，我们cancel执行时候传入的参数，会最终在response的error回调中，作为参数返回，这样我们的捕捉错误的方法可能会有报错。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// 假设我们的error方法是这样封装的。 来看一下sentryCatchApi</span>
    error => &#123;
      sentryCatchApi(error)
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
    &#125;
  <span class="hljs-comment">// 由于这个方法需要接收一个对象，但是我们cancel取消请求的情况下，返回的是一个字符串，这时就报错了。</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sentryCatchApi</span> (<span class="hljs-params">res</span>) </span>&#123;
      <span class="hljs-keyword">try</span> &#123;
        res = res || &#123;&#125;
        <span class="hljs-keyword">const</span> resData = res.data || &#123;&#125;
        Sentry.captureException(<span class="hljs-built_in">JSON</span>.stringify(resData))
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`
          获取数据失败:
          请在浏览器中打开进入 webview的地址，并粘贴出来，便于问题排查
          :接口相关信息:
          接口地址:<span class="hljs-subst">$&#123;res.config.url&#125;</span>,
          接口返回值:code:<span class="hljs-subst">$&#123;resData.code&#125;</span>,
          message:<span class="hljs-subst">$&#123;resData.message&#125;</span>,
          data:<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(resData.data)&#125;</span>
        `</span>)
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-built_in">console</span>.error(err)
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>需要使用isCancel这个api</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">
   error => &#123;
    <span class="hljs-keyword">if</span> (axios.isCancel(error)) <span class="hljs-keyword">return</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求被取消了'</span>, error.message)
    sentryCatchApi(error)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">最终效果</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36ee17f4ce34cfeb7e8cc0551897276~tplv-k3u1fbpfcp-watermark.image" alt="取消多次请求.gif" loading="lazy" referrerpolicy="no-referrer">
控制台也没有任何报错啦。（后续完善到项目中）</p></div>  
</div>
            