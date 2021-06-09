
---
title: 'AXIOS二次封装'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/undefined'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 20:44:43 GMT
thumbnail: 'https://juejin.cn/post/undefined'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Axios基础知识</h3>
<h4 data-id="heading-1">axios基本请求方法</h4>
<h5 data-id="heading-2">通用方法 <code>axios(config)</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//GET</span>
axios(&#123;
  <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
  <span class="hljs-attr">url</span>: <span class="hljs-string">'/user/12345'</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">firstName</span>: <span class="hljs-string">'Fred'</span>,
    <span class="hljs-attr">lastName</span>: <span class="hljs-string">'Flintstone'</span>
  &#125;
&#125;);

<span class="hljs-comment">/*-----*/</span>

<span class="hljs-comment">//POST</span>
axios(&#123;
  <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
  <span class="hljs-attr">url</span>: <span class="hljs-string">'/user/12345'</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">firstName</span>: <span class="hljs-string">'Fred'</span>,
    <span class="hljs-attr">lastName</span>: <span class="hljs-string">'Flintstone'</span>
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">简写GET</h4>
<blockquote>
<h5 data-id="heading-4">axios.get(url[, config])</h5>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.get(<span class="hljs-string">'http://localhost:9999/user/login'</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">简写POST</h4>
<blockquote>
<h5 data-id="heading-6">axios.post(url[, data[, config]])</h5>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.post(<span class="hljs-string">'http://localhost:9999/user/login'</span>,&#123;
    <span class="hljs-attr">account</span>:<span class="hljs-number">123</span>,
    <span class="hljs-attr">password</span>:<span class="hljs-number">123</span>
&#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">创建一个新的Axios实例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//一般用来创建一个新配置项</span>
axios.create([config])
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">分析配置项 <code>config</code></h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
   <span class="hljs-comment">// `url` 是用于请求的服务器 URL</span>
  <span class="hljs-attr">url</span>: <span class="hljs-string">'/user'</span>,
  <span class="hljs-comment">// `method` 是创建请求时使用的方法</span>
  <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>, <span class="hljs-comment">// default</span>
  <span class="hljs-comment">// `baseURL` 将自动加在 `url` 前面，除非 `url` 是一个绝对 URL。</span>
  <span class="hljs-comment">// 它可以通过设置一个 `baseURL` 便于为 axios 实例的方法传递相对 URL</span>
  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'https://some-domain.com/api/'</span>,

  <span class="hljs-comment">// `transformRequest` 允许在向服务器发送前，修改请求数据</span>
  <span class="hljs-comment">// 只能用在 'PUT', 'POST' 和 'PATCH' 这几个请求方法</span>
  <span class="hljs-comment">// 后面数组中的函数必须返回一个字符串，或 ArrayBuffer，或 Stream</span>
  <span class="hljs-attr">transformRequest</span>: [<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data, headers</span>) </span>&#123;
    <span class="hljs-comment">// 对 data 进行任意转换处理</span>
    <span class="hljs-keyword">return</span> data;
  &#125;],

  <span class="hljs-comment">// `transformResponse` 在传递给 then/catch 前，允许修改响应数据</span>
  <span class="hljs-attr">transformResponse</span>: [<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-comment">// 对 data 进行任意转换处理</span>
      <span class="hljs-comment">/*
      @1 比如后端需要 application/x-www-form-urlencoded 格式的数据
      return qs.stringify(data)//纯粹对象 => account=123&password=123
      */</span>
    <span class="hljs-keyword">return</span> data;
  &#125;],

  <span class="hljs-comment">// `headers` 是即将被发送的自定义请求头</span>
  <span class="hljs-attr">headers</span>: &#123;<span class="hljs-string">'X-Requested-With'</span>: <span class="hljs-string">'XMLHttpRequest'</span>&#125;,

  <span class="hljs-comment">// `params` 是即将与请求一起发送的 URL 参数</span>
  <span class="hljs-comment">// 必须是一个无格式对象(plain object)或 URLSearchParams 对象</span>
  <span class="hljs-attr">params</span>: &#123;
    <span class="hljs-attr">ID</span>: <span class="hljs-number">12345</span>
  &#125;,

   <span class="hljs-comment">// `paramsSerializer` 是一个负责 `params` 序列化的函数</span>
  <span class="hljs-comment">// (e.g. https://www.npmjs.com/package/qs, http://api.jquery.com/jquery.param/)</span>
  <span class="hljs-attr">paramsSerializer</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>) </span>&#123;
    <span class="hljs-keyword">return</span> Qs.stringify(params, &#123;<span class="hljs-attr">arrayFormat</span>: <span class="hljs-string">'brackets'</span>&#125;)
  &#125;,

  <span class="hljs-comment">// `data` 是作为请求主体被发送的数据</span>
  <span class="hljs-comment">// 只适用于这些请求方法 'PUT', 'POST', 和 'PATCH'</span>
  <span class="hljs-comment">// 在没有设置 `transformRequest` 时，必须是以下类型之一：</span>
  <span class="hljs-comment">// - string, plain object, ArrayBuffer, ArrayBufferView, URLSearchParams</span>
  <span class="hljs-comment">// - 浏览器专属：FormData, File, Blob</span>
  <span class="hljs-comment">// - Node 专属： Stream默认传输的格式是application/json</span>
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">firstName</span>: <span class="hljs-string">'Fred'</span>
  &#125;,

  <span class="hljs-comment">// `timeout` 指定请求超时的毫秒数(0 表示无超时时间)</span>
  <span class="hljs-comment">// 如果请求话费了超过 `timeout` 的时间，请求将被中断</span>
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">1000</span>,

   <span class="hljs-comment">// `withCredentials` 表示跨域请求时是否需要使用凭证</span>
  <span class="hljs-attr">withCredentials</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// default</span>

  <span class="hljs-comment">// `adapter` 允许自定义处理请求，以使测试更轻松</span>
  <span class="hljs-comment">// 返回一个 promise 并应用一个有效的响应 (查阅 [response docs](#response-api)).</span>
  <span class="hljs-attr">adapter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">config</span>) </span>&#123;
    <span class="hljs-comment">/* ... */</span>
  &#125;,

 <span class="hljs-comment">// `auth` 表示应该使用 HTTP 基础验证，并提供凭据</span>
  <span class="hljs-comment">// 这将设置一个 `Authorization` 头，覆写掉现有的任意使用 `headers` 设置的自定义 `Authorization`头</span>
  <span class="hljs-attr">auth</span>: &#123;
    <span class="hljs-attr">username</span>: <span class="hljs-string">'janedoe'</span>,
    <span class="hljs-attr">password</span>: <span class="hljs-string">'s00pers3cret'</span>
  &#125;,

   <span class="hljs-comment">// `responseType` 表示服务器响应的数据类型，可以是 'arraybuffer', 'blob', 'document', 'json', 'text', 'stream'</span>
  <span class="hljs-attr">responseType</span>: <span class="hljs-string">'json'</span>, <span class="hljs-comment">// default</span>

  <span class="hljs-comment">// `responseEncoding` indicates encoding to use for decoding responses</span>
  <span class="hljs-comment">// Note: Ignored for `responseType` of 'stream' or client-side requests</span>
  <span class="hljs-attr">responseEncoding</span>: <span class="hljs-string">'utf8'</span>, <span class="hljs-comment">// default</span>

   <span class="hljs-comment">// `xsrfCookieName` 是用作 xsrf token 的值的cookie的名称</span>
  <span class="hljs-attr">xsrfCookieName</span>: <span class="hljs-string">'XSRF-TOKEN'</span>, <span class="hljs-comment">// default</span>

  <span class="hljs-comment">// `xsrfHeaderName` is the name of the http header that carries the xsrf token value</span>
  <span class="hljs-attr">xsrfHeaderName</span>: <span class="hljs-string">'X-XSRF-TOKEN'</span>, <span class="hljs-comment">// default</span>

   <span class="hljs-comment">// `onUploadProgress` 允许为上传处理进度事件</span>
  <span class="hljs-attr">onUploadProgress</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">progressEvent</span>) </span>&#123;
    <span class="hljs-comment">// Do whatever you want with the native progress event</span>
  &#125;,

  <span class="hljs-comment">// `onDownloadProgress` 允许为下载处理进度事件</span>
  <span class="hljs-attr">onDownloadProgress</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">progressEvent</span>) </span>&#123;
    <span class="hljs-comment">// 对原生进度事件的处理</span>
  &#125;,

   <span class="hljs-comment">// `maxContentLength` 定义允许的响应内容的最大尺寸 一般也不动</span>
  <span class="hljs-attr">maxContentLength</span>: <span class="hljs-number">2000</span>,

  <span class="hljs-comment">// `validateStatus` 定义对于给定的HTTP 响应状态码是 resolve 或 reject  promise 。如果 `validateStatus` 返回 `true` (或者设置为 `null` 或 `undefined`)，promise 将被 resolve; 否则，promise 将被 rejecte</span>
  <span class="hljs-attr">validateStatus</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">status</span>) </span>&#123;
    <span class="hljs-keyword">return</span> status >= <span class="hljs-number">200</span> && status < <span class="hljs-number">300</span>; <span class="hljs-comment">// default</span>
  &#125;,

  <span class="hljs-comment">// `maxRedirects` 定义在 node.js 中 follow 的最大重定向数目</span>
  <span class="hljs-comment">// 如果设置为0，将不会 follow 任何重定向</span>
  <span class="hljs-attr">maxRedirects</span>: <span class="hljs-number">5</span>, <span class="hljs-comment">// default</span>

  <span class="hljs-comment">// `socketPath` defines a UNIX Socket to be used in node.js.</span>
  <span class="hljs-comment">// e.g. '/var/run/docker.sock' to send requests to the docker daemon.</span>
  <span class="hljs-comment">// Only either `socketPath` or `proxy` can be specified.</span>
  <span class="hljs-comment">// If both are specified, `socketPath` is used.</span>
  <span class="hljs-attr">socketPath</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// default</span>

  <span class="hljs-comment">// `httpAgent` 和 `httpsAgent` 分别在 node.js 中用于定义在执行 http 和 https 时使用的自定义代理。允许像这样配置选项：</span>
  <span class="hljs-comment">// `keepAlive` 默认没有启用</span>
  <span class="hljs-attr">httpAgent</span>: <span class="hljs-keyword">new</span> http.Agent(&#123; <span class="hljs-attr">keepAlive</span>: <span class="hljs-literal">true</span> &#125;),
  <span class="hljs-attr">httpsAgent</span>: <span class="hljs-keyword">new</span> https.Agent(&#123; <span class="hljs-attr">keepAlive</span>: <span class="hljs-literal">true</span> &#125;),

  <span class="hljs-comment">// 'proxy' 定义代理服务器的主机名称和端口</span>
  <span class="hljs-comment">// `auth` 表示 HTTP 基础验证应当用于连接代理，并提供凭据</span>
  <span class="hljs-comment">// 这将会设置一个 `Proxy-Authorization` 头，覆写掉已有的通过使用 `header` 设置的自定义 `Proxy-Authorization` 头。</span>
  <span class="hljs-attr">proxy</span>: &#123;
    <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">9000</span>,
    <span class="hljs-attr">auth</span>: &#123;
      <span class="hljs-attr">username</span>: <span class="hljs-string">'mikeymike'</span>,
      <span class="hljs-attr">password</span>: <span class="hljs-string">'rapunz3l'</span>
    &#125;
  &#125;,

  <span class="hljs-comment">// `cancelToken` 指定用于取消请求的 cancel token</span>
  <span class="hljs-comment">// （查看后面的 Cancellation 这节了解更多）</span>
  <span class="hljs-attr">cancelToken</span>: <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">cancel</span>) </span>&#123;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">全局的 axios 默认值</h4>
<blockquote>
<p>使用defaults</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.defaults.baseURL = <span class="hljs-string">'https://api.example.com'</span>;
axios.defaults.headers.common[<span class="hljs-string">'Authorization'</span>] = AUTH_TOKEN;
axios.defaults.headers.post[<span class="hljs-string">'Content-Type'</span>] = <span class="hljs-string">'application/x-www-form-urlencoded'</span>;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image-20210528161310890" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">自定义实例默认值</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Set config defaults when creating the instance</span>
<span class="hljs-keyword">const</span> instance = axios.create(&#123;
  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'https://api.example.com'</span>
&#125;);

<span class="hljs-comment">// Alter defaults after instance has been created</span>
instance.defaults.headers.common[<span class="hljs-string">'Authorization'</span>] = AUTH_TOKEN;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">拦截器</h4>
<blockquote>
<p>返回一个Promise</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 添加请求拦截器</span>
axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">config</span>) </span>&#123;
    <span class="hljs-comment">// 在发送请求之前做些什么</span>
    <span class="hljs-keyword">return</span> config;
  &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-comment">// 对请求错误做些什么</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;);

<span class="hljs-comment">// 添加响应拦截器</span>
axios.interceptors.response.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
    <span class="hljs-comment">// 对响应数据做点什么</span>
    <span class="hljs-keyword">return</span> response;
  &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-comment">// 对响应错误做点什么</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;);

<span class="hljs-comment">//移除拦截器</span>
<span class="hljs-keyword">const</span> myInterceptor = axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">/*...*/</span>&#125;);
axios.interceptors.request.eject(myInterceptor);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">axios二次封装</h3>
<blockquote>
<p>http.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* 
  axios二次封装：把每一次基于axios发送请求的公共部分进行提取
    + axios.defaults.xxx
    + axios.interceptors.request/response  拦截器 
 */</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
<span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;
<span class="hljs-keyword">import</span> tool <span class="hljs-keyword">from</span> <span class="hljs-string">'./tool'</span>;

<span class="hljs-comment">// 请求URL地址没有加前缀，则默认把BASE-URL加上；如果请求时候，自己设置前缀了，则以自己写的为主；</span>
<span class="hljs-comment">// 真实开发的时候，我们项目有各种不同的环境「开发、测试、灰度、生产」：我们需要针对不同的环境，有不同的BASE-URL</span>
<span class="hljs-comment">//  1)在运行编译的时候，设置环境变量</span>
<span class="hljs-comment">//    + 安装cross-env插件   $ npm i cross-env</span>
<span class="hljs-comment">//    + package.json的scripts中做处理</span>
<span class="hljs-comment">//      开发环境 serve:"cross-env NODE_ENV=development vue-cli-service serve",</span>
<span class="hljs-comment">//      生产环境 build:"cross-env NODE_ENV=production vue-cli-service build"</span>
<span class="hljs-comment">//  2)在代码中获取环境变量的值，根据不同值，设置不同的BASE-URL</span>
<span class="hljs-keyword">let</span> env = process.env.NODE_ENV || <span class="hljs-string">'development'</span>,
    baseURL = <span class="hljs-string">''</span>;
<span class="hljs-keyword">switch</span> (env) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'development'</span>:
        baseURL = <span class="hljs-string">'http://127.0.0.1:9999'</span>;
        <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'production'</span>:
        baseURL = <span class="hljs-string">'http://api.zhufengpeixun.cn'</span>;
        <span class="hljs-keyword">break</span>;
&#125;
axios.defaults.baseURL = baseURL;

<span class="hljs-comment">// 一些可以提取的小东西:超时时间 & CORS跨域中是否允许携带资源凭证(例如:cookie)</span>
<span class="hljs-comment">//   + 客户端的withCredentials:true，那么服务器端也要设置为允许</span>
axios.defaults.timeout = <span class="hljs-number">10000</span>;
axios.defaults.withCredentials = <span class="hljs-literal">true</span>;

<span class="hljs-comment">// POST系列请求中:请求主体中传递给服务器的信息，项目要求需要是URLENCODED格式；当代浏览器中，我们请求主体传递给服务器的格式是啥，浏览器会自动在请求头中，更新Content-Type!</span>
axios.defaults.transformRequest = <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-comment">// 只有我们写的DATA是一个纯粹的对象，才需要按需求处理</span>
    <span class="hljs-keyword">if</span> (tool.isPlainObject(data)) data = qs.stringify(data);
    <span class="hljs-keyword">return</span> data;
&#125;;

<span class="hljs-comment">// 自己规定，服务器返回的状态码，值是多少算是请求成功</span>
<span class="hljs-comment">//   成功:服务器正常返回响应信息，且返回的HTTP状态码是经过validateStatus校验通过的</span>
<span class="hljs-comment">//   失败:</span>
<span class="hljs-comment">//   + 服务器有返回的信息，但是返回的HTTP状态码并没有经过validateStatus的校验</span>
<span class="hljs-comment">//   + 请求超时或者请求中断  reason.code==='ECONNABORTED'</span>
<span class="hljs-comment">//   + 服务器没有返回任何信息「可能是断网了」</span>
<span class="hljs-comment">//   + ...</span>
axios.defaults.validateStatus = <span class="hljs-function"><span class="hljs-params">status</span> =></span> &#123;
    <span class="hljs-keyword">return</span> status >= <span class="hljs-number">200</span> && status < <span class="hljs-number">400</span>;
&#125;;

<span class="hljs-comment">// 请求拦截器:在axios内部已经把config的那些配置项处理差不多了，并且打算按照配置项，向服务器发送请求之前进行拦截；拦截目的是把配置项中的一些信息再改改！</span>
axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-comment">// 常见需求：在每一次发送请求的时候，通过请求头把token信息传递给服务器</span>
    <span class="hljs-keyword">const</span> token = <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'token'</span>);
    <span class="hljs-keyword">if</span> (token) &#123;
        config.headers[<span class="hljs-string">'Authorization'</span>] = token;
    &#125;
    <span class="hljs-keyword">return</span> config;
&#125;);

<span class="hljs-comment">// 响应拦截器:onfulfilled/onrejected，发生在请求成功/失败，在业务层具体.then/catch之前进行拦截处理</span>
axios.interceptors.response.use(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-comment">// 请求成功:一般我们会返回响应主体信息</span>
    <span class="hljs-keyword">return</span> response.data;
&#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
    <span class="hljs-comment">// 请求失败:一般我们会做统一的错误提示</span>
    <span class="hljs-keyword">if</span> (reason && reason.response) &#123;
        <span class="hljs-keyword">let</span> response = reason.response;
        <span class="hljs-comment">// 有响应信息，但是状态码不对，我们根据不同的状态码做不同的提示</span>
        <span class="hljs-keyword">switch</span> (response.status) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-number">400</span>:
                <span class="hljs-comment">// ...</span>
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-number">401</span>:
                <span class="hljs-comment">// ...</span>
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-number">404</span>:
                <span class="hljs-comment">// ...</span>
                <span class="hljs-keyword">break</span>;
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (reason && reason.code === <span class="hljs-string">'ECONNABORTED'</span>) &#123;
            <span class="hljs-comment">// 请求超时或者中断</span>
        &#125;
        <span class="hljs-keyword">if</span> (!navigator.onLine) &#123;
            <span class="hljs-comment">// 断网了</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(reason);
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>index.js 入口文件</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'./http'</span>;
<span class="hljs-keyword">import</span> instance <span class="hljs-keyword">from</span> <span class="hljs-string">'./http2'</span>;
<span class="hljs-keyword">import</span> md5 <span class="hljs-keyword">from</span> <span class="hljs-string">'blueimp-md5'</span>;

<span class="hljs-keyword">const</span> queryUserList = <span class="hljs-function">(<span class="hljs-params">departmentId = <span class="hljs-number">0</span>, search = <span class="hljs-string">''</span></span>) =></span> &#123;
    <span class="hljs-keyword">return</span> axios.get(<span class="hljs-string">'/user/list'</span>, &#123;
        <span class="hljs-attr">params</span>: &#123;
            departmentId,
            search
        &#125;
    &#125;);
&#125;;

<span class="hljs-keyword">const</span> setUserLogin = <span class="hljs-function">(<span class="hljs-params">account, password</span>) =></span> &#123;
    password = md5(password);
    <span class="hljs-keyword">return</span> axios.post(<span class="hljs-string">'/user/login'</span>, &#123;
        account,
        password
    &#125;);
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    queryUserList,
    setUserLogin
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>vue 中挂载到全局  在main.js中</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>;
<span class="hljs-keyword">import</span> api <span class="hljs-keyword">from</span> <span class="hljs-string">'./api/index'</span>;

Vue.config.productionTip = <span class="hljs-literal">false</span>;

<span class="hljs-comment">//之后每个页面this.$api可以获取</span>
Vue.prototype.$api = api;

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App),
&#125;).$mount(<span class="hljs-string">'#app'</span>);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            