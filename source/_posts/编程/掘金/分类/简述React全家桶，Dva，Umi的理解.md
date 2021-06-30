
---
title: '简述React全家桶，Dva，Umi的理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/336ca85cd6724040bc46850091df9d4c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 22:08:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/336ca85cd6724040bc46850091df9d4c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.  前言</h2>
<p>首先赘述一遍各个框架的官方口号</p>
<ul>
<li><code>React</code></li>
</ul>
<blockquote>
<p>用于构建用户界面的 <code>JavaScript</code> 库</p>
</blockquote>
<ul>
<li><code>Redux</code></li>
</ul>
<blockquote>
<p><code>Redux</code> 是 <code>JavaScript</code>状态容器，提供可预测化的状态管理</p>
</blockquote>
<ul>
<li><code>React-Router</code></li>
</ul>
<blockquote>
<p>通过管理 <code>URL</code>，实现组件的切换和状态的变化</p>
</blockquote>
<ul>
<li><code>React-Thunk和React-Saga</code></li>
</ul>
<blockquote>
<p><code>Redux store</code> 仅支持同步数据流。使用 <code>thunk</code> 等中间件可以帮助在 <code>Redux</code> 应用中实现异步性</p>
</blockquote>
<p><code>React</code>通过声明式渲染和组件化很好的胜任了<code>UI</code>层面的工作，但是没有路由功能（管理页面之间的切换）和状态容器（管理全局数据），<code>action</code>中也不能执行异步操作，所以就有了<code>react-router</code>和<code>redux</code>和<code>thunk</code>。</p>
<hr>
<h2 data-id="heading-1">2. 全家桶整合实例代码（基于<code>Creat-React-App</code>脚手架）</h2>
<p>入口文件<code>src/index.jsx</code>
(整合<code>redux</code>和<code>thunk</code>，其中<code>ConnectedRouter</code> 是为了把<code>redux</code>中整合的<code>router</code>数据和<code>react</code>组件的<code>router</code>数据联系起来，不然在<code>action</code>里是没办法正确跳转的)</p>
<pre><code class="copyable">import React from "react" 
import ReactDom from "react-dom"
import MyApp from "./app"
import &#123;createStore,applyMiddleware&#125; from "redux"
import rootReducers from "./reducer/index"
import &#123;Provider&#125; from "react-redux"    
import reduxThunk from "redux-thunk"
import &#123; ConnectedRouter&#125; from 'connected-react-router'
import history from "@/actions/history";

