
---
title: '深度剖析Javascript的柯里化机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6553'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 23:57:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=6553'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 30 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<blockquote>
<p>柯里化，可以理解为提前接收部分参数，延迟执行，不立即输出结果，而是返回一个接受剩余参数的函数。因为这样的特性，也被称为部分计算函数。柯里化，是一个逐步接收参数的过程。在接下来的剖析中，你会深刻体会到这一点。</p>
</blockquote>
<h2 data-id="heading-1">从一道面试题说起</h2>
<p>我们来看下这道面试题：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    sum(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>) <span class="hljs-comment">// 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要求该函数的返回结果为5，简单，我们来实现下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">b</span>) </span>&#123;
            <span class="hljs-keyword">return</span> a + b
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完美实现，这时候，题目需要加难度了，变成了这样</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    sum(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>)(<span class="hljs-number">4</span>)() <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>审题后发现，我们需要做以下几件事：</p>
<ol>
<li>多个参数，需要相加，如sum(2, 3)等价于sum(5)</li>
<li>调用次数是不确定的，不能像上面一样写死返回函数</li>
<li>调用的参数为空时，需要返回结果</li>
</ol>
<p>代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">currying</span>(<span class="hljs-params">fn</span>)</span>&#123;
        <span class="hljs-keyword">var</span> allArgs = [];

        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">var</span> args = [].slice.call(<span class="hljs-built_in">arguments</span>);

            <span class="hljs-keyword">if</span>(args.length > <span class="hljs-number">0</span>)&#123;
                allArgs = allArgs.concat(args);
                <span class="hljs-keyword">return</span> next;
            &#125;<span class="hljs-keyword">else</span>&#123;
                <span class="hljs-keyword">return</span> fn.apply(<span class="hljs-literal">null</span>, allArgs);
            &#125;
        &#125; 
    &#125;

    <span class="hljs-keyword">var</span> sum = currying(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> _sum = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">arguments</span>.length; i++)&#123;
            _sum += <span class="hljs-built_in">arguments</span>[i];
        &#125;
        <span class="hljs-keyword">return</span> _sum;
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于是延迟计算结果，所以要对参数进行记忆。</p>
<p>这里的实现方式是采用闭包。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">currying</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-keyword">var</span> allArgs = [];

    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> args = [].slice.call(<span class="hljs-built_in">arguments</span>);

        <span class="hljs-keyword">if</span>(args.length > <span class="hljs-number">0</span>)&#123;
            allArgs = allArgs.concat(args);
            <span class="hljs-keyword">return</span> next;
        &#125;
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当执行var add = currying(...)时，add变量已经指向了next方法。此时，allArgs在next方法内部有引用到，所以不能被GC回收。也就是说，allArgs在该赋值语句执行后，一直存在，形成了闭包。</p>
<p>依靠这个特性，只要把接收的参数，不断放入allArgs变量进行存储即可。</p>
<p>所以，当arguments.length > 0时，就可以将接收的新参数，放到allArgs中。</p>
<p>最后返回next函数指针，形成链式调用。</p>
<p>另外，由于计算结果的方法，是作为参数传入currying函数，所以要利用apply进行执行。</p>
<p>综合上述思考，就可以得到以下完整的柯里化函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">currying</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-keyword">var</span> allArgs = []; <span class="hljs-comment">// 用来接收参数</span>

    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> args = [].slice.call(<span class="hljs-built_in">arguments</span>);

        <span class="hljs-comment">// 判断是否执行计算</span>
        <span class="hljs-keyword">if</span>(args.length > <span class="hljs-number">0</span>)&#123;
            allArgs = allArgs.concat(args); <span class="hljs-comment">// 收集传入的参数，进行缓存</span>
            <span class="hljs-keyword">return</span> next;
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-keyword">return</span> fn.apply(<span class="hljs-literal">null</span>, allArgs); <span class="hljs-comment">// 符合执行条件，执行计算</span>
        &#125;
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">小结</h2>
<p>最后，我们再来总结一下柯里化机制：</p>
<ol>
<li>逐步接收参数，形式包含多个参数、多次调用，并缓存供后期计算使用</li>
<li>最后发出计算指令后，计算返回</li>
</ol></div>  
</div>
            