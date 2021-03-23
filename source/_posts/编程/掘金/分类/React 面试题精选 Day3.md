
---
title: 'React 面试题精选 Day3'
categories: 
 - 编程
 - 掘金
 - — 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4baa06c59bd4152ae40df8a232a03ae~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 03:45:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4baa06c59bd4152ae40df8a232a03ae~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a></p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文翻译自 <a href="https://github.com/sudheerj/reactjs-interview-questions" target="_blank" rel="nofollow noopener noreferrer">sudheerj/reactjs-interview-questions</a></p>
<p>本文同步于公众号洛竹早茶馆，转载请联系作者。</p>
</blockquote>
<ul>
<li><a href="https://juejin.cn/post/6940873220618731551" target="_blank">React 面试题精选 Day1</a></li>
<li><a href="https://juejin.cn/post/6942438427291811870" target="_blank">React 面试题精选 Day2</a></li>
</ul>
<h2 data-id="heading-0">1. refs 转发是什么？</h2>
<p><em>Ref 转发</em> 是让某些组件可以使用它们接收的 <code>ref</code> 的特性，这些组件还可以进一步将其传递给子组件。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> ButtonElement = React.forwardRef(<span class="hljs-function">(<span class="hljs-params">props, ref</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"CustomButton"</span>></span>
    &#123;props.children&#125;
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
));

<span class="hljs-comment">// Create ref to the DOM button:</span>
<span class="hljs-keyword">const</span> ref = React.createRef();
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ButtonElement</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref&#125;</span>></span>&#123;'Forward Ref'&#125;<span class="hljs-tag"></<span class="hljs-name">ButtonElement</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. refs 回调和 <code>findDOMNode()</code> 哪个是首选项？</h2>
<p>最好使用 refs 回调 而不是 <code>findDOMNode()</code> API。因为 <code>findDOMNode()</code> 将来会阻止对 React 的某些改进。</p>
<p>使用 <code>findDOMNode</code> 的“传统”方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    findDOMNode(<span class="hljs-built_in">this</span>).scrollIntoView();
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> /></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>推荐的方式是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.node = createRef();
  &#125;
  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.node.current.scrollIntoView();
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.node&#125;</span> /></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3. 为什么 Strings Refs 被遗弃了？</h2>
<p>如果你以前使用过 React，那么你可能会熟悉一个较旧的 API，其中的<code>ref</code> 属性是一个字符串，例如 <code>ref = &#123;textInput'&#125;</code>，并且 DOM 节点作为<code>this.refs.textInput</code> 访问。我们建议你不要这样做，因为 String 引用有以下问题，并且被认为是旧版的。字符串引用已经在 <strong>React v16中被删除</strong>。</p>
<ol>
<li>他们迫使 React 跟踪当前正在执行的组件。这是有问题的，因为它使 React 模块成为有状态的，并因此在打包 React 模块时冲突而引起奇怪的错误。</li>
<li>它们是“不可组合的” — 如果库在传递的子项上放置了引用，则用户不能在其上放置其他引用。回调引用完全可以组合。</li>
<li>他们不能和静态分析工具配合（比如 Flow）。Flow 无法猜测出框架 <code>this.refs</code> 上出现的字符串引用及其类型（可能不同）。 回调引用对静态分析更友好。</li>
<li>它无法像大多数人期望的那样使用“渲染回调”模式（例如）
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  renderRow = <span class="hljs-function"><span class="hljs-params">index</span> =></span> &#123;
    <span class="hljs-comment">// This won't work. Ref will get attached to DataTable rather than MyComponent:</span>
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">input-</span>' + <span class="hljs-attr">index</span>&#125; /></span></span>;

    <span class="hljs-comment">// This would work though! Callback refs are awesome.</span>
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;input</span> =></span> (this['input-' + index] = input)&#125; /></span>;
  &#125;;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">DataTable</span> <span class="hljs-attr">data</span>=<span class="hljs-string">&#123;this.props.data&#125;</span> <span class="hljs-attr">renderRow</span>=<span class="hljs-string">&#123;this.renderRow&#125;</span> /></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-3">4. 虚拟 DOM 是什么？</h2>
