
---
title: '【react】context VS redux'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8818'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 03:18:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=8818'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>自从新的<code>context API</code>和<code>hook</code>特性相继出来后，江湖上类似于“我们再也不需要redux”，“redux已死”的论调甚上尘嚣。如果不能在使用redux的过程中，保持一个深度思考状态，你可能也人云亦云，甚至为这些论调做出一些推波助澜的举动。这好像不能怪你，因为<code>context API</code>, <code>context API + useReducer</code>和 <code>redux + react-redux</code> 三者之间的功能差异如果不加以仔细审查的话，是难以区分的。所以，我们今天就来理一理这三者之间的区别是什么，各自使用的场景是什么。</p>
<h2 data-id="heading-1">正文</h2>
<h3 data-id="heading-2">Context API</h3>
<h4 data-id="heading-3">什么是 Context API ？</h4>
<p>首先，需要明确的是，本文中提到的<code>Context API</code>都是指【<strong>新版Context API</strong>】。新版<code>Context API</code> 是在 react 16.3 版本所引入的。在这个版本之前的 <code>context API</code>我们称之为<a href="https://reactjs.org/docs/legacy-context.html" target="_blank" rel="nofollow noopener noreferrer"><code>旧版 context API</code></a>。它们都是为了解决同样的问题：“跨组件层级传递props的效率问题（prop-drilling）”。在没有提出
<code>旧版 context API</code>之前，如果我们需要跨组件层级去传递props问题，我们需要手动地层层传递。所跨层级越多，那么就越显得繁琐和低效。为了解决这个问题，react团队就提出了<code>旧版 context API</code>。有了这个<code>旧版 context API</code>，我们就只需要在父组件那里声明一下需要跨层级传递props的数据结构和类型，那么，在需要用到props的子组件再声明一次就可以通过<code>this.context.xxx</code>来访问到<code>xxx</code>这个prop。</p>
<p>但是，<code>旧版 context API</code>有一个重大的设计缺陷。那就是“传递截断”问题。所谓的“传递截断”就是指在如果在使用<code>旧版 context API</code>来跨层级去传递props过程中，假如承载了数据源的父组件和最终接收数据的子组件之间的某个组件通过<code>shouldComponentUpdate</code>来跳过自己的更新的话（<code>shouldComponentUpdate</code>函数里面return <code>false</code>），那么子组件也会被动跳过更新，因而无法拿到最新的prop值。</p>
<p><code>新版Context API</code>就是为了弥补这个设计缺陷而实现的，同时也解决了一个语法冗余的问题。<code>旧版 context API</code>很快就被淘汰了，因此关于它的语法就废话不说了。下面说一说，<code>新版 context API</code>的语法问题。</p>
<h4 data-id="heading-4">怎么用？</h4>
<p>使用<code>Context API</code>遵循下面三个步骤：</p>
<ol>
<li>首先，调用<code>const MyContext = React.createContext()</code>去创建一个context 对象实例；</li>
<li>其次，使用<code><MyContext.Provider value=&#123;someValue&#125;></code>组件去声明你想要传递的任何数据；</li>
<li>最后，通过render props范式<code><MyContext.Consumer>&#123;(someValue)=> ....&#125;</MyContext.Consumer></code>或者hook的写法<code>const theContextValue = useContext(MyContext)</code>来把想要读取的数据取回来再进行消费。</li>
</ol>
<p>在<code>新版Context API</code>的实现里面，只要某个子组件订阅了context对象实例所承载的数据，只要这些数据发生了改变，不管该子组件的上层组件做了什么，这个子组件都会得到更新。</p>
<h3 data-id="heading-5">Context API + useReducer</h3>
<p><code>Context API</code> 设计之处，主要是为了解决静态数据的跨组件层级传递的效率问题。当然，你也可以用它来传递动态数据 - 组件状态。这种情况下，那就变成了另外一种范式：<code>Context API</code>版的redux范式。</p>
<h4 data-id="heading-6">实现了什么功能？</h4>
<p>在hook的世界里面，如果状态结构简单的话，那么我们可以使用<code>useState</code>来创建组件状态，如果状态结果比较复杂的话，那么我们就可以使用<code>useReducer</code>来创建组件状态。不过，其实在react源码内部，<code>useState</code>也是也只是内置了reducer的<code>useReducer</code>，关于这一点，可以查看我的<a href="https://juejin.cn/post/6876659994448625671" target="_blank">《【react】react hook运行原理解析》</a>。所以，我这里的“<code>Context API</code>版的redux范式”就是指“Context API + useReducer”。</p>
<p>通过将<code>Context API</code>的跨任何组件层级运输数据的能力和<code>useReducer</code>组件状态创建和更新能力结合起来，最终把它们提升到组件树的根组件，我们就可以实现“<code>Context API</code>版的redux范式。</p>
<h4 data-id="heading-7">怎么用？</h4>
<ol>
<li>
<p>在根组件上（假设是<code><App></code>），使用<code>useReducer</code>来创建状态：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// App.js</span>
<span class="hljs-keyword">const</span> initialState = &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">0</span>&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reducer</span>(<span class="hljs-params">state, action</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'increment'</span>:
      <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count + <span class="hljs-number">1</span>&#125;;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'decrement'</span>:
      <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count - <span class="hljs-number">1</span>&#125;;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [state,dispatch] = useReducer(reducer,initialState)

    <span class="hljs-keyword">return</span> (......)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在根组件上，使用<code>Context API</code>来创建context对象实例，并使用它的<code>Provider</code>将状态和改变状态的方法（这里是<code>dispatch</code>）传递下去：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// App.js</span>
