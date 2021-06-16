
---
title: '函数式编程 - 柯里化 (Haskell Brooks Curry)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8902'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 17:23:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=8902'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">什么是柯里化</h4>
<ol>
<li>当一个函数有多个参数的时候先传递一部分参数调用它（这部分参数以后永远不变）</li>
<li>然后返回一个新的函数接收剩余的参数，返回结果</li>
</ol>
<ul>
<li>普通函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkAge</span> (<span class="hljs-params">age</span>) </span>&#123;
    <span class="hljs-keyword">let</span> min = <span class="hljs-number">18</span>;
    <span class="hljs-keyword">return</span> age >= min;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用柯里化的函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//使用柯里化解决上一个案例中硬编码的问题</span>
<span class="hljs-comment">// 柯里化</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkAge</span> (<span class="hljs-params">min</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">age</span>) </span>&#123;
        <span class="hljs-keyword">return</span> age >= min;
    &#125;
&#125;

<span class="hljs-comment">// es6</span>
<span class="hljs-keyword">let</span> checkAge = <span class="hljs-function"><span class="hljs-params">min</span> =></span> (<span class="hljs-function"><span class="hljs-params">age</span> =></span> age >= min);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">lodash中的柯里化函数</h4>
<p><strong>_.curry(func)</strong></p>
<ul>
<li>功能：创建一个函数，该函数接收一个或多个func的参数，如果func所需要的参数都被提供则执行func并返回执行的结果。否则继续返回该函数并等待接收剩余的参数。</li>
<li>参数：需要柯里化的函数</li>
<li>返回值：柯里化后的函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)
<span class="hljs-comment">// 要柯里化的函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSum</span> (<span class="hljs-params">a, b, c</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b + c;
&#125;
<span class="hljs-comment">// 柯里化后的函数</span>
<span class="hljs-keyword">let</span> curried = _.curry()
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>手写curry</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSum</span>(<span class="hljs-params">a, b, c</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b + c;
&#125;

<span class="hljs-keyword">const</span> curried = curry(getSum);

<span class="hljs-built_in">console</span>.log(curried(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>));
<span class="hljs-built_in">console</span>.log(curried(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>));
<span class="hljs-built_in">console</span>.log(curried(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)(<span class="hljs-number">3</span>));

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curry</span> (<span class="hljs-params">func</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curriedFn</span> (<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-comment">// 判断实参和形参的个数</span>
    <span class="hljs-keyword">if</span> (args.length < func.length) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 注意：这里有些博客用的 arguments.callee</span>
        <span class="hljs-comment">// 这个在es5的严格模式下禁止了</span>
        <span class="hljs-comment">// https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/arguments/callee</span>
        <span class="hljs-keyword">return</span> curriedFn(...args.concat(<span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>)));
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> func(...args);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">柯里化总结</h4>
<ul>
<li>柯里化可以让我闪给一个函数传递较少的参数得到一个已经记住了某些固定参数的新函数</li>
<li>这是一种对函数参数的'缓存'</li>
<li>让函数变得更灵活，让函数的粒度更小</li>
<li>可以把多无函数转换成一元函数，可以组合使用函数产生强大的功能</li>
</ul></div>  
</div>
            