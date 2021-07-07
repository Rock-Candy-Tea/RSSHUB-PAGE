
---
title: '我与Microtasks的前世今生之一眼望穿千年'
categories: 
 - 编程
 - 掘金
 - 收藏集
headimg: 'https://user-gold-cdn.xitu.io/2018/10/26/166aeb3cc1b575e5?imageView2/0/w/1280/h/960/ignore-error/1'
author: 掘金
comments: false
date: Thu, 25 Oct 2018 20:49:18 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2018/10/26/166aeb3cc1b575e5?imageView2/0/w/1280/h/960/ignore-error/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>转自IMWeb社区，作者：孙世吉，<a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Fimweb.io%2Ftopic%2F5bb9fd3779ddc80f36592f47" title="http://imweb.io/topic/5bb9fd3779ddc80f36592f47" ref="nofollow noopener noreferrer">原文链接</a></p>
</blockquote>
<p>本文有标题党之嫌，内含大量Microtaks相关总结性信息，请谨慎服用。</p>
<h2 data-id="heading-0">Google Developer Day China 2018 by Jake Archibald</h2>
<p>2018年9月21日，虽然没有参加该场GDD，但是也有幸拜读了百度@小蘑菇小哥总结的文章<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F45111890" title="https://zhuanlan.zhihu.com/p/45111890" ref="nofollow noopener noreferrer">深入浏览器的事件循环(GDD@2018)</a>,配注的说明插图形象生动，文终的click代码也很有意思，推荐大家阅读。这里就先恬不知耻的将该文的精华以及一些自己的总结陈列如下:</p>
<p></p><figure><img src="https://user-gold-cdn.xitu.io/2018/10/26/166aeb3cc1b575e5?imageView2/0/w/1280/h/960/ignore-error/1" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<table>
<thead>
<tr>
<th>异步任务</th>
<th>特点</th>
<th>常见产生处</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tasks (Macrotasks)</td>
<td>- 当次事件循环执行队列内的一个任务<br>- 当次事件循环产生的新任务会在指定时机加入任务队列等待执行</td>
<td>- setTimeout<br>- setInterval<br>- setImmediate<br>- I/O</td>
</tr>
<tr>
<td>Animation callbacks</td>
<td>- 渲染过程(Structure-Layout-Paint)前执行<br>- 当次事件循环<strong>执行队列里的所有任务</strong><br>- 当次事件循环<strong>产生的新任务会在下一次循环执行</strong></td>
<td>- rAF<br></td>
</tr>
<tr>
<td>Microtasks</td>
<td>- 当次事件循环的结尾立即执行的任务<br>- 当次事件循环<strong>执行队列里的所有任务</strong><br>- 当次事件循环<strong>产生的新任务会立即执行</strong></td>
<td>- Promise<br>- Object.observe<br>- MutationObserver<br>- process.nextTick</td>
</tr>
</tbody>
</table>
<h2 data-id="heading-1">直观的感受一下Macrotasks和Microtasks</h2>
<p>看过一篇公众号文章下面的留言:</p>
<blockquote>
<p>那个所谓的mtask和task的区别我并不认同...，我认为事件对列只有一个，就是task。</p>
</blockquote>
<p>特别是对于JS异步编程思维还不太熟悉的同学，比如两年前从java转成javascript后的我，对于这种异步的调用顺序其实很难理解。</p>
<p>不过有一个特别能说明Macrotasks和Microtasks的例子:</p>
<pre><code lang="javascript" class="copyable"><span>// 普通的递归, 造成死循环, 页面无响应</span>
<span><span>function</span> <span>callback</span>(<span></span>) </span>&#123;
    <span>console</span>.log(<span>'callback'</span>);
    callback();
&#125;
callback();
<span class="copy-code-btn">复制代码</span></code></pre><p>上面的代码相信大家非常好理解，一个很简单的递归，由于事件循环得不到释放，UI渲染无法进行导致页面无响应。</p>
<p>通常我们可以使用setTimeout来进行改造，我们把下一次执行放到异步队列里面，不会持久的占用计算资源，这就是我们说的Macrotasks:</p>
<pre><code lang="javascript" class="copyable"><span>// Macrotasks，不会造成死循环</span>
<span><span>function</span> <span>callback</span>(<span></span>) </span>&#123;
  <span>console</span>.log(<span>'callback'</span>);
  setTimeout(callback，<span>0</span>);
&#125;

