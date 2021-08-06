
---
title: 'React ref 从原理到应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37a12cb9a5eb40a489d726fd5227c1e9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 21:32:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37a12cb9a5eb40a489d726fd5227c1e9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>提到 <code>ref</code>或者 <code>refs</code> 如果你用过React 16以前的版本，第一印象都是用来访问DOM或者修改组件实例的,正如官网所介绍的这样:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37a12cb9a5eb40a489d726fd5227c1e9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后到了React 16.3出现的 <code>createRef</code> 以及16.8 hooks中的 <code>useRef</code> 出现时，发现这里的ref好像不仅仅只有之前的绑定到DOM/组件实例的作用？本文将尝试分析相关源码，带你彻底搞清React ref。</p>
<h2 data-id="heading-1">前置知识</h2>
<p>为了方便本文理解先在这里简单提及几个知识点。</p>
<h3 data-id="heading-2">Fiber架构</h3>
<p>Fiber是React更新时的最小单元,是一种包含指针的数据结构,从数据结构上看Fiber架构 ≈ 树 + 链表。
Fiber单元是从 jsx createElement之后根据ReactElement生成的，相比 ReactElement，Fiber单元具备动态工作能力。</p>
<h3 data-id="heading-3">React 的工作流程</h3>
<p>使用chrome perfomance录制一个react应用渲染看函数调用栈会看到下面这张图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c035a2cbbd94ad1810ac66660bb6f94~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这三块内容分别代表:</p>
<ol>
<li>生成react root节点</li>
<li>reconciler 协调生成需要更新的子节点</li>
<li>将节点更新 <strong>commit</strong> 到视图(commit阶段)</li>
</ol>
<h3 data-id="heading-4">Hooks基础知识</h3>
<p>在函数组件中每执行一次use开头的hook函数都会生成一个hook对象。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Hook = &#123;
  <span class="hljs-attr">memoizedState</span>: <span class="hljs-built_in">any</span>,   <span class="hljs-comment">// 上次更新之后的最终状态值</span>
  <span class="hljs-attr">queue</span>: UpdateQueue, <span class="hljs-comment">//更新队列</span>
  next, <span class="hljs-comment">// 下一个 hook 对象</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中memoizedState会保存该hook上次更新之后的最终状态,比如当我们使用一次<code>useState</code>之后就会在memoizedState中保存初始值。</p>
<p>React 中大部分 hook 分为两个阶段： 第一次初始化时<code>mount</code>阶段和更新<code>update</code>时阶段</p>
<p>hooks函数的执行分两个阶段 <code>mount</code>和 <code>update</code>,比如 <code>useState</code>只会在初始化时执行一次,下文中将提到的 <code>useImperativeHandle</code> 和 <code>useRef</code>也包括在内。</p>
<h3 data-id="heading-5">调试源码</h3>
<p>本文已梳理摘取了源码相关的函数,但你如果配合源码调试一起食用效果会更加。</p>
<p>本文基于React v17.0.2。</p>
<ol>
<li>拉取React代码并安装依赖</li>
<li>将react,scheduler以及react-dom打包为commonjs</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript">yarn build react/index,react-dom/index,scheduler --<span class="hljs-keyword">type</span> NODE
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>进入build/node_modules/react/cjs 执行yarn link 同理 react-dom</li>
<li>在 build/node_modules/react/cjs/react.development.js中加入link标记console以确保检查link状态</li>
<li>使用create-react-app创建一个测试应用 并link react，react-dom</li>
</ol>
<p><strong>下面开启正文</strong></p>
<h2 data-id="heading-6">ref prop</h2>
<p>组件上的ref属性是一个保留属性，你不能把ref当成一个普通的prop属性在一个组件中获取，比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;&#123;test:1&#125;&#125;</span>></span>
&#125;
const Child = (props) => &#123;
  console.log(props);
  // 这里获取不到ref属性
