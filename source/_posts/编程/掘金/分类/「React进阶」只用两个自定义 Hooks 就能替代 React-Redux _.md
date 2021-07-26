
---
title: '「React进阶」只用两个自定义 Hooks 就能替代 React-Redux _'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365036e1c9f44c648f6203b9b950c736~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 16:22:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365036e1c9f44c648f6203b9b950c736~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>之前有朋友问我，React Hooks 能否解决 React 项目状态管理的问题。这个问题让我思索了很久，最后得出的结论是：<strong>能，不过需要两个自定义 hooks 去实现</strong>。那么具体如何实现的呢？ 那就是今天要讲的内容了。</p>
<p>通过本文，你能够学习以下内容：</p>
<ul>
<li>useContext ，useRef ，useMemo，useEffect 的基本用法。</li>
<li>如何将不同组件的自定义 hooks 建立通信，共享状态。</li>
<li>合理编写自定义 hooks ， 分析 hooks 之间的依赖关系。</li>
<li>自定义 hooks 编写过程中一些细节问题。</li>
</ul>
<p>带着如上的知识点，开启阅读之旅吧～（创作不易，希望屏幕前的你能给笔者赏个赞，以此鼓励我继续创作前端硬文。）</p>
<h2 data-id="heading-1">一 设计思路</h2>
<p>首先，看一下要实现的两个自定义 hooks 具体功能。</p>
<ul>
<li><code>useCreateStore</code> 用于产生一个状态 Store ，通过 context 上下文传递 ，为了让每一个自定义 hooks <code>useConnect</code> 都能获取 context 里面的状态属性。</li>
<li><code>useConnect</code> 使用这个自定义 hooks 的组件，可以获取改变状态的 dispatch 方法，还可以订阅 state ，被订阅的 state 发生变化，组件更新。</li>
</ul>
<p><strong>如何让不同组件的自定义 hooks 共享状态并实现通信呢？</strong></p>
<p>首先不同组件的自定义 hooks ，可以通过 <code>useContext</code> 获得共有状态，而且还需要实现状态管理和组件通信，那么就需要一个状态调度中心来统一做这些事，可以称之为 <code>ReduxHooksStore</code> ，它具体做的事情如下：</p>
<ul>
<li>全局管理 state， state 变化，通知对应组件更新。</li>
<li>收集使用 <code>useConnect</code> 组件的信息。组件销毁还要清除这些信息。</li>
<li>维护并传递负责更新的 <code>dispatch</code> 方法。</li>
<li>一些重要 api 要暴露给 context 上下文，传递给每一个 <code>useConnect</code>。</li>
</ul>
<h3 data-id="heading-2">1 useCreateStore 设计</h3>
<p>首先 <code>useCreateStore</code> 是在靠近根部组件的位置的， 而且全局只需要一个，目的就是创建一个 <code>Store</code> ，并通过 <code>Provider</code> 传递下去。</p>
<p>使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> store = useCreateStore( reducer , initState )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数：</p>
<ul>
<li><code>reducer</code> ：全局 reducer，纯函数，传入 state 和 action ，返回新的 state 。</li>
<li><code>initState</code> ： 初始化 state 。</li>
</ul>
<p>返回值：为 store 暴露的主要功能函数。</p>
<h3 data-id="heading-3">2 Store设计</h3>
<p>Store 为上述所说的调度中心，接收全局 reducer ，内部维护状态 state ，负责通知更新 ，收集用 useConnect 的组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Store = <span class="hljs-keyword">new</span> ReduxHooksStore(reducer,initState).exportStore()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数：接收两个参数，透传 useCreateStore 的参数。</p>
<h3 data-id="heading-4">3 useConnect设计</h3>
<p>使用 useConnect 的组件，将获得 dispatch 函数，用于更新 state ，还可以通过第一个参数订阅 state ，被订阅的 state 改变 ，会让组件更新。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 订阅 state 中的 number </span>
<span class="hljs-keyword">const</span> mapStoreToState = <span class="hljs-function">(<span class="hljs-params">state</span>)=></span>(&#123; <span class="hljs-attr">number</span>: state.number  &#125;)
<span class="hljs-keyword">const</span> [ state , dispatch ] = useConnect(mapStoreToState)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数：</p>
<ul>
<li><code>mapStoreToState</code>：将 Store 中 state ，映射到组件的 state 中，可以做视图渲染使用。</li>
<li>如果没有第一个参数，那么只提供 <code>dispatch</code> 函数，不会订阅 state 变化带来的更新。</li>
</ul>
<p>返回值：返回值是一个数组。</p>
<ul>
<li>数组第一项：为映射的 state 的值。</li>
<li>数组第二项：为改变 state 的 <code>dispatch</code> 函数。</li>
</ul>
<h3 data-id="heading-5">4 原理图</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365036e1c9f44c648f6203b9b950c736~tplv-k3u1fbpfcp-watermark.image" alt="7.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">二 useCreateStore</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ReduxContext = React.createContext(<span class="hljs-literal">null</span>)
<span class="hljs-comment">/* 用于产生 reduxHooks 的 store */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useCreateStore</span>(<span class="hljs-params">reducer,initState</span>)</span>&#123;
   <span class="hljs-keyword">const</span> store = React.useRef(<span class="hljs-literal">null</span>)
   <span class="hljs-comment">/* 如果存在——不需要重新实例化 Store */</span>
   <span class="hljs-keyword">if</span>(!store.current)&#123;
       store.current  = <span class="hljs-keyword">new</span> ReduxHooksStore(reducer,initState).exportStore()
   &#125;
   <span class="hljs-keyword">return</span> store.current
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useCreateStore</code> 主要做的是：</p>
<ul>
<li>
<p>接收 <code>reducer</code> 和 <code>initState</code> ，通过 ReduxHooksStore 产生一个 store ，不期望把 store 全部暴露给使用者，只需要暴露核心的方法，所以调用实例下的 <code>exportStore</code>抽离出核心方法。</p>
</li>
<li>
<p>使用一个 <code>useRef</code> 保存核心方法，传递给 <code>Provider</code> 。</p>
</li>
</ul>
<h2 data-id="heading-7">三 状态管理者 —— ReduxHooksStore</h2>
<p>接下来看一下核心状态 ReduxHooksStore 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; unstable_batchedUpdates &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReduxHooksStore</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">reducer,initState</span>)</span>&#123;
       <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'__ReduxHooksStore__'</span>
       <span class="hljs-built_in">this</span>.id = <span class="hljs-number">0</span>
       <span class="hljs-built_in">this</span>.reducer = reducer
       <span class="hljs-built_in">this</span>.state = initState
       <span class="hljs-built_in">this</span>.mapConnects = &#123;&#125;
    &#125;
    <span class="hljs-comment">/* 需要对外传递的接口 */</span>
    exportStore=<span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">dispatch</span>:<span class="hljs-built_in">this</span>.dispatch.bind(<span class="hljs-built_in">this</span>),
            <span class="hljs-attr">subscribe</span>:<span class="hljs-built_in">this</span>.subscribe.bind(<span class="hljs-built_in">this</span>),
            <span class="hljs-attr">unSubscribe</span>:<span class="hljs-built_in">this</span>.unSubscribe.bind(<span class="hljs-built_in">this</span>),
            <span class="hljs-attr">getInitState</span>:<span class="hljs-built_in">this</span>.getInitState.bind(<span class="hljs-built_in">this</span>)
        &#125;
    &#125;
    <span class="hljs-comment">/* 获取初始化 state */</span>
    getInitState=<span class="hljs-function">(<span class="hljs-params">mapStoreToState</span>)=></span>&#123;
        <span class="hljs-keyword">return</span> mapStoreToState(<span class="hljs-built_in">this</span>.state)
    &#125;
    <span class="hljs-comment">/* 更新需要更新的组件 */</span>
    publicRender=<span class="hljs-function">()=></span>&#123;
        unstable_batchedUpdates(<span class="hljs-function">()=></span>&#123; <span class="hljs-comment">/* 批量更新 */</span>
            <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>.mapConnects).forEach(<span class="hljs-function"><span class="hljs-params">name</span>=></span>&#123;
                <span class="hljs-keyword">const</span> &#123; update &#125; = <span class="hljs-built_in">this</span>.mapConnects[name]
                update(<span class="hljs-built_in">this</span>.state)
            &#125;)
        &#125;)
    &#125;
    <span class="hljs-comment">/* 更新 state  */</span>
    dispatch=<span class="hljs-function">(<span class="hljs-params">action</span>)=></span>&#123;
       <span class="hljs-built_in">this</span>.state = <span class="hljs-built_in">this</span>.reducer(<span class="hljs-built_in">this</span>.state,action)
       <span class="hljs-comment">// 批量更新</span>
       <span class="hljs-built_in">this</span>.publicRender()
    &#125;
    <span class="hljs-comment">/* 注册每个 connect  */</span>
    subscribe=<span class="hljs-function">(<span class="hljs-params">connectCurrent</span>)=></span>&#123;
        <span class="hljs-keyword">const</span> connectName = <span class="hljs-built_in">this</span>.name + (++<span class="hljs-built_in">this</span>.id)
        <span class="hljs-built_in">this</span>.mapConnects[connectName] =  connectCurrent
        <span class="hljs-keyword">return</span> connectName
    &#125;
    <span class="hljs-comment">/* 解除绑定 */</span>
    unSubscribe=<span class="hljs-function">(<span class="hljs-params">connectName</span>)=></span>&#123;
        <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.mapConnects[connectName]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">状态</h4>
<ul>
<li><code>reducer</code>：这个 reducer 为全局的 reducer ，由 useCreateStore 传入。</li>
<li><code>state</code>：全局保存的状态 state ，每次执行 reducer 会得到新的 state 。</li>
<li><code>mapConnects</code>：里面保存每一个 useConnect 组件的更新函数。用于派发 state 改变带来的更新。</li>
</ul>
<h4 data-id="heading-9">方法</h4>
<p><strong>负责初始化：</strong></p>
<ul>
<li><code>getInitState</code>：这个方法给自定义 hooks 的 useConnect 使用，用于获取初始化的 state 。</li>
<li><code>exportStore</code>：这个方法用于把 ReduxHooksStore 提供的核心方法传递给每一个 useConnect 。</li>
</ul>
<p><strong>负责绑定｜解绑：</strong></p>
<ul>
<li><code>subscribe</code>： 绑定每一个自定义 hooks useConnect 。</li>
<li><code>unSubscribe</code>：解除绑定每一个 hooks 。</li>
</ul>
<p><strong>负责更新：</strong></p>
<ul>
<li>
<p><code>dispatch</code>：这个方法提供给业务组件层，每一个使用 useConnect 的组件可以通过 dispatch 方法改变 state ，内部原理是通过调用 reducer 产生一个新的 state 。</p>
</li>
<li>
<p><code>publicRender</code>：当 state 改变需要通知每一个使用 useConnect 的组件，这个方法就是通知更新，至于组件需不需要更新，那是 useConnect  内部需要处理的事情，这里还有一个细节，就是考虑到 dispatch 的触发场景可以是异步状态下，所以用 React-DOM 中 unstable_batchedUpdates 开启批量更新原则。</p>
</li>
</ul>
<h2 data-id="heading-10">四 useConnect</h2>
<p>useConnect 是整个功能的核心部分，它要做的事情是获取最新的 <code>state</code> ，然后通过订阅函数 <code>mapStoreToState</code> 得到订阅的 state ，判断订阅的 state 是否发生变化。如果发生变化渲染最新的 state 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useConnect</span>(<span class="hljs-params">mapStoreToState=()=>&#123;&#125;</span>)</span>&#123;
    <span class="hljs-comment">/* 获取 Store 内部的重要函数 */</span>
   <span class="hljs-keyword">const</span> contextValue = React.useContext(ReduxContext)
   <span class="hljs-keyword">const</span> &#123; getInitState , subscribe ,unSubscribe , dispatch &#125; = contextValue
   <span class="hljs-comment">/* 用于传递给业务组件的 state  */</span>
   <span class="hljs-keyword">const</span> stateValue = React.useRef(getInitState(mapStoreToState))

   <span class="hljs-comment">/* 渲染函数 */</span>
   <span class="hljs-keyword">const</span> [ , forceUpdate ] = React.useState()
   <span class="hljs-comment">/* 产生 */</span>
   <span class="hljs-keyword">const</span> connectValue = React.useMemo(<span class="hljs-function">()=></span>&#123;
       <span class="hljs-keyword">const</span> state =  &#123;
           <span class="hljs-comment">/* 用于比较一次 dispatch 中，新的 state 和 之前的state 是否发生变化  */</span>
           <span class="hljs-attr">cacheState</span>: stateValue.current,
           <span class="hljs-comment">/* 更新函数 */</span>
           <span class="hljs-attr">update</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">newState</span>) </span>&#123;
               <span class="hljs-comment">/* 获取订阅的 state */</span>
               <span class="hljs-keyword">const</span> selectState = mapStoreToState(newState)
               <span class="hljs-comment">/* 浅比较 state 是否发生变化，如果发生变化， */</span>
               <span class="hljs-keyword">const</span> isEqual = shallowEqual(state.cacheState,selectState)
               state.cacheState = selectState
               stateValue.current  = selectState
               <span class="hljs-keyword">if</span>(!isEqual)&#123;
                   <span class="hljs-comment">/* 更新 */</span>
                   forceUpdate(&#123;&#125;)
               &#125;
           &#125;
       &#125;
       <span class="hljs-keyword">return</span> state
   &#125;,[ contextValue ]) <span class="hljs-comment">// 将 contextValue 作为依赖项。</span>

   React.useEffect(<span class="hljs-function">()=></span>&#123;
       <span class="hljs-comment">/* 组件挂载——注册 connect */</span>
       <span class="hljs-keyword">const</span> name =  subscribe(connectValue)
       <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-comment">/* 组件卸载 —— 解绑 connect */</span>
           unSubscribe(name)
       &#125;
   &#125;,[ connectValue ]) <span class="hljs-comment">/* 将 connectValue 作为 useEffect 的依赖项 */</span>

   <span class="hljs-keyword">return</span> [ stateValue.current , dispatch ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>初始化</strong></p>
<ul>
<li>用 useContext 获取上下文中， ReduxHooksStore 提供的核心函数。</li>
<li>用 useRef 来保存得到的最新的 state 。</li>
<li>用 useState 产生一个更新函数 <code>forceUpdate</code> ，这个函数只是更新组件。</li>
</ul>
<p><strong>注册｜解绑流程</strong></p>
<ul>
<li>
<p>注册： 通过 <code>useEffect</code> 来向 ReduxHooksStore 中注册当前 useConnect 产生的 connectValue ，connectValue 是什么马上会讲到。subscribe 用于注册，会返回当前 connectValue 的唯一标识 name 。</p>
</li>
<li>
<p>解绑：在 useEffect 的销毁函数中，可以用调用 unSubscribe 传入 name 来解绑当前的 connectValue</p>
</li>
</ul>
<p><strong>connectValue是否更新组件</strong></p>
<ul>
<li>
<p>connectValue ：真正地向 ReduxHooksStore 注册的状态，首先用 <code>useMemo</code> 来对 connectValue 做缓存，connectValue 为一个对象，里面的 cacheState 保留了上一次的 mapStoreToState 产生的 state ，还有一个负责更新的 update 函数。</p>
</li>
<li>
<p><strong>更新流程</strong> ： 当触发 <code>dispatch</code> 在 ReduxHooksStore 中，会让每一个 connectValue 的 update 都执行， update 会触发映射函数 <code>mapStoreToState</code> 来得到当前组件想要的 state 内容。然后通过 <code>shallowEqual</code> 浅比较新老 state 是否发生变化，如果发生变化，那么更新组件。完成整个流程。</p>
</li>
<li>
<p>shallowEqual ： 这个浅比较就是 React 里面的浅比较，在第 11 章已经讲了其流程，这里就不讲了。</p>
</li>
</ul>
<p><strong>分清依赖关系</strong></p>
<ul>
<li>
<p>首先自定义 hooks useConnect 的依赖关系是上下文 contextValue 改变，那么说明 store 发生变化，所以重新通过 useMemo 产生新的 connectValue 。<strong>所以 useMemo 依赖 contextValue。</strong></p>
</li>
<li>
<p>connectValue 改变，那么需要解除原来的绑定关系，重新绑定。<strong>useEffect 依赖 connectValue。</strong></p>
</li>
</ul>
<p><strong>局限性</strong></p>
<p>整个 useConnect 有一些局限性，比如：</p>
<ul>
<li>没有考虑 mapStoreToState 可变性，无法动态传入 mapStoreToState 。</li>
<li>浅比较，不能深层次比较引用数据类型。</li>
</ul>
<h2 data-id="heading-11">五 使用与验证效果</h2>
<p>接下来就是验证效果环节，我模拟了组件通信的场景。</p>
<h3 data-id="heading-12">根部组件注入 Store</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ReduxContext , useConnect , useCreateStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./hooks/useRedux'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>  <span class="hljs-title">Index</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [ isShow , setShow ] =  React.useState(<span class="hljs-literal">true</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'index 渲染'</span>)
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">CompA</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">CompB</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">CompC</span> /></span>
        &#123;isShow &&  <span class="hljs-tag"><<span class="hljs-name">CompD</span> /></span>&#125;
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setShow(!isShow)&#125; >点击<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Root</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> store = useCreateStore(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">state,action</span>)</span>&#123;
        <span class="hljs-keyword">const</span> &#123; type , payload &#125; =action
        <span class="hljs-keyword">if</span>(type === <span class="hljs-string">'setA'</span> )&#123;
            <span class="hljs-keyword">return</span> &#123;
                ...state,
                <span class="hljs-attr">mesA</span>:payload
            &#125;
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(type === <span class="hljs-string">'setB'</span>)&#123;
            <span class="hljs-keyword">return</span> &#123;
                ...state,
                <span class="hljs-attr">mesB</span>:payload
            &#125;
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(type === <span class="hljs-string">'clear'</span>)&#123; <span class="hljs-comment">//清空</span>
            <span class="hljs-keyword">return</span>  &#123; <span class="hljs-attr">mesA</span>:<span class="hljs-string">''</span>,<span class="hljs-attr">mesB</span>:<span class="hljs-string">''</span> &#125;
        &#125;
        <span class="hljs-keyword">else</span>&#123;
            <span class="hljs-keyword">return</span> state
        &#125;
    &#125;,
    &#123; <span class="hljs-attr">mesA</span>:<span class="hljs-string">'111'</span>,<span class="hljs-attr">mesB</span>:<span class="hljs-string">'111'</span> &#125;)
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ReduxContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;store&#125;</span> ></span>
            <span class="hljs-tag"><<span class="hljs-name">Index</span>/></span>
        <span class="hljs-tag"></<span class="hljs-name">ReduxContext.Provider</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Root根组件</strong></p>
<ul>
<li>通过 useCreateStore 创建一个 store ，传入 reducer 和 初始化的值 <code>&#123; mesA:'111',mesB:'111' &#125;</code></li>
<li>用 Provider 传递 store。</li>
</ul>
<p><strong>Index组件</strong></p>
<ul>
<li>有四个子组件 CompA ， CompB ，CompC ，CompD 。其中 CompD 是 动态挂载的。</li>
</ul>
<h3 data-id="heading-13">业务组件使用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompA</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [ value ,setValue ] = useState(<span class="hljs-string">''</span>)
    <span class="hljs-keyword">const</span> [state ,dispatch ] = useConnect(<span class="hljs-function">(<span class="hljs-params">state</span>)=></span> (&#123; <span class="hljs-attr">mesB</span> : state.mesB &#125;) )
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"component_box"</span> ></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span> 组件A<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>组件B对我说 ： &#123;state.mesB&#125; <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span>=></span>setValue(e.target.value)&#125;
            placeholder="对B组件说"
        />
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span> dispatch(&#123; type:'setA' ,payload:value &#125;)&#125; >确定<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompB</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [ value ,setValue ] = useState(<span class="hljs-string">''</span>)
    <span class="hljs-keyword">const</span> [state ,dispatch ] = useConnect(<span class="hljs-function">(<span class="hljs-params">state</span>)=></span> (&#123; <span class="hljs-attr">mesA</span> : state.mesA &#125;) )
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"component_box"</span> ></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span> 组件B<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>组件A对我说 ： &#123;state.mesA&#125; <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span>=></span>setValue(e.target.value)&#125;
            placeholder="对A组件说"
        />
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span> dispatch(&#123; type:'setB' ,payload:value &#125;)&#125; >确定<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompC</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [state  ] = useConnect(<span class="hljs-function">(<span class="hljs-params">state</span>)=></span> (&#123; <span class="hljs-attr">mes1</span> : state.mesA,<span class="hljs-attr">mes2</span> : state.mesB &#125;) )
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"component_box"</span> ></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>组件A ： &#123;state.mes1&#125; <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>组件B ： &#123;state.mes2&#125; <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompD</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [ ,dispatch  ] = useConnect( )
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'D 组件更新'</span>)
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"component_box"</span> ></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span> dispatch(&#123; type:'clear' &#125;)&#125; > 清空 <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>CompA 和 CompB 模拟组件双向通信。</li>
<li>CompC 组件接收 CompA 和 CompB 通信内容，并映射到 <code>mes1 ，mes2</code> 属性上。</li>
<li>CompD 没有 mapStoreToState ，没有订阅 state ，state 变化组件不会更新，只是用 dispatch 清空状态。</li>
</ul>
<h3 data-id="heading-14">效果</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7b06820f28f461c91620d7240b63ed5~tplv-k3u1fbpfcp-watermark.image" alt="8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">六 总结</h2>
<p>本文通过两个自定义 hooks 实现了 React-Redux 的基本功能，这个模式在真实项目中可以使用吗？ 我觉得如果是小型项目，是完全可以使用的，对于大型项目还是用 React Redux 或者其他成熟的状态管理工具。</p>
<h3 data-id="heading-16">《React进阶实践指南》小册已经上线</h3>
<p>今天给大家推荐一本掘金小册 <strong>《React进阶实践指南》</strong>，本文中的自定义 hooks 也是小册自定义 hooks 章节中的一个案例。小册还有很多自定义 hooks 设计案例，而且自定义 hooks 设计和实践章节都在持续更新维护中，汇聚了笔者多年的心血，感兴趣的同学可以了解以下，下面是小册的介绍。</p>
<p>本小册从基础进阶篇，优化进阶篇，原理进阶篇，生态进阶篇，实践进阶篇，五个方向详细探讨 React 使用指南 和 原理介绍。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/491a1a2e509b4d2c892f68e64864be36~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在基础进阶篇里，将重新认识react中 state，props，ref，context等模块，详解其基本使用和高阶玩法。</li>
<li>在优化进阶篇里，将讲解 React性能调优和细节处理，让React写的更优雅。</li>
<li>在原理进阶篇里，将针对React几个核心模块原理进行阐述，一次性搞定面试遇到React原理问题。</li>
<li>在生态进阶篇里，将重温React重点生态的用法，从原理角度分析内部运行的机制。</li>
<li>在实践进阶篇里，将串联前几个模块，进行强化实践。</li>
</ul>
<p>至于小册为什么叫进阶实践指南，因为在讲解进阶玩法的同时，也包含了很多实践的小demo。还有一些面试中的问答环节，让读者从面试上脱颖而出。</p>
<p>目前小册已经上线，这里有 2 个 7 折的优惠码奉上，先到先得。</p>
<ul>
<li>小册 7 折优惠码： <strong>cRftnJvJ</strong></li>
<li>小册 7 折优惠码： <strong>5EPxuNV5</strong></li>
</ul></div>  
</div>
            