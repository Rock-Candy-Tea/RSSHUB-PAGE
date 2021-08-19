
---
title: '「硬核JS」图解Promise迷惑行为｜运行机制补充'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9ae985151a24f9fa8824e032c5a02b3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 18:52:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9ae985151a24f9fa8824e032c5a02b3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">写在前面</h2>
<p>Promise用起来很简单，JavaScript运行机制也不难，但是运行机制和 Promise 挂钩之后，往往就能把人迷的晕头转向，如果你也是如此，那此文或许能帮你解惑。</p>
<p>前些天有几个小伙伴看了我很早之前写的 <a href="https://juejin.cn/post/6844904050543034376" target="_blank" title="https://juejin.cn/post/6844904050543034376">「硬核JS」一次搞懂JS运行机制</a> 后私信给我提出了疑问，说是运行机制是懂了，可是涉及到 Promise 的种种迷惑行为（各种嵌套输出、链式 <code>then</code> 等等）还是不太懂。其实那篇文章的核心本来就只是运行机制的概念，而对于 Promise 迷惑行为拿捏不准的小伙伴是因为对 Promise 的整体实现机制不太了解导致的。</p>
<p>假如你不知道自己对这块是否了解，可以直接跳到最后几个小标题，看一看这些题型自己能否正确解答即可。</p>
<p>此文应读者要求，算是对 Promise+运行机制的一个梳理与补充，重要的是实战方面，列了几种常见的 Promise 相关求输出顺序的题型，几乎涵盖所有 Promise 难搞题型了，总之，目的只有一个：彻底搞明白 Promise+运行机制的各种迷惑行为。</p>
<h2 data-id="heading-1">JS运行机制简述</h2>
<p>在开始之前，还是有必要简单介绍下 JS 的运行机制。</p>
<p>JavaScript 中有同步/异步任务的概念，同步任务在主线程上执行，会形成一个 <code>执行栈</code>，主线程之外，事件触发线程管理着一个 <code>任务队列</code>，只要异步任务有了运行结果，就在 <code>任务队列</code> 之中放一个事件回调。一旦 <code>执行栈</code> 中的所有同步任务执行完毕，就会读取 <code>任务队列</code>，将可运行的异步任务（任务队列中的事件回调，只要任务队列中有事件回调，就说明可以执行）添加到执行栈中，开始执行。</p>
<p>同步/异步任务是广义上的，同时，JavaScript 中还有宏任务（macrotask）和微任务（microtask）这种更加细致的概念，我们可以将每次执行栈执行的代码当做是一个宏任务（包括每次从事件队列中获取一个事件回调并放到执行栈中执行）， 每一个宏任务会从头到尾执行完毕，不会执行其他。而在异步任务中，有些特殊的任务我们称之为微任务，它在当前宏任务执行后立即执行。</p>
<p>比较常见的微任务有这些：</p>
<ul>
<li>process.nextTick-Node</li>
<li>Promise.then</li>
<li>catch</li>
<li>finally</li>
<li>Object.observe</li>
<li>MutationObserver</li>
<li>queueMicrotask</li>
<li>...</li>
</ul>
<p>简单来说，一段完整的 JS 代码，浏览器会将整体的 script（作为第一个宏任务）开始执行，所有代码分为<code>同步任务</code>、<code>异步任务</code>两部分：</p>
<ol>
<li>同步任务直接进入主线程执行栈依次执行，异步任务会再分为普通异步任务（也是宏任务），和特殊异步任务（即微任务）；</li>
<li>普通的异步任务等有了运行结果其回调就会进入事件触发线程管理的 <code>任务队列</code>（可理解为宏任务队列）；</li>
<li>特殊的异步任务也就是微任务的回调会立即进入一个微任务队列；</li>
<li>当主线程内的任务执行完毕，即主线程为空时，会检查微任务队列，如果有任务，就全部执行，如果没有就执行下一个宏任务（事件触发线程管理的 <code>任务队列</code> 中）；</li>
</ol>
<p>上述过程会不断重复，这就是Event Loop，事件循环。</p>
<p>浏览器中加上渲染的话就是先执行一个宏任务，再执行当前所有的微任务，接着开始执行渲染，然后再执行下一个宏任务，如此循环。</p>
<blockquote>
<p>简单回顾，详细请看 👉 <a href="https://juejin.cn/post/6844904050543034376" target="_blank" title="https://juejin.cn/post/6844904050543034376">「硬核JS」一次搞懂JS运行机制</a></p>
</blockquote>
<h2 data-id="heading-2">Promise手写实现</h2>
<p>由于后面涉及到了一些 Promise 内部的运行机制，所以，这部分手写 Promise 请耐心看完，不多，只有核心部分，也很简单，看看思路即可。</p>
<h3 data-id="heading-3">Promises/A+</h3>
<p>Promises/A+标准是一个开放、健全且通用的 JavaScript Promise 标准，由开发者制定，供开发者参考。很多 Promise 三方库都是按照 Promises/A+标准实现的。</p>
<p>so，此次实现我们严格参照 Promises/A+标准，包括完成后我们会使用开源社区提供的测试包来测试。测试通过的话，足以证明代码符合 Promises/A+标准，是合法的、完全可以上线提供给他人使用的。</p>
<h3 data-id="heading-4">构造方法核心基础搭建</h3>
<ul>
<li>Promise 有三种状态进行中（Pending）、已完成（Resolved/Fulfilled）和已失败 （Rejected）。</li>
<li>Promise 是一个构造方法，实例化 Promise 时传入一个函数作为处理器。
<ul>
<li>处理器函数有两个参数（resolve 和 reject）分别将结果变为成功态和失败态。</li>
<li>Promise 对象执行成功了要有一个结果，通过 resolve 传递出去，失败的话失败原因通过 reject 传递出入。</li>
</ul>
</li>
<li>Promise 的原型上定义着 then 方法。</li>
</ul>
<p>那么根据我们上面的这些已知需求我们可以写出一个基础的结构（写法千千万，喜欢 class 也可以用 class）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-comment">// 状态描述 pending resolved rejected</span>
  <span class="hljs-built_in">this</span>.state = <span class="hljs-string">"pending"</span>
  <span class="hljs-comment">// 成功结果</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>
  <span class="hljs-comment">// 失败原因</span>
  <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>) </span>&#123;&#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>) </span>&#123;&#125;
&#125;

<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onFulfilled, onRejected</span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，我们创建了一个 Promise 构造方法，<code>state</code> 属性保存了 Promise 对象的状态，使用 <code>value</code> 属性保存 Promise 对象执行成功的结果，失败原因使用 <code>reason</code> 属性保存，这些命名完全贴合 Promises/A+标准。</p>
<p>接着我们在构造函数中创建了 <code>resolve</code> 和 <code>reject</code> 两个方法，然后在构造函数的原型上创建了一个 <code>then</code> 方法，以备待用。</p>
<h3 data-id="heading-5">初始化实例 executor 立即执行</h3>
<p>我们知道，在创建一个 Promise 实例时，处理器函数 <code>executor</code> 是会立即执行的，所以我们更改代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.state = <span class="hljs-string">"pending"</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>
  <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>

  <span class="hljs-comment">// 让其处理器函数立即执行</span>
  <span class="hljs-keyword">try</span> &#123;
    executor(resolve, reject)
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    reject(err)
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>) </span>&#123;&#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>) </span>&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">resolve&reject 回调实现</h3>
<p>Promises/A+ 规范中规定，当 Promise 对象已经由 pending 状态改变为成功态 <code>resolved</code> 或失败态 <code>rejected</code> 后不可再次更改状态，也就是说成功或失败后状态不可更新已经凝固。</p>
<p>因此我们更新状态时要判断，如果当前状态是等待态 <code>pending</code> 才可更新，由此我们来完善 <code>resolve</code> 和 <code>reject</code> 方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (_this.state === <span class="hljs-string">"pending"</span>) &#123;
    _this.value = value
    _this.state = <span class="hljs-string">"resolved"</span>
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (_this.state === <span class="hljs-string">"pending"</span>) &#123;
    _this.reason = reason
    _this.state = <span class="hljs-string">"rejected"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，首先我们在 Promise 构造函数内部用变量 <code>_this</code> 托管构造函数的 <code>this</code>。</p>
<p>接着我们在 <code>resolve</code> 和 <code>reject</code> 函数中分别加入了判断，因为只有当前态是 pending 才可进行状态更改操作。</p>
<p>同时将成功结果和失败原因都保存到对应的属性上。</p>
<p>然后将 state 属性置为更新后的状态。</p>
<h3 data-id="heading-7">then 方法基础实现</h3>
<p>接着我们来简单实现 <code>then</code> 方法。</p>
<p>首先 <code>then</code> 方法有两个回调，当 Promise 的状态发生改变，成功或失败会分别调用 <code>then</code> 方法的两个回调。</p>
<p>所以，then 方法的实现看起来挺简单，根据 state 状态来调用不同的回调函数即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onFulfilled, onRejected</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"resolved"</span>) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">"function"</span>) &#123;
      onFulfilled(<span class="hljs-built_in">this</span>.value)
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"rejected"</span>) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">"function"</span>) &#123;
      onRejected(<span class="hljs-built_in">this</span>.reason)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，由于 <code>onFulfilled & onRejected</code> 两个参数都不是必选参，所以我们在判断状态后又判断了参数类型，当参数不为函数类型，就不执行，因为在 Promises/A+规范中定义非函数类型可忽略。</p>
<h3 data-id="heading-8">让 Promise 支持异步</h3>
<p>写到这里，你可能会觉得，咦？Promise 实现起来也不难嘛，这么快就有模有样了，我们来简单测试下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  resolve(<span class="hljs-number">1</span>)
&#125;)

p.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> <span class="hljs-built_in">console</span>.log(data)) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嗯，符合预期，再来试下异步代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">1</span>);
  &#125;，<span class="hljs-number">1000</span>);
&#125;)

