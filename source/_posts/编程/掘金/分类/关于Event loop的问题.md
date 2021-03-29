
---
title: '关于Event loop的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9871'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 02:09:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=9871'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Event loop即事件循环，就是指浏览器或者Node（JS运行的环境）用来解决JS单线程运行阻塞的问题的一种机制。
关于Event loop,它分为MacroTask（宏任务）和MicroTask（微任务）。</p>
<p>首先，我们来谈一下JS的单线程运行。</p>
<p><strong>何为单线程？</strong></p>
<p>当一个程序运行时，就可以视为一个进程。运行中的程序和程序所需要的资源都是进程，而一个进程一般是由多个线程组成的。<br>
多个线程意味着有多个不同的执行流执行不同的任务。多线程运行时，不是其他线程等待一个执行完，而是各自运行。但是，同时多线程运行时占用的内存偏多，且会出现共享资源争夺的情况，容易造成很多麻烦的Bug。<br>
而单线程是按顺序执行，不需要占用过多的内存资源。</p>
<p><strong>那么为何JS会是单线程呢？</strong></p>
<p>JS从诞生之初就是单线程。阮一峰老师在他的博客中提到：大概是因为不想让浏览器变得像多线程那样复杂，因为多线程需要共享资源、且有可能修改彼此的运行结果，对于一个网络脚本语言来说，太过于复杂了，还是单线程比较适合JS。而Event loop就是用来解决JS单线程运行阻塞、等待时间过长的一种机制。</p>
<h3 data-id="heading-0">宏任务（Macro Task）</h3>
<p>宏任务是由宿主，也就是JS运行的环境（浏览器和Node），发起的。<br>
script代码、setTimeout、setInterval、setImmediate、I/O（Node.js）、UI rending/UI事件都是宏任务的具体事件<br>
在代码中，一般后运行，并会触发新一轮的Tick。</p>
<h3 data-id="heading-1">微任务（Micro Task）</h3>
<p>微任务是由JS引擎发起的。<br>
Promise、MutationObserve、Object.observe（已废弃；Proxy对象替代）、Process.nextTick（Node.js独有）<br>
在代码中，一般会先行运行，并不会触发新一轮的Tick。</p>
<h3 data-id="heading-2">浏览器与Event loop</h3>
<p>程序中，会设置两个线程，一个是负责程序本身的运行，为“主线程”（main thread）；另一个则负责主线程与I/O操作之间的通信，即调用栈（执行栈）call-stack，所有的任务都会放在栈中等待被主线程执行。</p>
<p>在主线程中，最先执行的任务会存储在任务队列中放入执行栈中执行，当任务队列为空时，则会从微任务队列中选择任务放入到任务队列中，直至任务都被完成。执行进入Micro的检查点时，会先设置Micro的检查点为true，当Micro不为空时，选择一个任务task进入队列中，并将其设置为已选择的microtask，运行microtask，将已经执行完的microtask设置为null，清理indexDB事务，重新设置Micro检查点为false,更新界面。</p>
<p>浏览器中Event loop会先检查执行栈，如果执行栈为空，则去执行宏任务，宏任务执行完成之后，会去检查微任务队列，如果不为空，则依次执行微任务，直至微任务执行完成之后再去执行宏任务。</p>
<h3 data-id="heading-3">Node.js与Event loop</h3>
<p>Node中Event loop中的libuv实现的。</p>
<p><strong>什么是libuv？</strong></p>
<p>libuv是一个高性能、事件驱动的异步I/O库。libuv封装了不同平台底层对于<strong>异步I/O模型</strong>的实现。<br>
现阶段的Node提供libuv作为封装层，使Node具备了跨平台的能力。</p>
<p>Node的Event loop被分为6个阶段：</p>
<ul>
<li>
<p>timers：执行setTimeout和setInterval中时间到期满足（达到最快定时器的阈值 - 由于调度会产生一些延时）的callback。</p>
</li>
<li>
<p>pending callback：某些系统操作的回调（例如：TCP错误类型）</p>
</li>
<li>
<p>poll：</p>
<ol>
<li>执行I/O回调</li>
<li>处理轮询队列中的事件</li>
</ol>
<p>如果poll队列不为空，则会循环遍历执行它们的callback队列；如果有setImmediate()需要回调执行，则停止poll阶段进入check阶段执行回调；如果没有setImmediate()，poll将callback放入队列中执行；如果poll为空，则会判断timer是否超时，如果有的话则回到timer。</p>
</li>
<li>
<p>check：如果poll已完成或者闲置并且setImmediate()已排队，则立即执行check阶段。</p>
</li>
<li>
<p>close callback：执行close事件中的callback。</p>
</li>
</ul>
<p><strong>setImmediate()与定时器</strong></p>
<p>setImmediate()在poll阶段执行完成或者闲置之后立即执行，在check阶段<br>
定时器在timer阶段执行</p>
<p><strong>Process.nectTick()</strong></p>
<p>process.nextTick()从技术上讲，并不是事件循环的一部分。在每个阶段完成之后，如果存在nextTick就会清空队列中所有的callback立即执行nextTick。</p>
<h3 data-id="heading-4">浏览器的Event loop与Node中的loop的区别</h3>
<p>Node端的事件循环，MicroTask在事件循环的各个阶段之间执行
浏览器中的时间循环，MicroTask在事件循环的MacroTask执行完之后再执行</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            