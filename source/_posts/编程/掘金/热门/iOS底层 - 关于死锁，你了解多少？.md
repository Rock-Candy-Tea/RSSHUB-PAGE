
---
title: 'iOS底层 - 关于死锁，你了解多少？'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57d18729cff84f73a6c267c898f2f987~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 23:26:14 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57d18729cff84f73a6c267c898f2f987~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<pre><code class="hljs language-js copyable" lang="js">写在前面： iOS底层原理探究是本人在平时的开发和学习中不断积累的一段进阶之
路的。 记录我的不断探索之旅，希望能有帮助到各位读者朋友。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">目录如下：</h2>
<ol>
<li><a href="https://juejin.cn/post/6970606949268193288" target="_blank" title="https://juejin.cn/post/6970606949268193288">iOS 底层原理探索 之 alloc</a></li>
<li><a href="https://juejin.cn/post/6971444915775471629" target="_blank" title="https://juejin.cn/post/6971444915775471629">iOS 底层原理探索 之 结构体内存对齐</a></li>
<li><a href="https://juejin.cn/post/6973676242595741726/" target="_blank" title="https://juejin.cn/post/6973676242595741726/">iOS 底层原理探索 之 对象的本质 & isa的底层实现</a></li>
<li><a href="https://juejin.cn/post/6974941925858082829/" target="_blank" title="https://juejin.cn/post/6974941925858082829/">iOS 底层原理探索 之 isa - 类的底层原理结构（上）</a></li>
<li><a href="https://juejin.cn/post/6977673328920100894" target="_blank" title="https://juejin.cn/post/6977673328920100894">iOS 底层原理探索 之 isa - 类的底层原理结构（中）</a></li>
<li><a href="https://juejin.cn/post/6978036844760039432" target="_blank" title="https://juejin.cn/post/6978036844760039432">iOS 底层原理探索 之 isa - 类的底层原理结构（下）</a></li>
<li><a href="https://juejin.cn/post/6978713387848957960" target="_blank" title="https://juejin.cn/post/6978713387848957960">iOS 底层原理探索 之 Runtime运行时&方法的本质</a></li>
<li><a href="https://juejin.cn/post/6979529808896229413" target="_blank" title="https://juejin.cn/post/6979529808896229413">iOS 底层原理探索 之 objc_msgSend</a></li>
<li><a href="https://juejin.cn/post/6980697882659651615" target="_blank" title="https://juejin.cn/post/6980697882659651615">iOS 底层原理探索 之 Runtime运行时慢速查找流程</a></li>
<li><a href="https://juejin.cn/post/6981034592098582541" target="_blank" title="https://juejin.cn/post/6981034592098582541">iOS 底层原理探索 之 动态方法决议</a></li>
<li><a href="https://juejin.cn/post/6983680283543339015" target="_blank" title="https://juejin.cn/post/6983680283543339015">iOS 底层原理探索 之 消息转发流程</a></li>
<li><a href="https://juejin.cn/post/6984330344728100877/" target="_blank" title="https://juejin.cn/post/6984330344728100877/">iOS 底层原理探索 之 应用程序加载原理dyld （上）</a></li>
<li><a href="https://juejin.cn/post/6984722324167753742" target="_blank" title="https://juejin.cn/post/6984722324167753742">iOS 底层原理探索 之 应用程序加载原理dyld （下）</a></li>
<li><a href="https://juejin.cn/post/6985539839798345758" target="_blank" title="https://juejin.cn/post/6985539839798345758">iOS 底层原理探索 之 类的加载</a></li>
<li><a href="https://juejin.cn/post/6986557323137253412" target="_blank" title="https://juejin.cn/post/6986557323137253412">iOS 底层原理探索 之 分类的加载</a></li>
<li><a href="https://juejin.cn/post/6987318200861982751" target="_blank" title="https://juejin.cn/post/6987318200861982751">iOS 底层原理探索 之 关联对象</a></li>
<li><a href="https://juejin.cn/post/6989133476326801415" target="_blank" title="https://juejin.cn/post/6989133476326801415">iOS底层原理探索 之 魔法师KVC</a></li>
<li><a href="https://juejin.cn/post/6991243196458074125" target="_blank" title="https://juejin.cn/post/6991243196458074125">iOS底层原理探索 之 KVO原理｜8月更文挑战</a></li>
<li><a href="https://juejin.cn/post/6991573899926306829" target="_blank" title="https://juejin.cn/post/6991573899926306829">iOS底层原理探索 之 重写KVO｜8月更文挑战</a></li>
<li><a href="https://juejin.cn/post/6992002318229045278" target="_blank" title="https://juejin.cn/post/6992002318229045278">iOS底层原理探索 之 多线程原理｜8月更文挑战</a></li>
<li><a href="https://juejin.cn/post/6993117234697043998" target="_blank" title="https://juejin.cn/post/6993117234697043998">iOS底层原理探索 之 GCD函数和队列</a></li>
<li><a href="https://juejin.cn/post/6992376672913719327" target="_blank" title="https://juejin.cn/post/6992376672913719327">iOS底层原理探索 之 GCD原理（上）</a></li>
</ol>
<hr>
<h4 data-id="heading-1">以上内容的总结专栏</h4>
<ul>
<li><a href="https://juejin.cn/column/6987556760298979358" target="_blank" title="https://juejin.cn/column/6987556760298979358">iOS 底层原理探索 之 阶段总结</a></li>
</ul>
<hr>
<h4 data-id="heading-2">细枝末节整理</h4>
<ul>
<li><a href="https://juejin.cn/column/6990244846300725284" target="_blank" title="https://juejin.cn/column/6990244846300725284">iOS开发 细节整理总结</a></li>
</ul>
<hr>
<h2 data-id="heading-3">前言</h2>
<p>我们从<code>GCD函数和队列</code>的内容中最后的经典案例中关于死锁的案例开始，从死锁的发生开始，看看其产生的本质原因是为什么。话不多说这就开始。</p>
<p>引用我们在<code>GCD函数和队列</code>一文中和死锁相关的内容：</p>
<ul>
<li>创建串行调度队列的解释：</li>
</ul>
<blockquote>
<p>当我们希望任务以特定的顺序执行时，串行队列很有用。串行队列一次只执行一个任务，并且总是从队列的头部拉去任务。我们可以<code>使用串行队列而不是锁来保护共享资源或可变数据结构</code>。与锁不同，串行队列确保任务以可以预测的顺序执行。而且 <strong>只要我们将任务异步提交到串行队列，队列就永远不会<code>死锁</code></strong>。</p>
</blockquote>
<ul>
<li>在将单个任务添加到队列中的解释：</li>
</ul>
<blockquote>
<p>有两种方法可以将任务添加到队列中：异步或同步。如果可能，使用<code>dispatch_async</code>和<code>dispatch_async_f</code>函数的异步执行优先于同步替代方案。当您将<a href="https://link.juejin.cn/?target=" target="_blank" title="https://link.juejin.cn?target=">块对象</a>或函数添加到队列时，无法知道该代码何时执行。因此，异步添加块或函数可让您安排代码的执行并继续从调用线程执行其他工作。如果您从应用程序的主线程调度任务，这尤其重要——也许是为了响应某些用户事件。</p>
<p>尽管您应该尽可能以异步方式添加任务，但有时您仍可能需要同步添加任务以防止竞争条件或其他同步错误。在这些情况下，您可以使用<code>dispatch_sync</code>和<code>dispatch_sync_f</code>函数将任务添加到队列中。这些函数会阻塞当前的执行线程，直到指定的任务完成执行。</p>
<p><strong>重要提示：</strong> 您永远不应从在您计划传递给函数的同一队列中执行的任务调用<code>dispatch_sync</code>或<code>dispatch_sync_f</code>函数。<strong><code>这对于保证死锁的串行队列尤其重要，但对于并发队列也应避免</code></strong>。</p>
</blockquote>
<p>以上两部分内容，是在阐述串行队列的概念解释和将任务添加到队列中的两种方式的规范内容。总的来说，是帮助我们在正确使用串行队列，以及在将任务添加到队列中时，避免<code>死锁</code>的发生。</p>
<p>下面，我们从案例中的死锁开始。</p>
<h2 data-id="heading-4">死锁的发生</h2>
<p>正如上面的重要提示中锁阐述的一样，我们永远不应该将函数添加到队列中执行任务时使用同步的方式。这对于保证死锁的串行队列尤其重要，但对于并发队列也应避免。</p>
<p>的确，这是避免死锁的重要思路，但是，还是难以避免，在实际开发中，我们使用了下面的代码：</p>
<h3 data-id="heading-5">串行队列，同步函数中同步函数</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57d18729cff84f73a6c267c898f2f987~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第180行，我们的程序发生来死锁，从堆栈的信息中可以看到是 ：</p>
<p>libdispatch.dylib<code>_dispatch_sync_f_slow:</code> -> libdispatch.dylib<code>__DISPATCH_WAIT_FOR_QUEUE__</code>:</p>
<h4 data-id="heading-6">跟踪流程</h4>
<p>在180行，打上断点。在<code>GCD函数和队列</code>篇章中，我们知道dispatch_syn函数的执行流程如下：</p>
<p><strong>dispatch_sync -> _dispatch_sync_f -> _dispatch_sync_f_inline</strong></p>
<p>在_dispatch_sync_f_inline中，有五条分支，我们分别下五个符号断点：</p>
<h4 data-id="heading-7"><strong>_dispatch_sync_f_inline</strong></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> inline <span class="hljs-keyword">void</span>
<span class="hljs-function"><span class="hljs-title">_dispatch_sync_f_inline</span>(<span class="hljs-params">dispatch_queue_t dq, <span class="hljs-keyword">void</span> *ctxt,
dispatch_function_t func, uintptr_t dc_flags</span>)</span>
&#123;
<span class="hljs-keyword">if</span> (likely(dq->dq_width == <span class="hljs-number">1</span>)) &#123;
<span class="hljs-keyword">return</span> _dispatch_barrier_sync_f(dq, ctxt, func, dc_flags);
&#125;

