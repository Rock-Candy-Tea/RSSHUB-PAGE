
---
title: 'Semaphore 信号量源码分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a51c42485b549158c60f226a6720dba~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 08:29:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a51c42485b549158c60f226a6720dba~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">概述</h1>
<p>Semaphore 信号量， 信号量维护了一组许可。如果有必要每个采集模块都回阻塞，直到有许可可用。然后获取许可证。每次发布都会添加一个许可证，可能会释放一个阻塞资源。但是，没有使用实际的许可对象；信号量可用数量的计数，并且进行操作。
信号量通常可以用于限制访问某些（物理或者逻辑）资源的线程数。例如下面是一个使用信号量控制对线程池访问。</p>
<pre><code class="hljs language-java copyable" lang="java"> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Pool</span> </span>&#123;
   <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> MAX_AVAILABLE = <span class="hljs-number">100</span>;
   <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Semaphore available = <span class="hljs-keyword">new</span> Semaphore(MAX_AVAILABLE, <span class="hljs-keyword">true</span>);

   <span class="hljs-function"><span class="hljs-keyword">public</span> Object <span class="hljs-title">getItem</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> InterruptedException </span>&#123;
     available.acquire();
     <span class="hljs-keyword">return</span> getNextAvailableItem();
   &#125;

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">putItem</span><span class="hljs-params">(Object x)</span> </span>&#123;
     <span class="hljs-keyword">if</span> (markAsUnused(x))
       available.release();
   &#125;

   <span class="hljs-comment">// Not a particularly efficient data structure; just for demo</span>

   <span class="hljs-keyword">protected</span> Object[] items = ... whatever kinds of items being managed
   <span class="hljs-keyword">protected</span> <span class="hljs-keyword">boolean</span>[] used = <span class="hljs-keyword">new</span> <span class="hljs-keyword">boolean</span>[MAX_AVAILABLE];

   <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">synchronized</span> Object <span class="hljs-title">getNextAvailableItem</span><span class="hljs-params">()</span> </span>&#123;
     <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < MAX_AVAILABLE; ++i) &#123;
       <span class="hljs-keyword">if</span> (!used[i]) &#123;
          used[i] = <span class="hljs-keyword">true</span>;
          <span class="hljs-keyword">return</span> items[i];
       &#125;
     &#125;
     <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>; <span class="hljs-comment">// not reached</span>
   &#125;

   <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">synchronized</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">markAsUnused</span><span class="hljs-params">(Object item)</span> </span>&#123;
     <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < MAX_AVAILABLE; ++i) &#123;
       <span class="hljs-keyword">if</span> (item == items[i]) &#123;
          <span class="hljs-keyword">if</span> (used[i]) &#123;
            used[i] = <span class="hljs-keyword">false</span>;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
          &#125; <span class="hljs-keyword">else</span>
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
       &#125;
     &#125;
     <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
   &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在获取项目之前，每个线程必须从信号量获取一个许可证，以确保项目可用。当线程处理完该项后，它将返回到池中，并向信号量返回一个许可证，允许另一个线程获取该项。请注意，在调用acquire时不会保持同步锁，因为这会阻止项目返回池。信号量封装了限制对池的访问所需的同步，与维护池本身一致性所需的任何同步分开。
