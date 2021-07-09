
---
title: 'Redux原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53f87103689744ee9bd72f11a4f8e130~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 01:04:22 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53f87103689744ee9bd72f11a4f8e130~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53f87103689744ee9bd72f11a4f8e130~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文会讲Redux 架构，包含基本概念的介绍和用法，以及redux原理。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs" ref="nofollow noopener noreferrer">github.com/reduxjs</a></p>
<h1 data-id="heading-0">你可能不需要 Redux</h1>
<p>首先明确一点，Redux 是一个有用的架构，但不是非用不可。
曾经有人说过这样一句话。</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 如果你不知道是否需要 Redux，那就是不需要它。</li>
<li class="task-list-item"><input type="checkbox" disabled> 只有遇到（React）实在解决不了的问题，你才需要 Redux 。</li>
</ul>
<p>简单说，如果你的UI层非常简单，没有很多互动，Redux 就是不必要的，用了反而增加复杂性。</p>
<ul>
<li>用户的使用方式非常简单</li>
<li>用户之间没有协作</li>
<li>不需要与服务器大量交互，也没有使用 WebSocket</li>
<li>视图层（View）只从单一来源获取数据</li>
</ul>
<p>如果：</p>
<ul>
<li>用户的使用方式复杂</li>
<li>不同身份的用户有不同的使用方式（比如普通用户和管理员）</li>
<li>多个用户之间可以协作</li>
<li>与服务器大量交互，或者使用了WebSocket</li>
<li>View要从多个来源获取数据</li>
</ul>
<p>上面这些情况才是 Redux 的适用场景：多交互、多数据源。</p>
<p>从组件角度看，如果你的应用有以下场景，可以考虑使用 Redux。</p>
<ul>
<li>某个组件的状态，需要共享</li>
<li>某个状态需要在任何地方都可以拿到</li>
<li>一个组件需要改变全局状态</li>
<li>一个组件需要改变另一个组件的状态</li>
</ul>
<p>另一方面，Redux 只是 Web 架构的一种解决方案，也可以选择其他方案。比如，如果是React，还可以使用Recoil。</p>
<h1 data-id="heading-1">设计思想</h1>
<p>（1）Web 应用是一个状态机，视图与状态是一一对应的。
（2）所有的状态，保存在一个对象里面。</p>
<h1 data-id="heading-2">基本概念和API</h1>
<h2 data-id="heading-3">store</h2>
<p>Store 就是保存数据的地方，你可以把它看成一个容器。整个应用只能有一个 Store。
Redux 提供createStore这个函数，用来生成 Store。</p>
<h2 data-id="heading-4">state</h2>
<p>Store对象包含所有数据。如果想得到某个时点的数据，就要对 Store 生成快照。这种时点的数据集合，就叫做 State。当前时刻的 State，可以通过store.getState()拿到。</p>
<p>Redux 规定， 一个 State 对应一个 View。只要 State 相同，View 就相同。你知道 State，就知道 View 是什么样，反之亦然。</p>
<h2 data-id="heading-5">action</h2>
<p>State 的变化，会导致 View 的变化。但是，用户接触不到 State，只能接触到 View。所以，State 的变化必须是 View 导致的。Action 就是 View 发出的通知，表示 State 应该要发生变化了。
Action 是一个对象。其中的type属性是必须的，表示 Action 的名称。其他属性可以自由设置，社区有一个规范可以参考。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> action = &#123;   
  <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD_TODO'</span>,   
  <span class="hljs-attr">payload</span>: <span class="hljs-string">'Learn Redux'</span> 
&#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以这样理解，Action 描述当前发生的事情。改变 State 的唯一办法，就是使用 Action。它会运送数据到 Store。</p>
<h2 data-id="heading-6">Action Creator</h2>
<p>View 要发送多少种消息，就会有多少种 Action。如果都手写，会很麻烦。可以定义一个函数来生成 Action，这个函数就叫 Action Creator。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ADD_TODO = <span class="hljs-string">'添加 TODO'</span>; 

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addTodo</span>(<span class="hljs-params">text</span>) </span>&#123;   
  <span class="hljs-keyword">return</span> &#123;     
    <span class="hljs-attr">type</span>: ADD_TODO,     
    text   
  &#125; &#125;；
  
<span class="hljs-keyword">const</span> action = addTodo(<span class="hljs-string">'Learn Redux'</span>); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，addTodo函数就是一个 Action Creator。</p>
<p><strong>思考：</strong>
上面的代码在书写上并没有减少多少代码，看上去好像没有什么用处。那上面的写法到底有什么好处呢？用上面的写法我们无需dispatch的时候每次都写action，达到了复用的效果，也会减少出错。</p>
<h2 data-id="heading-7">store.dispatch</h2>
<p>store.dispatch()是 View 发出 Action 的唯一方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>;
<span class="hljs-keyword">const</span> store = createStore(fn);

