
---
title: '（建议收藏） React Hooks 源码解毒'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5407cb77632040a5910f072c6b6dc3cb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 19:48:47 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5407cb77632040a5910f072c6b6dc3cb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>知其所以然的时刻到了。先来道面试题（相信绝大部分React开发童鞋都遇到过）</p>
<p>面试官：<strong>function</strong> 组件 和 <strong>class</strong> 组件有什么区别？</p>
<p>答： 有几方面。</p>
<ul>
<li>使用function创建的组件叫做 <strong><code>「无状态组件</code></strong>，使用class创建的组件叫做 <strong><code>「有状态组件」</code></strong> </li>
<li><strong><code>「无状态组件」</code></strong> 只能函数入参 （也就是 <strong>props</strong>）来接收外界传递过来的数据。 <strong><code>「有状态组件」</code></strong> 除了只读属性 <strong>this.props</strong> 外, 还有个存放私有数据的 <strong>this.state</strong> 属性，该属性可读写。 </li>
<li>function 没有 this 的困扰。因为你不会也不用在<strong>function</strong>里面写 <strong>this</strong>。吼！（破音） </li>
<li><strong><code>「有状态组件」</code></strong> 存在生命周期。 <strong><code>「无状态组件」</code></strong> 木有生命周期。 </li>
</ul>
<p>以上都是废话，<strong><code>「有 / 无 状态组件」</code><strong>最本质的区别在于：在</strong>class</strong>状态中，通过一个实例化的<strong>class</strong> ，去维护组件中的各种状态；但是在<strong>function</strong>组件中，没有一个状态机制去保存这些信息。每一次函数上下文执行，所有变量&常量都重新声明，执行完毕，再被垃圾机制回收。</p>
<p>（这里给面试官埋了坑，你要么继续往下问 react hooks，要么问函数执行上下文，再要么v8 GC。 这叫面试心理学，学着点～ 2333333）</p>
<p>那么，实际「<strong>React hooks</strong>」也并没有多难理解，说白了就是为 <strong><code>「无状态组件」</code></strong> 提供一套状态管理机制，在此基础上又增加了一些问题的解决方案。例如逻辑不能复用、无法优雅的打破纯函数平衡等。</p>
<p>来吧，热热身</p>
<p>以下问题，你能答好几个。</p>
<ol>
<li>在无状态组件每一次函数上下文执行的时候，「<strong>React</strong>」<code>** 用什么方式记录了 「**Hooks**」</code>** 的状态？ </li>
<li>「 <strong>react hooks</strong> 」`** 如何记录 每一个 钩子的使用顺序的？ </li>
<li>为什么不能条件语句中，声明 hooks ? </li>
<li>「<strong>function</strong>」<code>**组件中的 「useState」</code>** 和 「<strong>calss</strong>」`**组件的setState有什么区别？ </li>
<li>「useEffect」<code>**、「useMemo」</code>**需要依赖注入，为什么「useRef」`**不需要？ </li>
<li>「 useMemo 」`** 是如何对组件进行缓存的？ </li>
<li>为什么多次 调用多次 「useState」`** ，函数组件不更新? </li>
<li>能手动实现这些 hooks 吗？ </li>
</ol>
<h3 data-id="heading-1">React Hooks 原理</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5407cb77632040a5910f072c6b6dc3cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一切从使用开始分析：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span> (<span class="hljs-params"></span>) </span>&#123;

    <span class="hljs-keyword">const</span> [xx,setXx] = useState(<span class="hljs-string">''</span>)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当你 import 「 <strong>useState</strong> 」的时候，发生了什么事情？ <strong>废话，当然是执行源码去了</strong> ……</p>
<p>Path:  React/cjs/react.development.js</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c82930c69094a698b5a6f1e48cab71a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>贴图有点丑，后面就不贴了……</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 源码第1495行</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useState</span>(<span class="hljs-params">initialState</span>) </span>&#123;

  <span class="hljs-keyword">var</span> dispatcher = resolveDispatcher();

  <span class="hljs-keyword">return</span> dispatcher.useState(initialState);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显，我们调用的 <strong>useState</strong> 就是 <strong>dispatcher.useState</strong>， 而<strong>dispatcher</strong> 是 <strong>resolveDispatcher</strong>的执行结果。 so，接着看 <strong>resolveDispatcher</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveDispatcher</span>(<span class="hljs-params"></span>) </span>&#123;

  <span class="hljs-keyword">var</span> dispatcher = ReactCurrentDispatcher.current;


  <span class="hljs-keyword">if</span> (!(dispatcher !== <span class="hljs-literal">null</span>)) &#123;

    &#123;

      <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>( <span class="hljs-string">"Invalid hook call. Hooks can only be called inside of the body of a function component. This could happen for one of the following reasons:\n1. You might have mismatching versions of React and the renderer (such as React DOM)\n2. You might be breaking the Rules of Hooks\n3. You might have more than one copy of React in the same app\nSee https://fb.me/react-invalid-hook-call for tips about how to debug and fix this problem."</span> );

    &#125;

  &#125;


  <span class="hljs-keyword">return</span> dispatcher;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>破案<strong>1:</strong> 为什么<strong>hooks</strong> 必须要在<strong>function</strong>内部使用？</p>
<p>源码很好理解，ReactCurrentDispatcher.current 就是当前的 dispatcher </p>
<pre><code class="hljs language-js copyable" lang="js">

<span class="hljs-comment">/**

 * Keeps track of the current dispatcher.

 */</span>

<span class="hljs-keyword">var</span> ReactCurrentDispatcher = &#123;

  <span class="hljs-comment">/**

   * <span class="hljs-doctag">@internal</span>

   * <span class="hljs-doctag">@type <span class="hljs-type">&#123;ReactComponent&#125;</span></span>

   */</span>

  <span class="hljs-attr">current</span>: <span class="hljs-literal">null</span>

&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 先来读一下注释。 直译过来是跟踪当前调度程序，意译过来则是： 对当前的调度者保持联系。再看current的字段注释：<strong>ReactComponent</strong>。 ****意思是，这个调度者必须是<strong>React</strong>组件。</p>
<p>OK，源码看到这就开始尴尬了。因为没下文了呀，current 初始值是null，然后没了😅。既然 useState  这条路没走通，那就只能从useState的上一层来看了。</p>
<p><strong>function</strong> 是如何执行的？</p>
<p>因为function 内部才能使用react hooks 嘛！那我们知道在React 新架构中，什么东西在什么时候调用是由协调层统筹的。所以，我们可以抱着猜想去看看 「<strong>react-reconciler</strong>」`</p>
<p>Path: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fmain%2Fpackages%2Freact-reconciler%2Fsrc%2FReactFiberBeginWork.new.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/main/packages/react-reconciler/src/ReactFiberBeginWork.new.js" ref="nofollow noopener noreferrer">react/packages/react-reconciler/src/<strong>ReactFiberBeginWork.new.js</strong></a></p>
<p>在源码中你会看见大量的 「<strong>renderWithHooks</strong>」调用。看名字你也知道，这个方法就是用来渲染function组件的。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderWithHooks</span><<span class="hljs-title">Props</span>, <span class="hljs-title">SecondArg</span>>(<span class="hljs-params">

  current: Fiber | <span class="hljs-literal">null</span>, <span class="hljs-comment">//  如果是初始化 则 current 为 null</span>

  workInProgress: Fiber, <span class="hljs-comment">// *workInProgress Fiber*</span>

  Component: (p: Props, arg: SecondArg) => any, <span class="hljs-comment">// function Component 本身</span>

  props: Props,

  secondArg: SecondArg,

  nextRenderLanes: Lanes, <span class="hljs-comment">// 下一个渲染通道。 曾经也叫 渲染过期时间</span>

</span>): <span class="hljs-title">any</span> </span>&#123;

  renderLanes = nextRenderLanes;

  currentlyRenderingFiber = workInProgress; <span class="hljs-comment">// &1 *workInProgress*到底干嘛的？我们先给它打个标，待会儿解释</span>


  <span class="hljs-keyword">if</span> (__DEV__) &#123;

    hookTypesDev =

      current !== <span class="hljs-literal">null</span>

        ? ((current._debugHookTypes: any): <span class="hljs-built_in">Array</span><HookType>)

        : <span class="hljs-literal">null</span>;

    hookTypesUpdateIndexDev = -<span class="hljs-number">1</span>;

    <span class="hljs-comment">// Used for hot reloading:</span>

    ignorePreviousDependencies =

      current !== <span class="hljs-literal">null</span> && current.type !== workInProgress.type;

  &#125;


  workInProgress.memoizedState = <span class="hljs-literal">null</span>; <span class="hljs-comment">// &2  缓存state，具体放什么后面说</span>

  workInProgress.updateQueue = <span class="hljs-literal">null</span>; <span class="hljs-comment">// &3 更新队列</span>

  workInProgress.lanes = NoLanes;

  <span class="hljs-keyword">if</span> (__DEV__) &#123;

   <span class="hljs-comment">// code ……</span>

  &#125; <span class="hljs-keyword">else</span> &#123;

    ReactCurrentDispatcher.current =

      current === <span class="hljs-literal">null</span> || current.memoizedState === <span class="hljs-literal">null</span>

        ? HooksDispatcherOnMount

        : HooksDispatcherOnUpdate;

  &#125;


  <span class="hljs-keyword">let</span> children = Component(props, secondArg); <span class="hljs-comment">// **Component(props, secondArg)**</span>


  <span class="hljs-comment">// Check if there was a render phase update</span>

  <span class="hljs-keyword">if</span> (didScheduleRenderPhaseUpdateDuringThisPass <span class="hljs-comment">/*在此过程中，计划渲染阶段是否更新*/</span>) &#123;

    <span class="hljs-comment">// Keep rendering in a loop for as long as render phase updates continue to</span>

    <span class="hljs-comment">// be scheduled. Use a counter to prevent infinite loops.</span>

    <span class="hljs-keyword">let</span> numberOfReRenders: number = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">do</span> &#123;

      didScheduleRenderPhaseUpdateDuringThisPass = <span class="hljs-literal">false</span>;

      invariant(

        numberOfReRenders < RE_RENDER_LIMIT,

        <span class="hljs-string">'Too many re-renders. React limits the number of renders to prevent '</span> +

          <span class="hljs-string">'an infinite loop.'</span>,

      );


      numberOfReRenders += <span class="hljs-number">1</span>;

      <span class="hljs-comment">// code ……</span>


      ReactCurrentDispatcher.current = __DEV__

        ? HooksDispatcherOnRerenderInDEV

        : HooksDispatcherOnRerender;

      children = Component(props, secondArg);

    &#125; <span class="hljs-keyword">while</span> (didScheduleRenderPhaseUpdateDuringThisPass);

  &#125;



  <span class="hljs-comment">// We can assume the previous dispatcher is always this one, since we set it</span>

  <span class="hljs-comment">// at the beginning of the render phase and there's no re-entrance.</span>

  ReactCurrentDispatcher.current = ContextOnlyDispatcher;

    <span class="hljs-comment">// code... 源码太多，部分不贴了。</span>

  <span class="hljs-keyword">const</span> didRenderTooFewHooks =

      currentHook !== <span class="hljs-literal">null</span> && currentHook.next !== <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// code... 源码太多，部分不贴了。</span>

  invariant(

    !didRenderTooFewHooks,

    <span class="hljs-string">'Rendered fewer hooks than expected. This may be caused by an accidental '</span> +

      <span class="hljs-string">'early return statement.'</span>,

  );

  <span class="hljs-keyword">return</span> children;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>呼～！ 此处小结一下：</p>
