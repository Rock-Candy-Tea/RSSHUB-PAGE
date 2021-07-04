
---
title: 'levi_js 总结2'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/caf2f618530046658ab8e3b4a8699589~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 01:27:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/caf2f618530046658ab8e3b4a8699589~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">实现lazyman</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LazyManClass</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.taskList = [];
        <span class="hljs-built_in">this</span>.name = name;
        <span class="hljs-built_in">this</span>.taskList.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Hi! This is <span class="hljs-subst">$&#123;name&#125;</span>!`</span>);
          <span class="hljs-built_in">this</span>.run();
        &#125;);
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">this</span>.run();
        &#125;, <span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-function"><span class="hljs-title">sleepFirst</span>(<span class="hljs-params">time</span>)</span> &#123;
        <span class="hljs-keyword">let</span> fn = <span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`先睡个<span class="hljs-subst">$&#123;time&#125;</span>秒...`</span>);
            <span class="hljs-built_in">this</span>.run();
          &#125;, time * <span class="hljs-number">1000</span>);
        &#125;;
        <span class="hljs-built_in">this</span>.taskList.unshift(fn);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
      &#125;
      <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params">name</span>)</span> &#123;
        <span class="hljs-keyword">let</span> fn = <span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`I am eating <span class="hljs-subst">$&#123;name&#125;</span>`</span>);
          <span class="hljs-built_in">this</span>.run();
        &#125;;
        <span class="hljs-built_in">this</span>.taskList.push(fn);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
      &#125;
      <span class="hljs-function"><span class="hljs-title">sleep</span>(<span class="hljs-params">time</span>)</span> &#123;
        <span class="hljs-keyword">let</span> fn = <span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`睡了<span class="hljs-subst">$&#123;time&#125;</span>秒...`</span>);
            <span class="hljs-built_in">this</span>.run();
          &#125;, time * <span class="hljs-number">1000</span>);
        &#125;;
        <span class="hljs-built_in">this</span>.taskList.push(fn);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
      &#125;
      <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> fn = <span class="hljs-built_in">this</span>.taskList.shift();
        fn && fn();
      &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">LazyMan</span>(<span class="hljs-params">name</span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LazyManClass(name);
    &#125;
    LazyMan(<span class="hljs-string">'Tony'</span>).eat(<span class="hljs-string">'lunch'</span>).eat(<span class="hljs-string">'dinner'</span>).sleepFirst(<span class="hljs-number">2</span>).sleep(<span class="hljs-number">10</span>).eat(<span class="hljs-string">'junk food'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">Jquery选择器怎么实现的</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">    (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">window</span>, <span class="hljs-literal">undefined</span></span>) </span>&#123;
      <span class="hljs-keyword">var</span> rootjQuery = <span class="hljs-built_in">window</span>.document;
      <span class="hljs-keyword">var</span> jQuery = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> jQuery = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">selector, context</span>) </span>&#123;
          <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> jQuery.fn.init(selector, context, rootjQuery);
        &#125;;

        jQuery.fn = jQuery.prototype = &#123;
          <span class="hljs-attr">construct</span>: jQuery,
          <span class="hljs-attr">init</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">selector, context, rootjQuery</span>) </span>&#123;
            <span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;
            that.ele = <span class="hljs-literal">null</span>;
            that.value = <span class="hljs-string">''</span>;
            <span class="hljs-keyword">if</span> (selector.charAt(<span class="hljs-number">0</span>) === <span class="hljs-string">'#'</span>) &#123;
              <span class="hljs-built_in">console</span>.log(selector);
              that.ele = <span class="hljs-built_in">document</span>.getElementById(selector.slice(<span class="hljs-number">1</span>));
            &#125;
            that.getValue = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
              that.value = that.ele ? that.ele.innerHTML : <span class="hljs-string">'No value'</span>;
              <span class="hljs-keyword">return</span> that;
            &#125;;
            that.showValue = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
              <span class="hljs-keyword">return</span> that.value;
            &#125;;
          &#125;
        &#125;;

        jQuery.fn.init.prototype = jQuery.fn;
        <span class="hljs-keyword">return</span> jQuery;
      &#125;)();

      <span class="hljs-built_in">window</span>.jQuery = <span class="hljs-built_in">window</span>.$ = jQuery;
    &#125;)(<span class="hljs-built_in">window</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">给页面注入50万个li怎么做提升性能？</h4>
<h4 data-id="heading-3">手写懒加载（考虑防抖和重复加载问题）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">lazyImage</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">selector</span>)</span> &#123;
        <span class="hljs-built_in">this</span>._throttleFn = <span class="hljs-literal">null</span>;
        <span class="hljs-built_in">this</span>.imageElements = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">document</span>.getElementsByTagName(selector));

        <span class="hljs-built_in">this</span>.init();
      &#125;

      <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.initShow();
        <span class="hljs-built_in">this</span>._throttleFn = <span class="hljs-built_in">this</span>.throttle(<span class="hljs-built_in">this</span>.initShow);
        <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'scroll'</span>, <span class="hljs-built_in">this</span>._throttleFn.bind(<span class="hljs-built_in">this</span>));
      &#125;

      <span class="hljs-function"><span class="hljs-title">initShow</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> len = <span class="hljs-built_in">this</span>.imageElements.length;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
          <span class="hljs-keyword">let</span> imageElement = <span class="hljs-built_in">this</span>.imageElements[i];
          <span class="hljs-keyword">const</span> rect = imageElement.getBoundingClientRect();
          <span class="hljs-comment">// 出现在视野的时候加载图片</span>
          <span class="hljs-keyword">if</span> (rect.top < <span class="hljs-built_in">document</span>.documentElement.clientHeight) &#123;
            imageElement.src = imageElement.dataset.src;
            imageElement.removeAttribute(<span class="hljs-string">'data-src'</span>);
            imageElement.style.display = <span class="hljs-string">'block'</span>;
            <span class="hljs-built_in">Array</span>.prototype.splice.call(<span class="hljs-built_in">this</span>.imageElements, i, <span class="hljs-number">1</span>);
            len--;
            i--;

            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.imageElements.length === <span class="hljs-number">0</span>) &#123;
              <span class="hljs-comment">// 如果全部都加载完 则去掉滚动事件监听</span>
              <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'scroll'</span>, <span class="hljs-built_in">this</span>._throttleFn);
            &#125;
          &#125;
        &#125;
      &#125;

      <span class="hljs-function"><span class="hljs-title">throttle</span>(<span class="hljs-params">fn, delay = <span class="hljs-number">15</span></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">'function'</span>) &#123;
          <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'this is not a function'</span>);
        &#125;

        <span class="hljs-keyword">let</span> isStart = <span class="hljs-literal">false</span>;

        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>;
          <span class="hljs-keyword">if</span> (isStart) &#123;
            <span class="hljs-keyword">return</span>;
          &#125;
          isStart = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 初始化设置start 要执行一次</span>

          <span class="hljs-comment">/**
           * <span class="hljs-doctag">@description </span>利用定时器回调来控制start流转状态
           * */</span>
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            fn.apply(_this, <span class="hljs-built_in">arguments</span>); <span class="hljs-comment">// 确定this指向当前调用者 input</span>
            isStart = <span class="hljs-literal">false</span>;
          &#125;, delay);
        &#125;;
      &#125;
    &#125;

    <span class="hljs-keyword">new</span> lazyImage(<span class="hljs-string">'img'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">setTimeout和requestAnimationFrame的区别</h4>
<p>setTimeout</p>
<ul>
<li>需要设置时间间隔</li>
<li>间隔时间不精确，可能被其他任务阻塞</li>
<li>动画的间隔时间如果设定过短就会出现过度渲染占用大量资源，可能出现掉帧</li>
<li>实现动画在指定时间后执行，无论页面是否可见，浪费系统资源</li>
</ul>
<p>requestAnimationFrame</p>
<ul>
<li>不需要设定时间间隔</li>
<li>按帧对网页进行重绘。该方法告诉浏览器希望执行动画并请求浏览器在下一次重绘之前调用函数更新动画。</li>
<li>由系统来决定回调函数的执行机制。在运行时浏览器会自动优化方法的调用。</li>
<li>元素不可见时不会引起回流或重绘</li>
<li>页面不是激活状态下的话，动画会自动暂停，有效节省了CPU开销</li>
</ul>
<h4 data-id="heading-5">ajax和fetch区别</h4>
<p>ajax 本质上是 XMLHttpRequest</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
  xhr.open(<span class="hljs-string">'GET'</span>, url);
  xhr.responseType = <span class="hljs-string">'json'</span>;

  xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(xhr.response);
  &#125;;

  xhr.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Oops, error'</span>);
  &#125;;

  xhr.send();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fetch window上的方法</p>
<ul>
<li>window的一个方法</li>
<li>IE浏览器并不支持fetch</li>
<li>默认是get请求，可通过&#123;method: 'post'&#125;配置</li>
<li>默认不会接受或者发送cookies，需要设置 fetch(url, &#123;credentials: 'include'&#125;)</li>
<li>fetch请求不会讲http返回非200以外认为是错误状态，例如服务器返回 400，500 错误码时并不会 reject，只有网络错误这些导致请求不能完成时，fetch 才会被 reject</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-comment">// 第一个参数是请求url</span>
  <span class="hljs-comment">// 第二个参数可选参数 可以控制不同的init对象</span>
  <span class="hljs-comment">// 默认返回一个promise</span>
  <span class="hljs-keyword">var</span> promise = fetch(<span class="hljs-string">'http://localhost:3000/news'</span>, &#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>
  &#125;)
    .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
      <span class="hljs-keyword">return</span> response.json();
    &#125;)
    .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
      <span class="hljs-comment">// Error :(</span>
    &#125;);
  promise
    .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(data);
    &#125;)
    .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(error);
    &#125;);


  <span class="hljs-comment">// 实例</span>
  onfetch = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">window</span>.fetch(<span class="hljs-string">'http://localhost:8081'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res)).then;
    <span class="hljs-comment">/**
      body: ReadableStream // 返回流，需要特定插件处理下
      bodyUsed: false
      headers: Headers &#123;&#125;
      ok: true
      redirected: false
      status: 200
      statusText: "OK"
      type: "cors"
      url: "http://localhost:8081/"
      __proto__: Response
     * */</span>
  &#125;;


  <span class="hljs-comment">//  node开启服务</span>
  http
  .createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-comment">// const [path, query] = req.url.split('?')</span>
    <span class="hljs-comment">// const params = qs.parse(query, &#123; ignoreQueryPrefix: true &#125;)</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开始请求了'</span>)
    res.writeHead(<span class="hljs-number">300</span>, &#123;
      <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'text/javascript'</span>,
      <span class="hljs-string">'Access-Control-Allow-Origin'</span>: <span class="hljs-string">'*'</span>,
      <span class="hljs-string">'Access-Control-Allow-Methods'</span>: <span class="hljs-string">'PUT, GET, POST, DELETE, OPTIONS'</span>,
    &#125;)

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      res.end(<span class="hljs-string">'levi'</span>)
    &#125;, <span class="hljs-number">3000</span>)
  &#125;)
  .listen(<span class="hljs-number">8081</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">写一个加法函数(sum)，使他可以同时支持sum(x,y)和sum(x)(y)两种调用方式</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">currying</span>(<span class="hljs-params">func, ...args</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (args.length >= func.length) &#123;
      <span class="hljs-keyword">return</span> func(...args);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args2</span>) </span>&#123;
      <span class="hljs-keyword">return</span> currying(func, ...args, ...args2);
    &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
    <span class="hljs-keyword">return</span> num1 + num2;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">JS实现一个带并发限制的异步调度器Scheduler，保证同时运行的任务最多有两个。完善代码中Scheduler类，使得以下程序能正确输出</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// JS实现一个带并发限制的异步调度器Scheduler，保证同时运行的任务最多有两个。完善代码中Scheduler类，使得以下程序能正确输出。</span>
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Scheduler</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.tasks = [];
        <span class="hljs-built_in">this</span>.count = <span class="hljs-number">0</span>;
      &#125;
      <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">promiseCreator</span>)</span> &#123;
        <span class="hljs-comment">// TODO</span>
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
          <span class="hljs-built_in">this</span>.tasks.push(&#123;
            <span class="hljs-attr">creator</span>: promiseCreator,
            resolve
          &#125;);
          <span class="hljs-built_in">this</span>.run();
        &#125;);
      &#125;

      <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.count >= <span class="hljs-number">2</span>) <span class="hljs-keyword">return</span>;
        <span class="hljs-keyword">const</span> task = <span class="hljs-built_in">this</span>.tasks.shift();
        <span class="hljs-keyword">if</span> (task) &#123;
          <span class="hljs-built_in">this</span>.count++;
          task.creator().then(<span class="hljs-function">() =></span> &#123;
            task.resolve();
            <span class="hljs-built_in">this</span>.count--;
            <span class="hljs-built_in">this</span>.run();
          &#125;);
        &#125;
      &#125;
    &#125;

    <span class="hljs-keyword">const</span> timeout = <span class="hljs-function"><span class="hljs-params">time</span> =></span>
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(resolve, time);
      &#125;);

    <span class="hljs-keyword">const</span> scheduler = <span class="hljs-keyword">new</span> Scheduler();
    <span class="hljs-keyword">const</span> addTask = <span class="hljs-function">(<span class="hljs-params">time, order</span>) =></span> &#123;
      scheduler
        .add(<span class="hljs-function">() =></span> timeout(time))
        .then(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">console</span>.log(order);
        &#125;);
    &#125;;
    addTask(<span class="hljs-number">1000</span>, <span class="hljs-string">'1'</span>);
    addTask(<span class="hljs-number">500</span>, <span class="hljs-string">'2'</span>);
    addTask(<span class="hljs-number">300</span>, <span class="hljs-string">'3'</span>);
    addTask(<span class="hljs-number">400</span>, <span class="hljs-string">'4'</span>);
    <span class="hljs-comment">// output: 2 3 1 4</span>
    <span class="hljs-comment">// 一开始，1、2两个任务进入队列</span>
    <span class="hljs-comment">// 500ms时，2完成，输出2，任务3进队</span>
    <span class="hljs-comment">// 800ms时，3完成，输出3，任务4进队</span>
    <span class="hljs-comment">// 1000ms时，1完成，输出1</span>
    <span class="hljs-comment">// 1200ms时，4完成，输出4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">实现flat    [1,2,3,[4,5,[6,7]]] -> [1,2,3,4,5,6,7]</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 递归</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flat</span>(<span class="hljs-params">arr, prev</span>) </span>&#123;
<span class="hljs-keyword">let</span> result = prev || []
  
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i<arr.length; i++) &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(arr[i])) &#123;
        result.concat(flat(arr[i], result))
    &#125; <span class="hljs-keyword">else</span> &#123;
    result.push(arr[i])
    &#125;
  &#125;
  
  <span class="hljs-keyword">return</span> result
&#125;

<span class="hljs-comment">//  递归 reduce</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flat</span> (<span class="hljs-params">arr</span>) </span>&#123;
<span class="hljs-keyword">return</span> arr.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> pre.concat(<span class="hljs-built_in">Array</span>.isArray(cur) ? flat(cur) : cur)
  &#125;, [])
&#125;

<span class="hljs-comment">// while </span>
<span class="hljs-comment">// while </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flat</span> (<span class="hljs-params">arr</span>) </span>&#123;
<span class="hljs-keyword">while</span> (arr.some(<span class="hljs-built_in">Array</span>.isArray)) &#123;
  arr = [].concat(...arr)
  &#125;
  <span class="hljs-keyword">return</span> arr
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">一维数组转二维数组</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reflat</span> (<span class="hljs-params">arr, len</span>) </span>&#123;
  <span class="hljs-keyword">let</span> result = []

  <span class="hljs-keyword">let</span> loopNums = <span class="hljs-built_in">Math</span>.ceil(arr.length/len)

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < loopNums; i++) &#123;
    result.push(arr.slice(i*len, (i+<span class="hljs-number">1</span>) * len))
  &#125;

  <span class="hljs-keyword">return</span>(result)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">js实现repeat方法 const repeatFunc = repeat(alert, 4, 3000); 调用这个 repeatedFunc("hellworld")，会alert4次 helloworld, 每次间隔3秒</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">repeat</span>(<span class="hljs-params">func, num, time</span>) </span>&#123;
  <span class="hljs-keyword">var</span> flag = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timer</span>(<span class="hljs-params">str</span>) </span>&#123;
    func(str)
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      flag++
      <span class="hljs-keyword">if</span> (flag <= num) &#123;
        timer(str)
      &#125;
    &#125;, time);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">实现AutoComplete  TODO</h4>
<h4 data-id="heading-12">script的async有什么用</h4>
<p>正常情况下，script没有任何引入属性情况下，有以下特性
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/caf2f618530046658ab8e3b4a8699589~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>js脚本分为加载(Fetch)、解析（Execution）、执行(Execution)</li>
<li>js脚本的加载。解析、执行会阻塞DOM树渲染，因此一般会放置在尾部</li>
</ul>
<p>defer 和 async有下面异同</p>
<ul>
<li>都是属于异步加载脚本</li>
<li><strong>defer加载完成后，到DOM解析完成后才会执行，但是会发生在documentContentLoaded之前</strong></li>
</ul>
<h5 data-id="heading-13">async</h5>
<p>对脚本的请求是异步，不会阻塞html解析，一旦网络请求结果出来了，hmtl就会暂停解析，让js解析并执行相关代码
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/021b5dbeddb64db0a7099dc0a4dd076d~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果在async 请求发出来之后，html解析已经完成，那么对async不产生任何影响
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e5a89a4a1fe49ed9d5acaf25ef9aadd~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-14">defer</h5>
<p>脚本异步加载，获取脚本的请求的异步的，不会阻塞浏览器解析hmtl,一旦请求返回结果后，如果html解析还未完成，浏览器并不会解析并执行该返回结果脚本js代码，而是等到浏览器完全把hmtl解析完成在执行js代码<br>
<strong>如果存在多个多个defer标签，会按照引入顺序解析执行，这样并不会影响相互执行U依赖关系</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8313e4787f04c79838fec9961bda0fb~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-15">使用场景</h5>
<ul>
<li>如果脚本是模块化，不存在依赖关系，那么请使用async</li>
<li>如果脚本依赖另一个脚本，那么请使用defer</li>
<li>如果脚本是很小，并且异步脚本依赖他，那么请使用一个没有任何属性的内联脚本</li>
</ul>
<h4 data-id="heading-16">手写正则表达式判断电话号码</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 手机号码: 匹配1开头，第二位树是3-9的电话号码</span>
<span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/^1[3-9]\d&#123;9&#125;$/ig</span>; 

<span class="hljs-comment">// 座机号码 例如: (0511-4405222、021-87888822)</span>
<span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/\d&#123;3&#125;-\d&#123;8&#125;|\d&#123;4&#125;-\d&#123;7&#125;/ig</span>; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">js转千分位</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-comment">// Object.prototype.toLocaleString</span>
  <span class="hljs-keyword">const</span> number = <span class="hljs-number">123456789</span>;
  <span class="hljs-built_in">console</span>.log(number.toLocaleString()) <span class="hljs-comment">// 123,456,789</span>


  <span class="hljs-comment">// slice() 方法可从已有的数组中返回选定的元素,截取数组的一个方法</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toThousandsNum</span>(<span class="hljs-params">num</span>) </span>&#123;
    <span class="hljs-keyword">var</span> num = (num || <span class="hljs-number">0</span>).toString(),
      result = <span class="hljs-string">''</span>;

    <span class="hljs-keyword">while</span> (num.length > <span class="hljs-number">3</span>) &#123;
      <span class="hljs-comment">//此处用数组的slice方法，如果是负数，那么它规定从数组尾部开始算起的位置</span>
      result = <span class="hljs-string">','</span> + num.slice(-<span class="hljs-number">3</span>) + result;
      num = num.slice(<span class="hljs-number">0</span>, num.length - <span class="hljs-number">3</span>);
    &#125;
    <span class="hljs-comment">// 如果数字的开头为0,不需要逗号</span>
    <span class="hljs-keyword">if</span> (num) &#123;
      result = num + result;
    &#125;
    <span class="hljs-keyword">return</span> result;
  &#125;

  <span class="hljs-built_in">console</span>.log(toThousandsNum(<span class="hljs-number">123456789123</span>)); <span class="hljs-comment">// 123,456,789,123</span>

  <span class="hljs-comment">// 数组从尾部遍历</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toThousandsNum</span>(<span class="hljs-params">num</span>) </span>&#123;
    <span class="hljs-keyword">const</span> str = (num || <span class="hljs-number">0</span>).toString().split(<span class="hljs-string">''</span>);
    <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> result = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = str.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
      count++;
      result.unshift(str[i]);
      <span class="hljs-keyword">if</span> (count % <span class="hljs-number">3</span> === <span class="hljs-number">0</span> && i !== <span class="hljs-number">0</span>) &#123;
        result.unshift(<span class="hljs-string">','</span>);
      &#125;
    &#125;

    <span class="hljs-keyword">return</span> result.join(<span class="hljs-string">''</span>);
  &#125;

  <span class="hljs-built_in">console</span>.log(toThousandsNum(<span class="hljs-number">123456789123</span>)); <span class="hljs-comment">// 123,456,789,123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">sum(1)(2)(3).valueof()</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> args = [...arguments];
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum_backup</span>(<span class="hljs-params"></span>) </span>&#123;
      args.push(...arguments);
      <span class="hljs-keyword">return</span> sum_backup;
    &#125;

    sum_backup.valueof = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">return</span> args.reduce(<span class="hljs-function">(<span class="hljs-params">prev, cur</span>) =></span> prev + cur);
    &#125;;

    <span class="hljs-keyword">return</span> sum_backup;
  &#125;

  <span class="hljs-built_in">console</span>.log(sum(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>)(<span class="hljs-number">4</span>).valueof());
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">setTimeout一定会按时执行吗？</h4>
<p>不会，setTimeout是宏任务，得等到同步任务、事件队列中微任务、排序靠前的宏任务执行完了后，才能执行当前宏任务事件</p>
<blockquote>
<p>setTimeout是一个异步的宏任务，当执行setTimeout时是将回调函数在指定的时间之后放入到宏任务队列。但如果此时主线程有很多同步代码在等待执行，或者微任务队列以及当前宏任务队列之前还有很多任务在排队等待执行，那么要等他们执行完成之后setTimeout的回调函数才会被执行，因此并不能保证在setTimeout中指定的时间立刻执行回调函数</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"计时器执行"</span>) <span class="hljs-comment">// 几秒之后才执行</span>
  &#125;, <span class="hljs-number">0</span>)


  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1000000000</span>; i++) &#123;
    <span class="hljs-keyword">if</span> (i == <span class="hljs-number">999999999</span>) &#123;
      <span class="hljs-built_in">console</span>.log(i);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">hash路由和history路由的区别</h4>
<ul>
<li>hash模式是通过改变锚点(#)来更新页面URL，并不会触发页面重新加载，我们可以通过window.onhashchange监听到hash的改变。 仅仅改变hash，不会改变页面路径，刷新页面无影响</li>
<li>history模式是通过调用window.history对象上的一系列方法来实现页面的无刷新跳转。改变了pathname,刷新页面会以当前路径请求服务器，可能会出现404情况</li>
</ul>
<h5 data-id="heading-21">hash</h5>
<ul>
<li>可以改变URL，但不会触发页面重新加载（hash的改变会记录在window.hisotry中）因此并不算是一次http请求，所以这种模式不利于SEO优化</li>
<li>只能修改#后面的部分，因此只能跳转与当前URL同文档的URL</li>
<li>只能通过字符串改变URL</li>
<li>通过window.onhashchange监听hash的改变，借此实现无刷新跳转的功能</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.location.hash)&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">history</h5>
<ul>
<li>新的URL可以是与当前URL同源的任意 URL，也可以与当前URL一样，但是这样会把重复的一次操作记录到栈中</li>
<li>通过参数stateObject可以添加任意类型的数据到记录中</li>
<li>可额外设置title属性供后续使用</li>
<li>通过pushState、replaceState实现无刷新跳转的功能</li>
<li>需要服务端支持，不然一旦改变history， 刷新页面会导致404</li>
</ul>
<p>window提供popState来监听history change
<strong>可以监听到</strong></p>
<ul>
<li>用户点击浏览器的前进和后退操作</li>
<li>手动调用 history 的 back、forward 和 go 方法</li>
</ul>
<p><strong>监听不到</strong></p>
<ul>
<li>window.history.pushState()</li>
<li>window.history.replaceState()</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-built_in">window</span>.history.pushState(initialObject, title, url)
  <span class="hljs-built_in">window</span>.history.replaceState(initialObject, title, url);

  
  <span class="hljs-built_in">window</span>.history.go(-<span class="hljs-number">1</span>)
  <span class="hljs-built_in">window</span>.history.back();
  <span class="hljs-built_in">window</span>.history.forword() <span class="hljs-comment">// 前进到下一个路由</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">history 用nginx部署</h5>
<p>如果改变了history pathname。刷新页面，出导致nginx出现404，nginx以当前路径请求资源匹配不到时候， 需重定向到 /（index.html） 页面</p>
<h5 data-id="heading-24">前端路由实现原理（history）</h5>
<p><a href="https://zhuanlan.zhihu.com/p/130995492" target="_blank" rel="nofollow noopener noreferrer">深入理解前端中的 hash 和 history 路由</a></p>
<h4 data-id="heading-25">给定数组，求数组元素相加符合等于数字之和的组合</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> combinationSum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">candidates, target</span>) </span>&#123;
    <span class="hljs-keyword">let</span> res=[]
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">arr,sum,index</span>)</span>&#123;
        <span class="hljs-keyword">let</span> num=candidates[index]
        arr=arr.concat(num)
        sum+=num
        <span class="hljs-keyword">if</span>(sum>target)&#123;
            <span class="hljs-comment">//失败</span>
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(sum===target)&#123;
            <span class="hljs-comment">//成功</span>
            res.push(arr)
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=index;i<candidates.length;i++)&#123;
                add(arr,sum,i)
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<candidates.length;i++)&#123;
        add([],<span class="hljs-number">0</span>,i)
    &#125;
    <span class="hljs-keyword">return</span> res
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            