
---
title: '从中断机制看 React Fiber 技术'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c6eb9ebc97140abb73925523327298f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 03:55:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c6eb9ebc97140abb73925523327298f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>React 16 开始，采用了 Fiber 机制替代了原有的同步渲染 VDOM 的方案，提高了页面渲染性能和用户体验。Fiber 究竟是什么，网上也很多优秀的技术揭秘文章，本篇主要想从计算机的中断机制来聊聊 React Fiber 技术大概工作原理。</p>
<h2 data-id="heading-1">单任务</h2>
<p>在早期的单任务系统上，用户一次只能提交一个任务，当前运行的任务拥有全部硬件和软件资源，如果任务不主动释放 CPU 控制权，那么将一直占用所有资源，可能影响其他任务，造成资源浪费。该模式非常像当前浏览器运行模式，由于 UI 线程和 JS 线程的运行是互斥的，一旦 JS 长时间执行，浏览器无法及时响应用户交互，很容造成界面的卡顿，React 早期的同步渲染机制，当一次性更新的节点太多时，影响用户体验。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c6eb9ebc97140abb73925523327298f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">中断</h2>
<p>中断最初是用于提高处理器效率的一种手段，在没有中断的情况下，当 CPU 在执行一段代码时，如果程序不主动退出（如：一段无限循环代码），那么 CPU 将被一直占用，影响其他任务运行。</p>
<pre><code class="hljs language-plain copyable" lang="plain">while(true) &#123;
  ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而中断机制会强制中断当前 CPU 所执行的代码，转而去执行先前注册好的中断服务程序。比较常见的如：时钟中断，它每隔一定时间将中断当前正在执行的任务，并立刻执行预先设置的中断服务程序，从而实现不同任务之间的交替执行，这也是在多任务系统的重要的基础机制。中断机制主要通过硬件触发，CPU 属于被动接受。有了中断后，各任务执行时间就可以得到非常好的控制。
<img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2abc58a998fc4d2484fa836b41923564~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>回到浏览器，目前浏览器大多是 60Hz（60 帧/秒），既每一帧耗时大概在 16ms 左右，它会经过下面这几个过程：</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51850915302348abaa7d703ea64c41a3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>输入事件处理</li>
<li>requestAnimationFrame</li>
<li>DOM 渲染</li>
<li>RIC (RequestIdleCallback)</li>
</ol>
<p>我们除了在步骤 1-3 的中进行加塞外，无法进行任何干预，而步骤 4 的 RIC，算是一种防止多余计算资源被浪费的机制，例如，当一帧中步骤 1-3 只耗费 6ms，那么剩余 10ms 的计算资源则会被浪费，而 RIC 就是浏览器提供的一种资源利用的接口。RIC 非常像前面提到的“中断服务”，而浏览器的每一帧类似“中断机制”，利用它则可以在实现我们前面提到的大任务卡顿问题，例如：之前我们在 JS 中写如下代码时，无疑会阻塞浏览器渲染。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">task</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>)&#123;
   ...
  &#125;;
&#125;
task();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但利用 RIC 机制后，我们完全可以让大任务周期性的执行，从而不阻止浏览器正常渲染。
<img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7989590aa5fb44efb5e1e9057875038d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>将上面示例代码根据 RequestIdleCallback 进行调整，如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">task</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>)&#123;
   ...
  &#125;;
&#125;
requestIdleCallback(task);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遗憾的是，由于我们的代码运行在用户态，无法感知到底层的真实中断，我们现在利用的 RIC 也只是一种中断的近似模拟，以上代码并不会在 16ms 到期后被强制中断，我们只能主动进行释放，将控制权交还浏览器，RIC 提供了 timeRemaining 方法，让任务知道主动释放时机，我们调整以上代码，如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">task</span>(<span class="hljs-params">deadline</span>)</span>&#123;
  <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>)&#123;
   ...
   <span class="hljs-keyword">if</span>(!deadline.timeRemaining()) &#123;
     requestIdleCallback(task);
     <span class="hljs-comment">// 主动退出循环，将控制权交还浏览器</span>
     <span class="hljs-keyword">break</span>;
   &#125;
  &#125;;
