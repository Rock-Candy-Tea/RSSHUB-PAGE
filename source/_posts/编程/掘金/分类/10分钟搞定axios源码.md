
---
title: '10分钟搞定axios源码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://cors.zfour.workers.dev/?http://assets.processon.com/chart_image/611d15057d9c0834aa5b784e.png'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 19:37:33 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://assets.processon.com/chart_image/611d15057d9c0834aa5b784e.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先看一张Axios的整体流程图!!!
<img src="https://cors.zfour.workers.dev/?http://assets.processon.com/chart_image/611d15057d9c0834aa5b784e.png" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Axios方法的定义</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Axios</span>(<span class="hljs-params">instanceConfig</span>) </span>&#123;
  <span class="hljs-comment">//接受默认的配置参数</span>
  <span class="hljs-built_in">this</span>.defaults = instanceConfig;
  <span class="hljs-comment">//定义请求和响应的拦截器</span>
  <span class="hljs-built_in">this</span>.interceptors = &#123;
    <span class="hljs-attr">request</span>: <span class="hljs-keyword">new</span> InterceptorManager(),
    <span class="hljs-attr">response</span>: <span class="hljs-keyword">new</span> InterceptorManager()
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在创建Axios对象时会传入一个默认的配置对象，将它赋值给内部的属性最后会和我们自己配置的参数进行合并。然后会定义请求和响应的拦截对象，用户可以手动去添加拦截函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Axios.prototype.request = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-comment">//这里就是对参数进行预处理，因为axios传入参数的方式有好几种</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> config === <span class="hljs-string">'string'</span>) &#123;
    config = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>] || &#123;&#125;;
    config.url = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>];
  &#125; <span class="hljs-keyword">else</span> &#123;
    config = config || &#123;&#125;;
  &#125;
  <span class="hljs-comment">//将我们配置的参数和原始参数进行合并</span>
  config = mergeConfig(<span class="hljs-built_in">this</span>.defaults, config);

  <span class="hljs-comment">// Set config.method</span>
  <span class="hljs-keyword">if</span> (thod) &#123;
    config.methconfig.meod = config.method.toLowerCase();
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.defaults.method) &#123;
    config.method = <span class="hljs-built_in">this</span>.defaults.method.toLowerCase();
  &#125; <span class="hljs-keyword">else</span> &#123;
    config.method = <span class="hljs-string">'get'</span>;
  &#125;

  <span class="hljs-comment">// chain数组用来保存对config或者result处理的函数，同时这些处理函数都是成对出现的，默认传入的是dispatchRequest和undefine，dispatchRequest内部会发起真正XML的请求。</span>
  <span class="hljs-keyword">var</span> chain = [dispatchRequest, <span class="hljs-literal">undefined</span>];
  <span class="hljs-keyword">var</span> promise = <span class="hljs-built_in">Promise</span>.resolve(config);
<span class="hljs-comment">//将用户添加的请求拦截函数放入chain中，此时放入的是队头，因为它要在请求发起前执行。</span>
  <span class="hljs-built_in">this</span>.interceptors.request.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unshiftRequestInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;
    chain.unshift(interceptor.fulfilled, interceptor.rejected);
  &#125;);
<span class="hljs-comment">//将用户添加的响应拦截函数放入chain中，此时放入的是队尾，因为这是要对返回的数据进行处理。</span>
  <span class="hljs-built_in">this</span>.interceptors.response.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushResponseInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;
    chain.push(interceptor.fulfilled, interceptor.rejected);
  &#125;);
  <span class="hljs-comment">//循环执行，最终promise拿到的就是最终的数据</span>
  <span class="hljs-keyword">while</span> (chain.length) &#123;
    promise = promise.then(chain.shift(), chain.shift());
  &#125;

  <span class="hljs-keyword">return</span> promise;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Axios中的request方法其实就是做了三件事：</p>
