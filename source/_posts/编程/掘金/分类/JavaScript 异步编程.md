
---
title: 'JavaScript 异步编程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a20f6d92dd44deb87d2af6dfafb5cdf~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 19:46:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a20f6d92dd44deb87d2af6dfafb5cdf~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a name="user-content-WjOiM" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-0">内容概述</h2>
<p>众所周知目前主流javascript环境都是以单线程的模式去执行的javascript代码。
<a name="user-content-EZ5QH" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-1">采用单线程模式工作的原因</h3>
<p>采用单线程工作的原因与它最早的涉及初衷有关，最早的javascript语言就是一门运行在浏览器端的脚本语言，目的就是用来实现页面上的动态交互，而实现动态交互的核心就是Dom操作，这也就决定了必须使用单线程模型否则就会出现很复杂的线程同步问题。<br>假设我们同时有多个线程同时工作，有一个线程修改了某个Dom，另一个线程又删除了某个Dom，那么此时浏览器无法明确该以哪个线程的结果为准，所以为了避免这些问题，从一开始javascript就设计成了单线程模式去工作。</p>
<ul>
<li>单线程：单线程指的是在js执行环境中负责执行代码的环境只有一个。</li>
<li>优点：更安全更简单</li>
<li>缺点：耗时任务会阻塞执行</li>
</ul>
<p>为解决耗时任务阻塞执行的问题，javascript将任务的执行模式分为了两种。（同步模式，异步模式）。本文重点说的是在javascript与异步模式先关的内容。主要包括以下几点：</p>
<ul>
<li>同步模式(Synchronous)与异步模式(Asynchronous)</li>
<li>事件循环与消息队列</li>
<li>异步编程的几种方式</li>
<li>Promise 异步方案、宏任务、微任务队列</li>
<li>Generator 异步方案 、Async/await 语法糖</li>
</ul>
<p><a name="user-content-TIEYI" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-2">同步模式</h2>
<p>同步模式指的是我们代码中的任务依次执行，后一个任务就必须要等待前一个任务结束才能开始执行。执行顺序与我们代码的编码顺序完全一致。</p>
<ul>
<li>同步指的并不是同时执行，而是排队执行</li>
</ul>
<p>我们可以用代码来演示一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">"global begin"</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是foo"</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是bar"</span>);
  bar();
&#125;
foo();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"global end"</span>);

