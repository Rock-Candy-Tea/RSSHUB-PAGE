
---
title: '面试官：Vue项目中有封装过axios吗？怎么封装的？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce59acce03544740b4bd955f77138cee~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 01:53:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce59acce03544740b4bd955f77138cee~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce59acce03544740b4bd955f77138cee~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、什么是axios，有什么特性</h2>
<h4 data-id="heading-1">描述</h4>
<p>axios是一个基于<code>promise</code>的<code>HTTP</code>库，可以用在<code>浏览器</code>或者<code>node.js</code>中。本文围绕XHR。</p>
<blockquote>
<p>axios提供两个http请求适配器，XHR和HTTP。XHR的核心是浏览器端的XMLHttpRequest对象；HTTP的核心是node的http.request方法。</p>
</blockquote>
<p><strong>特性</strong>：</p>
<ul>
<li>从浏览器中创建XMLHttpRequests</li>
<li>从node.js创建http请求</li>
<li>支持promise API</li>
<li>拦截请求与响应</li>
<li>转换请求数据与响应数据</li>
<li>取消请求</li>
<li>自动转换JSON数据</li>
<li>客户端支持防御XSRF</li>
</ul>
<h4 data-id="heading-2">背景</h4>
<p>自<code>Vue</code>2.0起，尤大宣布取消对 <code>vue-resource</code> 的官方推荐，转而推荐 <code>axios</code>。现在 <code>axios</code> 已经成为大部分 <code>Vue</code> 开发者的首选，目前在github上有87.3k star。<code>axios</code>的熟练使用和基本封装也成为了vue技术栈系列必不可少的一部分。如果你还不了解axios，建议先熟悉
<a href="https://link.juejin.cn/?target=https%3A%2F%2Faxios-http.com%2Fdocs%2Fintro" target="_blank" rel="nofollow noopener noreferrer" title="https://axios-http.com/docs/intro" ref="nofollow noopener noreferrer">axios官网文档</a>。</p>
<h4 data-id="heading-3">基本使用</h4>
<p>安装</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install axios -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-comment">// 为给定ID的user创建请求 </span>
axios.get(<span class="hljs-string">'/user?ID=12345'</span>)   
    .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;     
        <span class="hljs-built_in">console</span>.log(response);   
    &#125;)   
    .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;    
        <span class="hljs-built_in">console</span>.log(error);   
    &#125;);  
