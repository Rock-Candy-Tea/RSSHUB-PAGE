
---
title: '基于Redux的状态管理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3aaa1cb249489cbf8ada70ebfb8707~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 01:56:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3aaa1cb249489cbf8ada70ebfb8707~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、什么是Redux</h2>
<p>Redux 是 JavaScript 状态容器，提供可预测化的状态管理。源于Facebook的flux架构。<strong>是一个使用叫做“action”的事件来管理和更新应用状态的模式和工具库</strong> 它以集中式Store（centralized store）的方式对整个应用中使用的状态进行集中管理，其规则确保状态只能以可预测的方式更新。利用React中<code>Context</code>(上下文)在组件之间共享状态的特性实现。</p>
<h2 data-id="heading-1">二、核心概念</h2>
<h3 data-id="heading-2">1. state</h3>
<p>整个应用的全局state ，存储在唯一一个store中, store通过createStore函数生成</p>
<p>示例：</p>
<pre><code class="copyable">//store/index.js
import &#123;createStore&#125; from 'redux';
//引入Reducer
import Reducer from './reducers';
​
const configureStore = (initialState) => &#123;
    const store = createStore(Reducer, initialState);
    return store;
&#125;
export default configureStore(&#123;
  addCount: &#123;
    count: 0,
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2. reducer</h3>
<p><code>reducer</code>定义 <code>state</code>改变的规则， 返回新的<code>state</code>给<code>store</code>，只有在<code>reducer</code>中才能改变<code>state</code>。reducer必须是<strong>纯函数</strong>，可以有多个，通过combineReducers 函数合成一个根Reducer。</p>
<p>示例：</p>
<pre><code class="copyable">const initState = &#123;
  count: 0,
&#125;;
​
const addCount = (state = initState, action) => &#123;
    switch (action.type) &#123;
        case 'ADD_COUNT':
            return &#123;
              ...state,
              ...action.count,
            &#125;;
        default:
            return state;
    &#125;
&#125;
​
​
export default combineReducers(&#123;
  addCount
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3. action</h3>
<p>​ 用来描述当前发生的操作，定义操作类型与参数，并传递给<code>Reducer</code>。</p>
<p><code>Action</code> 通过 <code>Store</code> 的 <code>Dispatch</code> 方法传递给 <code>Store</code>，<code>Store</code> 接收到 <code>Action</code>，连同之前的 <code>State</code> 一起传给 <code>Reducer</code></p>
<p>示例：</p>
<pre><code class="copyable">const addCount = (count) => &#123;
  return &#123;
      type: 'ADD_COUNT',
      count
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4. Middleware中间件</h3>
<p>在 Redux 中，同步的表现就是：Action 发出以后，Reducer 立即算出 State。那么异步的表现就是：Action 发出以后，过一段时间再执行 Reducer。那怎么才能 Reducer 在异步操作结束后自动执行呢？Redux 引入了中间件 <code>Middleware</code> 的概念。</p>
<p>实际上我们说的中间件指的是对 Dispatch 方法的封装。常用中间件：</p>
<ul>
<li>
<p><strong>redux-thunk 中间件 重写store.dispatch,解决异步操作</strong></p>
</li>
<li>
<p><strong>redux-promise 中间件 使得store.dispatch方法可以接受 Promise 对象作为参数</strong></p>
</li>
<li>
<p><strong>redux-logger中间件 日志中间件</strong></p>
</li>
</ul>
<p>示例代码：</p>
<pre><code class="copyable">//store/index.js
import &#123;createStore, applyMiddleware&#125; from 'redux';
//引入Reducer
import Reducer from './reducers';
//引入中间件
import logger from 'redux-logger';
​
const configureStore = (initialState) => &#123;
    // 通过 applyMiddleware来集成中间件
    const store = createStore(Reducer, initialState, applyMiddleware(logger));
    return store;
&#125;
export default configureStore(&#123;
  addCount: &#123;
    count: 0,
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5. connect</h3>
<p>connect是view与redux之间的桥梁。那他们是如何关联的呢，请看示例：</p>
<pre><code class="copyable">import React, &#123;Component&#125; from 'react';
import &#123;addCount&#125; from './store/actions/index';
import &#123;connect&#125; from 'react-redux';
​
class App extends Component &#123;
    constructor(props) &#123;
        super(props)
    &#125;
​
    addCount = () => &#123;
      this.props.dispatch(addCount(&#123;count: this.props.count + 1&#125;));
    &#125;
    
    render() &#123;
      return (
        <div className='App'>
          <div>当前计数：&#123;this.props.count&#125;</div>
          <div className='btn' onClick=&#123;this.addCount&#125;>增加</div>
        </div>
      )
    &#125;
&#125;
​
//添加store中的state
const mapStateToProps = (store) => &#123;
    return &#123;
      count: store.addCount.count,
    &#125;;
&#125;;
//添加dispatch方法
const mapDispatchToProps = (dispatch) => &#123;
    return &#123;
        dispatch,
    &#125;
&#125;
export default connect(mapStateToProps, mapDispatchToProps)(App)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在view中通过redux提供的connect方法将 store中的state与dispatch方法传入view的props中，以下是connect函数的核心代码</p>
<pre><code class="copyable">export default function connect(mapStateToProps, mapDispatchToProps, mergeProps, options = &#123;&#125;) &#123;
  return function wrapWithConnect(WrappedComponent) &#123;
    class Connect extends Component &#123;
      constructor(props, context) &#123;
        // 从祖先Component处获得store
        this.store = props.store || context.store
        this.stateProps = computeStateProps(this.store, props)
        this.dispatchProps = computeDispatchProps(this.store, props)
        this.state = &#123; storeState: null &#125;
        // 对stateProps、dispatchProps、parentProps进行合并
        this.updateState()
      &#125;
      shouldComponentUpdate(nextProps, nextState) &#123;
        // 进行判断，当数据发生改变时，Component重新渲染
        if (propsChanged || mapStateProducedChange || dispatchPropsChanged) &#123;
          this.updateState(nextProps)
            return true
          &#125;
        &#125;
        componentDidMount() &#123;
          // 改变Component的state
          this.store.subscribe(() = &#123;
            this.setState(&#123;
              storeState: this.store.getState()
            &#125;)
          &#125;)
        &#125;
        render() &#123;
          // 生成包裹组件Connect
          return (
            <WrappedComponent &#123;...this.nextState&#125; />
          )
        &#125;
      &#125;
      Connect.contextTypes = &#123;
        store: storeShape
      &#125;
      return Connect;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">6.数据流</h3>
<p><strong>此时我们看一下Redux事件流</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3aaa1cb249489cbf8ada70ebfb8707~tplv-k3u1fbpfcp-watermark.image" alt="redux-middleware流程图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结一下：Store通过connect将state、dispatch传给View, view调用dispatch发送Action，中间件处理action以及异步任务，处理完之后将结果放到action中并发送给Store，Store将action、previousState发送给Reducer来更改对应的State，并将处理之后的state返回给Store，view监听到state的变化之后从而触发Render。</p>
<h2 data-id="heading-8">三、技术演进</h2>
<h3 data-id="heading-9">1. dva</h3>
<p>dva 首先是一个基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Fredux" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/redux" ref="nofollow noopener noreferrer">redux</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fredux-saga%2Fredux-saga" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/redux-saga/redux-saga" ref="nofollow noopener noreferrer">redux-saga</a> 的数据流方案，也可以理解为一个轻量级的应用框架。</p>
<p>redux-saga是一个用于管理应用程序 Side Effect（副作用，例如异步获取数据，访问浏览器缓存等）的 library，它的目标是让副作用管理更容易，执行更高效，测试更简单，在处理故障时更容易。</p>
<p><strong>核心API</strong></p>
<ul>
<li>
<p>State 全局状态</p>
</li>
<li>
<p>Action</p>
<p>Action 是一个普通 javascript 对象，它是改变 State 的唯一途径。</p>
<p>示例：</p>
<pre><code class="copyable">dispatch(&#123;
  type: 'add',
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>dispatch函数</p>
<p>​ 一个用于触发 action 的函数，action 是改变 State 的唯一途径，但是它只描述了一个行为，而 dipatch 可以看作是触发这个行为的方式</p>
</li>
<li>
<p>Reducer</p>
<p>与Redux的reducer一样，描述如何改变数据的，必须是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fc_kite%2Farticle%2Fdetails%2F79138814" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/c_kite/article/details/79138814" ref="nofollow noopener noreferrer">”纯函数”</a>【一个函数的返回结果只依赖于它的参数，并且在执行过程里面没有副作用，我们就把这个函数叫做纯函数】</p>
<p>示例：</p>
<pre><code class="copyable">// 纯函数
const foo = (a,b) => a + b;
const bar = (obj, b) => obj.x + b;
//以下不是纯函数
const  a = 1;
const foo = (b) => a + b;
const foo = (obj, b) => &#123;
  obj.x = 2;
  return obj.x + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Effect</p>
<p>​ Effect被称为副作用，在我们的应用中，最常见的就是异步操作。dva 为了控制副作用的操作，底层引入了<a href="https://link.juejin.cn/?target=http%3A%2F%2Fsuperraytin.github.io%2Fredux-saga-in-chinese" target="_blank" rel="nofollow noopener noreferrer" title="http://superraytin.github.io/redux-saga-in-chinese" ref="nofollow noopener noreferrer">redux-sagas</a>做异步流程控制，由于采用了<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2015%2F04%2Fgenerator.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/blog/2015/04/generator.html" ref="nofollow noopener noreferrer">generator的相关概念</a>，所以将异步转成同步写法，从而将effects转为纯函数。</p>
<p>示例：</p>
<pre><code class="copyable"> effects: &#123;
    *fetch(&#123; payload &#125;, &#123; call, put, select &#125;) &#123;
      let count = yield select(state => state.example.count);
      count ++;
      console.log(count, 'count---')
      yield put(&#123; type: 'save', payload: &#123;count: count&#125;&#125;);
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Subscription</p>
<p>​ Subscription 语义是订阅，用于订阅一个数据源，然后根据条件 dispatch 需要的 action。数据源可以是当前的时间、服务器的 websocket 连接、keyboard 输入、geolocation 变化、history 路由变化等等。</p>
<p>示例：</p>
<pre><code class="copyable">subscriptions: &#123;
    setup(&#123;dispatch, history&#125;) &#123;
      history.listen((&#123;pathname&#125;) => &#123;
        if (pathname === '/users) &#123;
          dispatch(&#123;
            type: 'users/fetch'
          &#125;);
        &#125;
      &#125;)
    &#125;,
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-10">2. Vuex</h3>
<p>​ Vuex 是一个专为 Vue.js 应用程序开发的<strong>状态管理模式</strong>。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。Vuex借鉴了Redux的思想，并且针对web应用的开发模式和VUE框架做了优化。</p>
<p><strong>核心概念</strong></p>
<ul>
<li>
<p>State 单一状态树，包含了全部的应用层级状态</p>
</li>
<li>
<p>Getters 类似于computed，用于从state中派生出一些状态</p>
</li>
<li>
<p>Mutations</p>
<p>​ 更改Vuex 的 store 中的状态的唯一方法是提交 mutation。Mutation需遵守Vue的响应规则；Mutation必须是同步函数</p>
</li>
<li>
<p>Actions</p>
<p>Action 提交的是 mutation，而不是直接变更状态。</p>
<p>Action 可以包含任意异步操作。</p>
</li>
<li>
<p>Modules</p>
<p>​ 由于使用单一状态树，应用的所有状态会集中到一个比较大的对象。当应用变得非常复杂时，store 对象就有可能变得相当臃肿。</p>
<p>​ 为了解决以上问题，Vuex 允许我们将 store 分割成<strong>模块（module）</strong> 。每个模块拥有自己的 state、mutation、action、getter、甚至是嵌套子模块——从上至下进行同样方式的分割。</p>
<p>默认情况下，模块内部的 action、mutation 和 getter 是注册在<strong>全局命名空间</strong>的——这样使得多个模块能够对同一 mutation 或 action 作出响应。</p>
<p>如果希望你的模块具有更高的封装度和复用性，你可以通过添加 <code>namespaced: true</code> 的方式使其成为带命名空间的模块。当模块被注册后，它的所有 getter、action 及 mutation 都会自动根据模块注册的路径调整命名。</p>
</li>
<li>
<p>plugins</p>
<p>Vuex 插件就是一个函数，它接收 store 作为唯一参数：</p>
<p>插件可用来同步数据源到store，监控state变化，生成state快照等，内置<code>Logger</code>插件</p>
<p>示例：</p>
<pre><code class="copyable">import createLogger from 'vuex/dist/logger'
​
Vue.use(Vuex)
​
const debug = process.env.NODE_ENV !== 'production'
​
export default new Vuex.Store(&#123;
  state: &#123;&#125;,
  mutations: &#123;&#125;,
  actions: &#123;&#125;,
  modules: &#123;&#125;,
  plugins: debug ? [createLogger()] : []
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-11">3. Vuex、dva事件流</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/beb27207e8234fec9519ab7295ef3fce~tplv-k3u1fbpfcp-watermark.image" alt="vuex-dva事件流.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对比流程图我们发现，Vuex与dva的数据流向是极为相似的，区别只是api的命名以及实现方式不同，Reducer变成了Mutation，effect变成了action。</p>
<h2 data-id="heading-12">四、什么情况下应该用状态管理</h2>
<h4 data-id="heading-13">1. 当遇到如下问题时，建议开始使用 ：</h4>
<ul>
<li>你有很多数据随时间而变化</li>
<li>你希望状态有一个唯一确定的来源（single source of truth）</li>
<li>你发现将所有状态放在顶层组件中管理已不可维护</li>
</ul>
<p>例如： 用户信息、位置信息等,全局唯一且共用的属性</p>
<h4 data-id="heading-14">2. 当页面组件嵌套达到3层及以上时</h4>
<p>父子组件嵌套达到3层时，数据传递时需要层层处理，容易出现漏洞，维护成本高。</p>
<h4 data-id="heading-15">3. 当相同页面会在路由中重复出现时不建议使用或谨慎使用</h4>
<p>比如商品详情页，没有状态的隔离，会导致页面数据错乱。</p>
<p>如果逻辑实在复杂着实需要使用状态管理，
在Vuex中推荐使用vuex的<strong>模块重用</strong>（仅 2.3.0+ 支持）</p>
<p>即使用module的<code>store.registerModule</code> 、<code>store.unregisterModule(moduleName)</code> 进行动态注册</p>
<p>这是module的state与vue组件内的<code>data</code>有同样的问题，所以需要使用函数来声明模块的状态</p>
<pre><code class="copyable">
const MyReusableModule = &#123;
  state: () => (&#123;
    foo: 'bar'
  &#125;),
  // mutation、action 和 getter 等等...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="copyable">// src/store/dynamicModule/dynamicGoods.js
​
import store from '../index'
import goods from '../moduleGoods'
​
export default &#123;
  install (key) &#123;
    store.registerModule(key, goods)
  &#125;,
  uninstall (key) &#123;
    store.unregisterModule(key)
  &#125;
&#125;
​
// Vue文件
 created () &#123;
   // 用路由名称 + query + 时间戳 创建唯一routerKey进行隔离
    this.routerKey = `$&#123;this.$route.name&#125;$&#123;this.$route.query.productId || ''&#125;$&#123;new Date().getTime()&#125;`
    console.log('created-key', this.routerKey)
    storeGoods.install(this.routerKey)
     this.$store.dispatch(`$&#123;this.routerKey&#125;/changeGoodsId`, this.$route.query.productId)
  &#125;,
​
computed: &#123;
  getNum () &#123;
    // 通过唯一routerKey获取对应module数据
    return this.$store.state[this.routerKey].num
  &#125;,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在dva中原理类似，可直接将model中的state改为<code>Map</code>，利用页面路由参数创建唯一Key，作为Map的key来进行存储数据，达到隔离数据的效果。</p>
<h2 data-id="heading-16">Vuex使用误区</h2>
<h4 data-id="heading-17">1.vuex中action里可以直接操作state且会生效</h4>
<pre><code class="copyable"> changeCount (&#123; commit, state &#125;) &#123;
      state.count++
      // commit('setCount', state.count + 1)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然可以生效，但是不建议这么使用，不利于追踪state的改变，state必须在Mutations中进行改变。</p>
<h2 data-id="heading-18">参考资料</h2>
<p><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"><strong>redux文档</strong></a></p>
<p><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuex.vuejs.org%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuex.vuejs.org/zh/" ref="nofollow noopener noreferrer"><strong>vuex文档</strong></a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuex.vuejs.org%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuex.vuejs.org/zh/" ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"><strong>Flux文档</strong></a></p>
<p><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"><strong>dva文档</strong></a></p>
<p><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"><strong>react-saga文档</strong></a></p>
<p><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fustbhuangyi.github.io%2Fvue-analysis%2Fv2%2Fvuex%2F%23%25E4%25BB%2580%25E4%25B9%2588%25E6%2598%25AF-%25E7%258A%25B6%25E6%2580%2581%25E7%25AE%25A1%25E7%2590%2586%25E6%25A8%25A1%25E5%25BC%258F-%25EF%25BC%259F" target="_blank" rel="nofollow noopener noreferrer" title="https://ustbhuangyi.github.io/vue-analysis/v2/vuex/#%E4%BB%80%E4%B9%88%E6%98%AF-%E7%8A%B6%E6%80%81%E7%AE%A1%E7%90%86%E6%A8%A1%E5%BC%8F-%EF%BC%9F" ref="nofollow noopener noreferrer"><strong>Vue.js技术揭秘</strong></a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fustbhuangyi.github.io%2Fvue-analysis%2Fv2%2Fvuex%2F%23%25E4%25BB%2580%25E4%25B9%2588%25E6%2598%25AF-%25E7%258A%25B6%25E6%2580%2581%25E7%25AE%25A1%25E7%2590%2586%25E6%25A8%25A1%25E5%25BC%258F-%25EF%25BC%259F" target="_blank" rel="nofollow noopener noreferrer" title="https://ustbhuangyi.github.io/vue-analysis/v2/vuex/#%E4%BB%80%E4%B9%88%E6%98%AF-%E7%8A%B6%E6%80%81%E7%AE%A1%E7%90%86%E6%A8%A1%E5%BC%8F-%EF%BC%9F" ref="nofollow noopener noreferrer"><br>
</a></p></div>  
</div>
            