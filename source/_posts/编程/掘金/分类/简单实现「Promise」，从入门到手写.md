
---
title: '简单实现「Promise」，从入门到手写'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6502'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 07:33:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=6502'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p><code>Promise</code> 已经成为前端开发必备技能，它主要解决了异步编程时大量嵌套回调函数，导致的回调低于问题，本篇我将以学习笔记的形式，和大家一起来深入学习它。内容主要包括<strong>基本用法</strong>和<strong>手写</strong>两部分，适合刚入门的新手和想深入了解原理的小伙伴。</p>
<h1 data-id="heading-1">认识 Promise</h1>
<ul>
<li><code>CommonJS</code> 社区首先提出了 <code>Promise</code> 规范，在 <code>ES2015</code> 中被标准化，成为语言规范</li>
<li><code>Promise</code> 是一个对象，用来表示一个异步任务结束之后，是成功了还是失败了，任何一个 Promise 对象的初始状态都为 <code>Pending</code>，当任务成功后，状态改为 <code>Fulfilled</code>，然后执行成功任务的回调 <code>onFufilled</code>；当任务失败后，状态改为 <code>Rejected</code>，然后执行失败任务的回调 <code>onRejected</code></li>
<li>状态只能从 <code>Pending</code> 变为 <code>Fulfilled</code> 或者从 <code>Pending</code> 变成 <code>Rejected</code>，只有这两种变化，而且改变之后将<strong>不可能</strong>再对其进行修改，就像我承诺，今天晚上要请你吃饭，如果晚上请了，就是 Fulfilled，如果晚上没请，就是 Rejected，假如我说今天要加班，改成明天吧，那也是 Rejected，因为明天的承诺是明天的，今天这个承诺已经有结果了，无法改变了。</li>
</ul>
<h1 data-id="heading-2">Promise 基本用法</h1>
<h2 data-id="heading-3">第一步：创建实例</h2>
<p><code>Promise</code> 是 <code>ES2015</code> 中新增的一个全局对象，通过 <code>new</code> 创建一个 <code>Promise</code> 实例，传入一个 <code>executor</code> 函数，这个函数会立即开始执行，主要的业务流程都在 <code>executor</code> 函数中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-comment">/*异步操作成功*/</span>)&#123;
        resolve(<span class="hljs-string">'执行成功了'</span>)
    &#125;<span class="hljs-keyword">else</span>&#123;
        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'执行失败了'</span>))
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>resolve</code> 和 <code>reject</code>两个函数作为参数传递给 <code>executor</code> 函数</p>
<ul>
<li>调用 <code>resolve</code> 函数时，将我们的 <code>Promise</code> 状态修改为 <code>Fulfilled</code>，并将异步操作成功后的结果作为参数传递出去</li>
<li>调用 <code>reject</code> 函数时，将我们的 <code>Promise</code> 状态修改为 <code>Rejected</code>，并将异步操作失败的原因作为参数传递出去</li>
<li>二者只能调用其一，要么成功，要么失败</li>
<li>需要注意的是，<code>Promise</code> 是用来管理异步的，但它本身不是异步的，<code>executor</code> 函数会立即执行，我们往往会在 <code>executor</code> 中编写异步操作</li>
</ul>
<h2 data-id="heading-4">第二步：调用 then 方法</h2>
<p><code>Promise</code> 实例创建好之后，使用它的 <code>then</code> 方法来指定 <code>onFulfilled</code> 或者 <code>onRejected</code> 的回调函数，第一个参数是 <code>onFulfilled</code> 回调，第二个参数是 <code>onRejected</code> 回调，其中 <code>onRejected</code> 可以省略。</p>
<pre><code class="hljs language-js copyable" lang="js">promise.then( <span class="hljs-function"><span class="hljs-params">value</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resolved'</span>,value)
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span>&#123; <span class="hljs-comment">// onRejected 回调可以省略</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'rejected'</span>,error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">执行时序</h1>
<p>即使我们没有执行任何异步操作，promise.then 中的回调函数，也是在 JS 执行完同步任务之后才去执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
  resolve(<span class="hljs-number">100</span>)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
&#125;)
promise.then( <span class="hljs-function"><span class="hljs-params">value</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resolved'</span>,value)
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'rejected'</span>,error)
&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'3'</span>)

<span class="hljs-comment">/*输出结果*/</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 3</span>
<span class="hljs-comment">// resolved 100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>new Promise</code> 时先执行 <code>executor</code> 函数，打印出 1 和 2，因为 <code>resolve</code> 是微任务，先不执行它，继续往下执行同步任务，执行 <code>promise.then</code>，将成功回调和失败回调都存储到起来（存储到 Promie 实例的变量中，后面手写 Promise 的内容会讲到），此时先不执行他们，然后打印出 3，此时同步任务执行完毕，开始执行微任务，调用 then 方法的成功回调，打印出 resolved 100</p>
<p>然后我们再加入定时器来看一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
  resolve(<span class="hljs-number">100</span>)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
