
---
title: 'React基础篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47065bcf3f044e1d8959dd838e638f81~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 08:44:36 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47065bcf3f044e1d8959dd838e638f81~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">React基础篇</h2>
<h3 data-id="heading-1">一、<code>setState</code></h3>
<h4 data-id="heading-2">1.正确使用<code>setState</code></h4>
<blockquote>
<p>由于数据是双向绑定的原因，当数据频繁的被操作 ，会触发<code>dom</code>页面不断的刷新，如果数据量大的话，还会导致的卡顿，对性能消耗比较大，所以React官方统一使用<code>setState</code>函数批量的更新数据</p>
</blockquote>
<p><code>setState(partialState, callback)</code></p>
<ol>
<li>
<p><code>partialState</code>:  object| function</p>
<p>用于产生于当前state合并的子集。</p>
</li>
<li>
<p><code>callback</code>: function</p>
<p>state更新之后被调用</p>
</li>
</ol>
<h4 data-id="heading-3">2. 关于<code>setState()</code>的三件事</h4>
<h5 data-id="heading-4">不要直接修改State</h5>
<p>例如，此代码不会重新渲染组件:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 错误示范</span>
<span class="hljs-built_in">this</span>.state.comment = <span class="hljs-string">'hello'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而是应该使用<code>setState()</code>:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 正确使用</span>
<span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">comment</span>:<span class="hljs-string">'Hello'</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">State的更新可能是异步的</h5>
<p>出于性能考虑，React可能会把多个<code>setState()</code>调用合并成一个调用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SetStatePage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
   <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(props);
        <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
        &#125;
    &#125;
    changeValue = <span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">counter</span>: <span class="hljs-built_in">this</span>.state.counter + v
        &#125;)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'counter'</span>, <span class="hljs-built_in">this</span>.state.counter)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; counter &#125; = <span class="hljs-built_in">this</span>.state
        <span class="hljs-keyword">return</span> ( 
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>SetStatePage<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.setCounter&#125;</span>></span>&#123;counter&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要获取到最新状态值有以下方式：</p>
<ol>
<li>
<p>在回调中获取状态值</p>
<pre><code class="hljs language-js copyable" lang="js">changeValue = <span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">counter</span>: <span class="hljs-built_in">this</span>.state.counter + v
    &#125;, <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'counter'</span>, <span class="hljs-built_in">this</span>.state.counter)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用定时器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">this</span>.changeValue();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>原生事件中修改状态</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    docment.body.addEventLister(<span class="hljs-string">'click'</span>, <span class="hljs-built_in">this</span>.changeValue, <span class="hljs-literal">false</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h5 data-id="heading-6">总结： <code>setState</code>只有在合成事件和生命周期函数中是异步的，在原生事件和<code>setTimeout</code>中都是同步的，这里的异步其实是批量更新。</h5>
<h5 data-id="heading-7"><code>State</code>的更新会被合并</h5>
<pre><code class="hljs language-js copyable" lang="js">changeValue = <span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">counter</span>: <span class="hljs-built_in">this</span>.state.counter + v
    &#125;)
&#125;
setCounter = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.changeValue(<span class="hljs-number">1</span>);
    <span class="hljs-built_in">this</span>.changeValue(<span class="hljs-number">2</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想要链式更新<code>state</code></p>
<pre><code class="copyable">changeValue = v => &#123;
this.setState(state=>(&#123;counter: state.counter + v &#125;));
&#125;
setCounter = () => &#123;
this.changeValue(1);
this.changeValue(2);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">二、 组件生命周期</h3>
<blockquote>
<p>生命周期方法，用于在组件不同阶段执行自定义功能。在组件被创建插入到Dom时(即 挂载中阶段（mounting）)，组件更新时，组件取消挂载或从DOM中删除时，都有可以使用的生命周期方法。</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47065bcf3f044e1d8959dd838e638f81~tplv-k3u1fbpfcp-watermark.image" alt="React16.3的生命周期.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>V16.4之后的生命周期：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/053b3a8faea440528d9719187fbeff99~tplv-k3u1fbpfcp-watermark.image" alt="1628399943022.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>V17可能会废弃的三个生命周期函数用getDerivedStateFromProps替代，目前使用的话加上UNSAFGE_:</p>
<ul>
<li>componentWillMount</li>
<li>componentWilReceiveProps</li>
<li>componentWillUnUpdate</li>
</ul>
<p>引入两个新的生命周期函数：</p>
<ul>
<li>static getDerivedStateFromProps</li>
<li>getsnapshotBeforeUpdate</li>
</ul>
<h4 data-id="heading-9">新引入的两个生命周期函数</h4>
<h5 data-id="heading-10"><code>getDerivedStateFromPropos</code></h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> getDerivedStateFromProps(nextProps, preState) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>getDerivedStateFromProps</code>会在render之前调用，并且在初始挂载及后续更新时都会被调用。它应返回一个对象来更新<code>state</code>,如果返回null则不更新任何内容</p>
<p>请注意，不管原因时什么，都会在每次渲染前触发此方法。这次</p>
<p><code>UNSAFE_componentWillReceviProps</code>形成对比，后者仅在父组件重新渲染时触发，而不是在内部调用<code>setState</code>时。</p>
<h4 data-id="heading-11">getSnapshotBeforeUpdate</h4>
<p><code>getSnapshotBeforeUpdate(preProps, preveState)</code></p>
<p>在render之后，在componentDidUpdate之前。</p>
<p><code>getSnaopshotBeforeUpdate()</code>在最新一次渲染输出（提交到Dom节点）之前调用。它使得组件能在发生更新之前从Dom中捕获一些信息（例如：滚动位置）。此生命周期的任何返回值将作为参数传递<code>componentDidUpdate(preProps, prevState, snapshot)</code>。</p>
<h3 data-id="heading-12">三、<code>Redux</code></h3>
<p><code>redux</code>是<code>JavaScript</code>应用的状态容器，提供可预测的状态管理。它保证程序行为一致性且易于测试。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c8e7ab17f294c8d9340799a8160be2d~tplv-k3u1fbpfcp-watermark.image" alt="redux.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实操案例：</p>
<pre><code class="copyable">1. 需要一个store来存储数据
2. store里的reducer初始化state并定义state修改规则
3. 通过dispatch一个action来提交对数据的修改
4. action提交到reducer函数里，根据传入的action的type，返回新的state
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建store, <code>src/store/ReaduxStore.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-keyword">const</span> counterReducer = <span class="hljs-function">(<span class="hljs-params">state=<span class="hljs-number">0</span>, action</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span>(action.type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'ADD'</span>:
            <span class="hljs-keyword">return</span> state + <span class="hljs-number">1</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'MINUS'</span>:
            <span class="hljs-keyword">return</span> state - <span class="hljs-number">1</span>
         <span class="hljs-attr">default</span> : 
            <span class="hljs-keyword">return</span> state
    &#125;
&#125;
<span class="hljs-keyword">const</span> store = createStore(counterReducer)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建ReducPage</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"../store/ReduxStore"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReduxPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
 <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
     store.subscribe(<span class="hljs-function">() =></span> &#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"subscribe"</span>);
         <span class="hljs-built_in">this</span>.forceUpdate();
     &#125;);
 &#125;
 add = <span class="hljs-function">() =></span> &#123;
 store.dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"ADD"</span> &#125;);
 &#125;;
 minus = <span class="hljs-function">() =></span> &#123; store.dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"MINUS"</span> &#125;);
 <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
     <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"store"</span>, store);
     <span class="hljs-keyword">return</span> (
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>ReduxPage<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;store.getState()&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.add&#125;</span>></span>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.minus&#125;</span>></span>minus<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
         <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>);
     &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果点击按钮不能更新，因为没有订阅(subscribe)状态变更</p>
</blockquote>
<p>还可以在src/index.js的render里订阅状态变更</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store/ReduxStore'</span>
<span class="hljs-keyword">const</span> render = <span class="hljs-function">()=></span>&#123;
    ReactDom.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span>/></span></span>,
     <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#root'</span>)
    )
&#125;
render()
store.subscribe(render)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">四、react-redux</h3>
<p><code>react-redux</code>是基于redux专门为react再次封装的存储器。</p>
<h4 data-id="heading-14">使用react-redux</h4>
<ol>
<li><code>Provider</code> 为后代组件提供store</li>
<li><code>connect</code>为组件提供数据和变更方法</li>
</ol>
<p>全局提供<code>store</code>,<code>index</code></p>
<p><code>src/index.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactDom <span class="hljs-keyword">from</span> <span class="hljs-string">'reacat-dom'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store/'</span>
<span class="hljs-keyword">import</span> &#123; Provider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>

ReactDom.render(
    <Provider store = &#123;store&#125;>
    <App/>
    <Provider>,
    docment.getElementById('root')
)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>store</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; crateStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>

<span class="hljs-comment">// 定义state初始化和修改规则,reduce 是一个纯函数</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">counterReducer</span> (<span class="hljs-params">state = <span class="hljs-number">0</span>, action</span>) </span>&#123;
    <span class="hljs-keyword">switch</span>(action.type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ADD"</span>:
            <span class="hljs-keyword">return</span> state + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"MINUS"</span>:
            <span class="hljs-keyword">return</span> state - <span class="hljs-number">1</span>;
        <span class="hljs-keyword">default</span>: 
            <span class="hljs-keyword">return</span> state;
    &#125;
&#125;

<span class="hljs-keyword">const</span> store = createStore(counterReducer)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>App.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactReduxPage <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/ReactReduxPage'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ReacatReduxPage</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ReactReduxPage.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(
  <span class="hljs-comment">//mapStateToProps 把state映射到props</span>
 <span class="hljs-function"><span class="hljs-params">state</span> =></span> (&#123;<span class="hljs-attr">num</span>: state&#125;)
 ,   
  <span class="hljs-comment">// mapDispatchToProps 把dispatch 映射到 props  默认会映射</span>
  &#123;
  <span class="hljs-attr">add</span>:<span class="hljs-function">()=></span>(&#123;<span class="hljs-attr">type</span>:<span class="hljs-string">"ADD"</span>&#125;) 
  &#125;
)( calss ReactReduxPage <span class="hljs-keyword">extends</span> Componets &#123;
    <span class="hljs-keyword">const</span> &#123; num, dispatch , add &#125; = <span class="hljs-built_in">this</span>.props;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h3</span>></span> ReactReduxPage <span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;num&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                &#123;/*<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;</span> () =></span> dispatch(&#123; type:"ADD" &#125;)&#125;>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>*/&#125;
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">add</span> &#125;></span>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">五、react-router</h3>
<h4 data-id="heading-16">前言</h4>
<p>react-router包含3个库，react-router、react-router-dom和react-router-native。react-router提供最基本的路由功能，实际使用的时候我们不会直接安装<code>react-router</code>,而是根据应用运行环境选择安装<code>react-router-dom</code>(在浏览器使用)或者<code>react-router-native</code>在（rn中使用）。react-router-dom和react-router-native都依赖<code>react-router</code>,所以安装时，react-router也会自动安装，创建web应用</p>
<h4 data-id="heading-17">安装</h4>
<pre><code class="hljs language-js copyable" lang="js">npm i --save react-router-dom
<span class="copy-code-btn">复制代码</span></code></pre>
<p>案例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; BrowserRouter <span class="hljs-keyword">as</span> Router, Route, NavLink, Switch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>用户中心<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>   
        )
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">home</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>   
        )
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EmptyPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>404<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>   
        )
    &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">homePage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">NavLink</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">NavLink</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">NavLink</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/user-page"</span>></span>用户中心<span class="hljs-tag"></<span class="hljs-name">NavLink</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/user-page"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;UserPage&#125;</span> <span class="hljs-attr">children</span>=<span class="hljs-string">&#123;()</span>=></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span>children<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125; render=&#123;()=><span class="hljs-tag"><<span class="hljs-name">div</span>></span>render<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125; />
                        <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;home&#125;/</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;EmptyPage&#125;/</span>></span>
                    <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">Router</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">Route渲染内容的三种方式</h4>
<p>Route渲染优先级： children > component > render</p>
<h5 data-id="heading-19">children: fuc</h5>
<p>有时候，不管location是否匹配，你都需要渲染一些内容，这时候你可以用children。</p>
<p>除了不管location是否匹配都会被渲染之外，其它工作方法与render完全一样。</p>
<h5 data-id="heading-20">render: fuc</h5>
<p>但是当你调用render的时候，你调用的只是函数。</p>
<p>只在当location匹配的时候渲染</p>
<h5 data-id="heading-21">component: component</h5>
<p>只在当location匹配的时候渲染</p>
<h4 data-id="heading-22">404页面</h4>
<p>设定一个没有path的路由在路由列表最后，表示一定匹配</p>
<pre><code class="hljs language-js copyable" lang="js">   &#123;<span class="hljs-comment">/* 添加Switch表示仅匹配一个 */</span>&#125;
   <Switch>
        &#123;<span class="hljs-comment">/* 根路由要添加exact，实现进准匹配 */</span>&#125;
<Route path=<span class="hljs-string">"/"</span> component=&#123;home&#125;/>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/user-page"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;UserPage&#125;</span> /></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;EmptyPage&#125;/</span>></span></span>
   </Switch>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">六、PureComponent</h3>
<h4 data-id="heading-24">实现性能优化</h4>
<p>定制了shouldComponentUpdata后的Component</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component, PureComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PureComponentPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123;
    <span class="hljs-title">constructor</span> (<span class="hljs-params">props</span>) &#123;
        <span class="hljs-built_in">super</span>(props)
        <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
            <span class="hljs-attr">obj</span>: &#123; <span class="hljs-attr">num</span>: <span class="hljs-number">0</span> &#125;
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">setCount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">count</span>: <span class="hljs-number">100</span>,
            <span class="hljs-attr">obj</span>: &#123;
                <span class="hljs-attr">num</span>: <span class="hljs-number">100</span>
            &#125;
        &#125;)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'render'</span>)
        <span class="hljs-keyword">const</span> &#123; count &#125;  = <span class="hljs-built_in">this</span>.state
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span> 
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span> &#123;this.setCount()&#125;&#125;>改变<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">浅比较</h4>
<p>缺点是必须要用class形式，而且要注意是<b>浅比较</b></p>
<h4 data-id="heading-26">与Component 比较</h4>
<p><code>React.PureComponent</code>与<code>React.component</code>很相似。两者的区别在于<code>React.Component</code>并未实现<code>shouldComponentUpdate()</code>,而<code>Rect.PureComponent</code>中以浅层对比prop和state的方式来实现了该函数。</p>
<p>如果赋予React组件相同的props和state，<code>render()</code>函数会渲染相同的内容，那么在某些情况下使用<code>React.PureComponent</code>可提高性能。</p>
<blockquote>
<p>注意</p>
<p><code>React.PureComponent</code>中的<code>shouldComponentUpdate()</code>仅作对象的浅层比较。如果对象中包含复杂的数据结构，则有可能因为无法检查深层的差别，产生错误的比对结果。仅在你的props和state较为简单时，才使用<code>React.PureComponent</code>，或者在深层数据结构发生变化时调用<code>forceUpdate()</code>来确保组件被正确地更新。你也可以考虑使用<code>immutable</code>对象加速嵌套数据的比较。</p>
<p>此外，<code>React.PureComponent</code>中的<code>shouldComponentUpdate()</code>将跳过所有子组件树的<code>prop</code>更新。因此，请确保所有子组件也都是“纯”的组件</p>
</blockquote>
<h3 data-id="heading-27">七、Hook</h3>
<h4 data-id="heading-28">认识Hook</h4>
<p><b>Hoook是什么?</b> Hook 是一个特殊的函数，它可以让你"钩入"React的特性。例如，<code>useState</code>是允许你在React函数组件中添加state的Hook。</p>
<p><b>什么时候我会用Hook?</b> 如果你在编写函数组件并意识到需要向其添加一些state，以前的做法是必须将其转化为class。现在你可以在现有的函数组件中使用Hook。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React,&#123;useState&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HookPage</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 定义一个叫count的state变量，初始值为0</span>
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span> 
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>setCount(count+1)&#125;>添加<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">使用Effect Hook</h4>
<p><code>Effect Hook</code>可以让你在函数组件中执行副作用操作。</p>
<p>数据获取，设置订阅以及手动更改React组件中的Dom都属于副作用。不管你知不知道这些操作，或是“副作用”这个名字，应该都在组件中使用过它们。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React,&#123;useState, useEffect&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HookPage</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)
    useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You cliced <span class="hljs-subst">$&#123;count&#125;</span> times`</span>
    &#125;)
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span> 
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>setCount(count+1)&#125;>添加<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在函数组件主体内（这里指在React渲染阶段）改变DOM、添加订阅、设置定时器、记录日志以及执行其他包含副作用的操作都是不被允许的，因为这可能会产生莫名其妙的bug并破坏UI的一致性。</p>
<p>使用<code>useEffect</code>完成副作用操作。赋值给<code>useEffect</code>的函数会在组件渲染到屏幕之后执行。你可以把effect看作React的纯函数式世界通往命令式世界的逃生通道。</p>
<p>默认情况下，effect将在每轮渲染结束执行。但你可以选择让它<code>在只有某些值改变的时候</code>才执行。</p>
<h4 data-id="heading-30">effect的条件执行</h4>
<p>默认情况下，effect会在每轮组件渲染完成执行。这样的话，一旦effect的依赖发生变化，它就会被重新创建。</p>
<p>然而，在某些场景下这么做可能会娇枉过去。比如，在上一章节的订阅实例中，我们不需要在每次组件更新时都创建新的订阅，而是仅需要在<code>source</code> props改变时重新创建。</p>
<p>要实现这一点，可以给<code>useEffect</code>传递第二个参数，它是effect所依赖的值数组。更新后的示例如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React,&#123;useState, useEffect&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HookPage</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">const</span> [date, setDate] = useState(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>())
  
    useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'effect'</span>)
        <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You cliced <span class="hljs-subst">$&#123;count&#125;</span> times`</span>
    &#125;,[count])

    useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">const</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
            setDate(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>())
         &#125;, <span class="hljs-number">1000</span>)
    &#125;,[])
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span> 
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>时间:&#123;date.toLocaleTimeString()&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>setCount(count+1)&#125;>添加<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，只有当useEffect第二个参数数组里的数值改变后才会重新创建订阅。</p>
<h4 data-id="heading-31">清除effect</h4>
<p>通常，组件卸载时需要清除effect创建的诸如订阅或计时器ID等资源。要实现这一点，<code>useEffect</code>函数需返回一个清除函数，以防止内存泄漏，清除函数会在组件卸载前执行。</p>
<pre><code class="hljs language-js copyable" lang="js">   useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">const</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
            setDate(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>())
         &#125;, <span class="hljs-number">1000</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-function">()=></span><span class="hljs-built_in">clearInterval</span>(timer)
    &#125;,[])
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">自定义Hook</h4>
<p>有时候我们会想要在组件之间重用一些状态逻辑。目前为止，有两种主流方案来解决这个问题：<code>高阶组件</code>和<code>reader props</code> 。自定义Hook可以让你在不增加组件的情况下达到同样的目的。</p>
<p>自定义Hook是一个函数，其名称以<code>use</code>开头，函数内部可以调用其他的Hook。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React,&#123;useState, useEffect&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HookPage</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)
    useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'effect'</span>)
        <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You cliced <span class="hljs-subst">$&#123;count&#125;</span> times`</span>
    &#125;,[count])

    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span> 
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>时间:&#123;useClock().toLocaleTimeString()&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>setCount(count+1)&#125;>添加<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="hljs-keyword">const</span> useClock = <span class="hljs-function">()=></span> &#123;
    <span class="hljs-keyword">const</span> [date, setDate] = useState(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>())
    useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">const</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
            setDate(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>())
         &#125;, <span class="hljs-number">1000</span>)
         <span class="hljs-keyword">return</span> <span class="hljs-function">()=></span> <span class="hljs-built_in">clearInterval</span>(timer)
    &#125;, [])
    <span class="hljs-keyword">return</span> date
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">Hook使用规则</h4>
<p>Hook就是Javascript函数，但是使用它们会有两个额外的规则：</p>
<ul>
<li>只能在<b>函数最外层</b> 调用Hook，不要在循环，条件判断或者子函数中调用。</li>
<li>只能在<b>React的函数组件</b> 中调用Hook。不要再其他Javscript函数中调用。（还有一个地方可以调用Hook--就是自定义的Hook中。）</li>
</ul>
<h4 data-id="heading-34">useMemo</h4>
<p>把“创建”函数和依赖项数组作为参数传入<code>useMemo</code>,它仅会再某个依赖项改变时才会重新计算memoized值。这种优化有助于避免再每次渲染时都进行高开销的计算。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123;useState, useMemo&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useMemoPage</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)
    
    <span class="hljs-keyword">const</span> expensive = useMemo(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'expensive'</span>)
        <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<count;i++)&#123;
            sum+=i;
        &#125;
        <span class="hljs-keyword">return</span> sum
    &#125;, [count])

    <span class="hljs-keyword">const</span> [value, setValue] = useState(<span class="hljs-string">''</span>)
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>UseMemoPage<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span>count: &#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span> expensive: &#123;expensive&#125; <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>setCount(count+1)&#125;>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value&#125;</span> <span class="hljs-attr">onInput</span>=<span class="hljs-string">&#123;event</span> =></span> setValue(event.target.value)&#125; ><span class="hljs-tag"></<span class="hljs-name">input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">useCallback</h4>
<p>把内联回调函数及依赖项数组作为参数传入<code>useCallback</code>, 它将返回该回调函数的memoized版本，该回调函数仅在某个依赖项改变时才会更新。当你把回调函数传递给经过优化的并使用引用相等性去避免非必要渲染（例如<code>shouldComponentUpdate</code>）的子组件时，它将非常有用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123;useState, useCallback , PureComponent&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">UseCallbackPage</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)

    <span class="hljs-keyword">const</span> addClick =useCallback(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<count;i++)&#123;
            sum+=i;
        &#125;
        <span class="hljs-keyword">return</span> sum
    &#125;,[count]) 
    <span class="hljs-keyword">const</span> [value, setValue] = useState(<span class="hljs-string">''</span>)
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>UseMemoPage<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span>count: &#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>setCount(count+1)&#125;>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value&#125;</span> <span class="hljs-attr">onInput</span>=<span class="hljs-string">&#123;event</span> =></span> setValue(event.target.value)&#125; ><span class="hljs-tag"></<span class="hljs-name">input</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Children</span> <span class="hljs-attr">addClick</span>=<span class="hljs-string">&#123;addClick&#125;</span> ></span><span class="hljs-tag"></<span class="hljs-name">Children</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Children</span>  <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123; 
        <span class="hljs-keyword">const</span> &#123; addClick &#125; = <span class="hljs-built_in">this</span>.props
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Children render'</span>)
        <span class="hljs-keyword">return</span>( <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>addClick&#125;>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
       <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>)
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            