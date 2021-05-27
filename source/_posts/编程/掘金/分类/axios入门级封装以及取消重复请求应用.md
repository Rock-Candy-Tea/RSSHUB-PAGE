
---
title: 'axios入门级封装以及取消重复请求应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3295'
author: 掘金
comments: false
date: Thu, 27 May 2021 00:04:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=3295'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">axios封装以及取消重复请求应用</h1>
<h2 data-id="heading-1">封装代码</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// axios.js</span>
<span class="hljs-comment">// 封装axios请求,返回重新封装的数据格式</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> errHandle <span class="hljs-keyword">from</span> <span class="hljs-string">'./errHandle'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HttpRequest</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">baseUrl</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.baseUrl = baseUrl
  &#125;

  getInsideConfig () &#123;
    <span class="hljs-keyword">const</span> config = &#123;
      <span class="hljs-attr">baseURL</span>: <span class="hljs-built_in">this</span>.baseUrl,
      <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json;charset=utf-8'</span>
      &#125;,
      <span class="hljs-attr">timeout</span>: <span class="hljs-number">10000</span>
    &#125;
    <span class="hljs-keyword">return</span> config
  &#125;

  <span class="hljs-comment">// 设定拦截器</span>
  interceptors (instance) &#123;
    <span class="hljs-comment">// 添加请求拦截器</span>
    instance.interceptors.request.use(<span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
        <span class="hljs-comment">// 如果有token 的话 在header添加token 如果没有（登录的情况）就不传</span>
     <span class="hljs-keyword">if</span> () &#123;
            config.headers.Authorization = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">window</span>.localStorage.getItem(<span class="hljs-string">"Login"</span>)).token
     &#125;
        
      <span class="hljs-keyword">return</span> config
    &#125;, <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
      <span class="hljs-comment">// 对错误的统一处理</span>
      <span class="hljs-comment">// 对请求错误做些什么</span>
      errHandle(error)
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
    &#125;)

    <span class="hljs-comment">// 添加响应拦截器</span>
    instance.interceptors.response.use(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (res.status === <span class="hljs-number">200</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(res.data)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(res)
      &#125;
      <span class="hljs-comment">// 对响应数据做点什么</span>
    &#125;, <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
      <span class="hljs-comment">// debugger</span>
      errHandle(error)
      <span class="hljs-comment">// 对响应错误做点什么</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
    &#125;)
  &#125;

  <span class="hljs-comment">// 创建实例</span>
  request (options) &#123;
    <span class="hljs-keyword">const</span> instance = axios.create()
    <span class="hljs-keyword">const</span> newOptions = <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>.getInsideConfig(), options)
    <span class="hljs-built_in">this</span>.interceptors(instance)
    <span class="hljs-keyword">return</span> instance(newOptions)
  &#125;

  get (url, config) &#123;
    <span class="hljs-keyword">const</span> options = <span class="hljs-built_in">Object</span>.assign(&#123;
      <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
      url
    &#125;, config)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(options)
  &#125;

  post (url, data) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(&#123;
      <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
      url,
      data
    &#125;)
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> HttpRequest

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// request.js</span>
<span class="hljs-keyword">import</span> HttpRequest <span class="hljs-keyword">from</span> <span class="hljs-string">'./axios'</span>
<span class="hljs-keyword">import</span> config <span class="hljs-keyword">from</span> <span class="hljs-string">'./../config'</span>

<span class="hljs-comment">// 根据不同环境 不同的请求url</span>
<span class="hljs-keyword">const</span> baseUrl = process.env.NODE_ENV === <span class="hljs-string">'development'</span> ? config.baseUrl.dev
  : config.baseUrl.prod

<span class="hljs-keyword">const</span> axios = <span class="hljs-keyword">new</span> HttpRequest(baseUrl)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> axios
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">取消重复请求应用</h2>
<p>开发项目中，在处理<strong>长列表</strong>点击加载更多，需要考虑到用户网速比较慢的情况，在请求还没有到达之前，如果再次点击加载更多，需要对这种重复请求进行取消。</p>
<p><code>axios.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CancelToken = axios.CancelToken
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">baseUrl</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.baseUrl = baseUrl
    <span class="hljs-built_in">this</span>.pending = &#123;&#125; <span class="hljs-comment">// ++</span>
&#125;
<span class="hljs-comment">// ------------------------- </span>
<span class="hljs-comment">// key 判断是否相同的请求</span>
<span class="hljs-comment">// isRequest 判断请求是否已经得到响应</span>
<span class="hljs-comment">// this.pending[key] 判断是否发送了</span>
<span class="hljs-function"><span class="hljs-title">removePending</span>(<span class="hljs-params">key, isRequest = <span class="hljs-literal">false</span></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pending[key] && isRequest) &#123;
        <span class="hljs-built_in">this</span>.pending[key](<span class="hljs-string">'取消重复请求!'</span>)
    &#125;
    <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.pending[key]
&#125;
<span class="hljs-comment">// ------------------------- </span>
<span class="hljs-comment">// 判断上一次的请求是否有回应 请求拦截器</span>
instance.interceptors.request.use(<span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> key = config.url + <span class="hljs-string">'&'</span> + config.method
    <span class="hljs-built_in">this</span>.removePending(key, <span class="hljs-literal">true</span>)
    
    <span class="hljs-comment">// 核心.. 这个 c 个人理解为：调用则会取消此次请求。</span>
    config.cancelToken = <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function"><span class="hljs-params">c</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.pending[key] = c
    &#125;)
    <span class="hljs-keyword">return</span> config
&#125;,

<span class="hljs-comment">// -------------------------                </span>
                                  instance.interceptors.response.use(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> key = res.config.url + <span class="hljs-string">'&'</span> + res.config.method
    <span class="hljs-built_in">this</span>.removePending(key) <span class="hljs-comment">// 默认 isRequest = false</span>
 
    <span class="hljs-keyword">if</span> (res.status === <span class="hljs-number">200</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(res.data)
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(res)
    &#125;
    ...
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件中发送请求：</p>
<pre><code class="hljs language-js copyable" lang="js">getList(options).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-comment">// ...do sth</span>
&#125;).catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (e) &#123;
        <span class="hljs-built_in">this</span>.$alert(e.message)
    &#125;
    <span class="hljs-comment">// e.message(则是调用上面的c传的参数)</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整个流程就是 提交一次请求，此时<code>this.pending[key]</code> 有值，如果用户因为网速问题 (可以在浏览器network修改网速调试) 还没有得到响应，再次点击发送请求的时候，<code>this.pending[key]</code>就会执行<code>this.$alert(e.message) 会被执行 </code>。如果有响应的话，会<code>delete this.pending[key]</code>，这样就完成了重复请求的取消，并且对用户进行了提示。</p></div>  
</div>
            