
---
title: 'Next.js 是怎么做预渲染的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c06eb24944e4986b5516c904dbfb668~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 01:54:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c06eb24944e4986b5516c904dbfb668~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：<a href="https://juejin.cn/user/1380642337077933" target="_blank" title="https://juejin.cn/user/1380642337077933">逸恒</a></p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<p>打开 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnextjs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nextjs.org/" ref="nofollow noopener noreferrer">next.js</a> 官网，首先映入眼帘的是它的 Slogan 和介绍：</p>
<blockquote>
<p>The React Framework for Production</p>
<p>Next.js gives you the best developer experience with all the features you need for production: hybrid static & server rendering, TypeScript support, smart bundling, route pre-fetching, and more. No config needed.</p>
</blockquote>
<p>Next.js 提供了生产环境所需的所有功能以及最佳实践，包括构建时预渲染、服务端渲染、路由预加载、智能打包、零配置等。其中，Next.js 以其优秀的构建时渲染和服务端渲染能力，成为当今 React 生态中最受欢迎的框架之一。本文将介绍 Next.js 提供的三种预渲染模式以及混合渲染模式，来看看 Next.js 是怎么做预渲染的。</p>
<h1 data-id="heading-1">三种预渲染模式</h1>
<p>普通的单页应用只有一个 HTML，初次请求返回的 HTML 中没有任何页面内容，需要通过网络请求 JS bundle 并渲染，整个渲染过程都在客户端完成，所以叫客户端渲染（CSR）。这种渲染方式虽然在后续的页面切换速度很快，但是也明显存在两个问题：</p>
<ol>
<li>白屏时间过长：在 JS bundle 返回之前，页面一直是空白的。假如 bundle 体积过大或者网络条件不好的情况下，体验会更不好</li>
<li>SEO 不友好：搜索引擎访问页面时，只会看 HTML 中的内容，默认是不会执行 JS，所以抓取不到页面的具体内容</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c06eb24944e4986b5516c904dbfb668~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而 Next.js 提供的三种预渲染模式，均在 CSR 开始前，在服务端预先渲染出页面内容，避免出现白屏时间过长和 SEO 不友好的问题。</p>
<h2 data-id="heading-2">SSR</h2>
<p>为了解决上面出现的两个问题，SSR(Server Side Rendering)诞生了。相信大家对 SSR 不会陌生，它是在服务端直接实时同构渲染当前用户访问的页面，返回的 HTML 包含页面具体内容，提高用户的体验。React 从框架层面直接提供支持，只需要调用 <code>renderToString(Component)</code> 函数即可得到 HTML 内容。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6af1835f99fe481686659201ffd5ff16~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Next.js 提供 <code>getServerSideProps</code> 异步函数，以在 SSR 场景下获取额外的数据并返回给组件进行渲染。<code>getServerSideProps</code> 可以拿到每次请求的上下文（<code>Context</code>)，举个例子：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FirstPost</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-comment">// 在 props 中拿到数据</span>
  <span class="hljs-keyword">const</span> &#123; title &#125; = props;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Layout</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Layout</span>></span></span>
  )
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getServerSideProps</span>(<span class="hljs-params">context</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'context'</span>, context.req);
  <span class="hljs-comment">// 模拟获取数据</span>
  <span class="hljs-keyword">const</span> title = <span class="hljs-keyword">await</span> getTitle(context.req);
  <span class="hljs-comment">// 把数据放在 props 对象中返回出去</span>
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
      title
    &#125;
  &#125;
