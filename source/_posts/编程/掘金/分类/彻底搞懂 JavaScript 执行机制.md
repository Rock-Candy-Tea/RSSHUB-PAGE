
---
title: '彻底搞懂 JavaScript 执行机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18fb013a0e2f4f79aee800abfc93aee2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 18:34:23 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18fb013a0e2f4f79aee800abfc93aee2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">js运行原理与机制</h5>
<blockquote>
<p>不管你是前端新手还是老鸟，在日常的工作或者面试的过程中总会遇到这样的情况：给定的几行代码，写出其输出内容和顺序。所以我们就需要搞懂javascript的运行原理和执行机制</p>
</blockquote>
<h5 data-id="heading-1">前言</h5>
<p>首先，我们先看一道经典的面试题</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'定时器开始啦'</span>)
&#125;);

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve</span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'马上执行for循环啦'</span>);
 <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++)&#123;
  i == <span class="hljs-number">99</span> && resolve();
 &#125;
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行then函数啦'</span>)
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'代码执行结束'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我把这段代码粘贴到chrome执行了一下，输出的结果如图所示</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18fb013a0e2f4f79aee800abfc93aee2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">javascript灵魂三问</h4>
<h5 data-id="heading-3">1、为什么说js是单线程</h5>
<p>JavaScript语言的一大特点就是单线程，也就是说，同一个时间只能做一件事。那么，为什么JavaScript不能有多个线程呢？</p>
<p>技术的出现,都跟现实世界里的应用场景密切相关的。</p>
<p>JavaScript的主要用途是与用户互动，以及操作DOM。这决定了它只能是单线程，否则会带来很复杂的同步问题。</p>
<blockquote>
<p>比如，假定现在同时有两个线程操作同一个DOM元素，一个线程在DOM节点上添加内容，另一个线程删除了这个节点，这时浏览器应该以哪个线程为准？</p>
</blockquote>
<p>所以js就被设计成单线程</p>
<p>HTML5提出Web Worker标准，允许JavaScript脚本创建多个线程，但是子线程完全受主线程控制，且不得操作DOM。这个新标准并没有改变js单线程的本质。</p>
<h5 data-id="heading-4">2、JS为什么需要异步?</h5>
<p>javascript事件循环既然js是单线程，那就像只有一个窗口的银行，客户需要排队一个一个办理业务，同理js任务也要一个一个顺序执行。如果一个任务耗时过长，那么后一个任务也必须等着。</p>
<p>如果JS中不存在异步,只能自上而下执行,如果上一行解析时间很长,那么下面的代码就会被阻塞。
对于用户而言,阻塞就意味着"卡死",这样就导致了很差的用户体验</p>
<p>所以js存在同步任务和异步任务</p>
<blockquote>
<ul>
<li>同步任务：在主线程上排队执行的任务，只有前一个任务执行完毕，才能执行后一个任务。</li>
<li>异步任务：不进入主线程、而进入"任务队列"（task queue）的任务，只有"任务队列"通知主线程，某个异步任务可以执行了，该任务才会进入主线程执行。</li>
</ul>
</blockquote>
<h5 data-id="heading-5">3、js如何实现异步任务？</h5>
<p>既然JS是单线程的,只能在一条线程上执行,又是如何实现的异步呢?</p>
<p>是通过的事件循环(event loop),理解了event loop机制,就理解了JS的执行机制</p>
<h4 data-id="heading-6">执行栈与任务队列</h4>
<p>当javascript代码执行的时候会将不同的变量存于内存中的不同位置：堆（heap）和栈（stack）中来加以区分。其中，堆里存放着一些对象。而栈中则存放着一些基础类型变量以及对象的指针。 但是我们这里说的执行栈和上面这个栈的意义却有些不同。</p>
<blockquote>
<p>执行栈</p>
</blockquote>
<p>当我们调用一个方法的时候，js会生成一个与这个方法对应的执行环境（context），又叫执行上下文。这个执行环境中存在着这个方法的私有作用域，上层作用域的指向，方法的参数，这个作用域中定义的变量以及这个作用域的this对象。 而当一系列方法被依次调用的时候，因为js是单线程的，同一时间只能执行一个方法，于是这些方法被排队在一个单独的地方。这个地方被称为执行栈。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40c23683cb5c4b02bad1ef2bf7ee7eff~tplv-k3u1fbpfcp-watermark.image" alt="v2-2f761eb83b50f53d741e6aa1f15a9db1_b.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>任务队列（Task Queue）</p>
</blockquote>
<p>js的另一大特点是非阻塞，实现这一点的关键在于任务队列</p>
<p>任务队列是先进先出的原则，先进队列的事件先执行，后进队列的事件后执行。</p>
<p>js引擎遇到一个异步任务后并不会一直等待其返回结果，而是会将这个任务挂起（压入到任务队列中），继续执行执行栈中的其他任务。当一个异步任务返回结果后，js会将这个任务加入与当前执行栈不同的另一个队列，我们称之为任务队列。被放入任务队列不会立刻执行其回调，而是等待当前执行栈中的所有任务都执行完毕， 主线程处于闲置状态时，主线程会去查找任务队列是否有任务。如果有，那么主线程会从中取出排在第一位的事件，并把这个任务对应的回调放入执行栈中，然后执行其中的同步代码，如此反复，这样就形成了一个无限的循环。（下图（转引自Philip Roberts的演讲《Help, I'm stuck in an event-loop》）。）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/976e3f743c28429b85860c9a15687403~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中的stack表示我们所说的执行栈，web apis则是代表一些异步事件，而callback queue即事件队列。主线程运行的时候，产生堆（heap）和栈（stack），栈中的代码调用各种外部API，它们在"任务队列"中加入各种事件（click，load，done）。只要栈中的代码执行完毕，主线程就会去读取"任务队列"，依次执行那些事件所对应的回调函数。</p>
<h4 data-id="heading-7">Event Loop事件循环机制</h4>
<p>主线程从"任务队列"中读取事件，这个过程是循环不断的，所以整个的这种运行机制又称为Event Loop（事件循环）。</p>
<p>（1）所有同步任务都在主线程上执行，形成一个执行栈（execution context stack）。</p>
<p>（2）主线程之外，还存在一个"任务队列"（task queue）。只要异步任务有了运行结果，就在"任务队列"之中放置一个事件。</p>
<p>（3）同步和异步任务分别进入不同的执行"场所"，同步的进入主线程，异步的进入Event Table并注册函数。</p>
<p>（4）当指定的事情完成时，Event Table会将这个函数移入Event Queue。</p>
<p>（3）一旦"执行栈"中的所有同步任务执行完毕，系统就会读取"任务队列（event Queue）"的异步任务,如果有就推入主线程中。</p>
<p>（4）主线程不断重复上面的步骤。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8f4fc595b684110aa065eceb329763d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上循环执行,这就是event loop</p>
<h4 data-id="heading-8">宏任务和微任务</h4>
<blockquote>
<p>宏任务（macro task）</p>
</blockquote>
<p>包括整体代码script，setTimeout，setInterval</p>
<blockquote>
<p>微任务（micro-task）</p>
</blockquote>
<p>Promise，process.nextTick</p>
<p>不同类型的任务会进入对应的Event Queue，比如宏任务就会进入到宏任务的事件队列中，微任务就会进入到微任务的事件队列中。</p>
<p>事件循环的顺序，进入整体代码(宏任务)后，开始第一次循环。接着执行所有的微任务。然后再次从宏任务开始，找到其中一个任务队列执行完毕，再执行所有的微任务。</p>
<p>请看网络盗图</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78ad6f5557f848dba1ffcb329b4453d2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照这种分类方式:JS的执行机制是</p>
<ul>
<li>
<p>执行一个宏任务,过程中如果遇到微任务,就将其放到微任务的【事件队列】里</p>
</li>
<li>
<p>当前宏任务执行完成后,会查看微任务的【事件队列】,并将里面全部的微任务依次执行完</p>
</li>
</ul>
<h5 data-id="heading-9">分析面试题</h5>
<p>下面代码是文章开头的面试题：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'定时器开始啦'</span>)
&#125;);

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve</span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'马上执行for循环啦'</span>);
 <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++)&#123;
  i == <span class="hljs-number">99</span> && resolve();
 &#125;
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行then函数啦'</span>)
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'代码执行结束'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先执行script下的宏任务,遇到setTimeout,将其放到宏任务的【队列】里</p>
<p>遇到 new Promise直接执行,打印"马上执行for循环啦"</p>
<p>遇到then方法,是微任务,将其放到微任务的【队列里】</p>
<p>打印 "代码执行结束"</p>
<p>本轮宏任务执行完毕,查看本轮的微任务,发现有一个then方法里的函数, 打印"执行then函数啦"</p>
<p>到此,本轮的event loop 全部完成。</p>
<p>所以最后的执行顺序是【马上执行for循环啦 --- 代码执行结束 --- 执行then函数啦 --- 定时器开始啦】</p>
<h5 data-id="heading-10">写在最后</h5>
<p>(1)js的异步我们从最开头就说javascript是一门单线程语言，不管是什么新框架新语法糖实现的所谓异步，其实都是用同步的方法去模拟的，牢牢把握住单线程这点非常重要。</p>
<p>(2)事件循环Event Loop事件循环是js实现异步的一种方法，也是js的执行机制。</p>
<blockquote>
<p>参考资料</p>
</blockquote>
<p>1、阮一峰老师的JavaScript 运行机制详解：再谈Event Loop：<a href="http://www.ruanyifeng.com/blog/2014/10/event-loop.html" target="_blank" rel="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2014/1…</a>
2、segmentfault 10分钟理解JS引擎的执行机制：<a href="https://segmentfault.com/a/1190000012806637" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p>
<p>如果你觉得对你有帮助，记得点个赞和在看哦。同时也期待大家的留言讨论。</p>
<h3 data-id="heading-11">欢迎关注公众号：javascript艺术</h3></div>  
</div>
            