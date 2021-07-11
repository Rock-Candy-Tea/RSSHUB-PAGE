
---
title: 'React学习—生命周期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d3d706bf3244c02b2e0f8a7655281bb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 01:14:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d3d706bf3244c02b2e0f8a7655281bb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>该篇为笔者学习React时整理下来的学习笔记，主要讲述React组件的生命周期以及其常用的一些生命钩子函数和这些钩子函数的执行时机。</p>
<h1 data-id="heading-1">内容</h1>
<h2 data-id="heading-2">React生命周期</h2>
<p>首先看官方提供的React组件生命周期图：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d3d706bf3244c02b2e0f8a7655281bb~tplv-k3u1fbpfcp-watermark.image" alt="react生命周期.png" loading="lazy" referrerpolicy="no-referrer">
通过上图我们可以发现，React组件的生命周期可以大致分为三个阶段：</p>
<ol>
<li>组件挂载阶段（图中的挂载时）</li>
<li>数据更新阶段（图中的更新时）</li>
<li>组件卸载阶段（图中的卸载时）</li>
</ol>
<p>接下来按照这三个阶段进行梳理React的生命钩子函数<br>
注意：这里是以类组件作为展示，不涉及函数式组件实现钩子的方式，同时constructor和render是最基础的生命函数，以下就默认摘出了不会介绍。</p>
<h2 data-id="heading-3">组件挂载阶段</h2>
<p>组件挂载阶段顾名思义，是React组件在挂载过程中的阶段，这个阶段的大概流程为以下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4c0b336f22a46b98f9121a5f629e4eb~tplv-k3u1fbpfcp-watermark.image" alt="fc22740943b7a793c586d6f01aeafc4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>constructor：调用constructor构造函数</p>
</li>
<li>
<p>componentWillMount(生命钩子函数/已经弃用)<br>
注意：调用componentWillMount()时组件已经经历了constructor()初始化数据后，但是还未渲染DOM,这个钩子已经被弃用了,未来将会在17版本中直接废弃，这里了解下即可</p>
</li>
<li>
<p>getDerivedStateFromProps(生命钩子函数/不常使用)<br>
注意：React v16.4新增钩子，当组件的state需要依赖props传入的数据时可以使用</p>
</li>
<li>
<p>render: 调用render()函数</p>
</li>
<li>
<p>React内部更新DOM和refs</p>
</li>
<li>
<p>componentDidMount(生命钩子函数/经常使用)<br>
注意：此时组件已经被挂载到DOM上，这个函数组件在整个生命周期内只会调用一次</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-comment">//图中第一步调用constructor</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props)
  &#125;
  <span class="hljs-comment">//图中第二步调用getDerivedStateFromProps</span>
  <span class="hljs-keyword">static</span> getDerivedStateFromProps (nextProps, preState) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-comment">//图中第三步调用render</span>
  render () &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
  <span class="hljs-comment">//图中第五步调用componentDidMount</span>
  componentDidMount () &#123;

  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里主要就涉及到了两个生命钩子函数getDerivedStateFromProps和componentDidMount,接下来做一个基本介绍：</p>
<h3 data-id="heading-4">getDerivedStateFromProps：</h3>
<p>简介：React新增生命钩子函数，一般不常用，主要的作用是当组件的state的数据需要依赖外界传入的props的时候可以调用这个函数，通俗的讲就是将props数据映射到state上，函数的执行时机是在组件初始化数据后和调用render()前,且每次组件重新渲染前都会调用，因此值得注意的是即使props没有发生变化，但是父组件的state反生了变化，导致子组件发生了重新渲染，这个生命钩子也会被再次调用，基本使用和注意点如下：</p>
<ol>
<li>该函数为静态函数，因此无法通过this去获取组件实例数据，该函数内部的this指向undefined</li>
<li>该函数默认有两个参数，分别是当前传入的props，前一个的state，在这个函数执行后，可能会改变之前的state，生成新的state</li>
<li>该函数必须返回一个对象，当返回空对象null时，则不会state产生任何更改</li>
<li>如果返回的对象中有和state里重名的属性，那么返回对象上的属性将会覆盖原来state中的那个重名属性</li>
</ol>
<p>由于这个函数比较特殊，先贴上官方文档上的一段描述</p>
<pre><code class="hljs language-js copyable" lang="js">此方法适用于罕见的用例，即 state 的值在任何时候都取决于 props。例如，实现 <Transition> 组件可能很方便，该组件会比较当前组件与下一组件，以决定针对哪些组件进行转场动画。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模拟场景：初学react这个生命钩子笔者也没有真实的使用场景，笔者本能的认为，props和state之间应该是尽可能的不要存在依赖关系，否则这个组件的状态驱动就会产生两个源头，就有可能产生紊乱，当然业务需求可能使得完全解耦不太可能，因此笔者在网上找了一个使用场景，进行展示</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//组件受外部的状态来渲染列表</span>
<span class="hljs-keyword">static</span> propTypes = &#123;
    <span class="hljs-attr">type</span>: PropTypes.number
