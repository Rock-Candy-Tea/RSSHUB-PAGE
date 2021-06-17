
---
title: 'react源码解析14.手写hooks'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9331'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 16:50:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=9331'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">react源码解析14.手写hooks</h2>
<h4 data-id="heading-1">视频课程（高效学习）：<a href="https://xiaochen1024.com/series/60b1b600712e370039088e24/60b1b636712e370039088e25" target="_blank" rel="nofollow noopener noreferrer">进入课程</a></h4>
<h4 data-id="heading-2">课程目录：</h4>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b311cf10a4003b634719" target="_blank" rel="nofollow noopener noreferrer">1.开篇介绍和面试题</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b31ccf10a4003b63471a" target="_blank" rel="nofollow noopener noreferrer">2.react的设计理念</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b328cf10a4003b63471b" target="_blank" rel="nofollow noopener noreferrer">3.react源码架构</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b32ecf10a4003b63471c" target="_blank" rel="nofollow noopener noreferrer">4.源码目录结构和调试</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b334cf10a4003b63471d" target="_blank" rel="nofollow noopener noreferrer">5.jsx&核心api</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b33acf10a4003b63471e" target="_blank" rel="nofollow noopener noreferrer">6.legacy和concurrent模式入口函数</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b340cf10a4003b63471f" target="_blank" rel="nofollow noopener noreferrer">7.Fiber架构</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b348cf10a4003b634720" target="_blank" rel="nofollow noopener noreferrer">8.render阶段</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b354cf10a4003b634721" target="_blank" rel="nofollow noopener noreferrer">9.diff算法</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b360cf10a4003b634722" target="_blank" rel="nofollow noopener noreferrer">10.commit阶段</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b367cf10a4003b634723" target="_blank" rel="nofollow noopener noreferrer">11.生命周期</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b36ecf10a4003b634724" target="_blank" rel="nofollow noopener noreferrer">12.状态更新流程</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b374cf10a4003b634725" target="_blank" rel="nofollow noopener noreferrer">13.hooks源码</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b37acf10a4003b634726" target="_blank" rel="nofollow noopener noreferrer">14.手写hooks</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b556cf10a4003b634727" target="_blank" rel="nofollow noopener noreferrer">15.scheduler&Lane</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b55ccf10a4003b634728" target="_blank" rel="nofollow noopener noreferrer">16.concurrent模式</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b564cf10a4003b634729" target="_blank" rel="nofollow noopener noreferrer">17.context</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b56ccf10a4003b63472a" target="_blank" rel="nofollow noopener noreferrer">18事件系统</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b57bcf10a4003b63472b" target="_blank" rel="nofollow noopener noreferrer">19.手写迷你版react</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b581cf10a4003b63472c" target="_blank" rel="nofollow noopener noreferrer">20.总结&第一章的面试题解答</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b587cf10a4003b63472d" target="_blank" rel="nofollow noopener noreferrer">21.demo</a></p>
<p>最关键的是要理解hook队列和update队列的指针指向和updateQueue的更新计算，详细见视频讲解</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;

<span class="hljs-keyword">let</span> workInProgressHook;<span class="hljs-comment">//当前工作中的hook</span>
<span class="hljs-keyword">let</span> isMount = <span class="hljs-literal">true</span>;<span class="hljs-comment">//是否时mount时</span>

<span class="hljs-keyword">const</span> fiber = &#123;<span class="hljs-comment">//fiber节点</span>
  <span class="hljs-attr">memoizedState</span>: <span class="hljs-literal">null</span>,<span class="hljs-comment">//hook链表</span>
  <span class="hljs-attr">stateNode</span>: App<span class="hljs-comment">//dom</span>
&#125;;

