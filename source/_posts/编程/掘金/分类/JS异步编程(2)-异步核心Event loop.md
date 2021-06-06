
---
title: 'JS异步编程(2)-异步核心Event loop'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bce4150063264b4fa3c057446dd46dd0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 06:58:36 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bce4150063264b4fa3c057446dd46dd0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>Event loop 是 JavaScript 异步编程的核心，通过事件循环机制，让单线程的 JavaScript 具备异步处理任务的能力</p>
<h2 data-id="heading-0">异步任务队列</h2>
<p>异步任务队列分为<strong>两类</strong></p>
<ul>
<li>宏任务队列</li>
<li>微任务队列</li>
</ul>
<p>都用于存放异步任务</p>
<h3 data-id="heading-1">为什么异步队列要分宏微任务？</h3>
<p>其实在学习了 Event loop 很久之后，才突然反应过来，反问自己这个最初的问题<br>
异步队列有一个就行了，已经能够满足异步操作的需求，为什么还需要分两种队列呢？</p>
<p>答案是：<strong>为了插队！</strong></p>
<p>宏微任务的执行逻辑，本质上就是为了满足异步操作的插队需求，让某个后插入的异步操作尽量早的执行</p>
<h3 data-id="heading-2">宏任务(macrotasks)</h3>








































<table><thead><tr><th>API</th><th>Web</th><th>Node</th></tr></thead><tbody><tr><td>DOM API</td><td>✅</td><td>❌</td></tr><tr><td>I/O</td><td>❌</td><td>✅</td></tr><tr><td>setTimeout</td><td>✅</td><td>✅</td></tr><tr><td>setInterval</td><td>✅</td><td>✅</td></tr><tr><td>setImmediate</td><td>✅</td><td>✅</td></tr><tr><td>requestAnimationFrame</td><td>✅</td><td>❌</td></tr></tbody></table>
<p>有些地方会把 UI Rendering 也列为宏任务<br>
但是在 HTML 规范文档中，发现这其实是和<strong>微任务平行的一个操作步骤</strong></p>
<ul>
<li>UI Rendering 代表的不是一个单一的任务，而是一个任务队列(queue)</li>
<li>具备一些不同于普通宏任务和微任务的特性
<ul>
<li>触发的时机在当前微任务队列和下一个宏任务之间</li>
<li>UI Rendering 执行中触发的新的 requestAnimationFrame，不会推进当前正在执行的 UI Rendering 队列。而是进入下一次的 UI Rendering 队列</li>
</ul>
</li>
</ul>
<h3 data-id="heading-3">微任务(microtasks)</h3>

























<table><thead><tr><th>API</th><th>Web</th><th>Node</th></tr></thead><tbody><tr><td>process.nextTick</td><td>❌</td><td>✅</td></tr><tr><td>MutationObserver</td><td>✅</td><td>❌</td></tr><tr><td>Promise.then catch finally</td><td>✅</td><td>✅</td></tr></tbody></table>
<p>process.nextTick 和 web 端的 UI Rendering 类似</p>
<ul>
<li>process.nextTick 也有一个自己的任务队列 nextTick queue</li>
<li>具备一些不同于普通微任务的特性
<ul>
<li>触发的时机在当前宏任务和当前微任务队列之间</li>
</ul>
</li>
</ul>
<h2 data-id="heading-4">执行机制</h2>
<h3 data-id="heading-5">Web 中的执行机制</h3>
<p>浏览器环境下的 Event loop 是由HTML5规范<strong>明确定义</strong>，由各大浏览器厂商<strong>各自实现</strong><br>
这里主要涉及到下面几个浏览器线程：</p>
<ul>
<li>JS引擎线程：主要处理主执行栈任务（同步任务）</li>
<li>异步http请求线程：主要处理网络请求，将已完成的网络请求回调函数推进事件触发线程</li>
<li>定时器线程：将已完成待执行的定时器回调函数推进事件触发线程</li>
<li>事件触发线程：存储宏微任务的线程</li>
</ul>
<h4 data-id="heading-6">基本流程</h4>
<p>异步队列的执行机制，简单来说</p>
<ol>
<li>当主执行栈里的任务清空之后，开始读取异步任务队列中的任务</li>
<li>先读取微任务队列中的任务，依次读取执行直至队列清空</li>
<li>然后从宏任务中读取第一个任务执行</li>
<li>从第2步开始重复，直到宏任务队列为空</li>
</ol>
<p><code>同步任务 -> 全部微任务 -> UI Rendering -> 宏任务 -> 全部微任务 -> UI Rendering -> 下一个宏任务 -> ...</code></p>
<p>如果在执行过程中</p>
<ul>
<li>触发新的宏任务，会将其推进宏任务队列，等待读取</li>
<li>触发新的微任务，会将其推进当前的微任务队列，在本次微任务队列中完成执行</li>
</ul>
<p><code>同步任务 -> 全部微任务 -> UI Rendering -> 宏任务（触发新的宏任务和微任务） -> 全部微任务（包含新触发的微任务） -> UI Rendering -> 下一个宏任务（新触发的宏任务被推进宏任务列表等待执行） -> ...</code></p>
<ul>
<li>触发新的 UI Rendering，会将其推进<strong>下一个 UI Rendering</strong></li>
</ul>
<p><code>同步任务 -> 全部微任务 -> UI Rendering（触发新的 RAF） -> 宏任务 -> 全部微任务 -> UI Rendering（包含之前触发的新RAF） -> 下一个宏任务 -> ...</code></p>
<h4 data-id="heading-7">操作触发的浏览器事件回调</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// html</span>
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"parent"</span> onclick=<span class="hljs-string">"handleClick()"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"handleClick()"</span>/></span></span>
</div>

