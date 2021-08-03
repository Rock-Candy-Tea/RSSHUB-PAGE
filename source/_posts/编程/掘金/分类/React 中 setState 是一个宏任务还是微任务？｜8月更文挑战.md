
---
title: 'React 中 setState 是一个宏任务还是微任务？｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/232fa5cb8a8e491fb489b3c68b1098bf~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 17:16:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/232fa5cb8a8e491fb489b3c68b1098bf~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近有个朋友面试，面试官问了个奇葩的问题，也就是我写在标题上的这个问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/232fa5cb8a8e491fb489b3c68b1098bf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>能问出这个问题，面试官应该对 React 不是很了解，也是可能是看到面试者简历里面有写过自己熟悉 React，面试官想通过这个问题来判断面试者是不是真的熟悉 React 🤣。</p>
<h2 data-id="heading-0">面试官的问法是否正确？</h2>
<p>面试官的问题是，<code>setState</code> 是一个宏认为还是微任务，那么在他的认知里，<code>setState</code> 肯定是一个异步操作。为了判断 <code>setState</code> 到底是不是异步操作，可以先做一个实验，通过 CRA 新建一个 React 项目，在项目中，编辑如下代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> logo <span class="hljs-keyword">from</span> <span class="hljs-string">'./logo.svg'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./App.css'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">1000</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span>
          <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;logo&#125;</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"logo"</span>
          <span class="hljs-attr">className</span>=<span class="hljs-string">"App-logo"</span>
          <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>
        /></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我的关注人数：&#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面大概长这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c6e13cc89b941b7bc32c60d420f50f8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的 React Logo 绑定了一个点击事件，现在需要实现这个点击事件，在点击 Logo 之后，进行一次 <code>setState</code> 操作，在 set 操作完成时打印一个 log，并且在 set 操作之前，分别添加一个宏任务和微任务。代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">handleClick = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> fans = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">10</span>)
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'宏任务触发'</span>)
  &#125;)
  <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'微任务触发'</span>)
  &#125;)
  <span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + fans
  &#125;, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'新增粉丝数:'</span>, fans)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01f7fff9a8904213a2506d792f54ac7b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>很明显，在点击 Logo 之后，先完成了 <code>setState</code> 操作，然后再是微任务的触发和宏任务的触发。所以，<code>setState</code> 的执行时机是早于微任务与宏任务的，即使这样也只能说它的执行时机早于 <code>Promise.then</code>，还不能证明它就是同步任务。</p>
<pre><code class="hljs language-js copyable" lang="js">handleClick = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> fans = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">10</span>)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开始运行'</span>)
  <span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + fans
  &#125;, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'新增粉丝数:'</span>, fans)
  &#125;)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'结束运行'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76db591194f4c9893fa1e8cef9f4c71~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这么看，似乎 <code>setState</code> 又是一个异步的操作。主要原因是，在 React 的生命周期以及绑定的事件流中，所有的 <code>setState</code> 操作会先缓存到一个队列中，在整个事件结束后或者 mount 流程结束后，才会取出之前缓存的 <code>setState</code> 队列进行一次计算，触发 state 更新。只要我们跳出 React 的事件流或者生命周期，就能打破 React 对 <code>setState</code> 的掌控。最简单的方法，就是把 <code>setState</code> 放到 <code>setTimeout</code> 的匿名函数中。</p>
<pre><code class="hljs language-js copyable" lang="js">handleClick = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> fans = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">10</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开始运行'</span>)
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + fans
    &#125;, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'新增粉丝数:'</span>, fans)
    &#125;)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'结束运行'</span>)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ece7008134c04142bb1b37bbf3c57957~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，<code>setState</code> 就是一次同步行为，根本不存在面试官的问题。</p>
<h2 data-id="heading-1">React 是如何控制 setState 的 ？</h2>
<p>前面的案例中，<code>setState</code> 只有在 <code>setTimeout</code> 中才会变得像一个同步方法，这是怎么做到的？</p>
<pre><code class="hljs language-js copyable" lang="js">handleClick = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 正常的操作</span>
  <span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
  &#125;)
