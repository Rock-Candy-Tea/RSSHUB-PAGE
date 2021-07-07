
---
title: '面向具有 React 开发经验的开发者介绍 Svelte'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5739'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 22:15:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=5739'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://css-tricks.com/svelte-for-the-experienced-react-dev/" target="_blank" rel="nofollow noopener noreferrer">Svelte for the Experienced React Dev</a></li>
<li>原文作者：<a href="https://css-tricks.com/author/adam-rackis/" target="_blank" rel="nofollow noopener noreferrer">Adam Rackis</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/svelte-for-the-experienced-react-dev.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/Tong-H" target="_blank" rel="nofollow noopener noreferrer">没事儿</a></li>
<li>校对者：<a href="https://github.com/liyaxuanliyaxuan" target="_blank" rel="nofollow noopener noreferrer">liyaxuanliyaxuan</a>、<a href="https://github.com/CarlosChenN" target="_blank" rel="nofollow noopener noreferrer">CarlosChenN</a>、<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
</ul>
</blockquote>
<h1 data-id="heading-0">面向具有 React 开发经验的开发者介绍 Svelte</h1>
<p>这篇文章将从富有 React 开发经验的开发者的角度快速的介绍 Sevlte。首先我会做一个概览，然后重点关注 state 管理和 DOM 交互能力等等。我打算把进度加快一点，这样就能覆盖更多的话题。总之，希望能引起你对 Svelte 的兴趣。</p>
<p>关于对 Svelte 的介绍，没有任何博客可以和官方<a href="https://svelte.dev/tutorial/basics" target="_blank" rel="nofollow noopener noreferrer">教程</a>和<a href="https://svelte.dev/docs" target="_blank" rel="nofollow noopener noreferrer">文档</a>相比。</p>
<h2 data-id="heading-1">“Hello, World!” Svelte 风格</h2>
<p>让我们先快速浏览一遍 Svelte 的组件风格</p>
<pre><code class="hljs language-svelte copyable" lang="svelte"><script>
  let number = 0;
</script>

<style>
  h1 &#123;
    color: blue;
  &#125;
</style>

<h1>Value: &#123;number&#125;</h1>

<button on:click=&#123;() => number++&#125;>Increment</button>
<button on:click=&#123;() => number--&#125;>Decrement</button> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个内容被存放在 <code>.svelte</code> 文件中，通过 <a href="https://github.com/sveltejs/rollup-plugin-svelte" target="_blank" rel="nofollow noopener noreferrer">Rollup</a> 或 <a href="https://github.com/sveltejs/svelte-loader" target="_blank" rel="nofollow noopener noreferrer">webpack</a> 插件加工后生成 Svelte 组件。我们可以通过一些小片段了解。</p>
<p>首先，我们添加一个 <code><script></code> 标签存放所有我们需要的 state。</p>
<p>我们也可以添加一个 <code><style></code> 标签存放所有我们需要的 CSS。这些样式 <strong>只作用于这个组件</strong>，所以 <code><h1></code> 元素在<strong>这个</strong> 组件中将会是蓝色的。是的，被限制作用域的样式内置于 Svelte，不需要外部依赖。在 React 中，想要达到这样受限制的样式，你需要使用第三方插件类似 <a href="https://github.com/css-modules/css-modules" target="_blank" rel="nofollow noopener noreferrer">css-modules</a>, <a href="https://styled-components.com/" target="_blank" rel="nofollow noopener noreferrer">styled-components</a>, 或者其他的 (有几十种，甚至上百种选择).</p>
<p>接下来是一些 html 标记，像你预期的，你将需要学习类似 <code>&#123;#if&#125;</code>、<code>&#123;#each&#125;</code> 等 html 捆绑方法。相较于在 React 中，一切皆 JavaScript 的概念而言，这类特殊领域的语言功能可能看上去像是一个退步。但有几件事值得注意，Svelte 允许你在这些捆绑中放入任意的 JavaScript 代码。所以类似下面这类代码是完全有效的。</p>
<pre><code class="hljs language-svelte copyable" lang="svelte">&#123;#if childSubjects?.length&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你之前是使用 Knockout 或者 Ember，但现在使用并且忠于 React，那么这可能会令你感到惊喜。</p>
<p>还有，Svelte 处理组件的方法和 React 完全不同。只要一个组件的状态或者父组件中的任何地方(除非你缓存了)发生了改变，React 会重新运行所有的组件。这可能会导致效率低下，这也是为什么 React 会使用 <code>useCallback</code> 和 <code>useMemo</code> 来防止额外的重新计算数据。</p>
<p>在另一方面，Svelte 会分析你的模板，并且在相关的状态改变时创建目标 DOM 的更新代码。在上面的组件中，Svelte 将会看到 <code>number</code>  在哪里改变，然后在变更完成后添加代码去更新 <code><h1></code>的内容，这表示你不需要担心函数或者对象的缓存。事实上，你甚至不需要担心副作用的依赖列表，我们稍后会讨论这个问题。</p>
<p>但是我们先谈论……</p>
<h2 data-id="heading-2">State 管理</h2>
<p>在 React 中，当我们需要管理 state 的时候，我们使用 <code>useState</code> hook。我们向它提供一个初始值，然后得到一个包含当前值和用于设置新值的函数的元组。看起来可能是这样：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [number, setNumber] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Value: &#123;number&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setNumber(n => n + 1)&#125;>Increment<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setNumber(n => n - 1)&#125;>Decrement<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>setNumber</code>函数可以传递到任何地方，比如子组件等。</p>
<p>这个在 Svelte 中会简单点。我们可以创建一个变量，在需要时更新它。 Svelte 的<a href="https://en.wikipedia.org/wiki/Ahead-of-time_compilation" target="_blank" rel="nofollow noopener noreferrer">提前编译</a>(和 React 即时更新不同)将会追踪变量更新的脚步，然后推动 DOM 更新。和上面一样简单的例子:</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><script>
  <span class="hljs-keyword">let</span> number = <span class="hljs-number">0</span>;
