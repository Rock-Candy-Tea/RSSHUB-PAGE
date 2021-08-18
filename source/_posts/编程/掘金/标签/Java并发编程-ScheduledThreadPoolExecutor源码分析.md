
---
title: 'Java并发编程-ScheduledThreadPoolExecutor源码分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a76c162b07244396890a5dcd5784a92e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 00:49:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a76c162b07244396890a5dcd5784a92e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><strong>线程池系列</strong></p>
<p><a href="https://juejin.cn/post/6995603327094358046" target="_blank" title="https://juejin.cn/post/6995603327094358046">Java并发编程-线程池框架(一)</a><br>
<a href="https://juejin.cn/post/6995970056786018312" target="_blank" title="https://juejin.cn/post/6995970056786018312">Java并发编程-线程池源码分析（二）</a><br>
<a href="https://juejin.cn/post/6996532847364276237" target="_blank" title="https://juejin.cn/post/6996532847364276237">Java并发编程-JDK线程池和Spring线程池（三）</a><br>
<a href="https://juejin.cn/post/6996704389360517133" target="_blank" title="https://juejin.cn/post/6996704389360517133">Java并发编程-线程池优雅关闭（四）</a><br>
<a href="https://juejin.cn/post/6997076127466389540" target="_blank" title="https://juejin.cn/post/6997076127466389540">Java并发编程-阻塞队列BlockingQueue</a><br>
<a href="https://juejin.cn/post/6997426731426512903" target="_blank" title="https://juejin.cn/post/6997426731426512903">Java并发编程-如何设置线程池大小?</a></p>
<h2 data-id="heading-0">前言</h2>
<p>ScheduledThreadPoolExecutor 继承自ThreadPoolExecutor。它主要用来在给定的延迟之后执行任务，或者定期执行任务。<br>
ScheduledThreadPoolExecutor的功能与Timer类似，但比Timer更强大，更灵活，Timer对应的是单个后台线程，而ScheduledThreadPoolExecutor可以在构造函数中指定多个对应的后台线程数。</p>
<h2 data-id="heading-1">1. ScheduledThreadPoolExecutor 框架</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a76c162b07244396890a5dcd5784a92e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>构造函数</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">ScheduledThreadPoolExecutor</span><span class="hljs-params">(<span class="hljs-keyword">int</span> corePoolSize,
                                   ThreadFactory threadFactory,
                                   RejectedExecutionHandler handler)</span> </span>&#123;
    <span class="hljs-keyword">super</span>(corePoolSize, Integer.MAX_VALUE, <span class="hljs-number">0</span>, NANOSECONDS,
          <span class="hljs-keyword">new</span> DelayedWorkQueue(), threadFactory, handler);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ScheduledThreadPoolExecutor的本质依然是一个线程池，但是于其他的线程池不同的是使用了 DelayedWorkQueue().</p>
<h3 data-id="heading-2">1.1 ScheduledExecutorService</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1b33b015574492a84d9ff6b3c671919~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ScheduledExecutorService 本身继承了ExecutorService接口，并为调度任务额外提供了两种模式， 延迟执行和周期执行。</p>
<p><strong>延迟执行</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 1. 根据参数中设定的延时，执行一次任务</span>
<span class="hljs-keyword">public</span> ScheduledFuture<?> schedule(Runnable command,
                                   <span class="hljs-keyword">long</span> delay, TimeUnit unit);
<span class="hljs-comment">// 2. 根据参数中设定的延时，执行一次任务                                   </span>
<span class="hljs-keyword">public</span> <V> <span class="hljs-function">ScheduledFuture<V> <span class="hljs-title">schedule</span><span class="hljs-params">(Callable<V> callable,
                                       <span class="hljs-keyword">long</span> delay, TimeUnit unit)</span></span>;
                                  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>周期执行</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//3. 创建并执行一个周期性动作，该动作在给定的初始延迟之后首先启用，然后在给定的周期之后启用;</span>
<span class="hljs-comment">//也就是说，执行将在initialDelay之后开始，然后initialDelay+period，然后initialDelay+ 2 * period，以此类推。</span>
<span class="hljs-comment">//如果任务的任何执行遇到异常，则禁止后续执行。否则，任务只能通过取消或终止执行器来终止。</span>
<span class="hljs-comment">//如果该任务的任何执行花费的时间超过了它的周期，那么后续执行可能会延迟开始，但不会并发执行。</span>
<span class="hljs-keyword">public</span> ScheduledFuture<?> scheduleAtFixedRate(Runnable command,
                                              <span class="hljs-keyword">long</span> initialDelay,
                                              <span class="hljs-keyword">long</span> period,
                                              TimeUnit unit);

