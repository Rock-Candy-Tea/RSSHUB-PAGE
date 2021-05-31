
---
title: 'java架构师基础编程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=8809'
author: 掘金
comments: false
date: Mon, 31 May 2021 01:34:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=8809'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">死锁</h3>
<ul>
<li>DeadLockSample</li>
</ul>
<pre><code class="copyable">package deadLock;

public class DeadLockSample extends Thread &#123;
    private String first;
    private String second;
    public DeadLockSample(String name, String first, String second) &#123;
        super(name);
        this.first = first;
        this.second = second;
    &#125;

    public  void run() &#123;
        synchronized (first) &#123;
            System.out.println(this.getName()+this.getId() + " obtained: " + first);
            try &#123;
                Thread.sleep(1000L);
                synchronized (second) &#123;
                    System.out.println(this.getName() + " obtained: " + second);
                &#125;
            &#125; catch (InterruptedException e) &#123;
                
            &#125;
        &#125;
    &#125;
    public static void main(String[] args) throws InterruptedException &#123;
        long pid = ProcessHandle.current().pid();
        System.out.println("pid:"+pid);
        String lockA = "lockA";
        String lockB = "lockB";
        DeadLockSample t1 = new DeadLockSample("Thread1", lockA, lockB);
        DeadLockSample t2 = new DeadLockSample("Thread2", lockB, lockA);
        t1.start();
        t2.start();
        t1.join();
        t2.join();
    &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>DeadLockSampleV2</li>
</ul>
<pre><code class="copyable">package deadLock;

import java.lang.management.ManagementFactory;
import java.lang.management.ThreadInfo;
import java.lang.management.ThreadMXBean;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class DeadLockSampleV2 extends Thread &#123;
    private String first;
    private String second;

    public DeadLockSampleV2(String name, String first, String second) &#123;
        super(name);
        this.first = first;
        this.second = second;
    &#125;

    public void run() &#123;

        synchronized (first) &#123;
            System.out.println(this.getName() + this.getId() + " obtained: " + first);
            try &#123;
                Thread.sleep(1000L);
                synchronized (second) &#123;
                    System.out.println(this.getName() + " obtained: " + second);
                &#125;
            &#125; catch (InterruptedException e) &#123;
                
            &#125;
        &#125;
    &#125;

    public static void main(String[] args) throws InterruptedException &#123;
        long pid = ProcessHandle.current().pid();
        System.out.println("pid:" + pid);
        ThreadMXBean mbean = ManagementFactory.getThreadMXBean();

        
        Runnable dlCheck = new Runnable() &#123;
            @Override
            public void run() &#123;
                long[] threadIds = mbean.findDeadlockedThreads();
                if (threadIds != null) &#123;
                    ThreadInfo[] threadInfos = mbean.getThreadInfo(threadIds);
                    System.out.println("Detected deadlock threads:");
                    for (ThreadInfo threadInfo : threadInfos) &#123;
                        System.out.println(threadInfo.getThreadName());
                    &#125;
                &#125;
            &#125;
        &#125;;

        
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
        scheduler.scheduleAtFixedRate(dlCheck, 5L, 10L, TimeUnit.SECONDS);

        
        String lockA = "lockA";
        String lockB = "lockB";
        DeadLockSampleV2 t1 = new DeadLockSampleV2("Thread1", lockA, lockB);
        DeadLockSampleV2 t2 = new DeadLockSampleV2("Thread2", lockB, lockA);
        t1.start();
        t2.start();
        t1.join();
        t2.join();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何预防死锁？</p>
<ul>
<li>尽量避免使用多个锁，并且只有需要时才持有锁</li>
<li>如果必须使用多个锁，尽量设计好锁的获取顺序
<ul>
<li>辅助手法
<ul>
<li>使用图的方式表达</li>
<li>对象之间组合、调用的关系对比和组合，考虑可能调用时序。</li>
<li>按照可能时序合并，发现可能死锁的场景。</li>
</ul>
</li>
</ul>
</li>
<li>使用带超时的方法</li>
</ul>
<pre><code class="copyable">if (lock.tryLock() || lock.tryLock(timeout, unit)) &#123;
    
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过静态代码分析</li>
</ul>
<h2 data-id="heading-1">并发工具</h2>
<h3 data-id="heading-2">Semaphore</h3>
<pre><code class="copyable">package conCurrentTool;