store.dispatch(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD_TODO'</span>,
  <span class="hljs-attr">payload</span>: <span class="hljs-string">'Learn Redux'</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">Reducer</h2>
<p>Store 收到 Action 以后，必须给出一个新的 State，这样 View 才会发生变化。这种 State 的计算过程就叫做 Reducer。
Reducer 是一个函数，它接受 Action 和当前 State 作为参数，返回一个新的 State。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> reducer = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">state, action</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">return</span> new_state;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整个应用的初始状态，可以作为 State 的默认值。下面是一个实际的例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> defaultState = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state = defaultState, action</span>) =></span> &#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'ADD'</span>:
      <span class="hljs-keyword">return</span> state + action.payload;
    <span class="hljs-keyword">default</span>: 
      <span class="hljs-keyword">return</span> state;
  &#125;
&#125;;

<span class="hljs-keyword">const</span> state = reducer(<span class="hljs-number">1</span>, &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD'</span>,
  <span class="hljs-attr">payload</span>: <span class="hljs-number">2</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，createStore接受 Reducer 作为参数，生成一个新的 Store。以后每当store.dispatch发送过来一个新的 Action，就会自动调用 Reducer，得到新的 State。</p>
<p>为什么这个函数叫做 Reducer 呢？因为它可以作为数组的reduce方法的参数。请看下面的例子，一系列 Action 对象按照顺序作为一个数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> actions = [
  &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD'</span>, <span class="hljs-attr">payload</span>: <span class="hljs-number">0</span> &#125;,
  &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD'</span>, <span class="hljs-attr">payload</span>: <span class="hljs-number">1</span> &#125;,
  &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD'</span>, <span class="hljs-attr">payload</span>: <span class="hljs-number">2</span> &#125;
];

<span class="hljs-keyword">const</span> total = actions.reduce(reducer, <span class="hljs-number">0</span>); <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果按照上面的解释可以帮助理解的话，那可以按照上面的去理解。如果别人问你reducer到底是什么呢？怎么用一句话准确描述出来reducer的作用呢？</p>
<p><strong>reducer定义了数据的更新规则。</strong></p>
<p><strong>那combineReducers是什么呢？</strong>
如果项目中的reducer很大，维护起来很不方便，可以把reducer拆分成子reducer，combineReducers就是把子reducer合成一个总的reducer。</p>
<h1 data-id="heading-9">原理</h1>
<h2 data-id="heading-10">createStore 和 combineReducers</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params">reducer, initialState</span>) </span>&#123;
    <span class="hljs-keyword">let</span> currentState = initialState;

    <span class="hljs-keyword">const</span> getState = <span class="hljs-function">() =></span> currentState;
    <span class="hljs-keyword">let</span> listeners = [];

    <span class="hljs-keyword">const</span> subscribe = <span class="hljs-function">(<span class="hljs-params">sub</span>) =></span> &#123;
        listeners.push(sub);

        <span class="hljs-comment">// 取消订阅</span>
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">let</span> index = listeners.findIndex(<span class="hljs-function">(<span class="hljs-params">s</span>) =></span> s === sub);
            <span class="hljs-keyword">if</span>(index !== -<span class="hljs-number">1</span>) &#123;
                listeners.splice(index, <span class="hljs-number">1</span>);
            &#125;
        &#125;
    &#125;

    <span class="hljs-keyword">const</span> dispatch = <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> newState = reducer(currentState, action);

        <span class="hljs-keyword">if</span>(newState !== currentState) &#123;
            currentState = newState;

            listeners.forEach(<span class="hljs-function">(<span class="hljs-params">sub</span>) =></span> &#123;
                sub && sub();
            &#125;);
        &#125;
    &#125;


    <span class="hljs-keyword">return</span> &#123;
        getState,
        dispatch,
        subscribe
    &#125;;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">combineReducers</span>(<span class="hljs-params">reducers</span>)</span>&#123;
    <span class="hljs-keyword">const</span> reducerKeys = <span class="hljs-built_in">Object</span>.keys(reducers);
    <span class="hljs-keyword">const</span> finalReducers = &#123;&#125;;

    <span class="hljs-comment">// 去除reducers中不是函数的属性</span>
    reducerKeys.forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> reducers[key] === <span class="hljs-string">'function'</span>) &#123;
            finalReducers[key] = reducers[key];
        &#125;
    &#125;);

    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">combination</span>(<span class="hljs-params">state, action</span>) </span>&#123;
        <span class="hljs-keyword">let</span> hasChanged = <span class="hljs-literal">false</span>;
        <span class="hljs-keyword">const</span> nextState = &#123;&#125;;

        <span class="hljs-built_in">Object</span>.keys(finalReducers).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> reducer = finalReducers[key];

            <span class="hljs-keyword">const</span> previousStateForKey = state[key];
            <span class="hljs-keyword">const</span> nextStateForKey = reducer(previousStateForKey, action);

            <span class="hljs-keyword">if</span>(nextStateForKey == <span class="hljs-literal">null</span>) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'When called with an action, the reducer returned undefined'</span>);
            &#125;

            nextState[key] = nextStateForKey;
            hasChanged = hasChanged || nextStateForKey !== previousStateForKey;
        &#125;);

        hasChanged = hasChanged || <span class="hljs-built_in">Object</span>.keys(state).length !== <span class="hljs-built_in">Object</span>.keys(nextState).length;

        <span class="hljs-keyword">return</span> hasChanged ? nextState : state;
    &#125;;;
