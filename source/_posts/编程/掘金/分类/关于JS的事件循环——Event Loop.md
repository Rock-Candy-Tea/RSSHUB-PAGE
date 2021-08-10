
---
title: '关于JS的事件循环——Event Loop'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=201'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 01:58:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=201'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>众所周知，JavaScript是一门单线程的语言，虽然HTML5提出了Web Worker标准，允许JavaScript创建多个线程，但是它的子线程却完全受主线控制。且不能用于操作DOM，所以并没有改变JavaScript是单线程语言的本质</p>
<h2 data-id="heading-1">为什么是单线程？</h2>
<p>JavaScript作为一门浏览器的脚本语言，他是用户和浏览器交互的桥梁，其中自然避免不了操作DOM并且渲染DOM这个根本且重要的事，而既然要操作DOM。如果是多线程的话，如果某一时刻，一个线程给一个DOM元素添加一个属性，另一个线程又要删除那个属性时该怎么办呢？要以哪个为主呢？所以它的用途已经决定了它是单线程的本质。</p>
<h2 data-id="heading-2">任务队列</h2>
<p>单线程，这就异味着任务的执行需要一个个执行，而如何保证执行的顺序是可预期的，这时候就要引出任务队列的概念了，既然叫做队列，自然就遵循First-In-First-Out(FIFO)先进先出的原则，最先进入队列的最先执行。</p>
<p>但这里会出现一个问题，如果一些非阻塞性的任务执行需要耗时很久，如（Ajax请求等），需要时间等待才能执行结束的话，此刻控制的CPU就会造成不必要的资源浪费，所以在JavaScript中，任务又被分为了同步任务（synchronous）异步任务（asynchronous）两种</p>
<p>同步任务：会进入JS的主线程，在主线程上执行的任务，只有前一个任务执行完毕才会继续下一个任务</p>
<p>异步任务：异步任务不进入主线程，而是进入Event Table, 满足条件后进入“任务队列”（Task Queue），异步任务的执行，是在异步任务执行有了响应结果之后，在任务队列中推进一个事件，等待“执行栈”中的所有同步任务执行完毕，便读取“任务队列”，看看里面有哪些事件，这些事件对应的异步任务便结束等待，进入执行栈，开始执行</p>
<p>总结起来，异步任务的运行机制便可以如下</p>
<pre><code class="copyable">1. 所有的同步任务都在主线程上执行，形成一个执行栈

2. 主线程之外，会维护一个任务队列，只要异步任务运行有了结果，就在任务队列中放入一个事件

3. 如果执行栈的同步任务执行完毕，系统会读取任务队列，依次执行里面的任务

4. 主线程重复如上的步骤
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">事件循环和任务队列</h2>
<p>任务队列其实是一个事件的队列，也可以理解为成消息队列，IO设备完成一项任务，就在任务队列中添加一个事件，表示相关对应的异步任务可以进入执行栈了。主线程在执行完同步任务后，就会读取任务队列，其实就是读取里面的事件来执行。</p>
<p>而任务队列中的事件，除了一些IO设备的事件之外，还包括一些用户行为产生的事件，如点击，双击，获取焦点等回调，这些回调函数（事件）都会被推进任务队列，等待主线程读取然后依次执行</p>
<p>队列的本质是一个先进先出的数据结构，也就是说执行完的事件就会从队头弹出去，在队列中清空掉，而主线程执行栈的执行，就是读取任务队列中的事件，这个过程是循环不断的，直到队列清空为止，当前的执行环境才会结束，所以这个机制又被称为事件循环(<strong>Event Loop</strong>)</p>
<h2 data-id="heading-4">例子</h2>
<p>下面，我们举个小例子来说明一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span>)
&#125;, <span class="hljs-number">10</span>)

<span class="hljs-comment">// 输出 1， 2, 3， 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子，定时器setTimeout就是一个异步任务，如果剩余的三个console都是同步任务，所以他们会按照JavaScript的运行机制——解释执行，依次进入主线程的执行栈，逐步执行，而setTimeout则会主线程挂起，直到10毫秒后，异步任务结束，便将对应的回调函数（事件）放入事件队列（任务队列）中，由主线程中执行完同步任务后，依次读取。</p>
<p>上面的例子可以稍微改造一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span>)
&#125;, <span class="hljs-number">10</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>)

<span class="hljs-comment">// 输出 1， 2, 3，5, 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个改造后的例子，我们在定时器后面又加了一个console，但是他输出的顺序依然排在了定时器的前面，这更是说明了，主线程会优先读取完所有的同步任务依次执行，结束后才会读取任务队列依次执行。</p>
<h2 data-id="heading-5">宏任务和微任务</h2>
<p>在我的理解中，JS是分为了同步和异步任务，而异步任务又分为两种，一种是宏任务，一种又是微任务，同步任务的执行顺序优先于异步任务，而微任务又优先于宏任务。</p>
<h3 data-id="heading-6">宏任务</h3>






























<table><thead><tr><th>#</th><th>浏览器</th><th>Node</th></tr></thead><tbody><tr><td>setTimeout</td><td>√</td><td>√</td></tr><tr><td>setInterval</td><td>√</td><td>√</td></tr><tr><td>setImmediate</td><td>x</td><td>√</td></tr><tr><td>requestAnimationFrame</td><td>√</td><td>x</td></tr></tbody></table>
<h3 data-id="heading-7">微任务</h3>

























<table><thead><tr><th>#</th><th>浏览器</th><th>Node</th></tr></thead><tbody><tr><td>process.nextTick</td><td>x</td><td>√</td></tr><tr><td>MutationObserver</td><td>√</td><td>x</td></tr><tr><td>Promise.then catch finally</td><td>√</td><td>x</td></tr></tbody></table>
<p>下面，我们再详细举个例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)&#125;, <span class="hljs-number">10</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">r, j</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">6</span>)
    r()
   
  &#125;)
&#125;

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>)
&#125;)

fn().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">7</span>)
&#125;)

<span class="hljs-comment">// 输出</span>
<span class="hljs-comment">// 1, 4, 6, 5, 7, 2, </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上的运行机制，便是先遇到到了代码块，姑且也叫同步任务，输出1，然后遇到宏任务，由主线程挂起，进入到Event Table，说的再细一点，是挂起后，进入了宏任务队列（macrotask queue），再之后又遇到代码块console，输出4，继续往下，声明了fn函数，但是还没调用，再往下，遇到了一个promise.then, 将其放入微任务队列（microtask queue）, 再继续，我们调用了fn函数，进入了fn的执行环境，输出了6，然后调用了resolve，掉任务放进微任务队列，然后退出fn的执行环境。这时候，主线程的同步任务执行结束，开始扫描微任务队列，第一个输出5， 第二个输出了7，再继续，微任务队列被清空，开始进入宏任务队列扫描，输出了2，至此，这段代码便执行结束了。</p>
<p>值得注意的是，process.nextTick 永远大于 promise.then，在Node中，
_tickCallback在每一次执行完TaskQueue中的一个任务后被调用，而这个_tickCallback中实质上干了两件事：</p>
<p>1.nextTickQueue中所有任务执行掉(长度最大1e4，Node版本v6.9.1)</p>
<p>2.第一步执行完后执行_runMicrotasks函数，执行microtask中的部分(promise.then注册的回调)</p>
<p>所以很明显 process.nextTick > promise.then</p>
<p>但是，js和nodejs的event loop又存在于一些差异，到时候再找时间写一篇nodejs的event loop相关的文章吧</p></div>  
</div>
            