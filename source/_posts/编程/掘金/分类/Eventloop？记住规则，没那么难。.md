
---
title: 'Eventloop？记住规则，没那么难。'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/241a16aed7ba4a67baefb0e94d736116~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 18:56:44 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/241a16aed7ba4a67baefb0e94d736116~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>我们都知道 JavaScript 是一门 单线程 的语言：同一时间只能运行一个任务。通常情况下这没什么问题，但是如果你有一个任务需要耗费 30 秒的时间，那其他任务难道都要等它 30 秒么？（由于 JS 运行在浏览器的主线程，所以这 30 秒的时间里，整个页面都会处于卡死状态）</p>
<p>幸运的是，浏览器提供了一些 JS 引擎不具备的功能：Web API。它包括 DOM API，setTimeout，HTTP 请求 等等。这些功能都可以帮助我们处理 异步、非阻塞 的操作。</p>
<h2 data-id="heading-1">什么是Event loop？</h2>
<p>Event Loop 即事件循环，是指浏览器或Node的一种解决Javascript单线程运行时不会阻塞的一种机制，也就是异步的原理。</p>
<h2 data-id="heading-2">为啥要弄懂Event loop？</h2>
<ul>
<li>增加技术深度，也就是懂得Javascript的运行机制。</li>
<li>前端领域技术层出不穷，掌握底层原理可以以不变应万变。</li>
<li>应对大场面试，懂其原理，题目任意发挥。</li>
</ul>
<h2 data-id="heading-3">数据结构前置知识</h2>
<p>堆：利用完全二叉树维护的一组数据，是线性数据结构，相当于一维数组，有唯一后继。</p>
<p>栈：后进先出。类似桶装薯片，包装的时候只能从顶部放入，而吃的时候也只能从顶部拿出。</p>
<p>队列：先进先出。类似排队办理业务，排在最前面的最先办理。</p>
<p>调用栈：本质上当然还是个，它里面装的东西是一个个待执行的<strong>函数</strong>，记住，是函数！先拿两个函数来说：</p>
<ul>
<li>栈空</li>
<li>现在执行到一个 函数A，函数A 入栈</li>
<li>函数A 又调用了 函数B，函数B 入栈</li>
<li>函数B 执行完后 出栈</li>
<li>然后继续执行 函数A，执行完后A也 出栈</li>
<li>栈空</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/241a16aed7ba4a67baefb0e94d736116~tplv-k3u1fbpfcp-watermark.image" alt="调用栈.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">Event loop</h2>
<h3 data-id="heading-5">同步任务、异步任务</h3>
<p>Js单线程分为同步任务和异步任务。</p>
<p>同步任务会在调用栈中按照顺序等待主线程依次执行。</p>
<p>异步任务会在异步任务有了结果后，将注册的回调函数放入任务队列中，等调用栈为空时，会被读取到调用栈中等待主线程执行。</p>
<h3 data-id="heading-6">回调函数</h3>
<p>很多人看到“回调函数”就准备发懵了，但其实很简单。打个比方，有一家旅馆提供叫醒服务，但是要求旅客自己决定叫醒的方法。可以是打客房电话，也可以是派服务员去敲门，睡得死怕耽误事的，还可以要求往自己头上浇盆水。这里，“叫醒的方式”是由旅客决定并告诉旅馆的，旅馆会在第二天早上执行。这个“叫醒的方式”就是回调函数。而旅客告诉旅馆怎么叫醒自己的动作，也就是把回调函数传入库函数的动作，称为注册回调函数（to register a callback function）。</p>
<h3 data-id="heading-7">宏任务、微任务</h3>
<p>在Js中，任务被分为两种，宏任务（Macro Task，Task）和微任务(Micro Task)。</p>
<p>宏任务包括：</p>
<ul>
<li>script全部代码</li>
<li>setTimeout</li>
<li>setInterval</li>
<li>setImmediate</li>
<li>I/O</li>
<li>UI Rendering</li>
</ul>
<p>微任务包括：</p>
<ul>
<li>Process.nextTick(Node 独有)</li>
<li>Promise.then之后的任务</li>
<li>Mutation Observer</li>
</ul>
<p>可以看到，宏任务中既有同步任务，也有异步任务。</p>
<h4 data-id="heading-8">Event Table</h4>
<p>Event Table 可以理解成一张 事件->回调函数 对应表</p>
<p>它就是用来存储 JavaScript 中的异步事件 (request, setTimeout, IO等) 及其对应的回调函数的列表</p>
<h4 data-id="heading-9">Event Queue</h4>
<p>Event Queue 简单理解就是 回调函数 队列，所以它也叫 Callback Queue</p>
<p>当 Event Table 中的事件被触发，事件对应的 回调函数 就会被 push 进这个 Event Queue，然后等待被执行</p>
<h1 data-id="heading-10">Event Loop</h1>
<p>一个流程图秒懂：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a522e2088a84b779303672e9f12ac84~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">Event Loop规则，记住规则，万事easy~</h3>
<ol>
<li>
<p>js执行时，用到了两个数据结构，执行栈（call Stack）和任务队列（Event Queue）（都是软件范畴哦，其实都是数组，只不过按照特性抽象成了栈和队列）。</p>
</li>
<li>
<p>执行之前，首先会按照代码顺序将同步任务会被依次加入执行栈中依次执行，将异步任务分为宏任务和微任务分别放入宏任务队列和微任务队列。</p>
</li>
<li>
<p>在执行栈执行完同步任务（算作第一个宏任务）后，查看执行栈是否为空，如果执行栈为空，检查微任务队列是否为空，如果不为空，会按照先进先出的规则全部执行完微任务后，就会去执行第二个宏任务，每一个宏任务执行完毕后，检查微任务队列是否为空，如果不为空，会按照先进先出的规则全部执行完微任务后，再执行下一个宏任务，如此循环。</p>
</li>
<li>
<p>Promise在.then之前的代码是同步任务，直接执行，.then之后的才是异步任务，也是微任务，需要被放入微任务队列。</p>
</li>
</ol>
<h3 data-id="heading-12">例子-经典面试题，举一反三</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
&#125;, <span class="hljs-number">0</span>);

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
    resolve();
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>)
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">6</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>执行主线程同步任务：Promise.then前面的console.log(2);和 console.log(6)，输出 2 6</li>
<li>setTimeout丢入宏任务队列，Promise.then丢入微任务队列。</li>
<li>因为第1步执行了第一个宏任务，现在开始执行微任务，输出 3 4</li>
<li>执行下一个宏任务：输出 1</li>
</ol>
<p>最终答案;2 6 3 4 1</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
&#125;, <span class="hljs-number">0</span>);

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
        <span class="hljs-keyword">if</span> (i === <span class="hljs-number">10</span>) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>)
        &#125;
        i == <span class="hljs-number">9999</span> && resolve();
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>);
<span class="hljs-comment">// 2 10 3 5 4 1</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            