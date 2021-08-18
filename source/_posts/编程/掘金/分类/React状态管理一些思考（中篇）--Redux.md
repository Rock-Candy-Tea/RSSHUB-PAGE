
---
title: 'React状态管理一些思考（中篇）--Redux'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3b530aaef354fc88d996d66cb5e387c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 04:40:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3b530aaef354fc88d996d66cb5e387c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>传送门，上一期：<a href="https://juejin.cn/post/6995497136510992414" target="_blank" title="https://juejin.cn/post/6995497136510992414">React状态管理一些思考（上篇)</a></p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<p>Redux是Dan Abramov在2015年发布，是React生态里最火的状态管理库，其主要有四个特性：</p>
<ul>
<li>
<p>可预测</p>
<ul>
<li>reducer是纯函数，所以状态是可预测的</li>
</ul>
</li>
<li>
<p>中心化</p>
<ul>
<li>全局只有一个store</li>
</ul>
</li>
<li>
<p>易调试</p>
<ul>
<li>action --> change state</li>
</ul>
</li>
<li>
<p>灵活性</p>
<ul>
<li>middleware机制</li>
</ul>
</li>
</ul>
<p>他的源码十分的简洁，但是其扩展的生态却十分丰富，设计思想非常🐂，下面让我们一起来学习。</p>
<h1 data-id="heading-1">设计思想</h1>
<p>要了解Redux的设计思想，首先看看React的设计思想——单向数据流，看下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3b530aaef354fc88d996d66cb5e387c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>State描述的就是当前用户的状态，View是根据当前State渲染出来的，根据View层响应不用的Action，Action改变State，重新渲染view层。
Redux的设计思想就是：</p>
<ol>
<li>
<p><strong>应用是一个状态机，视图和状态是一一对应的。</strong></p>
</li>
<li>
<p><strong>把所有的State都集中管理，让整个UI和整个状态都能有对应的管理。</strong></p>
</li>
</ol>
<h1 data-id="heading-2">基本概念</h1>
<h2 data-id="heading-3">Store</h2>
<p>Store数据保存的地方，也可以理解为一个容器，全局只能有一个store。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> store =  createStore(reducer, initialValue) 
<span class="hljs-keyword">const</span> store2 = createStore(reducer, enhancer)
<span class="hljs-keyword">const</span> store2 = createStore(recuder, initialvalue, enhancer)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">State</h2>
<p>某个时刻Store数据的快照就叫State。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> state =  store.getState()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Action</h2>
<p>改变State的唯一方式，他有一定 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fredux-utilities%2Fflux-standard-action" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/redux-utilities/flux-standard-action" ref="nofollow noopener noreferrer">格式规范</a> ：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> action = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD_TODO'</span>,
  <span class="hljs-attr">payload</span>: <span class="hljs-string">'Learn Redux'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Action creater 就是创建Action的工厂函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAction</span>(<span class="hljs-params">payload</span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD_TODO'</span>,
        payload,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Dispatch</h2>
<p>View层发出Action的唯一方式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">store.dispatch(action);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">Reducer</h2>
<p>Reducer是一个纯函数，他接受Action和当前state为参数，这意味着他会返回一个全新的state，即要求数据流为不可变性。
这里要说一下纯函数的定义:</p>
<ol>
<li>
<p>相同的输入总是返回相同的输出。</p>
</li>
<li>
<p>不能有副作用。</p>
</li>
</ol>
<blockquote>
<p>纯函数、不可变性其实都是函数式编程的术语，JS本身不是一门函数的语言，但是他可以实现纯函数的特性。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">recuder</span>(<span class="hljs-params">state, action</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"INCREMENT"</span>:
      <span class="hljs-keyword">return</span> state + <span class="hljs-number">1</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"DECREMENT"</span>:
      <span class="hljs-keyword">return</span> state - <span class="hljs-number">1</span>;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> state;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">store.subscribe</h2>
<p>订阅数据变化。一旦state发生改变，执行回调。
显然我们可以在这里实现自动渲染。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">store.subscribe(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> state = store.getState()
    <span class="hljs-built_in">console</span>.log(state)
    render(state)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">总结</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a6c0982a13d4dd586cdae0fe367f5c1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b6cdfd6af3d42708d9a0cc0e1747ce6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">源码解析</h1>
<h2 data-id="heading-11">源码实现</h2>
<p>源码简单实现Demo： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fthirsty-field-7ekbp%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/thirsty-field-7ekbp?file=/src/index.js" ref="nofollow noopener noreferrer">codesandbox.io/s/thirsty-f…</a></p>
<ul>
<li>
<p>createStore</p>
<ul>
<li>
<p>发布订阅模式</p>
</li>
<li>
<p>把state传递给listener，需要自己调用store.getState()。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux.js.org%2Ffaq%2Fdesign-decisions%23why-doesnt-redux-pass-the-state-and-action-to-subscribers" target="_blank" rel="nofollow noopener noreferrer" title="https://redux.js.org/faq/design-decisions#why-doesnt-redux-pass-the-state-and-action-to-subscribers" ref="nofollow noopener noreferrer">为什么？</a> 性能优化</p>
</li>
</ul>
</li>
<li>
<p>combineReducers</p>
<ul>
<li>namespace</li>
</ul>
</li>
<li>
<p>applyMiddleware</p>
<ul>
<li>
<p>compose</p>
</li>
<li>
<p>中间件机制</p>
</li>
<li>
<p>拓展灵活性的关键</p>
</li>
</ul>
</li>
</ul>
<h1 data-id="heading-12">Redux-react</h1>
<p>我们一般说的redux其实都是react和redux-react，前者是跟任何框架无关的状态管理库，后者是将它和react联系起来的关键。
redux在每次数据更新的时候，都会调用订阅数据更新的回调。
我们当然可以像之前的Demo那样，在每次数据更新的时候，重新渲染整个React组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">store.subscribe(<span class="hljs-function">() =></span> &#123;
  render()
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样每次都全量渲染性能肯定是不好的。
可以看到Redux本身是一个功能非常简单的状态管理库，一些性能优化。。。的方法都是没有的。</p>
<h2 data-id="heading-13">版本更新历史</h2>
<p>简单过一下更新历史：
4.x</p>
<ul>
<li>connect组件里面判断是否需要更新</li>
</ul>
<p>5.x</p>
<ul>
<li>
<p>解决了"zombie child" bugs</p>
</li>
<li>
<p>5.0实现了自己的一套Subscription，嵌套的子组件总是订阅最近的父节点。</p>
</li>
<li>
<p>所有的更新逻辑被移除到组件外面了。</p>
</li>
</ul>
<p>6.x</p>
<ul>
<li>
<p>v5依赖componentWillReceiveProps</p>
</li>
<li>
<p>完全依赖new context api提供的渲染能力</p>
</li>
<li>
<p>性能有问题</p>
</li>
</ul>
<p>7.x</p>
<ul>
<li>
<p>5的性能</p>
</li>
<li>
<p>Store 传入 prop</p>
</li>
<li>
<p>增加hooks api</p>
</li>
<li>
<p>connect实现用函数组件实现了</p>
</li>
<li>
<p>React.memo 提升性能</p>
</li>
<li>
<p>unstable_batchedUpdates() 实现了api来提升性能。</p>
</li>
<li>
<p>Hooks api</p>
</li>
</ul>
<h2 data-id="heading-14">connect分析</h2>
<p>Connect的心智模型：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">connect</span>(<span class="hljs-params">mapStateToProps, mapDispatchToProps</span>) </span>&#123;
  <span class="hljs-comment">// It lets us inject component as the last step so people can use it as a decorator.</span>
  <span class="hljs-comment">// Generally you don't need to worry about it.</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">WrappedComponent</span>) </span>&#123;
    <span class="hljs-comment">// It returns a component</span>
    <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
          <span class="hljs-comment">// that renders your component</span>
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span>
            &#123;/* <span class="hljs-attr">with</span> <span class="hljs-attr">its</span> <span class="hljs-attr">props</span>  */&#125;
            &#123;<span class="hljs-attr">...this.props</span>&#125;
            &#123;/* <span class="hljs-attr">and</span> <span class="hljs-attr">additional</span> <span class="hljs-attr">props</span> <span class="hljs-attr">calculated</span> <span class="hljs-attr">from</span> <span class="hljs-attr">Redux</span> <span class="hljs-attr">store</span> */&#125;
            &#123;<span class="hljs-attr">...mapStateToProps</span>(<span class="hljs-attr">store.getState</span>(), <span class="hljs-attr">this.props</span>)&#125;
            &#123;<span class="hljs-attr">...mapDispatchToProps</span>(<span class="hljs-attr">store.dispatch</span>, <span class="hljs-attr">this.props</span>)&#125;
          /></span></span>
        )
      &#125;
      
      <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// it remembers to subscribe to the store so it doesn't miss updates</span>
        <span class="hljs-built_in">this</span>.unsubscribe = store.subscribe(<span class="hljs-built_in">this</span>.handleChange.bind(<span class="hljs-built_in">this</span>))
      &#125;
      
      <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// and unsubscribe later</span>
        <span class="hljs-built_in">this</span>.unsubscribe()
      &#125;
    
      <span class="hljs-function"><span class="hljs-title">handleChange</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// and whenever the store state changes, it re-renders.</span>
        <span class="hljs-built_in">this</span>.forceUpdate()
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的实现可以保证每次数据，更新都可以重新渲染组件，但这不够。
传递给 <code>connect</code> 组件的参数（通过 <code>mapStateToProps</code> and <code>mapDispatchToProps</code> 生成的对象）的浅对比。
但是有一种情况是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> mapStateToProps = <span class="hljs-function"><span class="hljs-params">state</span> =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">objects</span>: state.objectIds.map(<span class="hljs-function"><span class="hljs-params">id</span> =></span> state.objects[id])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">reselect性能优化</h3>
<p>可能state的数组并没有变化，但是 <strong>每次都会map生成新的数组，</strong> 所以每次都会重新渲染。
解决办法可能是我们自己去实现should component update去深对比，性能不好，还挺麻烦。
更好的办法是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freselect" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/reselect" ref="nofollow noopener noreferrer">Reselect</a> ，详细可以看这篇文章： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F33985606" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/33985606" ref="nofollow noopener noreferrer">关于react, redux, react-redux和reselect的一些思考</a> ，详细解读使用过程中reselect优化性能的问题。
其实现原理，它有点像hooks中的useMemo，当依赖发生改变的时候，会重新计算值，如果依赖没有发生改变就直接返回旧的值，感兴趣可以看看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freselect%2Fblob%2Fmaster%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/reselect/blob/master/src/index.js" ref="nofollow noopener noreferrer">源码</a> 。
上面的例子可以改写为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createSelector &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'reselect'</span>

