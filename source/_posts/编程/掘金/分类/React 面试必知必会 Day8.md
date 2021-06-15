
---
title: 'React 面试必知必会 Day8'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1594'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 07:45:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=1594'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a>，一个坚持写作的博主，感恩你的每一个点赞和评论。</p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文翻译自 <a href="https://github.com/sudheerj/reactjs-interview-questions" target="_blank" rel="nofollow noopener noreferrer">sudheerj/reactjs-interview-questions</a></p>
<p>本文同步于公众号洛竹早茶馆，转载请联系作者。</p>
</blockquote>
<h2 data-id="heading-0">1. 你如何实现服务器端渲染或SSR？</h2>
<p>React 已经具备了在 Nod e服务器上处理渲染的能力。有一个特殊版本的 DOM 渲染器，它与客户端的模式相同。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> ReactDOMServer <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom/server'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>;

ReactDOMServer.renderToString(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>)。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法将把常规的 HTML 输出为一个字符串，然后可以作为服务器响应的一部分放在页面主体内。在客户端，React 检测到预渲染的内容，并无缝地衔接该内容。</p>
<h3 data-id="heading-1">2. 如何在 React 中启用生产模式？</h3>
<p>你应该使用 Webpack 的 <code>DefinePlugin</code> 方法来设置 <code>NODE_ENV</code> 为 <code>production</code>，通过它来剥离诸如 propType 验证和额外警告的东西。除此之外，如果你对代码进行最小化处理，例如 Uglify 的无效代码消除法，剥离出只用于开发的代码和注释，这将极大地减少你的包的大小。</p>
<h2 data-id="heading-2">3. 什么是 CRA 以及它的好处？</h2>
<p><code>create-react-app</code> CLI 工具允许你快速创建和运行React应用程序，无需配置步骤。</p>
<p>让我们使用 CRA 创建 Todo 应用程序。</p>
<pre><code class="hljs language-console copyable" lang="console"><span class="hljs-meta">#</span><span class="bash"> 安装</span>
<span class="hljs-meta">$</span><span class="bash"> npm install -g create-react-app</span>
<span class="hljs-meta">
#</span><span class="bash"> 创建新项目</span>
<span class="hljs-meta">$</span><span class="bash"> create-react-app todo-app</span>
<span class="hljs-meta">$</span><span class="bash"> <span class="hljs-built_in">cd</span> todo-app</span>
<span class="hljs-meta">
#</span><span class="bash"> 构建、测试、运行</span>
<span class="hljs-meta">$</span><span class="bash"> npm run build</span>
<span class="hljs-meta">$</span><span class="bash"> npm run <span class="hljs-built_in">test</span></span>
<span class="hljs-meta">$</span><span class="bash"> npm start</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它包括我们建立一个 React 应用程序所需要的一切。</p>
<ol>
<li>支持 React、JSX、ES6 和 Flow 语法。</li>
<li>超越 ES6 的语言额外功能，如对象传播操作者。</li>
<li>自动前缀的 CSS，所以你不需要 <code>-webkit-</code> 或其他前缀。</li>
<li>一个快速的交互式单元测试运行器，内置支持覆盖率报告。</li>
<li>一个实时的开发服务器，对常见的错误发出警告。</li>
<li>一个构建脚本，用于捆绑 JS、CSS 和图片，并提供哈希和源码图。</li>
</ol>
<h2 data-id="heading-3">4. 安装中的生命周期方法的顺序是什么？</h2>
<p>当一个组件的实例被创建并插入到 DOM 中时，生命周期方法按以下顺序被调用。</p>
<ol>
<li><code>constructor()</code></li>
<li><code>static getDerivedStateFromProps()</code></li>
<li><code>render()</code></li>
<li><code>componentDidMount()</code></li>
</ol>
<h2 data-id="heading-4">5. 在 React v16 中，有哪些生命周期方法将被废弃？</h2>
<p>以下生命周期方法将是不安全的编码做法，在异步渲染中会出现更多问题。</p>
<ol>
<li><code>componentWillMount()</code></li>
<li><code>componentWillReceiveProps()</code></li>
<li><code>componentWillUpdate()</code></li>
</ol>
<p>从 React v16.3 开始，这些方法被别名为 <code>UNSAFE_</code> 前缀，未加前缀的版本将在 React v17 中被移除。</p>
<h2 data-id="heading-5">6. <code>getDerivedStateFromProps()</code> 生命周期方法的目的是什么？</h2>
<p>新的静态的 <code>getDerivedStateFromProps()</code> 生命周期方法在一个组件实例化后以及重新渲染前被调用。它可以返回一个对象来更新状态，也可以返回 <code>null</code> 来表示新的 props 不需要任何状态更新。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getDerivedStateFromProps</span>(<span class="hljs-params">props, state</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个生命周期方法与 <code>componentDidUpdate()</code> 一起涵盖了 <code>componentWillReceiveProps()</code> 的所有用例。</p>
<h3 data-id="heading-6">7. <code>getSnapshotBeforeUpdate()</code> 生命周期方法的目的是什么？</h3>
<p>新的 <code>getSnapshotBeforeUpdate()</code> 生命周期方法会在 DOM 更新前被调用。这个方法的返回值将作为第三个参数传递给 <code>componentDidUpdate()</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getSnapshotBeforeUpdate</span>(<span class="hljs-params">prevProps, prevState</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个生命周期方法与 <code>componentDidUpdate()</code> 一起涵盖了 <code>componentWillUpdate()</code> 的所有用例。</p>
<h2 data-id="heading-7">8. Hooks 是否取代了渲染 props 和高阶组件？</h2>
<p>渲染 props 和高阶组件都只渲染一个 children，但在大多数情况下，Hooks 是一种更简单的方式，通过减少树中的嵌套来达到这个目的。</p>
<h2 data-id="heading-8">9. 推荐用什么方式来命名组件？</h2>
<p>建议通过引用来命名组件，而不是使用 <code>displayName</code>。</p>
<p>使用 <code>displayName</code> 来命名组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React.createClass(&#123;
  <span class="hljs-attr">displayName</span>: <span class="hljs-string">'TodoApp'</span>,
  <span class="hljs-comment">// ...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>推荐的方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TodoApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">10. 建议在组件类中方法的排序是什么？</h2>
<p>建议从安装到渲染阶段的方法的排序。</p>
<ol>
<li><code>static</code> 方法</li>
<li><code>constructor()</code></li>
<li><code>getChildContext()</code></li>
<li><code>componentWillMount()</code></li>
<li><code>componentDidMount()</code></li>
<li><code>componentWillReceiveProps()</code></li>
<li><code>shouldComponentUpdate()</code></li>
<li><code>componentWillUpdate()</code></li>
<li><code>componentDidUpdate()</code></li>
<li><code>componentWillUnmount()</code></li>
<li>点击处理程序或事件处理程序，如 <code>onClickSubmit()</code> 或 <code>onChangeDescription()</code></li>
<li>渲染的 getter 方法，如 <code>getSelectReason()</code> 或 <code>getFooterContent()</code></li>
<li>可选的渲染方法，如 <code>renderNavigation()</code> 或 <code>renderProfilePicture()</code></li>
<li>render()</li>
</ol></div>  
</div>
            