
---
title: '在React 18中自动批处理以减少渲染次数(译文)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b32740aa161454c8818a8f889ea584b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 22:16:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b32740aa161454c8818a8f889ea584b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F21" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/21" ref="nofollow noopener noreferrer">在React 18中自动批处理以减少渲染次数</a></p>
<h2 data-id="heading-0">概述</h2>
<p>React 18增加了开箱即用的性能改进，默认做了更多的批处理，不再需要在应用程序或库代码中手动批处理更新。这篇文章将解释什么是批处理，它以前是如何工作的，以及有什么变化。</p>
<blockquote>
<p>注意：这是一个我们不希望大多数用户需要考虑的深入功能。但是，它可能与教育工作者和图书馆开发人员有关。</p>
</blockquote>
<h2 data-id="heading-1">什么是批处理？</h2>
<p>分批是指React将多个状态更新分组到一个重新渲染中以获得更好的性能。</p>
<p>例如，如果你在同一个点击事件里有两个状态更新，React总是把它们分到一个重新渲染中。如果你运行下面的代码，你会看到每次点击时，React只执行一次渲染，尽管你设置了两次状态。</p>
<pre><code class="copyable">function App() &#123;
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  function handleClick() &#123;
    setCount(c => c + 1); // 还没有重新渲染
    setFlag(f => !f); // 还没有重新渲染
    // React 只会在最后重新渲染一次（这是批处理！）
  &#125;

  return (
    <div>
      <button onClick=&#123;handleClick&#125;>Next</button>
      <h1 style=&#123;&#123; color: flag ? "blue" : "black" &#125;&#125;>&#123;count&#125;</h1>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>✅ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fspring-water-929i6%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/spring-water-929i6?file=/src/index.js" ref="nofollow noopener noreferrer">Demo: React 17 事件处理程序中的批处理</a>. (注意在控制台中每次点击都有一个渲染)</li>
</ul>
<p>这对性能非常有用，因为它避免了不必要的重新渲染。它还可以防止您的组件呈现仅更新一个状态变量的“半完成”状态，这可能会导致错误。这可能会提醒您，当您选择第一道菜时，餐厅服务员不会跑到厨房，而是等您完成订单。</p>
<p>然而，React 关于何时批量更新并不一致。例如，如果你需要获取数据，然后在上面的 <code>handleClick</code> 中更新 state，那么 React 不会批量更新，而是执行两次独立的更新。</p>
<p>这是因为React过去只在浏览器事件（如点击）期间进行批量更新，但在这里，我们是在事件已经被处理后（在fetch callback）才更新状态。</p>
<pre><code class="copyable">function App() &#123;
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  function handleClick() &#123;
    fetchSomething().then(() => &#123;
      // React 17 and earlier does NOT batch these because
      // they run *after* the event in a callback, not *during* it
      setCount(c => c + 1); // Causes a re-render
      setFlag(f => !f); // Causes a re-render
    &#125;);
  &#125;

  return (
    <div>
      <button onClick=&#123;handleClick&#125;>Next</button>
      <h1 style=&#123;&#123; color: flag ? "blue" : "black" &#125;&#125;>&#123;count&#125;</h1>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>🟡 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Ftrusting-khayyam-cn5ct%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/trusting-khayyam-cn5ct?file=/src/index.js" ref="nofollow noopener noreferrer">Demo: React 17 不批处理外部事件处理程序</a>. (注意控制台中每次点击两次渲染)</li>
</ul>
<p>在 React 18 之前，我们只在 React 事件处理程序期间批量更新。默认情况下，React 中不会对 <code>promise</code>、<code>setTimeout</code>、原生事件处理程序或任何其他事件中的更新进行批处理。</p>
<h2 data-id="heading-2">什么是自动批处理？</h2>
<p>从带有 <code>createRoot</code> 的 React 18 开始，所有更新都将自动批处理，无论它们来自何处。</p>
<p> 这意味着<code>timeouts</code>、<code>promises</code>、<code>native events</code>处理程序或任何其他事件内的更新将以与 React 事件内的更新相同的方式进行批处理。我们希望这会导致更少的渲染工作，从而在您的应用程序中获得更好的性能：</p>
<pre><code class="copyable">function App() &#123;
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  function handleClick() &#123;
    fetchSomething().then(() => &#123;
      // React 18和更高版本会批量处理这些内容
      setCount(c => c + 1);
      setFlag(f => !f);
      // React 只会在最后重新渲染一次（这是批处理！）
    &#125;);
  &#125;

  return (
    <div>
      <button onClick=&#123;handleClick&#125;>Next</button>
      <h1 style=&#123;&#123; color: flag ? "blue" : "black" &#125;&#125;>&#123;count&#125;</h1>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>✅ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fmorning-sun-lgz88%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/morning-sun-lgz88?file=/src/index.js" ref="nofollow noopener noreferrer">Demo: 即使在事件处理程序之外，也可以使用 createRoot 批处理 React 18!</a> (注意控制台中的每次点击渲染！)</li>
<li>🟡 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fjolly-benz-hb1zx%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/jolly-benz-hb1zx?file=/src/index.js" ref="nofollow noopener noreferrer">Demo: 带有旧版渲染的 React 18 保留了旧行为</a> (请注意控制台中每次单击两次渲染)</li>
</ul>
<blockquote>
<p>注意：作为采用React 18的一部分，预计你会升级到createRoot。渲染的旧行为只是为了使两个版本的生产实验更容易进行。</p>
</blockquote>
<p>无论更新发生在何处，React 都会自动批量更新，因此：</p>
<pre><code class="copyable">function handleClick() &#123;
  setCount(c => c + 1);
  setFlag(f => !f);
  // React 只会在最后重新渲染一次（这是批处理！）
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>行为与此相同：</p>
<pre><code class="copyable">setTimeout(() => &#123;
  setCount(c => c + 1);
  setFlag(f => !f);
  // React 只会在最后重新渲染一次（这是批处理！）
&#125;, 1000);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>行为与此相同：</p>
<pre><code class="copyable">fetch(/*...*/).then(() => &#123;
  setCount(c => c + 1);
  setFlag(f => !f);
  // React 只会在最后重新渲染一次（这是批处理！）
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>行为与此相同：</p>
<pre><code class="copyable">elm.addEventListener('click', () => &#123;
  setCount(c => c + 1);
  setFlag(f => !f);
  // React 只会在最后重新渲染一次（这是批处理！）
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：React 仅在通常安全的情况下才批量更新。例如，React 确保对于<strong>每个用户启动的事件（如单击或按键），DOM 在下一个事件之前完全更新</strong>。例如，这可确保在提交时禁用的表单不​​能被提交两次。</p>
</blockquote>
<h2 data-id="heading-3">如果我不想批处理怎么办？</h2>
<p>通常，批处理是安全的，但某些代码可能依赖于在状态更改后立即从 DOM 中读取某些内容。对于这些用例，您可以使用 ReactDOM.flushSync() 选择退出批处理：</p>
<pre><code class="copyable">import &#123; flushSync &#125; from 'react-dom'; // Note: react-dom, not react

function handleClick() &#123;
  flushSync(() => &#123;
    setCounter(c => c + 1);
  &#125;);
  // React 现在已经更新了 DOM
  flushSync(() => &#123;
    setFlag(f => !f);
  &#125;);
  // React 现在已经更新了 DOM
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们不期望这是个普遍现象</p>
<h2 data-id="heading-4">这对 Hooks 有什么影响吗？</h2>
<p>如果您使用 Hooks，我们希望自动批处理在绝大多数情况下都能“正常工作”。 （如果没有，请告诉我们！）</p>
<h2 data-id="heading-5">这对 Classes 有什么影响吗？</h2>
<p>请记住，更新 期间 React 事件处理程序一直是批处理的，因此对于这些更新没有任何更改。</p>
<p> 在类组件中存在边缘情况，这可能是一个问题。 </p>
<p>类组件有一个实现的怪癖，它可以同步读取事件内部的状态更新。这意味着您将能够在调用 <code>setState</code> 之间读取 <code>this.state</code>：</p>
<pre><code class="copyable">handleClick = () => &#123;
  setTimeout(() => &#123;
    this.setState((&#123; count &#125;) => (&#123; count: count + 1 &#125;));

    // &#123; count: 1, flag: false &#125;
    console.log(this.state);

    this.setState((&#123; flag &#125;) => (&#123; flag: !flag &#125;));
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在React 18中，情况不再是这样了。因为即使在<code>setTimeout</code>中的所有更新都是分批进行的，React不会同步渲染第一个<code>setState</code>的结果--渲染发生在浏览器的下一个时间段。所以渲染还没有发生。</p>
<pre><code class="copyable">handleClick = () => &#123;
  setTimeout(() => &#123;
    this.setState((&#123; count &#125;) => (&#123; count: count + 1 &#125;));

    // &#123; count: 0, flag: false &#125;
    console.log(this.state);

    this.setState((&#123; flag &#125;) => (&#123; flag: !flag &#125;));
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Finteresting-rain-hkjqw%3Ffile%3D%2Fsrc%2FApp.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/interesting-rain-hkjqw?file=/src/App.js" ref="nofollow noopener noreferrer">sandbox</a>.</p>
<p>如果这是升级到 React 18 的障碍，您可以使用 <code>ReactDOM.flushSync</code> 强制更新，但我们建议谨慎使用：</p>
<pre><code class="copyable">handleClick = () => &#123;
  setTimeout(() => &#123;
    ReactDOM.flushSync(() => &#123;
      this.setState((&#123; count &#125;) => (&#123; count: count + 1 &#125;));
    &#125;);

    // &#123; count: 1, flag: false &#125;
    console.log(this.state);

    this.setState((&#123; flag &#125;) => (&#123; flag: !flag &#125;));
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fhopeful-minsky-99m7u%3Ffile%3D%2Fsrc%2FApp.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/hopeful-minsky-99m7u?file=/src/App.js" ref="nofollow noopener noreferrer">sandbox</a>.</p>
<p>这个问题并不影响带有Hooks的函数组件，因为设置状态并不更新来自<code>useState</code>的现有变量。</p>
<pre><code class="copyable">function handleClick() &#123;
  setTimeout(() => &#123;
    console.log(count); // 0
    setCount(c => c + 1);
    setCount(c => c + 1);
    setCount(c => c + 1);
    console.log(count); // 0
  &#125;, 1000)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然当您采用 Hooks 时这种行为可能令人惊讶，但它为自动批处理铺平了道路。</p>
<h2 data-id="heading-6">unstable_batchedUpdates 怎么样？</h2>
<p>一些React库使用这个未记录的API来强制事件处理程序之外的setState被分批处理。</p>
<pre><code class="copyable">import &#123; unstable_batchedUpdates &#125; from 'react-dom';

unstable_batchedUpdates(() => &#123;
  setCount(c => c + 1);
  setFlag(f => !f);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 API 在 18 中仍然存在，但不再需要它了，因为批处理是自动发生的。我们不会在 18 中删除它，尽管在流行的库不再依赖于它的存在之后，它可能会在未来的主要版本中被删除。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b32740aa161454c8818a8f889ea584b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            