<p><em>Virtual DOM</em>（VDOM）是_Real DOM_的内存表示形式。 UI的表示形式保留在内存中，并与“真实” DOM同步。 这是在调用渲染函数和在屏幕上显示元素之间发生的一步。 这整个过程称为 <a href="https://zh-hans.reactjs.org/docs/reconciliation.html" target="_blank" rel="nofollow noopener noreferrer">协调</a>。</p>
<h2 data-id="heading-4">5. 虚拟 DOM 原理</h2>
<p>虚拟 DOM 工作原理只有三个简单的步骤。</p>
<ol>
<li>无论何时任何基础数据发生更改，整个 UI 都将以虚拟 DOM 表现形式重新呈现。</li>
</ol>
<p><img alt="vdom" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4baa06c59bd4152ae40df8a232a03ae~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>然后，计算先前的 DOM 表现形式与新的 DOM 表现形式之间的差异。</li>
</ol>
<p><img alt="vdom2" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9347aea466fb4796ad9d92cdf59cc08e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>一旦完成计算，将只会更新内容真正改变的那部分真是 DOM。</li>
</ol>
<p><img alt="vdom3" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d77d0da808024acd8f95b63b8f467aeb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">6. Shadow DOM 和 Virtual DOM 有什么区别？</h2>
<p>Shadow DOM 是一种浏览器技术，主要用于确定 web components 中的变量和 CSS。Virtual DOM 是由浏览器 API 之上的 JavaScript 库实现的概念。</p>
<h2 data-id="heading-6">7. React Fiber 是什么?</h2>
<p>Fiber 是React v16 中新的 <a href="https://zh-hans.reactjs.org/docs/reconciliation.html" target="_blank" rel="nofollow noopener noreferrer">协调</a> 引擎或核心算法的重新实现。React Fiber 的目标是提高其在动画、布局、手势、暂停、中止或重用工作的能力，以及为不同类型的更新分配优先级等方面的适用性和新的并发原语。</p>
<h2 data-id="heading-7">8. React Fiber 的主要设计目的是什么？</h2>
<p>React Fiber 的目标是提高其对动画、布局和手势等领域的适用性。它的 headline 功能是<strong>增量渲染</strong>：能够将渲染工作拆分为多个块并将其分布到多个帧中。</p>
<h2 data-id="heading-8">9. 受控组件是什么？</h2>
<p>在用户输入后能够控制表单中输入元素的组件被称为“受控组件”，比如每一个状态概念都将有一个相关的处理函数</p>
<p>例如下面的例子中，为了将名字转换为全大写，我们使用 <code>handleChange</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">handleChange</span>(<span class="hljs-params">event</span>)</span> &#123;
   <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">value</span>: event.target.value.toUpperCase()&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">10. 非受控组件是什么？</h3>
<p>受控组件是那些把状态维护在其内部的组件，当你想要获得当前值时需要使用 ref 查询 DOM。这有一点像传统的 HTML。</p>
<p>在下面的 <code>UserProfile</code> 组件中，<code>name</code> 输入被使用 <code>ref</code> 获取：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserProfile</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.handleSubmit = <span class="hljs-built_in">this</span>.handleSubmit.bind(<span class="hljs-built_in">this</span>);
    <span class="hljs-built_in">this</span>.input = React.createRef();
  &#125;

  <span class="hljs-function"><span class="hljs-title">handleSubmit</span>(<span class="hljs-params">event</span>)</span> &#123;
    alert(<span class="hljs-string">'A name was submitted: '</span> + <span class="hljs-built_in">this</span>.input.current.value);
    event.preventDefault();
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">onSubmit</span>=<span class="hljs-string">&#123;this.handleSubmit&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span>></span>
          &#123;'Name:'&#125;
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.input&#125;</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"Submit"</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">form</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大多数场景中，我们建议使用受控组件来代替表单组件。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            