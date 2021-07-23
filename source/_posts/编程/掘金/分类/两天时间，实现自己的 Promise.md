
---
title: '两天时间，实现自己的 Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3239'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:06:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=3239'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>为了更好的理解和实践 promise，我尝试自己写一个实现 promise 所有功能的类，并基于此去做一些扩展，达到可以在生产环境使用的程度；并且为了便于维护和理解，代码全部使用 typescript 编写。</p>
</blockquote>
<h2 data-id="heading-0">01. 目录</h2>
<ul>
<li><a href="https://juejin.cn/post/6987674192166518821#02-%E8%87%AA%E4%B8%8B%E8%80%8C%E4%B8%8A" target="_blank" title="#02-%E8%87%AA%E4%B8%8B%E8%80%8C%E4%B8%8A">02.自下而上</a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#03-%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0" target="_blank" title="#03-%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0">03.如何实现</a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#04-Promise-A-%E8%A7%84%E8%8C%83" target="_blank" title="#04-Promise-A-%E8%A7%84%E8%8C%83">04.Promise/A+规范</a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#05-%E6%9B%B4%E5%A4%9A%E4%BC%98%E5%8C%96" target="_blank" title="#05-%E6%9B%B4%E5%A4%9A%E4%BC%98%E5%8C%96">05.更多优化</a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#06-%E6%BA%90%E7%A0%81" target="_blank" title="#06-%E6%BA%90%E7%A0%81">06.源码</a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#07-%E5%B0%8F%E7%BB%93" target="_blank" title="#07-%E5%B0%8F%E7%BB%93">07.小结</a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#08-%E5%85%B6%E4%BB%96%E5%8F%82%E8%80%83" target="_blank" title="#08-%E5%85%B6%E4%BB%96%E5%8F%82%E8%80%83">08.其他参考</a></li>
</ul>
<h2 data-id="heading-1">02.自下而上</h2>
<h3 data-id="heading-2">02.01 基本概念</h3>
<ul>
<li>首先我们来整理一些 <code>Promise</code> 基本的概念，包括私有状态，内部方法，静态方法等等。</li>
</ul>
<h4 data-id="heading-3">私有属性</h4>
<ul>
<li>私有属性包括状态和值 <code>PromisState</code> <code>PromiseResult</code>，这些属性外部无法访问。</li>
<li>状态属性有以下三种：
<ul>
<li><code>pending</code> 初始化状态</li>
<li><code>fulfilled</code> 兑现(完成)</li>
<li><code>rejected</code> 拒绝</li>
</ul>
</li>
<li>值属性，由 <code>resolve</code> 或 <code>reject</code> 处理来决定。</li>
</ul>
<h4 data-id="heading-4">实例方法</h4>
<ul>
<li><a href="https://juejin.cn/post/6987674192166518821#Promise-prototype-then" target="_blank" title="#Promise-prototype-then"><code>then</code></a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#Promise-prototype-catch" target="_blank" title="#Promise-prototype-catch"><code>catch</code></a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#Promise-prototype-finally" target="_blank" title="#Promise-prototype-finally"><code>finally</code></a></li>
</ul>
<h4 data-id="heading-5">静态方法</h4>
<ul>
<li><a href="https://juejin.cn/post/6987674192166518821#Promise-reject" target="_blank" title="#Promise-reject"><code>Promise.reject</code></a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#Promise-resolve" target="_blank" title="#Promise-resolve"><code>Promise.resolve</code></a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#Promise-race" target="_blank" title="#Promise-race"><code>Promise.race</code></a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#Promise-all" target="_blank" title="#Promise-all"><code>Promise.all</code></a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#Promise-allSettled" target="_blank" title="#Promise-allSettled"><code>Promise.allSettled</code></a></li>
<li><a href="https://juejin.cn/post/6987674192166518821#Promise-any" target="_blank" title="#Promise-any"><code>Promise.any</code></a></li>
</ul>
<h2 data-id="heading-6">03.如何实现</h2>
<h3 data-id="heading-7">03.01 基础类</h3>
<ul>
<li>
<p>在罗列所有的状态和方法之后，我们首先来实现一个最基础的 <code>Promise</code> 类。</p>
</li>
<li>
<p>最基础的类，包括以下核心几点：</p>
<ul>
<li>拥有私有状态，也有着能够改变私有状态的私有方法。</li>
<li>同时接收一个执行器函数作为参数，执行器函数内部则是预先定义好的私有方法。</li>
<li>私有状态一旦改变（兑现或拒绝）后不可逆。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-comment">/**
   * Promise 内部状态的枚举
   */</span>
  <span class="hljs-built_in">enum</span> PROMISE_STATES &#123;
    PENDING = <span class="hljs-string">'pending'</span>,
    FULFILLED = <span class="hljs-string">'fulfilled'</span>,
    REJECTED = <span class="hljs-string">'rejected'</span>
  &#125;

  <span class="hljs-keyword">type</span> PromiseStates = PROMISE_STATES.PENDING | PROMISE_STATES.FULFILLED | PROMISE_STATES.REJECTED;

  <span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> isFunction = (fn: <span class="hljs-built_in">any</span>):<span class="hljs-function"><span class="hljs-params">boolean</span> =></span> <span class="hljs-keyword">typeof</span> fn === <span class="hljs-string">'function'</span>;
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> isObject = (obj: <span class="hljs-built_in">any</span>):<span class="hljs-function"><span class="hljs-params">boolean</span> =></span> <span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">'object'</span>;

  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
    <span class="hljs-keyword">protected</span> PromiseState: PromiseStates;
    <span class="hljs-keyword">protected</span> PromiseResult: <span class="hljs-built_in">any</span>;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.PromiseState = PROMISE_STATES.PENDING;
    <span class="hljs-built_in">this</span>.PromiseResult = <span class="hljs-literal">undefined</span>;

    executor(<span class="hljs-built_in">this</span>._resolve, <span class="hljs-built_in">this</span>._reject)
  &#125;

  _resolve = <span class="hljs-function">(<span class="hljs-params">value?: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PROMISE_STATES.PENDING) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-built_in">this</span>.PromiseState = PROMISE_STATES.FULFILLED;
    <span class="hljs-built_in">this</span>.PromiseResult = value;
  &#125;

  _reject = <span class="hljs-function">(<span class="hljs-params">value?: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PROMISE_STATES.PENDING) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-built_in">this</span>.PromiseState = PROMISE_STATES.REJECTED;
    <span class="hljs-built_in">this</span>.PromiseResult = value;
  &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-8">resolve 和 reject</h4>
