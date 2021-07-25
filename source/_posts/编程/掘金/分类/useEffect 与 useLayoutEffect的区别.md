
---
title: 'useEffect 与 useLayoutEffect的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1500'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 04:39:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=1500'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前置知识</h2>
<p>我们可以将 <code>React</code> 的工作流程划分为几大块：</p>
<ol>
<li><code>render</code> 阶段：主要生成 <code>Fiber节点</code>  并构建出完整的 <code>Fiber树</code></li>
<li><code>commit</code> 阶段：在上一个<code>render</code> 阶段中会在 <code>rootFiber</code> 上生成一条副作用链表，应用的<code>DOM操作</code>就会在本阶段执行</li>
</ol>
<p><code>commit</code>阶段的工作主要分为三部分，对应到源码中的函数名是：</p>
<ul>
<li><code>commitBeforeMutationEffects</code>阶段：主要处理执行DOM操作前的一些相关操作</li>
<li><code>commitMutationEffects</code>阶段：执行<code>DOM操作</code></li>
<li><code>commitLayoutEffects</code>阶段：主要处理执行DOM操作后的一些相关操作</li>
</ul>
<p><code>useEffect</code> 和 <code>useLayoutEffect</code> 的区别主要就在体现在这三个阶段的处理上。结论是：<code>useEffect</code> 会异步地去执行它的响应函数和上一次的销毁函数，而<code>useLayoutEffect</code> 会同步地执行它的响应函数和上一次的销毁函数，即会阻塞住 <code>DOM渲染</code>。</p>
<h2 data-id="heading-1">useEffect</h2>
<h3 data-id="heading-2">commitBeforeMutationEffects</h3>
<p>在这个阶段中 <code>useEffect</code> 着重会经历一句话如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitBeforeMutationEffects</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">while</span> (nextEffect$<span class="hljs-number">1</span> !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">// 一系列的赋值操作省略，这里的flags应取自对应FunctionComponent的effect的flags，具体实现请看源码</span>
    <span class="hljs-keyword">var</span> flags = effect.flags;

<span class="hljs-comment">// 处理生命周期</span>
    <span class="hljs-keyword">if</span> ((flags & Snapshot) !== NoFlags) &#123;
      setCurrentFiber(nextEffect$<span class="hljs-number">1</span>);
      commitBeforeMutationLifeCycles(current, nextEffect$<span class="hljs-number">1</span>);
      resetCurrentFiber();
    &#125;

<span class="hljs-comment">// 这个if判断只有 useEffect 为 true，useLayoutEffect 为false</span>
    <span class="hljs-keyword">if</span> ((flags & Passive) !== NoFlags) &#123;
      <span class="hljs-comment">// If there are passive effects, schedule a callback to flush at</span>
      <span class="hljs-comment">// the earliest opportunity.</span>
      <span class="hljs-keyword">if</span> (!rootDoesHavePassiveEffects) &#123;
        rootDoesHavePassiveEffects = <span class="hljs-literal">true</span>;
<span class="hljs-comment">// 这里就是 useEffect 异步的原因，DOM操作后React会调度 flushPassiveEffects</span>
        scheduleCallback(NormalPriority, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
          flushPassiveEffects();
          <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        &#125;);
      &#125;
    &#125;

    nextEffect$<span class="hljs-number">1</span> = nextEffect$<span class="hljs-number">1.</span>nextEffect;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">commitMutationEffects</h3>
<p>在这个阶段中，<code>React</code> 会进行一系列的<code>DOM节点更新</code> ，然后会执行一个方法: <code>commitHookEffectListUnmount(HookLayout | HookHasEffect, finishedWork);</code></p>
<p>那么一个拥有 <code>useEffect</code> 的 <code>Functional Component</code> 在这个阶段是不符合 <code>unmount</code> 的判断逻辑的，所以在这个地方不会做 <code>unmount</code> 操作。</p>
<h3 data-id="heading-4">commitLayoutEffects</h3>
<p>在这个阶段中，依然有一个很重要的方法存在：<code>commitHookEffectListMount(HookLayout | HookHasEffect, finishedWork);</code></p>
<p>这个if判断和上一阶段的if判断是一样的，<code>useEffec</code> 在这个判断中不会做任何操作。</p>
<h3 data-id="heading-5">后续阶段</h3>
<p>在完成了 <code>commitLayoutEffects</code> 后，还有一个操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (rootDoesHavePassiveEffects) &#123;
    <span class="hljs-comment">// This commit has passive effects. Stash a reference to them. But don't</span>
    <span class="hljs-comment">// schedule a callback until after flushing layout work.</span>
    rootDoesHavePassiveEffects = <span class="hljs-literal">false</span>;
    rootWithPendingPassiveEffects = root;
    pendingPassiveEffectsLanes = lanes;
    pendingPassiveEffectsRenderPriority = renderPriorityLevel;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即把 <code>rootWithPendingPassiveEffects</code> 置为 <code>root</code> ，这么做的原因和第一阶段 <code>commitBeforeMutationEffects</code> 中 <code>useEffect</code> 注册的下一次 <code>flushPassiveEffects</code> 异步调度有关，我们看以下 <code>flushPassiveEffects</code> 的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flushPassiveEffectsImpl</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">if</span> (rootWithPendingPassiveEffects === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
<span class="hljs-comment">// 省略一系列的性能追踪等操作</span>
commitPassiveUnmountEffects(root.current);
  commitPassiveMountEffects(root, root.current);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述代码段可以看见，<code>useEffect</code> 在第一阶段注册的调度回调会在页面更新后进行 <code>unmount</code> 和 <code>mount</code> 操作。值得一提的是，这个回调中effect的注册时机就是在<code> commitLayoutEffects</code> 阶段。</p>
<h2 data-id="heading-6">useLayoutEffect</h2>
<p>其实根据我们对 <code>useEffect</code> 的解析来看，就是在 <code>commitMutationEffects</code> 和 <code>commitLayoutEffects</code> 阶段中各自的 if 判断中，<code>useLayoutEffect</code> 是通过if判断的，所以在 <code>commitMutationEffects</code> 阶段中，同步执行了<code>useLayoutEffect</code> 的上一次销毁函数，在 <code>commitLayoutEffects</code> 阶段中，同步执行了 <code>useLayoutEffect</code> 本次的执行函数，并注册上销毁函数。</p>
<h2 data-id="heading-7">结论</h2>
<p>至此，我们粗略地查看了 <code>commit</code> 阶段的代码，分析了以下为什么 <code>useEffect</code> 是异步执行，而 <code>useLayoutEffect</code> 是同步执行，具体的代码我没有太过在文章中贴出来，因为这些都是可变的，真正的流程性的概览和 <code>React</code> 团队设计这一套机制的心智模型需要我们自己在不断调试代码和理解中慢慢去熟悉。</p>
<p>后续自己感兴趣的是 <code>hooks</code> 的实现，其中比较关键的 <code>useReducer</code> 会着重看一下源码，看看能不能写个简易版本的放到支付宝小程序中去实现一个 <code>自定义的支付宝hooks</code> 用于日常生产力开发。</p></div>  
</div>
            