<span class="hljs-comment">//执行结果</span>
<span class="hljs-comment">// global begin</span>
<span class="hljs-comment">// 我是foo</span>
<span class="hljs-comment">// 我是bar</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行机制：</p>
<ul>
<li>开始执行JS执行引擎会把整体代码加载进来，然后在调用栈中压入一个匿名的调用(可以理解为把全部的代码放到了一个匿名函数中去执行)，接着开始逐行执行</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a20f6d92dd44deb87d2af6dfafb5cdf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>首先第一行遇到<code>console.log('global begin')</code>调用，它就会把<code>console.log('global begin')</code>压入我们的调用栈，控制台打印<code>global begin</code>执行完成之后弹栈，继续执行</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/004541e46ba3443287c4d010be6e2790~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>接着是两个函数声明，不管函数还是变量的声明都不会产生调用，接着往下执行。</p>
</li>
<li>
<p>再往下就是<code>foo()</code>函数的调用，和第一行一样，先压栈</p>
</li>
<li>
<p>在bar函数内部遇到<code>console.log("我是foo")</code>先压栈，控制台打印<code>我是foo</code>，然后弹栈。</p>
</li>
<li>
<p>接着遇到<code>bar()</code>函数调用，先压栈</p>
</li>
<li>
<p>在foo函数内部遇到<code>console.log("我是bar")</code>，压栈，控制台打印<code>我是bar</code>，然后弹栈</p>
</li>
<li>
<p>bar函数执行完毕,弹栈</p>
</li>
<li>
<p>接着bar函数执行完毕，弹栈</p>
</li>
<li>
<p>再往下遇到<code>console.log("global end")</code>，先压栈，控制台打印<code>global end"</code>，然后弹栈</p>
</li>
<li>
<p>整体代码全部执行完毕，我们代码就会清空掉</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cd937e47baf45f2ad437bef31d67e38~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>如果某一个任务或者某一行执行时间过长，就会出现阻塞，对用户而言就会出现页面卡顿或者卡死，因此就必须要有异步操作来解决不可避免的耗时操作。
<a name="user-content-qSpaU" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-3">异步模式</h2>
<ul>
<li>浏览器端的ajax操作</li>
<li>nodeJs中的大文件读写</li>
<li>定时任务 如setTimeout</li>
</ul>
<p><a name="user-content-80l5a" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-4">介绍</h3>
<ul>
<li>异步模式的api不会等待当前任务结束才开始执行下一个任务，对于耗时操作都是开启之后就立即执行下一个任务</li>
<li>耗时任务的后续逻辑一般通过回调函数的方式定义，等异步任务执行结束后就会调用回调函数。</li>
<li>异步模式对JavaScript非常重要，如果没有异步模式单线程的JavaScript语法就无法同时处理大量耗时任务</li>
<li>对于开发人员来说，异步模式下的代码执行顺序是跳跃式的，不会像同步代码那样通俗易懂。</li>
</ul>
<p>接下来我们看一段代码来分析异步模式是如何执行的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">"global begin"</span>);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timer1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"timer1 invoke"</span>);
&#125;, <span class="hljs-number">1800</span>);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timer2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"timer2 invoke"</span>);
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inner</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"inner invoke"</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;, <span class="hljs-number">1000</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"global end"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>最开始也是加载整体代码，然后压入全局匿名调用</li>
<li>然后<code>console.log("global begin")</code>压栈，控制台打印<code>global begin</code>，<code>console.log("global begin")</code>出栈。</li>
<li>接着压入<code>setTimeout(timer1)</code>压入调用栈，但是这个函数内部是异步调用，我们需要关心内部api做了什么事情，很明显在内部为time1开启了一个倒计时器，然后单独放到一边（这个计时器是单独工作的，并不会受JS单线程的影响）开启过后对于<code>setTimeout</code>来讲调用就完成了所以就会弹栈继续往下执行。</li>
<li>接着又遇到一个<code>setTimeout</code>调用，同理先压栈，然后开启另一个倒计时器，然后弹栈</li>
<li>最后又遇到<code>console.log("global end")</code>先压栈，控制台打印，然后弹栈</li>
<li>打印完最后的<code>global end</code>之后那么对于整体的匿名调用就执行了，那么清空调用栈</li>
<li>这个时候Event Loop就会发挥作用，负责监听调用栈和时间队列（一旦调用栈结束了，就从事件队列取出第一个回调函数，然后引入调用栈）</li>
<li>timer2计时器先结束，然后timer2函数放到消息队列的第一位</li>
<li>然后timer1计时器结束，将timer1函数放到消息队列的第二位</li>
<li>一旦消息队列发生变化，事件循环就会监听到并把消息队列的第一个函数（timer2）函数取出来，压入调用栈继续执行timer2（相当于开启了新一轮的的执行），执行过程和之前是一致的，如果遇到异步调用也是相同的情况。</li>
<li>往后就是不断的调用重复，直到调用栈和消息队列当中都没有需要执行的任务了，那整体任务就算结束。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5b59fa1e3ec4e789dbf2d570c3f6083~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>如图，JavaScript线程某个时刻发起异步调用，然后继续往后执行其他任务，同时异步线程会去执行异步任务，异步任务执行完成之后会把异步任务放入消息队列，js线程完成所有任务之后，会依次执行消息队列的任务（注意：JavaScript是单线程的而浏览器并不是单线程的，更具体说通过JavaScript调用的某些内部api并不是单线程的，例如上述这个倒计时器内部就会有一个单独的线程去进行倒数）。<br>
<br>异步模式对单线程的 JavaScript 非常重要，同时也是 JavaScript 的核心特点，也是因为异步模式 API 的关系，写出来的代码不容易读，执行顺序也会复杂很多，因此诞生了很多为异步而生的语法，特别是在es2015过后退出的一系列新语法，新特性，它们慢慢弥补了JavaScript这块的不足。
<a name="user-content-MN2b5" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-5">回调函数</h2>
<p><strong>回调函数</strong>是实现异步编程的根本方式，其实所有的异步方案的根本都是回调函数，回调函数可以理解为知道要执行什么事情，但是不知道这个事情依赖的任务什么时候完成，所以说最好的办法就是把这些事情的步骤写到一个函数（<strong>回调函数</strong>）当中，交给任务的执行者，执行者是知道什么时候结束的，等结束之后执行你想做的事情（<strong>回调函数</strong>）。以ajax为例子，ajax就是希望拿到数据之后去做一些处理，但是请求什么时候完成不知道，所以得把请求响应之后要执行的事情统一放到函数中，ajax执行完就会自动执行这个函数，这些由调用者定义，交给执行者执行的函数就被称之为回调函数，具体实现方法也很简单，就是把函数作为参数传递，只不过这种方式不利于阅读，而且执行顺序也会非常混乱。
<a name="user-content-a3dsd" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-6">Promise</h2>
<p>回调函数是JavaScript异步编程方式的根基，但是直接使用传统的回调函数方式去完成复杂的异步流程就会出现大量回调函数嵌套，这就会导致常说的的回调地狱问题，为了避免回调地狱的问题CommonJS社区就提出了Promise规范，目的就是为JavaScript提供一种更合理，更强大的异步编程方案，后来在es2015中被标准化，成为语言规范。<br>所谓Promise就是一个对象用来去表示一个异步任务最终结束过后最终是成功还是失败，就像是内部对外部做出了一个承诺，最开始承诺是待定状态（pending）最终可能成功（Fulfilled）也可能是失败（rejected），不管是成功还是失败都会有相应的反应onFulFilled、onRejected，在承诺结束之后都会有相应的任务被执行，而且还有一个明显的特点，就是一旦明确了结果就不可以被改变了。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebd684647d9845378c18dacf0fa1a150~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-7YbnK" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-7">基本使用</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Promise 基本示例</span>
<span class="hljs-comment">// Promise 的构造函数需要接受一个函数作为参数，这个函数就可以理解为对象承诺的逻辑</span>
<span class="hljs-comment">// 这个函数会在构造 Promise 的过程中被同步执行</span>
<span class="hljs-comment">// 这个函数接受两个参数 resolve/reject，分别将 Promise 的状态改为成功、失败</span>
<span class="hljs-comment">// 状态是确定的，也就是说只会调用 resolve/reject 之一</span>