import java.util.concurrent.Semaphore;

public class UsualSemaphoreSample &#123;
    public static void main(String[] args) throws InterruptedException &#123;
        System.out.println("Action...GO!");
        Semaphore semaphore = new Semaphore(5);
        for (int i = 0; i < 10; i++) &#123;
            Thread t = new Thread(new SemaphoreWorker(semaphore));
            t.start();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">AbnormalSemaphore</h3>
<pre><code class="copyable">package conCurrentTool;

import java.util.concurrent.Semaphore;

public class AbnormalSemaphoreSample &#123;
    public static void main(String[] args) throws InterruptedException &#123;
        Semaphore semaphore = new Semaphore(0);
        for (int i = 0; i < 10; i++) &#123;
            Thread t = new Thread(new MyWorker(semaphore));
            t.start();
        &#125;
        System.out.println("Action...GO!");
        semaphore.release(5);
        System.out.println("Wait for permits off");
        while (semaphore.availablePermits() != 0) &#123;
            Thread.sleep(100L);
        &#125;
        System.out.println("Action...GO again!");
        semaphore.release(5);
    &#125;
&#125;

class MyWorker implements Runnable &#123;
    private Semaphore semaphore;

    public MyWorker(Semaphore semaphore) &#123;
        this.semaphore = semaphore;
    &#125;

    @Override
    public void run() &#123;
        try &#123;
            semaphore.acquire();
            System.out.println("Executed!");
        &#125; catch (InterruptedException e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">SemaphoreWorker</h3>
<pre><code class="copyable">package conCurrentTool;

import java.util.concurrent.Semaphore;

public class SemaphoreWorker  implements Runnable&#123;
    private String name;
    private Semaphore semaphore;

    public SemaphoreWorker(Semaphore semaphore) &#123;
        this.semaphore = semaphore;
    &#125;

    @Override
    public void run() &#123;
        try &#123;
            log("is waiting for a permit!");
            semaphore.acquire();
            log("acquired a permit!");
            log("executed!");
        &#125; catch (InterruptedException e) &#123;
            e.printStackTrace();
        &#125; finally &#123;
            log("released a permit!");
            semaphore.release();
        &#125;
    &#125;

    private void log(String msg) &#123;
        if (name == null) &#123;
            name = Thread.currentThread().getName();
        &#125;
        System.out.println(name + " " + msg);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">LatchSample</h3>
<pre><code class="copyable">package conCurrentTool;


import java.util.concurrent.CountDownLatch;
public class LatchSample &#123;
    public static void main(String[] args) throws InterruptedException &#123;
        CountDownLatch latch = new CountDownLatch(6);
        for (int i = 0; i < 5; i++) &#123;
            Thread t = new Thread(new FirstBatchWorker(latch));
            t.start();
        &#125;
        for (int i = 0; i < 5; i++) &#123;
            Thread t = new Thread(new SecondBatchWorker(latch));
            t.start();
        &#125;
        
        while ( latch.getCount() != 1 )&#123;
            Thread.sleep(100L);
        &#125;
        System.out.println("Wait for first batch finish");
        latch.countDown();
    &#125;
&#125;
class FirstBatchWorker implements Runnable &#123;
    private CountDownLatch latch;
    public FirstBatchWorker(CountDownLatch latch) &#123;
        this.latch = latch;
    &#125;
    @Override
    public void run() &#123;
        System.out.println("First batch executed!");
        latch.countDown();
    &#125;
&#125;
class SecondBatchWorker implements Runnable &#123;
    private CountDownLatch latch;
    public SecondBatchWorker(CountDownLatch latch) &#123;
        this.latch = latch;
    &#125;
    @Override
    public void run() &#123;
        try &#123;
            latch.await();
            System.out.println("Second batch executed!");
        &#125; catch (InterruptedException e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">队列</h2>