const store = createStore(rootReducers,&#123;&#125;,applyMiddleware(logger,reduxThunk))

ReactDom.render(
<Provider store=&#123;store&#125;>
<ConnectedRouter history=&#123;history&#125;>
<MyApp/>
</ConnectedRouter>
</Provider>,
document.getElementById("app"))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>redux</code>入口文件<code>/src/redux/index.js</code>
(整合自己全部的<code>reducer</code>，同时整合<code>history</code>实现<code>action</code>里路由跳转)</p>
<pre><code class="copyable">import login from './login'   //这里可以写自己的reducer
import &#123; combineReducers &#125; from 'redux'
import &#123; connectRouter &#125; from 'connected-react-router'
import history from "@/actions/history";

//history模块是为了能在action里面进行路由跳转
const reducers = combineReducers (&#123;
router: connectRouter(history),
login,
&#125;)

export default reducers
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>actions</code>文件夹下的主要文件
<code>/src/actions/hisotry.js</code></p>
<pre><code class="copyable">import &#123;createBrowserHistory&#125; from 'history';
const history = createBrowserHistory()
export default history;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>/src/actions/login.js</code></p>
<pre><code class="copyable">import &#123; push &#125; from 'react-router-redux'

export const login = (&#123;payload&#125;) => (dispatch) => &#123;
        //模拟登陆，异步请求后执行跳转跳转
setTimeout(() => &#123;
dispatch(push('/home'))
&#125;, 1000)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后就是<code>app.jsx</code>文件（使用路由）</p>
<pre><code class="copyable">import React, &#123;Fragment&#125; from "react"
import &#123;BrowserRouter as Router, Route, Link, NavLink, Switch,&#125; from 'react-router-dom';

const mapStateToProps = (state) => (&#123;
login: state.login,
&#125;)

const mapDispatchToProps = (dispatch) => (&#123;
loginApi: (payload) => &#123;
login(payload)(dispatch)
&#125;
&#125;)

@withRouter
@connect(mapStateToProps, mapDispatchToProps)
export default class MyApp extends React.Component &#123;

render() &#123;
return (
<Fragment>
<Router>
    <Switch>
                                        //里面可以写自己的页面
    </Switch>
</Router>
</Fragment>
);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到这里是不是觉得头都大了，没错，为了把<code>react</code>，<code>router</code>，<code>redux</code>三者完美的联系起来，需要配置的东西太多了，严重影响开发效率。所以此时<code>Dva</code>和<code>Umi</code>等<code>React</code>框架就应运而生了。</p>
<hr>
<h2 data-id="heading-2">3. Dva</h2>
<p>首先老惯例还是看一下官网介绍</p>
<blockquote>
<p><code>dva</code> 首先是一个基于 <a href="https://github.com/reduxjs/redux%60" target="_blank" rel="nofollow noopener noreferrer">redux</a> 和 <a href="https://github.com/redux-saga/redux-saga" target="_blank" rel="nofollow noopener noreferrer">redux-saga</a> 的数据流方案，然后为了简化开发体验，<code>dva</code> 还额外内置了 <a href="https://github.com/ReactTraining/react-router" target="_blank" rel="nofollow noopener noreferrer">react-router</a> 和 <a href="https://github.com/github/fetch" target="_blank" rel="nofollow noopener noreferrer">fetch</a>，所以也可以理解为一个轻量级的应用框架。</p>
</blockquote>
<p>光说不练假把式，我们快速创建一个<code>dva</code>脚手架项目看看结构</p>
<pre><code class="copyable">npm install dva-cli -g
dva new dva-quickstart
cd dva-quickstart
npm start
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目录结构
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/336ca85cd6724040bc46850091df9d4c~tplv-k3u1fbpfcp-zoom-1.image" alt="dva.png" loading="lazy" referrerpolicy="no-referrer">
<code>Dva</code>帮我们整合了很多东西，在<code>index.js</code>里，通过几个<code>API</code>就整合了<code>router</code>和<code>redux</code></p>
<pre><code class="copyable">//index.js
import dva from 'dva';
import './index.css';

// 1. Initialize
const app = dva();

// 2. Plugins
// app.use(&#123;&#125;);

// 3. Model
// app.model(require('./models/example').default);

// 4. Router
app.router(require('./router').default);

// 5. Start
app.start('#root');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面连接<code>redux</code></p>
<pre><code class="copyable">import React from 'react';
import &#123; connect &#125; from 'dva';
import styles from './IndexPage.css';

function IndexPage() &#123;
  return (
    <div className=&#123;styles.normal&#125;>
    </div>
  );
&#125;

IndexPage.propTypes = &#123;
&#125;;

export default connect()(IndexPage);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而且还提出了极具规范性的<code>model</code></p>
<pre><code class="copyable">import &#123;routerRedux&#125; from 'dva/router'

export default &#123;
  namespace: 'example',
  state: &#123;&#125;,
  subscriptions: &#123;
    setup(&#123; dispatch, history &#125;) &#123;  // eslint-disable-line
    &#125;,
  &#125;,
  effects: &#123;
    *fetch(&#123; payload &#125;, &#123; call, put &#125;) &#123;  // eslint-disable-line
      yield put(&#123; type: 'save' &#125;);
      yield.put(routerRedux.push('/'))
    &#125;,
  &#125;,
  reducers: &#123;
    save(state, action) &#123;
      return &#123; ...state, ...action.payload &#125;;
    &#125;,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>model</code>其实就是把所有跟<code>redux</code>相关的一个<code>reducer</code>整合在一个<code>model</code>文件里，通过<code>namespace</code>区分<code>model</code>，通过<code>state</code>存储数据，通过<code>subsciprtions</code>实现<code>hisotry</code>等监听，通过<code>effect</code>发起异步操作，通过<code>reducer</code>执行同步操作，简直完美！</p>
<p>看来<code>Dva</code>已经帮我们规划好了一切，我们只要按着官网的<code>API</code>文档，一部一部搭建自己的应用就好了。
但是牛逼的前人们不安于现状，<code>Umi</code>横空出世</p>
<hr>
<h2 data-id="heading-3">4. Umi 是什么？</h2>
<p>老惯例</p>
<blockquote>
<p><code>Umi</code>，中文可发音为乌米，是可扩展的企业级前端应用框架。<code>Umi</code> 以路由为基础的，同时支持配置式路由和约定式路由，保证路由的功能完备，并以此进行功能扩展。然后配以生命周期完善的插件体系，覆盖从源码到构建产物的每个生命周期，支持各种功能扩展和业务需求。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e94bf48a3a7843bbaf11d37047436ed7~tplv-k3u1fbpfcp-zoom-1.image" alt="umi.png" loading="lazy" referrerpolicy="no-referrer">
简单来说，<code>Umi</code>就是一个支持约定式路由和配置式路由的大杂烩，他整合了所有React生态的东西，<code>Antd</code>、<code>Dva</code>等等，把他们都当成了<code>Umi</code>的插件，我们想使用的时候，直接通过配置就能使用</p>
<p>再一次口说无凭，我们快速创建一个<code>Umi</code>脚手架项目看看结构</p>
<p><code>umi</code>官网推荐用<code>yarn</code>代替<code>npm</code></p>
<pre><code class="copyable">npm i yarn tyarn -g
mkdir myapp && cd myapp
yarn create @umijs/umi-app
yarn install
yarn start
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目录结构
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/637782c1db714cf4a2756566944da8e3~tplv-k3u1fbpfcp-zoom-1.image" alt="umi1.png" loading="lazy" referrerpolicy="no-referrer">
可以看到Umi实际上就只有<code>src</code>下的一个<code>pages</code>文件夹（.Umi文件不用管，是项目启动之后动态构建的），内置了<code>Dva（@umijs/plugin-dva）</code>，<code>antd（@umijs/plugin-antd）</code>等功能。我们只需要写页面组件就好了，简直无敌</p>
<h2 data-id="heading-4">写在最后</h2>
<p>当然了，<code>Dva</code>和<code>Umi</code>的功能虽然强大，但是为了很好的使用他们，我们必须花更多的时间去看官网文档，重头了解他们要如何使用，如何配置。而基于<code>Webpack</code>构建的<code>creat-react-app</code>让我们有更高的自由度，实现任何功能，对习惯了<code>webpack</code>的人来说有种回家的感觉。</p></div>  
</div>
            