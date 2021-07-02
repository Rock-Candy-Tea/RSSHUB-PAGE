
---
title: '「Webpack」从0到1学会 code splitting'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 17:50:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image" alt="掘金引流终版.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://juejin.cn/post/6963056815420473357#heading-0" target="_blank">构建专栏系列目录入口</a></p>
</blockquote>
<blockquote>
<p>焦传锴，微医前端技术部平台支撑组。不是吧阿 sir，又要兼容 IE？</p>
</blockquote>
<h2 data-id="heading-0">一、前言</h2>
<p>在默认的配置情况下，我们知道，webpack 会把所有代码打包到一个 chunk 中，举个例子当你的一个单页面应用很大的时候，你可能就需要将每个路由拆分到一个 chunk 中，这样才方便我们实现按需加载。</p>
<p>代码分离是 webpack 中最引人注目的特性之一。此特性能够把代码分离到不同的 bundle 中，然后可以按需加载或并行加载这些文件。代码分离可以用于获取更小的 bundle，以及控制资源加载优先级，如果使用合理，会极大影响加载时间。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8185b7ee74c04a55bd1ca42868c97e36~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">二、关于代码分割</h2>
<p>接下来我们会分别分析不同的代码分隔方式带来的打包差异，首先我们的项目假设有这两个简单的文件👇</p>
<p><strong>index.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; mul &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./test'</span>
<span class="hljs-keyword">import</span> $ <span class="hljs-keyword">from</span> <span class="hljs-string">'jquery'</span>

<span class="hljs-built_in">console</span>.log($)
<span class="hljs-built_in">console</span>.log(mul(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>))

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>test.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> $ <span class="hljs-keyword">from</span> <span class="hljs-string">'jquery'</span>

<span class="hljs-built_in">console</span>.log($)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mul</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a * b
&#125;

<span class="hljs-keyword">export</span> &#123; mul &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到现在他们二者都依赖于 jquery 这个库，并且相互之间也会有依赖。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbe4ac3853d84cd28e52d975d3440bc7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当我们在默认配置的情况下进行打包，结果是这样的👇，会把所有内容打包进一个 main bundle 内（<strong>324kb</strong>）
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf407f65d92e42d88c5c7aa38d94dfde~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55eb0b703bff48808a96fa2fd169f219~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
那么我们如何用最直接的方式从这个 bundle 中分离出其他模块呢？</p>
<h3 data-id="heading-2">1. 多入口</h3>
<p>webpack 配置中的 <code>entry</code> ，可以设置为多个，也就是说我们可以分别将 index 和 test 文件分别作为入口：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// entry: './src/index.js', 原来的单入口</span>
<span class="hljs-comment">/** 现在分别将它们作为入口 */</span>
<span class="hljs-attr">entry</span>:&#123;
  <span class="hljs-attr">index</span>:<span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">test</span>:<span class="hljs-string">'./src/test.js'</span>
&#125;,
<span class="hljs-attr">output</span>: &#123;
  <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[hash:8].js'</span>,
  <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./dist'</span>),
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样让我们看一下这样打包后的结果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d8bfbd2c5da4c9980647a7437ed051b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
确实打包出了两个文件！但是为什么两个文件都有 <strong>320+kb</strong> 呢？不是说好拆分获取更小的 bundle ？这是因为由于二者都引入了 jquery 而 webpack 从两次入口进行打包分析的时候会每次都将依赖的模块分别打包进去👇
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c53980998f2a419285a78a0cc8263e71~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没错，这种配置的方式确实会带来一些<strong>隐患</strong>以及不便：</p>
<ul>
<li>如果入口 chunk 之间包含一些重复的模块，那些重复模块都会被引入到各个 bundle 中。</li>
<li>这种方法不够灵活，并且不能动态地将核心应用程序逻辑中的代码拆分出来。</li>
</ul>
<p>那么有没有方式可以既可以将共同依赖的模块进行打包分离，又不用进行繁琐的手动配置入口的方式呢？那必然是有的。</p>
<h3 data-id="heading-3">2. SplitChunksPlugin</h3>
<p><code>SplitChunks</code> 是 webpack4 开始<strong>自带的开箱即用的</strong>一个插件，他可以将满足规则的 chunk 进行分离，也可以自定义配置。在 webpack4 中用它取代了之前用来解决重复依赖的 <code>CommonsChunkPlugin</code> 。</p>
<p>让我们在我们的 webpack 配置中加上一些配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">entry: <span class="hljs-string">'./src/index.js'</span>, <span class="hljs-comment">// 这里我们改回单入口</span>
<span class="hljs-comment">/** 加上如下设置 */</span>
<span class="hljs-attr">optimization</span>: &#123;
  <span class="hljs-attr">splitChunks</span>: &#123;
    <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
  &#125;,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包后的结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/073a351fbc63420da9cb76541f7ef41e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到很明显除了根据入口打包出的 main bundle 之外，还多出了一个名为 <code>vendors-node_modules_jquery_dist_jquery_js.xxxxx.js</code> ，显然这样我们将公用的 jquery 模块就提取出来了。</p>
