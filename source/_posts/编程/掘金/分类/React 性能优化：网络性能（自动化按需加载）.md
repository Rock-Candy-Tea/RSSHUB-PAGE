
---
title: 'React 性能优化：网络性能（自动化按需加载）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73d2f3c1154d49cc802ce3226c420022~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 18:56:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73d2f3c1154d49cc802ce3226c420022~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 11 天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8 月更文挑战</a></p>
<p>在性能优化中，有一块很重要的部分 -- <strong>网络性能优化（自动化按需加载）</strong>。</p>
<p>什么是自动化按需加载呢？在应用加载的过程中，我们不会将所有的资源一次性加载到前端；而是选择在切换页面/功能时，再加载其相关的资源。</p>
<p><strong>如何在 React 中实现按需加载？</strong></p>
<ul>
<li>使用 Webpack 提供的 <code>import</code> API，实现模块按需切割加载的功能。</li>
<li>使用 <code>react-loadable</code> 库实现 React 异步加载。</li>
</ul>
<h2 data-id="heading-0">代码分割</h2>
<h3 data-id="heading-1">打包</h3>
<p>打包是一个将文件引入并合并到一个单独文件的过程，最终形成一个 “bundle”。接着在页面上引入该 bundle，整个应用即可一次性加载。</p>
<ul>
<li>App 文件：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">import</span> &#123; add &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./math.js'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">16</span>, <span class="hljs-number">26</span>)); <span class="hljs-comment">// 42</span>
<span class="hljs-comment">// math.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>打包后文件：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;

<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">16</span>, <span class="hljs-number">26</span>)); <span class="hljs-comment">// 42</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">代码分割</h3>
<p>随着应用迭代/完善，你的代码包也将随之增长，尤其是在整合了体积巨大的第三方库的情况下；此时，需要思考如何避免因体积过大而导致加载时间过长？</p>
<p>为了避免搞出大体积的代码包，在前期就思考代码分割是个不错的选择。代码分割能够提供“Lazy Loading （懒加载）” -- 只加载当前用户所需要的内容，这可以显著地提高应用性能。尽管并没有减少应用整体的代码体积，但可以避免加载用户永远不需要的代码，并在初始加载的时候减少所需加载的代码量。</p>
<h3 data-id="heading-3">import()</h3>
<p>引入代码分割的最佳方式是通过动态 <code>import()</code> 语法。</p>
<ul>
<li>使用之前：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; add &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./math'</span>;

<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">16</span>, <span class="hljs-number">26</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用之后：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span>(<span class="hljs-string">'./math'</span>).then(<span class="hljs-function">(<span class="hljs-params">math</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(math.add(<span class="hljs-number">16</span>, <span class="hljs-number">26</span>));
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 <code>Webpack</code> 解析到该语法时，会自动进行代码分割。如果你使用 <code>Create React App</code>，该功能已开箱即用，你可以立刻使用该特性。<code>Next.js</code> 也已支持该特性而无需进行配置。</p>
<h2 data-id="heading-4">React Loadable</h2>
<p><code>React Loadable</code> 是一个很小的库，<code>Loadable </code>是一个高阶组件用来轻易地在组件层面拆分 bundle。</p>
<h3 data-id="heading-5">安装</h3>
<pre><code class="copyable">yarn add react-loadable
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Loadable</code> 的用法很简单。你仅仅要做的就是把要加载的组件和当你加载组件时的 <code>Loading</code> 组件传入一个方法中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Loadable <span class="hljs-keyword">from</span> <span class="hljs-string">'react-loadable'</span>;
<span class="hljs-keyword">import</span> Loading <span class="hljs-keyword">from</span> <span class="hljs-string">'./my-loading-component'</span>;

