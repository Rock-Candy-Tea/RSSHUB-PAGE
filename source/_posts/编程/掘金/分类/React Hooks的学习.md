
---
title: 'React Hooks的学习'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6227'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 02:29:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=6227'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、为什么学习hooks，hooks是什么，hooks有什么作用?</h2>
<p><strong>Hook</strong> 是React16.8的新增特性，它是一个特殊的函数，可以让你“钩入” React 的特性，可以在不用编写class组件的情况下使用state以及其他的React特性。为什么要学习hook呢？因为我们在开发的时候，往往会遇到一些问题，例如：<strong>在组件之间复用状态逻辑困难</strong>、<strong>复杂组件变得难以理解</strong>、<strong>难以理解的class</strong>等等。Hook 在无需修改组件结构的情况下<strong>复用状态逻辑</strong>。Hook 将组件中相互关联的部分拆分成更小的函数（<strong>比如设置订阅或请求数据</strong>），而<strong>并非强制按照生命周期划分</strong>。还可以使用 reducer 来管理组件的内部状态，使其更加<strong>可预测</strong>。Hook还可以在不使用class的情况下，使用更多的React特性。</p>
<h2 data-id="heading-1">2、HOOKS概览</h2>
<h4 data-id="heading-2">1、 使用 <strong>useState</strong></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 声明一个叫 “count” 的 state 变量。</span>
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You clicked &#123;count&#125; times<span class="hljs-tag"></<span class="hljs-name">p</span>></span> &#123;/*使用State时*/&#125;
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count + 1)&#125;> &#123;/*更新state*/&#125;
        Click me
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>useState 唯一的参数就是<strong>初始 state</strong>，在例子中就是<strong>useState(0)</strong>，0就是初始state。useState 会返回一对值：<strong>当前状态(count)和一个更新它的函数(setCount)</strong>。可以在事件处理函数中或其他一些地方调用这个函数。它<strong>类似 class 组件的 this.setState</strong>，但是它不会把新的 state 和旧的 state 进行合并。以下是等价的class hook实现的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Example</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You clicked &#123;this.state.count&#125; times<span class="hljs-tag"></<span class="hljs-name">p</span>></span> &#123;/*使用State时*/&#125;
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.setState(&#123; count: this.state.count + 1 &#125;)&#125;> &#123;/*更新state*/&#125;
          Click me
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上比较发现：在 class 中，通过在构造函数中设置 <code>this.state</code> 为 <code>&#123; count: 0 &#125;</code> 来初始化 <code>count </code>state 为 <code>0</code>，显示当前state时，需读取<code>this.state.count</code>，在函数中可直接使用<code>count</code>。更改state时，在 class 中，需要<code>this.setState()</code>来更新 count 值。在函数中，已经有了<code>setCount</code>和<code>count</code>变量，<code>不需要 this</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Example</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在函数组件中没有 this，所以不能分配或读取 this.state。可直接在组件中调用 useState Hook，useState Hook可以在一个组件中<strong>多次使用</strong>，可以同时创建多个变量，在调用useState 时可以给 state 变量取不同的名字：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 声明一个叫 “count” 的 state 变量</span>
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-comment">// 声明多个 state 变量！</span>
  <span class="hljs-keyword">const</span> [age, setAge] = useState(<span class="hljs-number">42</span>);
  <span class="hljs-keyword">const</span> [fruit, setFruit] = useState(<span class="hljs-string">'banana'</span>);
  <span class="hljs-keyword">const</span> [todos, setTodos] = useState([&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'Learn Hooks'</span> &#125;]);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：<strong>调用 useState 方法的时候做了什么?</strong> 定义了一个变量<code>count</code>，与 class 里面的 <code>this.state </code>提供的功能完全相同，一般来说，在函数退出后变量就会”消失”，而 <strong>state 中的变量会被 React 保留</strong>。useState()里唯一的参数就是初始 state，与class不同的是，不必须使用对象，可以按照需要使用数字或字符串进行赋值。<strong>useState 方法的返回值是什么？</strong> 就是<code>const [count, setCount] = useState()</code>解构出来的<code>count</code>和<code>setCount</code>这与 class 里面 <code>this.state.count </code>和 <code>this.setState </code>类似，唯一区别就是<strong>需要成对的获取</strong>它们。所以上面是示例可以理解为：声明了一个叫 <code>count</code> 的 state 变量，然后把它设为<code> 0</code>。React 会在重复渲染时记住它当前的值，并且提供最新的值给<code>setCount</code>函数，通过调用 <code>setCount</code> 来<strong>更新当前</strong>的<code>count</code>。</p>
</blockquote>
<h4 data-id="heading-3">2、使用 <strong>useEffect</strong></h4>
<p>在熟悉 React class 的生命周期函数后，可以将 useEffect Hook 看做 <code>componentDidMount</code> <code>componentDidUpdate</code> 和 <code>componentWillUnmount</code> 这三个函数的组合。与 <code>componentDidMount</code> 或 <code>componentDidUpdate</code> <strong>不同的是，使用 useEffect 调度的 effect 不会阻塞浏览器更新屏幕，使应用看起来响应更快。</strong> 大多数情况下，effect 不需要同步地执行。useEffect可以在函数组件中执行副作用操作（<strong>数据获取，设置订阅以及手动更改 React 组件中的 DOM 都属于副作用</strong>）以下是分别是<strong>class组件/函数组件</strong> 例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//class组件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Example</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You clicked <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.state.count&#125;</span> times`</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You clicked <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.state.count&#125;</span> times`</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You clicked &#123;this.state.count&#125; times<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.setState(&#123; count: this.state.count + 1 &#125;)&#125;>
          Click me
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="hljs-comment">//函数组件</span>
<span class="hljs-keyword">import</span> React, &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-comment">// 与componentDidMount和componentDidUpdate类似：</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 使用浏览器API更新文档标题</span>
    <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You clicked <span class="hljs-subst">$&#123;count&#125;</span> times`</span>;
  &#125;);

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
<blockquote>
<p>注意： 在 class 组件中，要在两个生命周期函数中编写重复的代码。而使用<strong>useEffect</strong>，告诉了组件在渲染后执行某些操作，将其保存，在执行 DOM 更新之后调用它。为什么在函数组件内部调用呢？因为将 useEffect 放在组件内部让我们可以在 effect 中直接访问 <code>count</code> state 变量（或其他 props），Hook <strong>使用了 JavaScript 的闭包机制</strong>，不用引入特定的 React API来读取它。默认情况下，useEffect在<strong>第一次渲染之后和每次更新之后都会执行</strong>。</p>
</blockquote>
<p>将 useEffect Hook 看做 <code>componentDidMount</code> <code>componentDidUpdate</code> 和 <code>componentWillUnmount</code> 这三个函数的组合的写法如下：当返回一个函数时，即做了清除操作。更新逻辑不需要特定的代码来处理，因为 useEffect 默认就会处理，它会在调用一个新的 effect 之前对前一个 effect 进行清理。可使用多个effect，将不相关逻辑分离到不同的 effect 中，</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleStatusChange</span>(<span class="hljs-params">status</span>) </span>&#123;
      setIsOnline(status.isOnline);
    &#125;

    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123; <span class="hljs-comment">//清除操作</span>
      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
    &#125;;
  &#125;);
<span class="hljs-comment">//性能优化</span>
useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You clicked <span class="hljs-subst">$&#123;count&#125;</span> times`</span>;
&#125;, [count]); <span class="hljs-comment">// 仅在 count 更改时更新</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">3、使用useContext</h4>
<p><code>const value = useContext(MyContext);</code>接收一个 context 对象（React.createContext 的返回值）并返回该 <strong>context 的当前值</strong>，当前值<strong>由上层组件中距离当前组件最近的 <MyContext.Provider> 的 value prop 决定</strong>，当组件上最近的<code><MyContext.Provider></code>更新时，useContext会触发<strong>重渲染</strong>，并使用最新值传递给 <code>MyContext provider</code> 的 <code>context value</code> 值，如以下示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> themes = &#123;
  <span class="hljs-attr">light</span>: &#123;
    <span class="hljs-attr">foreground</span>: <span class="hljs-string">"#000000"</span>,
    <span class="hljs-attr">background</span>: <span class="hljs-string">"#eeeeee"</span>
  &#125;,
  <span class="hljs-attr">dark</span>: &#123;
    <span class="hljs-attr">foreground</span>: <span class="hljs-string">"#ffffff"</span>,
    <span class="hljs-attr">background</span>: <span class="hljs-string">"#222222"</span>
  &#125;
&#125;;
<span class="hljs-keyword">const</span> ThemeContext = React.createContext(themes.light);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ThemeContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;themes.dark&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Toolbar</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">ThemeContext.Provider</span>></span></span>
  );
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Toolbar</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> theme = useContext(ThemeContext);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">background:</span> <span class="hljs-attr">theme.background</span>, <span class="hljs-attr">color:</span> <span class="hljs-attr">theme.foreground</span> &#125;&#125;></span>
      I am styled by theme context!
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">4、使用useReducer</h4>
<p><code>const [state, dispatch] = useReducer(reducer, initialArg, init)</code>是<code>useState</code>的替代方案，当state 逻辑较复杂且包含多个子值，或者下一个 state 依赖于之前的 state 时，useReducer 会比 useState 更适用，且使用 useReducer 还能给那些会触发深更新的组件做性能优化，以下是用 reducer 重写 useState 例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params">initialCount</span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: initialCount&#125;;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reducer</span>(<span class="hljs-params">state, action</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'increment'</span>:
      <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count + <span class="hljs-number">1</span>&#125;;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'decrement'</span>:
      <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count - <span class="hljs-number">1</span>&#125;;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'reset'</span>:
      <span class="hljs-keyword">return</span> init(action.payload);
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params">&#123;initialCount&#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [state, dispatch] = useReducer(reducer, initialCount, init);
  <span class="hljs-comment">//第三个参数，用作惰性初始化</span>
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      Count: &#123;state.count&#125;
      <span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch(&#123;type: 'reset', payload: initialCount&#125;)&#125;>
        Reset
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch(&#123;type: 'decrement'&#125;)&#125;>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch(&#123;type: 'increment'&#125;)&#125;>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">5、使用useCallback</h4>
<p>把<strong>内联回调函数</strong>及<strong>依赖项数组</strong>作为参数传入 useCallback，返回该函数的当前版本，该回调函数仅在某个依赖项改变时才会更新</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> memoizedCallback = useCallback(
  <span class="hljs-function">() =></span> &#123;
    doSomething(a, b);
  &#125;,
  [a, b],
);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：依赖项数组不会作为参数传给回调函数。虽然从概念上来说它表现为：所有回调函数中引用的值都应该出现在依赖项数组中。</p>
</blockquote>
<h4 data-id="heading-7">6、使用useMemo</h4>
<p><code>const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b])</code>把<strong>创建函数</strong>和<strong>依赖项数组</strong>作为参数传入 useMemo，它仅会在某个依赖项改变时才重新计算 memoized 值。这种优化有助于避免在每次渲染时都进行高开销的计算。<strong>传入 useMemo 的函数会在渲染期间执行,不要在这个函数内部执行与渲染无关的操作</strong>，如果没有提供依赖项数组，useMemo 在每次渲染时都会计算新的值，可以把 useMemo 作为性能优化的手段，但不要把它当成语义上的保证，<code>useCallback(fn, deps) </code>相当于 <code>useMemo(() => fn, deps)</code>。</p>
<h4 data-id="heading-8">6、使用useRef</h4>
<p><code>const refContainer = useRef(initialValue)</code>useRef 返回一个可变的 ref 对象，其 <code>.current </code>属性<strong>被初始化为传入的参数（initialValue）</strong>。返回的 ref 对象在组件的整个生命周期内保持不变。将 ref 对象以 <code><div ref=&#123;myRef&#125; /> </code>形式传入组件，则无论该节点如何改变，React 都会将 ref 对象的 <code>.current</code> 属性设置为<strong>相应的 DOM 节点</strong>。useRef() 比 ref 属性更有用,它可以很方便地保存任何可变值,因为ref 属性创建的是一个普通 Javascript 对象。而 useRef() 和自建一个 &#123;current: ...&#125; 对象的唯一区别是，useRef 会在每次渲染时返回同一个 ref 对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">TextInputWithFocusButton</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> myRef = useRef(<span class="hljs-literal">null</span>); <span class="hljs-comment">// null为初始值</span>
  <span class="hljs-keyword">const</span> onButtonClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// `current` 指向已挂载到 DOM 上的文本输入元素</span>
    myRef.current.focus();
  &#125;;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;myRef&#125;</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onButtonClick&#125;</span>></span>Focus the input<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">7、使用useImperativeHandle</h4>
<p><code>useImperativeHandle(ref, createHandle, [deps])</code>useImperativeHandle 可以在使用 ref 时自定义暴露给父组件的实例值。在大多数情况下，应当避免使用 ref 这样的命令式代码。<code>useImperativeHandle</code> 应当与<code>forwardRef</code> 一起使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FancyInput</span>(<span class="hljs-params">props, ref</span>) </span>&#123;
  <span class="hljs-keyword">const</span> inputRef = useRef();
  useImperativeHandle(ref, <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">focus</span>: <span class="hljs-function">() =></span> &#123;
      inputRef.current.focus();
    &#125;
  &#125;));
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;inputRef&#125;</span> <span class="hljs-attr">...</span> /></span></span>;
&#125;
FancyInput = forwardRef(FancyInput);
<span class="hljs-comment">// 渲染 <FancyInput ref=&#123;inputRef&#125; /> 的父组件可以调用 inputRef.current.focus()。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">8、使用useLayoutEffect</h4>
<blockquote>
<p>函数形参与 useEffect 相同，但它会在所有的 DOM 变更之后同步调用 effect。可以使用它来读取 DOM 布局并同步触发重渲染。在浏览器执行绘制之前，useLayoutEffect 内部的更新计划将被同步刷新。</p>
</blockquote>
<h4 data-id="heading-11">9、使用useDebugValue</h4>
<p>useDebugValue 可用于在 React 开发者工具中显示自定义 hook 的标签。例如：一个返回 Date 值的自定义 Hook 可以通过格式化函数来避免不必要的 toDateString 函数调用：
<code>useDebugValue(date, date => date.toDateString());</code></p></div>  
</div>
            