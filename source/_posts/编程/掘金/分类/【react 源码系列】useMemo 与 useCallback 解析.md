
---
title: '【react 源码系列】useMemo 与 useCallback 解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9841'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 20:17:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=9841'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>作为 React 的使用者，在尝试对现有代码进行优化的时候，我们可能会尝试使用 <code>useMemo</code> 以及 <code>useCallback</code> 来进行优化，对<code>数据</code>或者<code>函数</code>进行缓存，在下次组件更新时，如果对应的<code>依赖</code>没有变化，就可以无须重新计算而拿到<code>缓存值</code>。</p>
<p>接下来，我会从 <code>使用</code> 以及 <code>原理</code> 两个角度来解析 <code>useMemo</code> 以及 <code>useCallback</code></p>
<h2 data-id="heading-1">使用 useMemo、useCallback</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> React, &#123; useState, useMemo, useCallback &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)
  <span class="hljs-keyword">const</span> [isChanged, setIsChanged] = useState(<span class="hljs-literal">false</span>)
  
  <span class="hljs-comment">// // useCallback 接收两个参数，一个是依赖发生变化时需要被执行的函数, 一个是依赖项</span>
  <span class="hljs-keyword">const</span> calDoubleCount = useCallback(<span class="hljs-function">() =></span> &#123;
    setCount(<span class="hljs-function"><span class="hljs-params">count</span> =></span> count + <span class="hljs-number">1</span>)
  &#125;, [])

  <span class="hljs-comment">// useMemo 接收两个参数，一个是依赖发生变化时需要被执行的函数, 一个是依赖项</span>
  <span class="hljs-keyword">const</span> doubleCount = useMemo(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> count * <span class="hljs-number">2</span>
  &#125;, [count])
  
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setIsChanged(isChanged => !isChanged)&#125;>change me<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count => count + 1)&#125;>&#123;doubleCount&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;calDoubleCount&#125;</span>></span>click me<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这段代码描述了 <code>useMemo</code> 在实际开发中是如何使用的，我们通过点击第二个 <code>p</code> 标签改变 <code>count</code> 值，而 <code>doubleCount</code> 的依赖中存在 <code>count</code>, 所以当 <code>count</code> 变化时， <code>doubleCount</code> 会重新计算并且返回最新的值。</p>
<p>当点击第一个 <code>p</code> 标签时，因为并没有引起 <code>count</code> 的变化，所以 <code>doubleCount</code> 会使用上一次计算的值，而不是重新计算</p>
<h2 data-id="heading-2">useMemo 源码剖析</h2>
<p>在讲 <code>useMemo</code> 源码之前，有个前提是我们需要先了解清楚的，就是每次 <code>hook</code> 的执行我们可以分成两部分来看</p>
<ol>
<li>mount</li>
<li>update</li>
</ol>
<p>当第一次挂载组件时，走的是 <code>mount</code>, 之后的每一次组件渲染，走的都是 <code>update</code>。我们来看一段 <code>hook</code> 相关的源码。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// mount</span>
<span class="hljs-keyword">const</span> HooksDispatcherOnMount: Dispatcher = &#123;
  <span class="hljs-attr">useCallback</span>: mountCallback,
  <span class="hljs-attr">useMemo</span>: mountMemo,
  <span class="hljs-comment">// 省略其他 hook</span>
&#125;;

<span class="hljs-comment">// update</span>
<span class="hljs-keyword">const</span> HooksDispatcherOnUpdate: Dispatcher = &#123;
  <span class="hljs-attr">useCallback</span>: updateCallback,
  <span class="hljs-attr">useMemo</span>: updateMemo,
  <span class="hljs-comment">// 省略其他 hook</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从源码我们可以知道，<code>hook</code> 在首次执行时，执行的是 <code>HooksDispatcherOnMount</code>,在更新时，执行的是<code>HooksDispatcherOnUpdate</code>。了解了这个前提后，我们再看下面这段代码。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// mount</span>
HooksDispatcherOnMountInDEV = &#123;
  useMemo<T>(create: <span class="hljs-function">() =></span> T, <span class="hljs-attr">deps</span>: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-built_in">void</span> | <span class="hljs-literal">null</span>): T &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">return</span> mountMemo(create, deps);
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-comment">// 省略</span>
    &#125;
  &#125;
&#125;
<span class="hljs-comment">// update</span>
HooksDispatcherOnUpdateInDEV = &#123;
  useMemo<T>(create: <span class="hljs-function">() =></span> T, <span class="hljs-attr">deps</span>: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-built_in">void</span> | <span class="hljs-literal">null</span>): T &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">return</span> updateMemo(create, deps);
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-comment">// 省略</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说，<code>第一次</code> 挂载组件时调用的 <code>useMemo</code> ，实际上调用的是 <code>mountMemo</code>。之后的每次执行，调用的都是 <code>updateMemo</code>。</p>
<h2 data-id="heading-3">mountMemo</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountMemo</span><<span class="hljs-title">T</span>>(<span class="hljs-params">
  nextCreate: () => T,                                <span class="hljs-comment">// 依赖变化时需要执行的函数</span>
  deps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-built_in">void</span> | <span class="hljs-literal">null</span>,                   <span class="hljs-comment">// 依赖</span>
</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-keyword">const</span> hook = mountWorkInProgressHook();
  <span class="hljs-keyword">const</span> nextDeps = deps === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">null</span> : deps;
  <span class="hljs-keyword">const</span> nextValue = nextCreate();
  hook.memoizedState = [nextValue, nextDeps];
  <span class="hljs-keyword">return</span> nextValue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>nextCreate</code> 实际上就是我们传入 <code>useMemo</code> 的第一个参数，是一个回调函数，当依赖更新时，该回调函数会被执行，<code>dep</code> 就是我们传入的第二个参数，是一个依赖数组。</p>
<p>可以看到，对于<code>第一次</code>挂载组件，<code>useMemo</code> 会直接执行 <code>nextCreat</code>,返回计算后的值。
而 <code>hook.memoizedState</code> 保存的是 <code>计算后的值</code> 以及对应的 <code>依赖</code>,目的是下次执行 <code>useMemo</code> 时，通过判断 <code>依赖</code> 是否变化来决定是返回重新计算的值，还是上一次计算的结果。</p>
<h2 data-id="heading-4">updateMemo</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateMemo</span><<span class="hljs-title">T</span>>(<span class="hljs-params">
  nextCreate: () => T,
  deps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-built_in">void</span> | <span class="hljs-literal">null</span>,
</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-keyword">const</span> hook = updateWorkInProgressHook();
  <span class="hljs-keyword">const</span> nextDeps = deps === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">null</span> : deps;
  <span class="hljs-comment">// hook.memoizedState 就是 [value, deps]</span>
  <span class="hljs-keyword">const</span> prevState = hook.memoizedState;
  <span class="hljs-keyword">if</span> (prevState !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">// 如果依赖不为空</span>
    <span class="hljs-keyword">if</span> (nextDeps !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-comment">// 上一次更新后的依赖</span>
      <span class="hljs-keyword">const</span> prevDeps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-literal">null</span> = prevState[<span class="hljs-number">1</span>];
      <span class="hljs-comment">// 比较当前与上一次的依赖</span>
      <span class="hljs-keyword">if</span> (areHookInputsEqual(nextDeps, prevDeps)) &#123;
        <span class="hljs-comment">// 如果两者依赖相等，直接返回上一次计算的结果</span>
        <span class="hljs-keyword">return</span> prevState[<span class="hljs-number">0</span>];
      &#125;
    &#125;
  &#125;
  <span class="hljs-comment">// 否则重新计算依赖值</span>
  <span class="hljs-keyword">const</span> nextValue = nextCreate();
  <span class="hljs-comment">// 将重新计算过后的值以及依赖赋值给 hook.memoizedState</span>
  hook.memoizedState = [nextValue, nextDeps];
  <span class="hljs-keyword">return</span> nextValue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">useCallback</h2>
<p>上面我们了解了 <code>useMemo</code> 的原理，那么 <code>useCallback</code> 也就很简单了。</p>
<p><code>useCallback</code> 跟 <code>useMemo</code>，几乎一模一样，唯一的区别在于 <code>useMemo</code> 返回的是<code>函数计算的值</code>， 而 <code>useCallback</code> 返回的是<code>函数本身</code></p>
<h2 data-id="heading-6">mountCallback</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountCallback</span><<span class="hljs-title">T</span>>(<span class="hljs-params">callback: T, deps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-built_in">void</span> | <span class="hljs-literal">null</span></span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-keyword">const</span> hook = mountWorkInProgressHook();
  <span class="hljs-keyword">const</span> nextDeps = deps === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">null</span> : deps;
  hook.memoizedState = [callback, nextDeps];
  <span class="hljs-comment">// 直接返回函数本身</span>
  <span class="hljs-keyword">return</span> callback;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">updateCallback</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateCallback</span><<span class="hljs-title">T</span>>(<span class="hljs-params">callback: T, deps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-built_in">void</span> | <span class="hljs-literal">null</span></span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-keyword">const</span> hook = updateWorkInProgressHook();
  <span class="hljs-keyword">const</span> nextDeps = deps === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">null</span> : deps;
  <span class="hljs-keyword">const</span> prevState = hook.memoizedState; <span class="hljs-comment">// [callback, deps]</span>
  <span class="hljs-keyword">if</span> (prevState !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">// 是否有依赖</span>
    <span class="hljs-keyword">if</span> (nextDeps !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">const</span> prevDeps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-literal">null</span> = prevState[<span class="hljs-number">1</span>];
      <span class="hljs-comment">// 对比当前依赖跟上一次计算后的依赖</span>
      <span class="hljs-keyword">if</span> (areHookInputsEqual(nextDeps, prevDeps)) &#123;
        <span class="hljs-comment">// 依赖如果一样这直接返回上次的缓存值</span>
        <span class="hljs-keyword">return</span> prevState[<span class="hljs-number">0</span>];
      &#125;
    &#125;
  &#125;
  hook.memoizedState = [callback, nextDeps];
  <span class="hljs-comment">// 直接返回函数本身</span>
  <span class="hljs-keyword">return</span> callback;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上对比我们可以知道 <code>updateCallback</code> 跟 <code>updateMemo</code> 的唯一区别就在于 <code>updateMemo</code> 在内部执行了回调函数，并将返回值返回。而<code>useCallback</code>则是直接把函数返回了，并没有计算。</p>
<h2 data-id="heading-8">总结</h2>
<p>通过上面对 <code>useMemo</code> 以及 <code>useCallback</code> 的解析，我们了解到两者的区别其实很简单。改写的都写在上面了，但这里我最后想说一下。虽然 <code>useMemo</code> 跟 <code>useCallback</code> 都可以对数据进行缓存，但是也不能因此而滥用，我们应该考虑的是哪些数据值得去缓存，因为对于 <code>useMemo</code> 和 <code>useCallback</code> 来说，除了计算值耗时以外，对比依赖的变化也是需要时间的，我们应该对此进行衡量，才能够更好的去使用 <code>hook</code>，而不是为了优化而优化。</p></div>  
</div>
            