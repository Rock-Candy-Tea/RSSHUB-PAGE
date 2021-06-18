
---
title: '再学 React Hooks (二）：函数式组件性能优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2813da37cea341b69a0b26f485f14b76~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 17:58:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2813da37cea341b69a0b26f485f14b76~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 10 天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<blockquote>
<p><em>Hook</em> 是 React 16.8 的新增特性。它可以让你在不编写 class 的情况下使用 state 以及其他的 React 特性</p>
</blockquote>
<p><strong>Hook</strong> 和<strong>函数式组件</strong>让我们更加方便地开发 <strong>React</strong> 应用。本文将介绍<strong>函数式组件</strong>性能优化的几个方法。</p>
<h2 data-id="heading-1">减少 render 次数</h2>
<h3 data-id="heading-2">使用 React.memo</h3>
<p><a href="https://github.com/facebook/react/blob/master/CHANGELOG.md#1660-october-23-2018" target="_blank" rel="nofollow noopener noreferrer">React v16.6.0</a> 提供了 <code>React.memo()</code> 这个 API 来解决前后 props 相同组件却仍然 render 的问题。</p>
<blockquote>
<p>如果你的组件在相同 props 的情况下渲染相同的结果，那么你可以通过将其包装在 <code>React.memo</code> 中调用，以此通过记忆组件渲染结果的方式来提高组件的性能表现。这意味着在这种情况下，React 将跳过渲染组件的操作并直接复用最近一次渲染的结果。</p>
</blockquote>
<p>使用示例如下(<a href="https://zh-hans.reactjs.org/docs/react-api.html#reactmemo" target="_blank" rel="nofollow noopener noreferrer">示例来自官方文档</a>)：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> MyComponent = React.memo(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyComponent</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-comment">/* 使用 props 渲染 */</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>React.memo</strong> 的注意点：</p>
<ol>
<li><code>React.memo</code> 仅检查 props 变更。如果函数式组件内部有 useState、useReducer 和 useReducer 的 Hook，当 context 发生变化时，它仍会重新渲染。</li>
<li><code>React.memo</code> 只对 props 复杂对象做浅比较。如果要自定义比较，需要传入比较函数作为第二个参数。</li>
</ol>
<p>使用示例如下(<a href="https://zh-hans.reactjs.org/docs/react-api.html#reactmemo" target="_blank" rel="nofollow noopener noreferrer">示例来自官方文档</a>)：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyComponent</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-comment">/* 使用 props 渲染 */</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">areEqual</span>(<span class="hljs-params">prevProps, nextProps</span>) </span>&#123;
  <span class="hljs-comment">/*
  如果把 nextProps 传入 render 方法的返回结果与
  将 prevProps 传入 render 方法的返回结果一致则返回 true，
  否则返回 false
  */</span>
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React.memo(MyComponent, areEqual);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">使用 useCallBack、useMemo 缓存传给子组件的 props</h3>
<p>现有下面的代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 父组件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [appCount, setAppCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [childCount, setChildCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-keyword">const</span> handleAppAdd = <span class="hljs-function">() =></span> &#123;
    setAppCount(appCount + <span class="hljs-number">1</span>);
  &#125;;

  <span class="hljs-keyword">const</span> handleChildAdd = <span class="hljs-function">() =></span> &#123;
    setChildCount(childCount + <span class="hljs-number">1</span>);
  &#125;;

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'app render'</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>App<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleAppAdd&#125;</span>></span>appCount + 1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>appCount: &#123;appCount&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>child<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleChildAdd&#125;</span>></span>childCount + 1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;childCount&#125;</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-comment">// child 组件</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">const</span> Child = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child render'</span>);
  <span class="hljs-keyword">const</span> &#123; value &#125; = props;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Child: &#123;value&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React.memo(Child);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的 <code>Child</code> 组件已经使用 <code>React.memo</code> 优化，当仅有父组件 <code>appCount</code> 变化时， <code>Child</code> 组件不会重新渲染。</p>
<p>现在我们在改造 <code>Child</code> 组件：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">const</span> Child = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child render'</span>);
  <span class="hljs-keyword">const</span> &#123; value, handleAdd &#125; = props;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Child: &#123;value&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleAdd&#125;</span>></span>btn in child: childCount + 1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React.memo(Child);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中我们在子组件也加一个可以增减 <code>ChildCount</code> 的按钮，点击它时调用父组件中传入的 <code>props.handleAdd</code>。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// app.jsx</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [appCount, setAppCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [childCount, setChildCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-keyword">const</span> handleAppAdd = <span class="hljs-function">() =></span> &#123;
    setAppCount(appCount + <span class="hljs-number">1</span>);
  &#125;;

  <span class="hljs-keyword">const</span> handleChildAdd = <span class="hljs-function">() =></span> &#123;
    setChildCount(childCount + <span class="hljs-number">1</span>);
  &#125;;

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'app render'</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>App<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleAppAdd&#125;</span>></span>appCount + 1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>appCount: &#123;appCount&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>child<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleChildAdd&#125;</span>></span>childCount + 1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;childCount&#125;</span> <span class="hljs-attr">handleAdd</span>=<span class="hljs-string">&#123;handleChildAdd&#125;</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码给 <code>Child</code> 传入了 <code>handleAdd</code> 的 props。然而当我们再次点击 <code>appCount + 1</code> 时，虽然 <code>childCount</code> 未变化，但是 <code>Child</code> 却刷新了，日志如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2813da37cea341b69a0b26f485f14b76~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210616201446852" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面的情况我们可以分析出，是新传入 <code>Child</code> 的<code>props.handleAdd</code>导致了重新渲染。因为 <code>handleAdd</code> 在 <code>App</code> 组件中每次都是重新生成的一个新函数，<code>React.memo </code>浅比较 props 改变，<code>Child</code> 重新 render。</p>
<p>那么我们怎么解决 props 上存在函数的问题呢？<a href="https://zh-hans.reactjs.org/docs/hooks-reference.html#usecallback" target="_blank" rel="nofollow noopener noreferrer">React.useCallback</a> 可以解决这个问题。</p>
<blockquote>
<p>把内联回调函数及依赖项数组作为参数传入 <code>useCallback</code>，它将返回该回调函数的 memoized 版本，该回调函数仅在某个依赖项改变时才会更新。</p>
<p><code>useCallback(fn, deps)</code> 相当于 <code>useMemo(() => fn, deps)</code>。</p>
</blockquote>
<p>由官方文档可以看出，只要 deps 未改变， <code>useCallback</code>返回的还是同一个函数。同样地 ，如果 props 是复杂对象， 我们也可以使用 <code>useMemo</code> 来处理。</p>
<p>上面 <code>child</code> 重复 render 的问题, 我们如下处理：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// App.js</span>

<span class="hljs-keyword">const</span> handleChildAdd = useCallback(<span class="hljs-function">() =></span> &#123;
  setChildCount(childCount + <span class="hljs-number">1</span>);
&#125;, [childCount]);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://stackblitz.com/edit/react-hook-perf" target="_blank" rel="nofollow noopener noreferrer">点击这里查看示例代码</a></p>
<h2 data-id="heading-4">占位组件的 render 优化</h2>
<p>我们通常有一这样的需求，比如子组件有一个占位区域，占位区域的组件需要通过 props 传入，我们可以通过在父组件中创建好   <code>React.Element</code> 来减少占位组件的渲染次数。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75b902677cf542d38939bbcc1c6910b4~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210617132917614" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码如下：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> Content = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Content render'</span>);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>content<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;;

<span class="hljs-comment">// 优化前</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">content</span>=<span class="hljs-string">&#123;Content&#125;</span> /></span></span>;
&#125;

<span class="hljs-comment">// 优化后</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">content</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">Content</span> /></span>&#125; /></span>;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中, 我们要注意 <code>Child</code> 组件传入 <code>content</code> 的方式。</p>
<ol>
<li>优化前：传入的是 <strong>Content 组件</strong></li>
<li>优化后：传入的是 <code><Content /></code> 形式的 <code>React.Element</code></li>
</ol>
<p>通过在父组件件内部使用 <code><Content /></code> 创建  <code>React.Element</code>，这样可以避免子组件自身 render 重新创建 <code>Content</code> 的   <code>React.Element</code>。</p>
<h2 data-id="heading-5">React.Context 读写分离</h2>
<p><a href="https://juejin.cn/post/6889247428797530126" target="_blank"><strong>读写分析部分的参考文章</strong></a></p>
<p>未分离前：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> LogContext = React.createContext();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">LogProvider</span>(<span class="hljs-params">&#123; children &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [logs, setLogs] = useState([]);
  <span class="hljs-keyword">const</span> addLog = <span class="hljs-function">(<span class="hljs-params">log</span>) =></span> setLogs(<span class="hljs-function">(<span class="hljs-params">prevLogs</span>) =></span> [...prevLogs, log]);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">LogContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">logs</span>, <span class="hljs-attr">addLog</span> &#125;&#125;></span>
      &#123;children&#125;
    <span class="hljs-tag"></<span class="hljs-name">LogContext.Provider</span>></span></span>
  );
&#125;

作者：ssh_晨曦时梦见兮
链接：https:<span class="hljs-comment">//juejin.cn/post/6889247428797530126</span>
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当 Provider 的 <code>value</code> 值发生变化时，它内部的所有消费组件都会重新渲染。Provider 及其内部 consumer 组件都不受制于 <code>shouldComponentUpdate</code> 函数，因此当 consumer 组件在其祖先组件退出更新的情况下也能更新。</p>
</blockquote>
<p>优化前的代码中，只要 <code>setLogs</code> 更新了状态, value 就会传入新的值。所有用到 <code>logContext</code> 对应的函数都会被更新。</p>
<p>优化后的代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">LogProvider</span>(<span class="hljs-params">&#123; children &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [logs, setLogs] = useState([]);
  <span class="hljs-keyword">const</span> addLog = useCallback(<span class="hljs-function">(<span class="hljs-params">log</span>) =></span> &#123;
    setLogs(<span class="hljs-function">(<span class="hljs-params">prevLogs</span>) =></span> [...prevLogs, log]);
  &#125;, []);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">LogDispatcherContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;addLog&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">LogStateContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;logs&#125;</span>></span>
        &#123;children&#125;
      <span class="hljs-tag"></<span class="hljs-name">LogStateContext.Provider</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">LogDispatcherContext.Provider</span>></span></span>
  );
&#125;

作者：ssh_晨曦时梦见兮
链接：https:<span class="hljs-comment">//juejin.cn/post/6889247428797530126</span>
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们通过 <code>LogDispatcherContext</code> 和 <code>LogStateContext</code> 实现读写分离。只需要使用 <code>addLog</code> 的组件就不会因为 <code>logs</code> 改变而刷新了。</p>
<h2 data-id="heading-6">参考资料</h2>
<ul>
<li><a href="https://zh-hans.reactjs.org/docs/react-api.html#reactmemo" target="_blank" rel="nofollow noopener noreferrer">React 官方文档</a></li>
<li><a href="https://juejin.cn/post/6889247428797530126" target="_blank">我在工作中写React，学到了什么？性能优化篇</a></li>
</ul></div>  
</div>
            