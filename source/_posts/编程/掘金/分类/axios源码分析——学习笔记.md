
---
title: 'axios源码分析——学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33de11d4574541728e571e478aa57c7d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 06:14:46 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33de11d4574541728e571e478aa57c7d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">写在前面</h1>
<p>本文章是axios学习源码的笔记文章，原视频是尚硅谷的axios教学视频，链接如下：<a href="https://www.bilibili.com/video/BV1NJ41197u6?p=1" target="_blank" rel="nofollow noopener noreferrer">www.bilibili.com/video/BV1NJ…</a></p>
<h1 data-id="heading-1">axios与Axios的关系</h1>
<ol>
<li>Axios是构造函数，axios是一个函数</li>
<li>语法上来说axios不是由Axios构建的实例，但是功能上来说axios具有Axios实例的功能（属性和方法）</li>
<li>axios是Axios.prototype.request函数bind()返回的函数</li>
</ol>
<p>图解：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33de11d4574541728e571e478aa57c7d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">axios与 axios.create返回的instance区别</h1>
<ol>
<li>axios多了create，CancelToken，all等方法</li>
<li>axios和instance的配置（axios.defaults+createConfig）可能不一样</li>
</ol>
<p>axios.js代码段：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createInstance</span>(<span class="hljs-params">defaultConfig</span>) </span>&#123;
  <span class="hljs-comment">//创建Axios实例对象context</span>
  <span class="hljs-keyword">var</span> context = <span class="hljs-keyword">new</span> Axios(defaultConfig);
  <span class="hljs-comment">//将Axios.prototype.request函数的this指向绑定context，</span>
  <span class="hljs-comment">//并将该新函数返回赋值给instance</span>
  <span class="hljs-keyword">debugger</span>
  <span class="hljs-keyword">var</span> instance = bind(Axios.prototype.request, context);

  <span class="hljs-comment">//将原型上的方法添加到instance上</span>
  utils.extend(instance, Axios.prototype, context);

  <span class="hljs-comment">// 将context（Axios原型实例）上的属性（defaults和interceptors）添加到instance上</span>
  utils.extend(instance, context);

  <span class="hljs-keyword">return</span> instance;
&#125;

<span class="hljs-comment">// 创建axios用于模块输出（调用了createInstance）</span>
<span class="hljs-keyword">var</span> axios = createInstance(defaults);

<span class="hljs-comment">// Expose Axios class to allow class inheritance</span>
<span class="hljs-comment">//将Axios类暴露，从而实现类的继承</span>
axios.Axios = Axios;

<span class="hljs-comment">// 定义create方法</span>
axios.create = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">instanceConfig</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createInstance(mergeConfig(axios.defaults, instanceConfig));
&#125;;

<span class="hljs-comment">// Expose Cancel & CancelToken</span>
axios.Cancel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/Cancel'</span>);
axios.CancelToken = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/CancelToken'</span>);
axios.isCancel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/isCancel'</span>);

<span class="hljs-comment">// Expose all/spread</span>
axios.all = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">all</span>(<span class="hljs-params">promises</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(promises);
&#125;;
axios.spread = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./helpers/spread'</span>);