<span class="hljs-comment">//创建并执行一个周期性操作，该操作在给定的初始延迟之后首先启用，然后在一次执行终止和下一次执行开始之间启用给定的延迟。</span>
<span class="hljs-comment">//如果任务的任何执行遇到异常，则禁止后续执行。否则，任务只能通过取消或终止执行器来终止。</span>
<span class="hljs-keyword">public</span> ScheduledFuture<?> scheduleWithFixedDelay(Runnable command,
                                                 <span class="hljs-keyword">long</span> initialDelay,
                                                 <span class="hljs-keyword">long</span> delay,
                                                 TimeUnit unit);

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.2 内部类 ScheduledFutureTask</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b02cb9c062a14dc5a741f4d462a03e1e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
ScheduledFutureTask是ScheduledThreadPoolExecutor对于RunnableScheduledFuture的默认实现，并且继承了FutureTask。<br>
它覆盖了FutureTask的run方法来实现对延时执行、周期执行的支持。</p>
<h3 data-id="heading-4">1.3 内部类 DelayedWorkQueue</h3>
<p>DelayedWorkQueue是ScheduledThreadPoolExecutor中阻塞队列的实现，它内部使用了小根堆来使得自身具有优先队列的功能，并且通过Leader/Follower模式避免线程不必要的等待。<br>
从DelayedWorkQueue中取出任务时，任务一定已经至少到了可以被执行的时间。</p>
<h2 data-id="heading-5">2. 使用案例</h2>
<p>设置一个调度线程池, 设置两种不同的调度方法，并执行。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BeeperControl</span> </span>&#123;
    <span class="hljs-comment">// 定义一个定时调度线程池</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> ScheduledExecutorService scheduler =
            <span class="hljs-keyword">new</span> ScheduledThreadPoolExecutor(<span class="hljs-number">1</span>);

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">beepForAnHour</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">final</span> Runnable beeper = <span class="hljs-keyword">new</span> Runnable() &#123;
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123; System.out.println(<span class="hljs-string">"beep"</span>); &#125;
        &#125;;
        <span class="hljs-comment">// 设置周期执行, 10s执行一次</span>
        <span class="hljs-keyword">final</span> ScheduledFuture<?> beeperHandle =
                scheduler.scheduleAtFixedRate(beeper, <span class="hljs-number">10</span>, <span class="hljs-number">10</span>, TimeUnit.SECONDS);

        <span class="hljs-comment">// 延迟执行     </span>
        scheduler.schedule(<span class="hljs-keyword">new</span> Runnable() &#123;
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
                beeperHandle.cancel(<span class="hljs-keyword">true</span>);
            &#125;
        &#125;, <span class="hljs-number">60</span> * <span class="hljs-number">60</span>, TimeUnit.SECONDS);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        beepForAnHour();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">3. 源码分析</h2>
<h3 data-id="heading-7">3.1 ScheduledThreadPoolExecutor</h3>
<p>ScheduledThreadPoolExecutor 任务提交的入口方法主要是execute,submit, schedule, scheduleAtFixedRate以及scheduleWithFixedDelay这几类。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">execute</span><span class="hljs-params">(Runnable command)</span> </span>&#123;
    schedule(command, <span class="hljs-number">0</span>, NANOSECONDS);
&#125;


<span class="hljs-keyword">public</span> <T> <span class="hljs-function">Future<T> <span class="hljs-title">submit</span><span class="hljs-params">(Runnable task, T result)</span> </span>&#123;
    <span class="hljs-keyword">return</span> schedule(Executors.callable(task, result), <span class="hljs-number">0</span>, NANOSECONDS);
&#125;


<span class="hljs-keyword">public</span> ScheduledFuture<?> schedule(Runnable command,
                                   <span class="hljs-keyword">long</span> delay,
                                   TimeUnit unit) &#123;
    <span class="hljs-keyword">if</span> (command == <span class="hljs-keyword">null</span> || unit == <span class="hljs-keyword">null</span>)
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> NullPointerException();
    RunnableScheduledFuture<?> t = decorateTask(command,
        <span class="hljs-keyword">new</span> ScheduledFutureTask<Void>(command, <span class="hljs-keyword">null</span>,
                                      triggerTime(delay, unit)));
    delayedExecute(t);
    <span class="hljs-keyword">return</span> t;
&#125;

<span class="hljs-keyword">public</span> ScheduledFuture<?> scheduleAtFixedRate(Runnable command,
                                              <span class="hljs-keyword">long</span> initialDelay,
                                              <span class="hljs-keyword">long</span> period,
                                              TimeUnit unit) &#123;
    <span class="hljs-keyword">if</span> (command == <span class="hljs-keyword">null</span> || unit == <span class="hljs-keyword">null</span>)
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> NullPointerException();
    <span class="hljs-keyword">if</span> (period <= <span class="hljs-number">0</span>)
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalArgumentException();
    ScheduledFutureTask<Void> sft =
        <span class="hljs-keyword">new</span> ScheduledFutureTask<Void>(command,
                                      <span class="hljs-keyword">null</span>,
                                      triggerTime(initialDelay, unit),
                                      unit.toNanos(period));
    RunnableScheduledFuture<Void> t = decorateTask(command, sft);
    sft.outerTask = t;
    delayedExecute(t);
    <span class="hljs-keyword">return</span> t;
&#125;

<span class="hljs-keyword">public</span> ScheduledFuture<?> scheduleWithFixedDelay(Runnable command,
                                                 <span class="hljs-keyword">long</span> initialDelay,
                                                 <span class="hljs-keyword">long</span> delay,
                                                 TimeUnit unit) &#123;
    <span class="hljs-keyword">if</span> (command == <span class="hljs-keyword">null</span> || unit == <span class="hljs-keyword">null</span>)
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> NullPointerException();
    <span class="hljs-keyword">if</span> (delay <= <span class="hljs-number">0</span>)
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalArgumentException();
    ScheduledFutureTask<Void> sft =
        <span class="hljs-keyword">new</span> ScheduledFutureTask<Void>(command,
                                      <span class="hljs-keyword">null</span>,
                                      triggerTime(initialDelay, unit),
                                      unit.toNanos(-delay));
    RunnableScheduledFuture<Void> t = decorateTask(command, sft);
    sft.outerTask = t;
    delayedExecute(t);
    <span class="hljs-keyword">return</span> t;
&#125;

<span class="hljs-keyword">public</span> <T> <span class="hljs-function">Future<T> <span class="hljs-title">submit</span><span class="hljs-params">(Callable<T> task)</span> </span>&#123;
    <span class="hljs-keyword">return</span> schedule(task, <span class="hljs-number">0</span>, NANOSECONDS);
&#125;

<span class="hljs-keyword">public</span> <V> <span class="hljs-function">ScheduledFuture<V> <span class="hljs-title">schedule</span><span class="hljs-params">(Callable<V> callable,
                                       <span class="hljs-keyword">long</span> delay,
                                       TimeUnit unit)</span> </span>&#123;
    <span class="hljs-keyword">if</span> (callable == <span class="hljs-keyword">null</span> || unit == <span class="hljs-keyword">null</span>)
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> NullPointerException();
    RunnableScheduledFuture<V> t = decorateTask(callable,
        <span class="hljs-keyword">new</span> ScheduledFutureTask<V>(callable,
                                   triggerTime(delay, unit)));
    delayedExecute(t);
    <span class="hljs-keyword">return</span> t;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">3.2 ScheduledFutureTask</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee7cb9eea9ed4ed7ac5620df126943de~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">3.2.1 基本属性</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 任务的序列号,在排序中会用到。</span>
<span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> sequenceNumber;

<span class="hljs-comment">// 任务可以被执行的时间，以纳秒表示。</span>
<span class="hljs-keyword">private</span> <span class="hljs-keyword">long</span> time;

<span class="hljs-comment">// 0表示非周期任务。正数表示fixed-rate模式，负数表示fixed-delay模式。</span>
<span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> period;

<span class="hljs-comment">// The actual task to be re-enqueued by reExecutePeriodic</span>
RunnableScheduledFuture<V> outerTask = <span class="hljs-keyword">this</span>;

<span class="hljs-comment">// 用于维护该任务在DelayedWorkQueue内部堆中的索引(在堆数组中的index)。</span>
<span class="hljs-keyword">int</span> heapIndex;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">3.2.2 ScheduledFutureTask#run方法</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-comment">// 是否是周期性任务</span>
    <span class="hljs-keyword">boolean</span> periodic = isPeriodic();
    <span class="hljs-comment">// 检查任务是否可以被执行</span>
    <span class="hljs-keyword">if</span> (!canRunInCurrentRunState(periodic))
        cancel(<span class="hljs-keyword">false</span>);
    <span class="hljs-comment">// 如果非周期性任务直接调用run运行即可。    </span>
    <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!periodic)
        ScheduledFutureTask.<span class="hljs-keyword">super</span>.run();
    <span class="hljs-comment">// 如果成功runAndRest  </span>
    <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (ScheduledFutureTask.<span class="hljs-keyword">super</span>.runAndReset()) &#123;
        <span class="hljs-comment">// 设置下次运行时间并调用reExecutePeriodic。</span>
        setNextRunTime();
        <span class="hljs-comment">// 需要重新将任务(outerTask)放到工作队列中。</span>
        reExecutePeriodic(outerTask);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">3.2.3 ScheduledFutureTask#cancel方法</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">cancel</span><span class="hljs-params">(<span class="hljs-keyword">boolean</span> mayInterruptIfRunning)</span> </span>&#123;
    <span class="hljs-comment">// 先调用父类FutureTask#cancel来取消任务</span>
    <span class="hljs-keyword">boolean</span> cancelled = <span class="hljs-keyword">super</span>.cancel(mayInterruptIfRunning);
    <span class="hljs-comment">// removeOnCancel开关用于控制任务取消后是否应该从队列中移除。</span>
    <span class="hljs-keyword">if</span> (cancelled && removeOnCancel && heapIndex >= <span class="hljs-number">0</span>)
        remove(<span class="hljs-keyword">this</span>);
    <span class="hljs-keyword">return</span> cancelled;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3.3 DelayedWorkQueue</h3>
