
---
title: '给我5分钟！教你写出干净清爽的 React 代码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78a7b501a6664d6384ca6b3c63ce8533~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Apr 2021 01:06:21 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78a7b501a6664d6384ca6b3c63ce8533~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="搜索框传播样式-白色版.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78a7b501a6664d6384ca6b3c63ce8533~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>作为React开发人员，我们都希望编写更简洁、更容易阅读的代码。</p>
<p>在这篇指南中，我总结了七种最重要的方法，你可以从今天开始编写更干净的React代码，让构建React项目和检查代码变得更容易。</p>
<p>一般来说，学习如何编写更清晰的React代码将使你成为一个更有价值、更快乐的React开发人员，所以让我们开始吧!</p>
<h2 data-id="heading-0">1. 使用JSX简写</h2>
<p>如何将<code>true</code>的值传递给给定的<code>prop</code>?</p>
<p>在下面的例子中，我们使用<code>showTitle</code>这个<code>prop</code>来在导航栏组件中显示我们应用的标题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/App.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Navbar</span> <span class="hljs-attr">showTitle</span>=<span class="hljs-string">&#123;true&#125;</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Navbar</span>(<span class="hljs-params">&#123; showTitle &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      &#123;showTitle && <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>My Special App<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要显式设置showTitle为布尔值true吗?不!<strong>一个要记住的简单方法是，组件上提供的任何<code>prop</code>都有一个默认值<code>true</code>。</strong></p>
<p>因此，如果我们在导航栏上添加<code>showTitle prop</code>，我们的title元素将显示:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/App.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Navbar</span> <span class="hljs-attr">showTitle</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Navbar</span>(<span class="hljs-params">&#123; showTitle &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      &#123;showTitle && <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>My Special App<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>&#125; // title shown!
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个需要记住的有用的速记方法是传递字符串 prop 。当你传递一个字符串的prop 值时，你不需要用花括号包装它。</p>
<p>如果我们要设置导航栏的标题，使用title prop，我们只需要在双引号中包含它的值:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/App.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Navbar</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"My Special App"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Navbar</span>(<span class="hljs-params">&#123; title &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 将不相关的代码移动到单独的组件中</h2>
<p>毫无疑问，要想编写更清晰的React代码，最简单也是最重要的方法就是将代码抽象到单独的React组件中。</p>
<p>让我们看看下面的例子。我们的代码在做什么?</p>
<p>我们的应用正在显示一个导航栏组件。我们使用<code>.map()</code>遍历一个帖子数组，并在页面上显示它们的标题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/App.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> posts = [
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">"How to Build App with React"</span>
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">"How to Write Your First React Hook"</span>
    &#125;
  ];

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Navbar</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"My Special App"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        &#123;posts.map(post => (
          <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;post.id&#125;</span>></span>
            &#123;post.title&#125;
          <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        ))&#125;
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Navbar</span>(<span class="hljs-params">&#123; title &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们怎样才能使它更干净呢?</p>
<p>为什么我们不抽象我们正在循环的代码——我们的post，并在一个单独的组件中显示它们，我们将其称为<code>featuredpost</code>。</p>
<p>让我们来看看结果:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/App.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
 <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Navbar</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"My Special App"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">FeaturedPosts</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Navbar</span>(<span class="hljs-params">&#123; title &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FeaturedPosts</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> posts = [
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">"How to Build App with React"</span>
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">"How to Write Your First React Hook"</span>
    &#125;
  ];

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      &#123;posts.map((post) => (
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;post.id&#125;</span>></span>&#123;post.title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如你所见，我们现在只需要看看我们的App组件。通过读取其中组件、导航栏和FeaturedPosts的名称，我们可以准确地看到我们的应用程序正在显示什么。</p>
<h2 data-id="heading-2">3.为每个组件创建单独的文件</h2>
<p>在前面的例子中，我们把所有的组件都包含在一个单独的文件<code>app.js</code>中。</p>
<p>就像<strong>我们将代码抽象到单独的组件中以使我们的应用程序更具可读性</strong>，使我们的应用程序文件更具可读性一样，我们可以将<strong>每个组件放到一个单独的文件中</strong>。</p>
<p>这再次帮助我们分离应用程序中的关注点。这意味着<strong>每个文件只负责一个组件</strong>，如果我们想在整个应用中重用它，就不会混淆组件来自哪里:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/App.js</span>
<span class="hljs-keyword">import</span> Navbar <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/Navbar.js'</span>;
<span class="hljs-keyword">import</span> FeaturedPosts <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/FeaturedPosts.js'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Navbar</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"My Special App"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">FeaturedPosts</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/components/Navbar.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Navbar</span>(<span class="hljs-params">&#123; title &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/components/FeaturedPosts.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FeaturedPosts</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> posts = [
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">"How to Build YouTube with React"</span>
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">"How to Write Your First React Hook"</span>
    &#125;
  ];

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      &#123;posts.map((post) => (
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;post.id&#125;</span>></span>&#123;post.title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，通过在自己的文件中包含每个单独的组件，我们可以避免一个文件变得过于臃肿。如果我们想把所有的组件都添加到app.js文件中，我们很容易看到这个文件变得非常大。</p>
<h2 data-id="heading-3">4. 将公共的功能移到React Hooks中</h2>
<p>看看我们的FeaturedPosts组件，我们要从API中获取post数据，而不是显示静态的post数据。</p>
<p>我们可以使用fetch API。你可以看到下面的结果:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/components/FeaturedPosts.js</span>

