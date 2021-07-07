
---
title: 'Axios如何取消重复请求'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3001'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 06:31:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=3001'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在实际开发中，我们需要对用户发起的重复请求进行拦截处理，比如用户快速点击提交按钮。</p>
<p>对于重复的 get 请求，会导致页面更新多次，发生页面抖动的现象，影响用户体验；对于重复的 post 请求，会导致在服务端生成两次记录（例如生成两条订单记录）。</p>
<p>无论从用户体验或者从业务严谨方面来说，取消无用的请求是需要避免的。</p>
<h1 data-id="heading-0">一、一般处理方式</h1>
<p>我们可以在用户即将发送请求，但还未发送请求时给页面添加一个 loading 效果，提示数据正在加载，loading 会阻止用户继续操作。</p>
<p>这种方式在大部分情况下是可行的，但是在某些情况下却不奏效，比如在 loading 显示之前，用户就已经触发了两次请求的情况。</p>
<h1 data-id="heading-1">二、Axios 拦截器统一处理</h1>
<p>重复发送的请求的场景很多，我们需要在一个公共的地方对请求响应进行处理，Axios 拦截器就闪亮登场了。<br>
Axios 拦截器包括请求拦截器和响应拦截器，可以在请求发送前或响应后进行拦截处理，用法如下：</p>
<pre><code class="copyable">// 添加请求拦截器
axios.interceptors.request.use(
  function (config) &#123;
    // 在发送请求之前做些什么
    return config;
  &#125;,
  function (error) &#123;
    // 对请求错误做些什么
    return Promise.reject(error);
  &#125;
);

