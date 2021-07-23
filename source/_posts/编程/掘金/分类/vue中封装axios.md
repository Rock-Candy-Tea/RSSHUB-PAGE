
---
title: 'vue中封装axios'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4668'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 04:36:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=4668'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">axios基本用法</h1>
<h4 data-id="heading-1">1. 下载 axios</h4>
<ul>
<li><code>yarn add axios -S</code></li>
<li><code> npm i axios -S</code></li>
</ul>
<h4 data-id="heading-2">2. 封装请求工具</h4>
<ul>
<li>src文件下创建 utils / request.js</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">const</span> request = axios.create(&#123;
    <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'接口统一的前缀地址'</span>
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (&#123; method = <span class="hljs-string">'GET'</span>, url, params, data, headers &#125;) => &#123;
    <span class="hljs-keyword">return</span> request(&#123; method, url, params, data, headers &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>以后换库, 只需要改这里, 逻辑页面不用动, 保证代码的复用性和独立性(高内聚低耦合)</p>
</blockquote>
<h4 data-id="heading-3">3. 封装接口工具</h4>
<ul>
<li>src文件下创建 api / 各种接口函数文件</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">import</span> $http <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/request.js'</span>
    <span class="hljs-keyword">const</span> customFn = <span class="hljs-function">(<span class="hljs-params"> data, params, headers </span>) =></span> &#123; <span class="hljs-comment">// 形参按需传入</span>
        <span class="hljs-keyword">return</span> $http(&#123;
            <span class="hljs-attr">method</span>: <span class="hljs-string">'默认为GET'</span>，
            <span class="hljs-attr">url</span>: <span class="hljs-string">'请求地址'</span>,
            data,params,headers,<span class="hljs-comment">// 按需接收</span>
        &#125;)
    &#125;
    <span class="hljs-keyword">export</span> &#123; customFn &#125; <span class="hljs-comment">// 按需导出</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">4. 项目应用</h4>
<ul>
<li>按需导入接口函数文件</li>
<li>调用函数发送请求</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">import</span> &#123; customFn &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/接口函数文件'</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fn</span>(<span class="hljs-params"> data, params, headers </span>) </span>&#123; <span class="hljs-comment">// 形参按需传入</span>
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>:res &#125; = <span class="hljs-keyword">await</span> customFn( data, params, headers ) <span class="hljs-comment">// 按需接收</span>
            <span class="hljs-built_in">console</span>.log(res)
        &#125; <span class="hljs-keyword">catch</span>(error) &#123;
            <span class="hljs-built_in">console</span>.log(error)
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>async 和await 只能接收成功状态的返回值，需配合try - catch接收失败状态的返回值</p>
</blockquote>
<h1 data-id="heading-5">axios拦截器</h1>
<h4 data-id="heading-6">1.请求拦截器</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// 添加请求拦截器</span>
    axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">config</span>) </span>&#123;
      <span class="hljs-keyword">return</span> config <span class="hljs-comment">// 发送请求时的数据</span>
    &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
      <span class="hljs-comment">// 对请求错误做些什么</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2.响应拦截器</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// 添加响应拦截器</span>
    axios.interceptors.response.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123; <span class="hljs-comment">// 当状态码为2xx/3xx开头的进这里</span>
        <span class="hljs-comment">// 对响应数据做点什么</span>
        <span class="hljs-keyword">return</span> response
    &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123; <span class="hljs-comment">// 响应状态码4xx/5xx进这里</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">3.移除拦截器</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> myInterceptors = axios.interceptors.response.use(...)
    axios.interceptors.response.eject(myInterceptors)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            