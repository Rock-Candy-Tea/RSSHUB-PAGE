
---
title: 'Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7070'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 01:32:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=7070'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Promise</h1>
<h2 data-id="heading-1">Promise 是什么?</h2>
<p><code>Promise</code> 是异步编程的一种解决方案, 简单说就是一个容器，里面保存着一个尚未完成且预计在未来完成的异步操作</p>
<p>使用 <code>new Promise</code> 创建一个 <code>Promise</code> 对象, 用于表示一个异步操作的最终完成 (或失败)及其结果值, 有三种状态:
<code>pending</code>(进行中)
<code>fulfilled</code>(已完成)
<code>rejected</code>(已失败)</p>
<p><code>pending</code> 状态可以通过 <code>resolve</code>异步操作转为 <code>fulfilled</code> 状态, 或者通过 <code>reject</code> 异步操作转为 <code>rejected</code> 状态</p>
<p><code>fulfilled</code> 和 <code>rejected</code> 为最终态, 状态一旦改变就不会再变</p>
<h3 data-id="heading-2">优点</h3>
<ol>
<li>摆脱了回调地狱, 可以进行 <code>.then</code> 的链式调用, 让异步操作变得更加同步化, 流程更加清晰规范, 提高了代码的可维护性和可读性</li>
</ol>
<h3 data-id="heading-3">缺点</h3>
<ol>
<li>一旦执行无法取消</li>
<li>无法跟踪进度</li>
</ol>
<h2 data-id="heading-4">Promise/A+ 规范解读</h2>
<h3 data-id="heading-5">术语</h3>
<ol>
<li><code>promise</code> 是一个有 <code>then</code> 方法的对象或者是函数，行为遵循本规范</li>
<li><code>thenable</code> 是一个有 <code>then</code> 方法的对象或者是函数</li>
<li><code>value</code> 是 <code>promise</code> 状态成功时的值，也就是 <code>resolve</code> 的参数, 包括各种数据类型, 也包括 <code>undefined/thenable</code> 或者是 <code>promise</code></li>
<li><code>reason</code> 是 <code>promise</code> 状态失败时的值, 也就是 <code>reject</code> 的参数, 表示拒绝的原因</li>
<li><code>exception</code> 是一个使用 <code>throw</code> 抛出的异常值</li>
</ol>
<h3 data-id="heading-6">Promise Status</h3>
<p><code>promise</code> 应该有三种状态. 要注意他们之间的流转关系.</p>
<ol>
<li>
<p><code>pending</code></p>
<p>1.1 初始的状态, 可改变.
1.2 一个 <code>promise</code> 在 <code>resolve</code> 或者 <code>reject</code> 前都处于这个状态。
1.3 可以通过 <code>resolve</code> -> <code>fulfilled</code> 状态;
1.4 可以通过 <code>reject</code> -> <code>rejected</code> 状态;</p>
</li>
<li>
<p><code>fulfilled</code></p>
<p>2.1 最终态, 不可变.
2.2 一个 <code>promise</code> 被 <code>resolve</code> 后会变成这个状态.
2.3 必须拥有一个 <code>value</code> 值</p>
</li>
<li>
<p><code>rejected</code></p>
<p>3.1 最终态, 不可变.
3.2 一个 <code>promise</code> 被 <code>reject</code> 后会变成这个状态
3.3 必须拥有一个 <code>reason</code></p>
</li>
</ol>
<p>Tips: 总结一下, 就是 <code>promise</code> 的状态流转是这样的</p>
<p><code>pending</code> -> <code>resolve(value)</code> -> <code>fulfilled</code>
<code>pending</code> -> <code>reject(reason)</code> -> <code>rejected</code></p>
<h3 data-id="heading-7">then</h3>
<p>promise 应该提供一个 then 方法, 用来访问最终的结果, 无论是 value 还是 reason.</p>
<pre><code class="hljs language-js copyable" lang="js">promise.then(onFulfilled, onRejected);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p>参数要求</p>
<p>1.1 onFulfilled 必须是函数类型, 如果不是函数, 应该被忽略.
1.2 onRejected 必须是函数类型, 如果不是函数, 应该被忽略.</p>
</li>
<li>
<p>onFulfilled 特性</p>
<p>2.1 在 promise 变成 fulfilled 时，应该调用 onFulfilled, 参数是 value
2.2 在 promise 变成 fulfilled 之前, 不应该被调用.
2.3 只能被调用一次(所以在实现的时候需要一个变量来限制执行次数)</p>
</li>
<li>
<p>onRejected 特性</p>
<p>3.1 在 promise 变成 rejected 时，应该调用 onRejected, 参数是 reason
3.2 在 promise 变成 rejected 之前, 不应该被调用.
3.3 只能被调用一次(所以在实现的时候需要一个变量来限制执行次数)</p>
</li>
<li>
<p>onFulfilled 和 onRejected 应该是微任务</p>
<p>这里用 queueMicrotask 来实现微任务的调用.</p>
</li>
<li>
<p>then 方法可以被调用多次</p>
<p>5.1 promise 状态变成 fulfilled 后，所有的 onFulfilled 回调都需要按照 then 的顺序执行, 也就是按照注册顺序执行(所以在实现的时候需要一个数组来存放多个 onFulfilled 的回调)
5.2 promise 状态变成 rejected 后，所有的 onRejected 回调都需要按照 then 的顺序执行, 也就是按照注册顺序执行(所以在实现的时候需要一个数组来存放多个 onRejected 的回调)</p>
</li>
<li>
<p>返回值</p>
<p>then 应该返回一个 promise</p>
<pre><code class="hljs language-js copyable" lang="js">promise2 = promise1.then(onFulfilled, onRejected);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.1 onFulfilled 或 onRejected 执行的结果为 x, 调用 resolvePromise( 这里大家可能难以理解, 可以先保留疑问, 下面详细讲一下 resolvePromise 是什么东西 )
6.2 如果 onFulfilled 或者 onRejected 执行时抛出异常 e, promise2 需要被 reject
6.3 如果 onFulfilled 不是一个函数, promise2 以 promise1 的 value 触发 fulfilled
6.4 如果 onRejected 不是一个函数, promise2 以 promise1 的 reason 触发 rejected</p>
</li>
<li>
<p>resolvePromise</p>
<pre><code class="hljs language-js copyable" lang="js">resolvePromise(promise2, x, resolve, reject);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7.1 如果 promise2 和 x 相等，那么 reject TypeError
7.2 如果 x 是一个 promsie
如果 x 是 pending 态，那么 promise 必须要在 pending,直到 x 变成 fulfilled or rejected.
如果 x 被 fulfilled, fulfill promise with the same value.
如果 x 被 rejected, reject promise with the same reason.
7.3 如果 x 是一个 object 或者 是一个 function
let then = x.then.
如果 x.then 这步出错，那么 reject promise with e as the reason.
如果 then 是一个函数，then.call(x, resolvePromiseFn, rejectPromise)
resolvePromiseFn 的 入参是 y, 执行 resolvePromise(promise2, y, resolve, reject);
rejectPromise 的 入参是 r, reject promise with r.
如果 resolvePromise 和 rejectPromise 都调用了，那么第一个调用优先，后面的调用忽略。
如果调用 then 抛出异常 e
如果 resolvePromise 或 rejectPromise 已经被调用，那么忽略
则，reject promise with e as the reason
如果 then 不是一个 function. fulfill promise with x.</p>
</li>
</ol>
<h2 data-id="heading-8">实现一个 Promise</h2>
<h3 data-id="heading-9">一步步实现</h3>
<h4 data-id="heading-10">平常用 <code>promise</code> 的时候, 是通过 <code>new</code> 关键字来 <code>new Promise()</code>, 那就用 <code>class</code> 来实现一下吧.</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">YuPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">定义三种状态类型</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">"pending"</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">"fulfilled"</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">"rejected"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">设置初始状态</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">YuPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 初始状态为pending</span>
    <span class="hljs-built_in">this</span>.status = PENDING;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>;
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13"><code>resolve</code> 和 <code>reject</code> 方法</h4>
<ol>
<li>根据刚才的规范, 这两个方法是要更改 status 的, 从 pending 改到 fulfilled/rejected.</li>
<li>注意两个函数的入参分别是 value 和 reason.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">YuPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 初始状态为pending</span>
    <span class="hljs-built_in">this</span>.status = PENDING;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>;
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
      <span class="hljs-built_in">this</span>.value = value;
      <span class="hljs-built_in">this</span>.status = FULFILLED;
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
      <span class="hljs-built_in">this</span>.reason = reason;
      <span class="hljs-built_in">this</span>.status = REJECTED;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">加一下 promise 入参</h4>