<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FeaturedPosts</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [posts, setPosts] = React.useState([]);  
    
  React.useEffect(<span class="hljs-function">() =></span> &#123;
    fetch(<span class="hljs-string">'https://example.com/posts'</span>)
      .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> res.json())
      .then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> setPosts(data));
  &#125;, []);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      &#123;posts.map((post) => (
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;post.id&#125;</span>></span>&#123;post.title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，如果我们想跨多个组件执行这个数据请求，该怎么办呢?</p>
<p>假设除了FeaturedPosts组件外，我们还想创建一个名为<code>just Posts</code>的组件，该组件具有相同的数据。我们必须复制用于获取数据的逻辑，并将其粘贴到该组件中。</p>
<p>为了避免这样做，为什么我们不使用一个新的React Hooks 我们可以叫它<code>useFetchPosts</code>:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/hooks/useFetchPosts.js</span>

<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useFetchPosts</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [posts, setPosts] = React.useState([]);  
    
  React.useEffect(<span class="hljs-function">() =></span> &#123;
    fetch(<span class="hljs-string">'https://example.com/posts'</span>)
      .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> res.json())
      .then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> setPosts(data));
  &#125;, []);

  <span class="hljs-keyword">return</span> posts;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦我们在一个专门的“hooks”文件夹中创建了这个钩子，我们就可以在任何我们喜欢的组件中重用它，包括FeaturedPosts组件:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/components/FeaturedPosts.js</span>

<span class="hljs-keyword">import</span> useFetchPosts <span class="hljs-keyword">from</span> <span class="hljs-string">'../hooks/useFetchPosts.js'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FeaturedPosts</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> posts = useFetchPosts()

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      &#123;posts.map((post) => (
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;post.id&#125;</span>></span>&#123;post.title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5. 从JSX中移除尽可能多的JavaScript</h2>
<p>另一种非常有用但经常被忽视的清理组件的方法是尽可能从JSX中删除JavaScript。</p>
<p>让我们看看下面的例子:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/components/FeaturedPosts.js</span>

<span class="hljs-keyword">import</span> useFetchPosts <span class="hljs-keyword">from</span> <span class="hljs-string">'../hooks/useFetchPosts.js'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FeaturedPosts</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> posts = useFetchPosts()

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      &#123;posts.map((post) => (
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;event</span> =></span> &#123;
          console.log(event.target, 'clicked!');
        &#125;&#125; key=&#123;post.id&#125;>&#123;post.title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们正在处理我们的一个帖子上的点击事件。您可以看到，我们的<strong>JSX变得更难阅读了</strong>。由于我们的函数是作为内联函数包含的，因此它掩盖了这个组件及其相关函数的用途。</p>
