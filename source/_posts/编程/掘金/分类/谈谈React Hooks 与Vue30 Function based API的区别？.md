
---
title: '谈谈React Hooks 与Vue3.0 Function based API的区别？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d845ca16b2ac45abbda3d6f0655469ea~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 18:15:07 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d845ca16b2ac45abbda3d6f0655469ea~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>hi~ 豆皮粉儿. 又见面啦~</p>
<p><img alt="2dced3bf-e7dc-49aa-839a-743ade91348a.gif" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d845ca16b2ac45abbda3d6f0655469ea~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>React Hooks release 已经有很长一段时间了，Vue3.0 也带来了 Function based API，都我们提供了新的模式来复用和抽象逻辑，那这两者有什么区别的，saucxs 给大家带了解读</p>
<blockquote>
<p>作者: 松宝写代码</p>
</blockquote>
<h2 data-id="heading-0">一、前言</h2>
<p><strong>React Hooks</strong> 是 React16.8 引入的新特性，支持在类组件之外使用 state、生命周期等特性。</p>
<p><strong>Vue Function-based API</strong> 是 Vue3.0 最重要的 RFC (Requests for Comments)，将 2.x 中与组件逻辑相关的选项以 API函数 的形式重新设计。</p>
<p>目录：</p>
<ul>
<li>React Hooks
<ul>
<li>React Hooks是什么</li>
<li>useState Hook</li>
<li>useEffect Hook</li>
<li>React Hooks 引入的原因以及设计原则</li>
<li>React Hooks 使用原则及其背后的原理</li>
</ul>
</li>
<li>Vue3.0 Function-based API
<ul>
<li>基本用法</li>
<li>引入的原因以及解决的问题</li>
</ul>
</li>
<li>React Hooks 与 Vue3.0 Function-based API 的对比</li>
</ul>
<h2 data-id="heading-1">二、React Hooks</h2>
<h3 data-id="heading-2">React Hooks 是什么？</h3>
<p>引用官网的一段话：</p>
<blockquote>
<p>从概念上讲，React 组件更像是函数。而 Hooks 则拥抱了函数，同时也没有牺牲 React 的精神原则。Hooks 提供了问题的解决方案，无需学习复杂的函数式或响应式编程技术。</p>
</blockquote>
<p>另外，Hooks 是100%向后兼容的，也是完全可选的。</p>
<p>React Hooks 提供了三个基础 Hook : <code>useState</code>、<code>useEffect</code>、<code>useContext</code>，其他 Hooks 可参考<a href="https://zh-hans.reactjs.org/docs/hooks-reference.html" target="_blank" rel="nofollow noopener noreferrer">React Hooks API</a>。</p>
<h3 data-id="heading-3">useState Hook</h3>
<p>下面是一个实现计数器功能的类组件示例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Example</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">props</span>) &#123;
    <span class="hljs-built_in">super</span>(props)
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;

  render () &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You clicked &#123;this.state.count&#125; times<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.setState(&#123;count: this.state.count + 1)&#125;&#125;>Click me<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
       <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需求很简单，设定初始值为0，当点击按钮时，<code>count</code> 加 1。</p>
