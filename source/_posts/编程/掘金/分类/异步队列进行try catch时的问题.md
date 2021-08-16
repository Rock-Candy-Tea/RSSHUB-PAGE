
---
title: '异步队列进行try catch时的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8377'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 19:21:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=8377'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>我们在写js的时候，经常的会遇到需要异步去请求接口，或者通过setTimeout或Promise去做什么事， 然后让同步进程继续向下走， 当到某个时间节点的时候或者数据请求成功的时候在通过<code>eventloop</code>的方式回调执行。这本身是js的特点和优势。</p>
<p>但是，异步队列执行也存在错误的情况，这时，对于怎么进行错误处理，就成了我们的重点。</p>
<p>想一下项目中用到的方式，或者jquery的ajax方式，一般都会有catch、fail之类的回调方法供我们对错误结果进行处理。 那么现在讨论的话题是能不能使用<code>try catch</code>进行处理。</p>
<p>为什么写这篇文章？ 是因为我在写 <a href="https://juejin.cn/post/6995566641618616327" target="_blank" title="https://juejin.cn/post/6995566641618616327">10分钟了解express和koa中间件机制和错误处理机制 </a> 的时候，举例express的异步错误获取的时候，想到了这个点，我觉得有必要单独拿出来，写一篇断篇幅的，又能够清晰明了表达的一篇文章。于是这篇文章便生成了。</p>
<p>好了， 正文开始。</p>
<h2 data-id="heading-1">二、主要讲的异步队列方法</h2>
<h3 data-id="heading-2">2.1 setTimeout</h3>
<p>这里的setTimeout指的是一类，包括 <code>setTimeout</code>, <code>setInterval</code>这类所谓宏任务。
他们可以用try catch来捕获错误么?</p>
<h4 data-id="heading-3">2.1.1 问题表现</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">try</span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">let</span> a = c;
        &#125;, <span class="hljs-number">100</span>)
    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'能获取到错误么？？'</span>, e);
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果是不能获取到，程序直接报错了， 那么出现的后果可能就是整个页面挂了，或者在node中，整个服务挂了。 我们的初心是想让程序更加健壮，但却做了无用功。</p>
<p>那么我们在想，既然在setTimeout 外边无法获取，那么能不能在setTimeout里面先用try catch获取一下，然后捕获到错误后再传出去呢？ 想到就干，继续分析：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">try</span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
                <span class="hljs-keyword">let</span> a = c;
            &#125; <span class="hljs-keyword">catch</span>(e) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'some variable is not defined'</span>);
            &#125;
        &#125;, <span class="hljs-number">100</span>)
    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'能获取到错误么？？'</span>, e);
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>很抱歉，想法很好，但是也不行。<code>外边也catch不到</code>。</p>
<h4 data-id="heading-4">2.1.2 问题原因</h4>
<p>好了，我们把这个疑问分析一下吧。其实，这里的根本原因还是刚开始提到的<code>事件循环</code>。 事件循环不是空空的一句表述、一个概念，而是在代码中实实在在存在的。</p>
<p>具体事件循环的相关知识，可以看下我很早前写的<a href="https://juejin.cn/post/6844903795982499848" target="_blank" title="https://juejin.cn/post/6844903795982499848"># 从setTimeout说到事件循环机制(event-loop) </a> 文章。</p>
<p>回到这个例子中， 最外层的try catch是在一个<code>task</code>中，我们定义它为我们js文件的同步主任务，从上到下执行到这里了， 然后，会把里面的setTimeout推到一个<code>任务队列</code>中， 这个队列是存储在内存中的，由V8来管理。然后主task就继续向下执行， 一直到结束。</p>
<p>当该setTimeout时间到了，且没有其它的task执行了， 那么，就将这个setTimeout的代码推入<code>执行栈</code>开始执行。 当执行到错误代码的时候，也就是这个 <code>let a = c</code>, 因为c未定义，所以就会报错。</p>
<p>但问题的本质是，<strong>这个错误跟最外层的try catch并不在一个执行栈中，当里面执行的时候，外边的这个task早已执行完， 他们的context(上下文)已经完全不同了。</strong></p>
<p>所以，页面会直接报错，甚至程序崩溃。</p>
<h3 data-id="heading-5">2.2 Promise</h3>
<p>我们知道，<code>Promise</code> 也是一个异步的处理过程，它对应事件循环中的<code>微任务</code>。 那么这里其实与上面的setTimeout存在同样的问题。</p>
<p>举个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            reject(<span class="hljs-string">'promise error'</span>);
        &#125;)
    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'异步错误，能catch到么？？'</span>, e);
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信大家能够推导出结果了： <code>也catch不到</code></p>
<p>原因其实与上面的setTimeout是一样的，执行栈上下文已经不同了。</p>
<p>那么针对Promise，ECMA官方已经给我们提供了一个方法，那就是 <code>catch</code>， 通过catch我们获取到错误，可以阻止程序崩溃。 但是喜欢发散思维的你可能会想到， 那我用catch接到了，是不是就可以让外层的catch获取到了呢？ 想到就试一下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            reject(<span class="hljs-string">'promise error'</span>);
        &#125;).catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(e);
        &#125;)
    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'异步错误，能catch到么？？'</span>, e);
    &#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果就是 <code>不行</code>。相信大家通过我详细的例子和思维脉络，对这块已经真正掌握了吧？</p>
<p>哈哈，看到这里就应该给点个赞了~~😀</p>
<h3 data-id="heading-6">2.3 callback</h3>
<p>那么通过上面的，大家可能会有一种想法，只要是callback，就是catch不住的。 其实这种想法是错误的，我通过一个例子来证明。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fn</span>(<span class="hljs-params">cb</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'callback执行了'</span>);
        cb();
    &#125;

    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> cb = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'callback执行错误'</span>);
        &#125;
        Fn(cb);
    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'能够catch住么???'</span>)
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这里就是个烟雾弹， 考验大家对这个事件循环相关机制是不是明白了。</p>
<h3 data-id="heading-7">2.4 Async await</h3>
<p>现在的项目中，大家越来越愿意使用<code>Async await</code> 这对 es7标准里的api了。 因为它们这对组合是在是太好用了。 那么通过异步等待的方式，用try catch能够行么?</p>
<p>那么咱们使用一个例子验证一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> asyncFn = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            reject(<span class="hljs-string">'asyncFn执行时出现错误了'</span>)
        &#125;, <span class="hljs-number">100</span>);
    &#125;)
&#125;

<span class="hljs-keyword">const</span> executedFn = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">try</span>&#123;
        <span class="hljs-keyword">await</span> asyncFn();
    &#125;<span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'拦截到错误..'</span>, e);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果执行一下，就发现： <code>catch到了!</code></p>
<p><code>asyncFn</code>里面是有 Promise的，为什么外边就能catch到了呢？ 是不是跟上面讲的矛盾了呢？ 其实并没有。 看我分析一下：</p>
<p><code>async-await 是使用生成器、promise 和协程实现的,wait操作符还存储返回事件循环之前的执行上下文，以便允许promise操作继续进行。当内部通知解决等待的承诺时，它会在继续之前恢复执行上下文。</code> 所以说，能够回到最外层的上下文， 那就可以用try catch 啦。</p>
<p>简单的写了这么多，对一些机制没有太深入的去谈， 大家有兴趣可以先自行向下深挖一下。 或者评论留言，大家一起研究~~</p></div>  
</div>
            