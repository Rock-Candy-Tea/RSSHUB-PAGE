
---
title: 'React SSR 服务器渲染原理解析与实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/188e07025e5b4c8dbd8a760f2e024d7a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 01:32:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/188e07025e5b4c8dbd8a760f2e024d7a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、为什么使用服务器端渲染？</h1>
<h3 data-id="heading-1">1. 客户端渲染</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/188e07025e5b4c8dbd8a760f2e024d7a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">2.服务器端渲染</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35db351b22ec4dd3a020d3c838ee163b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">3.  使用 SSR 技术的主要因素</h3>
<ul>
<li>首屏等待: <em><strong>CSR 项目的 TTFP（Time To First Page）时间比较长</strong></em></li>
<li>SEO : <em><strong>CSR 项目的 SEO 能力极弱</strong></em></li>
</ul>
<h3 data-id="heading-4">4. React SSR 流程</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd09dc823947471a9749bd5db622addd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5"><strong>SSR 之所以能够实现，本质上是因为虚拟 DOM 的存在</strong></h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d09eb21a3afa4b779344f15f40d90ef8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">二、同构</h1>
<blockquote>
<p>概念：一套React 代码 在服务器端执行一次，在客户端再执行一次</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// /containers/Home</span>

<span class="hljs-keyword">const</span> Home = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>This is allValue!<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>&#123;alert('click1')&#125;&#125;>
                click
            <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按上面的操作给button 绑定click事件，服务器端渲染，click没有绑定上,
所以 需要在 客户端 再渲染一遍 把事件等 绑定上</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> nodeExternals = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-node-externals'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// 一旦发现是核心模块，不必把模块的代码合并到最终生成的代码中</span>
    <span class="hljs-attr">target</span>: <span class="hljs-string">'node'</span>,
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>,
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    <span class="hljs-comment">// 因为 Node 环境下通过 NPM 已经安装了这些包，直接引用就可以，不需要额外再打包到代码里</span>
    <span class="hljs-attr">externals</span>: [nodeExternals()],
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.js?$/</span>,
            loader: <span class="hljs-string">'babel-loader'</span>,
            <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>,
            options: &#123;
                <span class="hljs-attr">presets</span>: [<span class="hljs-string">'react'</span>, <span class="hljs-string">'stage-0'</span>, [<span class="hljs-string">'env'</span>, &#123;
                    <span class="hljs-attr">targets</span>: &#123;
                        <span class="hljs-attr">browsers</span>: [<span class="hljs-string">'last 2 versions'</span>]
                    &#125;
                &#125;]]
            &#125;
        &#125;]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src.index.js</span>

<span class="hljs-keyword">import</span> express <span class="hljs-keyword">from</span> <span class="hljs-string">'express'</span>;
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'./containers/Home'</span>;
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; renderToString &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom/server'</span>;

<span class="hljs-keyword">const</span> app = express();
app.use(express.static(<span class="hljs-string">'public'</span>));
<span class="hljs-keyword">const</span> content = renderToString(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Home</span> /></span></span>);

app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res</span>) </span>&#123;
  res.send(<span class="hljs-string">`
        <html>
            <head>
                <title>ssr</title>
            </head>
            <body>
                <span class="hljs-subst">$&#123;content&#125;</span>
                <script src='/index.js'></script>
            </body>
        </html>
  `</span>);
&#125;);

<span class="hljs-keyword">var</span> server = app.listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">三、在SSR框架中引入路由机制</h1>
<ul>
<li>实现 React 的 SSR 架构，我们需要让相同的 React 代码在客户端和服务器端各执行一次。这里说的相同的 React 代码，指的是我们写的各种组件代码,所以在同构中，只有组件的代码是可以公用的。</li>
</ul>
<h3 data-id="heading-8">路由为什么没有办法公用？</h3>
<p>其实原因很简单，在服务器端需要通过请求路径，找到路由组件，而在客户端需通过浏览器中的网址，找到路由组件，是完全不同的两套机制，所以这部分代码是肯定无法公用。我们来看看在 SSR 中，前后端路由的实现代码：</p>
<h3 data-id="heading-9">客户端路由：</h3>
<p>客户端路由代码非常简单，大家一定很熟悉，BrowserRouter 会自动从浏览器地址中，匹配对应的路由组件显示出来。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span>
    )