&#125;
<span class="hljs-comment">// 组件还具有自己的状态来渲染列表</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">List</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(props);
        <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">list</span>: [],
            <span class="hljs-attr">type</span>: <span class="hljs-number">0</span>,
        &#125;
    &#125;
&#125;
<span class="hljs-comment">//当同时需要两个源头驱动时，就可以使用该生命钩子</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getDerivedStateFromProps</span>(<span class="hljs-params">nextProps, prevState</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;type&#125; = nextProps;
    <span class="hljs-keyword">if</span> (type !== prevState.type) &#123;
        <span class="hljs-keyword">return</span> &#123;
            type,
        &#125;;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">componentDidMount</h3>
<p>简介：组件被挂载后调用的生命钩子，经常使用，这个钩子是组件在挂载生命周期内最后执行的一个钩子函数，该函数进行回调时，表明此时组件已经被挂载完毕dom节点已经生成，可以在这里进行ajax请求，利用setState()进行赋值，然后重新渲染组件，基本使用和注意点如下：</p>
<ol>
<li>有时候我们在赋值的时候会出现警告,当然也不限于此钩子内，警告内容如下:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">Can only update a mounted or mounting component. This usually      means you called setState() on an unmounted component. This is a   no-op. Please check the code <span class="hljs-keyword">for</span> the <span class="hljs-literal">undefined</span> component.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>警告的意思大概为，你只能更新已经挂载了或者挂载中的组件，这意味着你可能对未有被挂载的组件进行了setState操作,出现这种情况的可能性是，我们发送ajax请求，请求成功后进行赋值操作，但是请求操作是异步的，请求没回来前，组件已经被销毁了，解决方案如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props)
    <span class="hljs-built_in">this</span>.hasMount = <span class="hljs-literal">false</span>;
&#125;
componentDidMount () &#123;
    <span class="hljs-built_in">this</span>.hasMount = <span class="hljs-literal">true</span>
    axios.get(<span class="hljs-string">"xxxxx"</span>).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
        <span class="hljs-built_in">this</span>.hasMount&&<span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-comment">//进行赋值操作</span>
        &#125;)
    &#125;)