​</p>
<p>初始化为1的信号量，其使用方式是最多只有一个可用的许可证，可以用作互斥锁。这通常被称为二进制信号量，因为它只有两个状态：一个许可证可用，或者零个许可证可用。以这种方式使用时，二进制信号量的属性（与许多java.util.concurrent.locks.Lock实现不同）是“锁”可以由所有者以外的线程释放（因为信号量没有所有权的概念）。这在某些特定的上下文中非常有用，例如死锁恢复。
​</p>
<p>此类的构造函数可以选择接受公平性参数。当设置为false时，此类不保证线程获取许可的顺序。特别是，允许bargging，也就是说，调用acquire的线程可以在一直在等待的线程之前分配一个许可证-从逻辑上讲，新线程将自己置于等待线程队列的头部。当公平性设置为true时，信号量保证选择调用任何acquire方法的线程，以按照其调用这些方法的处理顺序（先进先出；先进先出）。请注意，FIFO排序必然适用于这些方法中的特定内部执行点。因此，一个线程可以在另一个线程之前调用acquire，但在另一个线程之后到达排序点，类似地，从方法返回时也是如此。还请注意，untimed tryAcquire方法不支持公平性设置，但将接受任何可用的许可。
​</p>
<p>通常，用于控制资源访问的信号量应该初始化为公平，以确保没有线程因访问资源而耗尽。当将信号量用于其他类型的同步控制时，非公平排序的吞吐量优势往往超过公平性考虑。
​</p>
<p>此类还提供了方便的方法，可以一次获取和发布多个许可证。当使用这些方法时，如果没有将公平设置为真，则要小心无限期延迟的风险增加。
​</p>
<p>内存一致性影响：在调用“release”方法（如release（））之前的线程中的操作发生在另一个线程中成功的“acquire”方法（如acquire（）之后的操作）之前。</p>
<h1 data-id="heading-1">原理分析</h1>
<p>Semaphore 信号量，是控制并发的有效手段。它底层通过 AQS 实现。入下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a51c42485b549158c60f226a6720dba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">构造方法</h2>
<p>Semaphore 构造方法有两个 <code>Semaphore(int permits)</code> 和 <code>Semaphore(int permits, boolean fair)</code> 后者有两个参数：第一个参数是许可数量初始化，第二个参数定义信号量是否公平锁同步（默认为非公平）。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Semaphore</span><span class="hljs-params">(<span class="hljs-keyword">int</span> permits)</span> </span>&#123;
    sync = <span class="hljs-keyword">new</span> NonfairSync(permits);
&#125;


<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Semaphore</span><span class="hljs-params">(<span class="hljs-keyword">int</span> permits, <span class="hljs-keyword">boolean</span> fair)</span> </span>&#123;
    sync = fair ? <span class="hljs-keyword">new</span> FairSync(permits) : <span class="hljs-keyword">new</span> NonfairSync(permits);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">acquire 方法</h2>
