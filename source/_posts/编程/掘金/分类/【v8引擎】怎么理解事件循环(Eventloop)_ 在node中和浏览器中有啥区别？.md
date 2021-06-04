
---
title: '【v8引擎】怎么理解事件循环(Eventloop)_ 在node中和浏览器中有啥区别？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/870d2a739821481ea1a2350b6376f4e7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 20:28:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/870d2a739821481ea1a2350b6376f4e7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>本文将给大家分享的是JS中了不起的事件循环机制（event loop）,通过精读可以了解到浏览器中的eventloop和nodejs中的eventloop 各自的特点和二者的区别，这也是笔者专栏原生JS灵魂拷问的第三篇，后续会持续更新，欢迎关注！（篇幅较长，有表达错误欢迎评论区指出和分享。）</p>
<h1 data-id="heading-1">一、什么是eventloop？为啥要去考究它？</h1>
<p>众所周知，JS是一门单线程的脚本语言，而Event Loop即事件循环，就是浏览器或nodejs的一种JavaScript单线程运行时处理各种事件却不会造成阻塞的机制，这也是使用异步的原理。那么JS引擎是如何做到单线程处理同步、异步、计时器各类事件而不会造成阻塞的呢？这就是我们考究Event Loop的意义所在。</p>
<h1 data-id="heading-2">二、基础知识储备</h1>
<h2 data-id="heading-3">进程和线程</h2>
<blockquote>
<p>官方标准：进程是CPU资源分配的最小单位,描述的是CPU在运行指令及加载和保存上下文所需要的时间。线程是CPU调度的最小单位，描述的是执行一段指令所需要的时间。（一个进程可以有多个线程，所以线程是进程中的更小的单位。）</p>
</blockquote>
<p>这里可以用一个实例来帮助理解：以Chrome浏览器为例，当新打开一个tab页面，其实就是创建了一个进程。而在该进程中，会有多个线程的存在：渲染线程、JS引擎线程、HTTP请求线程等。</p>
<h3 data-id="heading-4">多进程和多线程</h3>
<ul>
<li>1、多进程：在同一时间内，同一个计算机系统如果允许两个或两个以上的进程处于运行状态。多进程的好处是可见的：同时可以工作多个进程，并且是互不干扰的，这可以明显地提高引擎的工作效率。</li>
<li>2、多线程：程序中包含多个执行流，即在一个程序中可以同时运行多个不同的线程来执行不同的任务，即允许同时执行多行JS代码。</li>
</ul>
<p><strong>这里有个问题值得我们思考：JS为什么不修改为多线程？JS单线程能够带来什么好处？</strong></p>
<ul>
<li>首先JS单线程带来的效果：</li>
</ul>
<p>JS引擎在JS运行时会阻塞UI渲染（即JS引擎线程工作完，渲染线程才能工作）</p>
<ul>
<li>JS不修改为多线程的原因</li>
</ul>
<p>熟悉JS的人都知道，JS代码是可以修改DOM结构。如果JS改成多线程，就会导致，在JS引擎运行时，UI渲染线程也在工作，就可能导致不安全的渲染UI。</p>
<ul>
<li>JS单线程带来的好处</li>
</ul>
<ol>
<li>节省运行内存</li>
<li>节约上下文切换的时间</li>
</ol>
<h2 data-id="heading-5">微任务（Micro-Task）和宏任务（Macro-Task）</h2>
<p>笔者有特意去查过Microtask和Macrotask的概念，但并未在官方文档找到相关描述，因此，二者的定义也无从得知，下文只能通过实例来理解二者概念。望诸位大佬找到后在评论区告知。</p>
<p>这里可以用银行处理业务为例，可以将<strong>JS引擎比作一个银行业务员</strong>。我们平时去到银行处理业务，首先需要排队拿号，这就是引擎处理线程的任务队列，<strong>每个号对应的人就可以看作一个宏任务</strong>。当叫到号码对应的人时，即引擎开始处理队列中的一个宏任务；而<strong>每个人在窗口可能需要办理多个业务，这些业务其实就是微任务队列</strong>，业务员只有把这些微任务完全处理完，才能继续叫号，处理下一个宏任务。（这里主要是形象化微任务和宏任务的概念，<strong>二者有个共性：都是需要异步执行的任务</strong>）</p>
<ul>
<li><strong>在JS中，哪些属于宏任务？哪些属于微任务？</strong></li>
</ul>
<ol>
<li>Micro-Task：process.nextTick,promise,promise.then,MutationObserver</li>
<li>Macro-Task：script,setTimeout,setInterval,setImmediate,I/O,UI渲染</li>
</ol>
<ul>
<li>这里还需要了解JS中<strong>异步回调</strong>的两种机制</li>
</ul>
<ol>
<li>把异步回调函数封装成一个宏任务，添加到消息队列尾部，当循环系统执行到该任务的时候执行回调函数。</li>
<li>执行时机是在主函数执行结束之后，当前宏任务结束之前执行回调函数，这通常以微任务的形式体现</li>
</ol>
<ul>
<li>微任务就是一个需要异步执行的函数，执行时机是在主函数执行结束之后，当前宏任务结束之前</li>
</ul>
<h1 data-id="heading-6">三、浏览器中的EventLoop</h1>
<h2 data-id="heading-7">1、浏览器中的事件循环机制运作的几个步骤：</h2>
<ul>
<li><strong>消息的添加</strong>：在浏览器中，每当一个事件监听器绑定在该事件上时，一个消息就会被添加到消息队列。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/870d2a739821481ea1a2350b6376f4e7~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件 (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>消息的处理</strong>：一个js运行时包含了一个待处理消息的消息队列，每个消息都关联着一个用以处理这个消息的回调函数。运行时会从最先进入队列的消息开始处理队列中的消息。被处理的消息会被移出队列，再作为输入参数来调用与之关联的函数。调用函数就会创建一个新的栈帧，压入调用栈，函数的处理会一直进行到执行栈为空为止。然后，事件循环才会去处理队列中的下一个消息。</li>
</ul>
<h2 data-id="heading-8">2、举个例子：</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script start'</span>);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout'</span>);
&#125;, <span class="hljs-number">0</span>);

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise1'</span>);
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise2'</span>);
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script end'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">第一次执行</h3>
<blockquote>
<p>执行同步代码，将宏事件和微事件添加到对应的队列。这里先打印script start -> script end ,宏任务队列：setTimeout。微任务队列：promise.then1 , promise.then2。script执行完，执行栈内为空，开始执行微任务队列，将微任务队列中的各项按顺序放入执行栈中执行，直到执行栈中再次为空，此次执行结束。</p>
</blockquote>
<p><strong>所以第一次执行后已打印：script start -> script end ->promise1 -> promise2</strong></p>
<h3 data-id="heading-10">第二次执行</h3>
<blockquote>
<p>将setTimeout从宏任务队列中取出，放入栈中执行。执行完后，栈为空，去微任务队列中查找，微任务队列为空，本次执行结束。</p>
</blockquote>
<p><strong>所以，最终的打印顺序是：script start -> script end ->promise1 -> promise2 -> setTimeout</strong></p>
<h2 data-id="heading-11">3、一图胜千言</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/049c43cdbccb4e7aa7002283ae114f65~tplv-k3u1fbpfcp-watermark.image" alt="16860ae5ad02f993" loading="lazy" referrerpolicy="no-referrer">
（注：动态图出自<a href="https://juejin.cn/post/6844903764202094606#heading-15" target="_blank">该博文</a>，这大佬太牛了，这图很清晰！）</p>
<h2 data-id="heading-12">4、这种事件循环机制的特点及优劣</h2>
<ul>
<li>特性：只有当一个消息完整地执行完成后，其它消息才会被执行。</li>
<li>好处：当一个函数执行时，它不会被抢占，只有在它运行完毕之后才会去运行任何其他的代码，才能修改这个函数操作的数据。</li>
<li>坏处和解决方法：当一个消息需要太长时间才能处理完毕时，Web应用程序就无法处理与用户的交互，例如点击或滚动。为了缓解这个问题，浏览器一般会弹出一个“这个脚本运行时间过长”的对话框。一个良好的习惯是缩短单个消息处理时间，并在可能的情况下将一个消息裁剪成多个消息。</li>
</ul>
<h2 data-id="heading-13">5、总结</h2>
<ul>
<li>浏览器中的事件循环（EventLoop）的执行顺序:
<ol>
<li>首先执行同步代码（script脚本文件），这也属于宏任务</li>
<li>当执行完所有的同步代码后，此时执行栈为空，执行引擎会去查询是否有异步代码需要执行。如果有，执行所有的微任务。</li>
<li>执行完所有的微任务，此时执行栈再次为空时，如果有必要页面的渲染可以发生在这一步。第一次执行结束。</li>
<li>第二次执行开始，执行引擎去查询是否有宏任务需要执行。如果有，执行一个宏任务后，即栈再次为空后，再去查询是否有微任务需要被执行，若有，将微任务全部执行；若无，第二次执行完毕。</li>
<li>再开始下一轮Event-loop，重复上述操作，这就是浏览器中的事件循环机制（Event Loop）</li>
</ol>
</li>
</ul>
<h1 data-id="heading-14">四、nodejs中的EventLoop</h1>
<h2 data-id="heading-15">1、node中事件循环的官方定义</h2>
<blockquote>
<p>事件循环是 Node.js 处理非阻塞 I/O 操作的机制——尽管 JavaScript 是单线程处理的——当有可能的时候，它们会把操作转移到系统内核中去。即使目前大多数内核都是多线程的，它们可在后台处理多种操作。当其中的一个操作完成的时候，内核通知 Node.js 将适合的回调函数添加到 轮询 队列中等待时机执行。</p>
</blockquote>
<blockquote>
<p>Node端的事件循环：Node.js采用V8作为js的解析引擎，而I/O处理方面使用了自己设计的libuv，libuv是一个基于事件驱动的跨平台抽象层，封装了不同操作系统一些底层特性，对外提供统一的API，事件循环机制也是它里面的实现（下文会详细介绍）。</p>
</blockquote>
<h2 data-id="heading-16">2、node中事件循环机制解析</h2>
<p>当Node.js启动后，它会初始化事件循环，处理已提供的输入脚本，它可能会调用一些异步的API、调度定时器、或调用process.nextTick()，然后开始处理事件循环。下面的图表展示的就是事件循环操作顺序的简化模型（每个框都被称为事件循环机制的一个阶段）。由此不难看出，node的事件循环机制分为6个阶段，它们会按照顺序反复运行。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35fb9470894c443f889bd8f68f61e2b1~tplv-k3u1fbpfcp-watermark.image" alt="16841bd9860c1ee9.png" loading="lazy" referrerpolicy="no-referrer">
每个阶段的概述：</p>
<ol>
<li>从外部输入数据并进入到轮询阶段（poll）:获取新的I/O事件，适当的条件下node将阻塞在这里</li>
<li>进入检测阶段（check）:执行setImmediate()的回调</li>
<li>进入关闭事件回调阶段（close callback）:执行socket的close事件回调</li>
<li>进入定时器（timers）阶段:这个阶段执行timer(setTimeout,setInterval)的回调</li>
<li>进入I/O事件回调阶段（I/Ocallbacks）：处理用一些上一轮循环中的少数未执行的I/O回调</li>
<li>进入闲置阶段（idle,prepare）：仅在node内部使用</li>
<li>一轮结束，进入轮询进入下一轮</li>
</ol>
<h2 data-id="heading-17">3、下面将对理解node的事件循环的顺序比较重要的几个阶段进行详细描述：</h2>
<h3 data-id="heading-18">（1）timers</h3>
<ul>
<li>这个阶段中，主要是进行计时器的回调执行。</li>
<li>计时器(setTimeout,setInterval)有两个参数。第一个参数就是它的回调函数，第二个参数是<strong>指定可以执行所提供回调的阈值，而不是用户希望其执行的确切时间。</strong> 即在指定的一段时间间隔后，计时器的回调将尽可能早地执行。但是，系统调度或其他正在运行的回调可能会导致计时器的回调超出指定时间才执行。</li>
</ul>
<h3 data-id="heading-19">（2）poll</h3>
<ul>
<li>该阶段的两个功能：</li>
</ul>
<ol>
<li>计算应该阻塞和轮询的时间</li>
<li>处理轮询队列里的事件</li>
</ol>
<h3 data-id="heading-20">（3）check</h3>
<ul>
<li>
<p>此阶段允许人员在轮询阶段完成后立即执行回调。如果轮询阶段变为空闲状态，并且脚本使用 setImmediate() 后被排列在队列中，则事件循环可能继续到 检查 阶段而不是等待。</p>
</li>
<li>
<p>setImmediate() 实际上是一个在事件循环的单独阶段运行的特殊计时器。它使用一个 libuv API 来安排回调在 轮询 阶段完成后执行。</p>
</li>
<li>
<p>通常，在执行代码时，事件循环最终会命中轮询阶段，在那等待传入连接、请求等。但是，如果回调已使用 setImmediate()调度过，并且轮询阶段变为空闲状态，则它将结束此阶段，并继续到检查阶段而不是继续等待轮询事件。</p>
</li>
</ul>
<p><strong>注意：每个阶段都有各自不同的特点，但相同的是每当事件循环进入一个指定的阶段时，都将先执行特定于该阶段的任何操作，然后执行该队列中的回调，直到队列用尽或最大回调数已执行。当队列已用尽或达到回调限制，事件循环才会移动至下一阶段。</strong></p>
<h2 data-id="heading-21">4、举个例子</h2>
<p>看完上面那么多的相对官方的解析，如果是初学者，大概已经有点懵了，那么又回到最初的问题：<strong>node中的事件循环机制到底是怎么样的顺序执行？</strong> 下面结合一个例子来得出这个问题的答案。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'timer1'</span>)
    <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise1'</span>)
    &#125;)
