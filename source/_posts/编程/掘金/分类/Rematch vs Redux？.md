
---
title: 'Rematch vs Redux？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6644efdffaf9424db3fe1f2301ef71b2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 04:50:52 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6644efdffaf9424db3fe1f2301ef71b2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>看完 <a href="https://juejin.cn/post/6961006341347344421" target="_blank">【译】重新设计 Redux </a>后，这篇文章会继续聊聊 Rematch 和 Redux 的区别。我将分别用 Redux 和 Rematch 实现一个简易的计数器（Counter），其中 Redux 实现版本中对异步的处理分别使用 <a href="https://github.com/reduxjs/redux-thunk" target="_blank" rel="nofollow noopener noreferrer">redux-thunk</a> 和 <a href="https://github.com/redux-saga/redux-saga" target="_blank" rel="nofollow noopener noreferrer">redux-saga</a>。通过这个例子，我们来比较 Rematch 和 Redux 的差异，以及 Rematch 的优点在哪（减少了哪些学习成本，减少了哪些代码等等），最后，来讲讲 Rematch 如何包装 Redux，来做到平滑过渡的，这将涉及到 Rematch 的代码架构，我把它分成了几个部分，在后面的文章中会逐一讲解。</p>
<h2 data-id="heading-0">文章大纲</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6644efdffaf9424db3fe1f2301ef71b2~tplv-k3u1fbpfcp-watermark.image" alt="文章结构思维导图" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">简易计数器（Counter）案例</h2>
<p>下面我会用 Redux 和 Rematch 分别实现一个 React 版本的简易计数器，计数器包含增加、减少和异步增加功能。</p>
<p>页面截图如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5e4c4f3948414cb513e1ec459dae18~tplv-k3u1fbpfcp-watermark.image" alt="页面截图" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">Redux 实现</h3>
<p>纯 Redux 实现版本中，对于异步增加功能的实现，一种方案使用了 <a href="https://github.com/reduxjs/redux-thunk" target="_blank" rel="nofollow noopener noreferrer">redux-thunk</a>，另一种使用了 <a href="https://github.com/redux-saga/redux-saga" target="_blank" rel="nofollow noopener noreferrer">redux-saga</a>。</p>
<p>目录结构很简单：</p>
<pre><code class="copyable">src
|—— components
|  |—— Counter.js
|—— reducers
|  |—— index.js
|—— index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>components/Counter.js</code> 代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> PropTypes <span class="hljs-keyword">from</span> <span class="hljs-string">"prop-types"</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Counter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; value, onIncrement, onDecrement, onIncrementAsync &#125; = <span class="hljs-built_in">this</span>.props;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>
        Clicked: &#123;value&#125; times <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onIncrement&#125;</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>&#123;" "&#125;
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onDecrement&#125;</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>&#123;" "&#125;
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onIncrementAsync&#125;</span>></span>Increment async<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    );
  &#125;
&#125;

Counter.propTypes = &#123;
  <span class="hljs-attr">value</span>: PropTypes.number.isRequired,
  <span class="hljs-attr">onIncrement</span>: PropTypes.func.isRequired,
  <span class="hljs-attr">onDecrement</span>: PropTypes.func.isRequired,
  <span class="hljs-attr">onIncrementAsync</span>: PropTypes.func.isRequired,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Counter;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>reducers/index.js</code> 代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (state = <span class="hljs-number">0</span>, action) => &#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"INCREMENT"</span>:
      <span class="hljs-keyword">return</span> state + <span class="hljs-number">1</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"DECREMENT"</span>:
      <span class="hljs-keyword">return</span> state - <span class="hljs-number">1</span>;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> state;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 <code>index.js</code> 中的代码，由于包含异步逻辑，因此按使用的方案不同，代码也有差异，下面分别说明。</p>
<h4 data-id="heading-3">异步基于 redux-thunk</h4>
<p><a href="https://codesandbox.io/s/counter-demo-using-redux-thunk-257hc" target="_blank" rel="nofollow noopener noreferrer">完整代码请点击</a></p>
<p>如果异步使用 redux-thunk，<code>index.js</code> 中代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> &#123; applyMiddleware, createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> Counter <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/Counter"</span>;
<span class="hljs-keyword">import</span> counter <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers"</span>;
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">"redux-thunk"</span>;

<span class="hljs-keyword">const</span> store = createStore(counter, applyMiddleware(thunk));
<span class="hljs-keyword">const</span> rootEl = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fakeAsyncLogic</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">rs</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(rs, <span class="hljs-number">1000</span>);
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeAsyncIncrementAction</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">dispatch</span>) </span>&#123;
    <span class="hljs-keyword">await</span> fakeAsyncLogic();
    dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"INCREMENT"</span> &#125;);
  &#125;;