<p>接下来我们来探究一下 <code>SplitChunksPlugin</code> 。
首先看下配置的默认值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">splitChunks: &#123;
    <span class="hljs-comment">// 表示选择哪些 chunks 进行分割，可选值有：async，initial 和 all</span>
    <span class="hljs-attr">chunks</span>: <span class="hljs-string">"async"</span>,
    <span class="hljs-comment">// 表示新分离出的 chunk 必须大于等于 minSize，20000，约 20kb。</span>
    <span class="hljs-attr">minSize</span>: <span class="hljs-number">20000</span>,
    <span class="hljs-comment">// 通过确保拆分后剩余的最小 chunk 体积超过限制来避免大小为零的模块,仅在剩余单个 chunk 时生效</span>
    <span class="hljs-attr">minRemainingSize</span>: <span class="hljs-number">0</span>,
    <span class="hljs-comment">// 表示一个模块至少应被 minChunks 个 chunk 所包含才能分割。默认为 1。</span>
    <span class="hljs-attr">minChunks</span>: <span class="hljs-number">1</span>,
    <span class="hljs-comment">// 表示按需加载文件时，并行请求的最大数目。</span>
    <span class="hljs-attr">maxAsyncRequests</span>: <span class="hljs-number">30</span>,
    <span class="hljs-comment">// 表示加载入口文件时，并行请求的最大数目。</span>
    <span class="hljs-attr">maxInitialRequests</span>: <span class="hljs-number">30</span>,
    <span class="hljs-comment">// 强制执行拆分的体积阈值和其他限制（minRemainingSize，maxAsyncRequests，maxInitialRequests）将被忽略</span>
    <span class="hljs-attr">enforceSizeThreshold</span>: <span class="hljs-number">50000</span>,
    <span class="hljs-comment">// cacheGroups 下可以可以配置多个组，每个组根据 test 设置条件，符合 test 条件的模块，就分配到该组。模块可以被多个组引用，但最终会根据 priority 来决定打包到哪个组中。默认将所有来自 node_modules 目录的模块打包至 vendors 组，将两个以上的 chunk 所共享的模块打包至 default 组。</span>
    <span class="hljs-attr">cacheGroups</span>: &#123;
        <span class="hljs-attr">defaultVendors</span>: &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>,
            <span class="hljs-comment">// 一个模块可以属于多个缓存组。优化将优先考虑具有更高 priority（优先级）的缓存组。</span>
            priority: -<span class="hljs-number">10</span>,
            <span class="hljs-comment">// 如果当前 chunk 包含已从主 bundle 中拆分出的模块，则它将被重用</span>
            <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>,
        &#125;,
     <span class="hljs-attr">default</span>: &#123;
            <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>,
            <span class="hljs-attr">priority</span>: -<span class="hljs-number">20</span>,
            <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，SplitChunks 只会对异步调用的模块进行分割（<code>chunks: "async"</code>），并且默认情况下处理的 chunk 至少要有 20kb ，过小的模块不会被包含进去。</p>
