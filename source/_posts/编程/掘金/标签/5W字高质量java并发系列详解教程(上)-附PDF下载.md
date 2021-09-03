
---
title: '5W字高质量java并发系列详解教程(上)-附PDF下载'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d86fe0ff5e9345bf83da48e22a6bbcb0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 17:26:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d86fe0ff5e9345bf83da48e22a6bbcb0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>并发是java高级程序员必须要深入研究的话题，从Synchronized到Lock，JDK本身提供了很多优秀的并发类和锁控制器，灵活使用这些类，可以写出优秀的并发程序，而这些类基本上都是在java.util.concurrent包中的，本文将会从具体的例子出发，一步一步带领大家进入java高质量并发的世界。</p>
<p>本文PDF下载链接<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fddean2009%2Fwww.flydean.com%2Fblob%2Fmaster%2Fjava%2Fconcurrent%2Fconcurrent-all-in-one.pdf" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ddean2009/www.flydean.com/blob/master/java/concurrent/concurrent-all-in-one.pdf" ref="nofollow noopener noreferrer">concurrent-all-in-one.pdf</a></p>
<p>本文的例子可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fddean2009%2Flearn-java-concurrency%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ddean2009/learn-java-concurrency/" ref="nofollow noopener noreferrer">github.com/ddean2009/l…</a></p>
<h1 data-id="heading-0">第一章  java.util.concurrent简介</h1>
<p>java.util.concurrent包提供了很多有用的类，方便我们进行并发程序的开发。本文将会做一个总体的简单介绍。</p>
<h2 data-id="heading-1">主要的组件</h2>
<p>java.util.concurrent包含了很多内容， 本文将会挑选其中常用的一些类来进行大概的说明：</p>
<ul>
<li>Executor</li>
<li>ExecutorService</li>
<li>ScheduledExecutorService</li>
<li>Future</li>
<li>CountDownLatch</li>
<li>CyclicBarrier</li>
<li>Semaphore</li>
<li>ThreadFactory</li>
</ul>
<h2 data-id="heading-2">Executor</h2>
<p>Executor是一个接口，它定义了一个execute方法，这个方法接收一个Runnable，并在其中调用Runnable的run方法。</p>
<p>我们看一个Executor的实现：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Invoker</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Executor</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">execute</span><span class="hljs-params">(Runnable r)</span> </span>&#123;
        r.run();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们可以直接调用该类中的方法：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">execute</span><span class="hljs-params">()</span> </span>&#123;
        Executor executor = <span class="hljs-keyword">new</span> Invoker();
        executor.execute( () -> &#123;
            log.info(<span class="hljs-string">"&#123;&#125;"</span>, Thread.currentThread().toString());
        &#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意，Executor并不一定要求执行的任务是异步的。</p>
</blockquote>
<h2 data-id="heading-3">ExecutorService</h2>
<p>如果我们真正的需要使用多线程的话，那么就需要用到ExecutorService了。</p>
<p>ExecutorService管理了一个内存的队列，并定时提交可用的线程。</p>
<p>我们首先定义一个Runnable类：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Task</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-comment">// task details</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过Executors来方便的创建ExecutorService：</p>
<pre><code class="hljs language-java copyable" lang="java">ExecutorService executor = Executors.newFixedThreadPool(<span class="hljs-number">10</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面创建了一个ThreadPool， 我们也可以创建单线程的ExecutorService：</p>
<pre><code class="hljs language-java copyable" lang="java">ExecutorService executor =Executors.newSingleThreadExecutor();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们这样提交task：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">execute</span><span class="hljs-params">()</span> </span>&#123; 
    executor.submit(<span class="hljs-keyword">new</span> Task()); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为ExecutorService维持了一个队列，所以它不会自动关闭， 我们需要调用executor.shutdown() 或者executor.shutdownNow()来关闭它。</p>
<p>如果想要判断ExecutorService中的线程在收到shutdown请求后是否全部执行完毕，可以调用如下的方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">try</span> &#123;
            executor.awaitTermination( <span class="hljs-number">5l</span>, TimeUnit.SECONDS );
        &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
            e.printStackTrace();
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">ScheduledExecutorService</h2>
<p>ScheduledExecutorService和ExecutorService很类似，但是它可以周期性的执行任务。</p>
<p>我们这样创建ScheduledExecutorService：</p>
<pre><code class="hljs language-java copyable" lang="java">ScheduledExecutorService executorService
                = Executors.newSingleThreadScheduledExecutor();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>executorService的schedule方法，可以传入Runnable也可以传入Callable：</p>
<pre><code class="hljs language-java copyable" lang="java">Future<String> future = executorService.schedule(() -> &#123;
        <span class="hljs-comment">// ...</span>
        <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello world"</span>;
    &#125;, <span class="hljs-number">1</span>, TimeUnit.SECONDS);
 
    ScheduledFuture<?> scheduledFuture = executorService.schedule(() -> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;, <span class="hljs-number">1</span>, TimeUnit.SECONDS);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有两个比较相近的方法：</p>
<pre><code class="hljs language-java copyable" lang="java">scheduleAtFixedRate( Runnable command, <span class="hljs-keyword">long</span> initialDelay, <span class="hljs-keyword">long</span> period, TimeUnit unit )

scheduleWithFixedDelay( Runnable command, <span class="hljs-keyword">long</span> initialDelay, <span class="hljs-keyword">long</span> delay, TimeUnit unit ) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两者的区别是前者的period是以任务开始时间来计算的，后者是以任务结束时间来计算。</p>
<h2 data-id="heading-5">Future</h2>
<p>Future用来获取异步执行的结果。可以调用cancel(boolean mayInterruptIfRunning) 方法来取消线程的执行。</p>
<p>我们看下怎么得到一个Future对象：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">invoke</span><span class="hljs-params">()</span> </span>&#123;
    ExecutorService executorService = Executors.newFixedThreadPool(<span class="hljs-number">10</span>);
 
    Future<String> future = executorService.submit(() -> &#123;
        <span class="hljs-comment">// ...</span>
        Thread.sleep(<span class="hljs-number">10000l</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello world"</span>;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看下怎么获取Future的结果：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">if</span> (future.isDone() && !future.isCancelled()) &#123;
    <span class="hljs-keyword">try</span> &#123;
        str = future.get();
    &#125; <span class="hljs-keyword">catch</span> (InterruptedException | ExecutionException e) &#123;
        e.printStackTrace();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>future还可以接受一个时间参数，超过指定的时间，将会报TimeoutException。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">try</span> &#123;
    future.get(<span class="hljs-number">10</span>, TimeUnit.SECONDS);
&#125; <span class="hljs-keyword">catch</span> (InterruptedException | ExecutionException | TimeoutException e) &#123;
    e.printStackTrace();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">CountDownLatch</h2>
<p>CountDownLatch是一个并发中很有用的类，CountDownLatch会初始化一个counter，通过这个counter变量，来控制资源的访问。我们会在后面的文章详细介绍。</p>
<h2 data-id="heading-7">CyclicBarrier</h2>
<p>CyclicBarrier和CountDownLatch很类似。CyclicBarrier主要用于多个线程互相等待的情况，可以通过调用await() 方法等待，知道达到要等的数量。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Task</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span> </span>&#123;
 
    <span class="hljs-keyword">private</span> CyclicBarrier barrier;
 
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Task</span><span class="hljs-params">(CyclicBarrier barrier)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.barrier = barrier;
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            LOG.info(Thread.currentThread().getName() + 
              <span class="hljs-string">" is waiting"</span>);
            barrier.await();
            LOG.info(Thread.currentThread().getName() + 
              <span class="hljs-string">" is released"</span>);
        &#125; <span class="hljs-keyword">catch</span> (InterruptedException | BrokenBarrierException e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">start</span><span class="hljs-params">()</span> </span>&#123;
 
    CyclicBarrier cyclicBarrier = <span class="hljs-keyword">new</span> CyclicBarrier(<span class="hljs-number">3</span>, () -> &#123;
        <span class="hljs-comment">// ...</span>
        LOG.info(<span class="hljs-string">"All previous tasks are completed"</span>);
    &#125;);
 
    Thread t1 = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">new</span> Task(cyclicBarrier), <span class="hljs-string">"T1"</span>); 
    Thread t2 = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">new</span> Task(cyclicBarrier), <span class="hljs-string">"T2"</span>); 
    Thread t3 = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">new</span> Task(cyclicBarrier), <span class="hljs-string">"T3"</span>); 
 
    <span class="hljs-keyword">if</span> (!cyclicBarrier.isBroken()) &#123; 
        t1.start(); 
        t2.start(); 
        t3.start(); 
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">Semaphore</h2>
<p>Semaphore包含了一定数量的许可证，通过获取许可证，从而获得对资源的访问权限。通过 tryAcquire()来获取许可，如果获取成功，许可证的数量将会减少。</p>
<p>一旦线程release()许可，许可的数量将会增加。</p>
<p>我们看下怎么使用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">static</span> Semaphore semaphore = <span class="hljs-keyword">new</span> Semaphore(<span class="hljs-number">10</span>);
 
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">execute</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
 
    LOG.info(<span class="hljs-string">"Available permit : "</span> + semaphore.availablePermits());
    LOG.info(<span class="hljs-string">"Number of threads waiting to acquire: "</span> + 
      semaphore.getQueueLength());
 
    <span class="hljs-keyword">if</span> (semaphore.tryAcquire()) &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// ...</span>
        &#125;
        <span class="hljs-keyword">finally</span> &#123;
            semaphore.release();
        &#125;
    &#125;
 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">ThreadFactory</h2>
<p>ThreadFactory可以很方便的用来创建线程：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ThreadFactoryUsage</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">ThreadFactory</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> threadId;
    <span class="hljs-keyword">private</span> String name;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">ThreadFactoryUsage</span><span class="hljs-params">(String name)</span> </span>&#123;
        threadId = <span class="hljs-number">1</span>;
        <span class="hljs-keyword">this</span>.name = name;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Thread <span class="hljs-title">newThread</span><span class="hljs-params">(Runnable r)</span> </span>&#123;
        Thread t = <span class="hljs-keyword">new</span> Thread(r, name + <span class="hljs-string">"-Thread_"</span> + threadId);
        log.info(<span class="hljs-string">"created new thread with id : "</span> + threadId +
                <span class="hljs-string">" and name : "</span> + t.getName());
        threadId++;
        <span class="hljs-keyword">return</span> t;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">第二章 java并发中的Synchronized关键词</h1>
<p>如果在多线程的环境中，我们经常会遇到资源竞争的情况，比如多个线程要去同时修改同一个共享变量，这时候，就需要对资源的访问方法进行一定的处理，保证同一时间只有一个线程访问。</p>
<p>java提供了synchronized关键字，方便我们实现上述操作。</p>
<h2 data-id="heading-11">为什么要同步</h2>
<p>我们举个例子，我们创建一个类，提供了一个setSum的方法：</p>
<pre><code class="hljs language-java copyable" lang="java">
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SynchronizedMethods</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> sum = <span class="hljs-number">0</span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">calculate</span><span class="hljs-params">()</span> </span>&#123;
        setSum(getSum() + <span class="hljs-number">1</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们在多线程的环境中调用这个calculate方法：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">givenMultiThread_whenNonSyncMethod</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        ExecutorService service = Executors.newFixedThreadPool(<span class="hljs-number">3</span>);
        SynchronizedMethods summation = <span class="hljs-keyword">new</span> SynchronizedMethods();

        IntStream.range(<span class="hljs-number">0</span>, <span class="hljs-number">1000</span>)
                .forEach(count -> service.submit(summation::calculate));
        service.shutdown();
        service.awaitTermination(<span class="hljs-number">1000</span>, TimeUnit.MILLISECONDS);

        assertEquals(<span class="hljs-number">1000</span>, summation.getSum());
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照上面的方法，我们预计要返回1000， 但是实际上基本不可能得到1000这个值，因为在多线程环境中，对同一个资源进行同时操作带来的不利影响。</p>
<p>那我们怎么才能够建线程安全的环境呢？</p>
<h2 data-id="heading-12">Synchronized关键词</h2>
<p>java提供了多种线程安全的方法，本文主要讲解Synchronized关键词，Synchronized关键词可以有很多种形式：</p>
<ul>
<li>Instance methods</li>
<li>Static methods</li>
<li>Code blocks</li>
</ul>
<p>当我们使用synchronized时，java会在相应的对象上加锁，从而在同一个对象等待锁的方法都必须顺序执行，从而保证了线程的安全。</p>
<h3 data-id="heading-13">Synchronized Instance Methods</h3>
<p>Synchronized关键词可以放在实例方法的前面：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">synchronized</span> <span class="hljs-keyword">void</span> <span class="hljs-title">synchronisedCalculate</span><span class="hljs-params">()</span> </span>&#123;
        setSum(getSum() + <span class="hljs-number">1</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看下调用结果：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Test</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">givenMultiThread_whenMethodSync</span><span class="hljs-params">()</span> </span>&#123;
    ExecutorService service = Executors.newFixedThreadPool(<span class="hljs-number">3</span>);
    SynchronizedMethods method = <span class="hljs-keyword">new</span> SynchronizedMethods();
 
    IntStream.range(<span class="hljs-number">0</span>, <span class="hljs-number">1000</span>)
      .forEach(count -> service.submit(method::synchronisedCalculate));
    service.awaitTermination(<span class="hljs-number">1000</span>, TimeUnit.MILLISECONDS);
 
    assertEquals(<span class="hljs-number">1000</span>, method.getSum());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里synchronized将会锁住该方法的实例对象，多个线程中只有获得该实例对象锁的线程才能够执行。</p>
<h3 data-id="heading-14">Synchronized Static Methods</h3>
<p>Synchronized关键词也可以用在static方法前面：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">synchronized</span> <span class="hljs-keyword">void</span> <span class="hljs-title">syncStaticCalculate</span><span class="hljs-params">()</span> </span>&#123;
        staticSum = staticSum + <span class="hljs-number">1</span>;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Synchronized放在static方法前面和实例方法前面锁住的对象不同。放在static方法前面锁住的对象是这个Class本身，因为一个Class在JVM中只会存在一个，所以不管有多少该Class的实例，在同一时刻只会有一个线程可以执行该放方法。</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">givenMultiThread_whenStaticSyncMethod</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        ExecutorService service = Executors.newCachedThreadPool();

        IntStream.range(<span class="hljs-number">0</span>, <span class="hljs-number">1000</span>)
                .forEach(count ->
                        service.submit(SynchronizedMethods::syncStaticCalculate));
        service.shutdown();
        service.awaitTermination(<span class="hljs-number">100</span>, TimeUnit.MILLISECONDS);

        assertEquals(<span class="hljs-number">1000</span>, SynchronizedMethods.staticSum);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">Synchronized Blocks</h3>
<p>有时候，我们可能不需要Synchronize整个方法，而是同步其中的一部分，这时候，我们可以使用Synchronized Blocks：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">performSynchronizedTask</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">synchronized</span> (<span class="hljs-keyword">this</span>) &#123;
            setSum(getSum() + <span class="hljs-number">1</span>);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看下怎么测试：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">givenMultiThread_whenBlockSync</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        ExecutorService service = Executors.newFixedThreadPool(<span class="hljs-number">3</span>);
        SynchronizedMethods synchronizedBlocks = <span class="hljs-keyword">new</span> SynchronizedMethods();

        IntStream.range(<span class="hljs-number">0</span>, <span class="hljs-number">1000</span>)
                .forEach(count ->
                        service.submit(synchronizedBlocks::performSynchronizedTask));
        service.shutdown();
        service.awaitTermination(<span class="hljs-number">100</span>, TimeUnit.MILLISECONDS);

        assertEquals(<span class="hljs-number">1000</span>, synchronizedBlocks.getSum());
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们同步的是实例，如果在静态方法中，我们也可以同步class：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">performStaticSyncTask</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-keyword">synchronized</span> (SynchronizedMethods.class) &#123;
            staticSum = staticSum + <span class="hljs-number">1</span>;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看下怎么测试：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">givenMultiThread_whenStaticSyncBlock</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        ExecutorService service = Executors.newCachedThreadPool();

        IntStream.range(<span class="hljs-number">0</span>, <span class="hljs-number">1000</span>)
                .forEach(count ->
                        service.submit(SynchronizedMethods::performStaticSyncTask));
        service.shutdown();
        service.awaitTermination(<span class="hljs-number">100</span>, TimeUnit.MILLISECONDS);

        assertEquals(<span class="hljs-number">1000</span>, SynchronizedMethods.staticSum);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">第三章 java中的Volatile关键字使用</h1>
<p>在本文中，我们会介绍java中的一个关键字volatile。 volatile的中文意思是易挥发的，不稳定的。那么在java中使用是什么意思呢？</p>
<p>我们知道，在java中，每个线程都会有个自己的内存空间，我们称之为working memory。这个空间会缓存一些变量的信息，从而提升程序的性能。当执行完某个操作之后，thread会将更新后的变量更新到主缓存中，以供其他线程读写。</p>
<p>因为变量存在working memory和main memory两个地方，那么就有可能出现不一致的情况。 那么我们就可以使用Volatile关键字来强制将变量直接写到main memory，从而保证了不同线程读写到的是同一个变量。</p>
<h2 data-id="heading-17">什么时候使用volatile</h2>
<p>那么我们什么时候使用volatile呢？当一个线程需要立刻读取到另外一个线程修改的变量值的时候，我们就可以使用volatile。我们来举个例子：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VolatileWithoutUsage</span> </span>&#123;
    <span class="hljs-keyword">private</span>  <span class="hljs-keyword">int</span> count = <span class="hljs-number">0</span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">incrementCount</span><span class="hljs-params">()</span> </span>&#123;
        count++;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getCount</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> count;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个类定义了一个incrementCount()方法，会去更新count值，我们接下来在多线程环境中去测试这个方法：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testWithoutVolatile</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        ExecutorService service= Executors.newFixedThreadPool(<span class="hljs-number">3</span>);
        VolatileWithoutUsage volatileWithoutUsage=<span class="hljs-keyword">new</span> VolatileWithoutUsage();

        IntStream.range(<span class="hljs-number">0</span>,<span class="hljs-number">1000</span>).forEach(count ->service.submit(volatileWithoutUsage::incrementCount) );
        service.shutdown();
        service.awaitTermination(<span class="hljs-number">1000</span>, TimeUnit.MILLISECONDS);
        assertEquals(<span class="hljs-number">1000</span>,volatileWithoutUsage.getCount() );
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行一下，我们会发现结果是不等于1000的。</p>
<pre><code class="hljs language-txt copyable" lang="txt">
java.lang.AssertionError: 
Expected :1000
Actual   :999
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是因为多线程去更新同一个变量，我们在上篇文章也提到了，这种情况可以通过加Synchronized关键字来解决。</p>
<p>那么是不是我们加上Volatile关键字后就可以解决这个问题了呢？</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VolatileFalseUsage</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">volatile</span> <span class="hljs-keyword">int</span> count = <span class="hljs-number">0</span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">incrementCount</span><span class="hljs-params">()</span> </span>&#123;
        count++;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getCount</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> count;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的类中，我们加上了关键字Volatile，我们再测试一下：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testWithVolatileFalseUsage</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        ExecutorService service= Executors.newFixedThreadPool(<span class="hljs-number">3</span>);
        VolatileFalseUsage volatileFalseUsage=<span class="hljs-keyword">new</span> VolatileFalseUsage();

        IntStream.range(<span class="hljs-number">0</span>,<span class="hljs-number">1000</span>).forEach(count ->service.submit(volatileFalseUsage::incrementCount) );
        service.shutdown();
        service.awaitTermination(<span class="hljs-number">5000</span>, TimeUnit.MILLISECONDS);
        assertEquals(<span class="hljs-number">1000</span>,volatileFalseUsage.getCount() );
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行一下，我们会发现结果还是错误的：</p>
<pre><code class="hljs language-txt copyable" lang="txt">java.lang.AssertionError: 
Expected :1000
Actual   :992
~~

为什么呢？ 我们先来看下count++的操作，count++可以分解为三步操作，1. 读取count的值，2.给count加1， 3.将count写回内存。添加Volatile关键词只能够保证count的变化立马可见，而不能保证1，2，3这三个步骤的总体原子性。 要实现总体的原子性还是需要用到类似Synchronized的关键字。

下面看下正确的用法：

~~~java
public class VolatileTrueUsage &#123;
    private volatile int count = 0;

    public void setCount(int number) &#123;
        count=number;
    &#125;
    public int getCount() &#123;
        return count;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testWithVolatileTrueUsage</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        VolatileTrueUsage volatileTrueUsage=<span class="hljs-keyword">new</span> VolatileTrueUsage();
        Thread threadA = <span class="hljs-keyword">new</span> Thread(()->volatileTrueUsage.setCount(<span class="hljs-number">10</span>));
        threadA.start();
        Thread.sleep(<span class="hljs-number">100</span>);

        Thread reader = <span class="hljs-keyword">new</span> Thread(() -> &#123;
            <span class="hljs-keyword">int</span> valueReadByThread = volatileTrueUsage.getCount();
            assertEquals(<span class="hljs-number">10</span>, valueReadByThread);
        &#125;);
        reader.start();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">Happens-Before</h2>
<p>从java5之后，volatile提供了一个Happens-Before的功能。Happens-Before 是指当volatile进行写回主内存的操作时，会将之前的非volatile的操作一并写回主内存。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VolatileHappenBeforeUsage</span> </span>&#123;

    <span class="hljs-keyword">int</span> a = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">volatile</span> <span class="hljs-keyword">boolean</span> flag = <span class="hljs-keyword">false</span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">writer</span><span class="hljs-params">()</span> </span>&#123;
        a = <span class="hljs-number">1</span>;              <span class="hljs-comment">// 1 线程A修改共享变量</span>
        flag = <span class="hljs-keyword">true</span>;        <span class="hljs-comment">// 2 线程A写volatile变量</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中，a是一个非volatile变量，flag是一个volatile变量，但是由于happens-before的特性，a 将会表现的和volatile一样。</p>
<h1 data-id="heading-19">第四章  wait和sleep的区别</h1>
<p>在本篇文章中，我们将会讨论一下java中wait()和sleep()方法的区别。并讨论一下怎么使用这两个方法。</p>
<h2 data-id="heading-20">Wait和sleep的区别</h2>
<p>wait() 是Object中定义的native方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">native</span> <span class="hljs-keyword">void</span> <span class="hljs-title">wait</span><span class="hljs-params">(<span class="hljs-keyword">long</span> timeout)</span> <span class="hljs-keyword">throws</span> InterruptedException</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以每一个类的实例都可以调用这个方法。wait()只能在synchronized block中调用。它会释放synchronized时加在object上的锁。</p>
<p>sleep()是定义Thread中的native静态类方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">native</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sleep</span><span class="hljs-params">(<span class="hljs-keyword">long</span> millis)</span> <span class="hljs-keyword">throws</span> InterruptedException</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以Thread.sleep()可以在任何情况下调用。Thread.sleep()将会暂停当前线程，并且不会释放任何锁资源。</p>
<p>我们先看一下一个简单的wait使用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Slf4j</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WaitUsage</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Object LOCK = <span class="hljs-keyword">new</span> Object();

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">WaitExample</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        <span class="hljs-keyword">synchronized</span> (LOCK) &#123;
            LOCK.wait(<span class="hljs-number">1000</span>);
            log.info(<span class="hljs-string">"Object '"</span> + LOCK + <span class="hljs-string">"' is woken after"</span> +
                    <span class="hljs-string">" waiting for 1 second"</span>);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看一下sleep的使用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Slf4j</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SleepUsage</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sleepExample</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        Thread.sleep(<span class="hljs-number">1000</span>);
        log.info(
                <span class="hljs-string">"Thread '"</span> + Thread.currentThread().getName() +
                        <span class="hljs-string">"' is woken after sleeping for 1 second"</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">唤醒wait和sleep</h2>
<p>sleep()方法自带sleep时间，时间过后，Thread会自动被唤醒。
或者可以通过调用interrupt()方法来中断。</p>
<p>相比而言wait的唤醒会比较复杂，我们需要调用notify() 和 notifyAll()方法来唤醒等待在特定wait object上的线程。</p>
<p>notify()会根据线程调度的机制选择一个线程来唤醒，而notifyAll()会唤醒所有等待的线程，由这些线程重新争夺资源锁。</p>
<p>wait,notity通常用在生产者和消费者情形，我们看下怎么使用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Slf4j</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WaitNotifyUsage</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> count =<span class="hljs-number">0</span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">produceMessage</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;

        <span class="hljs-keyword">while</span>(<span class="hljs-keyword">true</span>) &#123;
            <span class="hljs-keyword">synchronized</span> (<span class="hljs-keyword">this</span>) &#123;
                <span class="hljs-keyword">while</span> (count == <span class="hljs-number">5</span>) &#123;
                    log.info(<span class="hljs-string">"count == 5 , wait ...."</span>);
                    wait();
                &#125;
                count++;
                log.info(<span class="hljs-string">"produce count &#123;&#125;"</span>, count);
                notify();
            &#125;
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">consumeMessage</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;

        <span class="hljs-keyword">while</span> (<span class="hljs-keyword">true</span>) &#123;
            <span class="hljs-keyword">synchronized</span> (<span class="hljs-keyword">this</span>) &#123;
                <span class="hljs-keyword">while</span> (count == <span class="hljs-number">0</span>) &#123;
                    log.info(<span class="hljs-string">"count == 0, wait ..."</span>);
                    wait();
                &#125;
                log.info(<span class="hljs-string">"consume count &#123;&#125;"</span>, count);
                count--;
                notify();
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看下怎么调用：</p>
<pre><code class="hljs language-java copyable" lang="java">   <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testWaitNotifyUsage</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException</span>&#123;
        WaitNotifyUsage waitNotifyUsage=<span class="hljs-keyword">new</span> WaitNotifyUsage();

        ExecutorService executorService=Executors.newFixedThreadPool(<span class="hljs-number">4</span>);
        executorService.submit(()-> &#123;
            <span class="hljs-keyword">try</span> &#123;
                waitNotifyUsage.produceMessage();
            &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
                e.printStackTrace();
            &#125;
        &#125;);

        executorService.submit(()-> &#123;
            <span class="hljs-keyword">try</span> &#123;
                waitNotifyUsage.consumeMessage();
            &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
                e.printStackTrace();
            &#125;
        &#125;);

        Thread.sleep(<span class="hljs-number">50000</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-22">第五章 java中Future的使用</h1>
<p>Future是java 1.5引入的一个interface，可以方便的用于异步结果的获取。 本文将会通过具体的例子讲解如何使用Future。</p>
<h2 data-id="heading-23">创建Future</h2>
<p>正如上面所说，Future代表的是异步执行的结果，意思是当异步执行结束之后，返回的结果将会保存在Future中。</p>
<p>那么我们什么时候会用到Future呢？ 一般来说，当我们执行一个长时间运行的任务时，使用Future就可以让我们暂时去处理其他的任务，等长任务执行完毕再返回其结果。</p>
<p>经常会使用到Future的场景有：1. 计算密集场景。2. 处理大数据量。3. 远程方法调用等。</p>
<p>接下来我们将会使用ExecutorService来创建一个Future。</p>
<pre><code class="hljs language-java copyable" lang="java">    <T> <span class="hljs-function">Future<T> <span class="hljs-title">submit</span><span class="hljs-params">(Callable<T> task)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面是ExecutorService中定义的一个submit方法，它接收一个Callable参数，并返回一个Future。</p>
<p>我们用一个线程来计算一个平方运算：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-keyword">private</span> ExecutorService executor
            = Executors.newSingleThreadExecutor();

    <span class="hljs-function"><span class="hljs-keyword">public</span> Future<Integer> <span class="hljs-title">calculate</span><span class="hljs-params">(Integer input)</span> </span>&#123;
        <span class="hljs-keyword">return</span> executor.submit(() -> &#123;
            System.out.println(<span class="hljs-string">"Calculating..."</span>+ input);
            Thread.sleep(<span class="hljs-number">1000</span>);
            <span class="hljs-keyword">return</span> input * input;
        &#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>submit需要接受一个Callable参数，Callable需要实现一个call方法，并返回结果。这里我们使用lamaba表达式来简化这一个流程。</p>
<h2 data-id="heading-24">从Future获取结果</h2>
<p>上面我们创建好了Future，接下来我们看一下怎么获取到Future的值。</p>
<pre><code class="hljs language-java copyable" lang="java">       FutureUsage futureUsage=<span class="hljs-keyword">new</span> FutureUsage();
        Future<Integer> futureOne = futureUsage.calculate(<span class="hljs-number">20</span>);
        <span class="hljs-keyword">while</span>(!futureOne.isDone()) &#123;
            System.out.println(<span class="hljs-string">"Calculating..."</span>);
            Thread.sleep(<span class="hljs-number">300</span>);
        &#125;
        Integer result = futureOne.get();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先我们通过Future.isDone() 来判断这个异步操作是否执行完毕，如果完毕我们就可以直接调用futureOne.get()来获得Futre的结果。</p>
<p>这里futureOne.get()是一个阻塞操作，会一直等待异步执行完毕才返回结果。</p>
<p>如果我们不想等待，future提供了一个带时间的方法：</p>
<pre><code class="hljs language-java copyable" lang="java">Integer result = futureOne.get(<span class="hljs-number">500</span>, TimeUnit.MILLISECONDS);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在等待时间结束的时候，Future还有返回，则会抛出一个TimeoutException。</p>
<h2 data-id="heading-25">取消Future</h2>
<p>如果我们提交了一个异步程序，但是想取消它， 则可以这样：</p>
<pre><code class="hljs language-java copyable" lang="java">uture<Integer> futureTwo = futureUsage.calculate(<span class="hljs-number">4</span>);

        <span class="hljs-keyword">boolean</span> canceled = futureTwo.cancel(<span class="hljs-keyword">true</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Future.cancel(boolean) 传入一个boolean参数，来选择是否中断正在运行的task。</p>
<p>如果我们cancel之后，再次调用get()方法，则会抛出CancellationException。</p>
<h2 data-id="heading-26">多线程环境中运行</h2>
<p>如果有两个计算任务，先看下在单线程下运行的结果。</p>
<pre><code class="hljs language-java copyable" lang="java">        Future<Integer> future1 = futureUsage.calculate(<span class="hljs-number">10</span>);
        Future<Integer> future2 = futureUsage.calculate(<span class="hljs-number">100</span>);

        <span class="hljs-keyword">while</span> (!(future1.isDone() && future2.isDone())) &#123;
            System.out.println(
                    String.format(
                            <span class="hljs-string">"future1 is %s and future2 is %s"</span>,
                            future1.isDone() ? <span class="hljs-string">"done"</span> : <span class="hljs-string">"not done"</span>,
                            future2.isDone() ? <span class="hljs-string">"done"</span> : <span class="hljs-string">"not done"</span>
                    )
            );
            Thread.sleep(<span class="hljs-number">300</span>);
        &#125;

        Integer result1 = future1.get();
        Integer result2 = future2.get();

        System.out.println(result1 + <span class="hljs-string">" and "</span> + result2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为我们通过Executors.newSingleThreadExecutor（）来创建的单线程池。所以运行结果如下：</p>
<pre><code class="hljs language-txt copyable" lang="txt">Calculating...10
future1 is not done and future2 is not done
future1 is not done and future2 is not done
future1 is not done and future2 is not done
future1 is not done and future2 is not done
Calculating...100
future1 is done and future2 is not done
future1 is done and future2 is not done
future1 is done and future2 is not done
100 and 10000
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们使用Executors.newFixedThreadPool(2)来创建一个多线程池，则可以得到如下的结果：</p>
<pre><code class="hljs language-txt copyable" lang="txt">calculating...10
calculating...100
future1 is not done and future2 is not done
future1 is not done and future2 is not done
future1 is not done and future2 is not done
future1 is not done and future2 is not done
100 and 10000
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-27">第六章 java并发中ExecutorService的使用</h1>
<p>ExecutorService是java中的一个异步执行的框架，通过使用ExecutorService可以方便的创建多线程执行环境。</p>
<p>本文将会详细的讲解ExecutorService的具体使用。</p>
<h2 data-id="heading-28">创建ExecutorService</h2>
<p>通常来说有两种方法来创建ExecutorService。</p>
<p>第一种方式是使用Executors中的工厂类方法，例如：</p>
<pre><code class="hljs language-java copyable" lang="java">ExecutorService executor = Executors.newFixedThreadPool(<span class="hljs-number">10</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了newFixedThreadPool方法之外，Executors还包含了很多创建ExecutorService的方法。</p>
<p>第二种方法是直接创建一个ExecutorService， 因为ExecutorService是一个interface，我们需要实例化ExecutorService的一个实现。</p>
<p>这里我们使用ThreadPoolExecutor来举例：</p>
<pre><code class="hljs language-java copyable" lang="java">ExecutorService executorService =
            <span class="hljs-keyword">new</span> ThreadPoolExecutor(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0L</span>, TimeUnit.MILLISECONDS,
                    <span class="hljs-keyword">new</span> LinkedBlockingQueue<Runnable>());
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">为ExecutorService分配Tasks</h2>
<p>ExecutorService可以执行Runnable和Callable的task。其中Runnable是没有返回值的，而Callable是有返回值的。我们分别看一下两种情况的使用：</p>
<pre><code class="hljs language-java copyable" lang="java">Runnable runnableTask = () -> &#123;
    <span class="hljs-keyword">try</span> &#123;
        TimeUnit.MILLISECONDS.sleep(<span class="hljs-number">300</span>);
    &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
        e.printStackTrace();
    &#125;
&#125;;
 
Callable<String> callableTask = () -> &#123;
    TimeUnit.MILLISECONDS.sleep(<span class="hljs-number">300</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Task's execution"</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将task分配给ExecutorService，可以通过调用xecute(), submit(), invokeAny(), invokeAll()这几个方法来实现。</p>
<p>execute() 返回值是void，他用来提交一个Runnable task。</p>
<pre><code class="hljs language-java copyable" lang="java">executorService.execute(runnableTask);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>submit() 返回值是Future，它可以提交Runnable task, 也可以提交Callable task。 提交Runnable的有两个方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><T> <span class="hljs-function">Future<T> <span class="hljs-title">submit</span><span class="hljs-params">(Runnable task, T result)</span></span>;

Future<?> submit(Runnable task);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个方法在返回传入的result。第二个方法返回null。</p>
<p>再看一下callable的使用：</p>
<pre><code class="hljs language-java copyable" lang="java">Future<String> future = 
  executorService.submit(callableTask);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>invokeAny() 将一个task列表传递给executorService，并返回其中的一个成功返回的结果。</p>
<pre><code class="hljs language-java copyable" lang="java">String result = executorService.invokeAny(callableTasks);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>invokeAll() 将一个task列表传递给executorService，并返回所有成功执行的结果：</p>
<pre><code class="hljs language-java copyable" lang="java">List<Future<String>> futures = executorService.invokeAll(callableTasks);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">关闭ExecutorService</h2>
<p>如果ExecutorService中的任务运行完毕之后，ExecutorService不会自动关闭。它会等待接收新的任务。如果需要关闭ExecutorService， 我们需要调用shutdown() 或者 shutdownNow() 方法。</p>
<p>shutdown() 会立即销毁ExecutorService，它会让ExecutorServic停止接收新的任务，并等待现有任务全部执行完毕再销毁。</p>
<pre><code class="hljs language-java copyable" lang="java">executorService.shutdown();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>shutdownNow()并不保证所有的任务都被执行完毕，它会返回一个未执行任务的列表：</p>
<pre><code class="hljs language-java copyable" lang="java">List<Runnable> notExecutedTasks = executorService.shutdownNow();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>oracle推荐的最佳关闭方法是和awaitTermination一起使用：</p>
<pre><code class="hljs language-java copyable" lang="java">executorService.shutdown();
       <span class="hljs-keyword">try</span> &#123;
           <span class="hljs-keyword">if</span> (!executorService.awaitTermination(<span class="hljs-number">800</span>, TimeUnit.MILLISECONDS)) &#123;
               executorService.shutdownNow();
           &#125;
       &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
           executorService.shutdownNow();
       &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先停止接收任务，然后再等待一定的时间让所有的任务都执行完毕，如果超过了给定的时间，则立刻结束任务。</p>
<h2 data-id="heading-31">Future</h2>
<p>submit() 和 invokeAll() 都会返回Future对象。之前的文章我们已经详细讲过了Future。 这里就只列举一下怎么使用：</p>
<pre><code class="hljs language-java copyable" lang="java">Future<String> future = executorService.submit(callableTask);
String result = <span class="hljs-keyword">null</span>;
<span class="hljs-keyword">try</span> &#123;
   result = future.get();
&#125; <span class="hljs-keyword">catch</span> (InterruptedException | ExecutionException e) &#123;
   e.printStackTrace();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">ScheduledExecutorService</h2>
<p>ScheduledExecutorService为我们提供了定时执行任务的机制。</p>
<p>我们这样创建ScheduledExecutorService：</p>
<pre><code class="hljs language-java copyable" lang="java">ScheduledExecutorService executorService
                = Executors.newSingleThreadScheduledExecutor();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>executorService的schedule方法，可以传入Runnable也可以传入Callable：</p>
<pre><code class="hljs language-java copyable" lang="java">Future<String> future = executorService.schedule(() -> &#123;
        <span class="hljs-comment">// ...</span>
        <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello world"</span>;
    &#125;, <span class="hljs-number">1</span>, TimeUnit.SECONDS);
 
    ScheduledFuture<?> scheduledFuture = executorService.schedule(() -> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;, <span class="hljs-number">1</span>, TimeUnit.SECONDS);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有两个比较相近的方法：</p>
<pre><code class="hljs language-java copyable" lang="java">scheduleAtFixedRate( Runnable command, <span class="hljs-keyword">long</span> initialDelay, <span class="hljs-keyword">long</span> period, TimeUnit unit )

scheduleWithFixedDelay( Runnable command, <span class="hljs-keyword">long</span> initialDelay, <span class="hljs-keyword">long</span> delay, TimeUnit unit ) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两者的区别是前者的period是以任务开始时间来计算的，后者是以任务结束时间来计算。</p>
<h2 data-id="heading-33">ExecutorService和 Fork/Join</h2>
<p>java 7 引入了Fork/Join框架。 那么两者的区别是什么呢？</p>
<p>ExecutorService可以由用户来自己控制生成的线程，提供了对线程更加细粒度的控制。而Fork/Join则是为了让任务更加快速的执行完毕。</p>
<h1 data-id="heading-34">第七章 java中Runnable和Callable的区别</h1>
<p>在java的多线程开发中Runnable一直以来都是多线程的核心，而Callable是java1.5添加进来的一个增强版本。</p>
<p>本文我们会详细探讨Runnable和Callable的区别。</p>
<h2 data-id="heading-35">运行机制</h2>
<p>首先看下Runnable和Callable的接口定义：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@FunctionalInterface</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Runnable</span> </span>&#123;
    <span class="hljs-comment">/**
     * When an object implementing interface <code>Runnable</code> is used
     * to create a thread, starting the thread causes the object's
     * <code>run</code> method to be called in that separately executing
     * thread.
     * <p>
     * The general contract of the method <code>run</code> is that it may
     * take any action whatsoever.
     *
     * <span class="hljs-doctag">@see</span>     java.lang.Thread#run()
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@FunctionalInterface</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Callable</span><<span class="hljs-title">V</span>> </span>&#123;
    <span class="hljs-comment">/**
     * Computes a result, or throws an exception if unable to do so.
     *
     * <span class="hljs-doctag">@return</span> computed result
     * <span class="hljs-doctag">@throws</span> Exception if unable to compute a result
     */</span>
    <span class="hljs-function">V <span class="hljs-title">call</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> Exception</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Runnable需要实现run（）方法，Callable需要实现call（）方法。</p>
<p>我们都知道要自定义一个Thread有两种方法，一是继承Thread，而是实现Runnable接口，这是因为Thread本身就是一个Runnable的实现：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Thread</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span> </span>&#123;
    <span class="hljs-comment">/* Make sure registerNatives is the first thing <clinit> does. */</span>
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">native</span> <span class="hljs-keyword">void</span> <span class="hljs-title">registerNatives</span><span class="hljs-params">()</span></span>;
    <span class="hljs-keyword">static</span> &#123;
        registerNatives();
    &#125;
    ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以Runnable可以通过Runnable和之前我们介绍的ExecutorService 来执行，而Callable则只能通过ExecutorService 来执行。</p>
<h2 data-id="heading-36">返回值的不同</h2>
<p>根据上面两个接口的定义，Runnable是不返还值的，而Callable可以返回值。</p>
<p>如果我们都通过ExecutorService来提交，看看有什么不同：</p>
<ul>
<li>使用runnable</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">executeTask</span><span class="hljs-params">()</span> </span>&#123;
        ExecutorService executorService = Executors.newSingleThreadExecutor();
        Future future = executorService.submit(()->log.info(<span class="hljs-string">"in runnable!!!!"</span>));
        executorService.shutdown();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用callable</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">executeTask</span><span class="hljs-params">()</span> </span>&#123;
        ExecutorService executorService = Executors.newSingleThreadExecutor();
        Future future = executorService.submit(()->&#123;
            log.info(<span class="hljs-string">"in callable!!!!"</span>);
            <span class="hljs-keyword">return</span> <span class="hljs-string">"callable"</span>;
        &#125;);
        executorService.shutdown();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然我们都返回了Future，但是runnable的情况下Future将不包含任何值。</p>
<h2 data-id="heading-37">Exception处理</h2>
<p>Runnable的run（）方法定义没有抛出任何异常，所以任何的Checked Exception都需要在run（）实现方法中自行处理。</p>
<p>Callable的Call（）方法抛出了throws Exception，所以可以在call（）方法的外部，捕捉到Checked Exception。我们看下Callable中异常的处理。</p>
<pre><code class="hljs language-java copyable" lang="java"> <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">executeTaskWithException</span><span class="hljs-params">()</span></span>&#123;
        ExecutorService executorService = Executors.newSingleThreadExecutor();
        Future future = executorService.submit(()->&#123;
            log.info(<span class="hljs-string">"in callable!!!!"</span>);
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> CustomerException(<span class="hljs-string">"a customer Exception"</span>);
        &#125;);
        <span class="hljs-keyword">try</span> &#123;
            Object object= future.get();
        &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (ExecutionException e) &#123;
            e.printStackTrace();
            e.getCause();
        &#125;
        executorService.shutdown();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中，我们在Callable中抛出了一个自定义的CustomerException。</p>
<p>这个异常会被包含在返回的Future中。当我们调用future.get()方法时，就会抛出ExecutionException，通过e.getCause()，就可以获取到包含在里面的具体异常信息。</p>
<h1 data-id="heading-38">第八章 ThreadLocal的使用</h1>
<p>ThreadLocal主要用来为当前线程存储数据，这个数据只有当前线程可以访问。</p>
<p>在定义ThreadLocal的时候，我们可以同时定义存储在ThreadLocal中的特定类型的对象。</p>
<pre><code class="hljs language-java copyable" lang="java">ThreadLocal<Integer> threadLocalValue = <span class="hljs-keyword">new</span> ThreadLocal<>();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们定义了一个存储Integer的ThreadLocal对象。</p>
<p>要存储和获取ThreadLocal中的对象也非常简单，使用get（）和set（）即可：</p>
<pre><code class="hljs language-java copyable" lang="java">threadLocalValue.set(<span class="hljs-number">1</span>);
Integer result = threadLocalValue.get();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我可以将ThreadLocal看成是一个map，而当前的线程就是map中的key。</p>
<p>除了new一个ThreadLocal对象，我们还可以通过：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <S> <span class="hljs-function">ThreadLocal<S> <span class="hljs-title">withInitial</span><span class="hljs-params">(Supplier<? extends S> supplier)</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> SuppliedThreadLocal<>(supplier);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ThreadLocal提供的静态方法withInitial来初始化一个ThreadLocal。</p>
<pre><code class="hljs language-java copyable" lang="java">ThreadLocal<Integer> threadLocal = ThreadLocal.withInitial(() -> <span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>withInitial需要一个Supplier对象，通过调用Supplier的get()方法获取到初始值。</p>
<p>要想删除ThreadLocal中的存储数据，可以调用：</p>
<pre><code class="hljs language-java copyable" lang="java">threadLocal.remove();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面我通过两个例子的对比，来看一下使用ThreadLocal的好处。</p>
<p>在实际的应用中，我们通常会需要为不同的用户请求存储不同的用户信息，一般来说我们需要构建一个全局的Map，来根据不同的用户ID，来存储不同的用户信息，方便在后面获取。</p>
<h2 data-id="heading-39">在Map中存储用户数据</h2>
<p>我们先看下如果使用全局的Map该怎么用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SharedMapWithUserContext</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span> </span>&#123;

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Map<Integer, Context> userContextPerUserId
            = <span class="hljs-keyword">new</span> ConcurrentHashMap<>();
    <span class="hljs-keyword">private</span> Integer userId;
    <span class="hljs-keyword">private</span> UserRepository userRepository = <span class="hljs-keyword">new</span> UserRepository();

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">SharedMapWithUserContext</span><span class="hljs-params">(<span class="hljs-keyword">int</span> i)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.userId=i;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        String userName = userRepository.getUserNameForUserId(userId);
        userContextPerUserId.put(userId, <span class="hljs-keyword">new</span> Context(userName));
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们定义了一个static的Map来存取用户信息。</p>
<p>再看一下怎么使用：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testWithMap</span><span class="hljs-params">()</span></span>&#123;
        SharedMapWithUserContext firstUser = <span class="hljs-keyword">new</span> SharedMapWithUserContext(<span class="hljs-number">1</span>);
        SharedMapWithUserContext secondUser = <span class="hljs-keyword">new</span> SharedMapWithUserContext(<span class="hljs-number">2</span>);
        <span class="hljs-keyword">new</span> Thread(firstUser).start();
        <span class="hljs-keyword">new</span> Thread(secondUser).start();
        assertEquals(SharedMapWithUserContext.userContextPerUserId.size(), <span class="hljs-number">2</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-40">在ThreadLocal中存储用户数据</h2>
<p>如果我们要在ThreadLocal中使用可以这样：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ThreadLocalWithUserContext</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> ThreadLocal<Context> userContext
            = <span class="hljs-keyword">new</span> ThreadLocal<>();
    <span class="hljs-keyword">private</span> Integer userId;
    <span class="hljs-keyword">private</span> UserRepository userRepository = <span class="hljs-keyword">new</span> UserRepository();

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">ThreadLocalWithUserContext</span><span class="hljs-params">(<span class="hljs-keyword">int</span> i)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.userId=i;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        String userName = userRepository.getUserNameForUserId(userId);
        userContext.set(<span class="hljs-keyword">new</span> Context(userName));
        System.out.println(<span class="hljs-string">"thread context for given userId: "</span>
                + userId + <span class="hljs-string">" is: "</span> + userContext.get());
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试代码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ThreadLocalWithUserContextTest</span> </span>&#123;

    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testWithThreadLocal</span><span class="hljs-params">()</span></span>&#123;
        ThreadLocalWithUserContext firstUser
                = <span class="hljs-keyword">new</span> ThreadLocalWithUserContext(<span class="hljs-number">1</span>);
        ThreadLocalWithUserContext secondUser
                = <span class="hljs-keyword">new</span> ThreadLocalWithUserContext(<span class="hljs-number">2</span>);
        <span class="hljs-keyword">new</span> Thread(firstUser).start();
        <span class="hljs-keyword">new</span> Thread(secondUser).start();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行之后，我们可以得到下面的结果：</p>
<pre><code class="hljs language-java copyable" lang="java">thread context <span class="hljs-keyword">for</span> given userId: <span class="hljs-number">1</span> is: com.flydean.Context@411734d4
thread context <span class="hljs-keyword">for</span> given userId: <span class="hljs-number">2</span> is: com.flydean.Context@1e9b6cc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不同的用户信息被存储在不同的线程环境中。</p>
<blockquote>
<p>注意，我们使用ThreadLocal的时候，一定是我们可以自由的控制所创建的线程。如果在ExecutorService环境下，就最好不要使用ThreadLocal，因为在ExecutorService中，线程是不可控的。</p>
</blockquote>
<h1 data-id="heading-41">第九章 java中线程的生命周期</h1>
<p>线程是java中绕不过去的一个话题， 今天本文将会详细讲解java中线程的生命周期，希望可以给大家一些启发。</p>
<h2 data-id="heading-42">java中Thread的状态</h2>
<p>java中Thread有6种状态，分别是：</p>
<ol>
<li>NEW - 新创建的Thread，还没有开始执行</li>
<li>RUNNABLE - 可运行状态的Thread，包括准备运行和正在运行的。</li>
<li>BLOCKED - 正在等待资源锁的线程</li>
<li>WAITING - 正在无限期等待其他线程来执行某个特定操作</li>
<li>TIMED_WAITING - 在一定的时间内等待其他线程来执行某个特定操作</li>
<li>TERMINATED - 线程执行完毕</li>
</ol>
<p>我们可以用一个图来直观的表示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d86fe0ff5e9345bf83da48e22a6bbcb0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>JDK代码中的定义如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">State</span> </span>&#123;
        <span class="hljs-comment">/**
         * Thread state for a thread which has not yet started.
         */</span>
        NEW,

        <span class="hljs-comment">/**
         * Thread state for a runnable thread.  A thread in the runnable
         * state is executing in the Java virtual machine but it may
         * be waiting for other resources from the operating system
         * such as processor.
         */</span>
        RUNNABLE,

        <span class="hljs-comment">/**
         * Thread state for a thread blocked waiting for a monitor lock.
         * A thread in the blocked state is waiting for a monitor lock
         * to enter a synchronized block/method or
         * reenter a synchronized block/method after calling
         * &#123;<span class="hljs-doctag">@link</span> Object#wait() Object.wait&#125;.
         */</span>
        BLOCKED,

        <span class="hljs-comment">/**
         * Thread state for a waiting thread.
         * A thread is in the waiting state due to calling one of the
         * following methods:
         * <ul>
         *   <li>&#123;<span class="hljs-doctag">@link</span> Object#wait() Object.wait&#125; with no timeout</li>
         *   <li>&#123;<span class="hljs-doctag">@link</span> #join() Thread.join&#125; with no timeout</li>
         *   <li>&#123;<span class="hljs-doctag">@link</span> LockSupport#park() LockSupport.park&#125;</li>
         * </ul>
         *
         * <p>A thread in the waiting state is waiting for another thread to
         * perform a particular action.
         *
         * For example, a thread that has called <tt>Object.wait()</tt>
         * on an object is waiting for another thread to call
         * <tt>Object.notify()</tt> or <tt>Object.notifyAll()</tt> on
         * that object. A thread that has called <tt>Thread.join()</tt>
         * is waiting for a specified thread to terminate.
         */</span>
        WAITING,

        <span class="hljs-comment">/**
         * Thread state for a waiting thread with a specified waiting time.
         * A thread is in the timed waiting state due to calling one of
         * the following methods with a specified positive waiting time:
         * <ul>
         *   <li>&#123;<span class="hljs-doctag">@link</span> #sleep Thread.sleep&#125;</li>
         *   <li>&#123;<span class="hljs-doctag">@link</span> Object#wait(long) Object.wait&#125; with timeout</li>
         *   <li>&#123;<span class="hljs-doctag">@link</span> #join(long) Thread.join&#125; with timeout</li>
         *   <li>&#123;<span class="hljs-doctag">@link</span> LockSupport#parkNanos LockSupport.parkNanos&#125;</li>
         *   <li>&#123;<span class="hljs-doctag">@link</span> LockSupport#parkUntil LockSupport.parkUntil&#125;</li>
         * </ul>
         */</span>
        TIMED_WAITING,

        <span class="hljs-comment">/**
         * Thread state for a terminated thread.
         * The thread has completed execution.
         */</span>
        TERMINATED;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-43">NEW</h2>
<p>NEW 表示线程创建了，但是还没有开始执行。我们看一个NEW的例子：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NewThread</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span></span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        Runnable runnable = <span class="hljs-keyword">new</span> NewThread();
        Thread t = <span class="hljs-keyword">new</span> Thread(runnable);
        log.info(t.getState().toString());
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码将会输出：</p>
<pre><code class="hljs language-txt copyable" lang="txt">NEW
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-44">Runnable</h2>
<p>Runnable表示线程正在可执行状态。包括正在运行和准备运行两种。</p>
<p>为什么这两种都叫做Runnable呢？我们知道在多任务环境中，CPU的个数是有限的，所以任务都是轮循占有CPU来处理的，JVM中的线程调度器会为每个线程分配特定的执行时间，当执行时间结束后，线程调度器将会释放CPU，以供其他的Runnable线程执行。</p>
<p>我们看一个Runnable的例子：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RunnableThread</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;

    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        Runnable runnable = <span class="hljs-keyword">new</span> RunnableThread();
        Thread t = <span class="hljs-keyword">new</span> Thread(runnable);
        t.start();
        log.info(t.getState().toString());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码将会输出：</p>
<pre><code class="hljs language-txt copyable" lang="txt">RUNNABLE
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-45">BLOCKED</h2>
<p>BLOCKED表示线程正在等待资源锁，而目前该资源正在被其他线程占有。</p>
<p>我们举个例子：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BlockThread</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        loopResource();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">synchronized</span> <span class="hljs-keyword">void</span> <span class="hljs-title">loopResource</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">while</span>(<span class="hljs-keyword">true</span>) &#123;
            <span class="hljs-comment">//无限循环</span>
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        Thread t1 = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">new</span> BlockThread());
        Thread t2 = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">new</span> BlockThread());

        t1.start();
        t2.start();

        Thread.sleep(<span class="hljs-number">1000</span>);
        log.info(t1.getState().toString());
        log.info(t2.getState().toString());
        System.exit(<span class="hljs-number">0</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中，由于t1是无限循环，将会一直占有资源锁，导致t2无法获取资源锁，从而位于BLOCKED状态。</p>
<p>我们会得到如下结果：</p>
<pre><code class="hljs language-txt copyable" lang="txt">12:40:11.710 [main] INFO com.flydean.BlockThread - RUNNABLE
12:40:11.713 [main] INFO com.flydean.BlockThread - BLOCKED
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-46">WAITING</h2>
<p>WAITING 状态表示线程正在等待其他的线程执行特定的操作。有三种方法可以导致线程处于WAITTING状态：</p>
<ol>
<li>object.wait()</li>
<li>thread.join()</li>
<li>LockSupport.park()</li>
</ol>
<p>其中1，2方法不需要传入时间参数。</p>
<p>我们看下使用的例子：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WaitThread</span> <span class="hljs-keyword">implements</span>  <span class="hljs-title">Runnable</span></span>&#123;

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Thread t1;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        Thread t2 = <span class="hljs-keyword">new</span> Thread(()->&#123;
            <span class="hljs-keyword">try</span> &#123;
                Thread.sleep(<span class="hljs-number">10000</span>);
            &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
                Thread.currentThread().interrupt();
                log.error(<span class="hljs-string">"Thread interrupted"</span>, e);
            &#125;
            log.info(<span class="hljs-string">"t1"</span>+t1.getState().toString());
        &#125;);
        t2.start();

        <span class="hljs-keyword">try</span> &#123;
            t2.join();
        &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
            Thread.currentThread().interrupt();
            log.error(<span class="hljs-string">"Thread interrupted"</span>, e);
        &#125;
        log.info(<span class="hljs-string">"t2"</span>+t2.getState().toString());
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        t1 = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">new</span> WaitThread());
        t1.start();

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，我们调用的t2.join()，这会使调用它的t1线程处于WAITTING状态。</p>
<p>我们看下输出结果：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-number">12</span>:<span class="hljs-number">44</span>:<span class="hljs-number">12.958</span> [Thread-<span class="hljs-number">1</span>] INFO com.flydean.WaitThread - t1 WAITING
<span class="hljs-number">12</span>:<span class="hljs-number">44</span>:<span class="hljs-number">12.964</span> [Thread-<span class="hljs-number">0</span>] INFO com.flydean.WaitThread - t2 TERMINATED
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-47">TIMED_WAITING</h2>
<p>TIMED_WAITING状态表示在一个有限的时间内等待其他线程执行特定的某些操作。</p>
<p>java中有5中方式来达到这种状态：</p>
<ol>
<li>thread.sleep(long millis)</li>
<li>wait(int timeout) 或者 wait(int timeout, int nanos)</li>
<li>thread.join(long millis)</li>
<li>LockSupport.parkNanos</li>
<li>LockSupport.parkUntil</li>
</ol>
<p>我们举个例子：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimedWaitThread</span> <span class="hljs-keyword">implements</span>  <span class="hljs-title">Runnable</span></span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            Thread.sleep(<span class="hljs-number">5000</span>);
        &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
            Thread.currentThread().interrupt();
            log.error(<span class="hljs-string">"Thread interrupted"</span>, e);
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        TimedWaitThread obj1 = <span class="hljs-keyword">new</span> TimedWaitThread();
        Thread t1 = <span class="hljs-keyword">new</span> Thread(obj1);
        t1.start();

        <span class="hljs-comment">// The following sleep will give enough time for ThreadScheduler</span>
        <span class="hljs-comment">// to start processing of thread t1</span>
        Thread.sleep(<span class="hljs-number">1000</span>);
        log.info(t1.getState().toString());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中我们调用了Thread.sleep(5000)来让线程处于TIMED_WAITING状态。</p>
<p>看下输出：</p>
<pre><code class="hljs language-txt copyable" lang="txt">12:58:02.706 [main] INFO com.flydean.TimedWaitThread - TIMED_WAITING
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么问题来了，TIMED_WAITING和WAITTING有什么区别呢？</p>
<p>TIMED_WAITING如果在给定的时间内没有等到其他线程的特定操作，则会被唤醒，从而进入争夺资源锁的队列，如果能够获取到锁，则会变成Runnable状态，如果获取不到锁，则会变成BLOCKED状态。</p>
<h2 data-id="heading-48">TERMINATED</h2>
<p>TERMINATED表示线程已经执行完毕。我们看下例子：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TerminatedThread</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span></span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;

    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        Thread t1 = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">new</span> TerminatedThread());
        t1.start();
        <span class="hljs-comment">// The following sleep method will give enough time for</span>
        <span class="hljs-comment">// thread t1 to complete</span>
        Thread.sleep(<span class="hljs-number">1000</span>);
        log.info(t1.getState().toString());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<pre><code class="hljs language-txt copyable" lang="txt">13:02:38.868 [main] INFO com.flydean.TerminatedThread - TERMINATED
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-49">第十章 java中join的使用</h1>
<p>join()应该是我们在java中经常会用到的一个方法，它主要是将当前线程置为WAITTING状态，然后等待调用的线程执行完毕或被interrupted。</p>
<p>join()是Thread中定义的方法，我们看下他的定义：</p>
<pre><code class="hljs language-java copyable" lang="java">   <span class="hljs-comment">/**
     * Waits for this thread to die.
     *
     * <p> An invocation of this method behaves in exactly the same
     * way as the invocation
     *
     * <blockquote>
     * &#123;<span class="hljs-doctag">@linkplain</span> #join(long) join&#125;&#123;<span class="hljs-doctag">@code</span> (0)&#125;
     * </blockquote>
     *
     * <span class="hljs-doctag">@throws</span>  InterruptedException
     *          if any thread has interrupted the current thread. The
     *          <i>interrupted status</i> of the current thread is
     *          cleared when this exception is thrown.
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">void</span> <span class="hljs-title">join</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        join(<span class="hljs-number">0</span>);
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看下join是怎么使用的，通常我们需要在线程A中调用线程B.join():</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">JoinThread</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span></span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> processingCount = <span class="hljs-number">0</span>;

    JoinThread(<span class="hljs-keyword">int</span> processingCount) &#123;
        <span class="hljs-keyword">this</span>.processingCount = processingCount;
        log.info(<span class="hljs-string">"Thread Created"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        log.info(<span class="hljs-string">"Thread "</span> + Thread.currentThread().getName() + <span class="hljs-string">" started"</span>);
        <span class="hljs-keyword">while</span> (processingCount > <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">try</span> &#123;
                Thread.sleep(<span class="hljs-number">1000</span>);
            &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
                log.info(<span class="hljs-string">"Thread "</span> + Thread.currentThread().getName() + <span class="hljs-string">" interrupted"</span>);
            &#125;
            processingCount--;
        &#125;
        log.info(<span class="hljs-string">"Thread "</span> + Thread.currentThread().getName() + <span class="hljs-string">" exiting"</span>);
    &#125;

    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">joinTest</span><span class="hljs-params">()</span>
            <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        Thread t2 = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">new</span> JoinThread(<span class="hljs-number">1</span>));
        t2.start();
        log.info(<span class="hljs-string">"Invoking join"</span>);
        t2.join();
        log.info(<span class="hljs-string">"Returned from join"</span>);
        log.info(<span class="hljs-string">"t2 status &#123;&#125;"</span>,t2.isAlive());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在主线程中调用了t2.join(),则主线程将会等待t2执行完毕，我们看下输出结果：</p>
<pre><code class="hljs language-txt copyable" lang="txt">06:17:14.775 [main] INFO com.flydean.JoinThread - Thread Created
06:17:14.779 [main] INFO com.flydean.JoinThread - Invoking join
06:17:14.779 [Thread-0] INFO com.flydean.JoinThread - Thread Thread-0 started
06:17:15.783 [Thread-0] INFO com.flydean.JoinThread - Thread Thread-0 exiting
06:17:15.783 [main] INFO com.flydean.JoinThread - Returned from join
06:17:15.783 [main] INFO com.flydean.JoinThread - t2 status false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当线程已经执行完毕或者还没开始执行的时候，join（）将会立即返回：</p>
<pre><code class="hljs language-java copyable" lang="java">Thread t1 = <span class="hljs-keyword">new</span> SampleThread(<span class="hljs-number">0</span>);
t1.join();  <span class="hljs-comment">//returns immediately</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>join还有两个带时间参数的方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">void</span> <span class="hljs-title">join</span><span class="hljs-params">(<span class="hljs-keyword">long</span> millis)</span> <span class="hljs-keyword">throws</span> InterruptedException
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">void</span> <span class="hljs-title">join</span><span class="hljs-params">(<span class="hljs-keyword">long</span> millis,<span class="hljs-keyword">int</span> nanos)</span> <span class="hljs-keyword">throws</span> InterruptedException
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在给定的时间内调用的线程没有返回，则主线程将会继续执行：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testJoinTimeout</span><span class="hljs-params">()</span>
            <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        Thread t3 =  <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">new</span> JoinThread(<span class="hljs-number">10</span>));
        t3.start();
        t3.join(<span class="hljs-number">1000</span>);
        log.info(<span class="hljs-string">"t3 status &#123;&#125;"</span>, t3.isAlive());
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子将会输出：</p>
<pre><code class="hljs language-txt copyable" lang="txt">06:30:58.159 [main] INFO com.flydean.JoinThread - Thread Created
06:30:58.163 [Thread-0] INFO com.flydean.JoinThread - Thread Thread-0 started
06:30:59.172 [main] INFO com.flydean.JoinThread - t3 status true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Join()还有个happen-before的特性，这就是如果thread t1调用 t2.join(), 那么当t2返回时，所有t2的变动都会t1可见。</p>
<p>之前我们讲volatile关键词的时候也提到了这个happen-before规则。  我们看下例子：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testHappenBefore</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
        JoinThread t4 =  <span class="hljs-keyword">new</span> JoinThread(<span class="hljs-number">10</span>);
        t4.start();
        <span class="hljs-comment">// not guaranteed to stop even if t4 finishes.</span>
        <span class="hljs-keyword">do</span> &#123;
            log.info(<span class="hljs-string">"inside the loop"</span>);
            Thread.sleep(<span class="hljs-number">1000</span>);
        &#125; <span class="hljs-keyword">while</span> ( t4.processingCount > <span class="hljs-number">0</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们运行下，可以看到while循环一直在进行中，即使t4中的变量已经变成了0。</p>
<p>所以如果我们需要在这种情况下使用的话，我们需要用到join（），或者其他的同步机制。</p>
<h1 data-id="heading-50">第十一章 怎么在java中关闭一个thread</h1>
<p>我们经常需要在java中用到thread，我们知道thread有一个start()方法可以开启一个线程。那么怎么关闭这个线程呢？</p>
<p>有人会说可以用Thread.stop（）方法。但是这个方法已经被废弃了。</p>
<p>根据Oracle的官方文档，Thread.stop是不安全的。因为调用stop方法的时候，将会释放它获取的所有监视器锁（通过传递ThreadDeath异常实现）。如果有资源该监视器锁所保护的话，就可能会出现数据不一致的异常。并且这种异常很难被发现。 所以现在已经不推荐是用Thread.stop方法了。</p>
<p>那我们还有两种方式来关闭一个Thread。</p>
<ol>
<li>Flag变量</li>
</ol>
<p>如果我们有一个无法自动停止的Thread，我们可以创建一个条件变量，通过不断判断该变量的值，来决定是否结束该线程的运行。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">KillThread</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span> </span>&#123;
    <span class="hljs-keyword">private</span> Thread worker;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> AtomicBoolean running = <span class="hljs-keyword">new</span> AtomicBoolean(<span class="hljs-keyword">false</span>);
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> interval;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">KillThread</span><span class="hljs-params">(<span class="hljs-keyword">int</span> sleepInterval)</span> </span>&#123;
        interval = sleepInterval;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">start</span><span class="hljs-params">()</span> </span>&#123;
        worker = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">this</span>);
        worker.start();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">stop</span><span class="hljs-params">()</span> </span>&#123;
        running.set(<span class="hljs-keyword">false</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        running.set(<span class="hljs-keyword">true</span>);
        <span class="hljs-keyword">while</span> (running.get()) &#123;
            <span class="hljs-keyword">try</span> &#123;
                Thread.sleep(interval);
            &#125; <span class="hljs-keyword">catch</span> (InterruptedException e)&#123;
                Thread.currentThread().interrupt();
                log.info(<span class="hljs-string">"Thread was interrupted, Failed to complete operation"</span>);
            &#125;
            <span class="hljs-comment">// do something here</span>
        &#125;
        log.info(<span class="hljs-string">"finished"</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        KillThread killThread= <span class="hljs-keyword">new</span> KillThread(<span class="hljs-number">1000</span>);
        killThread.start();
        killThread.stop();
    &#125;


&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中，我们通过定义一个AtomicBoolean 的原子变量来存储Flag标志。</p>
<p>我们将会在后面的文章中详细的讲解原子变量。</p>
<ol start="2">
<li>调用interrupt()方法</li>
</ol>
<p>通过调用interrupt()方法，将会中断正在等待的线程，并抛出InterruptedException异常。</p>
<p>根据Oracle的说明，如果你想自己处理这个异常的话，需要reasserts出去，注意，这里是reasserts而不是rethrows，因为有些情况下，无法rethrow这个异常，我们需要这样做：</p>
<pre><code class="hljs language-java copyable" lang="java"> Thread.currentThread().interrupt();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这将会reasserts InterruptedException异常。</p>
<p>看下我们第二种方法怎么调用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">KillThread</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Runnable</span> </span>&#123;
    <span class="hljs-keyword">private</span> Thread worker;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> AtomicBoolean running = <span class="hljs-keyword">new</span> AtomicBoolean(<span class="hljs-keyword">false</span>);
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> interval;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">KillThread</span><span class="hljs-params">(<span class="hljs-keyword">int</span> sleepInterval)</span> </span>&#123;
        interval = sleepInterval;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">start</span><span class="hljs-params">()</span> </span>&#123;
        worker = <span class="hljs-keyword">new</span> Thread(<span class="hljs-keyword">this</span>);
        worker.start();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">interrupt</span><span class="hljs-params">()</span> </span>&#123;
        running.set(<span class="hljs-keyword">false</span>);
        worker.interrupt();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">stop</span><span class="hljs-params">()</span> </span>&#123;
        running.set(<span class="hljs-keyword">false</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        running.set(<span class="hljs-keyword">true</span>);
        <span class="hljs-keyword">while</span> (running.get()) &#123;
            <span class="hljs-keyword">try</span> &#123;
                Thread.sleep(interval);
            &#125; <span class="hljs-keyword">catch</span> (InterruptedException e)&#123;
                Thread.currentThread().interrupt();
                log.info(<span class="hljs-string">"Thread was interrupted, Failed to complete operation"</span>);
            &#125;
            <span class="hljs-comment">// do something here</span>
        &#125;
        log.info(<span class="hljs-string">"finished"</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        KillThread killThread= <span class="hljs-keyword">new</span> KillThread(<span class="hljs-number">1000</span>);
        killThread.start();
        killThread.interrupt();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中，当线程在Sleep中时，调用了interrupt方法，sleep会退出，并且抛出InterruptedException异常。</p>
<h1 data-id="heading-51">第十二章 java中的Atomic类</h1>
<h2 data-id="heading-52">问题背景</h2>
<p>在多线程环境中，我们最常遇到的问题就是变量的值进行同步。因为变量需要在多线程中进行共享，所以我们必须需要采用一定的同步机制来进行控制。</p>
<p>通过之前的文章，我们知道可以采用Lock的机制，当然也包括今天我们讲的Atomic类。</p>
<p>下面我们从两种方式来分别介绍。</p>
<h2 data-id="heading-53">Lock</h2>
<p>在之前的文章中，我们也讲了同步的问题，我们再回顾一下。 如果定义了一个计数器如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Counter</span> </span>&#123;

    <span class="hljs-keyword">int</span> counter;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">increment</span><span class="hljs-params">()</span> </span>&#123;
        counter++;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是在单线程环境中，上面的代码没有任何问题。但是如果在多线程环境中，counter++将会得到不同的结果。</p>
<p>因为虽然counter++看起来是一个原子操作，但是它实际上包含了三个操作：读数据，加一，写回数据。</p>
<p>我们之前的文章也讲了，如何解决这个问题：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LockCounter</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">volatile</span> <span class="hljs-keyword">int</span> counter;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">synchronized</span> <span class="hljs-keyword">void</span> <span class="hljs-title">increment</span><span class="hljs-params">()</span> </span>&#123;
        counter++;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过加synchronized，保证同一时间只会有一个线程去读写counter变量。</p>
<p>通过volatile，保证所有的数据直接操作的主缓存，而不使用线程缓存。</p>
<p>这样虽然解决了问题，但是性能可能会受影响，因为synchronized会锁住整个LockCounter实例。</p>
<h2 data-id="heading-54">使用Atomic</h2>
<p>通过引入低级别的原子化语义命令（比如compare-and-swap (CAS)），从而能在保证效率的同时保证原子性。</p>
<p>一个标准的CAS包含三个操作：</p>
<ol>
<li>将要操作的内存地址M。</li>
<li>现有的变量A。</li>
<li>新的需要存储的变量B。</li>
</ol>
<p>CAS将会先比较A和M中存储的值是否一致，一致则表示其他线程未对该变量进行修改，则将其替换为B。 否则不做任何操作。</p>
<p>使用CAS可以不用阻塞其他的线程，但是我们需要自己处理好当更新失败的情况下的业务逻辑处理情况。</p>
<p>Java提供了很多Atomic类，最常用的包括AtomicInteger, AtomicLong, AtomicBoolean, 和 AtomicReference.</p>
<p>其中的主要方法：</p>
<ol>
<li>get() – 直接中主内存中读取变量的值，类似于volatile变量。</li>
<li>set() – 将变量写回主内存。类似于volatile变量。</li>
<li>lazySet() – 延迟写回主内存。一种常用的情景是将引用重置为null的情况。</li>
<li>compareAndSet() – 执行CAS操作，成功返回true，失败返回false。</li>
<li>weakCompareAndSet() – 比较弱的CAS操作，不同的是它不执行happens-before操作，从而不保证能够读取到其他变量最新的值。</li>
</ol>
<p>我们看下怎么用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AtomicCounter</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> AtomicInteger counter = <span class="hljs-keyword">new</span> AtomicInteger(<span class="hljs-number">0</span>);

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getValue</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> counter.get();
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">increment</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">while</span>(<span class="hljs-keyword">true</span>) &#123;
            <span class="hljs-keyword">int</span> existingValue = getValue();
            <span class="hljs-keyword">int</span> newValue = existingValue + <span class="hljs-number">1</span>;
            <span class="hljs-keyword">if</span>(counter.compareAndSet(existingValue, newValue)) &#123;
                <span class="hljs-keyword">return</span>;
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-55">第十三章 java中interrupt，interrupted和isInterrupted的区别</h1>
<p>前面的文章我们讲到了调用interrupt()来停止一个Thread，本文将会详细讲解java中三个非常相似的方法interrupt，interrupted和isInterrupted。</p>
<h2 data-id="heading-56">isInterrupted</h2>
<p>首先看下最简单的isInterrupted方法。isInterrupted是Thread类中的一个实例方法：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isInterrupted</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> isInterrupted(<span class="hljs-keyword">false</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过调用isInterrupted（）可以判断实例线程是否被中断。</p>
<p>它的内部调用了isInterrupted(false)方法：</p>
<pre><code class="hljs language-java copyable" lang="java">  <span class="hljs-comment">/**
     * Tests if some Thread has been interrupted.  The interrupted state
     * is reset or not based on the value of ClearInterrupted that is
     * passed.
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">native</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isInterrupted</span><span class="hljs-params">(<span class="hljs-keyword">boolean</span> ClearInterrupted)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法是个native方法，接收一个是否清除Interrupted标志位的参数。</p>
<p>我们可以看到isInterrupted()传入的参数是false，这就表示isInterrupted()只会判断是否被中断，而不会清除中断状态。</p>
<h2 data-id="heading-57">interrupted</h2>
<p>interrupted是Thread中的一个类方法：</p>
<pre><code class="hljs language-java copyable" lang="java"> <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">interrupted</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> currentThread().isInterrupted(<span class="hljs-keyword">true</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，interrupted（）也调用了isInterrupted(true)方法，不过它传递的参数是true，表示将会清除中断标志位。</p>
<blockquote>
<p>注意，因为interrupted()是一个类方法，调用isInterrupted(true)判断的是当前线程是否被中断。注意这里currentThread（）的使用。</p>
</blockquote>
<h2 data-id="heading-58">interrupt</h2>
<p>前面两个是判断是否中断的方法，而interrupt（）就是真正触发中断的方法。</p>
<p>我们先看下interrupt的定义：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">interrupt</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">this</span> != Thread.currentThread())
            checkAccess();

        <span class="hljs-keyword">synchronized</span> (blockerLock) &#123;
            Interruptible b = blocker;
            <span class="hljs-keyword">if</span> (b != <span class="hljs-keyword">null</span>) &#123;
                interrupt0();           <span class="hljs-comment">// Just to set the interrupt flag</span>
                b.interrupt(<span class="hljs-keyword">this</span>);
                <span class="hljs-keyword">return</span>;
            &#125;
        &#125;
        interrupt0();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从定义我们可以看到interrupt（）是一个实例方法。</p>
<p>它的工作要点有下面4点：</p>
<ol>
<li>
<p>如果当前线程实例在调用Object类的wait（），wait（long）或wait（long，int）方法或join（），join（long），join（long，int）方法，或者在该实例中调用了Thread.sleep（long）或Thread.sleep（long，int）方法，并且正在阻塞状态中时，则其中断状态将被清除，并将收到InterruptedException。</p>
</li>
<li>
<p>如果此线程在InterruptibleChannel上的I / O操作中处于被阻塞状态，则该channel将被关闭，该线程的中断状态将被设置为true，并且该线程将收到java.nio.channels.ClosedByInterruptException异常。</p>
</li>
<li>
<p>如果此线程在java.nio.channels.Selector中处于被被阻塞状态，则将设置该线程的中断状态为true，并且它将立即从select操作中返回。</p>
</li>
<li>
<p>如果上面的情况都不成立，则设置中断状态为true。</p>
</li>
</ol>
<p>我们来举个例子：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Slf4j</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">InterruptThread</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Thread</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span>  <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1000</span>; i++) &#123;
            log.info(<span class="hljs-string">"i= &#123;&#125;"</span>, (i+<span class="hljs-number">1</span>));
            log.info(<span class="hljs-string">"call inside thread.interrupted()： &#123;&#125;"</span>, Thread.interrupted());
        &#125;
    &#125;

    <span class="hljs-meta">@Test</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testInterrupt</span><span class="hljs-params">()</span></span>&#123;
        InterruptThread thread=<span class="hljs-keyword">new</span> InterruptThread();
        thread.start();
        thread.interrupt();
        <span class="hljs-comment">//test isInterrupted</span>
        log.info(<span class="hljs-string">"first call isInterrupted(): &#123;&#125;"</span>, thread.isInterrupted());
        log.info(<span class="hljs-string">"second call isInterrupted(): &#123;&#125;"</span>, thread.isInterrupted());

        <span class="hljs-comment">//test interrupted（)</span>
        log.info(<span class="hljs-string">"first call outside thread.interrupted()： &#123;&#125;"</span>, Thread.interrupted());
        log.info(<span class="hljs-string">"second call outside thread.interrupted() &#123;&#125;："</span>, Thread.interrupted());
        log.info(<span class="hljs-string">"thread is alive : &#123;&#125;"</span>,thread.isAlive() );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果如下：</p>
<pre><code class="hljs language-txt copyable" lang="txt">13:07:17.804 [main] INFO com.flydean.InterruptThread - first call isInterrupted(): true
13:07:17.808 [main] INFO com.flydean.InterruptThread - second call isInterrupted(): true

13:07:17.808 [Thread-1] INFO com.flydean.InterruptThread - call inside thread.interrupted()： true
13:07:17.808 [Thread-1] INFO com.flydean.InterruptThread - call inside thread.interrupted()： false

13:07:17.808 [main] INFO com.flydean.InterruptThread - first call outside thread.interrupted()： false
13:07:17.809 [main] INFO com.flydean.InterruptThread - second call outside thread.interrupted() false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中，两次调用thread.isInterrupted()的值都是true。</p>
<p>在线程内部调用Thread.interrupted()， 只有第一次返回的是ture，后面返回的都是false，这表明第一次被重置了。</p>
<p>在线程外部，因为并没有中断外部线程，所以返回的值一直都是false。</p>
<h1 data-id="heading-59">总结</h1>
<p>本文介绍了java并发系列文章1到14章，因为文件篇幅限制，剩下的章节将会在
5W字高质量java并发系列详解教程(下) 进行介绍，敬请期待！</p>
<p>本文的例子<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fddean2009%2Flearn-java-concurrency%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ddean2009/learn-java-concurrency/" ref="nofollow noopener noreferrer">github.com/ddean2009/l…</a></p>
<p>本文PDF下载链接<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fddean2009%2Fwww.flydean.com%2Fblob%2Fmaster%2Fjava%2Fconcurrent%2Fconcurrent-all-in-one.pdf" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ddean2009/www.flydean.com/blob/master/java/concurrent/concurrent-all-in-one.pdf" ref="nofollow noopener noreferrer">concurrent-all-in-one.pdf</a></p>
<blockquote>
<p>欢迎关注我的公众号:程序那些事，更多精彩等着您！
更多内容请访问 <a href="https://link.juejin.cn/?target=www.flydean.com" target="_blank" title="www.flydean.com" ref="nofollow noopener noreferrer">www.flydean.com</a></p>
</blockquote></div>  
</div>
            