&#125;

ReactDom.render(<span class="hljs-tag"><<span class="hljs-name">App</span>/></span>, document.querySelector('#root'))
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 BrowserRouter 我们能够匹配到浏览器即将显示的路由组件，对浏览器来说，我们需要把组件转化成 DOM，所以需要我们使用 ReactDom.render 方法来进行 DOM 的挂载。</p>
<h3 data-id="heading-10">服务器端路由：</h3>
<p>服务器端路由代码相对要复杂一点，需要你把 location（当前请求路径）传递给 StaticRouter 组件，这样 StaticRouter 才能根据路径分析出当前所需要的组件是谁。</p>
<blockquote>
<p>PS：StaticRouter 是 React-Router 针对服务器端渲染专门提供的一个路由组件。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">StaticRouter</span> <span class="hljs-attr">location</span>=<span class="hljs-string">&#123;req.path&#125;</span> <span class="hljs-attr">context</span>=<span class="hljs-string">&#123;context&#125;</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">StaticRouter</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span>
&#125;

Return ReactDom.renderToString(<span class="hljs-tag"><<span class="hljs-name">App</span>/></span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>StaticRouter 能够在服务器端匹配到将要显示的组件，对服务器端来说，我们要把组件转化成字符串，这时我们只需要调用 ReactDom 提供的 renderToString 方法，就可以得到 App 组件对应的 HTML 字符串。</p>
<h3 data-id="heading-11">为了方便统一管理，实际的路由配置是这样的</h3>
<p>细节部分可以看它 --> 👉 <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactrouter.com%2Fweb%2Fguides%2Fserver-rendering" target="_blank" rel="nofollow noopener noreferrer" title="https://reactrouter.com/web/guides/server-rendering" ref="nofollow noopener noreferrer">reactrouter.com/web/guides/…</a></p>
<pre><code class="hljs language-js copyable" lang="js">routes: [

    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">component</span>: Home,
        <span class="hljs-attr">exact</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">loadData</span>: Home.loadData,
        <span class="hljs-attr">key</span>: <span class="hljs-string">'home'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/goods'</span>,
        <span class="hljs-attr">component</span>: Goods,
        <span class="hljs-attr">exact</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">loadData</span>: Goods.loadData,
        <span class="hljs-attr">key</span>: <span class="hljs-string">'goods'</span>
    &#125;,
    &#123;
         ...xxxx

    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'*'</span>,
        <span class="hljs-attr">component</span>: NotFound,
        <span class="hljs-attr">exact</span>: <span class="hljs-literal">true</span>,
    &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">四、Node 中间层</h1>
<p>在 SSR 架构中，一般 Node 只是一个中间层，用来做 React 代码的服务器端渲染，而 Node 需要的数据通常由 API 服务器单独提供。</p>
<p>这样做一是为了工程解耦，二也是为了规避 Node 服务器的一些计算性能问题（？为什么不适合密集型计算，这个观点正确吗，能解决吗）</p>
<p>io异步完成的处理，是需要通过轮询队列去返回数据给到客户端的，但是这个过程是需要主线程是执行。由于密集型计算的任务，会阻塞主线程，导致无法及时响应异步队列的任务。</p>
<p>解决方法，通过 child_process 等方式，启用多进程或多线程来处理 CPU 密集型的任务，所以以上的方式是很早以前的观点</p>
<p>处理组件当中的数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Home</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">componentWillMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.staticContext) &#123;
            <span class="hljs-built_in">this</span>.props.staticContext.css.push(styles._getCss());
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            ...
        )
    &#125;
&#125;

Home.loadData = <span class="hljs-function">(<span class="hljs-params">store</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> store.dispatch(getHomeList())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 服务端对数据的处理</span>
<span class="hljs-comment">// matchedRoutes 是当前路由对应的所有需要显示的组件集合</span>

matchedRoutes.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (item.route.loadData) &#123;
        <span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            item.route.loadData(store).then(resolve).catch(resolve);
        &#125;)
        promises.push(promise);
    &#125;
&#125;)
<span class="hljs-built_in">Promise</span>.all(promises).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// TODO 生成 HTML 逻辑</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">五、CSS 的处理</h1>
<p>当我们的 React 代码中引入了一些 CSS 样式代码时，服务器端打包的过程会处理一遍 CSS，而客户端又会处理一遍。查看配置，我们可以看到，服务器端打包时我们用了 isomorphic-style-loader，它处理 CSS 的时候，只在对应的 DOM 元素上生成 class 类名，然后返回生成的 CSS 样式代码。</p>
<p>而在客户端代码打包配置中，我们使用了 css-loader 和 style-loader，css-loader 不但会在 DOM 上生成 class 类名，解析好的 CSS 代码，还会通过 style-loader 把代码挂载到页面上。不过这么做，由于页面上的样式实际上最终是由客户端渲染时添加上的，所以页面可能会存在一开始没有样式的情况，为了解决这个问题， 我们可以在服务器端渲染时，拿到 isomorphic-style-loader 返回的样式代码，然后以字符串的形式添加到服务器端渲染的 HTML 之中</p>
<h3 data-id="heading-14">客户端</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 客户端webpack配置</span>
<span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [&#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css?$/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
                <span class="hljs-attr">importLoaders</span>: <span class="hljs-number">1</span>,
                <span class="hljs-attr">modules</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">localIdentName</span>: <span class="hljs-string">'[name]_[local]_[hash:base64:5]'</span>
            &#125;
        &#125;]
    &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">服务端</h3>
<p>我们可以在服务器端渲染时，拿到 isomorphic-style-loader 返回的样式代码，然后以字符串的形式添加到服务器端渲染的 HTML 之中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [&#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css?$/</span>,
        use: [<span class="hljs-string">'isomorphic-style-loader'</span>, &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
                <span class="hljs-attr">importLoaders</span>: <span class="hljs-number">1</span>,
                <span class="hljs-attr">modules</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">localIdentName</span>: <span class="hljs-string">'[name]_[local]_[hash:base64:5]'</span>
            &#125;
        &#125;]
    &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> context = &#123;<span class="hljs-attr">css</span>: []&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> render = <span class="hljs-function">(<span class="hljs-params">store, routes, req, context</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> content = renderToString((
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">StaticRouter</span> <span class="hljs-attr">location</span>=<span class="hljs-string">&#123;req.path&#125;</span> <span class="hljs-attr">context</span>=<span class="hljs-string">&#123;context&#125;</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                    &#123;renderRoutes(routes)&#125;
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">StaticRouter</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
    ));
    <span class="hljs-keyword">const</span> cssStr = context.css.length ? context.css.join(<span class="hljs-string">'\n'</span>) : <span class="hljs-string">''</span>;
    
    <span class="hljs-keyword">return</span> <span class="hljs-string">`
        <html>
            <head>
                <title>ssr</title>
                <style><span class="hljs-subst">$&#123;cssStr&#125;</span></style>
            </head>
            <body>
                ...
            </body>
        </html>
    `</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Home</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">componentWillMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.staticContext) &#123;
            <span class="hljs-built_in">this</span>.props.staticContext.css.push(styles._getCss());
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">服务端直出时资源的搜集</h3>
<p>服务端输出<code>html</code>时，需要定义好<code>css</code>资源、<code>js</code>资源，让客户端接管后下载使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我们项目中的处理方式</span>
<span class="hljs-keyword">import</span> &#123; ChunkExtractor &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@loadable/server'</span>;
<span class="hljs-keyword">import</span> &#123; ServerStyleSheet &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>;

<span class="hljs-keyword">const</span> extractor = <span class="hljs-keyword">new</span> ChunkExtractor(&#123; statsFile &#125;);
....
<span class="hljs-keyword">const</span> &#123; routerPath, search &#125; = <span class="hljs-built_in">this</span>.baseData || &#123;&#125;;
<span class="hljs-keyword">const</span> sheet = <span class="hljs-keyword">new</span> ServerStyleSheet();

<span class="hljs-keyword">const</span> jsx = extractor.collectChunks(
    sheet.collectStyles(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">StaticRouter</span> <span class="hljs-attr">location</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">pathname:</span> <span class="hljs-attr">routerPath</span>, <span class="hljs-attr">search</span> &#125;&#125;></span>
            <span class="hljs-tag"><<span class="hljs-name">App</span>
                <span class="hljs-attr">i18nLang</span>=<span class="hljs-string">&#123;this.i18nLang&#125;</span>
                <span class="hljs-attr">pathname</span>=<span class="hljs-string">&#123;routerPath&#125;</span>
                <span class="hljs-attr">initialData</span>=<span class="hljs-string">&#123;this.baseData&#125;</span>
                <span class="hljs-attr">routeList</span>=<span class="hljs-string">&#123;routeList&#125;</span>
            /></span>
        <span class="hljs-tag"></<span class="hljs-name">StaticRouter</span>></span></span>,
    ),
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">六、 数据的脱水和注水</h1>
<h3 data-id="heading-18">在服务器注水：</h3>
<p>把数据作为 window.context 注入到 window 上面成为注水</p>
<h3 data-id="heading-19">在客户端脱水：</h3>
<p>客户端取数据使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 注水</span>
<span class="hljs-comment">// utils.js</span>
<script>
    <span class="hljs-built_in">window</span>.context = &#123;
        <span class="hljs-attr">store</span>:$&#123;<span class="hljs-built_in">JSON</span>.stringify(store.getState())&#125;
    &#125;
</script>

<span class="hljs-comment">//脱水</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getClientStore = <span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">const</span> defaultState = <span class="hljs-built_in">window</span>.context.store;
    <span class="hljs-keyword">return</span> createStore(
        reducer, defaultState, applyMiddleware(thunk)
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">七、SSR 中异步数据的获取 + Redux 的使用</h1>
<h2 data-id="heading-21">客户端渲染中</h2>
<p>异步数据结合 Redux 的使用方式遵循下面的流程（对应图中第 12 步）：</p>
<ol>
<li>创建 Store</li>
<li>根据路由显示组件</li>
<li>派发 Action 获取数据</li>
<li>更新 Store 中的数据</li>
<li>组件 Rerender</li>
</ol>
<h2 data-id="heading-22">服务器端</h2>
<p>页面一旦确定内容，就没有办法 Rerender 了，这就要求组件显示的时候，就要把 Store 的数据都准备好，所以服务器端异步数据结合 Redux 的使用方式，流程是下面的样子（对应图中第 4 步）：</p>
<ol>
<li>创建 Store</li>
<li>根据路由分析 Store 中需要的数据</li>
<li>派发 Action 获取数据</li>
<li>更新Store 中的数据</li>
<li>结合数据和组件生成 HTML，一次性返回</li>
</ol>
<p>下面，我们分析下服务器端渲染这部分的流程：</p>
<p>客户端渲染中，用户的浏览器中永远只存在一个 Store，所以代码上你可以这么写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 客户端写法</span>
<span class="hljs-keyword">const</span> store = createStore(reducer, defaultState)<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store;

<span class="hljs-comment">// Store 变成了一个单例，所有用户共享 Store</span>
<span class="hljs-comment">// 返回一个函数，每个用户访问的时候，这个函数重新执行，为每个用户提供一个独立的 Store</span>
<span class="hljs-keyword">const</span> getStore = <span class="hljs-function">(<span class="hljs-params">req</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> createStore(reducer, defaultState);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> getStore;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-23">八、SEO技巧的融入</h1>
<h3 data-id="heading-24">1. Title 和 Description的真正作用</h3>
<pre><code class="copyable">- 二代搜索引擎是基于网站全文的
- title 和 description 对搜索的影响比较小
- title 中出现吸引用户的关键字，吸引用户点击，提升转化率，而不是提升排名
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">2. 如何做好 SEO</h3>
<ul>
<li>网站的组成部分：多媒体、链接、文字</li>
<li>搜索引擎判断网站价值的时候，是从这三方面判断的。
<ul>
<li>文字优化 -- 原创</li>
<li>链接
<ul>
<li>内部链接：链接到的内容要与原网站的尽量的相关。</li>
<li>外部链接：越多说明这个网站的影响力比较大</li>
</ul>
</li>
<li>多媒体 -- 可以做图片识别、原创、高清</li>
</ul>
</li>
</ul>
<h3 data-id="heading-26">3. React-Helmet 的使用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    render () &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"application"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Helmet</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charSet</span>=<span class="hljs-string">"utf-8"</span> /></span>
                    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>My Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"canonical"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://mysite.com/example"</span> /></span>
                <span class="hljs-tag"></<span class="hljs-name">Helmet</span>></span>
                ...
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        );
    &#125;
&#125;;

<span class="hljs-comment">// 服务端</span>
<span class="hljs-keyword">const</span> helmet = Helmet.renderStatic()
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-27">九、使用预渲染解决SEO问题的新思路</h1>
<blockquote>
<p>不想使用 SSR 但是想提高搜索引擎排名 -- 预渲染</p>
</blockquote>
<ul>
<li>中间层访问网页，将网页内容拿过来渲染成完整的 html，将完整的 html返回给客户端</li>
</ul>
<p>具体详情请看 ---> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fprerender.io%2Fframework%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://prerender.io/framework/" ref="nofollow noopener noreferrer">prerender.io/framework/</a></p>
<p>使用 prerender，启动一个8000的端口号，去访问客户端渲染的网址
localhost:8000/render?url=<a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A3000" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:3000" ref="nofollow noopener noreferrer">http://localhost:3000</a></p>
<p>区分到是蜘蛛访问时，使用 preRender 服务器。</p>
<p>nginx 可以根据 userAgent 来区分</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8b03794938d432c9294ed2240211f3f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-28">十、总结</h1>
<p>使用 SSR 这种技术，将使原本简单的 React 项目变得非常复杂，项目的可维护性会降低，代码问题的追溯也会变得困难。</p>
<p>所以，使用 SSR 在解决问题的同时，也会带来非常多的副作用，有的时候，这些副作用的伤害比起 SSR 技术带来的优势要大的多。一般建议大家，除非你的项目特别依赖搜索引擎流量，或者对首屏时间有特殊的要求，否则不建议使用 SSR。</p>
<h1 data-id="heading-29">参考资料：</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FBXC6tZyY6fsi8l8dJ40nug" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/BXC6tZyY6fsi8l8dJ40nug" ref="nofollow noopener noreferrer">【第1443期】React 中同构（SSR）原理脉络梳理</a></li>
<li><a href="https://juejin.cn/post/6844903943902855176#heading-11" target="_blank" title="https://juejin.cn/post/6844903943902855176#heading-11">【长文慎入】一文吃透 React SSR 服务端渲染和同构原理</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoding.imooc.com%2Fclass%2F276.html" target="_blank" rel="nofollow noopener noreferrer" title="https://coding.imooc.com/class/276.html" ref="nofollow noopener noreferrer">React服务器渲染原理解析与实践</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freactrouter.com%2Fweb%2Fguides%2Fquick-start%2F2nd-example-nested-routing" target="_blank" rel="nofollow noopener noreferrer" title="https://reactrouter.com/web/guides/quick-start/2nd-example-nested-routing" ref="nofollow noopener noreferrer">reactrouter.com</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fprerender.io%2Fframework%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://prerender.io/framework/" ref="nofollow noopener noreferrer">prerender.io/framework/</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freactrouter.com%2Fweb%2Fguides%2Fserver-rendering" target="_blank" rel="nofollow noopener noreferrer" title="https://reactrouter.com/web/guides/server-rendering" ref="nofollow noopener noreferrer">reactrouter.com/web/guides/…</a></li>
</ul></div>  
</div>
            