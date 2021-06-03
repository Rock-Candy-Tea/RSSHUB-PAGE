
---
title: '【译】5种高级React模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/598bc664b81e4fe0912d9e94837c1425~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 01:32:32 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/598bc664b81e4fe0912d9e94837c1425~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文地址：<a href="https://javascript.plainenglish.io/5-advanced-react-patterns-a6b7624267a6" target="_blank" rel="nofollow noopener noreferrer">5 Advanced React Patterns</a></p>
<p>原文作者：Alexis Regnaud</p>
</blockquote>
<p><strong>限于个人能力，如有错漏之处，烦请不吝赐教。</strong></p>
<p>本文概述了5种现代高级React模式，包括集成代码、优点和缺点，以及在公共库中的具体用法。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/598bc664b81e4fe0912d9e94837c1425~tplv-k3u1fbpfcp-watermark.image" alt="Photo by Ferenc Almasi on Unsplash" loading="lazy" referrerpolicy="no-referrer"></p>
<p>像每个React开发者一样，你可能已经问过自己以下问题之一</p>
<ul>
<li>我如何建立一个<strong>可重复使用</strong>的组件以适应不同的使用情况？</li>
<li>我如何建立一个具有<strong>简单API</strong>的组件，使其易于使用？</li>
<li>我如何建立一个在用户界面和功能方面<strong>可扩展</strong>的组件？</li>
</ul>
<p>这些反复出现的问题催生了整个React社区的一些高级模式的出现</p>
<p>在这篇文章中，我们将看到5种不同模式的概述。为了便于比较，我们将对所有这些模式使用一个相同的结构。</p>
<p>我们将从一个小的介绍开始，然后是一个真实的代码例子（基于同一个简单的<code>Counter</code>组件）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a14d83744d34635ad3a81f68fda51b7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>所有的源代码都可以在这个github仓库中获得：<a href="https://github.com/alex83130/advanced-react-patterns%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">github.com/alex83130/a…</a></p>
</blockquote>
<p>我们将列出优点和缺点，然后在一个名为 "标准"的部分中定义两个因素。</p>
<ul>
<li><a href="https://kentcdodds.com/blog/inversion-of-control" target="_blank" rel="nofollow noopener noreferrer">反转控制</a>: 你的组件给用户提供的灵活性和控制等级</li>
<li>实施的复杂性: 你和用户实现该模式的难度。</li>
</ul>
<p>最后，我们将找一些公共库在生产环境中使用该模式的例子</p>
<blockquote>
<p>在这篇文章中，我们将考虑一个React开发者（你）为其他开发者构建一个组件的情况。因此，"用户"这个角色直接指的是这些开发者（而不是使用你的网站/应用程序的最终用户）。</p>
</blockquote>
<h1 data-id="heading-0">1. 复合组件模式（Compound Components Pattern）</h1>
<p>这种模式允许创建富有表现力和声明性的组件，避免非必要的<a href="https://kentcdodds.com/blog/prop-drilling" target="_blank" rel="nofollow noopener noreferrer">prop drilling</a>。如果你想让你的组件更有可塑性，有更好的关注点分离和易理解的API，你应该考虑使用这种模式。</p>
<h3 data-id="heading-1">例子</h3>
<p>Github: <a href="https://github.com/alex83130/advanced-react-patterns/tree/main/src/patterns/compound-component" target="_blank" rel="nofollow noopener noreferrer">github.com/alex83130/a…</a></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Counter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./Counter"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Usage</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> handleChangeCounter = <span class="hljs-function">(<span class="hljs-params">count</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"count"</span>, count);
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Counter</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;handleChangeCounter&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter.Decrement</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"minus"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter.Label</span>></span>Counter<span class="hljs-tag"></<span class="hljs-name">Counter.Label</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter.Count</span> <span class="hljs-attr">max</span>=<span class="hljs-string">&#123;10&#125;</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter.Increment</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"plus"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">Counter</span>></span></span>
  );
