
---
title: 'OC底层原理探索之GCD源码分析终章'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e5790051a843c2b6b8cbba747b8da2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 04:17:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e5790051a843c2b6b8cbba747b8da2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">栅栏函数</h4>
<p>栅栏函数最直接作用是控制任务的执行顺序产生同步的效果。</p>
<ul>
<li><code>dispatch_barrier_async</code>：前面的任务执行完毕才会来到这里</li>
<li><code>dispatch_barrier_sync</code>：作用相同，但是会阻塞线程，影响后面函数的执行。</li>
</ul>
<h4 data-id="heading-1">示例演示</h4>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)demo1 &#123;
    <span class="hljs-built_in">dispatch_queue_t</span> concurrentQueue = dispatch_queue_create(<span class="hljs-string">"cooci"</span>, DISPATCH_QUEUE_CONCURRENT);
    <span class="hljs-comment">// 这里是可以的额!</span>
    <span class="hljs-comment">/* 1.异步函数 */</span>
    <span class="hljs-built_in">dispatch_async</span>(concurrentQueue, ^&#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"123"</span>);
    &#125;);
    <span class="hljs-comment">/* 2.异步函数 */</span>
    <span class="hljs-built_in">dispatch_async</span>(concurrentQueue, ^&#123;
        sleep(<span class="hljs-number">1</span>);
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"456"</span>);
    &#125;);
    <span class="hljs-comment">/* 3. 栅栏函数 */</span> <span class="hljs-comment">// - dispatch_barrier_sync</span>
    dispatch_barrier_async(concurrentQueue, ^&#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"----%@-----"</span>,[<span class="hljs-built_in">NSThread</span> currentThread]);
    &#125;);
    <span class="hljs-comment">/* 4. 异步函数 */</span>
    <span class="hljs-built_in">dispatch_async</span>(concurrentQueue, ^&#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"加载那么多,喘口气!!!"</span>);
    &#125;);
    <span class="hljs-comment">// 5</span>
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"**********起来干!!"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e5790051a843c2b6b8cbba747b8da2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里使用了异步并发队列，在异步并发的时候使用栅栏函数，前面的任务执行完毕才会来到这里，但是不会阻塞后面任务的执行，所以步骤3栅栏函数必然在步骤1、2之后执行。步骤1、2无序，步骤4、5无序。
注意：如果我们把这个并发队列换成全局并发队列呢？</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-built_in">dispatch_queue_t</span> concurrentQueue = dispatch_get_global_queue(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d92f3aeb8c5b436b8badbf1bc620857e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们发现此时栅栏函数并没有效果了，<strong>也就是说在并发队列中的栅栏函数在全局并发队列中失效了</strong>，那么为什么呢？我们此时照例需要上一份dispatch的源码来一窥究竟</p>
<h4 data-id="heading-2"><code>dispatch_barrier_sync</code></h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">void</span>
<span class="hljs-title">dispatch_barrier_sync</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">dispatch_block_t</span> work)</span>
</span>&#123;
<span class="hljs-keyword">uintptr_t</span> dc_flags = DC_FLAG_BARRIER | DC_FLAG_BLOCK;
<span class="hljs-keyword">if</span> (unlikely(_dispatch_block_has_private_data(work))) &#123;
<span class="hljs-keyword">return</span> _dispatch_sync_block_with_privdata(dq, work, dc_flags);
&#125;
_dispatch_barrier_sync_f(dq, work, _dispatch_Block_invoke(work), dc_flags);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个代码一样就跟之前介绍的同步函数的很像，我们定位下调用链
<code>dispatch_barrier_sync</code> -> <code>_dispatch_barrier_sync_f_inline</code>
通过符号断点我们定位到了<code>_dispatch_sync_f_slow</code> -> <code>_dispatch_sync_invoke_and_complete_recurse</code> -> <code>_dispatch_sync_complete_recurse</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
_dispatch_sync_complete_recurse(<span class="hljs-keyword">dispatch_queue_t</span> dq, <span class="hljs-keyword">dispatch_queue_t</span> stop_dq,
<span class="hljs-keyword">uintptr_t</span> dc_flags)
&#123;
<span class="hljs-keyword">bool</span> barrier = (dc_flags & DC_FLAG_BARRIER);
<span class="hljs-keyword">do</span> &#123;
<span class="hljs-keyword">if</span> (dq == stop_dq) <span class="hljs-keyword">return</span>;
        <span class="hljs-comment">// 是否存在barrier 存在的话 前面的队列全部执行</span>
<span class="hljs-keyword">if</span> (barrier) &#123;
dx_wakeup(dq, <span class="hljs-number">0</span>, DISPATCH_WAKEUP_BARRIER_COMPLETE);
&#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 不存在 执行普通的同步函数</span>
_dispatch_lane_non_barrier_complete(upcast(dq)._dl, <span class="hljs-number">0</span>);
&#125;
dq = dq->do_targetq;
barrier = (dq->dq_width == <span class="hljs-number">1</span>);
&#125; <span class="hljs-keyword">while</span> (unlikely(dq->do_targetq));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>存在栅栏函数的话走<code>dx_wakeup</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> dx_wakeup(x, y, z) dx_vtable(x)->dq_wakeup(x, y, z)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
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
<p>自己创建的并发队列的话=<code>_dispatch_lane_wakeup</code>,
全局并发队列的话=<code>_dispatch_root_queue_wakeup</code>
​</p>
<h4 data-id="heading-3"><code>queue_concurrent</code> VS <code>queue_global</code></h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">void</span>
_dispatch_lane_wakeup(<span class="hljs-keyword">dispatch_lane_class_t</span> dqu, <span class="hljs-keyword">dispatch_qos_t</span> qos,
<span class="hljs-keyword">dispatch_wakeup_flags_t</span> flags)
&#123;
<span class="hljs-keyword">dispatch_queue_wakeup_target_t</span> target = DISPATCH_QUEUE_WAKEUP_NONE;

<span class="hljs-keyword">if</span> (unlikely(flags & DISPATCH_WAKEUP_BARRIER_COMPLETE)) &#123;
<span class="hljs-keyword">return</span> _dispatch_lane_barrier_complete(dqu, qos, flags);
&#125;
<span class="hljs-keyword">if</span> (_dispatch_queue_class_probe(dqu)) &#123;
target = DISPATCH_QUEUE_WAKEUP_TARGET;
&#125;
<span class="hljs-keyword">return</span> _dispatch_queue_wakeup(dqu, qos, flags, target);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">void</span>
_dispatch_root_queue_wakeup(<span class="hljs-keyword">dispatch_queue_global_t</span> dq,
DISPATCH_UNUSED <span class="hljs-keyword">dispatch_qos_t</span> qos, <span class="hljs-keyword">dispatch_wakeup_flags_t</span> flags)
&#123;
<span class="hljs-keyword">if</span> (!(flags & DISPATCH_WAKEUP_BLOCK_WAIT)) &#123;
DISPATCH_INTERNAL_CRASH(dq->dq_priority,
<span class="hljs-string">"Don't try to wake up or override a root queue"</span>);
&#125;
<span class="hljs-keyword">if</span> (flags & DISPATCH_WAKEUP_CONSUME_2) &#123;
<span class="hljs-keyword">return</span> _dispatch_release_2_tailcall(dq);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从源码的地方我们也可以明显的看出来不同。在全局并发队列中并没有判断跟栅栏函数有关的地方，而自己创建的并发队列则有对栅栏函数的判断<code>_dispatch_lane_barrier_complete</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
_dispatch_lane_barrier_complete(<span class="hljs-keyword">dispatch_lane_class_t</span> dqu, <span class="hljs-keyword">dispatch_qos_t</span> qos,
<span class="hljs-keyword">dispatch_wakeup_flags_t</span> flags)
&#123;
<span class="hljs-keyword">dispatch_queue_wakeup_target_t</span> target = DISPATCH_QUEUE_WAKEUP_NONE;
<span class="hljs-keyword">dispatch_lane_t</span> dq = dqu._dl;

<span class="hljs-keyword">if</span> (dq->dq_items_tail && !DISPATCH_QUEUE_IS_SUSPENDED(dq)) &#123;
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_object_s</span> *<span class="hljs-title">dc</span> =</span> _dispatch_queue_get_head(dq);
        <span class="hljs-comment">// 同步函数</span>
<span class="hljs-keyword">if</span> (likely(dq->dq_width == <span class="hljs-number">1</span> || _dispatch_object_is_barrier(dc))) &#123;
<span class="hljs-keyword">if</span> (_dispatch_object_is_waiter(dc)) &#123;
<span class="hljs-keyword">return</span> _dispatch_lane_drain_barrier_waiter(dq, dc, flags, <span class="hljs-number">0</span>);
&#125;
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (dq->dq_width > <span class="hljs-number">1</span> && !_dispatch_object_is_barrier(dc)) &#123;
<span class="hljs-keyword">return</span> _dispatch_lane_drain_non_barriers(dq, dc, flags);
&#125;
<span class="hljs-comment">// ...</span>
&#125;
<span class="hljs-comment">//...</span>
<span class="hljs-keyword">return</span> _dispatch_lane_class_barrier_complete(dq, qos, flags, target, owned);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是同步队列就会等待否则就进入到了完成<code>_dispatch_lane_class_barrier_complete</code>,也就是说要保证前面的所有任务都执行完成。</p>
<p>由此也验证了上面的结论：全局并发队列不处理栅栏函数相关，所以栅栏函数在全局并发队列中无用。这样设计的原因是，系统级别的也会调用全局并发队列，而栅栏函数本质是卡住了当前的线程，这样影响效率。栅栏函数必须要在同一个队列中使用，比如使用AFN的时候我们并不能拿到AFN当前的队列，所以这个栅栏函数平时使用的场景并不多，而我们使用的最多的是调度组
​</p>
<h4 data-id="heading-4">信号量<code>dispatch_semaphore_t</code></h4>
<p><code>dispatch_semaphore_create</code> 创建信号量，里面的数字是表示最大并发数
<code>dispatch_semaphore_wait</code> 信号量等待 -1
<code>dispatch_semaphore_signal </code>信号量释放 +1</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"> -(<span class="hljs-keyword">void</span>)test &#123;
<span class="hljs-built_in">dispatch_queue_t</span> queue = dispatch_get_global_queue(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
   dispatch_semaphore_t sem = dispatch_semaphore_create(<span class="hljs-number">0</span>); 
    <span class="hljs-comment">//任务1</span>
    <span class="hljs-built_in">dispatch_async</span>(queue, ^&#123;
        dispatch_semaphore_wait(sem, DISPATCH_TIME_FOREVER); <span class="hljs-comment">// 等待</span>
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"执行任务1"</span>);
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"任务1完成"</span>);
    &#125;);
    
    <span class="hljs-comment">//任务2</span>
    <span class="hljs-built_in">dispatch_async</span>(queue, ^&#123;
        sleep(<span class="hljs-number">2</span>);
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"执行任务2"</span>);
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"任务2完成"</span>);
        dispatch_semaphore_signal(sem); <span class="hljs-comment">// 发信号 +1</span>
    &#125;);
    
    <span class="hljs-comment">//任务3</span>
    <span class="hljs-built_in">dispatch_async</span>(queue, ^&#123;
        dispatch_semaphore_wait(sem, DISPATCH_TIME_FOREVER);
        sleep(<span class="hljs-number">2</span>);
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"执行任务3"</span>);
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"任务3完成"</span>);
        dispatch_semaphore_signal(sem);
    &#125;);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f70ce0ac46843d2b81ab255bc9b45a1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>任务3不会执行，永远等待下去了。
​</p>
<h4 data-id="heading-5"><code>dispatch_semaphore_create</code></h4>
<pre><code class="hljs language-c copyable" lang="c"> * @param value
 * The starting value <span class="hljs-keyword">for</span> the semaphore. Passing a value less than zero will
 * cause <span class="hljs-literal">NULL</span> to be returned.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>信号量的起始值。传递一个小于零的值将导致返回NULL。
​</p>
<h4 data-id="heading-6"><code>dispatch_semaphore_signal</code></h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">intptr_t</span>
<span class="hljs-title">dispatch_semaphore_signal</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_semaphore_t</span> dsema)</span> <span class="hljs-comment">//0</span>
</span>&#123;
<span class="hljs-keyword">long</span> value = os_atomic_inc2o(dsema, dsema_value, release); <span class="hljs-comment">// +=1  value = 1</span>
<span class="hljs-keyword">if</span> (likely(value > <span class="hljs-number">0</span>)) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;   <span class="hljs-comment">//直接返回0</span>
&#125;
<span class="hljs-keyword">if</span> (unlikely(value == LONG_MIN)) &#123;
DISPATCH_CLIENT_CRASH(value,
<span class="hljs-string">"Unbalanced call to dispatch_semaphore_signal()"</span>);
&#125;
<span class="hljs-keyword">return</span> _dispatch_semaphore_signal_slow(dsema);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7"><code>dispatch_semaphore_wait</code></h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">intptr_t</span>
<span class="hljs-title">dispatch_semaphore_wait</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_semaphore_t</span> dsema, <span class="hljs-keyword">dispatch_time_t</span> timeout)</span>
</span>&#123;
<span class="hljs-keyword">long</span> value = os_atomic_dec2o(dsema, dsema_value, acquire); <span class="hljs-comment">//-=1  0-1 = -1</span>
<span class="hljs-keyword">if</span> (likely(value >= <span class="hljs-number">0</span>)) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="hljs-keyword">return</span> _dispatch_semaphore_wait_slow(dsema, timeout); <span class="hljs-comment">// 走这里</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中，创建的信号量的最大并发数是0，进入到<code>wait</code>这里，<code>0-1 = -1</code>直接到了<code>_dispatch_semaphore_wait_slow</code>这个函数</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">intptr_t</span>
_dispatch_semaphore_wait_slow(<span class="hljs-keyword">dispatch_semaphore_t</span> dsema,
<span class="hljs-keyword">dispatch_time_t</span> timeout) <span class="hljs-comment">// 参数1：0    参数2：FOREVER</span>
&#123;

