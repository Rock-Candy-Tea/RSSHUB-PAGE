
---
title: 'React 面试必知必会 Day 6'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5626'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 07:59:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=5626'
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
<h2 data-id="heading-0">1. 如何在 React 中对 props 进行验证？</h2>
<p>当应用程序运行在开发模式时，React 会自动检查我们在组件上设置的所有 props，以确保它们具有正确的类型。如果类型不正确，React 会在控制台生成警告信息。由于对性能的影响，它在生产模式中被禁用。必需 props 是用 <code>isRequired</code> 定义的。</p>
<p>预定义的 props 类型集合。</p>
<ol>
<li><code>PropTypes.number</code></li>
<li><code>PropTypes.string</code></li>
<li><code>PropTypes.array</code></li>
<li><code>PropTypes.object</code></li>
<li><code>PropTypes.func</code></li>
<li><code>PropTypes.node</code></li>
<li><code>PropTypes.element</code></li>
<li><code>PropTypes.bool</code></li>
<li><code>PropTypes.symbol</code></li>
<li><code>PropTypes.any</code></li>
</ol>
<p>我们可以为 <code>User</code> 组件定义 <code>propTypes</code>，如下所示。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> PropTypes <span class="hljs-keyword">from</span> <span class="hljs-string">'prop-types'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-keyword">static</span> propTypes = &#123;
    <span class="hljs-attr">name</span>: PropTypes.string.isRequired,
    <span class="hljs-attr">age</span>: PropTypes.number.isRequired,
  &#125;;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;`Welcome, $&#123;this.props.name&#125;`&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;`Age, $&#123;this.props.age&#125;`&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"></></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：在 React v15.5 中，<code>PropTypes</code> 被从 <code>React.PropTypes</code> 移到 <code>prop-types</code>库中。</p>
</blockquote>
<p>等效的函数式组件：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> PropTypes <span class="hljs-keyword">from</span> <span class="hljs-string">'prop-types'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">User</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;`Welcome, $&#123;this.props.name&#125;`&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;`Age, $&#123;this.props.age&#125;`&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;

User.propTypes = &#123;
  <span class="hljs-attr">name</span>: PropTypes.string.isRequired,
  <span class="hljs-attr">age</span>: PropTypes.number.isRequired,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. React 的优势是什么？</h2>
