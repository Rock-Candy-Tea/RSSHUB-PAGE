
---
title: 'Vue nextTick 实现原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8588'
author: 掘金
comments: false
date: Sat, 22 May 2021 01:53:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=8588'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>由于 Vue 更新 DOM 是异步执行的，如果在数据修改后面直接做某些操作，会被立即执行，而此时DOM还未更新，Vue 提供了 <code>nextTick</code>，在数据修改后立即调用，可以确保传入的回调函数会在更新完成之后执行。</p>
<p>接下来跟着两个问题来探索 nextTick 的原理</p>
<ul>
<li>调用 nextTick 会发生什么呢？</li>
<li>它是如何检测到DOM更新完成的呢？</li>
</ul>
<h2 data-id="heading-1">nextTick</h2>
<p>全局API <code>Vue.nextTick</code> 和实例方法 <code>vm.$nextTick</code> 内部实际上都是在调用 <code>nextTick</code> 函数。<code>nextTick</code>逻辑很简单，其作用就是将传进去的回调函数推入 <code>callbacks</code> 队列，（如果没有回调且支持Promise，则传入一个resolve）然后判断 <code>pending</code> 为 false 则调用 <code>timerFunc</code>，到此就结束了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> callbacks = []
<span class="hljs-keyword">let</span> pending = <span class="hljs-literal">false</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nextTick</span> (<span class="hljs-params">cb, ctx</span>) </span>&#123;
  <span class="hljs-keyword">let</span> _resolve
  callbacks.push(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (cb) &#123;
      <span class="hljs-keyword">try</span> &#123;
        cb.call(ctx)
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        handleError(e, ctx, <span class="hljs-string">'nextTick'</span>)
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (_resolve) &#123;
      _resolve(ctx)
    &#125;
  &#125;)
  <span class="hljs-keyword">if</span> (!pending) &#123;
    pending = <span class="hljs-literal">true</span>
    timerFunc()
  &#125;
  <span class="hljs-keyword">if</span> (!cb && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Promise</span> !== <span class="hljs-string">'undefined'</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      _resolve = resolve
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，timerFunc 就是决定何时执行回调函数的关键。<code>pending</code> 表示当前是否有异步任务正在执行，如果没有则立即调用 <code>timerFunc</code> 并修改 <code>pending</code> 为 <code>true</code>，防止重复调用，导致进程阻塞。</p>
<p>调用 <code>timerFunc</code> 会创建一个异步任务，等到这个异步任务结束了，就会去执行callbacks 队列中的函数，并且 <code>pending</code> 置为 <code>false</code> 等待下一个 <code>nextTick</code> 被调用，当 <code>timerFunc</code> 还没结束时，重复调用nextTick只会触发一次执行。</p>
<h2 data-id="heading-2">Vue 如何实现异步任务</h2>
<p>看到这里，已经迫不及待想要知道 timerFunc 如何实现的，还有何时去执行回调函数的了。别急，这里还要先了解一点前置知识，就是浏览器的 <code>Event Loop</code></p>
<h3 data-id="heading-3">Event Loop 事件循环</h3>
<p>我们知道 js 是单线程的，同步任务会被顺序执行，还知道有事件监听器的回调、setTimeout、Promise 等等的异步任务不会被立即执行。那么，js 引擎是如何决定这些异步任务在何时被调用的呢？</p>
<h4 data-id="heading-4">消息队列</h4>
<p>Javascript 运行时包含一个消息队列，用于管理待处理的消息，当一个绑定了事件监听器的事件被触发、或者添加了一个 setTimeout 的回调函数，就会添加一个消息入列，等待被处理。</p>
<h4 data-id="heading-5">任务队列</h4>
<p>每个消息都有一个与之关联的回调函数，放在任务队列中，每次都会从消息队列的队头开始处理消息，并执行与之关联的回调函数，直到回调函数被执行完成。</p>
<h4 data-id="heading-6">任务与微任务</h4>
<p>上面说到，一个（宏）任务与消息相关联，消息被处理时，对应的任务会被执行，如事件触发的回调、使用 setTimeout 添加的任务。</p>
<p>而<strong>微任务</strong>则是独立存放在<strong>微任务队列</strong>中，当一个（宏）任务开始执行，新添加的微任务会被添加到微任务队列，等到任务执行完成后要进行下一轮迭代之前，会依次执行微任务直至微任务队列为空。如果不断添加微任务，就会继续处理直到微任务队列为空，因此，要防止重复添加微任务导致阻塞进程。</p>
<p>（宏）任务：事件监听器触发的回调、setTimeout、setInterval
微任务：Promise、queueMicrotask、MutationObserver</p>
<h4 data-id="heading-7">Event Loop 小结</h4>
<p>结合上面三个概念，可以总结出这几个步骤</p>
<ol>
<li>当一个消息被添加到消息队列，其对应的任务也会被添加到任务队列，js 引擎空闲时取出一个消息开始处理，后面的消息需要等待前面消息执行至完成才会被处理</li>
<li>当消息被处理，其对应的任务也会从任务队列被取出，在此期间新添加的微任务，如创建一个 Promise，就会被添加到微任务队列</li>
<li>等到任务执行至完成，会依次执行微任务直到微任务队列为空</li>
<li>开始处理下一个消息，重复步骤123，这就是事件循环</li>
</ol>
<h3 data-id="heading-8">timerFunc 原理</h3>
<p>了解了事件循环是怎么回事之后，就来看看 timerFunc 的原理，以及执行nextTick回调函数的时机。</p>
<p>从源码中可以看到 Vue 在创建异步任务做了很多兼容处理，依次尝试使用<code>Promise</code>,<code>MutationObserver</code>,<code>setImmediate</code>,<code>setTimeout</code> 来创建异步任务</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> timerFunc

<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Promise</span> !== <span class="hljs-string">'undefined'</span> && isNative(<span class="hljs-built_in">Promise</span>)) &#123;
  <span class="hljs-comment">// ...</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!isIE && <span class="hljs-keyword">typeof</span> MutationObserver !== <span class="hljs-string">'undefined'</span> && (
  isNative(MutationObserver) ||
  <span class="hljs-comment">// PhantomJS and iOS 7.x</span>
  MutationObserver.toString() === <span class="hljs-string">'[object MutationObserverConstructor]'</span>
)) &#123;
  <span class="hljs-comment">// ...</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> setImmediate !== <span class="hljs-string">'undefined'</span> && isNative(setImmediate)) &#123;
  <span class="hljs-comment">// ...</span>
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">Promise.then</h4>
<p>首先判断是否原生支持 Promise，原生 <code>Promise.then</code> 是一个微任务，优先级比（宏）任务高，调用 <code>timerFunc</code> 会添加一个微任务，等到DOM更新完成，下一次事件循环开始之前 <code>flushCallbacks</code> 会被执行</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Promise</span> !== <span class="hljs-string">'undefined'</span> && isNative(<span class="hljs-built_in">Promise</span>)) &#123;
  <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve()
  timerFunc = <span class="hljs-function">() =></span> &#123;
    p.then(flushCallbacks)
    <span class="hljs-comment">// iOS 中奇怪的bug，微任务入列了却没有刷新，直到浏览器需要处理其他一些工作，如定时器，这里用来强制刷新队列</span>
    <span class="hljs-keyword">if</span> (isIOS) <span class="hljs-built_in">setTimeout</span>(noop)
  &#125;
  isUsingMicroTask = <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">MutationObserver</h4>
