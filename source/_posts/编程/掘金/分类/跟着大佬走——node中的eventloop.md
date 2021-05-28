
---
title: '跟着大佬走——node中的eventloop'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f695f843e24fadadbf0103b9275a00~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 17:49:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f695f843e24fadadbf0103b9275a00~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>废话不多说，书接上文。</p>
<h2 data-id="heading-0">node 中的 eventloop</h2>
<p>node 也是单线程，在处理 eventloop 上与浏览器稍有不同，从 API 层面来看，node 增加了两个方法<code>process.nextTick</code>,<code>setImmediate</code></p>
<p>前文中我们提到过，node 中 eventloop 是基于 libuv 的库，那么这个库的实现机制是什么呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f695f843e24fadadbf0103b9275a00~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#event-loop-explained," title="1" target="_blank" rel="nofollow noopener noreferrer">官网</a>对此的解释为:</p>
<blockquote>
<ul>
<li>定时器（timers）：本阶段执行已经被 <code>setTimeout()</code> 和 <code>setInterval()</code> 的调度回调函数。</li>
<li>待定回调（pending callbacks）：执行延迟到下一个循环迭代的 I/O 回调。</li>
<li>idle, prepare：仅系统内部使用。</li>
<li>轮询（poll）：检索新的 I/O 事件；执行与 I/O 相关的回调（几乎所有情况下，除了关闭的回调函数，那些由计时器和 <code>setImmediate()</code> 调度的之外），其余情况 Node 将在适当的时候在此阻塞。</li>
<li>检测（check）：<code>setImmediate()</code> 回调函数在这里执行。</li>
<li>关闭的回调函数（close callbacks）：一些关闭的回调函数，如：socket.on('close', ...)。</li>
</ul>
</blockquote>
<h2 data-id="heading-1">setTimeout & setImmediate</h2>
<p>show me the code:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'timeout'</span>);
&#125;, <span class="hljs-number">0</span>);

setImmediate(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'immediate'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>node 环境下运行结果为：</p>
<pre><code class="hljs language-js copyable" lang="js">timeout
immediate
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<pre><code class="hljs language-js copyable" lang="js">immediate
timeout
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想不到吧，我们来看下官方解释：</p>
<p>首先，执行计时器的顺序将根据调用它们的<strong>上下文</strong>而异。</p>
<p>其次，若从主模块内部调用，择机时期受<strong>进程</strong>约束。</p>
<p>若在 I/O 循环内，那么<code>setImmediate</code>总是被有限次调用。</p>
<p>借用一位博主的话解释就是：</p>
<p><a href="https://juejin.cn/post/6844904021296316429#heading-8," title="2" target="_blank">使用 setImmediate 相对 setTimeout 的优势主要在于：无论存在多少个定时器，在 IO 周期内，setImmediate 总是在所有定时器前执行。</a></p>
<h2 data-id="heading-2">process.nextTick()</h2>
<p>这个 api 类似昨天文章中的 <code>Promise</code> 或是 <code>MutationObserver</code> 微任务实现，在代码块中可以随时插<strong>保证</strong>在下一个宏任务开始前执行。</p>
<p>show me the code：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Lib</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">require</span>('<span class="hljs-title">events</span>').<span class="hljs-title">EventEmitter</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-built_in">super</span>()

    <span class="hljs-built_in">this</span>.emit(<span class="hljs-string">'init'</span>)
  &#125;
&#125;

<span class="hljs-keyword">const</span> lib = <span class="hljs-keyword">new</span> Lib()

lib.on(<span class="hljs-string">'init'</span>, <span class="hljs-function"><span class="hljs-params">_</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'init!'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上方代码段可看出，console 永远不会执行。让我们看看，怎么用<code>process.nextTick</code> 搞定输出问题：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Lib</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">require</span>('<span class="hljs-title">events</span>').<span class="hljs-title">EventEmitter</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-built_in">super</span>()

    process.nextTick(<span class="hljs-function"><span class="hljs-params">_</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.emit(<span class="hljs-string">'init'</span>)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是很简单！当 node 主线程执行完毕后，程序触发 eventloop 流程查找有误微任务，发现微任务队列不为空时，则发送 init 事件。</p>
<p>浏览器端可用 Promise.resolve() 实现同样效果。</p></div>  
</div>
            