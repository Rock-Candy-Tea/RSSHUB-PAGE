
---
title: 'JS中Event Loop'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34ceeb98e0844728ac3e842f329fd36d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 01:34:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34ceeb98e0844728ac3e842f329fd36d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Event Loop</h1>
<p>JS中任务分为<strong>同步任务和异步任务</strong></p>
<p><strong>同步任务</strong>：在主线程上排队执行的任务，只有前一个任务执行完毕，才能执行后一个任务</p>
<p><strong>异步任务</strong>：不进入主线程、而进入"任务队列"（task queue）的任务，只有"任务队列"通知主线程，某个异步任务可以执行了，该任务才会进入主线程执行（鼠标点击、键盘事件、httpq请求、setTimeOut）</p>
<p>具体执行流程：</p>
<ol>
<li>所有同步任务都在主线程上执行，形成一个执行栈</li>
<li>主线程之外，还存在一个"任务队列"（task queue）。只要异步任务有了运行结果，就在"任务队列"之中放置一个事件。</li>
<li>一旦"执行栈"中的所有同步任务执行完毕，系统就会读取"任务队列"，看看里面有哪些事件。那些对应的异步任务，于是结束等待状态，进入执行栈，开始执行。</li>
<li>主线程不断重复上面的第三步。</li>
</ol>
<p><strong>主线程从"任务队列"中读取事件，这个过程是循环不断的，所以整个的这种运行机制又称为Event Loop（事件循环）</strong></p>
<p><strong>不管是<code>setTimeout/setInterval</code>和<code>XHR/fetch</code>代码，在这些代码执行时， 本身是同步任务，而其中的回调函数才是异步任务,才会进入到任务队列中</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34ceeb98e0844728ac3e842f329fd36d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">宏任务、微任务</h1>
<h2 data-id="heading-2">宏任务</h2>
<p>我们可以将每次执行栈执行的代码当做是一个宏任务（包括每次从事件队列中获取一个事件回调并放到执行栈中执行）， 每一个宏任务会从头到尾执行完毕，不会执行其他</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61f5232d8cc7417a87010c195b2f53bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">微任务</h2>
<p>微任务仅来自于我们的代码。它们通常是由 promise 创建的：对 <code>.then/catch/finally</code> 处理程序的执行会成为微任务。微任务也被用于 <code>await</code> 的“幕后”，因为它是 promise 处理的另一种形式</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd6020e34504cc18bec073e8a3c0482~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>执行一个<code>宏任务</code>（栈中没有就从<code>事件队列</code>中获取）</p>
</li>
<li>
<p>执行过程中如果遇到<code>微任务</code>，就将它添加到<code>微任务</code>的任务队列中</p>
</li>
<li>
<p><code>宏任务</code>执行完毕后，立即执行当前<code>微任务队列</code>中的所有<code>微任务</code>（依次执行）</p>
</li>
<li>
<p>当前<code>宏任务</code>执行完毕，开始检查渲染，然后<code>GUI线程</code>接管渲染</p>
</li>
<li>
<p>渲染完毕后，<code>JS线程</code>继续接管，开始下一个<code>宏任务</code>（从事件队列中获取）</p>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54923356afbf413a8d323125c3de9456~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">参考</h1>
<p><a href="https://juejin.cn/post/6844903919789801486#heading-11" target="_blank" title="https://juejin.cn/post/6844903919789801486#heading-11"> 「前端进阶」从多线程到Event Loop全面梳理</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2014%2F10%2Fevent-loop.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2014/10/event-loop.html" ref="nofollow noopener noreferrer">JavaScript 运行机制详解：再谈Event Loop</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.javascript.info%2Fevent-loop" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.javascript.info/event-loop" ref="nofollow noopener noreferrer">事件循环：微任务和宏任务</a></p></div>  
</div>
            