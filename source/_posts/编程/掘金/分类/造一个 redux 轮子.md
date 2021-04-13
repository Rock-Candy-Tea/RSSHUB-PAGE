
---
title: '造一个 redux 轮子'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8708739b76f94e7e86b6825c7efac988~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Apr 2021 18:23:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8708739b76f94e7e86b6825c7efac988~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8708739b76f94e7e86b6825c7efac988~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>文章源码：<a href="https://github.com/Haixiang6123/my-redux" target="_blank" rel="nofollow noopener noreferrer">github.com/Haixiang612…</a></p>
<p>参考轮子：<a href="https://www.npmjs.com/package/redux" target="_blank" rel="nofollow noopener noreferrer">www.npmjs.com/package/red…</a></p>
</blockquote>
<h2 data-id="heading-0">前言吐槽</h2>
<p>Redux 应该是很多前端新手的噩梦。还记得我刚接触 Redux 的时候也是刚从 Vue 转过来的时候，觉得Redux 概念非常多，想写一个 Hello World 都难。</p>
<p>文档也是很难看懂，并不是看不懂英文，而是看的时候总会想：TMD在说泥🐴呢。看得出文档想手把手把新手教好，结果却是适得而反，啰嗦的排版和系统性地阐述让新手越来越蒙逼。文档还有一步令人窒息的操作：把 redux、react-redux、redux-toolkit 三个库放在一起来讲。靠，你的标题叫 redux 文档啊，就讲 Redux 不就行了嘛？搞得新手总会觉得 Redux 就是像 Vuex 一样为 React 量身订做的，其实并不是。</p>
<h2 data-id="heading-1">Redux 和 React 的关系</h2>
<p>Redux 和 React 根本没关系。</p>
<p>看 Redux 的官网开头：<strong><a href="https://redux.js.org/" target="_blank" rel="nofollow noopener noreferrer">"A Predictable State Container for JS Apps"</a></strong>。再看 Vuex 的官网开头：<strong><a href="https://vuex.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">"Vuex is a state management pattern + library for Vue.js applications"</a></strong>。</p>
<p>请问哪里出现了 "react" 这个单词了？</p>
<p>两者的定位本来就不一样：Redux 仅仅是个事件中心（事件总线，随便怎么叫），就是 for JS Apps 的。而 Vuex 除了事件中心，也是 for Vue.js applications 的。</p>
<h2 data-id="heading-2">解决了什么问题</h2>
<p>为了重新认识 Redux，我们先搞清楚 Redux 到底是个啥、解决了什么问题。</p>
<p>简单来说：</p>
<ul>
<li>创建一个事件中心，里面存一些数据，叫 <code>store</code></li>
<li>向外提供读、写操作，叫 <code>getState</code> 和 <code>dispatch</code>，通过分发事件修改数据，叫 <code>dispatch(action)</code></li>
<li>添加监听器，每次 dispatch 数据改了，就触发监听器，达到监听数据变化的效果，叫 <code>subscribe</code></li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa8ee9d68f664d51a03c9d7cd593a5e5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Redux 本来就是一个超级简单的库，只是文档不知不觉把它写复杂了，搞得新手无从下手，口口相传觉得 Redux 很难、很复杂。其实 Redux 一点都不难、简单得一批。</p>
<p>不信？下面就带大家一起写一个完整的 Redux。</p>
<h2 data-id="heading-3">createStore</h2>
<p>这个函数创建一个 Object，里面存放数据，并提供读和写方法。实现如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params">reduce, preloadedState, enhancer</span>) </span>&#123;
  <span class="hljs-keyword">let</span> currentState = preloadedState <span class="hljs-comment">// 当前数据（状态）</span>
  <span class="hljs-keyword">let</span> currentReducer = reducer <span class="hljs-comment">// 计算新数据（状态）</span>
  <span class="hljs-keyword">let</span> isDispatching = <span class="hljs-literal">false</span> <span class="hljs-comment">// 是否在 dispatch</span>

  <span class="hljs-comment">// 获取 state</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getState</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isDispatching) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'还在 dispatching 呢，获取不了 state 啊'</span>)
    &#125;
    <span class="hljs-keyword">return</span> currentState
  &#125;

  <span class="hljs-comment">// 分发 action 的函数</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span>(<span class="hljs-params">action</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isDispatching) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'还在 dispatching 呢，dispatch 不了啊'</span>)
    &#125;

    <span class="hljs-keyword">try</span> &#123;
      isDispatching = <span class="hljs-literal">true</span>
      currentState = currentReducer(currentState, action)
    &#125; <span class="hljs-keyword">finally</span> &#123;
      isDispatching = <span class="hljs-literal">false</span>
    &#125;

    <span class="hljs-keyword">return</span> action
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    getState,
    dispatch
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面将数据存于 <code>currentState</code>。<code>getState</code> 返回当前数据。在 <code>dispatch</code> 里使用 <code>reducer</code> 计算新的数据（状态）从而修改 <code>currentState</code>。</p>
<p>上面还用 <code>isDispatching</code> 防止多重 dispatch 情况下操作同一资源的问题。</p>
<p>假如别人不给你传 <code>preloadedState</code>，那 <code>currentState</code> 初始时就会为 <code>undefuned</code> 了呀，<code>undefined</code> 作为 state 是不行的。为了解决这个问题，可以在 <code>createStore</code> 的时候直接 dispatch 一个 action，这个 action 不命中所有 reducer 里的 case，那么 <code>reducer</code> 都返回初始值，以此达到初始化 state 的目的，这也是为什么在 <code>reducer</code> 里的 switch-case 的 default 一定要返回 state 而不是啥都不处理。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 生成随机字符串，注意这里的 toString(36) 的 36 是基数</span>
<span class="hljs-keyword">const</span> randomString = <span class="hljs-function">() =></span> <span class="hljs-built_in">Math</span>.random().toString(<span class="hljs-number">36</span>).substring(<span class="hljs-number">7</span>).split(<span class="hljs-string">''</span>).join(<span class="hljs-string">'.'</span>)

