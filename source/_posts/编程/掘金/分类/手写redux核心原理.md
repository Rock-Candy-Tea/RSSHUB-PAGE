
---
title: '手写redux核心原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5668'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 23:26:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=5668'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文从零实现一个简单的 <code>redux</code> ，主要内容在于redux 的设计思路及实现原理</p>
<p>redux 是一个状态管理器，里面存放着数据，比如我们创建 store.js，在里面我们存放着这些数据，只需要在任何地方引用这个文件就可以拿到对应的状态值：</p>
<pre><code class="copyable">let state = &#123;
  count: 1
&#125;

console.log(state.count)
state.count = 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>复制代码现在我们实现了状态（计数）的修改和使用了！当然上面的有一个很明显的问题：这个状态管理器只能管理 count，修改 count 之后，使用 count 的地方不能收到通知。</p>
<h2 data-id="heading-0">实现 subscribe</h2>
<p>我们可以使用发布-订阅模式来解决这个问题。我们用个函数封装一下 <code>redux</code></p>
<pre><code class="copyable">function createStore(initState) &#123;
  let state = initState
  let listeners = []

  /* 订阅函数 */
  function subscribe(listener) &#123;
    listeners.push(listener)
  &#125;

  function changeState(newState) &#123;
    state = newState
    /* 执行通知 */
    for (let i = 0; i < listeners.length; i++) &#123;
      const listener = listeners[i]
      listener()
    &#125;
  &#125;

  function getState() &#123;
    return state
  &#125;

  return &#123; subscribe, changeState, getState &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们完成了一个简单的状态管理器。state 的数据可以自由的定, 我们修改状态，在订阅的地方监听变化，可以实现监听。</p>
<pre><code class="copyable">let initState = &#123;
  count: 1,
  detail: &#123;
    age: 24
  &#125;
&#125;

let store = createStore(initState)