<ul>
<li>对用户传进来的配置参数进行合并</li>
<li>将用户配置的请求拦截和响应拦截添加到执行队列中</li>
<li>执行请求拦截函数---->发起请求----->执行响应拦截函数</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//将['delete', 'get', 'head', 'options']方法加入到Axios的原型中</span>
utils.forEach([<span class="hljs-string">'delete'</span>, <span class="hljs-string">'get'</span>, <span class="hljs-string">'head'</span>, <span class="hljs-string">'options'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEachMethodNoData</span>(<span class="hljs-params">method</span>) </span>&#123;
  Axios.prototype[method] = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">url, config</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(utils.merge(config || &#123;&#125;, &#123;
      <span class="hljs-attr">method</span>: method,
      <span class="hljs-attr">url</span>: url
    &#125;));
  &#125;;
&#125;);
<span class="hljs-comment">//将['post', 'put', 'patch']方法加入到Axios的原型中</span>
utils.forEach([<span class="hljs-string">'post'</span>, <span class="hljs-string">'put'</span>, <span class="hljs-string">'patch'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEachMethodWithData</span>(<span class="hljs-params">method</span>) </span>&#123;
  Axios.prototype[method] = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">url, data, config</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(utils.merge(config || &#123;&#125;, &#123;
      <span class="hljs-attr">method</span>: method,
      <span class="hljs-attr">url</span>: url,
      <span class="hljs-attr">data</span>: data
    &#125;));
  &#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里其实就是讲我们常用的一些请求方法加入到Axios的原型中，这样我们就行直接通过调用axios对象上的请求方法发起请求，比如<code>axios.get('xxx', &#123;&#125;)</code>，其实最终调用还是我们的Axios上的request方法。</p>
<blockquote>
<p>axios对象的创建</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createInstance</span>(<span class="hljs-params">defaultConfig</span>) </span>&#123;
  <span class="hljs-comment">//创建axios对象，将默认配置参数传入</span>
  <span class="hljs-keyword">var</span> context = <span class="hljs-keyword">new</span> Axios(defaultConfig);
  <span class="hljs-comment">//通过bind方法重新创建一个函数，并向将Axios原型上的方法和属性复制给这个函数</span>
  <span class="hljs-keyword">var</span> instance = bind(Axios.prototype.request, context);
  utils.extend(instance, Axios.prototype, context);
  utils.extend(instance, context);
  <span class="hljs-keyword">return</span> instance;
&#125;
<span class="hljs-comment">//创建请求方法，这个对象就是我们最终发送请求使用的方法，这一提醒下axios是一个函数。</span>
<span class="hljs-keyword">var</span> axios = createInstance(defaults);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>createInstance函数的目的首先明确一下：<code>它创建出来的是一个函数，我们可以直接调用这个函数或者原型上的请求方法发送请求</code>，下面详细讲解下过程：</p>
<ul>
<li>
<p>创建一个axios对象，将我们的默认配置参数传入</p>
</li>
<li>
<p>调用bind函数，创建一个新的函数，函数的返回值是执行Axios.request后的返回值，其实bind实现很简单：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bind</span>(<span class="hljs-params">fn, thisArg</span>)</span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrap</span>(<span class="hljs-params">...args</span>)</span>&#123;
<span class="hljs-keyword">return</span> fn.apply(thisArg,args);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>args就是我们发送请求时配置的参数，最终aegs会交给Axios.request函数，而之所以我们最后能使用<code>axios.get()</code>发送请求是因为我们将Axios原型上的方法复制给了wrap函数，也就是上面的extend函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.Cancel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/Cancel'</span>);
axios.CancelToken = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/CancelToken'</span>);
axios.isCancel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/isCancel'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一块就是向axios上添加取消请求的方法，让我们能够中断发送的请求，具体实现后面会介绍。</p>
</li>
</ul>
<blockquote>
<p>调用dispatchRequest发起请求</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">  config.data = transformData(
    config.data,
    config.headers,
    config.transformRequest
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先是将我们传入的参数进行转换，<code>axios.defaults.transformRequest</code> 数组中默认就有一个函数，他会根据我们参数的类型进行不同的转换，比如我们将**&#123;"name":"zhangsan","age":12&#125;**作为参数传入，最终结果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1307d2c66ceb4dd38a3d2d98aa46dd10~tplv-k3u1fbpfcp-watermark.image" alt="image-20210819220851881.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>他会被转换成JSON字符串。如果我们想自定义转换函数可以通过concat链接自定义的函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.get(<span class="hljs-string">'xxxx'</span>, &#123;
  <span class="hljs-attr">transformResponse</span>: axios.defaults.transformResponse.concat(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data, headers</span>) </span>&#123;
    <span class="hljs-comment">//....</span>
    <span class="hljs-keyword">return</span> data;
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>transformData</code>执行的时候就会遍历axios.defaults.transformRequest数组中的转换函数对数据进行转换，接下来就是发送请求。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">return</span> adapter(config).then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onAdapterResolution</span>(<span class="hljs-params">response</span>) </span>&#123;
    throwIfCancellationRequested(config);
    <span class="hljs-comment">//....对response进行处理</span>
    <span class="hljs-keyword">return</span> response;
  &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onAdapterRejection</span>(<span class="hljs-params">reason</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!isCancel(reason)) &#123;
      throwIfCancellationRequested(config);

      <span class="hljs-comment">// Transform response data</span>
      <span class="hljs-keyword">if</span> (reason && reason.response) &#123;
        <span class="hljs-comment">//...对reason进行处理</span>
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(reason);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里最关键的其实就是调用<code>adapter</code>函数发送请求，然后对返回的数据进行处理，也就是说dispatchRequest函数最终返回的是一个Promise，我们可以通过调用其then方法拿到数据。</p>
<blockquote>
<p>adapter方法</p>
</blockquote>
<p>首先我们来追溯下dispatchRequest中调用的<code>adapter</code>是怎么拿到的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> adapter = config.adapter || defaults.adapter;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到这里就明白了，adapter是从我们的config中拿到的，默认情况下config上的adapter就是从默认配置中继承过来的，下面看下defaults.adapter是怎么的来的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> defaults = &#123;
<span class="hljs-attr">adapter</span>: getDefaultAdapter(), 
    <span class="hljs-comment">//.....</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDefaultAdapter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> adapter;
  <span class="hljs-comment">//根据XMLHttpRequest判断当前是不是浏览器环境，如果不是就根据process判断是不是在node环境</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> XMLHttpRequest !== <span class="hljs-string">'undefined'</span>) &#123;
    adapter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./adapters/xhr'</span>);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> process !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">Object</span>.prototype.toString.call(process) === <span class="hljs-string">'[object process]'</span>) &#123;
    adapter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./adapters/http'</span>);
  &#125;
  <span class="hljs-keyword">return</span> adapter;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从getDefaultAdapter中我们就能知道axios是支持浏览器和node环境的，如果是在浏览器环境就引入<code>XMLHttpRequest</code>，如果是node环境就引入<code>http</code>，下面主要探究浏览器环境。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">xhrAdapter</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatchXhrRequest</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-comment">//...数据处理</span>
    <span class="hljs-keyword">var</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest();
<span class="hljs-comment">//...</span>
    request.open();
    <span class="hljs-comment">//设置超时时间</span>
    request.timeout = config.timeout;
    request.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleLoad</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">//...处理返回的数据</span>
      settle(resolve, reject, response);
      request = <span class="hljs-literal">null</span>;
    &#125;;
    <span class="hljs-comment">//监听中断操作</span>
    request.onabort = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleAbort</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
    <span class="hljs-comment">//监听错误</span>
    request.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleError</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
    <span class="hljs-comment">//监听超时</span>
    request.ontimeout = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleTimeout</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
    <span class="hljs-keyword">if</span> (requestData === <span class="hljs-literal">undefined</span>) &#123;
      requestData = <span class="hljs-literal">null</span>;
    &#125;
    request.send(requestData);
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面就是XML请求的大致过程，从上面我们可以知道axios内部可以进行<code>错误处理</code>、<code>请求拦截</code>、<code>中断请求</code>、<code>请求超时处理</code>等功能，下面会介绍一下实现的其他功能。</p>
<p><strong>withCredentials ：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">if</span> (!utils.isUndefined(config.withCredentials)) &#123;
      request.withCredentials = !!config.withCredentials;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>了解过CORS的同学应该对withCredentials不陌生，这个属性是一个布尔值，用来设置在进行跨域请求时是否携带授权信息，比如<code>cookie</code>或授权<code>header</code>头。</p>
<p><strong>监听上传和下载进度：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//监听下载进度    </span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> config.onDownloadProgress === <span class="hljs-string">'function'</span>) &#123;
      request.addEventListener(<span class="hljs-string">'progress'</span>, config.onDownloadProgress);
&#125;
<span class="hljs-comment">//监听上传进度</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> config.onUploadProgress === <span class="hljs-string">'function'</span> && request.upload) &#123;
      request.upload.addEventListener(<span class="hljs-string">'progress'</span>, config.onUploadProgress);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>progress是XML自带的一个事件，当请求接受到更多数据时，会周期性的触发，我们在定义config的时候可以自定义上传或者下载事件，然后通过event对象可以知道上传或者下载的进度。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.post(action, formData, &#123;
   <span class="hljs-attr">onUploadProgress</span>: <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
       <span class="hljs-comment">//获取当前上体积与总体积</span>
       <span class="hljs-keyword">let</span> percentage = <span class="hljs-built_in">Math</span>.round((e.loaded * <span class="hljs-number">100</span>) / e.total) || <span class="hljs-number">0</span>;
       <span class="hljs-keyword">if</span>(percentage < <span class="hljs-number">100</span>) &#123;
            <span class="hljs-comment">//....进度条展示当前进度</span>
       &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>中断请求：</strong></p>
<p><img src="https://cors.zfour.workers.dev/?http://assets.processon.com/chart_image/611f1957079129553ebe5491.png" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先看个例子，怎么去中断请求：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> CancelToken = axios.CancelToken;
<span class="hljs-keyword">const</span> source = CancelToken.source();
axios.get(<span class="hljs-string">'xxxxx'</span>, &#123;
  <span class="hljs-attr">cancelToken</span>: source.token
&#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res)
&#125;).catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(err);
&#125;);
source.cancel(<span class="hljs-string">'中断请求'</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从代码中可以知道我们首先需要给我们的请求配置上<code>cancelToken</code>这个属性，然后就可以在请求返回之前随时调用<code>cancel</code>方法中断请求，</p>
<p>下面一步一步来解析这个过程。</p>
<ul>
<li>
<p>获取CancelToken</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.CancelToken = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/CancelToken'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在知道了，axios上的CancelToken就是从<code>./cancel/CancelToken</code>这个模块中导出来的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CancelToken</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-keyword">var</span> resolvePromise;
  <span class="hljs-built_in">this</span>.promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promiseExecutor</span>(<span class="hljs-params">resolve</span>) </span>&#123;
    resolvePromise = resolve;
  &#125;);
  <span class="hljs-keyword">var</span> token = <span class="hljs-built_in">this</span>;
  executor(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cancel</span>(<span class="hljs-params">message</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (token.reason) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;
    token.reason = <span class="hljs-keyword">new</span> Cancel(message);
    resolvePromise(token.reason);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原来CancelToken是一个方法，这个方法就是在<code>this</code>上绑定了一个promise，根据以往的经验这个this要么指向调用CancelToken的实例，要么指向new出来的新对象，暂时先放着。</p>
<p>接着执行executor函数，这个函数里面传递了一个cancel方法，其实这个cancel方法就是用户调用的cancel方法。</p>
<p>在cancel方法中我们看到它调用了promise的resolve方法将<code>message</code>抛出去，看到这里可以再去看下上面的流程图。</p>
</li>
<li>
<p>执行CancelToken.source</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">CancelToken.source = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">source</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> cancel;
  <span class="hljs-keyword">var</span> token = <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">executor</span>(<span class="hljs-params">c</span>) </span>&#123;
    cancel = c;
  &#125;);
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">token</span>: token,
    <span class="hljs-attr">cancel</span>: cancel
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>source方法首先帮我们new了一个新实例token，现在就知道了上面的<code>this</code>指向的就是这个新实例，也就是说token上有一个pending状态的promise，等待用户去触发cancel。</p>
<p>这个函数返回的一个是token，这个token会作为config的CancelToken属性的值，另一个返回值就是cancel函数，也就是CancelToken中executor函数传递过来的参数。</p>
</li>
<li>
<p>执行cancel函数</p>
<p>我们现在知道执行cancel目的就是让CancelToken中的promise的状态从pendinig变为resolve状态，那这有啥用呢？因为我们生成的token最终会作为CancelToken属性的值传入，所以我们看看最终是怎么处理CancelToken属性的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (config.cancelToken) &#123;
      config.cancelToken.promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onCanceled</span>(<span class="hljs-params">cancel</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (!request) &#123;
          <span class="hljs-keyword">return</span>;
        &#125;

        request.abort();
        reject(cancel);
        request = <span class="hljs-literal">null</span>;
      &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在应该可以恍然大悟了，在执行xml请求时会执行这段代码，如果我们配置了CancelToken就会进入判断条件里面，里面就会调用<code>cancelToken.promise.then</code>，如果用户不调用cancel方法让<code>cancelToken.promise</code>从pending状态变为resolve状态，那么他的then方法就不会被执行，也就不会影响正常的请求。</p>
<p>如果我们调用了cancel方法，那么就会执行then方法中的代码，我们看到，里面就触发了xml的<strong>abort</strong>函数，同时执行了<code>reject</code>函数，我们知道axios最终的返回值就是一个promise，这里的<code>reject</code>对应的就是这个promise。</p>
</li>
</ul>
<blockquote>
<p>总结</p>
</blockquote>
<p>axios是一个非常强大的库，一般日常开发都会使用，同时里面的一点调用逻辑也是值得去学习的，比如说最后的cancel逻辑，他将axios返回的promise控制权交给用户，当用户想终止可以直接触发他的reject方法。</p></div>  
</div>
            