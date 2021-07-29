
---
title: '一位初级进阶中级 JavaScript 工作者的自我修养（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab94e52f465d408d8a5093d16300387f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 18:54:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab94e52f465d408d8a5093d16300387f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>最近的前端面试已经<strong>卷</strong>的飞起了<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab94e52f465d408d8a5093d16300387f~tplv-k3u1fbpfcp-zoom-1.image" alt="😂" loading="lazy" referrerpolicy="no-referrer">，从<strong>计算机原理、编译原理、数据结构、算法、设计模式、编程范式</strong>到<strong>编译工具、格式工具、Git、NPM、单元测试、Nginx、PM2、CI / CD 了解和使用</strong>。</p>
<p>这随便挑选一个部分，知识点都可以<strong>深入</strong>挖掘，<strong>深不见底</strong>那种。</p>
<p>前两天发布了 JS 基础系列第一篇文章，得到了同学们比较好的反馈。❤️❤️❤️</p>
<p>让我们继续学习这个系列其他<strong>有意思</strong>的内容，希望可以给大家带来一点点🤏帮助。</p>
<blockquote>
<p>温馨提示：本文适用于<strong>前端入门的同学</strong>和最近在准备想要<strong>系统化温习 JS 基础的朋友</strong>。已经工作多年的中高级前端大佬可以直接跳过本文哈～</p>
</blockquote>
<p>相关文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6989436364693454855" target="_blank" title="https://juejin.cn/post/6989436364693454855">《一位初级进阶中级 JavaScript 工作者的自我修养（一）》</a></li>
<li>《一位初级进阶中级 JavaScript 工作者的自我修养（二）》</li>
</ul>
<h1 data-id="heading-1">第四章 「重学 JavaScript」执行机制</h1>
<h2 data-id="heading-2">一、try 和 finally</h2>
<blockquote>
<p>为何 try 里面放 return，finally 还会执行，理解其内部机制</p>
</blockquote>
<h3 data-id="heading-3">1.1 Completion 类型</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// return 执行了但是没有立即返回，而是先执行了 finally</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">kaimo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.log(err);
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"a"</span>);
  &#125;
&#125;

<span class="hljs-built_in">console</span>.log(kaimo()); <span class="hljs-comment">// a 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// finally 中的 return 覆盖了 try 中的 return。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">kaimo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.log(err);
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
  &#125;
&#125;

<span class="hljs-built_in">console</span>.log(kaimo()); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Completion Record
Completion Record 用于描述异常、跳出等语句执行过程。表示一个语句执行完之后的结果，它有三个字段。</p>
<p>[[type]]：表示完成的类型，有 break、continue、return、throw、normal 几种类型</p>
<p>[[value]]：表示语句的返回值，如果语句没有，则是 empty</p>
<p>[[target]]：表示语句的目标，通常是一个 JavaScript 标签</p>
<p>JavaScript 使用 Completion Record 类型，控制语句执行的过程。</p>
<h3 data-id="heading-4">1.2 普通语句</h3>
<p>在 JavaScript 中，把不带控制能力的语句称为普通语句。种类可以参考引言的图片。</p>
<p>1、这些语句在执行时，从前到后顺次执行（这里先忽略 var 和函数声明的预处理机制），没有任何分支或者重复执行逻辑。</p>
<p>2、普通语句执行后，会得到 [[type]] 为 normal 的 Completion Record，JavaScript 引擎遇到这样的 Completion Record，会继续执行下一条语句。</p>
<p>3、在 Chrome 控制台输入一个表达式，可以得到结果，但是在前面加上 var，就变成了 undefined。Chrome 控制台显示的正是语句的 Completion Record 的 [[value]]。</p>
<h3 data-id="heading-5">1.3 语句块</h3>
<p>语句块就是拿大括号括起来的一组语句，它是一种语句的复合结构，可以嵌套。</p>
<p>语句块内部的语句的 Completion Record 的 [[type]] 如果不为 normal，会打断语句块后续的语句执行。</p>
<h4 data-id="heading-6">1.3.1 内部为普通语句的一个语句块</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在每一行的注释中为 Completion Record</span>
&#123;
  <span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; <span class="hljs-comment">// normal, empty, empty</span>
  i++; <span class="hljs-comment">// normal, 1, empty</span>
  <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">//normal, undefined, empty</span>
&#125; <span class="hljs-comment">// normal, undefined, empty</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个 block 中都是 normal 类型的话，该程序会按顺序执行。</p>
<h4 data-id="heading-7">1.3.2 加入 return</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在每一行的注释中为 Completion Record</span>
&#123;
  <span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; <span class="hljs-comment">// normal, empty, empty</span>
  <span class="hljs-keyword">return</span> i; <span class="hljs-comment">// return, 1, empty</span>
  i++;
  <span class="hljs-built_in">console</span>.log(i);
