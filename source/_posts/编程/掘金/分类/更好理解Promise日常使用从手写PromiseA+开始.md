
---
title: '更好理解Promise日常使用从手写PromiseA+开始'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8196'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 19:08:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=8196'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Promise</h1>
<p>目的：为了更好使用Promise日常使用。</p>
<h2 data-id="heading-1">Promise概念</h2>
<p>Promise是JavaScript的<code>内置对象</code>，同时也是一个<code>构造函数</code>。<br>
特别说明：Promise构造函数是为了解决<code>异步问题</code>;同步代码中也可以使用（大材小用）。</p>
<h3 data-id="heading-2">作为内置对象</h3>
<h4 data-id="heading-3">静态方法</h4>
<ul>
<li>Promise.all(iterable)</li>
<li>Promise.allSettled(iterable)</li>
<li>Promise.any(iterable)</li>
<li>Promise.race(iterable)</li>
<li>Promise.reject(reason)</li>
<li>Promise.resolve(value)</li>
</ul>
<h3 data-id="heading-4">作为构造函数</h3>
<h4 data-id="heading-5">Promise.prototype</h4>
<ul>
<li>Promise.prototype.constructor</li>
<li>Promise.prototype.then(onFulfilled, onRejected)
<ul>
<li>onFulfilled为可选参数</li>
<li>onRejected为可选参数</li>
</ul>
</li>
<li>Promise.prototype.catch(onRejected)
<ul>
<li>onRejected为可选参数</li>
</ul>
</li>
<li>Promise.prototype.finally(onFinally)
<ul>
<li>onFinally为可选参数</li>
</ul>
</li>
</ul>
<h4 data-id="heading-6">Promise实例</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// ...省略代码</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-comment">/* 异步操作成功 */</span>)&#123;
    resolve(value);
  &#125; <span class="hljs-keyword">else</span> &#123;
    reject(error);
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">关于executor函数、resolve函数、reject函数的说明</h5>
<ul>
<li>Promise构造函数接受一个<code>executor</code>函数作为参数</li>
<li><code>executor</code>函数的两个参数分别是<code>resolve</code>函数和<code>reject</code>函数
<ul>
<li><code>resolve</code>函数的作用是，将Promise对象的状态从“未完成”变为“成功”（即从 <code>pending</code> 变为 <code>resolved</code>），在异步操作成功时调用，并将异步操作的结果，作为参数传递出去；</li>
<li><code>reject</code>函数的作用是，将Promise对象的状态从“未完成”变为“失败”（即从 <code>pending</code> 变为 <code>rejected</code>），在异步操作失败时调用，并将异步操作报出的错误，作为参数传递出去。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-comment">// success</span>
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-comment">// failure</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">关于then方法说明</h5>
<ul>
<li>Promise实例生成以后，可以用<code>then</code>方法分别指定<code>fulfilled</code>状态和<code>rejected</code>状态的回调函数。</li>
<li><code>then</code>方法可以接受两个参数。
<ul>
<li>参数可选：onFulfilled 和 onRejected 都是可选参数，不一定要提供。</li>
<li>如果 <code>onFulfilled</code> 不是函数，其必须被忽略</li>
<li>如果 <code>onRejected</code> 不是函数，其必须被忽略</li>
<li>如果 <code>onFulfilled</code> 是函数：
<ul>
<li>当 promise 执行结束后其必须被调用，其第一个参数为 promise 的终值value</li>
<li>在 promise 执行结束前其不可被调用</li>
<li>其调用次数不可超过一次</li>
</ul>
</li>
<li>如果 <code>onRejected</code> 是函数：
<ul>
<li>当 promise 被拒绝执行后其必须被调用，其第一个参数为 promise 的据因reason</li>
<li>在 promise 被拒绝执行前其不可被调用</li>
<li>其调用次数不可超过一次</li>
</ul>
</li>
</ul>
</li>
<li><code>then</code>方法返回的是一个新的Promise实例（注意，不是原来那个Promise实例）。因此可以采用链式写法，即then方法后面再调用另一个then方法。</li>
</ul>
<h2 data-id="heading-9">手写Promise构造函数更好理解Promise（PromiseA+标准）</h2>
<p>特别说明：通过类实现Promise构造函数</p>
<h3 data-id="heading-10">1. 实现<code>executor</code>函数、<code>resolve</code>函数、<code>reject</code>函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;
  <span class="hljs-comment">// 构造器</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123;
    <span class="hljs-comment">// 成功</span>
    <span class="hljs-keyword">let</span> resolve = <span class="hljs-function">() =></span> &#123; &#125;;
    <span class="hljs-comment">// 失败</span>
    <span class="hljs-keyword">let</span> reject = <span class="hljs-function">() =></span> &#123; &#125;;
    <span class="hljs-comment">// 立即执行executor函数</span>
    executor(resolve, reject);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">2.实现Promise构造函数基本状态(state)</h3>
