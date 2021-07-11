
---
title: '揭开Chrome V8垃圾回收机制的面纱'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06cc10052af5475c892196d44dc8d919~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 07:21:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06cc10052af5475c892196d44dc8d919~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>提到垃圾回收机制，我们不免要想到：</p>
<ol>
<li>为什么要进行垃圾回收，要对谁进行垃圾回收？</li>
<li>V8垃圾回收机制的原理是什么？</li>
<li>V8垃圾回收采用了哪些技术来进行实现和优化？</li>
</ol>
<p>看完这篇文章，相信您对这些问题自然会一目了然。</p>
<h2 data-id="heading-0">JavaScript的内存管理决定了谁该被垃圾回收</h2>
<p>基础数据类型：null, undefined, String, Boolean, Number, Symbol, BigInt，按值访问（call by value），值存储在栈内存（Stack）中。</p>
<p>引用数据类型，比如数组，对象，函数等，按引用访问（call by reference），引用/指针存储在栈内存中，引用指向的数据存储在堆内存（Heap）中。 严格来说，对象是按引用访问的，因为数组属于对象，而函数也属于对象。</p>
<p>MDN中的原文就提到，函数是第一类对象。</p>
<blockquote>
<p>In JavaScript, functions are first-class objects, because they can have properties and methods just like any other object. What distinguishes them from other objects is that functions can be called. In brief, they are Function objects.</p>
</blockquote>
<p>对于栈内存，操作系统会自动进行内存分配和内存释放。</p>
<p>而堆内存需要由JS引擎手动进行释放。</p>
<p><strong>问题</strong>：为什么栈的速度比堆快？</p>
<p>答：栈是机器系统提供的数据结构，计算机会在底层对栈提供支持：分配专门的寄存器存放栈的地址，压栈出栈都有专门的指令执行，这就决定了栈的效率比较高。</p>
<p>堆是C/C++函数库提供的，它的机制很复杂。比如：为了分配一块内存，库函数会遵照一定的算法在堆内存中搜索可用的足够大小的连续内存空间来进行分配。</p>
<p>所以，总结两点：</p>
<ol>
<li>
<p>从分配和释放的角度，堆内存的分配/释放都需要调用函数（malloc，free），这花费了一定的时间，而栈不需要。</p>
</li>
<li>
<p>从访问的角度，访问堆的一个具体单元，先从栈中读取指针，然后在根据指针读取堆中的数据；而访问栈只需要访问一次。</p>
</li>
</ol>
<h2 data-id="heading-1">Chrome V8垃圾回收机制</h2>
<p>Chrome V8是JS引擎中的一种。它是用C++编写的开源高性能引擎，由Google丹麦开发，是Google Chrome的一部分，也用于Node.js。</p>
<p>V8将堆分为两类：新生代和老生代。</p>
<p>副垃圾回收器 Minor GC - Scavenge：负责新生代的垃圾回收。</p>
<p>主垃圾回收器 Major GC - Mark-Sweep & Mark-Compact：主要负责整个堆的垃圾回收。 </p>
<h3 data-id="heading-2">Minor GC</h3>
<p>将新生代堆分为两个区，from-space和to-space。</p>
<p>Scavenge算法：</p>
<ol>
<li>标记活动对象和非活动对象</li>
<li>复制from-space的活动对象到to-space的一个连续的内存块里</li>
<li>释放from-space的空间</li>
<li>将from-space和to-space角色互换</li>
<li>更新引用已移动的原始对象的指针。新建的对象会被分配到from-space中的下一个空闲地址</li>
</ol>
<p>新生代还分为Nursery子代和Intermediate子代。给一个对象第一次分配内存时，它会被分配到Nursery子代，如果经过一轮垃圾回收，它有幸存活，那么它就会被移动到Intermediate子代。再经过一轮垃圾回收，它还幸免于难，那么它将会被移动到老生代。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06cc10052af5475c892196d44dc8d919~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当对象在GC中幸存，它们会世代移动。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1274d5b1a1fb4c37b858a44e37af577a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Nursery活动对象移动到To-Space，变成Intermediate。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41e1efe8452749b4b74f000b62d63f03~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Intermediate活动对象移动到老生代，Nursery活动对象移动到To-Space。</p>
<p><strong>问题</strong>：GC如何区分活动对象和非活动对象？</p>
<p>答：对象的可达性（Reachability）。表示从根节点（window，global）的指针开始，向下开始搜索子节点，被搜索到的子节点是可达的，并为其留下标记，然后递归这个搜索过程，直到所有子节点都被遍历完。没有被标记的节点，说明没有从根节点到该节点的引用链，它是垃圾回收器回收的对象。根节点指针指向的对象称之为根集（root set）。</p>
<h3 data-id="heading-3">Major GC</h3>
<p>当老生代中活动对象的大小超出启发式限制（heuristically-derived limit）时，将执行整个堆的垃圾回收工作。</p>
<p>它分为两个步骤：</p>
<p><strong>1. Mark-Sweep</strong></p>
<p>Mark：标记所有的活动对象</p>
<p>Sweep：清理所有的非活动对象，会产生内存碎片空隙</p>
<p>清理非活动对象而遗留的内存间隙会被添加到空闲列表的数据结构中。标记完成后，连续的内存空隙会被添加到合适的空闲列表中，以便分配新对象时，查找到相应的内存空间进行存储。</p>
<p><strong>2. Mark-Compact</strong></p>
<p>目的：解决内存碎片空隙问题</p>
<p>将所有的活动对象移动到空闲的连续内存空间中，完成后，就可以清理掉内存碎片空隙。（实质是 复制-删除）</p>
<h2 data-id="heading-4">Stop-The-World 主线程暂停</h2>
<p>衡量垃圾回收所花费时间的一项重要指标是执行GC时主线程暂停所花费的时间。 </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c7a017265ad451882c35fa4b50b13a4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">Orinoco （V8垃圾回收器）奥利诺科</h2>
<h3 data-id="heading-6">并行（Parallel）</h3>
<p>并行是主线程和辅助线程同时执行大致相同数量工作的地方。</p>
<p>这仍是一种“Stop-The-World”的方法，但现在总的暂停时间是它除以参与线程的数量（外加一些同步开销）。</p>
<p><strong>难点</strong>：没有JavaScript运行时，JavaScript堆是暂停的（原因是没有新建的对象在堆分配空间），因此每一个辅助线程需要确保它能同步访问其他辅助线程可能访问的任何对象。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/535494298df34f2b8a1e11f530fca464~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">增量（Incremental）</h3>
<p>增量是主线程间歇执行GC所需工作总量的一小部分，JavaScript在两个增量工作段之间执行。</p>
<p>这意味着堆的状态已改变，这可能会使以前增量执行的工作无效。</p>
<p>从图中可以看出，这不会减少花费在主线程上的时间（实际上，通常会稍微增加时间），它会随着时间的流逝而扩展。但它仍是解决<strong>主线程延时</strong>的好技术。</p>
<p><strong>优点</strong>：通过允许JavaScript间歇执行，而且还可以继续执行垃圾回收任务，应用程序仍可以响应用户输入并在动画上取得进展。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d7e99c0969a4fafaae354d00346c17a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>增量 = 增量标记 + 懒性清理</p>
<p>增量标记只是对活动对象和非活动对象进行标记，懒性清理用来真正的释放内存。当增量标记完成后，假如当前的可用内存足以让我们快速的执行代码，这时没有必要立即清理内存，可以将清理过程延时一下，让JavaScript逻辑代码先执行，也无需一次性清理完所有的非活动对象，垃圾回收器会按需逐一清理，直到清理完毕。 </p>
<h3 data-id="heading-8">并发（Concurrent）</h3>
<p>并发是指主线程不断的执行JavaScript，而辅助线程则在后台完全执行GC。</p>
<p><strong>难点</strong>：</p>
<ol>
<li>JavaScript堆上的任何内容都可以随时改变，从而使之前所做的工作无效。</li>
<li>可能存在辅助线程和主线程同时读取或修改相同的对象，导致读/写争用的问题。</li>
</ol>
<p><strong>优点</strong>：主线程可以自由执行JavaScript。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cda857a7a5e42a0b042b3ae05f1e6cc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">State of GC in V8</h2>
<h3 data-id="heading-10">Scavenging</h3>
<p>在新生代垃圾回收期间，V8使用并行清理将清理工作分发到多个辅助线程和主线程中。</p>
<p>不论在哪个线程，每个被复制的对象会有一个转发地址，用于更新原始指针，使其指向新的位置。 </p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/934a50423243434283e928082f6f9800~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">Major GC</h3>
<p>V8中，Major GC以并发标记开始。当堆接近动态计算限制时，将启动并发标记任务。当JavaScript在主线程运行时，并发标记完全在后台（辅助线程）进行。在辅助线程进行并发标记的过程中，写屏障（Write Barriers）用于跟踪主线程创建对象的新引用。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/910563c617574bf39d70479ea2fbdba5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">当并发标记完成，或者达到动态分配限制时，主线程执行快速标记终止步骤。主线程暂停在此阶段开始，这代表Major GC的总暂停时间。</p>
<p>主线程再次扫描根集，确保标记了所有的活动对象，然后与许多辅助线程进行压缩和指针更新。主线程在暂停期间启动并发清除任务。他们与并行压缩任务和主线程本身同时运行，即使JavaScript在主线程上运行，它们也可以继续运行。</p>
<h3 data-id="heading-12">空闲时间GC</h3>
<p>V8为嵌入器提供了一种触发垃圾回收的机制。</p>
<p>GC可以发布空闲任务（Idle Tasks），这些是最终会被触发的可选工作。Chrome之类的嵌入器可能有一些空闲时间的概念。比如：在Chrome中，以每秒60帧的速度，浏览器大约需要16.6毫秒来渲染动画的每一帧。如果动画提前完成，Chrome可以选择在下一帧之前的空闲时间内，运行GC创建一些空闲任务。 </p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1933b7fb8064222baf1999c04ad475e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            