<span class="hljs-keyword">const</span> actionTypes = &#123;
  <span class="hljs-attr">INIT</span>: <span class="hljs-string">`@@redux/INIT<span class="hljs-subst">$&#123;randomString()&#125;</span>`</span>, <span class="hljs-comment">// 为了重名，追加随机字符串</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params">reduce, preloadedState, enhancer</span>) </span>&#123;
  ...

  <span class="hljs-comment">// 获取 state</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getState</span>(<span class="hljs-params"></span>) </span>&#123;
    ...
  &#125;

  <span class="hljs-comment">// 分发 action 的函数</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span>(<span class="hljs-params">action</span>) </span>&#123;
    ...
  &#125;

  <span class="hljs-comment">// 初始化</span>
  dispatch(&#123;<span class="hljs-attr">type</span>: actionTypes.INIT&#125;)

  <span class="hljs-keyword">return</span> &#123;
    getState,
    dispatch
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以用我们的 Redux 啦~</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'increment'</span>:
      <span class="hljs-keyword">return</span> state + action.payload
    <span class="hljs-keyword">case</span> <span class="hljs-string">'decrement'</span>:
      <span class="hljs-keyword">return</span> state - action.payload
    <span class="hljs-attr">default</span>:
      <span class="hljs-keyword">return</span> state
  &#125;
&#125;

<span class="hljs-keyword">const</span> store = createStore(reducer, <span class="hljs-number">1</span>) <span class="hljs-comment">// 1，不管有没有初始值，都会 dispatch @@redux/INIT 来初始化 state</span>

store.dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'increment'</span>, <span class="hljs-attr">payload</span>: <span class="hljs-number">2</span> &#125;) <span class="hljs-comment">// 1 + 2</span>

<span class="hljs-built_in">console</span>.log(store.getState()) <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">isPlainObject 和 kindOf</h2>
<p>Redux 对 action 是有要求的，一定要是普通对象。所以我们还要需要判断一下，如果不是普通对象，就抛出错误并说明 action 此时的类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 分发 action 的函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span>(<span class="hljs-params">action: A</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!isPlainObject(action)) &#123; <span class="hljs-comment">// 是不是纯对象</span>
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`不是纯净的 Object，是一个类似 <span class="hljs-subst">$&#123;kindOf(action)&#125;</span> 的东西`</span>) <span class="hljs-comment">// 不是，是一个类似 XXX 的东西</span>
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>isPlainObject</code> 和 <code>kindOf</code> 都是可以从 npm 里的 <a href="https://www.npmjs.com/package/is-plain-object" target="_blank" rel="nofollow noopener noreferrer">is-plain-object</a> 和 <a href="https://www.npmjs.com/package/kind-of" target="_blank" rel="nofollow noopener noreferrer">kind-of</a> 获得。这两个包实现都很简单。是不是会觉得：啊？就这？就这么小的包都有几万的下载量？？？我自己实现也行啊。没错，前端开发就是这么无聊，写这么小的包都能一炮而红，只难当年还不会 JS 没能夺得先机 😢。</p>
<p>这里我们用 npm  包，自己实现一波吧：</p>
<p>首先是 <code>isPlainObject</code>，一般来说通过判断 <code>typeof obj === 'object'</code> 就可以了，但是 <code>typeof  null</code> 也是 object，这是因为最初实现 JS 的时候，用 <strong>type</strong> 和 <strong>value</strong> 表示 JS 的值，当 <code>type === 0</code> 时表示是 Object，而当初 <code>null</code> 的地址又为 <code>0x00</code> 所以 <strong>null</strong> 的 type 一直是 0，因此 <code>typeof null === null</code>，可以 <a href="https://stackoverflow.com/questions/18808226/why-is-typeof-null-object" target="_blank" rel="nofollow noopener noreferrer">参考这里</a>。 另一个点是原型键只有一层。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> isPlainObject = <span class="hljs-function">(<span class="hljs-params">obj: <span class="hljs-built_in">any</span></span>) =></span> &#123;
  <span class="hljs-comment">// 检查类型</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj !== <span class="hljs-string">'object'</span> || obj === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>

  <span class="hljs-comment">// 检查是否由 constructor 生成</span>
  <span class="hljs-keyword">let</span> proto = obj
  <span class="hljs-keyword">while</span> (<span class="hljs-built_in">Object</span>.getPrototypeOf(proto) !== <span class="hljs-literal">null</span>) &#123;
    proto = <span class="hljs-built_in">Object</span>.getPrototypeOf(proto)
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.getPrototypeOf(obj) === proto
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> isPlainObject
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个函数 <code>kindOf</code> 实现就繁琐多了，除了要判断一些简单的 typeof 值，还要判断 Array, Date, Error 等多种对象。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> isDate = <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span> &#123; <span class="hljs-comment">// 是不是 Date</span>
  <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Date</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  <span class="hljs-keyword">return</span> (
    <span class="hljs-keyword">typeof</span> value.toDateString === <span class="hljs-string">'function'</span> &&
    <span class="hljs-keyword">typeof</span> value.getDate === <span class="hljs-string">'function'</span> &&
    <span class="hljs-keyword">typeof</span> value.setDate === <span class="hljs-string">'function'</span>
  )
&#125;

<span class="hljs-keyword">const</span> isError = <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span> &#123; <span class="hljs-comment">// 是不是 Error</span>
  <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Error</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  <span class="hljs-keyword">return</span> (
    <span class="hljs-keyword">typeof</span> value.message === <span class="hljs-string">'string'</span> &&
    value.constructor &&
    <span class="hljs-keyword">typeof</span> value.constructor.stackTraceLimit === <span class="hljs-string">'number'</span>
  )
&#125;

<span class="hljs-keyword">const</span> getCtorName = (value: <span class="hljs-built_in">any</span>): <span class="hljs-built_in">string</span> | <span class="hljs-function"><span class="hljs-params">null</span> =></span> &#123; <span class="hljs-comment">// 获取</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> value.constructor === <span class="hljs-string">'function'</span> ? value.constructor.name : <span class="hljs-literal">null</span>
&#125;

