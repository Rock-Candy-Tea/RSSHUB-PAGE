
---
title: 'React小册 - Redux 入门 👾'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7445498d73ca4f749894fba79f3ac6d3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 22:57:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7445498d73ca4f749894fba79f3ac6d3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>本文参考如下文档</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://redux.js.org/" ref="nofollow noopener noreferrer">Redux 官方文档</a></p>
</blockquote>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.redux.org.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.redux.org.cn/" ref="nofollow noopener noreferrer">Redux 中文文档</a></p>
</blockquote>
<h2 data-id="heading-0">传送门 🤖</h2>
<ul>
<li>
<p><a href="https://juejin.cn/post/6995070859840847902/" target="_blank" title="https://juejin.cn/post/6995070859840847902/">React 小册 - 起步 JSX</a>  ✅ ✅</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6995440094341496868/" target="_blank" title="https://juejin.cn/post/6995440094341496868/">React 小册 - 扬帆起航 </a> ✅ ✅</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6995840303814934565/" target="_blank" title="https://juejin.cn/post/6995840303814934565/">React 小册 - Hooks </a> ✅ ✅</p>
</li>
<li>
<p>React 小册 - CSS 解决方案</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6998718183674757134/" target="_blank" title="https://juejin.cn/post/6998718183674757134/">React 小册 - 生命周期</a> ✅ ✅</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6999886777666240548/" target="_blank" title="https://juejin.cn/post/6999886777666240548/">React 小册 - 状态管理 Redux</a> ✅ ✅</p>
</li>
<li>
<p>React 小册 - 状态管理 Redux 中间件</p>
</li>
<li>
<p>React 小册 - 状态管理 Mobx</p>
</li>
<li>
<p>React 小册 - Router</p>
</li>
<li>
<p>React 小册 - 性能优化</p>
</li>
<li>
<p>React 小册 - SSR</p>
</li>
<li>
<p>React 小册 - React 生态</p>
</li>
</ul>
<h2 data-id="heading-1">Redux 简介</h2>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7445498d73ca4f749894fba79f3ac6d3~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>Redux 由 Flux 演变而来 是一套管理公共状态的第三方工具</p>
<blockquote>
<p>关于 Flux 思想 可参考 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2016%2F01%2Fflux.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/blog/2016/01/flux.html" ref="nofollow noopener noreferrer">阮一峰的网络日志</a></p>
</blockquote>
<p>虽然不是 React 官方开发 但已经成为 React 管理状态事实上的标准</p>
<h3 data-id="heading-2">Redux 工作流程</h3>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d762c4fc4ff4fa3bcc50885566d62a9~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>
<p>View 视图层内派发 action <code>(dispatch(action))</code></p>
</li>
<li>
<p>Reducer 接收到 action 进行分发和处理 返回一个新的 state 给 store</p>
</li>
<li>
<p>Store 接收到新的 state 数据发生改变</p>
</li>
<li>
<p>View 视图层 通过 store.subscribe 订阅 store 更新页面</p>
</li>
</ul>
<p>具体流程可见下图</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35aaef12c7694057a0c2c5a67f0dbfa5~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/053ae7c3512a413e90ddd13a4d5ac3fb~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-3">三大原则</h3>
<h4 data-id="heading-4">单一数据源</h4>
<p>虽然 Redux 源于 Flux 架构 但是它并不是完全按照 Flux 架构去设计的</p>
<p>例如 Flux 架构中 允许有多个 store 但是 Redux 中只允许有一个 store 存在</p>
<p>所有的 state 都被存在了唯一的一个 store 中</p>
<p>这也就确保了数据的<code>可追踪</code>和<code>可预测</code></p>
<h4 data-id="heading-5">不可变数据</h4>
<p>不要尝试直接修改 store 中的数据 这将会使你的应用发生不可预测的结果</p>
<p>唯一改变 state 的方法就是触发 action</p>
<p>这样 每次你的修改都会返回一个新的 store</p>
<p>Redux 就可以记录每一次 store 的变化 从而实现调试等功能</p>
<h4 data-id="heading-6">使用纯函数</h4>
<blockquote>
<p>此函数在相同的输入值时，需产生相同的输出。函数的输出和输入值以外的其他隐藏信息或状态无关，也和由 I/O 设备产生的外部输出无关。
该函数不能有语义上可观察的函数副作用，诸如“触发事件”，使输出设备输出，或更改输出值以外物件的内容等。 ------ 维基百科</p>
</blockquote>
<p>Reducer 只是一些纯函数 这意味着 Reducer 的结果将只受 Action 控制</p>
<p>再回过头来看 Redux 的官方定义</p>
<blockquote>
<p>A Predictable State Container for JS Apps ----- Redux 官方</p>
</blockquote>
<p>我们会发现 这三大原则其实都只在一件事 就是 Predictable 可预测的</p>
<h2 data-id="heading-7">Store: 它是一个单一的数据源，而且是只读的</h2>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c9c5b41a2b847c2972d5a3b678912bd~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-8">Action: 是“动作”的意思，它是对变化的描述</h2>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4eb5bd6d834f4f64869f8313b7c43890~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-9">Reducer: 它负责对变化进行分发和处理，最终将新的数据返回给 Store</h2>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b400f11cea6485288f3a5dcca1c1d18~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-10">API</h2>
<h3 data-id="heading-11">creatorStore</h3>
<p>创建 store 对象</p>
<h3 data-id="heading-12">appleMiddleware</h3>
<p>使用中间件 在下一讲中间件中会提到</p>
<h3 data-id="heading-13">bindActionCreators</h3>
<p>该 Api 用于将 action 和 dispatch 绑定 从而使组件可以无感知 Redux 的存在</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; dispatch &#125; = useDispatch();
<span class="hljs-keyword">const</span> _bindActionCreators = bindActionCreators(
  &#123;
    <span class="hljs-comment">// 定义好的一些actionCreators</span>
    addCounter,
    subCounter,
  &#125;,
  dispatch
);