<span class="hljs-keyword">if</span> (unlikely(dx_metatype(dq) != _DISPATCH_LANE_TYPE)) &#123;
DISPATCH_CLIENT_CRASH(<span class="hljs-number">0</span>, <span class="hljs-string">"Queue type doesn't support dispatch_sync"</span>);
&#125;

dispatch_lane_t dl = upcast(dq)._dl;
<span class="hljs-comment">// 全局并发队列和绑定到非分派线程的队列</span>
<span class="hljs-comment">// 总是落在慢的情况下 DISPATCH_ROOT_QUEUE_STATE_INIT_VALUE</span>
<span class="hljs-keyword">if</span> (unlikely(!_dispatch_queue_try_reserve_sync_width(dl))) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_f_slow(dl, ctxt, func, <span class="hljs-number">0</span>, dl, dc_flags);
&#125;

<span class="hljs-keyword">if</span> (unlikely(dq->do_targetq->do_targetq)) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_recurse(dl, ctxt, func, dc_flags);
&#125;
_dispatch_introspection_sync_begin(dl);
_dispatch_sync_invoke_and_complete(dl, ctxt, func DISPATCH_TRACE_ARG(
_dispatch_trace_item_sync_push_pop(dq, ctxt, func, dc_flags)));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先来到了  <code>_dispatch_barrier_sync_f</code> 分支</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e255d66266df4d8fb69341686d63f5e8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">_dispatch_barrier_sync_f</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
<span class="hljs-function"><span class="hljs-title">_dispatch_barrier_sync_f</span>(<span class="hljs-params">dispatch_queue_t dq, <span class="hljs-keyword">void</span> *ctxt,
dispatch_function_t func, uintptr_t dc_flags</span>)</span>
&#123;
_dispatch_barrier_sync_f_inline(dq, ctxt, func, dc_flags);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再下 <code>_dispatch_barrier_sync_f_inline</code> 符号断点， 很遗憾没有断住，直接来到了 <code>_dispatch_sync_f_slow</code> :</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a296ab599c2406d96c4c9e131519b72~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们来到 <code>_dispatch_barrier_sync_f_inline</code> 内部的实现：</p>
<h4 data-id="heading-9"><strong>_dispatch_barrier_sync_f_inline</strong></h4>
<pre><code class="hljs language-js copyable" lang="js">DISPATCH_ALWAYS_INLINE
<span class="hljs-keyword">static</span> inline <span class="hljs-keyword">void</span>
<span class="hljs-function"><span class="hljs-title">_dispatch_barrier_sync_f_inline</span>(<span class="hljs-params">dispatch_queue_t dq, <span class="hljs-keyword">void</span> *ctxt,
dispatch_function_t func, uintptr_t dc_flags</span>)</span>
&#123;
dispatch_tid tid = _dispatch_tid_self();