<ul>
<li>Promise构造函数三种状态
<ul>
<li><code>pending</code>（进行中）</li>
<li><code>fulfilled</code>（已成功)</li>
<li><code>rejected</code>（已失败）</li>
</ul>
</li>
<li>Promise构造函数状态切换
<ul>
<li><code>pending</code>（等待态）为初始态</li>
<li>通过<code>resolve函数</code>可以转化为<code>fulfilled</code>（成功态）
<ul>
<li>成功时，不可转为其他状态，且必须有一个不可改变的值（value）</li>
</ul>
</li>
<li>通过<code>reject函数</code>可以转化为<code>rejected</code>（失败态）
<ul>
<li>失败时，不可转为其他状态，且必须有一个不可改变的原因（reason）</li>
</ul>
</li>
<li>若是<code>executor函数</code>报错 直接执行<code>reject函数</code></li>
</ul>
</li>
<li>Promise构造函数几个关键属性
<ul>
<li><code>state</code>: 状态描述</li>
<li><code>value</code>: 成功值</li>
<li><code>reason</code>: 失败原因</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123;
    <span class="hljs-comment">// 初始化state为等待态(state状态只能改变一次)</span>
    <span class="hljs-comment">// 因为只有状态为pending时候可以改变</span>
    <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'pending'</span>;
    <span class="hljs-comment">// 成功初始值</span>
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
    <span class="hljs-comment">// 失败原因初始值</span>
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>;
    
    <span class="hljs-comment">// resolve函数、reject函数</span>
    <span class="hljs-keyword">const</span> resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-comment">// 如果state不为pending,下面条件为false,块级作用域代码不再执行</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-comment">// resolve调用后，state转化为fulfilled成功态</span>
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'fulfilled'</span>;
        <span class="hljs-comment">// 更新成功的值</span>
        <span class="hljs-built_in">this</span>.value = value;
      &#125;
    &#125;;
    <span class="hljs-keyword">const</span> reject = <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
      <span class="hljs-comment">// 如果state不为pending,下面条件为false,块级作用域代码不再执行</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-comment">// reject调用后，state转化为rejected失败态</span>
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'rejected'</span>;
        <span class="hljs-comment">// 更新失败的原因</span>
        <span class="hljs-built_in">this</span>.reason = reason;
      &#125;
    &#125;;
    
    <span class="hljs-comment">// 如果executor执行报错，直接执行reject函数,错误信息作为入参传给reject函数</span>
    <span class="hljs-keyword">try</span>&#123;
      executor(resolve, reject);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      reject(error);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3.实现Promise实例的then方法（Promise.prototype.then）</h3>
