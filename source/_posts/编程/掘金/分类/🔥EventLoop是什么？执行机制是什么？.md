
---
title: '🔥EventLoop是什么？执行机制是什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d79dbd1dd9da44b5aa7da5bc4241ee95~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 06:26:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d79dbd1dd9da44b5aa7da5bc4241ee95~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d79dbd1dd9da44b5aa7da5bc4241ee95~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是我参与更文挑战的第20天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<h4 data-id="heading-0">前言</h4>
<blockquote>
<p>面试官：给我说说事件循环吧，就是EventLoop的机制，这个你听说过吧。</p>
<p>我：...💥💥💥🚀</p>
</blockquote>
<h4 data-id="heading-1">什么是 EventLoop ？</h4>
<p>先看这张图，先不管宏任务，微任务是什么，先看整个流程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eb93e9f9d144993acd9eac570dfc70b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210406150156448" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分析：</p>
<ol>
<li>
<p>判断宏任务队列是否为空</p>
<ul>
<li>不空 --> 执行最早进入队列的任务 --> 执行下一步</li>
<li>空 --> 执行下一步</li>
</ul>
</li>
<li>
<p>判断微任务队列是否为空</p>
<ul>
<li>不空 --> 执行最早进入队列的任务 --> <strong>继续检查微任务队列空不空</strong></li>
<li>空 --> 执行下一步</li>
</ul>
</li>
</ol>
<blockquote>
<p>因为首次执行宏队列中会有 script（整体代码块）任务，所以实际上就是 Js 解析完成后，在异步任务中，会先执行完所有的微任务，这里也是很多<code>面试题喜欢考察的。</code>需要注意的是，新创建的微任务会立即进入微任务队列排队执行，不需要等待下一次轮回。</p>
</blockquote>
<p>主线程从任务队列读取事件，这个过程是循环不断的，所以整个运行机制又称为 <code>Event Loop(事件循环)。</code></p>
<p>在深入事件循环机制之前，需要弄懂一下几个概念：</p>
<ul>
<li><code>执行上下文( Execution context ) </code></li>
<li><code>执行栈（ Execution stack ） </code></li>
<li><code>微任务（ micro-task ）</code></li>
<li><code>宏任务（ macro-task ）</code></li>
</ul>
<h4 data-id="heading-2"><code>执行上下文( Execution context )</code></h4>
<blockquote>
<p>执行上下文是一个抽象的概念，可以理解为是代码执行的一个环境。JS 的执行上下文分为三种，<code>全局执 行上下文、函数(局部)执行上下文、Eval 执行上下文。 </code></p>
</blockquote>
<ul>
<li><code>全局执行上下文</code>：全局执行上下文指的是全局 this 指向的 window ，可以是外部加载的 JS 文件 或者本地  标签中的代码。</li>
<li><code>函数执行上下文</code>：函数上下文也称为局部上下文，每个函数被调用的时候，都会创建一个新的局部 上下文。</li>
<li>Eval 执行上下文： 这个不常用，这里不说。</li>
</ul>
<h4 data-id="heading-3"><code>执行栈（ Execution stack )</code></h4>
<p>执行栈，就是我们数据结构中的“栈”，它具有“先进后出”的特点，正是因为这种特点，在我们代码进行 执行的时候，遇到一个执行上下文就将其依次压入执行栈中。</p>
<p>当代码执行的时候，先执行位于栈顶的执行上下文中的代码，当栈顶的执行上下文代码执行完毕就会出 栈，继续执行下一个位于栈顶的执行上下文。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>);
    bar();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b'</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'c'</span>);
