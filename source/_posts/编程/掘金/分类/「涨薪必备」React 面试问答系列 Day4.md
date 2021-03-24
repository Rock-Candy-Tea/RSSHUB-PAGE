
---
title: '「涨薪必备」React 面试问答系列 Day4'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fac807b8490c4c11a9630a9f29e467d3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 03:29:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fac807b8490c4c11a9630a9f29e467d3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a></p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文翻译自 <a href="https://github.com/sudheerj/reactjs-interview-questions" target="_blank" rel="nofollow noopener noreferrer">sudheerj/reactjs-interview-questions</a></p>
<p>本文同步于公众号洛竹早茶馆，转载请联系作者。</p>
</blockquote>
<ul>
<li><a href="https://juejin.cn/post/6940873220618731551" target="_blank">「涨薪必备」React 面试问答系列 Day1</a></li>
<li><a href="https://juejin.cn/post/6942438427291811870" target="_blank">「涨薪必备」React 面试问答系列 Day2</a></li>
<li><a href="https://juejin.cn/post/6942813303664017444" target="_blank">「涨薪必备」React 面试问答系列 Day3</a></li>
</ul>
<h2 data-id="heading-0">1. createElement 和 cloneElement 的区别是什么？</h2>
<p>JSX 元素将被转换为 <code>React.createElement()</code> 函数以创建 React 元素，这些元素将用于 UI 的对象表示。而 <code>cloneElement</code> 用于克隆元素并将新的 <code>props</code> 传递给它。</p>
<p><strong>课后扩展：</strong></p>
<ul>
<li><a href="https://zh-hans.reactjs.org/docs/react-api.html" target="_blank" rel="nofollow noopener noreferrer">React 顶层 API</a></li>
</ul>
<h2 data-id="heading-1">2. React 中的状态提升是什么？</h2>
<p>当多个组件需要共享相同的变化数据时，建议将共享状态提升到它们最接近的共同祖先。这意味着，如果两个子组件共享来自其父组件的相同数据，则将状态移到父组件，而不是在两个子组件中都保持内部状态。</p>
<h2 data-id="heading-2">3. 组件生命周期有哪些不同阶段？</h2>
<p>组件生命周期具有三个不同的生命周期阶段。</p>
<ol>
<li>**Mounting：**组件已准备好安装在浏览器DOM中。这个阶段涵盖了生命周期方法 <code>constructor()</code>、<code>getDerivedStateFromProps()</code>、 <code>render()</code> 和 <code>componentDidMount()</code> 的初始化。</li>
<li>**Updating：**在此阶段，组件以两种方式进行更新，即发送新 <code>props</code> 和从 <code>setState()</code> 或 <code>forceUpdate()</code> 更新状态。此阶段涵盖了<code>getDerivedStateFromProps()</code>，<code>shouldComponentUpdate()</code>，<code>render()</code> 、<code>getSnapshotBeforeUpdate()</code> 和 <code>componentDidUpdate()</code> 生命周期方法。</li>
<li>**Unmounting：**在最后一个阶段，不再需要该组件并从浏览器DOM上卸载该组件。 这个阶段包括 <code>componentWillUnmount()</code> 生命周期方法。</li>
</ol>
<p>值得一提的是，在将更改应用于 DOM 时，React 内部具有阶段性概念。 它们分开如下</p>
<ol>
<li><strong>Render：</strong> 该组件将渲染而没有任何副作用。这适用于 Pure 组件，在此阶段，React 可以暂停、中止或重新启动渲染。</li>
<li><strong>Pre-commit：</strong> 在组件将更改实际应用于 DOM 之前，有一段时间可以让 React 通过 <code>getSnapshotBeforeUpdate()</code> 从 DOM 中读取内容。</li>
<li><strong>Commit</strong> React 与 DOM 一起工作并分别执行最终的生命周期：<code>componentDidMount()</code> 用于安装，<code>componentDidUpdate()</code> 用于更新，以及 <code>componentWillUnmount()</code> 用于卸载。</li>
</ol>
<p>React 16.3+ (或者 <a href="http://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/" target="_blank" rel="nofollow noopener noreferrer">在线交互版本</a>)</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fac807b8490c4c11a9630a9f29e467d3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>React 16.3 之前的版本：</p>
<p><img alt="phases 16.2" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33a918a89bdd49c08e80732f5f6af367~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">4. React 生命周期有哪些？</h2>
<p>React 16.3 以前的版本：</p>
<ul>
<li>** componentWillMount：**在渲染之前执行，用于根组件中的应用程序级别配置。</li>
<li>** componentDidMount：**在首次渲染之后执行，所有 AJAX 请求，DOM 或状态更新以及设置事件侦听器都应在此执行。</li>
<li>** componentWillReceiveProps：**在特定属性更新以触发状态转换时执行。</li>
<li>** shouldComponentUpdate：**确定是否要更新组件。默认情况下，它返回 <code>true</code>。如果你确定在状态或属性更新后不需要渲染组件，则可以返回 <code>false</code> 值。这是提高性能的好地方，因为如果组件收到新的 <code>props</code>，它可以防止重新渲染。</li>
<li>** componentWillUpdate：**当有属性或状态改变被<code>shouldComponentUpdate()</code> 确认并返回 <code>true</code> 时，在重新渲染组件之前执行。</li>
<li>** componentDidUpdate：**通常，它用于响应属性或状态更改来更新 DOM。</li>
<li>** componentWillUnmount：**它将用于取消任何传出的网络请求，或删除与该组件关联的所有事件侦听器。</li>
</ul>
<p>React 16.3+ 版本</p>
<ul>
<li>**getDerivedStateFromProps：**在调用 <code>render()</code> 之前被调用，并且在每次渲染中都会被调用。对于需要派生状态的罕见用例，这是存在的。<a href="https://reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html" target="_blank" rel="nofollow noopener noreferrer">如果您需要派生状态</a> 值得一读。</li>
<li><strong>componentDidMount：</strong> 在首次渲染之后执行，并且所有 AJAX 请求、DOM 或状态更新以及设置事件侦听器都应在此发生。</li>
<li><strong>shouldComponentUpdate：</strong> 确定是否将更新组件。默认情况下，它返回 <code>true</code>。如果你确定在状态或属性更新后不需要渲染组件，则可以返回 <code>false</code>值。这是提高性能的好地方，因为如果组件接收到新的属性，它可以防止重新渲染。</li>
<li><strong>getSnapshotBeforeUpdate：</strong> 在将呈现的输出提交给 DOM 之前立即执行。此方法返回的任何值都将传递到 <code>componentDidUpdate()</code> 中。 这对于从 DOM（即滚动位置）捕获信息很有用。</li>
<li><strong>componentDidUpdate：</strong> 通常，它用于响应属性或状态更改来更新DOM。如果 <code>shouldComponentUpdate()</code> 返回 <code>false</code>，则不会触发。</li>
<li><strong>componentWillUnmount：</strong> 它将用于取消任何传出的网络请求，或删除与该组件关联的所有事件侦听器。</li>
</ul>
<h2 data-id="heading-4">5. 高阶组件是什么</h2>
<p>A <em>higher-order component</em> (<em>HOC</em>) is a function that takes a component and returns a new component. Basically, it's a pattern that is derived from React's compositional nature.</p>
<p>We call them <strong>pure components</strong> because they can accept any dynamically provided child component but they won't modify or copy any behavior from their input components.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> EnhancedComponent = higherOrderComponent(WrappedComponent)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>HOC can be used for many use cases:</p>
<ol>
<li>Code reuse, logic and bootstrap abstraction.</li>
<li>Render hijacking.</li>
<li>State abstraction and manipulation.</li>
<li>Props manipulation.</li>
</ol>
<h2 data-id="heading-5">6. 如何为 HOC 组件 创建 props 代理？</h2>
<p>您可以使用属性代理模式添加或编辑传递给组件的属性，如下所示：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HOC</span>(<span class="hljs-params">WrappedComponent</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> newProps = &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'New Header'</span>,
        <span class="hljs-attr">footer</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">showFeatureX</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">showFeatureY</span>: <span class="hljs-literal">true</span>
      &#125;

      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span> &#123;<span class="hljs-attr">...this.props</span>&#125; &#123;<span class="hljs-attr">...newProps</span>&#125; /></span></span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>课后扩展：</strong></p>
<ul>
<li><a href="https://juejin.cn/post/6844903641074106381" target="_blank">react 高阶组件的代理模式</a></li>
</ul>
<h2 data-id="heading-6">7. context 是什么？</h2>
<p><code>Context</code> 提供了一种通过组件树传递数据的方法，而不需要一层一层手动传递属性。</p>
<p>例如，需要由许多组件在应用程序中访问经过身份验证的用户，本地设置首选项，UI 主题等。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123;Provider, Consumer&#125; = React.createContext(defaultValue)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">8. 什么是 children 属性？</h2>
<p><code>Children</code> 是一个 prop（<code>this.props.children</code>），允许你将组件作为数据传递给其他组件，就像你使用的任何其他 prop 一样。放置在组件的开始标记和结束标记之间的组件树将作为 <code>children</code> 道具传递给该组件。</p>
<p>React API 中有许多方法可作为该属性。其中包括 <code>React.Children.map</code>、<code>React.Children.forEach</code>，<code>React.Children.count</code>、<code>React.Children.only</code> 和 <code>React.Children.toArray</code>。</p>
<p>children 的简单用法如下所示：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> MyDiv = React.createClass(&#123;
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.props.children&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  &#125;
&#125;)

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyDiv</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;'Hello'&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;'World'&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">MyDiv</span>></span></span>,
  node
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">9. React 中如何写注释？</h2>
<p>React JSX 中的注释和 JavaScript 的多行注释很像，但是用大括号括起来。</p>
<p><strong>单行注释：</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div>
  &#123;<span class="hljs-comment">/* 这里是单行注释 */</span>&#125;
  &#123;<span class="hljs-string">`Welcome <span class="hljs-subst">$&#123;user&#125;</span>, let's play React`</span>&#125;
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>多行注释：</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div>
  &#123;<span class="hljs-comment">/* Multi-line comments for more than
   one line */</span>&#125;
  &#123;<span class="hljs-string">`Welcome <span class="hljs-subst">$&#123;user&#125;</span>, let's play React`</span>&#125;
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">10. 在 constructor 中给 <code>super</code> 函数传递 props 的目的是什么？</h2>
<p>一个子类构造器在 <code>super()</code> 方法调用之前是无法拿到 <code>this</code> 引用的。这同样也适用于 ES6 中的 sub-classes。调用 <code>super()</code> 时传递 props 的主要是为了在子类的构造器中访问 <code>this.props</code>。</p>
<p><strong>传递 props：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props)

    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.props) <span class="hljs-comment">// 打印 &#123; name: 'John', age: 42 &#125;</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Not passing props:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>()

    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.props) <span class="hljs-comment">// 打印 undefined</span>

    <span class="hljs-comment">// 但是 props 参数依然可以访问</span>
    <span class="hljs-built_in">console</span>.log(props) <span class="hljs-comment">// 打印 &#123; name: 'John', age: 42 &#125;</span>
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 在 constructor 之外没有影响</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.props) <span class="hljs-comment">// 打印 &#123; name: 'John', age: 42 &#125;</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码片段揭示了 <code>this.props</code> 仅在构造函数中有所不同。在构造函数外部表现将是相同的。</p>
<p>更多信息可以参考 <a href="https://overreacted.io/zh-hans/why-do-we-write-super-props/" target="_blank" rel="nofollow noopener noreferrer">为什么我们要写 super(props) ？</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            