&#125;

<span class="hljs-keyword">export</span> &#123; Usage &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">优点</h3>
<ul>
<li>减少了API的复杂性：与其把所有的<code>props</code>都塞进一个巨大的父组件中，然后再把这些<code>props</code>钻到子UI组件中，不如在这里把每个<code>props</code>都连接到各自最有意义的子组件上。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bc3be15a37142b4a647e2c0e5c28ba1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>灵活的标记结构：你的组件有很大的UI灵活性，允许从一个单一的组件创建各种情况。例如，用户可以改变子组件的顺序或定义哪个组件应该被显示。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fea100aec804093815add4ccfb35afe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>关注点分离：大部分的逻辑都包含在主<code>Counter</code>组件中，然后用<code>React.Context</code>来分享所有子组件的状态和事件处理。我们得到了一个明确的责任划分。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/889e67cf345b4d26a7a21bae9ef10d89~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">缺点</h3>
<ul>
<li>
<p>太高的UI灵活性：拥有灵活性的同时，也有可能引发意想不到的行为（把一个不需要的组件的子组件放进去，把子组件的顺序弄乱，忘记包含一个必须的子组件）</p>
<p>根据你想要用户如何使用你的组件，你可能不希望有那么多的灵活性。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b96eecf08388447c884e9280d09d0b6e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>更重的JSX：应用这种模式会增加JSX行的数量，特别是当你使用像<code>ESLint</code>这样的代码检测工具或类似<code>Prettier</code>这样的代码格式化工具时</li>
</ul>
<p>在单个组件的规模上，这似乎不是什么大问题，但当你从全局来看时，肯定会产生巨大的差异。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94ca345ac5114168a94d83b2ab0e7440~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">标准</h3>
<ul>
<li>反转控制：1/4</li>
<li>实施的复杂性：1/4</li>
</ul>
<h3 data-id="heading-5">使用此模式的公共库</h3>
<ul>
<li><a href="https://react-bootstrap.github.io/components/dropdowns/" target="_blank" rel="nofollow noopener noreferrer">React Bootstrap</a></li>
<li><a href="https://reach.tech/accordion" target="_blank" rel="nofollow noopener noreferrer">Reach UI</a></li>
</ul>
<h1 data-id="heading-6">2. 受控属性模式</h1>
<p>这种模式将你的组件转变为一个受控组件。外部状态作为 "单一事实源 "被消耗，允许用户插入自定义逻辑，修改默认组件的行为。</p>
<h3 data-id="heading-7">例子</h3>
<p>Github: <a href="https://github.com/alex83130/advanced-react-patterns/tree/main/src/patterns/control-props" target="_blank" rel="nofollow noopener noreferrer">github.com/alex83130/a…</a></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Counter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./Counter"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Usage</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-keyword">const</span> handleChangeCounter = <span class="hljs-function">(<span class="hljs-params">newCount</span>) =></span> &#123;
    setCount(newCount);
  &#125;;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Counter</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;count&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;handleChangeCounter&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter.Decrement</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">&#123;</span>"<span class="hljs-attr">minus</span>"&#125; /></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter.Label</span>></span>Counter<span class="hljs-tag"></<span class="hljs-name">Counter.Label</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter.Count</span> <span class="hljs-attr">max</span>=<span class="hljs-string">&#123;10&#125;</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter.Increment</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">&#123;</span>"<span class="hljs-attr">plus</span>"&#125; /></span>
    <span class="hljs-tag"></<span class="hljs-name">Counter</span>></span></span>
  );
&#125;