&#125;
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SSR 方案虽然解决了 CSR 带来的两个问题，但是同时又引入另一个问题：需要一个服务器承载页面的实时请求、渲染和响应，这无疑会<strong>增大服务端开发和运维的成本</strong>。另外对于一些较为静态场景，比如博客、官网等，它们的内容相对来说比较确定，变化不频繁，每次通过服务端<strong>渲染出来的内容都是一样的</strong>，无疑浪费了很多没必要的服务器资源。这时，有没有一种方案可以让这些页面变得静态呢？这时，静态站点生成（SSG，也叫构建时预渲染）诞生了。</p>
<h2 data-id="heading-3">SSG</h2>
<p>SSG(Static Site Generation) 是指在应用编译构建时预先渲染页面，并生成静态的 HTML。把生成的 HTML 静态资源部署到服务器后，浏览器不仅首次能请求到带页面内容的 HTML ，而且不需要服务器实时渲染和响应，大大节约了服务器运维成本和资源。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c52bb0c7c2eb4c6c95faaacd37b26aba~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Next.js 默认为每个页面开启 SSG。对于页面内容需要依赖静态数据的场景，允许在每个页面中 <code>export</code> 一个 <code>getStaticProps</code> 异步函数，在这个函数中可以把该页面组件所需要的数据收集并返回。当 <code>getStaticProps</code> 函数执行完成后，页面组件就能在 <code>props</code> 中拿到这些数据并执行静态渲染。举个在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnextjs.org%2Fdocs%2Frouting%2Fintroduction" target="_blank" rel="nofollow noopener noreferrer" title="https://nextjs.org/docs/routing/introduction" ref="nofollow noopener noreferrer">静态路由</a>中使用 SSG 的例子：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// pages/posts/first-post.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Post</span>(<span class="hljs-params">props</span>) </span>&#123;
<span class="hljs-keyword">const</span> &#123; postData &#125; = props;
  
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;postData.title&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getStaticProps</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 模拟获取静态数据</span>
<span class="hljs-keyword">const</span> postData = <span class="hljs-keyword">await</span> getPostData();
  <span class="hljs-keyword">return</span> &#123;
  <span class="hljs-attr">props</span>: &#123; postData &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnextjs.org%2Fdocs%2Frouting%2Fdynamic-routes" target="_blank" rel="nofollow noopener noreferrer" title="https://nextjs.org/docs/routing/dynamic-routes" ref="nofollow noopener noreferrer">动态路由</a>的场景，Next.js 是如何做 SSG 的呢？Next.js 提供 <code>getStaticPaths</code> 异步函数，在这个方法中，会返回一个 <code>paths</code> 数组，这个数组包含了这个动态路由在构建时需要预渲染的页面数据。举个例子：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// pages/posts/[id].js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Post</span>(<span class="hljs-params">props</span>) </span>&#123;
