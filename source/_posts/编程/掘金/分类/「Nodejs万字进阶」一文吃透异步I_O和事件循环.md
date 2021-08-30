
---
title: '「Nodejs万字进阶」一文吃透异步I_O和事件循环'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03b18f3581404873a0603040da9bfe54~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 22:29:22 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03b18f3581404873a0603040da9bfe54~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一 前言</h2>
<p>本文讲详细讲解 nodejs 中两个比较难以理解的部分<strong>异步I/O</strong>和<strong>事件循环</strong>，对 nodejs 核心知识点，做梳理和补充。</p>
<p>送人玫瑰，手有余香，希望阅读后感觉不错的同学，可以给<strong>点个赞</strong>，鼓励我继续创作前端硬文。</p>
<p>老规矩我们带上疑问开始今天的分析🤔🤔🤔：</p>
<ul>
<li>1 说说 nodejs 的异步I/O ？</li>
<li>2 说说 nodejs 的事件循环机制 ？</li>
<li>3 介绍一下 nodejs 中事件循环的各个阶段 ？</li>
<li>4 nodejs 中 promise 和 nextTick 的区别？</li>
<li>5 nodejs 中 setImmediate 和 setTimeout 区别 ？</li>
<li>6 setTimeout 是精确的吗，什么情况影响 setTimeout 的执行？</li>
<li>7 nodejs 中事件循环和浏览器有什么不同 ？</li>
</ul>
<h2 data-id="heading-1">二 异步I/O</h2>
<h3 data-id="heading-2">概念</h3>
<p>处理器访问任何寄存器和 Cache 等封装以外的数据资源都可以当成 I/O 操作，包括内存，磁盘，显卡等外部设备。<strong>在 Nodejs 中像开发者调用 <code>fs</code> 读取本地文件或网络请求等操作都属于I/O操作。（最普遍抽象 I/O 是文件操作和 TCP/UDP 网络操作）</strong></p>
<p>Nodejs 为单线程的，在单线程模式下，任务都是顺序执行的，但是前面的任务如果用时过长，那么势必会影响到后续任务的进行，通常 I/O 与 cpu 之间的计算是可以并行进行的，但是同步的模式下，I/O的进行会导致后续任务的等待，这样阻塞了任务的执行，也造成了资源不能很好的利用。</p>
<p>为了解决如上的问题，<strong>Nodejs 选择了异步I/O的模式，让单线程不再阻塞，更合理的使用资源。</strong></p>
<h3 data-id="heading-3">如何合理的看待Nodejs中异步I/O</h3>
<p>前端开发者可能更清晰浏览器环境下的 JS 的异步任务，比如发起一次 <code>ajax</code> 请求，正如 ajax 是浏览器提供给 js 执行环境下可以调用的 api 一样 ，在 Nodejs 中提供了 http 模块可以让 js 做相同的事。比如监听｜发送 http 请求，除了 http 之外，nodejs 还有操作本地文件的 fs 文件系统等。</p>
<p>如上 fs http 这些任务在 nodejs 中叫做 I/O 任务。理解了 I/O 任务之后，来分析一下在 Nodejs 中，I/O 任务的两种形态——阻塞和非阻塞。</p>
<h3 data-id="heading-4">nodejs中阻塞和非阻塞IO</h3>
<p>nodejs 对于大部分的 I/O 操作都提供了<strong>阻塞</strong>和<strong>非阻塞</strong>两种用法。阻塞指的是执行 I/O 操作的时候必须等待结果，才往下执行 js 代码。如下一下阻塞代码</p>
<p><strong>阻塞I/O</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* <span class="hljs-doctag">TODO:</span>  阻塞 */</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> data = fs.readFileSync(<span class="hljs-string">'./file.js'</span>);
<span class="hljs-built_in">console</span>.log(data)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>代码阻塞 ：读取同级目录下的 <code>file.js</code> 文件，结果 <code>data</code> 为 <code>buffer</code> 结构，这样当读取过程中，会阻塞代码的执行，所以 <code>console.log(data)</code> 将被阻塞，只有当结果返回的时候，才能正常打印 <code>data</code> 。</li>
<li>异常处理 ：如上操作有一个致命点就是，如果出现了异常，（比如在同级目录下没有 file.js 文件），就会让整个程序报错，接下来的代码讲不会执行。通常需要 try catch来捕获错误边界。代码如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* <span class="hljs-doctag">TODO:</span> 阻塞 - 捕获异常  */</span>
<span class="hljs-keyword">try</span>&#123;
    <span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
    <span class="hljs-keyword">const</span> data = fs.readFileSync(<span class="hljs-string">'./file1.js'</span>);
    <span class="hljs-built_in">console</span>.log(data)