// 添加响应拦截器
axios.interceptors.response.use(
  function (response) &#123;
    // 对响应数据做点什么
    return response;
  &#125;,
  function (error) &#123;
    // 对响应错误做点什么
    return Promise.reject(error);
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，如何进行拦截呢？也就是如何取消用户的请求，将它扼杀在摇篮里...</p>
<h1 data-id="heading-2">2.1、如何取消请求</h1>
<p>众所周知，浏览器是通过 XMLHttpRequest 对象进行 http 通信的，如果要取消请求的话，我们可以通过调用 XMLHttpRequest 对象上的 abort 方法来取消请求。</p>
<pre><code class="copyable">let xhr = new XMLHttpRequest();
xhr.open("GET", "http://www.shanzhonglei.com/", true);
xhr.send();
setTimeout(() => xhr.abort(), 300);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Axios是一个主流的http请求库，它提供了两种取消请求的方式。</p>
<p><strong>第一种</strong>，通过axios.CancelToken.source生成取消令牌token和取消方法cancel。</p>
<pre><code class="copyable">const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios.get('/user/12345', &#123;
  cancelToken: source.token
&#125;).catch(function(thrown) &#123;
  if (axios.isCancel(thrown)) &#123;
    console.log('Request canceled', thrown.message);
  &#125; else &#123;
    // handle error
  &#125;
&#125;);

// cancel the request (the message parameter is optional)
source.cancel('Operation canceled by the user.');
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>第二种</strong>，通过axios.CancelToken构造函数生成取消函数。</p>
<pre><code class="copyable">const CancelToken = axios.CancelToken;
let cancel;

axios.get('/user/12345', &#123;
  cancelToken: new CancelToken(function executor(c) &#123;
    // An executor function receives a cancel function as a parameter
    cancel = c;
  &#125;)
&#125;);

// cancel the request
cancel();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是在catch中捕获异常时，应该使用axios.isCancel()判断当前请求是否是主动取消的，以此来区分普通的异常逻辑。</p>
<p>知道了如何取消请求就好办了，如果两个请求是相同的，那么我们就可以对后一个请求进行拦截操作。</p>
<h2 data-id="heading-3">2.2、判断重复请求</h2>
<p>我们可以把每个请求的方法、url 和参数组合成一个字符串，作为该请求的唯一标识 key，与此同时，为对应的 key 生成一个 CancelToken 以备取消当前的请求。把 key 和对应的 cancel 函数以键值对的形式保存在 Map 对象中。</p>
<pre><code class="copyable">const pendingRequest = new Map();
const requestKey = [
  method,
  url,
  JSON.stringify(params),
  JSON.stringify(data),
].join("&");
const cancelToken = new CancelToken(function executor(cancel) &#123;
  if (!pendingRequest.has(requestKey)) &#123;
    pendingRequest.set(requestKey, cancel);
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义pendingRequests 为 map 对象的目的是为了方便我们查询它是否包含某个 key，以及添加和删除 key。</p>
<p>在请求拦截器中，会检查pendingRequests 对象中是否包含当前请求的 requestKey，如果重复，就cancel拦截掉当前请求，如果不重复，则将requestKey 添加到 pendingRequests 对象中。</p>
<h2 data-id="heading-4">2.3 具体实现</h2>
<p>我们先来生成几个辅助函数：</p>
<p><code>generateReqKey</code>：用于根据当前请求的信息，生成请求 Key</p>
<pre><code class="copyable">function generateReqKey(config) &#123;
  const &#123; method, url, params, data &#125; = config;
  return [method, url, JSON.stringify(params), JSON.stringify(data)].join("&");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>addPendingRequest</code>：用于把当前请求信息添加到 pendingRequest 对象中</p>
<pre><code class="copyable">const pendingRequest = new Map();
function addPendingRequest(config) &#123;
  const requestKey = generateReqKey(config);
  config.cancelToken = config.cancelToken || new axios.CancelToken((cancel) => &#123;
    if (!pendingRequest.has(requestKey)) &#123;
       pendingRequest.set(requestKey, cancel);
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>removePendingRequest</code>：检查是否存在重复请求，若存在则取消已发的请求</p>
<pre><code class="copyable">function removePendingRequest(config) &#123;
  const requestKey = generateReqKey(config);
  if (pendingRequest.has(requestKey)) &#123;
    const cancelToken = pendingRequest.get(requestKey);
    cancelToken(requestKey);
    pendingRequest.delete(requestKey);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>clearPending</code> 清空 pending 中的请求（在路由跳转时调用）</p>
<pre><code class="copyable">function clearPending() &#123;
  for (const [requestKey, cancelToken] of pendingRequest) &#123;
    cancelToken(requestKey)
  &#125;
  pendingRequest.clear()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实操来了...</p>
<h3 data-id="heading-5">请求拦截器</h3>
<pre><code class="copyable">axios.interceptors.request.use(
  function (config) &#123;
    removePendingRequest(config); // 检查是否存在重复请求，若存在则取消已发的请求
    addPendingRequest(config); // 把当前请求信息添加到pendingRequest对象中
    return config;
  &#125;,
  (error) => &#123;
    // 这里出现错误可能是网络波动造成的，清空 pendingRequests 对象
    pendingRequests.clear();
    return Promise.reject(error);
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">响应拦截器</h3>
<p>在这里，说明请求已经结束了，状态已经变成pending，这时需要把它从pendingRequests删除。</p>
<pre><code class="copyable">axios.interceptors.response.use(
  (response) => &#123;
    removePendingRequest(response.config); // 从pendingRequest对象中移除请求
    return response;
  &#125;,
  (error) => &#123;
    removePendingRequest(error.config || &#123;&#125;); // 从pendingRequest对象中移除请求
    if (axios.isCancel(error)) &#123;
      console.warn(error);
      return Promise.reject(error);
    &#125; else &#123;
      // 添加其它异常处理
    &#125;
    return Promise.reject(error);
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，我们要在页面切换之前取消上一个路由中未完成的请求，清空缓存的pendingRequest对象。</p>
<pre><code class="copyable">router.beforeEach((to, from, next) => &#123;
  clearPending();
  // ...
  next();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            