<p>当使用 useState Hook 实现上述需求时：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You clicked &#123;count&#125; times<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count + 1)&#125;>
        Click me
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>useState Hook</code> 做了哪些事情呢？</p>
<ol>
<li>在调用 useState 方法时，定义了一个state变量count，它与类组件中的this.state功能完全相同。对于普通变量，在函数退出后即消失，而state中的变量会被 React 保留。</li>
<li>useState 方法只接收一个参数，那就是初始值。useState 方法一次只定义一个变量，如果想在state中存储两个变量，只需要调用两次 useState() 即可。</li>
<li>useState 的返回值是一个由 <code>当前state</code> 以及 <code>更新state的函数</code> 组成的数组。这也是采用 <strong>数组解构</strong> 方式来获取的原因。</li>
</ol>
<p>在使用 Hooks 实现的示例中，会发现 useState 让代码更加简洁了：</p>
<ul>
<li>获取state：类组件中使用 <code>this.state.count</code> ，而使用了 useSatet Hook 的函数组件中直接使用 <code>count</code> 即可。</li>
<li>更新state：类组件中使用 <code>this.setState()</code> 更新，函数组件中使用 <code>setCount()</code> 即可。</li>
</ul>
<p>这里抛出几个疑问，在讲解原理的地方会进行详细解释：</p>
<ul>
<li><strong>React 是如何记住 useState 上次值的？</strong>。</li>
<li><strong>React 是如何知道 useState 对应的是哪一个组件？</strong>。</li>
<li><strong>如果一个组件内有多个 useState，那重新渲染时 useState 的取值顺序又是怎么确定的？</strong>。</li>
</ul>
<h3 data-id="heading-4">useEffect Hook</h3>
<p>在讲 <code>useEffect</code> 之前，先讲一下 React 的副作用。</p>
<p>在 React 中，数据获取、订阅或者手动修改DOM等操作，均被称为 '副作用'，或者 '作用' 。</p>
<p>而 useEffect 就是一个 Effect Hook ，为函数组件添加操作副作用的能力，可以把它看作是类组件中的<code>componentDidMount</code>、<code>componentDidUpdate</code>、<code>componentWillUnmount</code>三个周期函数的组合。</p>
<p>下面是一个关于订阅的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Example</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">props</span>) &#123;
    <span class="hljs-built_in">super</span>(props)
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">isOnline</span>: <span class="hljs-literal">null</span>
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    ChatAPI.subscribeToFriendStatus(
      <span class="hljs-built_in">this</span>.props.friend.id,
      <span class="hljs-built_in">this</span>.handleStatusChange
    );
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params">prevProps</span>)</span> &#123;
    <span class="hljs-comment">// 当 friend.id 变化时进行更新</span>
    <span class="hljs-keyword">if</span> (prevProps.friend.id !== <span class="hljs-built_in">this</span>.props.friend.id) &#123;
      <span class="hljs-comment">// 取消订阅之前的 friend.id</span>
      ChatAPI.unsubscribeFromFriendStatus(
        prevProps.friend.id,
        <span class="hljs-built_in">this</span>.handleStatusChange
      );
      <span class="hljs-comment">// 订阅新的 friend.id</span>
      ChatAPI.subscribeToFriendStatus(
        <span class="hljs-built_in">this</span>.props.friend.id,
        <span class="hljs-built_in">this</span>.handleStatusChange
      );
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
    ChatAPI.unsubscribeFromFriendStatus(
      <span class="hljs-built_in">this</span>.props.friend.id,
      <span class="hljs-built_in">this</span>.handleStatusChange
    );
  &#125;

  handleStatusChange = <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">isOnline</span>: status.isOnline
    &#125;);
  &#125;

  render () &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        &#123;this.state.isOnline === null ? 'Loading...' :
          (this.state.isOnline ? 'Online' : 'Offline')
        &#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述的代码中不难发现，存在一定的重复代码，逻辑不得不拆分在三个生命周期内部。另外由于类组件不会默认绑定 this ，在定义 <code>handleStatusChange</code> 时，还需要为它 <code>绑定this</code>。</p>