&#125; <span class="hljs-comment">// return, 1, empty</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 block 中产生的非 normal 的完成类型可以穿透复杂的语句嵌套结构，产生控制效果。</p>
<h3 data-id="heading-8">1.4 控制型语句</h3>
<p>控制型语句带有 if、switch 关键字，它们会对不同类型的 Completion Record 产生反应。</p>
<p>控制类语句分成两部分：</p>
<p>对其内部造成影响：如 if、switch、while/for、try。
对外部造成影响：如 break、continue、return、throw。</p>
<p>穿透就是去上一层的作用域或者控制语句找可以消费 break，continue 的执行环境，消费就是在这一层就执行了这个 break 或者 continue</p>
<p>这两类语句的配合，会产生控制代码执行顺序和执行逻辑的效果。</p>
<h3 data-id="heading-9">1.5 带标签的语句</h3>
<p>1、任何 JavaScript 语句是可以加标签的，在语句前加冒号即可：。</p>
<pre><code class="hljs language-js copyable" lang="js">firstStatement: <span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、类似于注释，基本没有任何用处。唯一有作用的时候是：与完成记录类型中的 target 相配合，用于跳出多层循环。</p>
<pre><code class="hljs language-js copyable" lang="js">outer: <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"outer"</span>);
  inner: <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"inner1"</span>);
    <span class="hljs-keyword">break</span> outer;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"inner2"</span>);
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"finished"</span>);
<span class="hljs-comment">// outer  inner1  finished</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">二、宏任务和微任务</h2>
<blockquote>
<p>宏任务和微任务分别有哪些</p>
</blockquote>
<p>宏任务主要有：script(整体代码)、setTimeout、setInterval、I/O、UI 交互事件、postMessage、MessageChannel、setImmediate(Node.js 环境)。</p>
<p>微任务主要有：Promise.then、 MutationObserver、 process.nextTick(Node.js 环境)。</p>
<h2 data-id="heading-11">三、异步编程</h2>
<blockquote>
<p>JavaScript 如何实现异步编程，可以详细描述 EventLoop 机制</p>
</blockquote>
<p>在 js 中，任务分为宏任务(macrotask)和微任务(microtask)，这两个任务分别维护一个队列，均采用先进先出的策略进行执行！同步执行的任务都在宏任务上执行。</p>
<p>具体的操作步骤如下：</p>
<ul>
<li>从宏任务的头部取出一个任务执行；</li>
<li>执行过程中若遇到微任务则将其添加到微任务的队列中；</li>
<li>宏任务执行完毕后，微任务的队列中是否存在任务，若存在，则挨个儿出去执行，直到执行完毕；</li>
<li>GUI 渲染；</li>
<li>回到步骤 1，直到宏任务执行完毕；</li>
</ul>
<p>前 4 步构成了一个事件的循环检测机制，即我们所称的 eventloop。</p>
<h2 data-id="heading-12">四、分析异步嵌套</h2>
<blockquote>
<p>可以快速分析一个复杂的异步嵌套逻辑，并掌握分析方法</p>
</blockquote>
<p>可以先把复杂的异步写法转换为简单写法。比如 async、await 异步的这种写法，其原理就是回调函数。</p>
<p>然后按照事件的循环机制进行分析。</p>
<h2 data-id="heading-13">五、使用 Promise 实现串行</h2>
<h3 data-id="heading-14">5.1 概述</h3>
<p>最常用的队列操作就是 Array.prototype.reduce()</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> result = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">5</span>].reduce(<span class="hljs-function">(<span class="hljs-params">accumulator, item</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> accumulator + item;
&#125;, <span class="hljs-number">0</span>); <span class="hljs-comment">// <-- Our initial value.</span>

<span class="hljs-built_in">console</span>.log(result); <span class="hljs-comment">// 8</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一个值 0 是起始值，每次 reduce 返回的值都会作为下次 reduce 回调函数的第一个参数，直到队列循环完毕，因此可以进行累加计算。</p>
<p>那么将 reduce 的特性用在 Promise 试试：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runPromiseByQueue</span>(<span class="hljs-params">myPromise</span>) </span>&#123;
  myPromise.reduce(
    <span class="hljs-function">(<span class="hljs-params">previousPromise, nextPromise</span>) =></span> previousPromise.then(<span class="hljs-function">() =></span> nextPromise()),
    <span class="hljs-built_in">Promise</span>.resolve()
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当上一个 Promise 开始执行（previousPromise.then），当其执行完毕后再调用下一个 Promise，并作为一个新 Promise 返回，下次迭代就会继续这个循环。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> createPromise = <span class="hljs-function">(<span class="hljs-params">time, id</span>) =></span> <span class="hljs-function">() =></span>
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise"</span>, id);
      solve();
    &#125;, time)
  );