&#125;
<span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-built_in">this</span>.hasMount = <span class="hljs-literal">false</span> 
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者在组件componentWillUnmount取消没有完成的请求</p>
<h2 data-id="heading-6">数据更新阶段</h2>
<p>数据更新阶段，在这个阶段内React会进行数据更新操作，继而触发一系列的钩子函数，先重新展示这个生命周期图片，这个阶段的执行流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d97ca28646f4d8a95ba6b4c8f7a9f6f~tplv-k3u1fbpfcp-watermark.image" alt="7ecb9822d6b9b1169c2e9c26530d829.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>组件触发NewProps、setState()、forceUpdate()时，组件会进入数据更新阶段</p>
</li>
<li>
<p>首先进行回调getDerivedStateFromProps(生命钩子函数/不常使用)<br>
这个钩子我们之前介绍过了，这里就不多做介绍了</p>
</li>
<li>
<p>然后执行shouldComponentUpdata()(生命钩子函数/不常使用)<br>
注意：这个钩子主要的作用是，判断组件是否需要重新进行渲染，如果你调用这个函数，返回了一个fasle,那么后边将不会继续调用render,开发中我们一般不会主动去调用，但是实际上有时候是默认调用的，后边会详细介绍</p>
</li>
<li>
<p>调用render()重新渲染</p>
</li>
<li>
<p>调用getSnapshotBeforeUpdate()(生命钩子函数/不常使用)<br>
注意：这个钩子函数用于，你在数据更新前是否需要保存一个当前状态的快照，如果需要你可以在这个函数的最后返回一个对象用于保存当前需要保存的快照，供后续的componentDidUpdate()使用</p>
</li>
<li>
<p>React内部更新DOM和refs</p>
</li>
<li>
<p>componentDidUpdate()(生命钩子函数/经常使用)<br>
注意：这个钩子是数据更新完毕后触发的回调函数，当这个钩子被回调时，说明react组件数据已经发生了更新，如果想要更新前的某种状态，可以通过上一个生命钩子，返回的快照进行读取</p>
</li>
</ol>
<p>在数据更新阶段共有4个生命钩子函数需要注意，getDerivedStateFromProps、shouldComponentUpdata、getSnapshotBeforeUpdate、componentDidUpdate，除去getDerivedStateFromProps我们之前已经介绍了，剩下的简单介绍一下</p>
<h3 data-id="heading-7">shouldComponentUpdata</h3>
<p>简介：该函数默认传递两个参数，一个nextProps、一个nextState，该函数需要返回一个Boolean值，当返回return的时候，会继续向下调用render，当返回fasle的时候则不会继续调用render，如果不调用这个钩子，react默认会在内部执行时返回true,继续取调用render，该函数主要用于react的性能优化，避免每次数据更新都必须重新渲染组件。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//比如我们想如果组件内的type没有发生改变，该组件不需要重新渲染，那么我们就可以这样使用</span>
    <span class="hljs-function"><span class="hljs-title">shouldComponentUpdata</span>(<span class="hljs-params">nextProps,nextState</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.state.type === nextState.type;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是简单的使用示范，该函数有几下几点需要注意：</p>
<ol>
<li>
<p>该函数主要是为了优化react性能，比如父组件中的数据反生了更新，导致子组件发生的re-render，但是实际上父组件更新的这部分数据完全没有影响到子组件，那么此时子组件没有必要反生更新，通过这个钩子我们就可以避免子组件的无意义更新</p>
</li>
<li>
<p>不要在这个函数内去使用深层比较，react官方指出，不建议在这个函数内进行深层比较或者使用JSON.stringify()函数，会非常的影响效率损害性能</p>
</li>
<li>
<p>为了保持性能优化，是不是每一个组件都需要去调用这个函数？<br>
其实并不是，一般而言当父组件发生更新，但是子组件的state和props的值并没有发生变化，这种情况下子组件基本是不需要重新渲染的，但是如果我们要在每一个组件内去实现这个钩子，就显得太过繁杂了，如果是类组件，我们其实可以使用继承的方法，定义一个带有该方法的类组件，然后依次去继承这个类，从而避免多次书写，其实react已经有实现了这样功能的类PureComponent</p>
</li>
</ol>
<h4 data-id="heading-8">PureComponent</h4>
<p>直接说结论，有兴趣的同学可以去熟悉源码，这个组件对于shouldComponentUpdata这里有着默认的处理，在继承该类的组件，如果没有指定shouldComponentUpdata这个钩子，在调用这个钩子时react内部会进行判断，如果这个值为undefined，那么他会在内部有一个默认的函数给shouldComponentUpdata赋值去调用，这个函数会用原来的state和props和新的state和props进行浅层比较（遍历后进行对应的键值对比较），如果比较一致返回true,否则返回false,如果有任意一方不是对象或者为null,直接返回false，因此一般而言我们在使用类组件时，无特殊要求可以直接去继承PureComponent这个类</p>
<p>问题： 有些同学可能会感觉到疑惑，类组件可以继承PureComponent去实现，如果是使用函数式组件如何去处理这个地方？<br>
实际上函数式组件也有对应的处理方式，使用memo高阶组件,接下来给出基本的使用</p>
<h3 data-id="heading-9">memo</h3>
<p>其实本质上这个函数返回的组件也是对函数式组件的传入的props进行浅层比较，然后决定这个组件需不需要重新渲染</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React,&#123;memo&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-comment">//传入一个函数式组件返回一个新的函数式组件，新的组件就可以默认处理shouldComponentUpdata钩子</span>
<span class="hljs-keyword">const</span> MemoCpm = memo(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>)</span>&#123;
    reutn (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是使用memo创建的新组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">getSnapshotBeforeUpdate</h3>
<p>简介：在最近一次渲染输出（提交到 DOM 节点）之前调用。它使得组件能在发生更改之前从 DOM 中捕获一些信息（例如，滚动位置）。此生命周期方法的任何返回值将作为参数传递给 componentDidUpdate()，以下来自官方文档案例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ScrollingList</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.listRef = React.createRef();
  &#125;

  <span class="hljs-function"><span class="hljs-title">getSnapshotBeforeUpdate</span>(<span class="hljs-params">prevProps, prevState</span>)</span> &#123;
    <span class="hljs-comment">// 我们是否在 list 中添加新的 items ？</span>
    <span class="hljs-comment">// 捕获滚动​​位置以便我们稍后调整滚动位置。</span>
    <span class="hljs-keyword">if</span> (prevProps.list.length < <span class="hljs-built_in">this</span>.props.list.length) &#123;
      <span class="hljs-keyword">const</span> list = <span class="hljs-built_in">this</span>.listRef.current;
      <span class="hljs-keyword">return</span> list.scrollHeight - list.scrollTop;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params">prevProps, prevState, snapshot</span>)</span> &#123;
    <span class="hljs-comment">// 如果我们 snapshot 有值，说明我们刚刚添加了新的 items，</span>
    <span class="hljs-comment">// 调整滚动位置使得这些新 items 不会将旧的 items 推出视图。</span>
    <span class="hljs-comment">//（这里的 snapshot 是 getSnapshotBeforeUpdate 的返回值）</span>
    <span class="hljs-keyword">if</span> (snapshot !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">const</span> list = <span class="hljs-built_in">this</span>.listRef.current;
      list.scrollTop = list.scrollHeight - snapshot;
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.listRef&#125;</span>></span>&#123;/* ...contents... */&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数用的不多，官网文档也就提供了这样一个案例，记录组件更新前的滚动位置，在组件发生更新后，可以调整组件的滚动位置，因此这个函数大多数会在UI操作相关功能上使用</p>
<h3 data-id="heading-11">componentDidUpdate</h3>
<p>简介：该函数会在数据更新后立即被调用，接受三个参数prevProps, prevState, snapshot, 你可以在此进行数据更新后的DOM操作、发送网络请求、或者调用setState()，但是有一点必须要注意，如果你调用了setState(),那么一定要给出条件，否则就会再次触发数据更新，继而无限循环。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params">prevProps, prevState, snapshot</span>)</span>&#123;
          <span class="hljs-comment">// 典型用法（不要忘记比较 props）：</span>
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.userID !== prevProps.userID) &#123;
               <span class="hljs-built_in">this</span>.fetchData(<span class="hljs-built_in">this</span>.props.userID);
          &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，如果在此之前没有调用getSnapshotBeforeUpdate，那么这个函数的snapshot参数为undefined</p>
<h2 data-id="heading-12">组件卸载阶段</h2>
<p>这个阶段相对直接，我们只要了解componentWillUnmount这个钩子函数就可以了</p>
<h3 data-id="heading-13">componentWillUnmount</h3>
<p>会在组件卸载及销毁之前直接调用。在此方法中执行必要的清理操作，例如，清除 timer，取消网络请求或清除在 componentDidMount() 中创建的订阅等,还有需要注意在此你不应该再去调用setState()了，因为组件之后会卸载不会重新渲染了</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//清除定时任务</span>
        <span class="hljs-comment">//取消未完成的网络请求</span>
        <span class="hljs-comment">//请求在componentDidMount()订阅</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">结语</h1>
<p>以上就是笔者整理的React生命周期的相关知识，内容相对基础，当然还有一些不常见的生命钩子函数就没有整理，更细节内容大家可以查阅React官方文档，初步学习，能力有限，仅供参考，若有错误恳请指正。</p></div>  
</div>
            