<ul>
<li>
<p>上述代码比较好理解， 我们定义了状态，定义了执行器函数以及相关的两个参数，这两个参数对应的方法分别修改了对应的状态。</p>
</li>
<li>
<p>但是差点忘了， <code>Promise</code> 是异步的，意味着这两个函数处理也应当是异步的；这里可以使用 <code>setTimeout</code> 来模拟异步进程。这部分还可以优化，后面我们会提到。</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
    * 使状态变更为 fulfilled
    * 调用注册的事件，注意调用后进行清除
    * <span class="hljs-doctag">@param <span class="hljs-variable">value</span></span>
    * <span class="hljs-doctag">@returns</span>
    */</span>
  _resolve = <span class="hljs-function">(<span class="hljs-params">value?: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-keyword">const</span> resolveCb = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PROMISE_STATES.PENDING) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;

      <span class="hljs-built_in">this</span>.PromiseState = FULFILLED;
      <span class="hljs-built_in">this</span>.PromiseResult = value;
    &#125;

    <span class="hljs-comment">// 使任务变成异步的</span>
    <span class="hljs-built_in">setTimeout</span>(resolveCb, <span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-comment">/**
   * 使状态变更为 rejected
    * <span class="hljs-doctag">@param <span class="hljs-variable">value</span></span>
    */</span>
  _reject = <span class="hljs-function">(<span class="hljs-params">value?: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-keyword">const</span> rejectCb = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PROMISE_STATES.PENDING) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;

      <span class="hljs-built_in">this</span>.PromiseState = REJECTED;
      <span class="hljs-built_in">this</span>.PromiseResult = value;
    &#125;

    <span class="hljs-built_in">setTimeout</span>(rejectCb, <span class="hljs-number">0</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>我们可以接着实现相关的静态方法，因为它们所做的事很简单，就是修改当前的内部状态，于是完全可以直接调用当前类实例化来处理。</p>
</li>
<li>
<p>重复代码不再罗列，下面是新增的静态方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">// ...sth</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value?: <span class="hljs-built_in">any</span></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> resolve(value));
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">value?: <span class="hljs-built_in">any</span></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(value));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>一个简单的基础类就这样完成了。不过先不要着急，当前的实现显然有许多要完善的地方，甚至也许有错误，让我们进一步来梳理。</p>
</li>
</ul>
<h3 data-id="heading-9">03.02 原型方法</h3>
<h4 data-id="heading-10"><code>Promise.prototype.then</code></h4>
<ul>
<li>
<p>相信对 <code>Promise</code> 有所了解的都知道 <code>Promise</code> 的 <code>then</code> 方法以及它的链式调用。本质上，**它是对 <code>Thenable</code> 接口的具体实现。**这句话很重要，后面会用到。</p>
</li>
<li>
<p>让我们先来回顾一下 <code>then</code> 的用法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">29</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fulfilled</span>(<span class="hljs-params">res</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.info(res);
  <span class="hljs-keyword">return</span> res;
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">rejected</span>(<span class="hljs-params">err</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.error(err);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>then</code> 方法接收两个参数，分别用来处理 <code>resolve</code> 和 <code>reject</code> 的结果，称之为完成回调和拒绝回调。默认情况下，同时注册这两个回调方法，一次只可能会调用到其中一个。即使在前一个函数中抛出了异常，第二个异常捕获函数也无法立即捕获。</p>
<ul>
<li>完成回调，接收先前 <code>promise</code> 的 <code>resolve</code> 值作为默认参数，处理对应数据，并返回一个值，作为下一个 <code>then</code> 内部函数调用的默认参数。</li>
<li>让我们再仔细想想， <code>then</code> 注册事件的调用次数是否和注册次数相同？是的。假如使用 <code>then</code> 注册了多个回调函数，则它们会依次执行。这意味着我们得在原先的基础上加上相应的事件队列。</li>
<li>另外别忘了， <code>then</code> 方法支持<strong>链式调用</strong>，我们这里先使用 <code>return this</code> 的方式来简单实现。</li>
</ul>
</li>
<li>
<p>现在我们对上面的基础类进行改进和修复。</p>
<ul>
<li>定义两个数组，分别用来保存完成回调和拒绝回调。</li>
<li>下面罗列核心代码：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> interface ICallbackFn &#123;
  (value?: any): any;
&#125;

type CallbackParams = ICallbackFn | <span class="hljs-literal">null</span>;

<span class="hljs-keyword">export</span> interface IExecutorFn &#123;
  (resolve: ICallbackFn,  <span class="hljs-attr">reject</span>: ICallbackFn): any;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  protected PromiseState: PromiseStates;
  protected PromiseResult: any;

  resolveCallbackQueues: <span class="hljs-built_in">Array</span><ICallbackFn>;
  rejectCallbackQueues: <span class="hljs-built_in">Array</span><ICallbackFn>;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor: IExecutorFn</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!isFunction(executor)) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Promise resolver undefined is not a function'</span>);
    &#125;
    <span class="hljs-built_in">this</span>.PromiseState = PENDING;
    <span class="hljs-built_in">this</span>.PromiseResult = <span class="hljs-literal">undefined</span>;

    <span class="hljs-comment">// 分别用于两个注册事件保存的数组</span>
    <span class="hljs-built_in">this</span>.resolveCallbackQueues = [];
    <span class="hljs-built_in">this</span>.rejectCallbackQueues = [];

    executor(<span class="hljs-built_in">this</span>._resolve, <span class="hljs-built_in">this</span>._reject);
  &#125;

  <span class="hljs-comment">/**
   * 使状态变更为 fulfilled
  * 调用注册的事件，注意调用后进行清除
  * <span class="hljs-doctag">@param <span class="hljs-variable">value</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  _resolve = <span class="hljs-function">(<span class="hljs-params">value: any</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> resolveCb = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PROMISE_STATES.PENDING) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.resolveCallbackQueues.length) &#123;
        <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>.resolveCallbackQueues.shift();
        fn && fn(value);
      &#125;
      <span class="hljs-built_in">this</span>.PromiseState = FULFILLED;
      <span class="hljs-built_in">this</span>.PromiseResult = value;
    &#125;

    <span class="hljs-comment">// 使任务变成异步的</span>
    <span class="hljs-built_in">setTimeout</span>(resolveCb, <span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-comment">/**
   * 使状态变更为 rejected
  * <span class="hljs-doctag">@param <span class="hljs-variable">value</span></span>
  */</span>
  _reject = <span class="hljs-function">(<span class="hljs-params">value: any</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> rejectCb = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PROMISE_STATES.PENDING) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.rejectCallbackQueues.length) &#123;
        <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>.rejectCallbackQueues.shift();
        fn && fn(value);
      &#125;
      <span class="hljs-built_in">this</span>.PromiseState = REJECTED;
      <span class="hljs-built_in">this</span>.PromiseResult = value;
    &#125;

    <span class="hljs-built_in">setTimeout</span>(rejectCb, <span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-comment">/**
   * 根据当前不同状态来执行对应逻辑
  * 如果在默认状态就是注册对应事件
  * 如果状态变化则是执行对应事件
  * <span class="hljs-doctag">@param <span class="hljs-variable">onFulfilled</span></span>
  * <span class="hljs-doctag">@param <span class="hljs-variable">onRejected</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  then = <span class="hljs-function">(<span class="hljs-params">onFulfilled, onRejected</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.PromiseState) &#123;
      <span class="hljs-keyword">case</span> PENDING:
        isFunction(onFulfilled) && <span class="hljs-built_in">this</span>.resolveCallbackQueues.push(onFulfilled);
        isFunction(onRejected) && <span class="hljs-built_in">this</span>.rejectCallbackQueues.push(onRejected);
      <span class="hljs-keyword">case</span> FULFILLED:
        isFunction(onFulfilled) && onFulfilled(<span class="hljs-built_in">this</span>.PromiseResult);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> REJECTED:
        isFunction(onRejected) && onRejected(<span class="hljs-built_in">this</span>.PromiseResult);
        <span class="hljs-keyword">break</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>我们丰富了 <code>then</code> 方法。但是你我都知道，<code>return this</code> 看起来并不太可靠。</p>
</li>
<li>
<p>让我们来回顾一点，<strong><code>Promise</code> 的私有状态一旦改变后不可逆</strong>。如果在这个 <code>then</code> 方法里抛出异常， <code>promise</code> 显然会变成拒绝状态，而同一实例的状态在改变后是不能够再次修改的。所以， <code>then</code> 的链式调用本质上是每次都会生成一个新的实例。</p>
</li>
<li>
<p>也许再贴一个使用 <code>then</code> 的例子会让我们有一些启发。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">123</span>);
<span class="hljs-keyword">const</span> p1 = p.then();
<span class="hljs-keyword">const</span> p2 = p1.then(<span class="hljs-function">(<span class="hljs-params">val</span>) =></span> val + <span class="hljs-number">123</span>))
<span class="hljs-keyword">const</span> p3 = p2.then(<span class="hljs-built_in">console</span>.info));
<span class="hljs-keyword">const</span> p4 = p3.then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Oops!'</span>);
&#125;);
  <span class="hljs-comment">// 分别打印 p1 p2 p3 p4</span>
  <span class="hljs-comment">// Promise &#123;<fulfilled>: 123&#125;</span>
  <span class="hljs-comment">// Promise &#123;<fulfilled>: 246&#125;</span>
  <span class="hljs-comment">// Promise &#123;<fulfilled>: undefined&#125;</span>
  <span class="hljs-comment">// Promise &#123;<rejected>: Error: Oops!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>这段代码的输出，有助于让我们进一步理解 <code>then</code> 内部所做的事。</p>
<ul>
<li>p1: 在没有传入回调函数的时候，它仅仅是将值传递，也就是内部会初始化一个默认的处理函数，这个处理函数只会乖乖地传递值。</li>
<li>p2: 存在完成回调时，可以获取值并进行处理，这个新的值通过<strong>返回的形式</strong>继续往后传递。</li>
<li>p3: 如果传入完成回调函数，但没有显式返回值，则最终的 <code>promise</code> 的值是 <code>undefined</code>.</li>
<li>p4: <code>promise</code> 状态已经变更成 <code>rejected</code>, 意味着是新的 <code>promise</code>. 符合我们的预期。</li>
</ul>
</li>
<li>
<p>带着上述理解，我们来改进 <code>then</code> 方法。</p>
</li>
<li>
<p>首先，需要处理参数异常的情况，也就是传入参数不是函数，或者未传的情况，就给定默认处理函数。</p>
<ul>
<li>完成回调负责传递参数。</li>
<li>拒绝回调负责抛出异常。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts">then = <span class="hljs-function">(<span class="hljs-params">onFulfilled?: CallbackParams, onRejected?: CallbackParams</span>) =></span> &#123;
 <span class="hljs-comment">// 默认处理！！！</span>
 onFulfilled = isFunction(onFulfilled) ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
 onRejected = isFunction(onRejected) ? onRejected : <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-keyword">throw</span> err &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>我们把这两个兼容处理放在函数内的顶部，这样有助于理解，也可以简化后续的逻辑。</p>
</li>
<li>
<p>下面是具体的内容，其中核心改动已注释说明。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * 根据当前不同状态来执行对应逻辑
  * 如果在默认状态就是注册对应事件
  * 如果状态变化则是执行对应事件
  * <span class="hljs-doctag">@param <span class="hljs-variable">onFulfilled</span></span>
  * <span class="hljs-doctag">@param <span class="hljs-variable">onRejected</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  then = <span class="hljs-function">(<span class="hljs-params">onFulfilled: CallbackParams, onRejected: CallbackParams</span>) =></span> &#123;
    <span class="hljs-comment">// 默认处理！！！</span>
    onFulfilled = isFunction(onFulfilled) ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
    onRejected = isFunction(onRejected) ? onRejected : <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-keyword">throw</span> err &#125;;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-comment">/**
       * 封装完成回调函数
      * <span class="hljs-doctag">@param <span class="hljs-variable">val</span></span>
      */</span>
      <span class="hljs-keyword">const</span> handleFulfilled = <span class="hljs-function">(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">const</span> res = onFulfilled(val);
          resolve(res);
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-comment">// 如果当前执行逻辑内发生异常，则抛出异常</span>
          reject(error);
        &#125;
      &#125;;

      <span class="hljs-comment">/**
       * 封装错误回调函数
      * <span class="hljs-doctag">@param <span class="hljs-variable">val</span></span>
      */</span>
      <span class="hljs-keyword">const</span> handleRejected = <span class="hljs-function">(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">const</span> res = onRejected(val);
          reject(res);
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          reject(error);
        &#125;
      &#125;

      <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.PromiseState) &#123;
        <span class="hljs-keyword">case</span> PROMISE_STATES.PENDING:
          <span class="hljs-built_in">this</span>.resolveCallbackQueues.push(handleFulfilled);
          <span class="hljs-built_in">this</span>.rejectCallbackQueues.push(handleRejected);
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> PROMISE_STATES.FULFILLED:
          handleFulfilled(<span class="hljs-built_in">this</span>.PromiseResult);
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> PROMISE_STATES.REJECTED:
          handleRejected(<span class="hljs-built_in">this</span>.PromiseResult);
          <span class="hljs-keyword">break</span>;
      &#125;
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>这个 <code>then</code> 方法的处理已经接近完善，不过在 <code>Promise</code> 里有一点容易被人遗忘。</p>
<ul>
<li>在 <code>Promise</code> 中处理 <code>Promise</code>，内部处理会将其展开来获取其中的值。</li>
<li>下面这个例子出来你就理解了。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">41</span>) === <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">41</span>)); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>不好意思，走错片场。js 中每个单独定义的引用类型都是不相等的。</p>
<ul>
<li>再来一次。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">41</span>);
<span class="hljs-built_in">Promise</span>.resolve(p) === p; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>没错，如果我们给 <code>promise</code> 一个 <code>promise</code> 值，内部机制会将其展开。这个过程是递归的，这里我们先不展开探讨，但记住有这样的场景需要处理。</p>
</li>
<li>
<p>可以先定义一个静态方法判断是否是 <code>Promise</code> 实例，方便后续的判断。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * 判断是否是当前类的实例
  * <span class="hljs-doctag">@param <span class="hljs-variable">promise</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">is</span>(<span class="hljs-params">promise: PromiseType</span>)</span> &#123;
    <span class="hljs-keyword">return</span> promise <span class="hljs-keyword">instanceof</span> PromiseLike;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>有了这个方法，我们可以进一步完善上面的 <code>then</code> 方法。注意观察其中的变化，有注释说明。</p>