runPromiseByQueue([
  createPromise(<span class="hljs-number">3000</span>, <span class="hljs-number">1</span>),
  createPromise(<span class="hljs-number">2000</span>, <span class="hljs-number">2</span>),
  createPromise(<span class="hljs-number">1000</span>, <span class="hljs-number">3</span>),
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">5.2 精读</h3>
<p>Reduce 是同步执行的，在一个事件循环就会完成，但这仅仅是在内存快速构造了 Promise 执行队列，展开如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-comment">// Promise #1</span>

  resolve();
&#125;)
  .then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
    <span class="hljs-comment">// Promise #2</span>

    <span class="hljs-keyword">return</span> result;
  &#125;)
  .then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
    <span class="hljs-comment">// Promise #3</span>

    <span class="hljs-keyword">return</span> result;
  &#125;); <span class="hljs-comment">// ... and so on!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Reduce 的作用就是在内存中生成这个队列，而不需要把这个冗余的队列写在代码里！</p>
<h3 data-id="heading-16">5.3 更简单的方法</h3>
<p>在 async/await 的支持下，runPromiseByQueue 函数可以更为简化：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runPromiseByQueue</span>(<span class="hljs-params">myPromises</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> value <span class="hljs-keyword">of</span> myPromises) &#123;
    <span class="hljs-keyword">await</span> value();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>多亏了 async/await，代码看起来如此简洁明了。</p>
<p>不过要注意，这个思路与 reduce 思路不同之处在于，利用 reduce 的函数整体是个同步函数，自己先执行完毕构造 Promise 队列，然后在内存异步执行；而利用 async/await 的函数是利用将自己改造为一个异步函数，等待每一个 Promise 执行完毕。</p>
<h2 data-id="heading-17">六、EventLoop</h2>
<blockquote>
<p>Node 与浏览器 EventLoop 的差异</p>
</blockquote>
<h3 data-id="heading-18">6.1 与浏览器环境有何不同</h3>
<p>在 node 中，事件循环表现出的状态与浏览器中大致相同。不同的是 node 中有一套自己的模型。node 中事件循环的实现是依靠的 libuv 引擎。我们知道 node 选择 chrome v8 引擎作为 js 解释器，v8 引擎将 js 代码分析后去调用对应的 node api，而这些 api 最后则由 libuv 引擎驱动，执行对应的任务，并把不同的事件放在不同的队列中等待主线程执行。 因此实际上 node 中的事件循环存在于 libuv 引擎中。</p>
<h3 data-id="heading-19">6.2 事件循环模型</h3>
<p>下面是一个 libuv 引擎中的事件循环的模型:</p>
<pre><code class="hljs language-js copyable" lang="js">   ┌───────────────────────┐
┌─>│       timers          │
│  └──────────┬────────────┘
│  ┌──────────┴────────────┐
│  │    I/O callbacks      │
│  └──────────┬────────────┘
│  ┌──────────┴────────────┐
│  │    idle, prepare      │
│  └──────────┬────────────┘ ┌───────────────┐
│  ┌──────────┴────────────┐ │ incoming:     │
│  │        poll           │<──connections───│
│  └──────────┬────────────┘ │ data, etc.    │
│  ┌──────────┴────────────┐ └───────────────┘
│  │        check          │
│  └──────────┬────────────┘
│  ┌──────────┴────────────┐
└──┤    close callbacks    │
   └───────────────────────┘
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：模型中的每一个方块代表事件循环的一个阶段</p>
<p>这个模型是 node 官网上的一篇文章中给出的，我下面的解释也都来源于这篇文章。我会在文末把文章地址贴出来，有兴趣的朋友可以亲自与看看原文。</p>
<h3 data-id="heading-20">6.3 事件循环各阶段详解</h3>
<p>从上面这个模型中，我们可以大致分析出 node 中的事件循环的顺序：</p>
<p>外部输入数据-->轮询阶段(poll)-->检查阶段(check)-->关闭事件回调阶段(close callback)-->定时器检测阶段(timer)-->I/O 事件回调阶段(I/O callbacks)-->闲置阶段(idle, prepare)-->轮询阶段...</p>
<p>以上各阶段的名称是根据我个人理解的翻译，为了避免错误和歧义，下面解释的时候会用英文来表示这些阶段。</p>
<p>这些阶段大致的功能如下：</p>
<ul>
<li>timers: 这个阶段执行定时器队列中的回调如  setTimeout()  和  setInterval()。</li>
<li>I/O callbacks: 这个阶段执行几乎所有的回调。但是不包括 close 事件，定时器和 setImmediate()的回调。</li>
<li>idle, prepare: 这个阶段仅在内部使用，可以不必理会。</li>
<li>poll: 等待新的 I/O 事件，node 在一些特殊情况下会阻塞在这里。</li>
<li>check: setImmediate()的回调会在这个阶段执行。</li>
<li>close callbacks: 例如 socket.on('close', ...)这种 close 事件的回调。</li>
</ul>
<p>下面我们来按照代码第一次进入 libuv 引擎后的顺序来详细解说这些阶段：</p>
<h4 data-id="heading-21">6.3.1 poll 阶段</h4>
<p>当个 v8 引擎将 js 代码解析后传入 libuv 引擎后，循环首先进入 poll 阶段。poll 阶段的执行逻辑如下： 先查看 poll queue 中是否有事件，有任务就按先进先出的顺序依次执行回调。 当 queue 为空时，会检查是否有 setImmediate()的 callback，如果有就进入 check 阶段执行这些 callback。但同时也会检查是否有到期的 timer，如果有，就把这些到期的 timer 的 callback 按照调用顺序放到 timer queue 中，之后循环会进入 timer 阶段执行 queue 中的 callback。 这两者的顺序是不固定的，收到代码运行的环境的影响。如果两者的 queue 都是空的，那么 loop 会在 poll 阶段停留，直到有一个 i/o 事件返回，循环会进入 i/o callback 阶段并立即执行这个事件的 callback。</p>
<p>值得注意的是，poll 阶段在执行 poll queue 中的回调时实际上不会无限的执行下去。有两种情况 poll 阶段会终止执行 poll queue 中的下一个回调：1.所有回调执行完毕。2.执行数超过了 node 的限制。</p>
<h4 data-id="heading-22">6.3.2 check 阶段</h4>
<p>check 阶段专门用来执行 setImmediate()方法的回调，当 poll 阶段进入空闲状态，并且 setImmediate queue 中有 callback 时，事件循环进入这个阶段。</p>
<h4 data-id="heading-23">6.3.3 close 阶段</h4>
<p>当一个 socket 连接或者一个 handle 被突然关闭时（例如调用了 socket.destroy()方法），close 事件会被发送到这个阶段执行回调。否则事件会用 process.nextTick（）方法发送出去。</p>
<h4 data-id="heading-24">6.3.4 timer 阶段</h4>
<p>这个阶段以先进先出的方式执行所有到期的 timer 加入 timer 队列里的 callback，一个 timer callback 指得是一个通过 setTimeout 或者 setInterval 函数设置的回调函数。</p>
<h4 data-id="heading-25">6.3.5 I/O callback 阶段</h4>
<p>如上文所言，这个阶段主要执行大部分 I/O 事件的回调，包括一些为操作系统执行的回调。例如一个 TCP 连接生错误时，系统需要执行回调来获得这个错误的报告。</p>
<h3 data-id="heading-26">6.4 推迟任务执行的方法</h3>
<p>在 node 中有三个常用的用来推迟任务执行的方法：process.nextTick,setTimeout（setInterval 与之相同）与 setImmediate</p>
<p>这三者间存在着一些非常不同的区别：</p>
<p>process.nextTick()</p>
<p>尽管没有提及，但是实际上 node 中存在着一个特殊的队列，即 nextTick queue。这个队列中的回调执行虽然没有被表示为一个阶段，当时这些事件却会在每一个阶段执行完毕准备进入下一个阶段时优先执行。当事件循环准备进入下一个阶段之前，会先检查 nextTick queue 中是否有任务，如果有，那么会先清空这个队列。与执行 poll queue 中的任务不同的是，这个操作在队列清空前是不会停止的。这也就意味着，错误的使用 process.nextTick()方法会导致 node 进入一个死循环。。直到内存泄漏。</p>
<p>那么合适使用这个方法比较合适呢？下面有一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> server = net.createServer(<span class="hljs-function">() =></span> &#123;&#125;).listen(<span class="hljs-number">8080</span>);

server.on(<span class="hljs-string">"listening"</span>, <span class="hljs-function">() =></span> &#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子中当，当 listen 方法被调用时，除非端口被占用，否则会立刻绑定在对应的端口上。这意味着此时这个端口可以立刻触发 listening 事件并执行其回调。然而，这时候 on('listening)还没有将 callback 设置好，自然没有 callback 可以执行。为了避免出现这种情况，node 会在 listen 事件中使用 process.nextTick()方法，确保事件在回调函数绑定后被触发。</p>
<p>setTimeout()和 setImmediate()
在三个方法中，这两个方法最容易被弄混。实际上，某些情况下这两个方法的表现也非常相似。然而实际上，这两个方法的意义却大为不同。</p>
<p>setTimeout()方法是定义一个回调，并且希望这个回调在我们所指定的时间间隔后第一时间去执行。注意这个“第一时间执行”，这意味着，受到操作系统和当前执行任务的诸多影响，该回调并不会在我们预期的时间间隔后精准的执行。执行的时间存在一定的延迟和误差，这是不可避免的。node 会在可以执行 timer 回调的第一时间去执行你所设定的任务。</p>
<p>setImmediate()方法从意义上将是立刻执行的意思，但是实际上它却是在一个固定的阶段才会执行回调，即 poll 阶段之后。有趣的是，这个名字的意义和之前提到过的 process.nextTick()方法才是最匹配的。node 的开发者们也清楚这两个方法的命名上存在一定的混淆，他们表示不会把这两个方法的名字调换过来---因为有大量的 ndoe 程序使用着这两个方法，调换命名所带来的好处与它的影响相比不值一提。</p>
<p>setTimeout()和不设置时间间隔的 setImmediate()表现上及其相似。猜猜下面这段代码的结果是什么？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"timeout"</span>);
&#125;, <span class="hljs-number">0</span>);

setImmediate(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"immediate"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上，答案是不一定。没错，就连 node 的开发者都无法准确的判断这两者的顺序谁前谁后。这取决于这段代码的运行环境。运行环境中的各种复杂的情况会导致在同步队列里两个方法的顺序随机决定。但是，在一种情况下可以准确判断两个方法回调的执行顺序，那就是在一个 I/O 事件的回调中。下面这段代码的顺序永远是固定的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

fs.readFile(__filename, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"timeout"</span>);
  &#125;, <span class="hljs-number">0</span>);
  setImmediate(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"immediate"</span>);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案永远是：</p>
<p>immediate</p>
<p>timeout</p>
<p>因为在 I/O 事件的回调中，setImmediate 方法的回调永远在 timer 的回调前执行。</p>
<h2 data-id="heading-27">七、处理海量数据</h2>
<blockquote>
<p>如何在保证页面运行流畅的情况下处理海量数据</p>
</blockquote>
<p>如果要在前端呈现大量的数据，一般的策略就是分页。前端要呈现百万数据，这个需求是很少见的，但是展示千条稍微复杂点的数据，这种需求还是比较常见，只要内存够，javascript 肯定是吃得消的，计算几千上万条数据，js 效率根本不在话下，但是 DOM 的渲染浏览器扛不住，CPU 稍微搓点的电脑必然会卡爆。</p>
<p>策略：显示三屏数据，其他的移除 DOM。</p>
<h3 data-id="heading-28">7.1 策略</h3>
<p>下面是我简单勾画的一个草图，我们把一串数据放到一个容器当中，这串数据的高度（Data List）肯定是比 Container 的高度要高很多的，如果我们一次性把数据都显示出来，浏览器需要花费大量的时间来计算每个 data 的位置，并且依次渲染出来，整个过程中 JS 并没有花费太多的时间，开销主要是 DOM 渲染。</p>
<p>为了解决这个问题，我们让数据是显示一部分，这一部分是 Container 可视区域的内容，以及上下各一屏（一屏指的是 Container 高度所能容纳的区域大小）的缓存内容。如果 Container 比较高，也可是只缓存半屏，缓存的原因是，在我们滚动滚动条的时候，js 需要时间来拼凑字符串（或者创建 Node ），这个时候浏览器还来不及渲染，所以会出现临时的空白，这种体验是相当不好的。</p>
<h3 data-id="heading-29">7.2 Demo</h3>
<pre><code class="hljs language-js copyable" lang="js"><title>百万数据前端快速流畅显示</title>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-id">#box</span> &#123;<span class="hljs-attribute">position</span>: relative; <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>; <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>; <span class="hljs-attribute">border</span>:<span class="hljs-number">1px</span> solid <span class="hljs-number">#CCC</span>; <span class="hljs-attribute">overflow</span>: auto&#125;
<span class="hljs-selector-id">#box</span> <span class="hljs-selector-tag">div</span> &#123; <span class="hljs-attribute">position</span>: absolute; <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>; <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>; <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>; <span class="hljs-attribute">overflow</span>: hidden; <span class="hljs-attribute">font</span>: <span class="hljs-number">16px</span>/<span class="hljs-number">20px</span> Courier;&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> total = <span class="hljs-number">1e5</span>
  , len = total
  , height = <span class="hljs-number">300</span>
  , delta = <span class="hljs-number">20</span>
  , num = height / delta
  , data = [];

<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < total; i++)&#123;
    data.push(&#123;<span class="hljs-attr">content</span>: <span class="hljs-string">"item-"</span> + i&#125;);
&#125;

<span class="hljs-keyword">var</span> box = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"box"</span>);
box.onscroll = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> sTop = box.scrollTop||<span class="hljs-number">0</span>
      , first = <span class="hljs-built_in">parseInt</span>(sTop / delta, <span class="hljs-number">10</span>)
      , start = <span class="hljs-built_in">Math</span>.max(first - num, <span class="hljs-number">0</span>)
      , end = <span class="hljs-built_in">Math</span>.min(first + num, len - <span class="hljs-number">1</span>)
      , i = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> s = start; s <= end; s++)&#123;
        <span class="hljs-keyword">var</span> child = box.children[s];
        <span class="hljs-keyword">if</span>(!box.contains(child) && s != len - <span class="hljs-number">1</span>)&#123;
            insert(s);
        &#125;
    &#125;

    <span class="hljs-keyword">while</span>(child = box.children[i++])&#123;
        <span class="hljs-keyword">var</span> index = child.getAttribute(<span class="hljs-string">"data-index"</span>);
        <span class="hljs-keyword">if</span>((index > end || index < start) && index != len - <span class="hljs-number">1</span>)&#123;
            box.removeChild(child);
        &#125;
    &#125;

&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insert</span>(<span class="hljs-params">i</span>)</span>&#123;
    <span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
    div.setAttribute(<span class="hljs-string">"data-index"</span>, i);
    div.style.top = delta * i + <span class="hljs-string">"px"</span>;
    div.appendChild(<span class="hljs-built_in">document</span>.createTextNode(data[i].content));
    box.appendChild(div);
&#125;

box.onscroll();
insert(len - <span class="hljs-number">1</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">7.3 算法说明</h3>
<ul>
<li>
<p>计算 start 和 end 节点</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a659deaf5814aca8f46e5e25120b46f~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
Container 可以容纳的 Data 数目为 num = height / delta，Container 顶部第一个节点的索引值为</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> first = <span class="hljs-built_in">parseInt</span>(Container.scrollTop / delta);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我们上下都有留出一屏，所以</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> start = <span class="hljs-built_in">Math</span>.max(first - num, <span class="hljs-number">0</span>);
<span class="hljs-keyword">var</span> end = <span class="hljs-built_in">Math</span>.min(first + num, len - <span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>插入节点</p>
<p>通过上面的计算，从 start 到 end 将节点一次插入到 Container 中，并且将最后一个节点插入到 DOM 中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 插入最后一个节点</span>
insert(len - <span class="hljs-number">1</span>);
<span class="hljs-comment">// 插入从 start 到 end 之间的节点</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> s = start; s <= end; s++) &#123;
  <span class="hljs-keyword">var</span> child = Container.children[s];
  <span class="hljs-comment">// 如果 Container 中已经有该节点，或者该节点为最后一个节点则跳过</span>
  <span class="hljs-keyword">if</span> (!Container.contains(child) && s != len - <span class="hljs-number">1</span>) &#123;
    insert(s);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里解释下为什么要插入最后一个节点，插入节点的方式是：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insert</span>(<span class="hljs-params">i</span>)</span>&#123;
<span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
div.setAttribute(<span class="hljs-string">"data-index"</span>, i);
div.style.top = delta \* i + <span class="hljs-string">"px"</span>;
div.appendChild(<span class="hljs-built_in">document</span>.createTextNode(data[i].content));
Container.appendChild(div);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到我们给插入的节点都加了一个 top 属性，最后一个节点的 top 是最大的，只有把这个节点插入到 DOM 中，才能让滚动条拉长，让人感觉放了很多的数据。</p>
</li>
<li>
<p>删除节点</p>
<p>为了减少浏览器的重排（reflow），我们可以隐藏三屏之外的数据。我这里为了方便，直接给删除掉了，后续需要再重新插入。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">while</span> ((child = Container.children[i++])) &#123;
  <span class="hljs-keyword">var</span> index = child.getAttribute(<span class="hljs-string">"data-index"</span>);
  <span class="hljs-comment">// 这里记得不要把最后一个节点给删除掉了</span>
  <span class="hljs-keyword">if</span> ((index > end || index < start) && index != len - <span class="hljs-number">1</span>) &#123;
    Container.removeChild(child);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 DOM 加载完毕之后，触发一次 Container.onscroll()，然后整个程序就 OK 了。</p>
</li>
</ul>
<h1 data-id="heading-31">第五章 「重学 JavaScript」语法和 API</h1>
<h2 data-id="heading-32">一、ECMAScript 和 JavaScript</h2>
<blockquote>
<p>理解 ECMAScript 和 JavaScript 的关系</p>
</blockquote>
<p>一个常见的问题是，ECMAScript 和 JavaScript 到底是什么关系？</p>
<p>要讲清楚这个问题，需要回顾历史。1996 年 11 月，JavaScript 的创造者 Netscape 公司，决定将 JavaScript 提交给标准化组织 ECMA，希望这种语言能够成为国际标准。次年，ECMA 发布 262 号标准文件（ECMA-262）的第一版，规定了浏览器脚本语言的标准，并将这种语言称为 ECMAScript，这个版本就是 1.0 版。</p>
<p>该标准从一开始就是针对 JavaScript 语言制定的，但是之所以不叫 JavaScript，有两个原因。一是商标，Java 是 Sun 公司的商标，根据授权协议，只有 Netscape 公司可以合法地使用 JavaScript 这个名字，且 JavaScript 本身也已经被 Netscape 公司注册为商标。二是想体现这门语言的制定者是 ECMA，不是 Netscape，这样有利于保证这门语言的开放性和中立性。</p>
<p>因此，ECMAScript 和 JavaScript 的关系是，前者是后者的规格，后者是前者的一种实现（另外的 ECMAScript 方言还有 JScript 和 ActionScript）。日常场合，这两个词是可以互换的。</p>
<h2 data-id="heading-33">二、ES6</h2>
<blockquote>
<p>熟练运用 es5、es6 提供的语法规范</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwangdoc.com%2Fjavascript%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://wangdoc.com/javascript/" ref="nofollow noopener noreferrer">JavaScript 教程</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fes6.ruanyifeng.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://es6.ruanyifeng.com/" ref="nofollow noopener noreferrer">ECMAScript 6 入门</a></p>
<h2 data-id="heading-34">三、setInterval</h2>
<blockquote>
<p>setInterval 需要注意的点，使用 settimeout 实现 setInterval</p>
</blockquote>
<h3 data-id="heading-35">3.1 setInterval 需要注意的点</h3>
<p>在使用 setInterval 方法时，每一次启动都需要对 setInterval 方法返回的值做一个判断，判断是否是空值，若不是空值，则要停止定时器并将值设为空，再重新启动，如果不进行判断并赋值，有可能会造成计时器循环调用，在同等的时间内同时执行调用的代码，并会随着代码的运行时间增加而增加，导致功能无法实现，甚至占用过多资源而卡死奔溃。因此在每一次使用 setInterval 方法时，都需要进行一次判断。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> timer = <span class="hljs-built_in">setInterval</span>(func, <span class="hljs-number">1000</span>);
<span class="hljs-comment">// 在其他地方再次用到setInterval(func, 1000)</span>
<span class="hljs-keyword">if</span> (timer !== <span class="hljs-literal">null</span>) &#123;
  <span class="hljs-built_in">clearInterval</span>(timer);
  timer = <span class="hljs-literal">null</span>;
&#125;
timer = <span class="hljs-built_in">setInterval</span>(func, <span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">3.2 使用 settimeout 实现 setInterval</h3>
<pre><code class="hljs language-js copyable" lang="js">setIntervalFunc = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>); <span class="hljs-comment">//使用递归</span>
  <span class="hljs-built_in">setTimeout</span>(setIntervalFunc, <span class="hljs-number">1000</span>);
&#125;;
<span class="hljs-built_in">setInterval</span>();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">四、正则表达式</h2>
<blockquote>
<p>JavaScript 提供的正则表达式 API、可以使用正则表达式（邮箱校验、URL 解析、去重等）解决常见问题</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwangdoc.com%2Fjavascript%2Fstdlib%2Fregexp.html" target="_blank" rel="nofollow noopener noreferrer" title="https://wangdoc.com/javascript/stdlib/regexp.html" ref="nofollow noopener noreferrer">RegExp 对象</a></p>
<h2 data-id="heading-38">五、错误处理</h2>
<blockquote>
<p>JavaScript 异常处理的方式，统一的异常处理方案</p>
</blockquote>
<p>当 JavaScript 引擎执行 JavaScript 代码时，有可能会发生各种异常，例如是语法异常，语言中缺少的功能，由于来自服务器或用户的异常输出而导致的异常。</p>
<p>而 Javascript 引擎是单线程的，因此一旦遇到异常，Javascript 引擎通常会停止执行，阻塞后续代码并抛出一个异常信息，因此对于可预见的异常，我们应该捕捉并正确展示给用户或开发者。</p>
<h3 data-id="heading-39">5.1 Error 对象</h3>
<p>throw 和 Promise.reject() 可以抛出字符串类型的异常，而且可以抛出一个 Error 对象类型的异常。</p>
<p>一个 Error 对象类型的异常不仅包含一个异常信息，同时也包含一个追溯栈这样你就可以很容易通过追溯栈找到代码出错的行数了。</p>
<p>所以推荐抛出 Error 对象类型的异常，而不是字符串类型的异常。</p>
<p>创建自己的异常构造函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyError</span>(<span class="hljs-params">message</span>) </span>&#123;
  <span class="hljs-keyword">var</span> instance = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(message);
  instance.name = <span class="hljs-string">"MyError"</span>;
  <span class="hljs-built_in">Object</span>.setPrototypeOf(instance, <span class="hljs-built_in">Object</span>.getPrototypeOf(<span class="hljs-built_in">this</span>));
  <span class="hljs-keyword">return</span> instance;
&#125;

MyError.prototype = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">Error</span>.prototype, &#123;
  <span class="hljs-attr">constructor</span>: &#123;
    <span class="hljs-attr">value</span>: MyError,
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;);

<span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.setPrototypeOf) &#123;
  <span class="hljs-built_in">Object</span>.setPrototypeOf(MyError, <span class="hljs-built_in">Error</span>);
&#125; <span class="hljs-keyword">else</span> &#123;
  MyError.__proto__ = <span class="hljs-built_in">Error</span>;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> MyError;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在代码中抛出自定义的异常类型并捕捉</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> MyError(<span class="hljs-string">"some message"</span>);
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  <span class="hljs-built_in">console</span>.log(e.name + <span class="hljs-string">":"</span> + e.message);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">5.2 Throw</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">throw</span> expression;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>throw 语句用来抛出一个用户自定义的异常。当前函数的执行将被停止（throw 之后的语句将不会执行），并且控制将被传递到调用堆栈中的第一个 catch 块。如果调用者函数中没有 catch 块，程序将会终止。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"before throw error"</span>);
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"throw error"</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"after throw error"</span>);
&#125; <span class="hljs-keyword">catch</span> (err) &#123;
  <span class="hljs-built_in">console</span>.log(err.message);