p.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> <span class="hljs-built_in">console</span>.log(data)) <span class="hljs-comment">// 无输出</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题来了，Promise 一个异步解决方案被我们写的不支持异步。本来是等 1000ms 后执行<code>then</code>方法，运行上面代码发现没有结果，哪里有问题呢？</p>
<p>setTimeout 函数让<code>resolve</code>变成了异步执行，有延迟，调用<code>then</code>方法的时候，此刻状态还是等待态 <code>pending</code>，<code>then</code>方法即没有调用<code>onFulfilled</code>也没有调用<code>onRejected</code>。</p>
<p>原因搞清楚了，我们开始改造。我们可以在执行<code>then</code>方法时如果还在等待态 <code>pending</code>，就把回调函数临时寄存到队列（就是一个数组）里，当状态发生改变时依次从数组中取出执行就好了。</p>
<p>思路有了，我们来实现下：</p>
<p>首先，我们要在构造方法中新增两个 Array 类型的数组，用于存放成功和失败的回调函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>
  <span class="hljs-built_in">this</span>.state = <span class="hljs-string">"pending"</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>
  <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>
  <span class="hljs-comment">// 保存成功回调</span>
  <span class="hljs-built_in">this</span>.onResolvedCallbacks = []
  <span class="hljs-comment">// 保存失败回调</span>
  <span class="hljs-built_in">this</span>.onRejectedCallbacks = []
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还需要改善<code>then</code>方法，在<code>then</code>方法执行时如果状态是等待态，就将其回调函数存入对应数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onFulfilled, onRejected</span>) </span>&#123;
  <span class="hljs-comment">// 新增等待态判断，此时异步代码还未走完，回调入数组队列</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"pending"</span>) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(onFulfilled)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(onRejected)
    &#125;
  &#125;

  <span class="hljs-comment">// 以下为之前代码块</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"resolved"</span>) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">"function"</span>) &#123;
      onFulfilled(<span class="hljs-built_in">this</span>.value)
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"rejected"</span>) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">"function"</span>) &#123;
      onRejected(<span class="hljs-built_in">this</span>.reason)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，我们改写<code>then</code>方法，除了判断成功态 <code>resolved</code>、失败态 <code>rejected</code>，我们又加了一个等待态 <code>pending</code> 判断，当状态为等待态时，异步代码还没有走完，那么我们把对应的回调先存入准备好的数组中即可。</p>
<p>现在，就差最后一步执行了，我们在 <code>resolve</code> 和 <code>reject</code> 方法中调用即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (_this.state === <span class="hljs-string">"pending"</span>) &#123;
    _this.value = value
    <span class="hljs-comment">// 遍历执行成功回调</span>
    _this.onResolvedCallbacks.forEach(<span class="hljs-function">(<span class="hljs-params">cb</span>) =></span> cb(value))
    _this.state = <span class="hljs-string">"resolved"</span>
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (_this.state === <span class="hljs-string">"pending"</span>) &#123;
    _this.reason = reason
    <span class="hljs-comment">// 遍历执行失败回调</span>
    _this.onRejectedCallbacks.forEach(<span class="hljs-function">(<span class="hljs-params">cb</span>) =></span> cb(reason))
    _this.state = <span class="hljs-string">"rejected"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到了这里，我们已经完成了 Promise 的异步支持。</p>
<h3 data-id="heading-9">实现 Promise 经典的链式调用</h3>
<p>Promise 的<code>then</code>方法可以链式调用，这也是 Promise 的精华之一，在实现起来也算是比较复杂的地方了。</p>
<p>首先我们要理清楚<code>then</code>的需求是什么，这需要仔细看 Promises/A+ 规范中对<code>then</code>方法的返回值定义及 Promise 解决过程，如下：</p>
<ul>
<li>
<p><strong>首先<code>then</code> 方法必须返回一个 <code>promise</code> 对象(划重点)</strong></p>
</li>
<li>
<p><strong>如果<code>then</code>方法中返回的是一个普通值(如 Number、String 等)就使用此值包装成一个新的 Promise 对象返回</strong></p>
</li>
<li>
<p><strong>如果<code>then</code>方法中没有<code>return</code>语句，就返回一个用 Undefined 包装的 Promise 对象</strong></p>
</li>
<li>
<p><strong>如果<code>then</code>方法中出现异常，则调用失败态方法(reject)跳转到下一个<code>then</code>的 onRejected</strong></p>
</li>
<li>
<p><strong>如果<code>then</code>方法没有传入任何回调，则继续向下传递(值穿透)</strong></p>
</li>
<li>
<p><strong>如果<code>then</code>方法中返回了一个 Promise 对象，那就以这个对象为准，返回它的结果</strong></p>
</li>
</ul>
<p>嗯，到此我们需求已经明确，开始代码实现。</p>
<p>需求中说如果<code>then</code>方法没有传入任何回调，则继续向下传递，但是每个<code>then</code>中又返回一个新的 Promise，也就是说当<code>then</code>方法中没有回调时，我们需要把接收到的值继续向下传递，这个其实好办，只需要在判断回调参数不为函数时我们把他变成回调函数返回普通值即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onFulfilled, onRejected</span>) </span>&#123;
  onFulfilled =
    <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">"function"</span> ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value
  onRejected =
    <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">"function"</span>
      ? onRejected
      : <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          <span class="hljs-keyword">throw</span> err
        &#125;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们上面<code>then</code>实现中，在每个可执行处都加了参数是否为函数的类型校验，但是我们这里在<code>then</code>方法开头统一做了校验，就不需要参数校验了。</p>
<p>现在的<code>then</code>方法变成了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onFulfilled, onRejected</span>) </span>&#123;
  onFulfilled =
    <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">"function"</span> ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value
  onRejected =
    <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">"function"</span>
      ? onRejected
      : <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          <span class="hljs-keyword">throw</span> err
        &#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"pending"</span>) &#123;
    <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(onFulfilled)
    <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(onRejected)
  &#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"resolved"</span>) &#123;
    onFulfilled(<span class="hljs-built_in">this</span>.value)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"rejected"</span>) &#123;
    onRejected(<span class="hljs-built_in">this</span>.reason)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然每个<code>thne</code>都返回一个新的 Promise，那么我们就先在<code>then</code>中创建一个 Promise 实例返回，开始改造。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onFulfilled, onRejected</span>) </span>&#123;
  onFulfilled =
    <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">"function"</span> ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value
  onRejected =
    <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">"function"</span>
      ? onRejected
      : <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          <span class="hljs-keyword">throw</span> err
        &#125;

  <span class="hljs-keyword">let</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"pending"</span>) &#123;
      <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(onFulfilled)
      <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(onRejected)
    &#125;

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"resolved"</span>) &#123;
      onFulfilled(<span class="hljs-built_in">this</span>.value)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"rejected"</span>) &#123;
      onRejected(<span class="hljs-built_in">this</span>.reason)
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> promise2
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在<code>then</code>方法中先实例化了一个 Promise 对象并返回，我们把原来写的代码放到该实例的处理器函数中。</p>
<p>我们把原来写的代码放到该实例的处理器函数中。</p>
<p>接着在每个执行函数处使用<code>try..catch</code>语法，try 中<code>resolve</code>执行结果，catch 中<code>reject</code>异常，原来的<code>then</code>方法中有 resolved、rejected 和 pending 三种逻辑判断，如下：</p>
<p>在 resolved 状态判断时，rejected 和 resolved 逻辑一致。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"resolved"</span>) &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 拿到返回值resolve出去</span>
    <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value)
    resolve(x)
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-comment">// catch捕获异常reject抛出</span>
    reject(e)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>pending 状态判断，逻辑也和 resolved 相似，但是由于此处为了处理异步，我们在这里做了 push 操作，所以我们 push 时在 onFulfilled 和 onRejected 回调外面再套一个回调做操作即可，都是 JS 惯用小套路，不过分解释。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"pending"</span>) &#123;
  <span class="hljs-comment">// push(onFulfilled)</span>
  <span class="hljs-comment">// push(()=>&#123; onFulfilled() &#125;)</span>
  <span class="hljs-comment">// 上面两种执行效果一致，后者可在回调中加一些其他功能，如下</span>
  <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value)
      resolve(x)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      reject(e)
    &#125;
  &#125;)
  <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.value)
      resolve(x)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      reject(e)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再接下来我们开始处理根据上一个<code>then</code>方法的返回值来生成新 Promise 对象，这块逻辑复杂些，规范中可以抽离出一个方法来做这件事，我们来照做。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 解析then返回值与新Promise对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>新的Promise对象，就是我们创建的promise2实例
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>x 上一个then的返回值
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Function&#125;</span> </span>resolve promise2处理器函数的resolve
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Function&#125;</span> </span>reject promise2处理器函数的reject
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise2, x, resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来一步步分析完善 resolvePromise 函数。</p>
<p><strong>避免循环引用，当 then 的返回值与新生成的 Promise 对象为同一个(引用地址相同)，则抛出 TypeError 错误：</strong></p>
<p>例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> promise2 = p.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> promise2
&#125;)

<span class="hljs-comment">// TypeError: Chaining cycle detected for promise #<Promise></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果返回了自己的 Promise 对象，状态永远为等待态(pending)，再也无法成为 resolved 或是 rejected，程序就死掉了，因此要先处理它。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise2, x, resolve, reject</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (promise2 === x) &#123;
    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"请避免Promise循环引用"</span>))
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>判断 x 类型，分情况处理：</strong></p>
<p>当 x 是一个 Promise，就执行它，成功即成功，失败即失败，如果<code>x</code>是一个对象或是函数，再进一步处理它，否则就是一个普通值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise2, x, resolve, reject</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (promise2 === x) &#123;
    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"请避免Promise循环引用"</span>))
  &#125;

  <span class="hljs-keyword">if</span> (x !== <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"object"</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"function"</span>)) &#123;
    <span class="hljs-comment">// 可能是个对象或是函数</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 是个普通值</span>
    resolve(x)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 x 是个对象，尝试将对象上的 then 方法取出来，此时如果报错，那就将 promise2 转为失败态。</p>
<p>在这里 catch 防止报错是因为 Promise 有很多实现，假设另一个人实现的 Promise 对象使用<code>Object.defineProperty()</code>在取值时抛错，我们可以防止代码出现 bug。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// resolvePromise方法内部片段</span>

<span class="hljs-keyword">if</span> (x !== <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"object"</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"function"</span>)) &#123;
  <span class="hljs-comment">// 可能是个对象或是函数</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 尝试取出then方法引用</span>
    <span class="hljs-keyword">let</span> then = x.then
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    reject(e)
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 是个普通值</span>
  resolve(x)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果对象中有<code>then</code>，且<code>then</code>是函数类型，就可以认为是一个 Promise 对象，之后，使用<code>x</code>作为其 this 来调用执行<code>then</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// resolvePromise方法内部片段</span>

