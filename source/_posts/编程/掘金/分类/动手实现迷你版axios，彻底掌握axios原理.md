
---
title: '动手实现迷你版axios，彻底掌握axios原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf0209aa96704ddf8dacdb3a33b5d87a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 19:16:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf0209aa96704ddf8dacdb3a33b5d87a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>有几个问题，我们可以先思考一下，是否知道答案？</strong></p>
<ol>
<li>为什么 axios 既可以当函数调用，也可以当对象使用，比如axios(&#123;&#125;)、axios.get。</li>
<li>axios 的调用流程是怎样的？</li>
<li>拦截器吗原理是怎样的？</li>
<li>axios的取消功能是怎么实现的？</li>
<li>为什么支持浏览器中发送请求也支持node发送请求？</li>
</ol>
<p>如果对于以上的问题还是一知半解或根本没听说，那么是时候深入了解下axios了~</p>
<p>为了更好地了解axios源码，我们先手写一个发送请求的小demo，掌握了大体流程之后，阅读axios源码会更加得心应手。</p>
<h2 data-id="heading-0">手写mini axios</h2>
<p>初步搭建的框架如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf0209aa96704ddf8dacdb3a33b5d87a~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>定义一种字符串字面量类型 <code>Method</code>：</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> Method = <span class="hljs-string">'get'</span> | <span class="hljs-string">'GET'</span>
  | <span class="hljs-string">'delete'</span> | <span class="hljs-string">'Delete'</span>
  | <span class="hljs-string">'head'</span> | <span class="hljs-string">'HEAD'</span>
  | <span class="hljs-string">'options'</span> | <span class="hljs-string">'OPTIONS'</span>
  | <span class="hljs-string">'post'</span> | <span class="hljs-string">'POST'</span>
  | <span class="hljs-string">'put'</span> | <span class="hljs-string">'PUT'</span>
  | <span class="hljs-string">'patch'</span> | <span class="hljs-string">'PATCH'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>定义 <code>AxiosRequestConfig</code> 接口类型：</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> AxiosRequestConfig &#123;
  <span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>
  method?: Method
  data?: <span class="hljs-built_in">any</span>
  params?: <span class="hljs-built_in">any</span>,
  headers?: <span class="hljs-built_in">any</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>封装xhr，实现发送请求逻辑</li>
</ol>
<p>新建<code>xhr.ts</code> 文件，导出 <code>xhr</code> 方法，其中使用到了<code>XMLHttpRequest</code>对象，调用<code>send</code>方法发送请求。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; AxiosRequestConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./types'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">xhr</span>(<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data = <span class="hljs-literal">null</span>, url, method = <span class="hljs-string">'get'</span> &#125; = config
  <span class="hljs-keyword">const</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest()
  request.open(method.toUpperCase(), url, <span class="hljs-literal">true</span>)
  request.send(data)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>定义axios类，引入xhr方法</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; AxiosRequestConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./types'</span>
<span class="hljs-keyword">import</span> xhr <span class="hljs-keyword">from</span> <span class="hljs-string">'./xhr'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">axios</span>(<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">void</span> </span>&#123;
  xhr(config)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此为止，发送请求的最小闭环已经实现了，之后会逐渐剖析其他功能。</p>
<h3 data-id="heading-1">1. 处理url</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fb79d6fc4994a0dbfdbb18a4752c0b5~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们使用axios发送请求的结构可以为以下形式：</p>
<pre><code class="hljs language-ts copyable" lang="ts">axios(&#123;
  <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
  <span class="hljs-attr">url</span>: <span class="hljs-string">'xx/xx'</span>,
  <span class="hljs-attr">params</span>: &#123;&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，params的参数形式非常多，如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 对象，`/base/get?a=1&b=2`</span>
<span class="hljs-attr">params</span>: &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>
&#125;

<span class="hljs-comment">// 数组，’/base/get?foo[]=bar&foo[]=baz'</span>
<span class="hljs-attr">params</span>: &#123;
    <span class="hljs-attr">foo</span>: [<span class="hljs-string">'bar'</span>, <span class="hljs-string">'baz'</span>]
&#125;

<span class="hljs-comment">// 复杂对象，/base/get?foo=%7B%22bar%22:%22baz%22%7D</span>
<span class="hljs-attr">params</span>: &#123;
    <span class="hljs-attr">foo</span>: &#123;
        <span class="hljs-attr">bar</span>: <span class="hljs-string">'baz'</span>
    &#125;
&#125;

<span class="hljs-comment">// Date类型，/base/get?date=2019-04-01T05:55:39.030Z</span>
<span class="hljs-attr">params</span>: &#123;
    date
&#125;

<span class="hljs-comment">// 特殊字符，空格需要转换为+号</span>
<span class="hljs-attr">params</span>: &#123;
    <span class="hljs-attr">foo</span>: <span class="hljs-string">'@:$, '</span>
&#125;

<span class="hljs-comment">// 空值null，需要忽略</span>
<span class="hljs-attr">params</span>: &#123;
    <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>,
    <span class="hljs-attr">baz</span>: <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而且url也可能遇到以下几种形式：</p>
<pre><code class="hljs language-ts copyable" lang="ts">url: <span class="hljs-string">'/base/get#hash'</span>,<span class="hljs-comment">// 需要丢弃 url 中的哈希标记</span>
<span class="hljs-attr">url</span>: <span class="hljs-string">'/base/get?foo=bar'</span>,<span class="hljs-comment">// 需要保留url中的参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于以上的规则，我们写一个拼接请求url的函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 辅助方法</span>
<span class="hljs-keyword">const</span> toString = <span class="hljs-built_in">Object</span>.prototype.toString
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_isDate</span>(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">val</span> <span class="hljs-title">is</span> <span class="hljs-title">Date</span> </span>&#123;
    <span class="hljs-keyword">return</span> toString.call(val) === <span class="hljs-string">'[object Date]'</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_isObject</span>(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">val</span> <span class="hljs-title">is</span> <span class="hljs-title">Object</span> </span>&#123;
    <span class="hljs-keyword">return</span> val !== <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'object'</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_encode</span>(<span class="hljs-params">val: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">string</span> </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">encodeURIComponent</span>(val)
        .replace(<span class="hljs-regexp">/%40/g</span>, <span class="hljs-string">'@'</span>)
        .replace(<span class="hljs-regexp">/%3A/gi</span>, <span class="hljs-string">':'</span>)
        .replace(<span class="hljs-regexp">/%24/g</span>, <span class="hljs-string">'$'</span>)
        .replace(<span class="hljs-regexp">/%2C/gi</span>, <span class="hljs-string">','</span>)
        .replace(<span class="hljs-regexp">/%20/g</span>, <span class="hljs-string">'+'</span>)
        .replace(<span class="hljs-regexp">/%5B/gi</span>, <span class="hljs-string">'['</span>)
        .replace(<span class="hljs-regexp">/%5D/gi</span>, <span class="hljs-string">']'</span>)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bulidURL</span>(<span class="hljs-params">url: <span class="hljs-built_in">string</span>, params?: <span class="hljs-built_in">any</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!params) &#123;
        <span class="hljs-keyword">return</span> url
    &#125;
    <span class="hljs-keyword">const</span> parts: <span class="hljs-built_in">string</span>[] = []
    <span class="hljs-built_in">Object</span>.keys(params).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> val = params[key]
        <span class="hljs-keyword">if</span> (val === <span class="hljs-literal">null</span> || <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'undefined'</span>) &#123;
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">let</span> values: <span class="hljs-built_in">string</span>[]
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(val)) &#123;
            values = val
            key += <span class="hljs-string">'[]'</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            values = [val]
        &#125;
        values.forEach(<span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (_isDate(val)) &#123;
                val = val.toISOString()
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (_isObject(val)) &#123;
                val = <span class="hljs-built_in">JSON</span>.stringify(val)
            &#125;
            parts.push(<span class="hljs-string">`<span class="hljs-subst">$&#123;_encode(key)&#125;</span>=<span class="hljs-subst">$&#123;_encode(val)&#125;</span>`</span>)
        &#125;)
    &#125;)
    <span class="hljs-keyword">let</span> serializedParams = parts.join(<span class="hljs-string">'&'</span>)
    <span class="hljs-keyword">if</span> (serializedParams) &#123;
        <span class="hljs-keyword">const</span> markIndex = url.indexOf(<span class="hljs-string">'#'</span>)
        <span class="hljs-keyword">if</span> (markIndex !== -<span class="hljs-number">1</span>) &#123;
            url = url.slice(<span class="hljs-number">0</span>, markIndex)
        &#125;
        url += (url.indexOf(<span class="hljs-string">'?'</span>) === -<span class="hljs-number">1</span> ? <span class="hljs-string">'?'</span> : <span class="hljs-string">'&'</span>) + serializedParams
    &#125;
    <span class="hljs-keyword">return</span> url
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现完此函数后，在axios类中添加此方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">axios</span> (<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">void</span> </span>&#123;
  processConfig(config)
  xhr(config)
&#125;
<span class="hljs-comment">// 对config中的url进行规范化处理，重新设置config.url</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processConfig</span> (<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">void</span> </span>&#123;
  config.url = transformUrl(config)
&#125;
<span class="hljs-comment">// 对url进行规范化处理</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformUrl</span> (<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">const</span> &#123; url, params &#125; = config
  <span class="hljs-keyword">return</span> bulidURL(url, params)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2. 处理data</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e5a1e4a844442f796352be4e6c2d984~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer">
<code>send</code> 方法的参数支持 <code>Document</code> 和 <code>BodyInit</code> 类型，<code>BodyInit</code> 包括了 <code>Blob</code>, <code>BufferSource</code>, <code>FormData</code>, <code>URLSearchParams</code>, <code>ReadableStream</code>、<code>USVString</code>，当没有数据的时候，我们还可以传入 <code>null</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 判断是否是普通的json对象，具有key-value的形式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_isPlainObject</span>(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">val</span> <span class="hljs-title">is</span> <span class="hljs-title">Object</span> </span>&#123;
   <span class="hljs-keyword">return</span> toString.call(val) === <span class="hljs-string">'[object Object]'</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformRequest</span>(<span class="hljs-params">data: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">any</span> </span>&#123;
   <span class="hljs-keyword">if</span> (_isPlainObject(data)) &#123;
       <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.stringify(data)
   &#125;
   <span class="hljs-keyword">return</span> data
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现完此函数后，在axios类中添加此方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processConfig</span>(<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">void</span> </span>&#123;
   config.url = transformURL(config)
   config.data = transformRequestData(config)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformRequestData</span>(<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">any</span> </span>&#123;
   <span class="hljs-keyword">return</span> transformRequest(config.data)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3. 处理header</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d0c86dfed784960977bf97507b44a18~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer">
上面我们把data转化为了json，但是服务器此时还不能正确地解析，我们在发送数据时需要设置合适的content-type。
首先编写处理header的函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 判断是否是普通的json对象，具有key-value的形式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_isPlainObject</span>(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">val</span> <span class="hljs-title">is</span> <span class="hljs-title">Object</span> </span>&#123;
    <span class="hljs-keyword">return</span> toString.call(val) === <span class="hljs-string">'[object Object]'</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">normalizeHeaderName</span>(<span class="hljs-params">headers: <span class="hljs-built_in">any</span>, normalizedName: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">void</span> </span>&#123;
    <span class="hljs-keyword">if</span> (!headers) &#123;
        <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-built_in">Object</span>.keys(headers).forEach(<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (name !== normalizedName && name.toUpperCase() === normalizedName.toUpperCase()) &#123;
            headers[normalizedName] = headers[name]
            <span class="hljs-keyword">delete</span> headers[name]
        &#125;
    &#125;)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processHeaders</span>(<span class="hljs-params">headers: <span class="hljs-built_in">any</span>, data: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">any</span> </span>&#123;
    normalizeHeaderName(headers, <span class="hljs-string">'Content-Type'</span>)
    <span class="hljs-keyword">if</span> (_isPlainObject(data)) &#123;
        <span class="hljs-keyword">if</span> (headers && !headers[<span class="hljs-string">'Content-Type'</span>]) &#123;
            headers[<span class="hljs-string">'Content-Type'</span>] = <span class="hljs-string">'application/json;charset=utf-8'</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> headers
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在xhr方法中，我们也需要处理下header：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">xhr</span> (<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data = <span class="hljs-literal">null</span>, url, method = <span class="hljs-string">'get'</span>, headers &#125; = config
  <span class="hljs-keyword">const</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest()
  request.open(method.toUpperCase(), url, <span class="hljs-literal">true</span>)
  <span class="hljs-built_in">Object</span>.keys(headers).forEach(<span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (data === <span class="hljs-literal">null</span> && name.toLowerCase() === <span class="hljs-string">'content-type'</span>) &#123;
      <span class="hljs-keyword">delete</span> headers[name]
    &#125; <span class="hljs-keyword">else</span> &#123;
      request.setRequestHeader(name, headers[name])
    &#125;
  &#125;)
  request.send(data)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现完此函数后，在axios文件中添加此方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processConfig</span> (<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">void</span> </span>&#123;
  config.url = transformURL(config)
  config.headers = transformHeaders(config)
  config.data = transformRequestData(config)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformHeaders</span> (<span class="hljs-params">config: AxiosRequestConfig</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; headers = &#123;&#125;, data &#125; = config
  <span class="hljs-keyword">return</span> processHeaders(headers, data)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4. 处理response</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db326d98931d469a9cfff9b5344f8554~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer">
如何实现服务端处理响应数据，并且返回promise链式调用的形式？
首先定义一个接口类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> AxiosResponse &#123;
  <span class="hljs-attr">data</span>: <span class="hljs-built_in">any</span>
  <span class="hljs-attr">status</span>: <span class="hljs-built_in">number</span>
  <span class="hljs-attr">statusText</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">headers</span>: <span class="hljs-built_in">any</span>
  <span class="hljs-attr">config</span>: AxiosRequestConfig
  <span class="hljs-attr">request</span>: <span class="hljs-built_in">any</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>xhr</code> 函数添加<code>onreadystatechange</code>事件处理函数，并且让 <code>xhr</code> 函数返回的是 <code>AxiosPromise</code> 类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">xhr</span>(<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">AxiosPromise</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; data = <span class="hljs-literal">null</span>, url, method = <span class="hljs-string">'get'</span>, headers, responseType &#125; = config
    <span class="hljs-keyword">const</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest()
    <span class="hljs-keyword">if</span> (responseType) &#123;
      request.responseType = responseType
    &#125;
    request.open(method.toUpperCase(), url, <span class="hljs-literal">true</span>)
<span class="hljs-comment">// 这里添加onreadystatechange监听事件</span>
    request.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleLoad</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (request.readyState !== <span class="hljs-number">4</span>) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">const</span> responseHeaders = request.getAllResponseHeaders()
      <span class="hljs-keyword">const</span> responseData = responseType && responseType !== <span class="hljs-string">'text'</span> ? request.response : request.responseText
  <span class="hljs-comment">// 构造 `AxiosResponse` 类型的 `reponse` 对象，并把它 `resolve` 出去</span>
      <span class="hljs-keyword">const</span> response: AxiosResponse = &#123;
        <span class="hljs-attr">data</span>: responseData,
        <span class="hljs-attr">status</span>: request.status,
        <span class="hljs-attr">statusText</span>: request.statusText,
        <span class="hljs-attr">headers</span>: responseHeaders,
        config,
        request
      &#125;
      resolve(response)
    &#125;
    <span class="hljs-built_in">Object</span>.keys(headers).forEach(<span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (data === <span class="hljs-literal">null</span> && name.toLowerCase() === <span class="hljs-string">'content-type'</span>) &#123;
        <span class="hljs-keyword">delete</span> headers[name]
      &#125; <span class="hljs-keyword">else</span> &#123;
        request.setRequestHeader(name, headers[name])
      &#125;
    &#125;)
    request.send(data)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改axios函数，使其返回AxiosPromise的数据：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">axios</span>(<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">AxiosPromise</span> </span>&#123;
  processConfig(config)
  <span class="hljs-keyword">return</span> xhr(config)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">5. 处理response-header</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e726e0c055414d7bb405d0f4b5574d9e~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer">
通过 <code>XMLHttpRequest</code> 对象的 <code>getAllResponseHeaders</code> 方法获取到的值是一段字符串，我们需要将它们处理成对象的结构：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parseHeaders</span>(<span class="hljs-params">headers: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">any</span> </span>&#123;
    <span class="hljs-keyword">let</span> parsed = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">if</span> (!headers) &#123; <span class="hljs-keyword">return</span> parsed &#125;
    headers.split(<span class="hljs-string">'\r\n'</span>).forEach(<span class="hljs-function"><span class="hljs-params">line</span> =></span> &#123;
        <span class="hljs-keyword">let</span> [key, val] = line.split(<span class="hljs-string">':'</span>)
        key = key.trim().toLowerCase()
        <span class="hljs-keyword">if</span> (!key) &#123; <span class="hljs-keyword">return</span> &#125;
        <span class="hljs-keyword">if</span> (val) &#123; val = val.trim() &#125;
        parsed[key] = val
    &#125;)
    <span class="hljs-keyword">return</span> parsed
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来在xhr方法中使用这个函数，用来处理response的header：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> responseHeaders = parseHeaders(request.getAllResponseHeaders())
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">6. 处理response-data</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e20bc8881345f2b7f6228a69a02b6d~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer">
服务器返回给我们的是string类型，我们需要将其转化为json对象。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformResponse</span>(<span class="hljs-params">data: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">any</span> </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'string'</span>) &#123;
    <span class="hljs-keyword">try</span> &#123;data = <span class="hljs-built_in">JSON</span>.parse(data)&#125; <span class="hljs-keyword">catch</span> (e) &#123;&#125;
  &#125;
  <span class="hljs-keyword">return</span> data
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用此方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">axios</span>(<span class="hljs-params">config: AxiosRequestConfig</span>): <span class="hljs-title">AxiosPromise</span> </span>&#123;
  processConfig(config)
  <span class="hljs-keyword">return</span> xhr(config).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> transformResponseData(res)
  &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformResponseData</span>(<span class="hljs-params">res: AxiosResponse</span>): <span class="hljs-title">AxiosResponse</span> </span>&#123;
  res.data = transformResponse(res.data)
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">7. 常见错误监听与处理</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e924672968be4b50a9428124ecf38439~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>监听网络异常</li>
</ol>
<p>在xhr方法中添加：</p>
<pre><code class="hljs language-ts copyable" lang="ts">request.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleError</span>(<span class="hljs-params"></span>) </span>&#123;
  reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'网络错误'</span>))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>网络超时</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> &#123; <span class="hljs-comment">/*...*/</span> timeout &#125; = config
<span class="hljs-keyword">if</span> (timeout) &#123;
  request.timeout = timeout
&#125;
request.ontimeout = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleTimeout</span>(<span class="hljs-params"></span>) </span>&#123;
  reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Timeout of <span class="hljs-subst">$&#123;timeout&#125;</span> ms exceeded`</span>))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>非 200 状态码</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts">request.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleLoad</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (request.readyState !== <span class="hljs-number">4</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">if</span> (request.status === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">const</span> responseHeaders = parseHeaders(request.getAllResponseHeaders())
    <span class="hljs-keyword">const</span> responseData = responseType && responseType !== <span class="hljs-string">'text'</span> ? request.response : request.responseText
    <span class="hljs-keyword">const</span> response: AxiosResponse = &#123;
        <span class="hljs-attr">data</span>: responseData,
        <span class="hljs-attr">status</span>: request.status,
        <span class="hljs-attr">statusText</span>: request.statusText,
        <span class="hljs-attr">headers</span>: responseHeaders,
        config,
        request
    &#125;
    handleResponse(response)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleResponse</span>(<span class="hljs-params">response: AxiosResponse</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (response.status >= <span class="hljs-number">200</span> && response.status < <span class="hljs-number">300</span>) &#123;
        resolve(response)
    &#125; <span class="hljs-keyword">else</span> &#123;
        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Request failed with status code <span class="hljs-subst">$&#123;response.status&#125;</span>`</span>))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">8. 错误类封装</h3>
<p>我们可以封装一个AxiosError类，用来承载详细的错误信息。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> AxiosError <span class="hljs-keyword">extends</span> Error &#123;
  <span class="hljs-attr">config</span>: AxiosRequestConfig
  code?: <span class="hljs-built_in">string</span>
  request?: <span class="hljs-built_in">any</span>
  response?: AxiosResponse
  <span class="hljs-attr">isAxiosError</span>: <span class="hljs-built_in">boolean</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; AxiosRequestConfig, AxiosResponse &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../types'</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AxiosError</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Error</span> </span>&#123;
  <span class="hljs-attr">isAxiosError</span>: <span class="hljs-built_in">boolean</span>
  <span class="hljs-attr">config</span>: AxiosRequestConfig
  code?: <span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span>
  request?: <span class="hljs-built_in">any</span>
  response?: AxiosResponse

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">
    message: <span class="hljs-built_in">string</span>,
    config: AxiosRequestConfig,
    code?: <span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span>,
    request?: <span class="hljs-built_in">any</span>,
    response?: AxiosResponse
  </span>)</span> &#123;
    <span class="hljs-built_in">super</span>(message)
    <span class="hljs-built_in">this</span>.config = config
    <span class="hljs-built_in">this</span>.code = code
    <span class="hljs-built_in">this</span>.request = request
    <span class="hljs-built_in">this</span>.response = response
    <span class="hljs-built_in">this</span>.isAxiosError = <span class="hljs-literal">true</span>
    <span class="hljs-built_in">Object</span>.setPrototypeOf(<span class="hljs-built_in">this</span>, AxiosError.prototype)
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createError</span>(<span class="hljs-params">
  message: <span class="hljs-built_in">string</span>,
  config: AxiosRequestConfig,
  code?: <span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span>,
  request?: <span class="hljs-built_in">any</span>,
  response?: AxiosResponse
</span>): <span class="hljs-title">AxiosError</span> </span>&#123;
  <span class="hljs-keyword">const</span> error = <span class="hljs-keyword">new</span> AxiosError(message, config, code, request, response)
  <span class="hljs-keyword">return</span> error
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在抛出错误的时候，我们使用到<code>createError</code>方法自定义错误信息。</p>
<h2 data-id="heading-9">axios源码</h2>
<h3 data-id="heading-10">1. axios.js文件</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20fe8426748c4c50b05ffa0c7c559687~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer">
这个文件的作用：</p>
<ol>
<li>暴露了一个默认的Axios实例</li>
<li>暴露了创建Axios实例的工厂方法</li>
<li>暴露了Axios类方便继承</li>
<li>暴露了Cancel相关的API</li>
</ol>
<p>注意代码中<code>utils.extend(instance, Axios.prototype, context); </code>是把Axios.prototype的所有方法和域都复制到实例中，因此axios本身就可以作为一个函数使用，如：</p>
<pre><code class="hljs language-js copyable" lang="js">axios.request(&#123;
  <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
  <span class="hljs-attr">url</span>: <span class="hljs-string">'/user'</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'xxx'</span>
  &#125;
  <span class="hljs-comment">// ...other</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整源码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">var</span> utils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./utils'</span>);
<span class="hljs-keyword">var</span> bind = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./helpers/bind'</span>);
<span class="hljs-keyword">var</span> Axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./core/Axios'</span>);
<span class="hljs-keyword">var</span> defaults = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./defaults'</span>);

<span class="hljs-comment">// 创建一个Axios实例</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createInstance</span>(<span class="hljs-params">defaultConfig</span>) </span>&#123;
  <span class="hljs-keyword">var</span> context = <span class="hljs-keyword">new</span> Axios(defaultConfig);
  <span class="hljs-keyword">var</span> instance = bind(Axios.prototype.request, context);<span class="hljs-comment">//实际上是 Axios.prototype.request 这个方法</span>
  utils.extend(instance, Axios.prototype, context); <span class="hljs-comment">//把Axios.prototype的所有方法和域都复制到实例中</span>
  utils.extend(instance, context);  <span class="hljs-comment">//把context的所有域都复制到实例中</span>
  <span class="hljs-keyword">return</span> instance;
&#125;

<span class="hljs-comment">//创建默认实例</span>
<span class="hljs-keyword">var</span> axios = createInstance(defaults);

<span class="hljs-comment">//暴露 Axios类 方便外部使用继承</span>
axios.Axios = Axios;

<span class="hljs-comment">// 暴露创建Axios实例的工厂方法</span>
axios.create = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">instanceConfig</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createInstance(utils.merge(defaults, instanceConfig));
&#125;;

<span class="hljs-comment">// 暴露 取消request相关的方法</span>
axios.Cancel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/Cancel'</span>);
axios.CancelToken = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/CancelToken'</span>);
axios.isCancel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./cancel/isCancel'</span>);

<span class="hljs-comment">// 暴露 all 和 spread 这2个工具方法</span>
axios.all = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">all</span>(<span class="hljs-params">promises</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(promises);
&#125;;
axios.spread = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./helpers/spread'</span>);

<span class="hljs-built_in">module</span>.exports = axios;
<span class="hljs-built_in">module</span>.exports.default = axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">2. core/Axios.js文件</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7a03245ee4c497390b538a687ce7523~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer">
这个文件定义了Axios类，其中包括了以下几点：</p>
<ol>
<li>定义Axios类</li>
<li>定义了Axios.prototype.request（包括配置与处理、拦截器处理）</li>
<li>定义了Axios.prototype.delete, Axios.prototype.get, Axios.prototype.head, Axios.prototype.options（不需要payload）</li>
<li>定义了Axios.prototype.put, Axios.prototype.post, Axios.prototype.patch（需要payload）</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">var</span> defaults = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./../defaults'</span>);
<span class="hljs-keyword">var</span> utils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./../utils'</span>);
<span class="hljs-keyword">var</span> InterceptorManager = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./InterceptorManager'</span>);
<span class="hljs-keyword">var</span> dispatchRequest = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./dispatchRequest'</span>);

<span class="hljs-comment">//Axios类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Axios</span>(<span class="hljs-params">instanceConfig</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.defaults = instanceConfig;
  <span class="hljs-built_in">this</span>.interceptors = &#123; <span class="hljs-comment">//初始化 interceptors （拦截器）</span>
    <span class="hljs-attr">request</span>: <span class="hljs-keyword">new</span> InterceptorManager(),
    <span class="hljs-attr">response</span>: <span class="hljs-keyword">new</span> InterceptorManager()
  &#125;;
&#125;

<span class="hljs-comment">// Axios的核心方法request</span>
<span class="hljs-comment">// 将 request发起，request拦截器和 response拦截器 链式拼接，最后用 promise 串起来调用</span>
Axios.prototype.request = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> config === <span class="hljs-string">'string'</span>) &#123;
    config = utils.merge(&#123;
      <span class="hljs-attr">url</span>: <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>]
    &#125;, <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>]);
  &#125;
  config = utils.merge(defaults, &#123;<span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>&#125;, <span class="hljs-built_in">this</span>.defaults, config);
  config.method = config.method.toLowerCase();

  <span class="hljs-comment">//链表初始值是 dispatchRequest 和 undefined 组成的 2个元素的数组</span>
  <span class="hljs-keyword">var</span> chain = [dispatchRequest, <span class="hljs-literal">undefined</span>];
  <span class="hljs-comment">// promise 链的第一个promise将 config 传入</span>
  <span class="hljs-keyword">var</span> promise = <span class="hljs-built_in">Promise</span>.resolve(config);
  <span class="hljs-comment">// 将request拦截器逐一插入到 链表的头部</span>
  <span class="hljs-built_in">this</span>.interceptors.request.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unshiftRequestInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;
    chain.unshift(interceptor.fulfilled, interceptor.rejected);
  &#125;);
<span class="hljs-comment">// 将request拦截器逐一插入到 链表的尾部</span>
  <span class="hljs-built_in">this</span>.interceptors.response.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushResponseInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;
    chain.push(interceptor.fulfilled, interceptor.rejected);
  &#125;);

  <span class="hljs-keyword">while</span> (chain.length) &#123;
    <span class="hljs-comment">// 从链表中从头连续取出2个元素，第一个作为 promise 的 resolve handler， 第二个做 reject handler</span>
    promise = promise.then(chain.shift(), chain.shift());
  &#125;
  <span class="hljs-keyword">return</span> promise;
&#125;;

<span class="hljs-comment">// 用更优雅更短的代码定义了 Axios.prototype.delete, Axios.prototype.get, Axios.prototype.head, Axios.prototype.options，这四个方法都不需要payload（代码中的data）</span>
utils.forEach([<span class="hljs-string">'delete'</span>, <span class="hljs-string">'get'</span>, <span class="hljs-string">'head'</span>, <span class="hljs-string">'options'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEachMethodNoData</span>(<span class="hljs-params">method</span>) </span>&#123;
  Axios.prototype[method] = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">url, config</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(utils.merge(config || &#123;&#125;, &#123;
      <span class="hljs-attr">method</span>: method,
      <span class="hljs-attr">url</span>: url
    &#125;));
  &#125;;
&#125;);

<span class="hljs-comment">// 用更优雅更短的代码定义了  Axios.prototype.put, Axios.prototype.post, Axios.prototype.patch，这三个方法都需要payload（代码中的data）</span>
utils.forEach([<span class="hljs-string">'post'</span>, <span class="hljs-string">'put'</span>, <span class="hljs-string">'patch'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEachMethodWithData</span>(<span class="hljs-params">method</span>) </span>&#123;
  Axios.prototype[method] = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">url, data, config</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(utils.merge(config || &#123;&#125;, &#123;
      <span class="hljs-attr">method</span>: method,
      <span class="hljs-attr">url</span>: url,
      <span class="hljs-attr">data</span>: data
    &#125;));
  &#125;;
&#125;);

<span class="hljs-built_in">module</span>.exports = Axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3. InterceptorManager文件</h3>
<p>由上述的<code>core/Axios.js</code>代码可以看出，在 Axios 的构造器里，request 和 response 拦截器就被初始化了，它们都是 InterceptorManager 实例，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 初始化 interceptors （拦截器）</span>
  <span class="hljs-built_in">this</span>.interceptors = &#123; 
    <span class="hljs-attr">request</span>: <span class="hljs-keyword">new</span> InterceptorManager(),
    <span class="hljs-attr">response</span>: <span class="hljs-keyword">new</span> InterceptorManager()
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来看看InterceptorManager的源码：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dd6cb40177c44db8c50867552405db0~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer">
我们可以看到这段代码是非常容易读的，包括了以下几点：</p>
<ol>
<li>InterceptorManager类</li>
<li>原型上的use方法——添加handler</li>
<li>原型上的eject方法——删除handler</li>
<li>原型上的forEach方法——依次调用handler</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> utils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./../utils'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">InterceptorManager</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.handlers = [];<span class="hljs-comment">// 内部使用一个简单数组存放所有 handler</span>
&#125;

<span class="hljs-comment">// use方法加入新的 handler —— 加到数组的尾部，返回所在的下标（即数组最后一位）作为 id</span>
InterceptorManager.prototype.use = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">use</span>(<span class="hljs-params">fulfilled, rejected</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.handlers.push(&#123;
    <span class="hljs-attr">fulfilled</span>: fulfilled,
    <span class="hljs-attr">rejected</span>: rejected
  &#125;);
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.handlers.length - <span class="hljs-number">1</span>;
&#125;;
<span class="hljs-comment">// 根据 id （实际上就是数组下标）废除使用指定的 handler</span>
InterceptorManager.prototype.eject = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">eject</span>(<span class="hljs-params">id</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.handlers[id]) &#123;
    <span class="hljs-built_in">this</span>.handlers[id] = <span class="hljs-literal">null</span>; 
  &#125;
&#125;;
<span class="hljs-comment">// 遍历所有非null的 handler，并且调用</span>
InterceptorManager.prototype.forEach = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEach</span>(<span class="hljs-params">fn</span>) </span>&#123;
  utils.forEach(<span class="hljs-built_in">this</span>.handlers, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEachHandler</span>(<span class="hljs-params">h</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (h !== <span class="hljs-literal">null</span>) &#123;
      fn(h);
    &#125;
  &#125;);
&#125;;
<span class="hljs-built_in">module</span>.exports = InterceptorManager;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，在<code>Axios.prototype.request</code>方法中，我们可以采用<code>this.interceptors.request.forEach</code>、<code>this.interceptors.response.forEach</code>进行拦截器的遍历。</p>
<p>我们来想一想，目前的request拦截器和response拦截器有哪些作用呢？</p>
<p><strong>request拦截器：</strong></p>
<ol>
<li>记录每次request的时间和内容</li>
<li>请求发送之前呈现loading效果</li>
<li>给request加额外的数据</li>
<li>验证request是否有合法权限</li>
<li>对请求数据进行统一预处理</li>
<li>……</li>
</ol>
<p><strong>response拦截器：</strong></p>
<ol>
<li>记录接收到响应的时间，从而可以记录整个请求花销的时间</li>
<li>处理完请求后呈现请求已完成的效果</li>
<li>网络抖动情况下使用重试机制</li>
<li>更改response状态码</li>
<li>对响应数据进行统一预处理</li>
<li>……</li>
</ol>
<h3 data-id="heading-13">4. dispatchRequest文件</h3>
<p>我们爱看看<code>Axios.prototype.request</code>里做了什么：</p>
<ol>
<li>用一个链表 把 request拦截器(interceptors.request) + 真正发起request(dispatchRequest) + response拦截器(interceptors.response) 连起来</li>
<li>用 promise 逐个调用这个链表</li>
<li>返回 promise 给调用者</li>
</ol>
<p>其中，有个核心的函数是<code>dispatchRequest</code>，<code>dispatchRequest</code>的代码也清晰易懂，其中包含了对于request 和 response 的处理 —— <code>transformRequest</code> 和 <code>transformResponse</code>。（可以具体看dispatchRequest.js的源码）。</p>
<p><strong>transformRequest做了以下的操作：</strong></p>
<ol>
<li>规范化header中的Content-Type</li>
<li>规范化request的data类型</li>
<li>根据数据类型补充request header（如果是json则转换成 json string）</li>
</ol>
<p><strong>transformResponse做了以下的操作：</strong>
将后端 response 的数据转化为 json 格式（默认）</p>
<pre><code class="hljs language-js copyable" lang="js">transformRequest: [<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformRequest</span>(<span class="hljs-params">data, headers</span>) </span>&#123;
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
    <span class="hljs-comment">// 根据数据类型 补充request header</span>
    <span class="hljs-keyword">if</span> (utils.isURLSearchParams(data)) &#123;
      setContentTypeIfUnset(headers, <span class="hljs-string">'application/x-www-form-urlencoded;charset=utf-8'</span>);
      <span class="hljs-keyword">return</span> data.toString();
    &#125;
    <span class="hljs-comment">// 根据数据类型 补充request header 且 转换成 json string</span>
    <span class="hljs-keyword">if</span> (utils.isObject(data)) &#123;
      setContentTypeIfUnset(headers, <span class="hljs-string">'application/json;charset=utf-8'</span>);
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.stringify(data);
    &#125;
    <span class="hljs-keyword">return</span> data;
  &#125;],

  <span class="hljs-comment">// 默认后端 response 的数据 是 json 格式</span>
  <span class="hljs-attr">transformResponse</span>: [<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformResponse</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'string'</span>) &#123;
      <span class="hljs-keyword">try</span> &#123;
        data = <span class="hljs-built_in">JSON</span>.parse(data);
      &#125; <span class="hljs-keyword">catch</span> (e) &#123; <span class="hljs-comment">/* Ignore */</span> &#125; <span class="hljs-comment">// “竟然” 默认吞掉了 error </span>
    &#125;
    <span class="hljs-keyword">return</span> data;
  &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">解答</h2>
<p>开头提出的问题的答案：</p>
<ol>
<li>为什么 axios 既可以当函数调用，也可以当对象使用，比如axios(&#123;&#125;)、axios.get。</li>
</ol>
<p>答：axios本质是函数，赋值了一些别名方法，比如get、post方法，可被调用，最终调用的还是Axios.prototype.request函数。</p>
<ol start="2">
<li>简述 axios 调用流程。</li>
</ol>
<p>答：实际是调用的Axios.prototype.request方法，最终返回的是promise链式调用，实际请求是在dispatchRequest中派发的。</p>
<ol start="3">
<li>拦截器吗原理是怎样的？</li>
</ol>
<p>答：用axios.interceptors.request.use添加请求成功和失败拦截器函数，用axios.interceptors.response.use添加响应成功和失败拦截器函数。在Axios.prototype.request函数组成promise链式调用时，Interceptors.protype.forEach遍历请求和响应拦截器添加到真正发送请求dispatchRequest的两端，从而做到请求前拦截和响应后拦截。拦截器也支持用Interceptors.protype.eject方法移除。</p>
<ol start="4">
<li>axios的取消功能是怎么实现的？</li>
</ol>
<p>答：通过传递config配置cancelToken的形式，来取消的。判断有传cancelToken，在promise链式调用的dispatchRequest抛出错误，在adapter中request.abort()取消请求，使promise走向rejected，被用户捕获取消信息。</p>
<ol start="5">
<li>为什么支持浏览器中发送请求也支持node发送请求？</li>
</ol>
<p>答：axios.defaults.adapter默认配置中根据环境判断是浏览器还是node环境，使用对应的适配器。适配器支持自定义。</p></div>  
</div>
            