
---
title: 'Redux笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19ba250a9dfe48138e5263190512d2e7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 23:50:32 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19ba250a9dfe48138e5263190512d2e7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简介</h2>
<p>Redux 是 JavaScript 应用的状态容器，提供可预测的状态管理。不与任意 UI 库绑定。</p>
<h2 data-id="heading-1">Redux Flow</h2>
<h3 data-id="heading-2">流程图</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19ba250a9dfe48138e5263190512d2e7~tplv-k3u1fbpfcp-watermark.image" alt="redux读书笔记.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">Flow Gif</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/622b645830264235a476de3286f8f508~tplv-k3u1fbpfcp-watermark.image" alt="ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">核心 API 探索</h2>
<h3 data-id="heading-5">核心 API List</h3>
<p>@redux/src/index.ts</p>
<pre><code class="copyable">export &#123;
  createStore, //创建根 Store；采用闭包创建了 dispatch 等函数操作闭包内的对象
  combineReducers, // 关联多个 reducer 一般用于大型应用的分区逻辑
  bindActionCreators,
  applyMiddleware, // 中间件逻辑
  compose, // 多个 fuc 串联执行的封装
  __DO_NOT_USE__ActionTypes
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">Redux.createStore</h3>
<p>作用：创建根 Store；采用闭包创建了 dispatch 等函数操作闭包内的对象</p>
<p>核心代码:</p>
<pre><code class="copyable">/**
 * Creates a Redux store that holds the state tree.
 * The only way to change the data in the store is to call `dispatch()` on it.
 *
 * There should only be a single store in your app. To specify how different
 * parts of the state tree respond to actions, you may combine several reducers
 * into a single reducer function by using `combineReducers`.
 *
...
const store = &#123;
    dispatch: dispatch as Dispatch<A>,
    subscribe,
    getState,
    replaceReducer,
    [$$observable]: observable
  &#125; as unknown as Store<ExtendState<S, StateExt>, A, StateExt, Ext> & Ext
  return store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应用程序理论上只会使用一次<code>createStore</code>，剩余的所有操作均是对 <code>createStore</code> 拿到的 root store 做操作。</p>
<h3 data-id="heading-7">Store.dispatch</h3>
<p>作用: <strong>唯一</strong>一种改变 store 的方式</p>
<p>核心代码：</p>
<pre><code class="copyable">  function dispatch(action: A) &#123;
    if (isDispatching) &#123; // 如果正在 dispatch 则中断逻辑
      throw new Error('Reducers may not dispatch actions.')
    &#125;

    try &#123;
      isDispatching = true
      currentState = currentReducer(currentState, action) 
      // 调用 reducer 的方法根据 action 重新计算 state
    &#125; finally &#123;
      isDispatching = false
    &#125;

    const listeners = (currentListeners = nextListeners) // 发送state更新的广播
    for (let i = 0; i < listeners.length; i++) &#123;
      const listener = listeners[i]
      listener()
    &#125;

    return action
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Store.getState</h3>
<p>作用：获取最新的 state 镜像</p>
<pre><code class="copyable"> /**
   * Reads the state tree managed by the store.
   *
   * @returns The current state tree of your application.
   */
  function getState(): S &#123;
    if (isDispatching) &#123;
      throw new Error(
        'You may not call store.getState() while the reducer is executing. ' +
          'The reducer has already received the state as an argument. ' +
          'Pass it down from the top reducer instead of reading it from the store.'
      )
    &#125;

    return currentState as S
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">Store.subscribe</h3>
<p>作用: 注册 state 变更的监听。返回 unsubscribe 用于取消监听防止内存泄漏</p>
<pre><code class="copyable">  function subscribe(listener: () => void) &#123;
    let isSubscribed = true

    ensureCanMutateNextListeners()
    nextListeners.push(listener)

    return function unsubscribe() &#123;
      if (!isSubscribed) &#123;
        return
      &#125;

      if (isDispatching) &#123;
        throw new Error(
          'You may not unsubscribe from a store listener while the reducer is executing. ' +
            'See https://redux.js.org/api/store#subscribelistener for more details.'
        )
      &#125;

      isSubscribed = false

      ensureCanMutateNextListeners()
      const index = nextListeners.indexOf(listener)
      nextListeners.splice(index, 1)
      currentListeners = null
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Redux.applyMiddleware</h3>
<p>作用：redux 中间件，用于在 dispatch 方法执行前后进行切面操作</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/804783aecdfa48538a54f27b11092524~tplv-k3u1fbpfcp-watermark.image" alt="redux读书笔记-中间件模型.jpg" loading="lazy" referrerpolicy="no-referrer">
注意：中间的 dispatch 是 store.dispatch 没有经过任何中间件加强。</p>
<p>核心代码：
@redux/</p>
<pre><code class="copyable">const middlewareAPI: MiddlewareAPI = &#123;
        getState: store.getState,
        dispatch: (action, ...args) => dispatch(action, ...args)
      &#125;
const chain = middlewares.map(middleware => middleware(middlewareAPI)) // 遍历中间件形成中间件链
dispatch = compose<typeof dispatch>(...chain)(store.dispatch)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>@redux/src/compose.ts</p>
<p>接收一个 func 数组，从左到右连接。内部使用了 Array 的 reduce 方法进行收拢。</p>
<pre><code class="copyable">/**
 * Composes single-argument functions from right to left. The rightmost
 * function can take multiple arguments as it provides the signature for the
 * resulting composite function.
 *
 * @param funcs The functions to compose.
 * @returns A function obtained by composing the argument functions from right
 *   to left. For example, `compose(f, g, h)` is identical to doing
 *   `(...args) => f(g(h(...args)))`.
 */
function compose(...funcs: Function[]) &#123;
  if (funcs.length === 0) &#123;
    // infer the argument type so it is usable in inference down the line
    return <T>(arg: T) => arg
  &#125;

  if (funcs.length === 1) &#123;
    return funcs[0]
  &#125;

  return funcs.reduce(
    (a, b) =>
      (...args: any) =>
        a(b(...args))
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">启发</h2>
<ol>
<li>代码中涉及到代码组合时考虑使用 componse 将函数进行组合方便后续扩展</li>
<li>TODO</li>
</ol>
<h2 data-id="heading-12">参考</h2>
<ol>
<li>官网 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fcn.redux.js.org%2Fintroduction%2Fgetting-started" target="_blank" rel="nofollow noopener noreferrer" title="http://cn.redux.js.org/introduction/getting-started" ref="nofollow noopener noreferrer">cn.redux.js.org/introductio…</a></li>
<li><a href="https://juejin.cn/post/6844904191228411911#heading-18" target="_blank" title="https://juejin.cn/post/6844904191228411911#heading-18">juejin.cn/post/684490…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fecmadao%2FCoding-Guide%2Fblob%2Fmaster%2FNotes%2FReact%2FRedux%2FRedux%25E5%2585%25A5%25E5%259D%2591%25E8%25BF%259B%25E9%2598%25B6-%25E6%25BA%2590%25E7%25A0%2581%25E8%25A7%25A3%25E6%259E%2590.md%23%25E6%259F%25AF%25E9%2587%258C%25E5%258C%2596%25E5%2587%25BD%25E6%2595%25B0curry" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ecmadao/Coding-Guide/blob/master/Notes/React/Redux/Redux%E5%85%A5%E5%9D%91%E8%BF%9B%E9%98%B6-%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90.md#%E6%9F%AF%E9%87%8C%E5%8C%96%E5%87%BD%E6%95%B0curry" ref="nofollow noopener noreferrer">Coding-Guide</a></li>
</ol></div>  
</div>
            