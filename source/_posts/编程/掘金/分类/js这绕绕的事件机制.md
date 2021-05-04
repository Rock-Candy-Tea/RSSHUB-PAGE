
---
title: 'js这绕绕的事件机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5994'
author: 掘金
comments: false
date: Tue, 04 May 2021 00:59:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=5994'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>众所周知，js是单线程，负责页面绘制和用户事件等，即我们通常理解的UI线程，对于页面的绘制，只能在一个线程上更新，这是共识，不然同时有多个线程更新UI，这是不可理解的。虽然android的UI线程也是如此，但是android是支持多线程的，而js就只有单线程，这意味着我们同一时间只能做一件事情，虽说有异步任务，但那也只是把执行时间延后罢了。</p>
<p>当然后面为了适应时代发展，js通过web worker支持了多线程能力，这有一个<a href="https://zhuanlan.zhihu.com/p/29165800" target="_blank" rel="nofollow noopener noreferrer">例子</a></p>
<p>下面是一些概念:</p>
<h2 data-id="heading-0">同步任务</h2>
<p>JS 主线程里面立即被推入执行栈且可以被执行的函数。在主线程上排队执行的任务，只有前一个执行完毕，才能执行后一个，代码是阻塞的，<strong>顺序执行</strong>。要注意的是，click，dispatchEvent等人工合成事件是<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/dispatchEvent" target="_blank" rel="nofollow noopener noreferrer">同步任务</a>，同步调用事件处理程序。可以参考以下链接：</p>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Introducing" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></li>
<li><a href="https://www.zhihu.com/question/362096226" target="_blank" rel="nofollow noopener noreferrer">www.zhihu.com/question/36…</a></li>
</ul>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 下面输出为</span>
<span class="hljs-comment">// on click</span>
<span class="hljs-comment">// end</span>

<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;(ref)</span> =></span> &#123;
      if(ref) &#123;
        ref.click()
        console.log('end')
      &#125;
    &#125;&#125; onClick=&#123;() =>&#123;
      console.log('on click')
    &#125;&#125;>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">异步任务</h2>
<p>如果一个函数在调用之后 不能马上得到预期结果 那么就是异步任务，任务是非阻塞的。</p>
<p>每次执行异步任务，就会将任务放进对应的任务队列。</p>
<ul>
<li>setTimeout  setInterval</li>
<li>promise</li>
<li>dom事件</li>
<li>网络请求</li>
<li>...</li>
</ul>
<h2 data-id="heading-2">事件循环</h2>
<p>js的主线程通过等待任务队列，执行任务源源不断地处理用户事件和页面绘制，每次事件循环称为一次tick，包括从任务队列取出任务执行，清空微任务队列，页面重绘（不一定执行）。</p>
<h3 data-id="heading-3">宏任务（浏览器发起的）</h3>
<p>执行宏任务进入宏任务队列</p>
<ul>
<li>I/O</li>
<li>dom事件</li>
<li>setTimeout setInterval（web api）   浏览器有个定时器模块，定时器到了执行时间才会把异步任务放到异步队列，setTimeOut setInterval的延时就是指多少时间后回调函数会放入任务队列</li>
</ul>
<h3 data-id="heading-4">微任务（js引擎发起的）</h3>
<p>执行微任务会进入当前任务的微任务队列，在下一个事件到来之前会被清空执行。微任务的好处就是优先级高， 但是如果反复执行微任务，会造成下一个事件的处理延后。</p>
<ul>
<li>Promise.then  .catch</li>
<li>MutationObserver</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/HTML_DOM_API/Microtask_guide" target="_blank" rel="nofollow noopener noreferrer">queueMicrotask</a>   把函数当成微任务入队</li>
</ul>
<h3 data-id="heading-5">requestAnimationFrame</h3>
<p>requestAnimationFrame也属于异步任务，但是它比较特殊，既不属于宏也不属于微，它是在event下次重绘之前调用，也就是晚于微任务，早于下一次事件。具体可以看<a href="https://zhuanlan.zhihu.com/p/101374817" target="_blank" rel="nofollow noopener noreferrer">这个</a>。但是每个eventloop不一定会进行重绘，所以在不同浏览器中，requestAnimationFrame的执行时机不太一样，这是重绘时机的<a href="https://html.spec.whatwg.org/multipage/webappapis.html#rendering-opportunity" target="_blank" rel="nofollow noopener noreferrer">规范</a>。</p>
<h3 data-id="heading-6">任务队列</h3>
<p>有一个演示效果的demo <a href="http://latentflip.com/loupe" target="_blank" rel="nofollow noopener noreferrer">latentflip.com/loupe</a></p>
<p><a href="https://pic2.zhimg.com/v2-edca0b28d3de98f77da38d0f994beebd_b.webp" target="_blank" rel="nofollow noopener noreferrer">pic2.zhimg.com/v2-edca0b28…</a></p>
<p>（图片来源<a href="https://zhuanlan.zhihu.com/p/105903652" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/105903652</a>）</p>
<h2 data-id="heading-7">例子</h2>
<p><a href="https://codesandbox.io/s/event--loop-ij9li?file=/src/App.tsx" target="_blank" rel="nofollow noopener noreferrer">代码</a>在这</p>
<p>模拟事件机制</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"--- task start ---"</span>);

  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"macro task 1"</span>);
  &#125;, <span class="hljs-number">0</span>);

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"wait countdown"</span>);

  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolved, reject</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> time = <span class="hljs-built_in">Date</span>.now();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"countdown 500ms start"</span>);
    <span class="hljs-keyword">while</span> (<span class="hljs-built_in">Date</span>.now() - time < <span class="hljs-number">500</span>) &#123;&#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"countdown end"</span>);
    resolved(<span class="hljs-string">'success'</span>)
  &#125;)
  .then(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"micro task 1"</span>);
  &#125;)

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"wait end"</span>);

  queueMicrotask(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"micro task 2"</span>);
  &#125;);

  queueMicrotask(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"micro task 3"</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"---micro task end---"</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"---macro task start---"</span>);
  &#125;);

  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"macro task 2"</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"---macro task end---"</span>);
  &#125;, <span class="hljs-number">0</span>);

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"---task end---"</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"---micro task start---"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-tsx copyable" lang="tsx">输出结果如下：