&#125;

<span class="hljs-comment">// before throw error</span>
<span class="hljs-comment">// throw error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">5.3 Try / Catch</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
try_statements
&#125;
[<span class="hljs-keyword">catch</span> (exception) &#123;
catch_statements
&#125;][<span class="hljs-keyword">finally</span> &#123;
  finally_statements
&#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>try/catch 主要用于捕捉异常。try/catch 语句包含了一个 try 块, 和至少有一个 catch 块或者一个 finally 块，下面是三种形式的 try 声明:</p>
<ul>
<li>try...catch</li>
<li>try...finally</li>
<li>try...catch...finally</li>
</ul>
<p>try 块中放入可能会产生异常的语句或函数</p>
<p>catch 块中包含要执行的语句，当 try 块中抛出异常时，catch 块会捕捉到这个异常信息，并执行 catch 块中的代码，如果在 try 块中没有异常抛出，这 catch 块将会跳过。</p>
<p>finally 块在 try 块和 catch 块之后执行。无论是否有异常抛出或着是否被捕获它总是执行。当在 finally 块中抛出异常信息时会覆盖掉 try 块中的异常信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"can not find it1"</span>);
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"can not find it2"</span>);
  &#125;
&#125; <span class="hljs-keyword">catch</span> (err) &#123;
  <span class="hljs-built_in">console</span>.log(err.message);