store.subscribe(() => &#123;
  let state = store.getState()
  console.log('t1: ', state)
&#125;)

store.changeState(&#123; ...store.getState(), count: store.getState().count + 1 &#125;)

// t1:  &#123; count: 2, detail: &#123; age: 24 &#125; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要理解的是 <code>createStore</code>，提供了 <code>changeState</code>，<code>getState</code>，<code>subscribe</code> 三个能力。</p>
<p>在上面的函数中，我们调用 <code>store.changeState</code> 可以改变 <code>state</code> 的值，这样就存在很大的弊端了。比如 <code>store.changeState(&#123;&#125;)</code></p>
<pre><code class="copyable">我们一不小心就会把 store 的数据清空，或者误修改了其他组件的数据，那显然不太安全，出错了也很难排查，因此
我们需要有条件地操作 store，防止使用者直接修改 store 的数据。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，我们需要一个约束来修改 <code>state</code> 的值，而不允许意外的情况来将 <code>state</code> 的值清空或者误操作。分两步来解决这个问题：</p>
<ul>
<li>
<p><code>1. dispatch: 制定一个 state 修改计划，告诉 store，我的修改计划是什么。</code></p>
</li>
<li>
<p><code>2. reducer: 修改 store.changeState 方法，告诉它修改 state 的时候，按照我们的计划修改。</code></p>
</li>
</ul>
<p>我们将 <code>store.changeState</code> 改写为 <code>store.dispatch</code>, 在函数中传递多一个 <code>reducer</code> 函数来约束状态值的修改。</p>
<h2 data-id="heading-1">实现 reducer</h2>
<p><code>reducer</code> 是一个纯函数，接受一个 <code>state</code>, 返回新的 <code>state</code>。</p>
<pre><code class="copyable">function createStore(reducer, initState) &#123;
  let state = initState
  let listeners = []

  /* 订阅函数 */
  function subscribe(listener) &#123;
    listeners.push(listener)
  &#125;

  /* state 值的修改 */
  function dispatch(action) &#123;
    state = reducer(state, action)
    /* 执行通知 */
    for (let i = 0; i < listeners.length; i++) &#123;
      const listener = listeners[i]
      listener()
    &#125;
  &#125;

  function getState() &#123;
    return state
  &#125;

  return &#123; subscribe, dispatch, getState &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来尝试使用 <code>dispatch</code> 和 <code>reducer</code> 来实现自增和自减</p>
<pre><code class="copyable">let initState = &#123;
  count: 1,
  detail: &#123;
    age: 24
  &#125;
&#125;

function reducer(state, action) &#123;
  switch (action.type) &#123;
    case 'INCREMENT':
      return &#123; ...state, count: state.count + 1 &#125;
    case 'DECREMENT':
      return &#123; ...state, count: state.count - 1 &#125;
    default:
      return state
  &#125;
&#125;

let store = createStore(reducer, initState)

store.subscribe(() => &#123;
  let state = store.getState()
  console.log('t1: ', state)
&#125;)

store.dispatch(&#123; type: 'INCREMENT' &#125;) // 自增
store.dispatch(&#123; type: 'DECREMENT' &#125;) // 自减
store.dispatch(&#123; count: 2 &#125;) // 计划外：不生效
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们知道 <code>reducer</code> 是一个约束函数，接收老的 <code>state</code>，按计划返回新的 <code>state</code>。那我们项目中，有大量的 <code>state</code>，每个 <code>state</code> 都需要约束函数，如果所有的计划写在一个 <code>reducer</code> 函数里面，会导致 <code>reducer</code> 函数及其庞大复杂。所以我们需要将封装 <code>combineReducers</code> 来优化 <code>reducer</code> 函数。</p>
<h2 data-id="heading-2">实现 combineReducers</h2>
<h4 data-id="heading-3">粒子化 reducer</h4>
<ul>
<li>
<p>传入对象参数，<code>key</code> 值即为 <code>state</code> 状态树的 <code>key</code> 值， <code>value</code> 为对应的 <code>reducer</code> 函数。</p>
</li>
<li>
<p>遍历对象参数，执行每一个 <code>reducer</code> 函数，传入 <code>state[key]</code>, 函数获得每个 <code>reducer</code> 最新的 <code>state</code> 值。</p>
</li>
<li>
<p>耦合 <code>state</code> 的值, 并返回。返回合并后的新的 <code>reducer</code> 函数。</p>
</li>
</ul>
<pre><code class="copyable">function combineReducers(reducers) &#123;
  const reducerKeys = Object.keys(reducers)

  /*返回合并后的新的reducer函数*/
  return function combination(state = &#123;&#125;, action) &#123;
    /*生成的新的state*/
    const nextState = &#123;&#125;

    /*遍历执行所有的reducers，整合成为一个新的state*/
    for (let i = 0; i < reducerKeys.length; i++) &#123;
      const key = reducerKeys[i]
      const reducer = reducers[key]
      /*之前的 key 的 state*/
      const previousStateForKey = state[key]
      /*执行 分 reducer，获得新的state*/
      const nextStateForKey = reducer(previousStateForKey, action)

      nextState[key] = nextStateForKey
    &#125;
    return nextState
  &#125;
&#125;

//使用 combineReducers:
let state = &#123;
  counter: &#123; count: 0 &#125;,
  detail: &#123; age: 24 &#125;
&#125;

function counterReducer(state, action) &#123;
  switch (action.type) &#123;
    case 'INCREMENT':
      return &#123; count: state.count + 1 &#125;
    default:
      return state
  &#125;
&#125;

function detailReducer(state, action) &#123;
  switch (action.type) &#123;
    case 'INCREMENT-AGE':
      return &#123; age: state.age + 1 &#125;
    default:
      return state
  &#125;
&#125;

const reducers = combineReducers(&#123;
  counter: counterReducer,
  info: detailReducer
&#125;)

let store = createStore(reducers, initState)

store.subscribe(() => &#123;
  let state = store.getState()
  console.log('t1: ', state)
&#125;)

store.dispatch(&#123; type: 'INCREMENT' &#125;)
store.dispatch(&#123; type: 'INCREMENT-AGE' &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把 <code>reducer</code> 按组件维度拆分了，通过 <code>combineReducers</code> 合并了起来。 但是还有个问题， <code>state</code> 我们还是写在一起的，这样会造成 <code>state</code> 树很庞大，不直观，很难维护。我们需要拆分，一个 <code>state</code>，一个 <code>reducer</code> 写一块。</p>
<h4 data-id="heading-4">粒子化 state</h4>
<p>改写 <code>combineReducers</code> 函数，在 <code>createStore</code> 函数中执行 <code>dispatch(&#123; type: Symbol() &#125;)</code></p>
<pre><code class="copyable">function createStore(reducer, initState) &#123;
  let state = initState
  let listeners = []

  /* 订阅函数 */
  function subscribe(listener) &#123;
    listeners.push(listener)
  &#125;

  function dispatch(action) &#123;
    state = reducer(state, action)
    /* 执行通知 */
    for (let i = 0; i < listeners.length; i++) &#123;
      const listener = listeners[i]
      listener()
    &#125;
  &#125;

  /* 注意！！！只修改了这里，用一个不匹配任何计划的 type，来获取初始值 */
  dispatch(&#123; type: Symbol() &#125;)

  function getState() &#123;
    return state
  &#125;

  return &#123; subscribe, dispatch, getState &#125;
&#125;

//将 state 分别传入各自的 reducer:
function counterReducer(state = &#123; count: 1 &#125;, action) &#123;
  //...
&#125;

function detailReducer(state = &#123; age: 24 &#125;, action) &#123;
  //...
&#125;

// 合并 reducer
const reducers = combineReducers(&#123;
  counter: counterReducer,
  info: infoReducer
&#125;)

// 移除 initState
let store = createStore(reducers)

console.log(store.getState()) // &#123; counter: &#123; count: 1 &#125;, detail: &#123; age: 24 &#125; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>createStore</code> 的时候，用一个不匹配任何 <code>type</code> 的 <code>action</code>，来触发 <code>state = reducer(state, action)</code></li>
<li>因为 <code>action.type</code> 不匹配，每个子 <code>reducer</code> 都会进到 <code>default</code> 项，返回自己初始化的 <code>state</code>，这样就获得了初始化的 <code>state</code> 树了。</li>
</ul></div>  
</div>
            