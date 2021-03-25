
---
title: '如何吃透一个Java项目？（附学习实践）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edb849fc52f54c44a6e1268eaecc6506~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 00:00:03 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edb849fc52f54c44a6e1268eaecc6506~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先说一下自己的情况：就是对着视频敲Java项目，其中遇到的BUG还能解决，但就是每次敲完一个项目，就感觉很空虚，项目里面的知识点感觉懂了但又好像没懂，我应该怎样才能掌握一个项目所用的知识点呢？至少不至于过了一头半个月就想不起来这个项目是什么东西了。</p>
<p>写博客记录？，画思维导图？还是怎么样呢？有没有过来人能给点经验呢？</p>
<blockquote>
<p>首先，尝试分析下题主感到空虚、似懂非懂的原因，从问题描述来看原因可能有以下几方面：</p>
</blockquote>
<h1 data-id="heading-0">目标不清晰</h1>
<p>在项目学习之前，是否有认真梳理和思考过，希望通过项目学习到哪些技术、重点需掌握哪些知识点？这些知识点又属于自己技术体系中哪个环节，是需要必须熟练掌握还是了解原理即可？相信只有明确目标之后才有学习侧重点和方向。</p>
<h1 data-id="heading-1">学习方法</h1>
<p>项目学习过程中，是否有带着问题和思考？比如项目核心需要解决的问题场景、使用了哪些技术方案，为什么需要这些技术，方案选择考虑主要有哪些？系统模块这样分层和实现的好处是？这个方法的实现，性能是否可以进一步优化等等。</p>
<p>如果只是纯粹跟着视频将项目代码机械敲一遍，我认为跟练习打字没任何区别，写出来的代码也是没有灵魂如行尸走肉。我相信只有结合自己的思考和理解，才可能赋予新的灵魂，做到知其然知其所以然，相关知识点也才能真正转化为自己的技术。</p>
<h1 data-id="heading-2">复习与应用</h1>
<p>纸上得来终觉浅，绝知此事要躬行，相信对编程而言更是如此，唯有实践才能出真知。对项目中学到的相关技术、知识点需要在不同场景反复练习和应用，并对过程中遇到的问题不断总结和反思。</p>
<blockquote>
<p>其次，回到题主问题，如何吃透一个Java项目？从个人经验来看，大致可以从以下几方面入手：</p>
</blockquote>
<h1 data-id="heading-3">项目背景了解</h1>
<p>学习之前，先对项目业务背景和技术体系做大致的了解，这点非常重要，一是为了解项目核心要解决问题域，二是知道系统涉及哪些技术体系，这样在学习之前可以有相关技术知识准备，以便更轻松高效学习。另外，学习完之后也可以清楚知道，什么样问题可以使用什么技术、什么方案来解决、如何解决的。</p>
<h1 data-id="heading-4">系统设计文档学习</h1>
<p>对项目和系统大概了解之后，可以开始对系统设计文档熟悉，建议按照架构文档、概要设计、详细设计方式递进。通过设计文档的学习，可以快速对各系统模块有个框架性认识，知道什么各系统职责、边界、如何交互、系统核心模型等等。</p>
<p>对于设计文档的学习，切不可走马观花，一定要带着问题和思考。比如项目背景中的核心业务问题，架构师是如何转化成技术落地，方案为什么要这样设计，模型为什么要这样抽象，这样做的好处是什么等等？同时，对不理解的问题做需好笔记，以便后续向老师或其他同事请教或讨论等等。</p>
<h1 data-id="heading-5">系统熟悉和代码阅读</h1>
<p>通过设计文档的学习，对系统设计有整体了解之后，接下来就可以结合业务场景、相关问题去看代码如何实现了。不过代码阅读，需要注意方式方法，切不可陷入代码细节，应该自顶向下、分层分模块的阅读，以先整体、后模块、单功能点的方式层层递进。先快速走读整个代码模块逻辑，然后再精读某个类、方法的实现。</p>
<p>代码阅读过程中，建议一边阅读一边整理相关代码模块、流程分支、交互时序，以及类图等，以便更好理解，有些IDE工具也可根据代码自动生成，比如IntelliJ IDEA。</p>
<p>代码阅读除了关注具体功能的实现之外，更重要的是需要关心代码设计上的思路和原理、性能考究、设计模式、以及设计原则的应用等。同样，阅读代码注释也非常重要，在研究一个API或方法实现时，先认真阅读代码注释会让你事半功倍，尽可能不要做从代码中反推逻辑和功能的事情。</p>
<p>最后，对于核心功能代码建议分模块精读，不明白部分可借助代码调试。</p>
<blockquote>
<p>然后，对于技术学习这块我给几点个人建议，以供题主参考：</p>
</blockquote>
<h1 data-id="heading-6">制定学习规划</h1>
<p>梳理一份适合自己的技术规划，并制定明确的学习路线和计划，让学习更有方向和重点。同样在视频课程的选择上也会更清晰，知道什么样视频该学、什么不该学，也不容易感到迷茫和空虚。如今网上各种学习资料、视频汗牛充栋，学会如何筛选有效、适合自己的信息非常重要。</p>
<h1 data-id="heading-7">思考与练习</h1>
<p>对于技术编程，无捷径可言，思考和练习都非常重要，需要不断学习、思考、实践反复操练。从了解、会用、知原理、优化不断演进。结合学习计划，可以给自己制定不同挑战，比如学习spring可以尝试自己实现一个ioc容器等等。另外，工作或学习过程中遇到的问题，也是你快速提升技术能力的一个好方法，也请珍惜你遇到的每个问题的机会。时间允许的话，也请尽可能去帮助别人解答问题，像stackoverflow就是个非常不错的选择，帮助别人的同时提升自己。</p>
<h1 data-id="heading-8">分享与交流</h1>
<p>保持思考总结的习惯，将学到的技术多与人分享交流，教学相长。多与优秀的程序员一起、多参与优秀的开源项目等。</p>
<p>最后，我再以我们团队Dubbo核心开发@哲良大神的另一开源框架TransmittableThreadLocal(TTL)为例，来讲解下我们该如何学习和快速掌握一个项目。</p>
<p>结合上文所述，首先我会将TTL项目相关文档、issues列表认真阅读一遍，让自己对项目能有个大体的认识，并梳理出项目一些关键信息，比如：</p>
<p>• 核心要解决的问题</p>
<p>• 用于解决「在线程池或线程会被复用情况下，如何解决线程ThreadLocal传值问题」</p>
<p>• 有哪些典型业务场景</p>
<p>• 分布式跟踪系统或全链路压测（即链路打标）</p>
<p>• 日志收集记录系统上下文</p>
<p>• Session级Cache</p>
<p>• 应用容器或上层框架跨应用代码给下层SDK传递信息</p>
<p>• 使用到的技术</p>
<p>• 有线程、线程池、ThreadLocal、InheritableThreadLocal、并发、线程安全等。</p>
<p>然后，再结合使用文档编写几个测试demo，通过程序代码练习和框架使用，一步步加深对框架的理解。比如我这里首先会拿TTL与原生JDK InheritableThreadLocal进行不同比较，体验两者的核心区别。</p>
<pre><code class="copyable">public class ThreadLocalTest &#123;

    private static final AtomicInteger ID_SEQ = new AtomicInteger();
    private static final ExecutorService EXECUTOR = Executors.newFixedThreadPool(1, r -> new Thread(r, "TTL-TEST-" + ID_SEQ.getAndIncrement()));

    //
    private static ThreadLocal<String> THREAD_LOCAL = new InheritableThreadLocal<>();

    //⑴ 声明TransmittableThreadLocal类型的ThreadLocal
    //private static ThreadLocal<String> THREAD_LOCAL = new TransmittableThreadLocal<>();
    public static void testThreadLocal() throws InterruptedException &#123;
        try &#123;
            //doSomething()...
            THREAD_LOCAL.set("set-task-init-value");
            //
            Runnable task1 = () -> &#123;
                try &#123;
                    String manTaskCtx = THREAD_LOCAL.get();
                    System.out.println("task1:" + Thread.currentThread() + ", get ctx:" + manTaskCtx);
                    THREAD_LOCAL.set("task1-set-value");
                &#125; finally &#123;
                    THREAD_LOCAL.remove();
                &#125;
            &#125;;
            EXECUTOR.submit(task1);

            //doSomething....
            TimeUnit.SECONDS.sleep(3);

            //⑵ 设置期望task2可获取的上下文
            THREAD_LOCAL.set("main-task-value");

            //⑶ task2的异步任务逻辑中期望获取⑵中的上下文
            Runnable task2 = () -> &#123;
                String manTaskCtx = THREAD_LOCAL.get();
                System.out.println("task2:" + Thread.currentThread() + ", get ctx :" + manTaskCtx);
            &#125;;
            //⑷ 转换为TransmittableThreadLocal 增强的Runnable
            //task2 = TtlRunnable.get(task2);
            EXECUTOR.submit(task2);
        &#125;finally &#123;
            THREAD_LOCAL.remove();
        &#125;
    &#125;
    public static void main(String[] args) throws InterruptedException &#123;
        testThreadLocal();
    &#125;