<ul>
<li>renderWithHooks 其实是个高阶函数，最终会return 函数组件本身 </li>
<li>开始执行函数组件，初始化「<strong>workInProgress Fiber 树</strong>」的<code>「 memoizedState 」</code>和 「<strong>updateQueue</strong>」。 <strong>why</strong>？</li>
<li>
<ul>
<li>因为在接下来的过程中，要把新的hooks信息（update）挂载到这两个属性上，然后在组件commit阶段，将workInProgress树替换成current树，替换真实的<strong>DOM</strong>元素节点。并在current树保存hooks信息。 </li>
</ul>
</li>
<li>在函数组件上下文执行阶段，会循环判断在此过程中，计划渲染阶段是否更新（<strong>didScheduleRenderPhaseUpdateDuringThisPass</strong>）。 <strong>hooks</strong>被依次执行，把<strong>hooks</strong>信息依次保存到<strong>workInProgress</strong>树上（如何保存，后面再讲）。 </li>
<li>nextRenderLanes: 用来判定优先级。 </li>
<li>调用<strong>Component(props, secondArg)</strong> 。函数组件在这里真正的被执行了 </li>
<li>不管什么样的环境下，ReactCurrentDispatcher.current 都会被赋值。初始化则被赋予「<strong>HooksDispatcherOnMount</strong>」，更新则被赋予「<strong>HooksDispatcherOnUpdate</strong>」。 </li>
</ul>
<h3 data-id="heading-2">HooksDispatcherOnMount & HooksDispatcherOnUpdate</h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> HooksDispatcherOnMount: Dispatcher = &#123;

  readContext,

  <span class="hljs-attr">useCallback</span>: mountCallback,

  <span class="hljs-attr">useContext</span>: readContext,

  <span class="hljs-attr">useEffect</span>: mountEffect,

  <span class="hljs-attr">useImperativeHandle</span>: mountImperativeHandle,

  <span class="hljs-attr">useLayoutEffect</span>: mountLayoutEffect,

  <span class="hljs-attr">useMemo</span>: mountMemo,

  <span class="hljs-attr">useReducer</span>: mountReducer,

  <span class="hljs-attr">useRef</span>: mountRef,

  <span class="hljs-attr">useState</span>: mountState,

  <span class="hljs-attr">useDebugValue</span>: mountDebugValue,

  <span class="hljs-attr">useDeferredValue</span>: mountDeferredValue,

  <span class="hljs-attr">useTransition</span>: mountTransition,

  <span class="hljs-attr">useMutableSource</span>: mountMutableSource,

  <span class="hljs-attr">useOpaqueIdentifier</span>: mountOpaqueIdentifier,


  <span class="hljs-attr">unstable_isNewReconciler</span>: enableNewReconciler,