<span class="hljs-keyword">const</span> initialState = &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">0</span>&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> MyContext = React.createContext()

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reducer</span>(<span class="hljs-params">state, action</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'increment'</span>:
      <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count + <span class="hljs-number">1</span>&#125;;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'decrement'</span>:
      <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count - <span class="hljs-number">1</span>&#125;;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [state,dispatch] = React.useReducer(reducer,initialState)

    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;state,dispatch&#125;&#125;</span>></span>&#123;.....&#125;<span class="hljs-tag"></<span class="hljs-name">MyContext.Provider</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>最后是在需要消费的子组件里面导入context实例对象，使用<code>useContext()</code>来将状态和更新状态的方法取回来：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// ChildComponent.js</span>
<span class="hljs-keyword">import</span> &#123;MyContext&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ChildComponent</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> &#123;state,dispatch&#125; = useContext(MyContext)
    
    <span class="hljs-keyword">return</span> (
        <div>
         current count is &#123;state.count&#125;
         <button onClick=&#123;<span class="hljs-function">() =></span> dispatch(&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'decrement'</span>&#125;)&#125;>-</button>
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch(&#123;type: 'increment'&#125;)&#125;>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
        <div>
    )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>通过上面三个步骤，我们就可以实现一个redux范式。在这个实现里面：<code>Context API</code>负责数据的分发，<code>useReducer</code>复杂状态的管理（创建状态，更新状态），最后通过在根组件上把两者结合起来，那么子组件就可以通过<code>useContext</code>这个hook来消费了。</p>
<h3 data-id="heading-8">redux + react-redux</h3>
<h4 data-id="heading-9">什么是 redux ？</h4>
<p>当我们提起 “redux” 的时候，一般它有广义和狭义两种含义：狭义上它是单纯是指<code>redux.js</code>这个类库，也就是所谓的redux core；而广义上，它是指以<code>redux.js</code>为核心的Flux框架（围绕其中的有react，react-redux， redux-toolkit等类库），这个框架的核心概念有“store”，“state”，“view”，“dispatch”，“action”，“reducer”等。在这个小节，这里的“redux”是包含了上面广义和狭义的两种含义。</p>
<p>看看官方文档怎么说：</p>
<blockquote>
<p>Redux is a pattern and library for managing and updating application state, using events called "actions". It serves as a centralized store for state that needs to be used across your entire application, with rules ensuring that the state can only be updated in a predictable fashion.</p>
</blockquote>
<blockquote>
<p>The patterns and tools provided by Redux make it easier to understand when, where, why, and how the state in your application is being updated, and how your application logic will behave when those changes occur.</p>
</blockquote>
<p>注意，上面的阐述中强调了两点：</p>
<ul>
<li>redux是一个【状态管理】的框架；</li>
<li>这个框架能够很好地帮助你明白状态在“什么时候”，“在哪里”，“为什么”，“发生了怎样的”改变。</li>
</ul>
<p>自从redux core 团队推出 redux-toolkit之后，编写 redux 应用效率和体验也越来越好了，在这里，我就不赘述【怎样用 redux】了，感兴趣的自己去官网看看。</p>
<h4 data-id="heading-10">什么是 react-redux？</h4>
<p>众所周知，<code>react-redux</code>是一个桥接react和redux的类库。基本实现原理是通过消费redux core 所提供的 <code>store.subscribe(listener)</code> 这个 API 来完成的：即监听redux store的state变化，一旦它发生变化了，那么我么就通知 UI 层（react 组件）去重新渲染自己。虽然说，redux core 可以绑定到任何的 UI 层，但是目前为止，大家谈论到 redux 的时候都是默认指的绑定到用 react.js 实现的 UI 层。所以，在这种语境下，一个 redux 框架的最小集合是包括“react.js”,"redux.js","react-redux.js"，而react-redux是这个框架的不可或缺的重要一环。</p>
<h3 data-id="heading-11">三者之间有什么区别</h3>
<p>在探究三者之间有什么区别之前，我们不妨明确一下什么是“状态管理（state management）”。而在明确什么是“状态管理”之前需要明确一下什么是“状态”？</p>
<p>什么是状态呢？“状态”就是一些描述应用行为的动态数据。如果对前端状态进行区分的话，那么我们又可以分为“业务状态”和“UI 状态”，“本地状态” 和 “共享状态”等。如何划分状态不重要，重要的是“状态”是一个关于如何存储，读取，更新数据的一个话题。</p>
<p>状态机专家，<a href="https://github.com/davidkpiano/xstate" target="_blank" rel="nofollow noopener noreferrer">XState.js</a>类库作者 David Khourshid 说过：</p>
<blockquote>
<p>State management is how state changes over time.</p>
</blockquote>
<p>如果说实现了状态管理的集合代码就是“状态管理器”的话，综上所述，状态管理器需要满足以下要求：</p>
<ul>
<li>能够存储和初始化状态值</li>
<li>能够读取到现在的状态值</li>
<li>能够更新状态值并且通知到外界</li>
</ul>
<p>现在，从这个角度来看看，上面提到的两个技术（<code>Context API</code>,<code>Context API + useReducer</code>）跟<code>redux + react-redux</code>有什么不同。</p>
<ul>
<li>
<p>Context API</p>
<ul>
<li>这个技术目的是解决所谓的 “prop-drilling” 问题，实现了数据的【传递】和【共享】而已。它并不是真正的状态管理器。</li>
<li>在 React DevTools 中显示 Provider 和 Consumer 组件的当前context值，但不显示该值随时间变化的任何历史记录</li>
<li>订阅了context实例对象的组件在context值变化的时候一定会被强制更新，也就是说没办法跳过更新。</li>
<li>不包括任何副作用和中间件机制。</li>
</ul>
</li>
<li>
<p>Context API + useReducer</p>
<ul>
<li>
<p>纯 <code>Context API</code> 有点不足点，它一并具有</p>
</li>
<li>
<p>某种程度上是一个状态管理器，但是功能要比<code>redux + react-redux</code>要弱，比单纯的<code>Context API</code>要强。</p>
</li>
<li>
<p><code>Context API + useReducer</code>实现的redux范式没有副作用机制和中间件的扩展能力。当然，你可以在react hook 的能力上去封装出对应的副作用能力，中间件能力，selector能力，但是如果是那样的话，你只不过在实现在一个低配版的redux而已。</p>
</li>
<li>
<p>在这种范式下，只要你的组件订阅了context实例对象，那么一旦context对象的某部分值发生改变，你的组件都会被迫更新，即使你没有消费这部分的值。但是在 <code>redux+ react-redux</code> 的实现里面就不会这样。只有当前组件所消费的状态值发生改变了，当前组件才会被更新。这就避免了因为不必要更新所带来的性能问题。</p>
</li>
<li>
<p>在周边工具这一块，<code>Context API + useReducer</code>有React DevTools，而<code>redux+ react-redux</code> 有 Redux DevTools。从撞他管理的角度，Redux DevTools比React DevTools强多了，它能够回答关于状态管理的四个“什么”问题：状态在“什么时候”，“在什么地方”，“为什么”，“发生了什么样的”变化。</p>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-12">各自适用的场景</h3>
<p>还是那句老话，脱离具体的业务场景去讨论不同技术的好坏都是耍流氓。那些相似的技术就像世间上的各种“刀”，一旦发明出来，则意味着必定有它的最佳使用场景。下面我们来总结一下这三种技术的各自适用场景分别是什么。</p>
<ul>
<li>Context API
<ul>
<li>只考虑偏静态数据的跨组件层级传递和共享，不考虑状态更新</li>
</ul>
</li>
<li>Context API + useReducer
<ul>
<li>小中型的状态管理场景，意味着状态规模不大，更新状态的逻辑代码不复杂</li>
<li>对代码的可调试性没有很高的要求</li>
<li>对渲染性能没有很高的要求</li>
</ul>
</li>
<li>redux + react-redux
<ul>
<li>中大型的状态管理场景，意味着状态规模很大，更新状态的逻辑代码比较复杂，存在多人协作</li>
<li>代码的可调式性有比较高的要求。需要快速地知道四个“什么”问题（状态在“什么时候”，“在什么地方”，“为什么”，“发生了什么样的”变化）的答案。</li>
<li>需要用到副作用机制增加代码的可读性</li>
<li>需要用到中间件来增加应用的可扩展性</li>
<li>需要对用户操作轨迹进行日志记录</li>
<li>考虑使用一个redux store 对接到不同的 UI 层（比如同时对接到react和vue）</li>
<li>在渲染性能上有更高的追求</li>
</ul>
</li>
</ul>
<p>可能你会觉得在什么时候采用<code>Context API + useReducer</code>与什么时候采用<code>redux + react-redux</code>的抉择上依然感到困惑，那不妨考虑采纳 redux core 团队成员Mark Erikson的观点：</p>
<blockquote>
<p>if you get past 2-3 state-related contexts in an application, you're re-inventing a weaker version of React-Redux and should just switch to using Redux.</p>
</blockquote>
<p>也就是说，当你的react应用开始出现三个或者以上的context对象，你是时候要考虑切换到redux框架上来了。</p>
<h3 data-id="heading-13">总结</h3>
<p>时至今日，redux 死了没？我的答案是：“它还活着”。只要前端开发范式没有变，还是【数据驱动DOM更新】的话，我相信，redux 这种状态管理框架不但能活着，而且它还会在中大型的前端项目中继续大放异彩。</p>
<h3 data-id="heading-14">参考资料</h3>
<p>-<a href="https://blog.isquaredsoftware.com/2021/01/context-redux-differences/#comparing-context-and-redux" target="_blank" rel="nofollow noopener noreferrer">Blogged Answers: Why React Context is Not a "State Management" Tool (and Why It Doesn't Replace Redux)</a></p></div>  
</div>
            