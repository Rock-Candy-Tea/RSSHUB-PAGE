
---
title: 'try...catch错误捕获'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a1e0da79794ec996471a1ff547778f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 19:24:22 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a1e0da79794ec996471a1ff547778f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h3 data-id="heading-0">前言</h3>
<p>最近写快应用，有个数据格式转化的问题。为了防止后端数据出错，就加了个try...catch来错误捕获。结果发现有些情况明明数据出问题了，却没有将异常抛出来，后来仔细分析了下，原来因为代码在报错的时候，try...catch已经执行完了。这篇文章就来整理下try...catch的具体用法。</p>
<h3 data-id="heading-1">try...catch</h3>
<p>首先来看下try...catch的作用：</p>
<blockquote>
<p>try...catch能捕获的异常必须是线程执行进入到try...catch且try...catch未执行完的时候抛出来。</p>
</blockquote>
<h4 data-id="heading-2">1. 进入之前</h4>
<p>语法异常在语法检查阶段就报错了，线程尚未进入try...catch代码块，所以无法捕获到异常。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span> &#123;
    a.
&#125;<span class="hljs-keyword">catch</span>(e) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error-------'</span>, e);
&#125;

<span class="hljs-comment">// 执行结果：</span>
<span class="hljs-attr">VM483</span>:<span class="hljs-number">3</span> Uncaught <span class="hljs-built_in">SyntaxError</span>: Unexpected token <span class="hljs-string">'&#125;'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2. 进入之中</h4>
<p>代码报错的时候，线程处于try...catch之中，能够捕获到异常。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span> &#123;
    a.b
&#125;<span class="hljs-keyword">catch</span>(e) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error-------'</span>, e);
&#125;

<span class="hljs-attr">VM488</span>:<span class="hljs-number">4</span> error------- <span class="hljs-built_in">ReferenceError</span>: a is not defined
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">3. 进入之后</h4>
<p>代码报错的时候，线程已经执行完try...catch，这种无法捕获异常。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        a.b = <span class="hljs-number">1</span>;
    &#125;, <span class="hljs-number">1000</span>)
&#125;<span class="hljs-keyword">catch</span>(e) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error---------'</span>, e);
&#125;


<span class="hljs-comment">// 执行结果：</span>
<span class="hljs-attr">VM544</span>:<span class="hljs-number">3</span> Uncaught <span class="hljs-built_in">ReferenceError</span>: a is not defined
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>try...catch无法捕获异步代码中抛出的错误，如果要捕获则应该将try...catch代码写到异步代码内部。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">try</span>&#123;
        a.b = <span class="hljs-number">1</span>;
    &#125;<span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error---------'</span>, e);
    &#125;
&#125;, <span class="hljs-number">1000</span>)

<span class="hljs-comment">// 执行结果：</span>
error--------- <span class="hljs-built_in">ReferenceError</span>: a is not defined at <anonymous>:<span class="hljs-number">3</span>:<span class="hljs-number">9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">4. Promise的异常</h4>
<p>线程在执行a.b的时候，try...catch也在同步执行。为啥也没捕获到异常？？</p>
<p>Promise在执行的时候，函数代码周围都是有个隐式的try...catch包裹的，所有的同步异常都会被内部捕获到，但是并不会往上抛异常。所以我们写的try...catch并不会捕获到。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span>&#123;
    <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
        a.b;
    &#125;).then(<span class="hljs-function"><span class="hljs-params">v</span>=></span>&#123;
        <span class="hljs-built_in">console</span>.log(v);
    &#125;);
&#125;<span class="hljs-keyword">catch</span>(e)&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error---------------'</span>,e);
&#125;


<span class="hljs-comment">// 执行结果：</span>
<span class="hljs-built_in">Promise</span> &#123;<rejected>: <span class="hljs-built_in">ReferenceError</span>: a is not defined
    at <anonymous>:<span class="hljs-number">3</span>:<span class="hljs-number">9</span>
    at <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span> (<anonymous>)
    at <an…&#125;__proto__: <span class="hljs-built_in">Promise</span>[[PromiseState]]: <span class="hljs-string">"rejected"</span>[[PromiseResult]]: <span class="hljs-built_in">ReferenceError</span>: a is not defined
    at <anonymous>:<span class="hljs-number">3</span>:<span class="hljs-number">9</span>
    at <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span> (<anonymous>)
    at <anonymous>:<span class="hljs-number">2</span>:<span class="hljs-number">5</span>
    
<span class="hljs-attr">VM552</span>:<span class="hljs-number">3</span> Uncaught (<span class="hljs-keyword">in</span> promise) <span class="hljs-built_in">ReferenceError</span>: a is not defined
    at <anonymous>:<span class="hljs-number">3</span>:<span class="hljs-number">9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">5. async...await异常</h4>
<p>如何用try...catch去捕获async...await的错误呢？？</p>
<p>是不是像Promise那样直接写在async最外层？？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'await错误'</span>));
    &#125;
    f1();
&#125;<span class="hljs-keyword">catch</span>(e) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>, e)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a1e0da79794ec996471a1ff547778f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将try...catch写在async函数最外层并不能捕获async...await的异常，而是会走到Promise的异常抛出。</p>
<p>那如果将try...catch写在await呢？？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">try</span>&#123;
        <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'await出错'</span>));
    &#125;<span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>, e);
    &#125;
&#125;
f2();

<span class="hljs-comment">//执行结果：</span>
<span class="hljs-number">111</span> <span class="hljs-built_in">Error</span>: <span class="hljs-keyword">await</span>出错 at f2 (<anonymous>:<span class="hljs-number">3</span>:<span class="hljs-number">30</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>async...await捕获异常，需要将await函数写在try...catch中。</p>
</blockquote></div>  
</div>
            