&#125;)

<span class="hljs-comment">// 在此加入定时器，执行顺序是怎样的呢？</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout'</span>)
&#125;,<span class="hljs-number">0</span>)

promise.then( <span class="hljs-function"><span class="hljs-params">value</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resolved'</span>,value)
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'rejected'</span>,error)
&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'3'</span>)

<span class="hljs-comment">/*输出结果*/</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 3</span>
<span class="hljs-comment">// resolved 100</span>
<span class="hljs-comment">// setTimeout</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>setTimeout</code> 的时间为 0，会立即进入回调队列中排队，等待下一轮的执行。这里有个误区，因为 <code>setTimeout</code> 比 <code>Promise</code> 先执行，我们会以为 <code>setTimeout</code> 会先进入队列中，就先执行，但实际并不是这样。</p>
<p>因为 <code>Promise</code> 属于微任务，<code>setTimeout</code> 属于宏任务，当前同步代码执行完毕后，如果有微任务，就顺带把微任务执行了，如果有宏任务，则等到下一个队列中去执行。关于宏任务和微任务的概念与区别，具体可以参考<a href="https://juejin.cn/post/6844903657264136200" target="_blank">微任务、宏任务与Event-Loop</a></p>
<p>微任务是为了提高整体的响应能力，在 JS 中，大部分异步任务都是宏任务，只有 <code>Promise</code>、<code>MutationObserver</code> 和 node 中的 <code>process.nextTick</code> 会作为微任务执行。</p>
<h1 data-id="heading-6">常见的错误</h1>
<p><code>Promise</code> 的本质还是回调，当异步任务结束后，通过 <code>then</code> 方法执行回调，有的同学不自然就会嵌套回调，这是因为对 <code>Promise</code> 用法不清晰，不知道 <code>Promise</code> 链式调用的特点。</p>
<pre><code class="hljs language-js copyable" lang="js">promiseA.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value1</span>)</span>&#123;
    promiseB.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value2</span>)</span>&#123;
        promiseC.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value3</span>)</span>&#123;
            <span class="hljs-comment">/*回调地狱*/</span>
            ......
        &#125;)
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">Promise 的链式调用</h1>
<p><code>then</code> 方法在执行完成后返回一个新的 <code>Promise</code> 对象，因此可以使用链式调用避免回调地狱，使得代码扁平化。</p>
<p><code>Promise</code> 的链式调用与传统的链式调用有所不同：</p>
<ul>
<li>传统链式调用是在函数中返回 <code>this</code></li>
<li><code>Promise</code> 链式调用是在 <code>then</code> 中返回一个新的 <code>Promise</code> 对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    resolve(<span class="hljs-number">100</span>)
&#125;)
<span class="hljs-keyword">const</span> promise2 = promise1.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(value)
&#125;)
<span class="hljs-keyword">const</span> promsie3 = promise2.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(value)
&#125;)

<span class="hljs-built_in">console</span>.log(promise1 === promise2) <span class="hljs-comment">// false 证明返回的是新 Promise 对象</span>
<span class="hljs-built_in">console</span>.log(promise2 === promise3) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 <code>then</code> 返回的是一个新 <code>Promise</code>，所以当前调用的 <code>then</code>，是在给上一个 <code>then</code> 返回的 <code>Promise</code> 对象，添加状态改变后的回调：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    resolve(<span class="hljs-number">100</span>)
&#125;)

<span class="hljs-comment">/*链式调用*/</span>
promise
.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'11111'</span>)
&#125;)
.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'22222'</span>)
&#125;)
.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'33333'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以在 <code>then</code> 方法中手动返回新的 <code>Promise</code>，也可以返回一个普通值：</p>
<pre><code class="hljs language-js copyable" lang="js">promise
.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-comment">// 手动返回新的 Promise</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
        resolve(<span class="hljs-number">800</span>)
    &#125;)
&#125;)
.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(value) <span class="hljs-comment">// 800</span>
    <span class="hljs-comment">// 手动返回普通值</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello promise'</span>
