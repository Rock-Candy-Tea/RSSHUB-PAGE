
---
title: '掀开React 18的盖头，从入门到熟悉！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ead65e7a8824df4af1dc4450f52fda9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 18:38:51 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ead65e7a8824df4af1dc4450f52fda9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文从<code>React 18</code>的核心概念、新功能、更新、新api和hooks4个方面展开和讲解，从而全面揭开React 18的神秘面纱，帮助你快速上手和使用。</p>
<h2 data-id="heading-0">如何升级到React 18</h2>
<ol>
<li>通过<code>npm</code>、<code>yarn</code>或者<code>pnpm</code>安装 React 18和 React Dom</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 三种方式任取一种</span>
<span class="hljs-comment">// 使用npm</span>
npm install react react-dom
<span class="hljs-comment">// 使用yarn</span>
yarn add react react-dom
<span class="hljs-comment">// 使用pnpm </span>
pnpm install react react-dom
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用<code>createRoot</code>替代之前的<code>render</code>
在<code>index.tsx</code>或者<code>index.js</code>文件单重，用<code>ReactDom.createRoot</code>创建root节点渲染的方式来替换之前<code>ReactDom.render</code>的形式。</li>
</ol>
<ul>
<li>react 17版及以前</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-title class_">ReactDOM</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'root'</span>);

<span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, container);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>react 18版及以后</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-title class_">ReactDOM</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'root'</span>);

<span class="hljs-comment">// 创建root</span>
<span class="hljs-keyword">const</span> root = <span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">createRoot</span>(container);

<span class="hljs-comment">//通过root渲染App</span>
root.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">核心概念：Concurrency（并发）</h2>
<p>React的并发到底做了什么，使性能得到了提升，下面提供了一个新旧版本的示例（<code>顶部是个slider，拖放后会对整个chart区域缩放</code>）进行对比：</p>
<h3 data-id="heading-2"><strong>非</strong>并发模式进行以下操作：</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ead65e7a8824df4af1dc4450f52fda9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="stack-reconciler.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>火焰图调用信息如下</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50e5af8444614dbaa557a8e401f2ef5f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3"><strong>并发模式</strong>进行同样的操作：</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f818f65116943798e49458b62105973~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="fiber-reconciler.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>火焰图调用信息如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01bc893b718d497882e4f399b670e156~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过对比，可以很明显的感受到<strong>该场景下</strong>并发模式下的流畅性。</p>
<p>在<code>React 18</code>之前，渲染是一个单一的、不间断的、同步的事务，一旦渲染开始，就不能被打断。这是因为早期采用的是“stack reconciler"调度（类似串行调度），stack reconciler采用递归的方式创建虚拟DOM并提交Dom Mutation，整个过程同步并且<strong>无法中断工作或进行拆分</strong>。如果组件树的层级很深，递归会占用线程很多时间，递归更新时间超过了16ms，用户交互就会卡顿。</p>
<p><code>React 18</code>是并发渲染，并发是React渲染机制的一个基础性更新，React可以进行任务挂起（暂停）、恢复、中止、插入高优任务。这使得React可以快速响应用户的交互，即使它正处于一个繁重的渲染任务中。</p>
<p>并发是React渲染机制的一个基础性更新，suspense、流式服务器渲染和transitions等新功能都是由并发渲染提供的。</p>
<h2 data-id="heading-4">更新： Strict mode（严格模式）</h2>
<p><code>React 18</code>中的Strict mode将模拟mounting（挂载）、unmounting（卸载）和用以前的状态re-mounting(重新挂载)组件。这为未来的<strong>状态复用</strong>奠定了基础，在这种情况下，react可以通过使用卸载前的相同组件状态，来实现快速还原之前状态树并反馈到UI上。严格模式将确保组件在被多次挂载和卸载时具有很好的弹性效果。
启用方式也比较简单，将代码包裹在<code>StrictMode</code>组件中即可，在项目升级中可以逐个模块或者组件进行替换升级</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">Root</span> = (<span class="hljs-params"></span>) => &#123;
 ...
 <span class="hljs-keyword">return</span> (
   <!-- <span class="hljs-comment">// 显示调用 --></span>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">StrictMode</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">...</span>/></span>
   <span class="hljs-tag"></<span class="hljs-name">StrictMode</span>></span></span>
 )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，严格模式仅影响<code>开发环境</code>，对生产环境无影响。</p>
