
---
title: '介绍 Preact Signals'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d95ce989e9bb433992599bd160f7c607~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 07:38:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d95ce989e9bb433992599bd160f7c607~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 什么是 Signals？</h2>
<p>Signals 是用来处理状态的一种方式，它参考自 SolidJS，吸收了其大部分的优点。无论应用多么复杂，它都能保证快速响应。</p>
<p>Signals 的独特之处在于状态更改会以最有效的方式来自动更新组件和 UI。</p>
<p>Signals 基于自动状态绑定和依赖跟踪提供了出色的工效，并具有针对虚拟 DOM 优化的独特实现。</p>
<h2 data-id="heading-1">2. 为什么是 Signals？</h2>
<h3 data-id="heading-2">2.1 状态管理的困境</h3>
<p>随着应用越来越复杂，项目中的组件也会越来越多，需要管理的状态也越来越多。</p>
<p>为了实现组件状态共享，一般需要将状态提升到组件的共同的祖先组件里面，通过 <code>props</code> 往下传递，带来的问题就是更新时会导致所有子组件跟着更新，需要配合 <code>memo</code> 和 <code>useMemo</code> 来优化性能。</p>
<p>虽然这听起来还挺合理，但随着项目代码的增加，我们很难确定这些优化应该放到哪里。</p>
<p>即使添加了 <code>memoization</code>，也常常因为依赖值不稳定变得无效，由于 Hooks 没有可以用于分析的显式依赖关系树，所以也没法使用工具来找到原因。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d95ce989e9bb433992599bd160f7c607~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另一种解决方案就是放到 <code>Context</code> 上面，子组件作为消费者自行通过 <code>useContext</code> 来获取需要的状态。</p>
<p>但是有一个问题，只有传给 Provider 的值才能被更新，而且只能作为一个整体来更新，无法做到细粒度的更新。</p>
<p>为了处理这个问题，只能将 <code>Context</code> 进行拆分，业务逻辑又不可避免地会依赖多个 <code>Context</code>，这样就会出现 <code>Context</code> 套娃现象。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1360346ab5c14f439a7f953542f0511f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.2 通向未来的 Signals</h3>
<p>看到这里你一定感觉似曾相识，没错，通往未来的解决方案一定是我 —— Recoil，不对，这次的主角是 Signals。</p>
<p>signal 的核心是一个通过 <code>value</code> 属性 来保存值的对象。它有一个重要特征，那就是 signal 对象的值可以改变，但 signal 本身始终保持不变。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; signal &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@preact/signals"</span>;

<span class="hljs-keyword">const</span> count = <span class="hljs-title function_">signal</span>(<span class="hljs-number">0</span>);

<span class="hljs-comment">// Read a signal’s value by accessing .value:</span>
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(count.<span class="hljs-property">value</span>);   <span class="hljs-comment">// 0</span>

<span class="hljs-comment">// Update a signal’s value:</span>
count.<span class="hljs-property">value</span> += <span class="hljs-number">1</span>;

<span class="hljs-comment">// The signal's value has changed:</span>
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(count.<span class="hljs-property">value</span>);  <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Preact 中，当 signal 作为 props 或 context 向下传递时，传递的是对 signal 的引用。这样就可以在不重新渲染组件的情况下更新 signal，因为传给组件的是 signal 对象而不是它的值。</p>
<p>这让我们可以跳过所有昂贵的渲染工作，立即跳到任意访问 signal <code>.value</code> 属性的组件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/855ec40d699740869374880723a6cdea~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里有 VDOM 和 Signals 在 Chrome 里面更新时的火焰图对比，可以发现 Signals 非常快。相比组件树更新，Signals 渲染会更快一些，这是因为更新状态图所需的工作要少得多。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1735054a19347e090511e175cf4774f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Signals 具有第二个重要特征，即它们会跟踪其值何时被访问以及何时被更新。在 Preact 中，当 signal 的值发生变化时，从组件内访问 signal 的属性会自动重新渲染组件。</p>
<h3 data-id="heading-4">2.3 栗子</h3>
<p>我们可以用一个例子来理解 Signals 的独特之处：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; signal &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@preact/signals"</span>;

<span class="hljs-keyword">const</span> count = <span class="hljs-title function_">signal</span>(<span class="hljs-number">0</span>);

<span class="hljs-keyword">const</span> <span class="hljs-title function_">App</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Fragment</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> count.value++;&#125;>
        +
        &#123;console.log("++")&#125;
      <span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Fragment</span>></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们点击10次加号之后，count会从0变成10，那么"++"是否会被打印10次呢？</p>