<p>DelayedWorkQueue是ScheduledThreadPoolExecutor使用的工作队列。它内部维护了一个小根堆，根据任务的执行开始时间来维护任务顺序。但不同的地方在于，它对于ScheduledFutureTask类型的元素额外维护了元素在队列中堆数组的索引，用来实现快速取消。DelayedWorkQueue用了ReentrantLock+Condition来实现管程保证数据的线程安全性。</p>
<h4 data-id="heading-13">3.3.1 DelayedWorkQueue#offer方法</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">offer</span><span class="hljs-params">(Runnable x)</span> </span>&#123;
    <span class="hljs-keyword">if</span> (x == <span class="hljs-keyword">null</span>)
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> NullPointerException();
    RunnableScheduledFuture<?> e = (RunnableScheduledFuture<?>)x;
    <span class="hljs-keyword">final</span> ReentrantLock lock = <span class="hljs-keyword">this</span>.lock;
    lock.lock();
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">int</span> i = size;
        <span class="hljs-keyword">if</span> (i >= queue.length)
            grow();
        size = i + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">if</span> (i == <span class="hljs-number">0</span>) &#123;
            queue[<span class="hljs-number">0</span>] = e;
            setIndex(e, <span class="hljs-number">0</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
            siftUp(i, e);
        &#125;
        <span class="hljs-keyword">if</span> (queue[<span class="hljs-number">0</span>] == e) &#123;
            leader = <span class="hljs-keyword">null</span>;
            available.signal();
        &#125;
    &#125; <span class="hljs-keyword">finally</span> &#123;
        lock.unlock();
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">3.3.2 DelayedWorkQueue#take方法</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> RunnableScheduledFuture<?> take() <span class="hljs-keyword">throws</span> InterruptedException &#123;
    <span class="hljs-keyword">final</span> ReentrantLock lock = <span class="hljs-keyword">this</span>.lock;
    lock.lockInterruptibly();
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">for</span> (;;) &#123;
            RunnableScheduledFuture<?> first = queue[<span class="hljs-number">0</span>];
            <span class="hljs-keyword">if</span> (first == <span class="hljs-keyword">null</span>)
                available.await();
            <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">long</span> delay = first.getDelay(NANOSECONDS);
                <span class="hljs-keyword">if</span> (delay <= <span class="hljs-number">0</span>)
                    <span class="hljs-keyword">return</span> finishPoll(first);
                first = <span class="hljs-keyword">null</span>; <span class="hljs-comment">// don't retain ref while waiting</span>
                <span class="hljs-keyword">if</span> (leader != <span class="hljs-keyword">null</span>)
                    available.await();
                <span class="hljs-keyword">else</span> &#123;
                    Thread thisThread = Thread.currentThread();
                    leader = thisThread;
                    <span class="hljs-keyword">try</span> &#123;
                        available.awaitNanos(delay);
                    &#125; <span class="hljs-keyword">finally</span> &#123;
                        <span class="hljs-keyword">if</span> (leader == thisThread)
                            leader = <span class="hljs-keyword">null</span>;
                    &#125;
                &#125;
            &#125;
        &#125;
    &#125; <span class="hljs-keyword">finally</span> &#123;
        <span class="hljs-keyword">if</span> (leader == <span class="hljs-keyword">null</span> && queue[<span class="hljs-number">0</span>] != <span class="hljs-keyword">null</span>)
            available.signal();
        lock.unlock();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">3.3.3 DelayedWorkQueue#poll(long, TimeUnit)方法</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> RunnableScheduledFuture<?> poll(<span class="hljs-keyword">long</span> timeout, TimeUnit unit)
    <span class="hljs-keyword">throws</span> InterruptedException &#123;
    <span class="hljs-keyword">long</span> nanos = unit.toNanos(timeout);
    <span class="hljs-keyword">final</span> ReentrantLock lock = <span class="hljs-keyword">this</span>.lock;
    lock.lockInterruptibly();
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">for</span> (;;) &#123;
            RunnableScheduledFuture<?> first = queue[<span class="hljs-number">0</span>];
            <span class="hljs-keyword">if</span> (first == <span class="hljs-keyword">null</span>) &#123;
                <span class="hljs-keyword">if</span> (nanos <= <span class="hljs-number">0</span>)
                    <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
                <span class="hljs-keyword">else</span>
                    nanos = available.awaitNanos(nanos);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">long</span> delay = first.getDelay(NANOSECONDS);
                <span class="hljs-keyword">if</span> (delay <= <span class="hljs-number">0</span>)
                    <span class="hljs-keyword">return</span> finishPoll(first);
                <span class="hljs-keyword">if</span> (nanos <= <span class="hljs-number">0</span>)
                    <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
                first = <span class="hljs-keyword">null</span>; <span class="hljs-comment">// don't retain ref while waiting</span>
                <span class="hljs-keyword">if</span> (nanos < delay || leader != <span class="hljs-keyword">null</span>)
                    nanos = available.awaitNanos(nanos);
                <span class="hljs-keyword">else</span> &#123;
                    Thread thisThread = Thread.currentThread();
                    leader = thisThread;
                    <span class="hljs-keyword">try</span> &#123;
                        <span class="hljs-keyword">long</span> timeLeft = available.awaitNanos(delay);
                        nanos -= delay - timeLeft;
                    &#125; <span class="hljs-keyword">finally</span> &#123;
                        <span class="hljs-keyword">if</span> (leader == thisThread)
                            leader = <span class="hljs-keyword">null</span>;
                    &#125;
                &#125;
            &#125;
        &#125;
    &#125; <span class="hljs-keyword">finally</span> &#123;
        <span class="hljs-keyword">if</span> (leader == <span class="hljs-keyword">null</span> && queue[<span class="hljs-number">0</span>] != <span class="hljs-keyword">null</span>)
            available.signal();
        lock.unlock();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">3.3.4 DelayedWorkQueue#remove方法</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">remove</span><span class="hljs-params">(Object x)</span> </span>&#123;
    <span class="hljs-keyword">final</span> ReentrantLock lock = <span class="hljs-keyword">this</span>.lock;
    lock.lock();
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">int</span> i = indexOf(x);
        <span class="hljs-keyword">if</span> (i < <span class="hljs-number">0</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;

        setIndex(queue[i], -<span class="hljs-number">1</span>);
        <span class="hljs-keyword">int</span> s = --size;
        RunnableScheduledFuture<?> replacement = queue[s];
        queue[s] = <span class="hljs-keyword">null</span>;
        <span class="hljs-keyword">if</span> (s != i) &#123;
            siftDown(i, replacement);
            <span class="hljs-keyword">if</span> (queue[i] == replacement)
                siftUp(i, replacement);
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
    &#125; <span class="hljs-keyword">finally</span> &#123;
        lock.unlock();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">总结</h2>
<ol>
<li>ScheduledThreadPoolExecutor内部使用了ScheduledFutureTask来表示任务，即使对于execute方法也将其委托至schedule方法，以零延时的形式实现。同时ScheduledThreadPoolExecutor也允许我们通过decorateTask方法来包装任务以实现定制化的封装。</li>
<li>ScheduledThreadPoolExecutor内部使用的阻塞队列DelayedWorkQueue通过小根堆来实现优先队列的功能。由于DelayedWorkQueue是无界的，所以本质上对于ScheduledThreadPoolExecutor而言，maximumPoolSize并没有意义。</li>
</ol>
<h2 data-id="heading-18">参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fjavase%2F7%2Fdocs%2Fapi%2Fjava%2Futil%2Fconcurrent%2FScheduledExecutorService.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ScheduledExecutorService.html" ref="nofollow noopener noreferrer">Interface ScheduledExecutorService</a></p></div>  
</div>
            