callback();
<span class="copy-code-btn">复制代码</span></code></pre><p>但是Promise回调产生的Microtasks呢，如下代码，同样会造成死循环。</p>
<p>通过上文我们也可以知道<strong>当次事件循环产生的新Microtasks会立即执行</strong>，同时当次事件循环要等到所有Microtasks队列执行完毕后才会结束。所以当我们的Microtasks在产生新的任务的同时，会导致Microtasks队列一直有任务等待执行，这次事件循环永远不会退出，也就导致了我们的死循环。</p>
<pre><code lang="javascript" class="copyable"><span>// Microtasks，同样会造成死循环，页面无响应</span>
<span><span>function</span> <span>callback</span>(<span></span>) </span>&#123;
  <span>console</span>.log(<span>'callback'</span>);
  <span>Promise</span>.resolve().then(callback);
&#125;
callback();
<span class="copy-code-btn">复制代码</span></code></pre><h2 data-id="heading-2">Microtasks 与 Promise A+</h2>
<p>当然，上文解决了本人关于Microtasks的相关疑虑 (<s>特别是有人拿出一段参杂setTimeout和Promise的代码让你看代码输出顺序时</s>) 的同时，也让我回忆起似乎曾几何时也在哪里看到过关于Microtask的字眼。</p>
<p>经过多日的寻找，终于在以前写过的一片关于Promise的总结文章 <a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Fimweb.io%2Ftopic%2F57a0760393d9938132cc8da9" title="http://imweb.io/topic/57a0760393d9938132cc8da9" ref="nofollow noopener noreferrer">打开Promise的正确姿势</a> 里找到了。该文通过一个实例说明了新建Promise的代码是会立即执行的，并不会放到异步队列里:</p>
<pre><code lang="javascript" class="copyable"><span>var</span> d = <span>new</span> <span>Date</span>();

