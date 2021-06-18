
---
title: 'Redux-Saga基本使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7293'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 00:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7293'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文着重讲解Redux-Saga基本的使用，同时需要您有一些ES6_Generator/Redux/React-Redux/React相关知识。相关安装包有：redux,react-redux,redux-saga。</p>
</blockquote>
<h1 data-id="heading-0">1，Redux-Saga简述：</h1>
<p>redux-saga是redux的中间件，主要负责处理从action派发到更新store装填中间具有副作用行为的处理。</p>
<h1 data-id="heading-1">2，开始使用Redux-Saga</h1>
<blockquote>
<p>我们将使用create-react-app创建一个我们自己的react应用，该应用行为即点击按钮，页面上的数据完成+1行为。</p>
</blockquote>
<ul>
<li>
<p>下面是react的入口文件，我们使用了redux，react-redux进行状态管理，并使用了redux-saga中间件。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 当前路径：src/index.js</span>

    <span class="hljs-comment">// 第三方模块引入</span>
    <span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>  
    <span class="hljs-keyword">import</span> ReactDom <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
    <span class="hljs-keyword">import</span> &#123; Provider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>
    <span class="hljs-keyword">import</span> &#123; createStore, applyMiddleware &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
    <span class="hljs-keyword">import</span> createSagaMiddleware <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-saga'</span>

    <span class="hljs-comment">// 自定义模块引入</span>
    <span class="hljs-comment">// 1，redux中的 reducer引入</span>
    <span class="hljs-keyword">import</span> rootReducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./LearningSaga/reducer'</span>
    <span class="hljs-comment">// 2，react中 Counter组件引入</span>
    <span class="hljs-keyword">import</span> Counter <span class="hljs-keyword">from</span> <span class="hljs-string">'./LearningSaga/component'</span>
    <span class="hljs-comment">// 3， redux-saga中间件的 saga文件引入</span>
    <span class="hljs-keyword">import</span> rootSaga <span class="hljs-keyword">from</span> <span class="hljs-string">'./LearningSaga/saga'</span>

    <span class="hljs-comment">// 4，创建一个redux-saga中间件</span>
    <span class="hljs-keyword">const</span> sagaMiddleware = createSagaMiddleware()
    <span class="hljs-comment">// 5，将redux-saga中间件加入到redux中</span>
    <span class="hljs-keyword">const</span> store = createStore(rootReducer, &#123;&#125;, applyMiddleware(sagaMiddleware))
    <span class="hljs-comment">// 6，动态的运行saga，注意 sagaMiddleware.run(rootSaga) 只能在applyMiddleware(sagaMiddleware)之后进行</span>
    sagaMiddleware.run(rootSaga)

    <span class="hljs-comment">// 7，挂载react组件</span>
    ReactDom.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span><span class="hljs-tag"><<span class="hljs-name">Counter</span> /></span><span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>注释1是我们要用到的reducer，下面是reducer文件内容，很简单，我们创建了counterReducer，并使用redux提供的combineReducers处理并返回出去，熟悉redux使用的话，这里应该不用太多赘述，就是一个简单的对state.counter进行递增处理的reducer。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 当前路径：src/LearningSaga/reducer/index.js</span>

<span class="hljs-keyword">import</span> &#123; combineReducers &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">counterReducer</span>(<span class="hljs-params">state = <span class="hljs-number">1</span>, action = &#123;&#125;</span>) </span>&#123;
    <span class="hljs-keyword">switch</span> (action.type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"increment"</span>: <span class="hljs-keyword">return</span> state + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">default</span>: <span class="hljs-keyword">return</span> state
    &#125;
&#125;

<span class="hljs-keyword">const</span> rootReducer = combineReducers(&#123; <span class="hljs-attr">counter</span>: counterReducer &#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> rootReducer
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>注释2是我们react挂载的一个Counter组件，下面是Counter组件代码，也是个很简单的组件，其中使用了react-redux对Counter进行处理，这样就能在this.props中获取到redux中的状态以及dispatch方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 当前路径：src/LearningSaga/component/index.js</span>

<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Counter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-comment">// 派发一个type为 increment_saga 的action</span>
    add = <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.props.dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'increment_saga'</span> &#125;)
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;this.props.counter&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.add&#125;</span>></span>add1-sync<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="hljs-keyword">const</span> mapStateToProps = <span class="hljs-function"><span class="hljs-params">state</span> =></span> (&#123; <span class="hljs-attr">counter</span>: state.counter &#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(mapStateToProps)(Counter)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>注释4567完成了对redux创建，redux中redux-saga中间件的使用，以及Counter组件的挂载等。当然这里redux-saga中间件处理方式可能和其它中间件方式略有不同。</p>
</li>
<li>
<p>在讲注释3之前我们先回顾一下Counter组件的使用，首先Counter组件渲染出store（redux）中counter数据和一个递增按钮add1-sync，点击该按钮将派发一个类型为increment_saga的action。我们期待的事 是该动作派发后，store中的counter数据能够加1，其实如果仅是如此，我们派发一个类型为increment的action就可以做到，因为我们在注释1的reducer中已经实现了对类型为increment的action处理。但我们这里要用redux-saga中间件替我们完成，我们可以想一下redux-saga中间件要完成这个加1行为大概要做怎样一件事，首先，拦截到action，然后做一些处理，最后更新store中的counter数据完成+1。没错，redux-saga中间件的流程就是这样，所以按照这个流程回头看，<strong>这里我们派发一个类型为increment_saga的action，redux-saga中间件获取到该action，因为这个行为很纯粹就是+1，redux-saga中间件再继续调用<code>dispatch(&#123;type:'increment'&#125;)</code>完成对store中counter数据+1。</strong></p>
</li>
<li>
<p>现在回到注释3，这是redux-saga中saga文件，下面是该文件的代码，我们看到该文件中的函数全是generator函数，没错，redux-saga的世界中，就是通过这些generator函数完成dispatch过程中副作用的处理（当然我们现在这个+1例子中还没涉及到一些强烈具有副作用的行为），这些generator函数我们叫它saga。saga中yield 后面的内容我们称呼它为Effects(redux-saga的任务单元)，在Effects中我们可以进行启动其它saga，也可以处理一些副作用操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 当前路径：src/LearningSaga/saga/index.js</span>

<span class="hljs-keyword">import</span> &#123; all, put, takeEvery &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-saga/effects'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">increment</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 相当于：dispatch(&#123; type: 'increment' &#125;)</span>
    <span class="hljs-keyword">yield</span> put(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'increment'</span> &#125;) 
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">watchIncrement</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 监听类型为increment_saga的action，监听到启动increment</span>
    <span class="hljs-keyword">yield</span> takeEvery(<span class="hljs-string">'increment_saga'</span>, increment) 
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">rootSaga</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 启动watchIncrement</span>
    <span class="hljs-keyword">yield</span> all([watchIncrement()])
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> rootSaga
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>这里我们导出的是一个rootSaga函数，该函数内容很简单，只有一行<code> yield all([watchIncrement()])</code>，其中all是redux-saga所提供的一个方法，用来启动一个或多个Effects，这里我们只启动了一个watchIncrement的saga。</p>
</li>
<li>
<p>继续看watchIncrement这个saga，函数内容仅有一行<code>yield takeEvery('increment_saga', increment)</code>，其中takeEvery是redux-saga提供的一个方法，该方法传入两个参数（type,saga），其中type即对应action中的type，而saga则是redux-saga中间件匹配到对应type的action时需要启动的saga。<strong>所以这行代码的作用很简单，就是监听action类型为increment_saga，并启动对应saga进行处理该action。</strong> 现在假设watchIncrement监听到类型为increment_saga的动作，启动increment这个saga进行处理。我们进入increment函数中看看做了什么。</p>
</li>
<li>
<p>increment这个saga中也仅有一行代码<code> yield put(&#123; type: 'increment' &#125;)</code>，这行代码中put也是redux-saga提供的一个方法,其参数为一个action，其作用是产生一个dispatch行为的Effect，其action就是put中的参数action。我们可以理解这个动作就相当于<code>dispatch(&#123; type: 'increment' &#125;)</code>。所以这里将派发一个类型为increment动作去更新store中的state。</p>
</li>
<li>
<p>现在整个saga文件已经介绍完它的作用，我们来复盘<strong>从Counter组件点击add1-sync按钮那一刻到最后store中的counter数据加1的流程。</strong></p>
<ul>
<li>
<p>1，react入口文件中注释6启动了rootSaga，rootSaga执行<code>yield all([watchIncrement()])</code>，即启动了watchIncrement这个saga，并等待它运行完成</p>
</li>
<li>
<p>2，watchIncrement的作用在前面说了，是监听类型为increment_saga的action，如果监听到，则启动increment这个saga对action进行进一步处理。</p>
</li>
<li>
<p>3，现在Counter组件中add1-sync按钮点击，派发一个类型为increment_saga的动作。</p>
</li>
<li>
<p>4，watchIncrement这个saga监听到该动作（type:'increment_saga'），启动increment对该action进行处理。</p>
</li>
<li>
<p>5，increment中通过<code> yield put(&#123; type: 'increment' &#125;)</code> 派发一个类型为increment的action出去</p>
</li>
<li>
<p>6，reducer接受到类型为increment的action，执行对应的更新行为，完成store中counter数据+1的过程。</p>
</li>
<li>
<p>7，最后更新Counter组件中的<code>this.props.counter</code>数据（这个自动更新行为由react-redux替我们完成）。</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h1 data-id="heading-2">3，带有副作用的counter数据更新</h1>
<blockquote>
<p>我们将在原Counter组件 基础上增加一个add1-async按钮，点击该按钮将在1s后对counter数据进行+1</p>
</blockquote>
<ul>
<li>
<p>在原Counter组件上新增add1-async按钮</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 当前路径：src/LearningSaga/component/index.js</span>

<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Counter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    add = <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.props.dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'increment_saga'</span> &#125;)
    <span class="hljs-comment">// addAsync函数将派发一个类型为incrementAsync_saga的action</span>
    addAsync = <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.props.dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'incrementAsync_saga'</span> &#125;)
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;this.props.counter&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.add&#125;</span>></span>add1-sync<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.addAsync&#125;</span>></span>add1-async<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="hljs-keyword">const</span> mapStateToProps = <span class="hljs-function"><span class="hljs-params">state</span> =></span> (&#123; <span class="hljs-attr">counter</span>: state.counter &#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(mapStateToProps)(Counter)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>我们也要在saga文件中添加incrementAsync_saga动作对应的saga进行处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 当前路径：src/LearningSaga/saga/index.js</span>

<span class="hljs-keyword">import</span> &#123; all, put, takeEvery, delay &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-saga/effects'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">increment</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">yield</span> put(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'increment'</span> &#125;) <span class="hljs-comment">// 相当于：dispatch(&#123; type: 'increment' &#125;)</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">incrementAsync</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 延迟1s</span>
    <span class="hljs-keyword">yield</span> delay(<span class="hljs-number">1000</span>)
    <span class="hljs-comment">// 1s后，dispatch(&#123; type: 'increment' &#125;)</span>
    <span class="hljs-keyword">yield</span> put(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'increment'</span> &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">watchIncrement</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">yield</span> takeEvery(<span class="hljs-string">'increment_saga'</span>, increment) <span class="hljs-comment">// 监听类型为increment_saga的action，监听到启动increment</span>

    <span class="hljs-comment">// 监听类型为incrementAsync_saga的action，监听到启动incrementAsync</span>
    <span class="hljs-keyword">yield</span> takeEvery(<span class="hljs-string">'incrementAsync_saga'</span>, incrementAsync)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">rootSaga</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">yield</span> all([watchIncrement()]) <span class="hljs-comment">// 启动watchIncrement</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> rootSaga
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>我们在watchIncrement添加了新的一行代码<code> yield takeEvery('incrementAsync_saga', incrementAsync)</code>，上一节中学习我们知道，这行代码作用是 <strong>监听类型为incrementAsync_saga的action，监听到启动incrementAsync。</strong></p>
</li>
<li>
<p>继续看incrementAsync，相较于之前的increment，多了一行代码<code> yield delay(1000)</code>，其中delay是redux-saga提供的延迟函数，该行代码表示延迟1s后才可以继续处理之后的代码。其本质可以看做这么个函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// delay 相当于这里的 delay_</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">delay_</span>(<span class="hljs-params">timeout</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> r(), timeout);
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>所以延迟1s后，继续执行<code> yield put(&#123; type: 'increment' &#125;)</code>，即相当于<code>dispatch(&#123; type: 'increment' &#125;)</code> 完成counter更新。</p>
</li>
</ul>
</li>
</ul></div>  
</div>
            