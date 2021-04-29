
---
title: 'React-从源码开始（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7467'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 02:22:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=7467'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作为一名前端小白，会想起第一次debug React组件时的手足无措，在惊叹这个框架的奇妙之余也更加觊觎其中的道理。</p>
<h2 data-id="heading-0">万物伊始——react准备工作</h2>
<p>每个react的web应用想要展示到页面上的第一步都需要执行渲染函数<code>ReactDOM.createRoot(document.getElementById('root')).render(<App />)</code>
，而它都做了些什么呢？</p>
<p>首先我们看到的是<code>ReactDOM</code>调用的<code>createRoot</code>方法，它在react内部调用createRoot方法返回一个React容器对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRoot</span>(<span class="hljs-params">
  container: Container,
  options?: RootOptions,
</span>): <span class="hljs-title">RootType</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ReactDOMRoot(container, options);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数中的<code>container</code>，也就是我们通过<code>document.getElementById('root')</code>获取的dom对象，<code>options</code>这个参数，它主要用在服务端渲染流程中，所以现在为空。</p>
<p>再看，这个函数中返回的是ReactDOMRoot构造函数生成的对象，而<code>ReactDOMRoot</code>又是干什么呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ReactDOMRoot</span>(<span class="hljs-params">container: Container, options: <span class="hljs-keyword">void</span> | RootOptions</span>) </span>&#123;
  <span class="hljs-built_in">this</span>._internalRoot = createRootImpl(container, ConcurrentRoot, options);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它为我们创建的React容器对象的<code>_internalRoot</code>属性通过<code>createRootImpl</code>函数的返回值赋值，他又是做什么的呢。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRootImpl</span>(<span class="hljs-params">
  container: Container,
  tag: RootTag,
  options: <span class="hljs-keyword">void</span> | RootOptions,
</span>) </span>&#123;
  ...
  <span class="hljs-comment">// 创建FiberRoot对象</span>
  <span class="hljs-keyword">const</span> root = createContainer(container, tag, hydrate, hydrationCallbacks);
  <span class="hljs-comment">// 标记一下FiberRoot对象</span>
  markContainerAsRoot(root.current, container);
  <span class="hljs-comment">// 获取整个应用的挂在的那个元素</span>
  <span class="hljs-keyword">const</span> rootContainerElement =
    container.nodeType === COMMENT_NODE ? container.parentNode : container;
  <span class="hljs-comment">// 注册事件代理</span>
  listenToAllSupportedEvents(rootContainerElement);
  ...
  <span class="hljs-keyword">return</span> root;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先我们看到这个函数的参数由之前的两个变成了三个，中间的tag参数是用来标志react的工作模式。自从React16之后， react引入了Fiber，工作模式也由之前的一种变成两种，随之改变的是在react应用挂载时执行的渲染函数也由一种变成了三种。</p>
