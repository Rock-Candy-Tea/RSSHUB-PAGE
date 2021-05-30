
---
title: '【进阶探索】从源码分析Redux 和 Mobx 那个更优美 ，一起探索谁丝滑！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c04606f187344b8ad42a868b4df2971~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 02:32:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c04606f187344b8ad42a868b4df2971~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>探索Redux 和 Mobx 原理从我做起，从这篇文章看起！</p>
<h1 data-id="heading-1">所以</h1>
<p>一位程序员的职业生涯大约十年，只有人寿命的十分之一。前端项目只是你生活工作的一部分，而你却是它的全部，你是他的灵魂。请放下长时间的游戏、工作时的摸鱼。多学习来以最完美的状态好好陪你项目！</p>
<h1 data-id="heading-2">正文</h1>
<p>这篇文章将会详细分析 Redux 和 Mobx 核心 Api, 看一遍学不会就看两次、三次、手写一次！</p>
<h2 data-id="heading-3">知识点</h2>
<ul>
<li>Redux 基本使用（没有）</li>
<li>createStore</li>
<li>bindActionCreators</li>
<li>combineReducers</li>
<li>applyMiddleware</li>
<li>彩蛋 <code>thunk</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c04606f187344b8ad42a868b4df2971~tplv-k3u1fbpfcp-watermark.image" alt="Redux.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Mobx 基本使用（没有）</li>
<li>observable</li>
<li>autorun</li>
<li>observer</li>
</ul>
<p>这个 代码很多哦 ， 我这菜鸟看不懂 ，我看了文章，应该能实现 这些api 和 vue的的 响应式差不多.</p>
<h3 data-id="heading-4">Redux</h3>
<h4 data-id="heading-5">createStore</h4>
<p>这个是个比较核心的函数之创建仓库，分为了3个核心函数 <code>dispatch</code>,<code>getState</code>,<code>subscribe</code></p>
<p>这三个函数的基本使用是这样的...</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 构建仓库</span>
<span class="hljs-keyword">const</span> store = createStore(reducer);

<span class="hljs-keyword">const</span> unListen = store.subscribe(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"监听器1"</span>, store.getState());
&#125;)