</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Value: &#123;number&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;()</span> =></span> number++&#125;>Increment<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;()</span> =></span> number--&#125;>Decrement<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个需要注意的是，Svelte 不需要 JSX 那样的单独的包裹元素，也没有 React 片段语法 <code><></></code> 的等价物。</p>
<p>但如果我们想要传递一个更新函数给子组件呢？使它能更新这块的状态，就像我们用 React 做的那样，我们可以写一个更新函数：</p>
<pre><code class="hljs language-svelte copyable" lang="svelte"><script>
  import Component3a from "./Component3a.svelte";
        
  let number = 0;
  const setNumber = cb => number = cb(number);
</script>

<h1>Value: &#123;number&#125;</h1>

<button on:click=&#123;() => setNumber(val => val + 1)&#125;>Increment</button>
<button on:click=&#123;() => setNumber(val => val - 1)&#125;>Decrement</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们可以把这个更新函数传递到任何我们需要的地方，或者继续期待一个更自动化的解决方案。</p>
<h3 data-id="heading-3">Reducer 和 store</h3>
<p>React 还有 <code>useReducer</code> hook，让我们可以塑造更复杂的状态。我们提供一个 reducer 函数，然后得到我们当前的值，以及一个 dispatch 函数让我们可以用一个给定的参数去调用 reducer，从而触发一个状态更新，不管 reducer 返回的是什么。我们上面的计数器例子可能看起来会是这样：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React, &#123; useReducer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reducer</span>(<span class="hljs-params">currentValue, action</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (action) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"INC"</span>:
      <span class="hljs-keyword">return</span> currentValue + <span class="hljs-number">1</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"DEC"</span>:
      <span class="hljs-keyword">return</span> currentValue - <span class="hljs-number">1</span>;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [number, dispatch] = useReducer(reducer, <span class="hljs-number">0</span>);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Value: &#123;number&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch("INC")&#125;>Increment<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch("DEC")&#125;>Decrement<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Svelte 没有类似的功能，但是它有一个称为 <strong>store</strong> 的模块。最简单的是 writable store，是持一个值的 object。想要设置一个新值，你可以调用 store 上的 <code>set</code> 方法并传递一个新值，或者调用 update，传入一个回调函数，这个函数接受当前值并且返回新值(和 React 的 <code>useState</code>一样).</p>
<p>在需要时读取 store 的当前值，可以调用<a href="https://svelte.dev/docs#get" target="_blank" rel="nofollow noopener noreferrer"><code>get</code> 函数</a>，它会返回当前值。Store 也有一个 subscribe 函数，我们可以传入一个回调函数，在值改变时被执行。</p>
<p>Svelte 是简洁轻量的，其中有一些不错的语法快捷方式。如果你在一个组件内部，你可以给 store 加一个 $ 前缀用于读取其值，或者通过直接赋值去更新值。这是上面的计数器例子，使用了一个 store，以及一些额外的副作用日志打印用于展示 subscribe 是如何工作的：</p>
<pre><code class="hljs language-svelte copyable" lang="svelte"><script>
  import &#123; writable, derived &#125; from "svelte/store";
        
  let writableStore = writable(0);
  let doubleValue = derived(writableStore, $val => $val * 2);
        
  writableStore.subscribe(val => console.log("current value", val));
  doubleValue.subscribe(val => console.log("double value", val))