<ol>
<li>入参是一个函数, 函数接收 resolve 和 reject 两个参数.</li>
<li>注意在初始化 promise 的时候, 就要执行这个函数, 并且有任何报错都要通过 reject 抛出去</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">YuPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-comment">// 初始状态为pending</span>
    <span class="hljs-built_in">this</span>.status = PENDING;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>;
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>;

    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 绑定this, 使用当前promise实例上的 resolve 和 reject</span>
      fn(<span class="hljs-built_in">this</span>.resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.reject.bind(<span class="hljs-built_in">this</span>));
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-built_in">this</span>.reject(e);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
      <span class="hljs-built_in">this</span>.value = value;
      <span class="hljs-built_in">this</span>.status = FULFILLED;
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
      <span class="hljs-built_in">this</span>.reason = reason;
      <span class="hljs-built_in">this</span>.status = REJECTED;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">接下来来实现一下关键的 then 方法</h4>
<ol>
<li>then 接收两个参数, onFulfilled 和 onRejected</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>检查并处理参数, 之前提到的如果不是 function, 就忽略. 这个忽略指的是原样返回 value 或者 reason.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">isFunction</span>(<span class="hljs-params">param</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> param === <span class="hljs-string">'function'</span>;
&#125;

<span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">const</span> realOnFulfilled = <span class="hljs-built_in">this</span>.isFunction(onFulfilled) ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> value
    &#125;
    <span class="hljs-keyword">const</span> realOnRejected = <span class="hljs-built_in">this</span>.isFunction(onRejected) ? onRejected : <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
        <span class="hljs-keyword">throw</span> reason;
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>.then 的返回值整体是一个 promise, 用 promise 来包裹一下.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">const</span> realOnFulfilled = <span class="hljs-built_in">this</span>.isFunction(onFulfilled) ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> value
    &#125;
    <span class="hljs-keyword">const</span> realOnRejected = <span class="hljs-built_in">this</span>.isFunction(onRejected) ? onRejected : <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
        <span class="hljs-keyword">throw</span> reason;
    &#125;;
    <span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;&#125;)
    <span class="hljs-keyword">return</span> promise2
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>根据当前 promise 的状态, 调用不同的函数</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">const</span> realOnFulfilled = <span class="hljs-built_in">this</span>.isFunction(onFulfilled) ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> value
    &#125;
    <span class="hljs-keyword">const</span> realOnRejected = <span class="hljs-built_in">this</span>.isFunction(onRejected) ? onRejected : <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
        <span class="hljs-keyword">throw</span> reason;
    &#125;;
    <span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
            <span class="hljs-comment">// 这样写是在 then 函数调用瞬间会执行的, 主要是有一些直接决议的场景, 比如resolve(1)</span>
            <span class="hljs-keyword">case</span> FULFILLED: &#123;
                realOnFulfilled()
                <span class="hljs-keyword">break</span>;
            &#125;
            <span class="hljs-keyword">case</span> REJECTED: &#123;
                realOnRejected()
                <span class="hljs-keyword">break</span>;
            &#125;
        &#125;
    &#125;)
    <span class="hljs-keyword">return</span> promise2

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>这样写, 是在 then 函数被调用的瞬间就会执行. 那这时候如果 status 还没变成 fulfilled 或者 rejected 怎么办, 很有可能还是 pending 的. 所以我们需要一个状态的监听机制, 当状态变成 fulfilled 或者 rejected 后, 再去执行 callback.</li>
</ol>
<ul>
<li>
<p>那么我们首先要拿到所有的 callback, 然后才能在某个时机去执行他. 新建两个数组, 来分别存储成功和失败的回调, 调用 then 的时候, 如果还是 pending 就存入数组.</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用数组, 主要是可以在一个 promise 实例上 .then 多次</span>
  <span class="hljs-built_in">this</span>.fulfilledCallbackList = [];
  <span class="hljs-built_in">this</span>.rejectedCallbackList = [];

<span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
<span class="hljs-keyword">const</span> realOnFulfilled = <span class="hljs-built_in">this</span>.isFunction(onFulfilled) ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> value
&#125;
<span class="hljs-keyword">const</span> realOnRejected = <span class="hljs-built_in">this</span>.isFunction(onRejected) ? onRejected : <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
    <span class="hljs-keyword">throw</span> reason;
&#125;;
<span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
        <span class="hljs-keyword">case</span> FULFILLED: &#123;
            realOnFulfilled()
            <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">case</span> REJECTED: &#123;
            realOnRejected()
            <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">case</span> PENDING: &#123;
            <span class="hljs-built_in">this</span>.fulfilledCallbackList.push(realOnFulfilled)
            <span class="hljs-built_in">this</span>.rejectedCallbackList.push(realOnRejected)
        &#125;
    &#125;
&#125;)
<span class="hljs-keyword">return</span> promise2

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-16">在 status 发生变化的时候, 就执行所有的回调. 这里用一下 es6 的 getter 和 setter. 这样更符合语义, 当 status 改变时, 去做什么事情. (当然也可以顺序执行, 在给 status 赋值后, 下面再加一行 forEach)</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 防止 getter 时套娃</span>
<span class="hljs-built_in">this</span>._status = PENDING;

<span class="hljs-keyword">get</span> <span class="hljs-title">status</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._status;
&#125;

