
---
title: 'OC底层原理探索之GCD源码分析下篇'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cf14fae36bb4b988011428779a66499~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 00:59:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cf14fae36bb4b988011428779a66499~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">同步函数死锁</h4>
<p>主线程因为你同步函数的原因等着先执⾏任务</p>
<p>主队列等着主线程的任务执⾏完毕再执⾏⾃⼰的任务
主队列和主线程相互等待会造成死锁</p>
<pre><code class="hljs language-c copyable" lang="c">- (<span class="hljs-keyword">void</span>)textDemo2&#123;
    <span class="hljs-comment">// </span>
    <span class="hljs-keyword">dispatch_queue_t</span> <span class="hljs-built_in">queue</span> = dispatch_queue_create(<span class="hljs-string">"cooci"</span>, DISPATCH_QUEUE_SERIAL);
    NSLog(@<span class="hljs-string">"1"</span>);
    <span class="hljs-comment">// 异步函数</span>
    dispatch_async(<span class="hljs-built_in">queue</span>, ^&#123;
        NSLog(@<span class="hljs-string">"2"</span>);
        <span class="hljs-comment">// 串行队列和同步函数会造成死锁问题，本题是这个原因，但是不能说串行队列和同步函数一定会造成死锁问题</span>
        dispatch_sync(<span class="hljs-built_in">queue</span>, ^&#123;
        &#125;);
    &#125;);
    NSLog(@<span class="hljs-string">"5"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面造成死锁之后，bt一下看下调用栈
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cf14fae36bb4b988011428779a66499~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们顺着源码也来分析下：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">void</span>
<span class="hljs-title">dispatch_sync</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">dispatch_block_t</span> work)</span>
</span>&#123;
<span class="hljs-keyword">uintptr_t</span> dc_flags = DC_FLAG_BLOCK;
<span class="hljs-keyword">if</span> (unlikely(_dispatch_block_has_private_data(work))) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_block_with_privdata(dq, work, dc_flags);
&#125;
_dispatch_sync_f(dq, work, _dispatch_Block_invoke(work), dc_flags);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个流程比较熟悉，我们上一篇也讲过， <code>_dispatch_sync_f</code> -> <code>_dispatch_sync_f_inline</code>在这个函数中我们知道，同步函数的<code>dq_width  = 1</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">if</span> (likely(dq->dq_width == <span class="hljs-number">1</span>)) &#123;
<span class="hljs-keyword">return</span> _dispatch_barrier_sync_f(dq, ctxt, func, dc_flags);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以我们定位到了<code>_dispatch_barrier_sync_f</code> -> <code>_dispatch_barrier_sync_f_inline</code>
我们看下上面的死锁时候的调用栈，发现有个<code>_dispatch_sync_f_slow</code>,好的那么我们就在<code>_dispatch_barrier_sync_f_inline</code>中定位到<code>_dispatch_sync_f_slow</code>发现了报错的时候的函数<code>__DISPATCH_WAIT_FOR_QUEUE__</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
__DISPATCH_WAIT_FOR_QUEUE__(<span class="hljs-keyword">dispatch_sync_context_t</span> dsc, <span class="hljs-keyword">dispatch_queue_t</span> dq)
&#123;
<span class="hljs-keyword">uint64_t</span> dq_state = _dispatch_wait_prepare(dq);
    <span class="hljs-comment">// 第二个参数   .dsc_waiter  = _dispatch_tid_self()也就是线程的id</span>
<span class="hljs-keyword">if</span> (unlikely(_dq_state_drain_locked_by(dq_state, dsc->dsc_waiter))) &#123;
DISPATCH_CLIENT_CRASH((<span class="hljs-keyword">uintptr_t</span>)dq_state,
<span class="hljs-string">"dispatch_sync called on queue "</span>
<span class="hljs-string">"already owned by current thread"</span>);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_dq_state_drain_locked_by(dq_state, dsc->dsc_waiter)</code>这里的第二个参数 <code>.dsc_waiter  = _dispatch_tid_self()</code>也就是线程的id</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> _dispatch_tid_self()((dispatch_tid)_dispatch_thread_port())</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_dq_state_drain_locked_by</code> -> <code>_dispatch_lock_is_locked_by</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">bool</span>
_dispatch_lock_is_locked_by(dispatch_lock lock_value, dispatch_tid tid)
&#123;
<span class="hljs-comment">// equivalent to _dispatch_lock_owner(lock_value) == tid</span>
<span class="hljs-keyword">return</span> ((lock_value ^ tid) & DLOCK_OWNER_MASK) == <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>DLOCK_OWNER_MASK</code>是一个极大值，意思是说只要<code>lock_value ^ tid</code> 不为0，那么这个就不成立。相反如果要成立的话，也就是死锁的话，<code>lock_value ^ tid = 0</code>那么异或的两个值什么情况下为0呢，答案当然是相等。也就是说当前等待线程的tid和当前准备要调用的线程tid相等就会造成死锁</p>
<h4 data-id="heading-1">同步函数 + 全局队列</h4>
<p><code>dispatch_sync</code> + <code>global_queue</code></p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">   <span class="hljs-built_in">dispatch_queue_t</span> queue1 = dispatch_get_global_queue(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
   <span class="hljs-built_in">dispatch_sync</span>(queue1, ^&#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@"</span>,[<span class="hljs-built_in">NSThread</span> currentThread]);
   &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时bt一下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76cdbf6d9e3344c5806b97e44762dff8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们可以在第三行的时候下符号断点，在<code>_dispatch_sync_f_inline</code>函数中
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79899d3da7af4d57988020045d0e5c83~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在工程中符号断点这3个方法
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ee283916181471bbf36c8b27e380109~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
发现来到了这个方法结合上面bt的调用栈发现<code>_dispatch_sync_function_invoke</code>这个方法。接下来的流程就比较简单了。<code>_dispatch_sync_function_invoke</code> -> <code>_dispatch_sync_function_invoke_inline</code> -><code>_dispatch_client_callout</code>
​</p>
<h4 data-id="heading-2">异步函数 + 全局队列/并发队列</h4>
<p><code>dispatch_async</code> + <code>DISPATCH_QUEUE_CONCURRENT</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1498c50ad3c745d697fe89588f71c1cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>dispatch_async</code> + <code>global_queue</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b379589982534cecab3215535e51287f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">void</span>
<span class="hljs-title">dispatch_async</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">dispatch_block_t</span> work)</span>
</span>&#123;
<span class="hljs-keyword">dispatch_continuation_t</span> dc = _dispatch_continuation_alloc();
<span class="hljs-keyword">uintptr_t</span> dc_flags = DC_FLAG_CONSUME;
<span class="hljs-keyword">dispatch_qos_t</span> qos;

qos = _dispatch_continuation_init(dc, dq, work, <span class="hljs-number">0</span>, dc_flags);
_dispatch_continuation_async(dq, dc, qos, dc->dc_flags);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>dispatch_async</code> -> <code>_dispatch_continuation_async</code> -> <code>dx_push</code>这个流程比较熟悉上一篇已经讲过的。<code>.dq_push        = _dispatch_root_queue_push</code></p>
<pre><code class="hljs language-c copyable" lang="c">DISPATCH_VTABLE_SUBCLASS_INSTANCE(queue_concurrent, lane,
.do_type        = DISPATCH_QUEUE_CONCURRENT_TYPE,
.do_dispose     = _dispatch_lane_dispose,
.do_debug       = _dispatch_queue_debug,
.do_invoke      = _dispatch_lane_invoke,

.dq_activate    = _dispatch_lane_activate,
.dq_wakeup      = _dispatch_lane_wakeup,
.dq_push        = _dispatch_lane_concurrent_push,
);

DISPATCH_VTABLE_SUBCLASS_INSTANCE(queue_global, lane,
.do_type        = DISPATCH_QUEUE_GLOBAL_ROOT_TYPE,
.do_dispose     = _dispatch_object_no_dispose,
.do_debug       = _dispatch_queue_debug,
.do_invoke      = _dispatch_object_no_invoke,

.dq_activate    = _dispatch_queue_no_activate,
.dq_wakeup      = _dispatch_root_queue_wakeup,
.dq_push        = _dispatch_root_queue_push,
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里全局队列对应的是<code>_dispatch_root_queue_push</code>,并发队列对应的是<code>dispatch_lane_concurrent_push</code>，全局队列对应的是<code>_dispatch_root_queue_push</code>，我们先看复杂一点的并发队列吧</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">void</span>
_dispatch_lane_concurrent_push(<span class="hljs-keyword">dispatch_lane_t</span> dq, <span class="hljs-keyword">dispatch_object_t</span> dou,
<span class="hljs-keyword">dispatch_qos_t</span> qos)
&#123;
<span class="hljs-comment">// <rdar://problem/24738102&24743140> reserving non barrier width</span>
<span class="hljs-comment">// doesn't fail if only the ENQUEUED bit is set (unlike its barrier</span>
<span class="hljs-comment">// width equivalent), so we have to check that this thread hasn't</span>
<span class="hljs-comment">// enqueued anything ahead of this call or we can break ordering</span>
<span class="hljs-keyword">if</span> (dq->dq_items_tail == <span class="hljs-literal">NULL</span> &&
!_dispatch_object_is_waiter(dou) &&
!_dispatch_object_is_barrier(dou) &&
_dispatch_queue_try_acquire_async(dq)) &#123;
<span class="hljs-keyword">return</span> _dispatch_continuation_redirect_push(dq, dou, qos);
&#125;

_dispatch_lane_push(dq, dou, qos);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_dispatch_lane_push</code>这个其实也是串行队列的<code>.dq_push</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">void</span>
_dispatch_lane_push(<span class="hljs-keyword">dispatch_lane_t</span> dq, <span class="hljs-keyword">dispatch_object_t</span> dou,
<span class="hljs-keyword">dispatch_qos_t</span> qos)
&#123;
<span class="hljs-comment">//...</span>
<span class="hljs-keyword">if</span> (unlikely(_dispatch_object_is_waiter(dou))) &#123;
<span class="hljs-keyword">return</span> _dispatch_lane_push_waiter(dq, dou._dsc, qos);
&#125;

<span class="hljs-comment">//...</span>
<span class="hljs-keyword">if</span> (flags) &#123;
<span class="hljs-keyword">return</span> dx_wakeup(dq, qos, flags);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这里面其实只有两个<code>return</code>,在demo中下符号断点。<code>dx_wakeup</code>全局搜索定位到是一个宏</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> dx_wakeup(x, y, z) dx_vtable(x)->dq_wakeup(x, y, z)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>搜索<code>dq_wakeup</code>,由于现在研究的是并发队列所以<code>.dq_wakeup      = _dispatch_lane_wakeup,</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dfb1658bfb74879862a2ef46859f89c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
由符号断点可以知道并没有走<code>_dispatch_lane_push_waiter</code>这个方法，所以异步并发流程链路应该是：<code>dispatch_async</code> -> <code>_dispatch_continuation_async</code> -> <code>dx_push</code> -> <code>_dispatch_lane_concurrent_push</code> -> <code>_dispatch_lane_push</code> -> <code>dx_wakeup</code> -> <code>_dispatch_lane_wakeup</code> -> <code>_dispatch_queue_wakeup</code>
在<code>_dispatch_queue_wakeup</code>中一共有四个函数返回，我们分别下符号断点
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fef296b2e094a6ea7b4fa517422e2df~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在<code>_dispatch_lane_class_barrier_complete</code>中发现已经到了系统级别的函数了。我们知道全局队列的<code>.dq_push  = _dispatch_root_queue_push</code>我们试着下个断点，发现确实走到了这一步。所以可以这么总结：手动系统创建的并发队列<code>_dispatch_lane_concurrent_push</code>经过一段复杂的逻辑计算之后合流到了全局并发队列<code>_dispatch_root_queue_push</code>这里。这也从侧方便验证了全局队列是一种特殊的并发队列。
<code>_dispatch_root_queue_push_inline</code> -> <code>_dispatch_root_queue_poke</code> -> <code>_dispatch_root_queue_poke_slow</code> -> <code>_dispatch_root_queues_init</code>
说到这个<code>_dispatch_root_queues_init</code>就适当插入另外的一个单例知识
​</p>
<h4 data-id="heading-3">单例底层原理</h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_root_queues_init(<span class="hljs-keyword">void</span>)
&#123;
dispatch_once_f(&_dispatch_root_queues_pred, <span class="hljs-literal">NULL</span>,
_dispatch_root_queues_init_once);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是单例，我们上层调用的<code>dispatch_once</code>底层就是<code>dispatch_once_f</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">void</span>
<span class="hljs-title">dispatch_once</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_once_t</span> *val, <span class="hljs-keyword">dispatch_block_t</span> block)</span>
</span>&#123;
dispatch_once_f(val, block, _dispatch_Block_invoke(block));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">void</span>
<span class="hljs-title">dispatch_once_f</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_once_t</span> *val, <span class="hljs-keyword">void</span> *ctxt, <span class="hljs-keyword">dispatch_function_t</span> func)</span>
</span>&#123;
<span class="hljs-keyword">dispatch_once_gate_t</span> l = (<span class="hljs-keyword">dispatch_once_gate_t</span>)val;

<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> !DISPATCH_ONCE_INLINE_FASTPATH || DISPATCH_ONCE_USE_QUIESCENT_COUNTER</span>
<span class="hljs-keyword">uintptr_t</span> v = os_atomic_load(&l->dgo_once, acquire);
<span class="hljs-keyword">if</span> (likely(v == DLOCK_ONCE_DONE)) &#123;
<span class="hljs-keyword">return</span>;
&#125;
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> DISPATCH_ONCE_USE_QUIESCENT_COUNTER</span>
<span class="hljs-keyword">if</span> (likely(DISPATCH_ONCE_IS_GEN(v))) &#123;
<span class="hljs-keyword">return</span> _dispatch_once_mark_done_if_quiesced(l, v);
&#125;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-keyword">if</span> (_dispatch_once_gate_tryenter(l)) &#123;
<span class="hljs-keyword">return</span> _dispatch_once_callout(l, ctxt, func);
&#125;
<span class="hljs-keyword">return</span> _dispatch_once_wait(l);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一次调用的时候会来到<code>_dispatch_once_gate_tryenter(l)</code>那里，<code>_dispatch_once_gate_tryenter</code>进行一些原子操作加锁当前的线程，所以单例也是线程安全的<code>_dispatch_lock_value_for_self()</code>,<code>_dispatch_once_callout</code> -> <code>_dispatch_once_gate_broadcast</code> -> <code>_dispatch_once_mark_done</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">uintptr_t</span>
_dispatch_once_mark_done(<span class="hljs-keyword">dispatch_once_gate_t</span> dgo)
&#123;
<span class="hljs-keyword">return</span> os_atomic_xchg(&dgo->dgo_once, DLOCK_ONCE_DONE, release);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里全局标记<code>DLOCK_ONCE_DONE</code>所以下次进入的时候直接到了上面的<code>likely(v == DLOCK_ONCE_DONE</code>代码<code>return</code>
​</p>
<h4 data-id="heading-4">异步函数 + 全局队列/并发队列</h4>
<p>回到上面的流程，这里意思就是让<code>_dispatch_root_queues_init_once</code>这个函数只执行一次，那么<code>_dispatch_root_queues_init_once</code>做了什么？我们在这里发现了<code>_dispatch_worker_thread2</code>为了方便阅读，把之前异步并发的调用栈再贴一下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d771028951174879a8823304c706941e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看出下面就到了<code>libsystem_pthread.dylib</code>下层api，也就是说GCD就是在pthread之上封装改变而来。回到之前的函数</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
_dispatch_root_queue_poke_slow(<span class="hljs-keyword">dispatch_queue_global_t</span> dq, <span class="hljs-keyword">int</span> n, <span class="hljs-keyword">int</span> <span class="hljs-built_in">floor</span>)
&#123;
<span class="hljs-comment">//从外面传递的参数知道 n=1,floor=0</span>
    <span class="hljs-keyword">int</span> remaining = n;
_dispatch_root_queues_init();
 <span class="hljs-comment">// ...</span>
<span class="hljs-keyword">int</span> can_request, t_count;
t_count = os_atomic_load2o(dq, dgq_thread_pool_size, ordered);
<span class="hljs-keyword">do</span> &#123;
        <span class="hljs-comment">// 剩下的可获取的线程数量</span>
can_request = t_count < <span class="hljs-built_in">floor</span> ? <span class="hljs-number">0</span> : t_count - <span class="hljs-built_in">floor</span>;
        <span class="hljs-comment">// 需要的数量 > 剩下的数量 报异常</span>
<span class="hljs-keyword">if</span> (remaining > can_request) &#123;
_dispatch_root_queue_debug(<span class="hljs-string">"pthread pool reducing request from %d to %d"</span>,
remaining, can_request);
os_atomic_sub2o(dq, dgq_pending, remaining - can_request, relaxed);
remaining = can_request;
&#125;
<span class="hljs-keyword">if</span> (remaining == <span class="hljs-number">0</span>) &#123;
_dispatch_root_queue_debug(<span class="hljs-string">"pthread pool is full for root queue: "</span>
<span class="hljs-string">"%p"</span>, dq);
<span class="hljs-keyword">return</span>;
&#125;
&#125; <span class="hljs-keyword">while</span> (!os_atomic_cmpxchgv2o(dq, dgq_thread_pool_size, t_count,
t_count - remaining, &t_count, acquire));
<span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里面的do whlie循环<code>dgq_thread_pool_size</code> = 1,而上一篇提到过线程数量</p>
<pre><code class="hljs language-c copyable" lang="c">  _dispatch_queue_init(dq, dqf, dqai.dqai_concurrent ?
      DISPATCH_QUEUE_WIDTH_MAX : <span class="hljs-number">1</span>, DISPATCH_QUEUE_ROLE_INNER |
      (dqai.dqai_inactive ? DISPATCH_QUEUE_INACTIVE : <span class="hljs-number">0</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> DISPATCH_QUEUE_WIDTH_POOL (DISPATCH_QUEUE_WIDTH_FULL - 1)</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> DISPATCH_QUEUE_WIDTH_MAX  (DISPATCH_QUEUE_WIDTH_FULL - 2)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以这里的<code>DISPATCH_QUEUE_WIDTH_POOL</code> - <code>DISPATCH_QUEUE_WIDTH_MAX</code> = 1</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_queue_global_s</span> _<span class="hljs-title">dispatch_mgr_root_queue</span> =</span> &#123;
.dq_atomic_flags = DQF_WIDTH(DISPATCH_QUEUE_WIDTH_POOL),
.dgq_thread_pool_size = <span class="hljs-number">1</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以从这里可以得出：
全局并发队列<code>dq_atomic_flags</code> - <code>_dispatch_queue_init</code>创建的并发队列<code>dq_atomic_flags</code> =1
全局并发队列<code>.dgq_thread_pool_size =1</code>，而创建的并发队列<code>.dgq_thread_pool_size=0</code>
所以上面的do  while就是线程池调度的规则。那么到底可以开辟多少线程呢？
​</p>
<h4 data-id="heading-5">dgq_thread_pool_size 线程池大小</h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_root_queue_init_pthread_pool(<span class="hljs-keyword">dispatch_queue_global_t</span> dq,
<span class="hljs-keyword">int</span> pool_size, <span class="hljs-keyword">dispatch_priority_t</span> pri)
&#123; 
    <span class="hljs-comment">//...</span>
<span class="hljs-keyword">int</span> thread_pool_size = DISPATCH_WORKQ_MAX_PTHREAD_COUNT;
dq->dgq_thread_pool_size = thread_pool_size;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> DISPATCH_WORKQ_MAX_PTHREAD_COUNT 255</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是线程池的最大数量是255
查找苹果官方文档pthread说明，512kb的大小但是最小能开16kb
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8af14d83524b4f9b9a1b5979ceef95e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们知道栈的内存是一定的，如果一个线程占的空间越大那么可以开辟的数量就越少，所以当是线程大小是16kb的时候此时开的线程数量是最多的。假如内核态1gb全部用来开线程的话，那么数量就在</p>
<ul>
<li>最大：1024 * 1024 / 16 = 64 * 1024</li>
<li>最小：1024 * 1024 /512 = 2048</li>
</ul>
<p>所以这个线程数量是不固定的。</p></div>  
</div>
            