<span class="hljs-keyword">if</span> (unlikely(dx_metatype(dq) != _DISPATCH_LANE_TYPE)) &#123;
DISPATCH_CLIENT_CRASH(<span class="hljs-number">0</span>, <span class="hljs-string">"Queue type doesn't support dispatch_sync"</span>);
&#125;

dispatch_lane_t dl = upcast(dq)._dl;
<span class="hljs-comment">// 更正确的做法是合并线程的qos</span>
<span class="hljs-comment">// 刚刚获得了进入队列状态的barrier锁。</span>
<span class="hljs-comment">//</span>
<span class="hljs-comment">// 然而，这对于快速路径来说太昂贵了，所以跳过它。</span>
<span class="hljs-comment">// 选择的权衡是，如果队列在较低优先级的线程上</span>
<span class="hljs-comment">// 与此快速路径，此线程可能收到无用的覆盖。</span>
<span class="hljs-comment">//</span>
<span class="hljs-comment">// 全局并发队列和绑定到非分派线程的队列</span>
<span class="hljs-comment">// 总是落在慢的情况下 DISPATCH_ROOT_QUEUE_STATE_INIT_VALUE</span>
<span class="hljs-keyword">if</span> (unlikely(!_dispatch_queue_try_acquire_barrier_sync(dl, tid))) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_f_slow(dl, ctxt, func, DC_FLAG_BARRIER, dl,
DC_FLAG_BARRIER | dc_flags);
&#125;