&#125;
handleClick = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 脱离 React 控制的操作</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + fans
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先回顾之前的代码，在这两个操作中，我们分别在 Performance 中记录一次调用栈，看看两者的调用栈有何区别。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26e6071c677f4fc0b56266989b216dde~tplv-k3u1fbpfcp-zoom-1.image" alt="正常操作" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3793c95ca8b9427fa5cac25cc2283a86~tplv-k3u1fbpfcp-zoom-1.image" alt="脱离 React 控制的操作" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在调用栈中，可以看到 <code>Component.setState</code> 方法最终会调用<code>enqueueSetState</code> 方法 ，而 <code>enqueueSetState</code> 方法内部会调用 <code>scheduleUpdateOnFiber</code> 方法，区别就在于正常调用的时候，<code>scheduleUpdateOnFiber</code> 方法内只会调用 <code>ensureRootIsScheduled</code> ，在事件方法结束后，才会调用 <code>flushSyncCallbackQueue</code> 方法​。而脱离 React 事件流的时候，<code>scheduleUpdateOnFiber</code> 在 <code>ensureRootIsScheduled</code> 调用结束后，会直接调用 <code>flushSyncCallbackQueue</code> 方法，这个方法就是用来更新 state 并重新进行 render。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913270bb8a534b198093f2e233e49877~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a20c12caf35b4dcdac2e37aaa472afbc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">scheduleUpdateOnFiber</span>(<span class="hljs-params">fiber, lane, eventTime</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (lane === SyncLane) &#123;
    <span class="hljs-comment">// 同步操作</span>
    ensureRootIsScheduled(root, eventTime);
    <span class="hljs-comment">// 判断当前是否还在 React 事件流中</span>
    <span class="hljs-comment">// 如果不在，直接调用 flushSyncCallbackQueue 更新</span>
    <span class="hljs-keyword">if</span> (executionContext === NoContext) &#123;
      flushSyncCallbackQueue();
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 异步操作</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码可以简单描述这个过程，主要是判断了 <code>executionContext</code> 是否等于 <code>NoContext</code> 来确定当前更新流程是否在 React 事件流中。</p>
<p>众所周知，React 在绑定事件时，会对事件进行合成，统一绑定到 <code>document</code> 上（ <code>react@17</code> 有所改变，变成了绑定事件到 <code>render</code> 时指定的那个 DOM 元素），最后由 React 来派发。</p>
<p>所有的事件在触发的时候，都会先调用 <code>batchedEventUpdates$1</code> 这个方法，在这里就会修改 <code>executionContext</code> 的值，React 就知道此时的 <code>setState</code> 在自己的掌控中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// executionContext 的默认状态</span>
<span class="hljs-keyword">var</span> executionContext = NoContext;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">batchedEventUpdates$1</span>(<span class="hljs-params">fn, a</span>) </span>&#123;
  <span class="hljs-keyword">var</span> prevExecutionContext = executionContext;
  executionContext |= EventContext; <span class="hljs-comment">// 修改状态</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">return</span> fn(a);
  &#125; <span class="hljs-keyword">finally</span> &#123;
    executionContext = prevExecutionContext;
<span class="hljs-comment">// 调用结束后，调用 flushSyncCallbackQueue</span>
    <span class="hljs-keyword">if</span> (executionContext === NoContext) &#123;
      flushSyncCallbackQueue();
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c47d13632db746aea8d7216f3b99929f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，不管是直接调用 <code>flushSyncCallbackQueue</code> ，还是推迟调用，这里本质上都是同步的，只是有个先后顺序的问题。</p>
<h2 data-id="heading-2">未来会有异步的 setState</h2>
<p>如果你有认真看上面的代码，你会发现在 <code>scheduleUpdateOnFiber</code> 方法内，会判断 <code>lane</code> 是否为同步，那么是不是存在异步的情况？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">scheduleUpdateOnFiber</span>(<span class="hljs-params">fiber, lane, eventTime</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (lane === SyncLane) &#123;
    <span class="hljs-comment">// 同步操作</span>
    ensureRootIsScheduled(root, eventTime);
    <span class="hljs-comment">// 判断当前是否还在 React 事件流中</span>
    <span class="hljs-comment">// 如果不在，直接调用 flushSyncCallbackQueue 更新</span>
    <span class="hljs-keyword">if</span> (executionContext === NoContext) &#123;
      flushSyncCallbackQueue();
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 异步操作</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React 在两年前，升级 fiber 架构的时候，就是为其异步化做准备的。在 React 18 将会正式发布 <code>Concurrent</code> 模式，关于 <code>Concurrent</code> 模式，官方的介绍如下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7617b796d43b461b92cb0ca276cc3be0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>什么是 Concurrent 模式？</strong></p>
<p>Concurrent 模式是一组 React 的新功能，可帮助应用保持响应，并根据用户的设备性能和网速进行适当的调整。在 Concurrent 模式中，渲染不是阻塞的。它是可中断的。这改善了用户体验。它同时解锁了以前不可能的新功能。</p>
</blockquote>
<p>现在如果想使用 <code>Concurrent</code> 模式，需要使用 React 的实验版本。如果你对这部分内容感兴趣可以阅读我之前的文章：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.shenfq.com%2Fposts%2F2020%2FReact%2520%25E6%259E%25B6%25E6%259E%2584%25E7%259A%2584%25E6%25BC%2594%25E5%258F%2598%2520-%2520%25E4%25BB%258E%25E5%2590%258C%25E6%25AD%25A5%25E5%2588%25B0%25E5%25BC%2582%25E6%25AD%25A5.html" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.shenfq.com/posts/2020/React%20%E6%9E%B6%E6%9E%84%E7%9A%84%E6%BC%94%E5%8F%98%20-%20%E4%BB%8E%E5%90%8C%E6%AD%A5%E5%88%B0%E5%BC%82%E6%AD%A5.html" ref="nofollow noopener noreferrer">《React 架构的演变 - 从同步到异步》</a>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd3d0ef658734f2e9cf5c5c3f85400c6~tplv-k3u1fbpfcp-watermark.image" alt="公众号推广.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            