<p>我们能做些什么来解决这个问题呢?<strong>我们可以将连接到onClick的内联函数提取到一个单独的处理程序中</strong>，我们可以给它一个合适的名称，如handlePostClick。</p>
<p>一旦我们这样做，我们的JSX再次变得可读:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/components/FeaturedPosts.js</span>

<span class="hljs-keyword">import</span> useFetchPosts <span class="hljs-keyword">from</span> <span class="hljs-string">'../hooks/useFetchPosts.js'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FeaturedPosts</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> posts = useFetchPosts()
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handlePostClick</span>(<span class="hljs-params">event</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(event.target, <span class="hljs-string">'clicked!'</span>);   
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      &#123;posts.map((post) => (
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handlePostClick&#125;</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;post.id&#125;</span>></span>&#123;post.title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6. 格式化内联样式以减少代码的膨胀</h2>
<p>React开发人员的一个常见模式是在JSX中编写<strong>内联样式</strong>。但是，这再次使我们的代码更难读，也更难编写额外的JSX:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/App.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">textAlign:</span> '<span class="hljs-attr">center</span>' &#125;&#125;></span>
      <span class="hljs-tag"><<span class="hljs-name">Navbar</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"My Special App"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Navbar</span>(<span class="hljs-params">&#123; title &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginTop:</span> '<span class="hljs-attr">20px</span>' &#125;&#125;></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">fontWeight:</span> '<span class="hljs-attr">bold</span>' &#125;&#125;></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们希望将关注点分离的概念应用到JSX样式中，方法是将内联样式移动到CSS样式表中，我们可以<strong>将CSS样式表导入到任何想要的组件中</strong>。</p>
<p>重写内联样式的<strong>另一种方法是将它们组织成对象</strong>。你可以看到这样的模式看起来像下面:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/App.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> styles = &#123;
    <span class="hljs-attr">main</span>: &#123; <span class="hljs-attr">textAlign</span>: <span class="hljs-string">"center"</span> &#125;
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.main&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Navbar</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"My Special App"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Navbar</span>(<span class="hljs-params">&#123; title &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> styles = &#123;
    <span class="hljs-attr">div</span>: &#123; <span class="hljs-attr">marginTop</span>: <span class="hljs-string">"20px"</span> &#125;,
    <span class="hljs-attr">h1</span>: &#123; <span class="hljs-attr">fontWeight</span>: <span class="hljs-string">"bold"</span> &#125;
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.div&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.h1&#125;</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">7.使用 React context 减少 prop drilling</h2>
<p>React项目的另一个基本模式是使用<code>React Context</code>(<strong>特别是当你有一些共同的属性，你想要在你的组件中重用，并且你发现自己正在编写许多重复的prop时</strong>)。</p>
<p>例如，如果我们想跨多个组件共享用户数据，而不是多个重复的prop(称为props drilling 的模式)，我们可以使用<strong>React库中内置的上下文特性</strong>。</p>
<p>在我们的例子中，如果我们想要在Navbar和FeaturedPosts组件中重用用户数据，我们只需要将整个应用打包到provider组件中。</p>
<p>接下来，我们可以把用户数据传递到value prop上，并在<code>useContext</code> hook 的帮助下，在各个组件中使用这个上下文:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/App.js</span>

<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-keyword">const</span> UserContext = React.createContext();

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> user = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"Reed"</span> &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">UserContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;user&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">main</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Navbar</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"My Special App"</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">FeaturedPosts</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">main</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">UserContext.Provider</span>></span></span>
  );
&#125;

<span class="hljs-comment">// src/components/Navbar.js</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Navbar</span>(<span class="hljs-params">&#123; title &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> user = React.useContext(UserContext);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      &#123;user && <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/logout"</span>></span>Logout<span class="hljs-tag"></<span class="hljs-name">a</span>></span>&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-comment">// src/components/FeaturedPosts.js</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FeaturedPosts</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> posts = useFetchPosts();
  <span class="hljs-keyword">const</span> user = React.useContext(UserContext);

  <span class="hljs-keyword">if</span> (user) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      &#123;posts.map((post) => (
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;post.id&#125;</span>></span>&#123;post.title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">总结</h2>
<p>我希望，当你试图改进你自己的React代码，使其更清晰、更容易阅读，并最终更享受创建你的React项目时，这篇指南对你有用。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            