<span class="hljs-keyword">switch</span> (timeout) &#123;
<span class="hljs-keyword">default</span>:
<span class="hljs-keyword">if</span> (!_dispatch_sema4_timedwait(&dsema->dsema_sema, timeout)) &#123;
<span class="hljs-keyword">break</span>;
&#125;
<span class="hljs-comment">// ...</span>
<span class="hljs-keyword">case</span> DISPATCH_TIME_FOREVER:
_dispatch_sema4_wait(&dsema->dsema_sema);
<span class="hljs-keyword">break</span>;
&#125;
<span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">void</span>
_dispatch_sema4_wait(<span class="hljs-keyword">_dispatch_sema4_t</span> *sema)
&#123;
<span class="hljs-keyword">int</span> ret = <span class="hljs-number">0</span>;
<span class="hljs-keyword">do</span> &#123;
ret = sem_wait(sema);
&#125; <span class="hljs-keyword">while</span> (ret == <span class="hljs-number">-1</span> && errno == EINTR);
DISPATCH_SEMAPHORE_VERIFY_RET(ret);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>sem_wait</code>底层Pthread封装的内核代码，我们只要关注这里的<code>do while</code>循环，本质就是<code>do while</code>死循环等待信号量变为正。
​</p>
<h4 data-id="heading-8">调度组<code>dispatch_group</code></h4>
<p>最直接的作⽤:控制任务执⾏顺序</p>
<ul>
<li><code>dispatch_group_create</code> :创建组</li>
<li><code>dispatch_group_async</code>: 进组任务</li>
<li><code>dispatch_group_notify</code> : 进组任务执⾏完毕通知</li>
<li><code>dispatch_group_wait</code> : 进组任务执⾏等待时间</li>
<li><code>dispatch_group_enter</code>: 进组</li>
<li><code>dispatch_group_leave</code> :出组</li>
</ul>
<p>方案一: <code>dispatch_group_async</code>使用：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)groupDemo&#123;
    dispatch_group_t group = dispatch_group_create();
    <span class="hljs-built_in">dispatch_queue_t</span> queue = dispatch_get_global_queue(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
    
    dispatch_group_async(group, queue, ^&#123;
    &#125;);
    
    dispatch_group_async(group, queue, ^&#123;
        
    &#125;);
    dispatch_group_notify(group, dispatch_get_main_queue(), ^&#123;

    &#125;);
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方案二: <code>enter</code>和<code>leave</code>搭配</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)groupDemo&#123;
    dispatch_group_t group = dispatch_group_create();
    <span class="hljs-built_in">dispatch_queue_t</span> queue = dispatch_get_global_queue(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
    
    dispatch_group_async(group, queue, ^&#123;
    &#125;);
    
    dispatch_group_enter(group);
    <span class="hljs-built_in">dispatch_async</span>(queue, ^&#123;
       dispatch_group_leave(group);
    &#125;);
    
    dispatch_group_notify(group, dispatch_get_main_queue(), ^&#123;

    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面两个效果一样。
为什么<code>dispatch_group_async</code> = <code>dispatch_group_enter</code> + <code>dispatch_group_leave</code>
​</p>
<h4 data-id="heading-9"><code>dispatch_group_create</code></h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">dispatch_group_t</span>
<span class="hljs-title">dispatch_group_create</span><span class="hljs-params">(<span class="hljs-keyword">void</span>)</span>
</span>&#123;
<span class="hljs-keyword">return</span> _dispatch_group_create_with_count(<span class="hljs-number">0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_dispatch_group_create_with_count</code>函数跟信号量那个挺类似的
​</p>
<h4 data-id="heading-10"><code>dispatch_group_enter</code></h4>
<p>进入到源码里面发现这个是个<code>--</code>操作
​</p>
<h4 data-id="heading-11"><code>dispatch_group_leave</code></h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">void</span>
<span class="hljs-title">dispatch_group_leave</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_group_t</span> dg)</span>
</span>&#123;
<span class="hljs-keyword">uint64_t</span> new_state, old_state = os_atomic_add_orig2o(dg, dg_state,
DISPATCH_GROUP_VALUE_INTERVAL, release); <span class="hljs-comment">//++  -1-> 0</span>
<span class="hljs-keyword">uint32_t</span> old_value = (<span class="hljs-keyword">uint32_t</span>)(old_state & DISPATCH_GROUP_VALUE_MASK);<span class="hljs-comment">// -1 & 极大值</span>
<span class="hljs-comment">// old_value == DISPATCH_GROUP_VALUE_MASK</span>
    <span class="hljs-comment">// 所以这一句的判断就是当 old_value = -1时</span>
<span class="hljs-keyword">if</span> (unlikely(old_value == DISPATCH_GROUP_VALUE_1)) &#123;
old_state += DISPATCH_GROUP_VALUE_INTERVAL;
<span class="hljs-keyword">do</span> &#123;
new_state = old_state;
<span class="hljs-keyword">if</span> ((old_state & DISPATCH_GROUP_VALUE_MASK) == <span class="hljs-number">0</span>) &#123;
new_state &= ~DISPATCH_GROUP_HAS_WAITERS;
new_state &= ~DISPATCH_GROUP_HAS_NOTIFS;
&#125; <span class="hljs-keyword">else</span> &#123;
new_state &= ~DISPATCH_GROUP_HAS_NOTIFS;
&#125;
<span class="hljs-keyword">if</span> (old_state == new_state) <span class="hljs-keyword">break</span>;
&#125; <span class="hljs-keyword">while</span> (unlikely(!os_atomic_cmpxchgv2o(dg, dg_state,
old_state, new_state, &old_state, relaxed)));
<span class="hljs-keyword">return</span> _dispatch_group_wake(dg, old_state, <span class="hljs-literal">true</span>);
&#125;

<span class="hljs-keyword">if</span> (unlikely(old_value == <span class="hljs-number">0</span>)) &#123;
DISPATCH_CLIENT_CRASH((<span class="hljs-keyword">uintptr_t</span>)old_value,
<span class="hljs-string">"Unbalanced call to dispatch_group_leave()"</span>);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由后面的注释分析可以知道，当<code>dg = -1</code>的时候,回来到一个<code>do while</code>的循环直到唤醒<code>_dispatch_group_wake</code>，这里唤醒的是<code>dispatch_group_notify</code>。回到上面的分析，我们先进组<code>enter</code>也就是先<code>--</code>，此时<code>dg=-1</code>, 在出组<code>leave</code>函数来到<code>do while</code>循环，函数块走完之后，唤醒<code>notify</code>
​</p>
<h4 data-id="heading-12"><code>dispatch_group_notify</code></h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_group_notify(<span class="hljs-keyword">dispatch_group_t</span> dg, <span class="hljs-keyword">dispatch_queue_t</span> dq,
<span class="hljs-keyword">dispatch_continuation_t</span> dsn)
&#123;
    <span class="hljs-comment">//...</span>
<span class="hljs-keyword">if</span> ((<span class="hljs-keyword">uint32_t</span>)old_state == <span class="hljs-number">0</span>) &#123;
os_atomic_rmw_loop_give_up(&#123;
<span class="hljs-keyword">return</span> _dispatch_group_wake(dg, new_state, <span class="hljs-literal">false</span>);
&#125;);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以看到当<code>old_state == 0</code> ,<code>_dispatch_group_wake</code>开启正常的异步或者同步函数也就是block的call out流程。如果在异步的时候，先执行到了notify，那么把此时的block跟当前的组绑定，等到leave出组的通知的时候，<code>_dispatch_group_wake(dg, old_state, true)</code>。这也就是为什么有两处都调用了这个方法，主要的目的是为了解决异步加载的时序问题，是不是设计的非常nice!
​</p>
<h4 data-id="heading-13"><code>dispatch_group_async</code> = <code>dispatch_group_enter</code> + <code>dispatch_group_leave</code></h4>
<p>由上面的例子我们知道这两个是等效的，那么<code>dispatch_group_async</code>是怎么封装进组和出组的实现呢</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">void</span>
<span class="hljs-title">dispatch_group_async</span><span class="hljs-params">(<span class="hljs-keyword">dispatch_group_t</span> dg, <span class="hljs-keyword">dispatch_queue_t</span> dq,
<span class="hljs-keyword">dispatch_block_t</span> db)</span>
</span>&#123;
<span class="hljs-keyword">dispatch_continuation_t</span> dc = _dispatch_continuation_alloc();
<span class="hljs-keyword">uintptr_t</span> dc_flags = DC_FLAG_CONSUME | DC_FLAG_GROUP_ASYNC;
<span class="hljs-keyword">dispatch_qos_t</span> qos;

qos = _dispatch_continuation_init(dc, dq, db, <span class="hljs-number">0</span>, dc_flags);
_dispatch_continuation_group_async(dg, dq, dc, qos);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_continuation_group_async(<span class="hljs-keyword">dispatch_group_t</span> dg, <span class="hljs-keyword">dispatch_queue_t</span> dq,
<span class="hljs-keyword">dispatch_continuation_t</span> dc, <span class="hljs-keyword">dispatch_qos_t</span> qos)
&#123;
dispatch_group_enter(dg);
dc->dc_data = dg;
_dispatch_continuation_async(dq, dc, qos, dc->dc_flags);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>明显可以看到在函数<code>_dispatch_continuation_group_async</code>有个进组的操作<code>dispatch_group_enter(dg)</code>，<code>_dispatch_continuation_async</code> -> <code>dx_push</code> -> <code>_dispatch_root_queue_push</code> -> <code>_dispatch_root_queue_push_inline</code> -> <code>_dispatch_root_queue_poke</code> -> <code>_dispatch_root_queue_poke_slow</code> -> <code>_dispatch_root_queues_init</code> -> <code>_dispatch_root_queues_init_once</code> -> <code>_dispatch_worker_thread2</code> -> <code>_dispatch_root_queue_drain</code> -> <code>_dispatch_continuation_pop_inline</code> -> <code>_dispatch_continuation_invoke_inline</code>
这些流程之前都来过，就不多说</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">if</span> (unlikely(dc_flags & DC_FLAG_GROUP_ASYNC)) &#123;
_dispatch_continuation_with_group_invoke(dc);
&#125; <span class="hljs-keyword">else</span> &#123;
_dispatch_client_callout(dc->dc_ctxt, dc->dc_func);
_dispatch_trace_item_complete(dc);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_dispatch_continuation_with_group_invoke</code></p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">void</span>
_dispatch_continuation_with_group_invoke(<span class="hljs-keyword">dispatch_continuation_t</span> dc)
&#123;
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dispatch_object_s</span> *<span class="hljs-title">dou</span> =</span> dc->dc_data;
<span class="hljs-keyword">unsigned</span> <span class="hljs-keyword">long</span> type = dx_type(dou);
<span class="hljs-keyword">if</span> (type == DISPATCH_GROUP_TYPE) &#123;
_dispatch_client_callout(dc->dc_ctxt, dc->dc_func);
_dispatch_trace_item_complete(dc);
dispatch_group_leave((<span class="hljs-keyword">dispatch_group_t</span>)dou);
&#125; <span class="hljs-keyword">else</span> &#123;
DISPATCH_INTERNAL_CRASH(dx_type(dou), <span class="hljs-string">"Unexpected object type"</span>);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>_dispatch_client_callout</code>之后看到了出组的代码<code>dispatch_group_leave</code>，我们想想也是，在当前的队列的任务执行完成之后才能调用出组来通知。
​</p>
<h4 data-id="heading-14"><code>dispatch_source</code></h4>
<p><code>GCD</code>和<code>runLoop</code>其实是同等级,没有所谓的归属关系，<code>dispatch_source</code>本质上就是通过条件来控制<code>block</code>的执行，它的CPU负荷⾮常⼩，尽量不占⽤资源。在任⼀线程上调⽤它的的⼀个函数<code>dispatch_source_merge_data</code>后，会执⾏<code>dispatch_source</code>事先定义好的句柄（可以把句柄简单理解为⼀个block）这个过程叫Customevent⽤户事件。</p>
<ul>
<li><code>dispatch_source_create</code> :创建源</li>
<li><code>dispatch_source_set_event_handler</code> :设置源事件回调</li>
<li><code>dispatch_source_merge_data </code> :源事件设置数据</li>
<li><code>dispatch_source_get_data</code> :获取源事件数据</li>
<li><code>dispatch_resume</code>  :继续</li>
<li><code>dispatch_suspend</code> :挂起</li>
</ul>
<p>使用方法比较简单</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">-(<span class="hljs-keyword">void</span>)demo &#123;
    <span class="hljs-comment">// 1.创建队列</span>
    <span class="hljs-keyword">self</span>.queue = dispatch_queue_create(<span class="hljs-string">"hb.com"</span>, <span class="hljs-literal">NULL</span>);
    <span class="hljs-comment">// 2.创建源</span>
    <span class="hljs-keyword">self</span>.source = dispatch_source_create(DISPATCH_SOURCE_TYPE_DATA_ADD, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, dispatch_get_main_queue());
    <span class="hljs-comment">// 3.源事件回调</span>
    dispatch_source_set_event_handler(<span class="hljs-keyword">self</span>.source, ^&#123;
        
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@"</span>,[<span class="hljs-built_in">NSThread</span> currentThread]);
        
        <span class="hljs-built_in">NSUInteger</span> value = dispatch_source_get_data(<span class="hljs-keyword">self</span>.source);
        <span class="hljs-keyword">self</span>.totalComplete += value;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"进度: %.2f"</span>,<span class="hljs-keyword">self</span>.totalComplete/<span class="hljs-number">100.0</span>);
        <span class="hljs-keyword">self</span>.progressView.progress = <span class="hljs-keyword">self</span>.totalComplete/<span class="hljs-number">100.0</span>;
    &#125;);
    
    <span class="hljs-keyword">self</span>.isRunning = <span class="hljs-literal">YES</span>;
    dispatch_resume(<span class="hljs-keyword">self</span>.source);
&#125;
<span class="hljs-comment">// 4.在使用的地方dispatch_source_merge_data修改源数据</span>
<span class="hljs-comment">// 5.dispatch_resume  继续</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且这里不受<code>runLoop</code>的影响是一个<code>workLoop</code>,本质是一个<code>pthread</code>下层封装。
​</p>
<h4 data-id="heading-15">补充：可变数组线程安全吗</h4>
<p>在多线程中操作同一个数组并不安全，因为会出现同时写入的情况，也就是同一时间对同一片内存空间操作不安全。而<code>atomic</code>只能保证自身安全不能保证外部访问安全，解决方法可以在对可变数组操作的时候加入一个栅栏函数相当于加锁的功能</p></div>  
</div>
            