<pre><code class="copyable">package queue;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class LinkedBlockingQueue &#123;

    
    private final ReentrantLock takeLock = new ReentrantLock();

    
    private final Condition notEmpty = takeLock.newCondition();

    
    private final ReentrantLock putLock = new ReentrantLock();

    
    private final Condition notFull = putLock.newCondition();

    public static void main(String[] args) &#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">队列使用场景与典型用例</h3>
<pre><code class="copyable">package queue;


import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class ConsumerProducer &#123;
    public static final String EXIT_MSG  = "Good bye!";
    public static void main(String[] args) &#123;

        BlockingQueue<String> queue = new ArrayBlockingQueue<>(3);
        Producer producer = new Producer(queue);
        Consumer consumer = new Consumer(queue);
        new Thread(producer).start();
        new Thread(consumer).start();
    &#125;


    static class Producer implements Runnable &#123;
        private BlockingQueue<String> queue;
        public Producer(BlockingQueue<String> q) &#123;
            this.queue = q;
        &#125;

        @Override
        public void run() &#123;
            for (int i = 0; i < 20; i++) &#123;
                try&#123;
                    Thread.sleep(5L);
                    String msg = "Message" + i;
                    System.out.println("Produced new item: " + msg);
                    queue.put(msg);
                &#125; catch (InterruptedException e) &#123;
                    e.printStackTrace();
                &#125;
            &#125;

            try &#123;
                System.out.println("Time to say good bye!");
                queue.put(EXIT_MSG);
            &#125; catch (InterruptedException e) &#123;
                e.printStackTrace();
            &#125;
        &#125;
    &#125;

    static class Consumer implements Runnable&#123;
        private BlockingQueue<String> queue;
        public Consumer(BlockingQueue<String> q)&#123;
            this.queue=q;
        &#125;

        @Override
        public void run() &#123;
            try&#123;
                String msg;
                while(!EXIT_MSG.equalsIgnoreCase( (msg = queue.take())))&#123;
                    System.out.println("Consumed item: " + msg);
                    Thread.sleep(10L);
                &#125;
                System.out.println("Got exit message, bye!");
            &#125;catch(InterruptedException e) &#123;
                e.printStackTrace();
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8"><code>Java</code> 并发类库提供的线程池</h2>
<ul>
<li>
<p><code>newCachedThreadPool</code></p>
<ul>
<li>处理大量短时间工作任务的线程池</li>
</ul>
</li>
<li>
<p><code>newFixedThreadPool</code></p>
<ul>
<li>其背后使用的是无界的工作队列，任何时候最多有 <code>nThreads</code> 个工作线程是活动的</li>
</ul>
</li>
<li>
<p><code>newSingleThreadExecutor</code></p>
<ul>
<li>它的特点在于工作线程数目被限制为 1</li>
</ul>
</li>
<li>
<p><code>newSingleThreadScheduledExecutor</code></p>
<ul>
<li>进行定时或周期性的工作调度，区别在于单一工作线程还是多个工作线程</li>
</ul>
</li>
<li>
<p><code>newWorkStealingPool</code></p>
<ul>
<li>并行地处理任务，不保证处理顺序。</li>
</ul>
<h2 data-id="heading-9">线程池的几个基本组成部分</h2>
</li>
<li>
<p><code>corePoolSize</code>，所谓的核心线程数，可以大致理解为长期驻留的线程数目（除非设置了 allowCoreThreadTimeOut）</p>
</li>
<li>
<p><code>maximumPoolSize</code>，顾名思义，就是线程不够时能够创建的最大线程数</p>
</li>
<li>
<p><code>keepAliveTime</code> 和 <code>TimeUnit</code>，这两个参数指定了额外的线程能够闲置多久，显然有些线程池不需要它。</p>
</li>
<li>
<p><code>workQueue</code>，工作队列，必须是 <code>BlockingQueue</code></p>
</li>
</ul>
<p>构造函数的配置：</p>
<pre><code class="copyable">public ThreadPoolExecutor(int corePoolSize,
                        int maximumPoolSize,
                        long keepAliveTime,
                        TimeUnit unit,
                        BlockingQueue<Runnable> workQueue,
                        ThreadFactory threadFactory,
                        RejectedExecutionHandler handler)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>状态如何表征：</p>
