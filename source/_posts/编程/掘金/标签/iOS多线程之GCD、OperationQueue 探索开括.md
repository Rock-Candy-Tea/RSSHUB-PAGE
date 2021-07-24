
---
title: 'iOS多线程之GCD、OperationQueue 探索开括'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfb614a2d02d48e3aa42b8dc041ab219~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 00:58:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfb614a2d02d48e3aa42b8dc041ab219~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfb614a2d02d48e3aa42b8dc041ab219~tplv-k3u1fbpfcp-watermark.image" alt="多线程分享3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">简介</h1>
<blockquote>
<p>iOS 提供了一些技术，允许您异步执行任何任务，而无需自己管理线程。异步启动任务的技术之一是 Grand Central Dispatch (GCD)。
这种技术采用线程管理代码，并将该代码移动到系统级别。
您所要做的就是定义要执行的任务，并将它们添加到适当的分派队列中。
GCD 负责创建所需的线程，并安排任务在这些线程上运行。由于线程管理现在是系统的一部分，GCD 提供了任务管理>和执行的整体方法，比传统线程提供了更高的效率。</p>
<p>OperationQueue（操作队列，api 类名为 NSOperationQueue ）是 Objective-C 对象，是对 GCD 的封装。其作用非常类似于分派队列。
您定义要执行的任务，然后将它们添加到 OperationQueue 中， OperationQueue 处理这些任务的调度和执行。
与 GCD 一样， OperationQueue 为您处理所有线程管理，确保在系统上尽可能快速有效地执行任务。</p>
</blockquote>
<p>收录：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.cocoachina.com%2Farticles%2F900673%3Ffilter%3Dios" target="_blank" rel="nofollow noopener noreferrer" title="http://www.cocoachina.com/articles/900673?filter=ios" ref="nofollow noopener noreferrer">www.cocoachina.com/articles/90…</a></p>
<h1 data-id="heading-1">GCD、OperationQueue 对比</h1>
<h2 data-id="heading-2">核心理念</h2>
<ul>
<li>GCD的核心概念：
<ul>
<li>将 任务(block) 添加到队列，并且指定执行任务的函数。</li>
</ul>
</li>
<li>NSOperation 的核心概念：
<ul>
<li>把 操作(异步) 添加到 队列。</li>
</ul>
</li>
</ul>
<h2 data-id="heading-3">区别</h2>
<ul>
<li>
<p>GCD：</p>
<ul>
<li>将任务（block）添加到队列(串行/并发/主队列)，并且指定任务执行的函数(同步/异步)</li>
<li>GCD是底层的C语言构成的API</li>
<li>iOS 4.0 推出的，针对多核处理器的并发技术</li>
<li>在队列中执行的是由 block 构成的任务，这是一个轻量级的数据结构</li>
<li>要停止已经加入 queue 的 block 需要写复杂的代码</li>
<li>需要通过 Barrier（dispatch_barrier_async）或者同步任务设置任务之间的依赖关系</li>
<li>只能设置队列的优先级</li>
<li><strong>高级功能：</strong>
<ul>
<li>dispatch_once_t（一次性执行, 多线程安全）；</li>
<li>dispatch_after（延迟）； dispatch_group（调度组）； dispatch_semaphore（信号量）；</li>
</ul>
<pre><code class="copyable">-   dispatch_apply（优化顺序不敏感大体量for循环）；
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>OperationQueue：</p>
<ul>
<li>
<p>OC 框架，更加面向对象，是对 GCD 的封装。</p>
</li>
<li>
<p>iOS 2.0 推出的，苹果推出 GCD 之后，对 NSOperation 的底层进行了全部重写。</p>
</li>
<li>
<p>可以设置队列中每一个操作的 QOS（） 队列的整体 QOS</p>
</li>
<li>
<p><strong>操作相关 Operation作为一个对象，为我们提供了更多的选择：</strong></p>
<ul>
<li>任务依赖（addDependency），可以跨队列设置操作的依赖关系；</li>
<li>在队列中的优先级（queuePriority） 服务质量（qualityOfService, iOS8+）;</li>
<li>完成回调（void (^completionBlock)(void）</li>
</ul>
</li>
<li>
<p>队列相关 服务质量（qualityOfService, iOS8+）;</p>
</li>
<li>
<p>最大并发操作数（maxConcurrentOperationCount），GCD 不易实现; 暂停/继续（suspended）；</p>
</li>
<li>
<p>取消所有操作（cancelAllOperations）；</p>
</li>
<li>
<p>KVO 监听队列任务执行进度（progress, iOS13+）；</p>
</li>
</ul>
</li>
</ul>
<p> </p>
<h1 data-id="heading-4">GCD</h1>
<p>从GCD常见面试题到底层源码分析，带你深入了解不一样的GCD
1、GCD常见面试题分析
2、GCD的注意事项（死锁）
3、GCD的底层原理（队列分析）</p>
<h3 data-id="heading-5">观看点击▼</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1QX4y1K76c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1QX4y1K76c" ref="nofollow noopener noreferrer">iOS多线程-『GCD』</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb03010f779c4273877bb45d9565853a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">队列</h2>
<h3 data-id="heading-7">串行队列（Serial Queues）</h3>
<blockquote>
<p>串行队列中的任务按顺序执行；
但是不同串行队列间没有任何约束；
多个串行队列同时执行时，不同队列中任务执行是并发的效果。</p>
</blockquote>
<p><strong>比如：火车站买票可以有多个卖票口，但是每个排的队都是串行队列，整体并发，单线串行。</strong></p>
<p><code>注意防坑：串行队列创建的位置。</code></p>
<p><strong>比如下面代码示例中：</strong></p>
<ul>
<li>在for循环内部创建时，每个循环都是创建一个新的串行队列，里面只装一个任务，多个串行队列，结果整体上是并发的效果。</li>
</ul>
<p>想要串行效果，必须在for循环外部创建串行队列。</p>
<p><strong>串行队列适合管理共享资源。保证了顺序访问，杜绝了资源竞争。</strong></p>
<p>代码示例:</p>
<pre><code class="copyable">    private func serialExcuteByGCD()&#123;
        let lArr : [UIImageView] = [imageView1, imageView2, imageView3, imageView4]

        //串行队列，异步执行时，只开一个子线程
        let serialQ = DispatchQueue.init(label: "com.companyName.serial.downImage")

        for i in 0..<lArr.count&#123;
            let lImgV = lArr[i]

            //清空旧图片
            lImgV.image = nil

         //注意，防坑：串行队列创建的位置,在这创建时，每个循环都是一个新的串行队列，里面只装一个任务，多个串行队列，整体上是并行的效果。
            //            let serialQ = DispatchQueue.init(label: "com.companyName.serial.downImage")

            serialQ.async &#123;

                print("第\(i)个 开始，%@",Thread.current)
                Downloader.downloadImageWithURLStr(urlStr: imageURLs[i]) &#123; (img) in
                    let lImgV = lArr[i]

                    print("第\(i)个 结束")
                    DispatchQueue.main.async &#123;
                        print("第\(i)个 切到主线程更新图片")
                        lImgV.image = img
                    &#125;
                    if nil == img&#123;
                        print("第\(i+1)个img is nil")
                    &#125;
                &#125;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">并发队列（Concurrent Queues）</h3>
<p>并发队列依旧保证中任务按加入的先后顺序开始（FIFO），但是无法知道执行顺序，执行时长和某一时刻的任务数。按 FIFO 开始后，他们之间不会相互等待。</p>
<p>比如：提交了 #1，#2，#3 任务到并发队列，开始的顺序是 #1，#2，#3。#2 和 #3 虽然开始的比 #1 晚，但是可能比 #1 执行结束的还要早。任务的执行是由系统决定的，所以执行时长和结束时间都无法确定。</p>
<p>需要用到并发队列时，<strong>强烈建议</strong> 使用系统自带的四种全局队列之一。但是，当你需要使用 barrier 对队列中任务进行栅栏时，只能使用自定义并发队列。</p>
<p>对比：barrier 和锁的区别</p>
<ul>
<li>依赖对象不同，barrier 依赖的对象是自定义并发队列，锁操作依赖的对象是线程。</li>
<li>作用不同，barrier 起到自定义并发队列中栅栏的作用；锁起到多线程操作时防止资源竞争的作用。</li>
</ul>
<p>代码示例:</p>
<pre><code class="copyable">private func concurrentExcuteByGCD()&#123;
        let lArr : [UIImageView] = [imageView1, imageView2, imageView3, imageView4]

        for i in 0..<lArr.count&#123;
            let lImgV = lArr[i]

            //清空旧图片
            lImgV.image = nil

            //并行队列:图片下载任务按顺序开始，但是是并行执行，不会相互等待，任务结束和图片显示顺序是无序的，多个子线程同时执行，性能更佳。
            let lConQ = DispatchQueue.init(label: "cusQueue", qos: .background, attributes: .concurrent)
            lConQ.async &#123;
                print("第\(i)个开始，%@", Thread.current)
                Downloader.downloadImageWithURLStr(urlStr: imageURLs[i]) &#123; (img) in
                    let lImgV = lArr[i]
                      print("第\(i)个结束")
                    DispatchQueue.main.async &#123;
                        lImgV.image = img
                    &#125;
                    if nil == img&#123;
                        print("第\(i+1)个img is nil")
                    &#125;
                &#125;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">串行、并发队列对比图</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ef55e8b56484c5f960d297bf6455be1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">注意事项</h3>
<ul>
<li>无论串行还是并发队列，都是 FIFO ；</li>
</ul>
<p>一般创建 任务（blocks）和加任务到队列是在主线程，但是任务执行一般是在其他线程（asyc）。
需要刷新 UI 时，如果当前不再主线程，需要切回主线程执行。
当不确定当前线程是否在主线程时，可以使用下面代码：</p>
<pre><code class="copyable">/**
Submits a block for asynchronous execution on a main queue and returns immediately.
*/
static inline void dispatch_async_on_main_queue(void (^block)()) &#123;
if (NSThread.isMainThread) &#123;
    block();
&#125; else &#123;
    dispatch_async(dispatch_get_main_queue(), block);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>主队列是串行队列，每个时间点只能有一个任务执行，因此如果耗时操作放到主队列，会导致界面卡顿。</p>
</li>
<li>
<p>系统提供一个串行主队列，4个 不同优先级的全局队列。 用 dispatch_get_global_queue 方法获取全局队列时，第一个参数有 4 种类型可选:</p>
<ul>
<li>DISPATCH_QUEUE_PRIORITY_HIGH</li>
<li>DISPATCH_QUEUE_PRIORITY_DEFAULT</li>
<li>DISPATCH_QUEUE_PRIORITY_LOW</li>
<li>DISPATCH_QUEUE_PRIORITY_BACKGROUND</li>
</ul>
</li>
<li>
<p>串行队列异步执行时，切到主线程刷 UI 也需要时间，切换完成之前，指令可能已经执行到下个循环了。但是看起来图片还是依次下载完成和显示的，因为每一张图切到主线程显示都需要时间。详见 demo 示例。</p>
</li>
<li>
<p>iOS8 之后，如果需要添加可被取消的任务，可以使用 DispatchWorkItem 类，此类有 cancel 方法。</p>
</li>
<li>
<p>应该避免创建大量的串行队列,如果希望并发执行大量任务，请将它们提交给全局并发队列之一。创建串行队列时，请尝试<strong>为每个队列确定一个用途</strong>，例如保护资源或同步应用程序的某些关键行为(如蓝牙检测结果需要有序处理的逻辑)。</p>
</li>
</ul>
<h2 data-id="heading-11">block（块）相关</h2>
<p>堆栈到底有什么区别？为什么面试中经常问到？</p>
<ul>
<li>堆的Block能捕获变量，栈的Block是否也行？</li>
<li>栈的Block堆上的使用有什么区别？</li>
<li>__weak真的能解决循环引用吗？</li>
<li>如何理解Block底层的结构体？</li>
</ul>
<h3 data-id="heading-12">观看点击▼</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1ii4y1L7vf" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1ii4y1L7vf" ref="nofollow noopener noreferrer">Block底层原理与LLDB Plugin</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6730ec7f86174184a736dadd92fc00a1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>调度队列复制添加到它们中的块，并在执行完成时释放块。  
虽然队列在执行小任务时比原始线程更有效，但是创建块并在队列上执行它们仍然存在开销。
如果一个块执行的工作量太少，那么内联执行它可能比将它分派到队列中要便宜得多。
判断一个块是否工作量太少的方法是使用性能工具为每个路径收集度量数据并进行比较。      
您可能希望将 block 的部分代码包含在 @autoreleasepool 中，以处理这些对象的内存管理。
尽管 GCD 调度队列拥有自己的自动释放池，但它们不能保证这些池何时耗尽。
如果您的应用程序是内存受限的，那么创建您自己的自动释放池可以让您以更有规律的间隔释放自动释放对象的内存。</p>
</blockquote>
<h2 data-id="heading-13">dispatch_after</h2>
<p>dispatch_after 函数并不是在指定时间之后才开始执行处理，而是在指定时间之后将任务追加到队列中。
这个时间并不是绝对准确的。</p>
<p>代码示例:</p>
<pre><code class="copyable">dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(2 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^&#123;
        NSLog(@"2s后执行");
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">dispatch_semaphore</h2>
<blockquote>
<p>在多线程访问可变变量时，是非线程安全的。</p>
</blockquote>
<p>可能导致程序崩溃。
此时，可以通过使用信号量（semaphore）技术，保证多线程处理某段代码时，后面线程等待前面线程执行，保证了多线程的安全性。
使用方法记两个就行了，一个是wait（dispatch_semaphore_wait），一个是signal（dispatch_semaphore_signal）。</p>
<h2 data-id="heading-15">dispatch_apply</h2>
<blockquote>
<p>当每次迭代中执行工作与其他所有迭代中执行的工作不同，且每个循环完成的顺序不重要时，可以用 dispatch_apply 函数替换循环。</p>
</blockquote>
<p><strong>注意：</strong> 替换后， dispatch_apply 函数整体上是同步执行，内部 block 的执行类型（串行/并发）由队列类型决定，但是串行队列易死锁，建议用并发队列。</p>
<p>原循环：</p>
<pre><code class="copyable">for (i = 0; i < count; i++) &#123;
   printf("%u\n",i);
&#125;
printf("done");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优化后：</p>
<pre><code class="copyable">dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);

 //count 是迭代的总次数。
dispatch_apply(count, queue, ^(size_t i) &#123;
   printf("%u\n",i);
&#125;);

//同样在上面循环结束后才调用。
printf("done");
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>您应该确保您的任务代码在每次迭代中完成合理数量的工作。</p>
</blockquote>
<p>与您分派到队列的任何块或函数一样，调度该代码以便执行会带来开销。
如果循环的每次迭代只执行少量的工作，那么调度代码的开销可能会超过将代码分派到队列可能带来的性能优势。
如果您在测试期间发现这一点是正确的，那么您可以使用步进来增加每个循环迭代期间执行的工作量。
通过大步前进，您可以将原始循环的多个迭代集中到一个块中，并按比例减少迭代次数。
例如，如果您最初执行了 100次 迭代，但决定使用步长为 4 的迭代，那么您现在从每个块执行 4 次循环迭代，迭代次数为 25次 。</p>
<h2 data-id="heading-16">自问自答</h2>
<ul>
<li>
<p>一个队列的不同任务可以在多个线程执行吗？</p>
<ul>
<li>串行队列，异步执行时，只开一个子线程；</li>
<li>无所谓多个线程执行；</li>
<li>并发队列，异步执行时，会自动开多个线程，可以在多个线程并发执行不同的任务。</li>
</ul>
</li>
<li>
<p>一个线程可以同时执行多个队列的任务吗？</p>
<ul>
<li>一个线程某个时间点只能执行一个任务，执行完毕后，可能执行到来自其他队列的任务（如果有的话）。</li>
</ul>
</li>
</ul>
<p><code>比如：主线程除了执行主队列中任务外，也可能会执行非主队列中的任务。</code></p>
<p>队列与线程关系示例图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/698295160b3a4be5bc119ef2f6c0ad79~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>qualityOfService 和 queuePriority 的区别是什么？
<ul>
<li>qualityOfService:      
<ul>
<li>用于表示 operation 在获取系统资源时的优先级，默认值：NSQualityOfServiceBackground，我们可以根据需要给 operation 赋不同的优化级，如最高优化级：NSQualityOfServiceUserInteractive。</li>
</ul>
</li>
<li>queuePriority:      
<ul>
<li>用于设置 operation 在 operationQueue 中的相对优化级，同一 queue 中优化级高的 operation(isReady 为 YES) 会被优先执行。    </li>
</ul>
</li>
</ul>
</li>
</ul>
<p> 需要注意区分 qualityOfService (在系统层面，operation 与其他线程获取资源的优先级) 与 queuePriority (同一 queue 中 operation 间执行的优化级)的区别。
同时，需要注意 dependencies (严格控制执行顺序)与 queuePriority (queue 内部相对优先级)的区别。</p>
<ul>
<li>添加依赖后，队列中网络请求任务有依赖关系时，任务结束判定以数据返回为准还是以发起请求为准？
<ul>
<li>以发起请求为准。</li>
</ul>
</li>
</ul>
<h1 data-id="heading-17">OperationQueue</h1>
<blockquote>
<p>NSOperation      NSOperation 是一个"抽象类"，不能直接使用。</p>
</blockquote>
<p>抽象类的用处是定义子类共有的属性和方法。
NSOperation 是基于 GCD 做的面向对象的封装。
相比较 GCD 使用更加简单，并且提供了一些用 GCD 不是很好实现的功能。
是苹果公司推荐使用的并发技术。</p>
<p>它有两个子类：</p>
<ul>
<li>NSInvocationOperation (调用操作)</li>
<li>NSBlockOperation (块操作)      一般常用NSBlockOperation，代码简单，同时由于闭包性使它没有传参问题。任务被封装在 NSOperation 的子类实例类对象里，一个 NSOperation 子类对象可以添加多个任务 block 和 一个执行完成 block ，当其关联的所有 block 执行完时，就认为操作结束了。</li>
<li>NSOperationQueue       OperationQueue也是对 GCD 的高级封装，更加面向对象，可以实现 GCD 不方便实现的一些效果。被添加到队列的操作默认是异步执行的。</li>
</ul>
<p>PS：常见的抽象类有：</p>
<ul>
<li>
<p>UIGestureRecognizer</p>
</li>
<li>
<p>CAAnimation</p>
</li>
<li>
<p>CAPropertyAnimation</p>
<h2 data-id="heading-18">可以实现 非FIFO 效果</h2>
</li>
</ul>
<p>通过对不同操作设置依赖,或优先级，可实现 非FIFO 效果。</p>
<p>代码示例:</p>
<pre><code class="copyable">func testDepedence()&#123;
        let op0 = BlockOperation.init &#123;
            print("op0")
        &#125;

        let op1 = BlockOperation.init &#123;
            print("op1")
        &#125;

        let op2 = BlockOperation.init &#123;
            print("op2")
        &#125;

        let op3 = BlockOperation.init &#123;
            print("op3")
        &#125;

        let op4 = BlockOperation.init &#123;
            print("op4")
        &#125;

        op0.addDependency(op1)
        op1.addDependency(op2)

        op0.queuePriority = .veryHigh
        op1.queuePriority = .normal
        op2.queuePriority = .veryLow

        op3.queuePriority = .low
        op4.queuePriority = .veryHigh

        gOpeQueue.addOperations([op0, op1, op2, op3, op4], waitUntilFinished: false)
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：操作间不存在依赖时，按优先级执行；存在依赖时，按依赖关系先后执行（与无依赖关系的其他任务相比，依赖集合的执行顺序不确定）</p>
<h2 data-id="heading-19">队列暂停/继续</h2>
<p>通过对队列的<code>isSuspended</code>属性赋值，可实现队列中未执行任务的暂停和继续效果。正在执行的任务不受影响。</p>
<pre><code class="copyable">///暂停队列，只对未执行中的任务有效。本例中对串行队列的效果明显。并发队列因4个任务一开始就很容易一起开始执行，即使挂起也无法影响已处于执行状态的任务。
    @IBAction func pauseQueueItemDC(_ sender: Any) &#123;
        gOpeQueue.isSuspended = true
    &#125;

    ///恢复队列，之前未开始执行的任务会开始执行
    @IBAction func resumeQueueItemDC(_ sender: Any) &#123;
       gOpeQueue.isSuspended = false
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">取消操作</h2>
<ul>
<li>一旦添加到操作队列中，操作对象实际上归队列所有，不能删除。取消操作的唯一方法是取消它。可以通过调用单个操作对象的 cancel 方法来取消单个操作对象，也可以通过调用队列对象的 cancelAllOperations 方法来取消队列中的所有操作对象。</li>
<li>更常见的做法是取消所有队列操作，以响应某些重要事件，如应用程序退出或用户专门请求取消，而不是有选择地取消操作。</li>
</ul>
<h3 data-id="heading-21">取消单个操作对象</h3>
<p>取消（cancel）时，有 3 种情况：</p>
<blockquote>
<p>1.操作在队列中等待执行，这种情况下，操作将不会被执行。
2.操作已经在执行中，此时，系统不会强制停止这个操作，但是，其 <code>cancelled</code>属性会被置为 true 。</p>
</blockquote>
<p>3.操作已完成，此时，cancel 无任何影响。</p>
<h3 data-id="heading-22">取消队列中的所有操作对象</h3>
<p>方法： cancelAllOperations。同样只会对未执行的任务有效。</p>
<p>demo 中代码：</p>
<pre><code class="copyable">    deinit &#123;
        gOpeQueue.cancelAllOperations()
        print("die:%@",self)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">自问自答</h2>
<ul>
<li>通过设置操作间依赖，可以实现 非FIFO 的指定顺序效果。那么，通过设置最大并发数为 1 ，可以实现指定顺序效果吗？</li>
</ul>
<blockquote>
<p>不可以！ 设置最大并发数为 1 后，虽然每个时间点只执行一个操作，但是操作的执行顺序仍然基于其他因素，如操作的依赖关系，操作的优先级（依赖关系比优先级级别更高，即先根据依赖关系排序;</p>
</blockquote>
<p>不存在依赖关系时，才根据优先级排序）。
因此，序列化 <strong>操作队列</strong> 不会提供与 GCD 中的序列 <strong>分派队列</strong> 完全相同的行为。
如果操作对象的执行顺序对您很重要，那么您应该在将操作添加到队列之前使用 <strong>依赖关系</strong> 建立该顺序，或改用 <strong>GCD 的 串行队列</strong> 实现序列化效果。</p>
<ul>
<li>Operation Queue的 block 中为何无需使用 [weak self] 或 [unowned self] ？</li>
</ul>
<blockquote>
<p>即使队列对象是为全局的，self -> queue -> operation block -> self，的确会造成循环引用。</p>
</blockquote>
<p>但是在队列里的操作执行完毕时，队列会自动释放操作，自动解除循环引用。所以不必使用 [weak self] 或 [unowned self] 。
此外，这种循环引用在某些情况下非常有用，你无需额外持有任何对象就可以让操作自动完成它的任务。
比如下载页面下载过程中，退出有循环引用的界面时，如果不执行 cancelAllOperation 方法，可以实现继续执行剩余队列中下载任务的效果。</p>
<blockquote>
<p>func addOperation(_ op: Operation) Discussion: Once added, the specified operation remains in the queue until it finishes executing. Declaration</p>
<p>func addOperation(_ block: @escaping () -> Void) Parameters block The block to execute from the operation. The block takes no parameters and has no return value. Discussion This method adds a single block to the receiver by first wrapping it in an operation object. You should not attempt to get a reference to the newly created operation object or determine its type information.</p>
</blockquote>
<ul>
<li>操作的 QOS 和队列的 QOS 有何关系？</li>
</ul>
<blockquote>
<p>队列的 QOS 设置，会自动把较低优先级的操作提升到与队列相同优先级。（原更高优先级操作的优先级保持不变）。</p>
</blockquote>
<p>后续添加进队列的操作，优先级低于队列优先级时，也会被自动提升到与队列相同的优先级。
注意，苹果文档如下的解释是错误的 <code>This property specifies the service level applied to operation objects added to the queue. If the operation object has an explicit service level set, that value is used instead.</code> </p>
<h1 data-id="heading-24">常见问题</h1>
<h2 data-id="heading-25">如何解决资源竞争问题</h2>
<p>资源竞争可能导致数据异常，死锁，甚至因访问野指针而崩溃。</p>
<ul>
<li>对于有明显先后依赖关系的任务，最佳方案是 <strong>GCD串行队列</strong>,可以在不使用线程锁时保证资源互斥。</li>
<li>其他情况，对存在资源竞争的代码加锁或使用信号量（初始参数填1，表示只允许一条线程访问资源）。</li>
<li>串行队列同步执行时，如果有<strong>任务相互等待</strong>，会死锁。</li>
</ul>
<p>比如：在主线程上同步执行任务时，因任务和之前已加入主队列但未执行的任务会相互等待，导致死锁。</p>
<pre><code class="copyable">func testDeadLock()&#123;
    //主队列同步执行，会导致死锁。block需要等待testDeadLock执行，而主队列同步调用，又使其他任务必须等待此block执行。于是形成了相互等待，就死锁了。
    DispatchQueue.main.sync &#123;
        print("main block")
    &#125;
    print("2")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是下面代码不会死锁，故<strong>串行队列同步执行任务不一定死锁</strong>。</p>
<pre><code class="copyable">- (void)testSynSerialQueue&#123;
    dispatch_queue_t myCustomQueue;
    myCustomQueue = dispatch_queue_create("com.example.MyCustomQueue", NULL);

    dispatch_async(myCustomQueue, ^&#123;
        printf("Do some work here.\n");
    &#125;);

    printf("The first block may or may not have run.\n");

    dispatch_sync(myCustomQueue, ^&#123;
        printf("Do some more work here.\n");
    &#125;);
    printf("Both blocks have completed.\n");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">如何提高代码效率</h2>
<h3 data-id="heading-27">“西饼传说”</h3>
<p>代码设计优先级：
<strong>系统方法 > 并行 > 串行 > 锁</strong>，简记为：<em>西饼传说</em></p>
<ul>
<li>尽可能依赖 <strong>系统</strong> 框架。实现并发性的最佳方法是利用系统框架提供的内置并发性。</li>
<li>尽早识别系列任务，并尽可能使它们更加 <strong>并行</strong>。如果因为某个任务依赖于某个共享资源而必须连续执行该任务，请考虑更改体系结构以删除该共享资源。您可以考虑为每个需要资源的客户机制作资源的副本，或者完全消除该资源。</li>
<li>不使用锁来保护某些共享资源，而是指定一个 <strong>串行</strong>队列 (或使用操作对象依赖项)以正确的顺序执行任务。</li>
<li>避免使用 <strong>锁</strong>。<strong>GCD 调度队列</strong> 和 <strong>操作队列</strong> 提供的支持使得在大多数情况下不需要锁定。</li>
</ul>
<h1 data-id="heading-28">术语解释摘录</h1>
<ul>
<li><strong>异步任务（asynchronous tasks）：</strong>
<ul>
<li>由一个线程启动，但实际上在另一个线程上运行，利用额外的处理器资源更快地完成工作。</li>
</ul>
</li>
<li><strong>互斥（mutex）：</strong>
<ul>
<li>提供对共享资源的互斥访问的锁。 互斥锁一次只能由一个线程持有。试图获取由不同线程持有的互斥对象会使当前线程处于休眠状态，直到最终获得锁为止。</li>
</ul>
</li>
<li><strong>进程（process）：</strong>
<ul>
<li>应用软件或程序的运行时实例。 进程有自己的虚拟内存空间和系统资源(包括端口权限) ，这些资源独立于分配给其他程序的资源。一个进程总是包含至少一个线程(主线程) ，并且可能包含任意数量的其他线程。</li>
</ul>
</li>
<li><strong>信号量（semaphore）：</strong>
<ul>
<li>限制对共享资源访问的受保护变量。 互斥（Mutexes）和条件（conditions）都是不同类型的信号量。</li>
</ul>
</li>
<li><strong>任务（task），表示需要执行的工作量。</strong></li>
<li><strong>线程（thread)：</strong>
<ul>
<li>进程中的执行流程。 每个线程都有自己的堆栈空间，但在其他方面与同一进程中的其他线程共享内存。</li>
</ul>
</li>
<li><strong>运行循环（run loop）:</strong>
<ul>
<li>一个事件处理循环， 接收事件并派发到适当的处理程序。</li>
</ul>
</li>
</ul>
<h1 data-id="heading-29">文末推荐：iOS热门文集&视频解析</h1>
<h2 data-id="heading-30"><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252Fcz-add%252FiOS_maker%252Ftree%252Fmaster%252FSwift" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcz-add%2FiOS_maker%2Ftree%2Fmaster%2FSwift" ref="nofollow noopener noreferrer">①　Swift</a></h2>
<h2 data-id="heading-31"><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252Fcz-add%252FiOS_maker%252Ftree%252Fmaster%252FiOS%2525E5%2525BA%252595%2525E5%2525B1%252582%2525E8%2525BF%25259B%2525E9%252598%2525B6" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcz-add%2FiOS_maker%2Ftree%2Fmaster%2FiOS%25E5%25BA%2595%25E5%25B1%2582%25E8%25BF%259B%25E9%2598%25B6" ref="nofollow noopener noreferrer">②　iOS底层技术</a></h2>
<h2 data-id="heading-32"><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252Fcz-add%252FiOS_maker%252Ftree%252Fmaster%252FiOS%2525E9%252580%252586%2525E5%252590%252591%2525E5%2525AE%252589%2525E9%252598%2525B2" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcz-add%2FiOS_maker%2Ftree%2Fmaster%2FiOS%25E9%2580%2586%25E5%2590%2591%25E5%25AE%2589%25E9%2598%25B2" ref="nofollow noopener noreferrer">③　iOS逆向防护</a></h2>
<h2 data-id="heading-33"><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252Fcz-add%252FiOS_maker%252Ftree%252Fmaster%252FiOS%2525E9%25259D%2525A2%2525E8%2525AF%252595%2525E5%252590%252588%2525E9%25259B%252586" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcz-add%2FiOS_maker%2Ftree%2Fmaster%2FiOS%25E9%259D%25A2%25E8%25AF%2595%25E5%2590%2588%25E9%259B%2586" ref="nofollow noopener noreferrer">④　iOS面试合集</a></h2>
<h2 data-id="heading-34"><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fwww.bilibili.com%252Fvideo%252FBV1v54y1h7M7" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1v54y1h7M7" ref="nofollow noopener noreferrer">⑤ 大厂面试题+底层技术+逆向安防+Swift</a></h2>
<blockquote>
<p>喜欢的小伙伴记得点赞喔~</p>
<p>收藏等于白嫖，点赞才是真情ღ( ´･ᴗ･` )ღ</p>
</blockquote></div>  
</div>
            