&#125;

//InheritableThreadLocal 运行结果：
task1:Thread[TTL-TEST-0,5,main], get ctx:set-task-init-value
task2:Thread[TTL-TEST-0,5,main], get ctx :null
    
//TransmittableThreadLocal 运行结果
task1:Thread[TTL-TEST-0,5,main], get ctx:set-task-init-value
task2:Thread[TTL-TEST-0,5,main], get ctx :main-task-value    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过代码运行结果，我们可以直观看到使用JDK原生InheritableThreadLocal，在task2异步任务中是无法正确获取代码⑵处所设置的上下文参数，只有改用TransmittableThreadLocal之后，程序才如我们预期正常获取。</p>
<p>不难发现，由JDK原生ThreadLocal切换到TransmittableThreadLocal，只需要做极少量的代码适配即可。</p>
<pre><code class="copyable">//private static ThreadLocal<String> THREAD_LOCAL = new InheritableThreadLocal<>();
//⑴ 声明TransmittableThreadLocal类型的ThreadLocal
private static ThreadLocal<String> THREAD_LOCAL = new TransmittableThreadLocal<>();

...
//⑷ 转换为TransmittableThreadLocal 增强的Runnable
task2 = TtlRunnable.get(task2);    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信看到这里我们都会不禁想问，为什么只需要简单的更改两行代码，就可以平滑实现上下文透传？TTL框架背后具体都做了哪些工作，到底是怎么实现的呢？相信你和我一样都会比较好奇，也一定有想立马阅读源码一探究竟的冲动。</p>
<p>不过，通常这个时候，我并不会一头扎进源码，一般都会先做几项目准备工作，一是回到设计文档再仔细的阅读下相关实现方案，把关键流程和原理了解清楚；二是把涉及到的技术体相关的基础知识再复习或学习一遍，以避免由于一些基础知识原理的不了解，导致源码无法深入研究或花费大量精力。像这里如果我对Thread、ThreadLocal、InheritableThreadLocal、线程池等相关知识不熟悉的话，一定会把相关知识先学习一遍，比如ThreadLocal基本原理、底层数据结构、InheritableThreadLocal如何实现父子线程传递等等。</p>
<p>假设这里你对这些知识都已掌握，如果不熟悉，网上相关介绍文章也早已是汗牛充栋，你搜索学习下即可。这里我们先带着到底如何实现的这个疑问，一起来探究下核心源码实现。</p>
<p>首先把源码clone下来导入IDE，然后结合文档把系统工程结构和各功能模块职责快速熟悉一遍，然后结合文档和Demo找到关键接口和实现类，利用IDE把相关类图结构生成出来，以便快速理解类之间关系。非常不错，TTL整体代码非常精练、命名和包信息描述也都非常规范和清晰，我们可以快速圈出来。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edb849fc52f54c44a6e1268eaecc6506~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从类图中我们可以清晰看到核心关键类TransmittableThreadLocal是从ThreadLocal继承而来，这样的好处是不破坏ThreadLocal原生能力的同时还可增强和扩展自有能力，也可保证业务代码原有互操作性和最小改动。</p>
<p>然后结合Demo代码，我们使用TTL主要有三个步骤，TransmittableThreadLocal声明、set、remove方法的调用。根据整个使用流程和方法调用栈，我们可以很方便梳理出整个代码处理初始化、调用时序。</p>
<p>(这里借用官方原图)</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8c419bdc93542e3a2e9fc9a0576bed0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过流程图，我们可以清晰看到TTL核心流程和原理是通过TransmittableThreadLocal.Transmitter 抓取当前线程的所有TTL值并在其他线程进行回放，然后在回放线程执行完业务操作后，再恢复为回放线程原来的TTL值。</p>
<blockquote>
<p>TransmittableThreadLocal.Transmitter提供了所有TTL值的抓取、回放和恢复方法（即CRR操作）：
capture方法：抓取线程（线程A）的所有TTL值。
replay方法：在另一个线程（线程B）中，回放在capture方法中抓取的TTL值，并返回 回放前TTL值的备份
restore方法：恢复线程B执行replay方法之前的TTL值（即备份）</p>
</blockquote>
<p>弄明白核心流程和原理后，我们现在来分析下相关核心代码，在声明TransmittableThreadLocal变量时，我们会发现框架初始化了一个类级别的变量holder用于存储用户设置的所有ttl上下文，也是为了后续执行capture抓取时使用。</p>
<pre><code class="copyable">    // Note about the holder:
    // 1. holder self is a InheritableThreadLocal(a *ThreadLocal*).
    // 2. The type of value in the holder is WeakHashMap<TransmittableThreadLocal<Object>, ?>.
    //    2.1 but the WeakHashMap is used as a *Set*:
    //        the value of WeakHashMap is *always* null, and never used.
    //    2.2 WeakHashMap support *null* value.
    private static final InheritableThreadLocal<WeakHashMap<TransmittableThreadLocal<Object>, ?>> holder =
        new InheritableThreadLocal<WeakHashMap<TransmittableThreadLocal<Object>, ?>>() &#123;
        @Override
        protected WeakHashMap<TransmittableThreadLocal<Object>, ?> initialValue() &#123;
            return new WeakHashMap<TransmittableThreadLocal<Object>, Object>();
        &#125;
        @Override
        protected WeakHashMap<TransmittableThreadLocal<Object>, ?> childValue(WeakHashMap<TransmittableThreadLocal<Object>, ?> parentValue) &#123;
            return new WeakHashMap<TransmittableThreadLocal<Object>, Object>(parentValue);
        &#125;
    &#125;;

    /**
     * see &#123;@link InheritableThreadLocal#set&#125;
     */
    @Override
    public final void set(T value) &#123;
        if (!disableIgnoreNullValueSemantics && null == value) &#123;
            // may set null to remove value
            remove();
        &#125; else &#123;
            super.set(value);
            addThisToHolder();
        &#125;
    &#125;

    private void addThisToHolder() &#123;
        if (!holder.get().containsKey(this)) &#123;
            holder.get().put((TransmittableThreadLocal<Object>) this, null); // WeakHashMap supports null value.
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合set方法实现来看，我们会发现holder变量设计的非常巧妙，业务设置的上下文value部分继续复用ThreadLocal原有数据结构ThreadLocalMap来存储( super.set(value))；capture的数据源利用holder进行引用存储(addThisToHolder put this)。这样即可保持ThreadLocal数据存储原有的封装性，又很好实现扩展。除此之外，holder还有其他设计考究，这里抛出来大家可以思考下：</p>
<ol>
<li>
<p>为什么holder需要设计成static final类级别变量？</p>
</li>
<li>
<p>ttl变量的存储为什么需要使用WeakHashMap，而不是hashmap或其他？</p>
</li>
</ol>
<p>然后我们再来看异步task转换 TtlRunnable.get(task2) 核心代码实现，代码整体实现相对比较简单，get方法是一个静态工厂方法，主要作用是将业务传入的普通Runnable task装饰成TtlRunable类，并在TtlRunable构造方法中进行线程capture动作(具体实现我们后面再分析)，然后将结果存储到对象属性capturedRef中。</p>
<pre><code class="copyable">@Nullable
    public static TtlRunnable get(@Nullable Runnable runnable, boolean releaseTtlValueReferenceAfterRun, boolean idempotent) &#123;
        if (null == runnable) return null;

        if (runnable instanceof TtlEnhanced) &#123;
            // avoid redundant decoration, and ensure idempotency
            if (idempotent) return (TtlRunnable) runnable;
            else throw new IllegalStateException("Already TtlRunnable!");
        &#125;
        //将入参runnable进行了装饰
        return new TtlRunnable(runnable, releaseTtlValueReferenceAfterRun);
    &#125;
　　