<ul>
<li>then的方法接收两个参数(可选)：<code>onFulfilled</code>函数和<code>onRejected</code>函数</li>
<li><code>onFulfilled</code>函数的参数为成功值<code>value</code></li>
<li><code>onRejected</code>函数的参数为失败原因<code>reason</code></li>
</ul>
<h4 data-id="heading-13">executor函数同步执行</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123; 
      <span class="hljs-comment">// ...省略代码</span>
  &#125;
  <span class="hljs-comment">// then方法有两个参数onFulfilled函数和onRejected函数</span>
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span> &#123;
    <span class="hljs-comment">// 状态为fulfilled，执行onFulfilled函数，传入成功的值</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'fulfilled'</span>) &#123;
      onFulfilled(<span class="hljs-built_in">this</span>.value);
    &#125;;
    <span class="hljs-comment">// 状态为rejected，执行onRejected函数，传入失败的原因</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'rejected'</span>) &#123;
      onRejected(<span class="hljs-built_in">this</span>.reason);
    &#125;;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">executor函数在异步中调用resolve函数或reject函数</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'pending'</span>;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>;
    <span class="hljs-comment">// onFulfilled函数回调数组</span>
    <span class="hljs-built_in">this</span>.onResolvedCallbacks = [];
    <span class="hljs-comment">// onRejected函数回调数组</span>
    <span class="hljs-built_in">this</span>.onRejectedCallbacks = [];
    <span class="hljs-keyword">const</span> resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'fulfilled'</span>;
        <span class="hljs-built_in">this</span>.value = value;
        <span class="hljs-comment">// 一旦resolve执行，调用onFulfilled函数回调数组</span>
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span>=></span>fn());
      &#125;
    &#125;;
    <span class="hljs-keyword">const</span> reject = <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'rejected'</span>;
        <span class="hljs-built_in">this</span>.reason = reason;
        <span class="hljs-comment">// 一旦reject执行，onRejected函数回调数组</span>
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span>=></span>fn());
      &#125;
    &#125;;
    <span class="hljs-keyword">try</span>&#123;
      executor(resolve, reject);
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      reject(err);
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'fulfilled'</span>) &#123;
      onFulfilled(<span class="hljs-built_in">this</span>.value);
    &#125;;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'rejected'</span>) &#123;
      onRejected(<span class="hljs-built_in">this</span>.reason);
    &#125;;
    <span class="hljs-comment">// 当状态state为pending时</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
      <span class="hljs-comment">// onFulfilled函数传入onFulfilled函数回调数组</span>
      <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">()=></span>&#123;
        onFulfilled(<span class="hljs-built_in">this</span>.value);
      &#125;)
      <span class="hljs-comment">// onRejected传入onRejected函数回调数组</span>
      <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">()=></span>&#123;
        onRejected(<span class="hljs-built_in">this</span>.reason);
      &#125;)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>上述代码同时实现了<code>同一个</code>promise实例被多个then调用问题</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 多个then的情况</span>
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>();
p.then();
p.then();
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-15">4.实现Promise实例的链式调用</h3>
<p>调用Promise构造函数原型对象的then、catch、finally都返回新的<code>promise实例</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123;
    <span class="hljs-comment">// ...省略代码</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span> &#123;
    <span class="hljs-comment">// 返回的promise2</span>
    <span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>)=></span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'fulfilled'</span>) &#123;
        <span class="hljs-keyword">const</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value);
        <span class="hljs-comment">// resolvePromise函数，处理onFulfilled函数return的x和默认的promise2的关系</span>
        resolvePromise(promise2, x, resolve, reject);
      &#125;;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'rejected'</span>) &#123;
        <span class="hljs-keyword">const</span> x = onRejected(<span class="hljs-built_in">this</span>.reason);
        <span class="hljs-comment">// resolvePromise函数，处理onRejected函数return的x和默认的promise2的关系</span>
        resolvePromise(promise2, x, resolve, reject);
      &#125;;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-keyword">const</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value);
          resolvePromise(promise2, x, resolve, reject);
        &#125;)
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-keyword">const</span> x = onRejected(<span class="hljs-built_in">this</span>.reason);
          resolvePromise(promise2, x, resolve, reject);
        &#125;)
      &#125;
    &#125;);
    <span class="hljs-comment">// 返回promise，完成链式</span>
    <span class="hljs-keyword">return</span> promise2;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">resolvePromise函数实现</h5>
<ol>
<li>如果<code>promise</code>和 <code>x</code> 指向同一对象(<code>x === promise2</code>)，会造成循环引用，自己等待自己完成，则报“循环引用”错误以 TypeError 为据因拒绝执行 promise</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
  resolve(<span class="hljs-string">'success'</span>);
&#125;);
<span class="hljs-keyword">const</span> p1 = p.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-comment">// 循环引用，自己等待自己完成，一辈子完不成</span>
  <span class="hljs-keyword">return</span> p1;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>比较x和promise2,避免循环应用</li>