</li>
<li>
<p>为方便阅读，只展示核心方法（只有这里改动）。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 封装完成回调函数
* <span class="hljs-doctag">@param <span class="hljs-variable">val</span></span>
*/</span>
<span class="hljs-keyword">const</span> handleFulfilled = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> res = onFulfilled(val);
    <span class="hljs-keyword">if</span> (PromiseLike.is(res)) &#123;
      <span class="hljs-comment">// 如果参数是 Promise 实例，直接可以把 promise 实例进行传递</span>
      res.then(resolve, reject);
    &#125; <span class="hljs-keyword">else</span>  &#123;
      resolve(res);
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-comment">// 如果当前执行逻辑内发生异常，则抛出异常</span>
    reject(error);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-11"><code>Promise.prototype.catch</code></h4>
<ul>
<li>
<p>在实现 <code>then</code> 方法之后，其实 <code>catch</code> 的实现是你想象不到的简单。</p>
</li>
<li>
<p>因为本质上 <code>catch</code> 方法是 <code>then</code> 第二个参数也就是错误回调函数的语法糖。照着这个理解，实现起来就比较容易。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * 错误处理
  * https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch
  * <span class="hljs-doctag">@param <span class="hljs-variable">rejectedCb</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  <span class="hljs-keyword">catch</span> = <span class="hljs-function">(<span class="hljs-params">rejectedCb: CallbackParams</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, rejectedCb);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-12"><code>Promise.prototype.finally</code></h4>
