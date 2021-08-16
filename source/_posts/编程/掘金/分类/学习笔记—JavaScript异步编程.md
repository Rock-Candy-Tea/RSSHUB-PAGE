
---
title: '学习笔记—JavaScript异步编程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec29021ae1a450183c0f4a4c991850b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 05:24:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec29021ae1a450183c0f4a4c991850b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<blockquote>
<p>在我们学习JS的时候一般都知道JavaScript是单线程的，那单线程是怎么处理网络复杂的请求和文件读写等耗时的操作呢，会不会效率很低，在不断的深入学习和了解，也逐渐明白了其中的奥秘，这也是接下来文章要写的我对于异步编程的理解。</p>
</blockquote>
<h1 data-id="heading-1">正文</h1>
<h2 data-id="heading-2">一、同步和异步</h2>
<p><strong>同步</strong></p>
<p>在学习异步之前我们先来看一下<strong>同步</strong>，比如在调用函数取得返回值的时候，能够直接得到预期结果（得到了预期的返回值），是按照你的代码顺序执行的，是连续的，那么就说这个函数是同步执行的。</p>
<p>下边看一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//在函数返回的时候，获得了预期的效果，即在控制台上打印了‘123’</span>
<span class="hljs-keyword">var</span> A = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;
A.prototype.n = <span class="hljs-number">123</span>;
<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">new</span> A();
<span class="hljs-built_in">console</span>.log(b,n);  <span class="hljs-comment">// 123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>如果函数是同步的，<strong>即是调用函数执行的任务比较耗时</strong>，也会一直等待直到得到预期结果。</strong> 因为它是按代码执行顺序执行的。</p>
<p><strong>异步</strong></p>
<p>如果在调用函数返回值的时候，不直接得到预期结果（预期的返回值），而是需要通过一定的方式获得，是<strong>不连续的不按代码顺序执行</strong>的，那么就可以说这个函数是异步的。</p>
<p>如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//读取文件</span>
fc.readFile(<span class="hljs-string">'hello'</span>,<span class="hljs-string">'utf8'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err,data</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(data)
&#125;);
<span class="hljs-comment">//网络请求</span>
<span class="hljs-keyword">var</span> pzh = <span class="hljs-keyword">new</span> XMLHttpRequest();
pzh.onreadystatechange = yyy;  <span class="hljs-comment">// 这里添加回调函数</span>
pzh.open(<span class="hljs-string">'GET'</span>,url);
pzh.send();<span class="hljs-comment">//发起函数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述示例中读取文件函数 readFile和网络请求的发起函数 ，send都将执行耗时操作，虽然函数会立即返回，但是不能立刻获取预期的结果，因为耗时操作交给其他线程执行，暂时获取不到预期结果。而在JavaScript中通过回调函数 function(err, data) &#123; console.log(data); &#125;和 onreadystatechange   ，在耗时操作执行完成后把相应的结果信息传递给回调函数，通知执行JavaScript代码的线程执行回调。</p>
<p>简单来说：同步按你的代码顺序执行，异步不按照代码顺序执行，异步的执行效率更高。</p>
<h2 data-id="heading-3">二、首先要知道的异步机制</h2>
<h3 data-id="heading-4"><strong>浏览器内核的多线程</strong></h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec29021ae1a450183c0f4a4c991850b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们都知道JavaScript是单线程的，但是浏览器的内核是多线程的；他们在内核的控制下互相配合以保持同步，一个浏览器至少实现三个常驻：Javascrpt引擎线程、GUI渲染线程、浏览器事件触发线程。</p>
<ul>
<li>
<p>JS引擎：基于事件驱动单线程执行的，JS引擎一直等待这任务队列中任务的到来，然后加以处理；浏览器无论什么时候都<strong>只有一个</strong>JS线程在运行JS程序。</p>
</li>
<li>
<p>GUI渲染线程：当界面需要重绘或由于某种操作引发回流时，线程就会执行。这里需要注意的是，<strong>渲染线程和JS引擎线程是不能同时进行的。</strong></p>
</li>
<li>
<p>事件触发线程：当一个事件被触发时，该线程会把世间添加到等待队列的队尾，等待JS引擎的处理，这些时间可来自JavaScript引擎执行当前的代码块，如：setTimeOut，也可以来自浏览器内核和其他线程如鼠标点击；AJAX异步请求等，但是由于JS 的单线程关系，所有这些事情都得排队等待JS引擎处理。</p>
</li>
</ul>
<h3 data-id="heading-5"><strong>事件循环机制</strong></h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d63b69e44c14df8b5f714a4d076e8a5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，左边的栈存储的是同步任务，就是那些能立即执行、不耗时的任务，如变量和函数的初始化、事件的绑定等等那些不需要回调函数的操作都可归为这一类。</p>
<p>右边的堆用来存储声明的变量、对象。下面的队列就是消息队列，一旦某个异步任务有了响应就会被推入队列中。如用户的点击事件、浏览器收到服务的响应和setTimeout中待执行的事件，每个异步任务都和回调函数相关联。</p>
<p>JS引擎线程用来执行栈中的同步任务，当所有同步任务执行完毕后，栈被清空，然后读取消息队列中的一个待处理任务，并把相关回调函数压入栈中，单线程开始执行新的同步任务。</p>
<p><strong>JS引擎线程从消息队列中读取任务是不断循环的，每次栈被清空后，都会在消息队列中读取新的任务，如果没有新的任务，就会等待，直到有新的任务，这就叫事件循环（Eventloop）。</strong></p>
<h3 data-id="heading-6">什么是宏任务与微任务？</h3>
<p>我们都知道 Js 是单线程的，但是一些高耗时操作就带来了进程阻塞问题。为了解决这个问题，Js 有两种任务的执行模式：<strong>同步模式（Synchronous）和异步模式（Asynchronous）。</strong></p>
<p>在异步模式下，创建异步任务主要分为<strong>宏任务与微任务</strong>两种。ES6 规范中，宏任务（Macrotask） 称为 Task， 微任务（Microtask） 称为 Jobs。<strong>宏任务是由宿主（浏览器、Node）发起的，而微任务由 JS 自身发起。</strong></p>
<ul>
<li>1)宏任务 （macrotask）：优先级低，先定义的先执行。包括：ajax，setTimeout，setInterval，事件绑定，postMessage，MessageChannel（用于消息通讯）。</li>
<li>2)微任务 （microtask）：优先级高，并且可以插队，不是先定义先执行。包括：promise.then，async/await [generator]，requestAnimationFrame，observer，MutationObserver，setImmediate。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd16e74bc432432fbe42c0ac18c8b534~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
由上图可以看到：</p>
<p>从JS主线程(整体代码)开始第一次循环，发起异步任务后，由（橙色）线程执行异步操作，而JS引擎主线程继续执行堆中的其他同步任务，直到堆中的所有异步任务执行完毕。之后全局上下文进入函数调用栈。直到调用栈清空(只剩全局)。然后执行所有的micro-task，当所有可执行的micro-task执行完毕之后。循环再次从macro-task开始，找到其中一个任务队列执行完毕，然后再执行所有的macro-task，这样一直循环下去。</p>
<p>根据事件循环机制，我们重新梳理一下流程：</p>
<p>1）首先执行栈里的任务</p>
<p>2）先找微任务队列，如果微任务队列中有，先从微任务队列中，一般按照存放顺序获取并且去执行。</p>
<p>3）如果微任务队列中没有，则再去宏任务队列中查找，在宏任务队列中，一般是按照谁先到达执行的条件，就先把谁拿出来执行。</p>
<p>4）以此循环</p>
<p><strong>明白事件循环之后我们要知道Javascript异步编程先后经历了四个阶段，分别是Callback阶段，Promise阶段，Generator阶段和Async/Await阶段。</strong></p>
<h2 data-id="heading-7">三、回调函数（Callback）阶段</h2>
<p>回调函数是异步操作最基本的方法。</p>
<p>demo1：假定有一个异步操作(asyncFn)，和一个同步操作(normalFn)。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncFn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'asyncFn'</span>);
     ),<span class="hljs-number">0</span>)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">normalFn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'normalFn'</span>);
