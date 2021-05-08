
---
title: '进击的Redux'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1227'
author: 掘金
comments: false
date: Sat, 08 May 2021 02:33:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=1227'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>网上Redux入门教程很多，但是为啥这么使用，却百思不得解。今天写一篇关于Redux的文章，帮助大家了解Redux为啥这么写，以及内部做了啥。<br></p>
<h3 data-id="heading-0">目录：</h3>
<ul>
<li>types
<ul>
<li>actions.ts</li>
<li>middleware.ts</li>
<li>reducers.ts</li>
<li>store.ts</li>
</ul>
</li>
<li>utils
<ul>
<li>actionTypes.ts</li>
<li>formatProdErrorMessage.ts</li>
<li>isPlainObject.ts</li>
<li>kindOf.ts</li>
<li>symbol-observable.ts</li>
<li>warning.ts</li>
</ul>
</li>
<li>applyMiddleware.ts</li>
<li>bindActionCreators.ts</li>
<li>combineReducers.ts</li>
<li>compose.ts</li>
<li>createStore.ts</li>
<li>index.ts</li>
</ul>
<h3 data-id="heading-1"><a href="https://github.com/reduxjs/redux/blob/master/src/applyMiddleware.ts" target="_blank" rel="nofollow noopener noreferrer">applyMiddleware.ts</a></h3>
<p>将所有中间件合并成一个数组，然后依次执行，用法如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> store = applyMiddleware([ loggerMiddleware, thunkMiddleware, ...others ])(createStore)(reducer, preloadState)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyMiddleware</span> (<span class="hljs-params">...middlewares</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">createStore</span>) =></span> <span class="hljs-function">(<span class="hljs-params">reducer, preloadState</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> store = createStore(reducer, preloadState)
    <span class="hljs-keyword">let</span> dispatch = <span class="hljs-function">() =></span> &#123;&#125;
    <span class="hljs-keyword">const</span> middlewareAPI = &#123;
      <span class="hljs-attr">getState</span>: store.getState,
      <span class="hljs-attr">dispatch</span>: <span class="hljs-function">(<span class="hljs-params">action, ...args</span>) =></span> dispatch(action, ...args)
    &#125;
    <span class="hljs-keyword">const</span> chain = middlewares.map(<span class="hljs-function"><span class="hljs-params">middleware</span> =></span> middleware(middlewareAPI))
    <span class="hljs-comment">// compose 是 src 目录下的compose方法，暂时不用管</span>
    dispatch = compose(...chain)(store.dispatch)
    <span class="hljs-keyword">return</span> &#123;
       ...store,
       dispatch
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"><a href="https://github.com/reduxjs/redux/blob/master/src/bindActionCreators.ts" target="_blank" rel="nofollow noopener noreferrer">bindActionCreators.ts</a></h3>
<p>将一个或多个action和dispatch组合起来生成mapDispatchToProps需要生成的内容，目的就是简化书写，减轻开发负担。用法如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用前</span>
<span class="hljs-keyword">import</span> React, &#123; useCallback &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; createStore, bindActionCreators &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> &#123; Provider, connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>;

<span class="hljs-comment">// 子组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">&#123; msg, onClick &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> onUserClick = useCallback(<span class="hljs-function">() =></span> &#123;
    onClick(<span class="hljs-string">"我被点击了"</span>);
  &#125;, [onClick]);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onUserClick&#125;</span>></span>被点击了吗？ &#123;msg&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;

<span class="hljs-comment">// 让子组件使用redux</span>
<span class="hljs-keyword">const</span> ChildWrap = connect(
  <span class="hljs-function"><span class="hljs-params">state</span> =></span> (&#123; <span class="hljs-attr">msg</span>: state.msg &#125;),
  <span class="hljs-function"><span class="hljs-params">dispatch</span> =></span> (&#123;
    <span class="hljs-attr">onClick</span>: <span class="hljs-function"><span class="hljs-params">payload</span> =></span> dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"CLICK"</span>, payload &#125;)
  &#125;)
)(React.memo(Child));

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> store = createStore(<span class="hljs-function">(<span class="hljs-params">state = &#123;&#125;, action</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span> (action.type) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"CLICK"</span>:
        state = &#123; <span class="hljs-attr">msg</span>: action.payload &#125;;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">default</span>:
        state = &#123;&#125;;
        <span class="hljs-keyword">break</span>;
    &#125;
    <span class="hljs-keyword">return</span> state;
  &#125;);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ChildWrap</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
  );
&#125;

<span class="hljs-comment">// 使用后</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> actionCreators <span class="hljs-keyword">from</span> <span class="hljs-string">'./actionCreators'</span>

<span class="hljs-keyword">const</span> ChildWrap = connect(
  <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> (&#123; <span class="hljs-attr">msg</span>: state.msg &#125;),
  <span class="hljs-function">(<span class="hljs-params">dispatch, ownProps</span>) =></span> bindActionCreators(actionCreators, dispatch)
)(React.memo(Child));

<span class="hljs-comment">// actionCreators.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> onClick = <span class="hljs-function">(<span class="hljs-params">payload</span>) =></span> (&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">"CLICK"</span>,
  payload
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 批量处理action
 * <span class="hljs-doctag">@actionCreators <span class="hljs-type">&#123; Function | Object &#125;</span> </span>如果是多个action，则需要传入对象
 * <span class="hljs-doctag">@dispatch       <span class="hljs-type">&#123; Function &#125;</span>          </span>store的dispatch对象
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindActionCreators</span> (<span class="hljs-params">actionCreators, dispatch</span>) </span>&#123;
  <span class="hljs-comment">// 如果是单个函数</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> actionCreators === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">return</span> bindActionCreator(actionCreators, dispatch)
  &#125;
  <span class="hljs-keyword">const</span> boundActionCreators = &#123;&#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> actionCreators) &#123;
    <span class="hljs-keyword">const</span> actionCreator = actionCreators[key]
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> actionCreator === <span class="hljs-string">'funciton'</span>) &#123;
      boundActionCreators[key] = bindActionCreator(actionCreator, dispatch)
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> boundActionCreators
&#125;

<span class="hljs-comment">/**
 * 处理单个action
 * <span class="hljs-doctag">@param </span>actionCreators &#123; Function | Object &#125; 如果是多个action，则需要传入对象
 * <span class="hljs-doctag">@param </span>dispatch       &#123; Function &#125;          store的dispatch对象
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindActionCreator</span> (<span class="hljs-params">actionCreator, dispatch</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">this</span>, ...args</span>) </span>&#123;
    <span class="hljs-keyword">return</span> dispatch(actionCreator.bind(<span class="hljs-built_in">this</span>, ...args))
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3"><a href="https://github.com/reduxjs/redux/blob/master/src/combineReducers.ts" target="_blank" rel="nofollow noopener noreferrer">combineReducers.ts</a></h3>
<p>使reducer结合到一起。即将各个子reducer合并成一个大的reducer合并后的reducer可以调用各个子 reducer，并把它们返回的结果合并成一个state对象。<br>
参数: 一个Object对象，key为 reducerName 可以自定义，value为 reducer函数<br>
返回值： 调用所有传入的reducer,即传入参数对象的 value 值。返回和传入参数结构一致的state对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useCallback &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; createStore, combineReducers &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> &#123; Provider, connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; msg, onClick &#125; = props
  <span class="hljs-keyword">const</span> onUserClick = useCallback(<span class="hljs-function">() =></span> &#123;
    onClick(<span class="hljs-string">"sssss"</span>);
  &#125;, [onClick]);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onUserClick&#125;</span>></span>11111 &#123;msg&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;

<span class="hljs-keyword">const</span> ChildWrap = connect(
  <span class="hljs-comment">// 注意此处的state.reduce1对应combineReducer中写的key</span>
  <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> (&#123; <span class="hljs-attr">msg</span>: state.reducer1.msg &#125;),
  <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> (&#123;
    <span class="hljs-attr">onClick</span>: <span class="hljs-function">(<span class="hljs-params">payload</span>) =></span> dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"CLICK"</span>, payload &#125;)
  &#125;)
)(Child);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> reducer1 = <span class="hljs-function">(<span class="hljs-params">state = &#123;&#125;, action</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span> (action.type) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"CLICK"</span>:
        state = &#123; <span class="hljs-attr">msg</span>: action.payload &#125;;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">default</span>:
        state = &#123;&#125;;
        <span class="hljs-keyword">break</span>;
    &#125;
    <span class="hljs-keyword">return</span> state;
  &#125;;

  <span class="hljs-keyword">const</span> reducer2 = <span class="hljs-function">(<span class="hljs-params">state = &#123;&#125;, action</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span> (action.type) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"CLICK2"</span>:
        state = &#123; <span class="hljs-attr">msg</span>: action.payload &#125;;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">default</span>:
        state = &#123;&#125;;
        <span class="hljs-keyword">break</span>;
    &#125;
    <span class="hljs-keyword">return</span> state;
  &#125;;

  <span class="hljs-keyword">const</span> store = createStore(combineReducers(&#123; reducer1, reducer2 &#125;));

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ChildWrap</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">combineReducers</span> (<span class="hljs-params">reducers</span>) </span>&#123;
  <span class="hljs-keyword">const</span> reducerKeys = <span class="hljs-built_in">Object</span>.keys(reducers)
  <span class="hljs-keyword">const</span> finalReducers = &#123;&#125;
  <span class="hljs-comment">// 剔除reducer中非方法的内容</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < reducerKeys.length; i ++) &#123;
    <span class="hljs-keyword">const</span> key = reducerKeys[i]
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> reducers[key] === <span class="hljs-string">'function'</span>) &#123;
      finalReducers[key] = reducers[key]
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> finalReducerKeys = <span class="hljs-built_in">Object</span>.keys(finalReducers)
  <span class="hljs-comment">// 组装在一起，相当于一个大的reducer，入参也和reducer一致</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">combination</span> (<span class="hljs-params">state = &#123;&#125;, action</span>) </span>&#123;
    <span class="hljs-keyword">let</span> hasChanged = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">const</span> nextState = &#123;&#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < finalReducerKeys.length; i ++) &#123;
      <span class="hljs-keyword">const</span> key = finalReducerKeys[i]
      <span class="hljs-keyword">const</span> reducer = finalReducerKeys[key]
      <span class="hljs-keyword">const</span> previousStateForKey = state[key]
      <span class="hljs-keyword">let</span> nextStateForKey = reducer(previousStateForKey, action)
      nextState[key] = nextStateForKey
      hasChanged = hasChanged || nextStateForKey !== previousStateForKey
    &#125;
    hasChanged = hasChanged || finalReducerKeys.length !== <span class="hljs-built_in">Object</span>.keys(state).length
    <span class="hljs-keyword">return</span> hasChanged ? nextState : state
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4"><a href="https://github.com/reduxjs/redux/blob/master/src/compose.ts" target="_blank" rel="nofollow noopener noreferrer">compose.ts</a></h3>
<p>函数式编程里常用的组合函数，将多个函数组合成一个函数依次执行。个人认为这个函数是redux整个源码中最值得一看的代码，而且可以脱离redux中，在日常开发中使用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span> (<span class="hljs-params">...funcs</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (funcs.length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;&#125;
  &#125;
  <span class="hljs-keyword">if</span> (funcs.length === <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> funcs[<span class="hljs-number">0</span>]
  &#125;
  <span class="hljs-keyword">return</span> funcs.reduce(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> a(b(...args)))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><a href="https://github.com/reduxjs/redux/blob/master/src/createStore.ts" target="_blank" rel="nofollow noopener noreferrer">createStore.ts</a></h3>
<p>相信这个方法绝对是大家用redux最多的一个方法，直接上源码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 创建store的方法
 *
 * <span class="hljs-doctag">@param </span>reducer        纯函数，接收store和action，返回新store
 * <span class="hljs-doctag">@param </span>preloadedState 初始化的state值
 * <span class="hljs-doctag">@param </span>enhancer       store增强函数，类似于applyMiddleware
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span> (<span class="hljs-params">reducer, preloadedState, enhancer</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> preloadedState === <span class="hljs-string">'function'</span> && <span class="hljs-keyword">typeof</span> enhancer === <span class="hljs-string">'undefined'</span>) &#123;
    enhancer = preloadedState
    preloadedState = <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> enhancer !== <span class="hljs-string">'undefined'</span> && <span class="hljs-keyword">typeof</span> enhancer === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">return</span> enhancer(createStore)(reducer, preloadedState)
  &#125;

  <span class="hljs-keyword">let</span> currentState = preloadedState
  <span class="hljs-keyword">let</span> currentReducer = reducer
  <span class="hljs-keyword">let</span> currentListeners = []
  <span class="hljs-keyword">let</span> nextListeners = currentListeners
  <span class="hljs-keyword">let</span> isDispatching = <span class="hljs-literal">false</span>

  <span class="hljs-comment">/**
   * 生成currentListeners的浅层副本，使用时可以将nextListeners用作临时列表。
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ensureCanMutateNextListeners</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (currentListeners === nextListeners) &#123;
      nextListeners = currentListeners.splice()
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * 获取最新的状态
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getState</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> currentState
  &#125;

  <span class="hljs-comment">/**
   * 添加更改侦听器。它将在任何时候调用一个动作，并且状态树的某些部分可能已经更改。然后可以调
   * 用“getState()”来读取回调中的当前状态树。
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">subscribe</span> (<span class="hljs-params">listener</span>) </span>&#123;
    <span class="hljs-keyword">let</span> isSubscribed = <span class="hljs-literal">true</span>

    ensureCanMutateNextListeners()
    nextListeners.push(listener)
    
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unSubscribe</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (!isSubscribed) &#123;
        <span class="hljs-keyword">return</span>
      &#125;

      isSubscribed = <span class="hljs-literal">false</span>

      ensureCanMutateNextListeners()
      <span class="hljs-keyword">const</span> index = nextListeners.indexOf(listener)
      nextListeners.splice(index, <span class="hljs-number">1</span>)
      currentListeners = <span class="hljs-literal">null</span>
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * 派发事件，触发reducer改变state的值。这是唯一可以修改state值的方法
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span> (<span class="hljs-params">action</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> action.type === <span class="hljs-string">'undefined'</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(
        <span class="hljs-string">'Actions may not have an undefined "type" property. You may have misspelled an action type string constant.'</span>
      )
    &#125;
    <span class="hljs-keyword">if</span> (isDispatching) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Reducers may not dispatch actions.'</span>)
    &#125;
    <span class="hljs-keyword">try</span> &#123;
      isDispatching = <span class="hljs-literal">true</span>
      currentState = currentReducer(currentState, action)
    &#125; <span class="hljs-keyword">finally</span> &#123;
      isDispatching = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">const</span> listeners = (currentListeners = nextListeners)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < listeners.length; i ++) &#123;
      <span class="hljs-keyword">const</span> listener = listeners[i]
      listener()
    &#125;
    <span class="hljs-keyword">return</span> action
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observable</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> outerSubscribe = subscribe
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-function"><span class="hljs-title">subscribe</span>(<span class="hljs-params">observer: unknown</span>)</span> &#123;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observeState</span>(<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-keyword">const</span> observerAsObserver = observer <span class="hljs-keyword">as</span> Observer<S>
          <span class="hljs-keyword">if</span> (observerAsObserver.next) &#123;
            observerAsObserver.next(getState())
          &#125;
        &#125;

        observeState()
        <span class="hljs-keyword">const</span> unsubscribe = outerSubscribe(observeState)
        <span class="hljs-keyword">return</span> &#123; unsubscribe &#125;
      &#125;,

      [$$observable]() &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
      &#125;
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * 替换当前当前用于计算的reducer
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">replaceReducer</span> (<span class="hljs-params">nextReducer</span>) </span>&#123;
    currentReducer = nextReducer
    dispatch(&#123; <span class="hljs-attr">type</span>: ActionTypes.REPLACE &#125;)
    <span class="hljs-keyword">return</span> store
  &#125;

  <span class="hljs-comment">// 所以明白了，reducer中的switch的default开始会执行一次了吧</span>
  dispatch(&#123; <span class="hljs-attr">type</span>: ActionTypes.INIT &#125;)

  <span class="hljs-keyword">const</span> store = &#123;
    dispatch,
    subscribe,
    getState,
    replaceReducer,
    [$$observable]: observable
  &#125;
  <span class="hljs-keyword">return</span> store
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">index.ts</h3>
<p>导出上面的方法</p>
<h3 data-id="heading-7">types</h3>
<p>定义了整个项目中需要使用的interface和type，篇幅原因，不再详细说明，有兴趣可以<a href="https://github.com/reduxjs/redux/tree/master/src/types" target="_blank" rel="nofollow noopener noreferrer">查看源码</a></p>
<h3 data-id="heading-8">utils</h3>
<p>工具类方法，篇幅原因，不再详细说明，有兴趣可以<a href="https://github.com/reduxjs/redux/tree/master/src/utils" target="_blank" rel="nofollow noopener noreferrer">查看源码</a></p></div>  
</div>
            