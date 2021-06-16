
---
title: 'React 面试必知必会 Day9'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5731'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 07:57:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=5731'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第15天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a>，一个坚持写作的博主，感恩你的每一个点赞和评论。</p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文翻译自 <a href="https://github.com/sudheerj/reactjs-interview-questions" target="_blank" rel="nofollow noopener noreferrer">sudheerj/reactjs-interview-questions</a></p>
<p>本文同步于公众号洛竹早茶馆，转载请联系作者。</p>
</blockquote>
<h2 data-id="heading-0">1. 什么是切换组件？</h2>
<p>切换组件是一个渲染许多组件中的一个组件。我们需要使用对象来将 props 值映射到组件。</p>
<p>例如，一个切换组件可以根据 <code>page</code> props 显示不同的页面。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> HomePage <span class="hljs-keyword">from</span> <span class="hljs-string">'./HomePage'</span>;
<span class="hljs-keyword">import</span> AboutPage <span class="hljs-keyword">from</span> <span class="hljs-string">'./AboutPage'</span>;
<span class="hljs-keyword">import</span> ServicesPage <span class="hljs-keyword">from</span> <span class="hljs-string">'./ServicesPage'</span>;
<span class="hljs-keyword">import</span> ContactPage <span class="hljs-keyword">from</span> <span class="hljs-string">'./ContactPage'</span>;

<span class="hljs-keyword">const</span> PAGES = &#123;
  <span class="hljs-attr">home</span>: HomePage,
  <span class="hljs-attr">about</span>: AboutPage,
  <span class="hljs-attr">services</span>: ServicesPage,
  <span class="hljs-attr">contact</span>: ContactPage,
&#125;;

<span class="hljs-keyword">const</span> Page = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-keyword">const</span> Handler = PAGES[props.page] || ContactPage;

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Handler</span> &#123;<span class="hljs-attr">...props</span>&#125; /></span></span>;
&#125;;

<span class="hljs-comment">// PAGES 对象的键可以在 props 类型中使用，以捕捉开发时间错误。</span>
Page.propTypes = &#123;
  <span class="hljs-attr">page</span>: PropTypes.oneOf(<span class="hljs-built_in">Object</span>.keys(PAGES)).isRequired,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 为什么我们需要向 <code>setState()</code> 传递一个函数？</h2>
<p>这背后的原因是，<code>setState()</code> 是一个异步操作。出于性能的考虑，React 会对状态变化进行批处理，所以在调用 <code>setState()</code> 后，状态可能不会立即发生变化。这意味着你在调用 <code>setState()</code> 时不应该依赖当前的状态，因为你不能确定这个状态会是什么。解决办法是将一个函数传递给 <code>setState()</code>，并将之前的状态作为参数。通过这样做，你可以避免由于 <code>setState()</code> 的异步性而导致用户在访问时获得旧的状态值的问题。</p>
<p>假设初始计数值为 0。在连续三次递增操作后，该值将只递增一个。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 假设 this.state.count === 0</span>
<span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span> &#125;);
<span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span> &#125;);
<span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span> &#125;);
<span class="hljs-comment">// this.state.count === 1，而不是 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们给 <code>setState()</code> 传递一个函数，计数就会被正确地递增。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">prevState, props</span>) =></span> (&#123;
  <span class="hljs-attr">count</span>: prevState.count + props.increment,