<pre><code class="copyable">
private final AtomicInteger ctl = new AtomicInteger(ctlOf(RUNNING, 0));

private static final int COUNT_BITS = Integer.SIZE - 3;
private static final int COUNT_MASK = (1 << COUNT_BITS) - 1;

private static final int RUNNING = -1 << COUNT_BITS;
…

private static int runStateOf(int c)  &#123; return c & ~COUNT_MASK; &#125;
private static int workerCountOf(int c)  &#123; return c & COUNT_MASK; &#125;
private static int ctlOf(int rs, int wc) &#123; return rs | wc; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整代码请见 <code>ExecuteMethod.java</code> ,仅供参考</p>
<h2 data-id="heading-10">实践</h2>
<ul>
<li>避免任务堆积
<ul>
<li>排查工具 ： <code>jmap</code></li>
</ul>
</li>
<li>避免过度扩展线程
<ul>
<li>在处理大量短时任务时，使用缓存的线程池</li>
</ul>
</li>
<li>线程泄漏
<ul>
<li>任务逻辑有问题，导致工作线程迟迟不能被释放。</li>
</ul>
</li>
<li>避免死锁等同步问题</li>
<li>尽量避免在使用线程池时操作 <code>ThreadLocal</code></li>
</ul>
<h2 data-id="heading-11">线程池大小选择</h2>
<ul>
<li>通常建议按照 <code>CPU</code> 核的数目 <code>N</code> 或者 <code>N+1</code>。</li>
<li>较多等待的任务
<ul>
<li><code>Brain Goetz</code> 推荐的计算方法：
<ul>
<li>根据采样或者概要分析等方式进行计算，然后在实际中验证和调整。```
线程数 = CPU核数 × 目标CPU利用率 ×（1 + 平均等待时间/平均工作时间）
<pre><code class="copyable"><span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
</li>
<li>实际还可能受各种系统资源限制影响</li>
<li>很多时候架构上的改变更能解决问题</li>
</ul>
<h2 data-id="heading-12"><code>AtomicInteger</code> 底层实现原理</h2>
<h3 data-id="heading-13">CAS</h3>
<p>表征的是一些列操作的集合，获取当前数值，进行一些运算，利用 <code>CAS</code> 指令试图进行更新 否则，可能出现不同的选择，要么进行重试，要么就返回一个成功或者失败的结果。</p>
<h3 data-id="heading-14">场景</h3>
<p>如何在数据库抽象层面实现，只有一个线程能够排他性地修改一个索引分区？</p>
<ol>
<li>可以考虑为索引分区对象添加一个逻辑上的锁：</li>
</ol>
<pre><code class="copyable">public class AtomicBTreePartition &#123;
private volatile long lock;
public void acquireLock()&#123;&#125;
public void releaseeLock()&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code>JAVA</code> 提供的公共 <code>API</code></li>
</ol>
<ul>
<li>AtomicLongFieldUpdater</li>
</ul>
<pre><code class="copyable">private static final AtomicLongFieldUpdater<AtomicBTreePartition> lockFieldUpdater =
        AtomicLongFieldUpdater.newUpdater(AtomicBTreePartition.class, "lock");

private void acquireLock()&#123;
    long t = Thread.currentThread().getId();
    while (!lockFieldUpdater.compareAndSet(this, 0L, t))&#123;
        
         …
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Variable Handle API</li>
</ul>
<pre><code class="copyable">private static final VarHandle HANDLE = MethodHandles.lookup().findStaticVarHandle
        (AtomicBTreePartition.class, "lock");

private void acquireLock()&#123;
    long t = Thread.currentThread().getId();
    while (!HANDLE.compareAndSet(this, 0L, t))&#123;
        
        …
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">理解 <code>AQS</code> 的原理与应用</h2>
<ul>
<li>
<p>原理 一种同步结构往往是可以利用其他的结构实现的</p>
<ul>
<li>可以使用 Semaphore 实现互斥锁</li>
<li>对某种同步结构的倾向，会导致复杂、晦涩的实现逻辑</li>
<li><code>Doug Lea</code> 将基础的同步相关操作抽象在 <code>AbstractQueuedSynchronizer</code> 中</li>
</ul>
</li>
<li>
<p><code>AQS</code> 内部数据和方法</p>
<ul>
<li>一个 <code>volatile</code> 的整数成员表征状态</li>
<li><code>FIFO</code> 等待线程队列</li>
<li>基于 <code>CAS</code> 的基础操作方法</li>
<li>两个基本类型的方法
<ul>
<li><code>acquire</code> 操作，获取资源的独占权</li>
<li><code>release</code> 操作，释放对某个资源的独占</li>
</ul>
</li>
</ul>
</li>
<li>
<p>示例</p>
<ul>
<li><code>ReentrantLock</code></li>
</ul>
<pre><code class="copyable">package conCurrentTool;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>/**</p>
<ul>
<li>@javaVersion 14</li>
<li>public final void acquire(int arg) &#123;</li>
<li>
<pre><code class="copyable">    if (!tryAcquire(arg))
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">        acquire(null, arg, false, false, false, 0L);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>/</li>
</ul>
<p>import java.util.concurrent.locks.AbstractQueuedSynchronizer;</p>
<p>public class ReentrantLockCase1 &#123; private final Sync sync;</p>
<pre><code class="copyable">public ReentrantLockCase1(Sync sync) &#123;
    this.sync = sync;
&#125;

public void lock() &#123;
    sync.acquire(1);
&#125;
public void unlock() &#123;
    sync.release(1);
&#125;


abstract static class Sync extends AbstractQueuedSynchronizer &#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">`ReentrantLock` 中的 `tryAcquire` 实现：

- `NonfairSync` 和 `FairSync`

 `AQS` 内部 `tryAcquire` 仅仅是个接近未实现的方法（直接抛异常）
 
 ```java
 protected boolean tryAcquire(int arg) &#123;
        throw new UnsupportedOperationException();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>公平性在 <code>ReentrantLock</code> 构建时:</p>