&#125;

<span class="hljs-keyword">const</span> render = <span class="hljs-function">() =></span>
  ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Counter</span>
      <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;store.getState()&#125;</span>
      <span class="hljs-attr">onIncrement</span>=<span class="hljs-string">&#123;()</span> =></span> store.dispatch(&#123; type: "INCREMENT" &#125;)&#125;
      onDecrement=&#123;() => store.dispatch(&#123; type: "DECREMENT" &#125;)&#125;
      onIncrementAsync=&#123;() => store.dispatch(makeAsyncIncrementAction())&#125;
    /></span>,
    rootEl
  );

render();
store.subscribe(render);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用了 thunk 中间件以后，<code>dispatch()</code> 可以接收函数作为参数，然后 redux store 会将 <code>dispatch</code> 和 <code>getState</code> 作为参数传入该函数中，这样一来，如果该函数是异步函数，则可以实现异步派发 action。</p>
<h4 data-id="heading-4">异步基于 redux-saga</h4>
<p><a href="https://codesandbox.io/s/counter-demo-using-redux-saga-5c6uu" target="_blank" rel="nofollow noopener noreferrer">完整代码请点击</a></p>
<p>如果异步使用 redux-saga，<code>index.js</code> 中代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> &#123; createStore, applyMiddleware &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> createSagaMiddleware <span class="hljs-keyword">from</span> <span class="hljs-string">"redux-saga"</span>;
<span class="hljs-keyword">import</span> Counter <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/Counter"</span>;
<span class="hljs-keyword">import</span> counter <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers"</span>;
<span class="hljs-keyword">import</span> defaultSaga <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers/saga"</span>;

<span class="hljs-keyword">const</span> sagaMiddleware = createSagaMiddleware();

<span class="hljs-keyword">const</span> store = createStore(counter, applyMiddleware(sagaMiddleware));
<span class="hljs-keyword">const</span> rootEl = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>);

sagaMiddleware.run(defaultSaga);

<span class="hljs-keyword">const</span> render = <span class="hljs-function">() =></span>
  ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Counter</span>
      <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;store.getState()&#125;</span>
      <span class="hljs-attr">onIncrement</span>=<span class="hljs-string">&#123;()</span> =></span> store.dispatch(&#123; type: "INCREMENT" &#125;)&#125;
      onDecrement=&#123;() => store.dispatch(&#123; type: "DECREMENT" &#125;)&#125;
      onIncrementAsync=&#123;() => store.dispatch(&#123; type: "INCREMENT_ASYNC" &#125;)&#125;
    /></span>,
    rootEl
  );

