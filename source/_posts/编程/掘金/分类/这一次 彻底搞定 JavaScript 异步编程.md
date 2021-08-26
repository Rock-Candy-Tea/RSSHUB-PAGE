
---
title: '这一次 彻底搞定 JavaScript 异步编程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7130'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 19:58:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=7130'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">💬 前言</h2>
<blockquote>
<p>异步编程的语法目标，就是怎样让它更像同步编程。——阮一峰《深入掌握 ECMAScript 6 异步编程》</p>
</blockquote>
<p>JavaScript 的异步编程发展经过了四个阶段：</p>
<ol>
<li>回调函数、发布订阅</li>
<li>Promise</li>
<li>co 自执行的 Generator 函数</li>
<li>async / await</li>
</ol>
<h2 data-id="heading-1">🤗Promise</h2>
<p>首先让我们来回忆一下 Promise 的使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">1</span>)
  &#125;, <span class="hljs-number">500</span>)
&#125;)
  .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res)
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(<span class="hljs-number">2</span>)
      &#125;, <span class="hljs-number">500</span>)
    &#125;)
  &#125;)
  .then(<span class="hljs-built_in">console</span>.log)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">😏 核心代码</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.cbs = []
  <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.data = value
      <span class="hljs-built_in">this</span>.cbs.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(value))
    &#125;)
  &#125;
  fn(resolve)
&#125;
<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onResolved</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">this</span>.cbs.push(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> res = onResolved(<span class="hljs-built_in">this</span>.data)
      <span class="hljs-keyword">if</span> (res <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
        res.then(resolve)
      &#125; <span class="hljs-keyword">else</span> &#123;
        resolve(res)
      &#125;
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>then</code>实现</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onResolved</span>) </span>&#123;
  <span class="hljs-comment">// 这里叫做 promise2</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">this</span>.cbs.push(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> res = onResolved(<span class="hljs-built_in">this</span>.data)
      <span class="hljs-keyword">if</span> (res <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
        <span class="hljs-comment">// resolve 的权力被交给了 user promise</span>
        res.then(resolve)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 如果是普通值 就直接 resolve</span>
        <span class="hljs-comment">// 依次执行 cbs 里的函数 并且把值传递给 cbs</span>
        resolve(res)
      &#125;
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合实例来说</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fn = <span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">1</span>)
  &#125;, <span class="hljs-number">500</span>)
&#125;

<span class="hljs-keyword">const</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(fn)

promise1.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res)
  <span class="hljs-comment">// user promise</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-number">2</span>)
    &#125;, <span class="hljs-number">500</span>)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里的命名：</p>
