
---
title: 'Event Loop事件循环机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3503'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 00:42:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=3503'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. Event Loop是什么</h2>
<p><code>Event Loop</code>即事件循环，是指浏览器或Node的一种解决<code>javaScript</code>单线程运行时不会阻塞的一种机制，也就是我们经常使用<strong>异步</strong>的原理。</p>
<p>JavaScript代码的执行过程中，除了依靠<strong>函数调用栈</strong>来完成函数的执行顺序外，还依靠<strong>任务队列</strong>(task queue)来搞定另外一些代码的执行。</p>
<p>整个执行过程，我们称为事件循环过程。一个线程中，事件循环是唯一的，但是任务队列可以拥有多个。任务队列又分为<code>macro-task</code>（宏任务）与<code>micro-task</code>（微任务），在最新标准中，它们被分别称为task与jobs。</p>
<h3 data-id="heading-1">宏任务Task</h3>
<p><code><script></script></code>标签体内内容，<code>setTimeout</code>, <code>setInterval</code>, <code>setImmediate</code>, <code>I/O</code>, <code>UI Rending</code>。</p>
<h3 data-id="heading-2">微任务microtask</h3>
<p><code>Process.nextTick(Node独有)</code>,<code>Promise</code>, <code>Object.observe(废弃)</code>, <code>MutationObserver</code>。</p>
<h3 data-id="heading-3">宏任务与微任务的执行顺序(*)</h3>
<p>执行宏任务，然后执行该宏任务产生的微任务，若微任务在执行过程中产生了新的微任务，则继续执行微任务，微任务执行完毕后，再回到宏任务中进行下一轮循环。</p>
<h2 data-id="heading-4">2. 浏览器中的Event Loop</h2>
<p>JavaScript有一个 main thread主线程和 call-stack 调用栈（执行栈），所有任务都会被放到调用栈，等待主线程执行。</p>
<h3 data-id="heading-5">JS调用栈</h3>
<p>JS调用栈采用的是后进先出的规则，当函数执行的时候，会被添加到栈的顶部，当执行栈执行完成后，就会从栈顶移出，直到栈内被清空。</p>
<h3 data-id="heading-6">同步任务和异步任务</h3>
<p>Javascript单线程任务被分为同步任务和异步任务，同步任务会在调用栈中按照顺序等待主线程依次执行，异步任务会在异步任务有了结果后，将注册的回调函数放入任务队列中等待主线程空闲的时候（调用栈被清空），被读取到栈内等待主线程的执行。</p>
<h3 data-id="heading-7">事件循环执行过程(*)</h3>
<p>执行栈在执行完<strong>同步任务</strong>后，查看执行栈是否为空，如果执行栈为空，就会去检查<strong>微任务</strong>(microTask)队列是否为空，如果为空的话，就执行Task（<strong>宏任务</strong>），否则就一次性执行完所有微任务。</p>
<h3 data-id="heading-8">理解<code>async/await</code></h3>
<p><code>async/await</code> 在底层转换成了 <code>promise</code> 和 <code>then</code> 回调函数。</p>
<p>也就是说，这是 <code>promise</code> 的语法糖。</p>
<p>每次我们使用 <code>await</code>, 解释器都创建一个 <code>promise</code> 对象，然后把剩下的 <code>async</code> 函数中的操作放到 then 回调函数中。</p>
<p><code>async/await</code> 的实现，离不开 <code>Promise</code>。从字面意思来理解，async 是“异步”的简写，而 await 是 <code>async wait</code>的简写可以认为是等待异步方法执行完成。</p>
<h3 data-id="heading-9">举例async/await执行顺序</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script start'</span>)

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async1</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">await</span> async2()
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async1 end'</span>)
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async2</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async2 end'</span>)
&#125;
async1()

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout'</span>)
&#125;, <span class="hljs-number">0</span>)

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Promise'</span>)
resolve()
&#125;)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise1'</span>)
&#125;)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise2'</span>)
&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script end'</span>)
 <span class="hljs-comment">// 旧版输出如下，但是请继续看完本文下面的注意那里，新版有改动</span>
<span class="hljs-comment">// script start => async2 end => Promise => script end => promise1 => promise2 => async1 end => setTimeout</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            