<p>acquire 方法可以为理解获取许可，如果存在剩余许可那么就可以进入后续代码块，如果没有获取线程进入阻塞。
在共享模式下获取，如果中断将中止。通过首先检查中断状态，然后调用至少一次tryAcquireShared，并在成功时返回来实现。否则线程将排队，可能会重复阻塞和取消阻塞，调用tryAcquireShared，直到成功或线程中断。</p>
<h2 data-id="heading-4">release 方法</h2>
<p>acquire 方法可以为理解释放许可，其他等待许可的线程进入资源竞争阶段。然后去查找等待队列队头有效的等待节点进行唤醒。</p>
<h2 data-id="heading-5">整体流程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccc01f0db56a4027bc3ebfbfeca86855~tplv-k3u1fbpfcp-watermark.image" alt="Semaphore 信号量原理.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">举个例子</h1>
<h2 data-id="heading-7">场景描述</h2>
<p>对于控制流量，或者控制并发我们可以使用  Semaphore 信号量来完成。
例子：
有100 个人需要过桥，但是桥上最多同时能够承受 5 个人的重量。如果我们需要有序的过桥那么就可以采用信号量的方式来控制。</p>
<ol>
<li>初始化 5 个许可。</li>
<li>上桥之前先去获取 许可，如果有剩余许可就上桥。</li>
<li>如果没有 许可，就等待许可。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/084043bdd98e4a948a6fc414e7a29dc9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">模拟代码</h2>
<ol>
<li>首先定义桥对象，入下所示：</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bridge</span> </span>&#123;

    <span class="hljs-keyword">private</span> String name;

    <span class="hljs-keyword">private</span> String address;

    <span class="hljs-keyword">private</span> Integer max;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getName</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> name;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setName</span><span class="hljs-params">(String name)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.name = name;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getAddress</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> address;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setAddress</span><span class="hljs-params">(String address)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.address = address;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> Integer <span class="hljs-title">getMax</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> max;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setMax</span><span class="hljs-params">(Integer max)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.max = max;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>然后定义迁徙者对象，就是过桥的人，然后他有个动作就是过桥。代码如下所示。</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Migrator</span> </span>&#123;

    <span class="hljs-keyword">private</span> String name;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">gapBridge</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"Migrator: "</span> + <span class="hljs-keyword">this</span>.name + <span class="hljs-string">", time:"</span> + System.currentTimeMillis());
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getName</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> name;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setName</span><span class="hljs-params">(String name)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.name = name;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>调用代码如下：</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MainTest</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        Bridge bridge = <span class="hljs-keyword">new</span> Bridge();
        bridge.setAddress(<span class="hljs-string">"云南"</span>);
        bridge.setName(<span class="hljs-string">"XX 桥"</span>);
        bridge.setMax(<span class="hljs-number">5</span>);

        Semaphore semaphore = <span class="hljs-keyword">new</span> Semaphore(bridge.getMax());
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i=<span class="hljs-number">0</span>; i< <span class="hljs-number">100</span>; i++) &#123;
            <span class="hljs-keyword">int</span> idx = i;
            <span class="hljs-keyword">new</span> Thread(()-> &#123;
                <span class="hljs-keyword">try</span> &#123;
                    Migrator migrator = <span class="hljs-keyword">new</span> Migrator();
                    migrator.setName(<span class="hljs-string">"name-"</span> + idx);
                    semaphore.acquire();
                    TimeUnit.SECONDS.sleep(<span class="hljs-number">1</span>);
                    migrator.gapBridge();
                    System.out.println(<span class="hljs-string">"name "</span> + migrator.getName() + <span class="hljs-string">" 通过"</span>);
                &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
                    e.printStackTrace();
                &#125; <span class="hljs-keyword">finally</span> &#123;
                    semaphore.release();
                &#125;
            &#125;).start();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>输出日志如下：我们可以看到刚开始的时候有 5 个线程获取到 "许可" 几乎同时过桥，后面逐渐就是释放一个许可，另外一个线程继续执行。</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java">Migrator: name-<span class="hljs-number">7</span>, time:<span class="hljs-number">1630495912011</span>
name name-<span class="hljs-number">7</span> 通过
Migrator: name-<span class="hljs-number">2</span>, time:<span class="hljs-number">1630495912011</span>
name name-<span class="hljs-number">2</span> 通过
Migrator: name-<span class="hljs-number">4</span>, time:<span class="hljs-number">1630495912011</span>
Migrator: name-<span class="hljs-number">8</span>, time:<span class="hljs-number">1630495912011</span>
Migrator: name-<span class="hljs-number">3</span>, time:<span class="hljs-number">1630495912011</span>
name name-<span class="hljs-number">3</span> 通过
name name-<span class="hljs-number">8</span> 通过
name name-<span class="hljs-number">4</span> 通过
Migrator: name-<span class="hljs-number">5</span>, time:<span class="hljs-number">1630495913012</span>
name name-<span class="hljs-number">5</span> 通过
Migrator: name-<span class="hljs-number">0</span>, time:<span class="hljs-number">1630495913012</span>
name name-<span class="hljs-number">0</span> 通过
Migrator: name-<span class="hljs-number">6</span>, time:<span class="hljs-number">1630495913013</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">参考文档</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fleesf456%2Fp%2F5414778.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/leesf456/p/5414778.html" ref="nofollow noopener noreferrer">www.cnblogs.com/leesf456/p/…</a></li>
</ul></div>  
</div>
            