<span>// 创建一个promise实例，该实例在2秒后进入fulfilled状态</span>
<span>var</span> promise1 = <span>new</span> <span>Promise</span>(<span><span>function</span> (<span>resolve，reject</span>) </span>&#123;
  setTimeout(resolve，<span>2000</span>，<span>'resolve from promise 1'</span>);
&#125;);

<span>// 创建一个promise实例，该实例在1秒后进入fulfilled状态</span>
<span>var</span> promise2 = <span>new</span> <span>Promise</span>(<span><span>function</span> (<span>resolve，reject</span>) </span>&#123;
  setTimeout(resolve，<span>1000</span>，promise1); <span>// resolve(promise1)</span>
&#125;);

promise2.then(
  <span><span>result</span> =></span> <span>console</span>.log(<span>'result:'</span>，result，<span>new</span> <span>Date</span>() - d),
  error => <span>console</span>.log(<span>'error:'</span>，error)
)
<span class="copy-code-btn">复制代码</span></code></pre><p>上面的代码输出</p>
<pre><code lang="bash" class="copyable">result: resolve from promise 1 2002
<span class="copy-code-btn">复制代码</span></code></pre><p>我们得到两点结论:</p>
<ul>
<li>验证了Promise/A+中的<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fpromisesaplus.com%2F%23point-49" title="https://promisesaplus.com/#point-49" ref="nofollow noopener noreferrer">2.3.2规范</a></li>
<li>新建Promise的代码时会立即执行的 (运行时间是2秒而不是3秒)</li>
</ul>
<p>但是当时本人忽略了Promise/A+的相关<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fpromisesaplus.com%2F%23point-67" title="https://promisesaplus.com/#point-67" ref="nofollow noopener noreferrer">注解内容</a>:</p>
<blockquote>
<p>Here “platform code” means engine，environment，and promise implementation code. In practice，this requirement ensures that <code>onFulfilled</code> and <code>onRejected</code> execute asynchronously，after the event loop turn in which <code>then</code> is called，and with a fresh stack. This can be implemented with either a “macro-task” mechanism such as <a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fhtml.spec.whatwg.org%2Fmultipage%2Fwebappapis.html%23timers" title="https://html.spec.whatwg.org/multipage/webappapis.html#timers" ref="nofollow noopener noreferrer"><code>setTimeout</code></a> or <a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fdvcs.w3.org%2Fhg%2Fwebperf%2Fraw-file%2Ftip%2Fspecs%2FsetImmediate%2FOverview.html%23processingmodel" title="https://dvcs.w3.org/hg/webperf/raw-file/tip/specs/setImmediate/Overview.html#processingmodel" ref="nofollow noopener noreferrer"><code>setImmediate</code></a>，or with a “micro-task” mechanism such as <a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fdom.spec.whatwg.org%2F%23interface-mutationobserver" title="https://dom.spec.whatwg.org/#interface-mutationobserver" ref="nofollow noopener noreferrer"><code>MutationObserver</code></a> or <a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.org%2Fapi%2Fprocess.html%23process_process_nexttick_callback" title="http://nodejs.org/api/process.html#process_process_nexttick_callback" ref="nofollow noopener noreferrer"><code>process.nextTick</code></a>. Since the promise implementation is considered platform code，it may itself contain a task-scheduling queue or “trampoline” in which the handlers are called.</p>
</blockquote>
<p>是的，这就是本人与MicroTasks的第一次相遇，没有一见钟情还真是非常抱歉啊。</p>
<p>该注解说明了Promise的 <code>onFulfilled</code> 和 <code>onRejected</code> 回调的执行只要确保是在 <code>then</code>被调用后异步执行就可以了。具体实现成 <a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fhtml.spec.whatwg.org%2Fmultipage%2Fwebappapis.html%23timers" title="https://html.spec.whatwg.org/multipage/webappapis.html#timers" ref="nofollow noopener noreferrer"><code>setTimeout</code></a> 似的 macrotasks 机制或者 <a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.org%2Fapi%2Fprocess.html%23process_process_nexttick_callback" title="http://nodejs.org/api/process.html#process_process_nexttick_callback" ref="nofollow noopener noreferrer"><code>process.nextTick</code></a> 似的microtasks机制都可以，具体视平台代码而定。</p>
<h2 data-id="heading-3">为什么需要Microtasks</h2>
<p>搜索引擎能找到的相关文章基本都指向了一篇<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fjakearchibald.com%2F2015%2Ftasks-microtasks-queues-and-schedules%2F%3Futm_source%3Dhtml5weekly" title="https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/?utm_source=html5weekly" ref="nofollow noopener noreferrer">《Tasks，microtasks，queues and schedules》</a>，也许这就是传说中原罪的发源之地吧。</p>
<blockquote>
<p><strong>Microtasks</strong> are usually scheduled for things that should happen straight after the currently executing script，such as reacting to a batch of actions，or to make something async without taking the penalty of a whole new task.</p>
</blockquote>
<p>简单来说，就是希望对一系列的任务做出回应或者执行异步操作，但是又不想额外付出一整个异步任务的代价。在这种情况下，Microtasks就可以用来调度这些<strong>应当在当前执行脚本结束后立马执行的任务</strong>。</p>
<blockquote>
<p>The microtask queue is processed after callbacks as long as no other JavaScript is mid-execution，and at the end of each task. Any additional microtasks queued during microtasks are added to the end of the queue and also processed.</p>
</blockquote>
<p>单独看Macrotasks和 Microtasks，执行顺序可以总结如下:</p>
<ul>
<li>取出Macrotasks任务队列的一个任务，执行;</li>
<li>取出Microtasks任务队列的所有任务，依次执行;</li>
<li>本次事件循环结束，等待下次事件循环;</li>
</ul>
<p>从这个方面我们也可以理解为什么Promise.then要被实现成Microtasks，回调在实现Promise/A+规范 (必须是异步执行)的基础上，也保证能够更快的被执行，而不是跟Macrotasks一样必须等到下次事件循环才能执行。大家可以重新执行一下上文对比Macrotasks和Microtasks时举的例子，也会发现他们两的单位时间内的执行次数是不一样的。</p>
<p>可以试想一些综合了异步任务和同步任务的的Promise实例，Microtasks可以保证它们更快的得到执行资源，例如:</p>
<pre><code lang="javascript" class="copyable"><span>new</span> <span>Promise</span>(<span>(<span>resolve</span>) =></span> &#123;
  <span>if</span>(<span>/* 检查资源是否需要异步加载 */</span>) &#123;
    <span>return</span> asyncAction().then(resolve);
  &#125;
  <span>// 直接返回加载好的异步资源</span>
  <span>return</span> syncResource;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre><p>如果上面的代码是为了加载远程的资源，那么只有第一次需要执行异步加载，后面的所有执行都可以直接同步读取缓存内容。如果使用Microtasks，我们也就不用每次都等待多一次的事件循环来获取该资源，Promise实例的新建过程是立即执行的，同时<code>onFulfilled</code>回调也是在本次事件循环中全部执行完毕的，减少了切换上下文的成本，提高了性能。</p>
<p>但是呢，从上文关于Promise/A+规范的引用中我们已经知道不同浏览器对于该实现是不一致的。部分浏览器 (越来越少) 将Promise的回调函数实现成了Macrotasks，原因就在于Promise的定义来自ECMAScript而不是HTML。</p>
<blockquote>
<p>A Job is an abstract operation that initiates an ECMAScript computation when no other ECMAScript computation is currently in progress. A Job abstract operation may be defined to accept an arbitrary set of job parameters.</p>
</blockquote>
<p>按照<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.github.io%2Fecma262%2F%23sec-jobs-and-job-queues" title="https://tc39.github.io/ecma262/#sec-jobs-and-job-queues" ref="nofollow noopener noreferrer">ECMAScript的规范</a>，是没有Microtasks的相关定义的，类似的有一个<code>jobs</code> 的概念，和Microtasks很相似.</p>
<h2 data-id="heading-4">相关应用</h2>
<p><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2Fdev%2Fsrc%2Fcore%2Futil%2Fnext-tick.js" title="https://github.com/vuejs/vue/blob/dev/src/core/util/next-tick.js" ref="nofollow noopener noreferrer">Vue - src/core/utils/next-tick.js</a> 中也有相关Macrotask和Microtask的实现</p>
<pre><code lang="javascript" class="copyable"><span>let</span> microTimerFunc
<span>let</span> macroTimerFunc
<span>if</span> (<span>typeof</span> setImmediate !== <span>'undefined'</span> && isNative(setImmediate)) &#123;
  macroTimerFunc = <span><span>()</span> =></span> &#123;
    setImmediate(flushCallbacks)
  &#125;
&#125; <span>else</span> <span>if</span> (<span>typeof</span> MessageChannel !== <span>'undefined'</span> && (
  isNative(MessageChannel) ||
  <span>// PhantomJS</span>
  MessageChannel.toString() === <span>'[object MessageChannelConstructor]'</span>
)) &#123;
  <span>const</span> channel = <span>new</span> MessageChannel()
  <span>const</span> port = channel.port2
  channel.port1.onmessage = flushCallbacks
  macroTimerFunc = <span><span>()</span> =></span> &#123;
    port.postMessage(<span>1</span>)
  &#125;
&#125; <span>else</span> &#123;
  <span>/* istanbul ignore next */</span>
  macroTimerFunc = <span><span>()</span> =></span> &#123;
    setTimeout(flushCallbacks，<span>0</span>)
  &#125;
&#125;
<span>// Determine microtask defer implementation.</span>
<span>/* istanbul ignore next，$flow-disable-line */</span>
<span>if</span> (<span>typeof</span> <span>Promise</span> !== <span>'undefined'</span> && isNative(<span>Promise</span>)) &#123;
  <span>const</span> p = <span>Promise</span>.resolve()
  microTimerFunc = <span><span>()</span> =></span> &#123;
    p.then(flushCallbacks)
    <span>// in problematic UIWebViews，Promise.then doesn't completely break，but</span>
    <span>// it can get stuck in a weird state where callbacks are pushed into the</span>
    <span>// microtask queue but the queue isn't being flushed，until the browser</span>
    <span>// needs to do some other work，e.g. handle a timer. Therefore we can</span>
    <span>// "force" the microtask queue to be flushed by adding an empty timer.</span>
    <span>if</span> (isIOS) setTimeout(noop)
  &#125;
&#125; <span>else</span> &#123;
  <span>// fallback to macro</span>
  microTimerFunc = macroTimerFunc
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><h2 data-id="heading-5">推荐阅读</h2>
<p><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F45111890" title="https://zhuanlan.zhihu.com/p/45111890" ref="nofollow noopener noreferrer">浏览器的 Event Loop</a></p>
<p><a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Fimweb.io%2Ftopic%2F57a0760393d9938132cc8da9" title="http://imweb.io/topic/57a0760393d9938132cc8da9" ref="nofollow noopener noreferrer">打开Promise的正确姿势</a></p>
<p><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fpromisesaplus.com" title="https://promisesaplus.com" ref="nofollow noopener noreferrer">Promise/A+</a></p>
<p><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fjakearchibald.com%2F2015%2Ftasks-microtasks-queues-and-schedules%2F%3Futm_source%3Dhtml5weekly" title="https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/?utm_source=html5weekly" ref="nofollow noopener noreferrer">Tasks，microtasks，queues and schedules</a></p>
</div>  
</div>
            