<span class="hljs-comment">// Expose isAxiosError</span>
axios.isAxiosError = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./helpers/isAxiosError'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">axios运行的整体流程</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c70acd9e8b84dd7b25cdeca7773eb56~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
从图中可以看出axios运行时最重要的三个函数：request(config) => dispatchRequest(config) => xhrAdapter(config)</p>
<h2 data-id="heading-4">request</h2>
<p>代码段：</p>
<pre><code class="hljs language-js copyable" lang="js">Axios.prototype.request = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-comment">/*eslint no-param-reassign:0*/</span>
  <span class="hljs-comment">// Allow for axios('example/url'[, config]) a la fetch API</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> config === <span class="hljs-string">'string'</span>) &#123;
    config = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>] || &#123;&#125;;
    config.url = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>];
  &#125; <span class="hljs-keyword">else</span> &#123;
    config = config || &#123;&#125;;
  &#125;

  config = mergeConfig(<span class="hljs-built_in">this</span>.defaults, config);

  <span class="hljs-comment">// Set config.method</span>
  <span class="hljs-keyword">if</span> (config.method) &#123;
    config.method = config.method.toLowerCase();
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.defaults.method) &#123;
    config.method = <span class="hljs-built_in">this</span>.defaults.method.toLowerCase();
  &#125; <span class="hljs-keyword">else</span> &#123;
    config.method = <span class="hljs-string">'get'</span>;
  &#125;

  <span class="hljs-comment">// Hook up interceptors middleware</span>
  <span class="hljs-keyword">var</span> chain = [dispatchRequest, <span class="hljs-literal">undefined</span>];
  <span class="hljs-keyword">var</span> promise = <span class="hljs-built_in">Promise</span>.resolve(config);

  <span class="hljs-built_in">this</span>.interceptors.request.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unshiftRequestInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;
    chain.unshift(interceptor.fulfilled, interceptor.rejected);
  &#125;);

  <span class="hljs-built_in">this</span>.interceptors.response.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushResponseInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;
    chain.push(interceptor.fulfilled, interceptor.rejected);
  &#125;);

  <span class="hljs-keyword">while</span> (chain.length) &#123;
    promise = promise.then(chain.shift(), chain.shift());
  &#125;

  <span class="hljs-keyword">return</span> promise;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>request函数的代码最主要的部分如下，这是request函数逻辑的重要实现部分：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> chain = [dispatchRequest, <span class="hljs-literal">undefined</span>];
  <span class="hljs-keyword">var</span> promise = <span class="hljs-built_in">Promise</span>.resolve(config);

  <span class="hljs-built_in">this</span>.interceptors.request.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unshiftRequestInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;
    chain.unshift(interceptor.fulfilled, interceptor.rejected);
  &#125;);

  <span class="hljs-built_in">this</span>.interceptors.response.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushResponseInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;
    chain.push(interceptor.fulfilled, interceptor.rejected);
  &#125;);

  <span class="hljs-keyword">while</span> (chain.length) &#123;
    promise = promise.then(chain.shift(), chain.shift());
  &#125;

  <span class="hljs-keyword">return</span> promise;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码首先定义了一个chain数组，通过数组的unshift方法和push方法，分别将请求拦截器的回调函数推入chain的左边，将响应拦截器的回调函数推入chain的右边，而chain的中间是dispatchRequest函数。之后通过从左往右弹出chain数组元素进行promise链式调用完成了从请求拦截器到响应拦截器之间的工作。
举一个例子，我们准备了两个请求拦截器requestInt1和requestInt2，两个响应拦截器responseInt1和responseInt2，用图来解释这四个拦截器是如何放入chain数组中以及最后如何被链式调用的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98edac89ffee483386d937c5f8b29036~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
由图可知，由于promise链式调用是两两一组（拦截器的成功回调+失败回调），所以chain数组初始定义了一个undefined和dispatchRequest组合防止链式调用时乱序。</p>
<h2 data-id="heading-5">dispatchRequest</h2>
<h3 data-id="heading-6">dispatchRequest模块的流程</h3>
<p>转换请求数据 => 调用xhrAdapter()发请求 => 请求返回后转换响应数据并返回promise对象</p>
<h4 data-id="heading-7">转换请求数据</h4>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// Transform request data</span>
  config.data = transformData(
    config.data,
    config.headers,
    config.transformRequest
  );
 <span class="hljs-comment">// Flatten headers</span>
  config.headers = utils.merge(
    config.headers.common || &#123;&#125;,
    config.headers[config.method] || &#123;&#125;,
    config.headers
  );

<span class="copy-code-btn">复制代码</span></code></pre>
<p>该部分主要用于转换的函数为defaults模块的transformRequest函数，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">transformRequest: [<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformRequest</span>(<span class="hljs-params">data, headers</span>) </span>&#123;
    normalizeHeaderName(headers, <span class="hljs-string">'Accept'</span>);
    normalizeHeaderName(headers, <span class="hljs-string">'Content-Type'</span>);
    <span class="hljs-keyword">if</span> (utils.isFormData(data) ||
      utils.isArrayBuffer(data) ||
      utils.isBuffer(data) ||
      utils.isStream(data) ||
      utils.isFile(data) ||
      utils.isBlob(data)
    ) &#123;
      <span class="hljs-keyword">return</span> data;
    &#125;
    <span class="hljs-keyword">if</span> (utils.isArrayBufferView(data)) &#123;
      <span class="hljs-keyword">return</span> data.buffer;
    &#125;
    <span class="hljs-keyword">if</span> (utils.isURLSearchParams(data)) &#123;
      setContentTypeIfUnset(headers, <span class="hljs-string">'application/x-www-form-urlencoded;charset=utf-8'</span>);
      <span class="hljs-keyword">return</span> data.toString();
    &#125;
    <span class="hljs-keyword">if</span> (utils.isObject(data)) &#123;
      setContentTypeIfUnset(headers, <span class="hljs-string">'application/json;charset=utf-8'</span>);
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.stringify(data);
    &#125;
    <span class="hljs-keyword">return</span> data;
  &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">请求返回后转换响应数据</h4>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> adapter = config.adapter || defaults.adapter;

  <span class="hljs-keyword">return</span> adapter(config).then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onAdapterResolution</span>(<span class="hljs-params">response</span>) </span>&#123;
    throwIfCancellationRequested(config);

    <span class="hljs-comment">// Transform response data</span>
    response.data = transformData(
      response.data,
      response.headers,
      config.transformResponse
    );

    <span class="hljs-keyword">return</span> response;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这部分的代码在adapter调用之后的promise回调中，用于转换的函数是defaults模块的transformResponse函数。</p>
