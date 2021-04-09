
---
title: '深入理解JS执行机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79eda5cc57334da4807a3f41d53debb8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 08:16:46 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79eda5cc57334da4807a3f41d53debb8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>JavaScript是一门单线程的非阻塞脚本语言，同一时刻只允许一个代码段执行。在单线程的机制下，执行异步任务时，在等待结果返回的这个时间段，后面的代码就无法执行了。</p>
<p>JS在执行代码时，遇到异步任务之后还有同步任务的场景时，它并不会等待异步任务执行完，而是先执行同步任务，那么JS是如何做到这一点的呢？</p>
<p>本篇文章将详细讲解上述问题，欢迎各位感兴趣的开发者阅读本文。</p>
<h2 data-id="heading-1">事件循环</h2>
<h3 data-id="heading-2">单线程</h3>
<p>讲事件循环之前，我们先来理解下为什么JS不设计成多线程的。</p>
<p>我们做个假设，如果JS是多线程的，因为JS有DOM API可以操作DOM，此时如果有两个线程在操作同一个DOM，线程1删除了这个dom节点，线程2要操作这个dom，就会产生矛盾，到底以哪个线程为主。</p>
<p>为了避免这种情况的出现，JS就被设计成了<strong>单线程</strong> 。</p>
<h3 data-id="heading-3">宏任务与微任务</h3>
<p>JS引擎把所有任务分为两类：宏任务、微任务。</p>
<p>宏任务有：</p>
<ul>
<li><code>script</code>整体代码</li>
<li>setTimeout、setInterval</li>
<li>I/O</li>
<li>UI渲染</li>
<li>postMessage</li>
<li>MessageChannel</li>
<li>requestAnimationFrame</li>
<li>setImmediate(Node.js 环境)</li>
</ul>
<p>微任务有：</p>
<ul>
<li>new Promise.then()</li>
<li>MutaionObserver</li>
<li>process.nextTick(Node.js 环境)</li>
</ul>
<h3 data-id="heading-4">执行规则</h3>
<p>文章一开头我们了解到了单线程的弊端，JS是通过事件循环机制（EventLoop）来解决这一弊端的，接下来我们来看下EventLoop的执行规则：</p>
<ul>
<li>所有代码作为宏任务进入主线程执行栈，开始执行</li>
<li>执行过程中，同步代码会立即执行，宏任务进入宏任务队列，微任务进入微任务队列</li>
<li>当前宏任务执行完成出队，读取微任务队列，有则执行，直至全部执行完毕</li>
<li>执行浏览器ui进程渲染</li>
<li>检查是否有webworker任务，有则执行</li>
<li>本轮宏任务执行完成，回到第2步，继续执行，直至宏任务与微任务队列全部清空</li>
</ul>
<h2 data-id="heading-5">举例说明</h2>
<p>我们了解完它的执行规则后，接下来我们举个例子来说明下，如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"1"</span>); <span class="hljs-comment">// 1 同步代码：立即执行 [1]</span>

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"2"</span>); <span class="hljs-comment">// 3 同步代码执行执行 输出2</span>
  process.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"3"</span>); <span class="hljs-comment">// 4 进入微任务队列 [3]</span>
  &#125;);
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"4"</span>); <span class="hljs-comment">// 3 同步代码执行执行 输出4</span>
    resolve();
  &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"5"</span>); <span class="hljs-comment">// 4 进入微任务队列 [3, 5]</span>
  &#125;);
&#125;);

process.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"6"</span>); <span class="hljs-comment">// 2 进入微任务队列 [6]</span>
&#125;);

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"7"</span>); <span class="hljs-comment">// 1 宏任务：立即执行 [1, 7]</span>
  resolve();
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"8"</span>); <span class="hljs-comment">// 2 进入微任务队列 [6, 8]</span>
&#125;);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"9"</span>); <span class="hljs-comment">// 5 宏任务：立即执行 [9]</span>
  process.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"10"</span>); <span class="hljs-comment">// 6 进入微任务队列 [10]</span>
  &#125;);
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"11"</span>); <span class="hljs-comment">// 5 宏任务：立即执行 [9, 11]</span>
    resolve();
  &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"12"</span>); <span class="hljs-comment">// 6 进入微任务队列 [10, 12]</span>
  &#125;);
&#125;);

<span class="hljs-comment">// 执行顺序：1 7 6 8 2 4 3 5 9 11 10 12</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>process.nextTick()为node中的方法，你可以把它理解为与promise一样的微任务，promise的executor函数中的同步代码会立即执行。</p>
</blockquote>
<p>我们来分析下上述代码的执行顺序，如下图所示：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79eda5cc57334da4807a3f41d53debb8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>运行结果如下所示：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c3d54d4f57f499b970ed72c514b2311~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>当你把上述示例代码啃透后，那么你也就理解js的事件循环机制了。</p>
<p>当然，你可能没有那么快就啃透这个例子，这种概念性的东西，掌握它最好的办法就是：将示例代码放到编辑器里，对照着事件循环的执行规则，一行一行的去读代码，大脑过一遍，猜测运行结果，然后再去执行代码判断执行结果是否与你猜的一致。</p>
<p>最后，举一反三，去网上找一些事件循环的面试题多加练习，慢慢的你就把这个知识点啃透了，Good Luck！</p>
</blockquote>
<h2 data-id="heading-6">代码地址</h2>
<p>本文为《JS原理学习》系列的第5篇文章，本系列的完整路线请移步：<a href="https://juejin.cn/post/6937688619503058974" target="_blank">JS原理学习 (1) 》学习路线规划</a></p>
<p>本系列文章的所有示例代码，请移步：<a href="https://github.com/likaia/js-learning" target="_blank" rel="nofollow noopener noreferrer">js-learning</a></p>
<h2 data-id="heading-7">写在最后</h2>
<p>至此，文章就分享完毕了。</p>
<p>我是<strong>神奇的程序员</strong>，一位前端开发工程师。</p>
<p>如果你对我感兴趣，请移步我的<a href="https://www.kaisir.cn/" target="_blank" rel="nofollow noopener noreferrer">个人网站</a>，进一步了解。</p>
<ul>
<li>文中如有错误，欢迎在评论区指正，如果这篇文章帮到了你，欢迎点赞和关注😊</li>
<li>本文首发于掘金，未经许可禁止转载💌</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            