&#125;
asyncFn();   <span class="hljs-comment">//asyncFn</span>
normalFn();   <span class="hljs-comment">//normalFn</span>
    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果按照正常的JS处理机制来说，同步操作一定发生在异步之前。如果我想要将顺序改变，最简单的方式就是使用回调（callback）的方式处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncFn</span>(<span class="hljs-params">callback</span>)</span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'asyncFn'</span>);
        callback();
    &#125;,<span class="hljs-number">0</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">normalFn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'normalFn'</span>);
&#125;

asyncFn(normalFn);
<span class="hljs-comment">//asyncFn</span>
<span class="hljs-comment">//normalFn</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回调函数的优点是简单、容易理解和实现，缺点是不利于代码的阅读和维护，各个部分之间高度耦合，使得程序结构混乱、流程难以追踪（尤其是多个回调函数嵌套的情况，容易出现回调地狱，可读性差），而且每个任务只能指定一个回调函数。此外不能使用 try catch 捕获错误，不能直接return。</p>
<h3 data-id="heading-8">回调函数易混淆点——传参：</h3>
<p>一，将回调函数的参数作为与回调函数同等级的参数进行传递。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fc640e742b146049df02eef97000696~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>二，回调函数的参数在调用回调函数内部创建。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/906ee49179f34f939267e7c714fd57f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">事件监听、发布订阅</h3>
<p><strong>事件监听</strong></p>
<p>事件监听也是一种非常常见的异步编程模式，它是一种典型的逻辑分离方式，对代码解耦很有用处。</p>
<p>下边看例子：还是以函数f1和f2为例</p>
<pre><code class="hljs language-js copyable" lang="js">f1.on(<span class="hljs-string">'done'</span>, f2);  <span class="hljs-comment">//f2必须等到f1执行完成，才可执行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params"></span>) </span>&#123; 
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// ... </span>
        f1.trigger(<span class="hljs-string">'done'</span>); 
    &#125;, <span class="hljs-number">1000</span>); 
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上，f1.trigger('done')表示，执行完成后，立即触发done事件，从而开始执行f2。</p>
<p>这种方法的<strong>优点</strong>是比较容易理解，可以绑定多个事件，每个事件可以指定多个回调函数，而且可以“去耦合”，有利于实现模块化。</p>
<p><strong>缺点</strong>是整个程序都要变成事件驱动型，运行流程会变得很不清晰。阅读代码的时候，很难看出主流程。</p>
<p><strong>发布订阅模式</strong></p>
<p>发布订阅式的应用非常 广泛，既可以用在异步编程中，也可以帮助我们完成更松耦合的代码编写。</p>
<p>假定，一家三口，妈妈作为“发布者”（publisher）实施和发布信号，爸爸作为中介“订阅”（subscribe）和处理这个信号，最后小明"订阅者"(subscriber)知道什么时候自己可以开始执行。这就叫做“发布/订阅模式”（publish-subscribe pattern）。</p>
<p>下边来看代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//订阅者接收到消息</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">eat</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'妈妈做好饭啦，去吃饭啦'</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cooking</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'妈妈认真做饭中'</span>);
    <span class="hljs-comment">//发布者向订阅中介发布消息</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'孩儿他爸饭做好了，叫小明来吃饭'</span>)
        Dad.publish(<span class="hljs-string">"done"</span>);<span class="hljs-comment">//中介接收消息</span>
    &#125;,<span class="hljs-number">3000</span>)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">read</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'小明假装学习'</span>) <span class="hljs-comment">//订阅者等消息</span>
    Dad.subscribe(<span class="hljs-string">'done'</span>,eat);