return <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这个ref去哪里了呢, React本身又对它做了什么呢?</p>
<p>我们知道React的解析是从createElement开始的，找到了下面创建ReactElement的地方，确实有对ref保留属性的处理。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, config, children</span>) </span>&#123;
<span class="hljs-keyword">let</span> propName;
  <span class="hljs-comment">// Reserved names are extracted</span>
  <span class="hljs-keyword">const</span> props = &#123;&#125;;
  <span class="hljs-keyword">let</span> ref = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">if</span> (config != <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">if</span> (hasValidRef(config)) &#123;
      ref = config.ref;
    &#125;
    <span class="hljs-keyword">for</span> (propName <span class="hljs-keyword">in</span> config) &#123;
      <span class="hljs-keyword">if</span> (
        hasOwnProperty.call(config, propName) &&
        !RESERVED_PROPS.hasOwnProperty(propName)
      ) &#123;
        props[propName] = config[propName];
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> ReactElement(
    type,
    key,
    ref,
    props,
    ...
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从createElement开始就已经创建了对ref属性的引用。</p>
<p>createElement之后我们需要构建Fiber工作树，接下来主要讲对ref相关的处理。</p>
<p>React对于不同的组件有不通的处理</p>
<p>先主要关注 FunctionComponent/ClassComponent/HostComponent(原生html标签)</p>
<p><strong>FunctionComponent</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateFunctionComponent</span>(<span class="hljs-params">current, workInProgress, Component, nextProps, renderLanes</span>) </span>&#123;
      <span class="hljs-keyword">try</span> &#123;
        nextChildren = renderWithHooks(current, workInProgress, Component, nextProps, context, renderLanes);
      &#125; <span class="hljs-keyword">finally</span> &#123;
        reenableLogs();
      &#125;
      reconcileChildren(current, workInProgress, nextChildren, renderLanes);
      <span class="hljs-keyword">return</span> workInProgress.child;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderWithHooks</span>(<span class="hljs-params">current, workInProgress, Component, props, secondArg, nextRenderLanes</span>)</span>&#123;
  children = Component(props, secondArg); <span class="hljs-comment">// 这里的Component就是指我们的函数组件</span>
<span class="hljs-keyword">return</span> children;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到函数组件在渲染的时候就是直接执行。</p>
<h3 data-id="heading-7">Class组件和原生标签的ref prop</h3>
<p><strong>ClassComponent</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateClassComponent</span>(<span class="hljs-params">current, workInProgress, Component, nextProps, renderLanes</span>) </span>&#123;
  ...
  &#123;
    ...
    constructClassInstance(workInProgress, Component, nextProps);
....
  &#125;
  <span class="hljs-keyword">var</span> nextUnitOfWork = finishClassComponent(current, workInProgress, Component, shouldUpdate, hasContext, renderLanes);
...
  <span class="hljs-keyword">return</span> nextUnitOfWork;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">constructClassInstance</span>(<span class="hljs-params">workInProgress, ctor, props</span>) </span>&#123;
....
  <span class="hljs-keyword">var</span> instance = <span class="hljs-keyword">new</span> ctor(props, context);
  <span class="hljs-comment">// 把instance实例挂载到workInProgress stateNode属性上</span>
  adoptClassInstance(workInProgress, instance);
.....
  <span class="hljs-keyword">return</span> instance;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">finishClassComponent</span>(<span class="hljs-params">current, workInProgress, Component, shouldUpdate, hasContext, renderLanes</span>) </span>&#123;
  <span class="hljs-comment">// 标记是否有ref更新</span>
  markRef(current, workInProgress);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">markRef</span>(<span class="hljs-params">current, workInProgress</span>) </span>&#123;
  <span class="hljs-keyword">var</span> ref = workInProgress.ref;

  <span class="hljs-keyword">if</span> (current === <span class="hljs-literal">null</span> && ref !== <span class="hljs-literal">null</span> || current !== <span class="hljs-literal">null</span> && current.ref !== ref) &#123;
    <span class="hljs-comment">// Schedule a Ref effect</span>
    workInProgress.flags |= Ref;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ClassComponent则是通过构造函数生成实例并标记了ref属性。</p>
<p>回顾一下之前提到的React工作流程，既然是要将组件实例或者真实DOM赋值给ref那肯定不能在一开始就处理这个ref，而是根据标记到commit阶段再给ref赋值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitLayoutEffectOnFiber</span>(<span class="hljs-params">finishedRoot, current, finishedWork, committedLanes</span>) </span>&#123;
....
  &#123;
    <span class="hljs-keyword">if</span> (finishedWork.flags & Ref) &#123;
      commitAttachRef(finishedWork);
    &#125;
  &#125;
  ....
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitAttachRef</span>(<span class="hljs-params">finishedWork</span>) </span>&#123;
  <span class="hljs-keyword">var</span> ref = finishedWork.ref;
  <span class="hljs-keyword">if</span> (ref !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">var</span> instance = finishedWork.stateNode;
    <span class="hljs-keyword">var</span> instanceToUse;
    <span class="hljs-keyword">switch</span> (finishedWork.tag) &#123;
      <span class="hljs-keyword">case</span> HostComponent:
        <span class="hljs-comment">// getPublicInstance 这里调用了DOM API 返回了DOM对象</span>
        instanceToUse = getPublicInstance(instance);
        <span class="hljs-keyword">break</span>;

      <span class="hljs-keyword">default</span>:
        instanceToUse = instance;
    &#125; 
    <span class="hljs-comment">// 对函数回调形式设置ref的处理</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> ref === <span class="hljs-string">'function'</span>) &#123;
      &#123;
        ref(instanceToUse);
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      ref.current = instanceToUse;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在commit阶段，如果是原生标签则将真实DOM赋值给ref对象的current属性, 如果是class componnet 则是组件instance。</p>
<h3 data-id="heading-8">函数组件的ref prop</h3>
<p>如果你对function组件未做处理直接加上ref,react会直接忽略并在开发环境给出警告</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2c60a47a1774e8a97ca864845a3f33e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>函数组件没有实例可以赋值给ref对象,而且组件上的ref prop会被当作保留属性无法在组件中获取,那该怎么办呢？</p>
<h4 data-id="heading-9">forwardRef</h4>
<p>React提供了一个forwardRef函数 来处理函数组件的 ref prop，用起来就像下面这个示例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> childRef = useRef(<span class="hljs-literal">null</span>)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;childRef&#125;/</span>></span></span>
&#125;

<span class="hljs-keyword">const</span> Child = forWardRef(<span class="hljs-function">(<span class="hljs-params">props,ref</span>) =></span> &#123;
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Child<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法的源码主体也非常简单，返回了一个新的elementType对象，这个对象的render属性包含了原本的这个函数组件,而$$typeof则标记了这个特殊组件类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forwardRef</span>(<span class="hljs-params">render</span>) </span>&#123;
  ....
  <span class="hljs-keyword">var</span> elementType = &#123;
    <span class="hljs-attr">$$typeof</span>: REACT_FORWARD_REF_TYPE,
    <span class="hljs-attr">render</span>: render
  &#125;
  ....
  <span class="hljs-keyword">return</span> elementType;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么React对forwardRef这个特殊的组件是怎么处理的呢</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">beginWork</span>(<span class="hljs-params">current, workInProgress, renderLanes</span>) </span>&#123;
...
  <span class="hljs-keyword">switch</span> (workInProgress.tag) &#123;
    <span class="hljs-keyword">case</span> FunctionComponent:
      &#123;
       ...
        <span class="hljs-keyword">return</span> updateFunctionComponent(current, workInProgress, _Component, resolvedProps, renderLanes);
      &#125;

    <span class="hljs-keyword">case</span> ClassComponent:
      &#123;
....
        <span class="hljs-keyword">return</span> updateClassComponent(current, workInProgress, _Component2, _resolvedProps, renderLanes);
      &#125;

    <span class="hljs-keyword">case</span> HostComponent:
      <span class="hljs-keyword">return</span> updateHostComponent(current, workInProgress, renderLanes);
    <span class="hljs-keyword">case</span> ForwardRef:
      &#123;
....
        <span class="hljs-comment">// 第三个参数type就是forwardRef创建的elementType</span>
        <span class="hljs-keyword">return</span> updateForwardRef(current, workInProgress, type, _resolvedProps2, renderLanes);
      &#125;
&#125;
  
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateForwardRef</span>(<span class="hljs-params">current, workInProgress, Component, nextProps, renderLanes</span>) </span>&#123;
....
  <span class="hljs-keyword">var</span> render = Component.render;
  <span class="hljs-keyword">var</span> ref = workInProgress.ref; <span class="hljs-comment">// The rest is a fork of updateFunctionComponent</span>

  <span class="hljs-keyword">var</span> nextChildren;

  &#123;
...
    <span class="hljs-comment">//将ref引用传入renderWithHooks</span>
    nextChildren = renderWithHooks(current, workInProgress, render, nextProps, ref, renderLanes);
    ...
  &#125;

  workInProgress.flags |= PerformedWork;
  reconcileChildren(current, workInProgress, nextChildren, renderLanes);
  <span class="hljs-keyword">return</span> workInProgress.child;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到和上面 <code>FunctionComponent</code>的主要区别仅仅是把ref保留属性当成普通属性传入 <code>renderWithHooks</code>方法!</p>
<p>那么又有一个问题出现了，如果只是传了一个ref引用，而没有像Class组件那样可以attach的实例,岂不是没有办法操作子函数组件的行为？</p>
<p>用上面的例子验证一下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> childRef = useRef(<span class="hljs-literal">null</span>)
  useEffect(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-built_in">console</span>.log(childref) <span class="hljs-comment">// &#123; current:null &#125;</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;childRef&#125;/</span>></span></span>
&#125;

<span class="hljs-keyword">const</span> Child = forwardRef(<span class="hljs-function">(<span class="hljs-params">props,ref</span>) =></span> &#123;
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Child<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;&#125;
                         
 <span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> childRef = useRef(<span class="hljs-literal">null</span>)
  useEffect(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-built_in">console</span>.log(childref) <span class="hljs-comment">// &#123; current: div &#125;</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;childRef&#125;/</span>></span></span>
&#125;

<span class="hljs-keyword">const</span> Child = forwardRef(<span class="hljs-function">(<span class="hljs-params">props,ref</span>) =></span> &#123;
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref&#125;</span>></span>Child<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合输出可以看出如果单独使用forwardRef仅仅只能转发ref属性。如果ref最终没有绑定到一个ClassCompnent或者原生DOM上那么这个ref将不会改变。</p>
<p>假设一个业务场景，你封装了一个表单组件，想对外暴露一些接口比如说提交的action以及校验等操作，这样应该如何处理呢？</p>
<h4 data-id="heading-10">useImperativeHandle</h4>
<p>react为我们提供了这个hook来帮助函数组件向外部暴露属性
先看下效果</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> childRef = useRef(<span class="hljs-literal">null</span>)
  useEffect(<span class="hljs-function">()=></span>&#123;
  chilRef.current.sayName();<span class="hljs-comment">// child</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;childRef&#125;/</span>></span></span>
&#125;

<span class="hljs-keyword">const</span> Child = forwardRef(<span class="hljs-function">(<span class="hljs-params">props,ref</span>) =></span> &#123;
  useImperativeHandle(ref,<span class="hljs-function">()=></span>(&#123;
  <span class="hljs-attr">sayName</span>:<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child'</span>)
    &#125;
  &#125;))
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Child<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下该hook的源码部分（以hook mount阶段为例）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">useImperativeHandle: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ref, create, deps</span>) </span>&#123;
      currentHookNameInDev = <span class="hljs-string">'useImperativeHandle'</span>;
      mountHookTypesDev();
      checkDepsAreArrayDev(deps);
      <span class="hljs-keyword">return</span> mountImperativeHandle(ref, create, deps);
 &#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountImperativeHandle</span>(<span class="hljs-params">ref, create, deps</span>) </span>&#123;
  &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> create !== <span class="hljs-string">'function'</span>) &#123;
      error(<span class="hljs-string">'Expected useImperativeHandle() second argument to be a function '</span> + <span class="hljs-string">'that creates a handle. Instead received: %s.'</span>, create !== <span class="hljs-literal">null</span> ? <span class="hljs-keyword">typeof</span> create : <span class="hljs-string">'null'</span>);
    &#125;
  &#125; <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> If deps are provided, should we skip comparing the ref itself?</span>


  <span class="hljs-keyword">var</span> effectDeps = deps !== <span class="hljs-literal">null</span> && deps !== <span class="hljs-literal">undefined</span> ? deps.concat([ref]) : <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">var</span> fiberFlags = Update;

  <span class="hljs-keyword">return</span> mountEffectImpl(fiberFlags, Layout, imperativeHandleEffect.bind(<span class="hljs-literal">null</span>, create, ref), effectDeps);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">imperativeHandleEffect</span>(<span class="hljs-params">create, ref</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> ref === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">var</span> refCallback = ref;

    <span class="hljs-keyword">var</span> _inst = create();

    refCallback(_inst);
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      refCallback(<span class="hljs-literal">null</span>);
    &#125;;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (ref !== <span class="hljs-literal">null</span> && ref !== <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">var</span> refObject = ref;

    &#123;
      <span class="hljs-keyword">if</span> (!refObject.hasOwnProperty(<span class="hljs-string">'current'</span>)) &#123;
        error(<span class="hljs-string">'Expected useImperativeHandle() first argument to either be a '</span> + <span class="hljs-string">'ref callback or React.createRef() object. Instead received: %s.'</span>, <span class="hljs-string">'an object with keys &#123;'</span> + <span class="hljs-built_in">Object</span>.keys(refObject).join(<span class="hljs-string">', '</span>) + <span class="hljs-string">'&#125;'</span>);
      &#125;
    &#125;
<span class="hljs-comment">// 这里执行了传给hook的第二个参数</span>
    <span class="hljs-keyword">var</span> _inst2 = create();

    refObject.current = _inst2;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      refObject.current = <span class="hljs-literal">null</span>;
    &#125;;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实就是将我们需要暴露的对象及传给useImperativeHandle的第二个函数参数执行结果赋值给了ref的current对象。</p>
<h3 data-id="heading-11">同一份引用</h3>
<p>到此为止我们大致梳理了组件上ref prop 的工作流程，以及如何在函数组件中使用ref prop,貌似比想象中简单。</p>
<p>上面的过程我们注意到从createElement再到构建WorkInProgess Fiber树到最后commit的过程，ref似乎是一直在被传递。</p>
<p>中间过程的代码过于庞大复杂,但是我们可以通过一个简单的测试来验证一下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> isEqualRefDemo = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> isEqualRef = useRef(<span class="hljs-number">1</span>)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"test"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;isEqualRef&#125;</span>></span>
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 class component 和 原生标签来说 就是 <code>createElement</code> 到 <code>commitAttachRef</code>之前:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/667ba2344f2347f1981ef2b3e9752550~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17c2f30f2f0748ac98a8db55924f1848~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在createElement里将ref挂载给window对象，然后在commitAttachRef里判断一下这两次的ref是否全等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65a2bde87736490aaecb2f103c0f83a4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于函数组件来说就是 <code>createElement</code> 到 hook执行 <code>imperativeHandleEffect</code> 之前：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> childRef = useRef(<span class="hljs-number">1</span>)
  useEffect(<span class="hljs-function">()=></span>&#123;
  chilRef.current.sayName();<span class="hljs-comment">// child</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;childRef&#125;/</span>></span></span>
&#125;

<span class="hljs-keyword">const</span> Child = forwardRef(<span class="hljs-function">(<span class="hljs-params">props,ref</span>) =></span> &#123;
  useImperativeHandle(ref,<span class="hljs-function">()=></span>(&#123;
  <span class="hljs-attr">sayName</span>:<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child'</span>)
    &#125;
  &#125;))
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Child<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b570d358556348dbb0bb6453fb40733e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff899adcce2a47ccb72015d37c73f704~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>从createElement添加ref到React整个渲染过程的末尾（commit阶段)被赋值前,这个ref都是同一份引用。</strong>
这也正如 <code>ref</code>单词的本意 <code>reference</code>引用一样。</p>
<h3 data-id="heading-12">小节总结</h3>
<ol>
<li>ref出现在组件上时是一个保留属性</li>
<li>ref在组件存在的生命周期内维护了同一个引用(可变对象 MutableObject)</li>
<li>当ref挂载的对象是原生html标签时会ref对象的current属性会被赋值为真实DOM 而如果是React组件会被赋值为React"组件实例"</li>
<li>ref挂载都在commit阶段处理</li>
</ol>
<h2 data-id="heading-13">创建ref的方式</h2>
<p>ref prop相当于在组件上挖了一个“坑” 来承接 ref对象，但是这样还不够我们还需要先创建ref对象</p>
<h3 data-id="heading-14">字符串ref & callback ref</h3>
<p>这两种创建ref的方式不再赘述，官网以及社区优秀文章可供参考。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fdocs%2Frefs-and-the-dom.html" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/docs/refs-and-the-dom.html" ref="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/refs-a…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Fhow-to-use-react-createref-ea014ad09dba%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/how-to-use-react-createref-ea014ad09dba/" ref="nofollow noopener noreferrer">blog.logrocket.com/how-to-use-…</a></li>
</ul>
<h3 data-id="heading-15">createRef & useRef</h3>
<h4 data-id="heading-16">createRef</h4>
<p>16.3引入了createRef这个api</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75cebeea31394c67af589bb806081bb3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>createRef的源码就是一个闭包，对外暴露了 一个具有 current属性的对象。</p>
<p>我们一般会这样在class component中使用createRef</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CreateRefComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.myRef = React.createRef()
  &#125;
  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.myRef.current.focus()
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.myRef.current)
    <span class="hljs-comment">// dom input</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.myRef&#125;</span> /></span></span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">为什么不能在函数组件中使用createRef</h4>
<p>结合第一节的内容以及 <code>createRef</code>的源码，我们发现，这不过就是在类组件内部挂载了一个可变对象。因为类组件构造函数不会被反复执行,因此这个<code>createRef</code>自然保持同一份引用。但是到了函数组件就不一样了,每一次组件更新, 因为没有特殊处理<code>createRef</code>会被反复重新创建执行，因此在函数组件中使用<code>createRef</code>将不能达到只有同一份引用的效果。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> CreateRefInFC = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> valRef = React.createRef();  <span class="hljs-comment">// 如果在函数组件中使用createRef 在这个例子中点击后ref就会被重新创建因此将始终显示为null</span>
  <span class="hljs-keyword">const</span> [, update] = React.useState();
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    value: &#123;valRef.current&#125;
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
      valRef.current = 80;
      update(&#123;&#125;);
    &#125;&#125;>+
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">useRef</h4>
<p>React 16.8中出现了hooks，使得我们可以在函数组件中定义状态，同时也带来了 <code>useRef</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8c2e49f9da442eaa43a4f1092bab437~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7268ed330bd8433f8b0ea13fb27117fb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>再来看<code>moutRef</code>和<code>updateRef</code>所做的事:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountRef</span>(<span class="hljs-params">initialValue</span>) </span>&#123;
  <span class="hljs-keyword">var</span> hook = mountWorkInProgressHook();

  &#123;
    <span class="hljs-keyword">var</span> _ref2 = &#123;
      <span class="hljs-attr">current</span>: initialValue
    &#125;;
    hook.memoizedState = _ref2;
    <span class="hljs-keyword">return</span> _ref2;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateRef</span>(<span class="hljs-params">initialValue</span>) </span>&#123;
  <span class="hljs-keyword">var</span> hook = updateWorkInProgressHook();
  <span class="hljs-keyword">return</span> hook.memoizedState;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>借助hook数据结构,第一次<code>useRef</code>时将创建的值保存在<code>memoizedState</code>中，之后每次更新阶段则直接返回。</p>
<p>这样在函数组件更新时重复执行useRef仍返回同一份引用。</p>
<p>因此实际上和 <code>createRef</code>一样本质上只是创建了一个 <code>Mutable Object</code>，只是因为渲染方式的不同，在函数组件中做了一些处理。而挂载和卸载的行为全部交由组件本身来维护。</p>
<h3 data-id="heading-19">被扩展的ref</h3>
<p>从 <code>createRef</code>开始我们可以看到，<code>ref</code>对象的消费不再和DOM以及组件属性所绑定了，这意味着你可以在任何地方消费他们，这也回答了本文一开始的那个问题。</p>
<h2 data-id="heading-20">useRef的应用</h2>
<h4 data-id="heading-21">解决闭包问题</h4>
<p>由于函数组件每次执行形成的闭包,下面这段代码会始终打印1</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ClosureDemo =  <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> [ count,setCount ] = useState(<span class="hljs-number">0</span>);
    useEffect(<span class="hljs-function">()=></span> &#123;
        <span class="hljs-keyword">const</span> interval = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
          setCount(count+<span class="hljs-number">1</span>)
        &#125;, <span class="hljs-number">1000</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> <span class="hljs-built_in">clearInterval</span>(interval)
      &#125;, [])
    <span class="hljs-comment">// count显示始终是1</span>
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123; count &#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 count 作为依赖传入useEffect可以解决上面这个问题</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ClosureDemo =  <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> [ count,setCount ] = useState(<span class="hljs-number">0</span>);
    useEffect(<span class="hljs-function">()=></span> &#123;
        <span class="hljs-keyword">const</span> interval = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
          setCount(count+<span class="hljs-number">1</span>)
        &#125;, <span class="hljs-number">1000</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> <span class="hljs-built_in">clearInterval</span>(interval)
      &#125;, [count])
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123; count &#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样定时器也会随着count值的更新而被不断创建，一方面会带来性能问题(这个例子中没有那么明显)，更重要的一个方面是它不符合我们的开发语义，因为很明显我们希望定时器本身是不变的。</p>
<p>另外一个方式也可以处理这个问题</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ClosureDemo =  <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> [ count,setCount ] = useState(<span class="hljs-number">0</span>);
    useEffect(<span class="hljs-function">()=></span> &#123;
        <span class="hljs-keyword">const</span> interval = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
          setCount(<span class="hljs-function"><span class="hljs-params">count</span>=></span> count + <span class="hljs-number">1</span>) <span class="hljs-comment">// 使用setSate函数式更新可以确保每次都取到新的值</span>
        &#125;, <span class="hljs-number">1000</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> <span class="hljs-built_in">clearInterval</span>(interval)
      &#125;, [])
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123; count &#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样做确实可以处理闭包带来的影响，但是仅限于需要使用setState的场景，对数据的修改和触发setState是需要绑定的，这可能会造成不必要的刷新。</p>
<p>使用useRef创建引用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ClosureDemo =  <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> [ count,setCount ] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> countRef = useRef(<span class="hljs-number">0</span>);
  countRef.current = count
    useEffect(<span class="hljs-function">()=></span> &#123;
        <span class="hljs-keyword">const</span> interval = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-comment">// 这里将更新count的逻辑和触发更新的逻辑解耦了</span>
          <span class="hljs-keyword">if</span>(countRef.current < <span class="hljs-number">5</span>)&#123;
          countRef.current++
          &#125; <span class="hljs-keyword">else</span> &#123;
          setCount(countRef.current)
          &#125;
        &#125;, <span class="hljs-number">1000</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> <span class="hljs-built_in">clearInterval</span>(interval)
      &#125;, [])
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123; count &#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">封装自定义hooks</h4>
<h5 data-id="heading-23">useCreation</h5>
<p>通过factory函数来避免类似于  <code>useRef(new Construcotr)</code>中构造函数的重复执行</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; useRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useCreation</span><<span class="hljs-title">T</span>>(<span class="hljs-params">factory: () => T, deps: <span class="hljs-built_in">any</span>[]</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; current &#125; = useRef(&#123;
    deps,
    <span class="hljs-attr">obj</span>: <span class="hljs-literal">undefined</span> <span class="hljs-keyword">as</span> <span class="hljs-literal">undefined</span> | T,
    <span class="hljs-attr">initialized</span>: <span class="hljs-literal">false</span>,
  &#125;);
  <span class="hljs-keyword">if</span> (current.initialized === <span class="hljs-literal">false</span> || !depsAreSame(current.deps, deps)) &#123;
    current.deps = deps;
    current.obj = factory();
    current.initialized = <span class="hljs-literal">true</span>;
  &#125;
  <span class="hljs-keyword">return</span> current.obj <span class="hljs-keyword">as</span> T;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">depsAreSame</span>(<span class="hljs-params">oldDeps: <span class="hljs-built_in">any</span>[], deps: <span class="hljs-built_in">any</span>[]</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">if</span> (oldDeps === deps) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> i <span class="hljs-keyword">in</span> oldDeps) &#123;
    <span class="hljs-keyword">if</span> (oldDeps[i] !== deps[i]) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-24">usePrevious</h5>
<p>通过创建两个ref来保存前一次的state</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; useRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> compareFunction<T> = <span class="hljs-function">(<span class="hljs-params">prev: T | <span class="hljs-literal">undefined</span>, next: T</span>) =></span> <span class="hljs-built_in">boolean</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">usePrevious</span><<span class="hljs-title">T</span>>(<span class="hljs-params">state: T, compare?: compareFunction<T></span>): <span class="hljs-title">T</span> | <span class="hljs-title">undefined</span> </span>&#123;
  <span class="hljs-keyword">const</span> prevRef = useRef<T>();
  <span class="hljs-keyword">const</span> curRef = useRef<T>();

  <span class="hljs-keyword">const</span> needUpdate = <span class="hljs-keyword">typeof</span> compare === <span class="hljs-string">'function'</span> ? compare(curRef.current, state) : <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">if</span> (needUpdate) &#123;
    prevRef.current = curRef.current;
    curRef.current = state;
  &#125;

  <span class="hljs-keyword">return</span> prevRef.current;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> usePrevious;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-25">useClickAway</h5>
<p>自定义的元素失焦响应hook</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; useEffect, useRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> BasicTarget<T = HTMLElement> =
  | (<span class="hljs-function">() =></span> T | <span class="hljs-literal">null</span>)
  | T
  | <span class="hljs-literal">null</span>
  | MutableRefObject<T | <span class="hljs-literal">null</span> | <span class="hljs-literal">undefined</span>>;
  
 <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTargetElement</span>(<span class="hljs-params">
  target?: BasicTarget<TargetElement>,
  defaultElement?: TargetElement,
</span>): <span class="hljs-title">TargetElement</span> | <span class="hljs-title">undefined</span> | <span class="hljs-title">null</span> </span>&#123;
  <span class="hljs-keyword">if</span> (!target) &#123;
    <span class="hljs-keyword">return</span> defaultElement;
  &#125;

  <span class="hljs-keyword">let</span> targetElement: TargetElement | <span class="hljs-literal">undefined</span> | <span class="hljs-literal">null</span>;

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'function'</span>) &#123;
    targetElement = target();
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-string">'current'</span> <span class="hljs-keyword">in</span> target) &#123;
    targetElement = target.current;
  &#125; <span class="hljs-keyword">else</span> &#123;
    targetElement = target;
  &#125;
  <span class="hljs-keyword">return</span> targetElement;
&#125;
<span class="hljs-comment">// 鼠标点击事件，click 不会监听右键</span>
<span class="hljs-keyword">const</span> defaultEvent = <span class="hljs-string">'click'</span>;

<span class="hljs-keyword">type</span> EventType = MouseEvent | TouchEvent;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useClickAway</span>(<span class="hljs-params">
  onClickAway: (event: EventType) => <span class="hljs-built_in">void</span>,
  target: BasicTarget | BasicTarget[],
  eventName: <span class="hljs-built_in">string</span> = defaultEvent,
</span>) </span>&#123;
  <span class="hljs-comment">// 使用useRef保存回调函数</span>
  <span class="hljs-keyword">const</span> onClickAwayRef = useRef(onClickAway);
  onClickAwayRef.current = onClickAway;

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> handler = <span class="hljs-function">(<span class="hljs-params">event: <span class="hljs-built_in">any</span></span>) =></span> &#123;
      <span class="hljs-keyword">const</span> targets = <span class="hljs-built_in">Array</span>.isArray(target) ? target : [target];
      <span class="hljs-keyword">if</span> (
        targets.some(<span class="hljs-function">(<span class="hljs-params">targetItem</span>) =></span> &#123;
          <span class="hljs-keyword">const</span> targetElement = getTargetElement(targetItem) <span class="hljs-keyword">as</span> HTMLElement;
          <span class="hljs-keyword">return</span> !targetElement || targetElement?.contains(event.target);
        &#125;)
      ) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      onClickAwayRef.current(event);
    &#125;;

    <span class="hljs-built_in">document</span>.addEventListener(eventName, handler);

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">document</span>.removeEventListener(eventName, handler);
    &#125;;
  &#125;, [target, eventName]);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上自定义hooks均出自<a href="https://link.juejin.cn/?target=https%3A%2F%2Fahooks.js.org%2Fzh-CN%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ahooks.js.org/zh-CN/" ref="nofollow noopener noreferrer">ahooks</a></p>
<p>还有许多好用的自定义hook以及仓库比如<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fstreamich%2Freact-use" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/streamich/react-use" ref="nofollow noopener noreferrer">react-use</a>都基于useRef自定义了很多好用的hook。</p>
<h2 data-id="heading-26">参考资料</h2>
<ul>
<li>React Fiber <a href="https://juejin.cn/post/6844903975112671239#heading-10" target="_blank" title="https://juejin.cn/post/6844903975112671239#heading-10">juejin.cn/post/684490…</a></li>
<li>React 官网ref使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fdocs%2Frefs-and-the-dom.html%23gatsby-focus-wrapper" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/docs/refs-and-the-dom.html#gatsby-focus-wrapper" ref="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/refs-a…</a></li>
<li>React 前生今世 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F40462264" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/40462264" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/40462264</a></li>
<li>React ref源码分析 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_32281471%2Farticle%2Fdetails%2F98473846" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_32281471/article/details/98473846" ref="nofollow noopener noreferrer">blog.csdn.net/qq_32281471…</a></li>
</ul>
<h2 data-id="heading-27">最后</h2>
<p>微信搜索公众号Eval Studio，关注更多动态。</p></div>  
</div>
            