<span class="hljs-keyword">if</span> (unlikely(dl->do_targetq->do_targetq)) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_recurse(dl, ctxt, func,
DC_FLAG_BARRIER | dc_flags);
&#125;
_dispatch_introspection_sync_begin(dl);
_dispatch_lane_barrier_sync_invoke_and_complete(dl, ctxt, func
DISPATCH_TRACE_ARG(_dispatch_trace_item_sync_push_pop(
dq, ctxt, func, dc_flags | DC_FLAG_BARRIER)));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(_dispatch_sync_f_inline 和 _dispatch_barrier_sync_f_inline 内部实现有点相似)</p>
<p>其内部的第二个分支便是调用 <code>_dispatch_sync_f_slow</code></p>
<h4 data-id="heading-10"><strong>_dispatch_sync_f_slow</strong></h4>
<pre><code class="hljs language-js copyable" lang="js">DISPATCH_NOINLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
<span class="hljs-function"><span class="hljs-title">_dispatch_sync_f_slow</span>(<span class="hljs-params">dispatch_queue_class_t top_dqu, <span class="hljs-keyword">void</span> *ctxt,
dispatch_function_t func, uintptr_t top_dc_flags,
dispatch_queue_class_t dqu, uintptr_t dc_flags</span>)</span>
&#123;
dispatch_queue_t top_dq = top_dqu._dq;
dispatch_queue_t dq = dqu._dq;
<span class="hljs-keyword">if</span> (unlikely(!dq->do_targetq)) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_function_invoke(dq, ctxt, func);
&#125;

pthread_priority_t pp = _dispatch_get_priority();
struct dispatch_sync_context_s dsc = &#123;
.dc_flags    = DC_FLAG_SYNC_WAITER | dc_flags,
.dc_func     = _dispatch_async_and_wait_invoke,
.dc_ctxt     = &dsc,
.dc_other    = top_dq,
.dc_priority = pp | _PTHREAD_PRIORITY_ENFORCE_FLAG,
.dc_voucher  = _voucher_get(),
.dsc_func    = func,
.dsc_ctxt    = ctxt,
.dsc_waiter  = _dispatch_tid_self(),
&#125;;

_dispatch_trace_item_push(top_dq, &dsc);
__DISPATCH_WAIT_FOR_QUEUE__(&dsc, dq);

<span class="hljs-keyword">if</span> (dsc.dsc_func == NULL) &#123;
<span class="hljs-comment">// dsc_func being cleared means that the block ran on another thread ie.</span>
<span class="hljs-comment">// case (2) as listed in _dispatch_async_and_wait_f_slow.</span>
dispatch_queue_t stop_dq = dsc.dc_other;
<span class="hljs-keyword">return</span> _dispatch_sync_complete_recurse(top_dq, stop_dq, top_dc_flags);
&#125;

