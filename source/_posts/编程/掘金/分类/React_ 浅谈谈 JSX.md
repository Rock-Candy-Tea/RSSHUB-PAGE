
---
title: 'React_ 浅谈谈 JSX'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2312'
author: 掘金
comments: false
date: Mon, 24 May 2021 19:39:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=2312'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是 JSX</h2>
<p><strong>JSX</strong>，是一个 <code>JavaScript</code> 的语法扩展；在 <code>JavaScript</code> 代码中可以直接写 <code>HTML</code>的标记。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> name = <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>hello &#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>JSX 的本质：</strong> 它并不是模版引擎，而是动态创建组件的一颗语法糖。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> name = <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">const</span> element = React.createElement(
  h1, <span class="hljs-comment">// type</span>
  <span class="hljs-literal">null</span>, <span class="hljs-comment">// attribute</span>
  <span class="hljs-string">"hello "</span>, <span class="hljs-comment">// ...children</span>
  name
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">如何使用</h2>
<blockquote>
<p><strong>Expressions：</strong> any valid unit of code that resolves to a value.
<strong>表达式：</strong> 会返回值的任何有效代码单元。</p>
</blockquote>
<h4 data-id="heading-2">1. <code>JSX</code> 本身就是表达式</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>hello jsx<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2. 在属性中使用表达式</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><h1 foo=&#123;<span class="hljs-number">1</span> + <span class="hljs-number">2</span> + <span class="hljs-number">3</span> + <span class="hljs-number">4</span>&#125;></h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">3. 支持扩展运算符（...）</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> props = &#123; <span class="hljs-attr">firstName</span>: <span class="hljs-string">""</span>, <span class="hljs-attr">lastName</span>: <span class="hljs-string">""</span> &#125;;
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyComponent</span> &#123;<span class="hljs-attr">...props</span>&#125; /></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">4. 表达式作为子元素</h4>
<p><code>props.children</code> 和其他 <code>prop</code> 一样，它可以传递任意类型的数据，而不仅仅是 <code>React</code> 已知的可渲染类型。</p>
<p>例如，如果你有一个自定义组件，你可以把回调函数作为 <code>props.children</code> 进行传递，但要确保返回值必须是可 <code>render</code> 的节点：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 调用子元素回调 numTimes 次，来重复生成组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Repeat</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">let</span> items = [];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < props.numTimes; i++) &#123;
    items.push(props.children(i));
  &#125;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;items&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ListOfTenThings</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Repeat</span> <span class="hljs-attr">numTimes</span>=<span class="hljs-string">&#123;10&#125;</span>></span>
      &#123;(index) => <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span>></span>This is item &#123;index&#125; in the list<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;
    <span class="hljs-tag"></<span class="hljs-name">Repeat</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种用法并不常见，但可以用于扩展 JSX。</p>
<h4 data-id="heading-6">5. 使用点语法</h4>
<p>当你在一个模块中导出许多 <code>React</code> 组件时，这会非常方便。例如，如果 <code>MyComponents.DatePicker</code> 是一个组件，你可以在 <code>JSX</code> 中直接使用：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-keyword">const</span> MyComponents = &#123;
  <span class="hljs-attr">DatePicker</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">DatePicker</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Imagine a &#123;props.color&#125; datepicker here.<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
  &#125;,
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">BlueDatePicker</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyComponents.DatePicker</span> <span class="hljs-attr">color</span>=<span class="hljs-string">"blue"</span> /></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">约定</h2>
<p>自定义组件使用大写字母开头。</p>
<ul>
<li><code>React</code> 默认小写的 <code>tag</code> 为原生 <code>DOM</code> 节点，如 <code>div</code>；</li>
<li>所有大写字母开头的都是自定义组件，<code>React</code> 会去寻找它的定义并 <code>render</code>。</li>
</ul>
<h2 data-id="heading-8">这是不被允许的</h2>
<p>不能将通用表达式作为 <code>React</code> 元素类型。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; PhotoStory, VideoStory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./stories'</span>;

<span class="hljs-keyword">const</span> components = &#123;
  <span class="hljs-attr">photo</span>: PhotoStory,
  <span class="hljs-attr">video</span>: VideoStory
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Story</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-comment">// 错误！JSX 类型不能是一个表达式。</span>
  <span class="hljs-keyword">return</span> <span class="xml"><components[props.storyType] story=&#123;props.story&#125; /></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果遇到需要根据 <code>prop</code> 来渲染不同组件的情况，可以赋值给大写字母开头的变量</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Story</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-comment">// 正确！JSX 类型可以是大写字母开头的变量。</span>
  <span class="hljs-keyword">const</span> SpecificStory = components[props.storyType];
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">SpecificStory</span> <span class="hljs-attr">story</span>=<span class="hljs-string">&#123;props.story&#125;</span> /></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">优点</h2>
<ul>
<li>声明式创建界面更直观（类 <code>HTML</code>）</li>
<li>代码动态创建界面更灵活</li>
<li>语法和 js 相同，无需学习新的模版语言</li>
</ul>
<h2 data-id="heading-10">参考资料</h2>
<ul>
<li>JSX 简介：<a href="https://zh-hans.reactjs.org/docs/introducing-jsx.html" target="_blank" rel="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/introd…</a></li>
<li>深入 JSX：<a href="https://zh-hans.reactjs.org/docs/jsx-in-depth.html" target="_blank" rel="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/jsx-in…</a></li>
</ul></div>  
</div>
            