&#125;

<span class="hljs-keyword">export</span> &#123;
    createStore,
    combineReducers
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">combineReducer的简洁实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> combineReducers = <span class="hljs-function"><span class="hljs-params">reducers</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">state = &#123;&#125;, action</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.keys(reducers).reduce(
      <span class="hljs-function">(<span class="hljs-params">nextState, key</span>) =></span> &#123;
        nextState[key] = reducers[key](state[key], action);
        <span class="hljs-keyword">return</span> nextState;
      &#125;,
      &#123;&#125; 
    );
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们实现了自己的redux，主要包含了createStore和combineReducers，那能不能使用起来呢？验证一些我们实现的是不是和真正的redux一样？</p>
<h2 data-id="heading-12">在html中使用</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.con</span>&#123;
            <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid green; 
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">20px</span>;
            <span class="hljs-attribute">min-height</span>: <span class="hljs-number">50px</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"con"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btnAdd"</span>></span>增加<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btnMinus"</span>></span>减少<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btnCancel"</span>></span>取消<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"span1"</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"con"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"msgInput"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>/></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btnMsg"</span>></span>改变<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"msg2"</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
        <span class="hljs-keyword">import</span> &#123; createStore, combineReducers &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./redux.js'</span>;

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">counterReducer</span>(<span class="hljs-params">state, action</span>)</span>&#123;
            <span class="hljs-keyword">switch</span>(action.type) &#123;
                <span class="hljs-keyword">case</span> <span class="hljs-string">'ADD'</span>:
                    <span class="hljs-keyword">return</span> &#123;
                        <span class="hljs-attr">counter</span>: state.counter + <span class="hljs-built_in">Number</span>(action.payload)
                    &#125;;
                <span class="hljs-keyword">case</span> <span class="hljs-string">'MINUS'</span>:
                    <span class="hljs-keyword">return</span> &#123;
                        <span class="hljs-attr">counter</span>: state.counter - <span class="hljs-built_in">Number</span>(action.payload)
                    &#125;;
                <span class="hljs-keyword">default</span>:
            &#125;

            <span class="hljs-keyword">return</span> state;
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">messageReducer</span>(<span class="hljs-params">state, action</span>)</span>&#123;
            <span class="hljs-keyword">switch</span>(action.type)&#123;
                <span class="hljs-keyword">case</span> <span class="hljs-string">'CHANGEMSG'</span>:
                    <span class="hljs-keyword">return</span> &#123;
                        <span class="hljs-attr">msg</span>: action.payload
                    &#125;;
                <span class="hljs-keyword">default</span>:
            &#125;

            <span class="hljs-keyword">return</span> state;
        &#125;

        <span class="hljs-keyword">const</span> reducer = combineReducers(&#123;
            <span class="hljs-attr">count</span>: counterReducer,
            <span class="hljs-attr">message</span>: messageReducer
        &#125;);
        <span class="hljs-keyword">const</span> store = createStore(reducer, &#123;
            <span class="hljs-attr">count</span>: &#123;
                <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
            &#125;,
            <span class="hljs-attr">message</span>: &#123;
                <span class="hljs-attr">msg</span>: <span class="hljs-string">''</span>
            &#125;
        &#125;);

        <span class="hljs-keyword">let</span> btnAdd = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btnAdd'</span>);
        <span class="hljs-keyword">let</span> btnMinus = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btnMinus'</span>);
        <span class="hljs-keyword">let</span> btnCancel = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btnCancel'</span>);
        <span class="hljs-keyword">let</span> btnMsg = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btnMsg'</span>);

        btnAdd.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            store.dispatch(&#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD'</span>,
                <span class="hljs-attr">payload</span>: <span class="hljs-number">1</span>
            &#125;);
        &#125;
        btnMinus.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            store.dispatch(&#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">'MINUS'</span>,
                <span class="hljs-attr">payload</span>: <span class="hljs-number">1</span>
            &#125;);
        &#125;
        btnCancel.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            unsubscribe();
        &#125;

        btnMsg.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">let</span> input = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#msgInput'</span>);

            <span class="hljs-keyword">if</span>(input.value) &#123;
                store.dispatch(&#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-string">'CHANGEMSG'</span>,
                    <span class="hljs-attr">payload</span>: input.value
                &#125;);
            &#125;
        &#125;
        

        <span class="hljs-keyword">const</span> unsubscribe = store.subscribe(<span class="hljs-function">() =></span> &#123;
            renderDOM();
        &#125;);

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderDOM</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">let</span> state = store.getState();
            <span class="hljs-built_in">console</span>.log(state);

            <span class="hljs-keyword">let</span> span1 = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#span1'</span>);
            span1.innerHTML = state.count.counter;

            <span class="hljs-keyword">let</span> msg = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#msg2'</span>);
            msg.innerHTML = state.message.msg;
        &#125;
        renderDOM();
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">在react中使用</h2>
<p>我们以react为例来使用我们自己的redux，实际上我们可以在任何javascript框架中使用我们自己的redux，这里只是以react为例。</p>
<p>redux/index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore, combineReducers &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./redux'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> countReducer = <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span> (action.type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'ADD'</span>:
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">count</span>: state.count + action.payload
            &#125;;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'MINUS'</span>:
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">count</span>: state.count - action.payload
            &#125;;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'RESET'</span>:
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
            &#125;;
        <span class="hljs-keyword">default</span>:
            <span class="hljs-keyword">return</span> state
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> msgReducer = <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span> (action.type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'CHANGE'</span>:
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">msg</span>: action.payload
            &#125;;
        <span class="hljs-keyword">default</span>:
            <span class="hljs-keyword">return</span> state
    &#125;
&#125;

<span class="hljs-keyword">const</span> reducer = combineReducers(&#123;
    <span class="hljs-attr">counter</span>: countReducer,
    <span class="hljs-attr">message</span>: msgReducer
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(reducer, &#123;
    <span class="hljs-attr">counter</span>: &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;,
    <span class="hljs-attr">message</span>: &#123;
        <span class="hljs-attr">msg</span>: <span class="hljs-string">''</span>
    &#125;
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>components/ReduxPage.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'../redux'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReduxPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
        <span class="hljs-built_in">super</span>(props);
    &#125;

    addBtnClick = <span class="hljs-function">()=></span>&#123;
        store.dispatch(&#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD'</span>,
            <span class="hljs-attr">payload</span>: <span class="hljs-number">1</span>
        &#125;);
    &#125;

    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span>&#123;
        store.subscribe(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.forceUpdate();
        &#125;);
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; count &#125; = store.getState().counter;
        
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">this.addBtnClick</span> &#125;></span>增加<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>components/ReduxPage2.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'../redux'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReduxPage2</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
        <span class="hljs-built_in">super</span>(props);

        <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">value</span>: <span class="hljs-string">''</span>
        &#125;;
    &#125;

    msgChange = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state.value) &#123;
            store.dispatch(&#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">'CHANGE'</span>,
                <span class="hljs-attr">payload</span>: <span class="hljs-built_in">this</span>.state.value
            &#125;);
        &#125;
    &#125;

    input = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(e.target.value) &#123;
            <span class="hljs-built_in">this</span>.setState(&#123;
                <span class="hljs-attr">value</span>: e.target.value
            &#125;);
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span>&#123;
        store.subscribe(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.forceUpdate();
        &#125;);
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; value &#125; = <span class="hljs-built_in">this</span>.state;
        <span class="hljs-keyword">const</span> &#123; msg &#125; = store.getState().message;

        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value&#125;</span> <span class="hljs-attr">onInput</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">this.input</span> &#125;/></span>
                    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">this.msgChange</span> &#125;></span>改变<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123; msg &#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>app.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> logo <span class="hljs-keyword">from</span> <span class="hljs-string">'./logo.svg'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./App.css'</span>;
<span class="hljs-keyword">import</span> ReduxPage <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/ReduxPage'</span>;
<span class="hljs-keyword">import</span> ReduxPage2 <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/ReduxPage2'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ReduxPage</span>/></span>
      <span class="hljs-tag"><<span class="hljs-name">ReduxPage2</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>bindActionCreators</strong>
实现比较简单，可以参考：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Fredux%2Fblob%2Fmaster%2Fsrc%2FbindActionCreators.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/redux/blob/master/src/bindActionCreators.ts" ref="nofollow noopener noreferrer">github.com/reduxjs/red…</a></p>
<p><strong>applyMiddleware 和 compose</strong>
实现稍微复杂一点，可以参考。会在我以后的文章中讲解它的实现。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Fredux%2Fblob%2Fmaster%2Fsrc%2FapplyMiddleware.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/redux/blob/master/src/applyMiddleware.ts" ref="nofollow noopener noreferrer">github.com/reduxjs/red…</a></p></div>  
</div>
            