<span class="hljs-keyword">if</span> (x !== <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"object"</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"function"</span>)) &#123;
  <span class="hljs-comment">// 可能是个对象或是函数</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 尝试取出then方法引用</span>
    <span class="hljs-keyword">let</span> then = x.then
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-comment">// then是function，那么执行Promise</span>
      then.call(
        x,
        <span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
          resolve(y)
        &#125;,
        <span class="hljs-function">(<span class="hljs-params">r</span>) =></span> &#123;
          reject(r)
        &#125;
      )
    &#125; <span class="hljs-keyword">else</span> &#123;
      resolve(x)
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    reject(e)
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 是个普通值</span>
  resolve(x)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，我们还要考虑到一种情况，如果 Promise 对象转为成功态或是失败时传入的还是一个 Promise 对象，此时应该继续执行，直到最后的 Promise 执行完，例如下面这种：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// resolve传入的还是Promise</span>
    resolve(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        resolve(<span class="hljs-number">2</span>)
      &#125;)
    )
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决这种情况，我们可以采用递归，把调用 resolve 改写成递归执行 resolvePromise，这样直到解析 Promise 成一个普通值才会终止。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// resolvePromise方法内部片段</span>
<span class="hljs-keyword">if</span> (x !== <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"object"</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"function"</span>)) &#123;
  <span class="hljs-comment">// 可能是个对象或是函数</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">let</span> then = x.then
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">"function"</span>) &#123;
      then.call(
        x,
        <span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
          <span class="hljs-comment">// 递归调用，传入y若是Promise对象，继续循环</span>
          resolvePromise(promise2, y, resolve, reject)
        &#125;,
        <span class="hljs-function">(<span class="hljs-params">r</span>) =></span> &#123;
          reject(r)
        &#125;
      )
    &#125; <span class="hljs-keyword">else</span> &#123;
      resolve(x)
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    reject(e)
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 普通值结束递归</span>
  resolve(x)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>规范中定义，如果 resolvePromise 和 rejectPromise 都被调用，或者多次调用同一个参数，第一个调用优先，任何进一步的调用都将被忽略，为了让成功和失败只能调用一个，我们接着完善，设定一个 called 来防止多次调用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// resolvePromise方法内部片段</span>
<span class="hljs-keyword">let</span> called
<span class="hljs-keyword">if</span> (x !== <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"object"</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"function"</span>)) &#123;
  <span class="hljs-comment">// 可能是个对象或是函数</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">let</span> then = x.then
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">"function"</span>) &#123;
      then.call(
        x,
        <span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>
          called = <span class="hljs-literal">true</span>
          <span class="hljs-comment">// 递归调用，传入y若是Promise对象，继续循环</span>
          resolvePromise(promise2, y, resolve, reject)
        &#125;,
        <span class="hljs-function">(<span class="hljs-params">r</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>
          called = <span class="hljs-literal">true</span>
          reject(r)
        &#125;
      )
    &#125; <span class="hljs-keyword">else</span> &#123;
      resolve(x)
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>
    called = <span class="hljs-literal">true</span>
    reject(e)
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 普通值结束递归</span>
  resolve(x)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此，我们算是实现好了<code>resolvePromise</code>方法，我们来调用它实现完整的<code>then</code>方法，在原来的原型方法<code>then</code>中我们<code>return</code>了一个 promise2，这个实例处理器函数的三种状态判断中把<code>resolve</code>处替换成<code>resolvePromise</code>方法即可。</p>
<p>那么，此时<code>then</code>方法实现完成了吗？</p>
<p>当然还没有，我们都知道，Promise 中处理器函数是同步执行，而<code>then</code>方法是异步且是个微任务，但是我们完成这个还是同步。</p>
<p>解决这个问题其实也很简单，我们可以使用 <code>queueMicrotask</code> 方法实现一个微任务，在<code>then</code>方法内执行处的所有地方使用 <code>queueMicrotask</code> 变为微任务即可，<code>queueMicrotask</code> API有兼容性问题，大多数 Promise 库中此处的实现是递进的策略，简单说就是有好几种微任务实现方案，依次向下，如果都不兼容的话最后使用 <code>setTimeout</code>，如下：</p>
<pre><code class="hljs language-js copyable" lang="js">queueMicrotask(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">let</span> x = onFulfilled(value)
    resolvePromise(promise2, x, resolve, reject)
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    reject(e)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们的终极版<code>then</code>方法就大功告成了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onFulfilled, onRejected</span>) </span>&#123;
  onFulfilled =
    <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">"function"</span> ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value
  onRejected =
    <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">"function"</span>
      ? onRejected
      : <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          <span class="hljs-keyword">throw</span> err
        &#125;

  <span class="hljs-keyword">let</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// 等待态判断，此时异步代码还未走完，回调入数组队列</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"pending"</span>) &#123;
      <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">() =></span> &#123;
        queueMicrotask(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value)
            resolvePromise(promise2, x, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
      &#125;)

      <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
        queueMicrotask(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.value)
            resolvePromise(promise2, x, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
      &#125;)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"resolved"</span>) &#123;
      queueMicrotask(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value)
          resolvePromise(promise2, x, resolve, reject)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          reject(e)
        &#125;
      &#125;)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">"rejected"</span>) &#123;
      queueMicrotask(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason)
          resolvePromise(promise2, x, resolve, reject)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          reject(e)
        &#125;
      &#125;)
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> promise2
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">catch 实现</h3>
<p>实现了最复杂的<code>then</code>方法后，<code>catch</code>实现非常简单，一看就懂了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.catch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onRejected</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, onRejected)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">代码测试</h3>
<p>开源社区提供了一个包用于测试我们的代码是否符合 Promises/A+规范：<code>promises-aplus-tests</code>。</p>
<p>首先我们要为该测试包提供一个 <code>deferred</code> 钩子，用于测试。</p>
<p>如下，将下面代码防止我们的 <code>Promise.js</code> 文件末尾即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// promises-aplus-tests测试</span>
<span class="hljs-built_in">Promise</span>.defer = <span class="hljs-built_in">Promise</span>.deferred = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> defer = &#123;&#125;
  defer.promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    defer.resolve = resolve
    defer.reject = reject
  &#125;)
  <span class="hljs-keyword">return</span> defer
&#125;
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">Promise</span>
&#125; <span class="hljs-keyword">catch</span> (e) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，安装这个包：</p>
<pre><code class="hljs language-js copyable" lang="js">npm install promises-aplus-tests -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行测试：</p>
<pre><code class="hljs language-js copyable" lang="js">npx promises-aplus-tests <span class="hljs-built_in">Promise</span>.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>静等片刻，如果控制台没有爆红就是成功了，符合规范，如图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9ae985151a24f9fa8824e032c5a02b3~tplv-k3u1fbpfcp-watermark.image" alt="image-20200206222942803" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其他的 resolve/reject/race/all 等比较简单，不在这里描述了。</p>
<p>给大家贴个我这边 Promise 多个方法实现的地址，大家有兴趣自行看代码吧，注释写的很详细了，也就大概 200 多行代码。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fisboyjc%2Fpromise" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/isboyjc/promise" ref="nofollow noopener noreferrer">Promise/A+实现</a></li>
</ul>
<p>其实，这块儿的 Promise 的手写实现是在很久之前的 <a href="https://juejin.cn/post/6844904064614924302" target="_blank" title="https://juejin.cn/post/6844904064614924302">「硬核JS」深入了解异步解决方案</a> 一文的 Promise 章节写的，但是搞懂此文需要这块，我就 Copy 了一下稍作修改，跑了一下测试还能过证明还不算过时。</p>
<p>注意一定要先搞懂手写实现的逻辑哦，不然下面不好懂，那接下来开始进入正文。</p>
<h2 data-id="heading-12">手写后的启发</h2>
<p>Promise 核心实现我们上面已经介绍过了，从上面代码中我们得到了什么启发？</p>
<p>哦，原来 then 方法返回的是一个全新的 Promise 对象。</p>
<p>哦，原来 then 方法是一个微任务这种说法是不准确的，应该说 then 方法的回调函数会被作为微任务执行。</p>
<p>哦，原来 then 方法并不是在上一个 Promise 对象 resolve 后才执行，它在一开始就执行并返回了一个新的 Promise，在返回的新 Promise 中会根据上一个 Promise 的状态来做判断。</p>
<ul>
<li>
<p>上一个 Promise 在成功态 <code>Fulfilled</code> 的时候会直接将 then 方法回调作为微任务入队</p>
</li>
<li>
<p>上一个 Promise 在失败态 <code>Rejected</code> 时候会直接将 then 方法回调作为微任务入队</p>
</li>
<li>
<p>上一个 Promise 还在等待态 <code>pending</code> 的时候它的内部会把 then 方法回调使用微任务方法包裹缓存到新 Promise 实例数组中，并没有直接入队。当上一个 Promise 从等待态变为成功态的时候会调用其自身返回的新 Promise 的 resolve 方法，从而调用新 Promise（也就是返回的那个新 Promise）实例数组中的方法，这时微任务方法包裹的回调函数就会执行，即入栈。</p>
</li>
</ul>
<p>哦，原来上一个 Promise 中 return 一个 Promise 和直接 return 一个值或不写的处理方式是不一样的</p>
<ul>
<li>上一个 Promise 中什么都 return 即其回调的返回值为 undefined，和直接 return 一个值一样，都会在上一个 Promise 状态为成功态时调用其返回时内部创建的新 Promise 的 resolve 方法并将值传出。</li>
<li>上一个 Promise 中 return 一个 Promise 的话会在上一个 Promise 状态为成功态时，<strong>调用其 then 方法执行</strong>，拿到值 resolve 或 reject 出去（注意，由于 return Promise 时回在内部执行一个 then 方法，所以这里多执行了一个微任务，但是这个微任务其实什么都没做，只是为了取我们自己 return 的 Promise 的值）</li>
</ul>
<p>绕晕了？没关系，概念还是概念，我们用案例说话。</p>
<h2 data-id="heading-13">多个Promise执行</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>)=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  resolve();
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
&#125;).then(<span class="hljs-function">() =></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;);

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">20</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">30</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">40</span>);
&#125;);

<span class="hljs-comment">// 1 2 10 3 20 30 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这题相对简单，目的是为了让大家先熟悉一下解题套路，过一遍整体流程，方面后面能够看懂。</p>
<p>首先，我们为整道题做一个拆分命名，方便后续讲解：</p>
<ul>
<li>整个程序有两个 Promise，我们记作 <code>P1、P2</code>。</li>
<li>P1中 Promise 传入的回调我们记作 <code>P1-主</code>，还有两个 then 方法我们记作 <code>P1-t1、P1-t2</code>。</li>
<li>P2中直接使用 Promise 构造函数中的 resolve 方法创建了一个成功态的实例，后面有 4 个 then 方法，我们记作 <code>P2-t1、P2-t2、P2-t3、P2-t4</code>。</li>
</ul>
<p>分析一下，整个程序会作为一个宏任务第一批执行，而 then 方法中的回调最终会被作为微任务入微任务队列，等待宏任务执行结束后依次执行，在宏任务执行过程中部分 then 方法回调在上一个 Promise 状态为 <code>pending</code> 时会被微任务方法包裹先存入各自 Promise 实例中缓存起来等待后续执行。</p>
<p>被微任务方法包裹这个描述大概意思就是下面这样子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 缓存数组</span>
<span class="hljs-keyword">let</span> arr = []

<span class="hljs-comment">// 微任务方法包裹的回调存入缓存</span>
arr.push(<span class="hljs-function">() =></span> &#123;
  queueMicrotask(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 需要作为微任务执行的代码</span>
    <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value)
    resolvePromise(promise2, x, resolve, reject)
    
    <span class="hljs-comment">// ...</span>
  &#125;)
&#125;)

<span class="hljs-comment">// 只有arr[0]这个函数执行的时候，微任务才会入队</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时，我们脑子里就形成了一个空白的结构图，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/289bfdd91ba64bb8a4198b97226bc13a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开始执行代码，首先执行第一个宏任务，即程序整体：</p>
<ul>
<li>因为 <code>new Promise</code> 时参数回调是同步执行，所以执行 <code>P1-主</code> 回调，输出 1，接着执行 <code>resolve</code> ，将 <code>new</code> 的 Promise 实例变为成功态 <code>Fulfilled</code> 。</li>
<li><code>P1-t1</code> 的 then 方法开始执行，由于上一个 Promise 为成功态，所以 <code>P1-t1</code> 回调直接入微任务对列等待执行。</li>
<li><code>P1-t2</code> 的 then 方法开始执行，由于 <code>P1-t1</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P1-t2</code> 回调使用微任务方法包裹缓存进 Promise 实例（注意：这里的 Promise 实例为 <code>P1-t1</code> 返回的新 Promise，所以我们在各实例缓存列表中以 <code>P1-t1返</code> 开头注明存在哪个 Promise 实例中）。</li>
<li>P1 执行完毕，开始执行 P2。</li>
<li>P2 中直接使用 Promise 构造函数中的 resolve 方法创建了一个成功态的实例，<code>P2-t1</code> 的 then 方法执行时，由于是成功态 <code>Fulfilled</code>，所以 <code>P2-t1</code> 直接作为微任务入队等待执行。</li>
<li>接着 <code>P2-t2</code> 的 then 方法开始执行，由于 <code>P2-t1</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t2</code> 回调使用微任务方法包裹缓存进 <code>P2-t1返</code> 这个 Promise 实例中。</li>
<li>接着 <code>P2-t3</code> 的 then 方法开始执行，由于 <code>P2-t2</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t3</code> 回调使用微任务方法包裹缓存进 <code>P2-t2返</code> 这个 Promise 实例中。</li>
<li>接着 <code>P2-t4</code> 的 then 方法开始执行，由于 <code>P2-t3</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t4</code> 回调使用微任务方法包裹缓存进 <code>P2-t3返</code> 这个 Promise 实例中。</li>
</ul>
<p>执行到这里，主程序这个宏任务结束，目前程序运行状态如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5653e0ea7fb14901bf81cb32d383e6bc~tplv-k3u1fbpfcp-watermark.image" alt="image-20210810192049256" loading="lazy" referrerpolicy="no-referrer"></p>
<p>宏任务执行完了，那接下来就是依次执行微任务队列中的任务了</p>
<ul>
<li>按照顺序，首先是 <code>P1-t1</code> 执行，输出 2，返回值是 <code>undefined</code> ，这时会调用 <code>P1-t1</code>  这个 then 方法中返回的新 Promise 实例的 resolve 方法并将返回值 <code>undefined</code> 传入，resolve方法执行后即 <code>P1-t1返</code> 实例状态更改为成功态 <code>Fulfilled</code> ，并执行 <code>P1-t1返</code> 实例的缓存方法。</li>
<li><code>P1-t1返</code> 实例的缓存中只有微任务方法包裹的 <code>P1-t2</code> 回调，执行后即 <code>P1-t2</code> 入微任务队列等待执行，到此微任务 <code>P1-t1</code> 执行结束，出队。</li>
</ul>
<p>现在程序运行状态如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ad8301494bc4eaaa4f7d8a5c080c929~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>继续执行微任务队列中的方法</p>
<ul>
<li><code>P2-t1</code> 执行，输出 10，返回值是 <code>undefined</code> ，这时会调用 <code>P2-t1</code>  这个 then 方法中返回的新 Promise 实例的 resolve 方法并将返回值 <code>undefined</code> 传入，resolve 方法执行后即 <code>P2-t1返</code> 实例状态更改为成功态 <code>Fulfilled</code> ，并执行 <code>P2-t1返</code> 实例的缓存方法</li>
<li><code>P2-t1返</code> 实例的缓存中只有微任务方法包裹的 <code>P2-t2</code> 回调，执行后即 <code>P2-t2</code> 入微任务队列等待执行，到此微任务 <code>P2-t1</code> 执行结束，出队</li>
</ul>
<p>现在程序运行状态如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ac44b794c7048a3a656001248246f9f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还是一样的套路，接着执行微任务队列的任务</p>
<ul>
<li><code>P1-t2</code> 执行，输出 3，返回值是 <code>undefined</code> ，这时会调用 <code>P1-t2</code>  这个 then 方法中返回的新 Promise 实例的 resolve 方法并将返回值 <code>undefined</code> 传入，resolve 方法执行后即 <code>P1-t2返</code> 实例状态更改为成功态 <code>Fulfilled</code> ，并执行 <code>P1-t2返</code> 实例的缓存方法，由于后续没有 then， <code>P1-t2返</code> 实例也就没有缓存的方法， <code>P1-t2</code>  出队，P1 到此结束</li>
</ul>
<p>此时程序运行状态如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d094cd83e834344a2bcd85fd2db2445~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>接着微任务队列中 <code>P2-t2</code> 执行，输出 20， 返回值是 <code>undefined</code> ，这时会调用 <code>P2-t2</code>  这个 then 方法中返回的新 Promise 实例的 resolve 方法并将返回值 <code>undefined</code> 传入，resolve 方法执行后即 <code>P2-t2返</code> 实例状态更改为成功态 <code>Fulfilled</code> ，并执行 <code>P2-t2返</code> 实例的缓存方法</li>
<li><code>P2-t2返</code> 实例的缓存中只有微任务方法包裹的 <code>P2-t3</code> 回调，执行后即 <code>P2-t3</code> 入微任务队列等待执行，到此微任务 <code>P2-t2</code> 执行结束，出队</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dad178d5db84f958a342de2511cbdec~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>接下来就是执行微任务队列中的 <code>P2-t3</code> ，输出 30，同样， <code>P2-t4</code> 入队，<code>P2-t3</code> 出队，如下图：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dad1d1b44fc495298efd6af6811ae52~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>最后 <code>P2-t4</code> 执行，输出 40，结束出队，P2 结束，执行完毕，如下图：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fff087f5d3e49e8a89f7fd26e3efbce~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，最终的输出如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 2 10 3 20 30 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实对于简单题型，我们完全可以脑子里想象一个微任务队列即可，复杂一点可以画图理解。</p>
<p>这题如果 Get 了的话，接着往下看。。</p>
<h2 data-id="heading-14">Promise嵌套执行</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>)=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"1"</span>)
  resolve()