<li>如果 <code>x== null</code> 或 <code>typeof x !== 'object'</code> 或 <code>typeof x !== 'function'</code>直接<code>resolv(x)</code></li>
<li>如果<code>x != null && (typeof x === 'object' || typeof x === 'function')</code>
<ul>
<li>x不是promise,直接<code>resolv(x)</code></li>
<li>x是promise直接调用then方法</li>
</ul>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise2, x, resolve, reject</span>)</span>&#123;
  <span class="hljs-comment">// 循环引用报错</span>
  <span class="hljs-keyword">if</span>(x === promise2)&#123;
    <span class="hljs-comment">// reject报错</span>
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Chaining cycle detected for promise'</span>));
  &#125;
  <span class="hljs-comment">// 防止多次调用</span>
  <span class="hljs-keyword">let</span> called;
  <span class="hljs-comment">// x不是null 且x是对象或者函数</span>
  <span class="hljs-keyword">if</span> (x != <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span>)) &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// A+规定，声明then = x的then方法</span>
      <span class="hljs-keyword">const</span> then = x.then;
      <span class="hljs-comment">// 如果then是函数，就默认是promise了</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">'function'</span>) &#123; 
        <span class="hljs-comment">// 就让then执行第一个参数是this后面是成功的回调和失败的回调</span>
        <span class="hljs-comment">// then方法中this指向x</span>
        then.call(x, <span class="hljs-function"><span class="hljs-params">y</span> =></span> &#123;
          <span class="hljs-comment">// 成功和失败只能调用一个</span>
          <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
          called = <span class="hljs-literal">true</span>;
          <span class="hljs-comment">// resolve的结果依旧是promise 那就继续解析</span>
          resolvePromise(promise2, y, resolve, reject);
        &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
          <span class="hljs-comment">// 成功和失败只能调用一个</span>
          <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
          called = <span class="hljs-literal">true</span>;
          reject(err);<span class="hljs-comment">// 失败了就直接执行reject函数</span>
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        resolve(x); <span class="hljs-comment">// 直接成功即可</span>
      &#125;
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-comment">// 也属于失败</span>
      <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
      called = <span class="hljs-literal">true</span>;
      <span class="hljs-comment">// 取then出错了那就不要在继续执行了</span>
      reject(e); 
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    resolve(x);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">5.完善then方法中onFulfilled函数和onRejected函数</h3>
<ul>
<li>1、PromiseA+规定onFulfilled,onRejected都是可选参数，如果他们不是函数，<code>必须被忽略</code>。
<ul>
<li>onFulfilled是一个普通的值，成功时直接等于 value => value</li>
<li>onRejected返回一个普通的值，失败时如果直接等于 value => value，则会跑到下一个then中的onFulfilled中，所以直接扔出一个错误reason => throw err</li>
</ul>
</li>
<li>4、PromiseA+规定onFulfilled或onRejected不能同步被调用，必须异步调用。我们就用setTimeout解决异步问题</li>
<li>5、如果onFulfilled或onRejected报错，则直接返回reject()</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123;
      <span class="hljs-comment">// ...省略代码</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span> &#123;
    <span class="hljs-comment">// onFulfilled如果不是函数，就忽略onFulfilled，直接返回value</span>
    onFulfilled = <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
    <span class="hljs-comment">// onRejected如果不是函数，就忽略onRejected，直接扔出错误</span>
    onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-keyword">throw</span> err &#125;;
    <span class="hljs-keyword">let</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'fulfilled'</span>) &#123;
        <span class="hljs-comment">// 异步</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value);
            resolvePromise(promise2, x, resolve, reject);
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e);
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'rejected'</span>) &#123;
        <span class="hljs-comment">// 异步</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// 如果报错</span>
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason);
            resolvePromise(promise2, x, resolve, reject);
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e);
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// 异步</span>
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value);
              resolvePromise(promise2, x, resolve, reject);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
              reject(e);
            &#125;
          &#125;, <span class="hljs-number">0</span>);
        &#125;);
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// 异步</span>
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason);
              resolvePromise(promise2, x, resolve, reject);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
              reject(e);
            &#125;
          &#125;, <span class="hljs-number">0</span>)
        &#125;);
      &#125;;
    &#125;);
    <span class="hljs-comment">// 返回promise，完成链式</span>
    <span class="hljs-keyword">return</span> promise2;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">6.实现catch和resolve、reject、race、all方法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'pending'</span>;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>;
    <span class="hljs-built_in">this</span>.onResolvedCallbacks = [];
    <span class="hljs-built_in">this</span>.onRejectedCallbacks = [];
    <span class="hljs-keyword">let</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'fulfilled'</span>;
        <span class="hljs-built_in">this</span>.value = value;
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span>=></span>fn());
      &#125;
    &#125;;
    <span class="hljs-keyword">let</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'rejected'</span>;
        <span class="hljs-built_in">this</span>.reason = reason;
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span>=></span>fn());
      &#125;
    &#125;;
    <span class="hljs-keyword">try</span>&#123;
      executor(resolve, reject);
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      reject(err);
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span> &#123;
    onFulfilled = <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
    onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-keyword">throw</span> err &#125;;
    <span class="hljs-keyword">let</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'fulfilled'</span>) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">const</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value);
            resolvePromise(promise2, x, resolve, reject);
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e);
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'rejected'</span>) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">const</span> x = onRejected(<span class="hljs-built_in">this</span>.reason);
            resolvePromise(promise2, x, resolve, reject);
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e);
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">const</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value);
              resolvePromise(promise2, x, resolve, reject);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
              reject(e);
            &#125;
          &#125;, <span class="hljs-number">0</span>);
        &#125;);
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">const</span> x = onRejected(<span class="hljs-built_in">this</span>.reason);
              resolvePromise(promise2, x, resolve, reject);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
              reject(e);
            &#125;
          &#125;, <span class="hljs-number">0</span>)
        &#125;);
      &#125;;
    &#125;);
    <span class="hljs-keyword">return</span> promise2;
  &#125;
  <span class="hljs-comment">// catch方法</span>
  <span class="hljs-keyword">catch</span>(fn)&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>,fn);
  &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise2, x, resolve, reject</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(x === promise2)&#123;
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Chaining cycle detected for promise'</span>));
  &#125;
  <span class="hljs-keyword">let</span> called;
  <span class="hljs-keyword">if</span> (x != <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span>)) &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> then = x.then;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">'function'</span>) &#123; 
        then.call(x, <span class="hljs-function"><span class="hljs-params">y</span> =></span> &#123;
          <span class="hljs-keyword">if</span>(called)<span class="hljs-keyword">return</span>;
          called = <span class="hljs-literal">true</span>;
          resolvePromise(promise2, y, resolve, reject);
        &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
          <span class="hljs-keyword">if</span>(called)<span class="hljs-keyword">return</span>;
          called = <span class="hljs-literal">true</span>;
          reject(err);
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        resolve(x);
      &#125;
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">if</span>(called)<span class="hljs-keyword">return</span>;
      called = <span class="hljs-literal">true</span>;
      reject(e); 
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    resolve(x);
  &#125;
&#125;
<span class="hljs-comment">//resolve方法</span>
<span class="hljs-built_in">Promise</span>.resolve = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    resolve(val)
  &#125;);
&#125;
<span class="hljs-comment">//reject方法</span>
<span class="hljs-built_in">Promise</span>.reject = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    reject(val)
  &#125;);
&#125;
<span class="hljs-comment">//race方法 </span>
<span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promises</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<promises.length;i++)&#123;
      promises[i].then(resolve,reject)
    &#125;;
  &#125;)
