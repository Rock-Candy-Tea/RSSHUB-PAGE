
---
title: '【React-native】Redux 全家桶实用指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/949a9bafa1fa4c6cb49f2b727518623b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 21:46:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/949a9bafa1fa4c6cb49f2b727518623b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<p>今天，想实现用户第一次登录后，下次免登录的功能。不难，但之前是用 realm 数据库来实现的，就存一个用户信息，用 realm 难免有点杀鸡用牛刀之意，就想用 Redux 来实现，顺带温习下知识。</p>
<p><strong>本文涉及到的组件有：</strong></p>
<ul>
<li>react-redux 及 redux （ 基础 ）</li>
<li>redux-persist             （ 用于缓存 ）</li>
<li>redux-thunk               （ 中间件，这里用于异步调用使用日志打印 ）</li>
<li>redux-actions            （ 简化接口调用 ）</li>
<li>redux-logger             （ redux 中数据变化时，打印日志 ）</li>
</ul>
<p>使用的详细的版本如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/949a9bafa1fa4c6cb49f2b727518623b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995044379970764813" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-0"> 总体思路：</h2>
<blockquote>
<p>在基础的 actions + reducer + store 上进行升级，用 redux-actions 对 reducer 进行简化，在 store 中加入 redux-persist 来对想缓存的数据进行缓存，且有白名单与黑名单的功能，然后打印日志。</p>
</blockquote>
<h2 data-id="heading-1">步骤：</h2>
<ol>
<li>配置 actions</li>
<li>配置 reducer</li>
<li>配置 store</li>
<li>入口文件包裹</li>
<li>页面调用</li>
</ol>
<hr>
<h2 data-id="heading-2">以下是文件结构：</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f5511190ad744d8a0fd8d5045121e07~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995044379970764813" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-3">一，配置 actions</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">/**
 * 用户令牌信息，涉及到所有网络请求中的身份校验
 * User token information, involving identity verification in all network requests
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> USER_TOKEN = <span class="hljs-string">'USER_TOKEN'</span>;

<span class="hljs-comment">/**
 * 用户信息，USER_TOKEN + USER_INFO 均有值，则无需再次输入账户密码即可登录
 * User information, USER_TOKEN + USER_INFO have values, you can log in without entering the account password again
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> USER_INFO = <span class="hljs-string">'USER_INFO'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044379970764813" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里就简单的先来两个，USER_TOKEN 是登录后发放的令牌， USER_INFO 则是用户信息。</p>
<h3 data-id="heading-4">二，配置 reducer</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Created by supervons on 2019/08/20.
 * Redux Reducer设置，使用 redux-actions 更清爽的写 reducer
 * Redux Reducer settings, use redux-actions to write more reducer
 */</span>
<span class="hljs-keyword">import</span> &#123; USER_TOKEN, USER_INFO &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../action/userActionTypes'</span>;
<span class="hljs-keyword">import</span> &#123; handleActions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-actions'</span>;

<span class="hljs-comment">// 初始化数据</span>
<span class="hljs-keyword">const</span> initialState = &#123;
  <span class="hljs-attr">userToken</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">userInfo</span>: &#123;&#125;
&#125;;

<span class="hljs-keyword">const</span> handler = &#123;&#125;;

handler[USER_TOKEN] = <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; userToken &#125; = action;
  <span class="hljs-keyword">return</span> &#123;
    ...state,
    userToken
  &#125;;
&#125;;

handler[USER_INFO] = <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; userInfo &#125; = action;
  <span class="hljs-keyword">return</span> &#123;
    ...state,
    userInfo
  &#125;;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> handleActions(handler, initialState);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044379970764813" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里关键是在 handler 方法，已经完成了之前 actions 的赋值，对比之前的用法，简化了很多。</p>
<p>更多参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux-actions.js.org" target="_blank" rel="nofollow noopener noreferrer" title="https://redux-actions.js.org" ref="nofollow noopener noreferrer">redux-actions.js.org</a></p>
<p>三，配置 store</p>
<p>重点来了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Created by supervons on 2019/08/20.
 * 对 redux 进行配置，增加 redux-persist 对 whitelist 中的数据作缓存（以 reducer 为单位）
 * Configure redux and add redux-persist to cache data in whitelist (in reducer)
 */</span>
<span class="hljs-keyword">import</span> &#123; createStore, applyMiddleware, compose &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>;
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-thunk'</span>;
<span class="hljs-keyword">import</span> rootReducer <span class="hljs-keyword">from</span> <span class="hljs-string">'../reducer'</span>;
<span class="hljs-keyword">import</span> &#123; persistStore, persistReducer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-persist'</span>;
<span class="hljs-keyword">import</span> storage <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-persist/lib/storage'</span>;
<span class="hljs-keyword">import</span> logger <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-logger'</span>;
<span class="hljs-keyword">const</span> middleWares = [thunk];

<span class="hljs-keyword">const</span> persistConfig = &#123;
  <span class="hljs-attr">key</span>: <span class="hljs-string">'root'</span>, <span class="hljs-comment">// 对于数据 key 的定义</span>
  storage, <span class="hljs-comment">// 选择的存储引擎</span>
  <span class="hljs-attr">whitelist</span>: [<span class="hljs-string">'UserReducer'</span>] <span class="hljs-comment">// 白名单，位于数组中的会被缓存</span>