&#125;<span class="hljs-keyword">catch</span>(e)&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发生错误：'</span>,e)
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'正常执行'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如上即便发生了错误，也不会影响到后续代码的执行以及应用程序发生错误导致的退出。</li>
</ul>
<p>阻塞 I/O 造成代码执行等待 I/O 结果，浪费等待时间，CPU 的处理能力得不到充分利用，I/O 失败还会让整整个线程退出。阻塞 I / O 在整个调用栈上示意图如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03b18f3581404873a0603040da9bfe54~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>非阻塞I/O</strong></p>
<p>Nodejs 的非阻塞 I/O 采用的是异步模式，就是刚刚介绍的异步I/O。首先看一下异步模式下的 I/O 操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* <span class="hljs-doctag">TODO:</span> 非阻塞 - 异步 I/O */</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
fs.readFile(<span class="hljs-string">'./file.js'</span>,<span class="hljs-function">(<span class="hljs-params">err,data</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(err,data) <span class="hljs-comment">// null  <Buffer 63 6f 6e 73 6f 6c 65 2e 6c 6f 67 28 27 68 65 6c 6c 6f 2c 77 6f 72 6c 64 27 29></span>
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>) <span class="hljs-comment">// 111 先被打印～</span>

fs.readFile(<span class="hljs-string">'./file1.js'</span>,<span class="hljs-function">(<span class="hljs-params">err,data</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(err,data) <span class="hljs-comment">// 保存  [ no such file or directory, open './file1.js'] ，找不到文件。</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>回调 callback 被异步执行，返回的第一个参数是错误信息，如果没有错误，那么返回 <code>null</code> ，第二个参数为 <code>fs.readFile</code> 执行得到的真正内容。</li>
<li>这种异步的形式可以会优雅的捕获到执行 I/O 中出现的错误，比如说如上当读取 <code>file1.js</code> 文件时候，出现了找不到对应文件的异常行为，会直接通过第一个参数形式传递到 callback 中。</li>
</ul>
<p>比如如上的 callback ，作为一个异步回调函数，就像 setTimeout(fn) 的 fn 一样，不会阻塞代码执行。会在得到结果后触发，对于 Nodejs 异步执行 I/O 回调的细节，接下来会慢慢剖析。</p>
<p>对于异步 I/O 的处理， Nodejs 内部使用了线程池来处理异步 I/O 任务，线程池中会有多个 I/O 线程来同时处理异步的 I/O 操作，比如如上的的例子中，在整个 I/O 模型中会这样。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6254615ccc9c4a29a4523b2ccc5c7580~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来将一起探索一下异步 I/O 执行过程。</p>
<h3 data-id="heading-5">事件循环</h3>
<p>和浏览器一样，Nodejs 也有自身的执行模型——事件循环（ eventLoop ），事件循环的执行模型受到宿主环境的影响，它不属于 javascript 执行引擎（ 例如 v8 ）的一部分，这就导致了不同宿主环境下事件循环模式和机制可能不同，直观的体现就是 Nodejs 和浏览器环境下对微任务（ microtask ）和宏任务（ macrotask ）处理存在差异。对于 Nodejs 的事件循环及其每一个阶段，接下来会详细探讨。</p>
<p>Nodejs 的事件循环有多个阶段，其中有一个专门处理 I/O 回调的阶段，每一个执行阶段我们可以称之为 <code>Tick</code> ， 每一个 <code>Tick</code> 都会查询是否还有事件以及关联的回调函数 ，如上异步 I/O 的回调函数，会在 I/O 处理阶段检查当前 I/O 是否完成，如果完成，那么执行对应的 I/O 回调函数，那么这个检查 I/O 是否完成的观察者我们称之为 I/O 观察者。</p>
<h3 data-id="heading-6">观察者</h3>
<p>如上提到了 I/O 观察者的概念，也讲了 Nodejs 中会有多个阶段，事实上每一个阶段都有一个或者多个对应的观察者，它们的工作很明确就是在每一次对应的 Tick 过程中，对应的观察者查找有没有对应的事件执行，如果有，那么取出来执行。</p>
<p>浏览器的事件来源于用户的交互和一些网络请求比如 <code>ajax</code> 等， <code>Nodejs</code> 中，事件来源于网络请求 <code>http</code> ，文件 I/O 等，这些事件都有对应的观察者，我这里枚举出一些重要的观察者。</p>
<ul>
<li>文件 I/O 操作      —— I/O 观察者；</li>
<li>网络 I/O 操作      —— 网络 I/O 观察者；</li>
<li>process.nextTick  —— idle 观察者</li>
<li>setImmediate      —— check 观察者</li>
<li>setTimeout/setInterval —— 延时器观察者</li>
<li>...</li>
</ul>
<p>在 Nodejs 中，对应观察者接收对应类型的事件，事件循环过程中，会向这些观察者询问有没有该执行的任务，如果有，那么观察者会取出任务，交给事件循环去执行。</p>
<h3 data-id="heading-7">请求对象与线程池</h3>
<p>从 <code>JavaScript</code> 调用到计算机系统执行完 I/O 回调，<strong>请求对象</strong>充当着很重要的作用，我们还是以一次异步 I/O 操作为例</p>
<p><strong>请求对象：</strong> 比如之前调用 <code>fs.readFile</code> ，本质上调用 <code>libuv</code> 上的方法创建一个请求对象。这个请求对象上保留着此次 I/O 请求的信息，包括此次 I/O 的主体和回调函数等。然后异步调用的第一阶段就完成了，JavaScript 会继续往下执行执行栈上的代码逻辑，当前的 I/O 操作将以请求对象的形式放入到线程池中，等待执行。达到了异步 I/O 的目的。</p>
<p><strong>线程池：</strong> Nodejs 的线程池在 Windows 下有内核（ IOCP ）提供，在 Unix 系统中由 <code>libuv</code> 自行实现， 线程池用来执行部分的 I/O （系统文件的操作），线程池大小默认为 4 ，多个文件系统操作的请求可能阻塞到一个线程中。那么线程池里面的 I/O 操作是怎么执行的呢？ 上一步说到，一次异步 I/O 会把请求对象放在线程池中，首先会判断当前线程池是否有可用的线程，如果线程可用，那么会执行请求对象的 I/O 操作，并把执行后的结果返回给请求对象。在事件循环中的 I/O 处理阶段，I/O 观察者会获取到已经完成的 I/O 对象，然后取出回调函数和结果调用执行。<strong>I/O 回调函数就这样执行，而且在回调函数的参数重获取到结果。</strong></p>
<h3 data-id="heading-8">异步 I/O 操作机制</h3>
<p>上述讲了整个异步 I/O 的执行流程，从一个异步 I/O 的触发，到 I/O 回调到执行。<strong>事件循环</strong> ，<strong>观察者</strong> ，<strong>请求对象</strong> ，<strong>线程池</strong> 构成了整个异步 I/O 执行模型。</p>
<p>用一幅图表示四者的关系：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d885c28bf5f450c97f543232b155000~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结上述过程：</p>
<ul>
<li>
<p>第一阶段：每一次<strong>异步 I/O 的调用</strong>，首先在 nodejs 底层设置请求参数和回调函 callback，形成<strong>请求对象</strong>。</p>
</li>
<li>
<p>第二阶段：形成的请求对象，会被放入<strong>线程池</strong>，如果线程池有空闲的 I/O 线程，会执行此次 I/O 任务，得到结果。</p>
</li>
<li>
<p>第三阶段：<strong>事件循环</strong>中 <strong>I/O 观察者</strong>，会从请求对象中找到已经得到结果的 I/O 请求对象，取出结果和回调函数，将回调函数放入事件循环中，执行回调，完成整个异步 I/O 任务。</p>
</li>
<li>
<p>对于如何感知异步 I/O 任务执行完毕的？以及如何获取完成的任务的呢？ libuv 作为中间层， 在不同平台上，采用手段不同，在 unix 下通过 epoll 轮询，在 Windows 下通过内核（ IOCP ）来实现 ，FreeBSD 下通过 kqueue 实现。</p>
</li>
</ul>
<h2 data-id="heading-9">三 事件循环</h2>
<blockquote>
<p>事件循环机制由宿主环境实现</p>
</blockquote>
<p>上述中已经提及了事件循环不是 JavaScript 引擎的一部分 ，事件循环机制由宿主环境实现，所以不同宿主环境下事件循环不同 ，不同宿主环境指的是浏览器环境还是 nodejs 环境 ，但在不同操作系统中，nodejs 的宿主环境也是不同的，接下来用一幅图描述一下 Nodejs 中的事件循环和 javascript 引擎之间的关系。</p>
<p>以 libuv 下 nodejs 的事件循环为参考，关系如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4629895edd4f4f458777239f7bf255ed~tplv-k3u1fbpfcp-watermark.image" alt="10.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以浏览器下 javaScript 的事件循环为参考，关系如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb66e8c9745c4b0ab6657d396dcf4ef9~tplv-k3u1fbpfcp-watermark.image" alt="11.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>事件循环本质上就像一个 while 循环，如下所示，我来用一段代码模拟事件循环的执行流程。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> queue = [ ... ]   <span class="hljs-comment">// queue 里面放着待处理事件</span>
<span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>)&#123;
    <span class="hljs-comment">//开始循环</span>
    <span class="hljs-comment">//执行 queue 中的任务</span>
    <span class="hljs-comment">//....</span>

    <span class="hljs-keyword">if</span>(queue.length ===<span class="hljs-number">0</span>)&#123;
       <span class="hljs-keyword">return</span> <span class="hljs-comment">// 退出进程</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Nodejs 启动后，就像创建一个 while 循环一样，<code>queue</code> 里面放着待处理的事件，每一次循环过程中，如果还有事件，那么取出事件，执行事件，如果存在事件关联的回调函数，那么执行回调函数，然后开始下一次循环。</li>
<li>如果循环体中没有事件，那么将退出进程。</li>
</ul>
<p>我总结了流程图如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c21d0a8093f84ea28734e724f7c158b8~tplv-k3u1fbpfcp-watermark.image" alt="4.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么如何事件循环是如何处理这些任务的呢？我们列出 Nodejs 中一些常用的事件任务：</p>
<ul>
<li><code>setTimeout</code> 或 <code>setInterval</code> 延时器计时器。</li>
<li>异步 I/O 任务：文件任务 ，网络请求等。</li>
<li><code>setImmediate</code> 任务。</li>
<li><code>process.nextTick</code> 任务。</li>
<li><code>Promise</code> 微任务。</li>
</ul>
<p>接下来会一一讲到 ，这些任务的原理以及 nodejs 是如何处理这些任务的。</p>
<h3 data-id="heading-10">1 事件循环阶段</h3>
<p>对于不同的事件任务，会在不同的事件循环阶段执行。根据 nodejs 官方文档，在通常情况下，nodejs 中的事件循环根据不同的操作系统可能存在特殊的阶段，但总体是可以分为以下 6 个阶段 （代码块的六个阶段） ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
   ┌───────────────────────────┐
┌─>│           timers          │     -> 定时器，延时器的执行    
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │     pending callbacks     │     -> i/o
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │       idle, prepare       │
│  └─────────────┬─────────────┘      ┌───────────────┐
│  ┌─────────────┴─────────────┐      │   incoming:   │
│  │           poll            │<─────┤  connections, │
│  └─────────────┬─────────────┘      │   data, etc.  │
│  ┌─────────────┴─────────────┐      └───────────────┘
│  │           check           │
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
└──┤      close callbacks      │
   └───────────────────────────┘
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>第一阶段： <strong><code>timer</code></strong> ，timer 阶段主要做的事是，执行 <code>setTimeout</code> 或 <code>setInterval</code> 注册的回调函数。</p>
</li>
<li>
<p>第二阶段：<strong>pending callback</strong> ，大部分 I/O 回调任务都是在 poll 阶段执行的，但是也会存在一些上一次事件循环遗留的被延时的 I/O 回调函数，那么此阶段就是为了调用之前事件循环延迟执行的 I/O 回调函数。</p>
</li>
<li>
<p>第三阶段：<strong>idle prepare</strong> 阶段，仅用于 nodejs 内部模块的使用。</p>
</li>
<li>
<p>第四阶段：<strong>poll</strong> 轮询阶段，这个阶段主要做两件事，一这个阶段会执行异步 I/O 的回调函数； 二 计算当前轮询阶段阻塞后续阶段的时间。</p>
</li>
<li>
<p>第五阶段：<strong>check阶段</strong>，当 poll 阶段回调函数队列为空的时候，开始进入 check 阶段，主要执行 <code>setImmediate</code> 回调函数。</p>
</li>
<li>
<p>第六阶段：<strong>close阶段</strong>，执行注册 <code>close</code> 事件的回调函数。</p>
</li>
</ul>
<p>对于每一个阶段的执行特点和对应的事件任务，我接下来会详细剖析。我们看一下六个阶段在底层源码中是怎么样体现的。</p>
<p>我们看一下 <code>libuv</code> 下 nodejs 的事件循环的源代码（在 <code>unix</code> 和 <code>win</code> 有点差别，不过不影响流程，这里以 unix 为例子。）：</p>
<blockquote>
<p>libuv/src/unix/core.c</p>
</blockquote>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_run</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, uv_run_mode mode)</span> </span>&#123;
  <span class="hljs-comment">// 省去之前的流程。</span>
  <span class="hljs-keyword">while</span> (r != <span class="hljs-number">0</span> && loop->stop_flag == <span class="hljs-number">0</span>) &#123;

    <span class="hljs-comment">/* 更新事件循环的时间 */</span> 
    <span class="hljs-built_in">uv__update_time</span>(loop);

    <span class="hljs-comment">/*第一阶段： timer 阶段执行  */</span>
    <span class="hljs-built_in">uv__run_timers</span>(loop);

    <span class="hljs-comment">/*第二阶段： pending 阶段 */</span>
    ran_pending = <span class="hljs-built_in">uv__run_pending</span>(loop);

    <span class="hljs-comment">/*第三阶段： idle prepare 阶段 */</span>
    <span class="hljs-built_in">uv__run_idle</span>(loop);
    <span class="hljs-built_in">uv__run_prepare</span>(loop);

    timeout = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">if</span> ((mode == UV_RUN_ONCE && !ran_pending) || mode == UV_RUN_DEFAULT)
     <span class="hljs-comment">/* 计算 timeout 时间  */</span>
      timeout = <span class="hljs-built_in">uv_backend_timeout</span>(loop);
    
    <span class="hljs-comment">/* 第四阶段：poll 阶段 */</span>
    <span class="hljs-built_in">uv__io_poll</span>(loop, timeout);

    <span class="hljs-comment">/* 第五阶段：check 阶段 */</span>
    <span class="hljs-built_in">uv__run_check</span>(loop);
    <span class="hljs-comment">/* 第六阶段： close 阶段  */</span>
    <span class="hljs-built_in">uv__run_closing_handles</span>(loop);
    <span class="hljs-comment">/* 判断当前线程还有任务 */</span> 
     r = <span class="hljs-built_in">uv__loop_alive</span>(loop);

    <span class="hljs-comment">/* 省去之后的流程 */</span>
  &#125;
  <span class="hljs-keyword">return</span> r;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>我们看到六个阶段是按序执行的，只有完成上一阶段的任务，才能进行下一阶段</li>
<li>当 <code>uv__loop_alive</code> 判断当前事件循环没有任务，那么退出线程。</li>
</ul>
<h3 data-id="heading-11">2 任务队列</h3>
<p>在整个事件循环过程中，有四个队列（<strong>实际的数据结构不是队列</strong>）是在 libuv 的事件循环中进行的，还有两个队列是在 nodejs 中执行的分别是 <strong>promise 队列</strong> 和 <strong>nextTick</strong> 队列。</p>
<blockquote>
<p>在 NodeJS 中不止一个队列，不同类型的事件在它们自己的队列中入队。在处理完一个阶段后，移向下一个阶段之前，事件循环将会处理两个中间队列，直到两个中间队列为空。</p>
</blockquote>
<h4 data-id="heading-12">libuv 处理任务队列</h4>
<p>事件循环的每一个阶段，都会执行对应任务队列里面的内容。</p>
<ul>
<li>
<p>timer 队列（ <strong>PriorityQueue</strong> ）：本质上的数据结构是<strong>二叉最小堆</strong>，二叉最小堆的根节点获取最近的时间线上的 timer 对应的回调函数。</p>
</li>
<li>
<p>I/O 事件队列：存放 I/O 任务。</p>
</li>
<li>
<p>Immediate 队列（ <strong>ImmediateList</strong> ）：多个 Immediate ，node 层用链表数据结构储存。</p>
</li>
<li>
<p>关闭回调事件队列：放置待 close 的回调函数。</p>
</li>
</ul>
<h4 data-id="heading-13">非 libuv 中间队列</h4>
<ul>
<li><strong>nextTick</strong> 队列 ： 存放 nextTick 的回调函数。这个是在 nodejs 中特有的。</li>
<li><strong>Microtasks</strong> 微队列 Promise ： 存放 promise 的回调函数。</li>
</ul>
<p>中间队列的执行特点：</p>
<ul>
<li>
<p>首先要明白两个中间队列并非在 libuv 中被执行，它们都是在 nodejs 层执行的，在 libuv 层处理每一个阶段的任务之后，会和 node 层进行通讯，那么会优先处理两个队列中的任务。</p>
</li>
<li>
<p>nextTick 任务的优先级要大于 Microtasks 任务中的 Promise 回调。也就是说 node 会首先清空 nextTick 中的任务，然后才是 Promise 中的任务。为了验证这个结论，例举一个打印结果的题目如下：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* <span class="hljs-doctag">TODO:</span> 打印顺序  */</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout 执行'</span>)
&#125;,<span class="hljs-number">0</span>)

<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>)=></span>&#123;
     <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Promise执行'</span>)
     resolve()