<ul>
<li>
<p>实现 <code>finally</code> 需要我们理解几个点。</p>
<ul>
<li>前面的状态只要不是 <code>pending</code>, 则一定会进入执行。</li>
<li>类似于 <code>then</code>, 它可以注册多个回调，每个回调函数会依次执行。</li>
<li>回调函数内无法获取内部值。</li>
<li>除非在回调函数内抛出异常会把状态变成 <code>rejected</code>，否则它所做的仅仅是把状态和值传递。</li>
</ul>
</li>
<li>
<p>了解上述几点之后，我们可以复用 <code>then</code> 方法，并自定义回调函数传入来实现。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally
  * <span class="hljs-doctag">@param <span class="hljs-variable">finallyCb</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  <span class="hljs-keyword">finally</span> = <span class="hljs-function">(<span class="hljs-params">finallyCb: CallbackParams</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(
      <span class="hljs-comment">// 完成回调时，执行注册函数，并且将原来的值传递下去</span>
      <span class="hljs-comment">// 封装 Promise 类，再调用 then 方法传递</span>
      <span class="hljs-function"><span class="hljs-params">val</span> =></span> PromiseLike.resolve(finallyCb && finallyCb()).then(<span class="hljs-function">() =></span> val),
      <span class="hljs-comment">// 异常回调时，执行注册函数，并且抛出异常</span>
      <span class="hljs-function"><span class="hljs-params">err</span> =></span> PromiseLike.resolve(finallyCb && finallyCb()).then(<span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">throw</span> err &#125;)
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>写到这里，几个核心的原型方法我们就实现完毕了。</p>
</li>
<li>
<p>心急的伙伴可以直接实例化一个对象来尝试，不过 <code>Promise</code> 当然还不止于此，接下来我们来实现对应的静态方法。</p>
</li>
</ul>
<h3 data-id="heading-13">03.03 静态方法</h3>
<ul>
<li>前面已经实现了一个自定义的 <code>Promise.is</code> 方法来判断实例。这个工具类函数简单实用，可以留着。</li>
<li>还有两个快速实例化 <code>Promise</code> 类的方法我们也进行了实现：<code>Promise.resolve</code> 和 <code>Promise.reject</code>. 下面来做一点改进。</li>
</ul>
<h4 data-id="heading-14"><code>Promise.resolve</code></h4>
<ul>
<li>
<p>既然我们定义好了 <code>Promise.is</code> 方法，加上对 <code>Promise</code> 的理解进一步加深，知道了如果传入的已经是 <code>Promise</code> 实例，则不必再进行处理。所以这个方法需要做一点兼容处理。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * 直接实例化 proimse
  * https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve
  * <span class="hljs-doctag">@param <span class="hljs-variable">value</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value?: <span class="hljs-built_in">any</span></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (PromiseLike.is(value)) &#123;
      <span class="hljs-keyword">return</span> value;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> resolve(value));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>现在我们可以尝试实现 <code>Promise</code> 提供的剩下两个类方法 <code>Promise.all</code>, <code>Promise.race</code>.</p>
</li>
</ul>
<h4 data-id="heading-15"><code>Promise.all</code></h4>
<ul>
<li>
<p>该方法是接收一个由 <code>Promise</code> 实例组成的数组，并返回 <code>Promise</code> 实例，其值是所有 <code>Promise</code> 实例的 <code>resolve</code> 的值组成的数组。</p>
<ul>
<li>当其中任意一个 <code>Promise</code> 有 <code>reject</code> 的值时，<code>Promise.all</code> 会返回最先 <code>rejected</code> 的值。</li>
<li>等到所有 <code>Promise</code>  <code>resolve</code> 之后，<code>Promise</code>.all 才会返回结果。</li>
<li><code>Promise.all</code> 也是支持链式调用的。</li>
</ul>
</li>
<li>
<p>大白话也许有些晦涩，我们直接看案例。</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-built_in">Promise</span>.all([<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>), <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-number">2</span>)]); <span class="hljs-comment">// Promise &#123;<rejected>: 2&#125;</span>
  <span class="hljs-built_in">Promise</span>.all([<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>), <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">2</span>)]); <span class="hljs-comment">// Promise &#123;<fulfilled>: Array(2)&#125; [1, 2]</span>
  <span class="hljs-built_in">Promise</span>.all([]); <span class="hljs-comment">// Promise &#123;<fulfilled>: Array(2)&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>其中，第三个表达式的结果对理解 <code>Promise.race</code> 和 <code>Promise.all</code> 的区别很重要。这点后面会谈。除此之外，结果是显而易见的。</p>
</li>
<li>
<p><code>Promise.all</code> 返回的结果是传入数组的参数的顺序，也可以理解为顺序执行，并填入对应的位置。基于这几点，要实现它就有思路了。</p>
<ul>
<li>顺序执行所有 <code>Promise</code>，并把结果保存到数组的对应位置，同时统计已执行的数量；当该数量等同于传入的数组长度时，返回由结果组成的数组。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all
  * <span class="hljs-doctag">@param </span>promises 严格意义上来说，参数是可迭代对象，为了简化实现这里统一成数组
  * <span class="hljs-doctag">@returns</span>
  */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promises: <span class="hljs-built_in">Array</span><ICallbackFn></span>)</span> &#123;
    <span class="hljs-comment">// 支持链式调用</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> len = promises.length;
      <span class="hljs-keyword">let</span> resolvedPromisesCount = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">let</span> resolvedPromisesResult = <<span class="hljs-built_in">any</span>>[];
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
        <span class="hljs-keyword">const</span> currentPromise = promises[i];
        <span class="hljs-comment">// 如果不是 Promise 实例，则需要包装一份；</span>
        <span class="hljs-comment">// 但因为直接包装 Promise 类的效果是幂等的，所以这里不需要判断，直接处理即可</span>
        PromiseLike.resolve(currentPromise)
        .then(<span class="hljs-function">(<span class="hljs-params">res: <span class="hljs-built_in">any</span></span>) =></span> &#123;
          resolvedPromisesCount++;
          resolvedPromisesResult[i] = res;
          <span class="hljs-comment">// 当所有值都 resolve 之后， 返回对应数组</span>
          <span class="hljs-keyword">if</span> (resolvedPromisesCount === len) &#123;
            resolve(resolvedPromisesResult);
          &#125;
        &#125;)
        <span class="hljs-comment">// 如果有任意一个异常，则直接推出</span>
        .catch(<span class="hljs-function">(<span class="hljs-params">err: <span class="hljs-built_in">any</span></span>) =></span> &#123;
          reject(err);
        &#125;);
      &#125;
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>如同在方法注释里说明的一样，其实 <code>Promise.all</code> 和 <code>Promise.race</code> 方法接收的参数都是可迭代对象，并不仅仅是数组。这里为了方便实现，使用数组替代。可迭代对象不在这篇文章的核心讨论范围之内，感兴趣的可以点进上面的链接继续了解。</p>
</li>
</ul>
<h4 data-id="heading-16"><code>Promise.race</code></h4>
<ul>
<li>
<p><code>Promise.race</code> 和 <code>Promise.all</code> 有些相似，至少就参数而言，都接收可迭代对象作为参数，也可以链式调用，意味着它也返回一个新的 <code>Promise</code> 实例。</p>
</li>
<li>
<p>不同的是，<code>Promise.race</code> 将会返回第一个 <code>Promise.resolve</code> 的值，或是第一个 reject 的值，而且这个值并不是数组。</p>
</li>
<li>
<p>了解到这两点之后，实现起来就有清晰的思路了。</p>
<ul>
<li>遍历顺序执行所有 Promise 并取出第一个 resolve 的值。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/race
  * <span class="hljs-doctag">@param <span class="hljs-variable">promises</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promises: <span class="hljs-built_in">Array</span><ICallbackFn></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < promises.length; i++) &#123;
        <span class="hljs-keyword">const</span> currentPromise = promises[i];
        PromiseLike.resolve(currentPromise)
          .then(<span class="hljs-function">(<span class="hljs-params">res: <span class="hljs-built_in">any</span></span>) =></span> &#123;
            resolve(res);
          &#125;)
          .catch(<span class="hljs-function">(<span class="hljs-params">err: <span class="hljs-built_in">any</span></span>) =></span> &#123;
            reject(err);
          &#125;);
      &#125;
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>再运行这样一段代码，得到的结果应该并不会让你意外。</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-built_in">Promise</span>.race([]); <span class="hljs-comment">// Promise &#123;<pending>&#125; 与 Promise.all 的结果不同</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>至此，目前已广泛兼容的两个核心方法我们都已经实现了。这是不是意味着可以愉快的玩耍了呢，当然可以。不过，既然都走到这一步了，我们顺带可以实现更多的 <code>Promise</code> 方法，一来锻炼动手能力，二来证明学以致用。</p>
</li>
</ul>
<h3 data-id="heading-17">03.04 其他静态方法</h3>
<h4 data-id="heading-18"><code>Promise.allSettled</code></h4>
<ul>
<li>
<p>这个方法和 <code>Promise.all</code> 非常相似，执行所有的 <code>Promise</code> 实例并返回所有的结果，不论结果如何，都在返回的数组里塞回一个对象。</p>
<ul>
<li>每个对象只有两个属性 <code>status</code> 和 <code>value</code> 或 <code>reason</code>；如果当前 <code>proimse</code> 是 <code>fulfilled</code> 则属性是 <code>status</code> 和 <code>value</code>, 如果当前是 <code>rejected</code> 则属性是 <code>status</code> 和 <code>reason</code>.</li>
</ul>
</li>
<li>
<p>对 <code>Promise.all</code> 稍加改动就可以实现。</p>
<ul>
<li>判断计数的逻辑在两个回调函数中都进行，并且对返回值加一层包装。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled
* <span class="hljs-doctag">@param </span>promises 严格意义上来说，参数是可迭代对象，为了简化实现这里统一成数组
* <span class="hljs-doctag">@returns</span>
*/</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">allSettled</span>(<span class="hljs-params">promises: <span class="hljs-built_in">Array</span><IPromiseType></span>)</span> &#123;
  <span class="hljs-comment">// 支持链式调用</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> len = promises.length;
    <span class="hljs-keyword">const</span> startTime = <span class="hljs-built_in">Date</span>.now();
    <span class="hljs-keyword">let</span> resolvedPromisesCount = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> resolvedPromisesResult = <<span class="hljs-built_in">any</span>>[];

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
      <span class="hljs-keyword">const</span> currentPromise = promises[i];
      <span class="hljs-comment">// 如果不是 Promise 实例，则需要包装一份；</span>
      <span class="hljs-comment">// 但因为直接包装 Promise 类的效果是幂等的，所以这里不需要判断，直接处理即可</span>
      PromiseLike.resolve(currentPromise)
      .then(<span class="hljs-function">(<span class="hljs-params">res: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        resolvedPromisesCount++;
        resolvedPromisesResult[i] = &#123;
          <span class="hljs-attr">status</span>: PROMISE_STATES.FULFILLED,
          <span class="hljs-attr">value</span>: res
        &#125;;
        <span class="hljs-comment">// 当所有 promises 完成后，返回数组；多封装了一个属性用于显示执行时间</span>
        <span class="hljs-keyword">if</span> (resolvedPromisesCount === len) &#123;
          resolvedPromisesResult.duringTime = <span class="hljs-built_in">Date</span>.now() - startTime + <span class="hljs-string">'ms'</span>;
          resolve(resolvedPromisesResult);
        &#125;
      &#125;)
      <span class="hljs-comment">// 如果有任意一个异常，则直接推出</span>
      .catch(<span class="hljs-function">(<span class="hljs-params">err: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        resolvedPromisesCount++;
        resolvedPromisesResult[i] = &#123;
          <span class="hljs-attr">status</span>: PROMISE_STATES.REJECTED,
          <span class="hljs-attr">reason</span>: err
        &#125;;
        <span class="hljs-keyword">if</span> (resolvedPromisesCount === len) &#123;
          resolvedPromisesResult.duringTime = <span class="hljs-built_in">Date</span>.now() - startTime + <span class="hljs-string">'ms'</span>;
          resolve(resolvedPromisesResult);
        &#125;
      &#125;);
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-19"><code>Promise.any</code></h4>
<ul>
<li>
<p>这是今年(2021)刚刚落定草案的新 API。定义和 <code>Promise.race</code> 很相似，接收可迭代对象作为参数，可以链式调用。</p>
</li>
<li>
<p>不同的是，它会返回第一个落定的，也就是 <code>resolve</code> 的值；如果传入的 <code>promise</code> 全都都进入拒绝状态，则它会等到所有拒绝状态都完成后，再返回一个由拒绝错误组成的对象。这个对象是新定义的类型 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAggregateError" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/AggregateError" ref="nofollow noopener noreferrer">AggregateError</a>，这里暂且先不展开，直接使用它。</p>
</li>
<li>
<p>从定义上来看，它和 <code>Promise.race</code> 相似，不过从实现上观察，却和 <code>Promise.all</code> 更加相似。</p>
<ul>
<li>只需要把计算数量的逻辑搬到错误回调中，并将其返回错误对象即可。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * 2021 年刚纳入规范的 any
  * https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/any
  * <span class="hljs-doctag">@param <span class="hljs-variable">promises</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">any</span>(<span class="hljs-params">promises: <span class="hljs-built_in">Array</span><ICallbackFn></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> len = promises.length;
      <span class="hljs-keyword">let</span> rejectedPromisesCount = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">let</span> rejectedPromisesResult = <any>[];
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < promises.length; i++) &#123;
        <span class="hljs-keyword">const</span> currentPromise = promises[i];
        PromiseLike.resolve(currentPromise)
          .then(<span class="hljs-function">(<span class="hljs-params">res: any</span>) =></span> &#123;
            resolve(res);
          &#125;)
          .catch(<span class="hljs-function">(<span class="hljs-params">err: any</span>) =></span> &#123;
            rejectedPromisesCount++;
            rejectedPromisesResult[i] = err;
            <span class="hljs-keyword">if</span> (rejectedPromisesCount === len) &#123;
              <span class="hljs-comment">// 如果浏览器支持，则直接抛出这个新对象，否则则直接抛出异常</span>
              <span class="hljs-keyword">if</span> (isFunction(AggregateError)) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> AggregateError(rejectedPromisesResult, <span class="hljs-string">'All promises were rejected'</span>);
              &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">throw</span> (rejectedPromisesResult);
              &#125;
            &#125;
          &#125;);
      &#125;
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-20">04.Promise/A+规范</h2>
<h3 data-id="heading-21">04.01 promises-aplus-tests 验证</h3>
<ul>
<li>
<p>这个库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpromises-aplus%2Fpromises-tests%23readme" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/promises-aplus/promises-tests#readme" ref="nofollow noopener noreferrer">promises-aplus-tests</a> 可以用来验证我们实现的 <code>Promise</code> 是否遵循 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpromises-aplus%2Fpromises-spec" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/promises-aplus/promises-spec" ref="nofollow noopener noreferrer">Promise/A+规范</a> 。</p>
</li>
<li>
<p>使用方式比较简单，注入一个方法即可，这个方法返回的对象包含 <code>Promise/resolve/reject</code>.</p>
</li>
<li>
<p>由于我们使用类的方式编写，所以直接新增一个静态函数即可。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * 三方库验证
  * <span class="hljs-doctag">@returns</span>
  */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">deferred</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> defer: <span class="hljs-built_in">any</span> = &#123;&#125;;
    defer.promise = <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      defer.resolve = resolve;
      defer.reject = reject;
    &#125;);
    <span class="hljs-keyword">return</span> defer;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>需要注意的是，要用 <code>commonjs</code> 规范的方式来导出，否则会出现报错。</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-built_in">module</span>.exports = PromiseLike;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>运行 <code>npx promises-aplus-tests 目录名</code> 进行验证。</p>
</li>
</ul>
<h3 data-id="heading-22">04.02 并不完美（兼容修复）</h3>
<ul>
<li>运行结果显示，有部分 case 没有通过。糟透了！下面一一提取。</li>
</ul>
<h4 data-id="heading-23">'Chaining cycle detected for promise'</h4>
<ul>
<li>
<p>这个异常显示，我们不能在 <code>promise</code> 中使用自身，否则会造成死循环。</p>
</li>
<li>
<p>举个例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>).then(<span class="hljs-function">() =></span> p);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>运行这段代码，就会得到上述报错。</p>
</li>
<li>
<p>解决办法并不难，定义变量来保存 <code>then</code> 函数的返回值，同时在内部方法返回的位置进行兼容处理，如果相等就抛出异常。</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-keyword">const</span> res = onFulfilled(val);
  <span class="hljs-comment">// 返回的 promise 不可以是当前的 promise 否则会造成死循环</span>
  <span class="hljs-keyword">if</span> (newPromise === res) &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Chaining cycle detected for promise #<Promise>'</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-24"><code>2.3.3: Otherwise, if </code>x<code> is an object or function</code></h4>
<ul>
<li>
<p>再次执行，发现 <code>Promise</code> 规范对传入参数是对象和函数类型也有着特殊的处理。我们并没有处理，所以出现了上述报错。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpromises-aplus%2Fpromises-spec" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/promises-aplus/promises-spec" ref="nofollow noopener noreferrer">规范里</a> 有所定义，我们可以简单理解为如果传入的参数是 <code>Thenable</code> 的，则需要调用其中的 <code>then</code> 方法，也就是将其展开调用。上文中自己有提到，终究是逃不过。</p>
</li>
<li>
<p>之前我们仅仅对 <code>Promise</code> 的实例进行了特殊处理，现在意识到还需要处理 <code>Thenable</code> 接口的对象。但因为 <code>Promise</code> 实例本身就是实现 <code>Thenable</code> 接口的特殊对象。(<code>typeof Promise.resolve(1); // object</code>)，所以实现了对 <code>Thenable</code> 接口的处理，自然也能涵盖原有的逻辑。</p>
</li>
<li>
<p>新定义一个单独的方法来实现，以提高可读性。</p>
<ul>
<li>这个函数有些复杂，但每一条逻辑都可以在规范里追溯。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 该实现遵循 Promise/A+ 规范
* https://github.com/promises-aplus/promises-spec
* <span class="hljs-doctag">@param <span class="hljs-variable">promise</span></span>
* <span class="hljs-doctag">@param <span class="hljs-variable">x</span></span>
* <span class="hljs-doctag">@param <span class="hljs-variable">resolve</span></span>
* <span class="hljs-doctag">@param <span class="hljs-variable">reject</span></span>
* <span class="hljs-doctag">@returns</span>
*/</span>
<span class="hljs-keyword">const</span> resolvePromise = <span class="hljs-function">(<span class="hljs-params">promise: <span class="hljs-built_in">any</span>, x: <span class="hljs-built_in">any</span>, resolve: ICallbackFn, reject: ICallbackFn</span>) =></span> &#123;
  <span class="hljs-comment">// 返回的 promise 不可以是当前的 promise 否则会造成死循环</span>
  <span class="hljs-keyword">if</span> (newPromise === x) &#123;
    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Chaining cycle detected for promise #<Promise>'</span>));
  &#125;
  <span class="hljs-comment">// 对可能是 thenable 接口实现的对象判断</span>
  <span class="hljs-keyword">if</span> (isObject(x) || isFunction(x)) &#123;
    <span class="hljs-keyword">if</span> (x === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">return</span> resolve(x);
    &#125;
    <span class="hljs-keyword">let</span> thenCb;
    <span class="hljs-keyword">try</span> &#123;
      thenCb = x.then;
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-keyword">return</span> reject(error);
    &#125;

    <span class="hljs-comment">// 如果是 thenable 的对象，则调用其 then 方法</span>
    <span class="hljs-comment">// 这一步涵盖了 Promise 实例的可能性</span>
    <span class="hljs-keyword">if</span> (isFunction(thenCb)) &#123;
      <span class="hljs-keyword">let</span> isCalled = <span class="hljs-literal">false</span>;
      <span class="hljs-keyword">try</span> &#123;
        thenCb.call(
          x, <span class="hljs-comment">// 指向当前函数或对象</span>
          <span class="hljs-function">(<span class="hljs-params">y: <span class="hljs-built_in">any</span></span>) =></span> &#123;
            <span class="hljs-comment">// 如果 resolvePromise 和 rejectPromise 都可能被调用</span>
            <span class="hljs-comment">// 则只需调用第一次（resolvePromise 或 rejectPromise），后续无需再执行</span>
            <span class="hljs-keyword">if</span> (isCalled) <span class="hljs-keyword">return</span>;
            isCalled = <span class="hljs-literal">true</span>;
            <span class="hljs-comment">// 传入当前函数，以实现递归展开调用</span>
            resolvePromise(promise, y, resolve, reject);
          &#125;,
          <span class="hljs-function">(<span class="hljs-params">r: <span class="hljs-built_in">any</span></span>) =></span> &#123;
            <span class="hljs-comment">// 对应前面任意的调用之后，就不再只需后续逻辑</span>
            <span class="hljs-keyword">if</span> (isCalled) <span class="hljs-keyword">return</span>;
            isCalled = <span class="hljs-literal">true</span>;
            reject(r);
          &#125;
        )
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-keyword">if</span> (isCalled) <span class="hljs-keyword">return</span>;
        reject(error);
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      resolve(x);
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    resolve(x);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在原先处理数据的地方，换成 <code>resolvePromise</code> 函数就可以了。</p>
</li>
<li>
<p>这下是可算是完整通过测试了。</p>
<pre><code class="hljs language-shell copyable" lang="shell">872 passing (14s)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-25">05.更多优化</h2>
<h3 data-id="heading-26">05.01 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindowOrWorkerGlobalScope%2FqueueMicrotask" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask" ref="nofollow noopener noreferrer">queueMicrosoft</a></h3>
<ul>
<li>学习过程中，意外发现 <code>queueMicrosoft</code> 这个方法，用于将任务转换成微任务。我们知道 <code>setTimeout</code> 虽然可以实现异步的效果，但它属于宏任务，与 <code>Promise</code> 所属的微任务不符。所以可以用 <code>queueMicrosoft</code> 来替换。</li>
<li>有关使用方式，可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTML_DOM_API%2FMicrotask_guide" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTML_DOM_API/Microtask_guide" ref="nofollow noopener noreferrer">查看这里</a></li>
</ul>
<h3 data-id="heading-27">05.02 typescript 完善</h3>
<ul>
<li>
<p>前面的例子里已经定义许多接口。这里举个例子完善一哈，更多详细内容可以查看下文的源码。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> IPromiseType &#123;
  <span class="hljs-attr">then</span>: IExecutorFn;
  <span class="hljs-keyword">catch</span>: ICallbackFn;
  <span class="hljs-keyword">finally</span>: ICallbackFn;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> <span class="hljs-title">implements</span> <span class="hljs-title">IPromiseType</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>由于自己的 typescript 实践仍在学习中，可能源码中还存在许多值得改进和优化的地方，可以在评论或 issue 中指出，合理的改进建议一定会采纳并实践。</p>
</li>
<li>
<p>使用版本：<code>"typescript": "^4.3.5"</code></p>
</li>
</ul>
<h3 data-id="heading-28">05.03 花里胡哨的变种方法</h3>
<h4 data-id="heading-29"><code>Promise.last</code></h4>
<ul>
<li>
<p>定义一个函数，返回最后一个完成的 <code>promise</code>, 并且可以选择是否需要 <code>rejected</code> 的 <code>promise</code>.</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 返回最后一个完成的值，可以自行决定是否忽略异常
* 如果不忽略，异常优先抛出
* 如果忽略，返回完成值
* <span class="hljs-doctag">@param <span class="hljs-variable">promises</span></span>
* <span class="hljs-doctag">@param <span class="hljs-variable">ignoreRejected</span></span>
* <span class="hljs-doctag">@returns</span>
*/</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">last</span>(<span class="hljs-params">promises: <span class="hljs-built_in">Array</span><IPromiseType>, ignoreRejected: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> len = promises.length;
    <span class="hljs-keyword">const</span> startTime = <span class="hljs-built_in">Date</span>.now();
    <span class="hljs-keyword">let</span> resolvedPromisesCount = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
      <span class="hljs-keyword">const</span> currentPromise = promises[i];
      PromiseLike.resolve(currentPromise)
      .then(<span class="hljs-function">(<span class="hljs-params">res: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        resolvedPromisesCount++;
        <span class="hljs-comment">// 当所有 promises 完成后，返回最后一个值；封装一个属性用于显示执行时间</span>
        <span class="hljs-keyword">if</span> (resolvedPromisesCount === len) &#123;
          isObject(res) && (res.duringTime = <span class="hljs-built_in">Date</span>.now() - startTime + <span class="hljs-string">'ms'</span>);
          resolve(res);
        &#125;
      &#125;)
      <span class="hljs-comment">// 如果有任意一个异常，则直接推出</span>
      .catch(<span class="hljs-function">(<span class="hljs-params">err: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (ignoreRejected) &#123;
          resolvedPromisesCount++;
        &#125; <span class="hljs-keyword">else</span> &#123;
          reject(err)
        &#125;
      &#125;);
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>还可以实现一个它的变种，即返回最后一个更新的值，不论是 <code>fulfilled</code> 或者 <code>rejected</code> 状态.源码有展示，这里不再赘述。</p>
</li>
</ul>
<h4 data-id="heading-30"><code>Promise.wrap</code></h4>
<ul>
<li>
<p>该方法可以将原来的普通异步请求包装成 <code>Promise</code> 实例，便于链式调用等。</p>
</li>
<li>
<p>假设有这样一个请求处理函数。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">url, cb</span>) </span>&#123;
  ajax(url, cb);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>想让它变成可以使用链式调用，使用方式见注释。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 把不是 promise 实例的函数包装成 promise 实例
* 例如 ajax 请求
* const request = Promise.wrap(ajax);
* request.then(callback);
* <span class="hljs-doctag">@param <span class="hljs-variable">fn</span></span>
* <span class="hljs-doctag">@returns</span>
*/</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">wrap</span>(<span class="hljs-params">fn: <span class="hljs-built_in">any</span></span>)</span> &#123;
  <span class="hljs-keyword">if</span> (!isFunction(fn)) &#123;
    <span class="hljs-keyword">return</span> fn;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> args: <span class="hljs-built_in">any</span>[] = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
      fn.apply(<span class="hljs-literal">null</span>, args.concat(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res: <span class="hljs-built_in">any</span>, err: <span class="hljs-built_in">any</span></span>) </span>&#123;
        res && resolve(res);
        err && resolve(err);
      &#125;));
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-31"><code>Promise.sequence</code></h4>
<ul>
<li>
<p>链式调用的能力可以结合数组的 <code>reduce</code> 完成串行操作，把函数传入组合成新的函数。</p>
<ul>
<li>这里的参数不涉及 <code>Promise</code> 实例，使用链式调用来实现。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 返回一个函数来执行
* <span class="hljs-doctag">@param <span class="hljs-variable">fns</span></span>
* <span class="hljs-doctag">@returns</span>
*/</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">sequence</span>(<span class="hljs-params">fns: <span class="hljs-built_in">Array</span><ICallbackFn></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>) =></span> fns.reduce(<span class="hljs-function">(<span class="hljs-params">acc, fn: ICallbackFn</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!isFunction(fn)) &#123;
      fn = <span class="hljs-function"><span class="hljs-params">x</span> =></span> x;
    &#125;
    <span class="hljs-keyword">return</span> acc.then(fn).catch(<span class="hljs-function">(<span class="hljs-params">err: <span class="hljs-built_in">any</span></span>) =></span> &#123; <span class="hljs-keyword">throw</span> err &#125;);
  &#125;, PromiseLike.resolve(x));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>假设有多个函数，我们可以通过这样的操作来将它们组合，组合的内容是处理函数。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addThree</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x + <span class="hljs-number">3</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addFive</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x + <span class="hljs-number">5</span>;
&#125;
<span class="hljs-keyword">const</span> addEight = ProimseLike.sequence([addThree, addFive]);
addEight(<span class="hljs-number">2</span>); <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>上面的函数其实已经实现了串行；还可以做一些改动把每个值按顺序保存下来。</p>
</li>
</ul>
<h4 data-id="heading-32"><code>Promise.sequenceByOrder</code></h4>
<ul>
<li>
<p>该方法顺序执行函数，并返回按完成顺序排列的值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 串行执行所有 promises,并返回按返回顺序排列的数组
* 注意接收的参数是返回 promise 实例的函数组成的数组
* <span class="hljs-doctag">@param <span class="hljs-variable">promises</span></span>
* <span class="hljs-doctag">@returns</span>
*/</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">sequenceByOrder</span>(<span class="hljs-params">promises: <span class="hljs-built_in">Array</span><ICallbackFn></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> promiseResults: <span class="hljs-built_in">any</span> = [];
    <span class="hljs-keyword">const</span> reduceRes = promises.reduce(<span class="hljs-function">(<span class="hljs-params">prevPromise, currentPromise: ICallbackFn, currentIndex: <span class="hljs-built_in">number</span></span>) =></span> &#123;
      <span class="hljs-keyword">return</span> prevPromise.then(<span class="hljs-function">(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        promiseResults.push(val);
        <span class="hljs-keyword">const</span> newVal = currentPromise(val);
        <span class="hljs-comment">// 最后一次循环时保存，并剔除第一个值（默认 undefined)</span>
        <span class="hljs-keyword">if</span> (currentIndex === promises.length - <span class="hljs-number">1</span>) &#123;
          promiseResults.unshift();
        &#125;
        <span class="hljs-keyword">return</span> newVal;
      &#125;);
    &#125;, PromiseLike.resolve());
    reduceRes.then(<span class="hljs-function">(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>) =></span> &#123;
      promiseResults.push(val);
      resolve(promiseResults);
    &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-33"><code>Promise.map</code></h4>
<ul>
<li>
<p>定义一个可以处理所有 <code>promise</code> 值的函数，类似数组的 <code>map</code> 方法。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 对每个 promise 的值进行特定的处理
* Promise.map([p1, p2, p3], (val, resolve) => &#123;
*   resolve(val + 1);
* &#125;)
* <span class="hljs-doctag">@param <span class="hljs-variable">promises</span></span>
* <span class="hljs-doctag">@param <span class="hljs-variable">fn</span></span>
* <span class="hljs-doctag">@returns</span>
*/</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">map</span>(<span class="hljs-params">promises: <span class="hljs-built_in">Array</span><IPromiseType>, fn: <span class="hljs-built_in">any</span></span>)</span> &#123;
  <span class="hljs-keyword">return</span> PromiseLike.all(promises.map(<span class="hljs-function">(<span class="hljs-params">currentPromise</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (!isFunction(fn)) &#123;
        fn = <span class="hljs-function">(<span class="hljs-params">val:<span class="hljs-built_in">any</span>, resolve: ICallbackFn</span>) =></span> resolve(val);
      &#125;
      fn(currentPromise, resolve);
    &#125;)
  &#125;));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-34"><code>Promise.observe</code></h4>
<ul>
<li>
<p>定义这样一个函数，用于清理 <code>promise</code> 相关的副作用，通常用在 <code>Promise.race</code> 中。假设我们使用 <code>Promise.race</code> 来设定超时，但仍然希望超时的场景里能够处理数据。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * Promise.race([Promise.observe(p, cleanup // 处理函数), timeoutFn // 超时函数])
* <span class="hljs-doctag">@param <span class="hljs-variable">promise</span></span>
* <span class="hljs-doctag">@param <span class="hljs-variable">fn</span></span>
* <span class="hljs-doctag">@returns</span>
*/</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">observe</span>(<span class="hljs-params">promise: IPromiseType, fn: ICallbackFn</span>)</span> &#123;
  promise
  .then(<span class="hljs-function">(<span class="hljs-params">res: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    PromiseLike.resolve(res).then(fn);
  &#125;, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    PromiseLike.resolve(err).then(fn);
  &#125;);
  <span class="hljs-keyword">return</span> promise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-35">06.源码</h2>
<h3 data-id="heading-36">06.01 部分源码</h3>
<ul>
<li>
<p>所有源码虽不多，全部张贴出来也比较占版面。下面是 <code>then</code> 的完整实现。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PromiseLike</span> </span>&#123;
  <span class="hljs-comment">/**
   * 根据当前不同状态来执行对应逻辑
  * 如果在默认状态就是注册对应事件
  * 如果状态变化则是执行对应事件
  * <span class="hljs-doctag">@param <span class="hljs-variable">onFulfilled</span></span>
  * <span class="hljs-doctag">@param <span class="hljs-variable">onRejected</span></span>
  * <span class="hljs-doctag">@returns</span>
  */</span>
  then = <span class="hljs-function">(<span class="hljs-params">onFulfilled?: CallbackParams, onRejected?: CallbackParams</span>) =></span> &#123;
    <span class="hljs-comment">// 默认处理！！！</span>
    onFulfilled = isFunction(onFulfilled) ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
    onRejected = isFunction(onRejected) ? onRejected : <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-keyword">throw</span> err &#125;;

    <span class="hljs-comment">/**
     * 该实现遵循 Promise/A+ 规范
    * https://github.com/promises-aplus/promises-spec
    * <span class="hljs-doctag">@param <span class="hljs-variable">promise</span></span>
    * <span class="hljs-doctag">@param <span class="hljs-variable">x</span></span>
    * <span class="hljs-doctag">@param <span class="hljs-variable">resolve</span></span>
    * <span class="hljs-doctag">@param <span class="hljs-variable">reject</span></span>
    * <span class="hljs-doctag">@returns</span>
    */</span>
    <span class="hljs-keyword">const</span> resolvePromise = <span class="hljs-function">(<span class="hljs-params">promise: IPromiseType, x: <span class="hljs-built_in">any</span>, resolve: ICallbackFn, reject: ICallbackFn</span>) =></span> &#123;
      <span class="hljs-comment">// 返回的 promise 不可以是当前的 promise 否则会造成死循环</span>
      <span class="hljs-keyword">if</span> (newPromise === x) &#123;
        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Chaining cycle detected for promise #<Promise>'</span>));
      &#125;
      <span class="hljs-comment">// 对可能是 thenable 接口实现的对象判断</span>
      <span class="hljs-keyword">if</span> (isObject(x) || isFunction(x)) &#123;
        <span class="hljs-keyword">if</span> (x === <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-keyword">return</span> resolve(x);
        &#125;
        <span class="hljs-keyword">let</span> thenCb;
        <span class="hljs-keyword">try</span> &#123;
          thenCb = x.then;
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-keyword">return</span> reject(error);
        &#125;

        <span class="hljs-comment">// 如果是 thenable 的对象，则调用其 then 方法</span>
        <span class="hljs-comment">// 这一步涵盖了 Promise 实例的可能性</span>
        <span class="hljs-keyword">if</span> (isFunction(thenCb)) &#123;
          <span class="hljs-keyword">let</span> isCalled = <span class="hljs-literal">false</span>;
          <span class="hljs-keyword">try</span> &#123;
            thenCb.call(
              x, <span class="hljs-comment">// 指向当前函数或对象</span>
              <span class="hljs-function">(<span class="hljs-params">y: <span class="hljs-built_in">any</span></span>) =></span> &#123;
                <span class="hljs-comment">// 如果 resolvePromise 和 rejectPromise 都可能被调用</span>
                <span class="hljs-comment">// 则只需调用第一次（resolvePromise 或 rejectPromise），后续无需再执行</span>
                <span class="hljs-keyword">if</span> (isCalled) <span class="hljs-keyword">return</span>;
                isCalled = <span class="hljs-literal">true</span>;
                <span class="hljs-comment">// 传入当前函数，以实现递归展开调用</span>
                resolvePromise(promise, y, resolve, reject);
              &#125;,
              <span class="hljs-function">(<span class="hljs-params">r: <span class="hljs-built_in">any</span></span>) =></span> &#123;
                <span class="hljs-comment">// 对应前面任意的调用之后，就不再只需后续逻辑</span>
                <span class="hljs-keyword">if</span> (isCalled) <span class="hljs-keyword">return</span>;
                isCalled = <span class="hljs-literal">true</span>;
                reject(r);
              &#125;
            )
          &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            <span class="hljs-keyword">if</span> (isCalled) <span class="hljs-keyword">return</span>;
            reject(error);
          &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
          resolve(x);
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        resolve(x);
      &#125;
    &#125;

    <span class="hljs-comment">// 定义变量，用于传参进行比较</span>
    <span class="hljs-keyword">const</span> newPromise = <span class="hljs-keyword">new</span> PromiseLike(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-comment">/**
       * 封装完成回调函数
      * <span class="hljs-doctag">@param <span class="hljs-variable">val</span></span>
      */</span>
      <span class="hljs-keyword">const</span> handleFulfilled = <span class="hljs-function">(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">const</span> x = onFulfilled && onFulfilled(val);
          resolvePromise(newPromise, x, resolve, reject);
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-comment">// 如果当前执行逻辑内发生异常，则抛出异常</span>
          reject(error);
        &#125;;
      &#125;;

      <span class="hljs-comment">/**
       * 封装错误回调函数
      * <span class="hljs-doctag">@param <span class="hljs-variable">val</span></span>
      */</span>
      <span class="hljs-keyword">const</span> handleRejected = <span class="hljs-function">(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>) =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">const</span> x = onRejected && onRejected(val);
          resolvePromise(newPromise, x, resolve, reject);
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          reject(error);
        &#125;
      &#125;

      <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.PromiseState) &#123;
        <span class="hljs-keyword">case</span> PROMISE_STATES.PENDING:
          <span class="hljs-built_in">this</span>.resolveCallbackQueues.push(handleFulfilled);
          <span class="hljs-built_in">this</span>.rejectCallbackQueues.push(handleRejected);
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> PROMISE_STATES.FULFILLED:
          handleFulfilled(<span class="hljs-built_in">this</span>.PromiseResult);
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> PROMISE_STATES.REJECTED:
          handleRejected(<span class="hljs-built_in">this</span>.PromiseResult);
          <span class="hljs-keyword">break</span>;
      &#125;
    &#125;);

    <span class="hljs-keyword">return</span> newPromise;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-37">06.02 全部源码</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkyriejoshua%2Fpromise-like%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/kyriejoshua/promise-like/" ref="nofollow noopener noreferrer">Github 地址</a></li>
</ul>
<h2 data-id="heading-38">07.小结</h2>
<ul>
<li>在这次尝试实现 <code>Promise</code> 的过程中，自己也在边写边学。这是我理解和实践的整个思路，并不一定适用其他人；希望它能作为一种参考，启发或者影响到他人。在写这篇文章之前，我没想到会投入了整整两天时间，却也只是弄懂了些皮毛。 而 <code>Promise</code> 内部显然还有许多值得探讨的地方，涉及的微任务， <code>async/await</code> 相关，迭代器和生成器；只是目前精力所限，先止于此。后面也许会解析迭代器和生成器的内容。</li>
<li>整个实践，也是自己练习 <code>typescipt</code> 的过程，这里我使用类的方式编写，主要是便于自己理解；但它也完全可以用函数实现。<code>typescript</code> 编译后的代码就是函数的实现，而且是 js. 可以直接查看下面的地址了解。另外，其中内容的编译转换也是值得探索的。
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkyriejoshua%2Fpromise-like%2Fblob%2Fmaster%2Fdist%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/kyriejoshua/promise-like/blob/master/dist/index.js" ref="nofollow noopener noreferrer">Github</a></li>
</ul>
</li>
</ul>
<h2 data-id="heading-39">08.其他参考</h2>
<h3 data-id="heading-40">08.01 参考内容</h3>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/" ref="nofollow noopener noreferrer">Typescript</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FLearn%2FJavaScript%2FAsynchronous%2FPromises" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Promises" ref="nofollow noopener noreferrer">优雅的异步处理</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise" ref="nofollow noopener noreferrer">内置对象 Promise</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpromisesaplus.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://promisesaplus.com/" ref="nofollow noopener noreferrer">Promise/A+</a></p>
<p><a href="https://juejin.cn/post/6945319439772434469" target="_blank" title="https://juejin.cn/post/6945319439772434469">Promise 实现</a></p>
</blockquote></div>  
</div>
            