<span class="hljs-keyword">export</span> &#123; Usage &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">优点</h3>
<ul>
<li>给予更多的控制：由于主状态暴露在你的组件之外，用户可以控制它，因此可以直接影响你的组件。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bdc0d0196d74e4aa9421cfd8a8de6c8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">缺点</h3>
<ul>
<li>实施的复杂性: 之前，在一个地方（<code>JSX</code>）的一个集成就足以使你的组件工作。现在，它将分散在3个不同的地方（<code>JSX</code> / <code>useState</code> / <code>handleChange</code>）。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fbef612a5e34ce0b15de86d11d5421f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">标准</h3>
<ul>
<li>反转控制：2/4</li>
<li>实施的复杂性：1/4</li>
</ul>
<h3 data-id="heading-11">使用此模式的公共库</h3>
<ul>
<li><a href="https://material-ui.com/components/rating/#rating" target="_blank" rel="nofollow noopener noreferrer">Material UI</a></li>
</ul>
<h1 data-id="heading-12">3. 自定义钩子模式</h1>
<p>让我们在 "控制反转 "中更进一步：主要的逻辑现在被转移到一个自定义的钩子中。这个钩子可以被用户访问，并且暴露了几个内部逻辑（状态、处理程序），允许他对你的组件有更好的控制。</p>
<h3 data-id="heading-13">例子</h3>
<p>Github: <a href="https://github.com/alex83130/advanced-react-patterns/tree/main/src/patterns/custom-hooks" target="_blank" rel="nofollow noopener noreferrer">github.com/alex83130/a…</a></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Counter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./Counter"</span>;
<span class="hljs-keyword">import</span> &#123; useCounter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./useCounter"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Usage</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; count, handleIncrement, handleDecrement &#125; = useCounter(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> MAX_COUNT = <span class="hljs-number">10</span>;

  <span class="hljs-keyword">const</span> handleClickIncrement = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">//Put your custom logic</span>
    <span class="hljs-keyword">if</span> (count < MAX_COUNT) &#123;
      handleIncrement();
    &#125;
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">Counter</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;count&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Counter.Decrement</span>
          <span class="hljs-attr">icon</span>=<span class="hljs-string">&#123;</span>"<span class="hljs-attr">minus</span>"&#125;
          <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleDecrement&#125;</span>
          <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;count</span> === <span class="hljs-string">0&#125;</span>
        /></span>
        <span class="hljs-tag"><<span class="hljs-name">Counter.Label</span>></span>Counter<span class="hljs-tag"></<span class="hljs-name">Counter.Label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Counter.Count</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">Counter.Increment</span>
          <span class="hljs-attr">icon</span>=<span class="hljs-string">&#123;</span>"<span class="hljs-attr">plus</span>"&#125;
          <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClickIncrement&#125;</span>
          <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;count</span> === <span class="hljs-string">MAX_COUNT&#125;</span>
        /></span>
      <span class="hljs-tag"></<span class="hljs-name">Counter</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClickIncrement&#125;</span> <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;count</span> === <span class="hljs-string">MAX_COUNT&#125;</span>></span>
        Custom increment btn 1
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;

<span class="hljs-keyword">export</span> &#123; Usage &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">优点</h3>
<ul>
<li>给予更多的控制: 用户可以在钩子和JSX元素之间插入自己的逻辑，允许他修改默认组件的行为。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1ec62fdd82b45c2bf0c69dadfe9e040~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">缺点</h3>
<ul>
<li>实施的复杂性：由于逻辑部分与渲染部分是分开的，所以必须由用户将两者联系起来。要正确地实现它，需要对你的组件的工作方式有一个很好的理解。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a7e677c782e4ab7a22b48ff1ad76d3d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">标准</h3>
<ul>
<li>反转控制：2/4</li>
<li>实施的复杂性：2/4</li>
</ul>
<h3 data-id="heading-17">使用此模式的公共库</h3>
<ul>
<li><a href="https://react-table.tanstack.com/docs/examples/basic" target="_blank" rel="nofollow noopener noreferrer">React table</a></li>
<li><a href="https://react-hook-form.com/api" target="_blank" rel="nofollow noopener noreferrer">React hook form</a></li>
</ul>
<h1 data-id="heading-18">4. Props getter 模式</h1>
<p>自定义钩子模式提供了很好的控制，但也使你的组件更难集成，因为用户必须处理大量的组件本地钩子的<code>props</code>，并在他那边重新创建逻辑。Props Getters模式试图掩盖这种复杂性。我们不暴露本地<code>props</code>，而是提供一个<code>props getters</code>  的短名单。一个<code>getter</code>是一个返回许多<code>props</code>的函数，它有一个有意义的名字，允许用户自然地将其链接到正确的JSX元素。</p>
<h3 data-id="heading-19">例子</h3>
<p>Github: <a href="https://github.com/alex83130/advanced-react-patterns/tree/main/src/patterns/props-getters" target="_blank" rel="nofollow noopener noreferrer">github.com/alex83130/a…</a></p>
<pre><code class="copyable">import React from "react";
import &#123; Counter &#125; from "./Counter";
import &#123; useCounter &#125; from "./useCounter";

