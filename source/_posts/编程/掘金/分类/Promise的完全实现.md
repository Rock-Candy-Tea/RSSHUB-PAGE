
---
title: 'Promise的完全实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6923'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:10:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=6923'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>开发中<code>Promise</code>是及其常用的语法，基本上对于异步的处理大都是通过<code>Promise</code>来进行完成。Promise规范有很多，ES6最终采用的是<code>Promise/A+ 规范</code>,所以以下代码也基本是基于这个规范来进行编写的。</p>
<p>首先我们先列举Promise的所有实例方法跟静态方法</p>
<p><strong>实例方法</strong></p>
<ul>
<li>then: <code>new Promise((resolve, reject) => &#123;...&#125;).then(() => &#123;console.log('rsolve成功回调')&#125;, () => &#123;console.log('reject失败回调')&#125;)</code></li>
<li>catch: <code>new Promise((resolve, reject) => &#123;...&#125;).catch(() => &#123;console.log('reject失败方法')&#125;)</code></li>
<li>finally: <code>new Promise((resolve, reject) => &#123;...&#125;).finally(() => &#123;console.log('成功失败都进入')&#125;)</code></li>
<li>以上方法调用都将返回新的<code>Promise</code></li>
</ul>
<p><strong>静态方法</strong></p>
<ul>
<li>resolve: <code>Promise.resolve(value)</code>返回<code>Promise</code>实例</li>
<li>reject: <code>Promise.reject(value)</code>返回<code>Promise</code>实例</li>
<li>all: <code>Promise.all(promises)</code>: 传入数组格式的<code>Promise</code>并返回新的<code>Promise</code>实例，成功便按照顺序把值返回出来，其中一个失败则直接变成失败</li>
<li>race: <code>Promise.race(promises)</code>: 传入数组格式的<code>Promise</code>并返回新的<code>Promise</code>实例，成功与失败取决第一个的完成方式</li>
</ul>
<p><code>Promise</code>状态一旦确定变不可再发生变化，有以下三个状态：<code>pending</code>、<code>fulfilled</code>、<code>rejected</code>
<code>Promise</code>在浏览器中的实现是放于微任务队列中的，需要做微任务的处理（<a href="https://segmentfault.com/a/1190000022805523" target="_blank" rel="nofollow noopener noreferrer"><code>JavaScript中的Event Loop（事件循环）机制</code></a>）</p>
<h2 data-id="heading-0">1.声明Promise的实例方法</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  _value
  _state = <span class="hljs-string">'pending'</span>
  _queue = []
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-string">'Promise resolver undefined is not a function'</span>
    &#125;
    <span class="hljs-comment">/* 
      new Promise((resolve, reject) => &#123;
        resolve: 成功
        reject: 失败
      &#125;)
    */</span>
    fn(<span class="hljs-built_in">this</span>._resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>._reject.bind(<span class="hljs-built_in">this</span>))
  &#125;

  <span class="hljs-comment">// 接收1-2参数，第一个为成功的回调，第二个为失败的回调</span>
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-comment">// 有可能已经resolve了，因为Promise可以提前resolve,然后then方法后面注册</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state === <span class="hljs-string">'fulfilled'</span>) &#123;
      onFulfilled?.(<span class="hljs-built_in">this</span>._value)
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// reject同理</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state === <span class="hljs-string">'rejected'</span>) &#123;
      onRejected?.(<span class="hljs-built_in">this</span>._value)
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// Promise还没有完成，push到一个队列，到时候完成的时候，执行这个队列里面对应的函数</span>
    <span class="hljs-built_in">this</span>._queue.push(&#123;
      onFulfilled,
      onRejected,
    &#125;)
  &#125;

  <span class="hljs-comment">// 接收失败的回调</span>
  <span class="hljs-keyword">catch</span>(onRejected) &#123;
    <span class="hljs-comment">// 相当于直接调用then传入失败的回调</span>
    <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, onRejected)
  &#125;

  <span class="hljs-comment">// 成功与失败都执行的回调</span>
  <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">onDone</span>)</span> &#123;
    <span class="hljs-keyword">const</span> fn = <span class="hljs-function">() =></span> onDone()
    <span class="hljs-built_in">this</span>.then(fn, fn)
  &#125;
  <span class="hljs-comment">// 成功resolve</span>
  <span class="hljs-function"><span class="hljs-title">_resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-comment">// 状态确定了，就不再发生变化了</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-built_in">this</span>._state = <span class="hljs-string">'fulfilled'</span>

    <span class="hljs-comment">// 把值存起来，当再次调用的时候直接取这个值就行，因为Promise一旦确定就不会发生改变了</span>
    <span class="hljs-built_in">this</span>._value = value

    <span class="hljs-comment">// 执行前面.then方法里面push函数形式的参数，这样就执行对应的方法了。</span>
    <span class="hljs-built_in">this</span>._queue.forEach(<span class="hljs-function">(<span class="hljs-params">callback</span>) =></span> &#123;
      callback.onFulfilled?.(<span class="hljs-built_in">this</span>._value)
    &#125;)
  &#125;

  <span class="hljs-comment">// 失败reject</span>
  <span class="hljs-function"><span class="hljs-title">_reject</span>(<span class="hljs-params">error</span>)</span> &#123;
    <span class="hljs-comment">// 状态确定了，就不再发生变化了</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-built_in">this</span>._state = <span class="hljs-string">'rejected'</span>
    <span class="hljs-built_in">this</span>._value = error
    <span class="hljs-built_in">this</span>._queue.forEach(<span class="hljs-function">(<span class="hljs-params">callback</span>) =></span> &#123;
      callback.onRejected?.(<span class="hljs-built_in">this</span>._value)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用逻辑：</p>
<ol>
<li>
<p>通过<code>then</code>方法传入函数形式的参数，也就是<code>onFulfilled</code> => <code>then((onFulfilled, onRejected) => &#123;...&#125;)</code></p>
</li>
<li>
<p>在<code>then</code>方法中把<code>onFulfilled</code>函数放入<code>_queue</code>这个集合中。 => <code>this._queue.push(&#123; onFulfilled, onRejected &#125;)</code></p>
</li>
<li>
<p>等异步回调完成，执行<code>resolve</code>函数，这个时候就调用<code>_queue</code>收集好的通过<code>then</code>方法注册的函数。统一执行这些函数，这样就达到异步回调完成，执行对应的<code>then</code>方法里面的函数</p>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 结果打印</span>
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-string">'success'</span>)
  &#125;, <span class="hljs-number">1000</span>)
&#125;)
p.then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// => success</span>
&#125;)

<span class="hljs-comment">// reject</span>
<span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    reject(<span class="hljs-string">'fail'</span>)
  &#125;, <span class="hljs-number">1000</span>)
&#125;)
p1.catch(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// => fail</span>
&#125;)

<span class="hljs-comment">// finally</span>
<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve()
  &#125;, <span class="hljs-number">1000</span>)
&#125;)
p2.finally(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'done'</span>) <span class="hljs-comment">// => done</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><a href="https://codesandbox.io/s/agitated-star-8w4cb?file=/Promise-step1.html" target="_blank" rel="nofollow noopener noreferrer">在线代码演示</a></p>
</blockquote>
<h2 data-id="heading-1">2. 微任务处理以及返回Promise</h2>
<h3 data-id="heading-2">a. 进行微任务处理</h3>
<p>在浏览器中 <code>Promise</code> 完成之后会被推入微任务，所以我们也需要进行这块的处理。浏览器中使用<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/MutationObserver/MutationObserver" target="_blank" rel="nofollow noopener noreferrer">MutationObserver</a>,node可以使用<code>process.nextTick</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  ...
  <span class="hljs-comment">// 推入微任务</span>
  <span class="hljs-function"><span class="hljs-title">_nextTick</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> MutationObserver !== <span class="hljs-string">'undefined'</span>) &#123; <span class="hljs-comment">// 浏览器通过MutationObserver实现微任务的效果</span>
      <span class="hljs-comment">// 这块可以单独拿出来共用，避免不必要的开销，不然每次都需要生成节点。</span>
      <span class="hljs-keyword">const</span> observer = <span class="hljs-keyword">new</span> MutationObserver(fn)
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">1</span>
      <span class="hljs-keyword">const</span> textNode = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-built_in">String</span>(count))
      observer.observe(textNode, &#123;
        <span class="hljs-attr">characterData</span>: <span class="hljs-literal">true</span>
      &#125;)
      textNode.data = <span class="hljs-built_in">String</span>(++count)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> process.nextTick !== <span class="hljs-string">'undefined'</span>) &#123; <span class="hljs-comment">// node端通过process.nextTick来实现</span>
      process.nextTick(fn)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">setTimeout</span>(fn, <span class="hljs-number">0</span>)
    &#125;
  &#125;
  <span class="hljs-comment">// 成功resolve</span>
  <span class="hljs-function"><span class="hljs-title">_resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-comment">// 状态确定了，就不再发生变化了</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 推入微任务</span>
    <span class="hljs-built_in">this</span>._nextTick(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>._state = <span class="hljs-string">'fulfilled'</span>
      <span class="hljs-built_in">this</span>._value = value
      <span class="hljs-built_in">this</span>._queue.forEach(<span class="hljs-function">(<span class="hljs-params">callback</span>) =></span> &#123;
        callback.onFulfilled?.(<span class="hljs-built_in">this</span>._value)
      &#125;)
    &#125;)
  &#125;

  <span class="hljs-comment">// 失败reject</span>
  <span class="hljs-function"><span class="hljs-title">_reject</span>(<span class="hljs-params">error</span>)</span> &#123;
    <span class="hljs-comment">// 状态确定了，就不再发生变化了</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 推入微任务</span>
    <span class="hljs-built_in">this</span>._nextTick(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>._state = <span class="hljs-string">'rejected'</span>
      <span class="hljs-built_in">this</span>._value = error
      <span class="hljs-built_in">this</span>._queue.forEach(<span class="hljs-function">(<span class="hljs-params">callback</span>) =></span> &#123;
        callback.onRejected?.(<span class="hljs-built_in">this</span>._value)
      &#125;)
    &#125;)
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><a href="https://codesandbox.io/s/agitated-star-8w4cb?file=/Promise-step2.html" target="_blank" rel="nofollow noopener noreferrer">效果演示</a></p>
</blockquote>
<h3 data-id="heading-3">b. 返回Promise进行链式调用</h3>
<p>通常<code>Promise</code>会处理多个异步请求，有时候请求之间是有相互依赖关系的。</p>
<p>例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> getUser = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(&#123;
        <span class="hljs-attr">userId</span>: <span class="hljs-string">'123'</span>
      &#125;)
    &#125;, <span class="hljs-number">500</span>)
  &#125;)
&#125;

<span class="hljs-keyword">const</span> getDataByUser = <span class="hljs-function">(<span class="hljs-params">userId</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// ....</span>
      resolve(&#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>&#125;)
    &#125;, <span class="hljs-number">500</span>)
  &#125;)
&#125;

<span class="hljs-comment">// 使用</span>
getUser().then(<span class="hljs-function">(<span class="hljs-params">user</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> getDataByUser(user.userId)
&#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">// &#123;a: 1&#125;</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>getDataByUser</code>依赖<code>getUser</code>请求回来的用户信息，这里就需要用到<code>Promise</code>链式的调用,下面我们来改动我们的代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">fn</span>)</span> &#123;
    fn(<span class="hljs-built_in">this</span>._resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>._reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  ...
  <span class="hljs-comment">// 1. 这时候then方法需要返回新的Promise了,因为需要进行链式调用，并且下一个then方法接受上一个then方法的值</span>
  <span class="hljs-comment">// 2. 返回的Promise肯定是一个新的Promise，不然就会共用状态跟返回结果了。</span>
  <span class="hljs-comment">// 3. 把上一个then方法中的返回值当做下一个Promise resolve的值</span>
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-comment">// 返回新的Promise</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-comment">// 有可能已经resolve了，因为Promise可以提前resolve,然后then方法后面注册,这个时候可以直接把值返给函数就好了</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state === <span class="hljs-string">'fulfilled'</span> && onFulfilled) &#123;
        <span class="hljs-built_in">this</span>._nextTick(onFulfilled.bind(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>._value))
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state === <span class="hljs-string">'rejected'</span> && onRejected) &#123;
        <span class="hljs-built_in">this</span>._nextTick(onRejected.bind(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>._value))
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-comment">/* 
        把当前Promise的then方法的参数跟新的Promise的resolve, reject存到一起，以此来做关联。
        这样就能把上一个Promise中的onFulfilled与新的Promise中的resolve两个关联到一块，然后便可以做赋值之类的操作了。reject同理
      */</span>
      <span class="hljs-built_in">this</span>._queue.push(&#123;
        onFulfilled,
        onRejected,
        resolve,
        reject
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-comment">// reject同理</span>
  <span class="hljs-function"><span class="hljs-title">_resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-comment">// 状态确定了，就不再发生变化了</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>

    <span class="hljs-comment">// 上面示例里面其实返回的是一个Promise,而不是直接返回的值，所以，这里我们需要做一个特殊处理。</span>
    <span class="hljs-comment">// 就是resolve()的值如果是Promise的对象，我们需要解析Promise的结果，然后在把值传给resolve</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span> && <span class="hljs-keyword">typeof</span> value.then === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-comment">// 我们可以把当前_resolve方法传递下去，因为then方法中的参数，一经下个Promise resolve,便会执行then方法对应的参数，然后把对应的值传入。</span>
      <span class="hljs-comment">// 这样就能取到Promise中的值</span>
      <span class="hljs-comment">// this._resove => obj.onFulfilled?.(this._value)</span>
      <span class="hljs-comment">// this._reject => obj.onRejected?.(this._value)</span>
      value.then(<span class="hljs-built_in">this</span>._resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>._reject.bind(<span class="hljs-built_in">this</span>))
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-comment">// 推入微任务</span>
    <span class="hljs-built_in">this</span>._nextTick(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>._state = <span class="hljs-string">'fulfilled'</span>
      <span class="hljs-built_in">this</span>._value = value
      <span class="hljs-built_in">this</span>._queue.forEach(<span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
        <span class="hljs-comment">// 接受onFulfilled返回值</span>
        <span class="hljs-keyword">const</span> val = obj.onFulfilled?.(<span class="hljs-built_in">this</span>._value)
        <span class="hljs-comment">// reoslve这个值,此时 onFulfilled 是当前Promise then方法中的第一个参数： Promise.then((res) => &#123;consolle.log(res)&#125;)</span>
        <span class="hljs-comment">// obj.resolve是新的Promise的resolve函数，这样就把then方法中的返回值传给下一个Promise</span>
        obj.resolve(val)
      &#125;)
    &#125;)
  &#125;
  ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><a href="https://codesandbox.io/s/agitated-star-8w4cb?file=/Promise-step3.html" target="_blank" rel="nofollow noopener noreferrer">效果演示</a></p>
</blockquote>
<p>调用逻辑：</p>
<ol>
<li>
<p>微任务采用<code>MutationObserver</code>跟<code>process.nextTick</code>来进行实现</p>
</li>
<li>
<p><code>Promise</code>链式调用，这里通过把<code>then</code>方法中的<code>(onFulfilled, onRejected)</code>参数与新返回的<code>Promise</code>中的<code>(resolve, reject)</code>关联到一起。</p>
</li>
<li>
<p>一旦上一个<code>Promise</code>成功,调用<code>onFulfilled</code>函数，就可以把<code>onFulfilled</code>中返回的值，放到新的Promise的resolve中。</p>
</li>
<li>
<p>如果遇到<code>resolve</code>的值是<code>Promise</code>对象，递归进行解析，然后再把值返回出去</p>
</li>
</ol>
<p>完整代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  _value
  _state = <span class="hljs-string">'pending'</span>
  _queue = []
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Promise resolver undefined is not a function'</span>)
    &#125;
    <span class="hljs-comment">/* 
      new Promise((resolve, reject) => &#123;
        resolve: 成功
        reject: 失败
      &#125;)
    */</span>
    fn(<span class="hljs-built_in">this</span>._resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>._reject.bind(<span class="hljs-built_in">this</span>))
  &#125;

  <span class="hljs-comment">// 接收1-2参数，第一个为成功的回调，第二个为失败的回调</span>
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-comment">// 返回新的Promise</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-comment">// 有可能已经resolve了，因为Promise可以提前resolve,然后then方法后面注册,这个时候可以直接把值返给函数就好了</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state === <span class="hljs-string">'fulfilled'</span> && onFulfilled) &#123;
        <span class="hljs-built_in">this</span>._nextTick(onFulfilled.bind(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>._value))
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state === <span class="hljs-string">'rejected'</span> && onRejected) &#123;
        <span class="hljs-built_in">this</span>._nextTick(onRejected.bind(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>._value))
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-comment">// 把当前Promise的then方法的参数跟新的Promise的resolve, reject存到一起，以此来做关联</span>
      <span class="hljs-built_in">this</span>._queue.push(&#123;
        onFulfilled,
        onRejected,
        resolve,
        reject
      &#125;)
    &#125;)
  &#125;

  <span class="hljs-comment">// 接收失败的回调</span>
  <span class="hljs-keyword">catch</span>(onRejected) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, onRejected)
  &#125;

  <span class="hljs-comment">// 成功与失败都执行的回调</span>
  <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">onDone</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      onDone()
      <span class="hljs-keyword">return</span> value
    &#125;, <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-comment">// console.log(value)</span>
      onDone()
      <span class="hljs-keyword">throw</span> value
    &#125;)
  &#125;

  <span class="hljs-comment">// 推入微任务</span>
  <span class="hljs-function"><span class="hljs-title">_nextTick</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> MutationObserver !== <span class="hljs-string">'undefined'</span>) &#123; <span class="hljs-comment">// 浏览器</span>
      <span class="hljs-comment">// 这块可以单独拿出来共用，避免不必要的开销，不然每次都需要生成节点。</span>
      <span class="hljs-keyword">const</span> observer = <span class="hljs-keyword">new</span> MutationObserver(fn)
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">1</span>
      <span class="hljs-keyword">const</span> textNode = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-built_in">String</span>(count))
      observer.observe(textNode, &#123;
        <span class="hljs-attr">characterData</span>: <span class="hljs-literal">true</span>
      &#125;)
      textNode.data = <span class="hljs-built_in">String</span>(++count)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> process.nextTick !== <span class="hljs-string">'undefined'</span>) &#123; <span class="hljs-comment">// node</span>
      process.nextTick(fn)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">setTimeout</span>(fn, <span class="hljs-number">0</span>)
    &#125;
  &#125;
  <span class="hljs-comment">// 成功resolve</span>
  <span class="hljs-function"><span class="hljs-title">_resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-comment">// 状态确定了，就不再发生变化了</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>

    <span class="hljs-comment">// 上面示例里面其实返回的是一个Promise,而不是直接返回的值，所以，这里我们需要做一个特殊处理。</span>
    <span class="hljs-comment">// 就是如果resolve()的如果是Promise的对象，我们需要解析Promise的结果，然后在把值传给resolve</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span> && <span class="hljs-keyword">typeof</span> value.then === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-comment">// 我们可以把当前_resolve方法传递下去，因为then方法中的参数，一经下个Promise resolve,便会执行then方法对应的参数，然后把对应的值传入。</span>
      <span class="hljs-comment">// 这样就能取到Promise中的值</span>
      <span class="hljs-comment">// this._resove => obj.onFulfilled?.(this._value)</span>
      <span class="hljs-comment">// this._reject => obj.onRejected?.(this._value)</span>
      value.then(<span class="hljs-built_in">this</span>._resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>._reject.bind(<span class="hljs-built_in">this</span>))
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-comment">// 推入微任务</span>
    <span class="hljs-built_in">this</span>._nextTick(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>._state = <span class="hljs-string">'fulfilled'</span>
      <span class="hljs-built_in">this</span>._value = value
      <span class="hljs-built_in">this</span>._queue.forEach(<span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
        <span class="hljs-comment">// 使用try catch 来捕获onFulfilled存在函数内部错误的情况</span>
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-comment">// 接受onFulfilled返回值，如果不存在，把this._value往下传递</span>
          <span class="hljs-keyword">const</span> val = obj.onFulfilled ? obj.onFulfilled(<span class="hljs-built_in">this</span>._value) : <span class="hljs-built_in">this</span>._value
          <span class="hljs-comment">// reoslve这个值,此时 onFulfilled 是当前Promise then方法中的第一个参数： Promise.then((res) => &#123;consolle.log(res)&#125;)</span>
          <span class="hljs-comment">// obj.resolve是新的Promise的resolve函数，这样就把then方法中的返回值传给下一个Promise</span>
          obj.resolve(val)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          obj.reject(e)
        &#125;
      &#125;)
    &#125;)
  &#125;

  <span class="hljs-comment">// 失败reject</span>
  <span class="hljs-function"><span class="hljs-title">_reject</span>(<span class="hljs-params">error</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-built_in">this</span>._nextTick(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>._state = <span class="hljs-string">'rejected'</span>
      <span class="hljs-built_in">this</span>._value = error
      <span class="hljs-built_in">this</span>._queue.forEach(<span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">const</span> val = obj.onRejected ? obj.onRejected(<span class="hljs-built_in">this</span>._value) : <span class="hljs-built_in">this</span>._value
          <span class="hljs-comment">// 当前 reject执行完毕之后，会返回新的Promise，应该是能正常resolve的，所以这里要用 resolve, 不应该继续使用reject来让下个Promise执行失败流程</span>
          obj.resolve(val)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          obj.reject(e)
        &#125;
      &#125;)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">声明Promise的静态方法</h2>
<p>总共有4个静态方法: <code>Promise.resolve</code>、<code>Promise.reject</code>、<code>Promise.all</code>、<code>Promise.race</code>，统一返回的都是新的Promise。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  ...
  <span class="hljs-comment">/**
   * 直接resolve
   */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-comment">// 是Promise直接返回</span>
    <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
      <span class="hljs-keyword">return</span> value
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span> && <span class="hljs-keyword">typeof</span> value.then === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-comment">// 传入的对象含有then方法</span>
      <span class="hljs-keyword">const</span> then = value.then
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        then.call(value, resolve)
      &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 正常返回值，直接返回新的Promise在resolve这个值</span>
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> resolve(value))
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * 直接reject, 测试下Promise.reject并没做特殊处理，所以直接返回即可。
   */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(value))
  &#125;

  <span class="hljs-comment">/**
   * 传入数组格式的`Promise`并返回新的`Promise`实例，成功便按照顺序把值返回出来，其中一个失败则直接变成失败
   */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promises</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
      <span class="hljs-keyword">let</span> arr = []
      <span class="hljs-comment">// 按照对应的下标push到数组里面</span>
      promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise, index</span>) =></span> &#123;
        <span class="hljs-comment">// 转换成Promise对象</span>
        <span class="hljs-built_in">Promise</span>.resolve(promise).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          count++
          arr[index] = res
          <span class="hljs-keyword">if</span> (count === promises.length) &#123;
            resolve(arr)
          &#125;
        &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> reject(err))
      &#125;)
    &#125;)
  &#125;
  
  <span class="hljs-comment">/**
   * 传入数组格式的`Promise`并返回新的`Promise`实例，成功与失败取决第一个的完成方式
   */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promises</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise, index</span>) =></span> &#123;
        <span class="hljs-comment">// 转换成Promise对象</span>
        <span class="hljs-built_in">Promise</span>.resolve(promise).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          <span class="hljs-comment">// 谁先执行直接resolve, 或reject</span>
          resolve(res)
        &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> reject(err))
      &#125;)
    &#125;)
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Promise实现完整代码</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  _value
  _state = <span class="hljs-string">'pending'</span>
  _queue = []
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Promise resolver undefined is not a function'</span>)
    &#125;
    <span class="hljs-comment">/* 
      new Promise((resolve, reject) => &#123;
        resolve: 成功
        reject: 失败
      &#125;)
    */</span>
    fn(<span class="hljs-built_in">this</span>._resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>._reject.bind(<span class="hljs-built_in">this</span>))
  &#125;

  <span class="hljs-comment">/**
   * 接收1-2参数，第一个为成功的回调，第二个为失败的回调
   *
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">onFulfilled</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">onRejected</span></span>
   * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span> </span>
   * <span class="hljs-doctag">@memberof <span class="hljs-variable">Promise</span></span>
   */</span>
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-comment">// 返回新的Promise</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-comment">// 有可能已经resolve了，因为Promise可以提前resolve,然后then方法后面注册,这个时候可以直接把值返给函数就好了</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state === <span class="hljs-string">'fulfilled'</span> && onFulfilled) &#123;
        <span class="hljs-built_in">this</span>._nextTick(onFulfilled.bind(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>._value))
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state === <span class="hljs-string">'rejected'</span> && onRejected) &#123;
        <span class="hljs-built_in">this</span>._nextTick(onRejected.bind(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>._value))
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-comment">// 把当前Promise的then方法的参数跟新的Promise的resolve, reject存到一起，以此来做关联</span>
      <span class="hljs-built_in">this</span>._queue.push(&#123;
        onFulfilled,
        onRejected,
        resolve,
        reject
      &#125;)
    &#125;)
  &#125;

  <span class="hljs-comment">/**
   * 接收失败的回调
   *
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">onRejected</span></span>
   * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span> </span>
   * <span class="hljs-doctag">@memberof <span class="hljs-variable">Promise</span></span>
   */</span>
  <span class="hljs-keyword">catch</span>(onRejected) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, onRejected)
  &#125;

  <span class="hljs-comment">/**
   * 成功与失败都执行的回调
   *
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">onDone</span></span>
   * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span> </span>
   * <span class="hljs-doctag">@memberof <span class="hljs-variable">Promise</span></span>
   */</span>
  <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">onDone</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      onDone()
      <span class="hljs-keyword">return</span> value
    &#125;, <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      onDone()
      <span class="hljs-comment">// 直接报错，可以在try catch中捕获错误</span>
      <span class="hljs-keyword">throw</span> value
    &#125;)
  &#125;

  <span class="hljs-comment">/**
   * 直接resolve
   *
   * <span class="hljs-doctag">@static</span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">value</span></span>
   * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span> </span>
   * <span class="hljs-doctag">@memberof <span class="hljs-variable">Promise</span></span>
   */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
      <span class="hljs-keyword">return</span> value
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span> && <span class="hljs-keyword">typeof</span> value.then === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-comment">// 传入的对象含有then方法</span>
      <span class="hljs-keyword">const</span> then = value.then
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        then.call(value, resolve)
      &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> resolve(value))
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * 直接reject, 测试下reject在Promise.reject中没做特殊处理
   *
   * <span class="hljs-doctag">@static</span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">value</span></span>
   * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span> </span>
   * <span class="hljs-doctag">@memberof <span class="hljs-variable">Promise</span></span>
   */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(value))
  &#125;

  <span class="hljs-comment">/**
   * 传入数组格式的`Promise`并返回新的`Promise`实例，成功便按照顺序把值返回出来，其中一个失败则直接变成失败
   *
   * <span class="hljs-doctag">@static</span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">promises</span></span>
   * <span class="hljs-doctag">@memberof <span class="hljs-variable">Promise</span></span>
   */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promises</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
      <span class="hljs-keyword">let</span> arr = []
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(promises)) &#123;
        <span class="hljs-keyword">if</span> (promises.length === <span class="hljs-number">0</span>) &#123;
          <span class="hljs-keyword">return</span> resolve(promises)
        &#125;
        promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise, index</span>) =></span> &#123;
          <span class="hljs-comment">// 转换成Promise对象</span>
          <span class="hljs-built_in">Promise</span>.resolve(promise).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
            count++
            arr[index] = res
            <span class="hljs-keyword">if</span> (count === promises.length) &#123;
              resolve(arr)
            &#125;
          &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> reject(err))
        &#125;)
        <span class="hljs-keyword">return</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        reject(<span class="hljs-string">`<span class="hljs-subst">$&#123;promises&#125;</span> is not Array`</span>)
      &#125;
    &#125;)
  &#125;
  
  <span class="hljs-comment">/**
   * 传入数组格式的`Promise`并返回新的`Promise`实例，成功与失败取决第一个的完成方式
   *
   * <span class="hljs-doctag">@static</span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">promises</span></span>
   * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span> </span>
   * <span class="hljs-doctag">@memberof <span class="hljs-variable">Promise</span></span>
   */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promises</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(promises)) &#123;
        promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise, index</span>) =></span> &#123;
          <span class="hljs-comment">// 转换成Promise对象</span>
          <span class="hljs-built_in">Promise</span>.resolve(promise).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
            resolve(res)
          &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> reject(err))
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        reject(<span class="hljs-string">`<span class="hljs-subst">$&#123;promises&#125;</span> is not Array`</span>)
      &#125;
    &#125;)
  &#125;

  <span class="hljs-comment">// 推入微任务</span>
  <span class="hljs-function"><span class="hljs-title">_nextTick</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> MutationObserver !== <span class="hljs-string">'undefined'</span>) &#123; <span class="hljs-comment">// 浏览器</span>
      <span class="hljs-comment">// 这块可以单独拿出来共用，避免不必要的开销，不然每次都需要生成节点。</span>
      <span class="hljs-keyword">const</span> observer = <span class="hljs-keyword">new</span> MutationObserver(fn)
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">1</span>
      <span class="hljs-keyword">const</span> textNode = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-built_in">String</span>(count))
      observer.observe(textNode, &#123;
        <span class="hljs-attr">characterData</span>: <span class="hljs-literal">true</span>
      &#125;)
      textNode.data = <span class="hljs-built_in">String</span>(++count)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> process.nextTick !== <span class="hljs-string">'undefined'</span>) &#123; <span class="hljs-comment">// node</span>
      process.nextTick(fn)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">setTimeout</span>(fn, <span class="hljs-number">0</span>)
    &#125;
  &#125;
  <span class="hljs-comment">// 成功resolve</span>
  <span class="hljs-function"><span class="hljs-title">_resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-comment">// 状态确定了，就不再发生变化了</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>

    <span class="hljs-comment">// 上面示例里面其实返回的是一个Promise,而不是直接返回的值，所以，这里我们需要做一个特殊处理。</span>
    <span class="hljs-comment">// 就是如果resolve()的如果是Promise的对象，我们需要解析Promise的结果，然后在把值传给resolve</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span> && <span class="hljs-keyword">typeof</span> value.then === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-comment">// 我们可以把当前_resolve方法传递下去，因为then方法中的参数，一经下个Promise resolve,便会执行then方法对应的参数，然后把对应的值传入。</span>
      <span class="hljs-comment">// 这样就能取到Promise中的值</span>
      <span class="hljs-comment">// this._resove => obj.onFulfilled?.(this._value)</span>
      <span class="hljs-comment">// this._reject => obj.onRejected?.(this._value)</span>
      value.then(<span class="hljs-built_in">this</span>._resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>._reject.bind(<span class="hljs-built_in">this</span>))
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-comment">// 通过打印测试，如果直接在线程里进行resolve, 状态跟值好像是直接就改变了，并没有执行完主流程，在执行微任务的时候进行修改的。</span>
    <span class="hljs-comment">// 所以把状态改变和值的修改移出了微任务，只有在走回调的时候才通过微任务进行处理</span>
    <span class="hljs-built_in">this</span>._state = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>._value = value

    <span class="hljs-comment">// 推入微任务</span>
    <span class="hljs-built_in">this</span>._nextTick(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>._queue.forEach(<span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
        <span class="hljs-comment">// 使用try catch 来捕获onFulfilled存在函数内部错误的情况</span>
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-comment">// 接受onFulfilled返回值，如果不存在，把this._value往下传递</span>
          <span class="hljs-keyword">const</span> val = obj.onFulfilled ? obj.onFulfilled(<span class="hljs-built_in">this</span>._value) : <span class="hljs-built_in">this</span>._value
          <span class="hljs-comment">// reoslve这个值,此时 onFulfilled 是当前Promise then方法中的第一个参数： Promise.then((res) => &#123;consolle.log(res)&#125;)</span>
          <span class="hljs-comment">// obj.resolve是新的Promise的resolve函数，这样就把then方法中的返回值传给下一个Promise</span>
          obj.resolve(val)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          obj.reject(e)
        &#125;
      &#125;)
    &#125;)
  &#125;

  <span class="hljs-comment">// 失败reject</span>
  <span class="hljs-function"><span class="hljs-title">_reject</span>(<span class="hljs-params">error</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._state !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-built_in">this</span>._state = <span class="hljs-string">'rejected'</span>
    <span class="hljs-built_in">this</span>._value = error

    <span class="hljs-built_in">this</span>._nextTick(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>._queue.forEach(<span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-comment">// 用户传入的函数内部错误捕获</span>
          <span class="hljs-keyword">if</span> (obj.onRejected) &#123;
            <span class="hljs-keyword">const</span> val = obj.onRejected(<span class="hljs-built_in">this</span>._value)
            <span class="hljs-comment">// 当前 reject执行完毕之后，会返回新的Promise，应该是能正常resolve的，所以这里要用 resolve, 不应该继续使用reject来让下个Promise执行失败流程</span>
            obj.resolve(val)
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 递归传递reject错误</span>
            obj.reject(<span class="hljs-built_in">this</span>._value)
          &#125;
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          obj.reject(e)
        &#125;
      &#125;)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><a href="https://codesandbox.io/s/agitated-star-8w4cb?file=/complete.html" target="_blank" rel="nofollow noopener noreferrer">完整演示效果</a></p>
</blockquote>
<blockquote>
<p><a href="https://dzblog.cn/article/60dc33e718dbe9391712042a" target="_blank" rel="nofollow noopener noreferrer">博客原文地址</a></p>
</blockquote>
<blockquote>
<p>本项目完整代码：<a href="https://github.com/cd-dongzi/source-code-analysis/blob/main/Promise/implement/index.js" target="_blank" rel="nofollow noopener noreferrer">GitHub</a></p>
</blockquote>
<p>以上就是Promise的实现方案,当然这个跟完整的<code>Promises/A+规范</code>是有区别的。这里只是用做于学习之用。</p>
<p>QQ群：前端打杂群</p>
<p>公众号：冬瓜书屋</p></div>  
</div>
            