--- task start --- 
wait countdown 
countdown 500ms start 
countdown end 
wait end 
---task end--- 
---micro task start--- 
micro task <span class="hljs-number">1</span> 
micro task <span class="hljs-number">2</span> 
micro task <span class="hljs-number">3</span> 
---micro task end--- 
---macro task start--- 
macro task <span class="hljs-number">1</span> 
macro task <span class="hljs-number">2</span> 
---macro task end---

<span class="hljs-comment">// 可以看出promise.then是微任务 微任务执行顺序和入队顺序一致</span>
<span class="hljs-comment">// promise里是同步任务 进入执行栈执行</span>
<span class="hljs-comment">// setTimeout是宏任务  执行顺序和入队顺序一致 晚于微任务执行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模拟dom事件</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> <span class="hljs-string">"./styles.css"</span>;

<span class="hljs-keyword">const</span> onClick = <span class="hljs-function">(<span class="hljs-params"><span class="hljs-keyword">type</span>:<span class="hljs-built_in">string</span></span>) =></span> &#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-keyword">type</span>&#125;</span> on click`</span>)
   <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
     <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-keyword">type</span>&#125;</span> micro task`</span>)
   &#125;)
   <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-keyword">type</span>&#125;</span> macro task`</span>)
   &#125;, <span class="hljs-number">0</span>);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>查看点击事件的过程<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"Parent"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>&#123;
          onClick('parent')
        &#125;&#125;>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"Child"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;(ref)</span> =></span> &#123;
           if(ref) &#123;
             console.log('---auto click---')
             ref.click()
           &#125;
        &#125;&#125;onClick=&#123;()=>&#123;
          onClick('child')
        &#125;&#125;>点我<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span> 
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-tsx copyable" lang="tsx">页面加载成功结果如下：
---auto click--- 
child on click 
parent on click 
child micro task 
parent micro task 
child macro task 
parent macro task 
<span class="hljs-comment">// 主动进行事件的合成和分发，这时候两个onClick是作为同步事件进入执行栈，</span>
<span class="hljs-comment">// 两个onClick在同一个事件中，所以会先输出两个on click</span>

点击按钮之后输出结果如下：
child on click 
parent on click 
child micro task 
parent micro task 
child macro task 
parent macro task

<span class="hljs-comment">// 而手动点击则不一样，这时候两个onClick都是作为异步任务进入宏队列</span>
<span class="hljs-comment">// 两个onClick不在同一个事件中，所以第一个onClick的promise会先于第二个onClick执行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">总结</h2>
<p>在每次事件循环中，从宏任务队列取出<strong>任务t</strong>执行，然后把<strong>任务t</strong>里的同步任务按顺序执行,  异步任务则进入任务队列，如果是宏任务，则进入宏任务队列，如果是微任务，则进入当前微任务队列。接着，等执行栈清空之后，会执行当前微任务队列的所有任务，接着浏览器根据是否重绘页面调用requestAnimationFrame。</p>
<h2 data-id="heading-9">参考</h2>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/105903652" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/105903652</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/HTML_DOM_API/Microtask_guide/In_depth" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></li>
<li><a href="https://juejin.cn/post/6844903805063004167" target="_blank">juejin.cn/post/684490…</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/101374817" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/101374817</a></li>
</ul></div>  
</div>
            