<span class="hljs-keyword">const</span> kindOf = (value: <span class="hljs-built_in">any</span>): <span class="hljs-function"><span class="hljs-params">string</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (value === <span class="hljs-built_in">void</span> <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">'undefined'</span>
  <span class="hljs-keyword">if</span> (value === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">'null'</span>

  <span class="hljs-keyword">const</span> <span class="hljs-keyword">type</span> = <span class="hljs-keyword">typeof</span> value
  <span class="hljs-keyword">switch</span> (<span class="hljs-keyword">type</span>) &#123; <span class="hljs-comment">// 有字面意思的值</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'boolean'</span>:
    <span class="hljs-keyword">case</span> <span class="hljs-string">'string'</span>:
    <span class="hljs-keyword">case</span> <span class="hljs-string">'number'</span>:
    <span class="hljs-keyword">case</span> <span class="hljs-string">'symbol'</span>:
    <span class="hljs-keyword">case</span> <span class="hljs-string">'function'</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">type</span>
  &#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) <span class="hljs-keyword">return</span> <span class="hljs-string">'array'</span> <span class="hljs-comment">//是不是数组</span>
  <span class="hljs-keyword">if</span> (isDate(value)) <span class="hljs-keyword">return</span> <span class="hljs-string">'date'</span> <span class="hljs-comment">// 是不是 Date</span>
  <span class="hljs-keyword">if</span> (isError(value)) <span class="hljs-keyword">return</span> <span class="hljs-string">'error'</span> <span class="hljs-comment">// 是不是 Error</span>

  <span class="hljs-keyword">const</span> ctorName = getCtorName(value)
  <span class="hljs-keyword">switch</span> (ctorName) &#123; <span class="hljs-comment">// 构造函数中读取类型</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'Symbol'</span>:
    <span class="hljs-keyword">case</span> <span class="hljs-string">'Promise'</span>:
    <span class="hljs-keyword">case</span> <span class="hljs-string">'WeakMap'</span>:
    <span class="hljs-keyword">case</span> <span class="hljs-string">'WeakSet'</span>:
    <span class="hljs-keyword">case</span> <span class="hljs-string">'Map'</span>:
    <span class="hljs-keyword">case</span> <span class="hljs-string">'Set'</span>:
      <span class="hljs-keyword">return</span> ctorName
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">type</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面两个函数在学习 Redux 并不是很重要，不过可以我们提供实现这两个工具函数的一些灵感，下次再次使用时我们也可以直接手写出来。</p>
<h2 data-id="heading-5">replaceReducer</h2>
<p><code>replaceReducer</code> 这个函数别说用了，估计没多少人听说过。在 Code Spliting 的时候才会用到。比如打包出来有 2 个 JS，第一个先加载了 reducer，第二个加载新的 reducer，这里可以用 <code>combineReducers</code> 去完成合并。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> newRootReducer = combineReducers(&#123;
  <span class="hljs-attr">existingSlice</span>: existingSliceReducer,
  <span class="hljs-attr">newSlice</span>: newSliceReducer
&#125;)

store.replaceReducer(newRootReducer)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在有太多做动态模块、代码分割的库帮我们做了这些事情了，所以我们没多大机会用到这个 API。</p>
<p>实现上也很简单，就是把原来的 <code>reducer</code> 替换掉就可以了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> actionTypes = &#123;
  <span class="hljs-attr">INIT</span>: <span class="hljs-string">`@@redux/INIT<span class="hljs-subst">$&#123;randomString()&#125;</span>`</span>,
  <span class="hljs-attr">REPLACE</span>: <span class="hljs-string">`@@redux/REPLACE<span class="hljs-subst">$&#123;randomString()&#125;</span>`</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params">reducer, preloadedState, enhancer</span>) </span>&#123;
  ...
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">replaceReducer</span>(<span class="hljs-params">nextReducer</span>) </span>&#123;
    currentReducer = nextReducer

    dispatch(&#123;<span class="hljs-attr">type</span>: actionTypes.REPLACE&#125; <span class="hljs-keyword">as</span> A) <span class="hljs-comment">// 重新初始化状态</span>

    <span class="hljs-keyword">return</span> store
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面除了直接替换，还 dispatch 了 <code>@@redux/REPALCE</code> 这个 action。把当前状态都重置了。</p>
<h2 data-id="heading-6">subscribe</h2>
<p>刚刚说到 Redux 需要监听数据的变化，非常 Easy ~ 可以在 dispatch 的时候触发所有监听器。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params">reducer, preloadedState, enhancer</span>) </span>&#123;
  <span class="hljs-keyword">let</span> currentState = preloadedState
  <span class="hljs-keyword">let</span> currentReducer = reducer
  <span class="hljs-keyword">let</span> currentListeners = [] <span class="hljs-comment">// 当前监听器</span>
  <span class="hljs-keyword">let</span> nextListeners = currentListeners <span class="hljs-comment">// 临时监听器集合</span>
  <span class="hljs-keyword">let</span> isDispatching = <span class="hljs-literal">false</span>

  <span class="hljs-comment">// 获取 state</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getState</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isDispatching) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'还在 dispatching 呢，获取不了 state 啊'</span>)
    &#125;
    <span class="hljs-keyword">return</span> currentState
  &#125;

  <span class="hljs-comment">// 分发 action 的函数</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span>(<span class="hljs-params">action: A</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!isPlainObject(action)) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`不是纯净的 Object，是一个类似 <span class="hljs-subst">$&#123;kindOf(action)&#125;</span> 的东西`</span>)
    &#125;

    <span class="hljs-keyword">if</span> (isDispatching) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'还在 dispatching 呢，dispatch 不了啊'</span>)
    &#125;

    <span class="hljs-keyword">try</span> &#123;
      isDispatching = <span class="hljs-literal">true</span>
      currentState = currentReducer(currentState, action)
    &#125; <span class="hljs-keyword">finally</span> &#123;
      isDispatching = <span class="hljs-literal">false</span>
    &#125;

    <span class="hljs-keyword">const</span> listeners = (currentListeners = nextListeners)
    listeners.forEach(<span class="hljs-function"><span class="hljs-params">listener</span> =></span> listener()) <span class="hljs-comment">// 全部执行一次</span>

    <span class="hljs-keyword">return</span> action
  &#125;

  <span class="hljs-comment">// 将 nextListeners 作为临时 listeners 集合</span>
  <span class="hljs-comment">// 防止 dispatching 时出现的一些 bug</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ensureCanMutateNextListeners</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (nextListeners !== currentListeners) &#123;
      nextListeners = currentListeners.slice()
    &#125;
  &#125;

  <span class="hljs-comment">// 订阅</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">subscribe</span>(<span class="hljs-params">listener: () => <span class="hljs-keyword">void</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isDispatching) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'还在 dispatching 呢，subscribe 不了啊'</span>)
    &#125;

    <span class="hljs-keyword">let</span> isSubscribed = <span class="hljs-literal">true</span>

    ensureCanMutateNextListeners()
    nextListeners.push(listener) <span class="hljs-comment">// 添加监听器</span>

    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unsubscribe</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (!isSubscribed) &#123;
        <span class="hljs-keyword">return</span>
      &#125;

      <span class="hljs-keyword">if</span> (isDispatching) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'还在 dispatching 呢，unsubscribe 不了啊'</span>)
      &#125;

      isSubscribed = <span class="hljs-literal">false</span>

      ensureCanMutateNextListeners()

      <span class="hljs-comment">// 去掉当前监听器</span>
      <span class="hljs-keyword">const</span> index = nextListeners.indexOf(listener)
      nextListeners.splice(index, <span class="hljs-number">1</span>)
      currentListeners = <span class="hljs-literal">null</span>
    &#125;
  &#125;

  <span class="hljs-comment">// 初始化</span>
  dispatch(&#123;<span class="hljs-attr">type</span>: actionTypes.INIT&#125;)

  <span class="hljs-keyword">return</span> &#123;
    getState,
    dispatch,
    subscribe,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面有几个点要注意：
<code>currentListeners</code> 用于执行监听器，<code>nextListeners</code> 作为临时监听器的存放数组用于增加和移除监听器。弄两个数组是为了防止修改数组数组时出现一些奇奇怪怪的 Bug，和上面用 <code>isDispatching</code> 解决操作同一资源的问题是差不多的。</p>
<p><code>subscribe</code> 的返回值为 <code>unsubscribe</code> 函数，这一是种很常用的编码设计：如果一个函数有 side-effect，那么返回值最好就是取消 side-effect 的函数，例如 <code>useEffect</code> 里的函数。</p>
<p>可能有人会问如果 subscribe 很多次，第一次的 <code>unsubscribe</code> 里的 <code>listener</code> 还是第一次的 listener 么？这是肯定的，因为 <code>listener</code> 和 <code>unsubscribe</code> 构成了闭包，每次的 <code>unsubscribe</code> 一直会引用那一次的 <code>listener</code>，<code>listener</code> 不会被销毁。</p>
<p>使用的例子如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> store = createStore(reducer, <span class="hljs-number">1</span>)

<span class="hljs-keyword">const</span> listener = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>)

<span class="hljs-keyword">const</span> unsubscirbe = store.subscribe(listener)

<span class="hljs-comment">// 1 + 2</span>
store.dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'increment'</span>, <span class="hljs-attr">payload</span>: <span class="hljs-number">2</span> &#125;) <span class="hljs-comment">// 打印 "hello"</span>

unsubscribe()

<span class="hljs-comment">// 3 + 2</span>
store.dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'increment'</span>, <span class="hljs-attr">payload</span>: <span class="hljs-number">2</span> &#125;) <span class="hljs-comment">// 不会打印 "hello"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">observable</h2>
<p>observable 是 <a href="https://github.com/tc39/proposal-observable" target="_blank" rel="nofollow noopener noreferrer">tc39</a> 提出的概念，表示一个可被观察的东西，里面也有一个 <code>subscribe</code> 函数，不同的是传入的参数为 <code>Observer</code>，这个 <code>Observer</code> 需要有一个 <code>next</code> 函数，将当前状态生成下一个状态。</p>
<p>刚刚已经实现 store 数据的监听了，那 store 也可以看作为一个可被观察的东西。我们弄一个函数就叫 <code>observable</code>，返回内容即为上面的 <code>observable</code> 的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> $$observable = (<span class="hljs-function">() =></span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> === <span class="hljs-string">'function'</span> && <span class="hljs-built_in">Symbol</span>.observable) || <span class="hljs-string">'@@observable'</span>)()

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> $$observable


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span><<span class="hljs-title">S</span>, <span class="hljs-title">A</span> <span class="hljs-title">extends</span> <span class="hljs-title">Action</span>>(<span class="hljs-params">reducer preloadedState, enhancer</span>) </span>&#123;
  ...
  <span class="hljs-comment">// 支持 observable/reactive 库</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observable</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> outerSubscribe = subscribe

    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-function"><span class="hljs-title">subscribe</span>(<span class="hljs-params">observer: unknown</span>)</span> &#123;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observeState</span>(<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-keyword">const</span> observerAsObserver = observer
          <span class="hljs-keyword">if</span> (observerAsObserver.next) &#123;
            observerAsObserver.next(getState())
          &#125;
        &#125;

        observeState() <span class="hljs-comment">// 获取当前 state</span>
        <span class="hljs-keyword">const</span> unsubscribe = outerSubscribe(observeState)
        <span class="hljs-keyword">return</span> &#123;unsubscribe&#125;
      &#125;,
      [$$observable]() &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
      &#125;
    &#125;
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以像下面这样去用：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> store = createStore(reducer, <span class="hljs-number">1</span>)

<span class="hljs-keyword">const</span> next = <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> state + <span class="hljs-number">2</span> <span class="hljs-comment">// 获取下一个状态的函数</span>

<span class="hljs-keyword">const</span> observable = store.observable()

observable.subscribe(&#123;next&#125;) <span class="hljs-comment">// 订阅后 next 一下：1 + 2</span>

store.dispatch(&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'increment'</span>, <span class="hljs-attr">payload</span>: <span class="hljs-number">2</span>&#125;) <span class="hljs-comment">// 1 + 2 + 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面可以看出，next 的效果就是一个累加的效果。一般人也用不到上面的特性，主要都是别的库会用到，比如 <a href="https://redux-observable.js.org/" target="_blank" rel="nofollow noopener noreferrer">redux-observable 这个轮子</a>。</p>
<h2 data-id="heading-8">applyMiddlewares</h2>
<p>现在 <code>createStore</code> 已经完成差不多啦，还有第三个参数 <code>enhancer</code> 没有用到。这个函数主要用于增强 <code>createStore</code> 的。在 <code>createStore</code> 里直接传入当前 <code>createStore</code>，enhance 之后返回一个船新的 <code>createStore</code>，再传入原来的 <code>reducer</code> 和 <code>preloadedState</code> 生成 store：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span><<span class="hljs-title">S</span>, <span class="hljs-title">A</span> <span class="hljs-title">extends</span> <span class="hljs-title">Action</span>>(<span class="hljs-params">reducer, preloadedState, enhancer</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (enhancer) &#123;
    <span class="hljs-keyword">return</span> enhancer(createStore)(reducer, preloadedState)
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>enhancer</code> 函数有很多种实现方式，其中最常见，也是官方提供的就是 <code>applyMiddlewares</code> 这个增强函数。它的目的是通过多种中间件来增强 <code>dispatch</code>，而 <code>dispatch</code> 又是 store 里的一员，相当于把 <code>store</code> 增强了，因此这个函数是个 enhancer。</p>
<p>在实现 <code>applyMiddlewares</code> 之前，我们要弄清楚中间件这个概念是怎么来的呢？又是如何增强 <code>dispatch</code> 的呢？为啥要用 <code>applyMiddlewares</code> 这个 enhancer 呢？</p>
<p>先从一个简单的例子说起：假如现在我们想在每次 dispatch 后都要 <code>console.log</code> 一下，最简单的方法：直接把 dispatch 改掉：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> originalDispatch = store.dispatch
store.dispatch = <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;  
    <span class="hljs-keyword">let</span> result = originalDispatch(action)  
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'next state'</span>, store.getState())  
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需要注意的是 dispatch 是一个传入 action 并返回 action 的函数，因此这里要将 result 返回出去。</strong></p>
<p>那假如我们再加个 Logger 2 呢？可能会是这样：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> logger1 = <span class="hljs-function">(<span class="hljs-params">store</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> originalDispatch = store.dispatch
    
    store.dispatch = <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger1 before'</span>)
        <span class="hljs-keyword">let</span> result = originalDispatch(action) <span class="hljs-comment">// 原来的 dispatch</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger 1 after'</span>)
        <span class="hljs-keyword">return</span> result
    &#125;
&#125;

<span class="hljs-keyword">const</span> logger2 = <span class="hljs-function">(<span class="hljs-params">store</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> originalDispatch = store.dispatch
    
    store.dispatch = <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger2 before'</span>)
        <span class="hljs-keyword">let</span> result = originalDispatch(action) <span class="hljs-comment">// logger 1 的返回函数</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger2 after'</span>)
        <span class="hljs-keyword">return</span> result
    &#125;
&#125;

logger1(store)
logger2(store)

<span class="hljs-comment">// logger2 before -> logger1 before -> dispatch -> logger1 after -> logger2 after</span>
store.dispatch(...)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>上面的 logger1 和 logger 2 就叫做中间件，它们可以拿到上一次的 <code>store.dispatch</code> 函数，然后一顿操作生成新的 <code>dispatch</code>，再赋值到 <code>store.dispatch</code> 来增强 <code>dispatch</code>。</strong></p>
<p>值得注意的点是，虽然先执行 logger1 再执行 logger2，但是 dispatch 时会以</p>
<pre><code class="copyable">logger2 before -> logger1 before -> dispatch -> logger1 after -> logger2 after
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>“倒叙”</strong> 的方式来执行中间件的内容。</p>
<p>如果有更多的中间件，可以用数组存起来。初始化也不能像上面那样跑脚本那样初始化了，可以把初始化封装为一个函数，就叫 <code>applyMiddlewares</code> 吧：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyMiddleware</span>(<span class="hljs-params">store, middlewares</span>) </span>&#123;
    middlewares = middlewares.slice()   <span class="hljs-comment">// 浅拷贝数组 </span>
    middlewares.reverse() <span class="hljs-comment">// 反转数组</span>

    <span class="hljs-comment">// 循环替换dispatch   </span>
    middlewares.forEach(<span class="hljs-function"><span class="hljs-params">middleware</span> =></span> store.dispatch = middleware(store))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刚刚提到如果正序初始化中间件，会出现“倒序”执行 dispatch 的情况，所以这里要做中间件数组的反转。而 <code>reverse</code> 会改变原数组，因此开头要做一次数组的浅拷贝。</p>
<p>上面的写法有一个问题：在 forEach 里直接改变 store.dispatch 会产生 side-effect。遵循函数式的思路，我们应该生成好一个最终的 dispatch，再赋值到 store.dispatch 上。</p>
<p>怎么生成最终 dispatch 呢？参考 dispatch 的传入 action 返回 action 的思路，我们也可以弄一个传入旧 dispatch 返回新 dispatch 的函数嘛。比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> dispatch1 = <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> &#123;...&#125;
<span class="hljs-keyword">const</span> dispatch2 = <span class="hljs-function">(<span class="hljs-params">dispatch1</span>) =></span> &#123;...&#125;
<span class="hljs-keyword">const</span> dispatch3 = <span class="hljs-function">(<span class="hljs-params">dispatch2</span>) =></span> &#123;...&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样 store 就传不进来了，不怕，合理运用柯里化可以完美解决我们的问题：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> logger1 => <span class="hljs-function">(<span class="hljs-params">store</span>) =></span> <span class="hljs-function">(<span class="hljs-params">next</span>) =></span> <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger1 before'</span>)
    <span class="hljs-keyword">let</span> result = originalDispatch(action)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger 1 after'</span>)
    <span class="hljs-keyword">return</span> result
&#125;

<span class="hljs-keyword">const</span> logger2 => <span class="hljs-function">(<span class="hljs-params">store</span>) =></span> <span class="hljs-function">(<span class="hljs-params">next</span>) =></span> <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger2 before'</span>)
    <span class="hljs-keyword">let</span> result = originalDispatch(action)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger2 after'</span>)
    <span class="hljs-keyword">return</span> result
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyMiddleware</span>(<span class="hljs-params">store, middlewares</span>) </span>&#123;
    <span class="hljs-comment">// 初始的 dispatch</span>
    <span class="hljs-keyword">let</span> dispatch = <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'还在构建 middlewares，不要 dispatch'</span>)
    &#125;

    middlewares = middlewares.slice() <span class="hljs-comment">// 浅拷贝数组 </span>
    middlewares.reverse() <span class="hljs-comment">// 反转数组</span>

    <span class="hljs-keyword">const</span> middlewareAPI = &#123;
      <span class="hljs-attr">getState</span>: store.getState,
      <span class="hljs-comment">// 这里先用初始的 dispatch，防止在构建过程中 dispatch 的情况</span>
      <span class="hljs-comment">// 如果直接用上面 dispatch 会有闭包的问题，构建的时候都会指向初始时的 dispatch，可能会出现一些奇奇怪怪的 Bug</span>
      <span class="hljs-comment">// 因此这里用了新生成的函数</span>
      <span class="hljs-attr">dispatch</span>: <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> dispatch(args)
    &#125;

    <span class="hljs-comment">// 怎么生成最终的 dispatch 呢？</span>
    <span class="hljs-keyword">const</span> xxx = middlewares.map(<span class="hljs-function"><span class="hljs-params">middleware</span> =></span> middleware(middlewareAPI))
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了像上面套娃般地生成新函数，需要用到 <code>reduce</code> 函数来将数组里每个函数进行头接尾尾接头的操作，这样的操作称为 <code>compose</code>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span>(<span class="hljs-params">...funcs: <span class="hljs-built_in">Function</span>[]</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (funcs.length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">arg</span>) =></span> arg
  &#125;

  <span class="hljs-keyword">if</span> (funcs.length === <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> funcs[<span class="hljs-number">0</span>]
  &#125;

  <span class="hljs-keyword">return</span> funcs.reduce(<span class="hljs-function">(<span class="hljs-params">prev, curt</span>) =></span> <span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span></span>) =></span> prev(curt(...args)))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将中间件一个个传入 <code>compose(logger1, logger2)</code> 时，就会出现：</p>
<pre><code class="copyable">logger1(
  logger1 before
  logger2(
    logger2 before
    dispatch -> 最原始的 dispatch
    logger2 after
  )
  logger2 after
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>的结构。这就是 Redux 最厉害的地方了，对中间件的处理十分的优雅，而且使用 <code>reducer</code> 还改变了函数的执行顺序连上面的 <code>reverse</code> 都不需要了。</p>
<p>整理一下上面的改动，再把 <code>applyMiddlewares</code> 写成 enhancer 的写法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyMiddlewares</span>(<span class="hljs-params">...middlewares: Middleware[]</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">createStore</span>) =></span> <span class="hljs-function">(<span class="hljs-params">reducer: Reducer, preloadState</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> store = createStore(reducer, preloadState)

    <span class="hljs-keyword">let</span> dispatch = <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'还在构建 middlewares，不要 dispatch'</span>)
    &#125;

    <span class="hljs-keyword">const</span> middlewareAPI: MiddlewareAPI = &#123;
      <span class="hljs-attr">getState</span>: store.getState,
      <span class="hljs-attr">dispatch</span>: <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> dispatch(args)
    &#125;

    <span class="hljs-keyword">const</span> chain = middlewares.map(<span class="hljs-function"><span class="hljs-params">middleware</span> =></span> middleware(middlewareAPI))
    dispatch = compose(...chain)(store.dispatch)

    <span class="hljs-keyword">return</span> &#123;...store, dispatch&#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到了这一步，你已经掌握了 Redux 的精髓中的精髓了。剩下的就是一些“杂鱼”函数了。</p>
<h2 data-id="heading-9">combineReducers</h2>
<p>一个非常无聊的函数，仅仅将一堆的 reducer 合并一个 reducer 而已。比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> nameReducer = <span class="hljs-function">() =></span> <span class="hljs-string">'111'</span>
<span class="hljs-keyword">const</span> ageReducer = <span class="hljs-function">() =></span> <span class="hljs-number">222</span>

<span class="hljs-keyword">const</span> reducer = combineReducers(&#123;
  <span class="hljs-attr">name</span>: nameReducer,
  <span class="hljs-attr">age</span>: ageReducer
&#125;)

<span class="hljs-keyword">const</span> store = createStore(reducer, &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Jack'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
&#125;)

store.dispatch(&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'xxx'</span>&#125;) <span class="hljs-comment">// state => &#123;name: '111', age: 222&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>怎么合并呢？简单得雅痞：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">combineReducers</span>(<span class="hljs-params">reducers: ReducerMapObject</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">combination</span>(<span class="hljs-params">state, action: AnyAction</span>) </span>&#123;
    <span class="hljs-keyword">let</span> hasChanged = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">let</span> nextState = &#123;&#125;
    <span class="hljs-built_in">Object</span>.entries(finalReducers).forEach(<span class="hljs-function">(<span class="hljs-params">[key, reducer]</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> previousStateForKey = state[key] <span class="hljs-comment">// 以前的状态</span>
      <span class="hljs-keyword">const</span> nextStateForKey = reducer(previousStateForKey, action) <span class="hljs-comment">// 更新为现在的状态</span>

      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> nextStateForKey === <span class="hljs-string">'undefined'</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'状态不能是 undefined 啊'</span>)
      &#125;

      nextState[key] = nextStateForKey <span class="hljs-comment">// 设置最新状态</span>
      hasChanged = hasChanged || nextStateForKey !== previousStateForKey <span class="hljs-comment">// 改了没有啊？</span>
    &#125;)

    <span class="hljs-comment">// reducer 的 key 的数目和 state 的 key 的数目是否一致</span>
    hasChanged = hasChanged || <span class="hljs-built_in">Object</span>.keys(finalReducers).length === <span class="hljs-built_in">Object</span>.keys(state).length

    <span class="hljs-keyword">return</span> hasChanged ? nextState : <span class="hljs-literal">null</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本质上就是把 reducerMapObject 里每个 reducer 都执行一遍，拿到新 state 更新对应 key 下的 state。当然，Redux 里的对这个函数的实现也没这么简单，它还做了很多异常情况的处理，如检查 reducer 到底是不是合法的 reducer。那啥是合法的 reducer 啊？答：找不到状态时不返回 <code>undefined</code> 就合法。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> randomString = <span class="hljs-function">() =></span> <span class="hljs-built_in">Math</span>.random().toString(<span class="hljs-number">36</span>).substring(<span class="hljs-number">7</span>).split(<span class="hljs-string">''</span>).join(<span class="hljs-string">'.'</span>)

<span class="hljs-keyword">const</span> actionTypes = &#123;
  <span class="hljs-attr">INIT</span>: <span class="hljs-string">`@@redux/INIT<span class="hljs-subst">$&#123;randomString()&#125;</span>`</span>,
  <span class="hljs-attr">REPLACE</span>: <span class="hljs-string">`@@redux/REPLACE<span class="hljs-subst">$&#123;randomString()&#125;</span>`</span>,
  <span class="hljs-attr">PROBE_UNKNOWN_ACTION</span>: <span class="hljs-function">() =></span> <span class="hljs-string">`@@redux/PROBE_UNKNOWN_ACTION<span class="hljs-subst">$&#123;randomString()&#125;</span>`</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">assertReducerShape</span>(<span class="hljs-params">reducers: ReducerMapObject</span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.values(reducers).forEach(<span class="hljs-function"><span class="hljs-params">reducer</span> =></span> &#123;
    <span class="hljs-keyword">const</span> initialState = reducer(<span class="hljs-literal">undefined</span>, &#123;<span class="hljs-attr">type</span>: actionTypes.INIT&#125;)
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> initialState === <span class="hljs-string">'undefined'</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'最开始 dispatch 后状态不能为 undefined'</span>)
    &#125;

    <span class="hljs-keyword">const</span> randomState = reducer(<span class="hljs-literal">undefined</span>, &#123;<span class="hljs-attr">type</span>: actionTypes.PROBE_UNKNOWN_ACTION&#125;)
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> randomState === <span class="hljs-string">'undefined'</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'乱 dispatch 后的状态也不能是 undefined'</span>)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 dispatch <code>@@redux/INIT</code> 和 <code>@@redux/PROBE_UNKNOWN_ACTION</code> 来判断不命中 reducer 里的 case 时有没有返回 <code>undefuned</code>。当然还检查了 state 啊、action 啊这些东西的合法性：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUnexpectedStateShapeWarningMessage</span>(<span class="hljs-params">
  inputState: <span class="hljs-built_in">object</span>,
  reducers: ReducerMapObject,
  action: Action,
  unexpectedKeyCache: &#123;[key: <span class="hljs-built_in">string</span>]: <span class="hljs-literal">true</span>&#125;
</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.keys(reducers).length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'都没有 reducer 还 combine 个啥呀'</span>
  &#125;

  <span class="hljs-keyword">if</span> (!isPlainObject(action)) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'都说了 action 要是普通的 Object 了，还传一些乱七八糟的东西进来？？'</span>
  &#125;

  <span class="hljs-keyword">if</span> (action.type === actionTypes.REPLACE) <span class="hljs-keyword">return</span> <span class="hljs-comment">// 因为 replaceReducer，所以这个 reducer 作废了</span>

  <span class="hljs-comment">// 收集 reducerMapObject 里不存在的 key</span>
  <span class="hljs-keyword">const</span> unexpectedKeys = <span class="hljs-built_in">Object</span>.keys(inputState).filter(
    <span class="hljs-function"><span class="hljs-params">key</span> =></span> !reducers.hasOwnProperty(key) && !unexpectedKeyCache[key]
  )
  unexpectedKeys.forEach(<span class="hljs-function"><span class="hljs-params">unexpectedKey</span> =></span> unexpectedKeyCache[unexpectedKey] = <span class="hljs-literal">true</span>)

  <span class="hljs-keyword">if</span> (unexpectedKeys.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`下面这些 Key 都不在 state 上：<span class="hljs-subst">$&#123;unexpectedKeys.join(<span class="hljs-string">', '</span>)&#125;</span>`</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>unexpectedKeyCache</code> 是一个 Map，如果某个子 state 有错，则设置为 <code>true</code>，这个 Map 是为了防止多次告警所做的缓存。</p>
<p>再次更新一下 <code>combineReducers</code>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">combineReducers</span>(<span class="hljs-params">reducers: ReducerMapObject</span>) </span>&#123;
  <span class="hljs-comment">// 检查是否为函数</span>
  <span class="hljs-keyword">let</span> finalReducers: ReducerMapObject = &#123;&#125;
  <span class="hljs-built_in">Object</span>.entries(reducers).forEach(<span class="hljs-function">(<span class="hljs-params">[key, reducer]</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> reducer === <span class="hljs-string">'function'</span>) &#123;
      finalReducers[key] = reducer
    &#125;
  &#125;, &#123;&#125;)

  <span class="hljs-keyword">let</span> shapeAssertionError: <span class="hljs-built_in">Error</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 检查 reducer 返回值是否有 undefined</span>
    assertReducerShape(finalReducers)
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    shapeAssertionError = e
  &#125;

  <span class="hljs-comment">// 用于收集状态不存在的 key</span>
  <span class="hljs-keyword">let</span> unexpectedKeyCache: &#123;[key: <span class="hljs-built_in">string</span>]: <span class="hljs-literal">true</span>&#125; = &#123;&#125;

  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">combination</span>(<span class="hljs-params">state, action: AnyAction</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (shapeAssertionError) <span class="hljs-keyword">throw</span> shapeAssertionError

    <span class="hljs-keyword">const</span> warningMessage = getUnexpectedStateShapeWarningMessage(
      state,
      finalReducers,
      action,
      unexpectedKeyCache
    )

    <span class="hljs-keyword">if</span> (warningMessage) &#123;
      <span class="hljs-built_in">console</span>.log(warningMessage)
    &#125;

    <span class="hljs-keyword">let</span> hasChanged = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">let</span> nextState = &#123;&#125;
    <span class="hljs-built_in">Object</span>.entries(finalReducers).forEach(<span class="hljs-function">(<span class="hljs-params">[key, reducer]</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> previousStateForKey = state[key]
      <span class="hljs-keyword">const</span> nextStateForKey = reducer(previousStateForKey, action)

      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> nextStateForKey === <span class="hljs-string">'undefined'</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'状态不能是 undefined 啊'</span>)
      &#125;

      nextState[key] = nextStateForKey
      hasChanged = hasChanged || nextStateForKey !== previousStateForKey
    &#125;)

    <span class="hljs-comment">// reducer 的 key 的数目和 state 的 key 的数目是否一致</span>
    hasChanged = hasChanged || <span class="hljs-built_in">Object</span>.keys(finalReducers).length === <span class="hljs-built_in">Object</span>.keys(state).length

    <span class="hljs-keyword">return</span> hasChanged ? nextState : <span class="hljs-literal">null</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">combineActionCreators</h2>
<p>更无聊的一个函数：仅仅把多个 action creator 执行，返回一些 <code>() => dispatch(actionCreator(xxx))</code> 的函数，比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> store = createStore(reducer, <span class="hljs-number">1</span>)

<span class="hljs-keyword">const</span> combinedCreators = combineActionCreators(&#123;
  <span class="hljs-attr">add</span>: <span class="hljs-function">(<span class="hljs-params">offset: <span class="hljs-built_in">number</span></span>) =></span> (&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'increment'</span>, <span class="hljs-attr">payload</span>: offset&#125;), <span class="hljs-comment">// 加法 actionCreator</span>
  <span class="hljs-attr">minus</span>: <span class="hljs-function">(<span class="hljs-params">offset: <span class="hljs-built_in">number</span></span>) =></span> (&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'decrement'</span>, <span class="hljs-attr">payload</span>: offset&#125;), <span class="hljs-comment">// 减法 actionCreator</span>
&#125;, store.dispatch)

combinedCreators.add(<span class="hljs-number">100</span>)
combinedCreators.minus(<span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要的“好处”是返回的 <code>combinedCreators</code> 里直接 <code>.add(100)</code>，这里的 <code>.add(100)</code> 可以不用感知 <code>dispatch</code> 的存在。</p>
<p>具体实现如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 绑定一个 actionCreator</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindActionCreator</span>(<span class="hljs-params">actionCreator, dispatch</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">this</span>: <span class="hljs-built_in">any</span>, ...args: <span class="hljs-built_in">any</span>[]</span>) </span>&#123;
    <span class="hljs-keyword">return</span> dispatch(actionCreator.apply(<span class="hljs-built_in">this</span>, args))
  &#125;
&#125;

<span class="hljs-comment">// 绑定多个 actionCreator</span>
<span class="hljs-keyword">const</span> combineActionCreators = <span class="hljs-function">(<span class="hljs-params">actionCreators, dispatch</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> actionCreators === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">return</span> bindActionCreator(actionCreators, dispatch)
  &#125;

  <span class="hljs-keyword">const</span> boundActionCreators: ActionCreatorsMapObject = &#123;&#125;

  <span class="hljs-built_in">Object</span>.entries(actionCreators).forEach(<span class="hljs-function">(<span class="hljs-params">[key, actionCreator]</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> actionCreator === <span class="hljs-string">'function'</span>) &#123;
      boundActionCreators[key] = bindActionCreator(actionCreator, dispatch)
    &#125;
  &#125;)

  <span class="hljs-keyword">return</span> boundActionCreators
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码非常简单，仅仅帮你执行一下 actionCreator，然后 dispatch 返回的 action。</p>
<p>官方希望的是你在某个地方（比如父组件 combineActionCreators 了），在另外的地方（比如子组件）就不需要拿到 <code>dispatch</code> 函数就可以直接 dispatch action。</p>
<p>理想很好，<strong>但是这个功能的前提是要有定义好 actionCreator，一般来说没人会花时间定义 actionCreator，都是直接 dispatch。</strong></p>
<h2 data-id="heading-11">总结</h2>
<p>上面已经实现整个 <a href="https://www.npmjs.com/package/redux" target="_blank" rel="nofollow noopener noreferrer">redux</a> 里所有的 API 了，基本上是一模一样的，没有偷工减料。</p>
<p>当然，有一些细节，比如判断参数是不是函数，是不是 undefined 是没有做的。为了不写起来太长，比如影响阅读体验，TS 类型也是简单定义，很多函数签名的声明也没有弄。不过这些并不太重要，类型的判断完全可以交给 TS 去做就好了，而 TS 的类型无需太多纠结，毕竟这不是 TS 教程嘛 😆</p>
<p>总结一下，我们都干了什么：</p>
<ul>
<li>实现一个事件总线 + 数据（状态）中心
<ul>
<li><code>getState</code> 获取数据（状态）</li>
<li><code>dispatch(action)</code> 修改数据（状态）</li>
<li><code>subscribe(listener)</code> 添加修改数据时的监听器，只要 <code>dispatch</code> 所有监听器依次触发</li>
<li><code>replaceReducer</code> 用新 reducer 替换旧 reducer，一般人用不了，忘了吧</li>
<li><code>observable</code> 为了配合 <a href="https://github.com/tc39/proposal-observable" target="_blank" rel="nofollow noopener noreferrer">tc39</a> 搞的，准确地说是为了配合 RxJS 搞的。一般人用不起，忘了吧</li>
<li><code>enhancer</code> 传入已有 <code>createStore</code> 一通乱搞后返回增强后的 <code>createStore</code>，最最最常见的 enhancer 为 <code>applyMiddlewares</code>。一般人只会用 <code>applyMiddlewares</code>，记住这个就可以了</li>
</ul>
</li>
<li>实现 <code>applyMiddlewares</code>，将一堆中间件通过 <code>compose</code> 组合起来，执行过程为“洋葱圈”模型。其中中间件的作用是为了增强 dispatch，在 dispatch 前后会做一些事情</li>
<li>实现 <code>compose</code>，原理为将一堆入参为旧 dispatch，返回新 dispatch 的函数数组，使用 <code>Array.reduce</code> 组合，变成 <code>mid1(mid2(mid3()))</code> 无限套娃的形式</li>
<li>实现 <code>combineReducers</code>，主要作用是将多个 reducer 组件成一个新 reducer，执行 dispatch 后，所有 map 里的 reducer 都会被执行。当你用到了多个子状态 <code>Slice</code> 时会用到，别的场景忘了吧</li>
<li><code>combineActionCreators</code>，将多个 actionCreators 都执行一遍，并返回 <code>() => dispatch(actionCreator())</code> 这样的函数。这个直接忘了吧</li>
</ul>
<p>看到这里，是不是觉得 Redux 其实并没有想象中那么的复杂，所有的“难”，“复杂”只是自己给自己设置的，硬刚源码才能战胜恐惧 👊</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            