&#125;
<span class="hljs-comment">//all方法(获取所有的promise，都执行then，把结果放到数组，一起返回)</span>
<span class="hljs-built_in">Promise</span>.all = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promises</span>)</span>&#123;
  <span class="hljs-keyword">let</span> arr = [];
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processData</span>(<span class="hljs-params">index,data</span>)</span>&#123;
    arr[index] = data;
    i++;
    <span class="hljs-keyword">if</span>(i == promises.length)&#123;
      resolve(arr);
    &#125;;
  &#125;;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<promises.length;i++)&#123;
      promises[i].then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
        processData(i,data);
      &#125;,reject);
    &#125;;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">Promise配合async/await使用</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> result = <span class="hljs-literal">true</span>;
<span class="hljs-comment">// 从服务器接口获取数据</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getServerData</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 模拟请求</span>
    <span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">if</span>(result)&#123;
                resolve(<span class="hljs-string">'data'</span>)
            &#125;<span class="hljs-keyword">else</span> &#123;
                reject(<span class="hljs-string">'err'</span>)
            &#125;
        &#125;, <span class="hljs-number">1000</span>);
    &#125;)
    <span class="hljs-keyword">return</span> p
&#125;
<span class="hljs-comment">// 供前端调用接口</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dataController</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
       <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> getServerData();
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'data'</span>,data);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-comment">// 可以捕获reject</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error'</span>, error);
    &#125;
&#125;
<span class="hljs-comment">// 前端接口</span>
dataController()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>特别说明<code>try...catch</code>中<code>catch</code>可以捕获<code>reject</code>函数的<code>reason</code></li>
</ul>
<h1 data-id="heading-20">参考文章</h1>
<p><a href="https://juejin.cn/post/6844903625769091079" target="_blank">BAT前端经典面试问题：史上最最最详细的手写Promise教程</a></p>
<h1 data-id="heading-21">关于Generator函数</h1></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            