</script>

<h1>Value: &#123;$writableStore&#125;</h1>

<!-- manually use update -->
<button on:click=&#123;() => writableStore.update(val => val + 1)&#125;>Increment</button>
<!-- use the $ shortcut -->
<button on:click=&#123;() => $writableStore--&#125;>Decrement</button>

<br />

Double the value is &#123;$doubleValue&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，我在上面添加了一个 <code>derived</code> store。<a href="https://svelte.dev/docs#derived" target="_blank" rel="nofollow noopener noreferrer">文档</a>深入的介绍了这个，但简单来说，<code>derived</code> store 让你可以使用和 writable store 一样的语法，让一个 store (或许多 store) 映射出一个新值。</p>
<p>Svelte 中的 Store 非常灵活。我们可以将多个 store 传递到子组件中，更改、组合它们，甚至通过传递一个 derived store 使它们只读。如果我们要把一些 React 的代码转化为 Svelte，我们甚至可以重建一些你可能喜欢或需要的 React 抽象。</p>
<h3 data-id="heading-4">React API 与 Svelte</h3>
<p>说完这些，让我们回到之前 React 的 <code>useReducer</code> hook 上。</p>
<p>我们的确是真的喜欢通过定义 reducer 函数来维护和更新 state。让我们看看使用 Svelte 的 store 去模仿 React 的 <code>useReducer</code> 会有多难。我们想要调用我们自己的 <code>useReducer</code>，传入一个带有初始值的 reducer 函数，然后得到带有当前值的 store，这和 dispatch 函数调用 reducer 去更新 store 是一样的，完成这个任务实际上不算太糟糕。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useReducer</span>(<span class="hljs-params">reducer, initialState</span>) </span>&#123;
  <span class="hljs-keyword">const</span> state = writable(initialState);
  <span class="hljs-keyword">const</span> dispatch = <span class="hljs-function">(<span class="hljs-params">action</span>) =></span>
    state.update(<span class="hljs-function"><span class="hljs-params">currentState</span> =></span> reducer(currentState, action));
  <span class="hljs-keyword">const</span> readableState = derived(state, <span class="hljs-function">(<span class="hljs-params">$state</span>) =></span> $state);

  <span class="hljs-keyword">return</span> [readableState, dispatch];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Svelte 的用法和 React 几乎是一样的。唯一的区别是我们当前的值是一个 store，而不是一个原始值，所以我们需要加上一个 <code>$</code> 前缀来读取值(或者手动调用 store 上的 <code>get</code> 或 <code>subscribe</code> )。</p>
<pre><code class="hljs language-svelte copyable" lang="svelte"><script>
  import &#123; useReducer &#125; from "./useReducer";
        
  function reducer(currentValue, action) &#123;
    switch (action) &#123;
      case "INC":
        return currentValue + 1;
      case "DEC":
        return currentValue - 1;
    &#125;
  &#125;
  const [number, dispatch] = useReducer(reducer, 0);      
</script>

<h1>Value: &#123;$number&#125;</h1>

<button on:click=&#123;() => dispatch("INC")&#125;>Increment</button>
<button on:click=&#123;() => dispatch("DEC")&#125;>Decrement</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">那么 <code>useState</code> 呢？</h3>
<p>如果你真的喜欢 React 的 <code>useState</code> hook，实现也很简单。实际上，我并没有觉得这是一个很有用的抽象，但这是个有趣的练习，可以展示 Svelte 的灵活性。</p>
<pre><code class="hljs language-svelte copyable" lang="svelte">export function useState(initialState) &#123;
  const state = writable(initialState);
  const update = (val) =>
    state.update(currentState =>
      typeof val === "function" ? val(currentState) : val
    );
  const readableState = derived(state, $state => $state);

  return [readableState, update];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">双向绑定<strong>真的</strong>糟糕吗？</h3>
<p>在结束 state 管理这部分之前，我要提及最后一个对 Svelte 而言比较特殊的技巧。我们已经知道了 Svelte 允许我们使用任何我们能用的 Rect 方法来传递更新函数到组件树。允许子组件通知他们的父组件，state 变化，这是个频繁的操作，我们已经做了几千次。一个子组件改变了 state，然后调用一个父组件传递过来的函数，这样父组件就可以接收 state 改变。</p>
<p>除了支持回调函数的传递，Svelte 也允许父组件与子组件 state 的双向绑定。比如，我们有这样一个组件：</p>
<pre><code class="hljs language-svelte copyable" lang="svelte"><!-- Child.svelte -->
<script>
  export let val = 0;