&#125;));
<span class="hljs-comment">// this.state.count === 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3. 为什么在 <code>setState()</code> 中首选函数而不是对象？</h2>
<p>React 可以将多个 <code>setState()</code> 的调用批量化为一次更新，以提高性能。因为 <code>this.props</code> 和 <code>this.state</code> 可能被异步更新，你不应该依赖它们的值来计算下一个状态。</p>
<p>这个计数器的例子将无法按预期更新。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 错误❌</span>
<span class="hljs-built_in">this</span>.setState(&#123;
  <span class="hljs-attr">counter</span>: <span class="hljs-built_in">this</span>.state.counter + <span class="hljs-built_in">this</span>.props.increment,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首选的方法是用函数而不是对象调用 <code>setState()</code>。该函数将接收先前的状态作为第一个参数，并将应用更新时的 props 作为第二个参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 正确✅</span>
<span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">prevState, props</span>) =></span> (&#123;
  <span class="hljs-attr">counter</span>: prevState.counter + props.increment,
&#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. React 中的严格模式是什么？</h2>
<p><code>React.StrictMode</code> 是一个有用的组件，用于暴露应用程序中的潜在问题。就像 <code><Fragment></code>，<code><StrictMode></code>不会渲染任何额外的 DOM 元素。它为其后代激活了额外的检查和警告。这些检查只适用于开发模式。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ExampleApplication</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Header</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">React.StrictMode</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">ComponentOne</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">ComponentTwo</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">React.StrictMode</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Footer</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的例子中，严格模式检查只适用于 <code><ComponentOne></code> 和 <code><ComponentTwo></code> 组件。</p>
<h2 data-id="heading-4">5. 为什么 <code>isMounted()</code> 是一个反模式，正确的解决方案是什么？</h2>
<p><code>isMounted()</code> 的主要用例是避免在组件被卸载后调用 <code>setState()</code>，因为它会发出警告。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isMounted()) &#123;
  <span class="hljs-built_in">this</span>.setState(&#123;...&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在调用 <code>setState()</code> 之前检查 <code>isMounted()</code> 确实可以消除警告，但这也违背了警告的目的。使用 <code>isMounted()</code> 是一种代码异味，因为你检查的唯一原因是你认为你可能在组件卸载后还持有一个引用。</p>
<p>一个最佳的解决方案是找到在组件卸载后可能调用 <code>setState()</code> 的地方，并修复它们。这种情况通常是由于回调引起的，当一个组件在等待一些数据时，在数据到达之前被卸载。理想情况下，任何回调都应该在 <code>componentWillUnmount()</code> 中取消（在解除挂载之前）。</p>
<blockquote>
<p>代码异味 (Code smell)：程序开发领域，代码中的任何可能导致深层次问题的症状都可以叫做代码异味。 通常，在对代码做简短的反馈迭代时，代码异味会暴露出一些深层次的问题，这里的反馈迭代，是指以一种小范围的、可控的方式重构代码。</p>
</blockquote>
<h2 data-id="heading-5">6. React 中支持哪些指针事件？</h2>
<p>指针事件提供了一个处理所有输入事件的统一方法。在过去，我们有一个鼠标和各自的事件监听器来处理它们，但现在我们有许多设备与拥有鼠标不相关，如带有触摸表面的手机或笔。我们需要记住，这些事件只能在支持 Pointer Events 规范的浏览器中工作。</p>
<p>以下事件类型现在在 React DOM 中可用。</p>
<ol>
<li><code>onPointerDown</code></li>
<li><code>onPointerMove</code></li>
<li><code>onPointerUp</code></li>
<li><code>onPointerCancel</code></li>
<li><code>onGotPointerCapture</code></li>
<li><code>onLostPointerCapture</code></li>
<li><code>onPointerEnter</code></li>
<li><code>onPointerLeave</code></li>
<li><code>onPointerOver</code></li>
<li><code>onPointerOut</code></li>
</ol>
<h2 data-id="heading-6">7. 为什么组件名称要以大写字母开头？</h2>
<p>如果你使用 JSX 渲染你的组件，该组件的名称必须以大写字母开头，否则 React 将抛出一个错误，即未识别的标签。这个惯例是因为只有 HTML 元素和 SVG 标签可以以小写字母开头。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SomeComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-comment">// 掘金不止，代码不停</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以定义名称以小写字母开头的组件类，但当它被导入时，它应该是大写字母。在这里，小写就可以了。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">myComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> /></span></span>;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> myComponent;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而当导入另一个文件时，它应该以大写字母开始。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> MyComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'./MyComponent'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">关于 React 组件的命名，有哪些例外情况？</h3>
<p>组件名称应以大写字母开头，但这一惯例也有少数例外。带点的小写标签名（属性访问器）仍被认为是有效的组件名。</p>
<p>例如，下面的标签可以被编译成一个有效的组件。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">obj.component</span> /></span></span> <span class="hljs-comment">// `React.createElement(obj.component)`</span>
   )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">8. React v16 中支持自定义 DOM 属性吗？</h2>
<p>是的，在过去，React 习惯于忽略未知的 DOM 属性。如果你写的 JSX 有一个 React 不认识的属性，React 会直接跳过它。</p>
<p>例如，让我们看一下下面的属性。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div mycustomattribute=&#123;<span class="hljs-string">'something'</span>&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用 React v15 渲染一个空的 div 到 DOM 上。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 React v16 中，任何未知的属性最终都会出现在 DOM 中。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">mycustomattribute</span>=<span class="hljs-string">"something"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这对于提供浏览器特定的非标准属性，尝试新的 DOM API，以及与有主见的第三方库集成是非常有用的。</p>
<h2 data-id="heading-9">9. constructor 和 getInitialState 的区别是什么？</h2>
<p>当使用 ES6 类时，你应该在构造函数中初始化状态，而当使用 <code>React.createClass()</code> 时，应该在 <code>getInitialState()</code> 方法中初始化状态。</p>
<p><strong>使用 ES6 类：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-comment">/* 初始化状态 */</span>
    &#125;;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用 <code>React.createClass()</code>：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> MyComponent = React.createClass(&#123;
  <span class="hljs-function"><span class="hljs-title">getInitialState</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">/* 初始化状态 */</span>
    &#125;;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong> <code>React.createClass()</code> 在 React v16 中已被废弃并删除。请使用普通的 JavaScript 类来代替。</p>
<h2 data-id="heading-10">10. 你能在不调用 setState 的情况下强制一个组件重新渲染吗？</h2>
<p>默认情况下，当你的组件的状态或 props 改变时，你的组件会重新渲染。如果你的 <code>render()</code> 方法依赖于其他数据，你可以通过调用 <code>forceUpdate()</code> 告诉 React 该组件需要重新渲染。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">component.forceUpdate(callback);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>建议避免使用 <code>forceUpdate()</code>，只在 <code>render()</code> 中读取<code>this.props</code> 和 <code>this.state</code>。</p></div>  
</div>
            