<pre><code class="copyable">
public ReentrantLock() &#123;
        sync = new NonfairSync(); 
    &#125;
    public ReentrantLock(boolean fair) &#123;
        sync = fair ? new FairSync() : new NonfairSync();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>里体现了非公平的语义:</p>
<pre><code class="copyable">
final boolean nonfairTryAcquire(int acquires) &#123;
    final Thread current = Thread.currentThread();
    int c = getState();
    if (c == 0) &#123; 
      if (compareAndSetState(0, acquires)) &#123;
          setExclusiveOwnerThread(current);  
          return true;
      &#125;
    &#125; else if (current == getExclusiveOwnerThread()) &#123; 
      int nextc = c + acquires;
      if (nextc < 0) 
          throw new Error("Maximum lock count exceeded");
      setState(nextc);
      return true;
  &#125;
  return false;
&#125;   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前线程会被包装成为一个排他模式的节点（<code>EXCLUSIVE</code>），通过 <code>addWaiter</code> 方法添加到队列中。</p>
<pre><code class="copyable">final boolean acquireQueued(final Node node, int arg) &#123;
      boolean interrupted = false;
      try &#123;
      for (;;) &#123;
          final Node p = node.predecessor();
          if (p == head && tryAcquire(arg)) &#123; 
              setHead(node); 
              p.next = null; 
              return interrupted;
          &#125;
          if (shouldParkAfterFailedAcquire(p, node)) 
              interrupted |= parkAndCheckInterrupt();
      &#125;
       &#125; catch (Throwable t) &#123;
      cancelAcquire(node);
      if (interrupted)
              selfInterrupt();
      throw t;
      &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            