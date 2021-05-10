
---
title: '探索React异步解决方案之redux-saga'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed48cf0c147644409c10c2ba62fd3268~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 09 May 2021 18:43:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed48cf0c147644409c10c2ba62fd3268~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.redux-saga是什么？</h3>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed48cf0c147644409c10c2ba62fd3268~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20201229144723252" loading="lazy" referrerpolicy="no-referrer">
<blockquote>
<p><code>redux-saga</code> is a library that aims to make application side effects (i.e. asynchronous things like data fetching and impure things like accessing the browser cache) easier to manage, more efficient to execute, easy to test, and better at handling failures.</p>
</blockquote>
<p>顾名思义saga与redux相关，redux-saga是一个以redux中间件形式存在的一个库，主要是为了更优雅地 <strong>管理</strong> Redux 应用程序中的 <strong>副作用（Side Effects）</strong>，执行更高效，<strong>测试更简单</strong>，在处理故障时更容易。同样的，从logo也可以看出saga于redux的关系。</p>
<p>关于saga的由来，它出自康奈尔大学的一篇论文（<a href="http://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf" target="_blank" rel="nofollow noopener noreferrer">链接</a>），是为了解决分布式系统中的长时运行事务(LLT)的数据一致性的问题。</p>
<h3 data-id="heading-1">2.什么是SideEffects?</h3>
<blockquote>
<p>Side effects are the most common way that a program interacts with the outside world (people, filesystems, other computers on networks).</p>
</blockquote>
<p>映射在 Javascript 程序中，Side Effects 主要指的就是：<strong>异步网络请求</strong>、<strong>本地读取 localStorage/Cookie</strong> 等外界操作：</p>
<blockquote>
<p>Asynchronous things like <strong>data fetching</strong> and impure things like <strong>accessing the browser cache</strong></p>
</blockquote>
<p>在 Web 应用，侧重点在于 Side Effects 的<strong>优雅管理（manage）</strong>，而不是 <strong>消除（eliminate）</strong>。</p>
<h3 data-id="heading-2">3.saga与thunk有什么不同？</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89eb069dca9c40d8a42febb96fd97212~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20201130161733674" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，比较了saga与thunk的包体积大小，二者相差<strong>10倍</strong>之多。</p>
<p>无论是redux-thunk也好还是redux-saga也好，都是redux的中间件。而redux作为主体，为每个中间件，提供了统一格式，下发getState、dispatch，以及调用dispatch，收集action。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//compose.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span>(<span class="hljs-params">..funcs</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (funcs.length === <span class="hljs-number">0</span>) &#123;
    retyrb arg => arg
  &#125;
  
  <span class="hljs-keyword">if</span> (funcs.length === <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> funcs[<span class="hljs-number">0</span>]
  &#125;
  
  <span class="hljs-keyword">return</span> funcs.reduce(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> a(b(...args)))
&#125;

<span class="hljs-comment">//applyMiddleware.js</span>


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyMiddleware</span>(<span class="hljs-params">...middlewares</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">createStore</span>) =></span> <span class="hljs-function">(<span class="hljs-params">reducer, preloaderState, enhancer</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> store = createStore(reducer, preloadedState, enhancer)
    <span class="hljs-keyword">let</span> dispatch = store.dispatch
    <span class="hljs-keyword">let</span> chain = []
    
    <span class="hljs-keyword">const</span> middlewareAPI = &#123;
      <span class="hljs-attr">getState</span>: store.getState,
      <span class="hljs-attr">diapatch</span>: <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> dispatch(action)
    &#125;
    chain = middlewares.map(<span class="hljs-function"><span class="hljs-params">middleware</span> =></span> middleware(middlewareAPI))
    dispatch = compose(...chain)(store.dispatch)
    
    <span class="hljs-keyword">return</span> &#123;
      ...store,
      dispatch
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，我们先再来看看thunk函数，在阮大大的文章中有介绍到thunk函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">m</span>)</span>&#123;
  <span class="hljs-keyword">return</span> m * <span class="hljs-number">2</span>;     
&#125;

f(x + <span class="hljs-number">5</span>);

<span class="hljs-comment">// 等同于</span>

<span class="hljs-keyword">var</span> thunk = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> x + <span class="hljs-number">5</span>;
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">thunk</span>)</span>&#123;
  <span class="hljs-keyword">return</span> thunk() * <span class="hljs-number">2</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译器的"传名调用"实现，往往是将参数放到一个临时函数之中，再将这个临时函数传入函数体。这个临时函数就叫做 Thunk 函数。<strong>在 JavaScript 语言中，Thunk 函数替换的不是表达式，而是多参数函数，将其替换成单参数的版本，且只接受回调函数作为参数。</strong></p>
<p>然后我们再来看看thunk的源码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createThunkMiddleware</span>(<span class="hljs-params">extraArgument</span>) </span>&#123;
  <span class="hljs-comment">//dispath,可以用来dispatch新的action</span>
  <span class="hljs-comment">//getState,可以用于访问当前的state</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">&#123;dispatch, getState&#125;</span>) =></span> <span class="hljs-function">(<span class="hljs-params">next</span>) =></span> <span class="hljs-function">(<span class="hljs-params">action</span>) =></span>  &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> action === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-keyword">return</span> action(dispatch, getState, extraArgument);
    &#125;
    
    <span class="hljs-keyword">return</span> next(action);
  &#125;;
&#125;

<span class="hljs-keyword">const</span> thunk = createThunkMiddleware();
thunk.withExtraArgument = createThunkMiddleware;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>redux-thunk是个中间件，去监控传入系统中的每一个<code>action</code>，如果是个函数的话，那么它就会调用那个函数。这就是<code>redux-thunk</code>的职责。redux-thunk 选择以 middleware 的形式来增强 redux store 的 dispatch 方法（即：支持了 <code>dispatch(function)</code>），从而在拥有了异步获取数据能力的同时，又可以进一步将数据获取相关的业务逻辑 从 View 层分离出去。</p>
<p>接着来看看redux-saga，saga模式是以命令/答复的形式与各个saga之间进行通讯，当接收到指令时会执行对应的saga，如图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448a9636eee442eab4f1302c4f1652b2~tplv-k3u1fbpfcp-zoom-1.image" alt="Command/Orchestration flow" loading="lazy" referrerpolicy="no-referrer"></p>
<p>saga模式将各个服务隔离开，采用集中分布式事务的编排，能够避免服务之间的循环依赖并有利于测试。同时减少了参与者的复杂性，因为他们只需要执行/回复命令。但是，saga会产生很多无用的action.type。</p>
<p>综上，redux-thunk与redux-saga都是redux的中间件，但是他们的设计思想不同，因此他们的使用方法也不同，首先来看redux-thunk的写法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// action.js</span>
<span class="hljs-comment">// ---------</span>
<span class="hljs-comment">// actionCreator(e.g. fetchData) 返回 function</span>
<span class="hljs-comment">// function 中包含了业务数据请求代码逻辑</span>
<span class="hljs-comment">// 以回调的方式，分别处理请求成功和请求失败的情况</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fetchData</span>(<span class="hljs-params">someValue</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">dispatch, getState</span>) =></span> &#123;
    myAjaxLib.post(<span class="hljs-string">"/someEndpoint"</span>, &#123; <span class="hljs-attr">data</span>: someValue &#125;)
      .then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"REQUEST_SUCCEEDED"</span>, <span class="hljs-attr">payload</span>: response &#125;)
        .catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"REQUEST_FAILED"</span>, <span class="hljs-attr">error</span>: error &#125;);
  &#125;;
&#125;


<span class="hljs-comment">// component.js</span>
<span class="hljs-comment">// ------------</span>
<span class="hljs-comment">// View 层 dispatch(fn) 触发异步请求</span>
<span class="hljs-comment">// 这里省略部分代码</span>
<span class="hljs-built_in">this</span>.props.dispatch(fetchData(&#123; <span class="hljs-attr">hello</span>: <span class="hljs-string">'saga'</span> &#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看redux-saga的写法，以及架构图：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// saga.js</span>
<span class="hljs-comment">// -------</span>
<span class="hljs-comment">// worker saga</span>
<span class="hljs-comment">// 它是一个 generator function</span>
<span class="hljs-comment">// fn 中同样包含了业务数据请求代码逻辑</span>
<span class="hljs-comment">// 但是代码的执行逻辑：看似同步 (synchronous-looking)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">fetchData</span>(<span class="hljs-params">action</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">payload</span>: &#123; someValue &#125; &#125; = action;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">yield</span> call(myAjaxLib.post, <span class="hljs-string">"/someEndpoint"</span>, &#123; <span class="hljs-attr">data</span>: someValue &#125;);
    <span class="hljs-keyword">yield</span> put(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"REQUEST_SUCCEEDED"</span>, <span class="hljs-attr">payload</span>: response &#125;);
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-keyword">yield</span> put(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"REQUEST_FAILED"</span>, <span class="hljs-attr">error</span>: error &#125;);
  &#125;
&#125;

<span class="hljs-comment">// watcher saga</span>
<span class="hljs-comment">// 监听每一次 dispatch(action)               </span>
<span class="hljs-comment">// 如果 action.type === 'REQUEST'，那么执行 fetchData</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">watchFetchData</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> takeEvery(<span class="hljs-string">'REQUEST'</span>, fetchData);
&#125;


<span class="hljs-comment">// component.js</span>
<span class="hljs-comment">// -------</span>
<span class="hljs-comment">// View 层 dispatch(action) 触发异步请求 </span>
<span class="hljs-comment">// 这里的 action 依然可以是一个 plain object</span>
<span class="hljs-built_in">this</span>.props.dispatch(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'REQUEST'</span>,
  <span class="hljs-attr">payload</span>: &#123;
    <span class="hljs-attr">someValue</span>: &#123; <span class="hljs-attr">hello</span>: <span class="hljs-string">'saga'</span> &#125;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4031686352b454e92c7af7f5fffe247~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>综上可以看出，redux-saga相较于redux-thunk有这几点不同</p>
<p>1.数据获取相关的业务逻辑被转移到单独的saga.js中，不再是参杂在action.js或component.js中。</p>
<p>2.每一个saga都是一个generator function，代码采用同步书写的方式来处理异步逻辑，代码变得更易读。</p>
<h3 data-id="heading-3">4.学习saga使用</h3>
<p>saga总共提供了两个<strong>MiddlewareAPI</strong>，为createSagaMiddleware、middleware.run。</p>
<p>createSagaMiddleware(options): 创建一个 Redux middleware，并将 Sagas 连接到 Redux Store。其中options支持的选项有(可不提供)：</p>
<ul>
<li>
<p>sagaMontior：用于接收middleware传递的监视事件。</p>
</li>
<li>
<p>emmiter：用于从redux向redux-saga进给actions</p>
</li>
<li>
<p>logger：自定义日志方法（默认情况下，middleware会把所有的错误和警告记录到控制台中）。</p>
</li>
<li>
<p>onError：当提供该方法时，middleware将带着Sagas中未被捕获的错误调用它。</p>
</li>
</ul>
<p>middleware.run(saga, ...args): 动态地运行 saga。只能用于在 applyMiddleware 阶段之后执行Saga，其中args为提供给saga的参数。</p>
<p>在安装完所有依赖后，首先将store 与saga的关联，并在最后去执行rootsaga。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createStore, applyMiddleware &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>;
<span class="hljs-keyword">import</span> createSagaMiddleware <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-saga'</span>;

<span class="hljs-keyword">import</span> rootSaga <span class="hljs-keyword">from</span> <span class="hljs-string">'./sagas'</span>
<span class="hljs-keyword">import</span> rootReducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./reducers'</span>

<span class="hljs-keyword">const</span> sgagMiddleware = createSagaMiddleware();

<span class="hljs-keyword">const</span> enhancer = applyMiddleware(sagaMiddleware);

<span class="hljs-keyword">const</span> store = createStore(rootReducer, enhancer);

<span class="hljs-comment">//执行rootSaga，通常是程序的初始化操作。</span>
sagaMiddleWare.run(rootSaga);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，再介绍saga中比较重要的几个概念，分别为：Task、Channel、Buffer、SagaMonitor。</p>
<h5 data-id="heading-4">1.Task</h5>
<p>Task 接口指定了通过 <code>fork</code>，<code>middleare.run</code> 或 <code>runSaga</code> 运行 Saga 的结果，并提供了相应的函数方法。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abf783318d034264921f823ef94ffa60~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20201223112205449" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8972241d4ccf47c3969213507e240c7b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20201223112119677" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-5">2.Channel</h5>
<p>channel 是用于在任务间发送和接收消息的对象。在被感兴趣的接收者请求之前，来自发送者的消息将被放入（put）队列；在信息可用之前，已注册的接收者将被放入队列。</p>
<p>Channel 接口定义了 3 个方法：<code>take</code>，<code>put</code> 和 <code>close</code></p>
<p><code>Channel.take(callback):</code> 用于注册一个 taker。</p>
<p><code>Channel.put(message):</code> 用于在 buffer 上放入消息。</p>
<p><code>Channel.flush(callback):</code> 用于从 channel 中提取所有被缓存的消息。</p>
<p><code>Channel.close():</code> 关闭 channel，意味着不再允许做放入操作。</p>
<h5 data-id="heading-6">3.Buffer</h5>
<p>用于为 channel 实现缓存策略。Buffer 接口定义了 3 个方法：<code>isEmpty</code>，<code>put</code> 和 <code>take</code></p>
<ul>
<li><code>isEmpty()</code>: 如果缓存中没有消息则返回。每当注册了新的 taker 时，channel 都会调用该方法。</li>
<li><code>put(message)</code>: 用于往缓存中放入新的消息。请注意，缓存可以选择不存储消息。（例如，一个 dropping buffer 可以丢弃超过给定限制的任何新消息）</li>
<li><code>take()</code>：用于检索任何被缓存的消息。请注意，此方法的行为必须与 <code>isEmpty</code> 一致。</li>
</ul>
<h5 data-id="heading-7">4.SagaMonitor</h5>
<p>用于由 middleware 发起监视（monitor）事件。实际上，middleware 发起 5 个事件：</p>
<ul>
<li>当一个 effect 被触发时（通过 <code>yield someEffect</code>），middleware 调用 <code>sagaMonitor.effectTriggered</code></li>
<li>如果该 effect 成功地被 resolve，则 middleware 调用 <code>sagaMonitor.effectResolved</code></li>
<li>如果该 effect 因一个错误被 reject，则 middleware 调用 <code>sagaMonitor.effectRejected</code></li>
<li>如果该 effect 被取消，则 middleware 调用 <code>sagaMonitor.effectCancelled</code></li>
<li>最后，当 Redux action 被发起时，middleware 调用 <code>sagaMonitor.actionDispatched</code></li>
</ul>
<p>接着再来介绍redux-saga中的Effect创建器，在redux-saga中主要通过effect来维护，关于Effect的描述如下：</p>
<blockquote>
<p>An effect is a plain JavaScript Object containing some instructions to be executed by the saga middleware.</p>
</blockquote>
<p>effect 本质上是一个普通对象，包含着一些指令信息，这些指令最终会被 saga middleware 解释并执行（实际上是一个发布订阅模式）。源码解析可参考文章（<a href="https://juejin.cn/post/6885223002703822855#heading-5%EF%BC%89" target="_blank">juejin.cn/post/688522…</a></p>
<p>以take为例，take是一个Effect创建器，用以创建Effect，源码如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48a6e662b76743558199d0fdc26ccf77~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20201223111205002" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c64ebd8b477140be8f341958fb7f47cf~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20201223111034645" loading="lazy" referrerpolicy="no-referrer"></p>
<p>官方解释：</p>
<ul>
<li>以下每个Effect创建函数都会返回一个普通 Javascript 对象（plain JavaScript object），并且不会执行任何其它操作。</li>
<li>执行是由 middleware 在上述迭代过程中进行的。</li>
<li>middleware 会检查每个 Effect 的描述信息，并进行相应的操作</li>
</ul>
<p>接下去简单解释一下各个Effect创建器以及Effect组合器、辅助函数的作用：</p>
<p>Take: 创建一个 Effect 描述信息，用来命令 middleware 在 Store 上等待指定的 action。 在发起与 <code>pattern</code> 匹配的 action 之前，Generator 将暂停。</p>
<p>Put: 创建一个 Effect 描述信息，用来命令 middleware 向 Store 发起一个 action。 这个 effect 是非阻塞型的，并且所有向下游抛出的错误（例如在 reducer 中），都不会冒泡回到 saga 当中。</p>
<p>Call: 创建一个 Effect 描述信息，用来命令 middleware 以参数 <code>args</code> 调用函数 <code>fn</code> 。</p>
<p>Apply: 类似Call。</p>
<p>Fork: 创建一个 Effect 描述信息，用来命令 middleware 以 <strong>非阻塞调用</strong> 的形式执行 <code>fn</code>。</p>
<p>Spawn: 与fork类似，但创建的是被分离的任务。被分离的任务与其父级任务保持独立。</p>
<p>Join: 创建一个 Effect 描述信息，用来命令 middleware 等待之前的一个分叉任务的结果。</p>
<p>Cancel:创建一个 Effect，用以取消任务。</p>
<p>Select: 创建一个 Effect，用来命令 middleware 在当前 Store 的 state 上调用指定的选择器（即返回 selector(getState(), ...args) 的结果）。</p>
<p>ActionChannel: 创建一个 Effect，用来命令 middleware 通过一个事件 channel 对匹配 <code>pattern</code> 的 action 进行排序。</p>
<p>Flush: 创建一个 Effect，用来命令 middleware 从 channel 中冲除所有被缓存的数据。被冲除的数据会返回至 saga，这样便可以在需要的时候再次被利用。</p>
<p>Cancelled: 创建一个 Effect，用来命令 middleware 返回该 generator 是否已经被取消。</p>
<p>setContext: 创建一个 effect，用来命令 middleware 更新其自身的上下文。</p>
<p>getContext: 创建一个 effect，用来命令 middleware 返回 saga 的上下文中的一个特定属性。</p>
<h5 data-id="heading-8">Effect组合器</h5>
<p>Race: 创建一个 Effect 描述信息，用来命令 middleware 在多个 Effect 间运行 竞赛（Race）（与 Promise.race([...]) 的行为类似）。</p>
<p>All: 创建一个 Effect 描述信息，用来命令 middleware 并行地运行多个 Effect，并等待它们全部完成。这是与标准的 Promise#all 相当对应的 API。</p>
<h5 data-id="heading-9">Saga辅助函数</h5>
<p>TakeEvery: 在发起（dispatch）到 Store 并且匹配 pattern 的每一个 action 上派生一个 saga。</p>
<p>TakeLatest: 在发起到 Store 并且匹配 pattern 的每一个 action 上派生一个 saga。并自动取消之前所有已经启动但仍在执行中的 saga 任务。</p>
<p>TakeLeading: 在发起到 Store 并且匹配 pattern 的每一个 action 上派生一个 saga。 它将在派生一次任务之后阻塞，直到派生的 saga 完成，然后又再次开始监听指定的 pattern。</p>
<p>Throttle: 在发起到 Store 并且匹配 pattern 的一个 action 上派生一个 saga。 它在派生一次任务之后，仍然将新传入的 action 接收到底层的 buffer 中，至多保留（最近的）一个。但与此同时，它在 ms 毫秒内将暂停派生新的任务 —— 这也就是它被命名为节流阀（throttle）的原因。其用途，是在处理任务时，无视给定的时长内新传入的 action。</p>
<h3 data-id="heading-10">5.Redux-Saga测试</h3>
<p>由于redux-saga将每个副作用细化到一个较小的维度，并使各个服务之间的耦合性较小。因此非常利于进行单元测试，案例如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">callApi</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">const</span> someValue = <span class="hljs-keyword">yield</span> select(somethingFromState)
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">yield</span> call(myApi, url, someValue)
    <span class="hljs-keyword">yield</span> put(success(result.json()));
    <span class="hljs-keyword">return</span> result.status;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-keyword">yield</span> put(error(e));
    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> dispatched = [];

<span class="hljs-keyword">const</span> saga = runSaga(&#123;
  <span class="hljs-attr">dispatch</span>: <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> dispatched.push(action),
  <span class="hljs-attr">getState</span>: <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'test'</span> &#125;),
&#125;, callApi, <span class="hljs-string">'http://url'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> sinon <span class="hljs-keyword">from</span> <span class="hljs-string">'sinon'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> api <span class="hljs-keyword">from</span> <span class="hljs-string">'./api'</span>;

test(<span class="hljs-string">'callApi'</span>, <span class="hljs-keyword">async</span> (assert) => &#123;
  <span class="hljs-keyword">const</span> dispatched = [];
  sinon.stub(api, <span class="hljs-string">'myApi'</span>).callsFake(<span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">json</span>: <span class="hljs-function">() =></span> (&#123;
      <span class="hljs-attr">some</span>: <span class="hljs-string">'value'</span>
    &#125;)
  &#125;));
  <span class="hljs-keyword">const</span> url = <span class="hljs-string">'http://url'</span>;
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> runSaga(&#123;
    <span class="hljs-attr">dispatch</span>: <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> dispatched.push(action),
    <span class="hljs-attr">getState</span>: <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">state</span>: <span class="hljs-string">'test'</span> &#125;),
  &#125;, callApi, url).done;

  assert.true(myApi.calledWith(url, somethingFromState(&#123; <span class="hljs-attr">state</span>: <span class="hljs-string">'test'</span> &#125;)));
  assert.deepEqual(dispatched, [success(&#123; <span class="hljs-attr">some</span>: <span class="hljs-string">'value'</span> &#125;)]);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后再推荐两个，阅读官方文档后觉得比较好的小技巧的使用。</p>
<h3 data-id="heading-11">6.Redux-Saga使用技巧</h3>
<h5 data-id="heading-12">1.ajax重试</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; call, put, take, delay, delay &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-saga/effects'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">updateApi</span>(<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> apiResponse = <span class="hljs-keyword">yield</span> call (apiRequest, &#123; data &#125;)
      <span class="hljs-keyword">return</span> apiResponse;
    &#125; <span class="hljs-keyword">catch</span>(error) &#123;
      <span class="hljs-keyword">yield</span> put(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'UPDATE_RETRY'</span>,
        error
      &#125;)
      <span class="hljs-keyword">yield</span> delay(<span class="hljs-number">2000</span>)
    &#125;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">updateResource</span>(<span class="hljs-params">&#123; data &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> apiResponse = <span class="hljs-keyword">yield</span> call(updateApi, data);
  <span class="hljs-keyword">yield</span> put(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'UPDATE_SUCCESS'</span>,
    <span class="hljs-attr">payload</span>: apiResponse.body,
  &#125;);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">watchUpdateResource</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> takeLatest(<span class="hljs-string">'UPDATE_START'</span>, updateResource);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">2.撤销</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; take, put, call, spawn, race, delay &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-saga/effects'</span>
<span class="hljs-keyword">import</span> &#123; updateThreadApi, actions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'somewhere'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">onArchive</span>(<span class="hljs-params">action</span>) </span>&#123;
  
  <span class="hljs-keyword">const</span> &#123; threadId &#125; = action
  <span class="hljs-keyword">const</span> undoId =<span class="hljs-string">`UNDO_ARCHIVE_<span class="hljs-subst">$&#123;threadId&#125;</span>`</span>
  
  <span class="hljs-keyword">const</span> thread = &#123; <span class="hljs-attr">id</span>: threadId, <span class="hljs-attr">archived</span>: <span class="hljs-literal">true</span>&#125;
  
  <span class="hljs-keyword">yield</span> put(actions.showUndo(undoId))
  
  <span class="hljs-keyword">yield</span> put(actions.updateThread(thread))
  
  <span class="hljs-keyword">const</span> &#123; undo, archive &#125; = <span class="hljs-keyword">yield</span> race(&#123;
    <span class="hljs-attr">undo</span>: take(<span class="hljs-function"><span class="hljs-params">action</span> =></span> action.type === <span class="hljs-string">'UNDO'</span> && action.undoId === undoId),
    <span class="hljs-attr">archive</span>: delay(<span class="hljs-number">5000</span>)
  &#125;)
  
  <span class="hljs-keyword">yield</span> put(actions.hideUndo(undoId))
  
  <span class="hljs-keyword">if</span> (undo) &#123;
    <span class="hljs-keyword">yield</span> put(actions.updateThread(&#123; <span class="hljs-attr">id</span>: threadId, <span class="hljs-attr">archived</span>: <span class="hljs-literal">false</span>&#125;))
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (archive) &#123;
    <span class="hljs-keyword">yield</span> call(updateThreadApi,thread)
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-keyword">const</span> action = <span class="hljs-keyword">yield</span> take(<span class="hljs-string">`ARCHIVE_THREAD`</span>)
    <span class="hljs-keyword">yield</span> spawn(onArchive, action)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">参考文章：</h5>
<p>1.<a href="https://zhuanlan.zhihu.com/p/35437092" target="_blank" rel="nofollow noopener noreferrer">Redux-Saga 漫谈</a></p>
<p>2.<a href="https://blog.couchbase.com/saga-pattern-implement-business-transactions-using-microservices-part-2/" target="_blank" rel="nofollow noopener noreferrer">Saga Pattern</a></p>
<p>3.<a href="https://redux-saga-in-chinese.js.org/" target="_blank" rel="nofollow noopener noreferrer">Redux-Saga官方文档</a></p>
<p>4.<a href="https://juejin.cn/post/6844903984038150152#heading-4" target="_blank">Why saga</a></p>
<p>5.<a href="https://juejin.cn/post/6885223002703822855#heading-5" target="_blank">手写Redux-Saga源码</a></p></div>  
</div>
            