store.dispatch(createAddUserAction(&#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"遇见同学"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">21</span>
&#125;));

unListen(); <span class="hljs-comment">//取消监听</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>本质就如思维导图思路</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31c90e6600474784b03c3083ffa4f4bd~tplv-k3u1fbpfcp-watermark.image" alt="createStore" loading="lazy" referrerpolicy="no-referrer"></p>
<p>基本实现且看代码的详细解释</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">/**
 * 得到一个指定长度的随机字符串
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>length 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandomString</span>(<span class="hljs-params">length</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.random().toString(<span class="hljs-number">36</span>).substr(<span class="hljs-number">2</span>, length).split(<span class="hljs-string">""</span>).join(<span class="hljs-string">"."</span>)
&#125;

<span class="hljs-comment">/**
 * 判断某个对象是否是一个plain-object
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>obj 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isPlainObject</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj !== <span class="hljs-string">"object"</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.getPrototypeOf(obj) === <span class="hljs-built_in">Object</span>.prototype;
&#125;

<span class="hljs-comment">// 上面连个都为辅助工具函数</span>

<span class="hljs-comment">/**
 * 实现createStore的功能
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>reducer reducer
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> </span>defaultState 默认的状态值
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params">reducer, defaultState</span>) </span>&#123;
    <span class="hljs-keyword">let</span> currentReducer = reducer, <span class="hljs-comment">//当前使用的reducer</span>
        currentState = defaultState; <span class="hljs-comment">//当前仓库中的状态</span>

    <span class="hljs-keyword">const</span> listeners = [];  <span class="hljs-comment">//记录所有的监听器（订阅者）</span>

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span>(<span class="hljs-params">action</span>) </span>&#123;
        <span class="hljs-comment">//验证action</span>
        <span class="hljs-keyword">if</span> (!isPlainObject(action)) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"action must be a plain object"</span>);
        &#125;
        <span class="hljs-comment">//验证action的type属性是否存在</span>
        <span class="hljs-keyword">if</span> (action.type === <span class="hljs-literal">undefined</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"action must has a property of type"</span>);
        &#125;
        currentState = currentReducer(currentState, action)
        <span class="hljs-comment">//运行所有的订阅者（监听器）</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> listener <span class="hljs-keyword">of</span> listeners) &#123;
            listener();
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getState</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> currentState;
    &#125;

    <span class="hljs-comment">/**
     * 添加一个监听器（订阅器）
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">subscribe</span>(<span class="hljs-params">listener</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> listener !== <span class="hljs-string">'function'</span>) &#123;
              <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(
                <span class="hljs-string">`Expected the listener to be a function. Instead, received: '<span class="hljs-subst">$&#123;kindOf(
                  listener
                )&#125;</span>'`</span>
              )
            &#125;
        listeners.push(listener); <span class="hljs-comment">//将监听器加入到数组中</span>
        <span class="hljs-keyword">let</span> isSubscribed = <span class="hljs-literal">false</span>;<span class="hljs-comment">//是否已经移除掉了</span>
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">if</span> (isSubscribed) &#123;
                <span class="hljs-keyword">return</span>;
            &#125;
            <span class="hljs-comment">//将listener从数组中移除</span>
            <span class="hljs-keyword">const</span> index = listeners.indexOf(listener);
            listeners.splice(index, <span class="hljs-number">1</span>);
            isSubscribed = <span class="hljs-literal">true</span>;
        &#125;
    &#125;

    <span class="hljs-comment">//创建仓库时，需要分发一次初始的action</span>
    dispatch(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">`@@redux/PROBE_UNKNOWN_ACTION<span class="hljs-subst">$&#123;getRandomString(<span class="hljs-number">6</span>)&#125;</span>`</span>
    &#125;)

    <span class="hljs-keyword">return</span> &#123;
        dispatch,
        getState,
        subscribe
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现的代码基本对标 <a href="https://github.com/reduxjs/redux/blob/54304330007b8d7c1db5825b42f5238773a7ee2e/src/createStore.ts#L238" target="_blank" rel="nofollow noopener noreferrer">Github Redux</a></p>
<p>由于官方使用的是Ts 写的 阅读起来可能更加困难</p>
<p>所以过滤许多的细节处理和TS，将本质的思维呈现出来！</p>
<p>从入口带你理解下一个核心函数<code>bindActionCreators</code></p>
<h4 data-id="heading-6">bindActionCreators</h4>
<ul>
<li>作用
用于返回可直接调用的 <code>dispatch</code> 的函数方法</li>
<li>参数
<ul>
<li>object | function</li>
<li>(store.dispatch)</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> actionCreators = &#123;
    <span class="hljs-attr">addUser</span>: createAddUserAction,
    <span class="hljs-attr">deleteUser</span>: createDeleteUserAction
&#125;

<span class="hljs-comment">// 这可直接传入一个函数</span>
<span class="hljs-keyword">const</span> actions = bindActionCreators(actionCreators, store.dispatch)

actions.addUser(&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"遇见同学"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">21</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用还是非常简单的, 本质也是一个函数, 非常的精妙，一起看看吧！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ac2a6614b9d463f8b53970798e5a764~tplv-k3u1fbpfcp-watermark.image" alt="bindActionCreators" loading="lazy" referrerpolicy="no-referrer"></p>
<p>思路是这样，核心函数是另外一个<code>getAutoDispatchActionCreator</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;object | function &#125;</span> </span>actionCreators 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>dispatch 
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">actionCreators,dispatch</span>) </span>&#123;
    <span class="hljs-comment">// 为函数时 直接调用自动分发的action创建函数</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> actionCreators === <span class="hljs-string">'function'</span>)&#123;
        _getAutoDispatchActionCreator(actionCreators,dispatch)
     <span class="hljs-comment">// 为对象时 遍历对象 转化为已创建自动分发的action创建函数的对象</span>
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> actionCreators === <span class="hljs-string">'object'</span>)&#123;
        <span class="hljs-keyword">const</span> result = &#123;&#125;
        <span class="hljs-built_in">Object</span>.keys(actionCreators).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>)=></span>&#123;
            result[key] = _getAutoDispatchActionCreator(actionCreators[key],dispatch)
        &#125;)
        <span class="hljs-keyword">return</span> result
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"actionCreators must be an object or function which means action creator"</span>)
    &#125;

&#125;
<span class="hljs-comment">/**
 * 自动分发的action创建函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>actionCreator 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> </span>dispatch 
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_getAutoDispatchActionCreator</span>(<span class="hljs-params">actionCreator, dispatch</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>)</span>&#123;
       <span class="hljs-keyword">return</span> dispatch(actionCreator(...args))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是豁然开朗了，乘热打铁进入下一个函数吧<code>combineReducers</code></p>
<h4 data-id="heading-7">combinReducers</h4>
<p>基本思路是这样的</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/762b32ee204e4db59bf6701bc0b1d59d~tplv-k3u1fbpfcp-watermark.image" alt="combinReducers" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">**
 * 合并reducers函数
 * @param &#123;object&#125; reducers 
 * @returns 
 */
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">reducers</span>) </span>&#123;
    validateReducers(reducers);
    <span class="hljs-comment">/**
     * 返回的是一个reducer函数
     */</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">state = &#123;&#125;, action</span>) </span>&#123;
        <span class="hljs-keyword">const</span> newState = &#123;&#125;; <span class="hljs-comment">//要返回的新的状态</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> reducers) &#123;
            <span class="hljs-keyword">if</span> (reducers.hasOwnProperty(key)) &#123;
                <span class="hljs-keyword">const</span> reducer = reducers[key];
                newState[key] = reducer(state[key], action);
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> newState; <span class="hljs-comment">//返回状态</span>
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">validateReducers</span>(<span class="hljs-params">reducers</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> reducers !== <span class="hljs-string">"object"</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"reducers must be an object"</span>);
    &#125;
    <span class="hljs-keyword">if</span> (!isPlainObject(reducers)) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"reducers must be a plain object"</span>);
    &#125;
    <span class="hljs-comment">//验证reducer的返回结果是不是undefined</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> reducers) &#123;
        <span class="hljs-keyword">if</span> (reducers.hasOwnProperty(key)) &#123;
            <span class="hljs-keyword">const</span> reducer = reducers[key];<span class="hljs-comment">//拿到reducer</span>
            <span class="hljs-comment">//传递一个特殊的type值</span>
            <span class="hljs-keyword">let</span> state = reducer(<span class="hljs-literal">undefined</span>, &#123;
                <span class="hljs-attr">type</span>:<span class="hljs-string">`@@redux/INIT<span class="hljs-subst">$&#123;getRandomString(<span class="hljs-number">6</span>)&#125;</span>`</span>
            &#125;)
            <span class="hljs-keyword">if</span> (state === <span class="hljs-literal">undefined</span>) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"reducers must not return undefined"</span>);
            &#125;
            state = reducer(<span class="hljs-literal">undefined</span>, &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">`@@redux/PROBE_UNKNOWN_ACTION<span class="hljs-subst">$&#123;getRandomString(<span class="hljs-number">6</span>)&#125;</span>`</span>
            &#125;)
            <span class="hljs-keyword">if</span> (state === <span class="hljs-literal">undefined</span>) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"reducers must not return undefined"</span>);
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来对比一下这个<a href="https://github.com/reduxjs/redux/blob/54304330007b8d7c1db5825b42f5238773a7ee2e/src/combineReducers.ts#L125" target="_blank" rel="nofollow noopener noreferrer">Redux 的 combinReducers</a>官方代码</p>
<p>总得来说这几个都属于辅助函数，而<code>createStore</code> 和 <code>传入的reducer</code> 才是调动整个 状态数据的核心, 不过Redux 提供了 一个核心机制 <code>中间件</code> 也是Redux 的灵魂之一。</p>
<p>接下来看下 <code>applyMiddleware</code> 是如何实现的</p>
<h4 data-id="heading-8">applyMiddleware</h4>
<p>像 <code>Koa</code> 、<code>Redux</code> 等优秀库都提供了中间思想, 中间件一出， 必有 <strong>组合函数</strong></p>
<p>我们看下 <code>Redux</code> 的组合函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span>(<span class="hljs-params">...funcs: <span class="hljs-built_in">Function</span>[]</span>) </span>&#123;
  <span class="hljs-keyword">return</span> funcs.reduce(
    <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span>
      <span class="hljs-function">(<span class="hljs-params">...args: any</span>) =></span>
        a(b(...args))
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>省略一些边界判断 ， 实现就一个 <code>reducer</code></p>
<p>就这一行</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">funcs.reduce(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> a(b(...args)))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数由内向外，返回作为 <code>reducer</code> 的新的累加值 依次执行 <code>b、a、...</code></p>
<p>再看看<code>applyMiddleware</code>函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> compose <span class="hljs-keyword">from</span> <span class="hljs-string">"./compose"</span>
<span class="hljs-comment">/**
 * 注册中间件
 * <span class="hljs-doctag">@param  <span class="hljs-type">&#123;...any&#125;</span> </span>middlewares 所有的中间件 本质是一个函数
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...middlewares</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createStore</span>) </span>&#123; <span class="hljs-comment">//给我创建仓库的函数</span>
        <span class="hljs-comment">//下面的函数用于创建仓库</span>
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">reducer, defaultState</span>) </span>&#123;
            <span class="hljs-comment">//创建仓库</span>
            <span class="hljs-keyword">const</span> store = createStore(reducer, defaultState);
            <span class="hljs-keyword">let</span> dispatch = <span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"目前还不能使用dispatch"</span>) &#125;;
            <span class="hljs-keyword">const</span> simpleStore = &#123;
                <span class="hljs-attr">getState</span>: store.getState,
                <span class="hljs-attr">dispatch</span>: <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> dispatch(...args)
            &#125;
            <span class="hljs-comment">//给dispatch赋值</span>
            <span class="hljs-comment">//根据中间件数组，得到一个dispatch创建函数的数组</span>
            <span class="hljs-keyword">const</span> dispatchProducers = middlewares.map(<span class="hljs-function"><span class="hljs-params">mid</span> =></span> mid(simpleStore));
            dispatch = compose(...dispatchProducers)(store.dispatch);
            <span class="hljs-keyword">return</span> &#123;
                ...store,
                dispatch
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以我理解干了这几件事</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29161cbeb432414aaac5cb53442158cb~tplv-k3u1fbpfcp-watermark.image" alt="applyMiddleware" loading="lazy" referrerpolicy="no-referrer"></p>
<p>调用返回了 一个具备以上能力的函数 抛出给 <code>createStore</code> 的第二个参数, 我们看看 <code>createStore</code> 有何改动</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params">reducer, defaultState, enhanced</span>) </span>&#123;
    <span class="hljs-comment">//enhanced表示applymiddleware返回的函数</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> defaultState === <span class="hljs-string">"function"</span>) &#123;
        <span class="hljs-comment">//第二个参数是应用中间件的函数返回值</span>
        enhanced = defaultState;
        defaultState = <span class="hljs-literal">undefined</span>;
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> enhanced === <span class="hljs-string">"function"</span>) &#123;
        <span class="hljs-comment">//进入applyMiddleWare的处理逻辑</span>
        <span class="hljs-keyword">return</span> enhanced(createStore)(reducer, defaultState);
    &#125;

   <span class="hljs-comment">// ....同上面代码</span>

    <span class="hljs-keyword">return</span> &#123;
        dispatch,
        getState,
        subscribe
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>执行<code>applyMiddleware</code> 返回一个需要仓库函数 的函数</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"> applyMiddleware(
        thunk, <span class="hljs-comment">// 返回中间件函数</span>
        logger
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接着 传入<code>createStore</code> 仓库函数函数本身 很巧妙</li>
<li>得到一个新的仓库构造函数 传入 <code>(reducer, defaultState)</code></li>
<li>用第一次传入的 <code>createStore</code> 和 <code>(reducer, defaultState)</code> 执行构造出没使用中间件的<strong>仓库</strong></li>
<li>挂载 <code>store</code> 和 <code>dispatch</code> 新对象传给 每一个中间件函数，返回新的<code>dispatch</code>数组</li>
<li>合并所有新的<code>dispatch</code>，执行第一次</li>
<li>返回 <code>store</code> 和 新的 <code>dispatch</code></li>
</ul>
<p>这便是 中间件的基本 运行流程 有些绕 <code>好好学习，天天向上</code></p>
<h4 data-id="heading-9">送你一个彩蛋 <code>thunk</code> 实现</h4>
<p>代码是个只有几行的函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createThunkMiddleware</span>(<span class="hljs-params">extraArgument</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">&#123; dispatch, getState &#125;</span>) =></span> <span class="hljs-function">(<span class="hljs-params">next</span>) =></span> <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> action === <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-keyword">return</span> action(dispatch, getState, extraArgument);
      &#125;
      <span class="hljs-keyword">return</span> next(action);
    &#125;;
  &#125;
  <span class="hljs-comment">// 创建 thunk 中间件</span>
  <span class="hljs-keyword">const</span> thunk = createThunkMiddleware();
  thunk.withExtraArgument = createThunkMiddleware;
  
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> thunk;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看图 我带你 穿起来 代码 一起解读</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/715da7a23ad2401095a4e4e5e1bf2d24~tplv-k3u1fbpfcp-watermark.image" alt="thunk" loading="lazy" referrerpolicy="no-referrer"></p>
<p>红色部分是 <code>中间件函数</code> 将 <code>dispatch, getState</code> 丢给 <code>thunk</code> , 接着返回函数</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da1752179a204e5382af8d4dd3ce6038~tplv-k3u1fbpfcp-watermark.image" alt="usethunk" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中红丝部分代表着 <code>thunk</code> 处理部分 , 判断是否 为 <strong>函数</strong> 不是就对给下步去执行</p>
<p>我们再看下 <code>next</code> 是什么。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9c04326a0d04c06b47a2bb6cf54effb~tplv-k3u1fbpfcp-watermark.image" alt="thunk" loading="lazy" referrerpolicy="no-referrer"></p>
<p>清晰的看一下 next 就是 <code>dispatch</code> 函数</p>
<p>后面两个 <code>action</code> 就是 一个普通 <strong>平面对象 类型</strong> 和 **异步函数 thunk 处理类型 **</p>
<h3 data-id="heading-10">Mobx</h3>
<p>Mobx 也是一款状态管理工具 ，但是思维模式不同</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b225fa2a0b6486ea5c2953dd4f5b107~tplv-k3u1fbpfcp-watermark.image" alt="Mobx" loading="lazy" referrerpolicy="no-referrer"></p>
<p>类似 Vue 响应式原理 ， 配合 <strong>观察者模式 收集依赖</strong> 实现</p>
<p>Api 有点多 我没看懂 ， 下面仅供参考</p>
<h4 data-id="heading-11">observable</h4>
<p>这个方法显而易见 构建出 一个 可观察的对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> reaction <span class="hljs-keyword">from</span> <span class="hljs-string">'./reaction'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observable</span>(<span class="hljs-params">target,key,descritor</span>)</span>&#123;
    <span class="hljs-comment">// 当使用装饰器 修饰属性时</span>
    <span class="hljs-keyword">if</span>( <span class="hljs-keyword">typeof</span> key === <span class="hljs-string">'string'</span>)&#123;
     <span class="hljs-keyword">let</span> Reaction = <span class="hljs-keyword">new</span> reaction
     <span class="hljs-keyword">let</span> v =  descritor.initailizer()
     v = createObservable(v)
     <span class="hljs-keyword">return</span> &#123;
       <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
       <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
       <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
        Reaction.collect()
        <span class="hljs-keyword">return</span> v
       &#125;,
       <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">value</span>)</span>&#123;
        v = value
        Reaction.run()
       &#125;,
     &#125;
    &#125;
      <span class="hljs-keyword">return</span> createObservable(target)
  &#125; 
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObservable</span>(<span class="hljs-params">val</span>)</span>&#123;
      <span class="hljs-keyword">let</span> handle = <span class="hljs-function">() =></span>&#123;
      <span class="hljs-keyword">let</span> Reaction = <span class="hljs-keyword">new</span> reaction
       <span class="hljs-keyword">return</span> &#123;
         <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target,key</span>)</span>&#123;
          Reaction.collect()
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(target,key)
         &#125;,
         <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target,key,value</span>)</span>&#123;
          <span class="hljs-keyword">let</span> v = <span class="hljs-built_in">Reflect</span>.set(target,key,value)
          Reaction.run()
          <span class="hljs-keyword">return</span> v
         &#125;,
       &#125;
      &#125;   
      <span class="hljs-keyword">return</span> deepProxy(val,handle)
  &#125;
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepProxy</span>(<span class="hljs-params">val,handle</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> val !== <span class="hljs-string">'object'</span>) <span class="hljs-keyword">return</span> val
  
    <span class="hljs-comment">// 从后往前依此实现代理</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> val)&#123;
      val[key] = deepProxy(val[key],handle)
    &#125;
  
    <span class="hljs-keyword">return</span> createObservable(val, handle())
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以很清楚的看到 这个函数实现了以下</p>
<ul>
<li>判断是否处于装饰器修饰使用状态</li>
<li>Proxy观察一个深度对象</li>
<li>在get时触发 依赖收集</li>
</ul>
<h4 data-id="heading-12">reaction</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> nowFn = <span class="hljs-literal">null</span>
<span class="hljs-keyword">let</span> counter = <span class="hljs-number">0</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Reaction</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.id = ++counter
    <span class="hljs-built_in">this</span>.store = &#123;&#125;

  &#125;
  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.store[<span class="hljs-built_in">this</span>.id])&#123;
      <span class="hljs-built_in">this</span>.store[<span class="hljs-built_in">this</span>.id].forEach(<span class="hljs-function"><span class="hljs-params">w</span>=></span>w())
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">collect</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">if</span>(nowFn)&#123;
      <span class="hljs-built_in">this</span>.store[<span class="hljs-built_in">this</span>.id] = <span class="hljs-built_in">this</span>.store[<span class="hljs-built_in">this</span>.id] || []
      <span class="hljs-built_in">this</span>.store[<span class="hljs-built_in">this</span>.id].push(nowFn)
    &#125;
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">start</span>(<span class="hljs-params">handle</span>)</span>&#123;
    nowFn = handle
  &#125;
  <span class="hljs-keyword">static</span> end ()&#123;
    nowFn = <span class="hljs-literal">null</span>
  &#125;
&#125;    
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">autorun</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">import</span> reaction <span class="hljs-keyword">from</span> <span class="hljs-string">'./reaction'</span>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">autorun</span>(<span class="hljs-params">handle</span>)</span>&#123;
    reaction.start()
    handle()
    reaction.end()
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再 看看 <code>autorun</code> 和 <code>reaction</code></p>
<p>基本就是一个简单的依赖收集 和 触发</p>
<p>相信 各位 知道 观察者模式 和 了解 Vue 依赖收集的对这样的写法并不陌生</p>
<p>而 最后的一个 <code>observer</code></p>
<h4 data-id="heading-14">observer</h4>
<pre><code class="copyable">/**
 * 装饰器 mobx-react 修饰类组件
 * @param &#123;*&#125; target 
 */
export default function observer(target)&#123;
    let cwm = target.prototype.componentWillMount;
    target.prototype.componentWillMount = function()&#123;
      cwm && cwm.call(this);
      autorun(()=>&#123;
        this.render();
        this.forceUpdate();
      &#125;)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个仅只是 修饰 react 类组件的 状态</p>
<h3 data-id="heading-15">对比</h3>
<h4 data-id="heading-16">Redux</h4>
<ul>
<li>单一数据源</li>
<li>状态数据只读</li>
<li>使用纯函数修改状态</li>
</ul>
<h4 data-id="heading-17">Mobx</h4>
<ul>
<li>多数据源</li>
<li>被观察对象</li>
<li>观察依赖</li>
<li>触发动作</li>
</ul>
<h4 data-id="heading-18">两者的区别：</h4>



































<table><thead><tr><th>比较</th><th>redux</th><th>mobx</th></tr></thead><tbody><tr><td>核心模块</td><td>Action,Reducer,Store，没有调度器的概念</td><td>observerState、Derivations、Actions...</td></tr><tr><td>Store</td><td>只有一个 Store， Store 和更改逻辑是分开的，带有分层 reducer的单一 Stor</td><td>多个 store</td></tr><tr><td>状态</td><td>状态是不可改变的(建议不可变值)</td><td>通常将状态包装成可观察对象，观察者依赖收集模式</td></tr><tr><td>编程思想</td><td>遵循函数式编程思想</td><td>函数响应式编程编程</td></tr><tr><td>对象</td><td>JavaScript对象</td><td>可观察对象</td></tr></tbody></table>
<h2 data-id="heading-19">总结</h2>
<ul>
<li>Redux 的 源码实现 了解中间件的核心思想</li>
<li>实现Mobx 的 核心 (其他的慢慢摸索是吧)</li>
<li>对比两中状态管理的 差异 优劣</li>
</ul>
<blockquote>
<p>本文首发 <a href="https://github.com/Meet-student/Meet-student/issues/4" target="_blank" rel="nofollow noopener noreferrer">GitHub</a> |
源码 <a href="https://github.com/Meet-student/Meet-student/tree/master/analysis" target="_blank" rel="nofollow noopener noreferrer">Analysis</a></p>
</blockquote></div>  
</div>
            