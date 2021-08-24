
---
title: '_重学 Next.js_  — 你应该知道的 Next.js 高级用法 10 点 （上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d9ad6ff0e044cdaab171f47f52a5d51~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 04:09:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d9ad6ff0e044cdaab171f47f52a5d51~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p>之前出过很多 Next.js 系列的文章，也因此收获了很多朋友，不敢说 Next.js 用的有多好，但是个人对于 Next.js 应该绝对算得上是真爱了。之前因为个人原因，Next.js 更多的是停留在用的阶段，并且因为工作原因，还有大概一年半的时间没用过 Next.js 写项目，最近随着经验和年限增加，回过头来看感觉有些意难平，希望重新拾起对 Next.js 的热情，因此准备了一个系列 —— 《重学 Next.js》，希望从更深的角度去重温这位老朋友。文章可能会分为几个方向，看感觉随机写：</p>
<ul>
<li>
<p>1 - 实践系列。比如高级用法、最佳实践以及新特性的使用等等。</p>
</li>
<li>
<p>2 - 源码系列。既然要更深入，那么源码就躲不过去，还是要啃的。</p>
</li>
<li>
<p>3 - 翻译系列。翻译国外很多大牛的文章，其实 <code>Next.js</code> 的受众，还是国外居多。<strong>如果是翻译，会先征得作者的同意</strong>。</p>
</li>
</ul>
<p>废话少说，开始第一篇文章，第一篇文章就简单的溜溜缝，在一年半之前最后使用 <code>Next.js</code> 更新的版本还是 Version 8，看一下官网他已经更新到了 Version 11，真的是非常感慨啊。有很多新特性都不清楚，所以从官网上找了一篇文章或者说文档更为准确，进行了一下翻译以及简单实用，理解自身的理解并且搭配 Demo，给大家说一下使用 <code>Next.js</code> 你应该掌握的 10 点高级用法。</p>
<blockquote>
<p>【注意】：如果觉得不喜欢看中文，或者就喜欢看原版，可以直接点击这里 —— <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvercel.com%2Fblog%2F10-next-js-tips-you-might-not-know" target="_blank" rel="nofollow noopener noreferrer" title="https://vercel.com/blog/10-next-js-tips-you-might-not-know" ref="nofollow noopener noreferrer">原文链接</a>，本文不是直译，会带有个人分析总结和代码。</p>
</blockquote>
<h2 data-id="heading-1">I - Next.js Redirects —— 重定向</h2>
<blockquote>
<p><strong>【版本】：</strong> >= Next.js Version 9.5</p>
<p><strong>【功能】：</strong> 将原路径重定向到一个新路径。</p>
<p><strong>【解释】：</strong> 原路径包含在你的应用内部任何可访问的路径，包括 <code>pages</code> 文件夹下的路由以及 <code>public</code> 文件夹下的静态资源。</p>
</blockquote>
<h3 data-id="heading-2">重要参数</h3>
<ul>
<li><code>source</code> ：传入的请求路径，也就是原路径</li>
<li><code>destination</code> 目标路径，也就是重定向到目标路径</li>
<li><code>permanent</code> 是否是永久重定向，如果为 <code>true</code> 就是永久重定向也就是 302，如果为 <code>false</code> 就是暂时的，也就是 301。</li>
</ul>
<blockquote>
<p>更多参数以及详细解释可以去看官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnextjs.org%2Fdocs%2Fapi-reference%2Fnext.config.js%2Fredirects" target="_blank" rel="nofollow noopener noreferrer" title="https://nextjs.org/docs/api-reference/next.config.js/redirects" ref="nofollow noopener noreferrer">Next.js Redirects</a></p>
</blockquote>
<h3 data-id="heading-3">示例代码</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// next.config.js</span>

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">redirects</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> [
      &#123;
        <span class="hljs-attr">source</span>: <span class="hljs-string">'/home'</span>,
        <span class="hljs-attr">destination</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">permanent</span>: <span class="hljs-literal">true</span>,
      &#125;,
    ]
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码，可以将 <code>/home</code> 路径重定向到 <code>/</code>，通过一个实际例子来看看效果。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d9ad6ff0e044cdaab171f47f52a5d51~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>熟悉 Next.js 的同学应该都知道，如上图所示，pages 文件夹就会被自动解析注册路由，那么现在我们整个系统里来说，其实只存在一个跟路径 <code>/</code>，并没有编写 <code>/home</code> 路由，正常来说如果没有使用 redirects 应该是 404，而现在我们是用了 redirects，看看是什么效果。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b5447969d6d4d11aed553451511dd9b~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-23 19.27.55.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，没有出现 404，而是输入 <code>/home</code> 直接帮我们进行了重定向，除此之外，还能进行多级路径匹配，功能很强大，感兴趣的可以自己去实际使用看看效果。</p>
<h2 data-id="heading-4">II - Next.js Rewrites —— 重写</h2>
<p>介绍完 Redirects 我们紧接着就来介绍一个官方也承认的和 Redirects 非常像的一个兄弟功能 —— Rewrites。</p>
<blockquote>
<p><strong>【版本】：</strong> >= Next.js Version 9.5</p>
<p><strong>【功能】：</strong> 将原路径充当代理以此来屏蔽目标路径。</p>
<p><strong>【解释】：</strong> 就是你看起来像是在访问目标路径，但实际上页面交互和效果都是原路径，简单来说就是用户无感知，因为重写并没有改变他们的在网站的位置。</p>
</blockquote>
<h3 data-id="heading-5">示例代码</h3>
<pre><code class="hljs language-js copyable" lang="js"> <Link href=<span class="hljs-string">"/list"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.card&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>List <span class="hljs-symbol">&rarr;</span><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>List 列表页.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>
 </Link>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/rewrites"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.card&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Rewrites <span class="hljs-symbol">&rarr;</span><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>路由 /rewrites.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Link</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// next.config.js</span>

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">rewrites</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> [
      &#123;
        <span class="hljs-attr">source</span>: <span class="hljs-string">'/rewrites'</span>,
        <span class="hljs-attr">destination</span>: <span class="hljs-string">'/list'</span>,
      &#125;
    ]
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，明确的是我们的路由系统没有 <code>/rewrites</code> 这个路由，有的是 <code>/list</code>，通过 Rewrites 把 <code>/rewrites</code> 重写成了 <code>/list</code> 对应的页面，来看一下效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2efaa70147694670943d868f8232e1f2~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-24 17.11.14.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以非常清楚地看到，我们访问一个路由系统里不存在的页面 <code>/rewrites</code>，原本应该是 404，但是因为我们对它进行了重写，所以最后呈现出来的是 <code>/list</code> 路由对应的页面。</p>
<h3 data-id="heading-6">Rewrites 和 Redirects 有什么区别呢？</h3>
<p>那么，看起来 Rewrites 和 Redirects 这俩兄弟功能做的事差不多啊，那么为啥还要做两个功能呢？这俩到底有啥区别呢？别着急，下面就来简单分析一下：</p>
<ul>
<li>表现形式不同</li>
</ul>
<p>仔细看上面两个 Demo 截图的效果，Redirects 和 Rewrites 从表现形式上来看有两点不同。</p>
<p>1 - 第一点：路径呈现效果不同，Redirects 呈现的是 destination 也就是目标路径，而 Rewrites 呈现的是 source 也就是元路径。</p>
<p>2 - 第二点：页面实际效果不同，Redirects 呈现的是一个类似刷新页面或者说 <code><a /></code> 标签的一个效果，看起来像脱离了站点，而 Rewrites 呈现的就是一个站内前端路由的一个效果，没有刷新跳转的过程。</p>
<blockquote>
<p>如果截图效果没看出来，大家可以自己亲自动手实践一下。</p>
</blockquote>
<ul>
<li>编译时调用时机不同</li>
</ul>
<p><code>Redirects</code> 是在检查整个文件系统 <code>pages</code> 和 <code>public</code> 之前调用。</p>
<p><code>Rewrites</code> 是在检查整个文件系统 <code>pages</code> 和 <code>public</code>  之后且在生成动态路由之前，进行调用。</p>
<p>上面这两句话可能看不太懂，没关系，我们还是通过代码来看看：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// next.config.js</span>

 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">redirects</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-keyword">return</span> [
     &#123;
       <span class="hljs-attr">source</span>: <span class="hljs-string">'/home'</span>,
       <span class="hljs-attr">destination</span>: <span class="hljs-string">'/'</span>,
       <span class="hljs-attr">permanent</span>: <span class="hljs-literal">true</span>,
     &#125;,
     &#123;
       <span class="hljs-attr">source</span>: <span class="hljs-string">'/rewrites'</span>,
       <span class="hljs-attr">destination</span>: <span class="hljs-string">'/list'</span>,
       <span class="hljs-attr">permanent</span>: <span class="hljs-literal">true</span>,
     &#125;
   ]
 &#125;,
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">rewrites</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-keyword">return</span> [
     &#123;
       <span class="hljs-attr">source</span>: <span class="hljs-string">'/rewrites'</span>,
       <span class="hljs-attr">destination</span>: <span class="hljs-string">'/list'</span>,
     &#125;
   ]
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，我们在 Redirects 和 Rewrites 都做了差不多的处理，在 Redirects 里我们把 <code>/rewrites</code> 重定向到 <code>/list</code>，在 Rewrites 里我们把 <code>/rewrites</code> 重写成 <code>/list</code>，那么通过最后页面的实际展现效果，我们也能知道二者的执行顺序，如果最后页面是 <code>/list</code>，那么就说明 Redirects 是后调用的，如果最后页面是 <code>/rewrites</code> 那么说明 Rewrites 是后调用的。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2efaa70147694670943d868f8232e1f2~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-24 17.11.14.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后的效果和上面总结的一样，说明 Redirects 是先被调用的，而 rewrites 是后被调用的，所以总结来说，虽然二者有很多相似的地方，但是存在着本质上的不同，所以还是两个 API，需要根据场景去使用。</p>
<h2 data-id="heading-7">III - Next.js Preview Mode —— 预览模式</h2>
<blockquote>
<p><strong>【版本】：</strong> >= Next.js Version 9.3</p>
<p><strong>【功能】：</strong> 针对 CMS 网站，做一些草稿提前预览的功能。</p>
<p><strong>【解释】：</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvercel.com%2Fdocs%2Fnext.js%2Fpreview-mode" target="_blank" rel="nofollow noopener noreferrer" title="https://vercel.com/docs/next.js/preview-mode" ref="nofollow noopener noreferrer">预览模式</a>允许开发人员在将静态生成的内容发布到 Web 之前查看它的草稿。Next.js 能够在请求时间而不是构建时间生成这些草稿页面，以便开发人员可以看到他们的内容在发布时的样子。</p>
</blockquote>
<p>预览模式的应用场景在平时开发过程中基本没怎么使用过，所以这里不做过多介绍，如果你恰好有类似的场景，比如 CMS，那么可以去官网查阅相关内容。对的没错就是这么随意，个人感觉应用场景不足，也没怎么使用过，介绍下来也不过是浪费时间，还不如去官网。</p>
<h2 data-id="heading-8">IV - Hooking into Build Process —— 构建过程钩子</h2>
<p>Next.js 是一个约定大于配置的框架，大部分的通用的基础功能 Next.js 框架本身已经帮开发者预置好了一套便捷可用方案，与此同时，如果你还是需要在构建时做一些额外的工作的话，那么 Next.js 也是支持的，它为开发者开了一个口子 —— <code>next.config.js</code>，在里面我们可以做诸如：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnextjs.org%2Fdocs%2Fapi-reference%2Fnext.config.js%2Fcustom-webpack-config" target="_blank" rel="nofollow noopener noreferrer" title="https://nextjs.org/docs/api-reference/next.config.js/custom-webpack-config" ref="nofollow noopener noreferrer">Webpack 配置</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleerob.io%2Fblog%2Fnextjs-sitemap-robots" target="_blank" rel="nofollow noopener noreferrer" title="https://leerob.io/blog/nextjs-sitemap-robots" ref="nofollow noopener noreferrer">创建站点地图</a>等。关于配置的详细信息，可以在此查看 -> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnextjs.org%2Fdocs%2Fapi-reference%2Fnext.config.js%2Fintroduction" target="_blank" rel="nofollow noopener noreferrer" title="https://nextjs.org/docs/api-reference/next.config.js/introduction" ref="nofollow noopener noreferrer">next.config.js 文档</a>。</p>
<h2 data-id="heading-9">V - Next.js with Preact</h2>
<p>众所周知，Next.js 是基于 React.js 的框架，但是其实 React.js 框架本身并不算轻量，如果你并不去及时的使用 React.js 的高级功能，只是使用 React.js 开发模式以及语法，那么 Next.js 支持将 React.js 切换成 Preact.js 来减小体积。</p>
<h3 data-id="heading-10">示例代码</h3>
<pre><code class="hljs language-json copyable" lang="json"> <span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-attr">"next"</span>: <span class="hljs-string">"11.1.0"</span>,
    <span class="hljs-attr">"preact"</span>: <span class="hljs-string">"^10.5.14"</span>,
    <span class="hljs-attr">"preact-render-to-string"</span>: <span class="hljs-string">"^5.1.19"</span>,
    <span class="hljs-attr">"react"</span>: <span class="hljs-string">"17.0.2"</span>,
    <span class="hljs-attr">"react-dom"</span>: <span class="hljs-string">"17.0.2"</span>
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// next.config.js</span>

 <span class="hljs-attr">webpack</span>: <span class="hljs-function">(<span class="hljs-params">config, &#123; dev &#125;</span>) =></span> &#123;
    <span class="hljs-comment">// Replace React with Preact only in client production build</span>
    <span class="hljs-keyword">if</span> (!dev) &#123;
      <span class="hljs-built_in">Object</span>.assign(config.resolve.alias, &#123;
        <span class="hljs-attr">react</span>: <span class="hljs-string">'preact/compat'</span>,
        <span class="hljs-string">'react-dom/test-utils'</span>: <span class="hljs-string">'preact/test-utils'</span>,
        <span class="hljs-string">'react-dom'</span>: <span class="hljs-string">'preact/compat'</span>
      &#125;);
    &#125;

    <span class="hljs-keyword">return</span> config;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过非常简单的配置，就可以完成 Preact 无缝替换 React，并且我们只需要在生产环境开启替换，所以也避免了开发过程就需要我们去熟悉掌握 Preact 相关知识这一问题，接着来直观对比一下二者的打包体积：</p>
<ul>
<li>React</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c732eb1af1d1486da85c9fe5d9785c09~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Preact</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ff82abda52249a38a671b0b4295d598~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>相同项目，核心 js 文件使用 React.js 比 Preact.js 单文件普遍大上 30 Kb 左右，当路由系统多了以后，几十个几百个页面，这个体积上的缩小还是十分可观的。</p>
<h2 data-id="heading-11">总结</h2>
<p>由于十点一起说完内容过多怕大家不容易消化，所以剩下的五点在下一篇文章给大家介绍，剩下的五点更加的有趣，敬请期待～</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FluffyZh%2Fnextjs-blogs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/luffyZh/nextjs-blogs" ref="nofollow noopener noreferrer">项目地址</a></p></div>  
</div>
            