&#125;
foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>初始化状态，执行栈任务为空。</li>
<li>foo 函数执行， foo 进入执行栈，输出 a ，碰到函数 bar 。</li>
<li>然后 bar 再进入执行栈，开始执行 bar 函数，输出 c 。</li>
<li>bar 函数执行完出栈，继续执行执行栈顶端的函数 foo ，最后输出 b 。</li>
<li>foo 出栈，所有执行栈内任务执行完毕。</li>
</ol>
<h4 data-id="heading-4">什么是宏任务与微任务？</h4>
<blockquote>
<p>我们都知道 Js 是单线程都，但是一些高耗时操作就带来了进程阻塞问题。为了解决这个问题，Js 有两种任务的执行模式：<strong><code>同步模式（Synchronous）和异步模式（Asynchronous）</code></strong>。</p>
</blockquote>
<p>在异步模式下，创建<strong>异步任务主要分为宏任务与微任务两种</strong>。ES6 规范中，</p>
<ul>
<li>宏任务（Macrotask） 称为 Task， 微任务（Microtask） 称为 Jobs。</li>
<li>宏任务是由宿主（浏览器、Node）发起的，而微任务由 JS 自身发起。</li>
</ul>
<h5 data-id="heading-5"><strong>宏任务与微任务的几种创建方式</strong> 👇</h5>
<table><thead><tr><th>宏任务（Macrotask）</th><th>微任务（Microtask）</th></tr></thead><tbody><tr><td>setTimeout</td><td>requestAnimationFrame（有争议）</td></tr><tr><td>setInterval</td><td>MutationObserver（浏览器环境）</td></tr><tr><td>MessageChannel</td><td>Promise.[ then/catch/finally ]</td></tr><tr><td>I/O，事件队列</td><td>process.nextTick（Node环境）</td></tr><tr><td>setImmediate（Node环境）</td><td>queueMicrotask</td></tr><tr><td>script（整体代码块）</td><td></td></tr></tbody></table>
<p><code>注意：nextTick 队列会比 Promie 队列先执行。</code></p>
<p><strong>如何理解 script（整体代码块）是个宏任务呢</strong> 🤔</p>
<blockquote>
<p>实际上如果同时存在两个 script 代码块，会首先在执行第一个 script 代码块中的同步代码，如果这个过程中创建了微任务并进入了微任务队列，第一个 script 同步代码执行完之后，会首先去清空微任务队列，再去开启第二个 script 代码块的执行。</p>
<p>所以这里应该就可以理解 script（整体代码块）为什么会是宏任务。</p>
</blockquote>
<p>以上概念弄明白之后，再来看循环机制是如何运行的呢？以下涉及到的任务执行顺序都是靠函数调用栈 来实现的。</p>
<ol>
<li>首先，事件循环机制的是从<code>script</code>标签内的代码开始的，上边我们提到过，整个<code>script</code>标签 作为一个宏任务处理的。</li>
<li>在代码执行的过程中，如果遇到宏任务，如：<code>setTimeout</code>，就会将当前任务分发到对应的执行队 列中去。</li>
<li>当执行过程中，如果遇到微任务，如：<code> Promise</code> ，在创建 <code>Promise </code>实例对象时,代码顺序执行，如果 到了执行<code>· then</code> 操作，该任务就会被分发到微任务队列中去。</li>
<li><code>script </code>标签内的代码执行完毕，同时执行过程中所涉及到的宏任务也和微任务也分配到相应的队 列中去。</li>
<li>此时宏任务执行完毕，然后去微任务队列执行所有的存在的微任务。</li>
<li>微任务执行完毕，第一轮的消息循环执行完毕，页面进行一次渲染。</li>
<li>然后开始第二轮的消息循环，从宏任务队列中取出任务执行。</li>
<li>如果两个任务队列没有任务可执行了，此时所有任务执行完毕。</li>
</ol>
<h4 data-id="heading-6">定时器 <code>setTimeout</code></h4>
<p>任务队列除此之外，还可以放定时器的回调函数，需要指定某些代码多少时间之后执行。</p>
<p>定时器主要包括两种， <code>setTimeout 和 setInterval 两个函数</code>。 当我们设置定时器的时间，执行某个特定的任务，如下：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 1 秒后执行</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
  &#125;, <span class="hljs-number">1000</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)


<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述的输出结果为 1, 2，执行完同步代码后，就会执行定时器中的任务事件</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 同步执行完立即执行</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
  &#125;, <span class="hljs-number">0</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们执行 <code>setTimeout（fn,0）</code> 定时器时，会将这个定时任务回调放在任务队列的尾部，代表的含 义就是尽早的执行。</p>
<p>也就是等到主线程同步任务和"任务队列"现有的事件都处理完，然后才会立即执行这个定时器的任务。</p>
<p><code>上述的前提是，等到同步任务和任务队列的代码执行完毕后，如果当前代码执行很长时间，定时器并没 办法保证一定在指定时间执行。</code></p>
<blockquote>
<p><code>注:HTML5 标准规定了setTimeout() 的第二个参数的最小值（最短间隔），不得低于4毫秒， 如果低于这个值，就会自动增加。</code></p>
</blockquote>
<p>如果涉及到页面的改动，这个定时器任务通常不会立即执行，而是 16 毫秒执行一次，我们通常使用<code> requestAnimationFrame() 。</code></p>
<h4 data-id="heading-7">小实战</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"ie=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>消息运行机制<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>);
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2'</span>)
  &#125;, <span class="hljs-number">1000</span>);
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'3'</span>);
    resolve();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'4'</span>);
  &#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'5'</span>);
  &#125;);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'6'</span>);<span class="hljs-comment">// 1,3,4,6,5,2</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析：</p>
<ul>
<li>初始化状态，执行栈为空。</li>
<li>首先执行<code><script></code>标签内的同步代码，此时全局的代码进入执行栈中，同步顺序执行代码，输出 1。</li>
<li>执行过程中遇到异步代码 <code>setTimeout （宏任务）</code>，将其分配到宏任务异步队列中。</li>
<li>同步代码继续执行，遇到一个<code> promise 异步代码（微任务）</code>。但是构造函数中的代码为同步代码，依次输出3、4，则<code>then</code>之后的任务加入到微任务队列中去。</li>
<li>最后执行同步代码，输出 6。</li>
<li>因为 <code>script </code>内的代码作为宏任务处理，所以此次循环进行到处理微任务队列中的所有异步任务，直达微任务队列中的所有任务执行完成为止，微任务队列中只有一个微任务，所以输出 5。</li>
<li>此时页面要进行一次页面渲染，渲染完成之后，进行下一次循环。</li>
<li>在宏任务队列中取出一个宏任务，也就是之前的<code> setTimeout</code>，最后输出 2。</li>
<li>此时任务队列为空，执行栈中为空，整个程序执行完毕。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/006f2b45be3e4034a99e448518947b06~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210406152314952" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上难免有些啰嗦，所以简化整理如下步骤：</p>
<ul>
<li>一开始执行宏任务（ script 中同步代码），执行完毕，调用栈为空。</li>
<li>然后检查微任务队列是否有可执行任务，执行完所有微任务。</li>
<li>进行页面渲染。</li>
<li>第二轮从宏任务队列取出一个宏任务执行，重复以上循环。</li>
</ul></div>  
</div>
            