//......
public final class TtlRunnable implements Runnable, TtlWrapper<Runnable>, TtlEnhanced, TtlAttachments &#123;
    private final AtomicReference<Object> capturedRef;
    private final Runnable runnable;
    private final boolean releaseTtlValueReferenceAfterRun;

    private TtlRunnable(@NonNull Runnable runnable, boolean releaseTtlValueReferenceAfterRun) &#123;
        this.capturedRef = new AtomicReference<Object>(capture());
        this.runnable = runnable;
        this.releaseTtlValueReferenceAfterRun = releaseTtlValueReferenceAfterRun;
    &#125;

    /**
     * wrap method &#123;@link Runnable#run()&#125;.
     */
    @Override
    public void run() &#123;
        final Object captured = capturedRef.get();
        if (captured == null || releaseTtlValueReferenceAfterRun && !capturedRef.compareAndSet(captured, null)) &#123;
            throw new IllegalStateException("TTL value reference is released after run!");
        &#125;

        final Object backup = replay(captured);
        try &#123;
            runnable.run();
        &#125; finally &#123;
            restore(backup);
        &#125;
    &#125;　

 　//........   
 ｝
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后是run方法，这也是核心关键的CRR操作了。这里通过模板方法将CRR操作编排在业务逻辑执行的前后了，也即业务逻辑执行前会将capturer的值进行replay恢复，执行后进行复原restore操作。同样这里也有几个问题很值我们思考：</p>
<ol>
<li>
<p>capture操作为什么需要放到TtlRunnable构造方法中，而不能在run方法中？</p>
</li>
<li>
<p>代码中使用了哪两个设计模式，使用设计模式的好处是什么？</p>
</li>
<li>
<p>业务执行完之后为什么还需要restore操作？</p>
</li>
</ol>
<p>接下来，我们再分别对capture、replay、restore方法实现做个一一分析。首先是capture方法，我们可以看到capture操作整体比较简单，主要是将set操作保存到holder变量中的值进行遍历并以Snapshot结构进行存储返回。</p>
<pre><code class="copyable"> /**
         * Capture all &#123;@link TransmittableThreadLocal&#125; and registered &#123;@link ThreadLocal&#125; values in the current thread.
         *
         * @return the captured &#123;@link TransmittableThreadLocal&#125; values
         * @since 2.3.0
         */
        @NonNull
        public static Object capture() &#123;
            return new Snapshot(captureTtlValues(), captureThreadLocalValues());
        &#125;

        private static HashMap<TransmittableThreadLocal<Object>, Object> captureTtlValues() &#123;
            HashMap<TransmittableThreadLocal<Object>, Object> ttl2Value = new HashMap<TransmittableThreadLocal<Object>, Object>();
            for (TransmittableThreadLocal<Object> threadLocal : holder.get().keySet()) &#123;
                ttl2Value.put(threadLocal, threadLocal.copyValue());
            &#125;
            return ttl2Value;
        &#125;

        private static HashMap<ThreadLocal<Object>, Object> captureThreadLocalValues() &#123;
            final HashMap<ThreadLocal<Object>, Object> threadLocal2Value = new HashMap<ThreadLocal<Object>, Object>();
            for (Map.Entry<ThreadLocal<Object>, TtlCopier<Object>> entry : threadLocalHolder.entrySet()) &#123;
                final ThreadLocal<Object> threadLocal = entry.getKey();
                final TtlCopier<Object> copier = entry.getValue();

                threadLocal2Value.put(threadLocal, copier.copy(threadLocal.get()));
            &#125;
            return threadLocal2Value;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个captureThreadLocalValues，主要是用于将一些已有ThreadLocal中的上下文一起复制，已有ThreadLocal需要通过registerThreadLocal方法来单独注册。相关代码如下：</p>