<p>这里补充一点，对于类组件，需要<strong>谨慎</strong>对待 JSX 回调函数中的 <code>this</code>，类组件默认是不会绑定 this 的，下面提供几种绑定 this 的方法：</p>
<ol>
<li>通常的做法是将事件处理函数声明为 class 中的方法，如：constructor内部 <code>this.handleClick = this.handleClick.bind(this)</code></li>
<li>在 onClick 内部使用箭头函数， 如：<code>onClick=&#123;e=>this.handleClick(id, e)&#125;</code>，注意：该方法在每次渲染时都会创建不同的回调函数。在大多数情况下，没什么问题，但如果该回调函数作为 prop 传入子组件时，这些组件可能会进行额外的重新渲染。</li>
<li>在 onClick 内部使用 bind 绑定， 如：<code>onClick=&#123;this.handleClick.bind(this, e)&#125;</code></li>
<li>使用 class fields 绑定：如：<code>handleClick = (e) => &#123;&#125;</code></li>
</ol>
<p>这也是 React 引入 Hooks 的其中一个原因。</p>
<p>下面让我们看一下 useEffect Hook 是如何实现上述需求的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [isOnline, setIsOnline] = useState(<span class="hljs-literal">null</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> handleStatusChange = <span class="hljs-function">(<span class="hljs-params">status</span>) =></span> &#123;
      setIsOnline(status.isOnline)
    &#125;
    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
    &#125;;
  &#125;, [props.friend.id]);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      &#123;isOnline === null ? 'Loading...' :
        (isOnline ? 'Online' : 'Offline')
      &#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述例子中，你可能会对 useEffect Hook 产生以下疑问：</p>
<ol>
<li>useEffect 做了什么？首先，接收了一个函数，而 React 会保存这个函数(称为'effect')，并且在执行 DOM 更新后调用这个函数，即添加订阅。</li>
<li><code>[props.friend.id]</code> 参数设置了什么？
<ul>
<li>默认情况下，useEffect 接收一个函数作为第一个参数，在不设置第二个参数时，每一次渲染都会执行 effect，这有可能会导致性能问题。</li>
<li>为了解决这个问题，可添加第二个参数，用来控制什么时候将会执行更新，这时候就相当于 <code>componentDidUpdate</code> 做的事情。</li>
<li>如果想只运行一次 effect ，即仅在组件挂载和卸载时执行，第二个参数可传递一个空数组<code>[]</code>。</li>
</ul>
</li>
<li>在 useEffect 中为什么要返回一个函数呢？这是一个可选的操作，每一个 effect 都可以返回一个清除函数。在 React 中，有一些副作用是需要清除的，比如 监听函数、定时器等，这时候就需要为 effect 增加一个返回函数，React 会在组件卸载的时候执行清除操作。</li>
</ol>
<p>Hooks 所提供的功能远不止这些，更多详细的介绍可以查阅<a href="https://reactjs.org/" target="_blank" rel="nofollow noopener noreferrer">官网文档</a>。</p>
<h3 data-id="heading-5">React Hooks 引入的原因以及设计原则</h3>
<p>React Hooks 具体解决了什么问题呢？ React 为什么要引入这一特性呢？</p>
<p>主要有以下三点原因：</p>
<ol>
<li>在组件之间复用状态逻辑很困难。
<ul>
<li>React 并没有提供将可复用行为附加到组件的途径，一般比较常见的方法是采用 <code>render props</code> 和 <code>高阶组件</code> 解决。</li>
<li>React Hooks 支持 <code>自定义Hook</code>，可以将状态逻辑从组件中提出，使得这些逻辑可进行单独测试、复用，在<strong>无需修改组件结构</strong>的情况下即可实现状态逻辑复用。点击查看<a href="https://zh-hans.reactjs.org/docs/hooks-custom.html" target="_blank" rel="nofollow noopener noreferrer">自定义Hook使用说明</a>。</li>
</ul>
</li>
<li>复杂组件变得难以理解。
<ul>
<li>每个生命周期函数内部逻辑复杂、功能不单一，相互关联的需求被拆分在各个生命周期中，而不相关的代码却需要在同一个周期内部进行整合。</li>
<li>为了解决这个问题，React Hooks 将组件中相互关联的部分拆分成更小的函数，引入了 <code>Effect Hook</code>，如上述 useEffect 的示例，正是解决了这个问题。</li>
</ul>
</li>
<li>难以理解的class。
<ul>
<li>this绑定</li>
<li>打包尺寸，函数通过ES export导出，可以借助 tree-shaking 把没用到的函数移除；压缩混淆，类的属性和方法没法压缩</li>
<li>class热重载不稳定</li>
</ul>
</li>
</ol>
<h3 data-id="heading-6">React Hooks 设计原则</h3>
<p>主要有以下四点：</p>
<ol>
<li>优雅高效的复用状态逻辑</li>
<li>无 class 困扰</li>
<li>具备 class 已有的能力</li>
<li>功能单一的副作用</li>
</ol>
<p>下面我们根据几个例子来感受 React Hooks 具体是如何体现的。</p>
<h4 data-id="heading-7">1、优雅高效的复用状态逻辑</h4>
<p>在之前，状态逻辑的复用一般是采用 <code>Mixins API</code>、<code>Render Props</code>或<code>HOC</code>实现，但是由于Render Props 与 HOC 本身也是组件，状态逻辑的复用也是通过封装组件的形式来实现，仍难以避免组件多层嵌套的问题，也比利于后续的理解与维护。</p>
<p>在 React Hooks 中，提供了 <code>自定义Hook</code> 来实现状态逻辑的复用。</p>
<p>比如 在聊天程序中，使用订阅获取好友的状态：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useOnline</span>(<span class="hljs-params">id</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [isOnline, setIsOnline] = useState(<span class="hljs-literal">null</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleStatusChange</span> (<span class="hljs-params">state</span>) </span>&#123;
      setIsOnline(status.isOnline)
    &#125;
    ChatAPI.subscribeToFriendStatus(id, handleStatusChange);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      ChatAPI.unsubscribeFromFriendStatus(id, handleStatusChange);
    &#125;;
  &#125;, [id]);

  <span class="hljs-keyword">return</span> isOnline;
&#125;

<span class="hljs-comment">// 使用 自定义Hook</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> isOnline = useOnline(props.friend.id);
  
  <span class="hljs-keyword">if</span> (isOnline === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'Loading...'</span>;
  &#125;
  <span class="hljs-keyword">return</span> isOnline ? <span class="hljs-string">'Online'</span> : <span class="hljs-string">'Offline'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到 useOnline 组件的逻辑是与业务完全无关的，它只是用来添加订阅、取消订阅，以获取用户的状态。</p>
<p>总结：</p>
<ul>
<li>数据来源清楚，之间根据函数返回值获得</li>
<li>代码量少，更易维护</li>
<li>避免重复创建组件带来性能损耗</li>
</ul>
<p><strong>注意</strong></p>
<ul>
<li>自定义Hook 是一个函数，名称必须以 <code>'use'</code> 开头，这是一个约定，如果不遵循，React 将无法自动检测是否违反了 Hook 规则。</li>
<li>在函数的内部可以调用其他 Hook，但是请确保只在顶层无条件地调用其他Hook。</li>
<li>React 会根据名称来检测 Hook 是否违反了规则。</li>
<li>自定义 Hook 是一种重用状态逻辑的机制，每次使用时，内部 state 与副作用是完全隔离的。</li>
</ul>
<h4 data-id="heading-8">2、无 class 困扰</h4>
<p>下面我们将根据一个具体例子 <strong>实现根据点击事件，控制节点的展示或者隐藏的需求</strong>，来对 <code>Render Props</code>、<code>HOC</code>、<code>Hooks</code>的实现方式做简单对比。</p>
<h5 data-id="heading-9">使用 Render Props 实现</h5>
<p>Render Props 是指一种在 React 组件之间使用一个值为函数的 prop 共享代码的简单技术。</p>
<p>创建 <code>VisibilityHelper</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> PropTypes <span class="hljs-keyword">from</span> <span class="hljs-string">'prop-types'</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VisibilityHelper</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">isDisplayed</span>: props.initialState || <span class="hljs-literal">false</span>,
    &#125;;
  &#125;
  hide = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">isDisplayed</span>: <span class="hljs-literal">false</span>,
    &#125;);
  &#125;
  show = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">isDisplayed</span>: <span class="hljs-literal">true</span>,
    &#125;);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.props.children(&#123;
      ...this.state,
      <span class="hljs-attr">hide</span>: <span class="hljs-built_in">this</span>.hide,
      <span class="hljs-attr">show</span>: <span class="hljs-built_in">this</span>.show,
    &#125;);
  &#125;
&#125;
VisibilityHelper.propTypes = &#123;
  <span class="hljs-attr">initialState</span>: PropTypes.bool,
  <span class="hljs-attr">children</span>: PropTypes.func.isRequired,
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> VisibilityHelper;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对 <code>VisibilityHelper</code> 的使用:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> VisibilityHelper <span class="hljs-keyword">from</span> <span class="hljs-string">'VisibilityHelper'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ButtonComponent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">VisibilityHelper</span> <span class="hljs-attr">initialState</span>=<span class="hljs-string">&#123;true&#125;</span>></span>
      &#123;
        (&#123;
          isDisplayed,
          hide,
          show
        &#125;) => (
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
              &#123;
                isDisplayed ?
                  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;hide&#125;</span>></span>Click to hide<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                  :
                  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;show&#125;</span>></span>Click to display<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
              &#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          )
      &#125;
    <span class="hljs-tag"></<span class="hljs-name">VisibilityHelper</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code><ButtonComponent></code>组件中，我们使用了一个带有<code>函数prop</code>的 <code><VisibilityHelper></code>组件，实现了代码复用。</p>
<h5 data-id="heading-10">使用 HOC 实现</h5>
<p>高阶组件，是 React 中复用组件逻辑的一种高级技巧，是一种基于 React 组合特性而形成的设计模式。</p>
<p>定义高阶组件 <code>VisibilityHelper</code> ，注意 HOC 不会修改传入的组件，也不会使用继承来复制其行为。相反，HOC 通过将组件包装在容器组件中来组成新组件。HOC 是纯函数，没有副作用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">VisibilityHelper</span>(<span class="hljs-params">WrappedComponent, initialState = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
      <span class="hljs-built_in">super</span>(props);
      <span class="hljs-built_in">this</span>.state = &#123;
        <span class="hljs-attr">isDisplayed</span>: initialState
      &#125;;
    &#125;

    hide = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">isDisplayed</span>: <span class="hljs-literal">false</span>,
      &#125;);
    &#125;
    show = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">isDisplayed</span>: <span class="hljs-literal">true</span>,
      &#125;);
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span>
        <span class="hljs-attr">isDisplayed</span>=<span class="hljs-string">&#123;this.state.isDisplayed&#125;</span>
        <span class="hljs-attr">show</span>=<span class="hljs-string">&#123;()</span> =></span> this.show()&#125;
        hide=&#123;() => this.hide()&#125;
        &#123;...this.props&#125; /></span>;
    &#125;
  &#125;;
&#125;
<span class="hljs-comment">// 定义 按钮组件</span>
<span class="hljs-keyword">let</span> ButtonComponent = <span class="hljs-function">(<span class="hljs-params">&#123; isDisplayed, hide, show &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      &#123;
        isDisplayed ?
          <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;hide&#125;</span>></span>Click to hide<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
          :
          <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;show&#125;</span>></span>Click to display<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      &#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-comment">// 使用高阶组件，并设定默认值</span>
ButtonComponent = VisibilityHelper(ButtonComponent, <span class="hljs-literal">true</span>);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> ButtonComponent
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">在 React Hooks 中是如何实现上述逻辑的呢？</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ButtonComponent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [isDisplayed, show] = useState(initialState || <span class="hljs-literal">false</span>)
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      &#123;
        isDisplayed ?
          <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> show(false)&#125;>Click to hide<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
          :
          <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> show(true)&#125;>Click to display<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      &#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从对比中可以发现，使用 Hooks 更简洁，且不需要在担心 this 绑定地问题。</p>
<h4 data-id="heading-12">3、具备 class 已有的能力</h4>
<p>对于常用的 class 能力，Hooks 已经基本覆盖。</p>
<p>对于其他不常见的能力，官方给出的回应是：</p>
<blockquote>
<p>目前暂时还没有对应不常用的 getSnapshotBeforeUpdate 和 componentDidCatch 生命周期的 Hook 等价写法，但我们计划尽早把它们加进来。目前 Hook 还处于早期阶段，一些第三方的库可能还暂时无法兼容 Hook。</p>
</blockquote>
<h4 data-id="heading-13">4、功能单一的副作用</h4>
<p>通过文中的几个示例，应该可以了解到 useEffect Hook 便是设计用来解决副作用分散、逻辑不单一的问题。</p>
<p>在真实的应用场景中，可根据业务需要编写多个 useEffect。</p>
<h3 data-id="heading-14">React Hooks 使用原则</h3>
<p>两条使用原则：</p>
<ol>
<li>只在最顶层使用 Hooks，不能在循环、条件或嵌套函数中调用 Hooks。这是为了保证 Hooks 在每一次渲染中都按照同样的顺序被调用。</li>
<li>只能在 React 的函数组件中或者 自定义Hook 中调用 Hooks。确保组件的状态逻辑在代码中清晰可见。</li>
</ol>
<p>这两条原则让 React 能够在多次的 useState 和 useEffect 调用之间保持 hook 状态的正确。</p>
<h3 data-id="heading-15">React Hooks 背后的原理</h3>
<p>之前的抛出的疑问：</p>
<ul>
<li><strong>React 是如何记住 useState 上次值的？</strong>。</li>
<li><strong>React 是如何知道 useState 对应的是哪一个组件？</strong>。</li>
<li><strong>如果一个组件内有多个 useState，那重新渲染时 useState 的取值顺序又是怎么确定的？</strong>。</li>
</ul>
<p>在 React 中从编译到渲染成 Dom，都要经历这样的过程：<code>JSX -> Element -> FiberNode -> Dom</code>。</p>
<p>Hooks 要想和一个函数组件进行绑定，
就要和这个转换过程的某个节点进行关联，由于 Hooks 只有在 render 过程中进行调用，很明显就只能关联到 <code>FiberNode</code> 上。</p>
<p>在 FiberNode 上有
一个属性 <code>memoizedState</code>，这个属性在 class 组件中对应最终渲染的 state。</p>
<p>class 组件的state一般是一个对象，在 函数组件中变成
一个链表，如 class 组件 <code>memoizedState = &#123;a: 1, b: 2&#125;  =>  函数组件 memoizedState = &#123;state: 1, next: &#123;state: 2, next: ..&#125;&#125;</code></p>
<p>每个链表的节点都是一个 useState，从而将所有 Hooks 进行串联起来。不仅仅 State Hook，其它 Hook 也是通过 memoizedState 串联起来的。</p>
<p>第一次渲染后，通过 FiberNode 的 memoizedState 将所有 Hook 进行收集完成。</p>
<p>当执行 setState 进行组件更新时，重新执行函数组件，这时会从收集的 Hooks 中按照执行顺讯依次取出，对于 State Hook 会进行计算将最新的值返回， Effect Hook 会在组件渲染结束后，先执行清除函数，再执行
副作用函数。</p>
<p>过程如图：
<img alt="过程" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b5b76b3a47e497884d1416e36dc032e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">三、Vue3.0 Function-based API</h2>
<p>首先提一下 Vue Function-based API 的升级策略。</p>
<p>vue官方提供了<a href="https://github.com/vuejs/vue-function-api" target="_blank" rel="nofollow noopener noreferrer">Vue Function API</a>，支持Vue2.x版本使用组件<strong>逻辑复用机制</strong>。3.x无缝替换掉该库。</p>
<p>另外，Vue3.x发布支持两个不同版本：</p>
<ul>
<li>兼容版本：同时支持新 API 和 2.x 的所有选项</li>
<li>标准版本：只支持新 API 和部分 2.x 选项</li>
</ul>
<p>下面是一个基础例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; value, computed, watch, onMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">const</span> App = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <span>count is &#123;&#123; count &#125;&#125;</span>
      <span>plusOne is &#123;&#123; plusOne &#125;&#125;</span>
      <button @click="increment">count++</button>
    </div>
  `</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// reactive state</span>
    <span class="hljs-keyword">const</span> count = value(<span class="hljs-number">0</span>)
    <span class="hljs-comment">// computed state</span>
    <span class="hljs-keyword">const</span> plusOne = computed(<span class="hljs-function">() =></span> count.value + <span class="hljs-number">1</span>)
    <span class="hljs-comment">// method</span>
    <span class="hljs-keyword">const</span> increment = <span class="hljs-function">() =></span> &#123; count.value++ &#125;
    <span class="hljs-comment">// watch</span>
    watch(<span class="hljs-function">() =></span> count.value * <span class="hljs-number">2</span>, <span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`count * 2 is <span class="hljs-subst">$&#123;val&#125;</span>`</span>)
    &#125;)
    <span class="hljs-comment">// lifecycle</span>
    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`mounted`</span>)
    &#125;)
    <span class="hljs-comment">// expose bindings on render context</span>
    <span class="hljs-keyword">return</span> &#123;
      count,
      plusOne,
      increment
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">Vue Function-based API 引入的原因及解决的问题</h3>
<p>引入的原因，借用官方推出的一段话：</p>
<blockquote>
<p>组件 API 设计所面对的核心问题之一就是如何组织逻辑，以及如何在多个组件之间抽取和复用逻辑。</p>
</blockquote>
<p>其实也就是 React Hooks 引入时提到的：在组件之间复用状态逻辑很困难。</p>
<p>在Vue2.0中，有一些常见的逻辑复用模式，如：<code>Mixins</code>、<code>高阶组件</code>、<code>Renderless Components</code>，这些模式均或多或少的存在以下问题：</p>
<ul>
<li>模版中的数据来源不清晰</li>
<li>命名空间容易冲突</li>
<li>性能问题，需要额外的组件实例嵌套来封装逻辑，带来不必要的性能开销等</li>
</ul>
<p>Function-based API 受 React Hooks 的启发，提供一个全新的逻辑复用方案，且不存在上述问题。</p>
<h2 data-id="heading-18">四、React Hooks 与 Vue Function-based API 的对比</h2>
<p>两者均具有基于函数提取和复用逻辑的能力。</p>
<p>React Hooks 在每次组件渲染时都会调用，通过隐式地将状态挂载在当前的内部组件节点上，在下一次渲染时根据调用顺序取出。而 Vue 的响应式
机制使 setup() 只需要在初始化时调用一次，状态通过引用储存在 setup() 的闭包内。这也是vue不受调用顺序限制的原因。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            