<pre><code class="hljs language-js copyable" lang="js">  transformResponse: [<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformResponse</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-comment">/*eslint no-param-reassign:0*/</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'string'</span>) &#123;
      <span class="hljs-keyword">try</span> &#123;
        data = <span class="hljs-built_in">JSON</span>.parse(data);
      &#125; <span class="hljs-keyword">catch</span> (e) &#123; <span class="hljs-comment">/* Ignore */</span> &#125;
    &#125;
    <span class="hljs-keyword">return</span> data;
  &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一开始作者不理解这一块的逻辑，后来试了一下，发现JSON数据的类型就是string格式，如果data是一个非JSON格式的字符串，则这段会报错，因此该函数选择了try cache的结构来防止程序报错。</p>
<h2 data-id="heading-9">xhrAdapter</h2>
<h3 data-id="heading-10">xhrAdapter模块的流程</h3>
<p>创建XHR对象（最底层，调用AJAX），根据config进行相应设置，发送特定请求，接受相应数据，返回promise。xhrAdapter模块的主要代码如下（从xhr.open到onreadystatechange部分）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">xhrAdapter</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatchXhrRequest</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">var</span> requestData = config.data;
    <span class="hljs-keyword">var</span> requestHeaders = config.headers;

    <span class="hljs-keyword">if</span> (utils.isFormData(requestData)) &#123;
      <span class="hljs-keyword">delete</span> requestHeaders[<span class="hljs-string">'Content-Type'</span>]; <span class="hljs-comment">// Let the browser set it</span>
    &#125;

    <span class="hljs-keyword">var</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest();

    <span class="hljs-comment">// HTTP basic authentication</span>
    <span class="hljs-keyword">if</span> (config.auth) &#123;
      <span class="hljs-keyword">var</span> username = config.auth.username || <span class="hljs-string">''</span>;
      <span class="hljs-keyword">var</span> password = config.auth.password ? <span class="hljs-built_in">unescape</span>(<span class="hljs-built_in">encodeURIComponent</span>(config.auth.password)) : <span class="hljs-string">''</span>;
      requestHeaders.Authorization = <span class="hljs-string">'Basic '</span> + btoa(username + <span class="hljs-string">':'</span> + password);
    &#125;

    <span class="hljs-keyword">var</span> fullPath = buildFullPath(config.baseURL, config.url);
    request.open(config.method.toUpperCase(), buildURL(fullPath, config.params, config.paramsSerializer), <span class="hljs-literal">true</span>);

    <span class="hljs-comment">// Set the request timeout in MS</span>
    request.timeout = config.timeout;

    <span class="hljs-comment">// Listen for ready state</span>
    request.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleLoad</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (!request || request.readyState !== <span class="hljs-number">4</span>) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;

      <span class="hljs-comment">// The request errored out and we didn't get a response, this will be</span>
      <span class="hljs-comment">// handled by onerror instead</span>
      <span class="hljs-comment">// With one exception: request that using file: protocol, most browsers</span>
      <span class="hljs-comment">// will return status as 0 even though it's a successful request</span>
      <span class="hljs-keyword">if</span> (request.status === <span class="hljs-number">0</span> && !(request.responseURL && request.responseURL.indexOf(<span class="hljs-string">'file:'</span>) === <span class="hljs-number">0</span>)) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;

      <span class="hljs-comment">// Prepare the response</span>
      <span class="hljs-keyword">var</span> responseHeaders = <span class="hljs-string">'getAllResponseHeaders'</span> <span class="hljs-keyword">in</span> request ? parseHeaders(request.getAllResponseHeaders()) : <span class="hljs-literal">null</span>;
      <span class="hljs-keyword">var</span> responseData = !config.responseType || config.responseType === <span class="hljs-string">'text'</span> ? request.responseText : request.response;
      <span class="hljs-keyword">var</span> response = &#123;
        <span class="hljs-attr">data</span>: responseData,
        <span class="hljs-attr">status</span>: request.status,
        <span class="hljs-attr">statusText</span>: request.statusText,
        <span class="hljs-attr">headers</span>: responseHeaders,
        <span class="hljs-attr">config</span>: config,
        <span class="hljs-attr">request</span>: request
      &#125;;

      settle(resolve, reject, response);

      <span class="hljs-comment">// Clean up request</span>
      request = <span class="hljs-literal">null</span>;
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到该部分返回一个Promise对象，而该对象状态的判定交给了settle函数，该部分函数代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">settle</span>(<span class="hljs-params">resolve, reject, response</span>) </span>&#123;
  <span class="hljs-keyword">var</span> validateStatus = response.config.validateStatus;
  <span class="hljs-keyword">if</span> (!response.status || !validateStatus || validateStatus(response.status)) &#123;
    resolve(response);
  &#125; <span class="hljs-keyword">else</span> &#123;
    reject(createError(
      <span class="hljs-string">'Request failed with status code '</span> + response.status,
      response.config,
      <span class="hljs-literal">null</span>,
      response.request,
      response
    ));
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该部分的validateStatus是axios的config设定，定义了返回状态码的合法范围，默认范围为[200,299]。</p>
<h1 data-id="heading-11">取消请求</h1>
<p>axios取消请求的实现牵涉到config中的canceltoken的配置，先来看看canceltoken的用法(cancel函数可以传入参数--取消原因)：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CancelToken = axios.CancelToken;
<span class="hljs-keyword">let</span> cancel;

axios.get(<span class="hljs-string">'/user/12345'</span>, &#123;
  <span class="hljs-attr">cancelToken</span>: <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">executor</span>(<span class="hljs-params">c</span>) </span>&#123;
    <span class="hljs-comment">// An executor function receives a cancel function as a parameter</span>
    cancel = c;
  &#125;)
&#125;);

<span class="hljs-comment">// cancel the request</span>
cancel();

<span class="copy-code-btn">复制代码</span></code></pre>
<p>CancelTOken部分的源码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CancelToken</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> executor !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'executor must be a function.'</span>);
  &#125;
  <span class="hljs-comment">//为取消请求准备了一个Promise对象promise，并把该对象的resolve函数存到外面</span>
  <span class="hljs-keyword">var</span> resolvePromise;
  <span class="hljs-built_in">this</span>.promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promiseExecutor</span>(<span class="hljs-params">resolve</span>) </span>&#123;
    resolvePromise = resolve;
  &#125;);
  <span class="hljs-comment">//保存当前的token对象</span>
  <span class="hljs-keyword">var</span> token = <span class="hljs-built_in">this</span>;
  executor(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cancel</span>(<span class="hljs-params">message</span>) </span>&#123;
    <span class="hljs-comment">//如果token中已有reason属性，说明取消已经被请求过</span>
    <span class="hljs-keyword">if</span> (token.reason) &#123;
      <span class="hljs-comment">// Cancellation has already been requested</span>
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-comment">//token.reason指定为一个Cancel对象</span>
    token.reason = <span class="hljs-keyword">new</span> Cancel(message);
    resolvePromise(token.reason);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用executor函数的参数，这里很巧妙地将CancelToken内部定义好的cancel函数传递给外部调用者，在需要取消请求时调用cancel函数，使得resolvePromise的状态变为fulfilled，值为reason。
而CancelToken的实例对象的canceltoken的promisethen方法的调用写在了xhr.js里面：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">if</span> (config.cancelToken) &#123;
      <span class="hljs-comment">// Handle cancellation</span>
      config.cancelToken.promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onCanceled</span>(<span class="hljs-params">cancel</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (!request) &#123;
          <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//取消请求</span>
        request.abort();
        <span class="hljs-comment">//让请求的promise失败</span>
        reject(cancel);
        <span class="hljs-comment">// Clean up request</span>
        request = <span class="hljs-literal">null</span>;
      &#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，该部分的cancel不是之前的cancel函数，而是一个Cancel对象，是CancelToken.js模块的token.reason。
调用cancel()的具体细节如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00bdb04fb3664b7bbb5463971a937b8e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            