&#125;).then(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"2"</span>)
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>)=></span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"10"</span>)
      resolve()
  &#125;).then(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"20"</span>)
  &#125;).then(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"30"</span>)
  &#125;)
&#125;).then(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"3"</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如题，还是与之前一样 new 了两个 Promise实例，不过此题两个 Promise 是嵌套的关系。</p>
<p>那我们还是先为整道题做一个拆分命名：</p>
<ul>
<li>整个程序有两个 Promise，我们记作 <code>P1、P2</code></li>
<li>P1 中 Promise 传入的回调我们记作 <code>P1-主</code>，还有两个 then 方法我们记作 <code>P1-t1、P1-t2</code></li>
<li>P2 中 Promise 传入的回调我们记作 <code>P2-主</code>，还有两个 then 方法我们记作 <code>P2-t1、P2-t2</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16d07551964a4c59bae4b9785905f572~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实还是按照一样的套路分析就可以了，首先整个程序会作为一个宏任务第一批执行：</p>
<ul>
<li>因为 <code>new Promise</code> 时参数回调是同步执行，所以执行 <code>P1-主</code> 回调，输出 1，接着执行 <code>resolve</code> ，将 <code>new</code> 的 Promise 实例变为成功态 <code>Fulfilled</code> 。</li>
<li><code>P1-t1</code> 的 then 方法开始执行，由于上一个 Promise 为成功态，所以 <code>P1-t1</code> 回调直接入微任务对列等待执行</li>
<li>接着 <code>P1-t2</code> 的 then 方法开始执行，由于 <code>P1-t1</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P1-t2</code> 回调使用微任务方法包裹缓存进 <code>P1-t1返</code> 这个 Promise 实例中。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcd79054198d4ffa955c3f6a0b4cdd7d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>宏任务执行结束，开始依次执行微任务队列所有微任务。</p>
<ul>
<li>执行 <code>P1-t1</code>，输出 2，接着执行 <code>P1-t1</code> 回调里的 P2
<ul>
<li><code>P2-主</code> 是同步代码直接执行，输出 10，接着执行 <code>resolve</code> ，将 P2  <code>new</code> 的 Promise 实例变为成功态 <code>Fulfilled</code> 。</li>
<li>执行 <code>P2-t1</code> 的 then 方法，由于上一个 Promise 为成功态，所以 <code>P2-t1</code> 回调直接入微任务对列等待执行。</li>
<li>执行 <code>P2-t2</code> 的 then 方法，由于 <code>P2-t1</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t2</code> 回调使用微任务方法包裹缓存进 <code>P2-t1返</code> 这个 Promise 实例中。</li>
</ul>
</li>
<li><code>P1-t1</code> 回调执行完毕，其返回值是 <code>undefined</code> ，这时会调用 <code>P1-t1</code>  这个 then 方法中返回的新 Promise 实例的 resolve 方法并将返回值 <code>undefined</code> 传入，resolve方法执行后即 <code>P1-t1返</code> 实例状态更改为成功态 <code>Fulfilled</code> ，并执行 <code>P1-t1返</code> 实例的缓存方法。</li>
<li><code>P1-t1返</code> 实例中存有被微任务方法包裹的 <code>P1-t2</code> ，执行其微任务方法，<code>P1-t2</code> 入队，最后 <code>P1-t1</code> 出队</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af4f8ff531ae448d876118418d1bcfbb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着执行微任务队列：</p>
<ul>
<li><code>P2-t1</code> 开始执行，输出 20，返回值是 <code>undefined</code> ，这时会调用 <code>P2-t1</code>  这个 then 方法中返回的新 Promise 实例的 resolve 方法并将返回值 <code>undefined</code> 传入，resolve 方法执行后即 <code>P2-t1返</code> 实例状态更改为成功态 <code>Fulfilled</code> ，并执行 <code>P2-t1返</code> 实例的缓存方法。</li>
<li><code>P2-t1返</code> 实例中存有被微任务方法包裹的 <code>P2-t2</code> ，执行其微任务方法，<code>P2-t2</code> 入队，最后 <code>P2-t1</code> 出队</li>
</ul>
<p>目前程序状态如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/170557d63f794b4dabd748d72e245549~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着执行微任务队列：</p>
<ul>
<li>执行 <code>P1-t2</code>，输出 3， <code>P1-t2</code> 出队。</li>
<li>执行 <code>P2-t2</code>，输出 30， <code>P2-t2</code> 出队，程序执行完毕，如下图</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fab682ec80974fed864a64af6a1060af~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，这个嵌套的 Promise 程序的执行输出是：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 2 10 20 3 30</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">嵌套返回新Promise</h2>
<h3 data-id="heading-16">基础版</h3>
<p>前面在手写 Promise 的时候说过，Promise 实例 resolve 或 then 方法中还可以返回一个新的 Promise，当返回 Promise 对象时内部进行的处理和返回一些基础的值是不同的，那我们接下来就来看看这种情况。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">2</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res)
&#125;)

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">20</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">30</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">40</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样的，我们还是先为整道题做一个拆分命名：</p>
<ul>
<li>整个程序有两个 Promise，我们记作 <code>P1、P2</code></li>
<li>P1 使用 Promise 构造函数中的 resolve 方法创建了一个成功态的实例，后面有 2 个 then 方法，我们记作 <code>P1-t1</code>、<code>P1-t2</code>。</li>
<li>P2 使用 Promise 构造函数中的 resolve 方法创建了一个成功态的实例，后面有 4 个 then 方法，记作 <code>P2-t1</code>，<code>P2-t2</code>，<code>P2-t3</code>，<code>P2-t4</code>。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feb3399d0a9648d8a107c31232674be3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先整个程序会作为一个宏任务第一批执行：</p>
<ul>
<li>P1 中直接使用 Promise 构造函数中的 resolve 方法创建了一个成功态的实例，<code>P1-t1</code> 的 then 方法执行时，由于是成功态 <code>Fulfilled</code>，所以 <code>P1-t1</code> 直接作为微任务入队等待执行。</li>
<li>接着 <code>P1-t2</code> 的 then 方法开始执行，由于 <code>P1-t1</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P1-t2</code> 回调使用微任务方法包裹缓存进 <code>P1-t1返</code> 这个 Promise 实例中。</li>
<li>P2 中也是使用 Promise 构造函数中的 resolve 方法创建了一个成功态的实例，<code>P2-t1</code> 的 then 方法执行时，由于是成功态 <code>Fulfilled</code>，所以 <code>P2-t1</code> 直接作为微任务入队等待执行。</li>
<li>接着 <code>P2-t2</code> 的 then 方法开始执行，由于 <code>P2-t1</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t2</code> 回调使用微任务方法包裹缓存进 <code>P2-t1返</code> 这个 Promise 实例中。</li>
<li>接着 <code>P2-t3</code> 的 then 方法开始执行，由于 <code>P2-t2</code> 的 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t3</code> 回调使用微任务方法包裹缓存进 <code>P2-t2返</code> 这个 Promise 实例中。</li>
<li>接着 <code>P2-t4</code> 的 then 方法开始执行，由于 <code>P2-t3</code> 的 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t4</code> 回调使用微任务方法包裹缓存进 <code>P2-t3返</code> 这个 Promise 实例中。</li>
</ul>
<p>现在程序运行的状态如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d592992ff264b8886de491f29c85441~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>宏任务执行结束，开始依次执行微任务队列中的任务：</p>
<ul>
<li>首先是执行 <code>P1-t1</code>，输出 1，注意 ⚠️⚠️⚠️ ，<code>P1-t1</code> 回调中返回的是一个 Promise 对象，还记得我们之前手写 Promise 时对于返回结果是 Promise 对象的处理吗？没错，我们会调用传入 Promise 对象的 then 方法，取到其是成功态或者是失败态并将值传出。由于我们内部又取了 <code>Promise.resolve(2)</code> 这个 Promise 的 then 方法执行，且  <code>Promise.resolve(2)</code>  是一个成功态的 Promise，所以这个 then 方法执行后，其回调也会入队等待，我们记作  <code>P1-t1返</code>  回调，其实 <code>P1-t1返</code> 这个 Promise 实例就是 <code>Promise.resolve(2).then((res)=>&#123;...&#125;)</code> 。</li>
<li><code>P1-t1返</code> 回调入队了，由于 <code>P1-t1返</code> 回调在队列中排队，还没有执行，所以 <code>P1-t2</code> 这个 then 方法 对应的 Promise 实例还是等待态 <code>pending</code> ，所以 <code>P1-t2</code> 还是无动作。</li>
</ul>
<p>我们来看图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfe08ad72326483391131e725455b907~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着开始执行后微任务队列中的 <code>P2-t1</code> ：</p>
<ul>
<li><code>P2-t1</code> 回调执行，输出 10，返回值是 <code>undefined</code> ，这时会调用 <code>P2-t1</code>  这个 then 方法中返回的新 Promise 实例的 resolve 方法并将返回值 <code>undefined</code> 传入，resolve 方法执行后即 <code>P2-t1返</code> 实例状态更改为成功态 <code>Fulfilled</code> ，并执行 <code>P2-t1返</code> 实例的缓存方法。</li>
<li><code>P2-t1返</code> 实例中存有被微任务方法包裹的 <code>P2-t2</code> ，执行其微任务方法，<code>P2-t2</code> 入队，最后 <code>P2-t1</code> 出队</li>
</ul>
<p>如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce58f08564224b828eeffb59787f4bbf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照微任务队列中的顺序，现在要开始执行 <code>P1-t1返</code> 这个回调了：</p>
<ul>
<li><code>P1-t1返</code> 这个回调是之前 <code>P1-t1</code> 中的 <code>Promise.resolve(2)</code> 的 then 方法回调，它是在内部调用的，其实什么都没做，只是通过 then 取到成功态然后再将 2 这个值传 resolve 出去而已，所以 <code>P1-t1返</code> 回调执行，无输出，<code>P1-t1返</code> 这个 Promise 实例内部 resolve 之后状态改为成功态 <code>Fulfilled</code> ，并执行 <code>P1-t1返</code> 实例的缓存方法。</li>
<li><code>P1-t1返</code> 实例中存有被微任务方法包裹的 <code>P1-t2</code> ，执行其微任务方法，<code>P1-t2</code> 入队，最后 <code>P1-t1返</code> 出队。</li>
</ul>
<p>如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e6ebe2cffc449279293aece4f330c88~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>后面的就和之前一样了：</p>
<ul>
<li>执行微任务队列中的 <code>P2-t2</code> ，输出 20，<code>P2-t3</code> 入队，<code>P2-t2</code> 出队。</li>
<li>执行微任务队列中的 <code>P1-t2</code>，输出 2，<code>P1-t2</code> 出队，P1 结束。</li>
<li>接着执行微任务队列中的 <code>P2-t3</code> ，输出 30，<code>P2-t4</code> 入队，<code>P2-t3</code> 出队。</li>
<li>执行微任务队列中的 <code>P2-t4</code>，输出 40，<code>P2-t4</code> 出队，P2 结束。</li>
</ul>
<p>最终程序的输出结果如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 10 20 2 30 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好像很顺畅，真的是这样吗？</p>
<p>我们 <code>copy</code> 一下这段程序在浏览器控制台中执行一下，查看输出结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 10 20 30 2 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>？？？这是为什么？</p>
<p>按照我们上面的手写 Promise 实现方式输出结果是第一种，但是浏览器中输出结果却是下面这种。。。</p>
<p>我们之前的手写实现，当使用 Promise 返回一个新的 Promise 时，内部会调用它的 then 方法从而产生一个新的微任务，其回调入队，后面微任务队列执行到这个回调时，拿到传入的值作处理后再 resolve 出去。</p>
<blockquote>
<p>但是在 TC39 ECMA 262 SPEC 的 <code>Promise</code> 规范中是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8cdfafae76c4ac0b2062e20062b6564~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/870bcee4b51348ac99cfd2567f90e349~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-promise-reject-functions" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-promise-reject-functions" ref="nofollow noopener noreferrer">ECMA 262 spec Promise Resolve Functions</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-promise.prototype.then" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-promise.prototype.then" ref="nofollow noopener noreferrer">ECMA 262 spec NewPromiseResolveThenableJob</a></li>
</ul>
<p>如果我们仔细看过规范后，其实就会发现，规范中说的很明确，大概意思就是在 resolve 一个 thenable 时，ECMA 262 规定这个动作必须通过一个 job <code>NewPromiseResolveThenableJob</code> 以异步的方式来完成，也就是说这个 job 其实执行了一个微任务，后面在执行 <code>NewPromiseResolveThenableJob</code> 时又调用了 then 函数（类似我们上面手写 Promise 时，如果返回 Promise 的话，内部回调用这个 Promise 的 then 方法），这个时候又执行了一个微任务，所以是两次微任务。</p>
</blockquote>
<p>在 Chrome V8 的 <code>Promise.then</code> 实现中，就严格遵守了这一规范，这里需注意一下，我们上面的 Promise 手写实现遵循的是 Promise/A+ 规范，这个是 ECMA 262 规范，所以我们上面写的也不错，只是我们在面试或者做这种考查输出的题时还是以浏览器为标准的，所以 ECMA 262 要晓得，我们只要知道在返回一个 Promise 对象时，浏览器对其内部的实现会产生 2 次微任务就行，不用刻意纠结，记住就好，没必要扒 V8 源码，意义不大。</p>
<p>那接下来，我们按照浏览器的标准从零再来解释一下这道题。</p>
<p>程序回到最初的状态如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4a0c29c704a4045a1ea4f65e05deeed~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先整个程序会作为一个宏任务第一批执行：</p>
<ul>
<li>P1 中直接使用 Promise 构造函数中的 resolve 方法创建了一个成功态的实例，<code>P1-t1</code> 的 then 方法执行时，由于是成功态 <code>Fulfilled</code>，所以 <code>P1-t1</code> 直接作为微任务入队等待执行。</li>
<li>接着 <code>P1-t2</code> 的 then 方法开始执行，由于 <code>P1-t1</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P1-t2</code> 回调使用微任务方法包裹缓存进 <code>P1-t1返</code> 这个 Promise 实例中。</li>
<li>P2 中也是使用 Promise 构造函数中的 resolve 方法创建了一个成功态的实例，<code>P2-t1</code> 的 then 方法执行时，由于是成功态 <code>Fulfilled</code>，所以 <code>P2-t1</code> 直接作为微任务入队等待执行。</li>
<li>接着 <code>P2-t2</code> 的 then 方法开始执行，由于 <code>P2-t1</code> 回调还在队列中，上一个 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t2</code> 回调使用微任务方法包裹缓存进 <code>P2-t1返</code> 这个 Promise 实例中。</li>
<li>接着 <code>P2-t3</code> 的 then 方法开始执行，由于 <code>P2-t2</code> 的 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t3</code> 回调使用微任务方法包裹缓存进 <code>P2-t2返</code> 这个 Promise 实例中。</li>
<li>接着 <code>P2-t4</code> 的 then 方法开始执行，由于 <code>P2-t3</code> 的 then 方法返回的 Promise 实例状态还是 <code>pending</code> ，所以 <code>P2-t4</code> 回调使用微任务方法包裹缓存进 <code>P2-t3返</code> 这个 Promise 实例中。</li>
</ul>
<p>现在程序运行的状态如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad6265aa8a3949d08319e8d1fd81f8ff~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>宏任务执行结束，开始依次执行微任务队列中的任务：</p>
<ul>
<li>首先是执行 <code>P1-t1</code>，输出 1，由于后面 <code>P1-t1</code> 回调中返回的是一个 Promise 对象，所以和规范中一致，创建一个微任务，我们记作 <code>PRTJob</code> 入队。</li>
</ul>
<p>如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ab2b9ed3b994c9b9b2c43836db3baad~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着开始执行后微任务队列中的 <code>P2-t1</code> ：</p>
<ul>
<li><code>P2-t1</code> 回调执行，输出 10，返回值是 <code>undefined</code> ，这时会调用 <code>P2-t1</code>  这个 then 方法中返回的新 Promise 实例的 resolve 方法并将返回值 <code>undefined</code> 传入，resolve 方法执行后即 <code>P2-t1返</code> 实例状态更改为成功态 <code>Fulfilled</code> ，并执行 <code>P2-t1返</code> 实例的缓存方法。</li>
<li><code>P2-t1返</code> 实例中存有被微任务方法包裹的 <code>P2-t2</code> ，执行其微任务方法，<code>P2-t2</code> 入队，最后 <code>P2-t1</code> 出队</li>
</ul>
<p>如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/487e6f4dac6f4631a8e17dc564e408fa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照微任务队列中的顺序，要开始执行 <code>PRTJob</code> 这个回调了：</p>
<ul>
<li><code>PRTJob</code> 是在内部调用的，所以没有任何输出， <code>PRTJob</code> 在执行时，就是走 <code>NewPromiseResolveThenableJob</code>  规范，又因为执行时其内部调用了 then 方法，所以此时会作为一个微任务再次入队（第二次微任务），这里我们记作 <code>P1-t1返</code> 回调。</li>
<li><code>P1-t1返</code> 回调还在队列中，所以 <code>P1-t1</code> 的 then 方法返回的 Promise 实例的状态还是 <code>pending</code>，所以后续的 <code>P1-t2</code> 还是无动作存在缓存数组中。</li>
</ul>
<p>如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e16a90bffeec4ed089f1bb0949e9eeb1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>接着执行微任务队列中的 <code>P2-t2</code> ，输出 20，<code>P2-t3</code> 入队，<code>P2-t2</code> 出队。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92c65c1157204ecc89f43b4218857d79~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>接着执行微任务队列中的 <code>P1-t1返</code> 回调，同样是内部调用，无输出，该回调内部执行完实例的 resolve 方法后，<code>P1-t1</code> 的 then 方法返回的 Promise 也就是 <code>P1-t1返</code> 这个Promise 实例终于变成了成功态 <code>Fulfilled</code>，接着清空实例的缓存， <code>P1-t2</code> 入队，<code>P1-t1返</code> 回调出队。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6754d7c7d15e4bf1ba1713f1d727ac42~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>接着执行微任务队列中的 <code>P2-t3</code>，输出 30，<code>P2-t4</code> 入队，<code>P2-t3</code> 出队。</li>
<li>再执行微任务队列中的 <code>P1-t2</code>，输出 2，<code>P1-t2</code> 出队，P1 执行结束。</li>
<li>接着执行微任务队列中的 <code>P2-t4</code>，输出 40，<code>P2-t4</code> 出队，P2 执行结束。</li>
</ul>
<p>最终程序执行输出结果如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 10 20 30 2 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">增强版</h3>
<p>上面那个小例子只是单纯返回了一个 Promise，我们再给它接个 then 试试看：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">2</span>).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
    <span class="hljs-keyword">return</span> res
  &#125;);
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res)
&#125;)

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">20</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">30</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">40</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器控制台里运行此段代码后，我们发现输出的结果是：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 10 20 30 2 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>诶？为什么接了一个 then 后输出顺序和没有接 then 是时候一样，没有变化？</p>
<p>再来接一个 then 试试，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">2</span>).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
    <span class="hljs-keyword">return</span> res
  &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
    <span class="hljs-keyword">return</span>  res
  &#125;)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res)
