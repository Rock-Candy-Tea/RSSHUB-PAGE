
---
title: 'React 面试必知必会 Day7'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8016'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 05:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8016'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a>，一个坚持写作的博主，感恩你的每一个点赞和评论。</p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文翻译自 <a href="https://github.com/sudheerj/reactjs-interview-questions" target="_blank" rel="nofollow noopener noreferrer">sudheerj/reactjs-interview-questions</a></p>
<p>本文同步于公众号洛竹早茶馆，转载请联系作者。</p>
</blockquote>
<h2 data-id="heading-0">1. 如何在 React 使用样式？</h2>
<p><code>style</code> 属性接受一个小驼峰命名法属性的 JavaScript 对象，而不是一个 CSS 字符串。这与 DOM 风格的 JavaScript 属性一致，更有效率，并能防止 XSS 安全漏洞。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> divStyle = &#123;
  <span class="hljs-attr">color</span>: <span class="hljs-string">'blue'</span>,
  <span class="hljs-attr">backgroundImage</span>: <span class="hljs-string">`url(<span class="hljs-subst">$&#123;imgUrl&#125;</span>)`</span>,
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HelloWorldComponent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;divStyle&#125;</span>></span>Hello World!<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式键名是符合驼峰命名法的，以便与在 JavaScript 中访问 DOM 节点的属性相一致（例如 <code>node.style.backgroundImage</code>）。</p>
<h2 data-id="heading-1">2. 事件在 React 中有何不同？</h2>
<p>Handling events in React elements has some syntactic differences:</p>
<p>在 React 元素上处理事件有一些语法上的不同：</p>
<ol>
<li>React 事件处理程序使用小驼峰命名，而不是小写。</li>
<li>使用 JSX，你传递一个函数作为事件处理程序，而不是一个字符串。</li>
</ol>
<h2 data-id="heading-2">3. 如果你在构造函数中使用 <code>setState()</code>，会发生什么？</h2>
<p>当你使用 <code>setState()</code> 时，除了分配给对象的状态外，React 还重新渲染组件和它的所有子组件。你会得到这样的错误：只能更新一个已挂载或正在挂载的组件。所以我们需要使用 <code>this.state</code> 来初始化构造函数中的变量。</p>
<h2 data-id="heading-3">4. 索引作为键的影响是什么？</h2>
<p>键应该是稳定的、可预测的和唯一的，这样 React 就可以跟踪元素。</p>
<p>在下面的代码片段中，每个元素的键都是基于索引的，而不是与被表示的数据相联系。这限制了 React 可以做的优化。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">&#123;
  todos.map(<span class="hljs-function">(<span class="hljs-params">todo, index</span>) =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Todo</span> &#123;<span class="hljs-attr">...todo</span>&#125; <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span> /></span></span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你使用元素数据作为唯一键，假设 <code>todo.id</code> 在这个列表中是唯一的，并且是稳定的，React 将能够对元素进行重新排序，而不需要像以前那样重新计算它们。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">&#123;
  todos.map(<span class="hljs-function"><span class="hljs-params">todo</span> =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Todo</span> &#123;<span class="hljs-attr">...todo</span>&#125; <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;todo.id&#125;</span> /></span></span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5. 在 <code>componentWillMount()</code> 方法中使用 <code>setState</code> 真的好吗?</h2>
<p>是的，在 <code>componentWillMount()</code> 方法中使用 <code>setState()</code> 是安全的。但同时，建议避免在<code>componentWillMount()</code> 生命周期方法中进行异步初始化。<code>componentWillMount()</code> 在挂载发生前立即被调用。它在 <code>render()</code> 之前被调用，因此在这个方法中设置状态不会触发重新渲染。避免在这个方法中引入任何副作用或订阅。我们需要确保组件初始化的异步调用发生在 <code>componentDidMount()</code> 而不是 <code>componentWillMount()</code>。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
  axios.get(<span class="hljs-string">`api/todos`</span>).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">messages</span>: [...result.data]
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6. 如果你在初始状态下使用 props，会发生什么？</h2>
<p>如果组件上的 props 被改变而组件没有被刷新，新的 props 值将永远不会被显示，因为构造函数永远不会更新组件的当前状态。来自 props 的状态初始化只在组件第一次被创建时运行。</p>
<p>下面这个组件就不会显示更新的输入值。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);

    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">records</span>: [],
      <span class="hljs-attr">inputValue</span>: <span class="hljs-built_in">this</span>.props.inputValue,
    &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.inputValue&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 render 方法中使用 props 将更新数值。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);

    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">record</span>: [],
    &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.props.inputValue&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">7. 你如何有条件地渲染组件？</h2>