&#125;

<span class="hljs-comment">// can not find it2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果从 finally 块中返回一个值，那么这个值将会成为整个 try-catch-finally 的返回值，无论是否有 return 语句在 try 和 catch 中。这包括在 catch 块里抛出的异常。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"can not find it1"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"can not find it2"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">3</span>;
  &#125;
&#125;

<span class="hljs-built_in">console</span>.log(test()); <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Try / Catch 性能</p>
<p>有一个大家众所周知的反优化模式就是使用 try/catch。</p>
<p>在 V8（其他 JS 引擎也可能出现相同情况）函数中使用了 try/catch 语句不能够被 V8 编译器优化。</p>
<h3 data-id="heading-42">5.4 window.onerror</h3>
<p>通过在 window.onerror 上定义一个事件监听函数，程序中其他代码产生的未被捕获的异常往往就会被 window.onerror 上面注册的监听函数捕获到。并且同时捕获到一些关于异常的信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">message, source, lineno, colno, error</span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>message：异常信息（字符串）</li>
<li>source：发生异常的脚本 URL（字符串）</li>
<li>lineno：发生异常的行号（数字）</li>
<li>colno：发生异常的列号（数字）</li>
<li>error：Error 对象（对象）</li>
</ul>
<p>注意：Safari 和 IE10 还不支持在 window.onerror 的回调函数中使用第五个参数，也就是一个 Error 对象并带有一个追溯栈</p>
<p>try/catch 不能够捕获异步代码中的异常，但是其将会把异常抛向全局然后 window.onerror 可以将其捕获。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"some message"</span>);
  &#125;, <span class="hljs-number">0</span>);