<p>从我们平时写 React 组件的经验来说，肯定会被打印10次，但在 Signals 里面不是这样。</p>
<p>从这个 Gif 可以看到，"++"一次都没被打印出来，这就是 Signals 的独特之处，整个组件没有被重新渲染。</p>
<p>不仅 h1 没有重新渲染，甚至连 span 节点都没有重新渲染，唯一更新的地方就只有 <code>&#123;count&#125;</code> 这个文本节点。 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0579559c637343cfa71a10db95b30820~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>❝</p>
<p>💡 提示：Signal 只有在设置新的值才会更新。如果设置的值没有发生变化，就不会触发更新。</p>
<p>❞</p>
</blockquote>
<p>除了文本节点，Signals 还能做到对 DOM 属性的细粒度更新。当点击加号的时候，只有 <code>data-id</code> 被更新了，甚至连 <code>span</code> 里面的 <code>random</code> 都没有被执行。</p>
<pre><code class="hljs language-ini copyable" lang="ini">const <span class="hljs-attr">count</span> = signal(<span class="hljs-number">0</span>)<span class="hljs-comment">;</span>

const <span class="hljs-attr">App</span> = () => &#123;
  return (
    <Fragment>
      <h1 <span class="hljs-attr">onClick</span>=&#123;() => count.value++<span class="hljs-comment">;&#125;></span>
        +
        &#123;console.log("++")<span class="hljs-comment">;&#125;</span>
      </h1>
      <span <span class="hljs-attr">data-id</span>=&#123;count&#125;>&#123;Math.random()&#125;</span>
    </Fragment>
  )<span class="hljs-comment">;</span>
&#125;<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3. 安装</h2>
<p>可以通过将 <code>@preact/signals</code> 包添加到项目中来安装 Signals：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install @preact/signals
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4. 用法</h2>
<p>我们接下来将会写一个 TodoList 的 Demo 来学习 Signals。</p>
<h3 data-id="heading-7">4.1 创建状态</h3>
<p>首先需要一个包含待办事项列表的 signal，可以用数组来表示：</p>
<pre><code class="hljs language-arduino copyable" lang="arduino"><span class="hljs-keyword">import</span> &#123; signal &#125; from <span class="hljs-string">"@preact/signals"</span>;