&#125;

<span class="hljs-comment">//执行代码</span>
cooking();
read()

<span class="hljs-comment">/*执行顺序
妈妈认真做饭中
小明假装学习
孩儿他爸饭做好了，叫小明来吃饭
妈妈做好饭啦，去吃饭啦

*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种模式下实现的异步编程，本质上还是通过回调函数实现的
，但是依然存在回调嵌套和无法捕捉异常问题的情况，接下来进入Promise阶段，看看是否能解决这两个问题。</p>
<h2 data-id="heading-10">四、Promise阶段</h2>
<p>Promise 并不是指某种特定的某个实现，它是一种规范(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpromisesaplus.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://promisesaplus.com/" ref="nofollow noopener noreferrer">PromiseA+规范</a>)，是一套处理JavaScript异步的机制。</p>
<h3 data-id="heading-11">1.Promise的三种状态</h3>
<ul>
<li><strong>Promise有三种状态pending，fulfilled和rejected</strong></li>
<li>状态转换只能是 <em><strong>pending到 resolved</strong></em></li>
<li>或者<em><strong>pending到 rejected</strong></em></li>
</ul>
<p><strong>状态一旦转换完成，不能再次转换</strong>。</p>
<p>可以由下图表示:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d9502fb91de46e796a4e60309d60bd4~tplv-k3u1fbpfcp-watermark.image" alt="1628436673(1).png" loading="lazy" referrerpolicy="no-referrer">
附上代码栗子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>) =></span> &#123;
    reject(<span class="hljs-string">'reject'</span>);
    resolve(<span class="hljs-string">'success'</span>)  <span class="hljs-comment">//无效代码不会执行</span>
&#125;)
p.then(
    <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(value)
    &#125;,
    <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(reason)  <span class="hljs-comment">//reject</span>
    &#125;
   )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们构造Promise 的时候，构造函数内部的代码是立即执行的</p>
<h3 data-id="heading-12">2.链式Promise</h3>
<p>先看两个例子：</p>
<p>demo1;</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//例1：</span>
<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>)
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(res);        <span class="hljs-comment">//打印 1</span>
        <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>   <span class="hljs-comment">//包装成Promsie.resolve（2）</span>
    &#125;)
    .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-number">3</span>);   <span class="hljs-comment">//这里catch会捕获没有捕获的异常</span>
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res))   <span class="hljs-comment">//打印 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当Promise创建对象调用resolve(...)或reject(...)时，这个Promise通过then(...)注册的回调函数就会在新的异步时间点上被触发。(then的链式调用)；
在then中使用return，那么return的值会被Promise.resolve（）包装。</p>
<p>demo2：以家务分配为例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">read</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'小明认真读书'</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">eat</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'好嘞，吃饭咯'</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'饭吃饱啦'</span>);
    &#125;, <span class="hljs-number">1000</span>)
  &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wash</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'唉，又要洗碗'</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'碗洗完啦'</span>);
    &#125;, <span class="hljs-number">1000</span>)
  &#125;)
&#125;
<span class="hljs-keyword">const</span> cooking = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>)=></span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'妈妈认真做饭'</span>); 
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; 
        resolve(<span class="hljs-string">'小明快过来，开饭啦'</span>); 
    &#125;, <span class="hljs-number">2000</span>); 
&#125;)

cooking.then(<span class="hljs-function"><span class="hljs-params">msg</span> =></span> &#123; 
    <span class="hljs-built_in">console</span>.log(msg); 
    <span class="hljs-keyword">return</span> eat(); 
&#125;).then(<span class="hljs-function"><span class="hljs-params">msg</span> =></span> &#123; 
    <span class="hljs-built_in">console</span>.log(msg); 
    <span class="hljs-keyword">return</span> wash();
&#125;).then(<span class="hljs-function"><span class="hljs-params">msg</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(msg);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'做完家务了，可以玩了'</span>)
&#125;)

read();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 执行顺序： 
妈妈认真做饭 
小明认真读书 
小明快过来，开饭啦 
好嘞，吃饭咯 
饭吃饱啦 
唉，又要洗碗
碗洗完啦 
做完家务了，可以玩了 
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实可以看出Promise.then（）可以解决的回调地狱（callback hell），但是无法捕获异常，还需要调用回调函数来解决。</p>
<blockquote>
<p>换句话说就是Promise 并没有真正脱离 callback ，Promise 只不过是用 then 方法来延迟了 callback 的绑定。</p>
</blockquote>
<h2 data-id="heading-13">五、生成器Generators/yield</h2>
<p>Generator 函数是 ES6 提供的一种异步编程解决方案，语法行为与传统函数完全不同，Generator 最大的特点就是可以控制函数的执行。</p>
<ul>
<li><code>function *</code>会定义一个生成器函数，并返回一个Generator（生成器）对象，其内部可以通过 <code>yield</code> 暂停代码，通过调用 <code>next</code> 恢复执行。</li>
</ul>
<p>简单看一下例子：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> * <span class="hljs-title">gen</span>(<span class="hljs-params"></span>) </span>&#123;
     <span class="hljs-keyword">yield</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>);
     <span class="hljs-keyword">yield</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'world'</span>);
     <span class="hljs-keyword">return</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ending'</span>);
&#125;

<span class="hljs-keyword">var</span> hw = gen();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台输入hw.next():</p>
<pre><code class="hljs language-js copyable" lang="js">hw.next(); 
index.html:<span class="hljs-number">156</span> hello 
hw.next(); 
index.html:<span class="hljs-number">157</span> world 
hw.next(); 
index.html:<span class="hljs-number">158</span> ending
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码定义了一个 Generator 函数helloWorldGenerator，它内部有两个yield表达式（hello和world），即该函数有三个状态：hello，world 和 return 语句（结束执行）。</p>
<p>必须调用遍历器对象的<code>next()</code>方法，使得指针移向下一个状态。每次调用next方法，内部指针就从上一次停下来的地方开始执行，直到遇到下一个<code>yield</code>表达式（或return语句）为止。</p>
<p>generator很方便处理异步（一般要配合tj/co库来用），这里举例说一下<code>co</code>，
<strong><code>co</code>是一个为Node.js和浏览器打造的基于生成器的流程控制工具，借助于Promise，你可以使用更加优雅的方式编写非阻塞代码</strong>。</p>
<p>安装<code>co</code>库只需：<code>npm install co</code></p>
<p>也可以自己去github找一下源码，了解一下</p>
<p>index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> co = <span class="hljs-built_in">require</span>(<span class="hljs-string">'co'</span>)
<span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-comment">// wrap the function to thunk</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readFile</span>(<span class="hljs-params">filename</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
        fs.readFile(filename, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, date</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (err) reject(err)
            resolve(data)
        &#125;)
    &#125;)
&#125;
<span class="hljs-comment">// generator 函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">gen</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> file1 = <span class="hljs-keyword">yield</span> readFile(<span class="hljs-string">'./file/1.txt'</span>) <span class="hljs-comment">// 1.txt内容为：content in 1.txt</span>
    <span class="hljs-keyword">var</span> file2 = <span class="hljs-keyword">yield</span> readFile(<span class="hljs-string">'./file/2.txt'</span>) <span class="hljs-comment">// 2.txt内容为：content in 2.txt</span>
    <span class="hljs-built_in">console</span>.log(file1)
    <span class="hljs-built_in">console</span>.log(file2)
    <span class="hljs-keyword">return</span> <span class="hljs-string">'done'</span>
&#125;
<span class="hljs-comment">// co</span>
co(gen).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, result</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(result)
&#125;)
<span class="hljs-comment">// content in 1.txt</span>
<span class="hljs-comment">// content in 2.txt</span>
<span class="hljs-comment">// done</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>co 函数库可以让你不用编写 generator 函数的执行器，generator 函数只要放在 co 函数里，就会自动执行。
再来看一个例子</p>
<pre><code class="hljs language-js copyable" lang="js">co(<span class="hljs-function"><span class="hljs-keyword">function</span> *(<span class="hljs-params"></span>)</span>&#123; 
    <span class="hljs-keyword">try</span> &#123; 
      <span class="hljs-keyword">var</span> res = <span class="hljs-keyword">yield</span> get(<span class="hljs-string">'http://baidu.com'</span>);
      <span class="hljs-built_in">console</span>.log(res); 
    &#125; <span class="hljs-keyword">catch</span>(e) &#123; 
      <span class="hljs-built_in">console</span>.log(e.code) 
   &#125; 
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>co 最大的好处在于通过它可以把异步的流程以同步的方式书写出来，并且可以使用 try/catch。</p>
<h2 data-id="heading-14">六、async/await</h2>
<p>使用async/await，可以轻松地达成之前使用生成器和co函数所做到的工作；
<strong>一句话，async 函数就是 Generator 函数的语法糖。</strong></p>
<p>然后用async/await实现上边（两个文件）的例子就可以这么写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> asyncReadFile = <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">var</span> f1 = <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'./file/1.txt'</span>);
  <span class="hljs-keyword">var</span> f2 = <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'./file/2.txt'</span>);
  <span class="hljs-built_in">console</span>.log(f1.toString());
  <span class="hljs-built_in">console</span>.log(f2.toString());
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一比较就会发现，async 函数就是将 Generator 函数的星号（*）替换成 async，将 yield 替换成 await。</p>
<h3 data-id="heading-15">1.async函数的特点：</h3>
<p>1.执行 async 函数，返回的<strong>都是</strong>Promise  对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test1</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-keyword">return</span> <span class="hljs-number">123</span>;
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test2</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">2</span>);
&#125;
<span class="hljs-keyword">const</span> result1 = test1();
<span class="hljs-keyword">const</span> result2 = test2();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'result1'</span>,result1);   <span class="hljs-comment">//promise</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'result2'</span>,result2)    <span class="hljs-comment">//promise</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自己可以 打印验证一下。</p>
<p>2.Promise.then  成功的情况对应 await</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test3</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> p3 = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">3</span>);
    p3.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'data'</span>,data);    
    &#125;)
    <span class="hljs-comment">//await 后边跟一个promise对象</span>
    <span class="hljs-keyword">const</span> data =<span class="hljs-keyword">await</span> p3;  
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'data'</span>,data);   <span class="hljs-comment">//data3</span>
&#125;
test3()

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test4</span>(<span class="hljs-params"></span>)</span>&#123;       <span class="hljs-comment">//await跟一个普通的数</span>
    <span class="hljs-keyword">const</span> data4 = <span class="hljs-keyword">await</span> <span class="hljs-number">4</span>;   <span class="hljs-comment">//await Promise.resolve(4)</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'data4'</span>,data4);     <span class="hljs-comment">//data4.4</span>
&#125;
test4();

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test5</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-keyword">const</span> data5 = <span class="hljs-keyword">await</span> test1();   <span class="hljs-comment">//  await跟一个异步的函数</span>
     <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'data5'</span>,data5);     <span class="hljs-comment">//data5.123</span>
&#125;
test5()
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>Promise.catch  异常的情况  对应 try...catch</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test6</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> p6 = <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-number">6</span>);
    <span class="hljs-comment">// const data6 = await p6;</span>
    <span class="hljs-comment">// console.log('data6',data6)    //报错：Uncaught (in promise)     6</span>
    <span class="hljs-keyword">try</span>&#123;
        <span class="hljs-keyword">const</span> data6 = <span class="hljs-keyword">await</span> p6;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'data6'</span>,data6);
    &#125;<span class="hljs-keyword">catch</span>(k)&#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'k'</span>,k);     <span class="hljs-comment">//捕获异常  k 6</span>
    &#125;
&#125;
test6()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结了这么多，如果还是不太理解，我推荐看一下这些
实战题（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FtetfPizYwMtr-XlBRfZAQA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/tetfPizYwMtr-XlBRfZAQA" ref="nofollow noopener noreferrer">ES6Promise实战练习题</a>）加速帮助消化。</p>
<p>此文章为个人学习笔记分享，技术有限，欢迎大家一起讨论学习。</p>
<p>参考文章：</p>
<p><a href="https://juejin.cn/post/6844903556084924423#heading-4" target="_blank" title="https://juejin.cn/post/6844903556084924423#heading-4">1.JavaScript异步机制详解</a></p>
<p><a href="https://juejin.cn/post/6844903760280420366#heading-1" target="_blank" title="https://juejin.cn/post/6844903760280420366#heading-1">2.JS 异步编程六种方案</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2012%2F12%2Fasynchronous%25EF%25BC%25BFjavascript.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/blog/2012/12/asynchronous%EF%BC%BFjavascript.html" ref="nofollow noopener noreferrer">3.Javascript异步编程的4种方法</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Flunahaijiao%2Farticle%2Fdetails%2F86743224" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/lunahaijiao/article/details/86743224" ref="nofollow noopener noreferrer">4.JS 基础之异步（五）：Generator</a></p></div>  
</div>
            