&#125; <span class="hljs-keyword">catch</span> (err) &#123;
  <span class="hljs-built_in">console</span>.log(err);
&#125;
<span class="hljs-comment">// Uncaught Error: some message</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.onerror = <span class="hljs-function">(<span class="hljs-params">msg, url, line, col, err</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(err);
&#125;;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"some message"</span>);
&#125;, <span class="hljs-number">0</span>);
<span class="hljs-comment">// Error: some message</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Chrome 中，window.onerror 能够检测到从别的域引用的 script 文件中的异常，并且将这些异常标记为 Script error。如果你不想处理这些从别的域引入的 script 文件，那么可以在程序中通过 Script error 标记将其过滤掉。然而，在 Firefox、Safari 或者 IE11 中，并不会引入跨域的 JS 异常，即使在 Chrome 中，如果使用 try/catch 将这些讨厌的代码包围，那么 Chrome 也不会再检测到这些跨域异常。</p>
<p>在 Chrome 中，如果你想通过 window.onerror 来获取到完整的跨域异常信息，那么这些跨域资源必须提供合适的跨域头信息。</p>
<h3 data-id="heading-43">5.5 Promise 中的异常</h3>
<ul>
<li>
<p>Promise 中抛出异常</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  reject();
&#125;);
<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  reject();
&#125;);
<span class="hljs-built_in">Promise</span>.reject();
<span class="hljs-keyword">throw</span> expression;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Promise 中捕捉异常</p>
<pre><code class="hljs language-js copyable" lang="js">promiseObj.then(<span class="hljs-literal">undefined</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
  catch_statements;
&#125;);
promiseObj.catch(<span class="hljs-function">(<span class="hljs-params">exception</span>) =></span> &#123;
  catch_statements;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 JavaScript 函数中，只有 return / yield / throw 会中断函数的执行，其他的都无法阻止其运行到结束的。</p>
<p>在 resolve / reject 之前加上 return 能阻止往下继续运行。</p>
<p>without return：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve()
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"before excute reject"</span>);
    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"throw error"</span>));
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"after excute reject"</span>);
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err.message);
  &#125;);