<p>以下是 React的 主要优势。</p>
<ol>
<li>通过虚拟 DOM 提高应用程序的性能。</li>
<li>JSX 使代码易于阅读和编写。</li>
<li>它在客户端和服务器端都能进行渲染（SSR）。</li>
<li>易于与框架（Angular, Backbone）集成，因为它只是一个视图库。</li>
<li>使用 Jest 等工具容易编写单元和集成测试。</li>
</ol>
<h2 data-id="heading-2">3. React 的局限性是什么？</h2>
<p>除了优点之外，React 也有一些限制。</p>
<ol>
<li>React 只是一个视图库，不是一个完整的框架。</li>
<li>对于刚接触网络开发的初学者来说，有一个学习曲线。</li>
<li>将 React 整合到传统的 MVC 框架中需要一些额外的配置。</li>
<li>代码的复杂性随着内联模板和 JSX 的增加而增加。</li>
<li>太多的小组件导致了过度工程化或模板化。</li>
</ol>
<h2 data-id="heading-3">4. 什么是 React v16 中的错误边界（Error Boundary）？</h2>
<p>错误边界是指在其子组件树的任何地方捕获 JavaScript 错误的组件，记录这些错误，并显示一个后备 UI ，而不是崩溃的组件树。</p>
<p>如果一个类组件定义了一个新的生命周期方法 <code>componentDidCatch(error, info)</code> 或 <code>static getDerivedStateFromError()</code> ，它就成为一个错误边界。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ErrorBoundary</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">false</span> &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidCatch</span>(<span class="hljs-params">error, info</span>)</span> &#123;
    <span class="hljs-comment">// 你也可以把错误记录到一个错误报告服务中去</span>
    logErrorToMyService(error, info)。
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getDerivedStateFromError</span>(<span class="hljs-params">error</span>)</span> &#123;
    <span class="hljs-comment">// 更新状态，以便下次渲染时显示回退的用户界面。</span>
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">true</span> &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state.hasError) &#123;
      <span class="hljs-comment">// 你可以渲染任何自定义的回退用户界面</span>
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;'Something went wrong.'&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.props.children。
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后把它作为一个普通的组件使用。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><ErrorBoundary>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyWidget</span> /></span></span>
</ErrorBoundary>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5. React v15 中是如何处理错误边界的？</h2>
<p>React v15 使用 <code>unstable_handleError</code> 方法为错误边界提供了非常基本的支持。在 React v16 中，它已经被重新命名为 <code>componentDidCatch</code>。</p>
<h2 data-id="heading-5">6. 静态类型检查的推荐方式是什么？</h2>
<p>通常我们使用 PropTypes 库（<code>React.PropTypes</code> 从 React v15.5 开始转移到 <code>prop-types</code> 包）来进行 React 应用中的类型检查。对于大型代码库，建议使用静态类型检查器，如 Flow 或 TypeScript，在编译时进行类型检查并提供自动补全功能。</p>
<h2 data-id="heading-6">7. <code>react-dom</code> 包有什么用？</h2>
<p><code>react-dom</code> 包提供了 DOM 特定的方法，可以在你的应用程序的顶层使用。大多数组件不需要使用此模块。这个包的一些方法是：</p>
<ol>
<li><code>render()</code></li>
<li><code>hydrate()</code></li>
<li><code>unmountComponentAtNode()</code></li>
<li><code>findDOMNode()</code></li>
<li><code>createPortal()</code></li>
</ol>
<h2 data-id="heading-7">8. <code>react-dom</code> 的 render 方法的目的是什么？</h2>
<p>此方法用于将 React 元素渲染到提供的容器中的 DOM 中，并返回对组件的引用。如果 React 元素之前已渲染到容器中，它将对其执行更新，并且仅在必要时更改 DOM 以反映最新更改。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">ReactDOM.render(element, container[, callback])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果提供了可选的回调，它将在组件渲染或更新后执行。</p>
<h2 data-id="heading-8">9. 什么是 ReactDOMServer？</h2>
<p><code>ReactDOMServer</code> 对象使你能够将组件呈现为静态标记（通常用于节点服务器）。该对象主要用于服务器端渲染（SSR）。以下方法可用于服务器和浏览器环境：</p>
<ol>
<li><code>renderToString()</code></li>
<li><code>renderToStaticMarkup()</code></li>
</ol>
<p>例如，你通常运行基于 Node 的 Web 服务器（如 Express、Hapi 或 Koa），然后调用 <code>renderToString</code> 将根组件渲染为字符串，然后将其作为响应发送。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用 Express</span>
<span class="hljs-keyword">import</span> &#123; renderToString &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom/server'</span>;
<span class="hljs-keyword">import</span> MyPage <span class="hljs-keyword">from</span> <span class="hljs-string">'./MyPage'</span>;

app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.write(<span class="hljs-string">'<!DOCTYPE html><html><head><title>My Page</title></head><body>'</span>);
  res.write(<span class="hljs-string">'<div id="content">'</span>);
  res.write(renderToString(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyPage</span> /></span></span>));
  res.write(<span class="hljs-string">'</div></body></html>'</span>);
  res.end();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">10. 如何在 React 中使用 innerHTML？</h2>
<p><code>dangerouslySetInnerHTML</code> 属性是 React 在浏览器 DOM 中使用 <code>innerHTML</code> 的替代品。就像 <code>innerHTML</code> 一样，考虑到跨站点脚本 (XSS) 攻击，使用此属性是有风险的。你只需要传递一个 <code>__html</code> 对象作为键和 HTML 文本作为值。</p>
<p>在这个例子中，MyComponent 使用 <code>dangerouslySetInnerHTML</code> 属性来设置 HTML 标记：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createMarkup</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">__html</span>: <span class="hljs-string">'First &middot; Second'</span> &#125;;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyComponent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">dangerouslySetInnerHTML</span>=<span class="hljs-string">&#123;createMarkup()&#125;</span> /></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            