&#125;)
p.then(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Promise 回调执行'</span>)
&#125;)

process.nextTick(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'nextTick 执行'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'代码执行完毕'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码块中的 nodejs 中的执行顺序是什么？</p>
<p>效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7e291478d4845a79c40f3e39b142372~tplv-k3u1fbpfcp-watermark.image" alt="7.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打印结果：Promise执行 -> 代码执行完毕 -> nextTick 执行 -> Promise 回调执行 -> setTimeout 执行</p>
<p>解释：很好理解为什么这么打印，在主代码事件循环中，<code> Promise执行</code> 和 <code>代码执行完毕</code> 最先被打印，nextTick 被放入 nextTick 队列中，Promise 回调放入 Microtasks 队列中，setTimeout 被放入 timer 堆中。接下来主循环完成，开始清空两个队列中的内容，首先清空 nextTick 队列，<code>nextTick 执行</code> 被打印，接下来清空 Microtasks 队列，<code>Promise 回调执行</code> 被打印，最后再判断事件循环 loop 中还有 timer 任务，那么开启新的事件循环 ，首先执行，timer 任务，<code>setTimeout 执行</code>被打印。 整个流程完毕。</p>
<ul>
<li>无论是 nextTick 的任务，还是 promise 中的任务， <strong>两个任务中的代码会阻塞事件循环的有序进行</strong>，导致 I/O 饿死的情况发生，所以需要谨慎处理两个任务中的逻辑。比如如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* <span class="hljs-doctag">TODO:</span> 阻塞 I/O 情况 */</span>
process.nextTick(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">const</span> now = +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
    <span class="hljs-comment">/* 阻塞代码三秒钟 */</span>
    <span class="hljs-keyword">while</span>( +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() < now + <span class="hljs-number">3000</span> )&#123;&#125;
&#125;)

fs.readFile(<span class="hljs-string">'./file.js'</span>,<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I/O: file '</span>)
&#125;)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout: '</span>)
&#125;, <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果：</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4eb41fb465c94979937592bab8b8d10f~tplv-k3u1fbpfcp-watermark.image" alt="17.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>三秒钟， 事件循环中的 timer 任务和 I/O 任务，才被有序执行。也就是说 <code>nextTick</code> 中的代码，阻塞了事件循环的有序进行。</li>
</ul>
<h3 data-id="heading-14">3 事件循环流程图</h3>
<p>接下来用流程图，表示事件循环的六大阶段的执行顺序，以及两个优先队列的执行逻辑。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/154c4b6a120a40f4a58f396a865db71c~tplv-k3u1fbpfcp-watermark.image" alt="6.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">4 timer 阶段 ->  计时器 timer / 延时器 interval</h3>
<p><strong>延时器计时器观察者（Expired timers and intervals）</strong>：延时器计时器观察者用来检查通过 <code>setTimeout</code> 或 <code>setInterval</code>创建的异步任务，内部原理和异步 I/O 相似，不过定期器/延时器内部实现没有用线程池。通过<code>setTimeout</code> 或 <code>setInterval</code>定时器对象会被插入到延时器计时器观察者内部的二叉最小堆中，每次事件循环过程中，会从二叉最小堆顶部取出计时器对象，判断 timer/interval 是否过期，如果有，然后调用它，出队。再检查当前队列的第一个，直到没有过期的，移到下一个阶段。</p>
<h4 data-id="heading-16">libuv 层如何处理 timer</h4>
<p>首先一起看一下 libuv 层是如何处理的 timer</p>
<blockquote>
<p>libuv/src/timer.c</p>
</blockquote>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">uv__run_timers</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">heap_node</span>* <span class="hljs-title">heap_node</span>;</span>
  <span class="hljs-keyword">uv_timer_t</span>* handle;

  <span class="hljs-keyword">for</span> (;;) &#123;
    <span class="hljs-comment">/* 找到 loop 中 timer_heap 中的根节点 （ 值最小 ） */</span>  
    heap_node = <span class="hljs-built_in">heap_min</span>((struct heap*) &loop->timer_heap);
    <span class="hljs-comment">/*  */</span>
    <span class="hljs-keyword">if</span> (heap_node == <span class="hljs-literal">NULL</span>)
      <span class="hljs-keyword">break</span>;

    handle = <span class="hljs-built_in">container_of</span>(heap_node, <span class="hljs-keyword">uv_timer_t</span>, heap_node);
    <span class="hljs-keyword">if</span> (handle->timeout > loop->time)
      <span class="hljs-comment">/*  执行时间大于事件循环事件，那么不需要在此次 loop 中执行  */</span>
      <span class="hljs-keyword">break</span>;

    <span class="hljs-built_in">uv_timer_stop</span>(handle);
    <span class="hljs-built_in">uv_timer_again</span>(handle);
    handle-><span class="hljs-built_in">timer_cb</span>(handle);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如上 handle timeout 可以理解成过期时间，也就是计时器回到函数的执行时间。</li>
<li>当 timeout 大于当前事件循环的开始时间时，即表示还没有到执行时机，回调函数还不应该被执行。那么根据二叉最小堆的性质，父节点始终比子节点小，那么根节点的时间节点都不满足执行时机的话，其他的 timer 也不满足执行时间。此时，退出 timer 阶段的回调函数执行，直接进入事件循环下一阶段。</li>
<li>当过期时间小于当前事件循环 tick 的开始时间时，表示至少存在一个过期的计时器，那么循环迭代计时器最小堆的根节点，并调用该计时器所对应的回调函数。每次循环迭代时都会更新最小堆的根节点为最近时间节点的计时器。</li>
</ul>
<p>如上是 timer 阶段在 libuv 中执行特点。接下里分析一下 node 中是如何处理定时器延时器的。</p>
<h4 data-id="heading-17">node 层如何处理 timer</h4>
<p>在 Nodejs 中 <code>setTimeout</code> 和 <code>setInterval</code> 是 nodejs 自己实现的，来一起看一下实现细节：</p>
<blockquote>
<p>node/lib/timers.js</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setTimeout</span>(<span class="hljs-params">callback，after</span>)</span>&#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-comment">/* 判断参数逻辑 */</span>
    <span class="hljs-comment">//..</span>
    <span class="hljs-comment">/* 创建一个 timer 观察者 */</span>
    <span class="hljs-keyword">const</span> timeout = <span class="hljs-keyword">new</span> Timeout(callback, after, args, <span class="hljs-literal">false</span>, <span class="hljs-literal">true</span>);
    <span class="hljs-comment">/* 将 timer 观察者插入到 timer 堆中  */</span>
    insert(timeout, timeout._idleTimeout);

    <span class="hljs-keyword">return</span> timeout;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>setTimeout： 逻辑很简单，就是创建一个 timer 时间观察者，然后放入计时器堆中。</li>
</ul>
<p>那么 Timeout 做了些什么呢？</p>
<blockquote>
<p>node/lib/internal/timers.js</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Timeout</span>(<span class="hljs-params">callback, after, args, isRepeat, isRefed</span>) </span>&#123;
  after *= <span class="hljs-number">1</span> 
  <span class="hljs-keyword">if</span> (!(after >= <span class="hljs-number">1</span> && after <= <span class="hljs-number">2</span> ** <span class="hljs-number">31</span> - <span class="hljs-number">1</span>)) &#123;
    after = <span class="hljs-number">1</span> <span class="hljs-comment">// 如果延时器 timeout 为 0 ，或者是大于 2 ** 31 - 1 ，那么设置成 1 </span>
  &#125;
  <span class="hljs-built_in">this</span>._idleTimeout = after; <span class="hljs-comment">// 延时时间 </span>
  <span class="hljs-built_in">this</span>._idlePrev = <span class="hljs-built_in">this</span>;
  <span class="hljs-built_in">this</span>._idleNext = <span class="hljs-built_in">this</span>;
  <span class="hljs-built_in">this</span>._idleStart = <span class="hljs-literal">null</span>;
  <span class="hljs-built_in">this</span>._onTimeout = <span class="hljs-literal">null</span>;
  <span class="hljs-built_in">this</span>._onTimeout = callback; <span class="hljs-comment">// 回调函数</span>
  <span class="hljs-built_in">this</span>._timerArgs = args;
  <span class="hljs-built_in">this</span>._repeat = isRepeat ? after : <span class="hljs-literal">null</span>;
  <span class="hljs-built_in">this</span>._destroyed = <span class="hljs-literal">false</span>;  

  initAsyncResource(<span class="hljs-built_in">this</span>, <span class="hljs-string">'Timeout'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在 nodejs 中无论 setTimeout 还是 setInterval 本质上都是 Timeout 类。超出最大时间阀 <code>2 ** 31 - 1</code> 或者 <code>setTimeout(callback, 0)</code> ，_idleTimeout 会被设置成 1 ，转换为 setTimeout(callback, 1) 来执行。</li>
</ul>
<h4 data-id="heading-18">timer 处理流程图</h4>
<p>用一副流程图描述一下，我们创建一个 timer ，再到 timer 在事件循环里面执行的流程。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e810db7d95cf43229f874145a8d57359~tplv-k3u1fbpfcp-watermark.image" alt="9.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-19">timer 特性</h4>
<p>这里有两点需要注意：</p>
<ul>
<li><strong>执行机制</strong> ：延时器计时器观察者，每一次都会执行一个，执行一个之后会清空 nextTick 和 Promise， 过期时间是决定两者是否执行的重要因素，还有一点 poll 会计算阻塞 timer 执行的时间，对 timer 阶段任务的执行也有很重要的影响。</li>
</ul>
<p>验证结论一次执行一个 timer 任务 ，先来看一段代码片段：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout1:'</span>)
    process.nextTick(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'nextTick'</span>)
    &#125;)
&#125;,<span class="hljs-number">0</span>)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout2:'</span>)
&#125;,<span class="hljs-number">0</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b2295a542f44969a5bf5799c22c8eba~tplv-k3u1fbpfcp-watermark.image" alt="5.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>nextTick 队列是在事件循环的每一阶段结束执行的，两个延时器的阀值都是 0 ，如果在 timer 阶段一次性执行完，过期任务的话，那么打印 setTimeout1  -> setTimeout2 -> nextTick ，实际上先执行一个 timer 任务，然后执行 nextTick 任务，最后再执行下一个 timer 任务。</p>
<ul>
<li>
<p><strong>精度问题</strong> ：关于 setTimeout 的计数器问题，计时器并非精确的，尽管在 nodejs 的事件循环非常的快，但是从延时器 timeout 类的创建，会占用一些事件，再到上下文执行， I/O 的执行，nextTick 队列执行，Microtasks 执行，都会阻塞延时器的执行。甚至在检查 timer 过期的时候，也会消耗一些 cpu 时间。</p>
</li>
<li>
<p><strong>性能问题</strong> ：如果想用 setTimeout(fn,0) 来执行一些非立即调用的任务，那么性能上不如 <code>process.nextTick</code> 实在，首先 setTimeout 精度不够，还有一点就是里面有定时器对象，并需要在 libuv 底层执行，占用一定性能，所以可以用 <code>process.nextTick</code> 解决这种场景。</p>
</li>
</ul>
<h3 data-id="heading-20">5 pending 阶段</h3>
<p>pending 阶段用来处理此次事件循环之前延时的 I/O 回调函数。首先看一下在 libuv 中执行时机。</p>
<blockquote>
<p>libuv/src/unix/core.c</p>
</blockquote>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">int</span> <span class="hljs-title">uv__run_pending</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  QUEUE* q;
  QUEUE pq;
  <span class="hljs-keyword">uv__io_t</span>* w
  <span class="hljs-comment">/* pending_queue 为空，清空队列 ，返回 0  */</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">QUEUE_EMPTY</span>(&loop->pending_queue))
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  
  <span class="hljs-built_in">QUEUE_MOVE</span>(&loop->pending_queue, &pq);
  <span class="hljs-keyword">while</span> (!<span class="hljs-built_in">QUEUE_EMPTY</span>(&pq)) &#123; <span class="hljs-comment">/* pending_queue 不为空的情况，清空 I/O 回调。返回 1  */</span>
    q = <span class="hljs-built_in">QUEUE_HEAD</span>(&pq);
    <span class="hljs-built_in">QUEUE_REMOVE</span>(q);
    <span class="hljs-built_in">QUEUE_INIT</span>(q);
    w = <span class="hljs-built_in">QUEUE_DATA</span>(q, <span class="hljs-keyword">uv__io_t</span>, pending_queue);
    w-><span class="hljs-built_in">cb</span>(loop, w, POLLOUT);
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果存放 I/O 回调的任务的 <code>pending_queue</code> 是空的，那么直接返回 0。</li>
<li>如果 pending_queue 有 I/O 回调任务，那么执行回调任务。</li>
</ul>
<h3 data-id="heading-21">6 idle, prepare  阶段</h3>
<p><code>idle</code> 做一些 libuv 一些内部操作， <code>prepare</code> 为接下来的 I/O 轮询做一些准备工作。接下来一起解析一下比较重要 <code>poll</code> 阶段。</p>
<h3 data-id="heading-22">7 poll I / O 轮询阶段</h3>
<p>在正式讲解 poll 阶段做哪些事情之前，首先看一下，在 libuv 中，轮询阶段的执行逻辑：</p>
<pre><code class="hljs language-c++ copyable" lang="c++">  timeout = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">if</span> ((mode == UV_RUN_ONCE && !ran_pending) || mode == UV_RUN_DEFAULT)
      <span class="hljs-comment">/* 计算 timeout   */</span>
      timeout = <span class="hljs-built_in">uv_backend_timeout</span>(loop);
      <span class="hljs-comment">/* 进入 I/O 轮询 */</span>
      <span class="hljs-built_in">uv__io_poll</span>(loop, timeout);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>初始化超时时间 timeout = 0 ，通过 <code>uv_backend_timeout</code> 计算本次 <code>poll</code> 阶段的超时时间。超时时间会影响到异步 I/O 和后续事件循环的执行。</li>
</ul>
<p><strong>timeout代表什么</strong></p>
<p>首先要明白不同 timeout ，在 I/O 轮询中代表什么意思。</p>
<ul>
<li>当 <code>timeout = 0</code> 的时候，说明 poll 阶段不会阻塞事件循环的进行，那么说明有更迫切执行的任务。那么当前的 poll 阶段不会发生阻塞，会尽快进入下一阶段，尽快结束当前 tick，进入下一次事件循环，那么这些<strong>紧急</strong>任务将被执行。</li>
<li>当 <code>timeout = -1</code>时，说明会一直阻塞事件循环，那么此时就可以停留在异步 I/O 的 poll 阶段，等待新的 I/O 任务完成。</li>
<li>当 <code>timeout</code>等于常数的情况，说明此时 io poll 循环阶段能够停留的时间，那么什么时候会存在 timeout 为常数呢，将马上揭晓。</li>
</ul>
<p><strong>获取timeout</strong></p>
<p>timeout 的获取是通过 uv_backend_timeout 那么如何获得的呢？</p>
<pre><code class="hljs language-js copyable" lang="js">int <span class="hljs-function"><span class="hljs-title">uv_backend_timeout</span>(<span class="hljs-params"><span class="hljs-keyword">const</span> uv_loop_t* loop</span>)</span> &#123;
    <span class="hljs-comment">/* 当前事件循环任务停止 ，不阻塞 */</span>
  <span class="hljs-keyword">if</span> (loop->stop_flag != <span class="hljs-number">0</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
   <span class="hljs-comment">/* 当前事件循环 loop 不活跃的时候 ，不阻塞 */</span>
  <span class="hljs-keyword">if</span> (!uv__has_active_handles(loop) && !uv__has_active_reqs(loop))
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  <span class="hljs-comment">/* 当 idle 句柄队列不为空时，返回 0，即不阻塞。 */</span>
  <span class="hljs-keyword">if</span> (!QUEUE_EMPTY(&loop->idle_handles))
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
   <span class="hljs-comment">/* i/o pending 队列不为空的时候。 */</span>  
  <span class="hljs-keyword">if</span> (!QUEUE_EMPTY(&loop->pending_queue))
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
   <span class="hljs-comment">/* 有关闭回调 */</span>
  <span class="hljs-keyword">if</span> (loop->closing_handles)
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  <span class="hljs-comment">/* 计算有没有延时最小的延时器 ｜ 定时器 */</span>
  <span class="hljs-keyword">return</span> uv__next_timeout(loop);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>uv_backend_timeout 主要做的事情是：</p>
<ul>
<li>当前事件循环停止时，不阻塞。</li>
<li>当前事件循环 loop 不活跃的时候 ，不阻塞。</li>
<li>当 idle 队列 （ setImmediate ） 不为空时，返回 0，不阻塞。</li>
<li>i/o pending 队列不为空的时候，不阻塞。</li>
<li>有关闭回调函数的时候，不阻塞。</li>
<li>如果上述均不满足，那么通过 <code>uv__next_timeout</code> 计算有没有延时阀值最小的定时器 ｜ 延时器（ 最急迫执行 ），返回延时时间。</li>
</ul>
<p>接下来看一下 <code>uv__next_timeout</code> 逻辑。</p>
<blockquote>
</blockquote>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv__next_timeout</span><span class="hljs-params">(<span class="hljs-keyword">const</span> <span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  <span class="hljs-keyword">const</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">heap_node</span>* <span class="hljs-title">heap_node</span>;</span>
  <span class="hljs-keyword">const</span> <span class="hljs-keyword">uv_timer_t</span>* handle;
  <span class="hljs-keyword">uint64_t</span> diff;
  <span class="hljs-comment">/* 找到延时时间最小的 timer  */</span>
  heap_node = <span class="hljs-built_in">heap_min</span>((<span class="hljs-keyword">const</span> struct heap*) &loop->timer_heap);
  <span class="hljs-keyword">if</span> (heap_node == <span class="hljs-literal">NULL</span>) <span class="hljs-comment">/* 如何没有 timer，那么返回 -1 ，一直进入 poll 状态  */</span>
    <span class="hljs-keyword">return</span> <span class="hljs-number">-1</span>; 

  handle = <span class="hljs-built_in">container_of</span>(heap_node, <span class="hljs-keyword">uv_timer_t</span>, heap_node);
   <span class="hljs-comment">/* 有过期的 timer 任务，那么返回 0，poll 阶段不阻塞 */</span>
  <span class="hljs-keyword">if</span> (handle->timeout <= loop->time)
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  <span class="hljs-comment">/* 返回当前最小阀值的 timer 与 当前事件循环的事件相减，得出来的时间，可以证明 poll 可以停留多长时间 */</span> 
  diff = handle->timeout - loop->time;
  <span class="hljs-keyword">return</span> (<span class="hljs-keyword">int</span>) diff;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>uv__next_timeout</code> 做的事情如下：</p>
<ul>
<li>找到时间阀值最小的 timer （最优先执行的），如何没有 timer，那么返回 -1 。poll 阶段将<strong>无限制阻塞</strong>。这样的好处是一旦有 I/O 执行完毕 ，I/O 回调函数会直接加入到 poll ，接下来就会执行对应的回调函数。</li>
<li>如果有 timer ，但是 <code>timeout <= loop.time</code> 证明已经过期了，那么返回 0，poll 阶段不阻塞，优先执行过期任务。</li>
<li>如果没有过期，返回当前最小阀值的 timer 与 当前事件循环的事件相减得值，即是可以证明 poll 可以停留多长时间。当停留完毕，证明有过期 timer ，那么进入到下一个 tick。</li>
</ul>
<p><strong>执行io_poll</strong></p>
<p>接下来就是 <code>uv__io_poll</code> 真正的执行，里面有一个 <code>epoll_wait</code> 方法，根据 timeout ，来轮询有没有 I/O 完成，有得话那么执行 I/O 回调。这也是 unix 下异步I/O 实现的重要环节。</p>
<p><strong>poll阶段本质</strong></p>
<p>接下来总结一下 poll 阶段的本质：</p>
<ul>
<li>poll 阶段就是通过 timeout 来判断，是否阻塞事件循环。poll 也是一种轮询，轮询的是 i/o 任务，事件循环倾向于 poll 阶段的持续进行，其目的就是更快的执行 I/O 任务。如果没有其他任务，那么将一直处于 poll 阶段。</li>
<li>如果有其他阶段更紧急待执行的任务，比如 timer ，close ，那么 poll 阶段将不阻塞，会进行下一个 tick 阶段。</li>
</ul>
<p><strong>poll 阶段流程图</strong></p>
<p>我把整个 poll 阶段做的事用流程图表示，省去了一些细枝末节。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33a962f0676a4286abc7c8f16ff7314b~tplv-k3u1fbpfcp-watermark.image" alt="8.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">8 check 阶段</h3>
<p>如果 poll 阶段进入 idle 状态并且 setImmediate 函数存在回调函数时，那么 poll 阶段将打破无限制的等待状态，并进入 check 阶段执行 check 阶段的回调函数。</p>
<p><strong>check 做的事就是处理 setImmediate 回调。</strong>，先来看一下 Nodejs 中是怎么定义的 <code>setImmediate</code>。</p>
<h4 data-id="heading-24">Nodejs 底层中的 setImmediate</h4>
<p><strong>setImmediate定义</strong></p>
<blockquote>
<p>node/lib/timer.js</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setImmediate</span>(<span class="hljs-params">callback, arg1, arg2, arg3</span>) </span>&#123;
  validateCallback(callback); <span class="hljs-comment">/* 校验一下回调函数 */</span>
   <span class="hljs-comment">/* 创建一个 Immediate 类   */</span>
   <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Immediate(callback, args);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当调用 <code>setImmediate</code> 本质上调用 nodejs 中的 setImmediate 方法，首先校验回调函数，然后创建一个 <code>Immediate</code> 类。接下来看一下 Immediate 类。</li>
</ul>
<blockquote>
<p>node/lib/internal/timers.js</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Immediate</span></span>&#123;
   <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callback, args</span>)</span> &#123;
    <span class="hljs-built_in">this</span>._idleNext = <span class="hljs-literal">null</span>;
    <span class="hljs-built_in">this</span>._idlePrev = <span class="hljs-literal">null</span>; <span class="hljs-comment">/* 初始化参数 */</span>
    <span class="hljs-built_in">this</span>._onImmediate = callback;
    <span class="hljs-built_in">this</span>._argv = args;
    <span class="hljs-built_in">this</span>._destroyed = <span class="hljs-literal">false</span>;
    <span class="hljs-built_in">this</span>[kRefed] = <span class="hljs-literal">false</span>;

    initAsyncResource(<span class="hljs-built_in">this</span>, <span class="hljs-string">'Immediate'</span>);
    <span class="hljs-built_in">this</span>.ref();
    immediateInfo[kCount]++;
    
    immediateQueue.append(<span class="hljs-built_in">this</span>); <span class="hljs-comment">/* 添加 */</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Immediate 类会初始化一些参数，然后将当前 Immediate 类，插入到 <code>immediateQueue</code> 链表中。</li>
<li>immediateQueue 本质上是一个链表，存放每一个 Immediate。</li>
</ul>
<p><strong>setImmediate执行</strong></p>
<p>poll 阶段之后，会马上到 check 阶段，执行 immediateQueue 里面的 Immediate。 在每一次事件循环中，会先执行一个setImmediate 回调，然后清空 nextTick 和 Promise 队列的内容。为了验证这个结论，同样和 setTimeout 一样，看一下如下代码块：</p>
<pre><code class="hljs language-js copyable" lang="js">setImmediate(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setImmediate1'</span>)
    process.nextTick(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'nextTick'</span>)
    &#125;)
&#125;)

setImmediate(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setImmediate2'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bbc572985ea400e851c5db9eb18ca36~tplv-k3u1fbpfcp-watermark.image" alt="12.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打印 setImmediate1 -> nextTick -> setImmediate2 ，在每一次事件循环中，执行一个 setImmediate ，然后执行清空 nextTick 队列，在下一次事件循环中，执行另外一个 setImmediate2 。</p>
<p><strong>setImmediate执行流程图</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90739785383347c2bd41dcfa1c4bfd0f~tplv-k3u1fbpfcp-watermark.image" alt="13.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-25">setTimeout & setImmediate</h4>
<p>接下来对比一下 <strong>setTimeout</strong> 和 <strong>setImmediate</strong>，如果开发者期望延时执行的异步任务，那么接下来对比一下 <code>setTimeout(fn,0)</code> 和 <code>setImmediate(fn)</code> 区别。</p>
<ul>
<li>setTimeout 是 用于在设定阀值的最小误差内，执行回调函数，setTimeout 存在精度问题，创建 setTimeout 和 poll 阶段都可能影响到 setTimeout 回调函数的执行。</li>
<li>setImmediate 在 poll 阶段之后，会马上进入 check 阶段，会执行 <code>setImmediate</code>回调。</li>
</ul>
<p>如果 setTimeout 和 setImmediate 在一起，那么谁先执行呢？</p>
<p>首先写一个 demo：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout'</span>)
&#125;,<span class="hljs-number">0</span>)

setImmediate(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log( <span class="hljs-string">'setImmediate'</span> )
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>猜测</strong></p>
<p>先猜测一下，setTimeout 发生 <code>timer</code> 阶段，setImmediate 发生在 <code>check</code> 阶段，timer 阶段早于 check 阶段，那么 setTimeout 优先于 setImmediate 打印。但事实是这样吗？</p>
<p><strong>实际打印结果</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0bf5b50bc234a6b96a6dc50623b444f~tplv-k3u1fbpfcp-watermark.image" alt="14.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从以上打印结果上看， <code>setTimeout</code> 和 <code>setImmediate</code> 执行时机是不确定的，为什么会造成这种情况，上文中讲到即使 setTimeout 第二个参数为 0，在 nodejs 中也会被处理 <code>setTimeout(fn,1)</code>。当主进程的同步代码执行之后，会进入到事件循环阶段，第一次进入 timer 中，此时 settimeout 对应的 timer 的时间阀值为 1，若在前文 uv__run_timer(loop) 中，系统时间调用和时间比较的过程总耗时没有超过 1ms 的话，在 timer 阶段会发现没有过期的计时器，那么当前 timer 就不会执行，接下来到 check 阶段，就会执行 setImmediate 回调，此时的执行顺序是： <strong>setImmediate -> setTimeout</strong>。</p>
<p>但是如果总耗时超过一毫秒的话，执行顺序就会发生变化，在 timer 阶段，取出过期的 setTimeout 任务执行，然后到 check 阶段，再执行 setImmediate ，此时  <strong>setTimeout</strong> -> <strong>setImmediate</strong>。</p>
<p>造成这种情况发生的原因是：timer 的时间检查距当前事件循环 tick 的间隔可能小于 1ms 也可能大于 1ms 的阈值，所以决定了 setTimeout 在第一次事件循环执行与否。</p>
<p>接下来我用代码阻塞的情况，会大概率造成 setTimeout 一直优先于 setImmediate 执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* <span class="hljs-doctag">TODO:</span>  setTimeout & setImmediate */</span>
setImmediate(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log( <span class="hljs-string">'setImmediate'</span> )
&#125;)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout'</span>)
&#125;,<span class="hljs-number">0</span>)
<span class="hljs-comment">/* 用 100000 循环阻塞代码，促使 setTimeout 过期 */</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-number">100000</span>;i++)&#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/895ee782008e447b9b85334876ee4600~tplv-k3u1fbpfcp-watermark.image" alt="15.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>100000</code> 循环阻塞代码，这样会让 setTimeout 超过时间阀值执行，这样就保证了每次先执行 <strong>setTimeout</strong> -> <strong>setImmediate</strong> 。</p>
<p>特殊情况：确定顺序一致性。我们看一下特殊的情况。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
fs.readFile(<span class="hljs-string">'./file.js'</span>,<span class="hljs-function">()=></span>&#123;
    setImmediate(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log( <span class="hljs-string">'setImmediate'</span> )
    &#125;)
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout'</span>)
    &#125;,<span class="hljs-number">0</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上情况就会造成，setImmediate 一直优先于 setTimeout 执行，至于为什么，来一起分析一下原因。</p>
<ul>
<li>首先分析一下异步任务——主进程中有一个异步 I/O 任务，I/O 回调中有一个 setImmediate 和 一个 setTimeout 。</li>
<li>在 <code>poll</code> 阶段会执行 I/O 回调。然后处理一个 setImmediate</li>
</ul>
<p>万变不离其宗，只要掌握了如上各个阶段的特性，那么对于不同情况的执行情况，就可以清晰的分辨出来。</p>
<h3 data-id="heading-26">9 close 阶段</h3>
<p>close 阶段用于执行一些关闭的回调函数。执行所有的 close 事件。接下来看一下 close 事件 <code>libuv</code> 的实现。</p>
<blockquote>
<p>libuv/src/unix/core.c</p>
</blockquote>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">uv__run_closing_handles</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  <span class="hljs-keyword">uv_handle_t</span>* p;
  <span class="hljs-keyword">uv_handle_t</span>* q;

  p = loop->closing_handles;
  loop->closing_handles = <span class="hljs-literal">NULL</span>;

  <span class="hljs-keyword">while</span> (p) &#123;
    q = p->next_closing;
    <span class="hljs-built_in">uv__finish_close</span>(p);
    p = q;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>uv__run_closing_handles</code> 这个方法循环执行 close 队列里面的回调函数。</li>
</ul>
<h3 data-id="heading-27">10 Nodejs 事件循环总结</h3>
<p>接下来总结一下 Nodejs 事件循环。</p>
<ul>
<li>
<p>Nodejs 的事件循环分为 6 大阶段。分别为 timer 阶段，pending 阶段，prepare 阶段，poll 阶段， check 阶段，close 阶段。</p>
</li>
<li>
<p>nextTick 队列和 Microtasks 队列执行特点，在每一阶段完成后执行， nextTick 优先级大于 Microtasks （ Promise ）。</p>
</li>
<li>
<p>poll 阶段主要处理 I/O，如果没有其他任务，会处于轮询阻塞阶段。</p>
</li>
<li>
<p>timer 阶段主要处理定时器/延时器，它们并非准确的，而且创建需要额外的性能浪费，它们的执行还收到 poll 阶段的影响。</p>
</li>
<li>
<p>pending 阶段处理 I/O 过期的回调任务。</p>
</li>
<li>
<p>check 阶段处理 setImmediate。 setImmediate 和 setTimeout 执行时机和区别。</p>
</li>
</ul>
<h2 data-id="heading-28">四 Nodejs事件循环习题演练</h2>
<p>接下来为了更清楚事件循环流程，这里出两道事件循环的问题。作为实践：</p>
<h3 data-id="heading-29">习题一</h3>
<pre><code class="hljs language-js copyable" lang="js">process.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>);
&#125;);
process.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2'</span>);
     setImmediate(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'3'</span>);
    &#125;);
    process.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'4'</span>);
    &#125;);
&#125;);

setImmediate(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'5'</span>);
     process.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'6'</span>);
    &#125;);
    setImmediate(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'7'</span>);
    &#125;);
&#125;);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-params">e</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">8</span>);
    <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-number">8</span>+<span class="hljs-string">'promise'</span>);
        resolve();
    &#125;).then(<span class="hljs-function"><span class="hljs-params">e</span>=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-number">8</span>+<span class="hljs-string">'promise+then'</span>);
    &#125;)
&#125;,<span class="hljs-number">0</span>)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-params">e</span>=></span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-number">9</span>); &#125;,<span class="hljs-number">0</span>)

setImmediate(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'10'</span>);
    process.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'11'</span>);
    &#125;);
    process.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'12'</span>);
    &#125;);
    setImmediate(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'13'</span>);
    &#125;);
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'14'</span>);
 <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">15</span>);
    resolve();
&#125;).then(<span class="hljs-function"><span class="hljs-params">e</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">16</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果刚看这个 demo 可以会发蒙，不过上述讲到了整个事件循环，再来看这个问题就很轻松了，下面来分析一下整体流程：</p>
<ul>
<li>第一阶段： 首先开始启动 js 文件，那么进入第一次事件循环，那么先会执行同步任务：</li>
</ul>
<p>最先打印：</p>
<blockquote>
<p>打印console.log('14');</p>
</blockquote>
<blockquote>
<p>打印console.log(15);</p>
</blockquote>
<p><strong>nextTick 队列：</strong></p>
<p>nextTick -> console.log(1)
nextTick -> console.log(2) -> setImmediate(3) -> nextTick(4)</p>
<p><strong>Promise队列</strong></p>
<p>Promise.then(16)</p>
<p><strong>check队列</strong></p>
<p>setImmediate(5) -> nextTick(6) -> setImmediate(7)
setImmediate(10) -> nextTick(11) -> nextTick(12) -> setImmediate(13)</p>
<p><strong>timer队列</strong></p>
<p>setTimeout(8) -> promise(8+'promise') -> promise.then(8+'promise+then')
setTimeout(9)</p>
<ul>
<li>第二阶段：在进入新的事件循环之前，清空 nextTick 队列，和 promise 队列，顺序是 nextTick 队列大于 Promise 队列。</li>
</ul>
<p><strong>清空 nextTick</strong> ，打印：</p>
<blockquote>
<p>console.log('1');</p>
</blockquote>
<blockquote>
<p>console.log('2');</p>
</blockquote>
<p>执行第二个 nextTick 的时候，又有一个 nextTick ，所以会把这个 nextTick 也加入到队列中。接下来马上执行。</p>
<blockquote>
<p>console.log('4')</p>
</blockquote>
<p><strong>接下来清空Microtasks</strong></p>
<blockquote>
<p>console.log(16);</p>
</blockquote>
<p>此时的 check 队列加入了新的 setImmediate。</p>
<p><strong>check队列</strong>
setImmediate(5) -> nextTick(6) -> setImmediate(7)
setImmediate(10) -> nextTick(11) -> nextTick(12) -> setImmediate(13)
setImmediate(3)</p>
<ul>
<li>然后进入新的事件循环，首先执行 timer 里面的任务。执行第一个 setTimeout。</li>
</ul>
<p><strong>执行第一个 timer:</strong></p>
<blockquote>
<p>console.log(8);</p>
</blockquote>
<p>此时发现一个 Promise 。在正常的执行上下文中：</p>
<blockquote>
<p>console.log(8+'promise');</p>
</blockquote>
<p>然后将 Promise.then 加入到 nextTick 队列中。接下里会马上清空 nextTick 队列。</p>
<blockquote>
<p>console.log(8+'promise+then');</p>
</blockquote>
<p><strong>执行第二个 timer:</strong></p>
<blockquote>
<p>console.log(9)</p>
</blockquote>
<ul>
<li>接下来到了 check 阶段，执行 check 队列里面的内容：</li>
</ul>
<p><strong>执行第一个 check:</strong></p>
<blockquote>
<p>console.log(5);</p>
</blockquote>
<p>此时发现一个 nextTick ，然后还有一个 setImmediate 将 setImmediate 加入到 check 队列中。然后执行 nextTick 。</p>
<blockquote>
<p>console.log(6)</p>
</blockquote>
<p><strong>执行第二个 check</strong></p>
<blockquote>
<p>console.log(10)</p>
</blockquote>
<p>此时发现两个 nextTick 和一个 setImmediate 。接下来清空 nextTick 队列。将 setImmediate 添加到队列中。</p>
<blockquote>
<p>console.log(11)</p>
</blockquote>
<blockquote>
<p>console.log(12)</p>
</blockquote>
<p>此时的 check 队列是这样的：</p>
<p>setImmediate(3)
setImmediate(7)
setImmediate(13)</p>
<p>接下来按顺序清空 check 队列。打印</p>
<blockquote>
<p>console.log(3)</p>
</blockquote>
<blockquote>
<p>console.log(7)</p>
</blockquote>
<blockquote>
<p>console.log(13)</p>
</blockquote>
<p>到此为止，执行整个事件循环。那么整体打印内容如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1a983b95c0c472b8b9719834717c8e8~tplv-k3u1fbpfcp-watermark.image" alt="16.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-30">五 总结</h2>
<p>本文主要讲的内容如下：</p>
<ul>
<li>异步 I/O 介绍及其内部原理。</li>
<li>Nodejs 的事件循环，六大阶段。</li>
<li>Nodejs 中 setTimeout ，setImmediate ， 异步 i/o ，nextTick ，Promise 的原理及其区别。</li>
<li>Nodejs 事件循环实践。</li>
</ul>
<h3 data-id="heading-31">参考资料</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F135449621" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/135449621" ref="nofollow noopener noreferrer">从 libuv 看 nodejs 事件循环</a></li>
<li><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">深入浅出Nodejs</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F35918797" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/35918797" ref="nofollow noopener noreferrer">Node.js 事件循环的工作流程 & 生命周期</a></li>
</ul>
<h3 data-id="heading-32">《React进阶实践指南》</h3>
<p>小册内容将持续更新，随着 React 版本升级持续维护，并有持续更新章节～</p>
<p>提前透露，小册接下来会补充：<code>React context</code> 原理部分，内容补充到第八章。</p>
<p>奉上几个小册 7 折 优惠码  <strong>F3Z1VXtv</strong> ，先到先得～</p></div>  
</div>
            