&#125;;


<span class="hljs-keyword">const</span> HooksDispatcherOnUpdate: Dispatcher = &#123;

  readContext,


  <span class="hljs-attr">useCallback</span>: updateCallback,

  <span class="hljs-attr">useContext</span>: readContext,

  <span class="hljs-attr">useEffect</span>: updateEffect,

  <span class="hljs-attr">useImperativeHandle</span>: updateImperativeHandle,

  <span class="hljs-attr">useLayoutEffect</span>: updateLayoutEffect,

  <span class="hljs-attr">useMemo</span>: updateMemo,

  <span class="hljs-attr">useReducer</span>: updateReducer,

  <span class="hljs-attr">useRef</span>: updateRef,

  <span class="hljs-attr">useState</span>: updateState,

  <span class="hljs-attr">useDebugValue</span>: updateDebugValue,

  <span class="hljs-attr">useDeferredValue</span>: updateDeferredValue,

  <span class="hljs-attr">useTransition</span>: updateTransition,

  <span class="hljs-attr">useMutableSource</span>: updateMutableSource,

  <span class="hljs-attr">useOpaqueIdentifier</span>: updateOpaqueIdentifier,


  <span class="hljs-attr">unstable_isNewReconciler</span>: enableNewReconciler,

&#125;;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，走到这，很多东西就逐渐明了了。 </p>
<ol>
<li>「<strong>renderWithHooks</strong>」`** ****调用后，<strong>Dispatcher</strong>有了。 </li>
<li>react hooks 钩子分 初始化和更新，初始化用mount XXX， 更新则是update XXX。 </li>
</ol>
<p>OK。再来张图解析一下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b16b4ac561d4f4eb5d81791998580f1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">调用<strong>useXXX</strong>之后发生了什么</h4>
<h5 data-id="heading-4"><strong>useState</strong></h5>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountWorkInProgressHook</span>(<span class="hljs-params"></span>): <span class="hljs-title">Hook</span> </span>&#123;

  <span class="hljs-keyword">const</span> hook: Hook = &#123;

    <span class="hljs-attr">memoizedState</span>: <span class="hljs-literal">null</span>,


    <span class="hljs-attr">baseState</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-attr">baseQueue</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-attr">queue</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-attr">next</span>: <span class="hljs-literal">null</span>,

  &#125;;

  <span class="hljs-keyword">if</span> (workInProgressHook === <span class="hljs-literal">null</span>) &#123;

    <span class="hljs-comment">// This is the first hook in the list</span>

    currentlyRenderingFiber.memoizedState = workInProgressHook = hook;

  &#125; <span class="hljs-keyword">else</span> &#123;

    <span class="hljs-comment">// Append to the end of the list</span>

    **workInProgressHook = workInProgressHook.next = hook;** <span class="hljs-comment">// &</span>

  &#125;

  <span class="hljs-keyword">return</span> workInProgressHook;

&#125;


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountState</span><<span class="hljs-title">S</span>>(<span class="hljs-params"> 

  initialState: (() => S) | S,

</span>): [<span class="hljs-title">S</span>, <span class="hljs-title">Dispatch</span><<span class="hljs-title">BasicStateAction</span><<span class="hljs-title">S</span>>>] </span>&#123;

  <span class="hljs-keyword">const</span> hook = mountWorkInProgressHook(); <span class="hljs-comment">// &1 </span>

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> initialState === <span class="hljs-string">'function'</span>) &#123;

    <span class="hljs-comment">// $FlowFixMe: Flow doesn't like mixed types</span>

    initialState = initialState();

  &#125;

  hook.memoizedState = hook.baseState = initialState;

  <span class="hljs-keyword">const</span> queue = (hook.queue = &#123; <span class="hljs-comment">// &2 </span>

    <span class="hljs-attr">pending</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-attr">interleaved</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-attr">lanes</span>: NoLanes,

    <span class="hljs-attr">dispatch</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-attr">lastRenderedReducer</span>: basicStateReducer,

    <span class="hljs-attr">lastRenderedState</span>: (initialState: any),

  &#125;);

  <span class="hljs-keyword">const</span> dispatch: Dispatch< <span class="hljs-comment">// &3</span>

    BasicStateAction<S>,

  > = (queue.dispatch = (dispatchAction.bind(

    <span class="hljs-literal">null</span>,

    currentlyRenderingFiber,

    queue,

  ): any));

  <span class="hljs-keyword">return</span> [hook.memoizedState, dispatch]; <span class="hljs-comment">// &4 </span>

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析一下：</p>
<ol>
<li>调用 mountWorkInProgressHook(), 得到一个hook对象。 源码直观看大，hook对象上有「<strong><code>memoizedState</code></strong>」、 「<strong><code>baseState</code></strong>」、「<strong><code>queue</code></strong>」 属性。 由 <code>mountWorkInProgressHook</code> 内部实现可知，每个 <code>hook</code> 都以链表形式串联起来，并赋值给 <code>workInProgress</code> 的 memoizedState，从而进一步证实函数组件用 <strong>memoizedState</strong> 存放 <strong>hooks</strong> 链表。 </li>
<li>「<strong><code>queue</code></strong>」。 更新队列 </li>
<li>「<strong><code>dispatch</code></strong>」， 调度，这是个动词。 </li>
<li>return [hook.memoizedState, dispatch]; 最终return 出 你可以结构出来的东西。（<code>（const [xxx,setXxx] = useState()） </code> ）</li>
</ol>
<p>这里要仔细看看，你会发现还有些属性不太懂。 Hook 对象中都存放了那些属性？</p>
<ul>
<li><strong><code>memoizedState</code></strong>： useState 中 保存 state 信息 ｜ useEffect 中 保存着effect 对象 ｜ useMemo 中 保存的是缓存的值和 deps｜ useRef 中保存的是ref 对象。 </li>
<li><strong><code>baseQueue</code></strong> : useState 和useReducer中 保存最新的更新队列。 </li>
<li><strong><code>baseState</code></strong> ： usestate 和 useReducer中,一次更新中 ，产生的最新state值。 </li>
<li><strong><code>queue</code></strong> ： 保存待更新队列 pendingQueue ，更新函数 dispatch 等信息。 </li>
<li><strong><code>next</code></strong>: 指向下一个 hooks对象。 </li>
</ul>
<p><strong><code>破案二： 为什么不能在 if 等条件语句中声明 hooks </code></strong></p>
<p>答： 因为 条件语句会破坏 函数组件用 <strong>memoizedState</strong> 存放 <strong>hooks</strong> 存放 <strong>hooks</strong> 的链表结构。你想让<strong>next</strong> 指向谁？</p>
<p><strong>Q</strong>：那<strong>dispatchAction</strong> 又是什么？</p>
<p>答： 「<strong><code>mountState</code></strong>」究竟做了什么上诉已经说明。但 「<strong><code>dispatchAction</code></strong>」  ……</p>
<p><strong>dispatchAction</strong></p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatchAction</span><<span class="hljs-title">S</span>, <span class="hljs-title">A</span>>(<span class="hljs-params">

  fiber: Fiber,

  queue: UpdateQueue<S, A>,

  action: A,

</span>) </span>&#123;

  <span class="hljs-keyword">if</span> (__DEV__) &#123;

    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">arguments</span>[<span class="hljs-number">3</span>] === <span class="hljs-string">'function'</span>) &#123;

      <span class="hljs-built_in">console</span>.error(

        <span class="hljs-string">"State updates from the useState() and useReducer() Hooks don't support the "</span> +

          <span class="hljs-string">'second callback argument. To execute a side effect after '</span> +

          <span class="hljs-string">'rendering, declare it in the component body with useEffect().'</span>,

      );

    &#125;

  &#125;



  <span class="hljs-comment">// &1 计算本次渲染通道</span>

  <span class="hljs-keyword">const</span> eventTime = requestEventTime();

  <span class="hljs-keyword">const</span> lane = requestUpdateLane(fiber);

 <span class="hljs-comment">// &2 声明update</span>

  <span class="hljs-keyword">const</span> update: Update<S, A> = &#123;

    lane,

    action,

    <span class="hljs-attr">eagerReducer</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-attr">eagerState</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-attr">next</span>: (<span class="hljs-literal">null</span>: any),

  &#125;;


  <span class="hljs-comment">//alternate 指向当前 Fiber 在 workInProgress 树中的对应 Fiber</span>

  <span class="hljs-keyword">const</span> alternate = fiber.alternate; 

  

  <span class="hljs-comment">// &3 判断当前是否在渲染阶段**</span>

  <span class="hljs-keyword">if</span> (

    fiber === currentlyRenderingFiber ||

    (alternate !== <span class="hljs-literal">null</span> && alternate === currentlyRenderingFiber)

  ) &#123;

    <span class="hljs-comment">// This is a render phase update. Stash it in a lazily-created map of</span>

    <span class="hljs-comment">// queue -> linked list of updates. After this render pass, we'll restart</span>

    <span class="hljs-comment">// and apply the stashed updates on top of the work-in-progress hook.</span>

    <span class="hljs-comment">// 似曾相似对吧？</span>

    **didScheduleRenderPhaseUpdateDuringThisPass** = didScheduleRenderPhaseUpdate = <span class="hljs-literal">true</span>;

    <span class="hljs-keyword">const</span> pending = queue.pending;

    <span class="hljs-keyword">if</span> (pending === <span class="hljs-literal">null</span>) &#123;

      <span class="hljs-comment">// This is the first update. Create a circular list.</span>

      update.next = update;

    &#125; <span class="hljs-keyword">else</span> &#123;

      update.next = pending.next;

      pending.next = update;

    &#125;

    queue.pending = update;

  &#125; <span class="hljs-keyword">else</span> &#123; 

  <span class="hljs-comment">/* 当前函数组件对应*fiber*没有处于调和渲染阶段 **，准备更新 **/</span>*

  

  <span class="hljs-comment">// &4 判断是否交叉更新</span>

    <span class="hljs-keyword">if</span> (isInterleavedUpdate(fiber, lane)) &#123;

      <span class="hljs-keyword">const</span> interleaved = queue.interleaved;

      <span class="hljs-keyword">if</span> (interleaved === <span class="hljs-literal">null</span>) &#123;

        <span class="hljs-comment">// This is the first update. Create a circular list.</span>

        update.next = update;

        <span class="hljs-comment">// At the end of the current render, this queue's interleaved updates will</span>

        <span class="hljs-comment">// be transferred to the pending queue.</span>

        <span class="hljs-comment">// &5 在当前渲染结束时，此队列的交错更新将传输到挂起队列。</span>

        pushInterleavedQueue(queue);

      &#125; <span class="hljs-keyword">else</span> &#123;

        update.next = interleaved.next;

        interleaved.next = update;

      &#125;

      queue.interleaved = update;

    &#125; <span class="hljs-keyword">else</span> &#123;

      <span class="hljs-keyword">const</span> pending = queue.pending;

      <span class="hljs-keyword">if</span> (pending === <span class="hljs-literal">null</span>) &#123;

        <span class="hljs-comment">// This is the first update. Create a circular list.</span>

        update.next = update;

      &#125; <span class="hljs-keyword">else</span> &#123;

        update.next = pending.next;

        pending.next = update;

      &#125;

      queue.pending = update;

    &#125;

    <span class="hljs-keyword">if</span> (

      fiber.lanes === NoLanes &&

      (alternate === <span class="hljs-literal">null</span> || alternate.lanes === NoLanes)

    ) &#123;

    <span class="hljs-comment">// &6 </span>

    <span class="hljs-keyword">const</span> lastRenderedReducer = queue.lastRenderedReducer;

    <span class="hljs-keyword">if</span> (lastRenderedReducer !== <span class="hljs-literal">null</span>) &#123;

        <span class="hljs-keyword">let</span> prevDispatcher;

        <span class="hljs-keyword">if</span> (__DEV__) &#123;

          prevDispatcher = ReactCurrentDispatcher.current;

          ReactCurrentDispatcher.current = InvalidNestedHooksDispatcherOnUpdateInDEV;

        &#125;

        <span class="hljs-keyword">try</span> &#123;

          <span class="hljs-keyword">const</span> currentState: S = (queue.lastRenderedState: any);

          <span class="hljs-keyword">const</span> eagerState = lastRenderedReducer(currentState, action);

        

          update.eagerReducer = lastRenderedReducer;

          update.eagerState = eagerState;

          <span class="hljs-comment">// &7 </span>

          <span class="hljs-keyword">if</span> (is(eagerState, currentState)) &#123;

    

            <span class="hljs-keyword">return</span>;

          &#125;

        &#125; 

         <span class="hljs-comment">// code。。。 省略部分源码，写不动了。</span>

      &#125;

      <span class="hljs-comment">// code。。。 省略部分源码，写不动了。</span>

    &#125;

    <span class="hljs-comment">// code。。。 省略部分源码，写不动了。</span>
、
    <span class="hljs-comment">// &8</span>

     <span class="hljs-keyword">const</span> root = scheduleUpdateOnFiber(fiber, lane, eventTime);

     <span class="hljs-comment">// code。。。 省略部分源码，写不动了。</span>

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析一下：</p>
<ol>
<li>计算本次渲染通道，判定优先级要用 </li>
<li>声明 update</li>
<li>
<ol>
<li>Lane : 不解释了 </li>
<li>action : 不解释了 </li>
<li>eagerReducer : 急减速器。 调整优先级方式的一种 </li>
<li>eagerState : 配套使用 </li>
<li>next : 不解释了 </li>
</ol>
</li>
<li>dispatchAction第二步就是判断当前函数组件的fiber对象是否处于渲染阶段，如果处于渲染阶段，那么不需要我们在更新当前函数组件，只需要更新一下当前update的 fiber.lanes 即可。</li>
<li>
<ol>
<li>无论是类组件调用setState,还是函数组件的dispatchAction ，都会产生一个 update对象，里面记录了此次更新的信息，然后将此update放入待更新的pending队列中。 </li>
</ol>
</li>
<li>判断是否交叉更新 </li>
<li>在当前渲染结束时，此队列的交错更新将传输到挂起队列。 </li>
<li>如果当前fiber没有处于更新阶段。那么通过调用lastRenderedReducer获取最新的eagerState </li>
<li>和上一次的currentState，进行浅比较，如果相等就直接return。 </li>
</ol>
<p>破案三：这就证实了为什么 <strong><code>useState</code></strong>，两次值相等的时候，组件不渲染的原因了。这个机制和 <strong><code>Component</code></strong> 模式下的 <strong><code>setState</code></strong> 有一定的区别。 <strong><code>scheduleUpdateOnFiber</code><strong>是</strong>react</strong>渲染更新的主要函数。</p>
<ol start="9">
<li>「<strong>scheduleUpdateOnFiber</strong>」渲染fiber </li>
</ol>
<p>Q：为什么 <strong>React</strong> 当中 ****在 ****非<strong>React API</strong>当中使用 <strong>set XXX</strong> 会被立刻更新？</p>
<p>答：正常的都被急减速器减速了，不正常的被pending了。 但这里还牵扯到 「<strong>Scheduler</strong> 调度层」。 我们目前 还处于 「<strong>Reconciler</strong> 协调层」。 这个以后再讲……</p>
<h4 data-id="heading-5">useEffect</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountEffectImpl</span>(<span class="hljs-params">fiberFlags, hookFlags, create, deps</span>): <span class="hljs-title">void</span> </span>&#123;

  <span class="hljs-keyword">const</span> hook = mountWorkInProgressHook();

  <span class="hljs-keyword">const</span> nextDeps = deps === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">null</span> : deps;

  currentlyRenderingFiber.flags |= fiberFlags;

  **hook.memoizedState = pushEffect**(

    HookHasEffect | hookFlags,

    create,

    <span class="hljs-literal">undefined</span>,

    nextDeps,

  );

&#125;


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountEffect</span>(<span class="hljs-params">

  create: () => (() => <span class="hljs-keyword">void</span>) | <span class="hljs-keyword">void</span>,

  deps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-keyword">void</span> | <span class="hljs-literal">null</span>,

</span>): <span class="hljs-title">void</span> </span>&#123;

  <span class="hljs-keyword">if</span> (__DEV__) &#123;

    <span class="hljs-comment">// $FlowExpectedError - jest isn't a global, and isn't recognized outside of tests</span>

    <span class="hljs-keyword">if</span> (<span class="hljs-string">'undefined'</span> !== <span class="hljs-keyword">typeof</span> jest) &#123;

      warnIfNotCurrentlyActingEffectsInDEV(currentlyRenderingFiber);

    &#125;

  &#125;

  <span class="hljs-keyword">if</span> (

    __DEV__ &&

    enableStrictEffects &&

    (currentlyRenderingFiber.mode & StrictEffectsMode) !== NoMode

  ) &#123;

    <span class="hljs-keyword">return</span> mountEffectImpl(

      MountPassiveDevEffect | PassiveEffect | PassiveStaticEffect,

      HookPassive,

      create,

      deps,

    );

  &#125; <span class="hljs-keyword">else</span> &#123;

    <span class="hljs-keyword">return</span> mountEffectImpl(

      PassiveEffect | PassiveStaticEffect,

      HookPassive,

      create,

      deps,

    );

  &#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>同理，每个hooks初始化都会创建一个hook对象，然后将 hook 的「<strong>memoizedState</strong>」保存当前effect hook信息。</p>
<p><strong>Tips</strong>：看清楚了，mountEffect 和 mountState的 「<strong>memoizedState</strong>」存放的东西是不一样的！</p>
<p>所以，<strong><code>hook.memoizedState = pushEffect</code></strong> 的 <strong>pushEffect</strong>是什么东西？</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushEffect</span>(<span class="hljs-params">tag, create, destroy, deps</span>) </span>&#123;

  <span class="hljs-keyword">const</span> effect: Effect = &#123;

    tag,

    create,

    destroy,

    deps,

    <span class="hljs-comment">// Circular</span>

    <span class="hljs-attr">next</span>: (<span class="hljs-literal">null</span>: any),

  &#125;;

  <span class="hljs-comment">// &1 </span>

  <span class="hljs-keyword">let</span> componentUpdateQueue: <span class="hljs-literal">null</span> | FunctionComponentUpdateQueue = (currentlyRenderingFiber.updateQueue: any);

  <span class="hljs-keyword">if</span> (componentUpdateQueue === <span class="hljs-literal">null</span>) &#123; <span class="hljs-comment">// &2 </span>

    componentUpdateQueue = createFunctionComponentUpdateQueue();

    currentlyRenderingFiber.updateQueue = (componentUpdateQueue: any);

    componentUpdateQueue.lastEffect = effect.next = effect;

  &#125; <span class="hljs-keyword">else</span> &#123;

    <span class="hljs-keyword">const</span> lastEffect = componentUpdateQueue.lastEffect;

    <span class="hljs-keyword">if</span> (lastEffect === <span class="hljs-literal">null</span>) &#123;

      componentUpdateQueue.lastEffect = effect.next = effect;

    &#125; <span class="hljs-keyword">else</span> &#123;

      <span class="hljs-keyword">const</span> firstEffect = lastEffect.next;

      lastEffect.next = effect;

      effect.next = firstEffect;

      componentUpdateQueue.lastEffect = effect;

    &#125;

  &#125;

  <span class="hljs-comment">// &3</span>

  <span class="hljs-keyword">return</span> effect;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（相信此时你对如何阅读源码已经有了一定心得。我就不写注释了…… 憋打我）</p>
<p>解析一下</p>
<ol>
<li><strong><code>「pushEffect」</code></strong> 创建effect对象，挂载 updateQueue </li>
<li>判断组件如果第一次渲染，那么创建 componentUpdateQueue ，就是workInProgress的updateQueue。然后将effect放入updateQueue中。 </li>
<li>最终返回 「effect」</li>
</ol>
<p><strong><code>Q：React 是如何执行所有的 effect 的？</code></strong></p>
<p>答：  Fiber对象 上有个effectTag 属性。 React是采取深度优先遍历的方式来便利Fiber 树，每个Fiber对象的effectTag属性，根据Fiber对象的firstEffect 属性，将Fiber对象有效的副作用提取出来 ，构建出一个只包含副作用的 EffectList。 最终遍历EffectList，根据effectTag属性去执行相对应的副作用回调函数。（这里是不是又开始对<strong>Fiber</strong> 对象好奇了？）</p>
<h4 data-id="heading-6">useMemo</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountMemo</span><<span class="hljs-title">T</span>>(<span class="hljs-params">

  nextCreate: () => T,

  deps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-keyword">void</span> | <span class="hljs-literal">null</span>,

</span>): <span class="hljs-title">T</span> </span>&#123;

  <span class="hljs-keyword">const</span> hook = mountWorkInProgressHook();

  <span class="hljs-keyword">const</span> nextDeps = deps === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">null</span> : deps;

  <span class="hljs-keyword">const</span> nextValue = nextCreate();

  hook.memoizedState = [nextValue, nextDeps];

  <span class="hljs-keyword">return</span> nextValue;

&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>自己看。没啥复杂的东西，就是记录了一个 memoizedState。</p>
<h4 data-id="heading-7">useRef</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountRef</span><<span class="hljs-title">T</span>>(<span class="hljs-params">initialValue: T</span>): </span>&#123;|current: T|&#125; &#123;

  <span class="hljs-keyword">const</span> hook = mountWorkInProgressHook();

  <span class="hljs-keyword">if</span> (enableUseRefAccessWarning) &#123;

    <span class="hljs-comment">// 原谅我又偷懒，省去了部分源码。</span>

  &#125; <span class="hljs-keyword">else</span> &#123;

    <span class="hljs-keyword">const</span> ref = &#123;<span class="hljs-attr">current</span>: initialValue&#125;;

    hook.memoizedState = ref;

    <span class="hljs-keyword">return</span> ref;

  &#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实，更简单。只不过现在的React版本加了一个使用UseRef的访问警告。 有兴趣的可以去查查……</p>
<h4 data-id="heading-8">updateWorkInProgressHook</h4>
<p>噢，既然有mount，自然就有update。 React 使用两套API来分别关心初始化和更新。但如果你看源码的话，会发现updateXXX代码都很简单得令人发指……</p>
<p>不信给你瞅瞅源码。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateState</span><<span class="hljs-title">S</span>>(<span class="hljs-params">

  initialState: (() => S) | S,

</span>): [<span class="hljs-title">S</span>, <span class="hljs-title">Dispatch</span><<span class="hljs-title">BasicStateAction</span><<span class="hljs-title">S</span>>>] </span>&#123;

  <span class="hljs-keyword">return</span> updateReducer(basicStateReducer, (initialState: any));

&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateRefresh</span>(<span class="hljs-params"></span>) </span>&#123;

  <span class="hljs-keyword">const</span> hook = updateWorkInProgressHook();

  <span class="hljs-keyword">return</span> hook.memoizedState;

&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateMemo</span><<span class="hljs-title">T</span>>(<span class="hljs-params">

  nextCreate: () => T,

  deps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-keyword">void</span> | <span class="hljs-literal">null</span>,

</span>): <span class="hljs-title">T</span> </span>&#123;

  <span class="hljs-keyword">const</span> hook = updateWorkInProgressHook();

  <span class="hljs-keyword">const</span> nextDeps = deps === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">null</span> : deps;

  <span class="hljs-keyword">const</span> prevState = hook.memoizedState;

  <span class="hljs-keyword">if</span> (prevState !== <span class="hljs-literal">null</span>) &#123;

    <span class="hljs-comment">// Assume these are defined. If they're not, areHookInputsEqual will warn.</span>

    <span class="hljs-keyword">if</span> (nextDeps !== <span class="hljs-literal">null</span>) &#123;

      <span class="hljs-keyword">const</span> prevDeps: <span class="hljs-built_in">Array</span><mixed> | <span class="hljs-literal">null</span> = prevState[<span class="hljs-number">1</span>];

      <span class="hljs-keyword">if</span> (areHookInputsEqual(nextDeps, prevDeps)) &#123;

        <span class="hljs-keyword">return</span> prevState[<span class="hljs-number">0</span>];

      &#125;

    &#125;

  &#125;

  <span class="hljs-keyword">const</span> nextValue = nextCreate();

  hook.memoizedState = [nextValue, nextDeps];

  <span class="hljs-keyword">return</span> nextValue;

&#125;

……
<span class="copy-code-btn">复制代码</span></code></pre>
<p>废话不多说，你会发现updateXX就做了大概两件事情。 </p>
<ol>
<li>调用 updateWorkInProgressHook </li>
<li>更新 hook.memoizedState </li>
</ol>
<p>那我们还是来解析一下updateWorkInProgressHook源码</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateWorkInProgressHook</span>(<span class="hljs-params"></span>): <span class="hljs-title">Hook</span> </span>&#123;

  <span class="hljs-comment">// This function is used both for updates and for re-renders triggered by a</span>

  <span class="hljs-comment">// render phase update. It assumes there is either a current hook we can</span>

  <span class="hljs-comment">// clone, or a work-in-progress hook from a previous render pass that we can</span>

  <span class="hljs-comment">// use as a base. When we reach the end of the base list, we must switch to</span>

  <span class="hljs-comment">// the dispatcher used for mounts.</span>

  <span class="hljs-keyword">let</span> nextCurrentHook: <span class="hljs-literal">null</span> | Hook;

  <span class="hljs-keyword">if</span> (currentHook === <span class="hljs-literal">null</span>) &#123; <span class="hljs-comment">// &1 判断是否是第一个*hooks*</span>

    <span class="hljs-keyword">const</span> current = currentlyRenderingFiber.alternate;

    <span class="hljs-keyword">if</span> (current !== <span class="hljs-literal">null</span>) &#123;

      nextCurrentHook = current.memoizedState;

    &#125; <span class="hljs-keyword">else</span> &#123;

      nextCurrentHook = <span class="hljs-literal">null</span>;

    &#125;

  &#125; <span class="hljs-keyword">else</span> &#123;

  

    nextCurrentHook = currentHook.next; <span class="hljs-comment">// &2 否，那么指向下一个 *hooks*</span>

  &#125;


  <span class="hljs-keyword">let</span> nextWorkInProgressHook: <span class="hljs-literal">null</span> | Hook;

  <span class="hljs-keyword">if</span> (workInProgressHook === <span class="hljs-literal">null</span>) &#123; <span class="hljs-comment">// &3 判断是否第一次访问*hooks*</span>

    nextWorkInProgressHook = currentlyRenderingFiber.memoizedState;

  &#125; <span class="hljs-keyword">else</span> &#123;

  

    nextWorkInProgressHook = workInProgressHook.next; <span class="hljs-comment">// &4 否，则指向……</span>

  &#125;


  <span class="hljs-keyword">if</span> (nextWorkInProgressHook !== <span class="hljs-literal">null</span>) &#123;

    <span class="hljs-comment">// There's already a work-in-progress. Reuse it.</span>

    <span class="hljs-comment">// &5 说明目前已经有hook正在执行，那就重复执行它！</span>

    workInProgressHook = nextWorkInProgressHook;

    nextWorkInProgressHook = workInProgressHook.next;


    currentHook = nextCurrentHook;

  &#125; <span class="hljs-keyword">else</span> &#123;

    <span class="hljs-comment">// Clone from the current hook.</span>

    invariant(

      nextCurrentHook !== <span class="hljs-literal">null</span>,

      <span class="hljs-string">'Rendered more hooks than during the previous render.'</span>,

    );

    currentHook = nextCurrentHook;


    <span class="hljs-keyword">const</span> newHook: Hook = &#123; <span class="hljs-comment">// &6 创建一个新的hook对象</span>

      <span class="hljs-attr">memoizedState</span>: currentHook.memoizedState,


      <span class="hljs-attr">baseState</span>: currentHook.baseState,

      <span class="hljs-attr">baseQueue</span>: currentHook.baseQueue,

      <span class="hljs-attr">queue</span>: currentHook.queue,

      <span class="hljs-attr">next</span>: <span class="hljs-literal">null</span>,

    &#125;;

    <span class="hljs-keyword">if</span> (workInProgressHook === <span class="hljs-literal">null</span>) &#123;

      <span class="hljs-comment">// &7 This is the first hook in the list.</span>

      currentlyRenderingFiber.memoizedState = workInProgressHook = newHook;

    &#125; <span class="hljs-keyword">else</span> &#123;

      <span class="hljs-comment">// &8 Append to the end of the list.</span>

      workInProgressHook = workInProgressHook.next = newHook;

    &#125;

  &#125;

  <span class="hljs-keyword">return</span> workInProgressHook;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">小结一下</h3>
<p>ps： 贴出来的源码我加的注释可以仔细看下，有助于理解。</p>
<p>其实源码也很简单对伐？ 弱弱的说一下，这块可能对大家面试有帮助……</p></div>  
</div>
            