<p>在某些情况下，你想根据一些状态来渲染不同的组件。JSX 不渲染 <code>false</code> 或 <code>undefined</code>，所以你可以使用条件性短路来渲染你的组件的某一部分，只有当某个条件为真时。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> MyComponent = <span class="hljs-function">(<span class="hljs-params">&#123; name, address &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    &#123;address && <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;address&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你需要一个 <code>if-else</code> 条件，则使用三元运算符。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> MyComponent = <span class="hljs-function">(<span class="hljs-params">&#123; name, address &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    &#123;address ? <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;address&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span> : <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;'Address is not available'&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">8. 为什么我们在 DOM 元素上传递 props 时需要谨慎？</h2>
<p>当我们传递 props 时，我们会遇到添加未知的 HTML 属性的风险，这是一个不好的做法。相反，我们可以使用带有 <code>...rest</code> 操作符的 prop 解构，所以它将只添加需要的 prop。</p>
<p>比如说。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> ComponentA = <span class="hljs-function">() =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ComponentB</span> <span class="hljs-attr">isDisplay</span>=<span class="hljs-string">&#123;true&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">componentStyle</span>'&#125; /></span></span>
);

<span class="hljs-keyword">const</span> ComponentB = <span class="hljs-function">(<span class="hljs-params">&#123; isDisplay, ...domProps &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> &#123;<span class="hljs-attr">...domProps</span>&#125;></span>&#123;'ComponentB'&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">9. 如何在 React 中使用装饰器？</h2>
<p>你可以对你的类组件进行装饰，这与将组件传入一个函数是一样的。<strong>装饰器</strong>是修改组件功能的灵活和可读的方式。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">@setTitle(<span class="hljs-string">'Profile'</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Profile</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-comment">//....</span>
&#125;

<span class="hljs-comment">/*
title 是一个字符串，将被设置为文档标题。WrappedComponent 是我们的装饰器在以下情况下会收到的东西直接放在一个组件类上面时，我们的装饰器会收到这样的信息，如上面的例子所示
*/</span>
<span class="hljs-keyword">const</span> setTitle = <span class="hljs-function"><span class="hljs-params">title</span> =></span> <span class="hljs-function"><span class="hljs-params">WrappedComponent</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">document</span>.title = title;
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span> &#123;<span class="hljs-attr">...this.props</span>&#125; /></span></span>;
    &#125;
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong> 装饰器是一个没有进入 ES7 的功能，但目前是一个第二阶段的建议。</p>
<h2 data-id="heading-9">10. 如何 memo 化一个组件？</h2>
<p>有一些可用的缓存库，可以用于函数组件。</p>
<p>例如，<code>moize</code> 库可以在另一个组件中对组件进行 memo 化。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> moize <span class="hljs-keyword">from</span> <span class="hljs-string">'moize'</span>;
<span class="hljs-keyword">import</span> Component <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/Component'</span>; <span class="hljs-comment">// 本模块导出一个非 memo 组件</span>

<span class="hljs-keyword">const</span> MemoizedFoo = moize.react(Component);

<span class="hljs-keyword">const</span> Consumer = <span class="hljs-function">() =></span> &#123;
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    &#123;'I will memoize the following entry:'&#125;
    <span class="hljs-tag"><<span class="hljs-name">MemoizedFoo</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>更新：</strong> 从 React v16.6.0 开始，我们有一个 <code>React.memo</code>。它提供了一个更高阶的组件，除非 props 发生变化，否则会将组件缓存。要使用它，只需在使用前用 <code>React.memo</code> 包住组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MemoComponent = React.memo(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MemoComponent</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-comment">/* render using props */</span>
&#125;);
<span class="hljs-comment">// 或者</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React.memo(MyFunctionComponent);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            