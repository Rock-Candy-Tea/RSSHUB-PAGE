
---
title: '解析事件循环机制（node、浏览器）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9526'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 19:15:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=9526'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一、为什么会有event loop?</p>
<pre><code class="copyable">js的任务分为同步和异步两种：
1、同步任务是直接放在主线程上排队依次执行；
2、异步任务会放在任务队列中，若有多个异步任务则需要在任务队列中排队等待，
   任务队列类似于缓冲区，任务下一步会被移到调用栈然后主线程执行调用栈的任务。
   
调用栈：是一个栈结构，函数调用会形成一个栈帧，帧中包含了当前执行函数的参数和局部变量等上下文信息，
函数执行完成后，它的执行上下文会从栈中弹出。

js是单线程的，单线程是指js引擎中解析和执行js代码的线程只有一个，每次只做一件事，
而ajax请求中，主线程在等待响应的过程中回去做其他的事情，浏览器先在事件表注册ajax的回调函数，
响应回来后回调函数被添加到任务队列中等待执行，不会造成线程阻塞，这种方式是异步的。

所以，检查调用栈是否为空以及将某个任务添加到调用栈中的过程就是event loop，这就是js实现异步的核心。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二、浏览器中的Event Loop</p>
<p>1、micro-task和macro-task</p>
<p>浏览器端事件循环中的异步队列有两种：micro(微任务队列)、macro(宏任务队列)；</p>
<p>常见的宏任务：setTimeout、setInterval、script(整体代码)、I/O操作、UI渲染等；</p>
<p>常见的微任务：new Promise().then()、MutationObserve、process.nextTick()等;</p>
<p>2、事件循环的过程</p>
<pre><code class="copyable">  检查宏任务队列是否为空，非空则执行宏任务队列中的一个任务，
  为空则继续检查微任务队列是否为空，
  非空则取出微任务队列中的任务执行，执行完成继续检查微任务对列，微任务队列为空则执行视图更新。
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三、node中的event loop</p>
<p>1、node中的事件循环和浏览器中的是完全不相同的东西。nodejs采用v8作为js的解析引擎，
I/O处理方面使用了自己设计的libuv,libuv是一个基于事件驱动的跨平台抽象层，封装了不同操作系统的底层特性，对外提供统一的api，事件循环机制也是它里面实现的。</p>
<p>2、node的运行机制如下：</p>
<pre><code class="copyable">1、v8引擎解析js脚本；
2、解析后的代码调用node api;
3、libuv库负责node API的执行。它将不同的任务分给不同的线程，形成一个事件循环，
以异步的方式将任务的执行结果返回給v8引擎；
4、v8引擎再将结果返回給用户。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、六大阶段</p>
<p>libuv引擎中的事件循环分为6个阶段，它们会按照顺序反复运行。</p>
<pre><code class="copyable">   1、timers阶段：这个阶段执行 timer（setTimeout、setInterval）的回调；
   2、I/O callbacks阶段：处理一些上一轮循环中的少数未执行的 I/O 回调；
   3、idle, prepare 阶段：仅 node 内部使用
   4、poll 阶段：获取新的 I/O 事件, 适当的条件下 node 将阻塞在这里
   5、check 阶段：执行 setImmediate() 的回调
   6、 callbacks 阶段：执行 socket 的 close 事件回调
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            