<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// 这里用于“兑现”承诺</span>

  <span class="hljs-comment">// resolve(100) // 承诺达成</span>

  reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'promise rejected'</span>)) <span class="hljs-comment">// 承诺失败</span>
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-comment">// 即便没有异步操作，then 方法中传入的回调仍然会被放入队列，等待下一轮执行</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resolved'</span>, value)
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'rejected'</span>, error)
&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'end'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-CiY6G" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-8">ajax案例</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Promise 方式的 AJAX</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
    xhr.open(<span class="hljs-string">'GET'</span>, url)
    xhr.responseType = <span class="hljs-string">"json"</span>;
    xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-number">200</span>) &#123;
        resolve(<span class="hljs-built_in">this</span>.response)
      &#125; <span class="hljs-keyword">else</span> &#123;
        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-built_in">this</span>.statusText))
      &#125;
    &#125;
    xhr.send()
  &#125;);
&#125;

ajax(<span class="hljs-string">"/api/get.json"</span>).then(
  <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(response);
  &#125;,
  <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(error);
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-lpYlz" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-9">Promise常见误区</h3>
<p>从上述演示代码我们发现Promise本质上也是使用回调函数的方式去定义异步任务结束后所需要执行的任务，只不过这里的回调函数是通过then方法传递进去的，而且Promise将回调分为两种（onFulfilled,onReject）<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f30be24218204fad8c990c018342375a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>这时候我们思考后发现既然还是回调函数那如果我们需要连续串联执行多个异步任务这里仍然会出现回调函数嵌套的问题。</p>
<ul>
<li>按照传统的思考方式我们会出现这样的情况</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//嵌套使用 Promise 是最常见的误区</span>
ajax(<span class="hljs-string">'/api/urls.json'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">urls</span>) </span>&#123;
  ajax(urls.users).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">users</span>) </span>&#123;
    ajax(urls.users).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">users</span>) </span>&#123;
      ajax(urls.users).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">users</span>) </span>&#123;
        ajax(urls.users).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">users</span>) </span>&#123;

        &#125;)
      &#125;)
    &#125;)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>正确的做法是借助于Promise then()方法的链式调用的特点，尽量保证异步任务的扁平化</li>
</ul>
<p>正如我们前面所说一样，then()方法的作用就是为Promise对象去添加状态明确后的回调函数，其中失败后的回调函数是可以省略的，then方法最大的特点就是内部也会返回一个Promise对象，我们可以尝试一下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> promise = ajax(<span class="hljs-string">'/api/users.json'</span>)
<span class="hljs-keyword">var</span> promise2 = promise.then(
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onFulfilled</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onFulfilled'</span>, value)
  &#125;,
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onRejected</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRejected'</span>, error)
  &#125;
)

<span class="hljs-built_in">console</span>.log(promise2)
<span class="hljs-built_in">console</span>.log(promise2 === promise) <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们发现promise2和promise并不是同一个promise对象，then方法返回的是一个全新的promise对象，目的就是为了实现Promise的链条，例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ajax(<span class="hljs-string">"/api/users.json"</span>)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1111</span>);
  &#125;) <span class="hljs-comment">// => Promise</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2222</span>);
  &#125;) <span class="hljs-comment">// => Promise</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3333</span>);
  &#125;) <span class="hljs-comment">// => Promise</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4444</span>);
  &#125;);

<span class="hljs-comment">//1111</span>
<span class="hljs-comment">// 2222</span>
<span class="hljs-comment">// 3333</span>
<span class="hljs-comment">// 4444</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以在then方法内部手动返回一个Promise对象，例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ajax(<span class="hljs-string">'/api/users.json'</span>)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1111</span>)
    <span class="hljs-keyword">return</span> ajax(<span class="hljs-string">'/api/urls.json'</span>)
  &#125;) <span class="hljs-comment">// => Promise</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2222</span>)
    <span class="hljs-built_in">console</span>.log(value)
    <span class="hljs-keyword">return</span> ajax(<span class="hljs-string">'/api/urls.json'</span>)
  &#125;) <span class="hljs-comment">// => Promise</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3333</span>)
    <span class="hljs-keyword">return</span> ajax(<span class="hljs-string">'/api/urls.json'</span>)
  &#125;) <span class="hljs-comment">// => Promise</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4444</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">'foo'</span>
  &#125;) <span class="hljs-comment">// => Promise</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">5555</span>)
    <span class="hljs-built_in">console</span>.log(value)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ul>
<li>Promise对象的then方法会返回一个全新的Promise对象</li>
<li>后面的then方法就是在为上一个then返回的Promise注册回调</li>
<li>前面then方法回调函数的返回值会作为后面then方法回调的参数</li>
<li>如果回调当中返回的是Promise，那后面then方法的回调会等待它的结束</li>
</ul>
<p><a name="user-content-AeSv2" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-10">Promise 异常处理</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65d878536b7243fe91b318870b388a5b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>正如前面所说Promise结果一旦失败就会调用在<code>then</code>方法中传入的onRejected回调函数，例如在上述例子我们请求一个根本不存在的地址就会执行onRejected函数，除此之外我们在Promise执行的过程中出现了异常或者手动抛出了一个异常，那么onReject回调也会被执行。看如下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span> (<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-comment">// foo() 执行过程出现了异常，会执行 onReject回调</span>
     <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>() <span class="hljs-comment">// 尝试手动抛出一个异常 会执行 onReject回调</span>
    <span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
    xhr.open(<span class="hljs-string">'GET'</span>, url)
    xhr.responseType = <span class="hljs-string">'json'</span>
    xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-number">200</span>) &#123;
        resolve(<span class="hljs-built_in">this</span>.response)
      &#125; <span class="hljs-keyword">else</span> &#123;
        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-built_in">this</span>.statusText))
      &#125;
    &#125;
    xhr.send()
  &#125;)
&#125;

ajax(<span class="hljs-string">'/api/users11.json'</span>)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onFulfilled</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onFulfilled'</span>, value)
  &#125;)
  .then(<span class="hljs-literal">undefined</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onRejected</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRejected'</span>, error)
  &#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于onReject回调的注册其实还有一种更常用的用法，那就是promise实例的catch方法去注册onReject回调，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ajax(<span class="hljs-string">'/api/users11.json'</span>)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onFulfilled</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onFulfilled'</span>, value)
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onRejected</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRejected'</span>, error)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果同样可以正常捕获到异常，其实cath就是then的另一种体现，如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//then(onRejected) 实际上就相当于 then(undefined, onRejected)</span>

ajax(<span class="hljs-string">'/api/users11.json'</span>)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onFulfilled</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onFulfilled'</span>, value)
  &#125;)
  .then(<span class="hljs-literal">undefined</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onRejected</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRejected'</span>, error)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从结果来看我们没发现两者的区别，但是仔细对比就会发现有很大差异：</p>
<ul>
<li>因为每个<code>then</code>方法返回的都是一个全新的promise，我们在后边通过链式调用方式调用的catch实际是给前边<code>then</code>方法返回的Promise 执行失败的回调，并不是给第一个Promise对象指定的，只不过这是因为这是同一个Promise链条，前面Promise会一直被往后传递，所以才能捕获到第一个Promise的异常，而通过<code>then</code>第二个参数指定的回调函数 只是给当前Promise指定的异常</li>
</ul>
<p><a name="user-content-HGeLY" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-11">Promise 静态方法</h2>
<p><a name="user-content-cWCWO" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-12">Promise.resolve</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//直接返回状态为fulfilled的 Promise对象  foo就会作为这个promise 所返回的值</span>
<span class="hljs-comment">//也就是说我们在onFulFilled回调中的拿到的参数就是foo</span>
<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'foo'</span>) 
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(value)
  &#125;)

<span class="hljs-comment">//上述代码等价于</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve,reject</span>)</span>&#123;
resolve(<span class="hljs-string">'foo'</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">//foo</span>
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外如果<code>Promise.resolve</code>接收到的是另一个Promise对象那么这个Promise对象就会原样返回，例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">var</span> promise = ajax(<span class="hljs-string">'/api/users.json'</span>)
<span class="hljs-keyword">var</span> promise2 = <span class="hljs-built_in">Promise</span>.resolve(promise)
<span class="hljs-built_in">console</span>.log(promise === promise2) <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有如果我们传入的是一个对象，而且也拥有和promise同样的<code>then</code>方法，那这个对象也可以作为一个Promise被执行，例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Promise</span>.resolve(&#123;
 <span class="hljs-attr">then</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onFulFilled,onRejected</span>)</span>&#123;
    onFulFilled(<span class="hljs-string">"foo"</span>)
 &#125;
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(value)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带有这种then方法的对象可以说是实现了 一个thenable的接口，支持这种对象的原因是因为原生promise没有普及之前都是使用第三方的库实现的Promise，如果说需要把第三方的Promise对象转换成原声的就可以借用这种机制。
<a name="user-content-dtL0o" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-13">promise.reject：</h3>
<p>快速创建一个一定失败的Promise对象,无论传入什么参数都作为Promise失败的理由
<a name="user-content-CSWd8" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-14">并行执行</h2>
<p><a name="user-content-KdZ7y" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-15">Promise.all</h3>
<p>如果我们需要并行执行多个异步任务，比如任务之间没有什么依赖，最好的选择就是同时请求多个接口。代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ajax(<span class="hljs-string">'/api/users.json'</span>)
 ajax(<span class="hljs-string">'/api/posts.json'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是会有问题，那我们怎么去判断所有的请求都已经结束的时机，传统做法是定义一个计数器，没成功一个请求就让它加一下，知道计数器和请求的数量相等时就表示所有任务都结束了，这种办法会非常麻烦还需要考虑出现异常的情况，为此我们可以使用Promise的<code>all</code>方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> promise = <span class="hljs-built_in">Promise</span>.all([
  ajax(<span class="hljs-string">'/api/users.json'</span>),
  ajax(<span class="hljs-string">'/api/posts.json'</span>)
])

promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">values</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(values)
&#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>all方法接收一个数组，数组中的每个元素都是一个Promise对象，这个方法会返回一个全新的Promise对象，当内部所有的Promise完成过后，我们返回的Promise才会完成，此时Promise对象拿到的结果就是一个数组，这个数组包含每个Promise的结果（只有全部的Promise执行完成才会触发），如果其中有一个Promise异常那么整个Proimse就会失败（rejected），代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ajax(<span class="hljs-string">'/api/urls.json'</span>)
  .then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-keyword">const</span> urls = <span class="hljs-built_in">Object</span>.values(value)
    <span class="hljs-keyword">const</span> tasks = urls.map(<span class="hljs-function"><span class="hljs-params">url</span> =></span> ajax(url))
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(tasks)
  &#125;)
  .then(<span class="hljs-function"><span class="hljs-params">values</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(values)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-S19R8" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-16">Promise.race</h3>
<p>与Promise.all方法不同的是promise.rece跟着所有任务中第一个完成的Promise执行，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Promise.race 实现超时控制</span>

<span class="hljs-keyword">const</span> request = ajax(<span class="hljs-string">'/api/posts.json'</span>)
<span class="hljs-keyword">const</span> timeout = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'timeout'</span>)), <span class="hljs-number">500</span>)
&#125;)

<span class="hljs-built_in">Promise</span>.race([
  request,
  timeout
])
.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(value)
&#125;)
.catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-lIrkq" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-17">Generator</h2>
<p>相比与传统的回调函数的方式，Promise处理异步调用最大的方式就是可以通过链式调用解决回调嵌套的问题。但是这样子仍然会有大量大的回调函数，如<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15afae6faf094b99a06d2bd99dc25fef~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>还是没有办法达到传统同步代码的可读性，传统的同步代码方式，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21e6b9ed6a444d839014c13bfa549929~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>下面我们说两种更优的异步编程写法
<a name="user-content-MqSXv" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-18">Generator 生产器函数</h3>
<ul>
<li>当我们调用生成器函数时，不会立即执行，而是得到一个生成器对象；</li>
<li>直到我们调用生成器对象的 next 方法，这个函数才会开始执行；</li>
<li>其次就是可以在函数内部使用 yield 向外返回一个值，另外在返回值中还有一个 done 属性，表示函数是否全部执行完成；</li>
<li>yield 不会像传统的 return 那样结束函数的执行，只是暂停函数的执行，直到外界下一次调用 next 方法时继续从 yield 的位置执行，</li>
<li>如果在 next 函数中传入一个参数，这个参数可以在 yield 左侧接收；</li>
<li>如果调用  generator.throw，生成器函数会抛出一个异常，如果不捕获就会直接停止当前执行；</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-keyword">function</span> * <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'test'</span>)
    <span class="hljs-keyword">const</span> req1 = <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>
    <span class="hljs-built_in">console</span>.log(req1)
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> req2 = <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>
      <span class="hljs-built_in">console</span>.log(req2)
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">console</span>.log(error)
    &#125;
    <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>
  &#125;
  <span class="hljs-comment">// 以下不会立即执行</span>
  <span class="hljs-keyword">const</span> generator  = test()
  <span class="hljs-built_in">console</span>.log(generator.next())
  <span class="hljs-comment">// test</span>
  <span class="hljs-comment">// &#123;value: 1, done: false&#125;</span>
  <span class="hljs-built_in">console</span>.log(generator.next(<span class="hljs-string">'传入A'</span>))
  <span class="hljs-comment">// 传入A</span>
  <span class="hljs-comment">// &#123;value: 2, done: false&#125;</span>
  generator.throw(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Generator Error'</span>))
  <span class="hljs-comment">// Error: Generator Error</span>
  <span class="hljs-comment">//     at eval (eval at <anonymous> (VM1178:8), <anonymous>:17:17)</span>
  <span class="hljs-comment">//     at VM1179:18</span>
  <span class="hljs-comment">// &#123;value: 3, done: false&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-WDCk9" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-19"><strong>使用 Generator 管理异步流程：</strong></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timeOut</span> (<span class="hljs-params">id</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"小明"</span> + id, <span class="hljs-attr">age</span>: id, <span class="hljs-attr">id</span>: id &#125;)
      &#125;, <span class="hljs-number">1000</span>)
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">main</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 第一个异步函数以及处理</span>
    <span class="hljs-keyword">const</span> res1 = <span class="hljs-keyword">yield</span> timeOut(<span class="hljs-number">1</span>)
    <span class="hljs-built_in">console</span>.log(res1)
    <span class="hljs-comment">// 第二个异步函数以及处理</span>
    <span class="hljs-keyword">const</span> res2 = <span class="hljs-keyword">yield</span> timeOut(<span class="hljs-number">12</span>)
    <span class="hljs-built_in">console</span>.log(res2)
    <span class="hljs-comment">// 第三个异步函数以及处理</span>
    <span class="hljs-keyword">const</span> res3 = <span class="hljs-keyword">yield</span> timeOut(<span class="hljs-number">18</span>)
    <span class="hljs-built_in">console</span>.log(res3)
    <span class="hljs-comment">// 第四个异步函数以及处理</span>
    <span class="hljs-keyword">const</span> res4 = <span class="hljs-keyword">yield</span> timeOut(<span class="hljs-number">24</span>)
    <span class="hljs-built_in">console</span>.log(res4)
  &#125;
  <span class="hljs-keyword">const</span> generator = main()
  <span class="hljs-keyword">const</span> res1 = generator.next()
  res1.value.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-keyword">const</span> res2 = generator.next(data)
    res2.value.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-keyword">const</span> res3 = generator.next(data)
      res3.value.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
        generator.next(data)
      &#125;)
    &#125;)
  &#125;)
  <span class="hljs-comment">// 依次输出：</span>
  <span class="hljs-comment">// &#123;name: "小明1", age: 1, id: 1&#125;</span>
  <span class="hljs-comment">// &#123;name: "小明12", age: 12, id: 12&#125;</span>
  <span class="hljs-comment">// &#123;name: "小明18", age: 18, id: 18&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述例子中，我们使用生成器函数把 Promise 的回调函数写在了 yield 后，实现了异步问题的代码简化，对于生成器函数的回调可以使用递归解决：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">const</span> g1 = main()
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleResult</span> (<span class="hljs-params">result</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (result.done) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
    result.value.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      handleResult(g1.next(data))
    &#125;, <span class="hljs-function"><span class="hljs-params">error</span>=></span>&#123;
      g
    &#125;)
  &#125;
  handleResult(g1.next())
  <span class="hljs-comment">// 依次输出：</span>
  <span class="hljs-comment">// &#123;name: "小明1", age: 1, id: 1&#125;</span>
  <span class="hljs-comment">// &#123;name: "小明12", age: 12, id: 12&#125;</span>
  <span class="hljs-comment">// &#123;name: "小明18", age: 18, id: 18&#125;</span>
  <span class="hljs-comment">// &#123;name: "小明24", age: 24, id: 24&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加上异常处理后，我们可以封装一个 exec 函数用于生成器函数的调用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timeOut</span> (<span class="hljs-params">id</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">if</span> (id < <span class="hljs-number">24</span>) &#123;
          resolve(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"小明"</span> + id, <span class="hljs-attr">age</span>: id, <span class="hljs-attr">id</span>: id &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'ID 超过24'</span>))
        &#125;
      &#125;, <span class="hljs-number">1000</span>)
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">main</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> res1 = <span class="hljs-keyword">yield</span> timeOut(<span class="hljs-number">1</span>)
      <span class="hljs-built_in">console</span>.log(res1)
      <span class="hljs-keyword">const</span> res2 = <span class="hljs-keyword">yield</span> timeOut(<span class="hljs-number">12</span>)
      <span class="hljs-built_in">console</span>.log(res2)
      <span class="hljs-keyword">const</span> res3 = <span class="hljs-keyword">yield</span> timeOut(<span class="hljs-number">18</span>)
      <span class="hljs-built_in">console</span>.log(res3)
      <span class="hljs-keyword">const</span> res4 = <span class="hljs-keyword">yield</span> timeOut(<span class="hljs-number">24</span>)
      <span class="hljs-built_in">console</span>.log(res4)
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">console</span>.log(error)
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">exec</span> (<span class="hljs-params">fun</span>) </span>&#123;
    <span class="hljs-keyword">const</span> generator = fun()
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleResult</span> (<span class="hljs-params">result</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (result.done) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      result.value.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
        handleResult(generator.next(data))
      &#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
        generator.throw(error)
      &#125;)
    &#125;
    handleResult(generator.next())
  &#125;
  exec(main)
  <span class="hljs-comment">// &#123;name: "小明1", age: 1, id: 1&#125;</span>
  <span class="hljs-comment">// &#123;name: "小明12", age: 12, id: 12&#125;</span>
  <span class="hljs-comment">// &#123;name: "小明18", age: 18, id: 18&#125;</span>
  <span class="hljs-comment">// Error: ID 超过24</span>
  <span class="hljs-comment">//     at <anonymous>:7:16</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的生成器函数执行器在社区中有一个完善的库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftj%2Fco" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tj/co" ref="nofollow noopener noreferrer">github.com/tj/co</a><br>这种方案在之前很流行的，但是自从 es 有了 async await 之后就没那么普及了，不过使用 generator 方案的最大优势就是让我们的异步调用回到扁平化，这是 js 异步编程中很重要的一步。
<a name="user-content-NzQxK" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-20">Async Await</h2>
<p>有了 Generator 之后，JavaScript 中的异步编程与同步代码就有类似的体验了，但是使用 Generator 这种方案还需要手动编写一个执行器函数，比较麻烦，在 es2017 中新增了一个 async await 同样提供了这种扁平化的异步编程体验，而且它是语言层面标准的语法，使用起来更加方便，其实 async await 就是生成器函数的一种更方便的语法糖，我们只要把生成器函数改成普通函数，使用 async 修饰，yield 修改成 await 就可以了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> res1 = <span class="hljs-keyword">await</span> timeOut(<span class="hljs-number">1</span>)
      <span class="hljs-built_in">console</span>.log(res1)
      <span class="hljs-keyword">const</span> res2 = <span class="hljs-keyword">await</span> timeOut(<span class="hljs-number">12</span>)
      <span class="hljs-built_in">console</span>.log(res2)
      <span class="hljs-keyword">const</span> res3 = <span class="hljs-keyword">await</span> timeOut(<span class="hljs-number">18</span>)
      <span class="hljs-built_in">console</span>.log(res3)
      <span class="hljs-keyword">const</span> res4 = <span class="hljs-keyword">await</span> timeOut(<span class="hljs-number">24</span>)
      <span class="hljs-built_in">console</span>.log(res4)
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">console</span>.log(error)
    &#125;
  &#125;
  main()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>async 函数的效果也和 Generator 一致，最大的好处就是不需要去配合类似于 co 这样的执行器，因为它是语言层面的标准异步语法，其次就是 async 会返回一个 Promise 对象，方便我们更好地控制代码，还有一个需要注意的是 await 只能出现在函数内部，不能再顶层作用域使用（现在已经在开发了，不久以后可能出现在标准中）。</p></div>  
</div>
            