<span class="hljs-keyword">const</span> LoadableComponent = Loadable(&#123;
  <span class="hljs-attr">loader</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./my-component'</span>),
  <span class="hljs-attr">loading</span>: Loading,
&#125;);

<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">LoadableComponent</span> /></span></span>;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">实战</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73d2f3c1154d49cc802ce3226c420022~tplv-k3u1fbpfcp-watermark.image" alt="lazy.gif" loading="lazy" referrerpolicy="no-referrer">
我们在之前的项目基础上，添加按需加载。可以看到，在之前的项目中切换不同的 Tab，Network 的资源加载是不会新增，也就是说所有的资源在一开始都加载进来了。</p>
<p>对于组件的代码是无需改动的，我们只需在路由中配置按需加载。</p>
<p>首先引入 <code>Loadable</code>，将静态导入改造为动态导入（<code>() => import('./pages/xxx')</code>），最后返回高级函数（<code>Loadable</code>）处理后的组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// App.js</span>
<span class="hljs-keyword">import</span> Loadable <span class="hljs-keyword">from</span> <span class="hljs-string">'react-loadable'</span>;

<span class="hljs-keyword">const</span> routers = [
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Form'</span>,
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/form'</span>,
    <span class="hljs-attr">loader</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./pages/form'</span>),
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'DynamicForm'</span>,
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/dynamic-form'</span>,
    <span class="hljs-attr">loader</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./pages/dynamicForm'</span>),
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Multiple Request'</span>,
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/multiple-request'</span>,
    <span class="hljs-attr">loader</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./pages/multipleRequest'</span>),
  &#125;,
  <span class="hljs-comment">// ...</span>
];

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Loading</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Loading...<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;

&#123;
  routers.map(<span class="hljs-function">(<span class="hljs-params">&#123; path, loader &#125;</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> Component = Loadable(&#123;
      loader,
      <span class="hljs-attr">loading</span>: Loading,
    &#125;);
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;path&#125;</span> <span class="hljs-attr">path</span>=<span class="hljs-string">&#123;path&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Component</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">Route</span>></span></span>
    );
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">效果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4dcfd82761343c8a15a7693ba13d00c~tplv-k3u1fbpfcp-watermark.image" alt="import.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>切换项目 Tab 时，Network 中加载了新的文件，这个文件就是 Tab 页相关的资源。</p>
<p>借助 chrome 的开发者工具，我们调慢网速来看一下 <code>loading</code> 状态。<code>loading</code> 显示正常 OK。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e51af78218cd4852b31efdccdfbcc45d~tplv-k3u1fbpfcp-watermark.image" alt="network.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>【不知道如何用 chrome 开发者工具 调整网速的小伙伴，看这里 ⬇️】</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02a2394ba75e4d06a80966194c19041e~tplv-k3u1fbpfcp-watermark.image" alt="network-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce2c082a9f344e04ae4cad079e15606c~tplv-k3u1fbpfcp-watermark.image" alt="network-2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">代码</h3>
<p>完整项目代码，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpinkqq%2Freact-antd%2Fblob%2Fmain%2Fsrc%2FApp.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pinkqq/react-antd/blob/main/src/App.js" ref="nofollow noopener noreferrer">看这里</a></p>
<h2 data-id="heading-9">参考资料</h2>
<ul>
<li>React 顶层 API：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fdocs%2Freact-api.html" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/docs/react-api.html" ref="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/react-…</a></li>
<li>用于数据获取的 Suspense（试验阶段）：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fdocs%2Fconcurrent-mode-suspense.html" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/docs/concurrent-mode-suspense.html" ref="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/concur…</a></li>
<li>代码分割：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fdocs%2Fcode-splitting.html" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/docs/code-splitting.html" ref="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/code-s…</a></li>
<li>react-loadable：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Freact-loadable" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/react-loadable" ref="nofollow noopener noreferrer">github.com/jamiebuilds…</a></li>
</ul>
<h2 data-id="heading-10">React 性能优化</h2>
<ul>
<li><a href="https://juejin.cn/post/6994631574515892238" target="_blank" title="https://juejin.cn/post/6994631574515892238">React 性能优化：性能永远是第一需求</a></li>
<li><a href="https://juejin.cn/post/6995000587620204574" target="_blank" title="https://juejin.cn/post/6995000587620204574">React 性能优化：网络性能（自动化按需加载）</a></li>
</ul></div>  
</div>
            