<pre><code class="hljs language-js copyable" lang="js">ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>， <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
ReactDOM.createBlockingRoot(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)).render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>)
ReactDOM.createRoot(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)).render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一种还是原始默认，其工作方式也是同步方式，而剩下两种则是使用新版的并行工作方式。
而它们之间就是通过刚才提到的tag参数进行区分的，而<code>createBlockingRoot</code>和<code>createRoot</code>之间借用官方的解释：</p>
<blockquote>
<p>对于较旧的代码库，concurrent 模式可能步子迈的太大。这就是我们在实验版本中提供“ blocking 模式”的原因。你可以通过使用 createBlockingRoot 代替 createRoot 尝试一下。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> type RootTag = <span class="hljs-number">0</span> | <span class="hljs-number">1</span> | <span class="hljs-number">2</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> LegacyRoot = <span class="hljs-number">0</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> BlockingRoot = <span class="hljs-number">1</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ConcurrentRoot = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入这个函数，最主要的就是做了两件事</p>
<ol>
<li>生成<code>FiberRoot</code>对象。</li>
<li>注册事件代理。</li>
</ol>
<p>我们先看第一步，通过调用<code>createContainer</code>函数生成<code>root</code>并最终返回这个<code>root</code>，这也就是<code>_internalRoot</code>的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createContainer</span>(<span class="hljs-params">
  containerInfo: Container,
  tag: RootTag,
  hydrate: boolean,
  hydrationCallbacks: <span class="hljs-literal">null</span> | SuspenseHydrationCallbacks,
</span>): <span class="hljs-title">OpaqueRoot</span> </span>&#123;
  <span class="hljs-comment">// 创建并返回FiberRoot</span>
  <span class="hljs-keyword">return</span> createFiberRoot(containerInfo, tag, hydrate, hydrationCallbacks);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>createContainer</code>中又调用了<code>createFiberRoot</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createFiberRoot</span>(<span class="hljs-params">
  containerInfo: any,
  tag: RootTag,
  hydrate: boolean,
  hydrationCallbacks: <span class="hljs-literal">null</span> | SuspenseHydrationCallbacks,
</span>): <span class="hljs-title">FiberRoot</span> </span>&#123;
  <span class="hljs-comment">// 实例化一个FiberRoot对象</span>
  <span class="hljs-keyword">const</span> root: FiberRoot = (<span class="hljs-keyword">new</span> FiberRootNode(containerInfo, tag, hydrate): any);
  ...
  <span class="hljs-comment">// 创建一个当前组件树的根节点HostRootFiber</span>
  <span class="hljs-keyword">const</span> uninitializedFiber = createHostRootFiber(tag);
  <span class="hljs-comment">// 将这个HostRootFiber对象作为FiberRoot对象current属性的引用</span>
  root.current = uninitializedFiber;
  <span class="hljs-comment">// 这个FiberRoot对象的stateNode属性指向容器对象</span>
  uninitializedFiber.stateNode = root;
  <span class="hljs-comment">// 初始化更新队列</span>
  initializeUpdateQueue(uninitializedFiber);
  <span class="hljs-keyword">return</span> root;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，调用<code>FiberRootNode</code>函数实例化<code>root</code>对象，这个函数会返回一个<code>RootNode</code>对象，赋值给root并最终也返回它。</p>