const MAX_COUNT = 10;

function Usage() &#123;
  const &#123;
    count,
    getCounterProps,
    getIncrementProps,
    getDecrementProps
  &#125; = useCounter(&#123;
    initial: 0,
    max: MAX_COUNT
  &#125;);

  const handleBtn1Clicked = () => &#123;
    console.log("btn 1 clicked");
  &#125;;

  return (
    <>
      <Counter &#123;...getCounterProps()&#125;>
        <Counter.Decrement icon=&#123;"minus"&#125; &#123;...getDecrementProps()&#125; />
        <Counter.Label>Counter</Counter.Label>
        <Counter.Count />
        <Counter.Increment icon=&#123;"plus"&#125; &#123;...getIncrementProps()&#125; />
      </Counter>
      <button &#123;...getIncrementProps(&#123; onClick: handleBtn1Clicked &#125;)&#125;>
        Custom increment btn 1
      </button>
      <button &#123;...getIncrementProps(&#123; disabled: count > MAX_COUNT - 2 &#125;)&#125;>
        Custom increment btn 2
      </button>
    </>
  );
&#125;

export &#123; Usage &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">优点</h3>
<ul>
<li>易用性：提供一种简单的方式来整合你的组件，复杂性被隐藏起来，用户只需将正确的getter连接到正确的JSX元素。</li>
</ul>
<p><img src="https://miro.medium.com/max/1400/1*auZca0g2eg1Cv7THl6df6g.png" alt="https://miro.medium.com/max/1400/1*auZca0g2eg1Cv7THl6df6g.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>灵活性： 用户仍然有可能重载<code>getters</code>中的<code>props</code>，以适应他的具体情况。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78b2802a2c2146f29acdf60aab99a66b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">缺点</h3>
<ul>
<li>缺少可见性： <code>getters</code> 带来的抽象性使你的组件更容易集成，但也更不透明和 "魔法"。为了正确地覆盖你的组件，用户必须知道<code>getters</code>所暴露的<code>props</code>列表，以及如果其中一个<code>props</code>被改变所带来的内部逻辑影响。</li>
</ul>
<h3 data-id="heading-22">标准</h3>
<ul>
<li>反转控制：3/4</li>
<li>集成的复杂性：3/4</li>
</ul>
<h3 data-id="heading-23">使用此模式的公共库</h3>
<ul>
<li><a href="https://react-table.tanstack.com/docs/examples/basic" target="_blank" rel="nofollow noopener noreferrer">React table</a></li>
<li><a href="https://github.com/downshift-js/downshift#usage" target="_blank" rel="nofollow noopener noreferrer">Downshift</a></li>
</ul>
<h1 data-id="heading-24">5. State reducer 模式</h1>
<p>在控制的反转方面是最先进的模式。它为用户提供了一种先进的方式来改变你的组件的内部操作方式。</p>
<p>代码类似于自定义钩子模式，但除此之外，用户还定义了一个被传递给钩子的<code>reducer</code>。这个<code>reducer</code>将重载你的组件的任何内部动作。</p>
<h3 data-id="heading-25">例子</h3>
<p>Github: <a href="https://github.com/alex83130/advanced-react-patterns/tree/main/src/patterns/state-reducer" target="_blank" rel="nofollow noopener noreferrer">github.com/alex83130/a…</a></p>
<pre><code class="copyable">    import React from "react";
    import &#123; Counter &#125; from "./Counter";
    import &#123; useCounter &#125; from "./useCounter";

    const MAX_COUNT = 10;
    function Usage() &#123;
      const reducer = (state, action) => &#123;
        switch (action.type) &#123;
          case "decrement":
            return &#123;
              count: Math.max(0, state.count - 2) //The decrement delta was changed for 2 (Default is 1)
            &#125;;
          default:
            return useCounter.reducer(state, action);
        &#125;
      &#125;;

      const &#123; count, handleDecrement, handleIncrement &#125; = useCounter(
        &#123; initial: 0, max: 10 &#125;,
        reducer
      );

      return (
        <>
          <Counter value=&#123;count&#125;>
            <Counter.Decrement icon=&#123;"minus"&#125; onClick=&#123;handleDecrement&#125; />
            <Counter.Label>Counter</Counter.Label>
            <Counter.Count />
            <Counter.Increment icon=&#123;"plus"&#125; onClick=&#123;handleIncrement&#125; />
          </Counter>
          <button onClick=&#123;handleIncrement&#125; disabled=&#123;count === MAX_COUNT&#125;>
            Custom increment btn 1
          </button>
        </>
      );
    &#125;

    export &#123; Usage &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在这个例子中，我们结合了State reducer模式和Custom hook模式，但是你也可以把它和Compound components模式一起使用，直接把reducer传递给主组件Counter。</p>