<h2 data-id="heading-5">新功能</h2>
<h3 data-id="heading-6">Automatic batching</h3>
<p>batching（批处理）是 React<strong>将多个状态更新分组到单个re-render中</strong>以获得更好的性能的操作。
例如，如果你在同一个点击事件中有两个状态更新，React 总是将它们分批处理到一个重新渲染中。如果你运行下面的代码，你会看到每次点击时，React 只执行一次渲染，尽管你设置了两次状态：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">App</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> [count, setCount] = <span class="hljs-title function_">useState</span>(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [flag, setFlag] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">false</span>);

  <span class="hljs-keyword">function</span> <span class="hljs-title function_">handleClick</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-title function_">setCount</span>(<span class="hljs-function"><span class="hljs-params">c</span> =></span> c + <span class="hljs-number">1</span>); <span class="hljs-comment">// 不会触发重新渲染</span>
    <span class="hljs-title function_">setFlag</span>(<span class="hljs-function"><span class="hljs-params">f</span> =></span> !f); <span class="hljs-comment">// 不会触发重新渲染</span>
    <span class="hljs-comment">// React这里只会触发一次渲染 (这就是batching!)</span>
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>Next<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> <span class="hljs-attr">flag</span> ? "<span class="hljs-attr">blue</span>" <span class="hljs-attr">:</span> "<span class="hljs-attr">black</span>" &#125;&#125;></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这对性能非常有用，因为它避免了不必要的重新渲染。它还可以防止您的组件呈现仅更新一个状态变量的“半完成”状态，这可能会导致错误。这可能会让您想起餐厅服务员在您选择第一道菜时不会跑到厨房，而是等待您完成订单。</p>
<p>但在React 18 之前，只有在<em><strong>React事件处理程序期间</strong></em>才会触发批量更新。默认情况下，React
<strong>不会对</strong><code>promise</code>、<code>setTimeout</code>、<code>原生事件处理（native event handlers）</code>或其它React默认不进行批处理的事件进行批处理操作。</p>
<p>从 React 18的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F5" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/5" ref="nofollow noopener noreferrer"><code>createRoot</code></a>开始，所有更新都将Aumatic Batching（自动批处理），无论它们来自何处。</p>
<p>这意味着promise<code>、</code>setTimeout<code>、</code>原生事件处理（native event handlers）`或任何其他事件内的更新将以与 React 事件内的更新相同的方式进行批处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">App</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> [count, setCount] = <span class="hljs-title function_">useState</span>(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [flag, setFlag] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">false</span>);

  <span class="hljs-keyword">function</span> <span class="hljs-title function_">handleClick</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-title function_">fetchSomething</span>().<span class="hljs-title function_">then</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// React 17 中，setCount和setFlag都会触发一次重新渲染</span>
      <span class="hljs-comment">// React 18 中，只会触发一次渲染，因为进行自动batching的操作</span>
      <span class="hljs-title function_">setCount</span>(<span class="hljs-function"><span class="hljs-params">c</span> =></span> c + <span class="hljs-number">1</span>);
      <span class="hljs-title function_">setFlag</span>(<span class="hljs-function"><span class="hljs-params">f</span> =></span> !f);
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
<ul>
<li>✅ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fmorning-sun-lgz88%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/morning-sun-lgz88?file=/src/index.js" ref="nofollow noopener noreferrer">演示：React 18<code>createRoot</code>在事件处理之外的批处理！</a>（注意控制台中的每次点击渲染一次！）</li>
<li>🟡 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fjolly-benz-hb1zx%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/jolly-benz-hb1zx?file=/src/index.js" ref="nofollow noopener noreferrer">演示：React 18 with legacy<code>render</code>保留了旧的行为</a>（注意控制台中每次点击两次渲染。）</li>
</ul>
<blockquote>
<p>但某些代码可能依赖于在状态更改后立即从 DOM 中读取某些内容。对于这些用例，您可以使用<code>ReactDOM.flushSync()</code>选择退出批处理：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; flushSync &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>; <span class="hljs-comment">// Note: react-dom, not react</span>

<span class="hljs-keyword">function</span> <span class="hljs-title function_">handleClick</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-title function_">flushSync</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-title function_">setCounter</span>(<span class="hljs-function"><span class="hljs-params">c</span> =></span> c + <span class="hljs-number">1</span>);
  &#125;);
  <span class="hljs-comment">// React has updated the DOM by now</span>
  <span class="hljs-title function_">flushSync</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-title function_">setFlag</span>(<span class="hljs-function"><span class="hljs-params">f</span> =></span> !f);
  &#125;);
  <span class="hljs-comment">// React has updated the DOM by now</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React <strong>不建议</strong> 频繁使用此场景。</p>
<h3 data-id="heading-7">Transitions</h3>
<p>React中定义了两种状态更新（<strong>记住，后面返回会提及这个概念</strong>）</p>
<ul>
<li>Urgent updates（紧急更新）:反馈用户的直接行为，比如：输入、点击、按键等等</li>
<li>Transition updates（过度性更新）:用户看到的界面变化，从一个界面变化为另一个界面</li>
</ul>
<p>Transitions是用来标记不需要紧急资源来更新的用户界面更新。例如：当在一个输入框字段中输入时，有两件事情正在发生：</p>
<ol>
<li>一个闪烁的光标显示你正在输入的内容的视觉反馈</li>
<li>一个在后台搜索被输入的数据的搜索功能。</li>
</ol>
<p>向用户显示视觉反馈是重要的，因此也是紧迫的。搜索则不那么紧急，因此可以被标记为非紧急。这些非紧急的更新被称为transitions。通过将非紧急的UI更新标记为 "transitions"，React将知道哪些更新需要优先处理，使其更容易优化渲染并摆脱陈旧的渲染。</p>
<p>更新可以通过使用startTransition来标记为非紧急状态。针对上面的说明，下面是一个实际的示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; startTransition &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-comment">// 紧急: 展示输入了什么</span>
<span class="hljs-title function_">setInputValue</span>(input);

<span class="hljs-comment">// 将不紧急的是状态更新标记为transition</span>
<span class="hljs-title function_">startTransition</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// Transition: 展示搜索结果</span>
  <span class="hljs-title function_">setSearchQuery</span>(input);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个看起来跟debounce或者是延迟（setTimeout之类的）很相似，两者有什么区别呢？</p>
<ul>
<li>执行时机： startTransition与setTimeout不同，会立即执行。setTimeout有一个保证的延迟，而startTransition的延迟取决于设备的速度，以及其他紧急渲染的情况。</li>
<li>可控制： startTransition的更新可以被打断，不像setTimeout那样，不会冻结页面。当用startTransition标记时，React可以跟踪并暴露出pending状态来使用户感知。</li>
</ul>
<h2 data-id="heading-8">新apis</h2>
<h3 data-id="heading-9">createRoot</h3>
<p>React中，<code>Root</code>是顶层的数据结构，它是一个<code>tree</code>，用来追踪React渲染。在以前的API当中，<code>Root</code>对用户并不是透明的，React直接把它绑定到Dom Element上，可以通过Dom节点访问到Root，并没有通过API的形式暴露出来</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> <span class="hljs-title class_">ReactDOM</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> rootElement = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'root'</span>);

<span class="hljs-comment">// 首次渲染</span>
<span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>, 通过rootElement);

<span class="hljs-comment">// 更新：需要再次传递container</span>
<span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"profile"</span> /></span></span>, 通过rootElement);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4ecccf4678f491b937e1c5d1a06c995~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="通过rootElement._reactRootContainer查看" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在新API中，我们可以直接通过root来进行渲染</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> <span class="hljs-title class_">ReactDOMClient</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom/client'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> rootElement = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'app'</span>);

<span class="hljs-comment">// 创建一个root</span>
<span class="hljs-keyword">const</span> root = <span class="hljs-title class_">ReactDOMClient</span>.<span class="hljs-title function_">createRoot</span>(rootElement);

<span class="hljs-comment">// 首次渲染: 通过root渲染一个元素.</span>
root.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>);

<span class="hljs-comment">// 更新：不需要再次传递container</span>
root.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"profile"</span> /></span></span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">两者有什么区别？</h4>
<p>官方给出了两个说法:</p>
<ul>
<li>修复了一些之前更新过程中不合符ergonomics（工程学）的问题。并且避免了频繁传入container的问题（哪怕没有任何修改）。</li>
<li>移除了<code>hydrate</code>并使用可以传入参数的root方法替换。并且移除了render callback函数。</li>
</ul>
<h4 data-id="heading-11">render callback如何处理</h4>
<p>我们都知道在以前的API中，我们可以传入一个回调函数，在组件render或者更新后会触发。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> container = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'app'</span>);

<span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">render</span>(container, <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>, <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-comment">// 首次渲染或者任何更新时触发.</span>
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'rendered'</span>).
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新API中移除了<code>callback</code>，原因是在部分hydration和渐进式SSR渲染的过程中，回调的触发时机跟用户期望的方式不一致，现在官方推荐使用以下两种形式。</p>
<ul>
<li>用异步回调：通过<code>requestIdleCallback</code>, <code>setTimeout</code></li>
<li>显示传入callback，在组件中直接调用
<ul>
<li>通过<code>ref</code>：当<code>div</code>添加到DOM中（一般是DOM Mutation完成的时），会<strong>同步触发</strong></li>
<li>通用<code>useEffect</code>：延时触发，在commit阶段完成后（页面渲染完成时）</li>
</ul>
</li>
</ul>
<p>用法需要根据具体的业务场景来进行选择。贴一下<code>ref</code>的代码示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">App</span>(<span class="hljs-params">&#123; callback &#125;</span>) &#123;
  <span class="hljs-comment">// Callback will be called when the div is first created.</span>
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;callback&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
root.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">callback</span>=<span class="hljs-string">&#123;()</span> =></span> console.log("renderered")&#125; /></span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">hydrateRoot</h3>
<p>早期的<code>hydrate</code>升级为了<code>hydrateRoot</code>。
以前：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> <span class="hljs-title class_">ReactDOM</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'app'</span>);

<span class="hljs-comment">// 通过hydration 渲染一个root节点</span>
<span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">hydrate</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>, container);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> <span class="hljs-title class_">ReactDOMClient</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom/client'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'App'</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'app'</span>);

<span class="hljs-comment">// 通过hydration**创建** 和 **渲染**一个root节点</span>
<span class="hljs-keyword">const</span> root = <span class="hljs-title class_">ReactDOMClient</span>.<span class="hljs-title function_">hydrateRoot</span>(container, <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>);
<span class="hljs-comment">// 不像createRoot，这里不需要再次单独调用root.render </span>

<span class="hljs-comment">// 如果在hydration后想要再次更新root节点，可以直接调用render方法</span>
root.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"profile"</span> /></span></span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意一点，和<code>createRoot不同</code>,<strong><code>hydrateRoot</code>接入初始化的jsx作为第二个参数</strong>，这是 因为初次的服务端渲染需要匹配对应渲染tree。</p>
<h2 data-id="heading-13">新hooks</h2>
<h3 data-id="heading-14">useId</h3>
<p><code>useId</code>是一个生成全局唯一id的hooks，它可以用在client和service端，从而可以避免水化过程中的不匹配，下面是一个简单的示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">CheckBox</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> id = <span class="hljs-title function_">useId</span>();
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">htmlFor</span>=<span class="hljs-string">&#123;id&#125;</span>></span>Do you like React?<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"react"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">&#123;id&#125;</span> /></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的实现也不复杂，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fpull%2F22644%2Ffiles%23diff-d0d3346ffbaafc7b47ed46f19ccdd179480fa697033bed903c60d8455a9ce8bbR2154-R2157" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/pull/22644/files#diff-d0d3346ffbaafc7b47ed46f19ccdd179480fa697033bed903c60d8455a9ce8bbR2154-R2157" ref="nofollow noopener noreferrer">源码</a>中的核心实现，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Used for ids that are generated completely client-side (i.e. not during</span>
<span class="hljs-comment">// hydration). This counter is global, so client ids are not stable across</span>
<span class="hljs-comment">// render attempts.</span>
<span class="hljs-keyword">let</span> <span class="hljs-attr">globalClientIdCounter</span>: number = <span class="hljs-number">0</span>;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">mountId</span>(<span class="hljs-params"></span>): string &#123;
  <span class="hljs-keyword">const</span> hook = <span class="hljs-title function_">mountWorkInProgressHook</span>();

  <span class="hljs-keyword">let</span> id;
  <span class="hljs-keyword">if</span> (<span class="hljs-title function_">getIsHydrating</span>()) &#123;
    <span class="hljs-keyword">const</span> treeId = <span class="hljs-title function_">getTreeId</span>();

    <span class="hljs-comment">// Use a captial R prefix for server-generated ids.</span>
    id = <span class="hljs-string">'R:'</span> + treeId;

    <span class="hljs-comment">// Unless this is the first id at this level, append a number at the end</span>
    <span class="hljs-comment">// that represents the position of this useId hook among all the useId</span>
    <span class="hljs-comment">// hooks for this fiber.</span>
    <span class="hljs-keyword">const</span> localId = localIdCounter++;
    <span class="hljs-keyword">if</span> (localId > <span class="hljs-number">0</span>) &#123;
      id += <span class="hljs-string">':'</span> + localId.<span class="hljs-title function_">toString</span>(<span class="hljs-number">32</span>);
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// Use a lowercase r prefix for client-generated ids.</span>
    <span class="hljs-keyword">const</span> globalClientId = globalClientIdCounter++;
    id = <span class="hljs-string">'r:'</span> + globalClientId.<span class="hljs-title function_">toString</span>(<span class="hljs-number">32</span>);
  &#125;

  hook.<span class="hljs-property">memoizedState</span> = id;
  <span class="hljs-keyword">return</span> id;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>客户端：一个全局计数器<code>globalClientIdCounter</code>，每次调用加+1后拼接<code>r</code>再转化成32进制输出返回。</li>
<li>服务端：稍微复杂一些，会基于<code>treeId</code> + <code>localIdCounter + 1</code>，然后再拼接转化32进制输出，这是因为React 18升级后流式渲染是无序的，所以早期单纯计数的方案可能会有问题。</li>
</ul>
<h3 data-id="heading-15">useTransition</h3>
<p>搭配<code>startTransition</code>来使用，如果用户需要在UI上感知到transition，react提供了一个hooks<code>useTransition</code>来获取transition的状态。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useTransition &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">const</span> [isPending, startTransition] = <span class="hljs-title function_">useTransition</span>();
<span class="hljs-comment">// 如果pending了，返回一个指示器</span>
 <span class="hljs-keyword">if</span> (isPending) &#123;
   <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Spinner</span> /></span></span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">useDeferredValue</h3>
<p><code>deferring（延迟）</code>一个值，跟我们经常提到的debounce和throttle有点类似。在React 18中，当传递给<code>useDeferredValue</code>的值发生变化时，React会根据当前<strong>渲染的优先级</strong>来返回之前的值或者是最新的值。</p>
<p>我们可以将<code>useDeferredValue</code>看成两次渲染调度：</p>
<ol>
<li>之前值的Urgent render(紧急渲染)</li>
<li>下一个值的Non-urgent render(非紧急渲染)，跟<code>startTransition</code>类似。</li>
</ol>
<p><code>useDeferredValue</code>和<code>startTransition</code>从广义上来说有着相似的行为，他们主要的区别是使用场景：</p>
<ul>
<li><code>startTransition</code>：当一个事件处理器中需要触发更新（比如：setState）时使用</li>
<li><code>useDeferredValue</code>： 当从父组件或者其它hook当中获取一个新的值。</li>
</ul>
<blockquote>
<p>useDeferredValue 仅延迟您传递给它的值。如果您想防止子组件在紧急更新期间重新渲染，您还必须使用 memo 或 useMemo 存储该组件，如下代码所示</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">Typeahead</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> query = <span class="hljs-title function_">useSearchQuery</span>(<span class="hljs-string">''</span>);
  <span class="hljs-keyword">const</span> deferredQuery = <span class="hljs-title function_">useDeferredValue</span>(query);

  <span class="hljs-comment">// Memoizing 告诉 React 只在 deferredQuery 改变时重新渲染——而不是当查询改变时.</span>
  <span class="hljs-keyword">const</span> suggestions = <span class="hljs-title function_">useMemo</span>(<span class="hljs-function">() =></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">SearchSuggestions</span> <span class="hljs-attr">query</span>=<span class="hljs-string">&#123;deferredQuery&#125;</span> /></span></span>,
    [deferredQuery]
  );

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">SearchInput</span> <span class="hljs-attr">query</span>=<span class="hljs-string">&#123;query&#125;</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">"Loading results..."</span>></span>
        &#123;suggestions&#125;
      <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式不是 <code>useDeferredValue</code>独有的，它与使用类似hooks（如 useThrottleValue 或 useDebouncedValue）的模式相同。</p>
<h3 data-id="heading-17">useSyncExternalStore</h3>
<p>推荐用于从外部数据源读取和订阅的场景，其方式与水化和时间切片等并发渲染功能兼容。</p>
<p>该方法返回存储的值，并接受三个参数。</p>
<ul>
<li>subscribe：注册一个回调的函数，每当store发生变化时就会调用。</li>
<li>getSnapshot：函数，返回store的当前值。</li>
<li>getServerSnapshot：返回服务器渲染时使用的快照的函数。</li>
</ul>
<p>最基本的例子只是简单地订阅了整个store。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> state = <span class="hljs-title function_">useSyncExternalStore</span>(store.<span class="hljs-property">subscribe</span>, store.<span class="hljs-property">getSnapshot</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">useInsertionEffect</h3>
<p>和<code>useEffect</code>的签名，但是它在所有的DOM mutation <strong>之前</strong> 触发。使用这个方法可以在<code>useLayoutEffect</code>中读取布局之前将样式注入到DOM中。由于使用场景优先，这个hook中不能使用ref也不能触发更新。</p>
<blockquote>
<p><code>useInsertionEffect</code> 只建议一些css-in-js的代码库作者使用。推荐使用<code>useEffect</code>或者<code>useLayoutEffect</code>来代替。</p>
</blockquote>
<h2 data-id="heading-19">废弃/不推荐</h2>
<h3 data-id="heading-20">ReactDOM.render</h3>
<p>这个是现在最常用的渲染React节点的方法，前面讲过了，这里不再展开了，后面也逐渐会废弃。</p>
<h3 data-id="heading-21">renderToString</h3>
<p>将一个 React 元素渲染成其初始的 HTML。此 API 对 Suspense 支持有限，并且不支持流。后面也逐渐会废弃。
在服务端，建议使用 <code>renderToPipeableStream</code> (Node.js) 或者 <code>renderToReadableStream</code> (for Web Streams) 代替。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ceb34890e2ba46fc95174cc4302596c6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="有收获的小伙伴麻烦来个三连暴击！" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-22">参考文章</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F21" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/21" ref="nofollow noopener noreferrer">Automatic batching for fewer renders in React 18</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F41" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/41" ref="nofollow noopener noreferrer">New feature: startTransition</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F112" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/112" ref="nofollow noopener noreferrer">React 18 is now in beta</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F5" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/5" ref="nofollow noopener noreferrer">Replacing render with createRoot</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F111" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/111" ref="nofollow noopener noreferrer">Intent to Ship: useId</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F19" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/19" ref="nofollow noopener noreferrer">Adding Reusable State to StrictMode</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F129" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/129" ref="nofollow noopener noreferrer">useDeferredValue</a></li>
</ul></div>  
</div>
            