<p>而之后调用<code>createHostRootFiber</code>创建<code>HostRootFiber</code>对象，赋值给<code>uninitializedFiber</code>
这里的<code>createHostRootFiber</code>函数最终返回的是一个<code>Fiber</code>对象。而传给<code>createHostRootFiber</code>的参数是当前工作模式的标志。</p>
<p>此时将<code>uninitializedFiber</code>赋值到<code>root.current</code>属性上，作为当前的组件树的根节点。</p>
<p>接下来初始化更新队列，调用<code>initializeUpdateQueue</code>函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initializeUpdateQueue</span><<span class="hljs-title">State</span>>(<span class="hljs-params">fiber: Fiber</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">const</span> queue: UpdateQueue<State> = &#123;
    <span class="hljs-attr">baseState</span>: fiber.memoizedState,
    <span class="hljs-attr">firstBaseUpdate</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">lastBaseUpdate</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">shared</span>: &#123;
      <span class="hljs-attr">pending</span>: <span class="hljs-literal">null</span>,
    &#125;,
    <span class="hljs-attr">effects</span>: <span class="hljs-literal">null</span>,
  &#125;;
  <span class="hljs-comment">// 为fiber节点也就是当前组件树的根节点的updateQueue属性赋初始值</span>
  fiber.updateQueue = queue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后返回<code>root</code>，返回并结束我们在<code>createRootImpl</code>中的第一步生成<code>FiberRoot</code>对象。</p>
<p>接下来执行<code>listenToAllSupportedEvents</code>，参数为依然是通过<code>document.getElementById('root')</code>获取的dom对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> listeningMarker =
  <span class="hljs-string">'_reactListening'</span> +
  <span class="hljs-built_in">Math</span>.random()
    .toString(<span class="hljs-number">36</span>)
    .slice(<span class="hljs-number">2</span>);

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">listenToAllSupportedEvents</span>(<span class="hljs-params">rootContainerElement: EventTarget</span>) </span>&#123;
  <span class="hljs-comment">// 当(rootContainerElement: any)[listeningMarker]不为true时向下执行</span>
  <span class="hljs-keyword">if</span> ((rootContainerElement: any)[listeningMarker]) &#123;
    <span class="hljs-comment">// 优化：在相同的portal容器或者根节点只迭代一次</span>
    <span class="hljs-comment">// 一旦移除这个标记，我们也许还可以删除一些用于懒加载的簿记图。</span>
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-comment">// 设置(rootContainerElement: any)[listeningMarker]为true，确保不再重复执行。</span>
  (rootContainerElement: any)[listeningMarker] = <span class="hljs-literal">true</span>;
  <span class="hljs-comment">// 为所有的原生事件添加监听</span>
  allNativeEvents.forEach(<span class="hljs-function"><span class="hljs-params">domEventName</span> =></span> &#123;
    <span class="hljs-comment">// 判断当前原生事件是否在不需要代理监听的事件列表里，如果不在则执行</span>
    <span class="hljs-keyword">if</span> (!nonDelegatedEvents.has(domEventName)) &#123;
      listenToNativeEvent(
        domEventName,
        <span class="hljs-literal">false</span>,
        ((rootContainerElement: any): Element),
        <span class="hljs-literal">null</span>,
      );
    &#125;
    listenToNativeEvent(
      domEventName,
      <span class="hljs-literal">true</span>,
      ((rootContainerElement: any): Element),
      <span class="hljs-literal">null</span>,
    );
  &#125;);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">listenToNativeEvent</span>(<span class="hljs-params">
  domEventName: DOMEventName,
  isCapturePhaseListener: boolean,
  rootContainerElement: EventTarget,
  targetElement: Element | <span class="hljs-literal">null</span>,
  eventSystemFlags?: EventSystemFlags = <span class="hljs-number">0</span>,
</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">let</span> target = rootContainerElement;
  <span class="hljs-comment">// selectionchange需要附加到文档上，否则它将无法捕获仅直接在文档上触发的传入事件。</span>
  <span class="hljs-keyword">if</span> (
    domEventName === <span class="hljs-string">'selectionchange'</span> &&
    (rootContainerElement: any).nodeType !== DOCUMENT_NODE
  ) &#123;
    target = (rootContainerElement: any).ownerDocument;
  &#125;
  <span class="hljs-comment">// If the event can be delegated (or is capture phase), we can</span>
  <span class="hljs-comment">// register it to the root container. Otherwise, we should</span>
  <span class="hljs-comment">// register the event to the target element and mark it as</span>
  <span class="hljs-comment">// a non-delegated event.</span>
  <span class="hljs-keyword">if</span> (
    targetElement !== <span class="hljs-literal">null</span> &&
    !isCapturePhaseListener &&
    nonDelegatedEvents.has(domEventName)
  ) &#123;
    <span class="hljs-comment">// 对于所有未委派的事件，除了滚动之外，还将其事件侦听器附加到其事件触发的各个元</span>
    <span class="hljs-comment">// 素上。 这意味着我们可以跳过此步骤，因为以前已经添加了事件侦听器。 但是，我们对滚</span>
    <span class="hljs-comment">// 动事件进行了特殊处理，因为现实是任何元素都可以滚动。</span>
    <span class="hljs-keyword">if</span> (domEventName !== <span class="hljs-string">'scroll'</span>) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;
    eventSystemFlags |= IS_NON_DELEGATED;
    target = targetElement;
  &#125;
  <span class="hljs-comment">// 创建或者获取事件代理集合</span>
  <span class="hljs-keyword">const</span> listenerSet = getEventListenerSet(target);
  <span class="hljs-comment">// 创建代理事件名称并标记这个事件是捕获还是冒泡</span>
  <span class="hljs-keyword">const</span> listenerSetKey = getListenerSetKey(
    domEventName,
    isCapturePhaseListener,
  );
  <span class="hljs-comment">// 如果是新增事件或者更新事件</span>
  <span class="hljs-keyword">if</span> (!listenerSet.has(listenerSetKey)) &#123;
    <span class="hljs-keyword">if</span> (isCapturePhaseListener) &#123;
      eventSystemFlags |= IS_CAPTURE_PHASE;
    &#125;
    <span class="hljs-comment">// 添加绑定事件</span>
    addTrappedEventListener(
      target,
      domEventName,
      eventSystemFlags,
      isCapturePhaseListener,
    );
    <span class="hljs-comment">// 将新增或更新事件添加到事件集合中</span>
    listenerSet.add(listenerSetKey);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，我们完成了万里长征的第一步，react在渲染更新前的准备工作</p>
<ol>
<li>初始化根节点</li>
<li>初始化事件代理</li>
</ol>
<p>万事开头难，然后中间难，最后会更难。每天挪一小步，光就会出现。</p></div>  
</div>
            