<span class="hljs-comment">// 上面的请求也可以这样做 </span>
axios.get(<span class="hljs-string">'/user'</span>, &#123;     
    <span class="hljs-attr">params</span>: &#123;<span class="hljs-attr">ID</span>: <span class="hljs-number">12345</span>&#125;&#125;)   
    .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;     
        <span class="hljs-built_in">console</span>.log(response);   
    &#125;)   
    .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;     
        <span class="hljs-built_in">console</span>.log(error);   
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">二、Vue项目中为什么要封装axios</h2>
<p><code>axios</code>的API很友好，可以在项目中直接使用。但是在大型项目中，http请求很多，且需要区分环境，
每个网络请求有相似需要处理的部分，如下，会导致代码冗余，破坏工程的<code>可维护性</code>，<code>扩展性</code></p>
<pre><code class="hljs language-js copyable" lang="js">axios(<span class="hljs-string">'http://www.kaifa.com/data'</span>, &#123;
  <span class="hljs-comment">// 配置代码</span>
  <span class="hljs-attr">method</span>: <span class="hljs-string">'GET'</span>,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">3000</span>,
  <span class="hljs-attr">withCredentials</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">headers</span>: &#123;
    <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json'</span>
  &#125;,
  <span class="hljs-comment">// 其他请求配置...</span>
&#125;)
.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-comment">// todo: 真正业务逻辑代码</span>
  <span class="hljs-built_in">console</span>.log(data);
&#125;, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
  <span class="hljs-comment">// 错误处理代码  </span>
  <span class="hljs-keyword">if</span> (err.response.status === <span class="hljs-number">401</span>) &#123;
  <span class="hljs-comment">// handle authorization error</span>
  &#125;
  <span class="hljs-keyword">if</span> (err.response.status === <span class="hljs-number">403</span>) &#123;
  <span class="hljs-comment">// handle server forbidden error</span>
  &#125;
  <span class="hljs-comment">// 其他错误处理.....</span>
  <span class="hljs-built_in">console</span>.log(err);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>环境区分</li>
<li>请求头信息</li>
<li>请求超时时间
<ul>
<li>timeout: 3000</li>
</ul>
</li>
<li>允许携带cookie
<ul>
<li>withCredentials: true</li>
</ul>
</li>
<li>响应结果处理
<ul>
<li>登录校验失败</li>
<li>无权限</li>
<li>成功</li>
</ul>
</li>
<li>...</li>
</ul>
<h2 data-id="heading-5">三、Vue项目中如何封装axios</h2>
<p>axios文件封装在目录<code>src/utils/https.js</code>，对外暴露<code>callApi</code>函数</p>
<h4 data-id="heading-6">1、环境区分</h4>
<p><code>callApi</code>函数暴露<code>prefixUrl</code>参数，用来配置api url<code>前缀</code>，默认值为<code>api</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/utils/https.js</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> callApi = <span class="hljs-function">(<span class="hljs-params">
  url,
  ...
  prefixUrl = <span class="hljs-string">'api'</span>
</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (!url) &#123;
    <span class="hljs-keyword">const</span> error = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请传入url'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
  &#125;
  <span class="hljs-keyword">const</span> fullUrl = <span class="hljs-string">`/<span class="hljs-subst">$&#123;prefixUrl&#125;</span>/<span class="hljs-subst">$&#123;url&#125;</span>`</span>
  
  ...
  
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">url</span>: fullUrl,
    ...
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到这里大家可能会问，为什么不用axios提供的配置参数<code>baseURL</code>，原因是<code>baseURL</code>会给每个接口都加上对应前缀，而项目实际场景中，存在一个前端工程，对应多个<code>服务</code>的场景。需要通过不用的前缀代理到不同的服务，<code>baseURL</code>虽然能实现，但是需要二级前缀，不优雅，且在使用的时候看不到真实的api地址是啥，因为代理前缀跟真实地址混合在一起了</p>
<p>使用<code>baseURL</code>，效果如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d55ea16e20694bb4ad68ee506c830007~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>函数设置prefixUrl参数，效果如下
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/613abcca4b2b4a7095974f6748072671~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>利用<code>环境变量</code>及<code>webpack代理</code>(这里用vuecli3配置)来作判断，用来区分开发、测试环境。生产环境同理配置<code>nginx</code>代理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue.config.js</span>
<span class="hljs-keyword">const</span> targetApi1 = process.env.NODE_ENV === <span class="hljs-string">'development'</span> ? <span class="hljs-string">"http://www.kaifa1.com"</span> : <span class="hljs-string">"http://www.ceshi1.com"</span>

<span class="hljs-keyword">const</span> targetApi2 = process.env.NODE_ENV === <span class="hljs-string">'development'</span> ? <span class="hljs-string">"http://www.kaifa2.com"</span> : <span class="hljs-string">"http://www.ceshi2.com"</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">proxy</span>: &#123;
            <span class="hljs-string">'/api1'</span>: &#123;
                <span class="hljs-attr">target</span>: targetApi1,
                <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">pathRewrite</span>: &#123;
                    <span class="hljs-string">'/api1'</span>: <span class="hljs-string">""</span>
                &#125;
            &#125;,
            <span class="hljs-string">'/api2'</span>: &#123;
                <span class="hljs-attr">target</span>: targetApi2,
                <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">pathRewrite</span>: &#123;
                    <span class="hljs-string">'/api2'</span>: <span class="hljs-string">""</span>
                &#125;
            &#125;,
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2、请求头</h4>
<p>常见以下三种</p>
<p><strong>(1)application/json</strong></p>
<p>参数会直接放在请求体中，以JSON格式的发送到后端。这也是axios请求的默认方式。这种类型使用最为广泛。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10a319a7114d4f8b96c7cd6ee6f480d6~tplv-k3u1fbpfcp-watermark.image" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>(2)application/x-www-form-urlencoded</strong></p>
<p>请求体中的数据会以普通表单形式（键值对）发送到后端。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59702b0ce1744f8e8eaca3482aebbd94~tplv-k3u1fbpfcp-watermark.image" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>(3)multipart/form-data</strong></p>
<p>参数会在请求体中，以标签为单元，用分隔符(可以自定义的boundary)分开。既可以上传键值对，也可以上传文件。通常被用来上传文件的格式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/704ca7c37dca4a9083ed5680e2b13b3c~tplv-k3u1fbpfcp-watermark.image" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer">
<code>callApi</code>函数暴露<code>contentType</code>参数，用来配置<code>请求头</code>，默认值为<code>application/json; charset=utf-8</code></p>
<p>看到这里大家可以会疑惑，直接通过<code>options</code>配置<code>headers</code>不可以嘛，答案是可以的，可以看到<code>newOptions</code>的取值顺序，先取默认值，再取配置的<code>options</code>，最后取<code>contentType</code></p>
<p>通过<code>options</code>配置<code>headers</code>，写n遍<code>headers: &#123;'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'&#125;</code>；而通过<code>contentType</code>配置，传参<code>json || urlencoded || multipart</code>即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/utils/https.js</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>

<span class="hljs-keyword">const</span> contentTypes = &#123;
  <span class="hljs-attr">json</span>: <span class="hljs-string">'application/json; charset=utf-8'</span>,
  <span class="hljs-attr">urlencoded</span>: <span class="hljs-string">'application/x-www-form-urlencoded; charset=utf-8'</span>,
  <span class="hljs-attr">multipart</span>: <span class="hljs-string">'multipart/form-data'</span>,
&#125;

<span class="hljs-keyword">const</span> defaultOptions = &#123;
  <span class="hljs-attr">headers</span>: &#123;
    <span class="hljs-attr">Accept</span>: <span class="hljs-string">'application/json'</span>,
    <span class="hljs-string">'Content-Type'</span>: contentTypes.json,
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> callApi = <span class="hljs-function">(<span class="hljs-params">
  url,
  data = &#123;&#125;,
  options = &#123;&#125;,
  contentType = <span class="hljs-string">'json'</span>, <span class="hljs-comment">// json || urlencoded || multipart</span>
  prefixUrl = <span class="hljs-string">'api'</span>
</span>) =></span> &#123;

  ...
  
  <span class="hljs-keyword">const</span> newOptions = &#123;
    ...defaultOptions,
    ...options,
    <span class="hljs-attr">headers</span>: &#123;
      <span class="hljs-string">'Content-Type'</span>: contentTypes[contentType],
    &#125;,
  &#125;
  
  <span class="hljs-keyword">const</span> &#123; method &#125; = newOptions

  <span class="hljs-keyword">if</span> (method !== <span class="hljs-string">'get'</span> && method !== <span class="hljs-string">'head'</span>) &#123;
    <span class="hljs-keyword">if</span> (data <span class="hljs-keyword">instanceof</span> FormData) &#123;
      newOptions.data = data
      newOptions.headers = &#123;
        <span class="hljs-string">'x-requested-with'</span>: <span class="hljs-string">'XMLHttpRequest'</span>,
        <span class="hljs-string">'cache-control'</span>: <span class="hljs-string">'no-cache'</span>,
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (options.headers[<span class="hljs-string">'Content-Type'</span>] === contentTypes.urlencoded) &#123;
      newOptions.data = qs.stringify(data)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (
          data[item] === <span class="hljs-literal">null</span> ||
          data[item] === <span class="hljs-literal">undefined</span> ||
          data[item] === <span class="hljs-string">''</span>
        ) &#123;
          <span class="hljs-keyword">delete</span> data[item]
        &#125;
      &#125;)
      <span class="hljs-comment">// 没有必要，因为axios会将JavaScript对象序列化为JSON</span>
      <span class="hljs-comment">// newOptions.data = JSON.stringify(data);</span>
    &#125;
  &#125;
  
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">url</span>: fullUrl,
    ...newOptions,
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，在<code>application/json</code>格式下，JSON.stringify处理传参没有意义，因为axios会将JavaScript对象序列化为JSON，也就说说无论你转不转化都是JSON</p>
<h4 data-id="heading-8">3、请求超时时间</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/utils/https.js</span>
<span class="hljs-keyword">const</span> defaultOptions = &#123;
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">15000</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">4、允许携带cookie</h4>
<pre><code class="copyable">// src/utils/https.js
const defaultOptions = &#123;
  withCredentials: true,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">5、响应结果处理</h4>
<p>通过axios<code>响应拦截器</code>处理</p>
<p>这块需要跟服务端约定<code>接口响应全局码</code>，从而统一处理<code>登录校验失败</code>，<code>无权限</code>，<code>成功</code>等结果</p>
<p>比如有些服务端对于<code>登录校验失败</code>，<code>无权限</code>，<code>成功</code>等返回的响应码都是200，在响应体内返回的状态码分别是20001，20002，10000，在<code>then()</code>中处理</p>
<p>比如有些服务端对于<code>登录校验失败</code>，<code>无权限</code>，<code>成功</code>响应码返回401，403，200，在<code>catch()</code>中处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/utils/https.js</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> &#123; Message &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"element-ui"</span>;

axios.interceptors.response.use(
<span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; data &#125; = response
  <span class="hljs-keyword">if</span> (data.code === <span class="hljs-string">'xxx'</span>) &#123; <span class="hljs-comment">// 与服务端约定</span>
    <span class="hljs-comment">// 登录校验失败</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (data.code === <span class="hljs-string">'xxx'</span>) &#123; <span class="hljs-comment">// 与服务端约定</span>
    <span class="hljs-comment">// 无权限</span>
    router.replace(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/403'</span> &#125;)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (data.code === <span class="hljs-string">'xxx'</span>) &#123; <span class="hljs-comment">// 与服务端约定</span>
    <span class="hljs-comment">// 成功</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(data)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> &#123; message &#125; = data
    Message.error(message)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(data)
  &#125;
&#125;,
<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (error.response) &#123;
    <span class="hljs-keyword">const</span> &#123; data &#125; = error.response
    <span class="hljs-keyword">const</span> resCode = data.status
    <span class="hljs-keyword">const</span> resMsg = data.message || <span class="hljs-string">'服务异常'</span>
    <span class="hljs-comment">// if (resCode === 401) &#123; // 与服务端约定</span>
    <span class="hljs-comment">//     // 登录校验失败</span>
    <span class="hljs-comment">// &#125; else if (data.code === 403) &#123; // 与服务端约定</span>
    <span class="hljs-comment">//     // 无权限</span>
    <span class="hljs-comment">//     router.replace(&#123; path: '/403' &#125;)</span>
    <span class="hljs-comment">// &#125;</span>
    Message.error(resMsg)
    <span class="hljs-keyword">const</span> err = &#123; <span class="hljs-attr">code</span>: resCode, <span class="hljs-attr">respMsg</span>: resMsg &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> err = &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'canceled'</span>, <span class="hljs-attr">respMsg</span>: <span class="hljs-string">'数据请求超时'</span> &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err)
  &#125;
&#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述方案在<code>Message.error(xx)</code>时，当多个接口返回的错误信息一致时，会存在<code>重复提示</code>的问题，如下图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dfffc98a241489d8d06470adb0a94a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优化方案，利用<code>防抖</code>，实现错误提示一次，更优雅</p>
<h2 data-id="heading-11">四、完整封装及具体使用</h2>
<p>可以访问<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzxyue25%2Faxios-%255Bajax" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zxyue25/axios-%5Bajax" ref="nofollow noopener noreferrer">github</a></p>
<h4 data-id="heading-12">完成封装</h4>
<p>默认<code>请求方式</code>为<code>get</code>，不同的请求方通过options参数传入</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/utils/https.js</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>
<span class="hljs-keyword">import</span> &#123; debounce &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./debounce'</span>

<span class="hljs-keyword">const</span> contentTypes = &#123;
  <span class="hljs-attr">json</span>: <span class="hljs-string">'application/json; charset=utf-8'</span>,
  <span class="hljs-attr">urlencoded</span>: <span class="hljs-string">'application/x-www-form-urlencoded; charset=utf-8'</span>,
  <span class="hljs-attr">multipart</span>: <span class="hljs-string">'multipart/form-data'</span>,
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toastMsg</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.keys(errorMsgObj).map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
    Message.error(item)
    <span class="hljs-keyword">delete</span> errorMsgObj[item]
  &#125;)
&#125;

<span class="hljs-keyword">let</span> errorMsgObj = &#123;&#125;

<span class="hljs-keyword">const</span> defaultOptions = &#123;
  <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
  <span class="hljs-attr">withCredentials</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 允许把cookie传递到后台</span>
  <span class="hljs-attr">headers</span>: &#123;
    <span class="hljs-attr">Accept</span>: <span class="hljs-string">'application/json'</span>,
    <span class="hljs-string">'Content-Type'</span>: contentTypes.json,
  &#125;,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">15000</span>,
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> callApi = <span class="hljs-function">(<span class="hljs-params">
  url,
  data = &#123;&#125;,
  options = &#123;&#125;,
  contentType = <span class="hljs-string">'json'</span>, <span class="hljs-comment">// json || urlencoded || multipart</span>
  prefixUrl = <span class="hljs-string">'api'</span>
</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (!url) &#123;
    <span class="hljs-keyword">const</span> error = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请传入url'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
  &#125;
  <span class="hljs-keyword">const</span> fullUrl = <span class="hljs-string">`/<span class="hljs-subst">$&#123;prefixUrl&#125;</span>/<span class="hljs-subst">$&#123;url&#125;</span>`</span>

  <span class="hljs-keyword">const</span> newOptions = &#123;
    ...defaultOptions,
    ...options,
    <span class="hljs-attr">headers</span>: &#123;
      <span class="hljs-string">'Content-Type'</span>: contentTypes[contentType],
    &#125;,
  &#125;

  <span class="hljs-keyword">const</span> &#123; method &#125; = newOptions

  <span class="hljs-keyword">if</span> (method !== <span class="hljs-string">'get'</span> && method !== <span class="hljs-string">'head'</span>) &#123;
    <span class="hljs-keyword">if</span> (data <span class="hljs-keyword">instanceof</span> FormData) &#123;
      newOptions.data = data
      newOptions.headers = &#123;
        <span class="hljs-string">'x-requested-with'</span>: <span class="hljs-string">'XMLHttpRequest'</span>,
        <span class="hljs-string">'cache-control'</span>: <span class="hljs-string">'no-cache'</span>,
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newOptions.headers[<span class="hljs-string">'Content-Type'</span>] === contentTypes.urlencoded) &#123;
      newOptions.data = qs.stringify(data)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (
          data[item] === <span class="hljs-literal">null</span> ||
          data[item] === <span class="hljs-literal">undefined</span> ||
          data[item] === <span class="hljs-string">''</span>
        ) &#123;
          <span class="hljs-keyword">delete</span> data[item]
        &#125;
      &#125;)
      <span class="hljs-comment">// 没有必要，因为axios会将JavaScript对象序列化为JSON</span>
      <span class="hljs-comment">// newOptions.data = JSON.stringify(data);</span>
    &#125;
  &#125;

  axios.interceptors.request.use(<span class="hljs-function">(<span class="hljs-params">request</span>) =></span> &#123;
    <span class="hljs-comment">// 移除起始部分 / 所有请求url走相对路径</span>
    request.url = request.url.replace(<span class="hljs-regexp">/^\//</span>, <span class="hljs-string">''</span>)
    <span class="hljs-keyword">return</span> request
  &#125;)

  axios.interceptors.response.use(
    <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> &#123; data &#125; = response
      <span class="hljs-keyword">if</span> (data.code === <span class="hljs-string">'xxx'</span>) &#123; <span class="hljs-comment">// 与服务端约定</span>
        <span class="hljs-comment">// 登录校验失败</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (data.code === <span class="hljs-string">'xxx'</span>) &#123; <span class="hljs-comment">// 与服务端约定</span>
        <span class="hljs-comment">// 无权限</span>
        router.replace(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/403'</span> &#125;)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (data.code === <span class="hljs-string">'xxx'</span>) &#123; <span class="hljs-comment">// 与服务端约定</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(data)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">const</span> &#123; message &#125; = data
        <span class="hljs-keyword">if</span> (!errorMsgObj[message]) &#123;
          errorMsgObj[message] = message
        &#125;
        <span class="hljs-built_in">setTimeout</span>(debounce(toastMsg, <span class="hljs-number">1000</span>, <span class="hljs-literal">true</span>), <span class="hljs-number">1000</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(data)
      &#125;
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (error.response) &#123;
        <span class="hljs-keyword">const</span> &#123; data &#125; = error.response
        <span class="hljs-keyword">const</span> resCode = data.status
        <span class="hljs-keyword">const</span> resMsg = data.message || <span class="hljs-string">'服务异常'</span>
        <span class="hljs-comment">// if (resCode === 401) &#123; // 与服务端约定</span>
        <span class="hljs-comment">//     // 登录校验失败</span>
        <span class="hljs-comment">// &#125; else if (data.code === 403) &#123; // 与服务端约定</span>
        <span class="hljs-comment">//     // 无权限</span>
        <span class="hljs-comment">//     router.replace(&#123; path: '/403' &#125;)</span>
        <span class="hljs-comment">// &#125;</span>
        <span class="hljs-keyword">if</span> (!errorMsgObj[resMsg]) &#123;
          errorMsgObj[resMsg] = resMsg
        &#125;
        <span class="hljs-built_in">setTimeout</span>(debounce(toastMsg, <span class="hljs-number">1000</span>, <span class="hljs-literal">true</span>), <span class="hljs-number">1000</span>)
        <span class="hljs-keyword">const</span> err = &#123; <span class="hljs-attr">code</span>: resCode, <span class="hljs-attr">respMsg</span>: resMsg &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">const</span> err = &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'canceled'</span>, <span class="hljs-attr">respMsg</span>: <span class="hljs-string">'数据请求超时'</span> &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err)
      &#125;
    &#125;
  )

  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">url</span>: fullUrl,
    ...newOptions,
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/utils/https.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> debounce = <span class="hljs-function">(<span class="hljs-params">func, timeout, immediate</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> timer

  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> context = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">let</span> args = <span class="hljs-built_in">arguments</span>

    <span class="hljs-keyword">if</span> (timer) <span class="hljs-built_in">clearTimeout</span>(timer)
    <span class="hljs-keyword">if</span> (immediate) &#123;
      <span class="hljs-keyword">var</span> callNow = !timer
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        timer = <span class="hljs-literal">null</span>
      &#125;, timeout)
      <span class="hljs-keyword">if</span> (callNow) func.apply(context, args)
    &#125; <span class="hljs-keyword">else</span> &#123;
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        func.apply(context, args)
      &#125;, timeout)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">具体使用</h4>
<p>api管理文件在目录<code>src/service</code>下，<code>index.js</code>文件暴露其他模块，其他文件按<code>功能模块划分</code>文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59a8b475074145bb8e191a13436434d7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
自定义前缀代理不同服务
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd261596595a4b4b805928df06d56e25~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
文件类型处理
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd5be0ca5ece4f3da860ef6578407d6e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">五、总结</h2>
<p><code>axios</code>封装没有一个绝对的标准，且需要结合项目中<code>实际场景</code>来设计，但是毋庸置疑，axios-ajax的封装是非常有必要的</p></div>  
</div>
            