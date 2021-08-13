
---
title: 'iOS多线程使用总结'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d3d1afbaccc40a7b70da17a939ee854~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 22:24:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d3d1afbaccc40a7b70da17a939ee854~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d3d1afbaccc40a7b70da17a939ee854~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一.概述与实现方案</h2>
<h3 data-id="heading-1">1. 线程与进程</h3>
<p>多线程在iOS中有着举足轻重的地位，是每一位开发者都必备的技能，当然也是面试常考的技术点，本文主要是探究我们实际开发或者面试中遇到的多线程问题。比如什么是线程？它跟进程是什么关系，队列跟线程什么关系，<code>同步、异步、并发（并行）、串行</code>这些概念又怎么来理解，iOS有哪些常用多线程方案，以及线程同步技术有哪些等等。</p>
<blockquote>
<p>线程（英语：thread）是操作系统能够进行运算调度的最小单位。大部分情况下，它被包含在进程之中，是进程中的实际运作单位。一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务。   --- 维基百科</p>
</blockquote>
<p>这里又多了一个 <code>进程</code>,那什么是进程呢,说白了就是是指在操作系统中正在运行的一个应用程序，如微信、支付宝app等都是一个进程。线程是就是进程的基本执行单元，一个进程的所有任务都在线程中执行。也就是说 一个进程最少要有一个线程，这个线程就是主线程。当然在我们实际使用过程中不可能只有一条主线程，我们为提高程序的执行效率，往往需要开辟多条子线程去执行一些耗时任务，这里就引出了多线程的概念。</p>
<blockquote>
<p>多线程（英语：multithreading），是指从软件或者硬件上实现多个线程并发执行的技术</p>
</blockquote>
<p>根据操作系统与硬件的不同分为两类：<code>软件多线程</code>与<code>硬件多线程</code></p>
<ul>
<li>
<p>软件多线程: 即便CPU只能运行一个线程，操作系统也可以通过快速的在不同线程之间进行切换，由于时间间隔很小，来给用户造成一种多个线程同时运行的假象</p>
</li>
<li>
<p>硬件多线程: 如果CPU有多个核心，操作系统可以让每个核心执行一条线程，从而具有真正的同时执行多个线程的能力，当然由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。</p>
</li>
</ul>
<p>以上都是google出来的一大堆东西，比较抽象，没关系我们来看下我们实际iOS开发中用到的多线程技术。</p>
<h3 data-id="heading-2">2.iOS中的多线程方案</h3>
<p>iOS 中的多线程方案主要有四种 <code>PThread</code>、<code>NSThread</code>、<code>GCD</code>、<code>NSOperation</code>，<code>PThread</code> 是一套纯粹<code>C</code>语言的API，能适用于Unix\Linux\Windows等系统,线程生命周期需要程序员自己管理，使用难度较大，在我们的实际开发中几乎用不到，在这里我们不做过多介绍，感兴趣的直接去百度。我们着重介绍另外三种方案。</p>
<blockquote>
<p>这里解释一下线程的生命周期，所谓的线程的生命周期就是线程从创建到死亡的过程。一般会经历：<code>新建 - 就绪 - 运行 - 阻塞 - 死亡</code>的过程。</p>
</blockquote>
<ul>
<li>新建：就是初始化线程对象</li>
<li>就绪：向线程对象发送start消息，线程对象被加入可调度线程池等待CPU调度。</li>
<li>运行：CPU 负责调度可调度线程池中线程的执行，线程执行完成之前，状态可能会在就绪和运行之间来回切换。就绪和运行之间的状态变化由CPU负责，程序员不能干预。</li>
<li>阻塞：当满足某个预定条件时，可以使用休眠或锁，阻塞线程执行</li>
<li>死亡：线程执行完毕，退出，销毁。</li>
</ul>
<h4 data-id="heading-3">(1) <code>NSThread</code></h4>
<p>NSThread是苹果官方提供面向对象操作线程的技术，简单方便，可以直接操作线程对象，不过需要自己控制线程的生命周期，我们看下苹果官方给出的方法。</p>
<h5 data-id="heading-4">[1] 初始化方法</h5>
<ul>
<li>实例初始化方法</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (instancetype)init API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0)) NS_DESIGNATED_INITIALIZER;
- (instancetype)initWithTarget:(id)target selector:(SEL)selector object:(nullable id)argument API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0));
- (instancetype)initWithBlock:(void (^)(void))block API_AVAILABLE(macosx(10.12), ios(10.0), watchos(3.0), tvos(10.0));

<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的初始化方法：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> //创建线程
 NSThread *newThread = [[NSThread alloc]initWithTarget:self selector:@selector(demo:) object:@"Thread"];
 NSThread  *newThread=[[NSThread alloc]init];
 NSThread  *newThread= [[NSThread alloc]initWithBlock:^&#123;
     NSLog(@"Block");
 &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意三种方法创建完成后都需要执行 <code>[newThread start]</code> 去启动线程。</p>
</blockquote>
<ul>
<li>类初始化方法</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">+ (void)detachNewThreadWithBlock:(void (^)(void))block API_AVAILABLE(macosx(10.12), ios(10.0), watchos(3.0), tvos(10.0));
+ (void)detachNewThreadSelector:(SEL)selector toTarget:(id)target withObject:(nullable id)argument;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意这两个类方法创建后就可执行，不需手动开启</p>
</blockquote>
<h5 data-id="heading-5">[2] 取消退出</h5>
<p>既然有了创建，那就得有退出</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">// 实例方法 取消线程
- (void)cancel;
//类方法 退出
+ (void)exit;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">[3] 线程执行状态</h5>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">// 线程正在执行
@property (readonly, getter=isExecuting) BOOL executing API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0));
// 线程执行结束
@property (readonly, getter=isFinished) BOOL finished API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0));
// 线程是否可取消
@property (readonly, getter=isCancelled) BOOL cancelled API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0));
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">[4] 线程间的通信方法</h5>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@interface NSObject (NSThreadPerformAdditions)
/*
* 去主线程执行指定方法
* aSelector: 方法
* arg: 参数
* wait:表示是否等待主线程做完事情后往下走，YES表示做完后执行下面事情，NO表示跟下面事情一起执行
*/
- (void)performSelectorOnMainThread:(SEL)aSelector withObject:(nullable id)arg waitUntilDone:(BOOL)wait modes:(nullable NSArray<NSString *> *)array;
- (void)performSelectorOnMainThread:(SEL)aSelector withObject:(nullable id)arg waitUntilDone:(BOOL)wait;
/*
* 去指定线程执行指定方法
* aSelector: 方法
* arg: 参数
* wait:表示是否等待本线程做完事情后往下走，YES表示做完后执行下面事，NO表示跟下面事一起执行
*/
- (void)performSelector:(SEL)aSelector onThread:(NSThread *)thr withObject:(nullable id)arg waitUntilDone:(BOOL)wait modes:(nullable NSArray<NSString *> *)array API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0));
- (void)performSelector:(SEL)aSelector onThread:(NSThread *)thr withObject:(nullable id)arg waitUntilDone:(BOOL)wait API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0));
/*
* 去开启的子线程执行指定方法
* SEL: 方法
* arg: 参数
*/
- (void)performSelectorInBackground:(SEL)aSelector withObject:(nullable id)arg API_AVAILABLE(macos(10.5), ios(2.0), watchos(2.0), tvos(9.0));

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们常说的线程间的通信所用的方法其实就是上面的这几个方法，所有继承NSObject实例化对象都可调用。当然还有其他方法也可以实现线程间的通信，如：<code>GCD</code>、<code>NSOperation</code>、<code>NSMachPort</code>端口等形式，我们后面用到在做介绍。
举个简单的例子：我们在子线程中下载图片，然后去主线程展示：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event &#123;
    // 子线程执行下载方法
    [self performSelectorInBackground:@selector(download) withObject:nil];