render();
store.subscribe(render);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了中间件配置代码那里的不同，saga 不是像 redux-thunk 那样派发一个函数作为 action，而是需要定义一些 saga 的异步逻辑（使用 saga 自带的一些异步 API），因此，<code>src/reducers</code> 目录下增加一个 <code>saga.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; takeEvery, call, put &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux-saga/effects"</span>;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fakeAsyncLogic</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">rs</span>) =></span> <span class="hljs-built_in">setTimeout</span>(rs, <span class="hljs-number">1000</span>));
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">increamentAsync</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> call(fakeAsyncLogic);
  <span class="hljs-keyword">yield</span> put(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"INCREMENT"</span> &#125;);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">defaultSaga</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> takeEvery(<span class="hljs-string">"INCREMENT_ASYNC"</span>, increamentAsync);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>saga 使用<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator" target="_blank" rel="nofollow noopener noreferrer">迭代器函数（generator）</a>来更加精细地控制异步流。上面代码导出了一个默认 saga 函数，<code>takeEvery("INCREMENT_ASYNC", increamentAsync)</code> 表示监听所有 <code>action.type</code> 为 <code>INCREMENT_ASYNC</code> 的 action，一旦监听到，执行 <code>increamentAsync()</code> 函数，在该函数中，使用 <code>call(fakeAsyncLogic)</code> 模拟异步调用，然后使用 <code>put(&#123; type: "INCREMENT" &#125;)</code> 来派发一个 action，最终这个 action 会使得 reducer 执行。</p>
<h3 data-id="heading-5">Rematch 实现</h3>
<p><a href="https://codesandbox.io/s/counter-demo-using-rematch-3u2nf" target="_blank" rel="nofollow noopener noreferrer">完整代码请点击</a></p>
<p>Rematch 中没有单独的 reducers，reducer 都归属于一个数据结构叫做 model，因此目录结构稍有不同（将 <code>reducers</code> 换为 <code>models</code>）：</p>
<pre><code class="copyable">src
|—— components
|  |—— Counter.js
|—— models
|  |—— index.js
|—— index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Counter.js</code> 中代码不变，<code>models/index.js</code> 中代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fakeAsyncLogic</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">rs</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(rs, <span class="hljs-number">1000</span>);
  &#125;);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> count = &#123;
  <span class="hljs-attr">state</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-attr">increment</span>: <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> state + <span class="hljs-number">1</span>;
    &#125;,
    <span class="hljs-attr">decrement</span>: <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> state - <span class="hljs-number">1</span>;
    &#125;,
  &#125;,
  <span class="hljs-attr">effects</span>: <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> (&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">incrementAsync</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">await</span> fakeAsyncLogic();
      dispatch.count.increment();
    &#125;,
  &#125;),
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，我们定义了一个叫做 <code>count</code> 的 model，其中包含了 <code>state</code>，<code>reducers</code> 以及 <code>effectes</code>，<code>state</code> 是归属于该 model 的数据，相当于 redux 中 reducer 函数的第一个参数（或者其返回值）。<code>reducers</code> 等同于 redux reducer，而最后的 <code>effects</code> 则是一些有副作用的逻辑（例如异步的接口调用等等）。</p>
<p>最后是 <code>index.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; init &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@rematch/core"</span>;
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> Counter <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/Counter"</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> models <span class="hljs-keyword">from</span> <span class="hljs-string">"./models"</span>;

<span class="hljs-keyword">const</span> store = init(&#123; models &#125;);
<span class="hljs-comment">// const store = createStore(counter, applyMiddleware(thunk));</span>
<span class="hljs-keyword">const</span> rootEl = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>);

<span class="hljs-keyword">const</span> render = <span class="hljs-function">() =></span>
  ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Counter</span>
      <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;store.getState().count&#125;</span>
      <span class="hljs-attr">onIncrement</span>=<span class="hljs-string">&#123;store.dispatch.count.increment&#125;</span>
      <span class="hljs-attr">onDecrement</span>=<span class="hljs-string">&#123;()</span> =></span> store.dispatch(&#123; type: "count/decrement" &#125;)&#125;
      onIncrementAsync=&#123;() => store.dispatch(&#123; type: "count/incrementAsync" &#125;)&#125;
    /></span>,
    rootEl
  );

render();
store.subscribe(render);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时 <code>store</code> 不再需要用 redux 的 API <code>createStore</code> 创建，而是使用 rematch 的 <code>init</code>。这里还需要注意 2 点：</p>
<ol>
<li>此时 <code>store.getState()</code> 返回的不再是一个数值，而是 <code>&#123; count: number &#125;</code></li>
<li><code>store.dispatch</code> 不仅仅是一个函数（维持 redux 调用方式），同时支持了 <code>dispatch.modelName.xxx</code> 这样调用一个 reducer 或者 effect。不过需要注意的是，<code>action.type</code> 此时为 <code>modelName/reducerName</code> 或者 <code>modelName/effectName</code> 这种形式</li>
</ol>
<p>前面提到过，rematch 中的最小组成单元就是一个 model。因此上述的改动也是为了兼容 model 这种形式。</p>
<h2 data-id="heading-6">rematch vs redux</h2>
<p>通过上面的例子，可以看出两者有如下几点不同：</p>
<ol>
<li>如果使用 redux，异步需要单独使用中间件，例如 thunk 或 saga。而 rematch 中可以直接使用 ES 的 <code>async/await</code> 异步语法来实现异步派发 action。</li>
<li>redux 中没有 model 的概念，如果 state 结构复杂，可以使用 <a href="https://redux.js.org/recipes/structuring-reducers/initializing-state#combined-reducers" target="_blank" rel="nofollow noopener noreferrer">combineReducers</a> 来合并不同的 reducer，同时形成一个类似的 state 结构。而 rematch 原生支持。</li>
<li>redux 的 <code>store.dispatch</code> 就是一个函数。但 rematch 中保留了函数功能，同时提供了链式调用的方式。</li>
</ol>
<p>由于上面例子比较简单，因此差异不多。更多差异可以参考<a href="https://juejin.cn/post/6961006341347344421#heading-7" target="_blank">【译】重新设计 Redux</a>。这里再提两点比较常见的差异：</p>
<ol>
<li>redux 更多的使用了函数式编程的思想，例如 store 初始化时，其提供了一个工具函数 <a href="https://redux.js.org/api/compose" target="_blank" rel="nofollow noopener noreferrer"><code>compose</code></a> 用于组合 store enhancer。</li>
<li>简化的 reducer，主要包括省略了 <code>action.type</code> 常量定义，省略了 reducer 中的 <code>switch/case</code> 分支判断，因此 rematch 中的 model 的一个 reducer 就相当于一个 <code>case</code> 分支，其 name 就相当于 <code>action.type</code>。</li>
</ol>
<p>个人觉得，rematch 优于 redux 的主要在于三个地方：</p>
<ol>
<li>更”合理“的数据结构设计，rematch 使用 model 的概念，整合了 state, reducer 以及 effect，这种整合在前端开发中非常实用，例如可以针对不同的页面路由设计不同的 model。</li>
<li>更简洁的 API 设计，redux 中使用的函数组合配置方法，对于不熟悉函数式编程的开发者来说，一开始可能比较困惑，而 rematch 使用的是基于对象的配置项，更加易于上手。</li>
<li>更少的代码。</li>
</ol>
<ul>
<li>移除了 redux 中大量的 <code>action.type</code> 常量以及分支判断</li>
<li>原生语法支持异步，无需使用中间件。使用 saga 有一定学习成本，使用 thunk，派发的 action 类型各异，也会产生一定困惑</li>
</ul>
<p>除此之外，rematch 还提供了插件机制，除了社区开发的很多插件，我们还可以进行定制开发，关于插件会在后面文章中详细介绍。</p>
<h2 data-id="heading-7">rematch 的代码结构</h2>
<p>我们知道，rematch 其实只是基于 redux 的包装，它把 redux 复杂的语法变得简单化了：</p>
<blockquote>
<p>Rematch is Redux best practices without the boilerplate.</p>
</blockquote>
<p>正因为如此，它顶层还是 redux，并没有减弱 redux 的功能。那么，rematch 是如何做到的，他是如何设计的？我接下来会基于 rematch v1.4.0（rematch v1 的最后一个版本）来讲解 rematch 核心代码结构。</p>
<blockquote>
<p>注：译者参与推动了 rematch v2 的更新，会在后面专门写一篇文章介绍 rematch v1 到 v2 的变化。此处使用 v1，是因为代码逻辑并无根本变化，v1 更易于阅读和理解，而 v2 风格变化较大。</p>
</blockquote>
<p>先来看看 rematch v1.4.0 的代码目录结构：</p>
<pre><code class="copyable">...
plugins
|—— ...
|—— loading
|—— immer
|—— select
src
|—— plugins
|  |—— dispatch.ts
|  |—— effects.ts
|—— typings
|  |—— index.ts
|—— utils
|  |—— deprecate.ts
|  |—— isListener.ts
|  |—— mergeConfig.ts
|  |—— validate.ts
|—— index.ts
|—— pluginFactory.ts
|—— redux.ts
|—— rematch.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据以上结构，我将 rematch 拆分为如下几个组成部分：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ef9b5db03d84cbabdbf61310e703cb8~tplv-k3u1fbpfcp-watermark.image" alt="rematch 组成" loading="lazy" referrerpolicy="no-referrer"></p>
<p>rematch 由 core 和 plugin 组成，其中 core 分为两部分，分别是 rematch 类和 <code>redux.ts</code> 这个文件，前者为 rematch 核心源码，后者主要包含 reducer 合并的一些代码，用于创建 redux store。</p>
<p>而 plugin 是 rematch 提供的插件机制，用于增强 rematch 的功能，主要代码定义在 plugin factory 中。rematch core 中包含了两个核心的 plugin，分别是 dispatch 和 effect，dispatch 插件可以增强 <code>store.dispatch</code> 功能，让其支持链式调用。而 effect 插件主要是用于支持 <code>async/await</code> 这种异步模式。除了这两个 plugin，rematch 团队还开发了其他的第三方插件，例如 loading, select 等等，集成了异步请求 loading 状态和 selector。</p>
<p>接下来，我会分别讲解这些部分，拆细一点，就是 rematch core，plugin factory && core plugins，3rd party plugins，一共 3 篇文章。3 篇文章结束后，我还会写 2 篇文章，其中一篇为 rematch v1 到 v2 升级的变化，另一篇介绍 rematch 类型系统（这是升级到 v2 带来的最大变化）以及这个类型系统残留的一些问题和难点，与大家探讨。</p>
<p>敬请期待！</p></div>  
</div>
            