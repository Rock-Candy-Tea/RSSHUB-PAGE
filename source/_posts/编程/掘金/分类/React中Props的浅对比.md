
---
title: 'React中Props的浅对比'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3081'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 23:17:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=3081'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上一周去面试的时候，面试官我<code>PureComponent</code>里是如何对比<code>props</code>的，概念已经牢记脑中，脱口而出就是浅对比，接着面试官问我是如何浅对比的，结果我就没回答上来。</p>
<p>趁着周末，再来看看源码里是如何实现的。</p>
<h2 data-id="heading-0">类组件的Props对比</h2>
<p>类组件是否需要更新需要实现<code>shouldComponentUpdate</code>方法，通常讲的是如果继承的是<code>PureComponent</code>则会有一个默认浅对比的实现。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ReactBaseClasses.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ComponentDummy</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
ComponentDummy.prototype = Component.prototype;

<span class="hljs-comment">/**
 * Convenience component with default shallow equality check for sCU.
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">PureComponent</span>(<span class="hljs-params">props, context, updater</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.props = props;
  <span class="hljs-built_in">this</span>.context = context;
  <span class="hljs-comment">// If a component has string refs, we will assign a different object later.</span>
  <span class="hljs-built_in">this</span>.refs = emptyObject;
  <span class="hljs-built_in">this</span>.updater = updater || ReactNoopUpdateQueue;
&#125;

<span class="hljs-keyword">const</span> pureComponentPrototype = (PureComponent.prototype = <span class="hljs-keyword">new</span> ComponentDummy());
pureComponentPrototype.constructor = PureComponent;
<span class="hljs-comment">// Avoid an extra prototype jump for these methods.</span>
<span class="hljs-built_in">Object</span>.assign(pureComponentPrototype, Component.prototype);
pureComponentPrototype.isPureReactComponent = <span class="hljs-literal">true</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>PureComponent</code>的实现如上，我以前以为在声明时默认会实现<code>shouldComponentUpdate</code>方法，但实际上并没有一个默认的方法。</p>
<p>接下来看看<code>shouldComponentUpdate</code>方法的调用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ReactFiberClassComponent.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkShouldComponentUpdate</span>(<span class="hljs-params">
  workInProgress,
  ctor,
  oldProps,
  newProps,
  oldState,
  newState,
  nextContext,
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> instance = workInProgress.stateNode;
  <span class="hljs-comment">// 如果实利实现了shouldComponentUpdate则返回调用它的结果</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> instance.shouldComponentUpdate === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">const</span> shouldUpdate = instance.shouldComponentUpdate(
      newProps,
      newState,
      nextContext,
    );
    <span class="hljs-keyword">return</span> shouldUpdate;
  &#125;

  <span class="hljs-comment">// PureReactComponent的时候进行浅对比</span>
  <span class="hljs-keyword">if</span> (ctor.prototype && ctor.prototype.isPureReactComponent) &#123;
    <span class="hljs-keyword">return</span> (
      !shallowEqual(oldProps, newProps) || !shallowEqual(oldState, newState)
    );
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出实际上并没有单独写一个<code>shouldComponentUpdate</code>方法给<code>PureReactComponent</code>，而是在对比的时候就返回浅对比的结果。</p>
<p>浅对比的答案都在<code>shallowEqual</code>方法里了。</p>
<h2 data-id="heading-1">shallowEqual 浅对比</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// shallowEqual.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowEqual</span>(<span class="hljs-params">objA: mixed, objB: mixed</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-comment">// 一样的对象返回true</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.is(objA, objB)) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;

  <span class="hljs-comment">// 不是对象或者为null返回false</span>
  <span class="hljs-keyword">if</span> (
    <span class="hljs-keyword">typeof</span> objA !== <span class="hljs-string">'object'</span> ||
    objA === <span class="hljs-literal">null</span> ||
    <span class="hljs-keyword">typeof</span> objB !== <span class="hljs-string">'object'</span> ||
    objB === <span class="hljs-literal">null</span>
  ) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;

  <span class="hljs-keyword">const</span> keysA = <span class="hljs-built_in">Object</span>.keys(objA);
  <span class="hljs-keyword">const</span> keysB = <span class="hljs-built_in">Object</span>.keys(objB);

  <span class="hljs-comment">// key数量不同返回false</span>
  <span class="hljs-keyword">if</span> (keysA.length !== keysB.length) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;

  <span class="hljs-comment">// 对应key的值不相同返回false</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < keysA.length; i++) &#123;
    <span class="hljs-keyword">if</span> (
      !hasOwnProperty.call(objB, keysA[i]) ||
      !<span class="hljs-built_in">Object</span>.is(objA[keysA[i]], objB[keysA[i]])
    ) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>shallowEqual</code>方法原理很简单了</p>
<ol>
<li>先判断两者是否为同一对象。</li>
<li>判断两者的值是否不为<code>object</code>或为<code>null。</code></li>
<li>对比两者<code>key</code>的长度。</li>
<li>判断两者<code>key</code>对应的值是否相同。</li>
</ol>
<p>原来原理是这样简单的对比，如果我面试的时候能够口喷源码，会不会工资更高一些呢？</p>
<h2 data-id="heading-2">函数组件的浅对比</h2>
<p>函数组件的浅对比方式则使用<code>React.memo</code>方法实现。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ReactMemo.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">memo</span><<span class="hljs-title">Props</span>>(<span class="hljs-params">
  type: React$ElementType,
  compare?: (oldProps: Props, newProps: Props) => boolean,
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> elementType = &#123;
    <span class="hljs-attr">$$typeof</span>: REACT_MEMO_TYPE,
    type,
    <span class="hljs-attr">compare</span>: compare === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">null</span> : compare,
  &#125;;
  <span class="hljs-keyword">return</span> elementType;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>React.memo</code>方法同样支持传入<code>compare</code>函数最为第二个参数。</p>
<p>内部的处理其实是手动创建了一个<code>$$typeof</code>为<code>REACT_MEMO_TYPE</code>的<code>ReactElement</code>，方便之后的类型判断。</p>
<p><code>React.memo</code>组件的创建会稍微复杂一些，由于可以传入第二个自定义的<code>compare</code>函数，所以在内部其实会被定义为2种类型的Fiber节点。</p>
<ul>
<li>没有传入<code>compare</code>函数的为<code>SimpleMemoComponent</code>。</li>
<li>传入了自定义<code>compare</code>函数的为<code>MemoComponent</code>。</li>
</ul>
<p>但是实际对于<code>Props</code>的比较都是相同的，默认都是调用<code>shallowEqual</code>方法来对比。</p>
<p><strong>updateSimpleMemoComponent</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (
  shallowEqual(prevProps, nextProps) &&
  current.ref === workInProgress.ref
) &#123;
<span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>updateMemoComponent</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">let</span> compare = Component.compare;
compare = compare !== <span class="hljs-literal">null</span> ? compare : shallowEqual;
<span class="hljs-keyword">if</span> (compare(prevProps, nextProps) && current.ref === workInProgress.ref) &#123;
  <span class="hljs-keyword">return</span> bailoutOnAlreadyFinishedWork(current, workInProgress, renderLanes);
&#125;
<span class="hljs-comment">// ... </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至于为什么要分为2个组件，我也没大看懂，蓝廋香菇，大概是和更新调度相关的。</p>
<p><code>SimpleMemoComponent</code>的Fiber节点实际等于改了个名的函数组件，走流程会直接走到函数组件里，而<code>MemoComponent</code>则是套了一层壳，需要先把壳剥开生成子Fiber节点，再由子Fiber节点的判断走到函数组件里。</p>
<hr>
<p>以上就是<code>Props</code>浅对比的分析了～</p></div>  
</div>
            