&#125;
- (void)download&#123;
    //图片的网络路径
     NSURL *url = [NSURL URLWithString:@"https://p3.ssl.qhimg.com/t011e94f0b9ed8e66b0.png"];
     //下载图片数据
     NSData *data = [NSData dataWithContentsOfURL:url];
     //生成图片
     UIImage *image = [UIImage imageWithData:data];
    // 回主线程显示图片
    [self performSelectorOnMainThread:@selector(showImage:) withObject:image waitUntilDone:YES];
&#125;
- (void)showImage:(UIImage *)image&#123;
    self.imageView.image = image;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">[5] 其他常用方法</h5>
<ul>
<li><code>+(void)currentThread</code> 获取当前线程</li>
<li><code>+(BOOL)isMultiThreaded</code> 判断当前是否运行在子线程</li>
<li><code>-(BOOL)isMainThread</code> 判断是否在主线程</li>
<li><code>+(void)sleepUntilDate:(NSDate *)date;+ (void)sleepForTimeInterval:(NSTimeInterval)ti;</code> 当前线程休眠时间</li>
</ul>
<h4 data-id="heading-9">(2) GCD</h4>
<p>在介绍<code>GCD</code>前我们先来了解下多线程中比较容易混淆的几个概念</p>
<h5 data-id="heading-10">[1]. 同步、异步、并发（并行）、串行</h5>
<ul>
<li>同步和异步主要影响：能不能开启新的线程</li>
</ul>
<p>同步：在当前线程中执行任务，不具备开启新线程的能力
异步：在新的线程中执行任务，具备开启新线程的能力</p>
<ul>
<li>并发和串行主要影响：任务的执行方式</li>
</ul>
<p>并发：也叫并行，也叫并行队列，多个任务并发（同时）执行
串行：也叫串行队列，一个任务执行完毕后，再执行下一个任务</p>
<p>单纯的介绍概念比较抽象，我们还是结合实际使用来说明：<br></p>
<h5 data-id="heading-11">[2] GCD 中的同步、异步方法</h5>
<ul>
<li>同步执行方法：<code>dispatch_sync()</code></li>
<li>异步执行方法：<code>dispatch_async()</code></li>
</ul>
<p>使用方法：</p>
<pre><code class="hljs language-c copyable" lang="c">dispatch_sync(<span class="hljs-keyword">dispatch_queue_t</span> <span class="hljs-built_in">queue</span>, DISPATCH_NOESCAPE <span class="hljs-keyword">dispatch_block_t</span> block);
dispatch_async(<span class="hljs-keyword">dispatch_queue_t</span> <span class="hljs-built_in">queue</span>, <span class="hljs-keyword">dispatch_block_t</span> block);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这个两个方法需要两个参数，第一个参数需要传入一个<code>dispatch_queue_t</code> 类型的队列，第二个是执行的block。下面介绍一下GCD的队列</p>
<h5 data-id="heading-12">[3] GCD 中的队列</h5>
<p>GCD中的队列有三种：<code>串行队列、并行队列、主队列</code>，创建方式也非常简单：</p>
<ul>
<li>串行队列</li>
</ul>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">dispatch_queue_t</span> queue1 = dispatch_queue_create(<span class="hljs-string">"myQueue"</span>, DISPATCH_QUEUE_SERIAL);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个参数是队列名称，第二个是一个宏定义，常用的两个宏 <code>DISPATCH_QUEUE_SERIAL</code> 和 <code>DISPATCH_QUEUE_CONCURRENT</code>分别表示串行队列和并行队列,除此之外，宏<code>DISPATCH_QUEUE_SERIAL_INACTIVE</code> 和 <code>DISPATCH_QUEUE_CONCURRENT_INACTIVE</code> 分别表示初始化的串行队列和并行队列处于不可活动状态。看下它的底层实现</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">dispatch_queue_attr_t</span>
<span class="hljs-title">dispatch_queue_attr_make_initially_inactive</span><span class="hljs-params">(
<span class="hljs-keyword">dispatch_queue_attr_t</span> _Nullable attr)</span></span>;

<span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> DISPATCH_QUEUE_SERIAL_INACTIVE \
dispatch_queue_attr_make_initially_inactive(DISPATCH_QUEUE_SERIAL)</span>