<span class="hljs-type">const</span> todos = <span class="hljs-built_in">signal</span>([
  &#123; text: <span class="hljs-string">"Buy groceries"</span> &#125;,
  &#123; text: <span class="hljs-string">"Walk the dog"</span> &#125;,
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，需要允许用户编辑输入框、创建新的 Todo 事项，所以还要创建输入值的 signal，然后直接设置 <code>.value</code> 来实现修改。</p>
<pre><code class="hljs language-ini copyable" lang="ini">// We'll use this for our input later
const <span class="hljs-attr">text</span> = signal(<span class="hljs-string">""</span>)<span class="hljs-comment">;</span>

function addTodo() &#123;
  <span class="hljs-attr">todos.value</span> = [...todos.value, &#123; text: text.value &#125;]<span class="hljs-comment">;</span>
  <span class="hljs-attr">text.value</span> = <span class="hljs-string">""</span><span class="hljs-comment">; // Clear input value on add</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们要添加的最后一个功能是从列表中删除待办事项。为此，我们将添加一个从 todos 数组中删除给定 todo 项的函数：</p>
<pre><code class="hljs language-ini copyable" lang="ini">function removeTodo(todo) &#123;
  <span class="hljs-attr">todos.value</span> = todos.value.filter(t => t !== todo)<span class="hljs-comment">;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">4.2 构建用户界面</h3>
<p>现在我们创建了所有的状态，接下来需要编写用户界面，这里使用了 Preact。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">function</span> <span class="hljs-title function_">TodoList</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">onInput</span> = event => (text.<span class="hljs-property">value</span> = event.<span class="hljs-property">target</span>.<span class="hljs-property">value</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;text.value&#125;</span> <span class="hljs-attr">onInput</span>=<span class="hljs-string">&#123;onInput&#125;</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;addTodo&#125;</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        &#123;todos.value.map(todo => (
          <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
            &#123;todo.text&#125;&#123;' '&#125;
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> removeTodo(todo)&#125;>❌<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        ))&#125;
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，一个完整的 TodoList 就已经完成了，你可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpreactjs.com%2Frepl%3Fexample%3Dtodo-list-signals" target="_blank" rel="nofollow noopener noreferrer" title="https://preactjs.com/repl?example=todo-list-signals" ref="nofollow noopener noreferrer">在这里</a>体验完整的功能。</p>
<h3 data-id="heading-9">4.3 衍生状态</h3>
<p>在 TodoList 里面有一个常见的场景，那就是展示已完成事项数量，这个要怎么去设计状态呢？</p>
<p>相信你的第一反应肯定是 Mobx 或者 Vue 的衍生状态，刚好在 Signals 里面也有。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; signal, computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@preact/signals"</span>;

<span class="hljs-keyword">const</span> todos = <span class="hljs-title function_">signal</span>([
  &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"Buy groceries"</span>, <span class="hljs-attr">completed</span>: <span class="hljs-literal">true</span> &#125;,
  &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"Walk the dog"</span>, <span class="hljs-attr">completed</span>: <span class="hljs-literal">false</span> &#125;,
]);

<span class="hljs-comment">// 基于其他 signals 创建衍生 signal</span>
<span class="hljs-keyword">const</span> completed = <span class="hljs-title function_">computed</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 当 todos 变化，这里会自动重新计算</span>
  <span class="hljs-keyword">return</span> todos.<span class="hljs-property">value</span>.<span class="hljs-title function_">filter</span>(<span class="hljs-function"><span class="hljs-params">todo</span> =></span> todo.<span class="hljs-property">completed</span>).<span class="hljs-property">length</span>;
&#125;);

<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(completed.<span class="hljs-property">value</span>); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">4.4 管理全局状态</h3>
<p>到目前为止，我们都是在组件树之外创建了 <code>signal</code>，对于小型应用来说没什么问题，但对于大型复杂应用来说，测试会比较困难。</p>
<p>因此，我们可以将 <code>signal</code> 提升至最外层组件里面，通过 <code>Context</code> 进行传递。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"preact"</span>;
<span class="hljs-keyword">import</span> &#123; useContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"preact/hooks"</span>;

<span class="hljs-comment">// 创建 App 状态</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">createAppState</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> todos = <span class="hljs-title function_">signal</span>([]);

  <span class="hljs-keyword">const</span> completed = <span class="hljs-title function_">computed</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> todos.<span class="hljs-property">value</span>.<span class="hljs-title function_">filter</span>(<span class="hljs-function"><span class="hljs-params">todo</span> =></span> todo.<span class="hljs-property">completed</span>).<span class="hljs-property">length</span>
  &#125;);

  <span class="hljs-keyword">return</span> &#123; todos, completed &#125;
&#125;

<span class="hljs-keyword">const</span> <span class="hljs-title class_">AppState</span> = <span class="hljs-title function_">createContext</span>();

<span class="hljs-comment">// 通过 Context 传递给子组件</span>
<span class="hljs-title function_">render</span>(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">AppState.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;createAppState()&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">AppState.Provider</span>></span></span>
);

<span class="hljs-comment">// 子组件接收后使用</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">App</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> state = <span class="hljs-title function_">useContext</span>(<span class="hljs-title class_">AppState</span>);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;state.completed&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">4.5 管理局部状态</h3>
<p>除了直接通过 <code>signals</code> 来创建状态，我们也可以使用提供的 hooks 来创建组件内部状态。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; useSignal, useComputed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@preact/signals"</span>;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">Counter</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> count = <span class="hljs-title function_">useSignal</span>(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> double = <span class="hljs-title function_">useComputed</span>(<span class="hljs-function">() =></span> count.<span class="hljs-property">value</span> * <span class="hljs-number">2</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;count&#125; x 2 = &#123;double&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> count.value++&#125;>click me<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useSignal</code> 的实现是基于 <code>signal</code> 的，原理比较简单，利用了 <code>useMemo</code> 来对 <code>signal</code> 进行缓存，避免更新时重新创建了新的 <code>signal</code>。</p>
<pre><code class="hljs language-scss copyable" lang="scss">function <span class="hljs-built_in">useSignal</span>(value) &#123;
    return <span class="hljs-built_in">useMemo</span>(() => <span class="hljs-built_in">signal</span>(value), <span class="hljs-selector-attr">[]</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4.6 订阅变化</h3>
<p>从前面的例子里面可以注意到，在组件外访问 <code>signal</code> 的时候，都是直接读取它的值，并不涉及到响应值的变化。</p>
<p>在 Mobx 里面提供了 <code>autoRun</code> 来订阅值的变化，<code>signal</code> 里面提供了 <code>effect</code> 方法来订阅。</p>
<p><code>effect</code> 接收一个回调函数作为参数，当回调函数中依赖的 <code>signal</code> 值发生了变化，这个回调函数也会被重新执行</p>
<pre><code class="hljs language-ini copyable" lang="ini">import &#123; signal, computed, effect &#125; from "@preact/signals-core"<span class="hljs-comment">;</span>

const <span class="hljs-attr">name</span> = signal(<span class="hljs-string">"Jane"</span>)<span class="hljs-comment">;</span>
const <span class="hljs-attr">surname</span> = signal(<span class="hljs-string">"Doe"</span>)<span class="hljs-comment">;</span>
const <span class="hljs-attr">fullName</span> = computed(() => `<span class="hljs-variable">$&#123;name.value&#125;</span> <span class="hljs-variable">$&#123;surname.value&#125;</span>`)<span class="hljs-comment">;</span>

// 每次名字变化的时候就打印出来
effect(() => console.log(fullName.value))<span class="hljs-comment">; // 打印: "Jane Doe"</span>

// 更新 name 的值
<span class="hljs-attr">name.value</span> = <span class="hljs-string">"John"</span><span class="hljs-comment">;</span>
// 触发自动打印: "John Doe"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>effect</code> 执行后会返回一个新的函数，用于取消订阅。</p>
<pre><code class="hljs language-ini copyable" lang="ini">
const <span class="hljs-attr">name</span> = signal(<span class="hljs-string">"Jane"</span>)<span class="hljs-comment">;</span>
const <span class="hljs-attr">surname</span> = signal(<span class="hljs-string">"Doe"</span>)<span class="hljs-comment">;</span>
const <span class="hljs-attr">fullName</span> = computed(() => name.value + <span class="hljs-string">" "</span> + surname.value)<span class="hljs-comment">;</span>

const <span class="hljs-attr">dispose</span> = effect(() => console.log(fullName.value))<span class="hljs-comment">;</span>

// 取消订阅
dispose()<span class="hljs-comment">;</span>

// 更新 name，会触发 fullName 的更新，但不会触发 effect 回调执行了
<span class="hljs-attr">name.value</span> = <span class="hljs-string">"John"</span><span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在极少情况下，你可能需要在 <code>effect(fn)</code> 里面更新 <code>signal</code>，但又不希望在 <code>signal</code> 更新时重新运行，所以可以使用 <code>.peek()</code> 来获取 <code>signal</code> 但不订阅。</p>
<pre><code class="hljs language-ini copyable" lang="ini">const <span class="hljs-attr">delta</span> = signal(<span class="hljs-number">0</span>)<span class="hljs-comment">;</span>
const <span class="hljs-attr">count</span> = signal(<span class="hljs-number">0</span>)<span class="hljs-comment">;</span>

effect(() => &#123;
  // 更新 count 但不订阅变化
  <span class="hljs-attr">count.value</span> = count.peek() + delta.value<span class="hljs-comment">;</span>
&#125;)<span class="hljs-comment">;</span>

<span class="hljs-attr">delta.value</span> = <span class="hljs-number">1</span><span class="hljs-comment">;</span>

// 不会触发 effect 回调函数重新执行
<span class="hljs-attr">count.value</span> = <span class="hljs-number">10</span><span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">4.7 批量更新</h3>
<p>有时候我们可能会同时有多个更新，但又不希望触发多次更新，所以需要像 React 的 setState 一样合并更新。</p>
<p>Signals 提供了 <code>batch</code> 方法允许我们对 <code>signal</code> 进行批量更新。</p>
<p>以我们创建待办事项、清空输入框为例：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-built_in">effect</span>(() => console<span class="hljs-selector-class">.log</span>(todos.length, text.value););

function <span class="hljs-built_in">addTodo</span>() &#123;
  <span class="hljs-built_in">batch</span>(() => &#123;
    <span class="hljs-comment">// effect 里面只会执行一次</span>
    todos<span class="hljs-selector-class">.value</span> = <span class="hljs-selector-attr">[...todos.value, &#123; text: text.value &#125;]</span>;
    text<span class="hljs-selector-class">.value</span> = "";
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">5. 总结</h2>
<p>Signals 是 Preact 最近新出的特性，目前还不稳定，不建议在生产环境使用，如果想尝试，可以考虑在小型项目中使用。</p>
<p>下一篇文章将会从介绍 Signals 的实现原理，也会带领大家从零开始实现一个 Signals。</p>
<h2 data-id="heading-15">推荐阅读</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpreactjs.com%2Fblog%2Fintroducing-signals%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://preactjs.com/blog/introducing-signals/" ref="nofollow noopener noreferrer">Introducing Signals</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpreactjs.com%2Fguide%2Fv10%2Fsignals%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://preactjs.com/guide/v10/signals/" ref="nofollow noopener noreferrer">Signals</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.solidjs.cn%2Fguides%2Fgetting-started" target="_blank" rel="nofollow noopener noreferrer" title="https://www.solidjs.cn/guides/getting-started" ref="nofollow noopener noreferrer">使用 Solid</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F394106764" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/394106764" ref="nofollow noopener noreferrer">各流派 React 状态管理对比和原理实现</a></li>
</ol></div>  
</div>
            