&#125;
requestIdleCallback(task);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上示例，可以让一个大循环在“中断”机制下，不阻塞浏览器的渲染和响应。</p>
<p><strong>注意：</strong> RIC 调用频率大概是 20 次/秒，远远低于页面流畅度的要求！这样每次你能得到差不多 50ms 的计算时间，如果完全用这 50ms 来做计算，同样会带来交互上的卡顿，所以 React Fiber 是基于自定义一套机制来模拟实现，如：setTimeout、setImmediate、MessageChannel。</p>
<p>以下是 React Fiber 中的主动释放片段代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">workLoop</span>(<span class="hljs-params">hasTimeRemaining, initialTime</span>) </span>&#123;
  <span class="hljs-keyword">let</span> currentTime = initialTime;
  advanceTimers(currentTime);
  currentTask = peek(taskQueue);
  <span class="hljs-keyword">while</span> (
    currentTask !== <span class="hljs-literal">null</span> &&
    !(enableSchedulerDebugging && isSchedulerPaused)
  ) &#123;
    <span class="hljs-keyword">if</span> (
      currentTask.expirationTime > currentTime &&
      (!hasTimeRemaining || shouldYieldToHost())
    ) &#123;
      <span class="hljs-comment">// 如果超时，则主动退出循环，将控制权交还浏览器</span>
      <span class="hljs-keyword">break</span>;
    &#125;
    ...
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">调度任务</h2>
<p>有了中断机制，中断服务后，不同任务就能实现间断执行的可能，如何实现多任务的合理调度，就需要一个调度任务来进行处理，这通常代表着操作系统。例如，当一个任务 A 在执行到一半时，被中断机制强制中断，此时操作系统需要对当前任务 A 进行现场保护，如：寄存器数据，然后切换到下一个任务 B，当任务 A 再次被调度时，操作系统需要还原之前任务 A 的现场信息，如：寄存器数据，从而保证任务 A 能继续执行下一半任务。<strong>调度过程中如何保证被中断任务的信息不被破坏是一个非常重要的功能。</strong></p>
<p>浏览器提供的 RIC 机制，类似“中断服务”注册机制，注册后我们只要合适的时机进行释放，就能实现“中断”效果，刚也提到对于不同任务之间切换，在中断后，需要考虑现场保护和现场还原。早期 React 是同步渲染机制，实际上是一个递归过程，递归可能会带来长的调用栈，这其实会给现场保护和还原变得复杂，React Fiber 的做法将递归过程拆分成一系列小任务(Fiber)，转换成线性的链表结构，此时现场保护只需要保存下一个任务结构信息即可，所以拆分的任务上需要扩展额外信息，该结构记录着任务执行时所需要的必备信息：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    stateNode,
    child,
    <span class="hljs-keyword">return</span>,
    sibling,
    expirationTime
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看以下示例代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"A"</span>></span>
    A
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"B"</span>></span>
      B<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"C"</span>></span>C<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"D"</span>></span>D<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>,
  node
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 React 进行渲染时，会生成如下任务链，此时如果在执行任务 B 后时发现时间不足，主动释放后，只需要记录下一次任务 C 的信息，等再次调度时取得上次记录的信息即可。使用该机制后，对于渲染任务的优先级、撤销、挂起、恢复都能得到非常好的控制。
<img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e82fe600ba244e3b2867143823e1fe0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">总结</h2>
<p>中断机制其实是一种非常重要的解决资源共享的手段，对于操作系统而言，它已经是一个必不可少功能。随着浏览器的功能越来越强，越来越多功能也搬到了浏览器，如何保证用户在使用过程中的流畅，也是经常需要思考的问题，在业务开发过程中，我们可以根据实际场景利用好“中断机制”，提高用户体验。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            