&#125;, <span class="hljs-number">0</span>)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'timer2'</span>)
    <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise2'</span>)
    &#125;)
&#125;, <span class="hljs-number">0</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要用Node的两个版本来描述运行顺序和结果：</p>
<h3 data-id="heading-22">（1）Node11版本</h3>
<ul>
<li>当Node更新到该版本时，其实可以说node的事件循环机制和浏览器端的相差无几了。在该版本中，一旦执行完一个阶段中的一个宏任务之后，就会立即执行微任务队列，所以它和浏览器端运行的结果是一致的，最后的结果为<code>timer1 -> promise1 -> timer2 -> promise2</code></li>
<li>该版本的运行顺序为：
<ol>
<li>首先执行同步代码（script脚本文件），将2个计时器依次放进timer队列，同步代码执行完毕，调用栈空闲，开始执行任务队列。</li>
<li>进入timers阶段，执行timer1的回调函数，打印timer1，并将peromise.then回调放入微任务队列，timer1执行完毕，调用栈再次为空，立刻执行微任务队列，打印promise1</li>
<li>再执行timer2的回调重复操作2</li>
<li>timers阶段执行完毕，事件循环机制进入下一阶段</li>
</ol>
</li>
</ul>
<h3 data-id="heading-23">（2）node10及之前的版本</h3>
<ul>
<li>在node11之前的版本中，事件循环机制的执行顺序和浏览器端还是有很大区别的，主要体现在node在上述6个阶段中，当每次某一个阶段执行完后，再执行微任务队列，所以执行结果为：<code>timer1 -> timer2 -> promise1 -> promise2</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e9ee8ae663f406694e82fb39ebaab48~tplv-k3u1fbpfcp-watermark.image" alt="1712f2e55556929c.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在该版本的运行顺序为：
<ol>
<li>首先执行同步代码（script脚本文件），将2个计时器依次放进timer队列，同步代码执行完毕，调用栈空闲，开始执行任务队列。</li>
<li>进入timers阶段，依次执行两个计时器的回调，依次打印timer1，timer2；并将promise1.then 和 promise2.then 依次放入微任务队列，到这里timers阶段执行结束</li>
<li>执行微任务队列，依次打印promise1 , promise2</li>
<li>微任务队列执行完后，事件循环进入下一阶段</li>
</ol>
</li>
</ul>
<h1 data-id="heading-24">五、浏览器的EventLoop 和 nodejs的EventLoop的区别是什么？</h1>
<ul>
<li>在Node11之后，其实node端和浏览器端的事件循环机制已经很接近了，如果说要区分的话，我的理解是这二者对每一轮循环的定义还是有差距的：
<ul>
<li>对浏览器端而言，执行一个宏任务，然后执行微任务队列中的微任务，直到全部执行完，这就完成了一轮。下一轮循环从执行下一个宏任务开始。</li>
<li>对Node11而言，Node的libuv引擎（node中事件循环的官方定义中有提及）将事件循环分为 6 个阶段，在这些阶段中都有宏任务的执行，虽然在每次宏任务执行完，都会立刻执行微任务队列（这与浏览端相同），但执行完微任务队列后，继续执行宏任务，再到微任务，当该阶段的宏任务执行结束，进入下一阶段。这些都属于同一轮循环中的，直到把Node的libuv引擎定义的事件循环的 6 个阶段全跑完，这一轮循环才算结束。</li>
</ul>
</li>
</ul>
<h1 data-id="heading-25">六、最后</h1>
<ul>
<li>在该篇文章中，还有一些知识笔者还没有真正的理解，如：
<ol>
<li>对比process.nextTick() 和 setImmediate()</li>
<li>对比setImmediate()和setTimeout()</li>
<li>为什么要使用process.nextTick()</li>
</ol>
等笔者有了自己的理解后，也会在该文章上继续更新。并且，笔者最近在做一件事情：将学习所得通过归纳总结为文章，再通过文章来搭建自己的知识体系，本篇文章被收录到笔者的<a href="https://juejin.cn/column/6961338034788761637" target="_blank">原生JS灵魂发问</a>专栏中，后面也会持续更新，感兴趣的小伙伴可以持续关注，和笔者一起学习，共同进步。此外，若对该篇文章或者笔者的表达有什么建议的话，当然欢迎各位大佬在评论区指出！！！</li>
</ul>
<h1 data-id="heading-26">参考文章</h1>
<ul>
<li><a href="https://juejin.cn/post/6844903761949753352#heading-24" target="_blank">浏览器与Node的事件循环(Event Loop)有何区别?</a></li>
<li><a href="https://juejin.cn/post/6844903827611598862#heading-20" target="_blank">最后一次搞懂 Event Loop</a></li>
<li><a href="https://nodejs.org/zh-cn/docs/guides/event-loop-timers-and-nexttick/#what-is-the-event-loop" target="_blank" rel="nofollow noopener noreferrer">Node.js 事件循环官方文档</a></li>
<li><a href="http://lynnelv.github.io/js-event-loop-nodejs" target="_blank" rel="nofollow noopener noreferrer">深入理解js事件循环机制（Node.js篇）</a></li>
</ul></div>  
</div>
            