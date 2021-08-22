
---
title: 'React 源码- key 有什么作用, 可以省略吗_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7515'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 07:59:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=7515'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<p>在react组件开发的过程中, <code>key</code>是一个常用的属性值, 多用于列表开发. 本文从源码的角度, 分析<code>key</code>在<code>react</code>内部是如何使用的, <code>key</code>是否可以省略.</p>
<h2 data-id="heading-0">ReactElement对象</h2>
<p>我们在编程时直接书写的<code>jsx</code>代码, 实际上是会被编译成ReactElement对象, 所以<code>key</code>是<code>ReactElement对象</code>的一个属性.</p>
<h3 data-id="heading-1">构造函数</h3>
<p>在把<code>jsx</code>转换成<code>ReactElement对象</code>的语法时, 有一个兼容问题. 会根据编译器的不同策略, 编译成2种方案.</p>
<ol>
<li>
<p>最新的转译策略: 会将<code>jsx</code>语法的代码, 转译成<code>jsx()</code>函数包裹</p>
<p><code>jsx</code>函数: 只保留与<code>key</code>相关的代码(其余源码本节不讨论)</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-comment">/**
   * https://github.com/reactjs/rfcs/pull/107
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">type</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;object&#125;</span> <span class="hljs-variable">props</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">key</span></span>
   */</span>
   <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jsx</span>(<span class="hljs-params">type, config, maybeKey</span>) </span>&#123;
     <span class="hljs-keyword">let</span> propName;

     <span class="hljs-comment">// 1. key的默认值是null</span>
     <span class="hljs-keyword">let</span> key = <span class="hljs-literal">null</span>;

     <span class="hljs-comment">// Currently, key can be spread in as a prop. This causes a potential</span>
     <span class="hljs-comment">// issue if key is also explicitly declared (ie. <div &#123;...props&#125; key="Hi" /></span>
     <span class="hljs-comment">// or <div key="Hi" &#123;...props&#125; /> ). We want to deprecate key spread,</span>
     <span class="hljs-comment">// but as an intermediary step, we will use jsxDEV for everything except</span>
     <span class="hljs-comment">// <div &#123;...props&#125; key="Hi" />, because we aren't currently able to tell if</span>
     <span class="hljs-comment">// key is explicitly declared to be undefined or not.</span>
     <span class="hljs-keyword">if</span> (maybeKey !== <span class="hljs-literal">undefined</span>) &#123;
       key = <span class="hljs-string">''</span> + maybeKey;
     &#125;

     <span class="hljs-keyword">if</span> (hasValidKey(config)) &#123;
       <span class="hljs-comment">// 2. 将key转换成字符串</span>
       key = <span class="hljs-string">''</span> + config.key; 
     &#125;
     <span class="hljs-comment">// 3. 将key传入构造函数</span>
     <span class="hljs-keyword">return</span> ReactElement(
       type,
       key,
       ref,
       <span class="hljs-literal">undefined</span>,
       <span class="hljs-literal">undefined</span>,
       ReactCurrentOwner.current,
       props,
     );
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>传统的转译策略: 会将<code>jsx</code>语法的代码, 转译成<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fv17.0.2%2Fpackages%2Freact%2Fsrc%2FReactElement.js%23L126-L146" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/v17.0.2/packages/react/src/ReactElement.js#L126-L146" ref="nofollow noopener noreferrer">React.createElement()函数包裹</a></p>
<p><code>React.createElement()函数</code>: 只保留与<code>key</code>相关的代码(其余源码本节不讨论)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
  * Create and return a new ReactElement of the given type.
  * See https://reactjs.org/docs/react-api.html#createelement
  */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">type, config, children</span>) </span>&#123;
  <span class="hljs-keyword">let</span> propName;

  <span class="hljs-comment">// Reserved names are extracted</span>
  <span class="hljs-keyword">const</span> props = &#123;&#125;;

  <span class="hljs-keyword">let</span> key = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">let</span> ref = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">let</span> self = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">let</span> source = <span class="hljs-literal">null</span>;

  <span class="hljs-keyword">if</span> (config != <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">if</span> (hasValidKey(config)) &#123;
      key = <span class="hljs-string">''</span> + config.key; <span class="hljs-comment">// key转换成字符串</span>
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> ReactElement(
    type,
    key,
    ref,
    self,
    source,
    ReactCurrentOwner.current,
    props,
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>可以看到无论采取哪种编译方式, 核心逻辑都是一致的:</p>
<ol>
<li><code>key</code>的默认值是<code>null</code></li>
<li>如果外界有显示指定的<code>key</code>, 则将<code>key</code>转换成字符串类型.</li>
<li>调用<code>ReactElement</code>这个构造函数, 并且将<code>key</code>传入.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ReactElement的构造函数: 本节就先只关注其中的key属性</span>
<span class="hljs-keyword">const</span> ReactElement = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">type, key, ref, self, source, owner, props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> element = &#123;
    <span class="hljs-attr">$$typeof</span>: REACT_ELEMENT_TYPE,
    <span class="hljs-attr">type</span>: type,
    <span class="hljs-attr">key</span>: key,
    <span class="hljs-attr">ref</span>: ref,
    <span class="hljs-attr">props</span>: props,
    <span class="hljs-attr">_owner</span>: owner,
  &#125;;
  <span class="hljs-keyword">return</span> element;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码看到这里, 虽然还只是个皮毛, 但是起码知道了<code>key</code>的默认值是<code>null</code>. 所以任何一个<code>reactElement</code>对象, 内部都是有<code>key</code>值的, 只是一般情况下(非list结构)没人显示去传入一个key.</p>
<h2 data-id="heading-2">Fiber对象</h2>
<p><code>react</code>的核心运行逻辑, 是一个从输入到输出的过程(回顾<code>reconciler 运作流程</code>). 编程直接操作的<code>jsx</code>是<code>reactElement对象</code>,我们(程序员)的数据模型是<code>jsx</code>, 而<code>react内核</code>的数据模型是<code>fiber树形结构</code>. 所以要深入认识<code>key</code>还需要从<code>fiber</code>的视角继续来看.</p>
<p><code>fiber</code>对象是在<code>fiber树构造循环</code>过程中构造的, 其构造函数如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FiberNode</span>(<span class="hljs-params">
  tag: WorkTag,
  pendingProps: mixed,
  key: <span class="hljs-literal">null</span> | string,
  mode: TypeOfMode,
</span>) </span>&#123;

  <span class="hljs-built_in">this</span>.tag = tag;
  <span class="hljs-built_in">this</span>.key = key;  <span class="hljs-comment">// 重点: key也是`fiber`对象的一个属性</span>

  <span class="hljs-comment">// ... </span>
  <span class="hljs-built_in">this</span>.elementType = <span class="hljs-literal">null</span>;
  <span class="hljs-built_in">this</span>.type = <span class="hljs-literal">null</span>;
  <span class="hljs-built_in">this</span>.stateNode = <span class="hljs-literal">null</span>;
  <span class="hljs-comment">// ... 省略无关代码</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到, <code>key</code>也是<code>fiber</code>对象的一个属性. 这里和<code>reactElement</code>的情况有所不同:</p>
<ol>
<li><code>reactElement</code>中的<code>key</code>是由<code>jsx</code>编译而来, <code>key</code>是由程序员直接控制的(及时是动态生成, 那也是直接控制)</li>
<li><code>fiber</code>对象是由<code>react</code>内核在运行时创建的, 所以<code>fiber.key</code>也是<code>react</code>内核进行设置的, 程序员没有直接控制.</li>
</ol>
<p>逻辑来到这里, 有2个疑问:</p>
<ol>
<li><code>fiber.key</code>是由<code>react</code>内核设置, 那他的值是否和<code>reactElement.key</code>相同?</li>
<li>如果<code>reactElement.key = null</code>, 那么<code>fiber.key</code>就一定是<code>null</code>吗?</li>
</ol>
<p>要继续跟进这些问题, 还得从<code>fiber</code>的创建说起. 上文提到了, <code>fiber</code>对象的创建发生在<code>fiber树构造循环</code>阶段中, 具体来讲, 是在<code>reconcilerChildren</code>调和函数中进行创建.</p>
<h2 data-id="heading-3">reconcilerChildren调和函数</h2>
<p><code>reconcilerChildren</code>是<code>react</code>中的一个<code>明星</code>函数, 最热点的问题就是<code>diff算法原理</code>, 事实上, <code>key</code>的作用完全就是为了<code>diff算法</code>服务的.</p>
<blockquote>
<p>注意: 本节只分析key相关的逻辑, 对于调和函数的算法原理, 请回顾算法章节<a href="https://juejin.cn/post/6998506888304263199" target="_blank" title="https://juejin.cn/post/6998506888304263199">React 算法之调和算法</a></p>
</blockquote>
<p>调和函数源码(本节示例, 只摘取了部分代码):</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ChildReconciler</span>(<span class="hljs-params">shouldTrackSideEffects</span>) </span>&#123;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildFibers</span>(<span class="hljs-params">
    returnFiber: Fiber,
    currentFirstChild: Fiber | <span class="hljs-literal">null</span>,
    newChild: any,
    lanes: Lanes,
  </span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;
    <span class="hljs-comment">// Handle object types</span>
    <span class="hljs-keyword">const</span> isObject = <span class="hljs-keyword">typeof</span> newChild === <span class="hljs-string">'object'</span> && newChild !== <span class="hljs-literal">null</span>;

    <span class="hljs-keyword">if</span> (isObject) &#123;
      <span class="hljs-keyword">switch</span> (newChild.$$typeof) &#123;
        <span class="hljs-keyword">case</span> REACT_ELEMENT_TYPE:
          <span class="hljs-comment">// newChild是单节点</span>
          <span class="hljs-keyword">return</span> placeSingleChild(
            reconcileSingleElement(
              returnFiber,
              currentFirstChild,
              newChild,
              lanes,
            ),
          );
      &#125;
    &#125;
    <span class="hljs-comment">//  newChild是多节点</span>
    <span class="hljs-keyword">if</span> (isArray(newChild)) &#123;
      <span class="hljs-keyword">return</span> reconcileChildrenArray(
        returnFiber,
        currentFirstChild,
        newChild,
        lanes,
      );
    &#125;
    <span class="hljs-comment">// ...</span>
  &#125;

  <span class="hljs-keyword">return</span> reconcileChildFibers;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">单节点</h3>
<p>这里先看单节点的情况<code>reconcileSingleElement</code>(只保留与<code>key</code>有关的逻辑):</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileSingleElement</span>(<span class="hljs-params">
    returnFiber: Fiber,
    currentFirstChild: Fiber | <span class="hljs-literal">null</span>,
    element: ReactElement,
    lanes: Lanes,
  </span>): <span class="hljs-title">Fiber</span> </span>&#123;
    <span class="hljs-keyword">const</span> key = element.key;
    <span class="hljs-keyword">let</span> child = currentFirstChild;
    <span class="hljs-keyword">while</span> (child !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-comment">//重点1: key是单节点是否复用的第一判断条件</span>
      <span class="hljs-keyword">if</span> (child.key === key) &#123; 
        <span class="hljs-keyword">switch</span> (child.tag) &#123;
          <span class="hljs-attr">default</span>: &#123;
            <span class="hljs-keyword">if</span> (child.elementType === element.type) &#123; <span class="hljs-comment">// 第二判断条件</span>
              deleteRemainingChildren(returnFiber, child.sibling);
              <span class="hljs-comment">// 节点复用: 调用useFiber</span>
              <span class="hljs-keyword">const</span> existing = useFiber(child, element.props);
              existing.ref = coerceRef(returnFiber, child, element);
              existing.return = returnFiber;
              <span class="hljs-keyword">return</span> existing;
            &#125;
            <span class="hljs-keyword">break</span>;
          &#125;
        &#125;
        <span class="hljs-comment">// Didn't match.</span>
        deleteRemainingChildren(returnFiber, child);
        <span class="hljs-keyword">break</span>;
      &#125; 
      child = child.sibling;
    &#125;
    <span class="hljs-comment">// 重点2: fiber节点创建, `key`是随着`element`对象被传入`fiber`的构造函数</span>
    <span class="hljs-keyword">const</span> created = createFiberFromElement(element, returnFiber.mode, lanes);
    created.ref = coerceRef(returnFiber, currentFirstChild, element);
    created.return = returnFiber;
    <span class="hljs-keyword">return</span> created;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到, 对于单节点来讲, 有2个重点:</p>
<ol>
<li><code>key</code>是单节点是否复用的第一判断条件(第二判断条件是<code>type</code>是否改变).
<ul>
<li>如果<code>key</code>不同, 其他条件是完全不看的</li>
</ul>
</li>
<li>在新建节点时, <code>key</code>随着<code>element</code>对象被传入<code>fiber</code>的构造函数.</li>
</ol>
<p>所以到这里才是<code>key</code>的最核心作用, 是调和函数中, 针对单节点是否可以复用的<code>第一判断条件</code>.</p>
<p>另外我们可以得到, <code>fiber.key</code>是<code>reactElement.key</code>的拷贝, 他们是完全相等的(包括<code>null</code>默认值).</p>
<h3 data-id="heading-5">多节点</h3>
<p>继续查看多节点相关的逻辑:</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildrenArray</span>(<span class="hljs-params">
    returnFiber: Fiber,
    currentFirstChild: Fiber | <span class="hljs-literal">null</span>,
    newChildren: <span class="hljs-built_in">Array</span><*>,
    lanes: Lanes,
  </span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;

    <span class="hljs-keyword">if</span> (__DEV__) &#123;
      <span class="hljs-comment">// First, validate keys.</span>
      <span class="hljs-keyword">let</span> knownKeys = <span class="hljs-literal">null</span>;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < newChildren.length; i++) &#123;
        <span class="hljs-keyword">const</span> child = newChildren[i];
        <span class="hljs-comment">// 1. 在dev环境下, 执行warnOnInvalidKey. </span>
        <span class="hljs-comment">//  - 如果没有设置key, 会警告提示, 希望能显示设置key</span>
        <span class="hljs-comment">//  - 如果key重复, 会错误提示.</span>
        knownKeys = warnOnInvalidKey(child, knownKeys, returnFiber);
      &#125;
    &#125;

    <span class="hljs-keyword">let</span> resultingFirstChild: Fiber | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">let</span> previousNewFiber: Fiber | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;

    <span class="hljs-keyword">let</span> oldFiber = currentFirstChild;
    <span class="hljs-keyword">let</span> lastPlacedIndex = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> newIdx = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> nextOldFiber = <span class="hljs-literal">null</span>;
    <span class="hljs-comment">// 第一次循环: 只会在更新阶段发生</span>
    <span class="hljs-keyword">for</span> (; oldFiber !== <span class="hljs-literal">null</span> && newIdx < newChildren.length; newIdx++) &#123;
      <span class="hljs-keyword">if</span> (oldFiber.index > newIdx) &#123;
        nextOldFiber = oldFiber;
        oldFiber = <span class="hljs-literal">null</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        nextOldFiber = oldFiber.sibling;
      &#125;
      <span class="hljs-comment">// 1. 调用updateSlot, 处理公共序列中的fiber</span>
      <span class="hljs-keyword">const</span> newFiber = updateSlot(
        returnFiber,
        oldFiber,
        newChildren[newIdx],
        lanes,
      );
    &#125;

    <span class="hljs-comment">// 第二次循环</span>
    <span class="hljs-keyword">if</span> (oldFiber === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;
        <span class="hljs-comment">// 2. 调用createChild直接创建新fiber</span>
        <span class="hljs-keyword">const</span> newFiber = createChild(returnFiber, newChildren[newIdx], lanes);
      &#125;
      <span class="hljs-keyword">return</span> resultingFirstChild;
    &#125;

    <span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;
      <span class="hljs-comment">// 3. 调用updateFromMap处理非公共序列中的fiber</span>
      <span class="hljs-keyword">const</span> newFiber = updateFromMap(
        existingChildren,
        returnFiber,
        newIdx,
        newChildren[newIdx],
        lanes,
      );
    &#125;

    <span class="hljs-keyword">return</span> resultingFirstChild;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>reconcileChildrenArray</code>中, 有3处调用与<code>fiber</code>有关(当然顺便就和<code>key</code>有关了), 它们分布是:</p>
<ol>
<li>
<p><code>updateSlot</code></p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateSlot</span>(<span class="hljs-params">
      returnFiber: Fiber,
      oldFiber: Fiber | <span class="hljs-literal">null</span>,
      newChild: any,
      lanes: Lanes,
    </span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;
      <span class="hljs-keyword">const</span> key = oldFiber !== <span class="hljs-literal">null</span> ? oldFiber.key : <span class="hljs-literal">null</span>;

      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> newChild === <span class="hljs-string">'object'</span> && newChild !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">switch</span> (newChild.$$typeof) &#123;
          <span class="hljs-keyword">case</span> REACT_ELEMENT_TYPE: &#123;
            <span class="hljs-comment">//重点: key用于是否复用的第一判断条件</span>
            <span class="hljs-keyword">if</span> (newChild.key === key) &#123;
              <span class="hljs-keyword">return</span> updateElement(returnFiber, oldFiber, newChild, lanes);
            &#125; <span class="hljs-keyword">else</span> &#123;
              <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
            &#125;
          &#125;
        &#125;
      &#125;

      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>createChild</code></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createChild</span>(<span class="hljs-params">
        returnFiber: Fiber,
        newChild: any,
        lanes: Lanes,
      </span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> newChild === <span class="hljs-string">'object'</span> && newChild !== <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-keyword">switch</span> (newChild.$$typeof) &#123;
            <span class="hljs-keyword">case</span> REACT_ELEMENT_TYPE: &#123;
              <span class="hljs-comment">// 重点: 调用构造函数进行创建</span>
              <span class="hljs-keyword">const</span> created = createFiberFromElement(
                newChild,
                returnFiber.mode,
                lanes,
              );
              <span class="hljs-keyword">return</span> created;
            &#125;
          &#125;
        &#125;

        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>updateFromMap</code></p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateFromMap</span>(<span class="hljs-params">
      existingChildren: <span class="hljs-built_in">Map</span><string | number, Fiber>,
      returnFiber: Fiber,
      newIdx: number,
      newChild: any,
      lanes: Lanes,
    </span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;

      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> newChild === <span class="hljs-string">'object'</span> && newChild !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">switch</span> (newChild.$$typeof) &#123;
          <span class="hljs-keyword">case</span> REACT_ELEMENT_TYPE: &#123;
            <span class="hljs-comment">//重点: key用于是否复用的第一判断条件</span>
            <span class="hljs-keyword">const</span> matchedFiber =
              existingChildren.get(
                newChild.key === <span class="hljs-literal">null</span> ? newIdx : newChild.key,
              ) || <span class="hljs-literal">null</span>;
            <span class="hljs-keyword">return</span> updateElement(returnFiber, matchedFiber, newChild, lanes);
          &#125;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>其中, 与key相关的重点都在注释中说明了, 需要注意的是<code>updateFromMap</code>这是第二次循环中对于非公共序列的解析, 如果<code>reactElement</code>没有显示设置key, 也就是其中<code>newChild.key === null</code>, 这时候, 会用<code>index</code>进行查找.</p>
<p>所以在多节点情况下, <code>key</code>任然是用于是否复用的第一判断条件, 如果<code>key</code>不同是肯定不会复用的.</p>
<h2 data-id="heading-6">总结</h2>
<p>本节从源码的角度, 分别从<code>reactElement对象</code>和<code>fiber对象</code>2个视角进行展开, 分析<code>key</code>在react内核中的使用情况. 最终在调和函数<code>reconcilerChildren</code>中, <code>key</code>得到了最终的应用, 作为<code>节点复用</code>的第一判断条件.</p></div>  
</div>
            