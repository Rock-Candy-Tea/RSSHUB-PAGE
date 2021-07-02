
---
title: 'React 18 新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4365'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 04:39:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=4365'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>React 18 alpha版已经发布了，新特性和新的API聚焦在用户体验和性能提升，一起来看看吧~</p>
<h1 data-id="heading-0">安装</h1>
<pre><code class="hljs language-js copyable" lang="js">npm install react@alpha react-dom@alpha
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">Root API</h1>
<ul>
<li><strong>Leacy root API</strong>： ReactDOM.render()</li>
<li><strong>New root API</strong>：ReactDOM.createRoot()</li>
</ul>
<h2 data-id="heading-2">差别</h2>
<p>旧 root API</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>) 

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, container);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新 root API（React 18）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>);

<span class="hljs-comment">// 创建个根节点</span>
<span class="hljs-keyword">const</span> root = ReactDOM.createRoot(container);

<span class="hljs-comment">// 初始渲染: 渲染元素到根节点</span>
root.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>);

<span class="hljs-comment">// 更新时, 不需要再传递容器了</span>
root.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"profile"</span> /></span></span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">hydration</h2>
<p>hydration 函数移动到了 <code>hydrateRoot</code>API<br>
之前：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>);

ReactDOM.hydrate(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>, container);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>);

<span class="hljs-comment">// 创建并渲染 hydration.</span>
<span class="hljs-keyword">const</span> root = ReactDOM.hydrateRoot(container, <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>);

<span class="hljs-comment">// 之后可以更新</span>
root.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"profile"</span> /></span></span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">render callback</h2>
<p>在旧 root API，render接受一个回调</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>);

ReactDOM.render(container, <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 初始渲染或更新后调用</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'rendered'</span>).
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>New root API</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> rootElement = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>);

ReactDOM.createRoot(rootElement).render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">callback</span>=<span class="hljs-string">&#123;()</span> =></span> console.log("renderered")&#125; /></span>);
<span class="hljs-comment">// 或者</span>
ReactDOM.createRoot(rootElement).render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>);
requestIdleCallback(callback);
<span class="hljs-comment">// 或者</span>
ReactDOM.createRoot(rootElement).render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>);
<span class="hljs-built_in">setTimeout</span>(callback, <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">Automatic batching</h1>
<h2 data-id="heading-6">差别</h2>
<p>之前：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [flag, setFlag] = useState(<span class="hljs-literal">false</span>);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
    setCount(<span class="hljs-function"><span class="hljs-params">c</span> =></span> c + <span class="hljs-number">1</span>);
    setFlag(<span class="hljs-function"><span class="hljs-params">f</span> =></span> !f);
    <span class="hljs-comment">// 两个属性更新了，但React只渲染一次（这个就是批量更新）</span>
  &#125;
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick2</span>(<span class="hljs-params"></span>) </span>&#123;
    fetchSomething().then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// React 17 及之前不会批量更新</span>
      setCount(<span class="hljs-function"><span class="hljs-params">c</span> =></span> c + <span class="hljs-number">1</span>); <span class="hljs-comment">// Causes a re-render</span>
      setFlag(<span class="hljs-function"><span class="hljs-params">f</span> =></span> !f); <span class="hljs-comment">// Causes a re-render</span>
    &#125;);
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>Next<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> <span class="hljs-attr">flag</span> ? "<span class="hljs-attr">blue</span>" <span class="hljs-attr">:</span> "<span class="hljs-attr">black</span>" &#125;&#125;></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React 18之前仅仅只有React事件处理函数中是批量更新的，promise，setTimeout，原生事件和其它事件中都不是批量更新。<br><br>
而React18中，在promise，setTimeout，原生事件和其它事件中也都会批量更新了。<br>
之后：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [flag, setFlag] = useState(<span class="hljs-literal">false</span>);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
    fetchSomething().then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// React 18 并且使用 New root API</span>
      setCount(<span class="hljs-function"><span class="hljs-params">c</span> =></span> c + <span class="hljs-number">1</span>);
      setFlag(<span class="hljs-function"><span class="hljs-params">f</span> =></span> !f);
      <span class="hljs-comment">// 只会渲染一次</span>
    &#125;);
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>Next<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> <span class="hljs-attr">flag</span> ? "<span class="hljs-attr">blue</span>" <span class="hljs-attr">:</span> "<span class="hljs-attr">black</span>" &#125;&#125;></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">不想批量更新？</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; flushSync &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
  flushSync(<span class="hljs-function">() =></span> &#123;
    setCounter(<span class="hljs-function"><span class="hljs-params">c</span> =></span> c + <span class="hljs-number">1</span>);
  &#125;);
  <span class="hljs-comment">// React 现在更新DOM了</span>
  flushSync(<span class="hljs-function">() =></span> &#123;
    setFlag(<span class="hljs-function"><span class="hljs-params">f</span> =></span> !f);
  &#125;);
  <span class="hljs-comment">// React 现在更新DOM了</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">startTransition()</h1>
<p>React中如果更新的DOM树很大，ODM比对要花很多时间，容易造成页面失去响应和卡顿。<code>startTransition()</code>可以来解决这个问题。
举一个例子：在输入框中输入文字，同时根据输入的文字查询数据展示提示列表。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 紧迫: 显示输入文字</span>
setInputValue(input);

<span class="hljs-comment">// 不紧迫: 显示查询结果</span>
setSearchQuery(input);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时如果结果很多，同步渲染结果列表，可能会让输入框卡顿。
React 18 之前所有的更新都是同时渲染的。<br></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 紧迫: 显示文字</span>
setInputValue(input);

<span class="hljs-comment">// 标记state</span>
startTransition(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// Transition: 显示结果</span>
  setSearchQuery(input);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>意味着startTransition标记的state更新可以被更加紧迫的更新打断。避免页面卡顿。</p>
<h1 data-id="heading-9">Suspense</h1>
<pre><code class="hljs language-js copyable" lang="js"><Layout>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">NavBar</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Sidebar</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RightPane</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Post</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">Spinner</span> /></span>&#125;>
      <span class="hljs-tag"><<span class="hljs-name">Comments</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">RightPane</span>></span></span>
</Layout>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>http请求会阻塞html的解析，把<code><Comments/></code>组件写到<code><Suspense/></code>中，React可以跳过请求评论数据，继续解析剩余的html。这样不会阻塞。</p>
<h1 data-id="heading-10">useDeferredValue</h1>
<p>不需要紧迫显示的text可以延迟一定时间，降低更新优先级</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> deferredValue = useDeferredValue(value, &#123; <span class="hljs-attr">timeoutMs</span>: <span class="hljs-number">3000</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><br>
<em>文章可能有些理解错误，请指正</em></p>
<p><a href="https://github.com/reactwg/react-18/discussions" target="_blank" rel="nofollow noopener noreferrer">React 18 所有更新讨论列表</a></p></div>  
</div>
            