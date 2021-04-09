
---
title: '如何在JavaScript中实现队列数据结构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9382e1fc878a4936b01205ef5946d99a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 07:30:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9382e1fc878a4936b01205ef5946d99a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>博客原文：<a href="https://blog.zhangbing.site/2021/03/28/javascript-queue/" target="_blank" rel="nofollow noopener noreferrer">blog.zhangbing.site/2021/03/28/…</a></p>
</blockquote>
<p>要成为一名优秀的开发人员，需要来自多个学科的知识。</p>
<p>然而，在了解编程语言的基础上，你还必须了解如何组织数据，以便根据任务轻松有效地操作数据。这就是数据结构的作用。</p>
<p>在这篇文章中，我将描述队列数据结构，其具有的操作以及向您展示JavaScript中的队列实现。</p>
<h2 data-id="heading-0">1.队列数据结构</h2>
<p>如果你喜欢旅行（像我一样），很可能你在机场通过了办理登机手续。如果有很多旅客愿意办理登机手续，自然就会在值机柜台前排起长龙。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9382e1fc878a4936b01205ef5946d99a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>刚进入机场并想要办理登机手续的旅客将排队进入队列，而刚刚在服务台办理了登机手续的旅客则可以离开队列。</p>
<p>这是队列的真实示例—队列数据结构以相同的方式工作。</p>
<p>队列是一种“先入先出”（FIFO）数据结构的类型。入队（输入）的第一项是要出队（输出）的第一项。</p>
<p>从结构上说，一个队列有2个指针。队列中最早的排队项目位于队列的顶部，而最新队列的项目位于队列的末尾。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b784192ad3e4819ac7e8ca934745fd7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2.队列中的操作</h2>
<p>队列主要支持两种操作：入队列（enqueue）和出队列（dequeue）。此外，您可能会发现使用peek和length操作非常有用。</p>
<h3 data-id="heading-2">2.1 入队操作</h3>
<p>入队操作在队列尾部插入一个项目。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebb65e6b320d45c3ad10585ecedc68d2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图中的入队操作将项目 <code>8</code> 插入尾部，<code>8</code> 成为队列的尾部。</p>
<pre><code class="hljs language-js copyable" lang="js">queue.enqueue(<span class="hljs-number">8</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.2 出队操作</h3>
<p>出队操作提取队列头部的项，队列中的下一项成为头。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec72f0cc1ec04f86ab226e451d8b93c1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在上面的图片中，出队操作从队列中返回并删除项目 <code>7</code>，在退出队列后，项目 <code>2</code> 成为新的头。</p>
<pre><code class="hljs language-js copyable" lang="js">queue.dequeue(); <span class="hljs-comment">// => 7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.3 Peek操作</h3>
<p>Peek操作读取队列的开头，而不会更改队列。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db494f2a863145f8935614e24b584e41~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>项目 <code>7</code> 是上图中队列的头部，Peek操作只是返回队列的头部——第 <code>7</code> 项，而不修改队列。</p>
<pre><code class="hljs language-js copyable" lang="js">queue.peek(); <span class="hljs-comment">// => 7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.4 队列长度</h3>
<p>长度操作计算队列包含多少个项目。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08ac4e4c537e465b8cfec1c31a2d2a51~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>图片中的队列有4个项目：<code>4</code>、<code>6</code>、<code>2</code> 和 <code>7</code>。因此，队列长度为 <code>4</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">queue.length; <span class="hljs-comment">// => 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.5 队列操作时间复杂度</h3>
<p>关于所有的队列操作--enqueue、dequeue、peek和length——重要的是，所有这些操作必须在恒定的时间内 <code>O(1)</code> 执行。</p>
<p>恒定的时间 <code>O(1)</code> 意味着无论队列的大小(它可以有10个或100万个项目)：enqueue、dequeue、peek和length操作必须在相对相同的时间内执行。</p>
<h2 data-id="heading-7">3.在JavaScript中实现队列</h2>
<p>让我们看一下队列数据结构的可能实现，同时维持所有操作必须在恒定时间 <code>O(1)</code> 中执行的要求。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Queue</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.items = &#123;&#125;;
    <span class="hljs-built_in">this</span>.headIndex = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.tailIndex = <span class="hljs-number">0</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">enqueue</span>(<span class="hljs-params">item</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.items[<span class="hljs-built_in">this</span>.tailIndex] = item;
    <span class="hljs-built_in">this</span>.tailIndex++;
  &#125;

  <span class="hljs-function"><span class="hljs-title">dequeue</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> item = <span class="hljs-built_in">this</span>.items[<span class="hljs-built_in">this</span>.headIndex];
    <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.items[<span class="hljs-built_in">this</span>.headIndex];
    <span class="hljs-built_in">this</span>.headIndex++;
    <span class="hljs-keyword">return</span> item;
  &#125;

  <span class="hljs-function"><span class="hljs-title">peek</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.items[<span class="hljs-built_in">this</span>.headIndex];
  &#125;

  <span class="hljs-keyword">get</span> <span class="hljs-title">length</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.tailIndex - <span class="hljs-built_in">this</span>.headIndex;
  &#125;
&#125;

<span class="hljs-keyword">const</span> queue = <span class="hljs-keyword">new</span> Queue();

queue.enqueue(<span class="hljs-number">7</span>);
queue.enqueue(<span class="hljs-number">2</span>);
queue.enqueue(<span class="hljs-number">6</span>);
queue.enqueue(<span class="hljs-number">4</span>);

queue.dequeue(); <span class="hljs-comment">// => 7</span>

queue.peek();    <span class="hljs-comment">// => 2</span>

queue.length;    <span class="hljs-comment">// => 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://jsfiddle.net/dmitri_pavlutin/g6pd4hqb/2/" target="_blank" rel="nofollow noopener noreferrer">Try the demo.</a></p>
<p><code>const queue = new Queue()</code> 是创建队列实例的方式。</p>
<p>调用 <code>queue.enqueue(7)</code> 方法会将项目7排队到队列中。</p>
<p><code>queue.dequeue()</code> 从队列中去队列一个头部的项目，而 <code>queue.peek()</code> 只是Peek头部的项目。</p>
<p>最后，<code>queue.length</code> 显示队列中还有多少项目。</p>
<h3 data-id="heading-8">队列方法的复杂性</h3>
<p>Queue类的 <code>queue()</code>、<code>dequeue()</code>、<code>peek()</code> 和 <code>length()</code> 方法仅使用：</p>
<ul>
<li>属性访问器（例如 <code>this.items[this.headIndex]</code> ），</li>
<li>或执行算术操作（例如 <code>this.headIndex++</code> ）</li>
</ul>
<p>因此，这些方法的时间复杂度是恒定时间 <code>O(1)</code>。</p>
<h2 data-id="heading-9">总结</h2>
<p>队列数据结构是“先入先出”（FIFO）的一种：最早入队的项是最早出队的项。</p>
<p>队列有2个主要操作：入队和出队。另外，队列可以具有辅助操作，例如Peek和长度。</p>
<p>所有队列操作必须在恒定时间 <code>O(1)</code> 中执行。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            