&#125;;

<span class="hljs-comment">// 对 reducers 的封装处理</span>
<span class="hljs-keyword">const</span> persistedReducer = persistReducer(persistConfig, rootReducer);

<span class="hljs-comment">/* global __DEV__
 * 开发环境加入日志输出，redux 中数据改变即输出
 */</span>
<span class="hljs-keyword">if</span> (__DEV__) &#123;
  middleWares.push(logger);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configureStore</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> enhancers = compose(applyMiddleware(...middleWares));

  <span class="hljs-keyword">const</span> store = createStore(persistedReducer, enhancers);

  <span class="hljs-comment">// 持久化 store</span>
  <span class="hljs-keyword">let</span> persist = persistStore(store, persistedReducer);
  <span class="hljs-keyword">return</span> &#123; store, persist &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044379970764813" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">四，入口文件包裹</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Provider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>;
<span class="hljs-keyword">import</span> configureStore <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/common/redux/store/store'</span>;
<span class="hljs-keyword">import</span> &#123; PersistGate &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-persist/integration/react'</span>;

<span class="hljs-comment">// 引入 redux 及 redux-persist 配置后的变量供使用</span>
<span class="hljs-keyword">const</span> &#123; store, persist &#125; = configureStore();
<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="hljs-comment">// 外层需 Provider 包裹， PersistGate 中的 loading 需为一个组件，否则在启动页后会有短暂黑屏</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">PersistGate</span> <span class="hljs-attr">loading</span>=<span class="hljs-string">&#123;null&#125;</span> <span class="hljs-attr">persistor</span>=<span class="hljs-string">&#123;persist&#125;</span>></span>
        &#123;...&#125;
      <span class="hljs-tag"></<span class="hljs-name">PersistGate</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044379970764813" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>注意：这里的 loading 组件需要自己配置，不然会出现短暂的灰屏，可以配一个 Image 标签，图片就是启动页，这样就延续了启动页，亦或是给一个 loading 加载器。</strong></p>
<h3 data-id="heading-6"><strong>五，页面调用</strong></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Login</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  componentDidMount(): <span class="hljs-keyword">void</span> &#123;
    <span class="hljs-comment">// 判断 redux-persist 缓存中是否有数据，有则取出直接登录</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.userToken && <span class="hljs-built_in">this</span>.props.userInfo) &#123;
      jwtToken = <span class="hljs-built_in">this</span>.props.userToken;
      userInfo = <span class="hljs-built_in">this</span>.props.userInfo;
      <span class="hljs-built_in">this</span>.props.navigation.replace(<span class="hljs-string">'MainPage'</span>);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">setToken</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 给 store 中赋值</span>
    <span class="hljs-built_in">this</span>.props.setToken(<span class="hljs-string">'123'</span>);
  &#125;
  &#123;...&#125;
&#125;

<span class="hljs-comment">// 取出 store 中的数据</span>
<span class="hljs-keyword">const</span> mapStateToProps = <span class="hljs-function"><span class="hljs-params">state</span> =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">userToken</span>: state.UserReducer.userToken,
    <span class="hljs-attr">userInfo</span>: state.UserReducer.userInfo
  &#125;;
&#125;;

<span class="hljs-comment">// Dispatch 方法</span>
<span class="hljs-keyword">const</span> mapDispatchToProps = <span class="hljs-function"><span class="hljs-params">dispatch</span> =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">setToken</span>: <span class="hljs-function"><span class="hljs-params">userToken</span> =></span> &#123;
      dispatch(&#123; <span class="hljs-attr">type</span>: USER_TOKEN, <span class="hljs-attr">userToken</span>: userToken &#125;);
    &#125;,
    <span class="hljs-attr">setUserInfo</span>: <span class="hljs-function"><span class="hljs-params">userInfo</span> =></span> &#123;
      dispatch(&#123; <span class="hljs-attr">type</span>: USER_INFO, <span class="hljs-attr">userInfo</span>: userInfo &#125;);
    &#125;
  &#125;;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (Login = connect(
  mapStateToProps,
  mapDispatchToProps
)(Login));
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044379970764813" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来的思路就简单了，在登录成功后，存储值，然后下次进入登录页的时候检测 store 中是否有值，如果有则取出，然后直接登录（ userInfo 与 jwtToken 设置为全局变量），没有则需要登录。然后在退出按钮中，清空 store 中的值，达到注销的目的。</p>
<p>最后，来一个效果图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac52dc17024b449e9bcc3fcd8487cf90~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995044379970764813" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<ol>
<li>数量过大的时候，建议结合 realm 使用。</li>
<li>并不是全部数据都需要使用 redux，主要是在子页面之间互传数据，跨多个页面的时候使用。</li>
<li>项目地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsupervons%2FExploreRN%2Fcommit%2F2b3871141f8aed7c6905f7fe887650a75f13a742" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/supervons/ExploreRN/commit/2b3871141f8aed7c6905f7fe887650a75f13a742" ref="nofollow noopener noreferrer">github.com/supervons/E…</a></li>
</ol>
<p>喜欢的话，点个 star 吧。</p>
<p>​</p></div>  
</div>
            