_dispatch_introspection_sync_begin(top_dq);
_dispatch_trace_item_pop(top_dq, &dsc);
_dispatch_sync_invoke_and_complete_recurse(top_dq, ctxt, func,top_dc_flags
DISPATCH_TRACE_ARG(&dsc));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到其实现内容，依然会觉得和上面两个（_dispatch_sync_f_inline 和 _dispatch_barrier_sync_f_inline） 有点相似。
再次根据分支下符号断点，就断不住了，直接会崩溃，根据堆栈，我们会来到：
<code>__DISPATCH_WAIT_FOR_QUEUE__(&dsc, dq)</code> 的执行。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40ed0e370d49453085f806beff88f187~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14ea9382bdf34ad5a5b45b41e10d7166~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">最终奔溃的点</h3>
<h4 data-id="heading-12"><strong><code>__DISPATCH_WAIT_FOR_QUEUE__</code></strong></h4>
<pre><code class="hljs language-js copyable" lang="js">DISPATCH_NOINLINE
<span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
<span class="hljs-function"><span class="hljs-title">__DISPATCH_WAIT_FOR_QUEUE__</span>(<span class="hljs-params">dispatch_sync_context_t dsc, dispatch_queue_t dq</span>)</span>
&#123;
    uint64_t dq_state = _dispatch_wait_prepare(dq);
    <span class="hljs-keyword">if</span> (unlikely(_dq_state_drain_locked_by(dq_state, dsc->dsc_waiter))) &#123;
            DISPATCH_CLIENT_CRASH((uintptr_t)dq_state,
                            <span class="hljs-string">"dispatch_sync called on queue "</span>
                            <span class="hljs-string">"already owned by current thread"</span>);
    &#125;
    
    ...
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>程序崩溃在这里，那么，我们就需要重点分析下这里的 if 判断条件是什么？符合了怎样的条件，以至于程序崩溃的发生。</p>
<p>函数对比的两个内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1、当前的队列线程的线程ID</span>
#define _dispatch_tid_self() ((dispatch_tid)_dispatch_thread_port())

#define _dispatch_thread_port() pthread_mach_thread_np(_dispatch_thread_self())

#define _dispatch_thread_self() ((uintptr_t)pthread_self())

<span class="hljs-comment">// 2、队列的状态</span>
 _dispatch_wait_prepare(dq);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_dq_state_drain_locked_by</code></p>
<pre><code class="hljs language-js copyable" lang="js">ISPATCH_ALWAYS_INLINE
<span class="hljs-keyword">static</span> inline bool
<span class="hljs-function"><span class="hljs-title">_dq_state_drain_locked_by</span>(<span class="hljs-params">uint64_t dq_state, dispatch_tid tid</span>)</span>
&#123;
<span class="hljs-keyword">return</span> _dispatch_lock_is_locked_by((dispatch_lock)dq_state, tid);
&#125;

#define DLOCK_OWNER_MASK ((dispatch_lock)<span class="hljs-number">0xfffffffc</span>)

DISPATCH_ALWAYS_INLINE
<span class="hljs-keyword">static</span> inline bool
<span class="hljs-function"><span class="hljs-title">_dispatch_lock_is_locked_by</span>(<span class="hljs-params">dispatch_lock lock_value, dispatch_tid tid</span>)</span>
&#123;
<span class="hljs-comment">// equivalent to _dispatch_lock_owner(lock_value) == tid</span>
        <span class="hljs-comment">// DLOCK_OWNER_MASK 是一个很大的数 ((dispatch_lock)0xfffffffc)</span>
        <span class="hljs-comment">// 前面的结果只要不为0 与上 DLOCK_OWNER_MASK 也不为0</span>
        <span class="hljs-comment">// 如果前面的结果与上DLOCK_OWNER_MASK结果为0 那前面的结果 必然为0</span>
        <span class="hljs-comment">// 最终， lock_value 和 tid 相同 才会 为 0</span>
<span class="hljs-keyword">return</span> ((lock_value ^ tid) & DLOCK_OWNER_MASK) == <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">总结</h2>
<p>最后， 本来这个锁住要等待的线程的状态和我们的线程ID相同。也就是我们的线程本来应该在等待状态，然而这个时候，又调用了线程的队列来添加任务，告诉系统要调起此线程，结果在我们的系统中此线程又是等待的状态。所以，此次添加任务是无法实现的。</p>
<p>在这里，又要调起线程，然后线程又是等待状态，此时就是一个矛盾，无法继续执行下去，所以就发生了<code>死锁</code>。</p></div>  
</div>
            