<span class="hljs-keyword">const</span> Dispatcher = (<span class="hljs-function">() =></span> &#123;<span class="hljs-comment">//Dispatcher对象</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountWorkInProgressHook</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">//mount时调用</span>
    <span class="hljs-keyword">const</span> hook = &#123;<span class="hljs-comment">//构建hook</span>
      <span class="hljs-attr">queue</span>: &#123;<span class="hljs-comment">//更新队列</span>
        <span class="hljs-attr">pending</span>: <span class="hljs-literal">null</span><span class="hljs-comment">//未执行的update队列</span>
      &#125;,
      <span class="hljs-attr">memoizedState</span>: <span class="hljs-literal">null</span>,<span class="hljs-comment">//当前state</span>
      <span class="hljs-attr">next</span>: <span class="hljs-literal">null</span><span class="hljs-comment">//下一个hook</span>
    &#125;;
    <span class="hljs-keyword">if</span> (!fiber.memoizedState) &#123;
      fiber.memoizedState = hook;<span class="hljs-comment">//第一个hook的话直接赋值给fiber.memoizedState</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      workInProgressHook.next = hook;<span class="hljs-comment">//不是第一个的话就加在上一个hook的后面，形成链表</span>
    &#125;
    workInProgressHook = hook;<span class="hljs-comment">//记录当前工作的hook</span>
    <span class="hljs-keyword">return</span> workInProgressHook;
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateWorkInProgressHook</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">//update时调用</span>
    <span class="hljs-keyword">let</span> curHook = workInProgressHook;
    workInProgressHook = workInProgressHook.next;<span class="hljs-comment">//下一个hook</span>
    <span class="hljs-keyword">return</span> curHook;
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useState</span>(<span class="hljs-params">initialState</span>) </span>&#123;
    <span class="hljs-keyword">let</span> hook;
    <span class="hljs-keyword">if</span> (isMount) &#123;
      hook = mountWorkInProgressHook();
      hook.memoizedState = initialState;<span class="hljs-comment">//初始状态</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      hook = updateWorkInProgressHook();
    &#125;

    <span class="hljs-keyword">let</span> baseState = hook.memoizedState;<span class="hljs-comment">//初始状态</span>
    <span class="hljs-keyword">if</span> (hook.queue.pending) &#123;
      <span class="hljs-keyword">let</span> firstUpdate = hook.queue.pending.next;<span class="hljs-comment">//第一个update</span>

      <span class="hljs-keyword">do</span> &#123;
        <span class="hljs-keyword">const</span> action = firstUpdate.action;
        baseState = action(baseState);
        firstUpdate = firstUpdate.next;<span class="hljs-comment">//循环update链表</span>
      &#125; <span class="hljs-keyword">while</span> (firstUpdate !== hook.queue.pending);<span class="hljs-comment">//通过update的action计算state</span>

      hook.queue.pending = <span class="hljs-literal">null</span>;<span class="hljs-comment">//重置update链表</span>
    &#125;
    hook.memoizedState = baseState;<span class="hljs-comment">//赋值新的state</span>

    <span class="hljs-keyword">return</span> [baseState, dispatchAction.bind(<span class="hljs-literal">null</span>, hook.queue)];<span class="hljs-comment">//useState的返回</span>
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    useState
  &#125;;
&#125;)();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatchAction</span>(<span class="hljs-params">queue, action</span>) </span>&#123;<span class="hljs-comment">//触发更新</span>
  <span class="hljs-keyword">const</span> update = &#123;<span class="hljs-comment">//构建update</span>
    action,
    <span class="hljs-attr">next</span>: <span class="hljs-literal">null</span>
  &#125;;
  <span class="hljs-keyword">if</span> (queue.pending === <span class="hljs-literal">null</span>) &#123;
    update.next = update;<span class="hljs-comment">//update的环状链表</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    update.next = queue.pending.next;<span class="hljs-comment">//新的update的next指向前一个update</span>
    queue.pending.next = update;<span class="hljs-comment">//前一个update的next指向新的update</span>
  &#125;
  queue.pending = update;<span class="hljs-comment">//更新queue.pending</span>

  isMount = <span class="hljs-literal">false</span>;<span class="hljs-comment">//标志mount结束</span>
  workInProgressHook = fiber.memoizedState;<span class="hljs-comment">//更新workInProgressHook</span>
  schedule();<span class="hljs-comment">//调度更新</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> [count, setCount] = Dispatcher.useState(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">let</span> [age, setAge] = Dispatcher.useState(<span class="hljs-number">10</span>);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Clicked &#123;count&#125; times<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(() => count + 1)&#125;> Add count<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Age is &#123;age&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setAge(() => age + 1)&#125;> Add age<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">schedule</span>(<span class="hljs-params"></span>) </span>&#123;
  ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#root"</span>));
&#125;

schedule();
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            