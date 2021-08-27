
---
title: 'Redux、React和Redux配合、logger _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7874771bb2554fb29d065a0a43ded08c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 02:28:49 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7874771bb2554fb29d065a0a43ded08c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">Redux</h2>
<blockquote>
<p>Redux 是一个可预测状态容器。</p>
</blockquote>
<p>官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://redux.js.org/" ref="nofollow noopener noreferrer">redux.js.org/</a></p>
<h3 data-id="heading-1"><a href="https://juejin.cn/post/7000683710735450143#%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AAredux%E9%A1%B9%E7%9B%AE%E7%94%A8nodejs%E8%B0%83%E8%AF%95" target="_blank" title="#%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AAredux%E9%A1%B9%E7%9B%AE%E7%94%A8nodejs%E8%B0%83%E8%AF%95"></a>创建一个Redux项目用Nodejs调试</h3>
<p>创建身份证</p>
<pre><code class="copyable">npm init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装依赖</p>
<pre><code class="copyable">npm install --save redux
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建app.js</p>
<pre><code class="copyable">var redux = require("redux");

//创建一个函数，叫做reducer。
const reducer = (state = &#123;"a" : 10&#125; , action) => &#123;
    if(action.type == "ADD")&#123;
        return &#123;
            "a" : state.a + 1
        &#125;
    &#125;else if(action.type == "MINUS")&#123;
        return &#123;
            "a" : state.a - 1
        &#125;
    &#125; else if (action.type == "PINGFANG") &#123;
        return &#123;
            "a" : state.a * state.a
        &#125;
    &#125;
    return state;
&#125;

//根据reducer函数创建store
const store = redux.createStore(reducer);

//得到store中的a
console.log(store.getState().a);

//发出ADD命令
store.dispatch(&#123;"type" : "ADD"&#125;); //10+1
store.dispatch(&#123;"type" : "ADD"&#125;); //11+1
store.dispatch(&#123;"type" : "ADD"&#125;); //12+1

//得到store中的a
console.log(store.getState().a); //13

//发出减法命令
store.dispatch(&#123;"type" : "MINUS"&#125;);  // 13-1

//得到store中的a
console.log(store.getState().a); // 12

store.dispatch(&#123; "type": "PINGFANG" &#125;); //12*12
//得到store中的a
console.log(store.getState().a); //144
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当dispatch 发出后 store变化了，而试图没有更新，需要使用订阅subscribe方法</p>
<p>1、 在组件内的 componentDidMount 声明周期内 强制刷新</p>
<pre><code class="copyable">componentDidMount()&#123;
    store.subscribe(()=>&#123;
      this.forceUpdate()
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、在入口文件中配置 subscribe,订阅后 重新 执行render</p>
<pre><code class="copyable">import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import store from './store'
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
)

store.subscribe(()=>&#123;
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    document.getElementById('root')
  )
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">使用redux 检查点</h2>
<ol>
<li>createStore 创建store</li>
<li>reducer 初始化、修改状态函数</li>
<li>getState 获取状态值</li>
<li>dispatch 提交更新</li>
<li>subscribe 变更订阅</li>
</ol>
<h3 data-id="heading-3"><a href="https://juejin.cn/post/7000683710735450143#%E5%8F%AF%E9%A2%84%E6%B5%8B%E7%8A%B6%E6%80%81%E5%AE%B9%E5%99%A8" target="_blank" title="#%E5%8F%AF%E9%A2%84%E6%B5%8B%E7%8A%B6%E6%80%81%E5%AE%B9%E5%99%A8"></a>可预测状态容器</h3>
<blockquote>
<p>Redux专门用于管理状态</p>
</blockquote>
<blockquote>
<p>使用Redux的主要优势之一是它可以帮助处理应用的共享状态，如果两个组件需要访问同一状态，这个两个组件同时需要访问同一状态的现象 称为“共享状态”。你可以将该状态提升到附近的父组件，但是如果该父组件在组件树种向上好几个组件的位置，那么将状态当做属性向下一个一个的传递，这项工作会变的很乏味。此外，在改父组件和子组件之间的组件甚至根本不需要访问该状态！！！</p>
</blockquote>
<blockquote>
<p>Redux不仅使我们能够有条理的方式存储数据，而且使我们能够在应用的任何位置快速获取该数据。只需要告诉Redux到底哪个组件需要哪个数据，它就会为你处理后续一切工作！</p>
</blockquote>
<p>借助Redux，你可以控制状态改变的时间、原因和方式。</p>
<h4 data-id="heading-4"><a href="https://juejin.cn/post/7000683710735450143#store-%E5%8D%95%E4%B8%80%E6%95%B0%E6%8D%AE%E6%BA%90" target="_blank" title="#store-%E5%8D%95%E4%B8%80%E6%95%B0%E6%8D%AE%E6%BA%90"></a>Store： 单一数据源</h4>
<p>步骤：引入createStore函数、引入reducer统领文件、创建store、试着弹出一个a。</p>
<blockquote>
<p>store包括应用的全局状态，全存储在一个对象树种。redux中的状态是只读的，React组件不能直接写入React状态，而是发出intent来更新状态（只有reducer的纯函数能够更改状态）。</p>
</blockquote>
<blockquote>
<p>store是用来持有state的，一个项目只有一个store，一个store中只有一个reducer（当然可以拆分，然后合并到一个index文件中）</p>
</blockquote>


























<table><thead><tr><th>store有下面的责任：</th></tr></thead><tbody><tr><td>持有app的state</td></tr><tr><td>允许通过getState()得到state</td></tr><tr><td>允许通过dispatch来改变state</td></tr><tr><td>只能有1个store在你的app中。</td></tr><tr><td>当你想切分你的数据逻辑，你应该考虑拆分reducer而不是拆分store。</td></tr><tr><td>创建一个reducer很简单，使用combineReducers()可以轻松合并多个reducer到一个。并且传入createStore()中</td></tr></tbody></table>
<p>得到Store的State的值，需要使用store.getState().a</p>
<h5 data-id="heading-5"><a href="https://juejin.cn/post/7000683710735450143#%E5%A4%8D%E6%9D%82%E7%9A%84state" target="_blank" title="#%E5%A4%8D%E6%9D%82%E7%9A%84state"></a>复杂的state</h5>
<p>state 可能是复杂的结构，此时写在行内不好看，可以提炼为变量（常量）</p>
<pre><code class="copyable">var redux = require("redux");

//初始state
const initState = &#123;
    students : [
        &#123;"id": 1, "name": "小明" , "age" : 12&#125;,
        &#123;"id": 2, "name": "小强" , "age" : 14&#125;,
        &#123;"id": 3, "name": "小钢炮" , "age" : 13&#125;
    ]
&#125;

//reducer
const reducer = (state = initState, action) => &#123;
    .........
    .........
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6"><a href="https://juejin.cn/post/7000683710735450143#reducer-%E7%BA%AF%E5%87%BD%E6%95%B0" target="_blank" title="#reducer-%E7%BA%AF%E5%87%BD%E6%95%B0"></a>reducer 纯函数</h4>
<blockquote>
<p>指的是一个函数接收A、B两个参数，根据B参数<em>返回</em>A参数的新值。</p>
</blockquote>














<table><thead><tr><th>记住4个no：</th></tr></thead><tbody><tr><td>No surprises. No side effects. No API calls. No mutations. Just a calculation.</td></tr><tr><td>没有惊喜、没有副作用、没有API调用、没有改变传入的参数。就是一个计算。</td></tr></tbody></table>
<p>纯函数是函数式编程的概念，必须遵守以下一些约束：</p>
<ul>
<li>不得改写参数</li>
<li>不能调用写I/O的API</li>
<li>不能调用Date.now() 或者Math.random()等不纯的方法，因为每次得到不一样的结果</li>
</ul>
<p>Reducer是纯函数，就可以保证同一的state，必定得到同样的View，Reducer函数里面不能改变State，必须返回一个全新的对象。</p>
<p>一个函数会有很多reducer，所以要有一个index.js作为“统领文件”</p>
<h3 data-id="heading-7"><a href="https://juejin.cn/post/7000683710735450143#dispatch%E5%92%8Caction" target="_blank" title="#dispatch%E5%92%8Caction"></a>dispatch和action</h3>
<blockquote>
<p>唯一能够改变state的方法就是dispatch一个action</p>
</blockquote>
<p><em>store.disptch()</em></p>
<h4 data-id="heading-8"><a href="https://juejin.cn/post/7000683710735450143#action" target="_blank" title="#action"></a>action</h4>
<ul>
<li>Action就是一个信息的载荷体，从APP（逻辑层、视图层）送到你的store中（数据层）。</li>
<li>action是store唯一的信息的来源。</li>
<li>action需要被dispatch()函数派发。</li>
<li>action是纯的、扁平的JavaScript对象。</li>
<li>action必须有一个type属性，type属性指示了这个action是干嘛的。</li>
</ul>
<p>action就是一个有type属性的JSON：</p>
<pre><code class="copyable">&#123;"type" : "ADD"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9"><a href="https://juejin.cn/post/7000683710735450143#payload-%E8%BD%BD%E8%8D%B7" target="_blank" title="#payload-%E8%BD%BD%E8%8D%B7"></a>payload 载荷</h4>
<p>action不仅有type属性，其他的属性，叫做载荷（payload）</p>
<h4 data-id="heading-10"><a href="https://juejin.cn/post/7000683710735450143#combinereducers-%E5%90%88%E5%B9%B6%E5%A4%9A%E4%B8%AAreducer" target="_blank" title="#combinereducers-%E5%90%88%E5%B9%B6%E5%A4%9A%E4%B8%AAreducer"></a>combineReducers 合并多个reducer</h4>
<blockquote>
<p>不同的业务放在多个标准的reducer中，最后用redux.combineReducer()合并一下。</p>
</blockquote>
<p>注意：</p>
<ul>
<li>访问值的时候，多个一个命名空间</li>
<li>改变值的时候，没有命名空间</li>
</ul>
<pre><code class="copyable">//要合并reducer，因为任何项目只能有一个reducer。
const reducer = redux.combineReducers(&#123;
    counterReducer ,
    studentReducer
&#125;);

//store，不管项目有多大，一定只有一个store
const store = redux.createStore(reducer);

//注意，访问值的时候，多了一个命名空间
console.log(store.getState().counterReducer.a);

//但是，改变值的时候，没有命名空间
store.dispatch(&#123; "type" : "ADD"&#125;);
store.dispatch(&#123; "type" : "ADD"&#125;);
store.dispatch(&#123; "type" : "ADD"&#125;);

//注意，访问值的时候，多了一个命名空间
console.log(store.getState().counterReducer.a);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11"><a href="https://juejin.cn/post/7000683710735450143#react%E5%92%8Credux%E9%85%8D%E5%90%88%E4%BD%BF%E7%94%A8" target="_blank" title="#react%E5%92%8Credux%E9%85%8D%E5%90%88%E4%BD%BF%E7%94%A8"></a>React和Redux配合使用</h2>
<p>所有的数据要保存在store中</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7874771bb2554fb29d065a0a43ded08c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">配置和使用</h3>
<ol>
<li>先配置好webpack+react那一套 安装依赖</li>
</ol>
<pre><code class="copyable">npm install --save redux
npm install --save react-redux
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>react-redux 是官方的“粘合剂”</li>
<li>
<ul>
<li>这个粘合剂就提供了两个东西：Provider组件、connect函数。</li>
</ul>
</li>
</ul>
<ol start="2">
<li>Provider from react-redux</li>
</ol>
<p>main.js</p>
<pre><code class="copyable">import React from "react";
import ReactDOM from "react-dom";
import &#123;createStore&#125; from "redux";
import &#123;Provider&#125; from "react-redux";

import App from "./App";
import reducer from "./reducers";

//创建store
const store = createStore(reducer);


ReactDOM.render(
    <Provider store=&#123;store&#125;>
        <App></App>
    </Provider>
    ,
    document.getElementById("app")
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>app.js</p>
<ul>
<li>import &#123; connect &#125; from "react-redux"</li>
</ul>
<pre><code class="copyable">import React, &#123; Component &#125; from 'react';
import &#123; connect &#125; from "react-redux";

class App extends Component &#123;
    constructor()&#123;
        super();
    &#125;
    render() &#123;
        return (
            <div>
                <h1>根组件&#123;this.props.a&#125;</h1>
                <button onClick=&#123;()=>&#123;
                    this.props.add();
                &#125;&#125;>按我加1</button>
            </div>
        )
    &#125;
&#125;
//connect 函数 有两个参数和需要连接的组件App
export default connect(
    (&#123;counterReducer&#125;) => (&#123;
        a : counterReducer.a
    &#125;),
    (dispatch) => (&#123;
        add()&#123;
            dispatch(&#123;"type" : "ADD"&#125;)
        &#125;
    &#125;)
)(App);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">Provider</h3>
<ul>
<li>Provider 是组件，在main.js入口文件中用一次</li>
<li>connect 是函数，哪个组件要“通天”要数据，哪个组件就要connect装饰一下。</li>
<li>Provider的机理是使用context上下文机理。</li>
</ul>
<p>Provider使用起来很简单，引包之后，包裹app，注意store属性：</p>
<pre><code class="copyable">import &#123;Provider&#125; from "react-redux";

ReactDOM.render(
    <Provider store=&#123;store&#125;>
        <App></App>
    </Provider>
    ,
    document.getElementById("app")
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14"><a href="https://juejin.cn/post/7000683710735450143#connect%E8%A3%85%E9%A5%B0%E5%99%A8" target="_blank" title="#connect%E8%A3%85%E9%A5%B0%E5%99%A8"></a>connect装饰器</h3>
<p>语法：</p>
<pre><code class="copyable">connect(mapStateToProps , mapDispatchToProps)(类名字)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>组件要更新视图，只有两种手段：</li>
<li>
<ul>
<li>组件自己的state改变</li>
</ul>
</li>
<li>
<ul>
<li>传入组件的props改变</li>
</ul>
</li>
<li>全局store数据变化了，组件视图要更新。</li>
<li>store中的数据，要被“装饰”到组件上，成为组件的props。</li>
</ul>
<p>组件要被connect()()装饰一下，才能暴露：</p>
<ul>
<li>第一个（）内写如何装饰，第二个（）内写装饰谁。</li>
<li>
<ul>
<li>第一个（）有两个参数 mapStateToProps和mapDispatchToProps</li>
</ul>
</li>
</ul>
<h4 data-id="heading-15"><a href="https://juejin.cn/post/7000683710735450143#mapstatetopropsstate-ownprops" target="_blank" title="#mapstatetopropsstate-ownprops"></a>mapStateToProps（state, ownProps）</h4>
<ul>
<li>mapStateToProps 是一个函数，用于建立组件跟store的state的映射关系，它传入两个参数，结果一定返回一个object。</li>
<li>mapStateToProps 可以不传，如果不传，组件不会监听store的变化，也就是说Store的更新不会引起UI的更新。</li>
</ul>
<pre><code class="copyable">export default connect(
    (&#123;counterReducer&#125;) => (&#123;
        a : counterReducer.a
    &#125;)
)(App);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数的形参中罗列reducer的名字，要用大括号包裹，函数返回值是一个对象，所以必须有一个小括号对。</p>
<p>这个返回的对象的所有的键，将成为组件的props。</p>
<pre><code class="copyable"><h1>根组件&#123;this.props.a&#125;</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">mapDispatchToProps</h4>
<p>mapDispatchToProps 用于建立组件跟store.dispatch的映射关系，可以是一个objeft，也可以传入一个函数</p>
<pre><code class="copyable">export default connect(
    (&#123;counterReducer&#125;) => (&#123;
        a: counterReducer.a
    &#125;),
    (dispatch) => (&#123;
        add()&#123;
            dispatch(&#123;"type" : "ADD"&#125;)
        &#125;
    &#125;)
)(App);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17"><a href="https://juejin.cn/post/7000683710735450143#logger-%E8%BE%93%E5%87%BA%E5%99%A8%E7%9A%84%E5%AE%89%E8%A3%85" target="_blank" title="#logger-%E8%BE%93%E5%87%BA%E5%99%A8%E7%9A%84%E5%AE%89%E8%A3%85"></a>logger -- 输出器的安装</h2>
<ul>
<li>一装一引一配 安装依赖</li>
</ul>
<pre><code class="copyable">npm install --save redux-logger
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js中的配置</p>
<pre><code class="copyable">import React from "react";
import ReactDOM from "react-dom";
import &#123;createStore , applyMiddleware&#125; from "redux";
import &#123;Provider&#125; from "react-redux";
import logger from "redux-logger";
 
import App from "./App";
import reducer from "./reducers";

//创建store
const store = createStore(reducer , applyMiddleware(logger));
 
ReactDOM.render(
    <Provider store=&#123;store&#125;>
        <App></App>
    </Provider>
    ,
    document.getElementById("app")
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>今后就能在任何一次dispatch发出的时候，看见控制台的自动输出：能够看见改变前的state、发出的action、改变之后的state。</p></div>  
</div>
            