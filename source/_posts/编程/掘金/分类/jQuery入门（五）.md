
---
title: 'jQuery入门（五）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5939'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 20:07:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=5939'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">发送 ajax 请求</h2>
<ul>
<li>
<p>发送 get 请求</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 直接使用 $.get 方法来发送一个请求</span>
<span class="hljs-comment">/*
参数一： 请求地址
参数二： 请求时携带的参数
参数三： 请求成功的回调
参数四： 返回的数据类型
*/</span>
$.get(<span class="hljs-string">'./ajax.php'</span>, &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">10</span> &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123; <span class="hljs-built_in">console</span>.log(res) &#125;, <span class="hljs-string">'json'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>发送 post 请求</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 直接使用 $.post 方法来发送一个请求</span>
<span class="hljs-comment">/*
参数一： 请求地址
参数二： 请求时携带的参数
参数三： 请求成功的回调
参数四： 返回的数据类型
*/</span>
$.post(<span class="hljs-string">'./ajax.php'</span>, &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">10</span> &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123; <span class="hljs-built_in">console</span>.log(res) &#125;, <span class="hljs-string">'json'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>综合发送 ajax 请求</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用 $.ajax 方法</span>
<span class="hljs-comment">// 只接受一个参数，是一个对象，这个对象对当前的请求进行所有的配置</span>
$.ajax(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">'./ajax'</span>,   <span class="hljs-comment">// 必填，请求的地址</span>
    <span class="hljs-attr">type</span>: <span class="hljs-string">'GET'</span>,   <span class="hljs-comment">// 选填，请求方式，默认是 GET（忽略大小写）</span>
    <span class="hljs-attr">data</span>: &#123;&#125;,   <span class="hljs-comment">// 选填，发送请求是携带的参数</span>
    <span class="hljs-attr">dataType</span>: <span class="hljs-string">'json'</span>,   <span class="hljs-comment">// 选填，期望返回值的数据类型，默认是 string</span>
    <span class="hljs-attr">async</span>: <span class="hljs-literal">true</span>,   <span class="hljs-comment">// 选填，是否异步，默认是 true</span>
    success () &#123;&#125;,   <span class="hljs-comment">// 选填，成功的回调函数</span>
    error () &#123;&#125;,   <span class="hljs-comment">// 选填，失败的回调函数</span>
    <span class="hljs-attr">cache</span>: <span class="hljs-literal">true</span>,   <span class="hljs-comment">// 选填，是否缓存，默认是 true</span>
    <span class="hljs-attr">context</span>: div,   <span class="hljs-comment">// 选填，回调函数中的 this 指向，默认是 ajax 对象</span>
    <span class="hljs-attr">status</span>: &#123;&#125;,   <span class="hljs-comment">// 选填，根据对应的状态码进行函数执行</span>
    <span class="hljs-attr">timeout</span>: <span class="hljs-number">1000</span>,   <span class="hljs-comment">// 选填，超时事件</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>发送一个 jsonp 请求</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用 $.ajax 方法也可以发送 jsonp 请求</span>
<span class="hljs-comment">// 只不过 dataType 要写成 jsonp</span>
$.ajax(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">'./jsonp.php'</span>,
    <span class="hljs-attr">dataType</span>: <span class="hljs-string">'jsonp'</span>,
    <span class="hljs-attr">data</span>: &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Jack'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;,
    success (res) &#123;
        <span class="hljs-built_in">console</span>.log(res)
    &#125;,
    <span class="hljs-attr">jsonp</span>: <span class="hljs-string">'cb'</span>,  <span class="hljs-comment">// jsonp 请求的时候回调函数的 key</span>
    <span class="hljs-attr">jsonpCallback</span>: <span class="hljs-string">'fn'</span>   <span class="hljs-comment">// jsonp 请求的时候回调函数的名称</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-1">全局 ajax 函数</h2>
<ul>
<li>全局的 <code>ajax</code> 函数我们也叫做 <strong><code>ajax</code> 的钩子函数</strong></li>
<li>也就是在一个 <code>ajax</code> 的整个过程中的某一个阶段执行的函数</li>
<li>而且每一个 <code>ajax</code> 请求都会触发</li>
</ul>
<h3 data-id="heading-2">ajaxStart</h3>
<ul>
<li>
<p>任意一个请求在 <strong>开始</strong> 的时候就会触发这个函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">$(<span class="hljs-built_in">window</span>).ajaxStart(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'有一个请求开始了'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-3">ajaxSend</h3>
<ul>
<li>
<p>任意一个请求在 <strong>准备 send 之前</strong> 会触发这个函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">$(<span class="hljs-built_in">window</span>).ajaxSend(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'有一个要发送出去了'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">ajaxSuccess</h3>
<ul>
<li>
<p>任意一个请求在 <strong>成功</strong> 的时候就会触发这个函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">$(<span class="hljs-built_in">window</span>).ajaxSuccess(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'有一个请求成功了'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            