<p><code>MutationObserver</code> 接收一个回调函数，使用 new 关键字创建并返回一个实例对象，会在指定的DOM发生变化时被调用。</p>
<p><code>MutationObserver</code> 虽然是指定 DOM 发生修改时会被触发，但只是添加一个微任务，并不会立即执行，而是等到所有 DOM 更新完毕才会被执行，因此，Vue 在这个地方只需要创建一个结点去修改它的内容，就可以实现监听了。</p>
<p>这里很巧妙的利用 <code>counter = (counter + 1) % 2</code> 让 counter 在 0/1 之间变化，调用 timerFunc 就会修改 textNode 的内容，等待监听到 textNode 变化就会添加一个微任务，DOM 更新完成之后就调用 <code>flushCallbacks</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> counter = <span class="hljs-number">1</span>
<span class="hljs-keyword">const</span> observer = <span class="hljs-keyword">new</span> MutationObserver(flushCallbacks)
<span class="hljs-keyword">const</span> textNode = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-built_in">String</span>(counter))
observer.observe(textNode, &#123;
  <span class="hljs-attr">characterData</span>: <span class="hljs-literal">true</span>
&#125;)
timerFunc = <span class="hljs-function">() =></span> &#123;
  counter = (counter + <span class="hljs-number">1</span>) % <span class="hljs-number">2</span>
  textNode.data = <span class="hljs-built_in">String</span>(counter)
&#125;
isUsingMicroTask = <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">setImmediate</h4>
<p>该方法用来把一些需要长时间运行的操作放在一个回调函数里，在浏览器完成后面的其他语句后，就立刻执行这个回调函数。</p>
<p>只有 IE10+ 支持，是一个（宏）任务</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">timerFunc = <span class="hljs-function">() =></span> &#123;
  setImmediate(flushCallbacks)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">setTimeout</h4>
<p>备选选项，以上都不支持的情况下，使用 <code>setTimeout</code> 创建异步任务，是个（宏）任务</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">timerFunc = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(flushCallbacks, <span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">flushCallbacks</h3>
<p>如上面所见，Vue 依次尝试使用 <code>Promise.then</code>, <code>MutationObserver</code>, <code>setImmediate</code>, <code>setTimeout</code> 来创建一个异步任务，<code>flushCallbacks</code> 会在DOM更新完成后被执行。</p>
<p><code>flushCallbacks</code> 首先将 pending 修改为 false，等待下一次调用 <code>timerFunc</code>，然后遍历回调函数队列，依次取出回调函数执行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flushCallbacks</span> (<span class="hljs-params"></span>) </span>&#123;
  pending = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">const</span> copies = callbacks.slice(<span class="hljs-number">0</span>)
  callbacks.length = <span class="hljs-number">0</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < copies.length; i++) &#123;
    copies[i]()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">小结</h2>
<p>由于Vue在更新DOM是异步执行的，因此<code>nextTick</code>需要维护一个回调函数队列，等待合适的时机才执行回调函数，这个时机则是利用了事件循环机制，Vue进行异步更新时，新添加一个异步任务，会等到Vue更新完成后被处理，此时回调函数会被依次执行。</p></div>  
</div>
            