</blockquote>
<h3 data-id="heading-26">优点</h3>
<ul>
<li>给予更多的控制：在最复杂的情况下，使用<code>state reducers</code>是把控制权留给用户的最好方法。你所有的内部组件的动作现在都可以从外部访问，并且可以被重写。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1d4a2d6e2d448368cb3877a905ab6c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-27">缺点</h3>
<ul>
<li>实施的复杂性：这种模式的实现肯定是最复杂的，无论是对你还是对用户。</li>
<li>缺少可见性：由于任何<code>reducer</code>的动作都可以被改变，因此需要很好地理解组件的内部逻辑。</li>
</ul>
<h3 data-id="heading-28">标准</h3>
<ul>
<li>反转控制：4/4</li>
<li>集成的复杂性：4/4</li>
</ul>
<h3 data-id="heading-29">使用此模式的公共库</h3>
<ul>
<li><a href="https://github.com/downshift-js/downshift#statereducer" target="_blank" rel="nofollow noopener noreferrer">Downshift</a></li>
</ul>
<h2 data-id="heading-30">总结</h2>
<p>通过这5个高级React模式，我们看到了利用 "控制反转 "概念的不同方式。它们给你提供了一个强大的方法来创建灵活和适应性强的组件。
然而，我们都知道这句著名的谚语："能力越大责任越大"，你越是把控制权转移给用户，你的组件就越是远离 "即插即用 "的思维方式。作为一个开发者，你的角色是选择正确的模式来对应正确的需求。
为了帮助你完成这项任务，下面的图表根据 "集成的复杂性 "和 "控制反转 "这两个因素对所有这些模式进行了分类。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e8312b508954342a1f1f2ef2114f5f2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这篇文章的灵感主要来自于Kent C. Dodds的惊人工作
如果你有兴趣了解更多关于每个模式的信息，请看他的<a href="https://kentcdodds.com/blog/" target="_blank" rel="nofollow noopener noreferrer">博客</a>。我希望你觉得这篇文章有用。
谢谢你的阅读。</p>
<p>更多内容请见 <a href="http://plainenglish.io/" target="_blank" rel="nofollow noopener noreferrer">plainenglish.io</a></p></div>  
</div>
            