<pre><code class="copyable">public static class Transmitter &#123;
    //....
    
private static volatile WeakHashMap<ThreadLocal<Object>, TtlCopier<Object>> threadLocalHolder = new WeakHashMap<ThreadLocal<Object>, TtlCopier<Object>>();
private static final Object threadLocalHolderUpdateLock = new Object();

    //......
    public static <T> boolean registerThreadLocal(@NonNull ThreadLocal<T> threadLocal, @NonNull TtlCopier<T> copier, boolean force) &#123;
        if (threadLocal instanceof TransmittableThreadLocal) &#123;
            logger.warning("register a TransmittableThreadLocal instance, this is unnecessary!");
            return true;
        &#125;

        synchronized (threadLocalHolderUpdateLock) &#123;
            if (!force && threadLocalHolder.containsKey(threadLocal)) return false;

            WeakHashMap<ThreadLocal<Object>, TtlCopier<Object>> newHolder = new WeakHashMap<ThreadLocal<Object>, TtlCopier<Object>>(threadLocalHolder);
            newHolder.put((ThreadLocal<Object>) threadLocal, (TtlCopier<Object>) copier);
            threadLocalHolder = newHolder;
            return true;
        &#125;
    &#125;
    //......
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里代码有个非常关键的处理，由于WeakHashMap非线程安全，为了避免并发问题安全加上了synchronized锁操作。这里有可以思考下除了synchronized关键字还有什么保障线程安全的方法。另外，实现threadLocal注册时为已经在锁块中了，为什么还要做new copy重新替换操作，这样做目的是什么？大家可以想想看。</p>
<p>最后就是replay和restore方法，整体实现逻辑非常清晰，主要是将captured的值在当前线程ThreadLocal中进行重新赋值初始化，以及业务执行后恢复到原来。这里很佩服作者对不同情况的细致考虑，不是直接将当前holder中的上下文直接备份，而是与之前已capture的内容比较，将业务后set的上下文进行剔除，以免在恢复restore时出现前后不一致的情况。</p>
<pre><code class="copyable">@NonNull
public static Object replay(@NonNull Object captured) &#123;
    final Snapshot capturedSnapshot = (Snapshot) captured;
    return new Snapshot(replayTtlValues(capturedSnapshot.ttl2Value), replayThreadLocalValues(capturedSnapshot.threadLocal2Value));