<ol>
<li>
<p>我们把 <code>new Promise</code> 返回的实例叫做 <code>promise1</code></p>
</li>
<li>
<p>在 <code>Promise.prototype.then</code> 的实现中，我们构造了一个新的 promise 返回，叫它 <code>promise2</code></p>
</li>
<li>
<p>在用户调用 <code>then</code> 方法的时候，用户手动构造了一个 promise 并且返回，用来做异步的操作，叫它 <code>user promise</code></p>
</li>
</ol>
<p>那么在 <code>then</code> 的实现中，内部的 this 其实就指向 <code>promise1</code>
而 <code>promise2</code> 的传入的 <code>fn</code> 函数执行了一个 <code>this.cbs.push()</code>，其实是往 <code>**promise1**</code> 的 <code>cbs</code> 数组中 push 了一个函数，等待后续执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onResolved</span>) </span>&#123;
  <span class="hljs-comment">// 这里叫做 promise2</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-comment">// 这里的 this 其实是 promise1</span>
    <span class="hljs-built_in">this</span>.cbs.push(<span class="hljs-function">() =></span> &#123;&#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么重点看这个 push 的函数，注意，这个函数在 <code>promise1</code> 被 <code>resolve</code> 了以后才会执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// promise2</span>
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
  <span class="hljs-built_in">this</span>.cbs.push(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// onResolved 就对应 then 传入的函数</span>
    <span class="hljs-keyword">const</span> res = onResolved(<span class="hljs-built_in">this</span>.data)
    <span class="hljs-comment">// 例子中的情况 用户自己返回了一个 user promise</span>
    <span class="hljs-keyword">if</span> (res <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
      <span class="hljs-comment">// user promise 的情况</span>
      <span class="hljs-comment">// 用户会自己决定何时 resolve promise2</span>
      <span class="hljs-comment">// 只有 promise2 被 resolve 以后</span>
      <span class="hljs-comment">// then 下面的链式调用函数才会继续执行</span>
      res.then(resolve)
    &#125; <span class="hljs-keyword">else</span> &#123;
      resolve(res)
    &#125;
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果用户传入给 then 的 onResolved 方法返回的是个<code> user promise</code>，那么这个<code>user promise</code>里用户会自己去在合适的时机 <code>resolve promise2</code>，那么进而这里的 <code>res.then(resolve)</code> 中的 resolve 就会被执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (res <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
  res.then(resolve)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合下面这个例子来看：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// resolve1</span>
    resolve(<span class="hljs-number">1</span>)
  &#125;, <span class="hljs-number">500</span>)
&#125;)
  <span class="hljs-comment">// then1</span>
  .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res)
    <span class="hljs-comment">// user promise</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// resolve2</span>
        resolve(<span class="hljs-number">2</span>)
      &#125;, <span class="hljs-number">500</span>)
    &#125;)
  &#125;)
  <span class="hljs-comment">// then2</span>
  .then(<span class="hljs-built_in">console</span>.log)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>then1</code>这一整块其实返回的是 <code>promise2</code>，那么 <code>then2</code> 其实本质上是 <code>promise2.then(console.log)</code>，
也就是说 <code>then2</code>注册的回调函数，其实进入了<code>promise2</code>的 <code>cbs</code> 回调数组里，又因为我们刚刚知道，resolve2 调用了之后，<code>user promise</code> 会被 resolve，进而触发 <code>promise2</code> 被 resolve，进而 <code>promise2</code> 里的 <code>cbs</code> 数组被依次触发。
这样就实现了用户自己写的 <code>resolve2</code> 执行完毕后，<code>then2</code> 里的逻辑才会继续执行，也就是<strong>异步链式调用</strong></p>
<h3 data-id="heading-3">😲 完整实现</h3>
<p>上面介绍了一下 Promise 的核心部分，下面我们根据 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpromisesaplus.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://promisesaplus.com/" ref="nofollow noopener noreferrer">Promises/A+规范</a> 实现一个较为完整的 Promise</p>
<p>Promise 有三种状态<code>pending</code>、<code>resolved</code>、<code>rejected</code>，在一个 Promise 中状态只能改变一次。</p>
<p>首先我们的 Promise 需要传入一个<code>executor</code>函数，它的两个参数可以让我们 resolve 一个 value 或者 reject 一个 reason</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> RESOLVED = <span class="hljs-string">'resolved'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.status = PENDING
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-built_in">this</span>.status = RESOLVED
      &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
        <span class="hljs-built_in">this</span>.reason = reason
        <span class="hljs-built_in">this</span>.status = REJECTED
      &#125;
    &#125;
    <span class="hljs-keyword">try</span> &#123;
      executor(resolve, reject)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      reject(e)
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === RESOLVED) &#123;
      onFulfilled(<span class="hljs-built_in">this</span>.value)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
      onRejected(<span class="hljs-built_in">this</span>.reason)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个 Promise 明显还有许多问题：</p>
<ul>
<li>
<p>如果我们的<code>executor</code>里有异步操作，那么调用<code>then</code>方法的时候，<code>status</code>可能还是<code>pending</code>状态。我们可以用两个数组分别存放回调函数<code>onFulfilledCallbacks</code>和<code>onRejectedCallbacks</code>，在执行<code>resolve</code>和<code>reject</code>函数的时候，再遍历数组中的函数执行。</p>
</li>
<li>
<p><code>promise</code>状态只能修改一次，所以如果状态不为<code>pending</code>进入了<code>resolve</code>或者<code>reject</code>函数时，应该直接 return 掉</p>
</li>
</ul>
<p>改造如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> RESOLVED = <span class="hljs-string">'resolved'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.status = PENDING
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>
    <span class="hljs-built_in">this</span>.onFulfilledCallbacks = []
    <span class="hljs-built_in">this</span>.onRejectedCallbacks = []
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.status = FULFILLED
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-built_in">this</span>.onFulfilledCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(<span class="hljs-built_in">this</span>.value))
      &#125;)
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.status = REJECTED
        <span class="hljs-built_in">this</span>.reason = reason
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(<span class="hljs-built_in">this</span>.reason))
      &#125;)
    &#125;
    <span class="hljs-keyword">try</span> &#123;
      executor(resolve, reject)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      reject(e)
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    onFulfilled =
      <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value
    onRejected =
      <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span>
        ? onRejected
        : <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
            <span class="hljs-keyword">throw</span> reason
          &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === RESOLVED) &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          onFulfilled(<span class="hljs-built_in">this</span>.value)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          reject(e)
        &#125;
      &#125;)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          onRejected(<span class="hljs-built_in">this</span>.reason)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          reject(e)
        &#125;
      &#125;)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
      <span class="hljs-built_in">this</span>.onFulfilledCallbacks.push(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          onFulfilled(<span class="hljs-built_in">this</span>.value)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          reject(e)
        &#125;
      &#125;)
      <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          onRejected(<span class="hljs-built_in">this</span>.reason)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          reject(e)
        &#125;
      &#125;)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们的 Promise 还不能链式调用了，所以我们继续对我们的 Promise 进行改造</p>
<p>首先我们思考一下，如果能够链式调用的话，我们的<code>then</code>方法肯定需要返回一个<code>promise</code>，我们命名为<code>bridgePromise</code></p>
<p>并且我们需要考虑一下<code>onFulfilled</code>和<code>onRejected</code>的返回值也是一个``promise`的情况</p>
<p>我们抽离一个<code>resolvePromise</code>方法来进行判断</p>
<ul>
<li><code>onFulfilled</code>和<code>onRejected</code>的返回值不能和<code>bridgePromise</code>相同</li>
<li>对于<code>result</code>也是一个<code>promise</code>或者是一个<code>thenable</code>的<code>function</code>或者<code>object</code>的情况，我们使用递归的方法来解决。</li>
<li>否则直接<code>resolve</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">bridgePromise, result, resolve, reject</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (bridgePromise === result) &#123;
    <span class="hljs-comment">// 循环</span>
    <span class="hljs-keyword">return</span> reject(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Chaining cycle detected for promise #<Promise>'</span>)
    )
  &#125;
  <span class="hljs-keyword">if</span> (isPromise(result)) &#123;
    <span class="hljs-keyword">if</span> (result.status === PENDING) &#123;
      result.then(
        <span class="hljs-function"><span class="hljs-params">y</span> =></span> resolvePromise(bridgePromise, y, resolve, reject),
        reject
      )
    &#125; <span class="hljs-keyword">else</span> &#123;
      result.then(resolve, reject)
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isThenable(result)) &#123;
    result.then(<span class="hljs-function"><span class="hljs-params">y</span> =></span> resolvePromise(bridgePromise, y, resolve, reject), reject)
  &#125; <span class="hljs-keyword">else</span> &#123;
    resolve(result)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们的<code>Promise</code>实现得就差不多啦</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> RESOLVED = <span class="hljs-string">'resolved'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.status = PENDING
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>
    <span class="hljs-built_in">this</span>.onFulfilledCallbacks = []
    <span class="hljs-built_in">this</span>.onRejectedCallbacks = []
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.status = FULFILLED
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-built_in">this</span>.onFulfilledCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(<span class="hljs-built_in">this</span>.value))
      &#125;)
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.status = REJECTED
        <span class="hljs-built_in">this</span>.reason = reason
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(<span class="hljs-built_in">this</span>.reason))
      &#125;)
    &#125;
    <span class="hljs-keyword">try</span> &#123;
      executor(resolve, reject)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      reject(e)
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    onFulfilled =
      <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value
    onRejected =
      <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span>
        ? onRejected
        : <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
            <span class="hljs-keyword">throw</span> reason
          &#125;
    <span class="hljs-keyword">return</span> (bridgePromise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === RESOLVED) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> result = onFulfilled(<span class="hljs-built_in">this</span>.value)
            resolvePromise(bridgePromise, result, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> result = onRejected(<span class="hljs-built_in">this</span>.reason)
            resolvePromise(bridgePromise, result, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
        <span class="hljs-built_in">this</span>.onFulfilledCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> result = onFulfilled(<span class="hljs-built_in">this</span>.value)
            resolvePromise(bridgePromise, result, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> result = onRejected(<span class="hljs-built_in">this</span>.reason)
            resolvePromise(bridgePromise, result, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
      &#125;
    &#125;))
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再补充一些<code>Promise</code>的其他方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> RESOLVED = <span class="hljs-string">'resolved'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.status = PENDING
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>
    <span class="hljs-built_in">this</span>.onFulfilledCallbacks = []
    <span class="hljs-built_in">this</span>.onRejectedCallbacks = []
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.status = FULFILLED
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-built_in">this</span>.onFulfilledCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(<span class="hljs-built_in">this</span>.value))
      &#125;)
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.status = REJECTED
        <span class="hljs-built_in">this</span>.reason = reason
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(<span class="hljs-built_in">this</span>.reason))
      &#125;)
    &#125;
    <span class="hljs-keyword">try</span> &#123;
      executor(resolve, reject)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      reject(e)
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    onFulfilled =
      <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value
    onRejected =
      <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span>
        ? onRejected
        : <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
            <span class="hljs-keyword">throw</span> reason
          &#125;
    <span class="hljs-keyword">return</span> (bridgePromise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === RESOLVED) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> result = onFulfilled(<span class="hljs-built_in">this</span>.value)
            resolvePromise(bridgePromise, result, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> result = onRejected(<span class="hljs-built_in">this</span>.reason)
            resolvePromise(bridgePromise, result, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
        <span class="hljs-built_in">this</span>.onFulfilledCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> result = onFulfilled(<span class="hljs-built_in">this</span>.value)
            resolvePromise(bridgePromise, result, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> result = onRejected(<span class="hljs-built_in">this</span>.reason)
            resolvePromise(bridgePromise, result, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
      &#125;
    &#125;))
  &#125;
  <span class="hljs-keyword">catch</span>(onRejected) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, onRejected)
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">p</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (isPromise(p)) <span class="hljs-keyword">return</span> p <span class="hljs-comment">// Promise.resolve(p) 与 new Promise(resolve => resolve(p)) 的区别</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (isThenable(p)) p.then(resolve, reject)
      <span class="hljs-keyword">else</span> resolve(p)
    &#125;)
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">p</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">_, reject</span>) =></span> reject(p))
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promises</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> values = []
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handle</span>(<span class="hljs-params">value, index</span>) </span>&#123;
        values[index] = value
        <span class="hljs-keyword">if</span> (++count === promises.length) resolve(values)
      &#125;
      <span class="hljs-comment">// p 可能不是 Promise，所以用 Promise.resolve 包一下</span>
      promises.forEach(<span class="hljs-function">(<span class="hljs-params">p, i</span>) =></span>
        <span class="hljs-built_in">Promise</span>.resolve(p).then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> handle(value, i), reject)
      )
    &#125;)
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promises</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      promises.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> <span class="hljs-built_in">Promise</span>.resolve(p).then(resolve, reject))
    &#125;)
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">allSettled</span>(<span class="hljs-params">promises</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      <span class="hljs-keyword">let</span> results = []
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handle</span>(<span class="hljs-params">result, index</span>) </span>&#123;
        results[index] = result
        <span class="hljs-keyword">if</span> (++count === promises.length) resolve(results)
      &#125;
      promises.forEach(<span class="hljs-function">(<span class="hljs-params">p, i</span>) =></span>
        <span class="hljs-built_in">Promise</span>.resolve(p).then(
          <span class="hljs-function"><span class="hljs-params">value</span> =></span> handle(&#123; <span class="hljs-attr">status</span>: <span class="hljs-string">'resolved'</span>, value &#125;, i),
          <span class="hljs-function"><span class="hljs-params">reason</span> =></span> handle(&#123; <span class="hljs-attr">status</span>: <span class="hljs-string">'rejected'</span>, reason &#125;, i)
        )
      )
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">📝 Generator</h2>
<p><code>Generator</code>可以用来处理异步事件，解决回调地狱的问题，比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> request = <span class="hljs-built_in">require</span>(<span class="hljs-string">'request'</span>)

request(<span class="hljs-string">'https://www.baidu.com'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error, response</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!error && response.statusCode == <span class="hljs-number">200</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'get times 1'</span>)

    request(<span class="hljs-string">'https://www.baidu.com'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error, response</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (!error && response.statusCode == <span class="hljs-number">200</span>) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'get times 2'</span>)

        request(<span class="hljs-string">'https://www.baidu.com'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error, response</span>) </span>&#123;
          <span class="hljs-keyword">if</span> (!error && response.statusCode == <span class="hljs-number">200</span>) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'get times 3'</span>)
          &#125;
        &#125;)
      &#125;
    &#125;)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>Generator</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> request = <span class="hljs-built_in">require</span>(<span class="hljs-string">'request'</span>)

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">requestGen</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sendRequest</span>(<span class="hljs-params">url</span>) </span>&#123;
    request(url, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error, response</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (!error && response.statusCode == <span class="hljs-number">200</span>) &#123;
        <span class="hljs-comment">// console.log(response.body)</span>

        <span class="hljs-comment">// 注意这里，引用了外部的迭代器 itor</span>
        itor.next(response.body)
      &#125;
    &#125;)
  &#125;

  <span class="hljs-keyword">const</span> url = <span class="hljs-string">'https://www.baidu.com'</span>

  <span class="hljs-comment">// 使用 yield 发起三个请求，每个请求成功后再继续调 next</span>
  <span class="hljs-keyword">const</span> r1 = <span class="hljs-keyword">yield</span> sendRequest(url)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'r1'</span>, r1)
  <span class="hljs-keyword">const</span> r2 = <span class="hljs-keyword">yield</span> sendRequest(url)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'r2'</span>, r2)
  <span class="hljs-keyword">const</span> r3 = <span class="hljs-keyword">yield</span> sendRequest(url)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'r3'</span>, r3)
&#125;

<span class="hljs-keyword">const</span> itor = requestGen()

<span class="hljs-comment">// 手动调第一个 next</span>
itor.next()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子中我们在生成器里面写了一个请求方法，这个方法会去发起网络请求，每次网络请求成功后又继续调用<code>next</code>执行后面的<code>yield</code>，最后是在外层手动调一个<code>next</code>触发这个流程。这样写可以解决回调地狱，但是在<code>requestGen</code>里面引用了外面的迭代器<code>itor</code>，耦合很高，而且不好复用。</p>
<h3 data-id="heading-5">🏀thunk 函数</h3>
<p>为了解决前面说的耦合高，不好复用的问题，就有了 thunk 函数。thunk 函数理解起来有点绕，我先把代码写出来，然后再一步一步来分析它的执行顺序：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Thunk</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">callback</span>) </span>&#123;
      <span class="hljs-keyword">return</span> fn.call(<span class="hljs-built_in">this</span>, ...args, callback)
    &#125;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-keyword">let</span> gen = fn()

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params">err, data</span>) </span>&#123;
    <span class="hljs-keyword">let</span> result = gen.next(data)

    <span class="hljs-keyword">if</span> (result.done) <span class="hljs-keyword">return</span>

    result.value(next)
  &#125;

  next()
&#125;

<span class="hljs-comment">// 使用 thunk 方法</span>
<span class="hljs-keyword">const</span> request = <span class="hljs-built_in">require</span>(<span class="hljs-string">'request'</span>)
<span class="hljs-keyword">const</span> requestThunk = Thunk(request)

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">requestGen</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> url = <span class="hljs-string">'https://www.baidu.com'</span>

  <span class="hljs-keyword">let</span> r1 = <span class="hljs-keyword">yield</span> requestThunk(url)
  <span class="hljs-built_in">console</span>.log(r1.body)

  <span class="hljs-keyword">let</span> r2 = <span class="hljs-keyword">yield</span> requestThunk(url)
  <span class="hljs-built_in">console</span>.log(r2.body)

  <span class="hljs-keyword">let</span> r3 = <span class="hljs-keyword">yield</span> requestThunk(url)
  <span class="hljs-built_in">console</span>.log(r3.body)
&#125;

<span class="hljs-comment">// 启动运行</span>
run(requestGen)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码里面的 Thunk 函数返回了好几层函数，我们从他的使用入手一层一层剥开看：</p>
<ol>
<li>
<p><code>requestThunk</code>是 Thunk 运行的返回值，也就是第一层返回值，参数是<code>request</code>，也就是：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback</span>) </span>&#123;
    <span class="hljs-keyword">return</span> request.call(<span class="hljs-built_in">this</span>, ...args, callback);   <span class="hljs-comment">// 注意这里调用的是 request</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>run</code>函数的参数是生成器，我们看看他到底干了啥：</p>
<ol>
<li>
<p>run 里面先调用生成器，拿到迭代器<code>gen</code>，然后自定义了一个<code>next</code>方法，并调用这个<code>next</code>方法，为了便于区分，我这里称这个自定义的<code>next</code>为局部<code>next</code></p>
</li>
<li>
<p>局部<code>next</code>会调用生成器的<code>next</code>，生成器的<code>next</code>其实就是<code>yield requestThunk(url)</code>，参数是我们传进去的<code>url</code>，这就调到我们前面的那个方法，这个<code>yield</code>返回的<code>value</code>其实是：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback</span>) </span>&#123;
  <span class="hljs-keyword">return</span> request.call(<span class="hljs-built_in">this</span>, url, callback);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>检测迭代器是否已经迭代完毕，如果没有，就继续调用第二步的这个函数，这个函数其实才真正的去<code>request</code>，这时候传进去的参数是局部<code>next</code>，局部<code>next</code>也作为了<code>request</code>的回调函数。</p>
</li>
<li>
<p>这个回调函数在执行时又会调<code>gen.next</code>，这样生成器就可以继续往下执行了，同时<code>gen.next</code>的参数是回调函数的<code>data</code>，这样，生成器里面的<code>r1</code>其实就拿到了请求的返回值。</p>
</li>
</ol>
</li>
</ol>
<p>Thunk 函数就是这样一种可以自动执行 Generator 的函数，因为 Thunk 函数的包装，我们在 Generator 里面可以像同步代码那样直接拿到<code>yield</code>异步代码的返回值。</p>
<h2 data-id="heading-6">🔧co</h2>
<p><code>co </code>接收一个 <code>generator </code>函数，返回一个 <code>promise</code>，<code>generator </code>函数中 <code>yieldable </code>对象有：</p>
<ul>
<li><code>promises</code></li>
<li><code>thunks </code>(functions)</li>
<li><code>array </code>(parallel execution)</li>
<li><code>objects </code>(parallel execution)</li>
<li><code>generators </code>(delegation)</li>
<li><code>generator functions</code> (delegation)</li>
</ul>
<p><code>co</code>会将以上各种对象转为<code>promise</code>，所以直接看对于 <code>yield </code>一个 <code>promise </code>的 <code>generator </code>怎么自动执行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fetch = <span class="hljs-built_in">require</span>(<span class="hljs-string">'node-fetch'</span>)
<span class="hljs-keyword">const</span> co = <span class="hljs-built_in">require</span>(<span class="hljs-string">'co'</span>)
co(<span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 直接用 fetch，简单多了，fetch 返回的就是 Promise</span>
  <span class="hljs-keyword">const</span> r1 = <span class="hljs-keyword">yield</span> fetch(<span class="hljs-string">'https://www.baidu.com'</span>)
  <span class="hljs-keyword">const</span> r2 = <span class="hljs-keyword">yield</span> fetch(<span class="hljs-string">'https://www.baidu.com'</span>)
  <span class="hljs-keyword">const</span> r3 = <span class="hljs-keyword">yield</span> fetch(<span class="hljs-string">'https://www.baidu.com'</span>)

  <span class="hljs-keyword">return</span> &#123;
    r1,
    r2,
    r3,
  &#125;
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-comment">// 这里同样可以拿到&#123;r1, r2, r3&#125;</span>
  <span class="hljs-built_in">console</span>.log(res)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">🤨 源码分析</h3>
<p><code>co</code>的源码并不多，总共两百多行，一半都是在进行 yield 后面的参数检测和处理，检测他是不是 Promise，如果不是就转换为 Promise，所以即使你 yield 后面传的 thunk，他还是会转换成 Promise 处理。转换 Promise 的代码相对比较独立和简单，我这里不详细展开了，这里主要还是讲一讲核心方法<code>co(gen)</code>。下面是我复制的去掉了注释的简化代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">co</span>(<span class="hljs-params">gen</span>) </span>&#123;
  <span class="hljs-keyword">var</span> ctx = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">var</span> args = slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>)

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> gen === <span class="hljs-string">'function'</span>) gen = gen.apply(ctx, args)
    <span class="hljs-keyword">if</span> (!gen || <span class="hljs-keyword">typeof</span> gen.next !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">return</span> resolve(gen)

    onFulfilled()

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onFulfilled</span>(<span class="hljs-params">res</span>) </span>&#123;
      <span class="hljs-keyword">var</span> ret
      <span class="hljs-keyword">try</span> &#123;
        ret = gen.next(res)
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-keyword">return</span> reject(e)
      &#125;
      next(ret)
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onRejected</span>(<span class="hljs-params">err</span>) </span>&#123;
      <span class="hljs-keyword">var</span> ret
      <span class="hljs-keyword">try</span> &#123;
        ret = gen.throw(err)
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-keyword">return</span> reject(e)
      &#125;
      next(ret)
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params">ret</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (ret.done) <span class="hljs-keyword">return</span> resolve(ret.value)
      <span class="hljs-keyword">var</span> value = toPromise.call(ctx, ret.value)
      <span class="hljs-keyword">if</span> (value && isPromise(value)) <span class="hljs-keyword">return</span> value.then(onFulfilled, onRejected)
      <span class="hljs-keyword">return</span> onRejected(
        <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(
          <span class="hljs-string">'You may only yield a function, promise, generator, array, or object, '</span> +
            <span class="hljs-string">'but the following object was passed: "'</span> +
            <span class="hljs-built_in">String</span>(ret.value) +
            <span class="hljs-string">'"'</span>
        )
      )
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>Promise 里面先把 Generator 拿出来执行，得到一个迭代器<code>gen</code></li>
<li>手动调用一次<code>onFulfilled</code>，开启迭代。第一次调用<code>onFulfilled</code>并没有传递参数，这个参数主要是用来接收后面的 then 返回的结果。然后调用<code>gen.next</code>，注意这个的返回值 ret 的形式是&#123;value, done&#125;，然后将这个 ret 传给局部的 next</li>
<li>然后执行局部 next，他接收的参数是 yield 返回值&#123;value, done&#125;
<ol>
<li>这里先检测迭代是否完成，如果完成了，就直接将整个 promise resolve</li>
<li>这里的 value 是 yield 后面表达式的值，可能是 thunk，也可能是 promise</li>
<li>将 value 转换成 promise</li>
<li>将转换后的 promise 拿出来执行，成功的回调是前面的<code>onFulfilled</code></li>
</ol>
</li>
<li>我们再来看下<code>onFulfilled</code>，这是第二次执行<code>onFulfilled</code>了。这次执行的时候传入的参数 res 是上次异步 promise 的执行结果，对应我们的 fetch 就是拿回来的数据，这个数据传给第二个<code>gen.next</code>，效果就是我们代码里面的赋值给了第一个<code>yield</code>前面的变量<code>r1</code>。然后继续局部 next，这个 next 其实就是执行第二个异步 Promise 了。这个 promise 的成功回调又继续调用<code>gen.next</code>，这样就不断的执行下去，直到<code>done</code>变成<code>true</code>为止。</li>
<li>最后看一眼<code>onRejected</code>方法，这个方法其实作为了异步 promise 的错误分支，这个函数里面直接调用了<code>gen.throw</code>，这样我们在 Generator 里面可以直接用<code>try...catch...</code>拿到错误。需要注意的是<code>gen.throw</code>后面还继续调用了<code>next(ret)</code>，这是因为在 Generator 的<code>catch</code>分支里面还可能继续有<code>yield</code>，比如错误上报的网络请求，这时候的迭代器并不一定结束了。</li>
</ol>
<h3 data-id="heading-8">⚙️ 原理</h3>
<p>co 的原理其实是通过 generator.next() 得到 generatorResult，由于 yield 出是一个 promise，通过 generatorResult.value.then 再把 promise 的结果通过 generator.next 的参数传给 yield 的左边，让 generator 自动执行，通过 generatorResult.done 判断是否执行结束</p>
<h2 data-id="heading-9">🍬 async / await</h2>
<p><code>async/await</code>其实是 Generator 和自动执行器的语法糖，写法和实现原理都类似 co 模块的 promise 模式。</p>
<p><code>await</code> 帮我们做到了在同步阻塞代码的同时还能够监听 Promise 对象的决议，一旦 <code>promise</code> 决议，原本暂停执行的 async 函数就会恢复执行。这个时候如果决议是 <code>resolve</code> ，那么返回的结果就是 <code>resolve</code> 出来的值。如果决议是 <code>reject</code> ，我们就必须用 <code>try..catch</code> 来捕获这个错误，因为它相当于执行了 <code>it.throw(err)</code> 。</p>
<p>下面直接给出一种主流的 async / await 语法版本的实现代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> runner = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">gen</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">var</span> it = gen()
    <span class="hljs-keyword">const</span> step = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">execute</span>) </span>&#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">var</span> next = execute()
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        reject(err)
      &#125;

      <span class="hljs-keyword">if</span> (next.done) <span class="hljs-keyword">return</span> resolve(next.value)

      <span class="hljs-built_in">Promise</span>.resolve(next.value)
        .then(<span class="hljs-function"><span class="hljs-params">val</span> =></span> step(<span class="hljs-function">() =></span> it.next(val)))
        .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> step(<span class="hljs-function">() =></span> it.throw(err)))
    &#125;
    step(<span class="hljs-function">() =></span> it.next())
  &#125;)
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-comment">// 等同于</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> gen = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
  &#125;
  runner(gen)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码我们可以看出 async 函数执行后返回的是一个 Promise 对象，然后使用递归的方法去自动执行生成器函数的暂停与启动。通过判断是否 done 进行 new Promise 的 resolve，如果没有完成就继续通过 next 进行传递，用 Promise.resolve 处理 result.value，当这个 promise 决议时就可以重新启动执行生成器函数或者抛出一个错误被 try..catch 所捕获并最终在 async 函数返回的 Promise 对象的错误处理函数中处理。</p>
<h2 data-id="heading-10">🙏参考文章</h2>
<p><a href="https://juejin.cn/post/6844904094079926286" target="_blank" title="https://juejin.cn/post/6844904094079926286">最简实现 Promise，支持异步链式调用（20 行）</a></p>
<p><a href="https://juejin.cn/post/6844904116913700877" target="_blank" title="https://juejin.cn/post/6844904116913700877">手写一个 Promise/A+, 完美通过官方 872 个测试用例</a></p>
<p><a href="https://juejin.cn/post/6844904133577670664" target="_blank" title="https://juejin.cn/post/6844904133577670664">从 Generator 入手读懂 co 模块源码</a></p></div>  
</div>
            