<span class="hljs-comment">// 这样就可以派发一个action了</span>
_bindActionCreators.addCounter();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">combineReducers</h3>
<p>当我们的页面变得越来越复杂的时候 可能我们需要针对模块拆分不同的 Store</p>
<p>这个 Api 就可以帮我们重新组合这些 Store 变成一个 Store</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56c63afe59dd44798b3f1f8f61eafacc~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-15">connect</h3>
<p>用于将 Store 和 Action 映射到组件的 props 上</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aead73d371b4df6ae18e9028dc0c624~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-16">compose</h3>
<p>compose 是函数式编程中的方法 用来从右到左来组合多个函数</p>
<p>本文只做 Redux 的入门 所以 compose 这个函数可以在函数式编程中深究</p>
<h2 data-id="heading-17">Redux DevTools</h2>
<p>这是一个 Chrome 的插件 可以让我们更好的调试我们的 Redux</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11f100b78b3441c8adbf311582af1290~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-18">react-redux</h2>
<p>这是一个用于将你的组件和 Redux 更方便连接的组件库</p>
<p>使用 如下</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> &#123; Provider, useDispatch, useSelector &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>;

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">A</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">B</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">C</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此一来 A B C 组件便都有能力获取到 Store 中的数据了</p>
<p>具体的用法 可以看接下来的 Demo</p>
<h2 data-id="heading-19">Demo</h2>
<p>这里我用一个计数器的 🌰 来快速过一遍 Redux</p>
<p>首先 创建我们的 store</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 导入核心API 创建Store</span>
<span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>;

<span class="hljs-keyword">interface</span> IStore &#123;
  <span class="hljs-attr">count</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> IAction &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-built_in">string</span>;
  [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span>;
&#125;

<span class="hljs-comment">// 定义我们的 Action Type</span>
<span class="hljs-built_in">enum</span> ACTION_TYPE &#123;
  ADD_COUNTER = <span class="hljs-string">'ADD_COUNTER'</span>,
  SUB_COUNTER = <span class="hljs-string">'SUB_COUNTER'</span>,
&#125;

<span class="hljs-comment">// 对外暴露 Action Creators 用于组件调用</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> addCounter = <span class="hljs-function">(<span class="hljs-params">payload: <span class="hljs-built_in">number</span></span>) =></span> (&#123;
  <span class="hljs-attr">type</span>: ACTION_TYPE.ADD_COUNTER,
  payload,
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> subCounter = <span class="hljs-function">(<span class="hljs-params">payload: <span class="hljs-built_in">number</span></span>) =></span> (&#123;
  <span class="hljs-attr">type</span>: ACTION_TYPE.SUB_COUNTER,
  payload,
&#125;);

<span class="hljs-comment">// 创建一个初始化的Store</span>
<span class="hljs-keyword">const</span> initStore: IStore = &#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
&#125;;

<span class="hljs-comment">// 创建Reducer 用于管理 View 派发过来的 Action</span>
<span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">store = initStore, action: IAction</span>) =></span> &#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> ACTION_TYPE.ADD_COUNTER:
      <span class="hljs-keyword">return</span> &#123; ...store, <span class="hljs-attr">count</span>: store.count + action.payload &#125;;
    <span class="hljs-keyword">case</span> ACTION_TYPE.SUB_COUNTER:
      <span class="hljs-keyword">return</span> &#123; ...store, <span class="hljs-attr">count</span>: store.count - action.payload &#125;;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> store;
  &#125;
&#125;;

<span class="hljs-comment">// 创建 Store 这里我们还开启了 Redux DEVTools</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> store = createStore(
  reducer,
  (<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).__REDUX_DEVTOOLS_EXTENSION_COMPOSE__()
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>视图层的代码如下</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; Button, Input &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> &#123; Provider, useDispatch, useSelector &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>;
<span class="hljs-keyword">import</span> &#123; store, addCounter, subCounter, IStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 获取 Store 中的数据</span>
  <span class="hljs-keyword">const</span> &#123; count &#125; = useSelector(<span class="hljs-function">(<span class="hljs-params">store: IStore</span>) =></span> store);
  <span class="hljs-keyword">const</span> dispatch = useDispatch();
  <span class="hljs-keyword">const</span> [payload, setPayload] = useState<<span class="hljs-built_in">number</span>>(<span class="hljs-number">1</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">Input</span>
        <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;payload&#125;</span>
        <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(v)</span> =></span> setPayload(parseInt(v.target.value))&#125;
      />
      <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch(addCounter(payload))&#125;>+<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch(subCounter(payload))&#125;>-<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Root</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">思考</h2>
<p>本文中的 reducers 都是同步代码 如果我们在发送 action 的时候 需要执行一些异步操作 这个时候应该怎么办呢</p>
<p>reducer 中是否可以处理异步操作呢 ？？？</p></div>  
</div>
            