<span class="hljs-comment">// js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise then'</span>))
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout msg'</span>), <span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码，如果用户点击 <code>child</code> 元素<br>
类似于用<strong>宏任务</strong>的触发方式，直接注册了 <code>parent</code> 和 <code>child</code> 元素的 click 回调函数<br>
<code>child click -> child promise then -> parent click -> parent promise then -> child setTimeout msg -> parent setTimeout msg</code></p>
<h4 data-id="heading-8">代码触发的浏览器事件回调</h4>
<p>同样是上面的代码，如果使用 JS 代码触发事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.child'</span>).click()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么和 <code>dispatchEvent</code> 类似，都是一种<strong>同步任务</strong>的触发方式<br>
把两次的 click 事件都推入<strong>主执行栈队列</strong><br>
<code>child click -> parent click -> child promise then -> parent promise then -> child setTimeout msg -> parent setTimeout msg</code></p>
<h3 data-id="heading-9">Node 中的执行机制</h3>
<p>与 Web 端 Event loop 依赖浏览器线程一样，Node 端 Event loop 也依赖一位新同学： <code>libuv</code></p>
<ul>
<li>libuv 是 Node 的新跨平台抽象层，核心是提供 i/o 的事件循环和异步回调</li>
<li>libuv使用异步，事件驱动的编程方式</li>
<li>libuv的API包含有时间，非阻塞的网络，异步文件操作，子进程等等。</li>
<li>Event Loop就是在libuv中实现的。</li>
</ul>
<h4 data-id="heading-10">6个阶段</h4>
<p>Node的 Event loop一共分为6个阶段，会按照顺序反复运行<br>
每当进入某一个阶段的时候，都会从对应的回调队列中取出函数去执行<br>
当队列为空或者执行的回调函数数量到达系统设定的阈值，就会进入下一阶段</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bce4150063264b4fa3c057446dd46dd0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每个细节具体如下：</p>
<ol>
<li>timers: 执行 setTimeout 和 setInterval 中到期的 callback，由 poll 调度进入该阶段</li>
<li>pending: 某些系统操作级别的回调，在这个阶段执行</li>
<li>idle, prepare: 仅在内部使用。</li>
<li>poll: 执行 I/O 回调，在适当的情况下回阻塞在这个阶段。</li>
<li>check: 执行 setImmediate 的回调函数</li>
<li>close: 执行close事件的 callback</li>
</ol>
<h5 data-id="heading-11">timers</h5>
<ul>
<li>timers 阶段会执行 setTimeout 和 setInterval 回调，由 poll 调度进入该阶段</li>
<li>timers 阶段如果触发了新的 setTimeout 和 setInterval，会推入到<strong>下一次的 timers 阶段</strong>，不会在本次 timers 阶段执行</li>
</ul>
<h5 data-id="heading-12">poll</h5>
<p>这一阶段主要处理两件事情</p>
<ol>
<li>回到 timers 阶段执行回调</li>
<li>执行 I/O 回调</li>
</ol>
<p>执行逻辑：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a347f64e50874756a594c5216c76851e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">Node 10.x 及以前的基本流程</h4>
<p>在 Node 10.x 及以前。Event loop 的每个阶段，都是先执行宏任务队列，再执行微任务队列<br>
<code>全部宏任务 -> 全部 nextTick 任务 -> 全部微任务</code></p>
<h4 data-id="heading-14">Node 11.x 及以后的基本流程</h4>
<p>Node.js 在升级到 11.x 后，Event Loop 运行原理发生了变化。一个宏任务执行完成就执行微任务队列，和浏览器一致了<br>
<code>宏任务 -> 全部 nextTick 任务 -> 全部微任务 -> 下一个宏任务 -> 全部 nextTick 任务 -> 全部微任务</code></p>
<h2 data-id="heading-15">总结</h2>
<p>在 Web 端，Event loop 依赖各个浏览器厂商的实现<br>
除了正常的宏微任务外，还拥有独特的 UI Rendering 和 MutationObserver<br>
依靠浏览器各线程的配合，完成 Event loop 的循环</p>
<p>而在 Node 端，Event loop 依赖 libuv 的实现，同时在 Node 11 版本前后有差异<br>
Node 端拥有 6 个事件阶段，每个阶段都可以进行 Event loop 循环</p>
<h2 data-id="heading-16">参考文章</h2>
<p>《<a href="https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/" target="_blank" rel="nofollow noopener noreferrer">Tasks, microtasks, queues and schedules</a>》<br>
《<a href="https://juejin.cn/post/6844903764202094606#heading-35" target="_blank">一次弄懂Event Loop（彻底解决此类面试问题）</a>》<br>
《<a href="https://blog.csdn.net/LuckyWinty/article/details/104765786" target="_blank" rel="nofollow noopener noreferrer">面试题：说说事件循环机制(满分答案来了)</a>》</p></div>  
</div>
            