&#125;

@NonNull
private static HashMap<TransmittableThreadLocal<Object>, Object> replayTtlValues(@NonNull HashMap<TransmittableThreadLocal<Object>, Object> captured) &#123;
    HashMap<TransmittableThreadLocal<Object>, Object> backup = new HashMap<TransmittableThreadLocal<Object>, Object>();

    for (final Iterator<TransmittableThreadLocal<Object>> iterator = holder.get().keySet().iterator(); iterator.hasNext(); ) &#123;
        TransmittableThreadLocal<Object> threadLocal = iterator.next();

        // backup
        backup.put(threadLocal, threadLocal.get());

        // clear the TTL values that is not in captured
        // avoid the extra TTL values after replay when run task
        if (!captured.containsKey(threadLocal)) &#123;
            iterator.remove();
            threadLocal.superRemove();
        &#125;
    &#125;

    // set TTL values to captured
    setTtlValuesTo(captured);

    // call beforeExecute callback
    doExecuteCallback(true);

    return backup;
&#125;

private static void setTtlValuesTo(@NonNull HashMap<TransmittableThreadLocal<Object>, Object> ttlValues) &#123;
    for (Map.Entry<TransmittableThreadLocal<Object>, Object> entry : ttlValues.entrySet()) &#123;
        TransmittableThreadLocal<Object> threadLocal = entry.getKey();
        threadLocal.set(entry.getValue());
    &#125;