<span class="hljs-comment">// before excute reject</span>
<span class="hljs-comment">// throw error</span>
<span class="hljs-comment">// after excute reject</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>use return：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve()
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"before excute reject"</span>);
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"throw error"</span>));
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"after excute reject"</span>);
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err.message);
  &#125;);

<span class="hljs-comment">// before excute reject</span>
<span class="hljs-comment">// throw error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Throw or Reject</p>
<p>无论是 try/catch 还是 promise 都能捕获到的是“同步”异常</p>
<p>reject 是回调，而 throw 只是一个同步的语句，如果在另一个异步的上下文中抛出，在当前上下文中是无法捕获到的。</p>
<p>因此在 Promise 中使用 reject 抛出异常。否则 catch 有可能会捕捉不到。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve()
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"throw error"</span>);
    &#125;, <span class="hljs-number">0</span>);
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
  &#125;);

<span class="hljs-comment">// Uncaught Error: throw error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve()
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"throw error"</span>));
      &#125;, <span class="hljs-number">0</span>);
    &#125;);
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
  &#125;);

<span class="hljs-comment">// Error: throw error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-44">5.6 window.onunhandledrejection</h3>
<p>window.onunhandledrejection 与 window.onerror 类似，在一个 JavaScript Promise 被 reject 但是没有 catch 来捕捉这个 reject 时触发。并且同时捕获到一些关于异常的信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.onunhandledrejection = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(event.reason);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>event 事件是 PromiseRejectionEvent 的实例，它有两个属性：</p>
<ul>
<li>event.promise：被 rejected 的 JavaScript Promise</li>
<li>event.reason：一个值或 Object 表明为什么 promise 被 rejected，是 Promise.reject() 中的内容。</li>
</ul>
<h3 data-id="heading-45">5.7 window.rejectionhandled</h3>
<p>因为 Promise 可以延后调用 catch 方法，若在抛出 reject 时未调用 catch 进行捕捉，但稍后再次调用 catch，此时会触发 rejectionhandled 事件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.onrejectionhandled = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"rejection handled"</span>);
&#125;;