<blockquote>
<p>补充一下，默认值会根据 mode 的配置不同有所变化，具体参见<a href="https://github.com/webpack/webpack/blob/HEAD/lib/config/defaults.js" target="_blank" rel="nofollow noopener noreferrer">源码</a>👇：</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; splitChunks &#125; = optimization;
<span class="hljs-keyword">if</span> (splitChunks) &#123;
  A(splitChunks, <span class="hljs-string">"defaultSizeTypes"</span>, <span class="hljs-function">() =></span> [<span class="hljs-string">"javascript"</span>, <span class="hljs-string">"unknown"</span>]);
  D(splitChunks, <span class="hljs-string">"hidePathInfo"</span>, production);
  D(splitChunks, <span class="hljs-string">"chunks"</span>, <span class="hljs-string">"async"</span>);
  D(splitChunks, <span class="hljs-string">"usedExports"</span>, optimization.usedExports === <span class="hljs-literal">true</span>);
  D(splitChunks, <span class="hljs-string">"minChunks"</span>, <span class="hljs-number">1</span>);
  F(splitChunks, <span class="hljs-string">"minSize"</span>, <span class="hljs-function">() =></span> (production ? <span class="hljs-number">20000</span> : <span class="hljs-number">10000</span>));
  F(splitChunks, <span class="hljs-string">"minRemainingSize"</span>, <span class="hljs-function">() =></span> (development ? <span class="hljs-number">0</span> : <span class="hljs-literal">undefined</span>));
  F(splitChunks, <span class="hljs-string">"enforceSizeThreshold"</span>, <span class="hljs-function">() =></span> (production ? <span class="hljs-number">50000</span> : <span class="hljs-number">30000</span>));
  F(splitChunks, <span class="hljs-string">"maxAsyncRequests"</span>, <span class="hljs-function">() =></span> (production ? <span class="hljs-number">30</span> : <span class="hljs-literal">Infinity</span>));
  F(splitChunks, <span class="hljs-string">"maxInitialRequests"</span>, <span class="hljs-function">() =></span> (production ? <span class="hljs-number">30</span> : <span class="hljs-literal">Infinity</span>));
  D(splitChunks, <span class="hljs-string">"automaticNameDelimiter"</span>, <span class="hljs-string">"-"</span>);
  <span class="hljs-keyword">const</span> &#123; cacheGroups &#125; = splitChunks;
  F(cacheGroups, <span class="hljs-string">"default"</span>, <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">idHint</span>: <span class="hljs-string">""</span>,
    <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">priority</span>: -<span class="hljs-number">20</span>
  &#125;));
  F(cacheGroups, <span class="hljs-string">"defaultVendors"</span>, <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">idHint</span>: <span class="hljs-string">"vendors"</span>,
    <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">test</span>: NODE_MODULES_REGEXP,
    <span class="hljs-attr">priority</span>: -<span class="hljs-number">10</span>
  &#125;));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>cacheGroups</code> <strong>缓存组</strong>是施行分割的重中之重，他可以使用来自 <code>splitChunks.*</code> 的<strong>任何选项</strong>，但是 <strong>test、priority 和 reuseExistingChunk</strong> 只能在缓存组级别上进行配置。默认配置中已经给我们提供了 Vendors 组和一个 defalut 组，**Vendors **组中使用 <code>test: /[\\/]node_modules[\\/]/</code> 匹配了 node_modules 中的所有符合规则的模块。</p>
<blockquote>
<p>Tip：当 webpack 处理文件路径时，它们始终包含 Unix 系统中的 / 和 Windows 系统中的 \。这就是为什么在 &#123;cacheGroup&#125;.test 字段中使用 [\/] 来表示路径分隔符的原因。&#123;cacheGroup&#125;.test 中的 / 或 \ 会在跨平台使用时产生问题。</p>
</blockquote>
<p>综上的配置，我们便可以理解为什么我们在打包中会产生出名为 <code>vendors-node_modules_jquery_dist_jquery_js.db47cc72.js</code> 的文件了。如果你想要<strong>对名称进行自定义</strong>的话，也可以使用 <code>splitChunks.name</code> 属性（每个 cacheGroup 中都可以使用），这个属性支持使用三种形式：</p>
<ol>
<li><code>boolean = false</code> 设为 false 将保持 chunk 的相同名称，因此不会不必要地更改名称。这是生产环境下构建的建议值。</li>
<li><code>function (module, chunks, cacheGroupKey) => string</code> 返回值要求是 string 类型，并且在 <code>chunks</code> 数组中每一个 <code>chunk</code> 都有 <code>chunk.name</code> 和 <code>chunk.hash</code> 属性，举个例子 👇</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">name</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, chunks, cacheGroupKey</span>)</span> &#123;
  <span class="hljs-keyword">const</span> moduleFileName = <span class="hljs-built_in">module</span>
  .identifier()
  .split(<span class="hljs-string">'/'</span>)
  .reduceRight(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item);
  <span class="hljs-keyword">const</span> allChunksNames = chunks.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.name).join(<span class="hljs-string">'~'</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;cacheGroupKey&#125;</span>-<span class="hljs-subst">$&#123;allChunksNames&#125;</span>-<span class="hljs-subst">$&#123;moduleFileName&#125;</span>`</span>;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>string</code> 指定字符串或始终返回相同字符串的函数会将所有常见模块和 vendor 合并为一个 chunk。这可能<strong>会导致更大的初始下载量并减慢页面加载速度</strong>。</li>
</ol>
<p>另外注意一下 <code>splitChunks.maxAsyncRequests</code> 和 <code>splitChunks.maxInitialRequests</code> 分别指的是<strong>按需加载时最大的并行请求数</strong>和<strong>页面初始渲染时候需要的最大并行请求数</strong></p>
<p>在我们的项目较大时，如果需要对某个依赖单独拆包的话，可以进行这样的配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cacheGroups: &#123;
  <span class="hljs-attr">react</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'react'</span>,
      <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/](react)/</span>,
      chunks: <span class="hljs-string">'all'</span>,
      <span class="hljs-attr">priority</span>: -<span class="hljs-number">5</span>,
  &#125;,
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样打包后就可以拆分指定的包：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1544c81b36334616a25034643fe6c10f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>更多配置详见<a href="https://webpack.js.org/plugins/split-chunks-plugin" target="_blank" rel="nofollow noopener noreferrer">官网配置文档</a></p>
<h3 data-id="heading-4">3. 动态 import</h3>
<p>使用 <a href="https://webpack.docschina.org/api/module-methods/#import" target="_blank" rel="nofollow noopener noreferrer">import()语法</a> 来实现动态导入也是我们非常推荐的一种代码分割的方式，我们先来简单修改一下我们的 <code>index.js</code> ，再来看一下使用后打包的效果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// import &#123; mul &#125; from './test'</span>
<span class="hljs-keyword">import</span> $ <span class="hljs-keyword">from</span> <span class="hljs-string">'jquery'</span>

<span class="hljs-keyword">import</span>(<span class="hljs-string">'./test'</span>).then(<span class="hljs-function">(<span class="hljs-params">&#123; mul &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(mul(<span class="hljs-number">2</span>,<span class="hljs-number">3</span>))
&#125;)

<span class="hljs-built_in">console</span>.log($)
<span class="hljs-comment">// console.log(mul(2, 3))</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，通过 <code>import()</code> 语法导入的模块在打包时会自动单独进行打包
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0205b531fbcb4408b9c9d125841255a5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>值得注意的是，这种语法还有一种很方便的“动态引用”的方式，他可以加入一些适当的表达式，举个例子，假设我们需要加载适当的主题：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> themeType = getUserTheme();
<span class="hljs-keyword">import</span>(<span class="hljs-string">`./themes/<span class="hljs-subst">$&#123;themeType&#125;</span>`</span>).then(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-built_in">module</span></span>) =></span> &#123;
  <span class="hljs-comment">// do sth aboout theme</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就可以“动态”加载我们需要的异步模块，实现的原理主要在于两点：</p>
<ol>
<li>至少需要<strong>包含模块相关的路径信息</strong>，打包可以限定于一个特定的目录或文件集。</li>
<li>根据路径信息 webpack 在打包时会把 <code>./themes</code>  中的<strong>所有</strong>文件打包进新的 chunk 中，以便需要时使用到。</li>
</ol>
<h3 data-id="heading-5">4. 魔术注释</h3>
<p>在上述的 <code>import()</code> 语法中，我们会发现打包自动生成的文件名并不是我们想要的，我们如何才能自己控制打包的名称呢？这里就要引入我们的魔术注释（Magic Comments）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "my-chunk-name" */</span><span class="hljs-string">'./test'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这样打包出来的文件：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7527340850846efb6261c3737063b4c~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>魔术注释不仅仅可以帮我们修改 chunk 名这么简单，他还可以实现譬如预加载等功能，这里举个例子：</p>
<p>我们通过希望在点击按钮时才加载我们需要的模块功能，代码可以这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// index.js</span>
<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">import</span>(<span class="hljs-string">'./test'</span>).then(<span class="hljs-function">(<span class="hljs-params">&#123; mul &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(mul(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>));
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//test.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mul</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a * b;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'test 被加载了'</span>);
<span class="hljs-keyword">export</span> &#123; mul &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f5c528021243b6810ba33106177974~tplv-k3u1fbpfcp-zoom-1.image" alt="03-03.gif" loading="lazy" referrerpolicy="no-referrer">
可以看到，在我们点击按钮的同时确实加载了 <code>test.js</code> 的文件资源。但是如果这个模块是一个很大的模块，在点击时进行加载可能会造成长时间 loading 等用户体验不是很好的效果，这个时候我们可以使用我们的 <code>/* webpackPrefetch: true */</code> 方式进行<strong>预获取</strong>，来看下效果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// index,js</span>

<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackPrefetch: true */</span><span class="hljs-string">'./test'</span>).then(<span class="hljs-function">(<span class="hljs-params">&#123; mul &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(mul(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>));
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0bc375826d847fe9a90d6bae23888c2~tplv-k3u1fbpfcp-zoom-1.image" alt="03-04.gif" loading="lazy" referrerpolicy="no-referrer">
可以看到整个过程中，在画面初始加载的时候，<code>test.js</code> 的资源就已经被预先加载了，而在我们点击按钮时，会从 <code>(prefetch cache)</code> 中读取内容。这就是模块预获取的过程。另外我们还有 <code>/* webpackPreload: true */</code> 的方式进行预加载。</p>
<p>但是 prefetch 和 preload 听起来感觉差不多，实际上他们的加载时机等是完全不同的：</p>
<ul>
<li>preload chunk 会在父 chunk 加载时，以并行方式开始加载。prefetch chunk 会在父 chunk 加载结束后开始加载。</li>
<li>preload chunk 具有中等优先级，并立即下载。prefetch chunk 在浏览器闲置时下载。</li>
<li>preload chunk 会在父 chunk 中立即请求，用于当下时刻。prefetch chunk 会用于未来的某个时刻。</li>
</ul>
<h2 data-id="heading-6">三、结尾</h2>
<p>在最初有工程化打包思想时，我们会考虑将多文件打包到一个文件内减少多次的资源请求，随着项目的越来越复杂，做项目优化时，我们发现项目加载越久用户体验就越不好，于是又可以通过代码分割的方式去减少页面初加载时的请求过大的资源体积。</p>
<p>本文中仅简单介绍了常用的 webpack 代码分割方式，但是在实际的项目中进行性能优化时，往往会有更加严苛的要求，希望可以通过本文的介绍让大家快速了解上手代码分割的技巧与优势。</p>
<h2 data-id="heading-7">参考</h2>
<p><a href="https://juejin.cn/post/6844904103848443912" target="_blank">如何使用 splitChunks 精细控制代码分割</a></p>
<p><a href="https://webpack.js.org/guides/code-splitting/" target="_blank" rel="nofollow noopener noreferrer">Code Splitting - Webpack</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/180fd06458bc4a8482fb4efbb9dd2875~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            