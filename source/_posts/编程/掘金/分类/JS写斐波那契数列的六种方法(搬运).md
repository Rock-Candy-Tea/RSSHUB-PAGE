
---
title: 'JS写斐波那契数列的六种方法(搬运)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65802e70102f46d8941c5a08c80459c9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 08:00:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65802e70102f46d8941c5a08c80459c9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">JS写斐波那契数列的六种方法</h1>
<p>斐波那契数，指的是这样一个数列：1、1、2、3、5、8、13、21、……在数学上，斐波那契数列以如下被以递归的方法定义：F0=0，F1=1，Fn=Fn-1+Fn-2（n>=2，n∈N*），用文字来说，就是斐波那契数列由 0 和 1 开始，之后的斐波那契数列系数就由之前的两数相加。　　</p>
<blockquote>
<p>常用的计算斐波那契数列的方法分为两大类：递归和循环。</p>
</blockquote>
<h2 data-id="heading-1">递归</h2>
<h3 data-id="heading-2">方法一：普通递归</h3>
<p>代码优美逻辑清晰。但是有重复计算的问题，如：当n为5的时候要计算fibonacci(4) + fibonacci(3)，当n为4的要计算fibonacci(3) + fibonacci(2) ，这时fibonacci(3)就是重复计算了。运行 fibonacci(50) 会出现浏览器假死现象，毕竟递归需要堆栈，数字过大内存不够</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fibonacci</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (n == <span class="hljs-number">1</span> || n == <span class="hljs-number">2</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
    &#125;;
    <span class="hljs-keyword">return</span> fibonacci(n - <span class="hljs-number">2</span>) + fibonacci(n - <span class="hljs-number">1</span>);
&#125;
fibonacci(<span class="hljs-number">30</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">方法二：改进递归-把前两位数字做成参数避免重复计算</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fibonacci</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fib</span>(<span class="hljs-params">n, v1, v2</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (n == <span class="hljs-number">1</span>)
            <span class="hljs-keyword">return</span> v1;
        <span class="hljs-keyword">if</span> (n == <span class="hljs-number">2</span>)
            <span class="hljs-keyword">return</span> v2;
        <span class="hljs-keyword">else</span>
            <span class="hljs-keyword">return</span> fib(n - <span class="hljs-number">1</span>, v2, v1 + v2)
    &#125;
    <span class="hljs-keyword">return</span> fib(n, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>)
&#125;
fibonacci(<span class="hljs-number">30</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">方法三：改进递归-利用闭包特性把运算结果存储在数组里，避免重复计算</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fibonacci = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> memo = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>];
    <span class="hljs-keyword">let</span> fib = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (memo[n] == <span class="hljs-literal">undefined</span>) &#123;
            memo[n] = fib(n - <span class="hljs-number">2</span>) + fib(n - <span class="hljs-number">1</span>)
        &#125;
        <span class="hljs-keyword">return</span> memo[n]
    &#125;
    <span class="hljs-keyword">return</span> fib;
&#125;()
fibonacci(<span class="hljs-number">30</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">方法四：改进递归-摘出存储计算结果的功能函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> memoizer = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">func</span>) </span>&#123;
    <span class="hljs-keyword">let</span> memo = [];
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (memo[n] == <span class="hljs-literal">undefined</span>) &#123;
            memo[n] = func(n)
        &#125;
        <span class="hljs-keyword">return</span> memo[n]
    &#125;
&#125;;
<span class="hljs-keyword">var</span> fibonacci=memoizer(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>)</span>&#123;
    <span class="hljs-keyword">if</span> (n == <span class="hljs-number">1</span> || n == <span class="hljs-number">2</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
    &#125;;
    <span class="hljs-keyword">return</span> fibonacci(n - <span class="hljs-number">2</span>) + fibonacci(n - <span class="hljs-number">1</span>);
&#125;)
fibonacci(<span class="hljs-number">30</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">循环</h2>
<h3 data-id="heading-7">方法一：普通for循环</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fibonacci</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-keyword">var</span> n1 = <span class="hljs-number">1</span>, n2 = <span class="hljs-number">1</span>, sum;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>; i < n; i++) &#123;
        sum = n1 + n2
        n1 = n2
        n2 = sum
    &#125;
    <span class="hljs-keyword">return</span> sum
&#125;
fibonacci(<span class="hljs-number">30</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">方法二：for循环+解构赋值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fibonacci = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-keyword">let</span> n1 = <span class="hljs-number">1</span>; n2 = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>; i < n; i++) &#123;
        [n1, n2] = [n2, n1 + n2]
    &#125;
    <span class="hljs-keyword">return</span> n2
&#125;
fibonacci(<span class="hljs-number">30</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>各种方法运行耗时如下图：普通递归>改进递归>for循环</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65802e70102f46d8941c5a08c80459c9~tplv-k3u1fbpfcp-watermark.image" alt="1291436-20190928145638190-1462696850.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选自哥哦狗子, 感谢大佬分享
原文链接 :<a href="https://www.cnblogs.com/superlizhao/p/11603158.html" target="_blank" rel="nofollow noopener noreferrer"> https://www.cnblogs.com/superlizhao/p/11603158.html</a></p></div>  
</div>
            