
---
title: 'JavaScript 中如何实现并发控制？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0375eb9d15849e08df0b8c39ed45490~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 15:53:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0375eb9d15849e08df0b8c39ed45490~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、并发控制简介</h3>
<p>在日常开发过程中，你可能会遇到并发控制的场景，比如控制请求并发数。那么在 JavaScript 中如何实现并发控制呢？在回答这个问题之前，我们来简单介绍一下并发控制。</p>
<p>假设有 6 个待办任务要执行，而我们希望限制同时执行的任务个数，即最多只有 2 个任务能同时执行。当 <strong>正在执行任务列表</strong> 中的任何 1 个任务完成后，程序会自动从 <strong>待办任务列表</strong> 中获取新的待办任务并把该任务添加到 <strong>正在执行任务列表</strong> 中。为了让大家能够更直观地理解上述的过程，阿宝哥特意画了以下 3 张图：</p>
<h4 data-id="heading-1">1.1 阶段一</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0375eb9d15849e08df0b8c39ed45490~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">1.2 阶段二</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33ebdd25cd5e48d0b0970af7599a5e90~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">1.3 阶段三</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab850a9e11564452b1d507c8b2efc311~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好的，介绍完并发控制之后，阿宝哥将以 Github 上 <a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a> 这个库来介绍一下异步任务并发控制的具体实现。</p>
<blockquote>
<p><a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a>：<a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">github.com/rxaviers/as…</a></p>
<p><strong>Run multiple promise-returning & async functions with limited concurrency using native ES6/ES7。</strong></p>
</blockquote>
<p>针对 <a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a> 这个库的具体应用，阿宝哥写了 <a href="https://mp.weixin.qq.com/s/E4SdYEkEzurfrnJrBu3bjA" target="_blank" rel="nofollow noopener noreferrer">JavaScript 中如何实现大文件并发下载？</a> 和 <a href="https://mp.weixin.qq.com/s/-iSpCMaLruerHv7717P0Wg" target="_blank" rel="nofollow noopener noreferrer">JavaScript 中如何实现大文件并发上传？</a> 两篇文章，感兴趣的小伙伴可以了解一下。</p>
<h3 data-id="heading-4">二、并发控制的实现</h3>
<p><a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a> 这个库提供了 ES7 和 ES6 两种不同版本的实现，在分析其具体实现之前，我们来看一下它如何使用。</p>
<h4 data-id="heading-5">2.1 asyncPool 的使用</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> timeout = <span class="hljs-function"><span class="hljs-params">i</span> =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> resolve(i), i));
<span class="hljs-keyword">await</span> asyncPool(<span class="hljs-number">2</span>, [<span class="hljs-number">1000</span>, <span class="hljs-number">5000</span>, <span class="hljs-number">3000</span>, <span class="hljs-number">2000</span>], timeout);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，我们使用 <a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a> 这个库提供的 <code>asyncPool</code> 函数来实现异步任务的并发控制。 <code>asyncPool</code> 函数的签名如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncPool</span>(<span class="hljs-params">poolLimit, array, iteratorFn</span>)</span>&#123; ... &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该函数接收 3 个参数：</p>
<ul>
<li><code>poolLimit</code>（数字类型）：表示限制的并发数；</li>
<li><code>array</code>（数组类型）：表示任务数组；</li>
<li><code>iteratorFn</code>（函数类型）：表示迭代函数，用于实现对每个任务项进行处理，该函数会返回一个 Promise 对象或异步函数。</li>
</ul>
<p>对于以上示例来说，在使用了 <code>asyncPool</code> 函数之后，对应的执行过程如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> timeout = <span class="hljs-function"><span class="hljs-params">i</span> =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> resolve(i), i));
<span class="hljs-keyword">await</span> asyncPool(<span class="hljs-number">2</span>, [<span class="hljs-number">1000</span>, <span class="hljs-number">5000</span>, <span class="hljs-number">3000</span>, <span class="hljs-number">2000</span>], timeout);
<span class="hljs-comment">// Call iterator (i = 1000)</span>
<span class="hljs-comment">// Call iterator (i = 5000)</span>
<span class="hljs-comment">// Pool limit of 2 reached, wait for the quicker one to complete...</span>
<span class="hljs-comment">// 1000 finishes</span>
<span class="hljs-comment">// Call iterator (i = 3000)</span>
<span class="hljs-comment">// Pool limit of 2 reached, wait for the quicker one to complete...</span>
<span class="hljs-comment">// 3000 finishes</span>
<span class="hljs-comment">// Call iterator (i = 2000)</span>
<span class="hljs-comment">// Itaration is complete, wait until running ones complete...</span>
<span class="hljs-comment">// 5000 finishes</span>
<span class="hljs-comment">// 2000 finishes</span>
<span class="hljs-comment">// Resolves, results are passed in given array order `[1000, 5000, 3000, 2000]`.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过观察以上的注释信息，我们可以大致地了解 <code>asyncPool</code> 函数内部的控制流程。下面我们先来分析 <code>asyncPool</code> 函数的 ES7 实现。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 50 几篇 TS 系列教程。</p>
</blockquote>
<h4 data-id="heading-6">2.2 asyncPool ES7 实现</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncPool</span>(<span class="hljs-params">poolLimit, array, iteratorFn</span>) </span>&#123;
  <span class="hljs-keyword">const</span> ret = []; <span class="hljs-comment">// 存储所有的异步任务</span>
  <span class="hljs-keyword">const</span> executing = []; <span class="hljs-comment">// 存储正在执行的异步任务</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> array) &#123;
    <span class="hljs-comment">// 调用iteratorFn函数创建异步任务</span>
    <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> iteratorFn(item, array));
    ret.push(p); <span class="hljs-comment">// 保存新的异步任务</span>

    <span class="hljs-comment">// 当poolLimit值小于或等于总任务个数时，进行并发控制</span>
    <span class="hljs-keyword">if</span> (poolLimit <= array.length) &#123;
      <span class="hljs-comment">// 当任务完成后，从正在执行的任务数组中移除已完成的任务</span>
      <span class="hljs-keyword">const</span> e = p.then(<span class="hljs-function">() =></span> executing.splice(executing.indexOf(e), <span class="hljs-number">1</span>));
      executing.push(e); <span class="hljs-comment">// 保存正在执行的异步任务</span>
      <span class="hljs-keyword">if</span> (executing.length >= poolLimit) &#123;
        <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.race(executing); <span class="hljs-comment">// 等待较快的任务执行完成</span>
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(ret);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，充分利用了 <code>Promise.all</code> 和 <code>Promise.race</code> 函数特点，再结合 ES7 中提供的 <code>async await</code> 特性，最终实现了并发控制的功能。利用 <code>await Promise.race(executing);</code> 这行语句，我们会等待 <strong>正在执行任务列表</strong> 中较快的任务执行完成之后，才会继续执行下一次循环。</p>
<p>asyncPool ES7 实现相对比较简单，接下来我们来看一下不使用 <code>async await</code> 特性要如何实现同样的功能。</p>
<h4 data-id="heading-7">2.3 asyncPool ES6 实现</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncPool</span>(<span class="hljs-params">poolLimit, array, iteratorFn</span>) </span>&#123;
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">const</span> ret = []; <span class="hljs-comment">// 存储所有的异步任务</span>
  <span class="hljs-keyword">const</span> executing = []; <span class="hljs-comment">// 存储正在执行的异步任务</span>
  <span class="hljs-keyword">const</span> enqueue = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (i === array.length) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve();
    &#125;
    <span class="hljs-keyword">const</span> item = array[i++]; <span class="hljs-comment">// 获取新的任务项</span>
    <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> iteratorFn(item, array));
    ret.push(p);

    <span class="hljs-keyword">let</span> r = <span class="hljs-built_in">Promise</span>.resolve();

    <span class="hljs-comment">// 当poolLimit值小于或等于总任务个数时，进行并发控制</span>
    <span class="hljs-keyword">if</span> (poolLimit <= array.length) &#123;
      <span class="hljs-comment">// 当任务完成后，从正在执行的任务数组中移除已完成的任务</span>
      <span class="hljs-keyword">const</span> e = p.then(<span class="hljs-function">() =></span> executing.splice(executing.indexOf(e), <span class="hljs-number">1</span>));
      executing.push(e);
      <span class="hljs-keyword">if</span> (executing.length >= poolLimit) &#123;
        r = <span class="hljs-built_in">Promise</span>.race(executing); 
      &#125;
    &#125;
 
    <span class="hljs-comment">// 正在执行任务列表 中较快的任务执行完成之后，才会从array数组中获取新的待办任务</span>
    <span class="hljs-keyword">return</span> r.then(<span class="hljs-function">() =></span> enqueue());
  &#125;;
  <span class="hljs-keyword">return</span> enqueue().then(<span class="hljs-function">() =></span> <span class="hljs-built_in">Promise</span>.all(ret));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 ES6 的实现版本中，通过内部封装的 <code>enqueue</code> 函数来实现核心的控制逻辑。当 <code>Promise.race(executing)</code> 返回的 <code>Promise</code> 对象变成已完成状态时，才会调用 <code>enqueue</code> 函数，从 <code>array</code> 数组中获取新的待办任务。</p>