</script>

<button on:click=&#123;() => val++&#125;>
  Increment
</button>

Child: &#123;val&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子创建一个带有 <code>val</code> 属性的组件。在 Svelte 中，<code>export</code> 关键字用于组件声明 props。通常，我们会把 props 传入到一个组件中，但这里有点不同。比如上面的例子，<code>val</code> prop 被子组件修改了。在 React 中，这是错误的，可能会引发 bug，但在 Svelte 中，渲染这个组件的组件可以做这个。</p>
<pre><code class="hljs language-svelte copyable" lang="svelte"><!-- Parent.svelte -->
<script>
  import Child from "./Child.svelte";
        
  let parentVal;
</script>

<Child bind:val=&#123;parentVal&#125; />
Parent Val: &#123;parentVal&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，在父组件中我们为子组件的 <code>val</code> prop 重新<strong>绑定</strong>了一个变量。如果子组件的 <code>val</code> prop 变化，那么父组件的 <code>parentVal</code> 也会自动被 Svelte 更新。</p>
<p>双向绑定是存在一些争论。如果你不喜欢，那就不要用它。但是少量使用，我认为这会是一个非常方便的工具，可以减少模板。</p>
<h2 data-id="heading-7">Svelte 中的副作用没有分离(或者过时的闭包)</h2>
<p>在 React 中，我们使用 <code>useEffect</code> hook 管理副作用。像这样：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Current value of number"</span>, number);
&#125;, [number]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们写了一个函数，以及依赖列表。每一次渲染，React 都会检查列表中的每一个元素，如果有一个与上一次渲染时不同，那么这个回调函数就会再次运行。如果我们想要在上一次运行后运行一个 cleanup 函数，那么我们可以从 effect 中返回一个 cleanup 函数。</p>
<p>像数字变化这类简单的需求，这很简单。但是任何有经验的 React 开发者都知道，对于非琐碎的使用案例，<code>useEffect</code> 会是个潜在的麻烦。这非常容易，在依赖列表遗漏一些什么从而引发过时的闭包问题。</p>
<p>在 Svelte 中，操作副作用最基础的形式是反应性的声明。看起来像这样。</p>
<pre><code class="hljs language-svelte copyable" lang="svelte">$: &#123;
  console.log("number changed", number);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给一个代码块加上一个前缀 <code>$:</code>，然后放入我们想要执行的代码。Svelte 分析哪个依赖被读，只要它们改变，Svelte 会重新运行这个代码块。没有直接的方法可以在上一次这个反应性代码块运行后去运行 cleanup，如果真的需要可以做一个替代方法，这非常简单。</p>
<pre><code class="hljs language-svelte copyable" lang="svelte">let cleanup;
$: &#123;
  cleanup?.();
  console.log("number changed", number);
  cleanup = () => console.log("cleanup from number change");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这并不会导致无限循环：在一个反应性的代码块内重新赋值不会再引发这个代码块运行。</p>
<p>这是有效的，cleanup effects 通常会用在组件卸载时，Svelte 对此有一个内置功能 <a href="https://svelte.dev/docs#onMount" target="_blank" rel="nofollow noopener noreferrer"><code>onMount</code>函数</a>，使我们可以返回一个 cleanup 函数能够在组件销毁时执行，更直接还有一个<a href="https://svelte.dev/docs#onDestroy" target="_blank" rel="nofollow noopener noreferrer"><code>onDestroy</code>函数</a>，可以做我们想做的事。</p>
<h3 data-id="heading-8">action 来增加一些趣味</h3>
<p>以上的一切都很好用，但 action 才是 Svelte 的最大亮点。副作用频繁的捆绑 DOM 节点。我们可能想在一个 DOM 节点上集成一个老式的(但仍然很不错) jQuery 插件，然后在节点离开 DOM 的时候拆除它；或者我们想为一个节点设置一个 <code>ResizeObserver</code>，然后在节点离开 DOM 的时候分离它，等等。这是非常普通的需求，Svelte 将其内置在 <a href="https://svelte.dev/docs#use_action" target="_blank" rel="nofollow noopener noreferrer">action</a> 中。让我们一起去看看。</p>
<pre><code class="hljs language-svelte copyable" lang="svelte">&#123;#if show&#125;
  <div use:myAction>
    Hello                
  </div>
