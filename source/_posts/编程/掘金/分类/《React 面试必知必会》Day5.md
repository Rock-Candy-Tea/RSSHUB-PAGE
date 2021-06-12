
---
title: '《React 面试必知必会》Day5'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=663'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 07:17:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=663'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a></p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文翻译自 <a href="https://github.com/sudheerj/reactjs-interview-questions" target="_blank" rel="nofollow noopener noreferrer">sudheerj/reactjs-interview-questions</a></p>
<p>本文同步于公众号洛竹早茶馆，转载请联系作者。</p>
</blockquote>
<h3 data-id="heading-0">1. 协调（reconciliation）是什么？</h3>
<p>当一个组件的 props 或 state 发生变化时，React 通过比较新返回的元素和之前渲染的元素来决定是否有必要进行实际的 DOM 更新。当它们不相等时，React 将更新 DOM。这个过程被称为 <em>协调（reconciliation）</em>。</p>
<h3 data-id="heading-1">2. 如何用一个动态键名来设置状态？</h3>
<p>如果你使用 ES6 或 Babel 转码器来转换你的 JSX 代码，那么你可以用计算属性命名完成。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">handleInputChange</span>(<span class="hljs-params">event</span>)</span> &#123;
  <span class="hljs-built_in">this</span>.setState(&#123; [event.target.id]: event.target.value &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. 每次组件渲染时，函数被调用的常见错误是什么？</h3>
<p>你需要确保在传递函数作为参数时，没有调用该函数。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-comment">// 错误❌： handleClick 被调用而不是作为引用被传入</span>
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick()&#125;</span>></span>&#123;'Click Me'&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>取而代之的是传递函数本身，不加圆括号。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-comment">// 正确：handleClick 是作为一个引用传递的!</span>
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>&#123;'Click Me'&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. lazy 函数是否支持命名导出？</h3>
<p>不，目前 <code>React.lazy</code> 函数只支持默认出口。如果你想导入被命名导出的模块，你可以创建一个中间模块，将其作为默认出口。这也保证了摇树的工作，不会拉取未使用的组件。</p>
<p>让我们来看看一个导出多个命名组件的组件文件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// MoreComponents.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> SomeComponent = <span class="hljs-comment">/* ... */</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> UnusedComponent = <span class="hljs-comment">/* ... */</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并在一个中间文件 <code>IntermediateComponent.js</code> 中重新导出 <code>MoreComponents.js</code> 组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// IntermediateComponent.js</span>
<span class="hljs-keyword">export</span> &#123; SomeComponent <span class="hljs-keyword">as</span> <span class="hljs-keyword">default</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./MoreComponents.js'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在你可以使用下面的 lazy 函数导入该模块。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; lazy &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">const</span> SomeComponent = lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./IntermediateComponent.js'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5. 为什么 React 使用 <code>className</code> 而不是 <code>class</code> 属性？</h3>
<p><code>class</code> 是 JavaScript 的一个关键字，而 JSX 是 JavaScript 的一个扩展。这就是为什么 React 使用 <code>className</code> 而不是 <code>class</code> 的主要原因。传递一个字符串作为 <code>className</code> prop。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">menu</span> <span class="hljs-attr">navigation-menu</span>'&#125;></span>&#123;'Menu'&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6. 片段（fragments）是什么？</h3>
<p>这是 React 中常见的模式，用于一个组件返回多个元素。片段让你可以对一个 children 的列表进行分组，而无需在 DOM 中添加额外的节点。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.Fragment</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ChildA</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">ChildB</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">ChildC</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">React.Fragment</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里还有一个短语法可以用，但是很多工具不支持：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">ChildA</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">ChildB</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">ChildC</span> /></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">7. 为什么片段（fragments）比 div 容器要好？</h3>
<ol>
<li>片段的速度更快一些，并且由于没有创建额外的 DOM 节点而使用更少的内存。这只有在非常大和深的树上才会体现出真正的好处。</li>
<li>一些 CSS 机制，如 Flexbox 和 CSS Grid 有一个特殊的父子关系，在中间添加 div 会使其难以保持所需的布局。</li>
<li>DOM 检查器不那么杂乱。</li>
</ol>
<h3 data-id="heading-7">8. 什么是 React 中的传递门（Portal）？</h3>
<p>传递门是一种推荐的方式，可以将子节点渲染到父组件的 DOM 层次结构之外的 DOM 节点中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ReactDOM.createPortal(child, container);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个参数是任何可渲染的 React children，比如一个元素、字符串或片段。第二个参数是一个 DOM 元素。</p>
<h3 data-id="heading-8">9. 什么是无状态组件?</h3>
<p>如果行为是独立于其状态的，那么它可以是一个无状态组件。你可以使用函数或类来创建无状态组件。但除非你需要在你的组件中使用生命周期钩子，否则你应该选择函数组件。如果你决定在这里使用函数组件，会有很多好处；它们易于编写、理解和测试，速度稍快，而且你可以完全避免使用 <code>this</code> 关键字。</p>
<h3 data-id="heading-9">10. 什么是状态组件?</h3>
<p>如果一个组件的行为依赖于该组件的状态（state），那么它可以被称为有状态的组件。这些有状态的组件总是类组件，并且有一个在构造器（<code>constructor</code>）中被初始化的状态。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-comment">// 也可以使用类字段语法</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">count</span>: <span class="hljs-number">0</span> &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>React 16.8 更新：</strong></p>
<p>Hooks 让你在不写类的情况下使用状态和其他 React 功能。</p>
<p>等效的函数组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123;useState&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">const</span> App = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-keyword">return</span> (
    <span class="hljs-comment">// JSX</span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            