<span class="hljs-keyword">const</span> &#123; postData &#125; = props;
  
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;postData.title&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getStaticPaths</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 返回该动态路由可能会渲染的页面数据，比如 params.id</span>
  <span class="hljs-keyword">const</span> paths = [
    &#123;
      <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'ssg-ssr'</span> &#125;
    &#125;,
    &#123;
      <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'pre-rendering'</span> &#125;
    &#125;
  ]
  <span class="hljs-keyword">return</span> &#123;
    paths,
    <span class="hljs-comment">// 命中尚未生成静态页面的路由直接返回 404 页面</span>
    <span class="hljs-attr">fallback</span>: <span class="hljs-literal">false</span>
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getStaticProps</span>(<span class="hljs-params">&#123; params &#125;</span>) </span>&#123;
  <span class="hljs-comment">// 使用 params.id 获取对应的静态数据</span>
  <span class="hljs-keyword">const</span> postData = <span class="hljs-keyword">await</span> getPostData(params.id)
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
      postData
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们执行 <code>nextjs build</code> 后，可以看到打包结果包含 <code>pre-rendering.html</code> 和 <code>ssg-ssr.html</code> 两个 HTML 页面，也就是说在执行 SSG 时，会对 <code>getStaticPaths</code> 函数返回的 <code>paths</code> 数组进行循环，逐一预渲染页面组件并生成 HTML。</p>
<pre><code class="hljs language-markdown copyable" lang="markdown">├── server
|  ├── chunks
|  ├── pages
|  |  ├── api
|  |  ├── index.html
|  |  ├── index.js
|  |  ├── index.json
|  |  └── posts
|  |     ├── [id].js
|  |     ├── first-post.html
|  |     ├── first-post.js
|  |     ├── pre-rendering.html       # 预渲染生成 pre-rendering 页面
|  |     ├── pre-rendering.json
|  |     ├── ssg-ssr.html             # 预渲染生成 ssg-ssr 页面
|  |     └── ssg-ssr.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SSG 虽然很好解决了白屏时间过长和 SEO 不友好的问题，但是它仅仅适合于页面内容较为静态的场景，比如官网、博客等。面对<strong>页面数据更新频繁</strong>或<strong>页面数量很多</strong>的情况，它似乎显得有点束手无策，毕竟在静态构建时不能拿到最新的数据和无法枚举海量页面。这时，就需要增量静态再生成(Incremental Static Regeneration)方案了。</p>
<h2 data-id="heading-4">ISR</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10622b56fb3c47559cfa5259d8356d3d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Next.js 推出的 ISR(Incremental Static Regeneration) 方案，允许<strong>在应用运行时再重新生成每个页面 HTML，而不需要重新构建整个应用</strong>。这样即使有海量页面，也能使用上 SSG 的特性。一般来说，使用 ISR 需要 <code>getStaticPaths</code> 和 <code>getStaticProps</code> 同时配合使用。举个例子：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// pages/posts/[id].js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Post</span>(<span class="hljs-params">props</span>) </span>&#123;
<span class="hljs-keyword">const</span> &#123; postData &#125; = props;
  
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;postData.title&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getStaticPaths</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> paths = <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">'https://.../posts'</span>);
  <span class="hljs-keyword">return</span> &#123;
    paths,
    <span class="hljs-comment">// 页面请求的降级策略，这里是指不降级，等待页面生成后再返回，类似于 SSR</span>
    <span class="hljs-attr">fallback</span>: <span class="hljs-string">'blocking'</span>
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getStaticProps</span>(<span class="hljs-params">&#123; params &#125;</span>) </span>&#123;
  <span class="hljs-comment">// 使用 params.id 获取对应的静态数据</span>
  <span class="hljs-keyword">const</span> postData = <span class="hljs-keyword">await</span> getPostData(params.id)
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
      postData
    &#125;,
    <span class="hljs-comment">// 开启 ISR，最多每10s重新生成一次页面</span>
    <span class="hljs-attr">revalidate</span>: <span class="hljs-number">10</span>,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在应用编译构建阶段，会生成已经确定的静态页面，和上面 SSG 执行流程一致。</p>
<p>在 <code>getStaticProps</code> 函数返回的对象中增加 <code>revalidate</code> 属性，表示开启 ISR。在上面的例子中，指定 <code>revalidate = 10</code>，表示最多10秒内重新生成一次静态 HTML。当浏览器请求已在构建时渲染生成的页面时，首先返回的是缓存的 HTML，10s 后页面开始重新渲染，页面成功生成后，更新缓存，浏览器再次请求页面时就能拿到最新渲染的页面内容了。</p>
<p>对于浏览器请求构建时未生成的页面时，会马上生成静态 HTML。在这个过程中，<code>getStaticPaths</code> 返回的 <code>fallback</code> 字段有以下的选项：</p>
<ul>
<li><code>fallback: 'blocking'</code>：不降级，并且要求用户请求一直等到新页面静态生成结束，静态页面生成结束后会缓存</li>
<li><code>fallback: true</code>：降级，先返回降级页面，当静态页面生成结束后，会返回一个 JSON 供降级页面 CSR 使用，经过二次渲染后，完整页面出来了</li>
</ul>
<p>在上面的例子中，使用的是不降级方案(<code>fallback: 'blocking'</code>)，实际上和 SSR 方案有相似之处，都是阻塞渲染，只不过多了缓存而已。</p>
<blockquote>
<p>If fallback is 'blocking', new paths not returned by getStaticPaths will wait for the HTML to be generated, identical to SSR (hence why blocking), and then be cached for future requests so it only happens once per path.</p>
</blockquote>
<p>也不是所有场景都适合使用 ISR。对于实时性要求较高的场景，比如新闻资讯类的网站，可能 SSR 才是最好的选择。</p>
<h1 data-id="heading-5">混合渲染模式</h1>
<p>Next.js 不仅支持 SSR、SSG、CSR、ISR，还支持渲染模式的混合使用。下面将介绍三种混合渲染模式。</p>
<h2 data-id="heading-6">SSR + CSR</h2>
<p>上面已经提及过，SSR 似乎已经解决了 CSR 带来的问题，那是不是 CSR 完全没有用武之地呢？其实并不是。使用 CSR 时，页面切换无需刷新，无需重新请求整个 HTML 的内容。既然如此，可以各取所长，各补其短，于是就有 SSR + CSR 的方案：</p>
<ul>
<li>首次加载页面走 SSR：保证首屏加载速度的同时，并且满足 SEO 的诉求</li>
<li>页面切换走 CSR：Next.js 会发起一次网络请求，执行 <code>getServerSideProps</code> 函数，拿到它返回的数据后，进行页面渲染</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59482eb5b37e4ba79eb02015679a7bc6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>二者的有机结合，大大减少后端服务器的压力和成本的同时，也能提高页面切换的速度，进一步提升用户的体验。除了 Next.js，还有其他的框架也使用 SSR + CSR 方案，比如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2Fice" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/ice" ref="nofollow noopener noreferrer">ice.js</a> 等。</p>
<h2 data-id="heading-7">SSG + CSR</h2>
<p>在上面已提及过，SSR 需要较高的服务器运维成本。对于某些静态网站或者实时性要求较低的网站来说，是没有必要使用 SSR 的。假如用 SSG 代替 SSR，使用 SSG + CSR 方案，是不是会更好：</p>
<ul>
<li>静态内容走 SSG：对于页面中较为静态的内容，比如导航栏、布局等，可以在编译构建时预先渲染静态 HTML</li>
<li>动态内容走 CSR：一般会在 <code>useEffect</code> 中请求接口获取动态数据，然后进行页面重新渲染</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24479c9b6e6f4b178560756265502b8c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然从体验来说，动态内容需要页面重新渲染后才能出现，体验上没有 SSR 好，但是避免 SSR 带来的高额服务器成本的同时，也能保证首屏渲染时间不会太长，相比纯 CSR 来说，还是提升了用户体验。</p>
<h2 data-id="heading-8">SSG + SSR</h2>
<p>在上面介绍的 ISR 方案时提及过，ISR 的实质是 SSG + SSR：</p>
<ul>
<li>静态内容走 SSG：编译构建时把相对静态的页面预先渲染生成 HTML，浏览器请求时直接返回静态 HTML</li>
<li>动态内容走 SSR：浏览器请求未预先渲染的页面，在运行时通过 SSR 渲染生成页面，然后返回到浏览器，并缓存静态 HTML，下次命中缓存时直接返回</li>
</ul>
<p>ISR 相比于 SSG + CSR 来说，动态内容可以直接直出，进一步提升了首次访问页面时的体验；相比于 SSR + CSR 来说，减少没必要的静态页面渲染，节省了一部分后端服务器成本。</p>
<h1 data-id="heading-9">总结</h1>
<p>本文首先介绍了 Next.js 提供的三种预渲染模式：SSR、SSG、ISR，并分别说明了它们的优缺点以及可能适用于哪些场景。后面介绍了 Next.js 目前支持的三种混合渲染模式，并和其他的渲染模式进行对比。</p>
<p>总的来说，没有十全十美的渲染方案，都需要根据实际场景进行权衡和取舍。</p>
<p>参考链接：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnextjs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nextjs.org/" ref="nofollow noopener noreferrer">Next.js 官方文档</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIwMTM5MTM1NA%3D%3D%26mid%3D2649473870%26idx%3D1%26sn%3D743cf2a440aff2fcccf82158b647bace%26chksm%3D8ef1cedbb98647cde09a99ae04a5d56406afd2d8c4dda0dd7689e0a77fb918598466227ba2c3%26cur_album_id%3D1557816410599407616%26scene%3D189%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzIwMTM5MTM1NA==&mid=2649473870&idx=1&sn=743cf2a440aff2fcccf82158b647bace&chksm=8ef1cedbb98647cde09a99ae04a5d56406afd2d8c4dda0dd7689e0a77fb918598466227ba2c3&cur_album_id=1557816410599407616&scene=189#rd" ref="nofollow noopener noreferrer">《从 Next.js 看企业级框架的 SSR 支持》</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F365113639" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/365113639" ref="nofollow noopener noreferrer">《新一代 Web 建站技术展的演进：SSR、SSG、ISR、DPR 都在做什么？》</a></li>
</ul></div>  
</div>
            