&#125;

public static void restore(@NonNull Object backup) &#123;
    final Snapshot backupSnapshot = (Snapshot) backup;
    restoreTtlValues(backupSnapshot.ttl2Value);
    restoreThreadLocalValues(backupSnapshot.threadLocal2Value);
&#125;

private static void restoreTtlValues(@NonNull HashMap<TransmittableThreadLocal<Object>, Object> backup) &#123;
    // call afterExecute callback
    doExecuteCallback(false);

    for (final Iterator<TransmittableThreadLocal<Object>> iterator = holder.get().keySet().iterator(); iterator.hasNext(); ) &#123;
        TransmittableThreadLocal<Object> threadLocal = iterator.next();

        // clear the TTL values that is not in backup
        // avoid the extra TTL values after restore
        if (!backup.containsKey(threadLocal)) &#123;
            iterator.remove();
            threadLocal.superRemove();
        &#125;
    &#125;

    // restore TTL values
    setTtlValuesTo(backup);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>核心代码分析完之后，再来简单总结下项目中学习到的知识点：</p>
<ol>
<li>
<p>对ThreadLocal、InheritableThreadLocal有了更加系统和深入的理解，包括两者继承关系、底层数据结构ThreadLocalMap与Thread关联关系等。</p>
</li>
<li>
<p>面向gc编程(gc相关)、WeakHashMap(Java对象引用类型强、软、弱等)、线程安全、并发等等</p>
</li>
<li>
<p>设计模式相关，装饰模式、工厂、模板方法、代理等</p>
</li>
<li>
<p>TTL虽然代码量不算多，但短小精悍，也处处体现了作者超高的设计和编程能力，每行代码都值得学习和反复琢磨。</p>
</li>
</ol>
<p>我相信通过类似这样的一个项目学习流程下来，把每个环节都能踏踏实实做好，且过程中有贯穿自己思考和理解。相信你一定能把每个项目吃透，并把项目中的每个技术点都牢牢掌握。</p>
<p>最后，我所在团队是淘系技术部淘系架构团队，主要在负责一站式serverless研发平台建设，为业务不断提升研发效率和极致体验。平台已平稳支撑淘系互动、淘宝人生、金币庄园、特价版、闲鱼、拍卖、品牌轻店等多个业务的6.18、双11、双12、春晚等多个大促活动。</p>
<hr>
<p>欢迎加入淘系架构团队，团队成员大牛云集，有阿里移动中间件的创始人员、Dubbo核心成员、更有一群热爱技术，期望用技术推动业务的小伙伴。</p>
<p>淘系架构团队，推进淘系（淘宝、天猫等）架构升级，致力于为淘系、整个集团提供基础核心能力、产品与解决方案：</p>
<p>• 业务高可用的解决方案与核心能力（精细化流量管控Marconi平台：为业务提供自适应流控、隔离与熔断的柔性高可用解决方案，站点高可用：故障自愈、多机房与异地容灾与快速切流恢复</p>
<p>• 一站式serverless研发平台GAIA，为业务提供高效研发效率和极致体验。</p>
<p>• 下一代网络协议QUIC实现与落地</p>
<p>• 移动中间件（API网关MTop、接入层AServer、消息/推送、配置中心等等）</p>
<p>期待一起参与加入淘系基础平台的建设~</p>
<p>简历投递至📮 ：少千　<a href="mailto:zhiheng.gao@alibaba-inc.com">zhiheng.gao@alibaba-inc.com</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            