<span class="hljs-keyword">const</span> objectIdsSelecter = <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.objecctIds;
<span class="hljs-keyword">const</span> objectsSelect = <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.objects;

<span class="hljs-keyword">const</span> objectsSelecter = createSelector(
    objectIdsSelecter, 
    objectsSelect, 
    <span class="hljs-function">(<span class="hljs-params">objectIds, objects</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> objectIds.map(<span class="hljs-function"><span class="hljs-params">id</span> =></span> objects[id])
    &#125;)
)
<span class="hljs-keyword">const</span> mapStteToprops = <span class="hljs-function"><span class="hljs-params">state</span> =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">objects</span>: objectsSelecter(state)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">僵尸节点问题</h3>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Freact-redux-zombie-child-demo-forked-bl3ol%3Ffile%3D%2Fsrc%2Findex.js%3A1228-1236" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/react-redux-zombie-child-demo-forked-bl3ol?file=/src/index.js:1228-1236" ref="nofollow noopener noreferrer">demo</a></p>
</blockquote>
<p>原因分析：</p>
<ol>
<li>
<p>V5之前的版本，由于之前是class组件是在componentdidmount 里面去处理订阅逻辑的（ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freact-redux%2Fblob%2F4.x%2Fsrc%2Fcomponents%2Fconnect.js%23L211" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/react-redux/blob/4.x/src/components/connect.js#L211" ref="nofollow noopener noreferrer">源码实现部分</a> ），所以子组件会比父组件先订阅更新。</p>
</li>
<li>
<p>selectors函数提取状态依赖父组件给他传的props，但是父组件删除了某些state，props还没来得及更新，如果子组件先订阅状态，意味着他会先更新，但是子组件的selector 函数去读state，此时已经删除了，就会报错。</p>
</li>
</ol>
<p>解决方式：实现订阅树。
订阅模式：</p>
<p>现在订阅模式：</p>
<p><strong>也就是说子节点会订阅自己最近的父节点，而不是直接订阅store。</strong></p>
<h3 data-id="heading-17">实现部分</h3>
<h4 data-id="heading-18">实现 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freact-redux%2Fblob%2Fmaster%2Fsrc%2Futils%2FSubscription.js%23L9" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/react-redux/blob/master/src/utils/Subscription.js#L9" ref="nofollow noopener noreferrer">subscription</a> ，</h4>
<p>亮点：创建了一个订阅函数的双向链表 ->  好处就是增删的时候比较快。</p>
<h4 data-id="heading-19">整体用Functioncomponent重构</h4>
<p>亮点：userMemo返回渲染节点的效果 和React.memo 和  shouldComponentUpdate 返回false的效果是一样的。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freact-redux%2Fblob%2Fmaster%2Fsrc%2Fcomponents%2FconnectAdvanced.js%23L455" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/react-redux/blob/master/src/components/connectAdvanced.js#L455" ref="nofollow noopener noreferrer">实现部分</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">      <span class="hljs-comment">// If React sees the exact same element reference as last time, it bails out of re-rendering</span>
      <span class="hljs-comment">// that child, same as if it was wrapped in React.memo() or returned false from shouldComponentUpdate.</span>
      <span class="hljs-keyword">const</span> renderedChild = useMemo(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">if</span> (shouldHandleStateChanges) &#123;
          <span class="hljs-comment">// If this component is subscribed to store updates, we need to pass its own</span>
          <span class="hljs-comment">// subscription instance down to our descendants. That means rendering the same</span>
          <span class="hljs-comment">// Context instance, and putting a different value into the context.</span>
          <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ContextToUse.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;overriddenContextValue&#125;</span>></span>
              &#123;renderedWrappedComponent&#125;
            <span class="hljs-tag"></<span class="hljs-name">ContextToUse.Provider</span>></span></span>
          )
        &#125;

        <span class="hljs-keyword">return</span> renderedWrappedComponent
      &#125;, [ContextToUse, renderedWrappedComponent, overriddenContextValue])

      <span class="hljs-keyword">return</span> renderedChild
<span class="copy-code-btn">复制代码</span></code></pre>
<p>亮点: 对比props，判断是否更新组件的逻辑，变为了直接使用React.memo，因为React会帮我们自己浅对比，判断是否更新组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// [https://github.com/reduxjs/react-redux/blob/master/src/components/connectAdvanced.js#L474](https://github.com/reduxjs/react-redux/blob/master/src/components/connectAdvanced.js#L474)</span>
<span class="hljs-keyword">const</span> Connect = pure ? React.memo(ConnectFunction) : ConnectFunction
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">利用Context API特性实现订阅树</h4>
<p>由于context会找最近的Privider提供的值，可以在这里实现store的状态树。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freact-redux%2Fblob%2Fmaster%2Fsrc%2Fcomponents%2FconnectAdvanced.js%23L355" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/react-redux/blob/master/src/components/connectAdvanced.js#L355" ref="nofollow noopener noreferrer">源码</a>
overriddenContextValue中的subscription，被覆盖为这一层的connect的subscription。如果上一层</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> subscription = <span class="hljs-keyword">new</span> Subscription(
          store, <span class="hljs-comment">// 如果没有父，直接用store。</span>
          contextValue.subscription <span class="hljs-comment">// 用父状态的</span>
)

<span class="hljs-keyword">const</span> overriddenContextValue = useMemo(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">return</span> &#123;
  ...contextValue,
  subscription,
&#125;
&#125;, [didStoreComeFromProps, contextValue, subscription])
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">计算新props的逻辑。</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// [https://github.com/reduxjs/react-redux/blob/master/src/connect/selectorFactory.js#L18](https://github.com/reduxjs/react-redux/blob/master/src/connect/selectorFactory.js#L18)</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleSubsequentCalls</span>(<span class="hljs-params">nextState, nextOwnProps</span>) </span>&#123;
    <span class="hljs-keyword">const</span> propsChanged = !areOwnPropsEqual(nextOwnProps, ownProps)
    <span class="hljs-keyword">const</span> stateChanged = !areStatesEqual(nextState, state)
    state = nextState
    ownProps = nextOwnProps

    <span class="hljs-keyword">if</span> (propsChanged && stateChanged) <span class="hljs-keyword">return</span> handleNewPropsAndNewState()
    <span class="hljs-keyword">if</span> (propsChanged) <span class="hljs-keyword">return</span> handleNewProps()
    <span class="hljs-keyword">if</span> (stateChanged) <span class="hljs-keyword">return</span> handleNewState()
    <span class="hljs-keyword">return</span> mergedProps
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分为三种情况：</p>
<ol>
<li>
<p>props 和 state都改变了</p>
</li>
<li>
<p>仅props改变</p>
</li>
<li>
<p>仅state改变</p>
</li>
</ol>
<h2 data-id="heading-22">hook源码分析</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Component</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> selectedValue = useSelecter(selector);
    <span class="hljs-keyword">const</span> store = useStore();
    <span class="hljs-keyword">const</span> dispatch = useDisaptch();
  
    <span class="hljs-keyword">return</span> <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没啥好分析的。。。Hook 实现十分简单，这也导致了很多库选择只使用hooks API。。。
useSelecter实现：</p>
<ol>
<li>
<p>通过subcribe订阅store更新，回调里通过seleter算出state，如果对比相等，阻止没必要更新，如果不相等forceUdpate。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freact-redux%2Fblob%2Fmaster%2Fsrc%2Fhooks%2FuseSelector.js%23L70" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/react-redux/blob/master/src/hooks/useSelector.js#L70" ref="nofollow noopener noreferrer">源码</a></p>
</li>
<li>
<p>如果其他原因更新：每次还是会算selctor，如果算出来是一样的话，其实还是返回上次的值，这算是一个小优化吧。。。。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freact-redux%2Fblob%2Fmaster%2Fsrc%2Fhooks%2FuseSelector.js%23L70" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/react-redux/blob/master/src/hooks/useSelector.js#L70" ref="nofollow noopener noreferrer">源码</a> 。</p>
</li>
</ol>
<p>useStore就是返回Store
useDispatch 就是返回Store.dispatch</p>
<h1 data-id="heading-23">Redux相关库</h1>
<p>由于社区上有太多的Redux相关或者使用redux思想的库，介绍不过来，但他们解决的问题大体相同，我认为主要有两点：</p>
<ul>
<li>
<p>为了提高开发者体验（减少模版代码，聚合逻辑，TS类型）</p>
</li>
<li>
<p>集合一些redux最佳实践（immer，redux-thunk）</p>
</li>
</ul>
<p>至于选择我觉得取决于团队或者个人的偏好。</p>
<h3 data-id="heading-24"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux-toolkit.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://redux-toolkit.js.org/" ref="nofollow noopener noreferrer">Redux Toolkit</a></h3>
<p>周下载量：592k
大小：11.02kb
Demo: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fagitated-mclaren-4f723%3Ffile%3D%2Fsrc%2Ffeatures%2Fcounter%2FcounterSlice.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/agitated-mclaren-4f723?file=/src/features/counter/counterSlice.js" ref="nofollow noopener noreferrer">codesandbox.io/s/agitated-…</a>
特点：</p>
<ul>
<li>
<p>redux官方出品，redux丰富的生态可供选择。（中性）他们的概念依旧很多。</p>
</li>
<li>
<p><code>createReuducer</code> <code>createAction</code> 帮助生成模版代码，React使用部分还是依赖 <code>react-redux</code> 的使用</p>
</li>
<li>
<p>支持自定义中间件。</p>
</li>
<li>
<p>内置immer、redux-thunk。</p>
</li>
<li>
<p>不支持生成衍生状态。</p>
</li>
<li>
<p>如果一开始就是使用redux全家桶，方便迁移。</p>
</li>
<li>
<p>支持HOC API、支持Hook API（react-redux支持）。</p>
</li>
</ul>
<h3 data-id="heading-25"></h3>
<h3 data-id="heading-26"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdoc.bytedance.net%2Fdocs%2F3516%2F4668%2F35374%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://doc.bytedance.net/docs/3516/4668/35374/" ref="nofollow noopener noreferrer">Reduck</a></h3>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frematch%2Frematch" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rematch/rematch" ref="nofollow noopener noreferrer">rematch</a>
周下载量：26K</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdfaff37932c4597999c2fb0d50fc6fb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
底层还是依赖redux、react-redux，用了一些api，魔改了一些api。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/595b0a4321a84f98aba547d7b8ed89b4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Demo：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.byted.org%2Ftoutiao-fe-arch%2Fjupiter_boilerplates%2Fblob%2Fmaster%2Freduck-ts%2Fsrc%2Fmodels%2Ftodo.ts%23L34" target="_blank" rel="nofollow noopener noreferrer" title="https://code.byted.org/toutiao-fe-arch/jupiter_boilerplates/blob/master/reduck-ts/src/models/todo.ts#L34" ref="nofollow noopener noreferrer">code.byted.org/toutiao-fe-…</a></p>
<p>特点:</p>
<ul>
<li>
<p>应该是借鉴了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frematch%2Frematch" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rematch/rematch" ref="nofollow noopener noreferrer">rematch</a> （ <a href="https://link.juejin.cn/?target=https%3A%2F%2Frematchjs.org%2Fexamples%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rematchjs.org/examples/" ref="nofollow noopener noreferrer">Examples | Rematch</a> ），但相比rematch多了 <strong>computed。。。</strong></p>
</li>
<li>
<p>我司jupiter团队出品，作为插件集成在Jupiter中。</p>
</li>
<li>
<p>不依赖React-redux。（自己实现）</p>
</li>
<li>
<p>支持HOC API、支持Hook API。都需要显示传入modal。</p>
</li>
<li>
<p>像rematch一样支持plugin，如immer</p>
</li>
<li>
<p>支持组件级别的储存（不存全局）。有点类似React-recoil。。。</p>
</li>
</ul>
<blockquote>
<p><strong>computed 的返回值（completedCount）会根据它的依赖参数被缓存起来，且只有当它的依赖值(参数)发生了改变才会被重新计算。</strong>
<strong>上述，computed 计算依赖于当前 Model 的 state，如果不只依赖于 Model 的 state，且依赖其余外部参数，来进行动态计算。或者对派生数据做更细致的缓存优化</strong> ，请看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdoc.bytedance.net%2Fdocs%2F3516%2F4739%2F37004%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://doc.bytedance.net/docs/3516/4739/37004/" ref="nofollow noopener noreferrer">高级用例-computed 部分</a> 。</p>
</blockquote>
<ul>
<li>事实上easy-peasy也是这样做的。。。</li>
</ul>
<h3 data-id="heading-27"></h3>
<h3 data-id="heading-28"><a href="https://link.juejin.cn/?target=https%3A%2F%2Feasy-peasy.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://easy-peasy.dev/" ref="nofollow noopener noreferrer">easy-peasy</a></h3>
<p>周下载量：32k
大小：10.21kb
Demo: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Feasy-peasytypescript-tutorialtyped-thunks-forked-x91g4%3Ffile%3D%2Fsrc%2Fmodel%2Ftodos.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/easy-peasytypescript-tutorialtyped-thunks-forked-x91g4?file=/src/model/todos.ts" ref="nofollow noopener noreferrer">codesandbox.io/s/easy-peas…</a></p>
<p>特点：</p>
<ul>
<li>
<p>比较轻量</p>
</li>
<li>
<p>不依赖React-redux。自己实现了其hook部分，和React-redux的差不多。</p>
</li>
<li>
<p>10min内上手，上手极其简单，学习体验极其舒适。</p>
</li>
<li>
<p>只支持 Hook API</p>
</li>
<li>
<p>内置immer、redux-thunk</p>
</li>
<li>
<p>支持组件级别的储存（不存全局）。</p>
</li>
</ul>
<h3 data-id="heading-29"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenbase.com%2Fjs%2Fzustand" target="_blank" rel="nofollow noopener noreferrer" title="https://openbase.com/js/zustand" ref="nofollow noopener noreferrer">zustand</a></h3>
<p>demo： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fdetermined-curran-5b0d3%3Ffile%3D%2Fsrc%2FApp.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/determined-curran-5b0d3?file=/src/App.js" ref="nofollow noopener noreferrer">codesandbox.io/s/determine…</a>
周下载量：74K
特点：</p>
<ul>
<li>
<p>比较轻量</p>
</li>
<li>
<p>简化了redux 的概念，保留了state、middileware等概念。</p>
</li>
<li>
<p>把action 和 state都放在一起储存。</p>
</li>
</ul>
<p>api十分简单：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> api = &#123; setState, getState, subscribe, destroy &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>核心源码部分：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpmndrs%2Fzustand%2Fblob%2Fmaster%2Fsrc%2Fvanilla.ts%23L37" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pmndrs/zustand/blob/master/src/vanilla.ts#L37" ref="nofollow noopener noreferrer">github.com/pmndrs/zust…</a>
看完有种鹈鹕醒脑的感觉，只像react setstate一样不可变数据流自己保证，然后就是数据发布订阅，这就是redux吗？</p>
<h1 data-id="heading-30"></h1></div>  
</div>
            