<h3 data-id="heading-8">三、阿宝哥有话说</h3>
<p>在 <code>asyncPool</code> 这个库的 ES7 和 ES6 的具体实现中，我们都使用到了 <code>Promise.all</code> 和 <code>Promise.race</code> 函数。其中手写 <code>Promise.all</code> 是一道常见的面试题。刚好趁着这个机会，阿宝哥跟大家一起来手写简易版的 <code>Promise.all</code> 和 <code>Promise.race</code> 函数。</p>
<h4 data-id="heading-9">3.1 手写 Promise.all</h4>
<p><strong><code>Promise.all(iterable)</code></strong> 方法会返回一个 promise 对象，当输入的所有 promise 对象的状态都变成 <code>resolved</code> 时，返回的 promise 对象就会以数组的形式，返回每个 promise 对象 resolve 后的结果。当输入的任何一个 promise 对象状态变成 <code>rejected</code> 时，则返回的 promise 对象会 reject 对应的错误信息。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Promise</span>.all = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">iterators</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!iterators || iterators.length === <span class="hljs-number">0</span>) &#123;
      resolve([]);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>; <span class="hljs-comment">// 计数器，用于判断所有任务是否执行完成</span>
      <span class="hljs-keyword">let</span> result = []; <span class="hljs-comment">// 结果数组</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < iterators.length; i++) &#123;
        <span class="hljs-comment">// 考虑到iterators[i]可能是普通对象，则统一包装为Promise对象</span>
        <span class="hljs-built_in">Promise</span>.resolve(iterators[i]).then(
          <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
            result[i] = data; <span class="hljs-comment">// 按顺序保存对应的结果</span>
            <span class="hljs-comment">// 当所有任务都执行完成后，再统一返回结果</span>
            <span class="hljs-keyword">if</span> (++count === iterators.length) &#123;
              resolve(result);
            &#125;
          &#125;,
          <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
            reject(err); <span class="hljs-comment">// 任何一个Promise对象执行失败，则调用reject()方法</span>
            <span class="hljs-keyword">return</span>;
          &#125;
        );
      &#125;
    &#125;
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是对于 <code>Promise.all</code> 的标准实现来说，它的参数是一个可迭代对象，比如 Array、String 或 Set 等。</p>
<h4 data-id="heading-10">3.2 手写 Promise.race</h4>
<p><strong><code>Promise.race(iterable)</code></strong> 方法会返回一个 promise 对象，一旦迭代器中的某个 promise 对象 <strong>resolved</strong> 或 <strong>rejected</strong>，返回的 promise 对象就会 resolve 或 reject 相应的值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">iterators</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> iter <span class="hljs-keyword">of</span> iterators) &#123;
      <span class="hljs-built_in">Promise</span>.resolve(iter)
        .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          resolve(res);
        &#125;)
        .catch(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
          reject(e);
        &#125;);
    &#125;
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本文阿宝哥带大家详细分析了 <a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a> 异步任务并发控制的具体实现，同时为了让大家能够更好地理解 <a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a> 的核心代码。最后阿宝哥还带大家一起手写简易版的 <code>Promise.all</code> 和 <code>Promise.race</code> 函数。其实除了 <code>Promise.all</code> 函数之外，还存在另一个函数 —— <code>Promise.allSettled</code>，该函数用于解决 <code>Promise.all</code> 存在的问题，感兴趣的小伙伴可以自行研究一下。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。<strong>想一起学习 TS/Vue 3.0 的小伙伴可以添加阿宝哥微信 —— semlinker</strong>。</p>
</blockquote>
<h3 data-id="heading-11">四、参考资源</h3>
<ul>
<li><a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">Github - async-pool</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all" target="_blank" rel="nofollow noopener noreferrer">MDN - Promise.all</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/race" target="_blank" rel="nofollow noopener noreferrer">MDN - Promise.race</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled" target="_blank" rel="nofollow noopener noreferrer">MDN - Promise.allSettled</a></li>
</ul></div>  
</div>
            