<span class="hljs-keyword">set</span> <span class="hljs-title">status</span>(<span class="hljs-params">newStatus</span>) &#123;
    <span class="hljs-built_in">this</span>._status = newStatus;
    <span class="hljs-keyword">switch</span> (newStatus) &#123;
        <span class="hljs-keyword">case</span> FULFILLED: &#123;
            <span class="hljs-built_in">this</span>.fulfilledCallbackList.forEach(<span class="hljs-function"><span class="hljs-params">callback</span> =></span> &#123;
                callback(<span class="hljs-built_in">this</span>.value);
            &#125;);
            <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">case</span> REJECTED: &#123;
            <span class="hljs-built_in">this</span>.rejectedCallbackList.forEach(<span class="hljs-function"><span class="hljs-params">callback</span> =></span> &#123;
                callback(<span class="hljs-built_in">this</span>.reason);
            &#125;);
            <span class="hljs-keyword">break</span>;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">then 的返回值</h4>
<p>上面只是简单说了下, then 的返回值是一个 Promise, 那么接下来具体讲一下返回 promise 的 value 和 reason 是什么.</p>
<ol>
<li>如果 onFulfilled 或者 onRejected 抛出一个异常 e ，则 promise2 必须拒绝执行，并返回拒因 e。(这样的话, 我们就需要手动 catch 代码，遇到报错就 reject)</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">const</span> realOnFulfilled = <span class="hljs-built_in">this</span>.isFunction(onFulfilled) ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> value
    &#125;
    <span class="hljs-keyword">const</span> realOnRejected = <span class="hljs-built_in">this</span>.isFunction(onRejected) ? onRejected : <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
        <span class="hljs-keyword">throw</span> reason;
    &#125;;
    <span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
         <span class="hljs-keyword">const</span> fulfilledMicrotask = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
                realOnFulfilled(<span class="hljs-built_in">this</span>.value);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
                reject(e)
            &#125;
        &#125;;
        <span class="hljs-keyword">const</span> rejectedMicrotask = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
                realOnRejected(<span class="hljs-built_in">this</span>.reason);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
                reject(e);
            &#125;
        &#125;

        <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
            <span class="hljs-keyword">case</span> FULFILLED: &#123;
                fulfilledMicrotask()
                <span class="hljs-keyword">break</span>;
            &#125;
            <span class="hljs-keyword">case</span> REJECTED: &#123;
                rejectedMicrotask()
                <span class="hljs-keyword">break</span>;
            &#125;
            <span class="hljs-keyword">case</span> PENDING: &#123;
              <span class="hljs-built_in">this</span>.fulfilledCallbackList.push(realOnFulfilled)
              <span class="hljs-built_in">this</span>.rejectedCallbackList.push(realOnRejected)
            &#125;
        &#125;
    &#125;)
    <span class="hljs-keyword">return</span> promise2
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p>如果 onFulfilled 不是函数且 promise1 成功执行， promise2 必须成功执行并返回相同的值</p>
</li>
<li>
<p>如果 onRejected 不是函数且 promise1 拒绝执行， promise2 必须拒绝执行并返回相同的据因。</p>
</li>
</ol>
<p>需要注意的是，如果 promise1 的 onRejected 执行成功了，promise2 应该被 resolve</p>
<p>这里咱们其实已经在参数检查的时候做过了, 也就是这段代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> realOnFulfilled = <span class="hljs-built_in">this</span>.isFunction(onFulfilled)
  ? onFulfilled
  : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> value;
    &#125;;
<span class="hljs-keyword">const</span> realOnRejected = <span class="hljs-built_in">this</span>.isFunction(onRejected)
  ? onRejected
  : <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
      <span class="hljs-keyword">throw</span> reason;
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>如果 onFulfilled 或者 onRejected 返回一个值 x ，则运行 resolvePromise 方法</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">const</span> realOnFulfilled = <span class="hljs-built_in">this</span>.isFunction(onFulfilled) ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> value
    &#125;
    <span class="hljs-keyword">const</span> realOnRejected = <span class="hljs-built_in">this</span>.isFunction(onRejected) ? onRejected : <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
        <span class="hljs-keyword">throw</span> reason;
    &#125;;
    <span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> fulfilledMicrotask = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
                realOnFulfilled(<span class="hljs-built_in">this</span>.value);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
                reject(e)
            &#125;
        &#125;;
        <span class="hljs-keyword">const</span> rejectedMicrotask = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
                realOnRejected(<span class="hljs-built_in">this</span>.reason);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
                reject(e);
            &#125;
        &#125;

        <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
            <span class="hljs-keyword">case</span> FULFILLED: &#123;
                fulfilledMicrotask()
                <span class="hljs-keyword">break</span>;
            &#125;
            <span class="hljs-keyword">case</span> REJECTED: &#123;
                rejectedMicrotask()
                <span class="hljs-keyword">break</span>;
            &#125;
            <span class="hljs-keyword">case</span> PENDING: &#123;
               <span class="hljs-built_in">this</span>.fulfilledCallbackList.push(realOnFulfilled)
               <span class="hljs-built_in">this</span>.rejectedCallbackList.push(realOnRejected)
            &#125;
        &#125;
    &#125;)
    <span class="hljs-keyword">return</span> promise2
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">resolvePromise</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise2, x, resolve, reject</span>)</span> &#123;
    <span class="hljs-comment">// 如果 newPromise 和 x 指向同一对象，以 TypeError 为据因拒绝执行 newPromise</span>
    <span class="hljs-comment">// 这是为了防止死循环</span>
    <span class="hljs-keyword">if</span> (promise2 === x) &#123;
        <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The promise and the return value are the same'</span>));
    &#125;

    <span class="hljs-keyword">if</span> (x <span class="hljs-keyword">instanceof</span> YuPromise) &#123;
        <span class="hljs-comment">// 如果 x 为 Promise ，则使 newPromise 接受 x 的状态</span>
        <span class="hljs-comment">// 也就是继续执行x，如果执行的时候拿到一个y，还要继续解析y</span>
        queueMicrotask(<span class="hljs-function">() =></span> &#123;
            x.then(<span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
                <span class="hljs-built_in">this</span>.resolvePromise(promise2, y, resolve, reject);
            &#125;, reject);
        &#125;)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span> || <span class="hljs-built_in">this</span>.isFunction(x)) &#123;
        <span class="hljs-comment">// 如果 x 为对象或者函数</span>
        <span class="hljs-keyword">if</span> (x === <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-comment">// null也会被判断为对象</span>
            <span class="hljs-keyword">return</span> resolve(x);
        &#125;

        <span class="hljs-keyword">let</span> then = <span class="hljs-literal">null</span>;

        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 把 x.then 赋值给 then</span>
            then = x.then;
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            <span class="hljs-comment">// 如果取 x.then 的值时抛出错误 e ，则以 e 为据因拒绝 promise</span>
            <span class="hljs-keyword">return</span> reject(error);
        &#125;

        <span class="hljs-comment">// 如果 then 是函数</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isFunction(then)) &#123;
            <span class="hljs-keyword">let</span> called = <span class="hljs-literal">false</span>;
            <span class="hljs-comment">// 将 x 作为函数的作用域 this 调用</span>
            <span class="hljs-comment">// 传递两个回调函数作为参数，第一个参数叫做 resolvePromise ，第二个参数叫做 rejectPromise</span>
            <span class="hljs-keyword">try</span> &#123;
                then.call(
                    x,
                    <span class="hljs-comment">// 如果 resolvePromise 以值 y 为参数被调用，则运行 resolvePromise</span>
                    <span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
                        <span class="hljs-comment">// 需要有一个变量called来保证只调用一次.</span>
                        <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
                        called = <span class="hljs-literal">true</span>;
                        <span class="hljs-built_in">this</span>.resolvePromise(promise2, y, resolve, reject);
                    &#125;,
                    <span class="hljs-comment">// 如果 rejectPromise 以据因 r 为参数被调用，则以据因 r 拒绝 promise</span>
                    <span class="hljs-function">(<span class="hljs-params">r</span>) =></span> &#123;
                        <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
                        called = <span class="hljs-literal">true</span>;
                        reject(r);
                    &#125;);
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
                <span class="hljs-comment">// 如果调用 then 方法抛出了异常 e：</span>
                <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;

                <span class="hljs-comment">// 否则以 e 为据因拒绝 promise</span>
                reject(error);
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 如果 then 不是函数，以 x 为参数执行 promise</span>
            resolve(x);
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 如果 x 不为对象或者函数，以 x 为参数执行 promise</span>
        resolve(x);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">onFulfilled 和 onRejected 是微任务</h4>
<p>使用 queueMicrotask 包裹执行函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fulfilledMicrotask = <span class="hljs-function">() =></span> &#123;
  queueMicrotask(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> x = realOnFulfilled(<span class="hljs-built_in">this</span>.value);
      <span class="hljs-built_in">this</span>.resolvePromise(promise2, x, resolve, reject);
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      reject(e);
    &#125;
  &#125;);
&#125;;
<span class="hljs-keyword">const</span> rejectedMicrotask = <span class="hljs-function">() =></span> &#123;
  queueMicrotask(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> x = realOnRejected(<span class="hljs-built_in">this</span>.reason);
      <span class="hljs-built_in">this</span>.resolvePromise(promise2, x, resolve, reject);
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      reject(e);
    &#125;
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">简单写点代码测试一下</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">111</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;).then(<span class="hljs-built_in">console</span>.log);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"case1"</span>, test);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"case2"</span>, test);
&#125;, <span class="hljs-number">2000</span>);

<span class="hljs-comment">// 打印一下内容, 符合预期</span>
<span class="hljs-comment">// case1 YuPromise &#123;</span>
<span class="hljs-comment">//     _status: 'pending',</span>
<span class="hljs-comment">//     value: null,</span>
<span class="hljs-comment">//     reason: null,</span>
<span class="hljs-comment">//     fullfilledList: [],</span>
<span class="hljs-comment">//     rejectedList: [] &#125;</span>
<span class="hljs-comment">// case2 YuPromise &#123;</span>
<span class="hljs-comment">//     _status: 'fullfilled',</span>
<span class="hljs-comment">//     value: undefined,</span>
<span class="hljs-comment">//     reason: null,</span>
<span class="hljs-comment">//     fullfilledList: [],</span>
<span class="hljs-comment">//     rejectedList: [] &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">为什么可以调用.then, 不可以调用.catch 呢? 因为我们并没有在类里面声明 catch 方法, 添加 catch 方法</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">catch</span> (onRejected) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, onRejected);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">promise.resolve</h4>
<p>将现有对象转为 Promise 对象，如果 Promise.resolve 方法的参数，不是具有 then 方法的对象（又称 thenable 对象），则返回一个新的 Promise 对象，且它的状态为 fulfilled。
注意这是一个静态方法, 因为是通过 Promise.resolve 调用的, 而不是通过实例去调用的.</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> YuPromise) &#123;
        <span class="hljs-keyword">return</span> value;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        resolve(value);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">promise.reject</h4>
<p>返回一个新的 Promise 实例，该实例的状态为 rejected。Promise.reject 方法的参数 reason，会被传递给实例的回调函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        reject(reason);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">promise.race</h4>
<p><code>const p = Promise.race([p1, p2, p3]);</code></p>
<p>该方法是将多个 Promise 实例，包装成一个新的 Promise 实例。
只要 p1、p2、p3 之中有一个实例率先改变状态，p 的状态就跟着改变。那个率先改变的 Promise 实例的返回值，就传递给 p 的回调函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promiseList</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> length = promiseList.length;

        <span class="hljs-keyword">if</span> (length === <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">return</span> resolve();
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
                YuPromise.resolve(promiseList[i]).then(
                    <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
                        <span class="hljs-keyword">return</span> resolve(value);
                    &#125;,
                    <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
                        <span class="hljs-keyword">return</span> reject(reason);
                    &#125;);
            &#125;
        &#125;
    &#125;);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">写段测试代码</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">111</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;);

<span class="hljs-keyword">const</span> test2 = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">222</span>);
  &#125;, <span class="hljs-number">2000</span>);
&#125;);

<span class="hljs-keyword">const</span> test3 = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">333</span>);
  &#125;, <span class="hljs-number">3000</span>);
&#125;);

YuPromise.race([test, test2, test3]).then(<span class="hljs-built_in">console</span>.log); <span class="hljs-comment">// 打印了 111, 符合预期</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">完整代码</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">"pending"</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">"fulfilled"</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">"rejected"</span>;

<span class="hljs-comment">// queueMicrotask pollfill</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> queueMicrotask !== <span class="hljs-string">"function"</span>) &#123;
  queueMicrotask = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">callback</span>) </span>&#123;
    <span class="hljs-built_in">Promise</span>.resolve()
      .then(callback)
      .catch(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">throw</span> e;
        &#125;);
      &#125;);
  &#125;;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">YuPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.status = PENDING;
    <span class="hljs-built_in">this</span>._status = PENDING;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>;
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>;
    <span class="hljs-built_in">this</span>.fulfilledCallbackList = [];
    <span class="hljs-built_in">this</span>.rejectedCallbackList = [];
    <span class="hljs-keyword">try</span> &#123;
      fn(<span class="hljs-built_in">this</span>.resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.reject.bind(<span class="hljs-built_in">this</span>));
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-built_in">this</span>.reject(e);
    &#125;
  &#125;

  <span class="hljs-keyword">get</span> <span class="hljs-title">status</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._status;
  &#125;

  <span class="hljs-keyword">set</span> <span class="hljs-title">status</span>(<span class="hljs-params">newStatus</span>) &#123;
    <span class="hljs-built_in">this</span>._status = newStatus;
    <span class="hljs-keyword">switch</span> (newStatus) &#123;
      <span class="hljs-keyword">case</span> FULFILLED: &#123;
        <span class="hljs-built_in">this</span>.fulfilledCallbackList.forEach(<span class="hljs-function">(<span class="hljs-params">callback</span>) =></span> &#123;
          callback(<span class="hljs-built_in">this</span>.value);
        &#125;);
        <span class="hljs-keyword">break</span>;
      &#125;
      <span class="hljs-keyword">case</span> REJECTED: &#123;
        <span class="hljs-built_in">this</span>.rejectedCallbackList.forEach(<span class="hljs-function">(<span class="hljs-params">callback</span>) =></span> &#123;
          callback(<span class="hljs-built_in">this</span>.reason);
        &#125;);
        <span class="hljs-keyword">break</span>;
      &#125;
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">this</span>.value = value;
    <span class="hljs-built_in">this</span>.status = FULFILLED;
  &#125;

  <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">this</span>.reason = reason;
    <span class="hljs-built_in">this</span>.status = REJECTED;
  &#125;

  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">const</span> realOnFulfilled = <span class="hljs-built_in">this</span>.isFunction(onFulfilled)
      ? onFulfilled
      : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> value;
        &#125;;
    <span class="hljs-keyword">const</span> realOnRejected = <span class="hljs-built_in">this</span>.isFunction(onRejected)
      ? onRejected
      : <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
          <span class="hljs-keyword">throw</span> reason;
        &#125;;
    <span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> fulfilledMicrotask = <span class="hljs-function">() =></span> &#123;
        queueMicrotask(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">const</span> x = realOnFulfilled(<span class="hljs-built_in">this</span>.value);
            <span class="hljs-built_in">this</span>.resolvePromise(promise2, x, resolve, reject);
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e);
          &#125;
        &#125;);
      &#125;;
      <span class="hljs-keyword">const</span> rejectedMicrotask = <span class="hljs-function">() =></span> &#123;
        queueMicrotask(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">const</span> x = realOnRejected(<span class="hljs-built_in">this</span>.reason);
            <span class="hljs-built_in">this</span>.resolvePromise(promise2, x, resolve, reject);
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e);
          &#125;
        &#125;);
      &#125;;

      <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
        <span class="hljs-keyword">case</span> FULFILLED: &#123;
          fulfilledMicrotask();
          <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">case</span> REJECTED: &#123;
          rejectedMicrotask();
          <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">case</span> PENDING: &#123;
          <span class="hljs-built_in">this</span>.fulfilledCallbackList.push(fulfilledMicrotask);
          <span class="hljs-built_in">this</span>.rejectedCallbackList.push(rejectedMicrotask);
        &#125;
      &#125;
    &#125;);
    <span class="hljs-keyword">return</span> promise2;
  &#125;

  <span class="hljs-keyword">catch</span>(onRejected) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, onRejected);
  &#125;

  <span class="hljs-function"><span class="hljs-title">isFunction</span>(<span class="hljs-params">param</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> param === <span class="hljs-string">"function"</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise2, x, resolve, reject</span>)</span> &#123;
    <span class="hljs-comment">// 如果 newPromise 和 x 指向同一对象，以 TypeError 为据因拒绝执行 newPromise</span>
    <span class="hljs-comment">// 这是为了防止死循环</span>
    <span class="hljs-keyword">if</span> (promise2 === x) &#123;
      <span class="hljs-keyword">return</span> reject(
        <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"The promise and the return value are the same"</span>)
      );
    &#125;

    <span class="hljs-keyword">if</span> (x <span class="hljs-keyword">instanceof</span> YuPromise) &#123;
      <span class="hljs-comment">// 如果 x 为 Promise ，则使 newPromise 接受 x 的状态</span>
      <span class="hljs-comment">// 也就是继续执行x，如果执行的时候拿到一个y，还要继续解析y</span>
      queueMicrotask(<span class="hljs-function">() =></span> &#123;
        x.then(<span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
          <span class="hljs-built_in">this</span>.resolvePromise(promise2, y, resolve, reject);
        &#125;, reject);
      &#125;);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"object"</span> || <span class="hljs-built_in">this</span>.isFunction(x)) &#123;
      <span class="hljs-comment">// 如果 x 为对象或者函数</span>
      <span class="hljs-keyword">if</span> (x === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// null也会被判断为对象</span>
        <span class="hljs-keyword">return</span> resolve(x);
      &#125;

      <span class="hljs-keyword">let</span> then = <span class="hljs-literal">null</span>;

      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 把 x.then 赋值给 then</span>
        then = x.then;
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-comment">// 如果取 x.then 的值时抛出错误 e ，则以 e 为据因拒绝 promise</span>
        <span class="hljs-keyword">return</span> reject(error);
      &#125;

      <span class="hljs-comment">// 如果 then 是函数</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isFunction(then)) &#123;
        <span class="hljs-keyword">let</span> called = <span class="hljs-literal">false</span>;
        <span class="hljs-comment">// 将 x 作为函数的作用域 this 调用</span>
        <span class="hljs-comment">// 传递两个回调函数作为参数，第一个参数叫做 resolvePromise ，第二个参数叫做 rejectPromise</span>
        <span class="hljs-keyword">try</span> &#123;
          then.call(
            x,
            <span class="hljs-comment">// 如果 resolvePromise 以值 y 为参数被调用，则运行 resolvePromise</span>
            <span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
              <span class="hljs-comment">// 需要有一个变量called来保证只调用一次.</span>
              <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
              called = <span class="hljs-literal">true</span>;
              <span class="hljs-built_in">this</span>.resolvePromise(promise2, y, resolve, reject);
            &#125;,
            <span class="hljs-comment">// 如果 rejectPromise 以据因 r 为参数被调用，则以据因 r 拒绝 promise</span>
            <span class="hljs-function">(<span class="hljs-params">r</span>) =></span> &#123;
              <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
              called = <span class="hljs-literal">true</span>;
              reject(r);
            &#125;
          );
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-comment">// 如果调用 then 方法抛出了异常 e：</span>
          <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;

          <span class="hljs-comment">// 否则以 e 为据因拒绝 promise</span>
          reject(error);
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 如果 then 不是函数，以 x 为参数执行 promise</span>
        resolve(x);
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 如果 x 不为对象或者函数，以 x 为参数执行 promise</span>
      resolve(x);
    &#125;
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> YuPromise) &#123;
      <span class="hljs-keyword">return</span> value;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
      resolve(value);
    &#125;);
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      reject(reason);
    &#125;);
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promiseList</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> length = promiseList.length;

      <span class="hljs-keyword">if</span> (length === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">return</span> resolve();
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
          YuPromise.resolve(promiseList[i]).then(
            <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
              <span class="hljs-keyword">return</span> resolve(value);
            &#125;,
            <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
              <span class="hljs-keyword">return</span> reject(reason);
            &#125;
          );
        &#125;
      &#125;
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">实现 Promise 周边</h2>
<h3 data-id="heading-28">封装一个简单的 xhr 请求</h3>
<ol>
<li>使用 cb 形式</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span>(<span class="hljs-params">url, success, fail</span>) </span>&#123;
    <span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> XMLHttpRequest();
    client.open(<span class="hljs-string">'GET'</span>, url);
    client.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.readystate !== <span class="hljs-number">4</span>) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === <span class="hljs-number">200</span>) &#123;
            success(<span class="hljs-built_in">this</span>.response);
        &#125;<span class="hljs-keyword">else</span> &#123;
            fail(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-built_in">this</span>.statusText));
        &#125;
    &#125;
    client.send();
&#125;

<span class="hljs-comment">// 如果请求2依赖请求1的结果, 那就在请求1的回调中再实现请求2, 一层层下去, 形成回调地狱</span>
ajax(<span class="hljs-string">'/test.json'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'success'</span>, res);
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">statusText</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error'</span>, statusText);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用 promise 进行封装(ps: 通常用 promise 封装呢会使用 Async 的词根, 跟 Node.js 学的)</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajaxAsync</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> XMLHttpRequest();
    client.open(<span class="hljs-string">"GET"</span>, url);
    client.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.readystate !== <span class="hljs-number">4</span>) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-number">200</span>) &#123;
        resolve(<span class="hljs-built_in">this</span>.response);
      &#125; <span class="hljs-keyword">else</span> &#123;
        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-built_in">this</span>.statusText));
      &#125;
    &#125;;
    client.send();
  &#125;);
&#125;

ajaxAsync(<span class="hljs-string">"/test.json"</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"success"</span>, res);
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"error"</span>, err);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更改为 promise 的步骤呢, 就是内部构造 promise 实例, 在原来执行回调函数的地方执行对应的更改 promise 状态的函数即可</p>
<h3 data-id="heading-29">实现一个 Promise.chain, 一条一条执行</h3>
<p>实现思路:</p>
<ol>
<li>for of 配合 async await</li>
<li>数组的 reduce 方法(进行转换, 转换成 promise1.then(() => &#123;return promise2&#125;) 的形式)</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 题目</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promiseCreator1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">1000</span>);
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promiseCreator2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">1000</span>);
  &#125;);
&#125;

<span class="hljs-keyword">const</span> promiseCreatorList = [promiseCreator1, promiseCreator2];
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">for of 配合 async await</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forOfLoop</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> promiseInstance <span class="hljs-keyword">of</span> promiseCreatorList) &#123;
      <span class="hljs-keyword">await</span> promiseInstance();
    &#125;
  &#125;
  <span class="hljs-keyword">await</span> forOfLoop();
&#125;
main();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">数组的 reduce 方法</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// reduce 可以接收第二个参数, 其实我们可以给它一个空的 Promise 实例, 那这样在迭代过程中就可以保证都是 Promise 实例</span>
<span class="hljs-keyword">const</span> promiseChain = promiseCreatorList.reduce(<span class="hljs-function">(<span class="hljs-params">prev, cur</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> prev.then(cur);
&#125;, <span class="hljs-built_in">Promise</span>.resolve());

<span class="hljs-comment">// 最后一次返回的值肯定也是一个 Promise 实例</span>
promiseChain.then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"end"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">Promise.allSeltted</h3>
<p>该 Promise.allSettled()方法返回一个在所有给定的 promise 都已经 fulfilled 或 rejected 后的 promise，并带有一个对象数组，每个对象表示对应的 promise 结果。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">PromiseAllSeltted</span>(<span class="hljs-params">promiseArray</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promiseArray)) &#123;
      <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"arguments muse be an array"</span>));
    &#125;
    <span class="hljs-keyword">let</span> counter = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> promiseNum = promiseArray.length;
    <span class="hljs-keyword">let</span> resolvedArray = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < promiseNum; i++) &#123;
      <span class="hljs-built_in">Promise</span>.resolve(promiseArray[i])
        .then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
          resolvedArray[i] = &#123;
            value,
            <span class="hljs-attr">status</span>: <span class="hljs-string">"fulfilled"</span>,
          &#125;;
        &#125;)
        .catch(<span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
          resolvedArray[i] = &#123;
            reason,
            <span class="hljs-attr">status</span>: <span class="hljs-string">"rejected"</span>,
          &#125;;
        &#125;)
        .finally(<span class="hljs-function">() =></span> &#123;
          counter++;
          <span class="hljs-keyword">if</span> (counter == promiseNum) &#123;
            resolve(resolvedArray);
          &#125;
        &#125;);
    &#125;
  &#125;);
&#125;

<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">const</span> pro1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">res, rej</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    res(<span class="hljs-string">"1"</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;);
<span class="hljs-keyword">const</span> pro2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">res, rej</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    rej(<span class="hljs-string">"2"</span>);
  &#125;, <span class="hljs-number">2000</span>);
&#125;);
<span class="hljs-keyword">const</span> pro3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">res, rej</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    res(<span class="hljs-string">"3"</span>);
  &#125;, <span class="hljs-number">3000</span>);
&#125;);

<span class="hljs-keyword">const</span> proAll = PromiseAllSeltted([pro1, pro2, pro3])
  .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> <span class="hljs-built_in">console</span>.log(res))
  .catch(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(e);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">手写一个 Promise.all</h3>
<p>它接收一个数组, 数组里面是 Promise 或者是常量, 返回一个 Promise, 它会使用 Promise.resolve 对数组元素包裹一层, 把非 Promise 元素也转变为 Promise, 当数组中所有的 Promise 执行完了, 就会 resolve 掉, 当有一个 Promise 报错了, 就会 reject 掉</p>
<p>当一个 Promise 报错后, 其他 Promise 会执行吗？
会的, Promise 在实例化的时候就执行完了, .then 只是为了拿到结果</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">PromiseAll</span>(<span class="hljs-params">promiseArray</span>) </span>&#123;
  <span class="hljs-comment">// 首先肯定是返回一个 promise</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// 判断一下是否是数组</span>
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promiseArray)) &#123;
      <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"传入的参数需要是一个数组"</span>));
    &#125;
    <span class="hljs-keyword">let</span> resArr = [];
    <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>; <span class="hljs-comment">// 记录执行返回的结果数量, 因为 resArr[i], 可能会出现 undefined, 可以举例子说明, 比如数组一开始为空, 如果 resArr[10] = 1, 这个时候的 resArr.length = 11, js 会把空间留出来</span>
    <span class="hljs-keyword">const</span> promiseLen = promiseArray.length;
    <span class="hljs-comment">// ps: 自己百度的, 如果是数组这种采用下标访问的, 使用 for, 效率已经够高了, 如果是链表结构的, 可以使用 forEach</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < promiseLen; i++) &#123;
      <span class="hljs-comment">// Promise.resolve 包裹一层可以把一些常量也转为 promise</span>
      <span class="hljs-built_in">Promise</span>.resolve(promiseArray[i])
        .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          <span class="hljs-comment">// 这种方式不对, 忽略了 Promise.all 的特性, Promise.all 接收的数组元素是什么顺序, 返回的结果也是什么顺序, 但是使用 push 有可能某一个 promise 执行得更快, 走在了前面 push</span>
          <span class="hljs-comment">// resArr.push(res);</span>
          resArr[i] = res;
          count++;
          <span class="hljs-comment">// 千万记住不能放在 .then 外面, 因为放外面是同步执行的</span>
          <span class="hljs-keyword">if</span> (count === promiseLen) &#123;
            resolve(resArr);
          &#125;
        &#125;)
        .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> reject(err));
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">实现一个 cachePromise</h3>
<p>所有的 Promise 在实例化的时候就已经执行了</p>
<p>这道题目的意义是, 比如要去调用一个接口, 这个请求调用的是一个常量, 可能很多页面都使用到了, 那如果没有全局的状态管理, 那每个页面都调用一遍, 执行一遍, 也会比较浪费服务器的性能</p>
<p>那这里使用装饰器来实现一遍</p>
<h4 data-id="heading-35">装饰器科普</h4>
<p>target 是所属类的原型
name 是修饰的属性名称
descriptor 是修饰的属性描述符号, 如 writable 这些配置等等, value 是属性值, 参考 Object.defineProperty</p>
<p>ES6 中定义一个类的写法，其实只是一个语法糖，而实际上当我们给一个类添加一个属性的时候，会调用到 Object.defineProperty 这个方法，它会接受三个参数：target 、name 和 descriptor</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 属性描述符</span>
<span class="hljs-keyword">let</span> descriptor = &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"meow ~"</span>);
  &#125;,
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
&#125;;

<span class="hljs-comment">// 经过 readonly 装饰器修饰后的属性描述符</span>
descriptor = readonly(Cat.prototype, <span class="hljs-string">"say"</span>, descriptor) || descriptor;

<span class="hljs-comment">// ES6中 给类添加属性</span>
<span class="hljs-built_in">Object</span>.defineProperty(Cat.prototype, <span class="hljs-string">"say"</span>, descriptor);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当装饰器作用于类本身的时候，我们操作的对象也是这个类本身，而当装饰器作用于类的某个具体的属性的时候，我们操作的对象既不是类本身，也不是类的属性，而是它的描述符（descriptor），而描述符里记录着我们对这个属性的全部信息，所以，我们可以对它自由的进行扩展和封装，最后达到的目的呢，就和之前说过的装饰器的作用是一样的。</p>
<p>当然，如果你喜欢的话，也可以直接在 target 上进行扩展和封装</p>
<h4 data-id="heading-36">cachePromise 实现</h4>
<p>刷新肯定就没了, 那没什么办法, 装饰器是 es7 的, 如果不支持可能要安装一个 babel 插件</p>
<p>有缓存, 就要考虑时效, 没有任何一个缓存是永久有效的, 在这里在去标识一下过期时间啊</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> cacheMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">enableCache</span>(<span class="hljs-params">target, name, descriptor</span>) </span>&#123;
  <span class="hljs-keyword">const</span> val = descriptor.value;
  descriptor.value = <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-keyword">const</span> cacheKey = <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span><span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(args)&#125;</span>`</span>;
    <span class="hljs-keyword">if</span> (!cacheMap.get(cacheKey)) &#123;
      <span class="hljs-keyword">const</span> cacheValue = <span class="hljs-built_in">Promise</span>.resolve(val.apply(<span class="hljs-built_in">this</span>, args)).catch(<span class="hljs-function">(<span class="hljs-params">_</span>) =></span> &#123;
        cacheMap.set(cacheKey, <span class="hljs-literal">null</span>);
      &#125;);
      cacheMap.set(cacheKey, cacheValue);
    &#125;
    <span class="hljs-keyword">return</span> cacheMap.get(cacheKey);
  &#125;;
  <span class="hljs-keyword">return</span> descriptor;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseClass</span> </span>&#123;
  @enableCache()
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getInfo</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

PromiseClass.getInfo.then(...).catch(...);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">Promise.race 的使用: 如果你的页面上有巨量的图片要展示, 那除了懒加载的形式, 还有什么形式可以来限制下同时加载的数量?(代码题, 写代码来实现并发的控制)</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">limitLoad</span>(<span class="hljs-params">urls, handler, limit</span>) </span>&#123;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadImg</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve();
    &#125;, url.time);
  &#125;);
&#125;

<span class="hljs-keyword">const</span> urls = [&#123; <span class="hljs-attr">info</span>: <span class="hljs-string">"info"</span>, <span class="hljs-attr">time</span>: <span class="hljs-number">200</span> &#125;...];

limitLoad(urls, loadImg, <span class="hljs-number">3</span>);

<span class="hljs-comment">// 1, 2, 3, 4, 5, 6, 7</span>
<span class="hljs-comment">// 先请求 1, 2, 3, 如果其中有一个加载完了, 就从剩下的选一个接着请求</span>
<span class="hljs-comment">// 保证一个时间就是 3 个同时在请求</span>
<span class="hljs-comment">// 利用 Promise.race, 竞态, 只要有一个完成了, 会直接 resolve</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">limitLoad</span>(<span class="hljs-params">urls, handler, limit</span>) </span>&#123;
    <span class="hljs-comment">// 不能对外部产生影响, 要进行拷贝</span>
    <span class="hljs-keyword">const</span> sequeue = [].cancat(urls);

    <span class="hljs-comment">// 截取三个, 注意这里用的 splice(), 会改变原数组, 所以下面遍历的时候其实这里使用的三个是不存在的了</span>
    <span class="hljs-keyword">const</span> promises = sequeue.splice(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>).map(<span class="hljs-function">(<span class="hljs-params">url, index</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> handler(url).then(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 记录当前的 index, 用于下面填补</span>
            <span class="hljs-keyword">return</span> index;
        &#125;);
    &#125;)

    <span class="hljs-comment">// 每次第一个完成了就会 resolve 掉</span>
    <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.race(promises);

    <span class="hljs-comment">// 这是一个同步 for 循环, 开启 .then().then()</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len= sequeue.length; i < len; i ++) &#123;
        p = p.then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
            promises[res] = handler(sequeue[i]).then(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">return</span> res;
            &#125;)
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.race(promises);
        &#125;)
    &#125;
&#125;

<span class="hljs-comment">// 思路:</span>
<span class="hljs-comment">// 首先截取三个去发送请求, 这三个请求就发出去了, 然后当有一个请求完成时, 就 resolve 了</span>
<span class="hljs-comment">// 然后在当前 resolve 的位置重新发出一个请求, 再开启一个竞态</span>
<span class="hljs-comment">// 这个遍历的话其实是链式调用, 会 .then().then().then(), 都是根据最先请求完成的位置开启的, 完成开启下一个</span>
<span class="hljs-comment">// 使用 Promise.race() 来实现并行, Promise 会在初始化的时候就执行了, 只不过是整个 Promise 会返回一个结果, Promise 数组里面的 Promise 还是会进行执行的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-38">看题说话</h2>
<h3 data-id="heading-39">为什么 promise resolve 了一个 value, 最后输出的 value 值却是 undefined</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">111</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;).then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"then"</span>);
&#125;);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(test);
&#125;, <span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为现在这种写法, 相当于在.then 里 return undefined, 所以最后的 value 是 undefined.
如果显式 return 一个值, 就不是 undefined 了；比如 return value.</p>
<h3 data-id="heading-40">.then 返回的是一个新 Promise, 那么原来 promise 实现的时候, 用数组来存回调函数有什么意义？</h3>
<p>这个问题提出的时候, 应该是有一个假定条件, 就是链式调用的时候.</p>
<p>这个时候, 每一个.then 返回的都是一个新 promise, 所以每次回调数组 fulfilledCallbackList 都是空数组.</p>
<p>针对这种情况, 确实用数组来存储回调没意义, 完全可以就用一个变量来存储。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">111</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;)
  .then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;&#125;)
  .then(<span class="hljs-function">() =></span> &#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是还有一种 promise 使用的方式, 这种情况下, promise 实例是同一个, 数组的存在就有了意义</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">111</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;);

test.then(<span class="hljs-function">() =></span> &#123;&#125;);
test.then(<span class="hljs-function">() =></span> &#123;&#125;);
test.then(<span class="hljs-function">() =></span> &#123;&#125;);
test.then(<span class="hljs-function">() =></span> &#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">为什么我在 catch 的回调里, 打印 promise, 显示状态是 pending</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    reject(<span class="hljs-number">111</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;).catch(<span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"报错"</span> + reason);
  <span class="hljs-built_in">console</span>.log(test);
&#125;);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(test);
&#125;, <span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>catch 函数会返回一个新的 promise, 而 test 就是这个新 promise</li>
<li>catch 的回调里, 打印 promise 的时候, 整个回调还并没有执行完成(所以此时的状态是 pending), 只有当整个回调完成了, 才会更改状态</li>
<li>catch 的回调函数, 如果成功执行完成了, 会改变这个新 Promise 的状态为 fulfilled</li>
</ol>
<h3 data-id="heading-42">这段代码会打印什么?(注意 node 版本不同会有所区别)</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> YuPromise(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve();
  &#125;, <span class="hljs-number">1000</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"case1"</span>, promise);
&#125;);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"case2"</span>, promise);
&#125;, <span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Promise 实例化的时候是同步的, Promise 里的 setTimeout 先加入任务队列, 称为 s1 吧
再是全局的 setTimeout 加入任务队列, 称为 s2 吧
然后 s1 执行, resolve 是微任务, 加入微任务队列, 会在当前宏任务把控制权交还给浏览器前先清空微任务队列, 然后 case1 先打印, 状态为 pending
再执行 s2, 由于 then 中 相当于是返回了 undefined, s2 这里状态是 fullfilled</p>
<ol>
<li>在浏览器中会是 case 1 -> case2, 没毛病</li>
<li>如果是在 node 环境运行, node 版本不同会有所差别, 如以下命令, node 版本为 10.16.3, case2 先执行了, node 版本为 14.17.1 时, 事件循环机制跟浏览器保持了一致, case1 先执行</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// xxx@MacBook-Pro Promise % node -v</span>
<span class="hljs-comment">// v10.16.3</span>
<span class="hljs-comment">// xxx@MacBook-Pro Promise % node Promise.js</span>
<span class="hljs-comment">// case2</span>
<span class="hljs-comment">// case1</span>
<span class="hljs-comment">// xxx@MacBook-Pro Promise % nvm use 14.17.1</span>
<span class="hljs-comment">// Now using node v14.17.1 (npm v6.14.13)</span>
<span class="hljs-comment">// xxx@MacBook-Pro Promise % node -v</span>
<span class="hljs-comment">// v14.17.1</span>
<span class="hljs-comment">// xxx@MacBook-Pro Promise % node Promise.js</span>
<span class="hljs-comment">// case1</span>
<span class="hljs-comment">// case2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-43">其他问题</h2>
<ol>
<li>图片的懒加载是不是用的 Promise?</li>
</ol>
<p>图片的懒加载通常是使用浏览器原生的 observer 来监听元素是否进入可视区, 替换元素的 src 来达到懒加载的目的</p>
<ol start="2">
<li>getter 中没有什么逻辑, 为什么要写 getter 呢？</li>
</ol>
<p>因为 getter 和 setter 是成对出现的</p>
<ol start="3">
<li>为什么要用一个私有变量呢?</li>
</ol>
<p>因为如果 getter 中访问的是 this.status, 那就死循环, 套娃了, 使用一个私有变量<code>_status</code> 是为了防止套娃</p>
<ol start="4">
<li>为什么使用 queueMicrotask 包裹而不是 setTimeout ?</li>
</ol>
<p>因为 setTimeout 是一个经典的宏任务</p>
<ol start="5">
<li>为什么 Promise.race 遍历, 传入 resolve, 不会多次执行?</li>
</ol>
<p>因为当 resolve 或者 reject 异步操作执行了就会被锁.</p>
<ol start="6">
<li>为什么用数组来存？</li>
</ol>
<p>因为数组可以存多个函数, 而且也满足顺序的条件</p>
<ol start="7">
<li>then 每次 return 的都是一个新的 Promise, 新的 Promise 每次都会初始化数组为空的, 那你用数组存的意义在哪里? 为什么不用一个变量来存?</li>
</ol>
<p>因为当前 promise 实例可以被多次调用, 不一定是链式调用</p>
<p>因为可以</p>
<pre><code class="hljs language-js copyable" lang="js">promise.then(<span class="hljs-function">() =></span> &#123;&#125;);
promise.then(<span class="hljs-function">() =></span> &#123;&#125;);
promise.then(<span class="hljs-function">() =></span> &#123;&#125;);
promise.then(<span class="hljs-function">() =></span> &#123;&#125;);
promise.then(<span class="hljs-function">() =></span> &#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>resolvePromise 是为了什么？</li>
</ol>
<p>为了解析 x 的值</p>
<ol start="9">
<li>race 方法 list 中第一个 promise 被决议之后状态就变更了 list 剩下的 promise 也会执行 他们的结果就不了了之了么?</li>
</ol>
<p>是的, 竞态, 谁跑的快就 resolve 谁, 或者 reject 谁, 其他的就陪跑</p>
<h2 data-id="heading-44">注意事项</h2>
<ol>
<li>
<p>try catch 只能捕获到同步抛出的错误, 不能捕获到异步任务抛出的错误, promise 的错误也不能捕获到, 除非使用了 async await</p>
</li>
<li>
<p>多个.then 链式调用, 最后用一个 .catch 捕获到的错误, 怎么区分是哪个 .then 抛出的错误, 所以其实也抛出一个问题, 如下写法其实是不严谨的, 像这个 catch 其实会捕获到两个 promise 抛出的错误, 所以如果需要区分的话, 可以在每一个 Promise 都 catch 一下.</p>
</li>
<li>
<p>每一个 Promise 的状态只取决于上次的 Promise 返回的状态, 如果上一个 Promise return 了一个值, 不是异常, 那 reject 就会终止掉</p>
</li>
</ol>
<h2 data-id="heading-45">参考文献 & 待看文章</h2>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise" target="_blank" rel="nofollow noopener noreferrer">Promise - MDN</a>
<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Using_promises" target="_blank" rel="nofollow noopener noreferrer">Using_promises - MDN</a>
<a href="https://promisesaplus.com/" target="_blank" rel="nofollow noopener noreferrer">Promises/A+规范</a>
<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled" target="_blank" rel="nofollow noopener noreferrer">Promise.allSettled() - MDN</a>
<a href="https://jelly.jd.com/article/6030875363dc65014d6fb76f" target="_blank" rel="nofollow noopener noreferrer">装饰器 - JELLY</a>
<a href="https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask" target="_blank" rel="nofollow noopener noreferrer">queueMicrotask - MDN</a>
<a href="https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide/In_depth" target="_blank" rel="nofollow noopener noreferrer">执行上下文 - MDN</a>
<a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Timeouts_and_intervals" target="_blank" rel="nofollow noopener noreferrer">协作异步 JavaScript - MDN</a>
<a href="https://juejin.cn/post/6945319439772434469" target="_blank">Promise 面试题 - 倔金</a>
<a href="https://juejin.cn/post/6844903512845860872" target="_blank">JavaScript 执行机制 - 倔金 </a>
<a href="https://nodejs.org/zh-cn/docs/guides/event-loop-timers-and-nexttick/" target="_blank" rel="nofollow noopener noreferrer">Node 事件循环机制 - Node</a></p></div>  
</div>
            