&#125;)

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">20</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">30</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">40</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们在返回的 <code>Promise.resolve(2)</code> 后面接了 2 个 then 方法，来看输出结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 10 20 30 40 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>诶？输出结果又变了，可以看到，在只返回一个单纯的 Promise 对象时和在 Promise 对象后跟一个 then 方法的输出结果是一样的，但是返回的 Promise 后面跟 2 个以上的 then 方法时，又会影响到输出顺序，这是为什么呢？</p>
<p>其实很简单，还按照我们之前的套路画一个入队的图就知道了，上面我们已经介绍过了单纯的返回一个 <code>Promise.resolve(2)</code> 的程序微任务入队出队图。这里就不给大家画详细的图了，我们口述一下，最后简单画一个程序整体微任务队列入队出队图。</p>
<p>回顾 No.1 中只返回一个 <code>Promise.resolve(2)</code> 的程序，我们看它整体的微任务队列图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95608e69d88a4dcba46d26bd4d19aa7f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们再来看 <code>Promise.resolve(2).then(res => return res)</code> 的程序：</p>
<ul>
<li>由于多了一个 then，整个程序除了之前说的 P1 和 P2，我们将 <code>Promise.resolve(2).then(res => return res)</code> 记作 P3，多出的这一个 then 方法我们记作 <code>P3-t1</code> 。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a56843cd48e4da9a805c98d58c849d4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单口述一下各个微任务的入队出队顺序，大家可以跟着在纸上画一下：</p>
<ul>
<li>程序主体作为一个宏任务第一批次执行。</li>
<li>P1 中由于是 <code>Promise.resolve()</code> ，所以直接返回成功态 Promise，<code>P1-t1</code> 入队。</li>
<li><code>P1-t2</code> 的 then 方法执行，由于上一个 then 方法返回的 Promise 还在等待态 <code>pending</code> ，所以缓存到 <code>P1-t1返</code> 这个 Promise 实例等待执行。</li>
<li>P2 中也是 <code>Promise.resolve()</code> ，所以直接返回成功态 Promise，<code>P2-t1</code> 入队。</li>
<li>P2 后续的 <code>P2-t2</code>、<code>P2-t3</code>、<code>P2-t4</code> 各自缓存进其上一个 then 方法返回的 Promise 实例中</li>
</ul>
<p>宏任务结束，开始执行微任务队列：</p>
<ul>
<li><code>P1-t1</code> 执行，输出 1，接着执行 <code>return Promise.resolve(2).then(...)</code>，<code>P3-1</code> 入队。</li>
<li>由于 <code>P1-t1</code> 回调的返回值为 Promise 对象，所以创建 <code>PRTJob</code> 入队。<code>P1-t1</code> 回调执行结束出队。</li>
<li>接着执行微任务队列中的 <code>P2-t1</code> 回调，输出 10，<code>P2-t1返</code> 实例变为成功态 <code>Fulfilled</code>，<code>P2-t2</code> 入队。</li>
<li>接着执行微任务队列中的 <code>P3-t1</code> 回调，<code>P3-t1</code> 的 then 方法返回的 Promise 实例状态改为成功态 <code>Fulfilled</code>，无输出，执行结束 <code>P3-t1</code> 出队。</li>
<li>接着执行微任务队列中的 <code>PRTJob</code> 回调，由于 <code>P3-t1</code> 中返回的 Promise 实例状态为成功态 <code>Fulfilled</code>，所以 <code>PRTJob</code> 执行时，调用 then 方法 <code>P1-t1返</code> 回调直接入队，<code>PRTJob</code> 出队。</li>
<li>接着执行微任务队列中的 <code>P2-t2</code> 回调，输出 20，<code>P2-t2返</code> 实例变为成功态 <code>Fulfilled</code>，<code>P2-t3</code> 入队， <code>P2-t2</code> 出队。</li>
<li>接着执行微任务队列中的 <code>P1-t1返</code> 回调， <code>P1-t1返</code> 实例变为成功态 <code>Fulfilled</code>，<code>P1-t2</code> 入队， <code>P1-t1返</code> 出队 。</li>
<li>接着执行微任务队列中的 <code>P2-t3</code> 回调，输出 30，<code>P2-t3返</code> 实例变为成功态 <code>Fulfilled</code>，<code>P2-t4</code> 入队， <code>P2-t3</code> 出队 。</li>
<li>接着执行微任务队列中的 <code>P1-t2</code> 回调，输出 2， <code>P1-t2</code> 出队，P1 结束。</li>
<li>接着执行微任务队列中的 <code>P2-t4</code> 回调，输出 40， <code>P2-t4</code> 出队，P2 结束。</li>
</ul>
<p>整个程序微任务入队出队顺序如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a19820491d054a0f9bb5d220bf550c79~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>再来看 <code>Promise.resolve(2).then(...).then(...)</code> 的程序：</p>
<ul>
<li>由于多了两个 then，整个程序除了之前说的 P1 和 P2，我们将 <code>Promise.resolve(2).then(...).then(...)</code> 记作 P3，两个 then 方法我们分别记作 <code>P3-t1</code>、<code>P3-t2</code> 。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/833cb200cd5b4184b2d45c4760851f4a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单口述一下各个微任务的入队出队顺序，和上面一样，大家可以跟着在纸上画一下：</p>
<ul>
<li>程序主体作为一个宏任务第一批次执行。</li>
<li>P1 中由于是 <code>Promise.resolve()</code> ，所以直接返回成功态 Promise，<code>P1-t1</code> 入队。</li>
<li><code>P1-t2</code> 的 then 方法执行，由于上一个 then 方法返回的 Promise 还在等待态 <code>pending</code> ，所以缓存到 <code>P1-t1返</code> 这个 Promise 实例等待执行。</li>
<li>P2 中也是 <code>Promise.resolve()</code> ，所以直接返回成功态 Promise，<code>P2-t1</code> 入队。</li>
<li>P2 后续的 <code>P2-t2</code>、<code>P2-t3</code>、<code>P2-t4</code> 各自缓存进其上一个 then 方法返回的 Promise 实例中</li>
</ul>
<p>宏任务结束，开始执行微任务队列：</p>
<ul>
<li><code>P1-t1</code> 执行，输出 1，接着执行 <code>return Promise.resolve(2).then(...)</code>，<code>P3-t1</code> 入队。</li>
<li>由于 <code>P1-t1</code> 回调的返回值为 Promise 对象，所以创建 <code>PRTJob</code> 入队。<code>P1-t1</code> 回调执行结束出队。</li>
<li>接着执行微任务队列中的 <code>P2-t1</code> 回调，输出 10，<code>P2-t1返</code> 实例变为成功态 <code>Fulfilled</code>，<code>P2-t2</code> 入队。</li>
<li>接着执行微任务队列中的 <code>P3-t1</code> 回调，<code>P3-t1</code> 的 then 方法返回的 Promise 实例状态改为成功态 <code>Fulfilled</code>，无输出，执行结束 <code>P3-t2</code> 入队， <code>P3-t1</code> 出队。</li>
<li>接着执行微任务队列中的 <code>PRTJob</code> 回调，由于 <code>P3-t2</code> 还在队列中，即返回的实例状态还在等待态 <code>pending</code>， 所以 <code>PRTJob</code> 执行时，调用实例的 then 方法会直接存入实例缓存，等待 <code>P3-t2</code> 回调执行后状态为成功态 <code>Fulfilled</code>时调用，<code>PRTJob</code> 出队。</li>
<li>接着执行微任务队列中的 <code>P2-t2</code> 回调，输出 20，<code>P2-t2返</code> 实例变为成功态 <code>Fulfilled</code>，<code>P2-t3</code> 入队， <code>P2-t2</code> 出队。</li>
<li>接着执行 <code>P3-t2</code> 回调，<code>P3-t2</code> 这个 then 方法返回的 Promise 状态改为成功态 <code>Fulfilled</code>，这时，内部调用其实例的 then 方法，规范中说的返回 Promise时产生的第二次微任务 <code>P1-t1返</code> 回调入队。</li>
<li>接着执行微任务队列中的 <code>P2-t3</code> 回调，输出 30，<code>P2-t3返</code> 实例变为成功态 <code>Fulfilled</code>，<code>P2-t4</code> 入队， <code>P2-t3</code> 出队 。</li>
<li>接着执行微任务队列中的 <code>P1-t1返</code> 回调， <code>P1-t1返</code> 实例变为成功态 <code>Fulfilled</code>，<code>P1-t2</code> 入队， <code>P1-t1返</code> 出队 。</li>
<li>接着执行微任务队列中的 <code>P2-t4</code> 回调，输出 40， <code>P2-t4</code> 出队，P2 结束。</li>
<li>接着执行微任务队列中的 <code>P1-t2</code> 回调，输出 2， <code>P1-t2</code> 出队，P1 结束。</li>
</ul>
<p>整个程序微任务入队出队顺序如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4140615a86d846c5a477aae04d9142f8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于为什么一个 then 和不带 then 的输出结果一致，我们来看三个程序的微任务入队出队顺序对比就知道了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51201f72d65449e598e89a5c36d7b1a4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实，主要是因为在返回的 Promise 对象后写一个 then，由于这个 then 的上个 Promise 是 <code>Promise.resolve()</code> ，状态是成功态，所以会先入队。返回一个 Promise 所造成的两次微任务，第二次是调用传入 Promise 对象的 then 方法，只要调用前该 Promise 实例的状态是成功态 <code>Fulfilled</code> 即可。直接返回 <code>Promise.resolve()</code> 的话，其状态直接就是成功态 <code>Fulfilled</code> ，而在返回的 Promise 后写两个及以上的 then，那传入到内部的 Promise 实例的就需要等最后一个 then 返回的 Promise 实例状态为成功态 <code>Fulfilled</code> 时才能执行。</p>
<p>如果看不懂我的描述也没关系，会画图就可以，按照我们的套路走即可。</p>
<h2 data-id="heading-18">async/await+Promise执行</h2>
<h3 data-id="heading-19">基础版</h3>
<p>async/await 其实就是 Generator + Promise 的一个语法糖，不过它也有很多坑。</p>
<p>来看下面这个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">await</span> async2();
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;
async1();

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);
  resolve();
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">20</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">30</span>)
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">40</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子在老版本浏览器和新版本浏览器中是有差异的，主要还是浏览器的内部实现。</p>
<p>可以简单的这样理解，await 下面的代码会被作为一个微任务入队。</p>
<p>接下来我们来逐步分析：</p>
<ul>
<li>首先，整体作为一个宏任务开始执行。</li>
<li>运行 <code>async1()</code> ，函数 async1 开始执行，输出 1，遇到 await，执行 <code>async2</code>，输出 3，await 下面的代码作为微任务入队。</li>
<li>接着执行 <code>new Promise()</code> 的回调，输出 10，<code>resolve</code> 的执行让返回的 Promise 实例状态变为了成功态 <code>Fulfilled</code>。</li>
<li>执行第一个 then 方法，由于接上一个 Promise 返回的实例是成功态 <code>Fulfilled</code> ，所以第一个 then 方法回调直接入队。</li>
<li>执行第二个 then 方法，由于第一个 then 方法回调还在队列中没有执行，所以上一个 Promise 返回的实例还是等待态 <code>pending</code> ，将第二个 then 方法回调由微任务方法包裹缓存进实例数组。</li>
<li>执行第三个 then 方法，由于第二个 then 方法回调还在队列中没有执行，所以上一个 Promise 返回的实例还是等待态 <code>pending</code> ，将第三个 then 方法回调由微任务方法包裹缓存进实例数组。</li>
</ul>
<p>到此，宏任务结束，开始执行微任务队列的任务。</p>
<ul>
<li>首先，执行先入队的 async1 方法中 await 下面的代码回调，输出 2，然后出队。</li>
<li>接着，执行队列中的第一个 then 回调，输出 20，返回undefined，内部执行 <code>resolve(undefined)</code> 后返回的实例状态改为成功态 <code>Fulfilled</code>，并执行实例上的缓存方法，所以第二个 then 方法回调入队，第一个 then 方法出队。</li>
<li>接着，执行队列中的第二个 then 回调，输出 30，返回undefined，内部执行 <code>resolve(undefined)</code> 后返回的实例状态改为成功态 <code>Fulfilled</code>，并执行实例上的缓存方法，所以第三个 then 方法回调入队，第一个 then 方法出队。</li>
<li>接着，执行队列中的第三个 then 回调，输出 40，返回undefined，内部执行 <code>resolve(undefined)</code> 后返回的实例状态改为成功态 <code>Fulfilled</code>，并执行实例上的缓存方法，实例上缓存数组为空，第三个 then 方法出队，程序结束。</li>
</ul>
<p>最终的输出结果为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 3 10 2 20 30 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">增强版</h3>
<p>题目简单一变，又能迷倒一大群人，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">await</span> async2();
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
&#125;
async1();

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);
  resolve();
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">20</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">30</span>)
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">40</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，之前的代码中 <code>async2</code> 函数没有写 return ，也就是返回的是一个 undefined，由于是 <code>async</code> 吗，最终函数是返回一个值为 undefined 的 Promise 对象，但现在我们在 <code>async2</code> 函数中返回了一个 Promise 对象。。。</p>
<p>输出一下，顺序变了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 3 10 20 30 2 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>聪明的小伙伴可能已经看出蹊跷来了，之前在说 Promise 的时候，我们就在说如果返回的是一个正常的值，Promise 内部会正常 resolve 出去，但是如果返回的是一个新的 Promise 对象，内部会产生 2 个微任务。</p>
<p>那这里为了方便理解，其实也完全可以按照这种思路来走。</p>
<p>现在我们在 <code>async2</code> 函数中返回了一个 Promise 对象，相当于多产生了 2 次微任务，所以输出中 2 的顺序后移了 2 位。</p>
<p>整体流程大概就是：</p>
<ul>
<li>首先，整体作为一个宏任务开始执行。</li>
<li>运行 <code>async1()</code> ，函数 async1 开始执行，输出 1，遇到 await，执行 <code>async2</code>，先输出 3，由于<code>async2</code> 中返回的是 Promise 对象，解析时产生的第一个微任务入队。</li>
<li>接着执行 <code>new Promise()</code> 的回调，输出 10，<code>resolve</code> 的执行让返回的 Promise 实例状态变为了成功态 <code>Fulfilled</code>。</li>
<li>执行第一个 then 方法，由于接上一个 Promise 返回的实例是成功态 <code>Fulfilled</code> ，所以第一个 then 方法回调直接入队。</li>
<li>执行第二个 then 方法，由于第一个 then 方法回调还在队列中没有执行，所以上一个 Promise 返回的实例还是等待态 <code>pending</code> ，将第二个 then 方法回调由微任务方法包裹缓存进实例数组。</li>
<li>执行第三个 then 方法，由于第二个 then 方法回调还在队列中没有执行，所以上一个 Promise 返回的实例还是等待态 <code>pending</code> ，将第三个 then 方法回调由微任务方法包裹缓存进实例数组。</li>
</ul>
<p>到此，宏任务结束，开始执行微任务队列的任务。</p>
<ul>
<li>首先，执行 <code>async2</code> 中返回 Promise 对象解析时所产生的第一个微任务，无输出，然后产生的第二个微任务入队，产生的第一个微任务出队。</li>
<li>接着，执行队列中的第一个 then 回调，输出 20，返回undefined，内部执行 <code>resolve(undefined)</code> 后返回的实例状态改为成功态 <code>Fulfilled</code>，并执行实例上的缓存方法，所以第二个 then 方法回调入队，第一个 then 方法出队。</li>
<li>接着，执行 <code>async2</code> 中返回 Promise 对象解析时所产生的第二个微任务，无输出，然后 <code>async1</code> 函数中 await 下面的代码作为微任务入队，返回 Promise 对象解析时所产生的第二个微任务出队。</li>
<li>接着，执行队列中的第二个 then 回调，输出 30，返回undefined，内部执行 <code>resolve(undefined)</code> 后返回的实例状态改为成功态 <code>Fulfilled</code>，并执行实例上的缓存方法，所以第三个 then 方法回调入队，第一个 then 方法出队。</li>
<li>接着，执行 <code>async1</code> 函数中 await 下面代码产生的微任务，输出 2，随后出队。</li>
<li>接着，执行队列中的第三个 then 回调，输出 40，返回undefined，内部执行 <code>resolve(undefined)</code> 后返回的实例状态改为成功态 <code>Fulfilled</code>，并执行实例上的缓存方法，实例上缓存数组为空，第三个 then 方法出队，程序结束。</li>
</ul>
<p>最终的输出结果即：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 3 10 20 30 2 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实，还可以在 <code>async2</code> 函数返回的 <code>Promise.resolve()</code> 后面加一个 then 方法，你会发现输出顺序还是上面这种，加 2 个及以上的 then 方法 输出结果的 2 才会产生后移。有没有发现哪里相似？</p>
<p>没错，和我们上面 Promise 中说过的案例如出一辙，这里就不再唠叨了，感兴趣可以自己写一写、画一画。。</p>
<p>其实由于规范在改动，浏览器也在不断升级，所以执行顺序这个东西真的是很扯淡。。。我们了解就好，只要能解释为什么，最终结果不用过分在意。。</p>
<h2 data-id="heading-21">杂七杂八的混编执行</h2>
<p>最后来一个混编的题型，以应对多个宏任务+多个微任务的场景下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);
  &#125;, <span class="hljs-number">2000</span>);
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">20</span>);
  &#125;, <span class="hljs-number">1000</span>);
  reslove();
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1-1'</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">30</span>);
      reslove();
    &#125;, <span class="hljs-number">500</span>);
  &#125;);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2-1'</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">40</span>);
      reslove();
    &#125;, <span class="hljs-number">200</span>);
  &#125;);
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，还是为程序中各个部分做一个拆分命名。</p>
<ul>
<li>程序中所有的 <code>setTimeout</code> 使用 <code>timer+定时的ms数字</code> 命名。</li>
<li>最外部的 Promise 记作 P1，<code>new Promise</code> 的回调记作 <code>P1-主</code>，其下三个 then 方法分别记作 <code>P1-t1</code>，<code>P1-t2</code>，<code>P1-t3</code>。</li>
<li><code>P1-t1</code> 中返回的 <code>new Promise</code> 实例记作 P2，其实例参数回调记作 <code>P2-主</code>。</li>
<li><code>P1-t2</code> 中返回的 <code>new Promise</code> 实例记作 P3，其实例参数回调记作 <code>P3-主</code>。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4314e118f3e54a668a36216f3f8f7044~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图为程序初始化状态，多了一个宏任务队列，我们慢慢来看。</p>
<p>首先整个程序作为一个宏任务先执行：</p>
<ul>
<li><code>P1-主</code> 执行，遇到 <code>timer2000</code> ，<code>setTimeout</code> 为异步宏任务，通过事件触发线程将其移交给定时触发器线程处理，等待其 <code>2000ms</code> 定时结束其回调入宏任务队列。接着执行，遇到 <code>timer1000</code> ，<code>setTimeout</code> 为异步宏任务，通过事件触发线程将其移交给定时触发器线程处理，等待其 <code>1000ms</code> 定时结束其回调入宏任务队列。最后执行 resolve 方法将返回的 Promise 实例状态改为成功态 <code>Fulfilled</code>。</li>
<li>由于 <code>new Promise</code> 实例参数回调中已经调用 resolve 方法，所以返回的 Promise 实例 <code>P1-主返</code> 状态为成功态 <code>Fulfilled</code> ，<code>P1-t1</code> 的 then 方法执行时，直接入微任务队列。</li>
<li><code>P1-t2</code> 由于 <code>P1-t1</code> 还在回调中，其返回的 Promise 实例 <code>P1-t1返</code> 状态为等待态 <code>pending</code> ，所以 <code>P1-t2</code> 回调被微任务方法包裹存入 <code>P1-t1返</code> 实例缓存数组中。</li>
<li><code>P1-t3</code> 由于 <code>P1-t2</code> 回调还未执行，其返回的 Promise 实例 <code>P1-t2返</code> 状态为等待态 <code>pending</code> ，所以 <code>P1-t3</code> 回调被微任务方法包裹存入 <code>P1-t2返</code> 实例缓存数组中。</li>
</ul>
<p>此时程序运行状态如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7686513ab8224478a64a405ef691da3b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>到此第一轮宏任务执行完毕，开始执行微任务队列。</p>
<ul>
<li>执行 <code>P1-t1</code> 回调，先输出 1，接着执行 return 的 Promise 实例参数回调 <code>P2-主</code> ，输出 <code>1-1</code>，又遇到了 <code>setTimeout</code> ，通过事件触发线程将其移交给定时触发器线程处理，等待其 <code>500ms</code> 定时结束其回调入宏任务队列，由于 resolve 方法是在定时器中执行的，所以此时 通过 new Promise 创建的 Promise 实例状态还是等待态 <code>pending</code>。</li>
<li>由于 <code>P1-t1</code> 最终返回的是一个 Promise 对象，所以和规范中一致，创建第一个微任务 job，我们记作 <code>PRTJob1</code> 入微任务队列。到此 <code>P1-t1</code> 出队。</li>
<li>接着执行微任务队列中的任务，即 <code>PRTJob1</code> 回调，执行结束后，开始执行 <code>P1-t1</code> 中 return 的 <code>new Promise</code> 实例的 then 方法（ 该方法执行后会返回 <code>P1-t1返</code> 实例 ），由于 <code>P1-t1</code> 中 return 的 <code>new Promise</code> 实例还是等待态 <code>pending</code>，所以 <code>P1-t1</code> 中 return 的 <code>new Promise</code> 实例的 then 方法回调（记作 <code>P1-t1返</code> 回调）被微任务方法包裹存入 <code>P1-t1返</code> 实例缓存数组中。</li>
</ul>
<p>此时程序状态如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e9c5dd4e78447e9a8d8fa4eeaa075fe~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时微任务队列已经执行完毕，宏任务队列没有任务，500ms 后，定时器触发线程的 <code>timer500</code> 执行有了结果后将其回调送入宏任务队列。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94cc7e28b56148629962cf24c33383f0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时主线程空闲，突然宏任务队列有了任务，所以立即取宏任务队列的第一个任务在 JS主执行栈执行，即开始执行新的宏任务 <code>timer500</code>。</p>
<ul>
<li>执行 <code>timer500</code> 回调，输出 30，再接着执行 resolve 方法，此时 <code>P1-t1</code> 中 return 的 <code>new Promise</code> 实例状态改为了成功态 <code>Fulfilled</code> ，并执行其实例中的缓存，即 <code>P1-t1返</code> 回调入微任务队列。</li>
</ul>
<p>如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ffade31f25c4262900769535f747355~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>宏任务执行完毕，开始执行当前宏任务所产生的所有微任务。</p>
<ul>
<li>执行微任务队列中的  <code>P1-t1返</code>  回调，修改 <code>P1-t1返</code>  实例的状态为成功态 <code>Fulfilled</code> ，执行其实例上的缓存，所以 <code>P1-t2</code> 入微任务队列。</li>
<li>接着执行微任务队列的  <code>P1-t2</code> 回调，输出 2，接着执行 return 的 Promise 实例参数回调 <code>P3-主</code> ，输出 <code>2-1</code>，又遇到了 <code>setTimeout</code> ，通过事件触发线程将其移交给定时触发器线程处理，等待其 <code>200ms</code> 定时结束其回调入宏任务队列，由于 resolve 方法是在定时器中执行的，所以此时通过 new Promise 创建的 Promise 实例状态还是等待态 <code>pending</code>。</li>
<li>由于 <code>P1-t2</code> 最终返回的是一个 Promise 对象，所以和规范中一致，创建第一个微任务 job，我们记作 <code>PRTJob2</code> 入微任务队列。到此 <code>P1-t2</code> 出队。</li>
<li>接着执行微任务队列中的任务，即 <code>PRTJob2</code> 回调，执行结束后，开始执行 <code>P1-t2</code> 中 return 的 <code>new Promise</code> 实例的 then 方法（ 该方法执行后会返回 <code>P1-t2返</code> 实例 ），由于 <code>P1-t2</code> 中 return 的 <code>new Promise</code> 实例还是等待态 <code>pending</code>，所以 <code>P1-t2</code> 中 return 的 <code>new Promise</code> 实例的 then 方法回调（记作 <code>P1-t2返</code> 回调）被微任务方法包裹存入 <code>P1-t2返</code> 实例缓存数组中。</li>
</ul>
<p>此时程序状态如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/385b184a780445bdb9d62b823dc61cd6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时微任务队列已经执行完毕，宏任务队列没有任务，200ms 后，定时器触发线程的 <code>timer200</code> 执行有了结果后将其回调送入宏任务队列。</p>
<p>此时主线程空闲，突然宏任务队列有了任务，所以立即取宏任务队列的第一个任务在 JS主执行栈执行，即开始执行新的宏任务 <code>timer200</code>。</p>
<ul>
<li>执行 <code>timer200</code> 回调，输出 40，再接着执行 resolve 方法，此时 <code>P1-t2</code> 中 return 的 <code>new Promise</code> 实例状态改为了成功态 <code>Fulfilled</code> ，并执行其实例中的缓存，即 <code>P1-t2返</code> 回调入微任务队列。</li>
</ul>
<p>如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b78d563b81248bbafe00845b526c58e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>宏任务执行完毕，开始执行当前宏任务所产生的所有微任务。</p>
<ul>
<li>执行微任务队列中的  <code>P1-t2返</code>  回调，修改 <code>P1-t2返</code>  实例的状态为成功态 <code>Fulfilled</code> ，执行其实例上的缓存，所以 <code>P1-t3</code> 入微任务队列。</li>
<li>接着执行微任务队列的  <code>P1-t3</code> 回调，输出 3。到这本轮微任务执行结束。</li>
</ul>
<p>此时程序状态如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77995b77dfdb4e6a8579417baab8609a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于宏任务队列没有任务，此时主线程空闲，（1000ms-500ms-200ms） 后，定时器触发线程的 <code>timer1000</code> 执行有了结果后将其回调送入宏任务队列。</p>
<p>宏任务队列有了任务，所以立即取宏任务队列的第一个任务在 JS主执行栈执行，即开始执行新的宏任务 <code>timer1000</code>。</p>
<ul>
<li>执行 <code>timer1000</code> 回调，输出 20，没有产生微任务，所以本轮执行结束。</li>
</ul>
<p>由于宏任务队列没有任务，此时主线程空闲，（2000ms-1000ms） 后，定时器触发线程的 <code>timer2000</code> 执行有了结果后将其回调送入宏任务队列。</p>
<p>宏任务队列有了任务，所以立即取宏任务队列的第一个任务在 JS主执行栈执行，即开始执行新的宏任务 <code>timer2000</code>。</p>
<ul>
<li>执行 <code>timer2000</code> 回调，输出 10，没有产生微任务，所以本轮执行结束。</li>
</ul>
<p>到此整个程序结束，最终输出：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1 1-1 30 2 2-1 40 3 20 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Get 到了吗？</p>
<h2 data-id="heading-22">写在最后</h2>
<p>那么，看懂了吗？看得懂最好了，看不懂也没必要懊恼，只要理解 JS运行机制以及 Promise 的核心概念对一些简单的执行顺序可以做出准确的分析即可，本文的内容对实际开发帮助不大，因为真的不敢想象开发中如果出现了这种基于复杂的调用顺序而写的代码是一件多么糟糕的事情，奈何还真有很多企业面试时会问这些无聊的问题，所以了解这些，从此就不用担心这类面试题了。</p>
<p>不清楚的地方请评论区留言，欢迎指错勘误！</p>
<p>最后，码字不易，画图更不易，点赞、点赞、点赞！欢迎关注 <a href="https://juejin.cn/column/6960559453037199391" target="_blank" title="https://juejin.cn/column/6960559453037199391">「硬核JS」</a> 专栏，Get 更多 JS 知识哦！！</p></div>  
</div>
            