<span class="hljs-keyword">let</span> p = <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"throw error"</span>));

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  p.catch(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(e);
  &#125;);
&#125;, <span class="hljs-number">1000</span>);

<span class="hljs-comment">// Uncaught (in promise) Error: throw error</span>
<span class="hljs-comment">// 1 秒后输出</span>
<span class="hljs-comment">// Error: throw error</span>
<span class="hljs-comment">// rejection handled</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-46">5.8 统一异常处理</h3>
<p>代码中抛出的异常，一种是要展示给用户，一种是展示给开发者。</p>
<p>对于展示给用户的异常，一般使用 alert 或 toast 展示；对于展示给开发者的异常，一般输出到控制台。</p>
<p>在一个函数或一个代码块中可以把抛出的异常统一捕捉起来，按照不同的异常类型以不同的方式展示，对于。</p>
<p>需要点击确认的异常类型：</p>
<p>ensureError.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">EnsureError</span>(<span class="hljs-params">message = <span class="hljs-string">"Default Message"</span></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">"EnsureError"</span>;
  <span class="hljs-built_in">this</span>.message = message;
  <span class="hljs-built_in">this</span>.stack = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>().stack;
&#125;
EnsureError.prototype = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">Error</span>.prototype);
EnsureError.prototype.constructor = EnsureError;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> EnsureError;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>弹窗提示的异常类型：</p>
<p>toastError.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ToastError</span>(<span class="hljs-params">message = <span class="hljs-string">"Default Message"</span></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">"ToastError"</span>;
  <span class="hljs-built_in">this</span>.message = message;
  <span class="hljs-built_in">this</span>.stack = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>().stack;
&#125;
ToastError.prototype = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">Error</span>.prototype);
ToastError.prototype.constructor = ToastError;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> ToastError;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示开发者的异常类型：</p>
<p>devError.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">DevError</span>(<span class="hljs-params">message = <span class="hljs-string">"Default Message"</span></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">"ToastError"</span>;
  <span class="hljs-built_in">this</span>.message = message;
  <span class="hljs-built_in">this</span>.stack = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>().stack;
&#125;
DevError.prototype = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">Error</span>.prototype);
DevError.prototype.constructor = DevError;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> DevError;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>异常处理器：</p>
<p>抛出普通异常时，可以带上 stackoverflow 上问题的列表，方便开发者查找原因。</p>
<p>errorHandler.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> EnsureError <span class="hljs-keyword">from</span> <span class="hljs-string">"./ensureError.js"</span>;
<span class="hljs-keyword">import</span> ToastError <span class="hljs-keyword">from</span> <span class="hljs-string">"./toastError.js"</span>;
<span class="hljs-keyword">import</span> DevError <span class="hljs-keyword">from</span> <span class="hljs-string">"./devError.js"</span>;
<span class="hljs-keyword">import</span> EnsurePopup <span class="hljs-keyword">from</span> <span class="hljs-string">"./ensurePopup.js"</span>;
<span class="hljs-keyword">import</span> ToastPopup <span class="hljs-keyword">from</span> <span class="hljs-string">"./toastPopup.js"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">errorHandler</span>(<span class="hljs-params">err</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (err <span class="hljs-keyword">instanceof</span> EnsureError) &#123;
    EnsurePopup(err.message);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (err <span class="hljs-keyword">instanceof</span> ToastError) &#123;
    ToastPopup(err.message);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (err <span class="hljs-keyword">instanceof</span> DevError) &#123;
    DevError(err.message);
  &#125; <span class="hljs-keyword">else</span> &#123;
    error.message += <span class="hljs-string">`https://stackoverflow.com/questions?q=<span class="hljs-subst">$&#123;<span class="hljs-built_in">encodeURI</span>(
      error.message
    )&#125;</span>`</span>;
    <span class="hljs-built_in">console</span>.error(err.message);
  &#125;
&#125;

<span class="hljs-built_in">window</span>.onerror = <span class="hljs-function">(<span class="hljs-params">msg, url, line, col, err</span>) =></span> &#123;
  errorHandler(err);
&#125;;

<span class="hljs-built_in">window</span>.onunhandledrejection = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  errorHandler(event.reason);
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> errorHandler;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            