&#125;)
.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(value) <span class="hljs-comment">// hello promise</span>
&#125;)
.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(value) <span class="hljs-comment">// undefined   上一个 then 没有返回值</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">异常处理</h1>
<pre><code class="hljs language-js copyable" lang="js">promise
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
&#125;)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>)</span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'error'</span>)
&#125;)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
&#125;)
.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRejected'</span>,error)
&#125;)
<span class="hljs-comment">// 输出</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在链式调用的最后使用 <code>catch</code> 捕获异常，指定失败的回调</li>
<li>它捕获到的是整个链式调用中所有的异常，有点类似于 “冒泡”，一直向后传递，直到被 <code>catch</code> 捕获</li>
<li>通过这种方式，我们不必在每个 <code>then</code> 中写 <code>onRejected</code> 回调，也不必每个 <code>then</code> 后面写 <code>catch</code>，这使我们的代码更优雅</li>
</ul>
<h1 data-id="heading-9">静态方法</h1>
<h2 data-id="heading-10">Promise.resolve( )</h2>
<p>如果接收的是普通值，把普通值作为结果，返回一个 Promise</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 返回状态为 Fulfilled 的 Promise 对象</span>
<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'hello world'</span>)
.then(<span class="hljs-function"><span class="hljs-params">value</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(value) <span class="hljs-comment">// hello world</span>
&#125;)
<span class="hljs-comment">// 等价于</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    resolve(<span class="hljs-string">'hello world'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果接收的是另一个 <code>Promise</code> 对象，则原样返回</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;&#125;)
<span class="hljs-keyword">const</span> promise2 = <span class="hljs-built_in">Promise</span>.resolve(promise)

<span class="hljs-built_in">console</span>.log(promise === promise2) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">Promise.reject( )</h2>
<p>返回一个失败的 Promise，无论传入什么参数，都将作为失败原因</p>
<pre><code class="hljs language-js copyable" lang="js">cosnt promise = <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'hello world'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">Promise.all( )</h2>
<p>将多个 <code>Promise</code> 实例组合成一个新的 <code>Promise</code> 实例，它的成功和失败返回值不同，成功时返回的是一个数组，包含每个 <code>Promise</code> 的执行结果，失败时返回的是最先 reject 的值。</p>
<ul>
<li><code>Promise.all</code> 当所有 <code>Promise</code> 对象都成功了，才会执行成功回调，只要有一个失败了，就会执行失败回调</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-built_in">Promise</span>.all([
    <span class="hljs-built_in">Promise</span>.resolve(&#123;<span class="hljs-attr">code</span>:<span class="hljs-number">200</span>,<span class="hljs-attr">data</span>:[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>]&#125;),
    <span class="hljs-built_in">Promise</span>.resolve(&#123;<span class="hljs-attr">code</span>:<span class="hljs-number">200</span>,<span class="hljs-attr">data</span>:[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]&#125;),
    <span class="hljs-built_in">Promise</span>.resolve(&#123;<span class="hljs-attr">code</span>:<span class="hljs-number">200</span>,<span class="hljs-attr">data</span>:[<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]&#125;),
])

promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">values</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(values) <span class="hljs-comment">// 此时拿到的 values 是数组，包含每个 promise 异步任务的执行结果</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如我们要同时请求多个接口，当所有数据都返回时再执行下一步，这时就可以使用<code>Promise.all</code> 方法</p>
<p>注意：<code>Promise.all</code> 得到的成功结果数组，与调用 <code>Promise.all</code> 时传入的实例顺序相同，也就是上面代码中，请求接口1、请求接口2、请求接口3的顺序，即使请求接口1最后才获取到结果，也是放在最前面。</p>
<h2 data-id="heading-13">Promise.allSettled( )</h2>
<p>有时我们不关心异步操作的结果，只关心这些操作有没有执行完，于是在 <code>ES2020</code> 中引入了 <code>Promise.allSettled</code> 方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.allSettled([
    <span class="hljs-built_in">Promise</span>.resolve(&#123;<span class="hljs-attr">code</span>:<span class="hljs-number">200</span>,<span class="hljs-attr">data</span>:[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>]&#125;),
    <span class="hljs-built_in">Promise</span>.reject(&#123;<span class="hljs-attr">code</span>:<span class="hljs-number">500</span>,<span class="hljs-attr">errMsg</span>:<span class="hljs-string">'服务器异常'</span>&#125;),
    <span class="hljs-built_in">Promise</span>.resolve(&#123;<span class="hljs-attr">code</span>:<span class="hljs-number">200</span>,<span class="hljs-attr">data</span>:[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]&#125;)
])
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">values</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(values)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Promise.allSettled</code> 与 <code>Promise.all</code> 很相似，唯一不同的是，<code>Promise.allSettled</code> 会拿到每一个 <code>Promise</code> 的状态，无论它是成功或者失败。</p>
<h2 data-id="heading-14">Promie.race( )</h2>
<p>同样是支持多个 Promise 调用，但与 Promise.all 有所不同，race 是赛跑的意思，Promise.race([p1,p2,p3]) 中哪个执行最快， 就返回哪个结果，无论它是成功还是失败</p>
<ul>
<li><code>Promise.all</code> 等待所有任务完成后，新返回的 Promise 才会完成</li>
<li><code>Promise.race</code> 只要有一个任务成功，新返回的 Promise 就会成功，只要有一个 Promise 失败，返回的 Promise 就会失败</li>
</ul>
<h2 data-id="heading-15">Promise.finally( )</h2>
<p><code>ES9</code> 新怎了 <code>finally</code> 方法，无论结果是 <code>Fulfilled</code> 还是 <code>Rejected</code>，都会执行 <code>finally</code> 指定的回调函数，这样就避免了我们在 <code>then</code> 和 <code>catch</code> 中各写一次操作的情况</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 请求接口时让页面转圈圈</span>
<span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>

axios.get(<span class="hljs-string">'http://juejin.cn/api'</span>)
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-comment">// this.loading = false</span>
    &#125;)
    .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-comment">// this.loading = false</span>
    &#125;)
    .finally(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">false</span>
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">手写 Promise</h1>
<p>我们不能直接罗列完整的 <code>Promise</code> 代码，那样看不出思路，我们要从无到有、渐进式地完成这项工作。所以我会在每一步的关键位置写上注释，通过前后代码对比的方式来学习，看似代码很多，但重点在于增量代码。</p>
<h2 data-id="heading-17">一个最基本的 Promise</h2>
<p>要想手写 <code>Promise</code>，得先对它的使用方式和特点做下总结：</p>
<ul>
<li><code>Promise</code> 通过 <code>new</code> 出来，那一定是个构造函数或者类，我们就用类的方式来实现</li>
<li>接收一个执行器函数 <code>executor</code>，并且能够立即执行</li>
<li>执行器函数接收 <code>resolve</code> 和 <code>reject</code>，它们用于改变 <code>Promise</code> 的状态</li>
<li><code>Promise</code> 有三种状态：<code>Pendding</code>、<code>Fulfilled</code>、<code>Rejected</code>，且一旦确定了就不能改变</li>
<li>通过 <code>then</code> 方法判断状态，如果是成功则执行 <code>onFulfilled</code>，如果是失败则执行 <code>onRejected</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义三个状态常量</span>
<span class="hljs-keyword">const</span> PENDDING = <span class="hljs-string">'PENDDING'</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-comment">// 接收一个执行器函数 executor</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
        <span class="hljs-comment">// 立即执行 executor，传入 resolve 和 reject 函数</span>
        executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject)
    &#125;
    <span class="hljs-comment">// 每个 Promise 实例都有一个属于自己的状态，初始为 PENDDING</span>
    status = PENDDING
    
    <span class="hljs-comment">// 缓存成功结果和失败原因</span>
    value = <span class="hljs-literal">undefined</span>
    reason = <span class="hljs-literal">undefined</span>

    resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-comment">/**
         * 1.业务代码的异步函数成功后，调用 resolve 并传入成功值 value
         * 2.resolve 的作用是将状态改为 FULFILLED，并将 value 保存起来
         * 3.为什么是箭头函数：我们是在 executor 中直接调用 resolve 的，如果是普通函数，this 会指向 window，我们需要 this 指向 Promise 实例
         * 4.如果状态不是 PENDDING，则不允许修改
         */</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = FULFILLED

        <span class="hljs-comment">// 保存成功后的值，将来在 then 方法的成功回调中使用</span>
        <span class="hljs-built_in">this</span>.value = value
    &#125;

    reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-comment">// 与 resolve 类似，reject 用于处理异步任务失败的情况</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = REJECTED

        <span class="hljs-comment">// 保存失败后的原因，将来在 then 方法的失败回调中使用</span>
        <span class="hljs-built_in">this</span>.reason = reason
    &#125;

    <span class="hljs-comment">/**
     * 1.每个 Promise 实例都有 then 方法，所以将 then 定义在类中
     * 2.then 方法接收两个参数，成功回调和失败回调
     * 3.根据状态判断调用哪个回调，并传入相应的值
     */</span>
    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED) &#123;
            onFulfilled(<span class="hljs-built_in">this</span>.value)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
            onRejected(<span class="hljs-built_in">this</span>.reason)
        &#125;
    &#125;

&#125;
<span class="hljs-comment">// 最后别忘了导出</span>
<span class="hljs-built_in">module</span>.exports = MyPromise
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试一下是否可用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyPromise = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./promise.js'</span>)

<span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-string">'成功'</span>)
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(value)
&#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(reason)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">处理异步情况</h2>
<p>接下来处理下业务中的异步情况，我们在业务代码中加入定时器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyPromise = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./promise.js'</span>)

<span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// 异步情况</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        resolve(<span class="hljs-string">'成功'</span>);
    &#125;,<span class="hljs-number">2000</span>)
&#125;)

<span class="hljs-comment">// 主线程不会等待 setTimeout，而是先执行到这里 </span>
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(value)
&#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(reason)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主线程不会等待 <code>setTimeout</code>，往下执行到 <code>then</code>，但此时还没有执行 <code>resolve</code> 或者 <code>reject</code>，也就意味着 <code>Promise</code> 的状态还是 <code>PENDDING</code>，所以要在 <code>then</code> 中加一个判断：如果是 <code>PENDDING</code> 状态，则先将 <code>onFulfilled</code> 和 <code>onRejected</code> 回调函数存储起来，等到异步任务执行完毕，开始执行 <code>resolve</code> 或者 <code>reject</code> 的时候再去调用回调函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDDING = <span class="hljs-string">'PENDDING'</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
        executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject)
    &#125;
    
    status = PENDDING
    
    value = <span class="hljs-literal">undefined</span>
    reason = <span class="hljs-literal">undefined</span>
    
    <span class="hljs-comment">// 缓存成功回调与失败回调</span>
    onFulfilled = <span class="hljs-literal">undefined</span>
    onRejected = <span class="hljs-literal">undefined</span>

    resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = FULFILLED

        <span class="hljs-built_in">this</span>.value = value

        <span class="hljs-comment">/**
         * 针对异步情况，判断成功回调是否存在，如果存在就调用
         */</span>
        <span class="hljs-built_in">this</span>.onFulfilled && <span class="hljs-built_in">this</span>.onFulfilled(<span class="hljs-built_in">this</span>.value)
    &#125;

    reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = REJECTED

        <span class="hljs-built_in">this</span>.reason = reason

        <span class="hljs-comment">/**
         * 针对异步情况，判断失败回调是否存在，如果存在就调用
         */</span>
        <span class="hljs-built_in">this</span>.onRejected && <span class="hljs-built_in">this</span>.onRejected(<span class="hljs-built_in">this</span>.reason)
    &#125;

    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED) &#123;
            onFulfilled(<span class="hljs-built_in">this</span>.value)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
            onRejected(<span class="hljs-built_in">this</span>.reason)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">/**
             * 如果是 PENDDING 状态，表明此时是异步情况
             * 但我们还不知道将来是成功还是失败，所以把它们都先存储起来
             * */</span>
            <span class="hljs-built_in">this</span>.onFulfilled = onFulfilled
            <span class="hljs-built_in">this</span>.onRejected = onRejected
        &#125;
    &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = MyPromise
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">处理多个回调情况</h2>
<p><code>then</code> 方法会被调用多次，每次都会传入成功或失败的回调函数，这些回调都是要执行的，所以要改进一下，将这些函数存储到数组中，在 <code>resolve</code> 和 <code>reject</code> 中依次调用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDDING = <span class="hljs-string">'PENDDING'</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
        executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject)
    &#125;

    status = PENDDING

    value = <span class="hljs-literal">undefined</span>
    reason = <span class="hljs-literal">undefined</span>


    <span class="hljs-comment">// 改成用数组存储这些回调</span>
    <span class="hljs-comment">// onFulfilled = undefined</span>
    <span class="hljs-comment">// onRejected = undefined</span>
    onFulfilled = []
    onRejected = []

    resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = FULFILLED

        <span class="hljs-built_in">this</span>.value = value

        <span class="hljs-comment">// 由只调用一次，改为遍历数组，调用所有回调函数</span>
        <span class="hljs-comment">// this.onFulfilled && this.onFulfilled(this.value)</span>
        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onFulfilled.length) &#123;
            <span class="hljs-built_in">this</span>.onFulfilled.shift()(<span class="hljs-built_in">this</span>.value)
        &#125;

    &#125;

    reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = REJECTED

        <span class="hljs-built_in">this</span>.reason = reason

        <span class="hljs-comment">// 由只调用一次，改为遍历数组，调用所有回调函数</span>
        <span class="hljs-comment">// this.onRejected && this.onRejected(this.reason)</span>
        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onRejected.length) &#123;
            <span class="hljs-built_in">this</span>.onRejected.shift()(<span class="hljs-built_in">this</span>.reason)
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED) &#123;
            onFulfilled(<span class="hljs-built_in">this</span>.value)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
            onRejected(<span class="hljs-built_in">this</span>.reason)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 回调可能为多个，全都存储起来</span>
            <span class="hljs-comment">// this.onFulfilled = onFulfilled</span>
            <span class="hljs-comment">// this.onRejected = onRejected</span>
            <span class="hljs-built_in">this</span>.onFulfilled.push(onFulfilled)
            <span class="hljs-built_in">this</span>.onRejected.push(onRejected)
        &#125;
    &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = MyPromise
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">then 方法的链式调用</h2>
<ul>
<li><code>then</code> 方法可以链式调用，每次返回的都是 <code>Promise</code> 对象</li>
<li>上一个 <code>then</code> 的返回值，传递给当前 <code>then</code> 的回调函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDDING = <span class="hljs-string">'PENDDING'</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
        executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject)
    &#125;

    status = PENDDING

    value = <span class="hljs-literal">undefined</span>
    reason = <span class="hljs-literal">undefined</span>

    onFulfilled = []
    onRejected = []

    resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = FULFILLED

        <span class="hljs-built_in">this</span>.value = value

        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onFulfilled.length) &#123;
            <span class="hljs-built_in">this</span>.onFulfilled.shift()(<span class="hljs-built_in">this</span>.value)
        &#125;

    &#125;

    reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = REJECTED

        <span class="hljs-built_in">this</span>.reason = reason

        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onRejected.length) &#123;
            <span class="hljs-built_in">this</span>.onRejected.shift()(<span class="hljs-built_in">this</span>.reason)
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
        <span class="hljs-comment">/**
         * then 方法需要返回一个新的 Promise 实例，实现链式调用
         */</span>
        <span class="hljs-keyword">const</span> newPromise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED) &#123;
                <span class="hljs-comment">// 拿到当前 then 的成功回调函数返回值</span>
                <span class="hljs-keyword">let</span> current = onFulfilled(<span class="hljs-built_in">this</span>.value)

                <span class="hljs-comment">/**
                 * current 可能是 promise 或者普通值，针对不同情况要做不同处理，
                 * 如果是普通值，直接调用 resolve
                 * 如果是 promise，查看 promise 的返回结果，再决定调用 resolve 还是 reject 
                 * 我们把处理过程封装成一个函数，方便给 onRejected 同样使用，
                 * 同时还要对比一下 newPromise 和 current，防止他们是同一个 promise，也就是循环调用的问题
                 * */</span>
                resolvePromise(newPromise, current, resolve, reject)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
                <span class="hljs-keyword">let</span> current = onRejected(<span class="hljs-built_in">this</span>.reason)
                resolvePromise(current, resolve, reject)
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-built_in">this</span>.onFulfilled.push(onFulfilled)
                <span class="hljs-built_in">this</span>.onRejected.push(onRejected)
            &#125;
        &#125;)

        <span class="hljs-keyword">return</span> newPromise
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">newPromise, current, resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (current === newPromise) &#123;
        <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'不能循环调用'</span>))
    &#125;
    <span class="hljs-keyword">if</span> (current <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
        current.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
            resolve(value)
        &#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
            reject(reason)
        &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
        resolve(current)
    &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = MyPromise
<span class="copy-code-btn">复制代码</span></code></pre>
<p>细心的同学会发现，<code>newPromise</code> 是在 <code>new Promise</code> 执行完成之后返回的，我们在调用 <code>resolvePromise</code> 时传入的 <code>newPromise</code> 此时还没有获取到，所以我们通过 <code>setTimeout</code> 将其转换成异步代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;

    <span class="hljs-keyword">const</span> newPromise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED) &#123;
            <span class="hljs-comment">// 转为异步代码，是为了获取到 newPromise</span>
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">let</span> current = onFulfilled(<span class="hljs-built_in">this</span>.value)
                resolvePromise(newPromise, current, resolve, reject)
            &#125;, <span class="hljs-number">0</span>);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">let</span> current = onRejected(<span class="hljs-built_in">this</span>.reason)
                resolvePromise(current, resolve, reject)
            &#125;, <span class="hljs-number">0</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.onFulfilled.push(onFulfilled)
            <span class="hljs-built_in">this</span>.onRejected.push(onRejected)
        &#125;
    &#125;)

    <span class="hljs-keyword">return</span> newPromise
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">错误处理机制</h2>
<ul>
<li>如果执行器函数出错了，应该在 <code>constructor</code> 中捕获出来并抛出</li>
<li>如果 <code>onFulfilled</code> 或者 <code>onRejected</code> 出错了，也应该捕获并抛出</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDDING = <span class="hljs-string">'PENDDING'</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
        <span class="hljs-comment">// 捕获执行器函数的错误</span>
        <span class="hljs-keyword">try</span> &#123;
            executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject)
        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
            <span class="hljs-built_in">this</span>.reject(err)
        &#125;
    &#125;

    status = PENDDING

    value = <span class="hljs-literal">undefined</span>
    reason = <span class="hljs-literal">undefined</span>

    onFulfilled = []
    onRejected = []

    resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = FULFILLED

        <span class="hljs-built_in">this</span>.value = value

        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onFulfilled.length) &#123;
            <span class="hljs-comment">// 不需要传值了</span>
            <span class="hljs-comment">// this.onFulfilled.shift()(this.value)</span>
            <span class="hljs-built_in">this</span>.onFulfilled.shift()()
        &#125;

    &#125;

    reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = REJECTED

        <span class="hljs-built_in">this</span>.reason = reason

        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onRejected.length) &#123;
            <span class="hljs-comment">// 不需要传值了</span>
            <span class="hljs-comment">// this.onRejected.shift()(this.reason)</span>
            <span class="hljs-built_in">this</span>.onRejected.shift()()
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;

        <span class="hljs-keyword">const</span> newPromise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED) &#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-comment">// 捕获 onFulfilled 的错误</span>
                    <span class="hljs-keyword">try</span> &#123;
                        <span class="hljs-keyword">let</span> current = onFulfilled(<span class="hljs-built_in">this</span>.value)
                        resolvePromise(newPromise, current, resolve, reject)
                    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                        reject(err)
                    &#125;
                &#125;, <span class="hljs-number">0</span>);
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-comment">// 捕获 onRejected 的错误</span>
                    <span class="hljs-keyword">try</span> &#123;
                        <span class="hljs-keyword">let</span> current = onRejected(<span class="hljs-built_in">this</span>.reason)
                        resolvePromise(current, resolve, reject)
                    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                        reject(err)
                    &#125;
                &#125;, <span class="hljs-number">0</span>);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// 捕获 onFulfilled 和 onRejected 的错误</span>
                <span class="hljs-comment">// this.onFulfilled.push(onFulfilled)</span>
                <span class="hljs-comment">// this.onRejected.push(onRejected)</span>
                <span class="hljs-built_in">this</span>.onFulfilled.push(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                        <span class="hljs-comment">// 捕获 onFulfilled 的错误</span>
                        <span class="hljs-keyword">try</span> &#123;
                            <span class="hljs-keyword">let</span> current = onFulfilled(<span class="hljs-built_in">this</span>.value)
                            resolvePromise(newPromise, current, resolve, reject)
                        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                            reject(err)
                        &#125;
                    &#125;, <span class="hljs-number">0</span>);
                &#125;)
                <span class="hljs-built_in">this</span>.onRejected.push(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                        <span class="hljs-comment">// 捕获 onRejected 的错误</span>
                        <span class="hljs-keyword">try</span> &#123;
                            <span class="hljs-keyword">let</span> current = onRejected(<span class="hljs-built_in">this</span>.reason)
                            resolvePromise(current, resolve, reject)
                        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                            reject(err)
                        &#125;
                    &#125;, <span class="hljs-number">0</span>);
                &#125;)
            &#125;
        &#125;)

        <span class="hljs-keyword">return</span> newPromise
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">newPromise, current, resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (current === newPromise) &#123;
        <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'不能循环调用'</span>))
    &#125;
    <span class="hljs-keyword">if</span> (current <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
        current.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
            resolve(value)
        &#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
            reject(reason)
        &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
        resolve(current)
    &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = MyPromise
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">实现 Promise.all( )</h2>
<ul>
<li><code>Promise.all</code> 是静态方法，通过 <code>static</code> 声明</li>
<li>接收一个数组，每一项都是一个 <code>Promise</code> 实例或者普通值，遍历这个数组，当所有 <code>Promise</code> 执行完毕之后，再返回结果</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Promise.all 是静态方法，通过 static 声明</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">array</span>)</span> &#123;
    <span class="hljs-keyword">let</span> result = [];
    <span class="hljs-comment">//计数器</span>
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addData</span>(<span class="hljs-params">key, value</span>) </span>&#123;
            result[key] = value;
            index++;
            <span class="hljs-comment">/**
             * 因为 for 循环中会存在异步函数，当 for 循环执行完了，异步函数还没有返回结果，此时执行 resolve 会出错
             * 所以我们等循环完成之后再执行 resolve
             * */</span>
            <span class="hljs-keyword">if</span> (index === array.length) &#123;
                resolve(result);
            &#125;
        &#125;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < array.length; i++) &#123;
            <span class="hljs-keyword">let</span> data = array[i];
            <span class="hljs-keyword">if</span> (data <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
                <span class="hljs-comment">// data 是 promise 对象的情况</span>
                data.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> addData(i, value), <span class="hljs-function"><span class="hljs-params">reason</span> =></span> reject(reason))
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// data 是普通值的情况</span>
                addData(i, data)
            &#125;
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">实现 Promise.resolve( ) 和 Promise.reject( )</h2>
<p>这两个比较简单，直接撸！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        resolve(value)
    &#125;)
&#125;

<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        reject(err);
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 finally 的回调函数返回的是一个异步的 promise 对象</p>
<h2 data-id="heading-24">实现 catch</h2>
<p>如果我们调用 <code>then</code> 方法的时候，没有传递失败回调，那么错误最终会被 <code>catch</code> 捕获</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">catch</span> (onRejected) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, onRejected)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-25">完整的代码</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDDING = <span class="hljs-string">'PENDDING'</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject)
        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
            <span class="hljs-built_in">this</span>.reject(err)
        &#125;
    &#125;

    status = PENDDING

    value = <span class="hljs-literal">undefined</span>
    reason = <span class="hljs-literal">undefined</span>

    onFulfilled = []
    onRejected = []

    resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = FULFILLED

        <span class="hljs-built_in">this</span>.value = value

        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onFulfilled.length) &#123;
            <span class="hljs-built_in">this</span>.onFulfilled.shift()()
        &#125;

    &#125;

    reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PENDDING) <span class="hljs-keyword">return</span>

        <span class="hljs-built_in">this</span>.status = REJECTED

        <span class="hljs-built_in">this</span>.reason = reason

        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onRejected.length) &#123;
            <span class="hljs-built_in">this</span>.onRejected.shift()()
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;

        <span class="hljs-keyword">const</span> newPromise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED) &#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-keyword">try</span> &#123;
                        <span class="hljs-keyword">let</span> current = onFulfilled(<span class="hljs-built_in">this</span>.value)
                        resolvePromise(newPromise, current, resolve, reject)
                    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                        reject(err)
                    &#125;
                &#125;, <span class="hljs-number">0</span>);
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-keyword">try</span> &#123;
                        <span class="hljs-keyword">let</span> current = onRejected(<span class="hljs-built_in">this</span>.reason)
                        resolvePromise(current, resolve, reject)
                    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                        reject(err)
                    &#125;
                &#125;, <span class="hljs-number">0</span>);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-built_in">this</span>.onFulfilled.push(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                        <span class="hljs-keyword">try</span> &#123;
                            <span class="hljs-keyword">let</span> current = onFulfilled(<span class="hljs-built_in">this</span>.value)
                            resolvePromise(newPromise, current, resolve, reject)
                        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                            reject(err)
                        &#125;
                    &#125;, <span class="hljs-number">0</span>);
                &#125;)
                <span class="hljs-built_in">this</span>.onRejected.push(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                        <span class="hljs-keyword">try</span> &#123;
                            <span class="hljs-keyword">let</span> current = onRejected(<span class="hljs-built_in">this</span>.reason)
                            resolvePromise(current, resolve, reject)
                        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                            reject(err)
                        &#125;
                    &#125;, <span class="hljs-number">0</span>);
                &#125;)
            &#125;
        &#125;)

        <span class="hljs-keyword">return</span> newPromise
    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">array</span>)</span> &#123;
        <span class="hljs-keyword">let</span> result = [];
        <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addData</span>(<span class="hljs-params">key, value</span>) </span>&#123;
                result[key] = value;
                index++;
                <span class="hljs-keyword">if</span> (index === array.length) &#123;
                    resolve(result);
                &#125;
            &#125;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < array.length; i++) &#123;
                <span class="hljs-keyword">let</span> data = array[i];
                <span class="hljs-keyword">if</span> (data <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
                    data.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> addData(i, value), <span class="hljs-function"><span class="hljs-params">reason</span> =></span> reject(reason))
                &#125; <span class="hljs-keyword">else</span> &#123;
                    addData(i, data)
                &#125;
            &#125;
        &#125;)
    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            resolve(value)
        &#125;)
    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            reject(err);
        &#125;)
    &#125;

    <span class="hljs-keyword">catch</span> (onRejected) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, onRejected)
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">newPromise, current, resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (current === newPromise) &#123;
        <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'不能循环调用'</span>))
    &#125;
    <span class="hljs-keyword">if</span> (current <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
        current.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
            resolve(value)
        &#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
            reject(reason)
        &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
        resolve(current)
    &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = MyPromise
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-26">写在最后</h1>
<p>写到这里基本就差不多了，虽然代码中还存在可以优化的点，可以继续打磨，但通过这篇文章的整理，我对 <code>Promise</code> 又加深了一次印象，学习就是不断遗忘的过程，需要我们不断巩固加深记忆，加油伙伴们！</p>
<h1 data-id="heading-27">参考资料</h1>
<ul>
<li><a href="https://github.com/ljianshu/Blog/issues/81" target="_blank" rel="nofollow noopener noreferrer">你真的懂Promise吗</a></li>
<li><a href="https://juejin.cn/post/6939688892526231582#heading-20" target="_blank">Promise从入门到手写 | [Promise系列一]</a></li>
</ul></div>  
</div>
            