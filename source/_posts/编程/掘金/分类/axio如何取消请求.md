
---
title: 'axio如何取消请求'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1764'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 01:34:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=1764'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第21天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">起源</h2>
<p>某个页面需要下载全部数据的功能，下载数据量大，接口延迟长.....</p>
<p>某个页面加载初始数据量延长长，但单个检索快速，出现初始数据加载中时，检索接口返回，初始数据后续返回覆盖了检索数据的展示....</p>
<p>这些情况需要我们：</p>
<ol>
<li>能够手动取消/终止请求Request。</li>
<li>某些页面接口同时只能有一个在请求。</li>
</ol>
<h2 data-id="heading-1">现状</h2>
<p>系统基于老哥花裤衩开源的vue-element-admin做的二次开发，其中的请求采用的是axios，其中封装的<code>request.js</code>关键代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// create an axios instance</span>
<span class="hljs-keyword">const</span> service = axios.create(&#123;
  <span class="hljs-attr">baseURL</span>: process.env.VUE_APP_BASE_API, <span class="hljs-comment">// url = base url + request url</span>
  <span class="hljs-attr">withCredentials</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// send cookies when cross-domain requests</span>
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">500000</span>, <span class="hljs-comment">// request timeout</span>
  <span class="hljs-attr">transformRequest</span>: [<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-comment">// 对 data 进行任意转换处理</span>
    <span class="hljs-keyword">return</span> Qs.stringify(&#123;
      ...data
    &#125;,
    <span class="hljs-comment">// 数组的转换</span>
    &#123; <span class="hljs-attr">arrayFormat</span>: <span class="hljs-string">'brackets'</span> &#125;)
  &#125;]
&#125;)

<span class="hljs-comment">// request interceptor</span>
service.interceptors.request.use(
  <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-comment">// do something before request is sent</span>

    <span class="hljs-keyword">if</span> (store.getters.token) &#123;
      <span class="hljs-comment">// let each request carry token</span>
      <span class="hljs-comment">// ['X-Token'] is a custom headers key</span>
      <span class="hljs-comment">// please modify it according to the actual situation</span>
      config.headers[<span class="hljs-string">'token'</span>] = getToken()
    &#125;
    <span class="hljs-keyword">return</span> config
  &#125;,
  <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-comment">// do something with request error</span>
    <span class="hljs-built_in">console</span>.log(error) <span class="hljs-comment">// for debug</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发起请求的方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remoteApi</span>(<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-keyword">return</span> request(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/api'</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    data
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">取消请求 cancelToken</h2>
<p>其官方文档：<a href="http://www.axios-js.com/zh-cn/docs/#%E5%8F%96%E6%B6%88" target="_blank" rel="nofollow noopener noreferrer">取消</a>:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> CancelToken = axios.CancelToken;
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
<h2 data-id="heading-3">修改后的请求方法</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remoteApi</span>(<span class="hljs-params">data, cancelToken</span>) </span>&#123;
  <span class="hljs-keyword">return</span> request(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/api'</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    cancelToken,
    data
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际请求时，创建cacelToken：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 组件方法内</span>
<span class="hljs-built_in">this</span>.cancelToken = CancelToken.source()
remoreApi(data, <span class="hljs-built_in">this</span>.cancelToken).then(....).catch(....).finally(....)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要取消请求时，执行：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 组件方法内</span>
<span class="hljs-built_in">this</span>.cancelToken.cancel(<span class="hljs-string">'取消下载'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">避免重复请求</h2>
<p>避免一个接口的重复请求，以免延时长的接口返回数据覆盖另一个接口的返回数据，造成数据显示错误。思路也相对简单，使用一个全局<code>Map</code>存储请求标识与对应的<code>cancelToken</code>。请求，在发起请求前，按照请求标识，唤起对应cancelToken的cancel方法，然后再发出新请求，即可满足条件。</p></div>  
</div>
            