<span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> DISPATCH_QUEUE_CONCURRENT_INACTIVE \
dispatch_queue_attr_make_initially_inactive(DISPATCH_QUEUE_CONCURRENT)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>应当注意的是，初始化后处于不可活动状态的队列，添加到其中的任务要想开始执行，必须先调用 <code>dispatch_activate()</code>函数使其状态变更为可活动状态.</p>
</blockquote>
<ul>
<li>并行队列</li>
</ul>
<p>并行队列有两种：<br>
第一种：全局并发队列创建方法,也是系统为我们创建好的并发队列，创建方式</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">/*  - QOS_CLASS_USER_INTERACTIVE
 *  - QOS_CLASS_USER_INITIATED
 *  - QOS_CLASS_DEFAULT
 *  - QOS_CLASS_UTILITY
 *  - QOS_CLASS_BACKGROUND
*/</span>
<span class="hljs-comment">//dispatch_get_global_queue(intptr_t identifier, uintptr_t flags); </span>

<span class="hljs-keyword">dispatch_queue_t</span> <span class="hljs-built_in">queue</span> = dispatch_get_global_queue(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有两个参数,第一个参数标识线程执行优先级，第二个是苹果保留参数传参：0 就可以。<br>
第二种：手动创建并发队列</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">// 串行执行，第一个参数是名称 ，第二个是标识：DISPATCH_QUEUE_CONCURRENT,并发队列标识</span>
<span class="hljs-keyword">dispatch_queue_t</span> <span class="hljs-built_in">queue</span> = dispatch_queue_create(<span class="hljs-string">"myQueue"</span>,DISPATCH_QUEUE_CONCURRENT);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>主队列</li>
</ul>
<p>主队列是一种特殊的串行队列</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">dispatch_queue_t</span> <span class="hljs-built_in">queue</span> = dispatch_get_main_queue();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同步、异步以及队列的组合就可以实现对任务进行多线程编程的需求了。</p>
<ol>
<li>同步串行队列</li>
</ol>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">  dispatch_queue_t queue1 = dispatch_queue_create("myQueue", DISPATCH_QUEUE_SERIAL);
    for(NSInteger i = 0; i < 10; i++)&#123;
        dispatch_sync(queue1, ^&#123;
            NSLog(@"thread == %@ i====%ld",[NSThread currentThread],(long)i);
        &#125;);
    &#125;
//thread == <NSThread: 0x6000011b8880>&#123;number = 1, name = main&#125; i====n
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可以看到没有开启新的线程，都是在主线程中执行任务,并且是顺序执行的</p>
</blockquote>
<ol start="2">
<li>同步并行队列</li>
</ol>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">dispatch_queue_t queue1 = dispatch_queue_create("myQueue", DISPATCH_QUEUE_CONCURRENT);
    for(NSInteger i = 0; i < 10; i++)&#123;
        dispatch_sync(queue1, ^&#123;
            NSLog(@"thread == %@ i====%ld",[NSThread currentThread],(long)i);
        &#125;);
    &#125;
// thread == <NSThread: 0x600001db8a00>&#123;number = 1, name = main&#125; i====n
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>也是在主线程中顺序执行。</p>
</blockquote>
<ol start="3">
<li>异步串行队列</li>
</ol>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">dispatch_queue_t queue1 = dispatch_queue_create("myQueue", DISPATCH_QUEUE_SERIAL);
    for(NSInteger i = 0; i < 10; i++)&#123;
        dispatch_async(queue1, ^&#123;
            NSLog(@"thread == %@ i====%ld",[NSThread currentThread],(long)i);
        &#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>开启子线程，顺序执行任务</p>
</blockquote>
<ol start="4">
<li>异步并发队列</li>
</ol>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> dispatch_queue_t queue1 = dispatch_queue_create("myQueue", DISPATCH_QUEUE_CONCURRENT);
    for(NSInteger i = 0; i < 10; i++)&#123;
        dispatch_async(queue1, ^&#123;
            NSLog(@"thread == %@ i====%ld",[NSThread currentThread],(long)i);
        &#125;);
    &#125;
/*
thread == <NSThread: 0x6000024f9440>&#123;number = 4, name = (null)&#125; i====0
thread == <NSThread: 0x6000024f5340>&#123;number = 5, name = (null)&#125; i====2
thread == <NSThread: 0x6000024a8780>&#123;number = 3, name = (null)&#125; i====3
thread == <NSThread: 0x6000024ac6c0>&#123;number = 6, name = (null)&#125; i====1
thread == <NSThread: 0x6000024f4a80>&#123;number = 8, name = (null)&#125; i====5
thread == <NSThread: 0x6000024b0b40>&#123;number = 7, name = (null)&#125; i====4
thread == <NSThread: 0x60000249cd00>&#123;number = 9, name = (null)&#125; i====6
thread == <NSThread: 0x6000024b0980>&#123;number = 10, name = (null)&#125; i====7
thread == <NSThread: 0x6000024cb900>&#123;number = 11, name = (null)&#125; i====8
thread == <NSThread: 0x6000024f5340>&#123;number = 5, name = (null)&#125; i====9
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>开启了多个子线程，并且是并发执行任务。</p>
</blockquote>
<p>注意 <code>dispatch_async()</code>具备开辟新线程的能力，但是不表示使用它就一定会开辟新的线程。 例如 传入的 queue 是主队列,就是在主线程中执行任务,没有开辟新线程。</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">  dispatch_queue_t queue1 = dispatch_get_main_queue();
    for(NSInteger i = 0; i < 10; i++)&#123;
        sleep(2);
        dispatch_async(queue1, ^&#123;
            NSLog(@"thread == %@ i====%ld",[NSThread currentThread],(long)i);
        &#125;);
    &#125;
//thread == <NSThread: 0x600002b24880>&#123;number = 1, name = main&#125; i====n
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>主队列是一种特殊的串行队列，从打印结果看出，这里执行方式是串行，而且没有开启新的线程。</p>
</blockquote>
<p>具体任务的执行方式可以参考下面的表格
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6618a38a2a7045e897efab9384f7d584~tplv-k3u1fbpfcp-watermark.image" alt="执行方式" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-13">[4] dispatch_ group_ t 队列组</h5>
<p><code>dispatch_group_t</code>是一个比较实用的方法，通过构造一个组的形式，将各个同步或异步提交任务都加入到同一个组中，当所有任务都完成后会收到通知，用于进一步处理.举个简单的例子如下:</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">dispatch_group_t group = dispatch_group_create();

    dispatch_group_async(group, concurrentQueue, ^&#123;
        for (int i = 0; i < 10; i++)
        &#123;
            NSLog(@"Task1 %@ %d", [NSThread currentThread], i);
        &#125;
    &#125;);
    dispatch_group_async(group, dispatch_get_main_queue(), ^&#123;
        for (int i = 0; i < 10; i++)
        &#123;
            NSLog(@"Task2 %@ %d", [NSThread currentThread], i);
        &#125;
    &#125;);
    dispatch_group_async(group, concurrentQueue, ^&#123;
        for (int i = 0; i < 10; i++)
        &#123;
            NSLog(@"Task3 %@ %d", [NSThread currentThread], i);
        &#125;
    &#125;);
    dispatch_group_notify(group, concurrentQueue, ^&#123;
        NSLog(@"All Task Complete");
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">[5] diapatch_barrier_async 栅栏异步调用函数</h5>
<p>有异步调用就也有同步调用函数<code>diapatch_barrier_sync()</code>，两者的区别：<code>dispatch_barrier_sync</code> 需要等待栅栏执行完才会执行栅栏后面的任务,而<code>dispatch_barrier_async</code> 无需等待栅栏执行完,会继续往下走，有什么用呢？其实栅栏函数用的最多的地方还是实现线程同步使用，比如我们有这样一个需求：怎么样利用GCD实现多读单写文件的IO操作？也就是怎么样实现多读单写，看代码：</p>
<pre><code class="copyable">@interface UserCenter()
&#123;
    // 定义一个并发队列
    dispatch_queue_t concurrent_queue;
    
    // 用户数据中心, 可能多个线程需要数据访问
    NSMutableDictionary *userCenterDic;
&#125;

// 多读单写模型
@implementation UserCenter

- (id)init
&#123;
    self = [super init];
    if (self) &#123;
        // 通过宏定义 DISPATCH_QUEUE_CONCURRENT 创建一个并发队列
        concurrent_queue = dispatch_queue_create("read_write_queue", DISPATCH_QUEUE_CONCURRENT);
        // 创建数据容器
        userCenterDic = [NSMutableDictionary dictionary];
    &#125;
    
    return self;
&#125;

- (id)objectForKey:(NSString *)key
&#123;
    __block id obj;
    // 同步读取指定数据,立刻返回读取结果
    dispatch_sync(concurrent_queue, ^&#123;
        obj = [userCenterDic objectForKey:key];
    &#125;);
    
    return obj;
&#125;

- (void)setObject:(id)obj forKey:(NSString *)key
&#123;
    // 异步栅栏调用设置数据
    dispatch_barrier_async(concurrent_queue, ^&#123;
        [userCenterDic setObject:obj forKey:key];
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可以看到把写操作放入栅栏函数，可以实现线程同步效果</p>
</blockquote>
<p>注意：使用<code>dispatch_barrier_async</code> ，该函数只能搭配自定义并发队列 <code>dispatch_queue_t</code> 使用。不能使用全局并发队列： <code>dispatch_get_global_queue</code>，否则 <code>dispatch_barrier_async</code>无作用。</p>
<h5 data-id="heading-15">[6] 线程死锁</h5>
<p>先来看两个例子：</p>
<pre><code class="copyable">dispatch_queue_t queue = dispatch_get_main_queue();
    dispatch_sync(queue, ^&#123;
        NSLog(@"执行任务2");
    &#125;);// 往主线程里面 同步添加任务 会发生死锁现象

 dispatch_queue_t myQueue = dispatch_queue_create("myQueue", DISPATCH_QUEUE_SERIAL);
    
    dispatch_async(myQueue, ^&#123;
        NSLog(@"1111,thread====%@",[NSThread currentThread]);
        
        dispatch_sync(myQueue, ^&#123;
            NSLog(@"2222,thread====%@",[NSThread currentThread]);
        &#125;);
    &#125;);
// 1111,thread====<NSThread: 0x6000022dd880>&#123;number = 5, name = (null)&#125; 
// crash
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>上面的例子可以看出，不能向当前的串行队列，同步添加任务，否则会产生死锁导致crash。线程死锁的条件：使用sync函数往当前串行队列里面添加任务，会产生死锁。</p>
</blockquote>
<h4 data-id="heading-16">(3) NSOperation</h4>
<p>NSOperation 是苹果对GCD面向对象的封装，它的底层是基于<code>GCD</code>实现的，相比于GCD它添加了更多实用的功能</p>
<ul>
<li>可以添加任务依赖</li>
<li>任务执行状态的控制</li>
<li>设置最大并发数</li>
</ul>
<p>它有两个核心类分别是<code>NSOperation</code>和<code>NSOperationQueue</code>，NSOperation就是对任务进行的封装，封装好的任务交给不同的NSOperationQueue即可进行串行队列的执行或并发队列的执行。</p>
<h5 data-id="heading-17">[1] NSOperation</h5>
<p>NSOperation 是一个抽象类，并不能直接使用，必须使用它的子类，有三种方式：<code>NSInvocationOperation</code>、<code>NSBlockOperation</code>、<code>自定义子类继承NSOperation</code>,前两种是苹果为我们封装好的，可以直接使用，自定义子类，需要我们实现相应的方法。</p>
<ul>
<li>NSBlockOperation & NSInvocationOperation</li>
</ul>
<p>使用：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">//创建一个NSBlockOperation对象，传入一个block
NSBlockOperation *operation = [NSBlockOperation blockOperationWithBlock:^&#123;
    for (int i = 0; i < 5; i++)
    &#123;
        NSLog(@"Task1 %@ %d", [NSThread currentThread], i);
    &#125;
&#125;];

/*
创建一个NSInvocationOperation对象，指定执行的对象和方法
该方法可以接收一个参数即object
*/
NSInvocationOperation *invocationOperation = [[NSInvocationOperation alloc] initWithTarget:self selector:@selector(task:) object:@"Hello, World!"];

// 执行
[operation start];
[invocationOperation start];

// 打印： Task1 <NSThread: 0x6000019581c0>&#123;number = 1, name = main&#125; 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到创建这两个任务对象去执行任务，并没有开启新线程。NSBlockOperation 相比 NSInvocationOperation 多了个<code>addExecutionBlock</code> 追加任务的方法，</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> NSBlockOperation *operation = [NSBlockOperation blockOperationWithBlock:^&#123;
        for (int i = 0; i < 5; i++)
        &#123;
            NSLog(@"task1=====%@ %d", [NSThread currentThread], i);
        &#125;
    &#125;];
    
    [operation addExecutionBlock:^&#123;
       
        NSLog(@"task2=====%@",[NSThread currentThread]);
    &#125;];
    
    [operation addExecutionBlock:^&#123;
       
        NSLog(@"task3=====%@",[NSThread currentThread]);
    &#125;];
    
    [operation addExecutionBlock:^&#123;
       
        NSLog(@"task4=====%@",[NSThread currentThread]);
    &#125;];
    
    [operation start];
/*
task3=====<NSThread: 0x600000509840>&#123;number = 6, name = (null)&#125;
task4=====<NSThread: 0x600000530200>&#123;number = 3, name = (null)&#125;
task1=====<NSThread: 0x600000558880>&#123;number = 1, name = main&#125; 0
task2=====<NSThread: 0x600000511680>&#123;number = 5, name = (null)&#125;
task1=====<NSThread: 0x600000558880>&#123;number = 1, name = main&#125; 1
task1=====<NSThread: 0x600000558880>&#123;number = 1, name = main&#125; 2
task1=====<NSThread: 0x600000558880>&#123;number = 1, name = main&#125; 3
task1=====<NSThread: 0x600000558880>&#123;number = 1, name = main&#125; 4
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>使用<code>addExecutionBlock</code>追加的任务是并发执行的,如果这个操作的任务数大于1那么会开启子线程并发执行任务，这里追加的任务不一定就是子线程，也有可能是主线程。</p>
</blockquote>
<h5 data-id="heading-18">[2] NSOperationQueue</h5>
<p>NSOperationQueue 有两种队列，一个是主队列通过<code>[NSOperationQueue mainQueue]</code> 获取，还有一个是自己创建的队列<code>[[NSOperationQueue alloc] init]</code>,它同时具备并发跟串行的能力，可以通过设置最大并发数来决定。</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> NSBlockOperation *operation = [NSBlockOperation blockOperationWithBlock:^&#123;
        for (int i = 0; i < 5; i++)
        &#123;
            NSLog(@"task1=====%@ %d", [NSThread currentThread], i);
        &#125;
    &#125;];
    
    NSBlockOperation *operation2 = [NSBlockOperation blockOperationWithBlock:^&#123;
        for (int i = 0; i < 5; i++)
        &#123;
            NSLog(@"Task2===== %@ %d", [NSThread currentThread], i);
        &#125;
    &#125;];
    
    NSOperationQueue *queues = [[NSOperationQueue alloc] init];
    [queues setMaxConcurrentOperationCount:2];//设置最大并发数，如果设置为1则串行执行
    [queues addOperation:operation];
    [queues addOperation:operation2];
/*
Task2===== <NSThread: 0x600000489940>&#123;number = 4, name = (null)&#125; 0
task1=====<NSThread: 0x6000004e15c0>&#123;number = 5, name = (null)&#125; 0
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子有两个任务，如果设置最大并发数为2，则会开辟两个线程，并发执行这两个任务。如果设置为1，则会在新的线程中串行执行。</p>
<h5 data-id="heading-19">[3] 任务依赖</h5>
<p><code>addDependency</code>可以建立两个任务之间的依赖关系，如<code>[operation2 addDependency:operation1];</code> 为任务2依赖任务1，必须等任务1执行完成后才会执行任务2，看个例子</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">  NSBlockOperation *operation = [NSBlockOperation blockOperationWithBlock:^&#123;
        for (int i = 0; i < 5; i++)
        &#123;
            NSLog(@"task1=====%@ %d", [NSThread currentThread], i);
        &#125;
    &#125;];
    
    NSBlockOperation *operation2 = [NSBlockOperation blockOperationWithBlock:^&#123;
        for (int i = 0; i < 5; i++)
        &#123;
            NSLog(@"Task2===== %@ %d", [NSThread currentThread], i);
        &#125;
    &#125;];
    
    NSOperationQueue *queues = [[NSOperationQueue alloc] init];
    [queues setMaxConcurrentOperationCount:2];
    //设置任务依赖
    [operation addDependency:operation2];
    
    [queues addOperation:operation];
    [queues addOperation:operation2];
/*
Task2===== <NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 0
Task2===== <NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 1
Task2===== <NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 2
Task2===== <NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 3
Task2===== <NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 4
task1=====<NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 0
task1=====<NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 1
task1=====<NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 2
task1=====<NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 3
task1=====<NSThread: 0x6000005b5dc0>&#123;number = 6, name = (null)&#125; 4
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是以上面的例子，设置<code>[operation addDependency:operation2];</code>,可以看到任务2完成后才会执行任务1的操作。</p>
<h5 data-id="heading-20">[4] 自定义NSOperation</h5>
<p>任务执行状态的控制是相对于自定义的NSOperation子类来说的。对于自定义NSOperation子类有两种类型：<br></p>
<ol>
<li>重写<code>main</code>方法</li>
</ol>
<p>只重写<code>operation</code>的main方法,main方法里面写要执行的任务，系统底层控制变更任务执行完成状态，以及任务的退出。看个例子</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">#import "TestOperation.h"

@interface TestOperation ()
@property (nonatomic, copy) id obj;

@end

@implementation TestOperation

- (instancetype)initWithObject:(id)obj&#123;
    if(self = [super init])&#123;
        self.obj = obj;
    &#125;
    return  self;
&#125;

- (void)main&#123;
    NSLog(@"开始执行任务%@ thread===%@",self.obj,[NSThread currentThread]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">  TestOperation *operation4 = [[TestOperation alloc] initWithObject:[NSString stringWithFormat:@"我是任务4"]];
    [operation4 setCompletionBlock:^&#123;
        NSLog(@"执行完成 thread===%@",[NSThread currentThread]);
    &#125;];
    [operation4 start];
// 打印
开始执行任务我是任务4 thread===<NSThread: 0x6000008d8880>&#123;number = 1, name = main&#125;
执行完成 thread===<NSThread: 0x60000089fa40>&#123;number = 7, name = (null)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到任务operation的main方法执行是在主线程中的，只是最后完成后的回调<code>setCompletionBlock</code>是异步的，好像没什么用，别着急，我们把他放入队列中执行看下，还是上面的例子,加入队列执行</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> NSOperationQueue *queue4 = [[NSOperationQueue alloc] init];
 TestOperation *operation4 = [[TestOperation alloc] initWithObject:[NSString stringWithFormat:@"我是任务4"]];
 TestOperation *operation5 = [[TestOperation alloc] initWithObject:[NSString stringWithFormat:@"我是任务5"]];
 TestOperation *operation6 = [[TestOperation alloc] initWithObject:[NSString stringWithFormat:@"我是任务6"]];

 [queue4 addOperation:operation4];
 [queue4 addOperation:operation5];
 [queue4 addOperation:operation6];
//打印：
开始执行任务我是任务6 thread===<NSThread: 0x600001fc8200>&#123;number = 5, name = (null)&#125;
开始执行任务我是任务4 thread===<NSThread: 0x600001fcc040>&#123;number = 6, name = (null)&#125;
开始执行任务我是任务5 thread===<NSThread: 0x600001fd7c80>&#123;number = 7, name = (null)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候可以看到任务的并发执行了，operation的main方法执行结束后就会调用各自的<code>dealloc</code>方法进行释放，任务的生命周期结束。如果我们想让任务4、5、6 倒序执行，可以添加任务依赖</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> [operation4 addDependency:operation5];
 [operation5 addDependency:operation6];
// 打印
开始执行任务我是任务6 thread===<NSThread: 0x600003d04680>&#123;number = 6, name = (null)&#125;
开始执行任务我是任务5 thread===<NSThread: 0x600003d04680>&#123;number = 6, name = (null)&#125;
开始执行任务我是任务4 thread===<NSThread: 0x600003d04680>&#123;number = 6, name = (null)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样做貌似是可以的，但是如果我们的operation 中又存在异步任务（如网络请求），我们想让网络任务6请求完后调用任务5，任务5调用成功后调任务4，那该怎么办呢，我们先卖个关子，我们在第二节<code>多个请求完成后继续进行下一个请求的方法总结</code>中介绍。
2. 重写<code>start</code>方法
通过重写<code>main</code>方法可以实现任务的串行执行，如果要让任务并发执行，就需要重写<code>start</code>方法。两者还是有很大区别的：
如果只是重写main方法，方法执行完毕，那么整个operation就会从队列中被移除。如果你是一个自定义的operation并且它是某些类的代理，这些类恰好有异步方法，这时就会找不到代理导致程序出错了。然而start方法就算执行完毕，它的finish属性也不会变，因此你可以控制这个operation的生命周期了。然后在任务完成之后手动cancel掉这个operation即可。</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@interface TestStartOperation : NSOperation
- (instancetype)initWithObject:(id)obj;
@property (nonatomic, copy) id obj;
@property (nonatomic, assign, getter=isExecuting) BOOL executing;
@property (nonatomic, assign, getter=isFinished) BOOL finished;
@end
@implementation TestStartOperation
@synthesize executing = _executing;
@synthesize finished = _finished;

- (instancetype)initWithObject:(id)obj&#123;
    if(self = [super init])&#123;
        self.obj = obj;
    &#125;
    return  self;
&#125;
- (void)start&#123;
    
    //在任务开始前设置executing为YES，在此之前可能会进行一些初始化操作
    self.executing = YES;
    NSLog(@"开始执行任务%@ thread===%@",self.obj,[NSThread currentThread]);
    /*
    需要在适当的位置判断外部是否调用了cancel方法
    如果被cancel了需要正确的结束任务
    */
    if (self.isCancelled)
    &#123;
        //任务被取消正确结束前手动设置状态
        self.executing = NO;
        self.finished = YES;
        return;
    &#125;
    
    NSString *str = @"https://www.360.cn";
    NSURL *url = [NSURL URLWithString:str];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    NSURLSession *session = [NSURLSession sharedSession];
    __weak typeof(self) weakSelf = self;
    NSURLSessionDataTask *task = [session dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) &#123;
       // NSLog(@"response==%@",response);
        NSLog(@"TASK完成:====%@ thread====%@",weakSelf.obj,[NSThread currentThread]);
        //任务执行完成后手动设置状态
        weakSelf.executing = NO;
        weakSelf.finished = YES;
    &#125;];
    [task resume];
&#125;
- (void)setExecuting:(BOOL)executing
&#123;
    //手动调用KVO通知
    [self willChangeValueForKey:@"isExecuting"];
    _executing = executing;
    //调用KVO通知
    [self didChangeValueForKey:@"isExecuting"];
&#125;
- (BOOL)isExecuting
&#123;
    return _executing;
&#125;
- (void)setFinished:(BOOL)finished
&#123;
    //手动调用KVO通知
    [self willChangeValueForKey:@"isFinished"];
    _finished = finished;
    //调用KVO通知
    [self didChangeValueForKey:@"isFinished"];
&#125;
- (BOOL)isFinished
&#123;
    return _finished;
&#125;
- (BOOL)isAsynchronous
&#123;
    return YES;
&#125;
- (void)dealloc&#123;
    NSLog(@"Dealloc %@",self.obj);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行与结果</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">NSOperationQueue *queue4 = [[NSOperationQueue alloc] init];
TestStartOperation *operation4 = [[TestStartOperation alloc] initWithObject:[NSString stringWithFormat:@"我是任务4"]];
TestStartOperation *operation5 = [[TestStartOperation alloc] initWithObject:[NSString stringWithFormat:@"我是任务5"]];
TestStartOperation *operation6 = [[TestStartOperation alloc] initWithObject:[NSString stringWithFormat:@"我是任务6"]];
//设置任务依赖 
[operation4 addDependency:operation5];
[operation5 addDependency:operation6];
[queue4 addOperation:operation4];
[queue4 addOperation:operation5];
[queue4 addOperation:operation6];
/*打印
开始执行任务我是任务6 thread===<NSThread: 0x600002bb8480>&#123;number = 6, name = (null)&#125;
TASK完成:====我是任务6 thread====<NSThread: 0x600002bd4d80>&#123;number = 8, name = (null)&#125;
开始执行任务我是任务5 thread===<NSThread: 0x600002bb0300>&#123;number = 5, name = (null)&#125;
TASK完成:====我是任务5 thread====<NSThread: 0x600002bb0300>&#123;number = 5, name = (null)&#125;
开始执行任务我是任务4 thread===<NSThread: 0x600002bfb080>&#123;number = 7, name = (null)&#125;
TASK完成:====我是任务4 thread====<NSThread: 0x600002bfb080>&#123;number = 7, name = (null)&#125;
2021-06-22 17:57:56.436591+0800 Interview01-打印[15994:9172130] Dealloc 我是任务4
2021-06-22 17:57:56.436690+0800 Interview01-打印[15994:9172130] Dealloc 我是任务5
2021-06-22 17:57:56.436784+0800 Interview01-打印[15994:9172130] Dealloc 我是任务6
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中我们在任务请求完成后，手动设置其<code>self.executing</code>和<code>self.finished</code>状态，并且手动触发KVO，队列会监听任务的执行状态。由于我们设置了任务依赖，当任务6请求完成后才会执行任务5，任务5请求完成后 才会执行任务4。最后对各自任务进行移除队列并释放。其实这样也变相解决了上面重写<code>main</code>方法中无法解决的问题。</p>
<h2 data-id="heading-21">二.实际应用</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9edf828ef644659a5e8bf76912e513d~tplv-k3u1fbpfcp-watermark.image" alt="执行" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>多个请求完成后继续进行下一个请求的方法总结</p>
</blockquote>
<p>在我们的工作中经常会遇到这样的请求：一个请求依赖另一个请求的结果，或者多个请求一起发出然后再获取所有的结果后继续后续操作。根据这几种情况总结常用的方法：</p>
<h3 data-id="heading-22">1. 使用<code>GCD</code>的<code>dispatch_group_t</code>实现</h3>
<p>需求：请求顺序执行，执行完成后回调结果</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> NSString *str = @"https://www.360.cn";
 NSURL *url = [NSURL URLWithString:str];
 NSURLRequest *request = [NSURLRequest requestWithURL:url];
 NSURLSession *session = [NSURLSession sharedSession];
   
 dispatch_group_t downloadGroup = dispatch_group_create();
 for (int i=0; i<10; i++) &#123;
       dispatch_group_enter(downloadGroup);
       NSURLSessionDataTask *task = [session dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) &#123;
           
          NSLog(@"执行完请求=%d",i);
          dispatch_group_leave(downloadGroup);
       &#125;];
       
       [task resume];
   &#125;
   dispatch_group_notify(downloadGroup, dispatch_get_main_queue(), ^&#123;
       NSLog(@"end");
   &#125;);
/*
2021-06-22 18:37:56.786878+0800 Interview01-打印[17121:9352056] 请求结束：0
2021-06-22 18:37:56.787770+0800 Interview01-打印[17121:9352057] 请求结束：1
2021-06-22 18:37:56.788492+0800 Interview01-打印[17121:9352057] 请求结束：2
2021-06-22 18:37:56.789148+0800 Interview01-打印[17121:9352057] 请求结束：3
2021-06-22 18:37:56.789837+0800 Interview01-打印[17121:9352057] 请求结束：4
2021-06-22 18:37:56.790433+0800 Interview01-打印[17121:9352059] 请求结束：5
2021-06-22 18:37:56.791117+0800 Interview01-打印[17121:9352059] 请求结束：6
2021-06-22 18:37:56.791860+0800 Interview01-打印[17121:9352059] 请求结束：7
2021-06-22 18:37:56.792614+0800 Interview01-打印[17121:9352059] 请求结束：8
2021-06-22 18:37:56.793201+0800 Interview01-打印[17121:9352059] 请求结束：9
2021-06-22 18:37:56.804529+0800 Interview01-打印[17121:9351753] end*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要方法：</p>
<ul>
<li><code>dispatch_group_t downloadGroup = dispatch_group_create();</code>创建队列组</li>
<li><code>dispatch_group_enter(downloadGroup);</code> 每次执行请求前调用</li>
<li><code>dispatch_group_leave(downloadGroup);</code> 请求完成后调用离开方法</li>
<li><code>dispatch_group_notify()</code> 所有请求完成后回调block</li>
<li>对于enter和leave必须配合使用，有几次enter就要有几次leave</li>
</ul>
<h3 data-id="heading-23">2. <code>GCD</code>信号量<code>dispatch_semaphore_t</code></h3>
<h4 data-id="heading-24">(1).需求：顺序执行多个请求，都执行完成后回调给end</h4>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">NSString *str = @"https://www.360.cn";
NSURL *url = [NSURL URLWithString:str];
NSURLRequest *request = [NSURLRequest requestWithURL:url];
NSURLSession *session = [NSURLSession sharedSession];
       
dispatch_semaphore_t sem = dispatch_semaphore_create(0);
   
for (int i=0; i<10; i++) &#123;
      
     NSURLSessionDataTask *task = [session dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) &#123;
           
           NSLog(@"请求结束：%d",i);
           dispatch_semaphore_signal(sem);
     &#125;];
     [task resume];
     dispatch_semaphore_wait(sem, DISPATCH_TIME_FOREVER);
&#125;
   dispatch_async(dispatch_get_main_queue(), ^&#123;
       NSLog(@"end");
   &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要方法</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">dispatch_semaphore_t sem = dispatch_semaphore_create(0);
dispatch_semaphore_signal(sem);
dispatch_semaphore_wait(sem, DISPATCH_TIME_FOREVER);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>dispatch_semaphore</code>信号量为基于计数器的一种多线程同步机制,<code>dispatch_semaphore_signal(sem);</code>表示为计数+1操作，<code>dispatch_semaphore_wait(sem, DISPATCH_TIME_FOREVER);</code> 信号量-1，遇到<code>dispatch_semaphore_wait</code>如果信号量的值小于0,就一直阻塞线程,不执行后面的所有程序,直到信号量大于等于0;当第一个for循环执行后<code>dispatch_semaphore_wait</code>堵塞线程，直到执行到<code>dispatch_semaphore_signal</code>后继续下一个for循环进行请求，以此类推完成顺序请求。</p>
<h4 data-id="heading-25">(2).需求：多个请求同时进行，都执行完成后回调给end</h4>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">NSString *str = @"https://www.360.cn";
NSURL *url = [NSURL URLWithString:str];
NSURLRequest *request = [NSURLRequest requestWithURL:url];
NSURLSession *session = [NSURLSession sharedSession];
       
 dispatch_semaphore_t sem = dispatch_semaphore_create(0);
 __block int count = 0;
 for (int i=0; i<10; i++) &#123;
           
      NSURLSessionDataTask *task = [session dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) &#123;
               
        NSLog(@"%d---%d",i,i);
        count++;
        if (count==10) &#123;
            dispatch_semaphore_signal(sem);
             count = 0;
         &#125;
       &#125;];
           
       [task resume];
   &#125;
   dispatch_semaphore_wait(sem, DISPATCH_TIME_FOREVER);
       
   dispatch_async(dispatch_get_main_queue(), ^&#123;
        NSLog(@"end");
   &#125;);
/*
2021-06-23 09:47:49.723576+0800 Interview01-打印[21740:9823752] 请求完成：0
2021-06-23 09:47:49.741118+0800 Interview01-打印[21740:9823751] 请求完成：1
2021-06-23 09:47:49.756781+0800 Interview01-打印[21740:9823752] 请求完成：3
2021-06-23 09:47:49.765250+0800 Interview01-打印[21740:9823752] 请求完成：2
2021-06-23 09:47:49.773008+0800 Interview01-打印[21740:9823756] 请求完成：4
2021-06-23 09:47:49.797809+0800 Interview01-打印[21740:9823751] 请求完成：5
2021-06-23 09:47:49.801775+0800 Interview01-打印[21740:9823751] 请求完成：6
2021-06-23 09:47:49.805542+0800 Interview01-打印[21740:9823751] 请求完成：7
2021-06-23 09:47:49.814714+0800 Interview01-打印[21740:9823751] 请求完成：8
2021-06-23 09:47:49.850517+0800 Interview01-打印[21740:9823753] 请求完成：9
2021-06-23 09:47:49.864394+0800 Interview01-打印[21740:9823591] end
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个也比较好理解，for循环运行后堵塞当前线程（当前是主线程，你也可以把这段代码放入子线程中去执行），当10个请求全部完成后发送信号，继续下面的流程。</p>
<h3 data-id="heading-26">3. 使用<code>NSOperation</code>与<code>GCD</code>结合使用</h3>
<p>需求：两个网络请求，第一个依赖第二个的回调结果</p>
<p>通过自定义<code>operation</code>实现，我们重写其main方法</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">@interface CustomOperation : NSOperation
@property (nonatomic, copy) id obj;
- (instancetype)initWithObject:(id)obj;
@end
@implementation CustomOperation

- (instancetype)initWithObject:(id)obj&#123;
    if(self = [super init])&#123;
        self.obj = obj;
    &#125;
    return  self;
&#125;

- (void)main&#123;
    
    //创建信号量并设置计数默认为0
    dispatch_semaphore_t sema = dispatch_semaphore_create(0);
    NSLog(@"开始执行任务%@",self.obj);
    NSString *str = @"https://www.360.cn";
    NSURL *url = [NSURL URLWithString:str];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    NSURLSession *session = [NSURLSession sharedSession];
    
    NSURLSessionDataTask *task = [session dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) &#123;
        NSLog(@"TASK完成:====%@ thread====%@",self.obj,[NSThread currentThread]);
        //请求成功 计数+1操作
        dispatch_semaphore_signal(sema);
    &#125;];

    [task resume];
    
    //若计数为0则一直等待
    dispatch_semaphore_wait(sema, DISPATCH_TIME_FOREVER);
    
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用与结果</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> NSOperationQueue *queue3 = [[NSOperationQueue alloc] init];
    [queue3 setMaxConcurrentOperationCount:2];
    CustomOperation *operation0 = [[CustomOperation alloc] initWithObject:@"我是任务0"];
    CustomOperation *operation1 = [[CustomOperation alloc] initWithObject:@"我是任务1"];
    CustomOperation *operation2 = [[CustomOperation alloc] initWithObject:@"我是任务2"];
    CustomOperation *operation3 = [[CustomOperation alloc] initWithObject:@"我是任务3"];

    [operation0 addDependency:operation1];
    [operation1 addDependency:operation2];
    [operation2 addDependency:operation3];

    [queue3 addOperation:operation0];
    [queue3 addOperation:operation1];
    [queue3 addOperation:operation2];
    [queue3 addOperation:operation3];
/**打印结果
开始执行任务我是任务3
TASK完成:====我是任务3 thread====<NSThread: 0x6000039c3340>&#123;number = 5, name = (null)&#125;
开始执行任务我是任务2
TASK完成:====我是任务2 thread====<NSThread: 0x6000039ece80>&#123;number = 7, name = (null)&#125;
开始执行任务我是任务1
TASK完成:====我是任务1 thread====<NSThread: 0x6000039c3340>&#123;number = 5, name = (null)&#125;
开始执行任务我是任务0
TASK完成:====我是任务0 thread====<NSThread: 0x6000039c3d00>&#123;number = 6, name = (null)&#125;
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>设置任务依赖并且添加到队列后是可以满足我们的需求</li>
<li>由于任务内部是异步回调，可以看到任务内部的执行还是依赖于<code>dispatch_semaphore_t</code>来实现的</li>
<li>也可以通过重写<code>start</code>方法实现，在上面章节我们已经介绍过了，这里不再赘述。</li>
</ul>
<h2 data-id="heading-27">三. 总结</h2>
<p>本文的篇幅有点长了，但是还有一些内容没有覆盖到，比如iOS中常用的线程锁、<code>NSOperationQueue</code>的暂停与取消等，我们会在后面的文章中逐步完善补充。</p>
<blockquote>
<p>由于作者水平有限，难免出现纰漏，如有问题还请不吝赐教。</p>
</blockquote>
<p>参考资料：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Flibrary%2Farchive%2Fdocumentation%2FGeneral%2FConceptual%2FConcurrencyProgrammingGuide%2FOperationObjects%2FOperationObjects.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationObjects/OperationObjects.html" ref="nofollow noopener noreferrer">苹果官方——并发编程指南：Operation Queues</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fliuyang11908%2Farticle%2Fdetails%2F70757534" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/liuyang11908/article/details/70757534" ref="nofollow noopener noreferrer">iOS GCD之dispatch_semaphore(信号量)</a></p></div>  
</div>
            