&#123;/if&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这个语法 <code>use:actionName</code>。这里我们将 <code><div></code> 与一个称作 <code>myAction</code> 的 action 捆绑，这个 action 只是个函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myAction</span>(<span class="hljs-params">node</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Node added"</span>, node);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只要 <code><div></code> 进入 DOM，就会调用这个 action，并且传递这个 DOM 节点给 action。这是一个时机可以去添加 jQuery 插件以及设置 <code>ResizeObserver</code> 等等。不只这样，我们还可以从中返回一个 cleanup 函数，比如这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myAction</span>(<span class="hljs-params">node</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Node added"</span>, node);

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-function"><span class="hljs-title">destroy</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Destroyed"</span>);
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当节点离开 DOM 的时候，<code>destroy()</code> 将会执行，这是我们销毁 jQuery 插件的地方。</p>
<h3 data-id="heading-9">慢着，还有！</h3>
<p>我们还可以传递参数给 action, 像这样：</p>
<pre><code class="hljs language-svelte copyable" lang="svelte"><div use:myAction=&#123;number&#125;>
  Hello                
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个参数将作为 action 函数的第二个参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myAction</span>(<span class="hljs-params">node, param</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Node added"</span>, node, param);

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-function"><span class="hljs-title">destroy</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Destroyed"</span>);
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你想在参数变化时做额外的工作，你可以返回一个 update 函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myAction</span>(<span class="hljs-params">node, param</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Node added"</span>, node, param);

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">param</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Update"</span>, param);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">destroy</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Destroyed"</span>);
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当传递给 action 的参数变化时，update 函数将会运行。向一个 action 传递多个参数，我们可以传递一个 object。</p>
<pre><code class="hljs language-svelte copyable" lang="svelte"><div use:myAction=&#123;&#123;number, otherValue&#125;&#125;>
  Hello                
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只要 object 的属性改变，Svelte 就会再次运行 update 函数。</p>
<p>Actions 是我最喜欢的 Svelte 功能之一，它们非常强大。</p>
<h2 data-id="heading-10">其他</h2>
<p>Svelte 还有很多其他的，React 没有与之相对的功能。还有很多表单捆绑（<a href="https://svelte.dev/tutorial/text-inputs" target="_blank" rel="nofollow noopener noreferrer">教程有涵盖</a>），以及 CSS <a href="https://svelte.dev/docs#class_name" target="_blank" rel="nofollow noopener noreferrer">辅助</a>。</p>
<p>来自 React 的开发者可能会惊喜，Svelte 开箱即用的动画。与其在 npm 里搜索然后希望能找到最好的，不如…内置。它甚至包含了<a href="https://css-tricks.com/svelte-and-spring-animations/" target="_blank" rel="nofollow noopener noreferrer">弹性动画，进入离开的动画</a>，Svelte 称之为<strong>transitions</strong>。</p>
<p>对于 <code>React.Chidren</code>，Svelte 与之对应的是 slots，<a href="https://svelte.dev/docs#slot" target="_blank" rel="nofollow noopener noreferrer">Svelte 的文档很好的讲解了这个</a>。我发现它们比 React’s Children API 更简单些。</p>
<p>最后，我最喜欢的功能之一，几乎算是隐藏的功能，通过 <a href="https://svelte.dev/docs#svelte_options" target="_blank" rel="nofollow noopener noreferrer"><code>svelte:options</code></a> 的属性<code>tagName</code>，Svelte 可以将自己的组件编译为真实的 web 组件。但一定要在 webpack 或 Rollup 配置中设置对应的属性。在 webpack 中是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">loader</span>: <span class="hljs-string">"svelte-loader"</span>,
  <span class="hljs-attr">options</span>: &#123;
    <span class="hljs-attr">customElement</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">有兴趣试试 Svelte 吗</h2>
<p>这篇文章中的任何一个知识点都可以单独拧出来写一个 blog 了，比如 state 管理和 actions，而我们可能只了解到了一些皮毛，我们看到了 Svelte 的功能，不仅是与 React 相匹配，甚至可以模仿很多 React 的 API。然后之前我们简单的谈到了一些 Svelte 的便利，比如内置动画（或者过渡）以及将 Svelte 组件转化为真实的 web 组件。</p>
<p>我希望我成功的激起了你的兴趣，有很多文章，教程或者在线课程等等可以更深入探究。如果你有任何问题可以在评论区告诉我。</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            